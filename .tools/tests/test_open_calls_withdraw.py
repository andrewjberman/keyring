#!/usr/bin/env python3
"""test_open_calls_withdraw.py -- the `withdrawn` close decision of the `approval` kind (NFRA_DEVPLN round 4, cell DP-e-1).

Runs the tool as a subprocess against a TEMPORARY state root (OPAL_STATE_ROOT) and a TEMPORARY portal git repository.
OPAL_OPENCALLS_CLOUD=0 is set as well. The real org/devices/state lists are never written; nothing is fetched or pushed.

A withdrawn row is an OPEN duplicate that is NOT a decision on the feature: it ends only an OPEN row, approval-status skips it,
and every reader (list, approval-status) accepts it. A withdraw of a CLOSED row is refused rc 2 with nothing written.

Last line: OPEN-CALLS-WITHDRAW-TEST cases=<k>/<n> ok=<True|False>
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
BOX = "laptop"
SERIAL = "0.9.0_WK_NFRA_DEVPLN~1"
PRD = "org/missions/D0/NFRA/NFRA_DEVPLN/prd/NFRA_DEVPLN_PRD.md"
CONTEXT = "Created by the withdraw-decision test; a duplicate registration of one branch under test here."
EMPTY_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"   # git's empty tree: every repository holds it
BRANCH = "cand/laptop/t-dup"
OTHER = "cand/laptop/t-ok"
FIXTURE_SLUGS = ("t-dup", "t-ok", "t-appr", "t-decl", "t-only")


def git(repo, *args):
    """stdout of one git command in the temporary portal; a failure is a test error, not a verdict."""
    p = subprocess.run(["git", "-C", repo, "-c", "user.name=test", "-c", "user.email=test@opal.agent", "-c", "commit.gpgsign=false"]
                       + list(args), capture_output=True, text=True, encoding="utf-8", errors="replace")
    if p.returncode != 0:
        raise RuntimeError("git %s rc=%d: %s" % (" ".join(args), p.returncode, p.stderr.strip()))
    return p.stdout.strip()


def make_commit(repo, parent, message):
    args = ["commit-tree", EMPTY_TREE, "-m", message]
    if parent:
        args += ["-p", parent]
    return git(repo, *args)


def build_portal(repo):
    """PROD = p1; DEV = p1 + d1 (a DEV-only commit); each cand/laptop/<slug> = p1 + one own commit (a PROD cut)."""
    os.makedirs(repo)
    git(repo, "init", "-q")
    p1 = make_commit(repo, None, "PROD release")
    d1 = make_commit(repo, p1, "DEV only")
    git(repo, "update-ref", "refs/remotes/origin/PROD", p1)
    git(repo, "update-ref", "refs/remotes/origin/DEV", d1)
    for slug in FIXTURE_SLUGS:
        git(repo, "update-ref", "refs/heads/cand/laptop/" + slug, make_commit(repo, p1, "own commit for " + slug))


def _force(func, path, _exc):
    """A read-only git object on Windows: clear the flag, then remove. Only inside this test's own temporary directory."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


class Env:
    """A temporary base holding a state root, a ruling file and a fixture portal. cleanup() removes that base."""

    def __init__(self):
        self.base = tempfile.mkdtemp(prefix="opalcalls_withdraw_")
        self.state = os.path.join(self.base, "state")
        self.box_dir = os.path.join(self.state, BOX)
        self.list = os.path.join(self.box_dir, "open_calls.json")
        self.ruling = os.path.join(self.base, "RULING.md")
        self.portal = os.path.join(self.base, "portal")
        build_portal(self.portal)
        os.makedirs(self.box_dir, exist_ok=True)
        with open(self.ruling, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("ruling for the withdraw-decision test\n")

    def cleanup(self):
        # the whole temporary base: the state root, the fixture portal and the ruling file
        shutil.rmtree(self.base, onerror=_force)


def run(env, args, serial=SERIAL):
    """(rc, stdout, stderr) of one tool call; the serial is what OPAL_AGENT_SERIAL holds for that call."""
    e = dict(os.environ)
    e.update({"OPAL_STATE_ROOT": env.state, "OPAL_OPENCALLS_CLOUD": "0", "AGENTBUS_DEVICE": BOX, "OPAL_AGENT_SERIAL": serial})
    try:
        p = subprocess.run([sys.executable, TOOL] + args, cwd=ROOT, env=e, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=120)
    except subprocess.TimeoutExpired:
        return 124, "", "TIMEOUT"
    return p.returncode, p.stdout, p.stderr


def rows(env):
    if not os.path.exists(env.list):
        return []
    with open(env.list, encoding="utf-8") as fh:
        return json.load(fh)["rows"]


def branch_rows(env, branch):
    """the approval rows for one branch, in file order (the oldest first)."""
    return [r for r in rows(env) if r.get("kind") == "approval" and r["approval"]["branch"] == branch]


def add_approval(env, branch, klass, serial=SERIAL):
    return run(env, ["add", "--kind", "approval", "--project", "NFRA_DEVPLN", "--box", BOX, "--branch", branch,
                     "--purpose", "test feature for the withdraw decision", "--pages", "portal/a.tsx",
                     "--class", klass, "--how", "open the page and look at it", "--portal", env.portal], serial)


def close_approval(env, cid, ruled_by, decision, serial=SERIAL):
    return run(env, ["close", "--id", cid, "--ruled-by", ruled_by, "--ruling-file", env.ruling, "--decision", decision], serial)


def status(env, branch):
    rc, out, _err = run(env, ["approval-status", "--branch", branch, "--store-dir", env.state])
    return rc, out.strip()


def file_bytes(env):
    with open(env.list, "rb") as fh:
        return fh.read()


def main():
    env = Env()
    cases = []

    def check(label, ok):
        cases.append((label, bool(ok)))

    try:
        # 1. two OPEN rows for one branch (the builder registered it twice); the newer is withdrawn; the older reads as the row
        add_approval(env, BRANCH, "client-facing")
        add_approval(env, BRANCH, "client-facing")
        older, newer = branch_rows(env, BRANCH)
        rc_w, _o, err_w = close_approval(env, newer["id"], "andrew", "withdrawn")
        rc_s, line = status(env, BRANCH)
        closed_newer = [r for r in rows(env) if r["id"] == newer["id"]][0]
        check("two OPEN rows, the newer withdrawn: approval-status reads the older row (state=OPEN valid=- row=<older id>)",
              rc_w == 0 and closed_newer["state"] == "CLOSED" and closed_newer["closed"]["decision"] == "withdrawn"
              and closed_newer["closed"]["by"] == "andrew"
              and rc_s == 0 and ("state=OPEN valid=- row=%s " % older["id"]) in line)

        # 2. withdraw the only row of a branch: ABSENT, the line exactly as for no row
        add_approval(env, OTHER, "test-only")
        only = branch_rows(env, OTHER)[0]
        rc_o, _o, _e = close_approval(env, only["id"], "andrew", "withdrawn")
        rc_a, line_a = status(env, OTHER)
        rc_n, line_n = status(env, "cand/laptop/none-9")
        check("withdraw the only row: ABSENT, the same line as for a branch with no row",
              rc_o == 0 and rc_a == 0 and line_a == line_n.replace("cand/laptop/none-9", OTHER)
              and line_a.startswith("APPROVAL branch=%s state=ABSENT valid=- row=- " % OTHER))

        # 3. withdraw an APPROVED row: refused rc 2, nothing written
        add_approval(env, "cand/laptop/t-appr", "test-only")
        appr = branch_rows(env, "cand/laptop/t-appr")[0]
        close_approval(env, appr["id"], "cto", "approved", serial="1.0.0_SA_CTO")
        before = file_bytes(env)
        rc_ap, _o, err_ap = close_approval(env, appr["id"], "andrew", "withdrawn")
        check("withdraw an APPROVED row: refused rc 2 naming approved, nothing written",
              rc_ap == 2 and "already closed (approved)" in err_ap and "a withdraw ends only an OPEN row" in err_ap
              and file_bytes(env) == before)

        # 4. withdraw a DECLINED row: refused rc 2, nothing written
        add_approval(env, "cand/laptop/t-decl", "test-only")
        decl = branch_rows(env, "cand/laptop/t-decl")[0]
        close_approval(env, decl["id"], "andrew", "declined")
        before = file_bytes(env)
        rc_dc, _o, err_dc = close_approval(env, decl["id"], "andrew", "withdrawn")
        check("withdraw a DECLINED row: refused rc 2 naming declined, nothing written",
              rc_dc == 2 and "already closed (declined)" in err_dc and file_bytes(env) == before)

        # 5. --decision withdrawn on a fork row is refused (rc 1, a REFUSED line), and the fork stays OPEN
        rc_f, _o, _e = run(env, ["add", "--project", "NONE", "--subject", "a fork for the refusal test", "--asked-by", SERIAL,
                                 "--source", PRD, "--context", CONTEXT, "--rec", "(a) because the test says so"])
        fork_id = [r["id"] for r in rows(env) if r.get("kind", "fork") == "fork"][-1]
        rc_fw, _o, err_fw = run(env, ["close", "--id", fork_id, "--by", "andrew", "--ruling-file", env.ruling,
                                      "--decision", "withdrawn"])
        fork_now = [r for r in rows(env) if r["id"] == fork_id][0]
        check("--decision withdrawn on a fork row is refused (REFUSED, rc 1) and the fork stays OPEN",
              rc_f == 0 and rc_fw == 1 and "REFUSED" in err_fw and fork_now["state"] == "OPEN")

        # 6. a list holding a withdrawn row passes list: the row shows CLOSED with its decision, and approval-status still passes
        rc_l, out_l, err_l = run(env, ["list", "--device", BOX])
        wline = [ln for ln in out_l.splitlines() if newer["id"] in ln and "[CLOSED] approval" in ln]
        check("a list holding a withdrawn row passes list: it shows [CLOSED] approval with closed withdrawn",
              rc_l == 0 and "REFUSED" not in out_l and len(wline) == 1
              and "closed withdrawn by andrew" in out_l)

        # 7. a withdraw of a row already withdrawn is refused rc 2 (a withdraw ends only an OPEN row)
        before = file_bytes(env)
        rc_ww, _o, err_ww = close_approval(env, newer["id"], "andrew", "withdrawn")
        check("withdraw a withdrawn row again: refused rc 2 naming withdrawn, nothing written",
              rc_ww == 2 and "already closed (withdrawn)" in err_ww and file_bytes(env) == before)
    finally:
        env.cleanup()

    fails = 0
    for label, ok in cases:
        print("  %s  %s" % ("PASS" if ok else "FAIL", label))
        fails += 0 if ok else 1
    print("OPEN-CALLS-WITHDRAW-TEST cases=%d/%d ok=%s" % (len(cases) - fails, len(cases), fails == 0))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
