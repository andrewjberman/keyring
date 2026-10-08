"""IRPT_BCKEND round 33 (workstream ~M, issuer 2.0.0_SA_COO~M2) -- checks of cell IB-mw-331 (row S388, the HoldingsSnapshot share).

The schema moved: docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json changed at e62 (01e843ce2e, sha256 7c221b13...),
and portal a6868784 hand-edited the wire type's class enum to match without regenerating it, so the committed header still names the
10-02 schema (0236991c...). The body already equals the generator's output; one header line drifts.

Usage: python <this file> <repo_root> <criterion_id>
Prints "<id> PASS" or "<id> FAIL" as the last line. Every check finishes inside 120 s.

  IBM33-331-AC1  in portal/: one run of the wire-regen test leaves HoldingsSnapshot.ts byte-unchanged (it equals the generator's
                 output from the schema at HEAD), its header names the schema's sha256 at HEAD, and the branch's diff against portal
                 DEV under contracts/wire names only HoldingsSnapshot.ts. Base (portal DEV 1cbc56a7): FAIL (the run rewrites it).
  IBM33-331-AC2  in portal/: tsc -b --noEmit exits 0. Base: PASS (a control).
  IBM33-G-200    A GUARD: worker ~200's workspace commits touch only its grant, never the portal gitlink. Base: PASS.
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

BASE = "0210ff5d27"
DEV = "1cbc56a7"
P = "org/missions/D9/IRPT/IRPT_BCKEND"
WIRE = "src/pages/InvestorReporting/contracts/wire"
MINE = WIRE + "/HoldingsSnapshot.ts"
SCHEMA = "docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json"
REGEN = "src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.wire-regen.test.ts"
GRANT = (P + "/surprise-channel/investigations/INVESTIGATION_v1.md", P + "/task-orders/IRPT_BCKEND.TO-IB-m33-331.",
         P + "/deliverables/0.9.0_WK_IRPT_BCKEND~200/")


def _run(cmd, cwd, timeout=110):
    r = subprocess.run(cmd, cwd=str(cwd), capture_output=True, timeout=timeout)
    out = (r.stdout or b"").decode("utf-8", "replace") + (r.stderr or b"").decode("utf-8", "replace")
    return r.returncode, re.sub(r"\x1b\[[0-9;]*m", "", out)


def _last(out):
    lines = [ln for ln in out.splitlines() if ln.strip()]
    return lines[-1] if lines else "(no output)"


def _changed(portal, paths):
    _, out = _run(["git", "diff", "--numstat", "--", *paths], portal)
    return [ln.split("\t")[-1] for ln in out.splitlines() if ln.strip() and not ln.startswith("warning")
            and (lambda a: a[0] != "0" or a[1] != "0")(ln.split("\t"))]


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    cid = sys.argv[2] if len(sys.argv) > 2 else ""
    portal = root / "portal"

    def fail(msg):
        print("FAIL: " + msg)
        print("%s FAIL" % (cid or "IBM33"))
        sys.exit(1)

    if cid == "IBM33-331-AC1":
        if _changed(portal, [WIRE]):
            fail("contracts/wire has uncommitted content changes before the run; commit or restore first")
        _run(["bun", "--no-install", "test", REGEN], portal, timeout=115)
        drifted = _changed(portal, [MINE])
        _run(["git", "checkout", "--", WIRE], portal)
        if drifted:
            fail("one regeneration rewrites HoldingsSnapshot.ts")
        want = hashlib.sha256((root / SCHEMA).read_bytes()).hexdigest()
        head = (portal / MINE).read_text(encoding="utf-8")
        if ("Source sha256: " + want) not in head:
            fail("HoldingsSnapshot.ts header does not name the schema's sha256 at HEAD (%s)" % want[:12])
        _, names = _run(["git", "diff", "--name-only", DEV, "HEAD", "--", WIRE], portal)
        touched = sorted(n for n in names.splitlines() if n.strip() and not n.startswith("warning"))
        extra = [n for n in touched if n != MINE]
        if extra:
            fail("the branch changes wire files other than HoldingsSnapshot.ts: %s" % extra)
        print("OK: HoldingsSnapshot.ts equals the generator's output (schema sha256 %s); branch touches %d wire file(s)"
              % (want[:12], len(touched)))
    elif cid == "IBM33-331-AC2":
        rc, out = _run(["node", "node_modules/typescript/bin/tsc", "-b", "--noEmit"], portal, timeout=115)
        if rc:
            fail("tsc -b --noEmit rc %d: %s" % (rc, _last(out)))
        print("OK: tsc -b --noEmit rc 0")
    elif cid == "IBM33-G-200":
        r = subprocess.run(["git", "log", "%s..HEAD" % BASE, "--author=0.9.0_WK_IRPT_BCKEND~200", "--name-only", "--format="],
                           cwd=str(root), capture_output=True)
        changed = sorted(set(ln for ln in r.stdout.decode("utf-8").splitlines() if ln.strip()))
        bad = [c for c in changed if not c.startswith(GRANT) or c == "portal"]
        if bad:
            fail("out-of-grant changes (the portal gitlink is never committed): %s" % bad[:8])
        print("OK: %d changed path(s), all inside slot ~200's grant" % len(changed))
    else:
        fail("unknown criterion %r" % cid)
    print("%s PASS" % cid)


if __name__ == "__main__":
    main()
