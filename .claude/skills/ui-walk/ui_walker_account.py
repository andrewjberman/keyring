#!/usr/bin/env python3
"""The Opal UI walker service account: one standing identity, DORMANT between walks.

Andrew-direct 2026-09-26 (4.0.0_SA_CRO terminal): "we need a service account setup that can walk these pages
visually, I need you to just build it". Record:
org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260926_220xZ_UI_WALKER_SERVICE_ACCOUNT.md

    python ui_walker_account.py status     # is the row present, active or disabled, and armed for how long
    python ui_walker_account.py provision  # create the row ONCE, disabled, with no usable password
    python ui_walker_account.py arm        # lease (armedBy/armedAt) then password -> SSM; prints HOLDER <id>; HELD if a live lease
    python ui_walker_account.py disarm <holder>  # holder only: row status disabled + unusable hash; SSM deleted; login refused

THE SAFETY MODEL:
- The row is `role admin`, `firmId opal-capital`, `userType Dev`, because /investor-reporting admits only that
  combination (portal ProtectedRoute requireAdmin + requireInternal + requireDev). That is a superadmin reach for as
  long as a session lives, so the account is DISABLED at rest and holds NO usable password at rest.
- `arm` mints a new random password for one walk and stores it ONLY in SSM. `disarm` sets the status to disabled
  (auth-handler refuses login AND refresh on status != active), replaces the hash with one nobody knows, deletes the
  SSM parameter, and proves a login with the old password is refused. The last access token dies <= 15 min later.
- Nothing prints a password. The walker reads it in-process (`secret`, guarded by an env var and a non-TTY stdout).
"""
from __future__ import annotations

import datetime as dt
import json
import os
import secrets
import socket
import sys
import urllib.error
import urllib.request

import bcrypt
import boto3
from botocore.exceptions import ClientError

TABLE = "opal-users-v2"
PK = "USER#usr_opal_ui_walker"
SK = "PROFILE"
EMAIL = "opal-ui-walker@opal.test"  # the .test TLD never receives mail
PARAM = "/opal/ui-walker/password"
AUTH_API = "https://opalinvest.dev"  # through CloudFront; the execute-api URL 403s at the origin guard
SALT_ROUNDS = 12  # auth-handler password.ts
MAX_ARMED_MINUTES = 60


def _now():
    return dt.datetime.now(dt.timezone.utc)


def _iso(t):
    return t.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def _ddb():
    return boto3.client("dynamodb")


def _ssm():
    return boto3.client("ssm")


def _unusable_hash():
    throwaway = secrets.token_urlsafe(48)
    return bcrypt.hashpw(throwaway.encode("ascii"), bcrypt.gensalt(SALT_ROUNDS)).decode("ascii")


def get_row():
    r = _ddb().get_item(TableName=TABLE, Key={"PK": {"S": PK}, "SK": {"S": SK}}, ConsistentRead=True)
    return r.get("Item")


def _param_present():
    try:
        _ssm().get_parameter(Name=PARAM)
        return True
    except ClientError as e:
        if e.response["Error"]["Code"] == "ParameterNotFound":
            return False
        raise


def status(quiet=False):
    row = get_row()
    if not row:
        line = "STATUS: row ABSENT (run provision); SSM %s" % ("PRESENT" if _param_present() else "ABSENT")
        out = {"row": False}
    else:
        st = (row.get("status") or {}).get("S")
        armed_at = (row.get("armedAt") or {}).get("S")
        armed_by = (row.get("armedBy") or {}).get("S")
        age = None
        if armed_at:
            age = (_now() - dt.datetime.strptime(armed_at, "%Y-%m-%dT%H:%M:%S.%fZ").replace(
                tzinfo=dt.timezone.utc)).total_seconds() / 60.0
        line = "STATUS: row PRESENT %s status=%s role=%s userType=%s armed=%s%s armedBy=%s; SSM %s" % (
            EMAIL, st, (row.get("role") or {}).get("S"), (row.get("userType") or {}).get("S"),
            "yes" if armed_at else "no", "" if age is None else " (%.1f min ago)" % age, armed_by or "none",
            "PRESENT" if _param_present() else "ABSENT")
        out = {"row": True, "status": st, "armed_minutes": age}
        if st == "active" and age is not None and age > MAX_ARMED_MINUTES:
            line += "\nWARN: armed longer than %d min -- run disarm NOW" % MAX_ARMED_MINUTES
    if not quiet:
        print(line)
    return out


def provision():
    if get_row():
        print("OK: row already present -- nothing written")
        return status()
    item = {"PK": {"S": PK}, "SK": {"S": SK}, "email": {"S": EMAIL}, "passwordHash": {"S": _unusable_hash()},
            "name": {"S": "Opal UI walker (service account, Andrew-direct 20260926)"}, "role": {"S": "admin"},
            "firmId": {"S": "opal-capital"}, "userType": {"S": "Dev"}, "status": {"S": "disabled"},
            "createdAt": {"S": _iso(_now())}, "createdBy": {"S": "4.0.0_SA_CRO ui-walker (Andrew-direct 20260926)"}}
    _ddb().put_item(TableName=TABLE, Item=item, ConditionExpression="attribute_not_exists(PK)")
    print("OK: provisioned %s (status disabled, no usable password)" % EMAIL)
    return status()


def _holder_id():
    return "%s:%d:%s" % (socket.gethostname(), os.getpid(), secrets.token_hex(4))


def arm():
    """Lease first (one conditional UpdateItem), then mint. A live lease is never stolen."""
    row = get_row()
    if not row:
        raise SystemExit("STOP: row absent -- run provision first")
    holder = _holder_id()
    now = _now()
    cutoff = _iso(now - dt.timedelta(minutes=MAX_ARMED_MINUTES))
    try:
        _ddb().update_item(
            TableName=TABLE, Key={"PK": {"S": PK}, "SK": {"S": SK}},
            UpdateExpression="SET armedBy = :b, armedAt = :t",
            ConditionExpression="attribute_not_exists(armedAt) OR armedAt < :c",
            ExpressionAttributeValues={":b": {"S": holder}, ":t": {"S": _iso(now)}, ":c": {"S": cutoff}})
    except ClientError as e:
        if e.response["Error"]["Code"] != "ConditionalCheckFailedException":
            raise
        cur = get_row() or {}
        raise SystemExit("HELD by %s since %s" % ((cur.get("armedBy") or {}).get("S", "<unknown legacy holder>"),
                                                  (cur.get("armedAt") or {}).get("S", "<unknown>")))
    password = secrets.token_urlsafe(32)
    pw_hash = bcrypt.hashpw(password.encode("ascii"), bcrypt.gensalt(SALT_ROUNDS)).decode("ascii")
    _ssm().put_parameter(Name=PARAM, Value=password, Type="SecureString", Overwrite=True,
                         Description="Opal UI walker password for ONE walk; deleted at disarm")
    del password
    _ddb().update_item(TableName=TABLE, Key={"PK": {"S": PK}, "SK": {"S": SK}},
                       UpdateExpression="SET passwordHash = :h, #s = :a",
                       ConditionExpression="armedBy = :b",
                       ExpressionAttributeNames={"#s": "status"},
                       ExpressionAttributeValues={":h": {"S": pw_hash}, ":a": {"S": "active"}, ":b": {"S": holder}})
    print("OK: ARMED %s; password by NAME %s (value never printed); disarm within %d min"
          % (EMAIL, PARAM, MAX_ARMED_MINUTES))
    print("HOLDER %s" % holder)
    return holder


def _login(password):
    body = json.dumps({"email": EMAIL, "password": password}).encode("ascii")
    req = urllib.request.Request(AUTH_API + "/auth/login", data=body, method="POST",
                                 headers={"Content-Type": "application/json", "Origin": AUTH_API,
                                          "User-Agent": "Mozilla/5.0 opal-ui-walker/1"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return False, "HTTP %d (a session was issued -- NOT refused)" % r.status
    except urllib.error.HTTPError as e:
        text = e.read().decode("utf-8", "replace").replace(password, "<redacted>")
        return e.code in (401, 403), "HTTP %d %s" % (e.code, text[:100])


def disarm(holder):
    """Runs only for the holder that armed: the UpdateItem is conditional on armedBy = holder."""
    password = None
    try:
        password = _ssm().get_parameter(Name=PARAM, WithDecryption=True)["Parameter"]["Value"]
    except ClientError as e:
        if e.response["Error"]["Code"] != "ParameterNotFound":
            raise
    if get_row():
        try:
            _ddb().update_item(TableName=TABLE, Key={"PK": {"S": PK}, "SK": {"S": SK}},
                               UpdateExpression="SET passwordHash = :h, #s = :d REMOVE armedBy, armedAt",
                               ConditionExpression="armedBy = :b",
                               ExpressionAttributeNames={"#s": "status"},
                               ExpressionAttributeValues={":h": {"S": _unusable_hash()}, ":d": {"S": "disabled"},
                                                          ":b": {"S": holder}})
        except ClientError as e:
            if e.response["Error"]["Code"] != "ConditionalCheckFailedException":
                raise
            cur = get_row() or {}
            raise SystemExit("REFUSED: %s is not the holder (held by %s) -- nothing changed"
                             % (holder, (cur.get("armedBy") or {}).get("S", "nobody")))
    # No ssm:DeleteParameter: the Dells hold GetParameter only (NFRA_CTLPLN step H), and DeleteParameter is unrecoverable.
    # The disarm ends at row disabled + password refused; the stored password is dead once the row's hash is unusable.
    row = get_row()
    st = (row.get("status") or {}).get("S") if row else "ABSENT"
    print("DISARM: row status=%s; SSM %s" % (st, "PRESENT" if _param_present() else "ABSENT (ParameterNotFound)"))
    if password is not None:
        refused, line = _login(password)
        password = None
        print("LOGIN WITH THE WALK PASSWORD AFTER DISARM: %s -> %s" % (line, "REFUSED" if refused else "NOT REFUSED"))
        if not refused:
            raise SystemExit("ESCALATE: login not refused after disarm")
    if st != "disabled" and row:
        raise SystemExit("ESCALATE: row not disabled")
    print("OK: DISARMED at %s" % _iso(_now()))


def secret():
    """For the walker process ONLY: it spawns this with UI_WALK_CHILD=1 and reads stdout in memory."""
    if os.environ.get("UI_WALK_CHILD") != "1" or sys.stdout.isatty():
        raise SystemExit("REFUSED: secret is for the walker process only (never run by hand)")
    sys.stdout.write(_ssm().get_parameter(Name=PARAM, WithDecryption=True)["Parameter"]["Value"])


if __name__ == "__main__":
    cmds = {"status": status, "provision": provision, "arm": arm, "disarm": disarm, "secret": secret}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds or len(sys.argv) != (3 if sys.argv[1] == "disarm" else 2):
        raise SystemExit("usage: ui_walker_account.py status|provision|arm|disarm <holder>")
    cmds[sys.argv[1]](*sys.argv[2:])
