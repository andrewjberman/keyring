#!/usr/bin/env python3
"""test_open_calls_waiver.py -- the named DEV-overlap waiver of the approval kind of .tools/open-calls.py (NFRA_DEVPLN round 3,
cell DP-d-1): --waive-overlap excuses exactly the named commits from the dev-overlap refusal, --waiver-ref must exist, a waiver
naming a sha outside the overlap set is refused, and --check-only takes any commit-ish (a bare sha).

Every portal here is a TEMPORARY git repository whose origin/PROD and origin/DEV refs are set with update-ref (nothing is
fetched). The feature branch is cut from PROD with two own commits (o1, o2) that DEV also carries, so its overlap is 2. The
tool runs as a subprocess against a TEMPORARY state root (OPAL_STATE_ROOT), and OPAL_OPENCALLS_CLOUD=0 is set, so the real
org/devices/state lists and the cluster copy are never written. The temporary directory is removed at the end.

Last line: OPEN-CALLS-WAIVER-TEST cases=<k>/<n> ok=<True|False>
"""
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, ".tools", "open-calls.py")
BOX = "laptop"
SERIAL = "0.9.0_WK_NFRA_DEVPLN~1"
EMPTY_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"   # git's empty tree: every repository holds it
PURPOSE = "test feature for the named waiver"
PAGES = "portal/a.tsx,portal/b.tsx"
FEATURE = "cand/laptop/wv"
CLEAN = "cand/laptop/clean"


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
    """PROD = p1. The feature cut from PROD carries o1 and o2. DEV = d1 on top of o2, so DEV carries o1 and o2 (the feature
    merged onto DEV) and d1 is a DEV-only commit outside the feature. CLEAN is cut from PROD with c1, which DEV does not carry.
    The feature's overlap is {o1, o2}: 2 commits of 2."""
    os.makedirs(repo)
    git(repo, "init", "-q")
    p1 = make_commit(repo, None, "PROD release")
    o1 = make_commit(repo, p1, "feature one")
    o2 = make_commit(repo, o1, "feature two")
    d1 = make_commit(repo, o2, "DEV only, after the feature merged")
    c1 = make_commit(repo, p1, "clean branch commit not on DEV")
    git(repo, "update-ref", "refs/remotes/origin/PROD", p1)
    git(repo, "update-ref", "refs/remotes/origin/DEV", d1)
    git(repo, "update-ref", "refs/heads/" + FEATURE, o2)
    git(repo, "update-ref", "refs/heads/" + CLEAN, c1)
    return {"p1": p1, "o1": o1, "o2": o2, "d1": d1, "c1": c1}


def _force(func, path, _exc):
    """A read-only git object on Windows: clear the flag, then remove. Only inside this test's own temporary directory."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


class Env:
    """A temporary base holding a state root, a portal repository, a ruling file and lease files. cleanup() removes that base."""

    def __init__(self):
        self.base = tempfile.mkdtemp(prefix="opalcalls_waiver_")
        self.state = os.path.join(self.base, "state")
        self.list = os.path.join(self.state, BOX, "open_calls.json")
        self.repo = os.path.join(self.base, "portal")
        self.lease_dir = os.path.join(self.base, "leases")
        os.makedirs(self.lease_dir)
        self.shas = build_portal(self.repo)
        self.ruling = os.path.join(self.base, "ruling.md")
        with open(self.ruling, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("# Ruling: the DEV-overlap refusal is waived for the named commits.\n")
        self.absent_ruling = os.path.join(self.base, "absent-ruling.md")

    def lease(self, name, expires_in=3600, seat=SERIAL):
        path = os.path.join(self.lease_dir, name)
        doc = {"mode": "FAST", "expires_epoch": int(time.time()) + expires_in, "seat": seat}
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(doc, indent=1) + "\n")
        return path

    def cleanup(self):
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


def row_for(env, branch):
    hits = [r for r in rows(env) if r.get("kind") == "approval" and r["approval"]["branch"] == branch]
    return hits[-1] if hits else None


def reg(env, branch, waive=None, ref=None, check_only=False, lease=None, portal="default"):
    """`add --kind approval` (or `approval-lease` with --lease-file) for a branch or a bare sha. waive is the --waive-overlap
    value, ref the --waiver-ref value; None omits the flag."""
    if lease is None:
        args = ["add", "--kind", "approval", "--project", "NFRA_DEVPLN"]
    else:
        args = ["approval-lease", "--project", "NFRA_DEVPLN", "--lease-file", lease]
    args += ["--box", BOX, "--branch", branch, "--purpose", PURPOSE, "--pages", PAGES, "--class", "client-facing",
             "--how", "open the page and look at it"]
    if portal == "default":
        portal = env.repo
    if portal is not None:
        args += ["--portal", portal]
    if waive is not None:
        args += ["--waive-overlap", waive]
    if ref is not None:
        args += ["--waiver-ref", ref]
    if check_only:
        args.append("--check-only")
    return run(env, args)


def main():
    env = Env()
    cases = []
    s = env.shas

    def check(label, ok):
        cases.append((label, bool(ok)))

    try:
        # 1. a feature cut from PROD whose 2 own commits DEV also carries is refused dev-overlap without a waiver
        before = len(rows(env))
        rc, out, _err = reg(env, FEATURE)
        check("the feature with 2 overlapping commits is refused dev-overlap overlap=2 without a waiver (rc 3), writes nothing",
              rc == 3 and "APPROVAL-REGISTER result=REFUSED reason=dev-overlap overlap=2 commits=2" in out
              and row_for(env, FEATURE) is None and len(rows(env)) == before)

        # 2. a waiver naming both overlap commits registers; the row stores the waiver, the success line prints waived=2
        rc, out, _err = reg(env, FEATURE, waive="%s,%s" % (s["o1"], s["o2"]), ref=env.ruling)
        r = row_for(env, FEATURE)
        check("a waiver naming both overlap commits registers (rc 0, waived=2) and the row stores approval.waiver",
              rc == 0 and ("APPROVAL-REGISTER result=OK row=%s head_sha=%s commits=2 waived=2" % (
                  r["id"] if r else "-", s["o2"])) in out
              and r is not None and r["approval"]["waiver"]["shas"] == [s["o1"], s["o2"]]
              and os.path.basename(r["approval"]["waiver"]["ref"]) == "ruling.md"
              and r["approval"]["head_sha"] == s["o2"] and r["approval"]["commits"] == 2)

        # 3. the stored waived row is read back by the list reader (the row's waiver is well formed)
        rc, out, err = run(env, ["list", "--device", BOX])
        check("the waived row is read back by list (rc 0, the approval line shown, no malformed-row refusal)",
              rc == 0 and "APPROVAL branch=%s" % FEATURE in out and "well-formed" not in err)

        # 4. --check-only takes a bare sha and abbreviated waiver shas (resolved to full), and writes nothing
        before = len(rows(env))
        rc, out, _err = reg(env, s["o2"], waive="%s,%s" % (s["o1"][:8], s["o2"][:8]), ref=env.ruling, check_only=True)
        check("--check-only takes a bare sha with abbreviated waiver shas (rc 0, waived=2) and writes nothing",
              rc == 0 and ("APPROVAL-REGISTER result=OK row=- head_sha=%s commits=2 check-only=yes waived=2" % s["o2"]) in out
              and len(rows(env)) == before)

        # 5. a waiver naming only one overlap commit is refused, unwaived=1, and writes nothing
        before = len(rows(env))
        rc, out, _err = reg(env, FEATURE, waive=s["o1"], ref=env.ruling)
        check("a waiver naming only one overlap commit is refused dev-overlap unwaived=1 (rc 3) and writes nothing",
              rc == 3 and "APPROVAL-REGISTER result=REFUSED reason=dev-overlap overlap=2 commits=2 unwaived=1" in out
              and len(rows(env)) == before)

        # 6. a waiver naming a sha outside the overlap set (the DEV-only commit d1) is refused, and writes nothing
        before = len(rows(env))
        rc, out, _err = reg(env, FEATURE, waive="%s,%s" % (s["o1"], s["d1"]), ref=env.ruling)
        check("a waiver naming a sha outside the overlap set (a DEV-only commit) is refused waiver-sha-not-in-overlap",
              rc == 3 and "APPROVAL-REGISTER result=REFUSED reason=waiver-sha-not-in-overlap" in out
              and len(rows(env)) == before)

        # 7. a waiver on a branch with no overlap is refused: every named sha is outside the (empty) overlap set
        before = len(rows(env))
        rc, out, _err = reg(env, CLEAN, waive=s["c1"], ref=env.ruling)
        check("a waiver on a branch with no overlap is refused waiver-sha-not-in-overlap (rc 3) and writes nothing",
              rc == 3 and "reason=waiver-sha-not-in-overlap" in out and row_for(env, CLEAN) is None and len(rows(env)) == before)

        # 8. a waiver without --waiver-ref is refused waiver-ref-missing
        before = len(rows(env))
        rc, out, _err = reg(env, FEATURE, waive="%s,%s" % (s["o1"], s["o2"]))
        check("a waiver without --waiver-ref is refused waiver-ref-missing (rc 3) and writes nothing",
              rc == 3 and "APPROVAL-REGISTER result=REFUSED reason=waiver-ref-missing" in out and len(rows(env)) == before)

        # 9. a --waiver-ref whose file does not exist is refused waiver-ref-missing
        before = len(rows(env))
        rc, out, _err = reg(env, FEATURE, waive="%s,%s" % (s["o1"], s["o2"]), ref=env.absent_ruling)
        check("a --waiver-ref that does not exist is refused waiver-ref-missing (rc 3) and writes nothing",
              rc == 3 and "APPROVAL-REGISTER result=REFUSED reason=waiver-ref-missing" in out and len(rows(env)) == before)

        # 10. a count, a range, a wildcard or a revision expression is never a waiver
        before = len(rows(env))
        bad_ok = True
        for bad in ("2", "%s..%s" % (s["o1"], s["o2"]), "*", "HEAD~1"):
            rc, out, _err = reg(env, FEATURE, waive=bad, ref=env.ruling)
            bad_ok = bad_ok and rc == 3 and "APPROVAL-REGISTER result=REFUSED reason=waiver-sha-invalid" in out
        check("a count, a range, a wildcard or HEAD~1 given as a waiver is refused waiver-sha-invalid (rc 3), each one",
              bad_ok and len(rows(env)) == before)

        # 11. approval-lease with the same waiver: a live FAST lease registers the waived row already CLOSED approved
        lease_ok = env.lease("lease-ok.json")
        rc, out, _err = reg(env, FEATURE, waive="%s,%s" % (s["o1"], s["o2"]), ref=env.ruling, lease=lease_ok)
        r = row_for(env, FEATURE)
        check("approval-lease with the waiver registers the row CLOSED with approval.waiver and waived=2 (rc 0)",
              rc == 0 and "APPROVAL-REGISTER result=OK" in out and "waived=2" in out and r is not None
              and r["state"] == "CLOSED" and r["closed"]["decision"] == "approved" and r["approval"]["waiver"]["shas"] == [s["o1"], s["o2"]])
    finally:
        env.cleanup()

    fails = 0
    for label, ok in cases:
        print("  %s  %s" % ("PASS" if ok else "FAIL", label))
        fails += 0 if ok else 1
    print("OPEN-CALLS-WAIVER-TEST cases=%d/%d ok=%s" % (len(cases) - fails, len(cases), fails == 0))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
