#!/usr/bin/env python3
"""Cases for .tools/named_commit_check.py and its two callers (NFRA_CTLPLN round 4, cell CT-d-3).

Run: python .tools/tests/test_named_commit_deploy.py   (LAST line: NAMED-COMMIT-TEST cases=<k>/8 ok=<True|False>)

Everything is built in a temporary directory: a local bare repository as `origin`, a clone, a temporary copy of the
device register, and a temporary ledger root. No real remote, no AWS, no deploy, no apply.

Cases 1-7 call the check exactly as the wrappers call it (`named_commit_check.py check --commit <hash>`), one case per
requirement. Case 8 runs the REAL .tools/safe-deploy.sh and .tools/safe-apply.sh with DEPLOY_COMMIT set and
SAFE_NAMED_COMMIT_CHECK_ONLY=1, which makes each wrapper exit right after the check and before the halt gate, the
terraform stage or the deploy core -- the wrappers are run only as far as the check.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import git_bash_resolver  # noqa: E402  the estate's canonical Git Bash, never a bare `bash`

CHECK = TOOLS / "named_commit_check.py"
REAL_REGISTER = ROOT / "org" / "devices" / "DEVICES.json"
SERIAL = "0.9.0_WK_NFRA_CTLPLN~7"


def run(argv, cwd=None, env=None):
    r = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       timeout=180)
    return r.returncode, (r.stdout + r.stderr)


def git(repo, *args):
    rc, out = run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-C", str(repo), *args])
    if rc != 0:
        raise RuntimeError("git %s failed rc=%s: %s" % (" ".join(args), rc, out))
    return out.strip()


def commit(repo, name):
    (Path(repo) / name).write_text(name + "\n", encoding="utf-8")
    git(repo, "add", name)
    git(repo, "commit", "-m", name)
    return git(repo, "rev-parse", "HEAD")


def base_env(register, device):
    env = dict(os.environ, OPAL_DEVICE_REGISTER=str(register), OPAL_AGENT_SERIAL=SERIAL)
    env.pop("AGENTBUS_DEVICE", None)
    env.pop("DEPLOY_LEDGER_SLUG", None)
    if device:
        env["AGENTBUS_DEVICE"] = device
    return env


def check(repo, commit_arg, register, device, extra=None):
    return run([sys.executable, str(CHECK), "check", "--commit", commit_arg, *(extra or [])], cwd=str(repo),
               env=base_env(register, device))


def verdict(out):
    for ln in out.splitlines():
        if ln.startswith("NAMED-COMMIT "):
            return ln.split()[1]
    return None


def field(out, key):
    for ln in out.splitlines():
        if ln.startswith("NAMED-COMMIT ") and (" %s=" % key) in ln:
            return ln.split(" %s=" % key, 1)[1].split(" ")[0]
    return None


def open_ledger(ledger_root, slug):
    """A real sentinel + entry, written by the real deploy_ledger.py copied into a temporary workspace."""
    (ledger_root / ".tools").mkdir(parents=True, exist_ok=True)
    (ledger_root / "org" / "critical_paths" / "change_management").mkdir(parents=True, exist_ok=True)
    shutil.copy(str(TOOLS / "deploy_ledger.py"), str(ledger_root / ".tools" / "deploy_ledger.py"))
    # deploy_ledger.py commits through safe-commit.sh, which imports git_bash_resolver from the real .tools;
    # the temporary ledger root holds no .tools copy of it, so the child gets the real .tools on PYTHONPATH.
    child_env = dict(os.environ)
    child_env["PYTHONPATH"] = os.pathsep.join(p for p in (str(TOOLS), child_env.get("PYTHONPATH", "")) if p)
    # open() also commits its two files through .tools/safe-commit.sh under WORKSPACE (this temporary root). The
    # commit is outside case 8's scope (case 8 reads the sentinel and entry on disk), so the root gets a zero-exit
    # test double instead of the real gate, which needs the real repository.
    (ledger_root / ".tools" / "safe-commit.sh").write_text(
        "#!/bin/sh\necho 'OK: fixture safe-commit double (test only; open commit not under test)'\nexit 0\n",
        encoding="utf-8", newline="\n")
    rc, out = run([sys.executable, str(ledger_root / ".tools" / "deploy_ledger.py"), "open", "--slug", slug,
                   "--title", "named-commit fixture", "--author", SERIAL, "--leg", "L1|git|fixture|hash pushed"],
                  cwd=str(ledger_root), env=child_env)
    if rc != 0:
        raise RuntimeError("deploy_ledger open failed rc=%s: %s" % (rc, out))
    state = json.loads((ledger_root / "org" / "critical_paths" / ".open_deploys" / (slug + ".json")).read_text("utf-8"))
    return state, ledger_root / state["entry_path"]


def wrapper(name, repo, commit_arg, register, device, ledger_root, extra_args=()):
    env = base_env(register, device)
    env.update(DEPLOY_COMMIT=commit_arg, SAFE_NAMED_COMMIT_CHECK_ONLY="1", NAMED_COMMIT_LEDGER_ROOT=str(ledger_root),
               SAFE_APPLY_TERRAFORM="terraform-not-run")
    return run(git_bash_resolver.bash_argv(str(TOOLS / name), *extra_args), cwd=str(repo), env=env)


def main():
    results = []
    tmp = Path(tempfile.mkdtemp(prefix="named_commit_"))
    try:
        origin = tmp / "origin.git"
        work = tmp / "work"
        run(["git", "init", "--bare", "-q", str(origin)])
        run(["git", "init", "-q", "-b", "CLOUD", str(work)])
        git(work, "remote", "add", "origin", str(origin))
        c_trunk = commit(work, "trunk.txt")
        git(work, "push", "-q", "origin", "CLOUD")
        git(work, "checkout", "-q", "-b", "q/dell1/X/round1")
        c_off = commit(work, "published-off-trunk.txt")
        git(work, "push", "-q", "origin", "q/dell1/X/round1")
        git(work, "checkout", "-q", "-b", "local-only")
        c_unpub = commit(work, "unpublished.txt")
        register = tmp / "DEVICES.json"
        shutil.copy(str(REAL_REGISTER), str(register))
        print("fixture: trunk=%s off_trunk_published=%s unpublished=%s" % (c_trunk[:12], c_off[:12], c_unpub[:12]))

        def case(num, label, ok, detail):
            results.append(bool(ok))
            print("%s case %d: %s | %s" % ("PASS" if ok else "FAIL", num, label, detail.strip().replace("\n", " // ")))

        rc, out = check(work, c_trunk, register, "dell1")
        case(1, "dell1, a commit on origin/CLOUD -> ADMITTED, ON-TRUNK",
             rc == 0 and verdict(out) == "ADMITTED" and field(out, "trunk") == "ON-TRUNK", "rc=%s %s" % (rc, out))

        rc, out = check(work, c_off, register, "dell1")
        case(2, "dell1, off the trunk, pushed to origin/q/dell1/X/round1 -> ADMITTED, OFF-TRUNK, branch printed",
             rc == 0 and verdict(out) == "ADMITTED" and field(out, "trunk") == "OFF-TRUNK"
             and field(out, "branch") == "q/dell1/X/round1", "rc=%s %s" % (rc, out))

        rc, out = check(work, c_unpub, register, "dell1")
        case(3, "dell1, off the trunk and NOT pushed -> REFUSED, not published",
             rc != 0 and verdict(out) == "REFUSED" and "not published" in out, "rc=%s %s" % (rc, out))

        rc, out = check(work, c_off[:7], register, "dell1")
        case(4, "dell1, the case-2 commit by its 7-character short hash -> REFUSED",
             rc != 0 and verdict(out) == "REFUSED" and "40-character" in out, "rc=%s %s" % (rc, out))

        rc, out = check(work, c_off, register, "laptop")
        case(5, "laptop (control-plane), the case-2 commit -> UNCHANGED (the wrappers never refused it), admitted",
             rc == 0 and verdict(out) == "UNCHANGED" and field(out, "role") == "control-plane"
             and field(out, "trunk") == "OFF-TRUNK", "rc=%s %s" % (rc, out))

        rc, out = check(work, c_off, register, None)
        case(6, "device unset -> REFUSED", rc != 0 and verdict(out) == "REFUSED" and "device unset" in out,
             "rc=%s %s" % (rc, out))

        dead = tmp / "work_dead_origin"
        run(["git", "clone", "-q", str(origin), str(dead)])
        git(dead, "remote", "set-url", "origin", str(tmp / "nowhere.git"))
        git(dead, "fetch", "-q", str(origin), "q/dell1/X/round1")  # the commit is local; only the remote is dead
        rc, out = check(dead, c_off, register, "dell1")
        case(7, "origin unreachable -> REFUSED, never OFF-TRUNK",
             rc != 0 and verdict(out) == "REFUSED" and field(out, "trunk") in (None, "-")
             and "fetch" in out and "OFF-TRUNK" not in out.split("reason=")[0], "rc=%s %s" % (rc, out))

        # case 8: the real wrappers, as far as the check.
        ok8, notes = True, []
        for name, extra, refuse_rc in (("safe-deploy.sh", (), 1), ("safe-apply.sh", ("-chdir=x", "apply"), 8)):
            root = tmp / ("ledger_" + name.replace(".sh", ""))
            state, entry = open_ledger(root, "fixture-" + name.replace(".sh", ""))
            rc, out = wrapper(name, work, c_off, register, "dell1", root, extra)
            sentinel = json.loads((root / "org" / "critical_paths" / ".open_deploys"
                                   / ("fixture-" + name.replace(".sh", "") + ".json")).read_text("utf-8"))
            md = entry.read_text("utf-8")
            want = "named_commit=%s trunk=OFF-TRUNK branch=q/dell1/X/round1 device=dell1" % c_off
            carried = want in md and sentinel.get("named_commit", {}).get("commit") == c_off \
                and any(want in str(e) for e in sentinel["log"])
            # a later tool re-render (close-leg) keeps the line, because it lives in the sentinel's log
            run([sys.executable, str(root / ".tools" / "deploy_ledger.py"), "close-leg", "--slug",
                 "fixture-" + name.replace(".sh", ""), "--leg-id", "L1", "--proof", "p"], cwd=str(root))
            survives = want in entry.read_text("utf-8")
            # controls on the wrapper: an unpublished commit and an off-trunk commit with no open sentinel are refused
            rc_u, out_u = wrapper(name, work, c_unpub, register, "dell1", root, extra)
            rc_n, out_n = wrapper(name, work, c_off, register, "dell1", tmp / "empty_ledger_root", extra)
            this = (rc == 0 and "NAMED-COMMIT ADMITTED" in out and carried and survives
                    and rc_u == refuse_rc and "not published" in out_u
                    and rc_n == refuse_rc and "exactly ONE open ledger sentinel" in out_n)
            notes.append("%s: rc=%s carried=%s survives_rerender=%s unpublished_rc=%s no_sentinel_rc=%s"
                         % (name, rc, carried, survives, rc_u, rc_n))
            ok8 = ok8 and this
        case(8, "the wrappers, on case 2 with an open sentinel, leave named_commit=<hash> in the ledger entry",
             ok8, "; ".join(notes))
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)
    k = sum(results)
    ok = k == 8 and len(results) == 8
    print("NAMED-COMMIT-TEST cases=%d/8 ok=%s" % (k, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
