#!/usr/bin/env python3
"""Cell CT-ai-3 of NFRA_CTLPLN round 19 (PRD outcome FWD-5): a box push carrying a pipeline script that no OPEN
change-management ledger names goes through, deploys nothing, and holds the script on the record.

Run:  python .tools/tests/test_round19_unsigned_push.py
      python .tools/tests/test_round19_unsigned_push.py --stub-control
LAST line:  UNSIGNED-PUSH push_rc=<rc> deployed=<n> held=<n> ok=<True|False>
            (with --stub-control:  STUB-CONTROL stub_saw=<n>)

Everything is built in a temporary directory: a bare `origin`, a working repository with branches CLOUD and box/laptop,
and a copy of the .tools/ tree in which the REAL pre-push hook (.tools/git-hooks/pre-push-safe-deploy.sh, installed as
.git/hooks/pre-push) and the REAL safe-deploy.sh run unchanged. The push runs with AGENTBUS_DEVICE=laptop and a
shadowing PATH whose first entry holds two stubs, `aws` and `python3`. `python3` is the name safe-deploy.sh gives the
deploy core (safe_deploy_core.py). Each stub only appends its argv to a log file and exits 0: no AWS call and no deploy
can run. `python` (the hook's deploy-scope lister and ledger reader) is NOT shadowed; it runs for real.
"""
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
sys.path.insert(0, str(TOOLS))
import git_bash_resolver  # noqa: E402  the estate's canonical Git Bash, never a bare `bash`

SERIAL = "0.9.0_WK_NFRA_CTLPLN~108"
# The deploy scope is the DECLARED gated trees only (safe_deploy_core.py CODE_TREES); data/fixture/scripts/ is not one,
# so a fixture there is never deploy-scope and the hold cannot be exercised. The inf gold home is the nearest declared
# deploy-gated layer. The file lives only in the temporary repository and is never uploaded.
FIXTURE = "data/inf/scripts/gold/fixture_unsigned.py"
AUDIT = "org/safe-deploy-bypass-audit.log"
OPEN_DIR = "org/critical_paths/.open_deploys"
ORDER_PATH = "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/FIXTURE_WORKER_ORDER.md"
STUB_SCRIPT = (
    "#!/usr/bin/env bash\n"
    "# TEST DOUBLE: records argv and exits 0. Touches nothing.\n"
    "case \"$*\" in\n"
    "  *safe_deploy_core.py*) printf 'DEPLOY-EXEC %s\\n' \"$*\" >> \"$STUB_LOG\" ;;\n"
    "  *) printf 'OTHER-CALL %s\\n' \"$*\" >> \"$STUB_LOG\" ;;\n"
    "esac\n"
    "exit 0\n"
)
AWS_STUB_SCRIPT = (
    "#!/usr/bin/env bash\n"
    "# TEST DOUBLE: records argv and exits 0. Touches nothing.\n"
    "printf 'AWS-CALL %s\\n' \"$*\" >> \"$STUB_LOG\"\n"
    "exit 0\n"
)


def run(argv, cwd=None, env=None):
    r = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       timeout=240)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def git(repo, *args):
    rc, out = run(["git", "-c", "user.name=fixture", "-c", "user.email=fixture@opal.agent", "-C", str(repo), *args])
    if rc != 0:
        raise RuntimeError("git %s failed rc=%s: %s" % (" ".join(args), rc, out))
    return out.strip()


def rm_tree(path):
    def onerror(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)
    shutil.rmtree(str(path), onerror=onerror)


def build(tmp):
    """The bare origin, the working repository, the real hook installed, and the fixture pushed to box/laptop
    (not yet pushed). Returns (origin, work, base_sha, box_sha)."""
    origin = tmp / "origin.git"
    work = tmp / "work"
    run(["git", "init", "-q", "--bare", str(origin)])
    run(["git", "init", "-q", "-b", "CLOUD", str(work)])
    git(work, "remote", "add", "origin", str(origin))
    shutil.copytree(str(TOOLS), str(work / ".tools"),
                    ignore=shutil.ignore_patterns("tests", "__pycache__", "*.pyc"))
    (work / "org").mkdir()
    # The real hook's halt gate admits a worker serial only while a NON-TERMINAL task order names it, read from the
    # tracked files at HEAD of this repository. The fixture order below is that admission and nothing else: the
    # serial is not changed and no inbox is written.
    order = work / ORDER_PATH
    order.parent.mkdir(parents=True)
    order.write_text("<issued_to>%s</issued_to>\n<issued_by>2.0.0_SA_COO~C</issued_by>\n<status>open</status>\n"
                     % SERIAL, encoding="utf-8")
    git(work, "add", "-A")
    git(work, "commit", "-q", "-m", "base: the trunk with the real .tools tree and one fixture worker order")
    base = git(work, "rev-parse", "HEAD")
    git(work, "push", "-q", "origin", "CLOUD")
    hooks = work / ".git" / "hooks"
    hooks.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(str(work / ".tools" / "git-hooks" / "pre-push-safe-deploy.sh"), str(hooks / "pre-push"))
    git(work, "checkout", "-q", "-b", "box/laptop")
    (work / FIXTURE).parent.mkdir(parents=True)
    (work / FIXTURE).write_text("# fixture: no OPEN change-management ledger names this script\nprint('fixture')\n",
                                encoding="utf-8")
    git(work, "add", "-A")
    git(work, "commit", "-q", "-m", "fixture: an unsigned pipeline script on the box branch")
    box = git(work, "rev-parse", "HEAD")
    # the open-change directory exists and holds NO sentinel: no OPEN change names the fixture
    (work / OPEN_DIR).mkdir(parents=True)
    return origin, work, base, box


def make_stubs(tmp):
    stubs = tmp / "stubs"
    stubs.mkdir()
    for name, body in (("aws", AWS_STUB_SCRIPT), ("python3", STUB_SCRIPT)):
        p = stubs / name
        p.write_text(body, encoding="utf-8", newline="\n")
        os.chmod(str(p), 0o755)
    return stubs


def stub_env(stubs, log):
    env = dict(os.environ)
    env["PATH"] = str(stubs) + os.pathsep + env.get("PATH", "")
    env["AGENTBUS_DEVICE"] = "laptop"
    env["OPAL_AGENT_SERIAL"] = SERIAL
    env["STUB_LOG"] = log.as_posix()
    env.pop("DEPLOY_COMMIT", None)
    return env


def log_lines(log):
    return log.read_text(encoding="utf-8").splitlines() if log.exists() else []


def main(control):
    tmp = Path(tempfile.mkdtemp(prefix="round19_unsigned_"))
    try:
        origin, work, base, box = build(tmp)
        stubs = make_stubs(tmp)
        log = tmp / "stub.log"
        env = stub_env(stubs, log)
        push_rc, push_out = run(["git", "-C", str(work), "push", "origin", "box/laptop"], env=env)
        print("PUSH rc=%d" % push_rc)
        for ln in push_out.splitlines():
            print("PUSH | " + ln)
        ls = git(work, "ls-remote", "origin", "refs/heads/box/laptop")
        landed = ls.split()[:1] == [box]
        print("REMOTE box/laptop=%s local=%s landed=%s" % ((ls.split() or ["-"])[0][:12], box[:12], landed))
        lines = log_lines(log)
        deployed = sum(1 for ln in lines if ln.startswith(("DEPLOY-EXEC", "AWS-CALL")))
        print("STUB-LOG lines=%d deployed=%d" % (len(lines), deployed))
        audit_path = work / AUDIT
        audit = audit_path.read_text(encoding="utf-8").splitlines() if audit_path.exists() else []
        held_rows = [ln for ln in audit if "HELD-DEPLOY" in ln and ("path=" + FIXTURE) in ln]
        for ln in held_rows:
            print("AUDIT | " + ln)
        held = len(held_rows)
        held_reason = any("reason=no-open-ledger-names-it" in ln for ln in held_rows)
        if not control:
            ok = push_rc == 0 and deployed == 0 and held == 1 and landed and held_reason
            print("UNSIGNED-PUSH push_rc=%d deployed=%d held=%d ok=%s" % (push_rc, deployed, held, ok))
            return 0 if ok else 1
        # control: the same fixture, the stub called once by hand, and the log read back
        log.unlink(missing_ok=True)
        bash = git_bash_resolver.git_bash()
        hand_rc, hand_out = run([bash, "-c", "python3 .tools/safe_deploy_core.py --stub-control"], cwd=str(work),
                                env=env)
        saw = sum(1 for ln in log_lines(log) if ln.startswith("DEPLOY-EXEC"))
        print("HAND-CALL rc=%d out=%s" % (hand_rc, hand_out.strip()[:200]))
        print("STUB-CONTROL stub_saw=%d" % saw)
        return 0 if saw == 1 else 1
    finally:
        rm_tree(tmp)


if __name__ == "__main__":
    sys.exit(main("--stub-control" in sys.argv[1:]))
