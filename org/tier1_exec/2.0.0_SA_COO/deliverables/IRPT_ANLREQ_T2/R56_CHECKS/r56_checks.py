"""IRPT_ANLREQ round 60, workstream T -- the issuer's checks of the FWD-5 live cross-firm run (2.0.0_SA_COO~T2).

  report  R56-REPORT  the driver's run report (fwd5_run_report.json, in the applier's deliverables folder) shows: schema fwd5_run_report/1,
                      the run's go token, firm-a cottonwood (the principal's firm) and firm-b 49financial (the ticket's owner), a signed-in
                      session, exactly 7 REFUSED, 0 LEAK, 0 UNREACHED and 2 EXCLUDED rows of 9, rc 0, and nothing in the file that is a
                      body, token, password or address.
  control R56-CONTROL the driver's --control report (fwd5_control_report.json, same folder): schema fwd5_control_report/1, mode control, the
                      go token, firm-a opal-capital, firm-b 49financial, signed in, ticket-read and ticket-list ALLOWED, rc 0, 9 rows with
                      only ALLOWED/DENIED/UNREACHED/EXCLUDED verdicts, nothing in the file that is a body, token, password or address.
  fence   R56-FENCE   per route, the fence is SHOWN iff the control read ALLOWED and the firm-B run read REFUSED; OK needs it SHOWN on
                      ticket-read and ticket-list (the CTO's positive control, msg 9804); other routes are listed, not required.
  absent  R56-ABSENT  BOTH minted principals (fwd5-cottonwood-r60@opal.invalid and fwd5-control-r60@opal.invalid) are gone from
                      opal-users-v2: no PROFILE row on a consistent read and a count of 0 on the email index. A control: it passes at
                      the base (nothing was minted) and after the run.
  --self-test         the evaluators against green cases and mutants.

Read-only: one file read (report), one get-item and one index-count query (absent). Prints R56-<ARM>-OK or -FAIL <reason>.
"""
import json
import os
import subprocess
import sys
import tempfile

REPORT_PATH = "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_fwd5_s2/fwd5_run_report.json"
GO = "IRPT_ANLREQ.TO-RUN-FWD5.live-cross-firm-s2-ib2"
EMAIL = "fwd5-cottonwood-r60@opal.invalid"
EMAIL_CONTROL = "fwd5-control-r60@opal.invalid"
CONTROL_PATH = REPORT_PATH.replace("fwd5_run_report.json", "fwd5_control_report.json")
TABLE = "opal-users-v2"
CALL_KEYS = {"route", "method", "status", "verdict", "body_len", "reason", "code"}
REPORT_SIDE = ("original-upload", "opal-report", "report-pdf", "commentary-pdf")
FENCE_CODES = ("FIRM_BINDING", "NOT_AUTHORIZED")
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
    for c in calls:
        if c.get("route") in REPORT_SIDE and c.get("verdict") == "REFUSED" and c.get("code") not in FENCE_CODES:
            return False, "report-side route %s is REFUSED with code %r, not a fence code" % (c.get("route"), c.get("code"))
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


def evaluate_control(text):
    """(ok, why) over the control report's text."""
    try:
        rep = json.loads(text)
    except ValueError:
        return False, "the control report is not JSON"
    if not isinstance(rep, dict):
        return False, "the control report is not an object"
    low = text.lower()
    bad = [w for w in FORBIDDEN if w in low]
    if bad:
        return False, "the control report holds a forbidden token: %s" % ",".join(bad)
    if rep.get("schema") != "fwd5_control_report/1" or rep.get("mode") != "control":
        return False, "schema/mode are not fwd5_control_report/1 / control"
    if rep.get("go") != GO:
        return False, "go token is not %s" % GO
    if rep.get("firm_a") != "opal-capital" or rep.get("firm_b") != "49financial":
        return False, "firm-a/firm-b are not opal-capital/49financial"
    if rep.get("sign_in") != "signed in":
        return False, "sign_in is %r" % rep.get("sign_in")
    calls = rep.get("calls")
    if not isinstance(calls, list) or len(calls) != 9:
        return False, "calls is not a list of 9"
    for c in calls:
        if not isinstance(c, dict) or set(c) != CALL_KEYS or c.get("verdict") not in ("ALLOWED", "DENIED", "UNREACHED", "EXCLUDED"):
            return False, "a call row has keys or a verdict outside the closed set"
    by = {c["route"]: c["verdict"] for c in calls}
    if by.get("ticket-read") != "ALLOWED" or by.get("ticket-list") != "ALLOWED":
        return False, "ticket-read/ticket-list are %s/%s, not ALLOWED" % (by.get("ticket-read"), by.get("ticket-list"))
    if rep.get("rc") != 0:
        return False, "rc is %r" % rep.get("rc")
    return True, "ticket-read ALLOWED, ticket-list ALLOWED, rc 0; " + ",".join("%s=%s" % (k, v) for k, v in sorted(by.items()))


def evaluate_fence(run_text, control_text):
    """(ok, why): per route the fence is SHOWN iff control ALLOWED and run REFUSED; OK needs ticket-read and ticket-list SHOWN."""
    okr, whyr = evaluate(run_text)
    okc, whyc = evaluate_control(control_text)
    if not okr:
        return False, "run report: " + whyr
    if not okc:
        return False, "control report: " + whyc
    run = {c["route"]: c["verdict"] for c in json.loads(run_text)["calls"]}
    ctl = {c["route"]: c["verdict"] for c in json.loads(control_text)["calls"]}
    shown = sorted(r for r in run if run[r] == "REFUSED" and ctl.get(r) == "ALLOWED")
    inconclusive = sorted(r for r in run if run[r] == "REFUSED" and ctl.get(r) != "ALLOWED")
    if "ticket-read" not in shown or "ticket-list" not in shown:
        return False, "fence not shown on ticket-read and ticket-list; shown=%s inconclusive=%s" % (shown, inconclusive)
    return True, "fence SHOWN on %s; INCONCLUSIVE (control not ALLOWED) on %s" % (shown, inconclusive)


def control():
    if not os.path.isfile(CONTROL_PATH):
        return False, "no control report at %s" % CONTROL_PATH
    with open(CONTROL_PATH, encoding="utf-8") as fh:
        return evaluate_control(fh.read())


def fence():
    for pth in (REPORT_PATH, CONTROL_PATH):
        if not os.path.isfile(pth):
            return False, "no report at %s" % pth
    with open(REPORT_PATH, encoding="utf-8") as a, open(CONTROL_PATH, encoding="utf-8") as b:
        return evaluate_fence(a.read(), b.read())


def report():
    if not os.path.isfile(REPORT_PATH):
        return False, "no report at %s" % REPORT_PATH
    with open(REPORT_PATH, encoding="utf-8") as fh:
        return evaluate(fh.read())


def aws(*args):
    r = subprocess.run(AWS + list(args), capture_output=True, text=True, timeout=120)
    return r.returncode, r.stdout, r.stderr


def absent():
    for email in (EMAIL, EMAIL_CONTROL):
        ok, why = absent_one(email)
        if not ok:
            return False, "%s: %s" % (email.split("@")[0], why)
    return True, "both principals: no PROFILE row (consistent), index count 0"


def absent_one(EMAIL):
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
    names = ["ticket-read", "ticket-list", "form-as-filled", "original-upload", "opal-report", "report-pdf", "commentary-pdf"]
    calls = [{"route": n, "method": "GET", "status": 404, "verdict": "REFUSED", "body_len": 0, "reason": "",
              "code": "FIRM_BINDING" if n in REPORT_SIDE else ""} for n in names]
    calls += [{"route": "x%d" % i, "method": "-", "status": None, "verdict": "EXCLUDED", "body_len": 0, "reason": "excluded",
               "code": ""} for i in range(2)]
    return {"schema": "fwd5_run_report/1", "go": GO, "principal_digest": "abcdef012345", "firm_a": "cottonwood",
            "firm_b": "49financial", "sign_in": "signed in", "calls": calls, "guard_refused": [],
            "counts": {"REFUSED": 7, "LEAK": 0, "UNREACHED": 0, "EXCLUDED": 2}, "rc": 0}


def _green_control():
    names = ["ticket-read", "ticket-list", "form-as-filled", "original-upload", "opal-report", "report-pdf", "commentary-pdf"]
    calls = [{"route": n, "method": "GET", "status": 200 if i < 2 else 404, "verdict": "ALLOWED" if i < 2 else "DENIED",
              "body_len": 5, "reason": "", "code": ""} for i, n in enumerate(names)]
    calls += [{"route": "x%d" % i, "method": "-", "status": None, "verdict": "EXCLUDED", "body_len": 0, "reason": "excluded",
               "code": ""} for i in range(2)]
    return {"schema": "fwd5_control_report/1", "mode": "control", "go": GO, "principal_digest": "abcdef012345",
            "firm_a": "opal-capital", "firm_b": "49financial", "sign_in": "signed in", "calls": calls, "guard_refused": [],
            "counts": {"ALLOWED": 2, "DENIED": 5, "UNREACHED": 0, "EXCLUDED": 2}, "rc": 0}


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

    mut("a CONTRACT_VERSION refusal graded REFUSED", lambda d: d["calls"][3].update(code="CONTRACT_VERSION"))
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
    gc = _green_control()
    ccases = [("control green", gc, True)]
    for name, fn in (("control ticket-read DENIED", lambda d: d["calls"][0].update(verdict="DENIED")),
                     ("control list UNREACHED", lambda d: d["calls"][1].update(verdict="UNREACHED")),
                     ("control wrong firm", lambda d: d.update(firm_a="cottonwood")),
                     ("control uses REFUSED", lambda d: d["calls"][2].update(verdict="REFUSED"))):
        d = json.loads(json.dumps(gc))
        fn(d)
        ccases.append((name, d, False))
    for name, d, want in ccases:
        got, _ = evaluate_control(json.dumps(d))
        if got != want:
            print("R56-SELFTEST-FAIL %s" % name)
            return 1
    okf, _ = evaluate_fence(json.dumps(g), json.dumps(gc))
    d = json.loads(json.dumps(gc))
    d["calls"][1]["verdict"] = "DENIED"
    badf, _ = evaluate_fence(json.dumps(g), json.dumps(d))
    if not okf or badf:
        print("R56-SELFTEST-FAIL fence")
        return 1
    print("R56-SELFTEST-OK green plus seven mutants refused; control green plus four mutants; fence both ways")
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        sys.exit(self_test())
    arms = {"report": ("REPORT", report), "control": ("CONTROL", control), "fence": ("FENCE", fence), "absent": ("ABSENT", absent)}
    if len(sys.argv) != 2 or sys.argv[1] not in arms:
        print("usage: r56_checks.py report|control|fence|absent | --self-test")
        sys.exit(2)
    name, fn = arms[sys.argv[1]]
    ok, why = fn()
    print("R56-%s-%s %s" % (name, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
