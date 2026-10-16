"""IRPT_ANLREQ round 60, workstream T -- the issuer's checks of the FWD-5 live cross-firm run (2.0.0_SA_COO~T2).

  report  R56-REPORT  the driver's run report (fwd5_run_report.json, in the applier's deliverables folder) shows: schema fwd5_run_report/1,
                      the run's go token, firm-a cottonwood (the principal's firm) and firm-b 49financial (the ticket's owner), a signed-in
                      session, exactly 7 REFUSED, 0 LEAK, 0 UNREACHED and 2 EXCLUDED rows of 9, rc 0, and nothing in the file that is a
                      body, token, password or address.
  absent  R56-ABSENT  the minted principal (fwd5-cottonwood-r60@opal.invalid) is gone from opal-users-v2: no PROFILE row on a consistent
                      read and a count of 0 on the email index. A control: it passes at the base (nothing was minted) and after the run.
  --self-test         the report evaluator against a green case and six mutants.

Read-only: one file read (report), one get-item and one index-count query (absent). Prints R56-<ARM>-OK or -FAIL <reason>.
"""
import json
import os
import subprocess
import sys
import tempfile

REPORT_PATH = "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_fwd5/fwd5_run_report.json"
GO = "IRPT_ANLREQ.TO-RUN-FWD5.live-cross-firm-ib2"
EMAIL = "fwd5-cottonwood-r60@opal.invalid"
TABLE = "opal-users-v2"
CALL_KEYS = {"route", "method", "status", "verdict", "body_len", "reason"}
FORBIDDEN = ("bearer", "password", "accesstoken", "refresh", "@opal.invalid", "set-cookie")
AWS = [sys.executable, "-c", "import subprocess,sys;sys.exit(subprocess.call(['bash','.tools/aws']+sys.argv[1:]))"]


def evaluate(text):
    """(ok, why) over the report file's text."""
    try:
        rep = json.loads(text)
    except ValueError:
        return False, "the report is not JSON"
    if not isinstance(rep, dict):
        return False, "the report is not an object"
    low = text.lower()
    bad = [w for w in FORBIDDEN if w in low]
    if bad:
        return False, "the report holds a forbidden token: %s" % ",".join(bad)
    if rep.get("schema") != "fwd5_run_report/1":
        return False, "schema is not fwd5_run_report/1"
    if rep.get("go") != GO:
        return False, "go token is not %s" % GO
    if rep.get("firm_a") != "cottonwood" or rep.get("firm_b") != "49financial":
        return False, "firm-a/firm-b are not cottonwood/49financial"
    if rep.get("sign_in") != "signed in":
        return False, "sign_in is %r" % rep.get("sign_in")
    calls = rep.get("calls")
    if not isinstance(calls, list) or len(calls) != 9:
        return False, "calls is not a list of 9"
    for c in calls:
        if not isinstance(c, dict) or set(c) != CALL_KEYS:
            return False, "a call row has keys outside the closed set"
    counts = {v: sum(1 for c in calls if c.get("verdict") == v) for v in ("REFUSED", "LEAK", "UNREACHED", "EXCLUDED")}
    if counts != {"REFUSED": 7, "LEAK": 0, "UNREACHED": 0, "EXCLUDED": 2}:
        return False, "counts are %s, not 7/0/0/2" % counts
    if rep.get("counts") != counts:
        return False, "the report's own counts disagree with its rows"
    if rep.get("rc") != 0:
        return False, "rc is %r" % rep.get("rc")
    if rep.get("guard_refused"):
        return False, "the guard refused a route"
    return True, "REFUSED=7 LEAK=0 UNREACHED=0 EXCLUDED=2 of 9, rc 0"


def report():
    if not os.path.isfile(REPORT_PATH):
        return False, "no report at %s" % REPORT_PATH
    with open(REPORT_PATH, encoding="utf-8") as fh:
        return evaluate(fh.read())


def aws(*args):
    r = subprocess.run(AWS + list(args), capture_output=True, text=True, timeout=120)
    return r.returncode, r.stdout, r.stderr


def absent():
    fds = []
    try:
        fd1, k = tempfile.mkstemp(suffix=".json")
        fds.append(k)
        with os.fdopen(fd1, "w", encoding="ascii") as fh:
            fh.write(json.dumps({"PK": {"S": "USER#" + EMAIL}, "SK": {"S": "PROFILE"}}))
        fd2, v = tempfile.mkstemp(suffix=".json")
        fds.append(v)
        with os.fdopen(fd2, "w", encoding="ascii") as fh:
            fh.write(json.dumps({":e": {"S": EMAIL}}))
        rc1, got, _ = aws("dynamodb", "get-item", "--table-name", TABLE, "--key", "file://" + k.replace("\\", "/"),
                          "--consistent-read", "--query", "Item.PK.S", "--output", "text")
        rc2, cnt, _ = aws("dynamodb", "query", "--table-name", TABLE, "--index-name", "email-index",
                          "--key-condition-expression", "email = :e",
                          "--expression-attribute-values", "file://" + v.replace("\\", "/"),
                          "--select", "COUNT", "--query", "Count", "--output", "text")
    finally:
        for p in fds:
            try:
                os.unlink(p)
            except OSError:
                pass
    if rc1 != 0 or rc2 != 0:
        return False, "a read failed rc=%d,%d" % (rc1, rc2)
    if got.strip() not in ("", "None", "null"):
        return False, "the PROFILE row is PRESENT on a consistent read"
    if cnt.strip() != "0":
        return False, "the email index counts %s" % cnt.strip()
    return True, "no PROFILE row (consistent), index count 0"


def _green():
    calls = [{"route": "r%d" % i, "method": "GET", "status": 404, "verdict": "REFUSED", "body_len": 0, "reason": ""}
             for i in range(7)]
    calls += [{"route": "x%d" % i, "method": "-", "status": None, "verdict": "EXCLUDED", "body_len": 0, "reason": "excluded"}
              for i in range(2)]
    return {"schema": "fwd5_run_report/1", "go": GO, "principal_digest": "abcdef012345", "firm_a": "cottonwood",
            "firm_b": "49financial", "sign_in": "signed in", "calls": calls, "guard_refused": [],
            "counts": {"REFUSED": 7, "LEAK": 0, "UNREACHED": 0, "EXCLUDED": 2}, "rc": 0}


def self_test():
    g = _green()
    cases = [("green", g, True)]

    def mut(name, fn):
        d = json.loads(json.dumps(g))
        fn(d)
        cases.append((name, d, False))

    def leak(d):
        d["calls"][0]["verdict"] = "LEAK"
        d["counts"] = {"REFUSED": 6, "LEAK": 1, "UNREACHED": 0, "EXCLUDED": 2}
        d["rc"] = 1

    def unreached(d):
        d["calls"][1]["verdict"] = "UNREACHED"
        d["counts"] = {"REFUSED": 6, "LEAK": 0, "UNREACHED": 1, "EXCLUDED": 2}
        d["rc"] = 2

    mut("a LEAK", leak)
    mut("an UNREACHED", unreached)
    mut("wrong firms", lambda d: d.update(firm_a="49financial", firm_b="cottonwood"))
    mut("wrong go", lambda d: d.update(go="IRPT_ANLREQ.TO-RUN-FWD5.other"))
    mut("a body key", lambda d: d["calls"][0].update(body="x"))
    mut("a secret", lambda d: d["calls"][0].update(reason="Bearer abc"))
    for name, d, want in cases:
        got, _ = evaluate(json.dumps(d))
        if got != want:
            print("R56-SELFTEST-FAIL %s" % name)
            return 1
    print("R56-SELFTEST-OK green plus six mutants refused")
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        sys.exit(self_test())
    arms = {"report": ("REPORT", report), "absent": ("ABSENT", absent)}
    if len(sys.argv) != 2 or sys.argv[1] not in arms:
        print("usage: r56_checks.py report|absent | --self-test")
        sys.exit(2)
    name, fn = arms[sys.argv[1]]
    ok, why = fn()
    print("R56-%s-%s %s" % (name, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
