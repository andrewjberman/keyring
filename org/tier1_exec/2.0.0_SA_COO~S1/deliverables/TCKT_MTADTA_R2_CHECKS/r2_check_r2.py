"""TCKT_MTADTA round 2, cell MD-r-2 checks (identity live, subscriptions, two scheduled fires). LIVE reads only.
Run from the repo root by the CloudOps seat, after Andrew's consent and the secret values.

  python r2_check_r2.py app  -> R2-APP-OK  (the credential secret holds tenant_id, client_id, client_secret; only the key NAMES are printed)
  python r2_check_r2.py subs -> R2-SUBS-OK (the three subscriptions are enabled; the sign-in feed is not)
  python r2_check_r2.py fires <start-time-file> -> R2-FIRES-OK (two scheduled collector invocations since that time, no function error)

No secret value, tenant id, client id, token or event is printed.
"""
import json
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request

SECRET = "m365-metadata/trino/api-credentials"
SUBJECT_KEY = "m365-metadata/trino/subject-key"
LOG_GROUP = "/aws/lambda/m365-metadata-trino-collector-lambda"
WANT = ["Audit.Exchange", "Audit.General", "Audit.SharePoint"]


def aws(*args, timeout=90):
    exe = shutil.which("aws") or "aws"
    p = subprocess.run([exe] + list(args) + ["--output", "json"], capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def credential():
    rc, out, err = aws("secretsmanager", "get-secret-value", "--secret-id", SECRET)
    if rc != 0:
        return None
    try:
        return json.loads(json.loads(out)["SecretString"])
    except (ValueError, KeyError):
        return None


def app():
    bad = []
    c = credential()
    if c is None:
        print("R2-APP-REFUSED the credential secret has no readable JSON value")
        return 1
    for k in ("tenant_id", "client_id", "client_secret"):
        if not c.get(k):
            bad.append("missing %s" % k)
    rc, out, err = aws("secretsmanager", "get-secret-value", "--secret-id", SUBJECT_KEY)
    if rc != 0 or len(json.loads(out).get("SecretString", "")) < 32:
        bad.append("the subject-key secret has no value of 32 characters or more")
    if bad:
        print("R2-APP-REFUSED " + "; ".join(bad))
        return 1
    print("R2-APP-OK keys=tenant_id,client_id,client_secret")
    return 0


def token(c):
    body = urllib.parse.urlencode({"grant_type": "client_credentials", "client_id": c["client_id"], "client_secret": c["client_secret"],
                                   "scope": "https://manage.office.com/.default"}).encode()
    req = urllib.request.Request("https://login.microsoftonline.com/%s/oauth2/v2.0/token" % c["tenant_id"], data=body, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())["access_token"]


def subs():
    c = credential()
    if c is None:
        print("R2-SUBS-REFUSED no credential")
        return 1
    req = urllib.request.Request("https://manage.office.com/api/v1.0/%s/activity/feed/subscriptions/list" % c["tenant_id"],
                                 headers={"Authorization": "Bearer " + token(c)})
    with urllib.request.urlopen(req, timeout=60) as r:
        rows = json.loads(r.read())
    on = sorted(x["contentType"] for x in rows if x.get("status") == "enabled")
    if on != WANT:
        print("R2-SUBS-REFUSED enabled content types %r, wanted %r" % (on, WANT))
        return 1
    print("R2-SUBS-OK %s" % ",".join(on))
    return 0


def log_events(ms, pattern):
    """Every event of the collector log group since ms matching pattern, following nextToken (a filtered read can return a partial page)."""
    events, token, pages = [], None, 0
    while True:
        args = ["logs", "filter-log-events", "--log-group-name", LOG_GROUP, "--start-time", ms, "--filter-pattern", pattern]
        if token:
            args += ["--next-token", token]
        rc, out, err = aws(*args)
        if rc != 0:
            return None, pages
        d = json.loads(out)
        events += d.get("events", [])
        pages += 1
        token = d.get("nextToken")
        if not token or pages > 200:
            return events, pages


def fires(since_file=None):
    import datetime as dt

    if not since_file:
        print("R2-FIRES-REFUSED pass the file holding the time the subscriptions started")
        return 1
    try:
        started = dt.datetime.fromisoformat(open(since_file, encoding="utf-8").read().strip().replace("Z", "+00:00"))
    except (OSError, ValueError):
        print("R2-FIRES-REFUSED no readable start time in the file")
        return 1
    ms = str(int(started.timestamp() * 1000))
    events, pages_r = log_events(ms, "REPORT RequestId")
    if events is None:
        print("R2-FIRES-REFUSED no collector log group yet")
        return 1
    reports = [e["message"] for e in events]
    bad_reports = [r for r in reports if "Status: timeout" in r or "Status: error" in r]
    err_events, _pages = log_events(ms, '?errorMessage ?Traceback ?"Task timed out"')
    errs = len(err_events) if err_events is not None else -1
    if len(reports) < 2 or errs != 0 or bad_reports:
        print("R2-FIRES-REFUSED invocations_since_start=%d (pages=%d) timed_out_or_errored_reports=%d function_error_lines=%d" % (len(reports), pages_r, len(bad_reports), errs))
        return 1
    print("R2-FIRES-OK invocations_since_start=%d (pages=%d) function_errors=0 timeouts=0" % (len(reports), pages_r))
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"app": app, "subs": subs, "fires": fires}.get(mode)
    try:
        sys.exit((fn(*sys.argv[2:3]) if mode == "fires" else fn()) if fn else 2)
    except Exception as e:  # noqa: BLE001
        print("R2-%s-REFUSED %s" % (mode.upper(), type(e).__name__))
        sys.exit(1)
