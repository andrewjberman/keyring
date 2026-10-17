"""IRPT_ANLREQ rounds 60-65, workstream T -- the issuer's checks of the FWD-5 live cross-firm sittings (2.0.0_SA_COO~T2).

The THIRD sitting (CTO msg 10010, CVO ADJUDICATION_v26) drives TWO targets with the same two principals:
  packaged   the packaged ticket TCK-20261014-2965a5e0 (its files exist), reports in <DIR>/packaged/
  synthetic  the synthetic ticket TCK-20261015-944c84f8 and its job (the job-level reads), reports in <DIR>/synthetic/
each holding fwd5_run_report.json (the firm-B principal) and fwd5_control_report.json (the entitled control). Each report has
15 rows: 13 made calls and 2 EXCLUDED.

  report  R56-REPORT  both run reports: schema, go token, firm-a cottonwood, firm-b 49financial, signed in, 13 REFUSED / 0 LEAK /
                      0 UNREACHED / 2 EXCLUDED, rc 0, every report-side REFUSED carrying a fence code (the no-selection call may be
                      refused by absence), nothing that is a body, token, password or address.
  control R56-CONTROL both control reports: schema, mode control, go, firm-a opal-capital, firm-b 49financial, ticket-read and
                      ticket-list ALLOWED, rc 0, verdicts only ALLOWED/DENIED/UNREACHED/EXCLUDED.
  fence   R56-FENCE   per target and route: SHOWN iff the control read ALLOWED and firm B read REFUSED; PAST-FENCE iff the control read
                      DENIED with a non-fence code (NOT_FOUND and the like: it passed the guard, no artifact) and firm B was REFUSED.
                      OK needs every made route except form-as-filled SHOWN or PAST-FENCE (the no-selection call needs firm B REFUSED
                      only), and on the packaged target original-upload, report-pdf and commentary-pdf SHOWN (the control served each file).
  absent  R56-ABSENT  BOTH minted principals are gone from opal-users-v2: no PROFILE row (consistent) and email-index count 0.
  --self-test         the evaluators against green cases and mutants.

Read-only: file reads (report, control, fence), one get-item and one index-count query per principal (absent). Prints R56-<ARM>-OK or -FAIL <reason>.
"""
import json
import os
import subprocess
import sys
import tempfile

DIR = "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_fwd5_s3/"
TARGETS = ("packaged", "synthetic")
GO = "IRPT_ANLREQ.TO-RUN-FWD5.live-cross-firm-s3-ib2"
EMAIL = "fwd5-cottonwood-r60@opal.invalid"
EMAIL_CONTROL = "fwd5-control-r60@opal.invalid"
TABLE = "opal-users-v2"
CALL_KEYS = {"route", "method", "status", "verdict", "body_len", "reason", "code"}
MADE_ROUTES = ("ticket-read", "ticket-list", "form-as-filled", "original-upload", "opal-report", "report-pdf", "commentary-pdf",
               "request-read", "request-history", "job-status", "narrative", "export-receipt", "request-read-no-selection")
REPORT_SIDE = MADE_ROUTES[3:]
FILE_ROUTES = ("original-upload", "report-pdf", "commentary-pdf")
NO_SELECTION = "request-read-no-selection"
FENCE_CODES = ("FIRM_BINDING", "NOT_AUTHORIZED")
NOT_PAST = FENCE_CODES + ("CONTRACT_VERSION", "?", "")
FORBIDDEN = ("bearer", "password", "accesstoken", "refresh", "@opal.invalid", "set-cookie")
AWS = [sys.executable, "-c", "import subprocess,sys;sys.exit(subprocess.call(['bash','.tools/aws']+sys.argv[1:]))"]


def _load(text):
    try:
        obj = json.loads(text)
    except ValueError:
        return None
    return obj if isinstance(obj, dict) else None


def _common(rep, text, schema, firm_a):
    low = text.lower()
    bad = [w for w in FORBIDDEN if w in low]
    if bad:
        return "the report holds a forbidden token: %s" % ",".join(bad)
    if rep.get("schema") != schema:
        return "schema is not %s" % schema
    if rep.get("go") != GO:
        return "go token is not %s" % GO
    if rep.get("firm_a") != firm_a or rep.get("firm_b") != "49financial":
        return "firm-a/firm-b are not %s/49financial" % firm_a
    if rep.get("sign_in") != "signed in":
        return "sign_in is %r" % rep.get("sign_in")
    calls = rep.get("calls")
    if not isinstance(calls, list) or len(calls) != 15:
        return "calls is not a list of 15"
    for c in calls:
        if not isinstance(c, dict) or set(c) != CALL_KEYS:
            return "a call row has keys outside the closed set"
    routes = [c["route"] for c in calls if c["verdict"] != "EXCLUDED"]
    if routes != list(MADE_ROUTES):
        return "the made routes are %s, not the 13 expected in order" % routes
    return None


def evaluate(text):
    """(ok, why) over a firm-B run report's text."""
    rep = _load(text)
    if rep is None:
        return False, "the report is not a JSON object"
    err = _common(rep, text, "fwd5_run_report/1", "cottonwood")
    if err:
        return False, err
    calls = rep["calls"]
    for c in calls:
        if c["verdict"] not in ("REFUSED", "LEAK", "UNREACHED", "EXCLUDED"):
            return False, "a verdict is outside the closed set"
        if c["route"] in REPORT_SIDE and c["verdict"] == "REFUSED" and c["route"] != NO_SELECTION and c["code"] not in FENCE_CODES:
            return False, "report-side route %s is REFUSED with code %r, not a fence code" % (c["route"], c["code"])
        if c["route"] == NO_SELECTION and c["verdict"] == "REFUSED" and c["code"] in ("CONTRACT_VERSION", "?", ""):
            return False, "the no-selection call is REFUSED with code %r, which refuses nothing" % c["code"]
    counts = {v: sum(1 for c in calls if c["verdict"] == v) for v in ("REFUSED", "LEAK", "UNREACHED", "EXCLUDED")}
    if counts != {"REFUSED": 13, "LEAK": 0, "UNREACHED": 0, "EXCLUDED": 2}:
        return False, "counts are %s, not 13/0/0/2" % counts
    if rep.get("counts") != counts:
        return False, "the report's own counts disagree with its rows"
    if rep.get("rc") != 0:
        return False, "rc is %r" % rep.get("rc")
    if rep.get("guard_refused"):
        return False, "the guard refused a route"
    return True, "REFUSED=13 LEAK=0 UNREACHED=0 EXCLUDED=2 of 15, rc 0"


def evaluate_control(text):
    """(ok, why) over a control report's text."""
    rep = _load(text)
    if rep is None:
        return False, "the control report is not a JSON object"
    if rep.get("mode") != "control":
        return False, "mode is not control"
    err = _common(rep, text, "fwd5_control_report/1", "opal-capital")
    if err:
        return False, err
    for c in rep["calls"]:
        if c["verdict"] not in ("ALLOWED", "DENIED", "UNREACHED", "EXCLUDED"):
            return False, "a verdict is outside the closed set"
    by = {c["route"]: c["verdict"] for c in rep["calls"]}
    if by.get("ticket-read") != "ALLOWED" or by.get("ticket-list") != "ALLOWED":
        return False, "ticket-read/ticket-list are %s/%s, not ALLOWED" % (by.get("ticket-read"), by.get("ticket-list"))
    if rep.get("rc") != 0:
        return False, "rc is %r" % rep.get("rc")
    return True, "ticket-read ALLOWED, ticket-list ALLOWED, rc 0"


def evaluate_fence(run_text, control_text, target):
    """(ok, why): per route SHOWN or PAST-FENCE; the file routes SHOWN on the packaged target."""
    okr, whyr = evaluate(run_text)
    okc, whyc = evaluate_control(control_text)
    if not okr:
        return False, "%s run report: %s" % (target, whyr)
    if not okc:
        return False, "%s control report: %s" % (target, whyc)
    run = {c["route"]: c for c in json.loads(run_text)["calls"]}
    ctl = {c["route"]: c for c in json.loads(control_text)["calls"]}
    shown, past, missing = [], [], []
    for r in MADE_ROUTES:
        if r == "form-as-filled":
            continue
        if run[r]["verdict"] != "REFUSED":
            missing.append(r)
            continue
        cv, cc = ctl[r]["verdict"], ctl[r]["code"]
        if r == NO_SELECTION:
            past.append(r)
        elif cv == "ALLOWED":
            shown.append(r)
        elif cv == "DENIED" and cc not in NOT_PAST:
            past.append(r)
        else:
            missing.append(r)
    if target == "packaged":
        notserved = [r for r in FILE_ROUTES if r not in shown]
        if notserved:
            return False, "packaged target: the control did not serve %s (shown=%s past=%s)" % (notserved, shown, past)
    if missing:
        return False, "%s: no fence reading on %s (shown=%s past=%s)" % (target, missing, shown, past)
    return True, "%s: SHOWN on %s; PAST-FENCE on %s" % (target, shown, past)


def _read(path):
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _each(fn_one):
    msgs = []
    for t in TARGETS:
        ok, why = fn_one(t)
        if not ok:
            return False, why
        msgs.append(why)
    return True, " || ".join(msgs)


def report():
    def one(t):
        text = _read(DIR + t + "/fwd5_run_report.json")
        if text is None:
            return False, "no run report at %s%s/fwd5_run_report.json" % (DIR, t)
        ok, why = evaluate(text)
        return ok, "%s: %s" % (t, why)
    return _each(one)


def control():
    def one(t):
        text = _read(DIR + t + "/fwd5_control_report.json")
        if text is None:
            return False, "no control report at %s%s/fwd5_control_report.json" % (DIR, t)
        ok, why = evaluate_control(text)
        return ok, "%s: %s" % (t, why)
    return _each(one)


def fence():
    def one(t):
        a, b = _read(DIR + t + "/fwd5_run_report.json"), _read(DIR + t + "/fwd5_control_report.json")
        if a is None or b is None:
            return False, "no reports under %s%s/" % (DIR, t)
        return evaluate_fence(a, b, t)
    return _each(one)


def aws(*args):
    r = subprocess.run(AWS + list(args), capture_output=True, text=True, timeout=120)
    return r.returncode, r.stdout, r.stderr


def absent_one(email):
    paths = []
    try:
        fd1, k = tempfile.mkstemp(suffix=".json")
        paths.append(k)
        with os.fdopen(fd1, "w", encoding="ascii") as fh:
            fh.write(json.dumps({"PK": {"S": "USER#" + email}, "SK": {"S": "PROFILE"}}))
        fd2, v = tempfile.mkstemp(suffix=".json")
        paths.append(v)
        with os.fdopen(fd2, "w", encoding="ascii") as fh:
            fh.write(json.dumps({":e": {"S": email}}))
        rc1, got, _ = aws("dynamodb", "get-item", "--table-name", TABLE, "--key", "file://" + k.replace("\\", "/"),
                          "--consistent-read", "--query", "Item.PK.S", "--output", "text")
        rc2, cnt, _ = aws("dynamodb", "query", "--table-name", TABLE, "--index-name", "email-index",
                          "--key-condition-expression", "email = :e",
                          "--expression-attribute-values", "file://" + v.replace("\\", "/"),
                          "--select", "COUNT", "--query", "Count", "--output", "text")
    finally:
        for p in paths:
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


def absent():
    for email in (EMAIL, EMAIL_CONTROL):
        ok, why = absent_one(email)
        if not ok:
            return False, "%s: %s" % (email.split("@")[0], why)
    return True, "both principals: no PROFILE row (consistent), index count 0"


def _row(route, verdict, code="", status=200, body_len=5):
    return {"route": route, "method": "GET", "status": status, "verdict": verdict, "body_len": body_len, "reason": "", "code": code}


def _excluded():
    return [{"route": "x%d" % i, "method": "-", "status": None, "verdict": "EXCLUDED", "body_len": 0, "reason": "excluded", "code": ""}
            for i in range(2)]


def _green_run():
    calls = []
    for r in MADE_ROUTES:
        if r in REPORT_SIDE:
            calls.append(_row(r, "REFUSED", "NOT_FOUND" if r == NO_SELECTION else "FIRM_BINDING"))
        else:
            calls.append(_row(r, "REFUSED", "", 403 if r != "ticket-list" else 200))
    calls += _excluded()
    return {"schema": "fwd5_run_report/1", "go": GO, "principal_digest": "abcdef012345", "firm_a": "cottonwood",
            "firm_b": "49financial", "sign_in": "signed in", "calls": calls, "guard_refused": [],
            "counts": {"REFUSED": 13, "LEAK": 0, "UNREACHED": 0, "EXCLUDED": 2}, "rc": 0}


def _green_control(packaged):
    calls = []
    for r in MADE_ROUTES:
        if r in ("ticket-read", "ticket-list"):
            calls.append(_row(r, "ALLOWED"))
        elif r == "form-as-filled":
            calls.append(_row(r, "DENIED", "", 404, 63))
        elif r in FILE_ROUTES and packaged:
            calls.append(_row(r, "ALLOWED"))
        else:
            calls.append(_row(r, "DENIED", "NOT_FOUND", 200, 460))
    calls += _excluded()
    return {"schema": "fwd5_control_report/1", "mode": "control", "go": GO, "principal_digest": "abcdef012345",
            "firm_a": "opal-capital", "firm_b": "49financial", "sign_in": "signed in", "calls": calls, "guard_refused": [],
            "counts": {"ALLOWED": 2, "DENIED": 11, "UNREACHED": 0, "EXCLUDED": 2}, "rc": 0}


def self_test():
    g = _green_run()
    gp, gs = _green_control(True), _green_control(False)
    dump = json.dumps
    checks = [("run green", evaluate(dump(g))[0], True), ("control green packaged", evaluate_control(dump(gp))[0], True),
              ("control green synthetic", evaluate_control(dump(gs))[0], True),
              ("fence packaged", evaluate_fence(dump(g), dump(gp), "packaged")[0], True),
              ("fence synthetic", evaluate_fence(dump(g), dump(gs), "synthetic")[0], True),
              ("fence packaged with the unserved control (the synthetic control)", evaluate_fence(dump(g), dump(gs), "packaged")[0], False)]

    def mutate(base, fn):
        d = json.loads(dump(base))
        fn(d)
        return dump(d)

    def idx(d, route):
        return [c["route"] for c in d["calls"]].index(route)

    checks += [
        ("run LEAK", evaluate(mutate(g, lambda d: d["calls"][idx(d, "narrative")].update(verdict="LEAK")))[0], False),
        ("run UNREACHED", evaluate(mutate(g, lambda d: d["calls"][idx(d, "job-status")].update(verdict="UNREACHED")))[0], False),
        ("CONTRACT_VERSION graded REFUSED", evaluate(mutate(g, lambda d: d["calls"][idx(d, "export-receipt")].update(code="CONTRACT_VERSION")))[0], False),
        ("no-selection refused with CONTRACT_VERSION", evaluate(mutate(g, lambda d: d["calls"][idx(d, NO_SELECTION)].update(code="CONTRACT_VERSION")))[0], False),
        ("a route missing", evaluate(mutate(g, lambda d: d["calls"].pop(idx(d, "request-history"))))[0], False),
        ("wrong go", evaluate(mutate(g, lambda d: d.update(go="IRPT_ANLREQ.TO-RUN-FWD5.other")))[0], False),
        ("a secret", evaluate(mutate(g, lambda d: d["calls"][0].update(reason="Bearer abc")))[0], False),
        ("control ticket-read DENIED", evaluate_control(mutate(gp, lambda d: d["calls"][0].update(verdict="DENIED")))[0], False),
        ("control wrong firm", evaluate_control(mutate(gp, lambda d: d.update(firm_a="cottonwood")))[0], False),
        ("control past-fence code is a fence code",
         evaluate_fence(dump(g), mutate(gs, lambda d: d["calls"][idx(d, "narrative")].update(code="FIRM_BINDING")), "synthetic")[0], False),
    ]
    for name, got, want in checks:
        if got != want:
            print("R56-SELFTEST-FAIL %s" % name)
            return 1
    print("R56-SELFTEST-OK %d cases (run green, control green x2, fence x3, 13 mutants refused)" % len(checks))
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
