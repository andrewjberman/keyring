#!/usr/bin/env python3
"""Cell CT-aj-2 of NFRA_CTLPLN round 20 (PRD outcome FWD-5; row NFRA_CTLPLN-D1-S8, remedy P1): a box push deploys a
deploy-scope file that an OPEN, pinned change-management entry names when the S3 bytes differ from the pinned blob, even
when that file is absent from the box's diff against origin/CLOUD (it reached CLOUD by integrate before the box push).

Run:  python .tools/tests/test_round20_pinned_entry_deploy.py
      python .tools/tests/test_round20_pinned_entry_deploy.py --negative
LAST line:  PINNED-ENTRY-DEPLOY deployed=<n> bucket_sha_equals_pin=<True|False> ok=<True|False>
            (with --negative:)  PINNED-ENTRY-NEGATIVE arms=<k>/3 ok=<True|False>

Everything is built in a temporary directory: a bare `origin`, a working repository with branch CLOUD (carrying the
pinned file, the OPEN entry and the entry markdown), a copy of the .tools/ tree in which the REAL pre-push hook
(.tools/git-hooks/pre-push-safe-deploy.sh, installed as .git/hooks/pre-push) and the REAL safe-deploy.sh run unchanged,
and a box branch box/laptop that does not carry the pinned file in its diff. The push runs with AGENTBUS_DEVICE=laptop and
a shadowing PATH whose first entry holds two stubs:
  aws      serves a LOCAL DIRECTORY (S3_DIR) as the bucket: `aws s3 cp s3://<bucket>/<key> <file>` copies from it, or fails
           with NoSuchKey. Every other aws call is logged and does nothing. No real AWS call can happen.
  python3  is the name safe-deploy.sh gives the deploy core. It is a TEST DOUBLE for safe_deploy_core.py: for each
           data/inf/scripts/gold/*.py argument it copies the working-tree file into S3_DIR (the bucket write) and logs
           DEPLOY-EXEC file=<path>. The real core is never edited and never run.
`python` (the hook's deploy-scope lister, ledger reader and seat gates) is NOT shadowed; it runs for real.
The round-19 fixture (tests/test_round19_unsigned_push.py: build of the repository, the halt-gate order, the stub
environment) is reused for the git helper, the run helper and the temporary-tree removal.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(TOOLS))
import test_round19_unsigned_push as r19  # noqa: E402  the round-19 fixture helpers (git, run, rm_tree)

SERIAL = "0.9.0_WK_NFRA_CTLPLN~113"
PINNED = "data/inf/scripts/gold/pinned_fixture.py"
UNPINNED = "data/inf/scripts/gold/unpinned_fixture.py"
ORDER_PATH = "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/FIXTURE_WORKER_ORDER.md"
OPEN_DIR = "org/critical_paths/.open_deploys"
SENTINEL = OPEN_DIR + "/pinned-fixture-entry.json"
ENTRY_MD = "org/critical_paths/change_management/pinned-fixture-entry.md"
AUDIT = "org/safe-deploy-bypass-audit.log"
PIN_BYTES = b"# pinned fixture: the bytes the OPEN entry pins\nprint('pinned v1')\n"
STALE_BYTES = b"# stale fixture: the bytes S3 holds before the push\nprint('stale v0')\n"
UNPINNED_BYTES = b"# unpinned fixture: no OPEN entry names this script\nprint('unpinned')\n"

AWS_STUB = (
    "#!/usr/bin/env bash\n"
    "# TEST DOUBLE: serves the local directory S3_DIR as the bucket. No real AWS call can happen.\n"
    "if [ \"$1\" = \"s3\" ] && [ \"$2\" = \"cp\" ]; then\n"
    "  src=\"${3#s3://}\"\n"
    "  if [ -f \"$S3_DIR/$src\" ]; then\n"
    "    cp \"$S3_DIR/$src\" \"$4\"; printf 'S3-READ %s\\n' \"$src\" >> \"$STUB_LOG\"; exit 0\n"
    "  fi\n"
    "  printf 'S3-MISS %s\\n' \"$src\" >> \"$STUB_LOG\"\n"
    "  echo 'An error occurred (NoSuchKey) when calling the GetObject operation' >&2\n"
    "  exit 1\n"
    "fi\n"
    "printf 'AWS-CALL %s\\n' \"$*\" >> \"$STUB_LOG\"\n"
    "exit 0\n"
)
CORE_STUB = (
    "#!/usr/bin/env bash\n"
    "# TEST DOUBLE for safe_deploy_core.py: copies each named data/inf gold script from the working tree into S3_DIR.\n"
    "case \"$*\" in\n"
    "  *safe_deploy_core.py*)\n"
    "    for a in \"$@\"; do\n"
    "      case \"$a\" in\n"
    "        data/inf/scripts/gold/*.py)\n"
    "          mkdir -p \"$S3_DIR/opal-data-inf/code/gold\"\n"
    "          cp \"$a\" \"$S3_DIR/opal-data-inf/code/gold/$(basename \"$a\")\"\n"
    "          printf 'DEPLOY-EXEC file=%s\\n' \"$a\" >> \"$STUB_LOG\" ;;\n"
    "      esac\n"
    "    done ;;\n"
    "  *) printf 'OTHER-CALL %s\\n' \"$*\" >> \"$STUB_LOG\" ;;\n"
    "esac\n"
    "exit 0\n"
)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def sentinel_text(status, blob):
    return json.dumps({"slug": "pinned-fixture-entry", "title": "FIXTURE OPEN pinned entry (round-20 test)",
                       "status": status, "entry_path": ENTRY_MD, "pins": {PINNED: blob}}, indent=2) + "\n"


def build(tmp, sentinel_status, bucket_bytes, box_extra):
    """The origin, the CLOUD trunk (pinned file, order, entry), the real hook installed, and the box branch carrying a
    README change plus box_extra {path: bytes}. The S3 directory holds bucket_bytes for the pinned key, if not None.
    Returns (origin, work, box_sha, s3_dir)."""
    origin = tmp / "origin.git"
    work = tmp / "work"
    s3_dir = tmp / "s3"
    r19.run(["git", "init", "-q", "--bare", str(origin)])
    r19.run(["git", "init", "-q", "-b", "CLOUD", str(work)])
    r19.git(work, "config", "core.autocrlf", "false")
    r19.git(work, "remote", "add", "origin", str(origin))
    shutil.copytree(str(TOOLS), str(work / ".tools"),
                    ignore=shutil.ignore_patterns("tests", "__pycache__", "*.pyc"))
    (work / "org").mkdir()
    order = work / ORDER_PATH
    order.parent.mkdir(parents=True)
    order.write_text("<issued_to>%s</issued_to>\n<issued_by>2.0.0_SA_COO~C</issued_by>\n<status>open</status>\n"
                     % SERIAL, encoding="utf-8")
    pinned = work / PINNED
    pinned.parent.mkdir(parents=True)
    pinned.write_bytes(PIN_BYTES)
    r19.git(work, "add", "-A")
    r19.git(work, "commit", "-q", "-m", "base: the trunk with the real .tools tree, the fixture order and the pinned file")
    blob = r19.git(work, "rev-parse", "HEAD:" + PINNED)
    # the OPEN (or CLOSED) entry and its markdown reach CLOUD in the same trunk commit, before the box branch is cut
    (work / OPEN_DIR).mkdir(parents=True, exist_ok=True)
    (work / SENTINEL).write_text(sentinel_text(sentinel_status, blob), encoding="utf-8")
    (work / ENTRY_MD).parent.mkdir(parents=True)
    (work / ENTRY_MD).write_text("# FIXTURE change-management entry\n\nPins %s at blob %s.\n" % (PINNED, blob),
                                 encoding="utf-8")
    r19.git(work, "add", "-A")
    r19.git(work, "commit", "-q", "-m", "fixture: the entry naming the pinned file reaches CLOUD")
    r19.git(work, "push", "-q", "origin", "CLOUD")
    hooks = work / ".git" / "hooks"
    hooks.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(str(work / ".tools" / "git-hooks" / "pre-push-safe-deploy.sh"), str(hooks / "pre-push"))
    r19.git(work, "checkout", "-q", "-b", "box/laptop")
    (work / "README.md").write_text("box work: no deploy-scope file\n", encoding="utf-8")
    for rel, data in (box_extra or {}).items():
        (work / rel).parent.mkdir(parents=True, exist_ok=True)
        (work / rel).write_bytes(data)
    r19.git(work, "add", "-A")
    r19.git(work, "commit", "-q", "-m", "box/laptop: a README change and the box's own files")
    box = r19.git(work, "rev-parse", "HEAD")
    s3_dir.mkdir()
    if bucket_bytes is not None:
        (s3_dir / "opal-data-inf" / "code" / "gold").mkdir(parents=True)
        (s3_dir / "opal-data-inf" / "code" / "gold" / "pinned_fixture.py").write_bytes(bucket_bytes)
    return origin, work, box, s3_dir


def make_stubs(tmp):
    stubs = tmp / "stubs"
    stubs.mkdir()
    for name, body in (("aws", AWS_STUB), ("python3", CORE_STUB)):
        p = stubs / name
        p.write_text(body, encoding="utf-8", newline="\n")
        os.chmod(str(p), 0o755)
    return stubs


def stub_env(stubs, log, s3_dir):
    env = dict(os.environ)
    env["PATH"] = str(stubs) + os.pathsep + env.get("PATH", "")
    env["AGENTBUS_DEVICE"] = "laptop"
    env["OPAL_AGENT_SERIAL"] = SERIAL
    env["STUB_LOG"] = log.as_posix()
    env["S3_DIR"] = s3_dir.as_posix()
    env.pop("DEPLOY_COMMIT", None)
    return env


def push_case(tmp, sentinel_status, bucket_bytes, box_extra, verbose):
    """Build one case, push box/laptop through the real hook, and read the stub log, the bucket and the audit log.
    Returns a dict of the measured values."""
    origin, work, box, s3_dir = build(tmp, sentinel_status, bucket_bytes, box_extra)
    stubs = make_stubs(tmp)
    log = tmp / "stub.log"
    env = stub_env(stubs, log, s3_dir)
    push_rc, push_out = r19.run(["git", "-C", str(work), "push", "origin", "box/laptop"], env=env)
    if verbose:
        print("PUSH rc=%d" % push_rc)
        for ln in push_out.splitlines():
            print("PUSH | " + ln)
    ls = r19.git(work, "ls-remote", "origin", "refs/heads/box/laptop")
    landed = ls.split()[:1] == [box]
    lines = r19.log_lines(log)
    deployed_files = [ln[len("DEPLOY-EXEC file="):] for ln in lines if ln.startswith("DEPLOY-EXEC file=")]
    audit_path = work / AUDIT
    audit = audit_path.read_text(encoding="utf-8").splitlines() if audit_path.exists() else []
    blob = r19.git(work, "rev-parse", "HEAD~1:" + PINNED)
    # the raw bytes of the pinned blob (r19.git strips the trailing newline, so it is not used for content)
    pin_data = subprocess.run(["git", "-C", str(work), "cat-file", "blob", blob], capture_output=True).stdout
    bucket_file = s3_dir / "opal-data-inf" / "code" / "gold" / "pinned_fixture.py"
    bucket_sha = sha(bucket_file.read_bytes()) if bucket_file.exists() else None
    if verbose:
        for ln in lines:
            print("STUB | " + ln)
        for ln in audit:
            if "HELD-DEPLOY" in ln or "PINNED-DEPLOY" in ln:
                print("AUDIT | " + ln)
    return {"push_rc": push_rc, "landed": landed, "deployed": len(deployed_files), "deployed_files": deployed_files,
            "pin_sha": sha(pin_data), "bucket_sha": bucket_sha,
            "s3_reads": sum(1 for ln in lines if ln.startswith("S3-READ ")),
            "held": sum(1 for ln in audit if "HELD-DEPLOY" in ln and ("path=" + UNPINNED) in ln),
            "held_reason": any("reason=no-open-ledger-names-it" in ln and ("path=" + UNPINNED) in ln for ln in audit)}


def main_positive():
    tmp = Path(tempfile.mkdtemp(prefix="round20_pinned_"))
    try:
        r = push_case(tmp, "OPEN", STALE_BYTES, None, verbose=True)
        bucket_eq = r["bucket_sha"] is not None and r["bucket_sha"] == r["pin_sha"]
        ok = r["push_rc"] == 0 and r["landed"] and r["deployed"] == 1 and bucket_eq
        print("PINNED-ENTRY-DEPLOY deployed=%d bucket_sha_equals_pin=%s ok=%s" % (r["deployed"], bucket_eq, ok))
        return 0 if ok else 1
    finally:
        r19.rm_tree(tmp)


def main_negative():
    arms = []
    specs = [
        # (a) equal bytes: the OPEN pin matches S3, so nothing is deployed
        ("a-equal-bytes", dict(sentinel_status="OPEN", bucket_bytes=PIN_BYTES, box_extra=None)),
        # (b) an UNPINNED deploy-scope file in the push: nothing deployed, the file held (the round-19 arm)
        ("b-unpinned-file", dict(sentinel_status="OPEN", bucket_bytes=PIN_BYTES,
                                 box_extra={UNPINNED: UNPINNED_BYTES})),
        # (c) a CLOSED entry: it authorizes nothing, so the stale bytes are not deployed
        ("c-closed-entry", dict(sentinel_status="CLOSED", bucket_bytes=STALE_BYTES, box_extra=None)),
    ]
    for name, kw in specs:
        tmp = Path(tempfile.mkdtemp(prefix="round20_neg_%s_" % name[0]))
        try:
            r = push_case(tmp, kw["sentinel_status"], kw["bucket_bytes"], kw["box_extra"], verbose=False)
            if name.startswith("a"):
                ok = r["push_rc"] == 0 and r["landed"] and r["deployed"] == 0 and r["bucket_sha"] == r["pin_sha"]
            elif name.startswith("b"):
                ok = (r["push_rc"] == 0 and r["landed"] and r["deployed"] == 0 and r["held"] == 1
                      and r["held_reason"] and r["bucket_sha"] == r["pin_sha"])
            else:
                ok = (r["push_rc"] == 0 and r["landed"] and r["deployed"] == 0
                      and r["bucket_sha"] != r["pin_sha"])
            arms.append(ok)
            print("PINNED-ENTRY-ARM %s ok=%s push_rc=%d deployed=%d held=%d s3_reads=%d bucket_sha_equals_pin=%s"
                  % (name, ok, r["push_rc"], r["deployed"], r["held"], r["s3_reads"],
                     r["bucket_sha"] is not None and r["bucket_sha"] == r["pin_sha"]))
        finally:
            r19.rm_tree(tmp)
    k = sum(1 for a in arms if a)
    print("PINNED-ENTRY-NEGATIVE arms=%d/3 ok=%s" % (k, k == 3))
    return 0 if k == 3 else 1


if __name__ == "__main__":
    sys.exit(main_negative() if "--negative" in sys.argv[1:] else main_positive())
