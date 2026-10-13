#!/usr/bin/env python3
"""test_open_calls_register.py -- the registration facts of the approval kind of .tools/open-calls.py (NFRA_DEVPLN round 1,
cell DP-b-5): head_sha and commits computed from the portal, the DEV-overlap refusal, --check-only, and the FAST-lease row.

Every portal here is a TEMPORARY git repository whose origin/PROD and origin/DEV refs are set with update-ref (nothing is
fetched). The tool runs as a subprocess against a TEMPORARY state root (OPAL_STATE_ROOT), and OPAL_OPENCALLS_CLOUD=0 is set,
so the real org/devices/state lists and the cluster copy are never written. The measurement (`scope`) reads the real
repository read-only, as the tool always does. The temporary directory is removed at the end.

Last line: OPEN-CALLS-REGISTER-TEST cases=<k>/<n> ok=<True|False>
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
OTHER_SEAT = "0.9.0_WK_OTHER~9"
EMPTY_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"   # git's empty tree: every repository holds it
PURPOSE = "test feature for the registration facts"
PAGES = "portal/a.tsx,portal/b.tsx"


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
    """PROD = p1. DEV = p1 + d1 + d2 (DEV carries commits PROD does not). The PROD cut carries o1, o2 on p1. The DEV cut
    carries d1, d2 and x1 (every DEV commit beneath its own). Returns the shas the cases name."""
    os.makedirs(repo)
    git(repo, "init", "-q")
    p1 = make_commit(repo, None, "PROD release")
    d1 = make_commit(repo, p1, "DEV only one")
    d2 = make_commit(repo, d1, "DEV only two")
    o1 = make_commit(repo, p1, "own one")
    o2 = make_commit(repo, o1, "own two")
    x1 = make_commit(repo, d2, "own on the DEV cut")
    git(repo, "update-ref", "refs/remotes/origin/PROD", p1)
    git(repo, "update-ref", "refs/remotes/origin/DEV", d2)
    git(repo, "update-ref", "refs/heads/cand/laptop/prod-cut", o2)
    git(repo, "update-ref", "refs/heads/cand/laptop/lease-ok", o2)
    git(repo, "update-ref", "refs/heads/cand/laptop/lease-deny", o2)
    git(repo, "update-ref", "refs/heads/prod-cut", o2)
    git(repo, "update-ref", "refs/heads/cand/laptop/dev-cut", x1)
    git(repo, "update-ref", "refs/heads/cand/laptop/empty", p1)
    return {"p1": p1, "d2": d2, "o2": o2, "x1": x1}


def _force(func, path, _exc):
    """A read-only git object on Windows: clear the flag, then remove. Only inside this test's own temporary directory."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


class Env:
    """A temporary base holding a state root, a portal repository and lease files. cleanup() removes that base."""

    def __init__(self):
        self.base = tempfile.mkdtemp(prefix="opalcalls_register_")
        self.state = os.path.join(self.base, "state")
        self.list = os.path.join(self.state, BOX, "open_calls.json")
        self.repo = os.path.join(self.base, "portal")
        self.lease_dir = os.path.join(self.base, "leases")
        os.makedirs(self.lease_dir)
        self.shas = build_portal(self.repo)

    def lease(self, name, mode="FAST", expires_in=3600, seat=SERIAL):
        path = os.path.join(self.lease_dir, name)
        doc = {"mode": mode, "expires_epoch": int(time.time()) + expires_in, "seat": seat}
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


def add(env, branch, portal="portal-default", klass="client-facing", check_only=False, serial=SERIAL):
    """`add --kind approval`; portal=None omits --portal (the refusal case)."""
    args = ["add", "--kind", "approval", "--project", "NFRA_DEVPLN", "--box", BOX, "--branch", branch, "--purpose", PURPOSE,
            "--pages", PAGES, "--class", klass, "--how", "open the page and look at it"]
    if portal == "portal-default":
        portal = env.repo
    if portal is not None:
        args += ["--portal", portal]
    if check_only:
        args.append("--check-only")
    return run(env, args, serial)


def register_lease(env, branch, lease_path, portal="portal-default", serial=SERIAL):
    args = ["approval-lease", "--branch", branch, "--project", "NFRA_DEVPLN", "--box", BOX, "--purpose", PURPOSE, "--pages", PAGES, "--class", "client-facing",
            "--how", "open the page and look at it", "--lease-file", lease_path]
    if portal == "portal-default":
        portal = env.repo
    if portal is not None:
        args += ["--portal", portal]
    return run(env, args, serial)


def status(env, branch):
    rc, out, _err = run(env, ["approval-status", "--branch", branch, "--store-dir", env.state])
    return rc, out.strip()


def main():
    env = Env()
    cases = []
    s = env.shas

    def check(label, ok):
        cases.append((label, bool(ok)))

    try:
        # 1. a branch cut from PROD with 2 own commits registers with commits=2 and the computed head
        rc, out, _err = add(env, "cand/laptop/prod-cut")
        r = row_for(env, "cand/laptop/prod-cut")
        check("a branch cut from PROD with 2 own commits registers with commits=2 and the computed head",
              rc == 0 and ("APPROVAL-REGISTER result=OK row=%s head_sha=%s commits=2" % (r["id"] if r else "-", s["o2"])) in out
              and r is not None and r["state"] == "OPEN" and r["approval"]["head_sha"] == s["o2"] and r["approval"]["commits"] == 2)

        # 2. a branch cut from DEV is refused dev-overlap and writes nothing
        before = len(rows(env))
        rc, out, _err = add(env, "cand/laptop/dev-cut")
        check("a branch cut from DEV is refused dev-overlap (rc 3) and writes nothing",
              rc == 3 and "APPROVAL-REGISTER result=REFUSED reason=dev-overlap overlap=2 commits=3" in out
              and row_for(env, "cand/laptop/dev-cut") is None and len(rows(env)) == before)

        # 3. a missing branch is refused
        before = len(rows(env))
        rc, out, _err = add(env, "cand/laptop/no-such-branch")
        check("a missing branch is refused branch-not-found (rc 3) and writes nothing",
              rc == 3 and "reason=branch-not-found" in out and len(rows(env)) == before)

        # 4. an empty branch is refused
        before = len(rows(env))
        rc, out, _err = add(env, "cand/laptop/empty")
        check("an empty branch (no commits over PROD) is refused reason=empty (rc 3) and writes nothing",
              rc == 3 and "reason=empty" in out and row_for(env, "cand/laptop/empty") is None and len(rows(env)) == before)

        # 5. no --portal is refused
        before = len(rows(env))
        rc, out, _err = add(env, "cand/laptop/prod-cut", portal=None)
        check("no --portal is refused reason=portal-required (rc 3) and writes nothing",
              rc == 3 and "APPROVAL-REGISTER result=REFUSED reason=portal-required" in out and len(rows(env)) == before)

        # 6. a live FAST lease of this seat writes an APPROVED row, read back by approval-status
        lease_ok = env.lease("lease-ok.json")
        rc, out, _err = register_lease(env, "cand/laptop/lease-ok", lease_ok)
        rc2, line = status(env, "cand/laptop/lease-ok")
        r = row_for(env, "cand/laptop/lease-ok")
        check("a live lease for this seat writes an APPROVED row (approval-status APPROVED valid=yes)",
              rc == 0 and "APPROVAL-REGISTER result=OK" in out and "ruled_by=lease" in out and rc2 == 0
              and "state=APPROVED valid=yes" in line and "by=FAST lease lease-ok.json" in line and r is not None
              and r["state"] == "CLOSED" and r["closed"]["decision"] == "approved" and r["closed"]["ruled_by"] == "lease"
              and r["closed"]["ruling"].endswith("lease-ok.json") and r["approval"]["head_sha"] == s["o2"]
              and r["approval"]["commits"] == 2)

        # 7-9. an expired lease, a lease for another seat and a lease with mode HOLD are each refused and write nothing
        refused_cases = [
            ("an expired lease", env.lease("expired.json", expires_in=-60), SERIAL),
            ("a lease for another seat", env.lease("other-seat.json", seat=OTHER_SEAT), SERIAL),
            ("a lease with mode HOLD", env.lease("hold.json", mode="HOLD"), SERIAL),
        ]
        refused_ok = True
        for label, path, serial in refused_cases:
            before = len(rows(env))
            rc, out, _err = register_lease(env, "cand/laptop/lease-deny", path, serial=serial)
            refused_ok = refused_ok and rc == 3 and "APPROVAL-REGISTER result=REFUSED reason=lease-not-live" in out \
                and row_for(env, "cand/laptop/lease-deny") is None and len(rows(env)) == before
        check("an expired lease, a lease for another seat and a lease with mode HOLD are each refused and write nothing",
              refused_ok)

        # 10. a lease file that is absent is refused as not live
        rc, out, _err = register_lease(env, "cand/laptop/lease-deny", os.path.join(env.lease_dir, "absent.json"))
        check("a lease file that does not exist is refused lease-not-live (rc 3) and writes nothing",
              rc == 3 and "reason=lease-not-live" in out and row_for(env, "cand/laptop/lease-deny") is None)

        # 11. a live lease on a DEV-cut branch is refused dev-overlap, the same registration checks as add
        before = len(rows(env))
        rc, out, _err = register_lease(env, "cand/laptop/dev-cut", lease_ok)
        check("a live lease on a DEV-cut branch is refused dev-overlap (rc 3) and writes nothing",
              rc == 3 and "reason=dev-overlap overlap=2 commits=3" in out and len(rows(env)) == before)

        # 12. --check-only runs the checks, prints the register line, accepts any branch name, and writes nothing
        before = len(rows(env))
        rc_a, out_a, _e = add(env, "cand/laptop/prod-cut", check_only=True)
        rc_b, out_b, _e2 = add(env, "prod-cut", check_only=True)
        rc_c, out_c, _e3 = add(env, "cand/laptop/dev-cut", check_only=True)
        check("--check-only prints the same register line for a branch of any name, refuses the DEV cut, and writes nothing",
              rc_a == 0 and ("APPROVAL-REGISTER result=OK row=- head_sha=%s commits=2 check-only=yes" % s["o2"]) in out_a
              and rc_b == 0 and ("head_sha=%s commits=2" % s["o2"]) in out_b
              and rc_c == 3 and "reason=dev-overlap" in out_c and len(rows(env)) == before)
    finally:
        env.cleanup()

    fails = 0
    for label, ok in cases:
        print("  %s  %s" % ("PASS" if ok else "FAIL", label))
        fails += 0 if ok else 1
    print("OPEN-CALLS-REGISTER-TEST cases=%d/%d ok=%s" % (len(cases) - fails, len(cases), fails == 0))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
