"""Cases for org/devices/role_request.py (NFRA_CTLPLN cell CT-c-2, PRD v0.8 C-ROLE-REQUEST (a)).

Run: python org/devices/test_role_request.py   (LAST line: ROLE-REQUEST cases=<k>/<n> ok=<True|False>)

Every case runs in a TEMPORARY repo root: a copy of the real register, fixture projects, a fixture Terraform root and a fixture code
file, with a temporary records directory. The live org/devices/DEVICES.json and org/devices/role_requests/ are never touched, and the
bus send is a RECORDER: nothing is sent.
"""
import contextlib
import importlib.util
import io
import json
import os
import pathlib
import shutil
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
spec = importlib.util.spec_from_file_location("role_request_under_test", str(HERE / "role_request.py"))
rr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rr)

GOOD_PERM = "logs:CreateLogStream,arn:aws:logs:us-east-1:111111111111:log-group:/aws/lambda/fix-probe:*,src/app.py:3"
SERIAL = "0.9.0_WK_FIXTURE~1"


def make_root(tmp: pathlib.Path) -> pathlib.Path:
    """A temporary repo root: the real register's bytes, a project placed on each Dell, one Terraform root, one 5-line code file."""
    (tmp / "org" / "devices").mkdir(parents=True)
    shutil.copy(str(ROOT / "org" / "devices" / "DEVICES.json"), str(tmp / "org" / "devices" / "DEVICES.json"))
    for code, placement in (("FIXD1", "DELL1"), ("FIXD2", "DELL2"), ("FIXLAP", "LAPTOP")):
        d = tmp / "org" / "missions" / "D0" / "FIX" / code
        d.mkdir(parents=True)
        (d / "project.json").write_text(json.dumps({"project_code": code, "placement": placement}), encoding="utf-8")
    (tmp / "infra" / "aws" / "terraform" / "fixroot").mkdir(parents=True)
    (tmp / "src").mkdir()
    (tmp / "src" / "app.py").write_text("a = 1\nb = 2\nc = 3\nd = 4\ne = 5\n", encoding="utf-8")
    return tmp


class Recorder:
    def __init__(self):
        self.calls = []

    def __call__(self, root, to_device, from_serial, line):
        self.calls.append((to_device, from_serial, line))
        return 0, "recorded"


def run(root, device, args, send=None):
    """Run main() in-process with AGENTBUS_DEVICE=device (None = unset); (rc, stdout, stderr, recorder)."""
    rec = send or Recorder()
    saved = {k: os.environ.get(k) for k in ("AGENTBUS_DEVICE", "OPAL_AGENT_SERIAL", "OPAL_DEVICE_REGISTER")}
    os.environ.pop("OPAL_DEVICE_REGISTER", None)
    os.environ["OPAL_AGENT_SERIAL"] = SERIAL
    if device is None:
        os.environ.pop("AGENTBUS_DEVICE", None)
    else:
        os.environ["AGENTBUS_DEVICE"] = device
    out, err = io.StringIO(), io.StringIO()
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = rr.main(args, root=root, send=rec)
    except SystemExit as exc:   # argparse refusals
        rc = exc.code if isinstance(exc.code, int) else 2
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
    return rc, out.getvalue(), err.getvalue(), rec


def write_args(project="FIXD1", perms=(GOOD_PERM,), root="fixroot", extra=()):
    a = ["write", "--project", project, "--root", root, "--kind", "aws_lambda_function", "--name", "fix-probe",
         "--service", "lambda.amazonaws.com"]
    for p in perms:
        a += ["--permission", p]
    return a + list(extra)


def records_of(root):
    return sorted((root / rr.RECORDS_REL).glob("*/*.json")) if (root / rr.RECORDS_REL).exists() else []


def refused(root, device, args, needle):
    """A refusal: rc != 0, the message holds `needle`, no record written, nothing sent."""
    rc, out, err, rec = run(root, device, args)
    ok = rc != 0 and needle in err and not records_of(root) and not rec.calls
    return ok, "rc=%s stderr=%s records=%d sent=%d" % (rc, err.strip()[:160], len(records_of(root)), len(rec.calls))


def case_valid(root):
    rc, out, err, rec = run(root, "dell1", write_args())
    files = records_of(root)
    if rc != 0 or len(files) != 1:
        return False, "rc=%s err=%s files=%d" % (rc, err, len(files))
    rc2, out2, _, _ = run(root, "dell1", ["validate", str(files[0])])
    last = out2.strip().splitlines()[-1]
    doc = json.loads(files[0].read_text(encoding="utf-8"))
    ok = (last == "ROLE-REQUEST-VALID %s ok=True" % doc["request_id"] and files[0].parent.name == "dell1"
          and doc["status"] == "requested" and len(rec.calls) == 1)
    return ok, last


def case_unset(root):
    return refused(root, None, write_args(), "AGENTBUS_DEVICE is not set")


def case_not_execution(root):
    return refused(root, "laptop", write_args(project="FIXLAP"), "only an `execution` box")


def case_other_dell(root):
    return refused(root, "dell1", write_args(project="FIXD2"), "is placed on DELL2, not on dell1")


def case_missing_file(root):
    return refused(root, "dell1", write_args(perms=(GOOD_PERM.replace("src/app.py:3", "src/nope.py:3"),)), "does not exist")


def case_line_past_end(root):
    return refused(root, "dell1", write_args(perms=(GOOD_PERM.replace("src/app.py:3", "src/app.py:6"),)), "line 6 is outside")


def case_iam(root):
    return refused(root, "dell1", write_args(perms=(GOOD_PERM.replace("logs:CreateLogStream", "iam:PassRole"),)), "iam: action")


def case_star(root):
    return refused(root, "dell1", write_args(perms=(GOOD_PERM.replace("logs:CreateLogStream", "*"),)), "wildcard")


def case_bus_line(root):
    rc, out, err, rec = run(root, "dell1", write_args())
    files = records_of(root)
    if rc != 0 or len(rec.calls) != 1 or len(files) != 1:
        return False, "rc=%s calls=%d files=%d" % (rc, len(rec.calls), len(files))
    to, frm, line = rec.calls[0]
    rid = files[0].stem
    want_path = "org/devices/role_requests/dell1/%s.json" % rid
    ok = (to == "laptop" and frm == SERIAL and line.startswith("ROLE-REQUEST %s FIXD1 aws_lambda_function/fix-probe " % rid)
          and line.endswith(want_path) and line in out)
    return ok, line


def case_list(root):
    run(root, "dell1", write_args())
    files = records_of(root)
    if len(files) != 1:
        return False, "expected one written record, got %d" % len(files)
    # a second record, with its own id, is placed by hand: two writes in one second would share a timestamp
    doc = json.loads(files[0].read_text(encoding="utf-8"))
    doc["request_id"] = doc["request_id"][:-4] + ("ffff" if not doc["request_id"].endswith("ffff") else "eeee")
    doc["resource"]["name"] = "fix-second"
    (files[0].parent / (doc["request_id"] + ".json")).write_text(json.dumps(doc), encoding="utf-8")
    files = records_of(root)
    files.sort()
    first = json.loads(files[0].read_text(encoding="utf-8"))["request_id"]
    adir = root / rr.RECORDS_REL / "laptop" / "answers"
    adir.mkdir(parents=True)
    (adir / (first + ".json")).write_text(json.dumps({
        "request_id": first, "status": "applied", "role_name": "fix-role", "role_arn": "arn:aws:iam::111111111111:role/fix-role",
        "applied_at": "2026-10-07T00:00:00Z", "applied_by": "laptop", "commit": "abcdef1"}), encoding="utf-8")
    rc, out, err, _ = run(root, "dell1", ["list"])
    lines = out.strip().splitlines()
    rc2, out2, _, _ = run(root, "dell1", ["list", "--status", "applied"])
    ok = (rc == 0 and len(files) == 2 and lines[-1] == "COUNT requested=1 applied=1 refused=0 total=2"
          and any(ln.startswith(first + " applied ") for ln in lines) and len(out2.strip().splitlines()) == 2)
    return ok, lines[-1] if lines else err


CASES = [case_valid, case_unset, case_not_execution, case_other_dell, case_missing_file, case_line_past_end, case_iam, case_star,
         case_bus_line, case_list]


def main():
    passed = 0
    for fn in CASES:
        with tempfile.TemporaryDirectory() as t:
            try:
                ok, detail = fn(make_root(pathlib.Path(t)))
            except Exception as exc:   # a case that raises is a failed case, with its reason
                ok, detail = False, "EXC %s: %s" % (type(exc).__name__, exc)
        print("%s %s: %s" % ("PASS" if ok else "FAIL", fn.__name__, detail))
        passed += bool(ok)
    n = len(CASES)
    print("ROLE-REQUEST cases=%d/%d ok=%s" % (passed, n, passed == n and n == 10))
    return 0 if passed == n else 1


if __name__ == "__main__":
    sys.exit(main())
