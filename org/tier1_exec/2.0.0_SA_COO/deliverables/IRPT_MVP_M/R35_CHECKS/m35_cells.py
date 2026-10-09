"""IRPT_BCKEND round 35 (workstream ~M, issuer 2.0.0_SA_COO~M2) -- checks of cell IB-mp-351: the publication_for port moves to a
standalone module, so irpt-ycharts-generate can stage it beside its own ycharts/extract/publication.py (~Y2 msg 2202).

Usage: python <this file> <repo_root> <criterion_id>
Prints "<id> PASS" or "<id> FAIL" as the last line. Every check finishes inside 120 s.

  IBM35-351-AC1  infra/aws/lambda/investor-reporting/holdings/holdings_publication_port.py exists and exposes
                 holdings_publication_for(s3_client=None); in a fresh interpreter whose path holds ONLY a temp dir staged the way
                 irpt-ycharts-generate stages it (the port module, holdings/publication.py AS holdings_publication.py, and
                 ycharts/extract/publication.py AS publication.py) plus lib/ and ycharts/extract (its siblings), the port imports, publication_for("cottonwood") returns
                 the HoldingsPublication class of the holdings_publication module (production table "holdings"), and "ALL" is
                 refused; snapshot.py no longer defines holdings_publication_for. Base: FAIL (the module does not exist).
  IBM35-351-AC2  the holdings and _scope suites pass. Base: PASS (a control).
  IBM35-G-202    A GUARD: worker ~202's workspace commits touch only its grant. Base: PASS.
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = "d968ed5db5"
P = "org/missions/D9/IRPT/IRPT_BCKEND"
LAMBDA = "infra/aws/lambda/investor-reporting"
GRANT = (LAMBDA + "/holdings/holdings_publication_port.py", LAMBDA + "/holdings/snapshot.py",
         LAMBDA + "/holdings/tests/test_publication_port.py",
         P + "/surprise-channel/investigations/INVESTIGATION_v1.md", P + "/task-orders/IRPT_BCKEND.TO-IB-m35-351.",
         P + "/deliverables/0.9.0_WK_IRPT_BCKEND~202/")

PROBE = r'''
import sys
sys.path[:0] = [sys.argv[1], sys.argv[2], sys.argv[3]]
import holdings_publication_port as port
import holdings_publication as hp
import publication as yp
assert not hasattr(yp, "HoldingsPublication"), "the staged publication.py is not ycharts' module"
class NoCall:
    def __getattr__(self, name):
        raise AssertionError("S3 called at construction: " + name)
pub = port.holdings_publication_for(NoCall())("cottonwood")
assert type(pub) is hp.HoldingsPublication and pub.table == "holdings" and pub.firm == "cottonwood", "wrong class or namespace"
try:
    port.holdings_publication_for(NoCall())("ALL")
    raise SystemExit("ALL was not refused")
except hp.PublicationRefused:
    pass
print("STAGED-OK")
'''


def _ac1(root):
    lam = root / LAMBDA
    mod = lam / "holdings" / "holdings_publication_port.py"
    if not mod.is_file():
        return "holdings/holdings_publication_port.py does not exist"
    if re.search(r"^def holdings_publication_for\b", (lam / "holdings" / "snapshot.py").read_text(encoding="utf-8"), re.M):
        return "snapshot.py still defines holdings_publication_for"
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(mod, Path(tmp) / "holdings_publication_port.py")
        shutil.copy(lam / "holdings" / "publication.py", Path(tmp) / "holdings_publication.py")
        shutil.copy(lam / "ycharts" / "extract" / "publication.py", Path(tmp) / "publication.py")
        probe = Path(tmp) / "_probe.py"
        probe.write_text(PROBE, encoding="utf-8")
        r = subprocess.run([sys.executable, "-I", str(probe), tmp, str(root / "lib"), str(lam / "ycharts" / "extract")], capture_output=True, timeout=110,
                           cwd=tmp)
        out = (r.stdout + r.stderr).decode("utf-8", "replace")
        if r.returncode or "STAGED-OK" not in out:
            return "staged import failed: " + " | ".join(out.strip().splitlines()[-3:])
    return None


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    cid = sys.argv[2] if len(sys.argv) > 2 else ""

    def fail(msg):
        print("FAIL: " + msg)
        print("%s FAIL" % (cid or "IBM35"))
        sys.exit(1)

    if cid == "IBM35-351-AC1":
        try:
            err = _ac1(root)
        except Exception as exc:  # noqa: BLE001 -- any failure grades FAIL with its reason
            err = "%s: %s" % (type(exc).__name__, exc)
        if err:
            fail(err)
        print("OK: the port imports beside ycharts' publication.py, binds holdings_publication.HoldingsPublication, refuses ALL")
    elif cid == "IBM35-351-AC2":
        for sub in ("holdings", "_scope"):
            r = subprocess.run([sys.executable, "-m", "pytest", "-q", "tests"], cwd=str(root / LAMBDA / sub),
                               capture_output=True, timeout=110)
            out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout.decode("utf-8", "replace"))
            last = [ln for ln in out.splitlines() if ln.strip()][-1:] or ["(no output)"]
            if r.returncode:
                fail("%s suite rc %d: %s" % (sub, r.returncode, last[0]))
            print("OK: %s %s" % (sub, last[0]))
    elif cid == "IBM35-G-202":
        r = subprocess.run(["git", "log", "%s..HEAD" % BASE, "--author=0.9.0_WK_IRPT_BCKEND~202", "--name-only", "--format="],
                           cwd=str(root), capture_output=True)
        changed = sorted(set(ln for ln in r.stdout.decode("utf-8").splitlines() if ln.strip()))
        bad = [c for c in changed if not c.startswith(GRANT)]
        if bad:
            fail("out-of-grant changes: %s" % bad[:8])
        print("OK: %d changed path(s), all inside slot ~202's grant" % len(changed))
    else:
        fail("unknown criterion %r" % cid)
    print("%s PASS" % cid)


if __name__ == "__main__":
    main()
