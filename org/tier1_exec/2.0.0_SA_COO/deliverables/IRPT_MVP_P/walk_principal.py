#!/usr/bin/env python3
"""The bounded Opal-class walk principal -- create and delete, exactly as packet
NEVER_WIDEN_SIGNOFF_PACKET_WALK_PRINCIPAL_20260926.md names it (K1 + K1-CRED; K2 is the walker's login).

    python walk_principal.py preread <epoch>
    python walk_principal.py create  <epoch>
    python walk_principal.py delete  <epoch>

The password is generated here, written ONLY to the SecureString, and never printed, logged or returned. Every
line printed is ASCII and carries no credential. A digest of K1 excludes passwordHash.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import secrets
import sys
import urllib.error
import urllib.request

import bcrypt
import boto3
from botocore.exceptions import ClientError

TABLE = "opal-users-v2"
AUTH_API = "https://7k3ed8px20.execute-api.us-east-1.amazonaws.com"  # portal AuthContext.tsx:76 default
SALT_ROUNDS = 12  # auth-handler password.ts:4


def names(epoch):
    return {"pk": "USER#usr_irptwalk_%s" % epoch, "email": "irpt-walk-%s@opal.test" % epoch,
            "param": "/irpt/walk-principal/%s/password" % epoch}


def _ddb():
    return boto3.client("dynamodb")


def _ssm():
    return boto3.client("ssm")


def k1_item(n, pw_hash, now):
    return {"PK": {"S": n["pk"]}, "SK": {"S": "PROFILE"}, "email": {"S": n["email"]},
            "passwordHash": {"S": pw_hash}, "name": {"S": "IRPT walk principal (Andrew-direct 20260926)"},
            "role": {"S": "user"}, "firmId": {"S": "opal-capital"}, "status": {"S": "active"},
            "createdAt": {"S": now}, "createdBy": {"S": "2.0.0_SA_COO~P walk-principal-20260926"}}


def digest(item):
    shown = {k: v for k, v in item.items() if k != "passwordHash"}
    return hashlib.sha256(json.dumps(shown, sort_keys=True).encode("ascii")).hexdigest()


def get_k1(n):
    r = _ddb().get_item(TableName=TABLE, Key={"PK": {"S": n["pk"]}, "SK": {"S": "PROFILE"}}, ConsistentRead=True)
    return r.get("Item")


def index_count(n):
    r = _ddb().query(TableName=TABLE, IndexName="email-index", KeyConditionExpression="email = :e",
                     ExpressionAttributeValues={":e": {"S": n["email"]}}, Select="COUNT")
    return r["Count"]


def param_exists(n):
    try:
        _ssm().describe_parameters(ParameterFilters=[{"Key": "Name", "Values": [n["param"]]}])["Parameters"][0]
        return True
    except IndexError:
        return False


def preread(n):
    k1 = get_k1(n)
    print("PREREAD: K1 base-table item %s; email-index count %d; K1-CRED %s"
          % ("PRESENT" if k1 else "ABSENT", index_count(n), "PRESENT" if param_exists(n) else "ABSENT"))
    return k1 is None and index_count(n) == 0 and not param_exists(n)


def create(n):
    if not preread(n):
        raise SystemExit("STOP: pre-read not clean")
    password = secrets.token_urlsafe(32)
    pw_hash = bcrypt.hashpw(password.encode("ascii"), bcrypt.gensalt(SALT_ROUNDS)).decode("ascii")
    _ssm().put_parameter(Name=n["param"], Value=password, Type="SecureString", Overwrite=False,
                         Description="IRPT walk principal password; deleted with K1")
    del password
    print("OK: K1-CRED put (value not printed) %s" % n["param"])
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    item = k1_item(n, pw_hash, now)
    _ddb().put_item(TableName=TABLE, Item=item, ConditionExpression="attribute_not_exists(PK)")
    back = get_k1(n)
    same = back is not None and digest(back) == digest(item) and back["passwordHash"] == item["passwordHash"]
    print("OK: K1 put %s at %s; read-back digest %s (passwordHash excluded) %s"
          % (n["pk"], now, digest(back or {}), "EQUAL" if same else "DIFFERENT"))
    if not same:
        raise SystemExit("STOP: K1 read-back differs -- run delete now")
    print("HANDOVER: email %s ; password by NAME %s" % (n["email"], n["param"]))


def _login_refused(email, password):
    body = json.dumps({"email": email, "password": password}).encode("ascii")
    req = urllib.request.Request(AUTH_API + "/auth/login", data=body, method="POST",
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return False, "HTTP %d (a session was issued -- NOT refused)" % r.status
    except urllib.error.HTTPError as e:
        text = e.read().decode("utf-8", "replace")
        return ("Invalid email or password" in text), "HTTP %d %s" % (e.code, text[:120].replace(password, "<redacted>"))


def delete(n):
    password = None
    try:
        password = _ssm().get_parameter(Name=n["param"], WithDecryption=True)["Parameter"]["Value"]
    except ClientError as e:
        print("WARN: K1-CRED not readable (%s); the refused-login arm is skipped" % e.response["Error"]["Code"])
    _ddb().delete_item(TableName=TABLE, Key={"PK": {"S": n["pk"]}, "SK": {"S": "PROFILE"}})
    gone = get_k1(n) is None
    print("K1 delete: consistent GetItem -> %s" % ("no Item (VERIFIED)" if gone else "ITEM STILL PRESENT"))
    if not gone:
        raise SystemExit("ESCALATE: K1 still present -- set status disabled")
    if password is not None:
        refused, line = _login_refused(n["email"], password)
        print("LOGIN AFTER DELETE: %s -> %s" % (line, "REFUSED 1 of 1" if refused else "NOT REFUSED"))
        password = None
    try:
        _ssm().delete_parameter(Name=n["param"])
    except ClientError as e:
        if e.response["Error"]["Code"] != "ParameterNotFound":
            raise
    try:
        _ssm().get_parameter(Name=n["param"])
        print("K1-CRED delete: STILL PRESENT")
    except ClientError as e:
        print("K1-CRED delete: get-parameter -> %s" % e.response["Error"]["Code"])
    print("AT %s" % dt.datetime.now(dt.timezone.utc).isoformat())


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("preread", "create", "delete"):
        raise SystemExit("usage: walk_principal.py preread|create|delete <epoch>")
    n = names(sys.argv[2])
    {"preread": preread, "create": create, "delete": delete}[sys.argv[1]](n)
