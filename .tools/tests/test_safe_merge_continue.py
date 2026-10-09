"""GS-f-6: safe-merge.sh --continue refuses a merge commit that does not carry every path the conflicted merge staged.

Runs in a throwaway LINKED WORKTREE of this repository on scratch branches (sparse: only .tools/ and the scratch dir are
checked out, so it takes seconds). Nothing is pushed and no shared branch is touched: the worktree and every branch it
made are removed at the end. The script under test is the one beside this file (.tools/safe-merge.sh); it runs with the
throwaway worktree as its cwd, so its ROOT, index, MERGE_HEAD and state file are the throwaway's.

Case a  : two files conflict (plus one clean file the feature adds); resolve BOTH, --continue -> rc 0, all three in the commit.
Case b  : the planted partial (D1-S5): resolve both, then unstage ONE resolved path; --continue -> rc 7, the REFUSED line
          names the unstaged path (and only it); the commit is not rewritten.
Case c  : the control: a deliberate keep-ours resolution of one path (nothing lost) -> rc 0, no REFUSED line.

Last line: SM-CONTINUE ok=<True|False> cases=<passed>/<total>
"""
import os
import shutil
import subprocess
import sys
import tempfile
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(os.path.dirname(HERE), "safe-merge.sh")
ROOT = os.path.dirname(os.path.dirname(HERE))
SERIAL = "0.9.0_WK_SMCONT~1"
SCR = "sm_continue_scratch"
TAG = uuid.uuid4().hex[:8]

CASES = []


def case(name, ok, detail=""):
    CASES.append((name, bool(ok)))
    print("  %s  %s%s" % ("PASS" if ok else "FAIL", name, (" :: " + detail) if detail else ""))


def bash():
    for c in (r"C:\Program Files\Git\bin\bash.exe", "/usr/bin/bash", "/bin/bash"):
        if os.path.exists(c):
            return c
    return shutil.which("bash") or "bash"


def git(cwd, *args, check=True, env=None):
    e = dict(os.environ)
    e.update({"GIT_AUTHOR_NAME": "x", "GIT_AUTHOR_EMAIL": "x@y", "GIT_COMMITTER_NAME": "x", "GIT_COMMITTER_EMAIL": "x@y"})
    if env:
        e.update(env)
    r = subprocess.run(["git"] + list(args), cwd=cwd, env=e, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and r.returncode != 0:
        raise RuntimeError("git %s rc=%s: %s" % (" ".join(args), r.returncode, r.stderr.strip()))
    return r


def write(wt, rel, text):
    p = os.path.join(wt, SCR, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def sm(wt, *args):
    env = dict(os.environ)
    env.update({"OPAL_AGENT_SERIAL": SERIAL, "SAFE_MERGE_IN_TREE": "1"})
    env.pop("SAFE_MERGE_FULL_GRADE", None)
    r = subprocess.run([bash(), SCRIPT] + list(args), cwd=wt, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=600)
    return r.returncode, r.stdout + r.stderr


def build(base_dir, name):
    """A throwaway worktree with branch main-<name> (base + one side) and feat-<name> (the other side), conflicting on
    c1.txt and c2.txt; feat also adds clean.txt. Returns (worktree, ours_branch, feat_branch)."""
    wt = os.path.join(base_dir, name)
    ours, feat = "sm-cont-%s-%s-ours" % (TAG, name), "sm-cont-%s-%s-feat" % (TAG, name)
    git(ROOT, "worktree", "add", "-q", "--no-checkout", "-b", ours, wt, "HEAD")
    git(wt, "sparse-checkout", "set", "--no-cone", "/.tools/", "/%s/" % SCR)
    git(wt, "checkout", "-q", ours)
    base = {"c1.txt": "r1\nr2\nr3\n", "c2.txt": "r1\nr2\nr3\n"}
    for f, t in base.items():
        write(wt, f, t)
    git(wt, "add", "-f", SCR)
    git(wt, "commit", "-q", "--no-verify", "-m", "base")
    git(wt, "checkout", "-q", "-b", feat)
    for f in base:
        write(wt, f, "r1\nr2\nr3\nFEAT-" + f + "\n")
    write(wt, "clean.txt", "feature-only file\n")
    git(wt, "add", "-f", SCR)
    git(wt, "commit", "-q", "--no-verify", "-m", "feat")
    git(wt, "checkout", "-q", ours)
    for f in base:
        write(wt, f, "r1\nr2\nr3\nOURS-" + f + "\n")
    git(wt, "add", "-f", SCR)
    git(wt, "commit", "-q", "--no-verify", "-m", "ours")
    return wt, ours, feat


def merged_paths(wt):
    return set(git(wt, "diff", "--name-only", "HEAD^1", "HEAD").stdout.split())


def parents(wt):
    return len(git(wt, "rev-list", "--parents", "-n", "1", "HEAD").stdout.split()) - 1


def resolve_union(wt, f):
    write(wt, f, "r1\nr2\nr3\nOURS-%s\nFEAT-%s\n" % (f, f))
    git(wt, "add", "-f", "--", "%s/%s" % (SCR, f))


def main():
    base_dir = tempfile.mkdtemp(prefix="smcont_", dir=os.path.join(ROOT, ".scratch") if os.path.isdir(os.path.join(ROOT, ".scratch")) else None)
    made = []  # (worktree, branches)
    try:
        # ---- case a: full resolution
        print("=== case a: resolve BOTH conflicted files, --continue ===")
        wt, ours, feat = build(base_dir, "a")
        made.append((wt, [ours, feat]))
        rc, out = sm(wt, feat)
        case("a1 the merge opens at rc 4 (CONFLICT, merge left open)", rc == 4, "rc=%s" % rc)
        for f in ("c1.txt", "c2.txt"):
            resolve_union(wt, f)
        rc, out = sm(wt, "--continue")
        got = merged_paths(wt) if parents(wt) == 2 else set()
        case("a2 --continue exits 0", rc == 0, "rc=%s :: %s" % (rc, out.strip().splitlines()[-1] if out.strip() else ""))
        case("a3 the commit is a two-parent merge", parents(wt) == 2)
        want = {"%s/c1.txt" % SCR, "%s/c2.txt" % SCR, "%s/clean.txt" % SCR}
        case("a4 both resolved files and the clean one are in the commit", want <= got, "got=%s" % sorted(got))
        case("a5 no REFUSED line on the full resolution", "REFUSED -- the merge commit lacks" not in out)

        # ---- case b: the planted partial
        print("=== case b: resolve both, unstage ONE resolved path (D1-S5), --continue ===")
        wt, ours, feat = build(base_dir, "b")
        made.append((wt, [ours, feat]))
        rc, out = sm(wt, feat)
        case("b1 the merge opens at rc 4", rc == 4, "rc=%s" % rc)
        for f in ("c1.txt", "c2.txt"):
            resolve_union(wt, f)
        git(wt, "restore", "--staged", "--", "%s/c2.txt" % SCR)
        head_before = git(wt, "rev-parse", "HEAD").stdout.strip()
        rc, out = sm(wt, "--continue")
        refused = [ln for ln in out.splitlines() if "REFUSED -- the merge commit lacks" in ln]
        case("b2 --continue exits non-zero (7)", rc == 7, "rc=%s" % rc)
        case("b3 the REFUSED line names the unstaged path", bool(refused) and "%s/c2.txt" % SCR in refused[0], refused[0] if refused else "no REFUSED line")
        case("b4 the REFUSED line does not name the carried path", bool(refused) and "c1.txt" not in refused[0])
        case("b5 the commit landed and was not rewritten (merge commit over the old HEAD)",
             parents(wt) == 2 and git(wt, "rev-parse", "HEAD^1").stdout.strip() == head_before)
        case("b6 the unstaged path is absent from the commit, the resolved one present",
             "%s/c2.txt" % SCR not in merged_paths(wt) and "%s/c1.txt" % SCR in merged_paths(wt))

        # ---- case c: control, a deliberate keep-ours resolution is not a lost path
        print("=== case c: control -- a deliberate keep-ours resolution of one path ===")
        wt, ours, feat = build(base_dir, "c")
        made.append((wt, [ours, feat]))
        rc, out = sm(wt, feat)
        case("c1 the merge opens at rc 4", rc == 4, "rc=%s" % rc)
        resolve_union(wt, "c1.txt")
        git(wt, "checkout", "--ours", "--", "%s/c2.txt" % SCR)
        git(wt, "add", "-f", "--", "%s/c2.txt" % SCR)
        rc, out = sm(wt, "--continue")
        case("c2 --continue exits 0 and names no lost path", rc == 0 and "REFUSED -- the merge commit lacks" not in out, "rc=%s" % rc)
    except Exception as exc:  # noqa: BLE001 -- a harness failure is a failed run, printed
        case("harness ran without raising", False, repr(exc))
    finally:
        for wt, brs in made:
            git(ROOT, "worktree", "remove", "--force", wt, check=False)
            for b in brs:
                git(ROOT, "branch", "-D", b, check=False)
        git(ROOT, "worktree", "prune", check=False)
        shutil.rmtree(base_dir, ignore_errors=True)
    left = [b for b in git(ROOT, "branch", "--list", "sm-cont-%s-*" % TAG, check=False).stdout.split()]
    case("cleanup: no scratch branch left", not left, str(left))
    passed = sum(1 for _, ok in CASES if ok)
    ok = passed == len(CASES)
    print("SM-CONTINUE ok=%s cases=%d/%d" % (ok, passed, len(CASES)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
