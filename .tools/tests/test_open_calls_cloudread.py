#!/usr/bin/env python3
"""test_open_calls_cloudread.py -- approval-status reads another box's list from the freshest readable source (NFRA_DEVPLN
round 4, cell DP-e-2; round 5 cell DP-f-2 repaired the seam to one variable).

A foreign box's list is read from three sources -- the cluster copy, origin/box/<box> and the working-tree copy -- and the
greatest written_at wins; a tie goes to the cluster copy, then git, then the working tree. This box reads its own working
tree only. A foreign box with no readable source is UNREADABLE rc 2, never ABSENT.

Test seams (never the live lists, never S3, never the real git refs):
  OPAL_STATE_ROOT         a temporary state root (the working-tree copies live there)
  OPAL_CLOUD_READ_LOCAL   a temporary directory holding box=<box>/open_calls.json (the cluster copy) and
                          git=<box>/open_calls.json (the origin/box/<box> copy)
OPAL_OPENCALLS_CLOUD=0 is set on every call. The stand-in directory is read only when OPAL_CLOUD_READ_LOCAL is set AND
OPAL_STATE_ROOT is set (DP-h-1): with OPAL_STATE_ROOT unset the variable is ignored and a NOTE line says so.

Last line: OPEN-CALLS-CLOUDREAD-TEST cases=<k>/<n> ok=<True|False>
"""
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, ".tools", "open-calls.py")
THIS = "laptop"          # this box in the test (AGENTBUS_DEVICE)
FOREIGN = "dell2"        # a box that is not this box
SERIAL = "0.9.0_WK_NFRA_DEVPLN~1"
PRD = "org/missions/D0/NFRA/NFRA_DEVPLN/prd/NFRA_DEVPLN_PRD.md"
SCHEMA = "open-calls/1"
T1 = "2026-10-13T10:00:00Z"   # the stale copy
T2 = "2026-10-13T12:00:00Z"   # the newer copy
T3 = "2026-10-13T11:00:00Z"   # between them
BRANCH_F = "cand/%s/t-slug" % FOREIGN
BRANCH_T = "cand/%s/t-slug" % THIS


def _force(func, path, _exc):
    """A read-only file on Windows: clear the flag, then remove. Only inside this test's own temporary directory."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def row(rid, branch, state="OPEN", closed=None):
    """one approval row for a branch, shaped as the tool writes it (validate_doc accepts it)."""
    return {"id": rid, "project": "NFRA_DEVPLN", "subject": "test row " + rid, "asked_by": SERIAL, "source": PRD,
            "orders": [], "roots": [], "state": state, "opened_at": T1, "scope": {"verdict": "OWN-BOX"}, "closed": closed,
            "kind": "approval",
            "approval": {"box": branch.split("/")[1], "branch": branch, "purpose": "test feature " + rid,
                         "pages": ["portal/a.tsx"], "class": "test-only", "how": "look at it", "head_sha": None,
                         "commits": None}}


def doc(box, written_at, rows):
    return {"schema": SCHEMA, "device": box, "written_at": written_at, "written_by": "test", "rows": rows}


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(obj, indent=1, ensure_ascii=True) + "\n")


class Env:
    """A temporary base: a state root (working-tree copies) and a stand-in directory (cluster and git copies)."""

    def __init__(self):
        self.base = tempfile.mkdtemp(prefix="opalcalls_cloudread_")
        self.state = os.path.join(self.base, "state")
        self.cloud = os.path.join(self.base, "cloud")
        os.makedirs(self.state)
        os.makedirs(self.cloud)

    def working_tree(self, box, obj):
        write_json(os.path.join(self.state, box, "open_calls.json"), obj)

    def cluster(self, box, obj):
        write_json(os.path.join(self.cloud, "box=%s" % box, "open_calls.json"), obj)

    def git_copy(self, box, obj):
        """the origin/box/<box> copy, standing in for the git ref: <dir>/git=<box>/open_calls.json."""
        write_json(os.path.join(self.cloud, "git=%s" % box, "open_calls.json"), obj)

    def cleanup(self):
        if os.path.isdir(self.base):
            shutil.rmtree(self.base, onerror=_force)


def run(env, args, box_env=THIS, cluster=True, state=True, git_dir=None):
    """(rc, stdout, stderr) of one approval-status call. cluster=False leaves OPAL_CLOUD_READ_LOCAL unset;
    state=False leaves OPAL_STATE_ROOT unset (the test switch off); git_dir, when given, points GIT_DIR at an
    empty repository so the production git source reads no real ref."""
    e = dict(os.environ)
    for k in ("OPAL_CLOUD_READ_LOCAL", "OPAL_OPENCALLS_CLOUD", "OPAL_STATE_ROOT", "GIT_DIR"):
        e.pop(k, None)
    e.update({"OPAL_OPENCALLS_CLOUD": "0", "AGENTBUS_DEVICE": box_env, "OPAL_AGENT_SERIAL": SERIAL})
    if state:
        e["OPAL_STATE_ROOT"] = env.state
    if cluster:
        e["OPAL_CLOUD_READ_LOCAL"] = env.cloud
    if git_dir:
        e["GIT_DIR"] = git_dir
    p = subprocess.run([sys.executable, TOOL] + args, cwd=ROOT, env=e, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=120)
    return p.returncode, p.stdout, p.stderr


def status(env, branch, **kw):
    return run(env, ["approval-status", "--branch", branch], **kw)


def main():
    cases = []

    def check(label, ok):
        cases.append((label, bool(ok)))

    env = None
    try:
        # 1. cluster copy newer than a stale working-tree copy: the cluster rows are read
        env = Env()
        env.working_tree(FOREIGN, doc(FOREIGN, T1, [row("wt-stale", BRANCH_F)]))
        env.cluster(FOREIGN, doc(FOREIGN, T2, [row("cl-new", BRANCH_F)]))
        rc, out, err = status(env, BRANCH_F)
        check("cluster newer than a stale working-tree copy: reads the cluster row (state=OPEN row=cl-new), NOTE cluster",
              rc == 0 and "state=OPEN" in out and "row=cl-new" in out and "row=wt-stale" not in out
              and ("NOTE: %s list read from cluster written_at=%s" % (FOREIGN, T2)) in err)
        env.cleanup()

        # 2. git copy newer than a stale cluster copy: git is read; no working-tree copy exists
        env = Env()
        env.cluster(FOREIGN, doc(FOREIGN, T1, [row("cl-stale", BRANCH_F)]))
        env.git_copy(FOREIGN, doc(FOREIGN, T2, [row("git-new", BRANCH_F)]))
        rc, out, err = status(env, BRANCH_F)
        check("git newer than a stale cluster copy: reads the git row (state=OPEN row=git-new), NOTE git",
              rc == 0 and "state=OPEN" in out and "row=git-new" in out and "row=cl-stale" not in out
              and ("NOTE: %s list read from git written_at=%s" % (FOREIGN, T2)) in err)
        env.cleanup()

        # 3. equal written_at in all three sources: the cluster copy is taken
        env = Env()
        env.working_tree(FOREIGN, doc(FOREIGN, T2, [row("wt-eq", BRANCH_F)]))
        env.cluster(FOREIGN, doc(FOREIGN, T2, [row("cl-eq", BRANCH_F)]))
        env.git_copy(FOREIGN, doc(FOREIGN, T2, [row("git-eq", BRANCH_F)]))
        rc, out, err = status(env, BRANCH_F)
        check("equal written_at in cluster, git and working tree: the cluster copy is taken (row=cl-eq), NOTE cluster",
              rc == 0 and "row=cl-eq" in out and "NOTE: %s list read from cluster" % FOREIGN in err)
        env.cleanup()

        # 4. no readable source and no stand-in (the test switch): UNREADABLE rc 2, never ABSENT
        env = Env()
        rc, out, err = status(env, BRANCH_F, cluster=False)
        check("no readable source, cluster read skipped under the test switch: UNREADABLE rc 2, never ABSENT",
              rc == 2 and "state=UNREADABLE" in out and "state=ABSENT" not in out and "no readable source" in out
              and "not read under the test switch" in out)
        env.cleanup()

        # 5. no readable source with the stand-in holding no object for the box: UNREADABLE rc 2
        env = Env()
        rc, out, err = status(env, BRANCH_F)
        check("no readable source, the stand-in holds no object for the box: UNREADABLE rc 2, never ABSENT",
              rc == 2 and "state=UNREADABLE" in out and "state=ABSENT" not in out and "cluster copy absent" in out)
        env.cleanup()

        # 6. this box reads only its own working tree, even with a newer cluster copy and a newer git copy of its list
        env = Env()
        env.working_tree(THIS, doc(THIS, T1, [row("wt-own", BRANCH_T)]))
        env.cluster(THIS, doc(THIS, T2, [row("cl-own", BRANCH_T, state="CLOSED",
                                             closed={"at": T2, "by": "andrew", "decision": "approved"})]))
        env.git_copy(THIS, doc(THIS, T3, [row("git-own", BRANCH_T)]))
        rc, out, err = status(env, BRANCH_T)
        check("this box reads only its working tree even with a newer cluster copy (row=wt-own, state=OPEN), NOTE working-tree",
              rc == 0 and "state=OPEN" in out and "row=wt-own" in out and "row=cl-own" not in out
              and "row=git-own" not in out and ("NOTE: %s list read from working-tree" % THIS) in err)
        env.cleanup()

        # 7. a cluster copy that fails validation (the wrong device) is skipped; the readable working-tree copy is read
        env = Env()
        env.working_tree(FOREIGN, doc(FOREIGN, T1, [row("wt-ok", BRANCH_F)]))
        env.cluster(FOREIGN, doc("dell1", T2, [row("cl-wrong", BRANCH_F)]))
        rc, out, err = status(env, BRANCH_F)
        check("a cluster copy that fails validation is skipped: the working-tree row is read (row=wt-ok), NOTE working-tree",
              rc == 0 and "row=wt-ok" in out and "row=cl-wrong" not in out
              and ("NOTE: %s list read from working-tree" % FOREIGN) in err)
        env.cleanup()

        # 8. a git copy newer than a stale cluster copy AND a stale working-tree copy: the git rows are read
        env = Env()
        env.working_tree(FOREIGN, doc(FOREIGN, T1, [row("wt-stale2", BRANCH_F)]))
        env.cluster(FOREIGN, doc(FOREIGN, T3, [row("cl-stale2", BRANCH_F)]))
        env.git_copy(FOREIGN, doc(FOREIGN, T2, [row("git-newest", BRANCH_F)]))
        rc, out, err = status(env, BRANCH_F)
        check("git newer than a stale cluster copy and a stale working-tree copy: reads the git row (row=git-newest), NOTE git",
              rc == 0 and "state=OPEN" in out and "row=git-newest" in out and "row=cl-stale2" not in out
              and "row=wt-stale2" not in out and ("NOTE: %s list read from git written_at=%s" % (FOREIGN, T2)) in err)
        env.cleanup()

        # 9. the stand-in set with OPAL_STATE_ROOT UNSET (DP-h-1): the seam is ignored, the production read runs and
        #    finds nothing for a box that exists nowhere in this repo -> UNREADABLE rc 2; the fixture row is NOT used;
        #    the NOTE line says why. OPAL_OPENCALLS_CLOUD=0 keeps this case off S3.
        env = Env()
        env.cluster("zz9", doc("zz9", T2, [row("zz9-fixture", "cand/zz9/t-slug")]))
        # GIT_DIR points at an EMPTY temporary repository: the production `git show origin/box/zz9` finds no real ref
        empty_repo = os.path.join(env.base, "empty-repo")
        os.makedirs(empty_repo)
        init_env = dict(os.environ)
        init_env.pop("GIT_DIR", None)
        init_env.pop("GIT_WORK_TREE", None)
        subprocess.run(["git", "init", "-q", empty_repo], check=True, capture_output=True, timeout=120, env=init_env)
        rc, out, err = status(env, "cand/zz9/t-slug", state=False, git_dir=os.path.join(empty_repo, ".git"))
        check("stand-in set, OPAL_STATE_ROOT unset: the seam is ignored (UNREADABLE rc 2, fixture row not used), NOTE on stderr",
              rc == 2 and "state=UNREADABLE" in out and "row=zz9-fixture" not in out and "state=OPEN" not in out
              and "OPAL_CLOUD_READ_LOCAL ignored: it is a test seam and OPAL_STATE_ROOT is not set" in err)
        env.cleanup()

        # 10. the same stand-in directory with OPAL_STATE_ROOT set to a temporary state root: the fixture row IS used
        env = Env()
        env.cluster("zz9", doc("zz9", T2, [row("zz9-fixture", "cand/zz9/t-slug")]))
        rc, out, err = status(env, "cand/zz9/t-slug")
        check("stand-in set with OPAL_STATE_ROOT set: the fixture row is used (state=OPEN row=zz9-fixture), no ignored NOTE",
              rc == 0 and "state=OPEN" in out and "row=zz9-fixture" in out
              and "OPAL_CLOUD_READ_LOCAL ignored" not in err)
        env.cleanup()
    finally:
        if env is not None:
            env.cleanup()

    fails = 0
    for label, ok in cases:
        print("  %s  %s" % ("PASS" if ok else "FAIL", label))
        fails += 0 if ok else 1
    print("OPEN-CALLS-CLOUDREAD-TEST cases=%d/%d ok=%s" % (len(cases) - fails, len(cases), fails == 0))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
