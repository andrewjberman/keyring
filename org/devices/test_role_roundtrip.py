"""Cases for the round trip (NFRA_CTLPLN cell CT-c-4): org/devices/role_roundtrip_check.py (a Dell) and the answer verbs in role_request.py.

Run: python org/devices/test_role_roundtrip.py   (LAST line: ROLE-ROUNDTRIP-SELFTEST cases=<k>/7 ok=<True|False>)

Nothing here touches AWS, the live bus, a real remote, the live org/devices/DEVICES.json or the live records directory. Every case builds a
temporary world: a local BARE git repository that plays `origin` (branch CLOUD), a Dell clone and a laptop clone of it, each carrying a copy of the
scripts, the schema, the register and a fixture project placed on DELL1. The Dell clone's .tools/agentbus-sqs.sh is a fake that appends to a
file. The `--aws` command is a small Python script this file writes: it answers each call from a table and logs the call.

The Dell's script runs as a real subprocess (its own command line); this process plays the laptop in-process, writes the answer through
role_request.py's own verbs, commits it and pushes it to the bare repository, so the Dell's `git fetch` reads a real ref.
"""
import contextlib
import importlib.util
import io
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
spec = importlib.util.spec_from_file_location("role_request_under_test", str(HERE / "role_request.py"))
rr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rr)

SERIAL = "0.9.0_WK_FIXTURE~1"
GOOD_ARN = "arn:aws:iam::313476888478:role/fix-probe-role"
UNNAMED_ARN = "arn:aws:iam::313476888478:role/fix-unnamed-role"
GIT = ["git", "-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid", "-c", "core.autocrlf=false"]

FAKE_AWS = '''import json, sys
table = json.load(open(sys.argv[1]))
log = sys.argv[2]
args = sys.argv[3:]
op = " ".join(args[:2])
key = op
if op == "lambda create-function":
    name = args[args.index("--function-name") + 1]
    key = op + (":unnamed" if name.endswith("-unnamed") else ":named")
with open(log, "a") as fh:
    fh.write(" ".join(args) + "\\n")
ans = table.get(key, {"rc": 9, "out": "", "err": "fake aws: no table row for " + key})
sys.stdout.write(ans.get("out", ""))
sys.stderr.write(ans.get("err", ""))
sys.exit(ans.get("rc", 0))
'''

DENIED_PASS = {"rc": 254, "out": "", "err": "An error occurred (AccessDeniedException) when calling the CreateFunction operation: "
                                             "User is not authorized to perform: iam:PassRole on resource: " + UNNAMED_ARN}
DENIED_TAG = {"rc": 254, "out": "", "err": "An error occurred (AccessDenied) when calling the TagRole operation: not authorized to perform iam:TagRole"}


def table_ok():
    return {
        "lambda create-function:named": {"rc": 0, "out": json.dumps({"FunctionName": "fix-probe"})},
        "lambda get-function": {"rc": 0, "out": json.dumps({"Configuration": {"FunctionName": "fix-probe", "Role": GOOD_ARN}})},
        "lambda create-function:unnamed": dict(DENIED_PASS),
        "iam tag-role": dict(DENIED_TAG),
    }


def git(cwd, *args):
    r = subprocess.run(GIT + list(args), cwd=str(cwd), capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    if r.returncode != 0:
        raise RuntimeError("git %s failed rc=%s: %s" % (" ".join(args), r.returncode, (r.stdout + r.stderr).strip()))
    return r.stdout


def put(path: pathlib.Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def make_world(tmp: pathlib.Path):
    """(dell clone, laptop clone, fake aws argv string, calls log, table path) over a local bare origin on branch CLOUD."""
    seed, bare = tmp / "seed", tmp / "origin.git"
    seed.mkdir()
    for rel in ("org/devices/role_request.py", "org/devices/role_roundtrip_check.py", "org/standards/ROLE_REQUEST.schema.json",
                "org/devices/DEVICES.json", ".tools/git_bash_resolver.py"):
        (seed / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(str(ROOT / rel), str(seed / rel))
    put(seed / "org/missions/D0/FIX/FIXD1/project.json", json.dumps({"project_code": "FIXD1", "placement": "DELL1"}))
    put(seed / "infra/aws/terraform/fixroot/main.tf", "# fixture\n")
    put(seed / ".tools/agentbus-sqs.sh", '#!/usr/bin/env bash\necho "$@" >> "$(dirname "$0")/sent.log"\n')
    git(tmp, "init", "--quiet", "--bare", "--initial-branch=CLOUD", str(bare))
    git(seed, "init", "--quiet", "--initial-branch=CLOUD")
    git(seed, "add", "-A")
    git(seed, "commit", "--quiet", "-m", "fixture")
    git(seed, "push", "--quiet", str(bare), "CLOUD")
    dell, laptop = tmp / "dell", tmp / "laptop"
    git(tmp, "clone", "--quiet", str(bare), str(dell))
    git(tmp, "clone", "--quiet", str(bare), str(laptop))
    fake = tmp / "fake_aws.py"
    put(fake, FAKE_AWS)
    table, calls = tmp / "table.json", tmp / "aws_calls.log"
    aws = '"%s" "%s" "%s" "%s"' % (sys.executable.replace("\\", "/"), fake.as_posix(), table.as_posix(), calls.as_posix())
    return dell, laptop, aws, calls, table


@contextlib.contextmanager
def as_device(device, serial=SERIAL):
    saved = {k: os.environ.get(k) for k in ("AGENTBUS_DEVICE", "OPAL_AGENT_SERIAL", "OPAL_DEVICE_REGISTER")}
    os.environ.pop("OPAL_DEVICE_REGISTER", None)
    os.environ["OPAL_AGENT_SERIAL"] = serial
    os.environ["AGENTBUS_DEVICE"] = device
    try:
        yield
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def answer_verb(laptop, device, args):
    """Run a role_request.py verb in-process against the laptop clone as `device`; (rc, stdout, stderr)."""
    out, err = io.StringIO(), io.StringIO()
    with as_device(device), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            rc = rr.main(args, root=laptop)
        except SystemExit as exc:
            rc = exc.code if isinstance(exc.code, int) else 2
    return rc, out.getvalue(), err.getvalue()


def publish_answer(laptop, record_file, verb_args):
    """The laptop's side: write the answer through the verb, commit it, push it to origin/CLOUD. Returns (rc, stderr)."""
    rc, out, err = answer_verb(laptop, "laptop", [verb_args[0], str(record_file)] + verb_args[1:])
    if rc != 0:
        return rc, err
    git(laptop, "add", "-A")
    git(laptop, "commit", "--quiet", "-m", "answer")
    git(laptop, "push", "--quiet", "origin", "HEAD:CLOUD")
    return 0, ""


def roundtrip(tmp, table, laptop_verb, wait):
    """Run the Dell's script as a subprocess against a fresh world. laptop_verb: None (the laptop never answers) or the verb args
    (['mark-applied', '--role-arn', ..., '--commit', ...]) the laptop runs once the Dell's record exists.
    Returns (last line, full output, aws calls, laptop publish note)."""
    dell, laptop, aws, calls, table_path = make_world(tmp)
    table_path.write_text(json.dumps(table), encoding="utf-8")
    env = dict(os.environ)
    env.pop("OPAL_DEVICE_REGISTER", None)
    env.update({"AGENTBUS_DEVICE": "dell1", "OPAL_AGENT_SERIAL": SERIAL, "PYTHONIOENCODING": "utf-8"})
    cmd = [sys.executable, str(dell / "org/devices/role_roundtrip_check.py"), "--project", "FIXD1", "--root", "fixroot",
           "--function-name", "fix-probe", "--unnamed-role-arn", UNNAMED_ARN, "--wait-seconds", str(wait), "--poll-seconds", "0.3", "--aws", aws]
    proc = subprocess.Popen(cmd, cwd=str(tmp), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
    note = "no answer by design"
    try:
        if laptop_verb is not None:
            rec_dir = dell / "org/devices/role_requests/dell1"
            deadline = time.monotonic() + 40
            files = []
            while time.monotonic() < deadline and proc.poll() is None:
                files = sorted(rec_dir.glob("*.json")) if rec_dir.is_dir() else []
                if files:
                    break
                time.sleep(0.1)
            if not files:
                note = "the Dell wrote no record"
            else:
                rc, err = publish_answer(laptop, files[0], laptop_verb)
                note = "laptop %s rc=%s %s" % (laptop_verb[0], rc, err.strip()[:120])
        out, _ = proc.communicate(timeout=90)
    except Exception:
        proc.kill()
        proc.communicate()
        raise
    lines = [ln for ln in out.strip().splitlines() if ln.strip()]
    sent = (dell / ".tools/sent.log")
    note += " | bus lines sent by the Dell: %d" % (len(sent.read_text(encoding="utf-8").splitlines()) if sent.exists() else 0)
    calls_text = calls.read_text(encoding="utf-8") if calls.exists() else ""
    return (lines[-1] if lines else "NO OUTPUT"), out, calls_text, note


def last_matches(last, answered, create, unnamed, iam, ok):
    pat = r"^ROLE-ROUNDTRIP request=(\S+) answered=%s create=%s unnamed_pass=%s iam_write=%s ok=%s$" % (answered, create, unnamed, iam, ok)
    return re.match(pat, last) is not None


APPLY = ["mark-applied", "--role-arn", GOOD_ARN, "--commit", "abcdef1"]


def case_happy(tmp):
    last, out, calls, note = roundtrip(tmp, table_ok(), APPLY, 20)
    order = [ln.split(" ")[0] + " " + ln.split(" ")[1] for ln in calls.splitlines()]
    ok = (last_matches(last, "applied", "ok", "refused", "refused", "True")
          and order == ["lambda create-function", "lambda get-function", "lambda create-function", "iam tag-role"]
          and "delete" not in calls and "-unnamed" in out and "LAPTOP-REMOVES function fix-probe ; function fix-probe-unnamed" in out)
    return ok, "%s | calls=%s | %s" % (last, order, note)


def case_refused(tmp):
    last, out, calls, note = roundtrip(tmp, table_ok(), ["mark-refused", "--reason", "fixture: not this one"], 20)
    ok = last_matches(last, "refused", "fail", "error", "error", "False") and calls == ""
    return ok, "%s | aws calls=%d | %s" % (last, len(calls.splitlines()), note)


def case_timeout(tmp):
    t0 = time.monotonic()
    last, out, calls, note = roundtrip(tmp, table_ok(), None, 2)
    ok = last_matches(last, "timeout", "fail", "error", "error", "False") and calls == "" and time.monotonic() - t0 < 60
    return ok, "%s | aws calls=%d | %s" % (last, len(calls.splitlines()), note)


def case_unnamed_allowed(tmp):
    table = table_ok()
    table["lambda create-function:unnamed"] = {"rc": 0, "out": json.dumps({"FunctionName": "fix-probe-unnamed"})}
    last, out, calls, note = roundtrip(tmp, table, APPLY, 20)
    ok = last_matches(last, "applied", "ok", "ALLOWED", "refused", "False")
    return ok, "%s | %s" % (last, note)


def case_iam_allowed(tmp):
    table = table_ok()
    table["iam tag-role"] = {"rc": 0, "out": ""}
    last, out, calls, note = roundtrip(tmp, table, APPLY, 20)
    ok = last_matches(last, "applied", "ok", "refused", "ALLOWED", "False")
    return ok, "%s | %s" % (last, note)


def fixture_record(laptop):
    """A valid request record by hand (the shape is the schema's), in the Dell's per-box directory of the laptop clone."""
    rid = "dell1-20261007T000000Z-abcd"
    rec = {"request_id": rid, "device": "dell1", "tailnet_name": "dell1", "requested_by": SERIAL, "requested_at": "2026-10-07T00:00:00Z",
           "project": "FIXD1", "terraform_root": "infra/aws/terraform/fixroot", "resource": {"kind": "aws_lambda_function", "name": "fix-probe"},
           "assuming_service": "lambda.amazonaws.com", "status": "requested",
           "permissions": [{"action": "logs:CreateLogStream", "resource_arn": "arn:aws:logs:us-east-1:313476888478:log-group:/aws/lambda/fix-probe:*",
                            "code_ref": "org/devices/role_roundtrip_check.py:1"}]}
    path = laptop / "org/devices/role_requests/dell1" / (rid + ".json")
    put(path, json.dumps(rec, indent=2) + "\n")
    return path, rid


def answers_in(laptop):
    return sorted((laptop / "org/devices/role_requests").glob("*/answers/*.json"))


def case_dell_cannot_answer(tmp):
    dell, laptop, aws, calls, table = make_world(tmp)
    path, rid = fixture_record(laptop)
    before = path.read_bytes()
    rc, out, err = answer_verb(laptop, "dell1", ["mark-applied", str(path), "--role-arn", GOOD_ARN, "--commit", "abcdef1"])
    refused_ok = rc != 0 and "only the `control-plane` box answers" in err and not answers_in(laptop)
    # the control: the same call as the laptop is accepted, writes ONE file in the laptop's own directory and leaves the Dell's record alone
    rc2, out2, err2 = answer_verb(laptop, "laptop", ["mark-applied", str(path), "--role-arn", GOOD_ARN, "--commit", "abcdef1"])
    files = answers_in(laptop)
    doc = json.loads(files[0].read_text(encoding="utf-8")) if files else {}
    ctl_ok = (rc2 == 0 and [f.relative_to(laptop).as_posix() for f in files] == ["org/devices/role_requests/laptop/answers/%s.json" % rid]
              and doc.get("status") == "applied" and doc.get("role_arn") == GOOD_ARN and doc.get("role_name") == "fix-probe-role"
              and not rr.shape_errors(doc, "answer") and path.read_bytes() == before
              and rr.effective_status(laptop / "org/devices/role_requests", rid) == "applied")
    return refused_ok and ctl_ok, "dell rc=%s err=%s | laptop rc=%s files=%d" % (rc, err.strip()[:90], rc2, len(files))


def case_wildcard_arn(tmp):
    dell, laptop, aws, calls, table = make_world(tmp)
    path, rid = fixture_record(laptop)
    bad = ["arn:aws:iam::313476888478:role/*", "arn:aws:iam::313476888478:role/fix-*", "arn:aws:iam::111111111111:role/fix-probe-role",
           "arn:aws:iam::313476888478:role/some/path/fix-probe-role", "arn:aws:iam::313476888478:role/"]
    results = []
    for arn in bad:
        rc, out, err = answer_verb(laptop, "laptop", ["mark-applied", str(path), "--role-arn", arn, "--commit", "abcdef1"])
        results.append(rc != 0 and "literal role name" in err)
    none_written = not answers_in(laptop)
    rc2, _, err2 = answer_verb(laptop, "laptop", ["mark-applied", str(path), "--role-arn", GOOD_ARN, "--commit", "abcdef1"])   # the control
    ok = all(results) and none_written and rc2 == 0 and len(answers_in(laptop)) == 1
    return ok, "refused=%s none_written=%s control rc=%s %s" % (results, none_written, rc2, err2.strip()[:80])


CASES = [case_happy, case_refused, case_timeout, case_unnamed_allowed, case_iam_allowed, case_dell_cannot_answer, case_wildcard_arn]


def main():
    passed = 0
    for fn in CASES:
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as t:
            try:
                ok, detail = fn(pathlib.Path(t))
            except Exception as exc:   # a case that raises is a failed case, with its reason
                ok, detail = False, "EXC %s: %s" % (type(exc).__name__, exc)
        print("%s %s: %s" % ("PASS" if ok else "FAIL", fn.__name__, detail), flush=True)
        passed += bool(ok)
    n = len(CASES)
    print("ROLE-ROUNDTRIP-SELFTEST cases=%d/%d ok=%s" % (passed, n, passed == n and n == 7))
    return 0 if passed == n else 1


if __name__ == "__main__":
    sys.exit(main())
