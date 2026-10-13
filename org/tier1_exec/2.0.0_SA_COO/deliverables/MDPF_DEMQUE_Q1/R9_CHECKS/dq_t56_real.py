"""MDPF_DEMQUE round 9, DQ-t-56 criterion AC2 (REAL request files, read only, NO Bloomberg call, nothing written).

Three arms, each one command; every arm must hold.
  (1) `standing_drawer.py --open` prints ONE JSON line {"open": [request ids in draw order], "not_drawable": [{"request_id","why"}]}. `open` must name
      DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS, MDPF_SECHIST-CARD-A-B1-OPTION-C, MDPF_SECHIST-CARD-A-PORTING-TEST and MDPF_SECHIST-CARD-A-B1-FUND-TYPE; B1 and the porting test come
      BEFORE the TR comparison (tier 2 before tier 4), and every not-drawable request carries a reason.
  (2) `standing_drawer.py --plan --request MDPF_SECHIST-CARD-A-B1-OPTION-C` prints {"request_id","remaining_cells","securities","identifier_forms"}: remaining_cells equals the cells
      `bbg_quote.py --quote` prices for the same file (nothing drawn yet); securities >= 600; identifier_forms is a dict whose values sum to securities.
  (3) `standing_drawer.py --plan --request MDPF_SECHIST-CARD-A-B1-FUND-TYPE` prints remaining_cells == 227 and channel "reference"; and the porting test plans remaining_cells equal to its quote.
DRAWER-REAL-OK; else DRAWER-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

D = os.path.join("data", "mdpf", "scripts", "demque")
REQ = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "requests")


def _line(cmd, timeout=40):
    r = subprocess.run([sys.executable] + cmd, capture_output=True, text=True, timeout=timeout, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-260:].strip())
    return json.loads(ls[-1]), ""


def _bad(why):
    print("DRAWER-REAL-BAD " + why)
    return 1


def _quote_cells(rid):
    q, e = _line([os.path.join(D, "bbg_quote.py"), "--quote", os.path.join(REQ, rid + ".json")])
    if q is None:
        return None
    cells = q.get("cells") or {}
    return sum(v for v in cells.values() if isinstance(v, int))


def main() -> int:
    a, e = _line([os.path.join(D, "standing_drawer.py"), "--open"])
    if a is None:
        return _bad("arm1 " + e)
    ids = a.get("open") or []
    print("arm1 open=%s not_drawable=%d" % (ids, len(a.get("not_drawable") or [])))
    need = ["MDPF_SECHIST-CARD-A-B1-OPTION-C", "MDPF_SECHIST-CARD-A-PORTING-TEST", "MDPF_SECHIST-CARD-A-B1-FUND-TYPE", "DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS"]
    if not all(n in ids for n in need):
        return _bad("arm1 open list lacks one of %s" % need)
    if not (ids.index("MDPF_SECHIST-CARD-A-B1-OPTION-C") < ids.index("DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS")
            and ids.index("MDPF_SECHIST-CARD-A-PORTING-TEST") < ids.index("DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS")):
        return _bad("arm1 tier order: B1 and the porting test must precede the TR comparison")
    if not all(isinstance(x, dict) and x.get("why") for x in a.get("not_drawable") or []):
        return _bad("arm1 a not-drawable request carries no reason")
    b, e = _line([os.path.join(D, "standing_drawer.py"), "--plan", "--request", "MDPF_SECHIST-CARD-A-B1-OPTION-C"])
    if b is None:
        return _bad("arm2 " + e)
    qc = _quote_cells("MDPF_SECHIST-CARD-A-B1-OPTION-C")
    forms = b.get("identifier_forms") or {}
    print("arm2 B1 remaining=%s quote=%s securities=%s forms=%s" % (b.get("remaining_cells"), qc, b.get("securities"), forms))
    if not (isinstance(qc, int) and b.get("remaining_cells") == qc and isinstance(b.get("securities"), int) and b["securities"] >= 600
            and isinstance(forms, dict) and sum(forms.values()) == b["securities"]):
        return _bad("arm2 B1 plan does not equal its quote or the identifier forms do not add up")
    c, e = _line([os.path.join(D, "standing_drawer.py"), "--plan", "--request", "MDPF_SECHIST-CARD-A-B1-FUND-TYPE"])
    if c is None:
        return _bad("arm3a " + e)
    p, e = _line([os.path.join(D, "standing_drawer.py"), "--plan", "--request", "MDPF_SECHIST-CARD-A-PORTING-TEST"])
    if p is None:
        return _bad("arm3b " + e)
    pq = _quote_cells("MDPF_SECHIST-CARD-A-PORTING-TEST")
    print("arm3 fund-type remaining=%s channel=%s | porting remaining=%s quote=%s" % (c.get("remaining_cells"), c.get("channel"), p.get("remaining_cells"), pq))
    if not (c.get("remaining_cells") == 227 and c.get("channel") == "reference" and isinstance(pq, int) and p.get("remaining_cells") == pq):
        return _bad("arm3 fund-type or porting-test plan does not equal its quote")
    print("DRAWER-REAL-OK the drawer plans B1 (%d cells), the porting test (%d) and the fund-type check (227) and orders them before the TR comparison" % (qc, pq))
    return 0


if __name__ == "__main__":
    sys.exit(main())
