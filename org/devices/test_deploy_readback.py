"""Cases for the deploy read-back (NFRA_CTLPLN cell CT-d-4): org/devices/deploy_readback_check.py, run on a Dell after a deploy.

Run: python org/devices/test_deploy_readback.py   (LAST line: DEPLOY-READBACK-SELFTEST cases=<k>/6 ok=<True|False>)

Nothing here touches AWS, a real remote, the live register or the live ledger. One temporary world: a local BARE git repository that
plays `origin` (branch CLOUD, plus an off-trunk branch q/dell1/X/round1 that holds the commit under test), a clone of it, a temporary
copy of the device register, and one temporary ledger root per case built by the REAL .tools/deploy_ledger.py (open, then
named_commit_check.py --record, then close-leg and close, so the entry is the layout the deploy tools write). The `--aws` command is a
small Python script this file writes: it serves object bytes and a Lambda CodeSha256 from a table and logs each call.

The deployed file holds CRLF line ends, a NUL and a 0xFF byte, so a text-mode read on either side would change its digest; the one-byte
arm flips one byte without changing the length, so a size check could not catch it.
"""
import base64
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
TOOLS = ROOT / ".tools"
SCRIPT = HERE / "deploy_readback_check.py"
NAMED = TOOLS / "named_commit_check.py"
REAL_REGISTER = ROOT / "org" / "devices" / "DEVICES.json"
SERIAL = "0.9.0_WK_NFRA_CTLPLN~7"
REPO_PATH = "app/deployed_code.bin"
BUCKET, KEY = "fixture-bucket", "code/deployed_code.bin"
CODE_BYTES = b"line one\r\nline two\r\n\x00\xff\x10 end\r\n"
FN, FN_ZIP = "fixture-fn", b"zip bytes the build produced"

FAKE_AWS = '''import base64, json, sys
table = json.load(open(sys.argv[1]))
args = sys.argv[3:]
with open(sys.argv[2], "a") as fh:
    fh.write(" ".join(args) + "\\n")
if args[:2] == ["s3api", "get-object"]:
    key = args[args.index("--bucket") + 1] + "/" + args[args.index("--key") + 1]
    if key not in table["objects"]:
        sys.stderr.write("An error occurred (NoSuchKey) when calling the GetObject operation: " + key)
        sys.exit(254)
    open(args[-1], "wb").write(base64.b64decode(table["objects"][key]))
    print("{}")
    sys.exit(0)
if args[:2] == ["lambda", "get-function"]:
    name = args[args.index("--function-name") + 1]
    if name not in table["lambdas"]:
        sys.stderr.write("An error occurred (ResourceNotFoundException) when calling GetFunction: " + name)
        sys.exit(254)
    print(table["lambdas"][name])
    sys.exit(0)
sys.stderr.write("fake aws: no answer for " + " ".join(args))
sys.exit(9)
'''


def run(argv, cwd=None, env=None):
    r = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240)
    return r.returncode, r.stdout + r.stderr


def git(repo, *args):
    rc, out = run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-c", "core.autocrlf=false", "-C", str(repo), *args])
    if rc != 0:
        raise RuntimeError("git %s failed rc=%s: %s" % (" ".join(args), rc, out))
    return out.strip()


def commit_file(repo, rel, data):
    path = Path(repo) / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    git(repo, "add", rel)
    git(repo, "commit", "-m", "add " + rel)
    return git(repo, "rev-parse", "HEAD")


def env_for(register, extra=None):
    env = dict(os.environ, OPAL_DEVICE_REGISTER=str(register), OPAL_AGENT_SERIAL=SERIAL, AGENTBUS_DEVICE="dell1",
               PYTHONIOENCODING="utf-8")
    env.pop("DEPLOY_LEDGER_SLUG", None)
    env.update(extra or {})
    return env


def make_ledger(tmp, slug, commit, register, repo, close=True):
    """A ledger entry by the real tools. commit: record this named commit (the real --record path); close: run close-leg and close."""
    root = Path(tmp) / ("ledger_" + slug)
    (root / ".tools").mkdir(parents=True)
    (root / "org" / "critical_paths" / "change_management").mkdir(parents=True)
    shutil.copy(str(TOOLS / "deploy_ledger.py"), str(root / ".tools" / "deploy_ledger.py"))
    tool = [sys.executable, str(root / ".tools" / "deploy_ledger.py")]
    rc, out = run(tool + ["open", "--slug", slug, "--title", "readback fixture", "--author", SERIAL,
                          "--leg", "L1|git|fixture|hash pushed"], cwd=str(root))
    if rc != 0:
        raise RuntimeError("deploy_ledger open rc=%s: %s" % (rc, out))
    state = json.loads((root / "org" / "critical_paths" / ".open_deploys" / (slug + ".json")).read_text(encoding="utf-8"))
    if commit:
        rc, out = run([sys.executable, str(NAMED), "check", "--commit", commit, "--repo", str(repo), "--record",
                       "--ledger-root", str(root)], env=env_for(register))
        if rc != 0:
            raise RuntimeError("named_commit_check --record rc=%s: %s" % (rc, out))
    if close:
        for argv in (["close-leg", "--slug", slug, "--leg-id", "L1", "--proof", "p"], ["close", "--slug", slug]):
            rc, out = run(tool + argv, cwd=str(root))
            if rc != 0:
                raise RuntimeError("deploy_ledger %s rc=%s: %s" % (argv[0], rc, out))
    return root / state["entry_path"]


def readback(world, commit, entry, objects, lambdas=(), aws_table=None):
    """Run the script as a subprocess; (rc, output, last line)."""
    table = world["tmp"] / "aws_table.json"
    table.write_text(json.dumps(aws_table if aws_table is not None else world["table"]), encoding="utf-8")
    calls = world["tmp"] / "aws_calls.log"
    aws = '"%s" "%s" "%s" "%s"' % (sys.executable.replace("\\", "/"), world["fake"].as_posix(), table.as_posix(), calls.as_posix())
    argv = [sys.executable, str(SCRIPT), "--repo", str(world["work"]), "--commit", commit, "--ledger", str(entry), "--aws", aws]
    for spec in objects:
        argv += ["--object", spec]
    for spec in lambdas:
        argv += ["--lambda-sha256", spec]
    rc, out = run(argv, env=env_for(world["register"]))
    lines = [ln for ln in out.strip().splitlines() if ln.strip()]
    return rc, out, (lines[-1] if lines else "NO OUTPUT")


def last_ok(last, commit, admitted, trunk, equal, ledger, ok, failed):
    pat = (r"^DEPLOY-READBACK commit=%s device=dell1 admitted=%s on_trunk=%s objects_equal=%s ledger=%s ok=%s failed=%s$"
           % (commit, admitted, trunk, re.escape(equal), ledger, ok, failed))
    return re.match(pat, last) is not None


def make_world(tmp):
    origin, work = tmp / "origin.git", tmp / "work"
    run(["git", "init", "--bare", "-q", "--initial-branch=CLOUD", str(origin)])
    run(["git", "init", "-q", "-b", "CLOUD", str(work)])
    git(work, "remote", "add", "origin", str(origin))
    commit_file(work, "trunk.txt", b"trunk\n")
    git(work, "push", "-q", "origin", "CLOUD")
    git(work, "checkout", "-q", "-b", "q/dell1/X/round1")
    c_off = commit_file(work, REPO_PATH, CODE_BYTES)
    git(work, "push", "-q", "origin", "q/dell1/X/round1")
    c_other = commit_file(work, "app/other.txt", b"another published off-trunk commit\n")
    git(work, "push", "-q", "origin", "q/dell1/X/round1")
    git(work, "checkout", "-q", "-b", "local-only", c_other)
    c_unpub = commit_file(work, "unpublished.txt", b"never pushed\n")
    register = tmp / "DEVICES.json"
    shutil.copy(str(REAL_REGISTER), str(register))
    fake = tmp / "fake_aws.py"
    fake.write_text(FAKE_AWS, encoding="utf-8", newline="\n")
    zip_b64 = base64.b64encode(hashlib.sha256(FN_ZIP).digest()).decode("ascii")
    table = {"objects": {"%s/%s" % (BUCKET, KEY): base64.b64encode(CODE_BYTES).decode("ascii")}, "lambdas": {FN: zip_b64}}
    return {"tmp": tmp, "origin": origin, "work": work, "register": register, "fake": fake, "table": table,
            "c_off": c_off, "c_other": c_other, "c_unpub": c_unpub, "zip_hex": hashlib.sha256(FN_ZIP).hexdigest()}


def case_happy(w):
    entry = make_ledger(w["tmp"], "happy", w["c_off"], w["register"], w["work"])
    spec = "%s=s3://%s/%s" % (REPO_PATH, BUCKET, KEY)
    rc, out, last = readback(w, w["c_off"], entry, [spec], ["%s=%s" % (FN, w["zip_hex"])])
    sha = hashlib.sha256(CODE_BYTES).hexdigest()
    ok = (rc == 0 and last_ok(last, w["c_off"], "True", "False", "2/2", "closed-named", "True", "none")
          and out.count(sha) >= 2 and "git_len=%d" % len(CODE_BYTES) in out and "deployed_len=%d" % len(CODE_BYTES) in out)
    # the control: the same deploy with NO object to compare cannot pass (n >= 1)
    rc0, out0, last0 = readback(w, w["c_off"], entry, [])
    ok = ok and rc0 != 0 and last_ok(last0, w["c_off"], "True", "False", "0/0", "closed-named", "False", "objects_equal")
    return ok, "%s | no-object control: %s" % (last, last0)


def case_one_byte(w):
    entry = make_ledger(w["tmp"], "onebyte", w["c_off"], w["register"], w["work"])
    flipped = bytearray(CODE_BYTES)
    flipped[5] ^= 0x01
    table = json.loads(json.dumps(w["table"]))
    table["objects"]["%s/%s" % (BUCKET, KEY)] = base64.b64encode(bytes(flipped)).decode("ascii")
    spec = "%s=s3://%s/%s" % (REPO_PATH, BUCKET, KEY)
    rc, out, last = readback(w, w["c_off"], entry, [spec], aws_table=table)
    ok = (rc != 0 and len(flipped) == len(CODE_BYTES)
          and last_ok(last, w["c_off"], "True", "False", "0/1", "closed-named", "False", "objects_equal")
          and hashlib.sha256(bytes(flipped)).hexdigest() in out and hashlib.sha256(CODE_BYTES).hexdigest() in out)
    # a Lambda whose deployed CodeSha256 is not the expected one is the same arm
    rc2, out2, last2 = readback(w, w["c_off"], entry, [spec], ["%s=%s" % (FN, "0" * 64)])
    ok = ok and rc2 != 0 and last_ok(last2, w["c_off"], "True", "False", "1/2", "closed-named", "False", "objects_equal")
    return ok, "%s | lambda control: %s" % (last, last2)


def case_on_trunk(w):
    entry = make_ledger(w["tmp"], "ontrunk", w["c_off"], w["register"], w["work"])
    spec = "%s=s3://%s/%s" % (REPO_PATH, BUCKET, KEY)
    git(w["work"], "push", "-q", "origin", "%s:refs/heads/CLOUD" % w["c_off"])   # the fast-forward another box's merge makes
    rc, out, last = readback(w, w["c_off"], entry, [spec])
    ok = rc != 0 and last_ok(last, w["c_off"], "True", "True", "1/1", "closed-named", "False", "on_trunk")
    return ok, last


def case_other_commit(w):
    entry = make_ledger(w["tmp"], "othercommit", w["c_other"], w["register"], w["work"])
    spec = "%s=s3://%s/%s" % (REPO_PATH, BUCKET, KEY)
    rc, out, last = readback(w, w["c_off"], entry, [spec])
    ok = rc != 0 and last_ok(last, w["c_off"], "True", "False", "1/1", "other-commit", "False", "ledger")
    # and a missing entry is its own value
    rc2, out2, last2 = readback(w, w["c_off"], w["tmp"] / "no_such_entry.md", [spec])
    ok = ok and rc2 != 0 and last_ok(last2, w["c_off"], "True", "False", "1/1", "missing", "False", "ledger")
    return ok, "%s | missing control: %s" % (last, last2)


def case_open(w):
    entry = make_ledger(w["tmp"], "stillopen", w["c_off"], w["register"], w["work"], close=False)
    spec = "%s=s3://%s/%s" % (REPO_PATH, BUCKET, KEY)
    rc, out, last = readback(w, w["c_off"], entry, [spec])
    ok = rc != 0 and last_ok(last, w["c_off"], "True", "False", "1/1", "open", "False", "ledger")
    return ok, last


def case_unpublished(w):
    entry = make_ledger(w["tmp"], "unpub", None, w["register"], w["work"])
    spec = "%s=s3://%s/%s" % (REPO_PATH, BUCKET, KEY)
    rc, out, last = readback(w, w["c_unpub"], entry, [spec])
    ok = (rc != 0 and last_ok(last, w["c_unpub"], "False", "Unknown", "0/1", "missing", "False", "admitted")
          and "not published" in out and "SKIPPED" in out)
    return ok, last


CASES = [case_happy, case_one_byte, case_on_trunk, case_other_commit, case_open, case_unpublished]


def main():
    passed = 0
    for fn in CASES:
        tmp = Path(tempfile.mkdtemp(prefix="deploy_readback_"))
        try:
            ok, detail = fn(make_world(tmp))
        except Exception as exc:   # a case that raises is a failed case, with its reason
            ok, detail = False, "EXC %s: %s" % (type(exc).__name__, exc)
        finally:
            shutil.rmtree(str(tmp), ignore_errors=True)
        print("%s %s: %s" % ("PASS" if ok else "FAIL", fn.__name__, detail), flush=True)
        passed += bool(ok)
    n = len(CASES)
    print("DEPLOY-READBACK-SELFTEST cases=%d/6 ok=%s" % (passed, passed == n and n == 6))
    return 0 if passed == n else 1


if __name__ == "__main__":
    sys.exit(main())
