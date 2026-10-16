"""SOC2_MSLOGS round 1, cell SM-r-1 checks (the release: apply, the sign-in subscription, the switch). LIVE reads only:
AWS get/describe/list and the Management API subscription list. Run from the repo root by the CloudOps lane after the apply.

  python s1_check_r1.py applied                 -> R1-APPLIED-OK (both functions run the built zips; the door may invoke the collector; both MFA Denies stand)
  python s1_check_r1.py subs                    -> R1-SUBS-OK    (all four feeds enabled, the sign-in feed included)
  python s1_check_r1.py switch <switch_at.txt>  -> R1-SWITCH-OK  (raw landed for the 7 days, the old table frozen, silver rebuilt, clean fires since the switch)

No object body, secret, token or event is printed. Counts, names and error codes only.
"""
import base64
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request

ROOT = os.getcwd()
BUCKET = "opal-data-trino"
PFX = "m365-metadata/trino/"
COLLECTOR = "m365-metadata-trino-collector-lambda"
DOOR = "globgrph-trino-access-lambda"
LOG_GROUP = "/aws/lambda/m365-metadata-trino-collector-lambda"
SECRET = "m365-metadata/trino/api-credentials"
FOUR = ["Audit.AzureActiveDirectory", "Audit.Exchange", "Audit.General", "Audit.SharePoint"]
ZIPS = {COLLECTOR: "infra/aws/lambda/m365-metadata-collector/build/m365-metadata-collector.zip",
        DOOR: "infra/aws/lambda/globgrph-trino-access/build/globgrph-trino-access.zip"}


def aws(*args, timeout=120):
    exe = shutil.which("aws") or "aws"
    env = dict(os.environ, MSYS_NO_PATHCONV="1")
    p = subprocess.run([exe] + list(args) + ["--output", "json"], capture_output=True, text=True, timeout=timeout, env=env)
    return p.returncode, p.stdout, p.stderr


def j(s):
    try:
        return json.loads(s)
    except ValueError:
        return None


def applied():
    bad = []
    for fn, rel in ZIPS.items():
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            bad.append("no built zip for %s" % fn)
            continue
        want = base64.b64encode(hashlib.sha256(open(p, "rb").read()).digest()).decode()
        rc, out, err = aws("lambda", "get-function-configuration", "--function-name", fn)
        d = j(out) or {}
        if rc != 0 or d.get("CodeSha256") != want:
            bad.append("%s does not run the built zip (live %s)" % (fn, str(d.get("CodeSha256"))[:10]))
        if fn == DOOR:
            env = (d.get("Environment") or {}).get("Variables") or {}
            if env.get("COLLECTOR_FUNCTION") != COLLECTOR:
                bad.append("the door's COLLECTOR_FUNCTION is %r" % env.get("COLLECTOR_FUNCTION"))
    rc, out, err = aws("iam", "get-role-policy", "--role-name", "globgrph-trino-access-role", "--policy-name", "globgrph-trino-access-policy")
    doc = (j(out) or {}).get("PolicyDocument", {})
    inv = [s for s in doc.get("Statement", []) if "lambda:InvokeFunction" in json.dumps(s.get("Action"))]
    if not inv or COLLECTOR not in json.dumps(inv):
        bad.append("the door role cannot invoke the collector function")
    for alias in ("member", "collector"):
        rc, out, err = aws("lambda", "get-policy", "--function-name", DOOR, "--qualifier", alias)
        if rc != 0 or "DenyInvokeWithoutMFA" not in out:
            bad.append("the MFA Deny is missing on the %s alias" % alias)
    if bad:
        print("R1-APPLIED-REFUSED " + "; ".join(bad))
        return 1
    print("R1-APPLIED-OK")
    return 0


def credential():
    rc, out, err = aws("secretsmanager", "get-secret-value", "--secret-id", SECRET)
    if rc != 0:
        return None
    try:
        return json.loads(json.loads(out)["SecretString"])
    except (ValueError, KeyError):
        return None


def subs():
    c = credential()
    if c is None:
        print("R1-SUBS-REFUSED no credential")
        return 1
    body = urllib.parse.urlencode({"grant_type": "client_credentials", "client_id": c["client_id"], "client_secret": c["client_secret"],
                                   "scope": "https://manage.office.com/.default"}).encode()
    with urllib.request.urlopen(urllib.request.Request("https://login.microsoftonline.com/%s/oauth2/v2.0/token" % c["tenant_id"], data=body, method="POST"), timeout=60) as r:
        tok = json.loads(r.read())["access_token"]
    req = urllib.request.Request("https://manage.office.com/api/v1.0/%s/activity/feed/subscriptions/list" % c["tenant_id"], headers={"Authorization": "Bearer " + tok})
    with urllib.request.urlopen(req, timeout=60) as r:
        rows = json.loads(r.read())
    on = sorted(x["contentType"] for x in rows if x.get("status") == "enabled")
    if on != FOUR:
        print("R1-SUBS-REFUSED enabled %r, wanted %r" % (on, FOUR))
        return 1
    print("R1-SUBS-OK %s" % ",".join(on))
    return 0


def list_prefix(prefix):
    rc, out, err = aws("s3api", "list-objects-v2", "--bucket", BUCKET, "--prefix", PFX + prefix, timeout=300)
    if rc != 0:
        return None
    return (j(out) or {}).get("Contents", []) or []


def log_events(ms, pattern):
    events, token = [], None
    for _ in range(200):
        args = ["logs", "filter-log-events", "--log-group-name", LOG_GROUP, "--start-time", ms, "--filter-pattern", pattern]
        if token:
            args += ["--next-token", token]
        rc, out, err = aws(*args)
        if rc != 0:
            return None
        d = j(out) or {}
        events += d.get("events", [])
        token = d.get("nextToken")
        if not token:
            break
    return events


def switch(since_file=None):
    if not since_file:
        print("R1-SWITCH-REFUSED pass the file holding the UTC time of the switch apply")
        return 1
    try:
        t0 = dt.datetime.fromisoformat(open(since_file, encoding="utf-8").read().strip().replace("Z", "+00:00"))
    except (OSError, ValueError):
        print("R1-SWITCH-REFUSED no readable switch time in the file")
        return 1
    bad = []
    rec = list_prefix("bronze/audit_records/")
    if rec is None:
        print("R1-SWITCH-REFUSED the bucket listing failed")
        return 1
    dates = sorted({m.group(1) for o in rec for m in [re.search(r"/date=(\d{8})/", o["Key"])] if m})
    if len(dates) < 7 or len(rec) < 800:
        bad.append("audit_records holds %d objects over %d dates (wanted >= 800 over >= 7)" % (len(rec), len(dates)))
    old = list_prefix("bronze/audit_events/") or []
    late = [o for o in old if dt.datetime.fromisoformat(o["LastModified"].replace("Z", "+00:00")) > t0]
    if late:
        bad.append("%d audit_events objects were written after the switch (the old table must be frozen)" % len(late))
    silver = list_prefix("silver/activity_events/") or []
    fresh = {re.search(r"/date=([\d-]+)/", o["Key"]).group(1) for o in silver if dt.datetime.fromisoformat(o["LastModified"].replace("Z", "+00:00")) > t0}
    if len(fresh) < 7:
        bad.append("silver was rebuilt for only %d dates since the switch (wanted >= 7)" % len(fresh))
    ms = str(int(t0.timestamp() * 1000))
    reports = log_events(ms, "REPORT RequestId")
    errs = log_events(ms, '?errorMessage ?Traceback ?"Task timed out"')
    if reports is None or errs is None:
        bad.append("the collector log group could not be read")
    else:
        badr = [e for e in reports if "Status: timeout" in e["message"] or "Status: error" in e["message"]]
        if len(reports) < 2 or badr or errs:
            bad.append("fires since the switch: %d invocations, %d timeouts or errors, %d error lines" % (len(reports), len(badr), len(errs)))
    if bad:
        print("R1-SWITCH-REFUSED " + "; ".join(bad))
        return 1
    print("R1-SWITCH-OK audit_records=%d dates=%d silver_dates=%d" % (len(rec), len(dates), len(fresh)))
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"applied": applied, "subs": subs, "switch": switch}.get(mode)
    try:
        sys.exit((fn(*sys.argv[2:3]) if mode == "switch" else fn()) if fn else 2)
    except Exception as e:  # noqa: BLE001
        print("R1-%s-REFUSED %s: %s" % (mode.upper(), type(e).__name__, str(e)[:160]))
        sys.exit(1)
