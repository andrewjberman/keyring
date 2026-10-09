"""IRPT_BCKEND round 34 (workstream ~M, issuer 2.0.0_SA_COO~M2) -- checks of cell IB-mp-341: the production publication_for port
(CTO msg 2127; ~Y2's CUSTODY_PORT_CONTRACT.md @859ae01405 port 2) for _scope/accepted_custody.py AcceptedCustodyReader.

Usage: python <this file> <repo_root> <criterion_id>
Prints "<id> PASS" or "<id> FAIL" as the last line. Every check finishes inside 120 s.

  IBM34-341-AC1  holdings/snapshot.py exposes holdings_publication_for(s3_client=None). Its publication_for(firm):
                 (a) returns a production-namespace HoldingsPublication bound to that firm, for each of the 3 canonical firms,
                     with no S3 call at construction;
                 (b) refuses "ALL", "", None, 7 and an unknown firm with PublicationRefused;
                 (c) over the in-memory versioned S3 of holdings/tests/test_publication.py: capture() then load_pinned(receipt)
                     returns the reader's shapes -- document.scope.firm_id == firm, manifest.firm_id == firm,
                     manifest.revision == receipt.date_row.revision, manifest.business_date == receipt.business_date -- and the
                     pinned reload is equal to the captured (document, manifest). Base: FAIL (the function does not exist).
  IBM34-341-AC2  the holdings and _scope suites pass (pytest -q tests in each). Base: PASS (a control).
  IBM34-G-201    A GUARD: worker ~201's workspace commits touch only its grant. Base: PASS.
"""
import importlib
import json
import re
import subprocess
import sys
from pathlib import Path

BASE = "6066a7d5cb"
P = "org/missions/D9/IRPT/IRPT_BCKEND"
LAMBDA = "infra/aws/lambda/investor-reporting"
GRANT = (LAMBDA + "/holdings/snapshot.py", LAMBDA + "/holdings/tests/test_publication_port.py",
         P + "/surprise-channel/investigations/INVESTIGATION_v1.md", P + "/task-orders/IRPT_BCKEND.TO-IB-m34-341.",
         P + "/deliverables/0.9.0_WK_IRPT_BCKEND~201/")
FIRMS = ("49financial", "cottonwood", "inflection")


def _ac1(root):
    holdings = root / LAMBDA / "holdings"
    for p in (str(root / "lib"), str(holdings), str(holdings / "tests")):
        if p not in sys.path:
            sys.path.insert(0, p)
    snapshot = importlib.import_module("snapshot")
    publication = importlib.import_module("publication")
    fixture = importlib.import_module("test_publication")
    factory = getattr(snapshot, "holdings_publication_for", None)
    if not callable(factory):
        return "snapshot.holdings_publication_for does not exist"

    class NoCall:
        def __getattr__(self, name):
            raise AssertionError("S3 called at construction: " + name)

    port = factory(NoCall())
    for firm in FIRMS:
        pub = port(firm)
        if type(pub).__name__ != "HoldingsPublication" or pub.firm != firm or pub.table != "holdings":
            return "publication_for(%r) is not a production HoldingsPublication for that firm" % firm
    for bad in ("ALL", "", None, 7, "acme"):
        try:
            port(bad)
            return "publication_for(%r) was not refused" % (bad,)
        except publication.PublicationRefused:
            pass
    s3, store = fixture.setup()
    fixture.publish(store)
    pub = factory(s3)("49financial")
    doc, manifest, receipt = pub.capture(as_of=None, account_ids=None)
    wire = json.loads(json.dumps(receipt))
    if (doc.get("scope", {}).get("firm_id") != "49financial" or manifest.get("firm_id") != "49financial"
            or manifest.get("revision") != receipt["date_row"]["revision"]
            or manifest.get("business_date") != receipt["business_date"]):
        return "capture() shapes do not meet the reader's rules"
    again = factory(s3)("49financial").load_pinned(wire, account_ids=None)
    if json.dumps(again, sort_keys=True, default=str) != json.dumps((doc, manifest), sort_keys=True, default=str):
        return "load_pinned(receipt) did not reload the captured document and manifest"
    return None


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    cid = sys.argv[2] if len(sys.argv) > 2 else ""

    def fail(msg):
        print("FAIL: " + msg)
        print("%s FAIL" % (cid or "IBM34"))
        sys.exit(1)

    if cid == "IBM34-341-AC1":
        try:
            err = _ac1(root)
        except Exception as exc:  # noqa: BLE001 -- any failure grades FAIL with its reason
            err = "%s: %s" % (type(exc).__name__, exc)
        if err:
            fail(err)
        print("OK: holdings_publication_for fences 3 of 3 firms, refuses 5 of 5 bad firms, capture/load_pinned meet the reader")
    elif cid == "IBM34-341-AC2":
        for sub in ("holdings", "_scope"):
            r = subprocess.run([sys.executable, "-m", "pytest", "-q", "tests"], cwd=str(root / LAMBDA / sub),
                               capture_output=True, timeout=110)
            out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout.decode("utf-8", "replace"))
            last = [ln for ln in out.splitlines() if ln.strip()][-1:] or ["(no output)"]
            if r.returncode:
                fail("%s suite rc %d: %s" % (sub, r.returncode, last[0]))
            print("OK: %s %s" % (sub, last[0]))
    elif cid == "IBM34-G-201":
        r = subprocess.run(["git", "log", "%s..HEAD" % BASE, "--author=0.9.0_WK_IRPT_BCKEND~201", "--name-only", "--format="],
                           cwd=str(root), capture_output=True)
        changed = sorted(set(ln for ln in r.stdout.decode("utf-8").splitlines() if ln.strip()))
        bad = [c for c in changed if not c.startswith(GRANT)]
        if bad:
            fail("out-of-grant changes: %s" % bad[:8])
        print("OK: %d changed path(s), all inside slot ~201's grant" % len(changed))
    else:
        fail("unknown criterion %r" % cid)
    print("%s PASS" % cid)


if __name__ == "__main__":
    main()
