#!/usr/bin/env python3
"""svc-irpt-analysis -- the ONE durable Analysis service principal (W27 packet W27-2; CTO half @dbbac713fc; CRO half
@2ab90bf162; Andrew-direct @51edcd3ee6). Adapted from IRPT_MVP_P/walk_principal.py (the estate's own mint tool):
the credential lives in SECRETS MANAGER permanently, readable by the walker's principal only; retirement is DISABLE.

    python svc_principal.py preread
    python svc_principal.py create      <walker-principal-arn>
    python svc_principal.py readback
    python svc_principal.py census      <role-arn> [<role-arn> ...]     # who can read the secret; DENY expected
    python svc_principal.py negcontrol  <out.json>                       # login + one non-cottonwood read + one cottonwood read
    python svc_principal.py disable     # retirement: status -> disabled (never delete)

The password is generated here, written ONLY to the secret, held in memory only for the login, and never printed,
logged, committed or returned. Every printed line is ASCII and carries no credential. ledger irpt-svc-analysis-principal-20260930.
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
EMAIL = "svc-irpt-analysis@opalinvest.com"
PK = "USER#" + EMAIL
SECRET = "irpt/svc-irpt-analysis/password"
API = "https://d2n2nzpeqf34ge.cloudfront.net"  # production's same-origin path (live_upload.py): /auth/* and /api/scoped/*
SALT_ROUNDS = 12  # auth-handler password.ts:4
ATTRS_NO_HASH = ("PK", "SK", "email", "name", "firstName", "lastName", "role", "userType", "firmId", "status",
                 "allowedFirmIds", "tier", "mfaEnabled", "mfaChannel", "mustChangePassword", "createdAt",
                 "createdBy", "updatedAt")


def _ddb():
    return boto3.client("dynamodb")


def _sm():
    return boto3.client("secretsmanager")


def _now():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def item(pw_hash, now):
    return {"PK": {"S": PK}, "SK": {"S": "PROFILE"}, "email": {"S": EMAIL}, "passwordHash": {"S": pw_hash},
            "name": {"S": "IRPT Analysis Service"}, "firstName": {"S": "IRPT"}, "lastName": {"S": "Analysis Service"},
            "role": {"S": "admin"}, "userType": {"S": "service"}, "firmId": {"S": "opal-capital"},
            "status": {"S": "active"}, "allowedFirmIds": {"S": "cottonwood"}, "tier": {"S": "internal"},
            "mfaEnabled": {"BOOL": False}, "mfaChannel": {"S": "none"}, "mustChangePassword": {"BOOL": False},
            "createdAt": {"S": now}, "updatedAt": {"S": now},
            "createdBy": {"S": "2.0.0_SA_COO~Y svc-irpt-analysis-20260930 (Andrew-direct @51edcd3ee6)"}}


def digest(row):
    shown = {k: v for k, v in row.items() if k != "passwordHash"}
    return hashlib.sha256(json.dumps(shown, sort_keys=True).encode("ascii")).hexdigest()


def get_row(projection=True):
    kw = {"TableName": TABLE, "Key": {"PK": {"S": PK}, "SK": {"S": "PROFILE"}}, "ConsistentRead": True}
    if projection:
        names = {"#f%d" % i: f for i, f in enumerate(ATTRS_NO_HASH)}
        kw.update(ProjectionExpression=", ".join(names), ExpressionAttributeNames=names)
    return _ddb().get_item(**kw).get("Item")


def index_count():
    r = _ddb().query(TableName=TABLE, IndexName="email-index", KeyConditionExpression="email = :e",
                     ExpressionAttributeValues={":e": {"S": EMAIL}}, Select="COUNT")
    return r["Count"]


def secret_state():
    try:
        d = _sm().describe_secret(SecretId=SECRET)
        stages = d.get("VersionIdsToStages") or {}
        return "PRESENT", d["ARN"], {v: s for v, s in stages.items()}
    except ClientError as e:
        return e.response["Error"]["Code"], None, {}


def preread():
    row = get_row()
    st, arn, stages = secret_state()
    print("PREREAD %s: row %s; email-index count %d; secret %s" % (_now(), "PRESENT" if row else "ABSENT",
                                                                    index_count(), st))
    return row is None and index_count() == 0 and st == "ResourceNotFoundException"


def policy_for(walker_arn, secret_arn):
    """Both statements name the secret's own ARN (never `*`): explicit on both sides, and simulable."""
    return json.dumps({"Version": "2012-10-17", "Statement": [
        {"Sid": "WalkerReadsByExplicitArn", "Effect": "Allow", "Principal": {"AWS": walker_arn},
         "Action": ["secretsmanager:GetSecretValue", "secretsmanager:DescribeSecret"], "Resource": secret_arn},
        {"Sid": "NobodyElseReadsTheValue", "Effect": "Deny", "Principal": "*",
         "Action": "secretsmanager:GetSecretValue", "Resource": secret_arn,
         "Condition": {"ArnNotEquals": {"aws:PrincipalArn": walker_arn}}}]})


def repolicy(walker_arn):
    st, arn, _ = secret_state()
    _sm().put_resource_policy(SecretId=SECRET, ResourcePolicy=policy_for(walker_arn, arn), BlockPublicPolicy=True)
    print("OK: resource policy re-put naming %s explicitly; Allow %s; Deny GetSecretValue for every other PrincipalArn"
          % (arn, walker_arn))


def create(walker_arn):
    if not preread():
        raise SystemExit("STOP: pre-read not clean")
    password = secrets.token_urlsafe(32)  # 32 random bytes, urlsafe base64 (43 chars)
    pw_hash = bcrypt.hashpw(password.encode("ascii"), bcrypt.gensalt(SALT_ROUNDS)).decode("ascii")
    created = _sm().create_secret(
        Name=SECRET, SecretString=password,
        Description="svc-irpt-analysis password (IRPT Analysis service principal); readable by the walker only; "
                    "W27 CTO @dbbac713fc / CRO @2ab90bf162",
        Tags=[{"Key": "Purpose", "Value": "InvestorReporting"}, {"Key": "System", "Value": "IRPT-Analysis"},
              {"Key": "Ledger", "Value": "irpt-svc-analysis-principal-20260930"}])
    del password
    _sm().put_resource_policy(SecretId=SECRET, ResourcePolicy=policy_for(walker_arn, created["ARN"]), BlockPublicPolicy=True)
    print("OK: secret created %s (value not printed); resource policy put: Allow %s; Deny GetSecretValue for every "
          "other PrincipalArn" % (created["ARN"], walker_arn))
    now = _now()
    it = item(pw_hash, now)
    _ddb().put_item(TableName=TABLE, Item=it, ConditionExpression="attribute_not_exists(PK)")
    back = get_row(projection=False)
    same = back is not None and digest(back) == digest(it) and back["passwordHash"]["S"] == pw_hash
    print("OK: row put %s at %s; read-back digest %s (passwordHash excluded) %s"
          % (PK, now, digest(back or {}), "EQUAL" if same else "DIFFERENT"))
    if not same:
        raise SystemExit("STOP: row read-back differs -- rollback: delete the row and the secret")
    print("HANDOVER: email %s ; password by NAME %s (Secrets Manager)" % (EMAIL, SECRET))


def readback():
    row = get_row() or {}
    flat = {k: list(v.values())[0] for k, v in row.items()}
    print("ROW (projection excludes passwordHash; %d of %d attributes present):" % (len(flat), len(ATTRS_NO_HASH)))
    for k in ATTRS_NO_HASH:
        print("  %-18s %s" % (k, json.dumps(flat.get(k))))
    print("email-index count:", index_count())
    st, arn, stages = secret_state()
    print("SECRET %s: %s; versions %d; stages %s (value never read here)" % (SECRET, st, len(stages),
                                                                             json.dumps(stages, sort_keys=True)))
    try:
        pol = _sm().get_resource_policy(SecretId=SECRET).get("ResourcePolicy")
        print("RESOURCE POLICY:", json.dumps(json.loads(pol), sort_keys=True) if pol else None)
    except ClientError as e:
        print("RESOURCE POLICY: %s" % e.response["Error"]["Code"])


def census(role_arns):
    st, arn, _ = secret_state()
    pol = _sm().get_resource_policy(SecretId=SECRET).get("ResourcePolicy")
    iam = boto3.client("iam")
    allowed, denied = [], []
    for r in role_arns:
        res = iam.simulate_principal_policy(PolicySourceArn=r, ActionNames=["secretsmanager:GetSecretValue"],
                                            ResourceArns=[arn], ResourcePolicy=pol)
        dec = res["EvaluationResults"][0]["EvalDecision"]
        (allowed if dec == "allowed" else denied).append((r.split("/")[-1], dec))
        print("  %-60s %s" % (r.split("/")[-1], dec))
    print("CENSUS: %d principal(s) simulated against %s with its resource policy: allowed %d, denied %d"
          % (len(role_arns), SECRET, len(allowed), len(denied)))
    if allowed:
        print("BLOCKING: a non-walker principal is ALLOWED to read the value:", allowed)


def _call(method, path, body, headers, log):
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(API + path, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            status, raw = r.status, r.read()
    except urllib.error.HTTPError as e:
        status, raw = e.code, e.read()
    try:
        parsed = json.loads(raw.decode("utf-8"))
    except Exception:
        parsed = raw.decode("utf-8", "replace")[:800]
    logged = parsed
    if isinstance(parsed, dict) and any("token" in k.lower() for k in parsed):
        logged = {k: ("<redacted>" if "token" in k.lower() else v) for k, v in parsed.items()}
    log.append({"at": _now(), "method": method, "path": path, "status": status, "response": logged})
    return status, parsed


def negcontrol(out):
    log = []
    password = _sm().get_secret_value(SecretId=SECRET)["SecretString"]  # the walker's own read, into memory only
    s, login = _call("POST", "/auth/login", {"email": EMAIL, "password": password},
                     {"Content-Type": "application/json"}, log)
    del password
    log[-1]["request"] = {"email": EMAIL, "password": "<redacted>"}
    token = login.get("accessToken") if isinstance(login, dict) else None
    print("K2 login: HTTP %d; token present %s; mfaRequired %s" % (s, bool(token),
          isinstance(login, dict) and login.get("mfaRequired")))
    results = {"login_status": s, "token_present": bool(token)}
    if token:
        h = {"Authorization": "Bearer " + token, "X-Contract-Version": "v1"}
        for firm in ("inflection", "cottonwood"):
            s2, resp = _call("GET", "/api/scoped/investor-reporting/status?selected_tenant=" + firm, None, h, log)
            reason = None
            if isinstance(resp, dict):
                st = resp.get("status") if isinstance(resp.get("status"), dict) else {}
                reason = st.get("public_reason_code") or resp.get("reason") or resp.get("error")
            ok = isinstance(resp, dict) and resp.get("ok")
            print("READ selected_tenant=%s: HTTP %d; ok %s; reason %s -> %s"
                  % (firm, s2, ok, reason, "ADMITTED" if s2 == 200 and ok else "REFUSED"))
            results[firm] = {"status": s2, "ok": ok, "reason": reason}
        # A RESOURCE read (CTO condition 4): the selected firm's directory population, ONE entry at most; the
        # log keeps counts and codes only -- never a directory entry (names are the firm's data).
        for firm in ("inflection", "cottonwood"):
            s3, resp = _call("GET", "/api/scoped/investor-reporting/directory/search?selected_tenant=" + firm
                             + "&q=&limit=1", None, h, log)
            data = resp.get("data") if isinstance(resp, dict) else None
            entries = data.get("entries") if isinstance(data, dict) else (data if isinstance(data, list) else None)
            n = len(entries) if isinstance(entries, list) else None
            reason = None
            if isinstance(resp, dict):
                st = resp.get("status") if isinstance(resp.get("status"), dict) else {}
                reason = st.get("public_reason_code") or resp.get("reason") or resp.get("error")
            ok = isinstance(resp, dict) and resp.get("ok")
            log[-1]["response"] = {"ok": ok, "reason": reason, "entries_returned": n,
                                   "firm_id": resp.get("firm_id") if isinstance(resp, dict) else None,
                                   "keys": sorted(resp) if isinstance(resp, dict) else None}
            verdict = "ADMITTED (a resource of %s was served)" % firm if (s3 == 200 and ok and n) else "REFUSED or EMPTY"
            print("DIRECTORY selected_tenant=%s: HTTP %d; ok %s; entries %s; reason %s -> %s"
                  % (firm, s3, ok, n, reason, verdict))
            results["directory_" + firm] = {"status": s3, "ok": ok, "entries": n, "reason": reason}
        del token
    json.dump({"principal": EMAIL, "at": _now(), "results": results, "calls": log},
              open(out, "w", encoding="utf-8", newline="\n"), indent=1)
    print("log written:", out)


def disable():
    _ddb().update_item(TableName=TABLE, Key={"PK": {"S": PK}, "SK": {"S": "PROFILE"}},
                       UpdateExpression="SET #s = :d, updatedAt = :t",
                       ExpressionAttributeNames={"#s": "status"},
                       ExpressionAttributeValues={":d": {"S": "disabled"}, ":t": {"S": _now()}},
                       ConditionExpression="attribute_exists(PK)")
    print("DISABLED %s at %s; status read-back: %s" % (PK, _now(), (get_row() or {}).get("status")))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] not in ("preread", "create", "readback", "census", "negcontrol", "disable", "repolicy"):
        raise SystemExit(__doc__)
    {"preread": lambda: preread(), "create": lambda: create(a[1]), "readback": readback,
     "census": lambda: census(a[1:]), "negcontrol": lambda: negcontrol(a[1]), "disable": disable,
     "repolicy": lambda: repolicy(a[1])}[a[0]]()
