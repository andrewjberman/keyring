"""IRPT_ANLREQ round 44, workstream T -- the issuer's LIVE read-only check (2.0.0_SA_COO~T2).

  ap1  R44-AP1  the commentary deploy is applied and proven: the three functions of the transcripts root run ONE digest, it is not the
                pre-act digest xC1GDXXp, and the commentary function's log group holds the INFO line the logger fix makes possible,
                `commentary draft exists request_id=REQ-d47252fe74634d0c5cdd8067` (the proof invoke for the draft that already existed)

Read-only: one configuration read per function and one log filter. Prints R44-AP1-OK or R44-AP1-FAIL <reason>.
"""
import json
import subprocess
import sys

FUNCTIONS = ["teams-global-transcripts-pull-lambda", "outlook-global-transcripts-pull-lambda", "outlook-global-commentary-draft-lambda"]
PRE_ACT = "xC1GDXXp"
LOG_GROUP = "/aws/lambda/outlook-global-commentary-draft-lambda"
PATTERN = "commentary draft exists request_id=REQ-d47252fe74634d0c5cdd8067"
AWS = [sys.executable, "-c", "import subprocess,sys;sys.exit(subprocess.call(['bash','.tools/aws']+sys.argv[1:]))"]


def aws(*args):
    r = subprocess.run(AWS + list(args), capture_output=True, text=True, timeout=120)
    return r.returncode, r.stdout, r.stderr


def digests():
    out = {}
    for fn in FUNCTIONS:
        rc, so, se = aws("lambda", "get-function-configuration", "--function-name", fn, "--query", "CodeSha256", "--output", "text")
        if rc != 0:
            return None, "read failed for %s rc=%d" % (fn, rc)
        out[fn] = so.strip()
    return out, ""


def main():
    d, why = digests()
    if d is None:
        return False, why
    vals = set(d.values())
    if len(vals) != 1:
        return False, "digests=%d (not one): %s" % (len(vals), ", ".join(sorted(v[:8] for v in vals)))
    live = vals.pop()
    if live.startswith(PRE_ACT):
        return False, "a function still runs the pre-act zip (%s)" % live[:8]
    rc, so, se = aws("logs", "filter-log-events", "--log-group-name", LOG_GROUP, "--filter-pattern", '"%s"' % PATTERN,
                     "--output", "json")
    if rc != 0:
        return False, "log read failed rc=%d" % rc
    try:
        n = len(json.loads(so).get("events") or [])
    except ValueError:
        return False, "log read unparseable"
    if n < 1:
        return False, "digest %s is live on all three, but the INFO line is absent (events=%d)" % (live[:8], n)
    return True, "digests=1 live=%s events_with_INFO_line=%d" % (live[:8], n)


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] != "ap1":
        print("usage: r44_checks.py ap1")
        sys.exit(2)
    ok, why = main()
    print("R44-AP1-%s %s" % ("OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
