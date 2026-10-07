"""role_roundtrip_check.py -- the round trip a Dell runs: write in, wait for the laptop's answer, create with the role (NFRA_CTLPLN cell CT-c-4).

PRD v0.8 C-ROLE-REQUEST (c): one exercised round trip -- a Dell writes in, the laptop applies, the Dell creates a function with that role,
a pass of an unnamed role is refused. This script is the Dell's half. It creates ONE Lambda function, deletes nothing (a Dell holds no
delete), and never changes access: the one IAM call it makes is an attempt that is EXPECTED to be refused.

    AGENTBUS_DEVICE=dell1 python org/devices/role_roundtrip_check.py --project <CODE> --root <dir under infra/aws/terraform/>
        --function-name <name> --unnamed-role-arn <arn of a role the Dell policy does not name> [--wait-seconds 1800] [--poll-seconds 30]
        [--aws <the AWS command; default the repo's .tools/aws shim>]

Steps, each printed as one line:
  1 write the request (role_request.py write, kind aws_lambda_function, service lambda.amazonaws.com, one logs:CreateLogStream permission)
  2 poll `git fetch` + `git show origin/CLOUD:org/devices/role_requests/<laptop>/answers/<request_id>.json` until an answer or the wait ends
  3 lambda create-function with the answered role, then lambda get-function to read it back
  4 lambda create-function for <name>-unnamed with --unnamed-role-arn: EXPECTED an AccessDenied on iam:PassRole
  5 iam tag-role on the answered role: EXPECTED AccessDenied
LAST line: ROLE-ROUNDTRIP request=<id> answered=<applied|refused|timeout> create=<ok|fail> unnamed_pass=<refused|ALLOWED|error>
           iam_write=<refused|ALLOWED|error> ok=<True|False>
A step that did not run (no answer, so no role) reports create=fail unnamed_pass=error iam_write=error. A failed write (no request id) and an
answer that does not hold the answer shape report answered=timeout and answered=refused respectively, with the reason on the line above.

Run from the repo checkout it lives in; the repo root is derived from this file's path. No bus send of its own: the request's bus line is
role_request.py's.
"""
from __future__ import annotations

import argparse
import contextlib
import importlib.util
import inspect
import io
import json
import pathlib
import re
import shlex
import subprocess
import sys
import tempfile
import time
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
REMOTE_REF = "origin/CLOUD"
HANDLER_SRC = "\n".join([
    "import json",
    "",
    "",
    "def handler(event, context):",
    "    # the round trip's probe: it answers and does nothing else",
    "    body = {'probe': 'role-roundtrip', 'ok': True}",
    "    print(json.dumps(body))",
    "    return body",
    "",
]) + "\n"


def _load_role_request():
    spec = importlib.util.spec_from_file_location("role_request_for_roundtrip", str(HERE / "role_request.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def step(n: int, what: str, result: str) -> None:
    print("STEP %d %s: %s" % (n, what, result), flush=True)


def run_cmd(argv: list, timeout: int = 120):
    """(rc, combined output) of one command; a timeout or a missing executable is rc 124 / 127 with the reason as output."""
    try:
        r = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
        return r.returncode, (r.stdout + r.stderr).strip()
    except subprocess.TimeoutExpired:
        return 124, "timeout after %ss: %s" % (timeout, " ".join(argv[:3]))
    except OSError as exc:
        return 127, "cannot run %s: %s" % (argv[0], exc)


def aws_argv(aws_arg, root: pathlib.Path) -> list:
    """The AWS command as an argv list: --aws (shell-split) when given, else the repo's .tools/aws shim through Git Bash."""
    if aws_arg:
        return shlex.split(aws_arg)
    sys.path.insert(0, str(root / ".tools"))
    import git_bash_resolver
    return git_bash_resolver.bash_argv(str(root / ".tools" / "aws"))


def zip_file(directory: pathlib.Path) -> pathlib.Path:
    path = directory / "probe.zip"
    with zipfile.ZipFile(str(path), "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("index.py", HANDLER_SRC)
    return path


def classify_refusal(rc: int, out: str, needle: str = "") -> str:
    """refused = the call failed with AccessDenied (and, when given, the named action); ALLOWED = the call succeeded; error = anything else."""
    if rc == 0:
        return "ALLOWED"
    if "AccessDenied" in out and (not needle or needle in out):
        return "refused"
    return "error"


def poll_answer(root: pathlib.Path, laptop: str, rid: str, wait: float, poll: float, rr):
    """(state, answer or None, detail). state: applied | refused | timeout. One fetch-and-read at least, then one per poll until `wait`."""
    rel = "%s/%s/answers/%s.json" % (rr.RECORDS_REL, laptop, rid)
    deadline = time.monotonic() + wait
    last = "no fetch yet"
    while True:
        rc, out = run_cmd(["git", "-C", str(root), "fetch", "--quiet", "origin"])
        if rc != 0:
            last = "git fetch rc=%s: %s" % (rc, out[:200])
        else:
            rc, out = run_cmd(["git", "-C", str(root), "show", "%s:%s" % (REMOTE_REF, rel)])
            if rc == 0:
                try:
                    ans = json.loads(out)
                except ValueError as exc:
                    return "refused", None, "the answer is not JSON: %s" % exc
                errs = rr.shape_errors(ans, "answer")
                if errs or ans.get("request_id") != rid:
                    return "refused", None, "the answer does not hold the answer shape or answers another request: %s" % "; ".join(errs[:3])
                if ans["status"] == "applied" and not rr.ROLE_ARN_RE.match(ans["role_arn"]):
                    return "refused", None, "the answer's role_arn %r is not a literal role in the account" % ans["role_arn"]
                return ans["status"], ans, "%s:%s" % (REMOTE_REF, rel)
            last = "no answer file at %s:%s yet" % (REMOTE_REF, rel)
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return "timeout", None, last
        time.sleep(min(poll, remaining))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="role_roundtrip_check.py", description=__doc__.splitlines()[0])
    ap.add_argument("--project", required=True)
    ap.add_argument("--root", required=True, help="the Terraform root, under infra/aws/terraform/ (passed to role_request.py write)")
    ap.add_argument("--function-name", required=True)
    ap.add_argument("--unnamed-role-arn", required=True)
    ap.add_argument("--wait-seconds", type=float, default=1800)
    ap.add_argument("--poll-seconds", type=float, default=30)
    ap.add_argument("--aws", default=None, help="the AWS command (default: the repo's .tools/aws shim)")
    a = ap.parse_args(argv)
    rr = _load_role_request()
    fn, fn_unnamed = a.function_name, a.function_name + "-unnamed"
    region = "us-east-1"
    names = "LAPTOP-REMOVES function %s ; function %s" % (fn, fn_unnamed)
    state = {"answered": "timeout", "create": "fail", "unnamed": "error", "iam": "error"}
    rid = "none"

    def finish() -> int:
        ok = state["answered"] == "applied" and state["create"] == "ok" and state["unnamed"] == "refused" and state["iam"] == "refused"
        print(names, flush=True)
        print("ROLE-ROUNDTRIP request=%s answered=%s create=%s unnamed_pass=%s iam_write=%s ok=%s"
              % (rid, state["answered"], state["create"], state["unnamed"], state["iam"], ok))
        return 0 if ok else 1

    # (1) write the request
    code_ref = "%s:%d" % ((pathlib.Path(__file__).resolve().relative_to(ROOT).as_posix() if pathlib.Path(__file__).resolve().is_relative_to(ROOT)
                           else "org/devices/role_roundtrip_check.py"), inspect.currentframe().f_lineno)
    log_arn = "arn:aws:logs:%s:%s:log-group:/aws/lambda/%s:*" % (region, rr.ACCOUNT, fn)
    wargs = ["write", "--project", a.project, "--root", a.root, "--kind", "aws_lambda_function", "--name", fn,
             "--service", "lambda.amazonaws.com", "--permission", "logs:CreateLogStream,%s,%s" % (log_arn, code_ref)]
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        wrc = rr.main(wargs, root=ROOT)
    m = re.search(r"^ROLE-REQUEST (\S+) ", out.getvalue(), re.M)
    if wrc != 0 or not m:
        step(1, "write the request", "FAIL rc=%s %s" % (wrc, (err.getvalue().strip() or out.getvalue().strip())[:300]))
        return finish()
    rid = m.group(1)
    step(1, "write the request", "OK request_id=%s" % rid)

    # (2) poll for the laptop's answer
    reg = rr.load_register(ROOT)
    laptop = next((d["name"] for d in reg["devices"] if d.get("role") == "control-plane"), None)
    if laptop is None:
        step(2, "wait for the answer", "FAIL the register holds no control-plane box")
        return finish()
    answered, ans, detail = poll_answer(ROOT, laptop, rid, a.wait_seconds, a.poll_seconds, rr)
    state["answered"] = answered
    step(2, "wait for the answer", "%s (%s)" % (answered, detail))
    if answered != "applied":
        return finish()
    role_arn, role_name = ans["role_arn"], ans["role_name"]

    aws = aws_argv(a.aws, ROOT)
    with tempfile.TemporaryDirectory() as td:
        zpath = zip_file(pathlib.Path(td)).as_posix()

        def create(name: str, role: str) -> list:
            return aws + ["lambda", "create-function", "--region", region, "--function-name", name, "--runtime", "python3.12",
                          "--role", role, "--handler", "index.handler", "--zip-file", "fileb://" + zpath]

        # (3) create with the answered role, read it back
        rc, out3 = run_cmd(create(fn, role_arn))
        rc2, out3b = run_cmd(aws + ["lambda", "get-function", "--region", region, "--function-name", fn]) if rc == 0 else (1, "not read: create failed")
        state["create"] = "ok" if rc == 0 and rc2 == 0 and fn in out3b else "fail"
        step(3, "create %s with %s" % (fn, role_name), "%s (create rc=%s, get-function rc=%s) %s" % (state["create"], rc, rc2, (out3 if rc else out3b)[:160]))
        # (4) a pass of an unnamed role: EXPECTED an AccessDenied on iam:PassRole
        rc, out4 = run_cmd(create(fn_unnamed, a.unnamed_role_arn))
        state["unnamed"] = classify_refusal(rc, out4, "iam:PassRole")
        step(4, "create %s with the unnamed role" % fn_unnamed, "%s (rc=%s) %s" % (state["unnamed"], rc, out4[:160]))
    # (5) one IAM write attempt: EXPECTED an AccessDenied
    rc, out5 = run_cmd(aws + ["iam", "tag-role", "--role-name", role_name, "--tags", "Key=roundtrip,Value=%s" % rid])
    state["iam"] = classify_refusal(rc, out5)
    step(5, "iam tag-role on %s" % role_name, "%s (rc=%s) %s" % (state["iam"], rc, out5[:160]))
    return finish()


if __name__ == "__main__":
    sys.exit(main())
