"""MDPF_DEMQUE round 1, DQ-t-3 criterion AC2: the Yahoo ledger home comes from the builder (CLAUDE.md rule 30, PRD
C-HOMES). Calls `lib.opal_naming.address("yahoo","global","bronze","demand_ledger","dt=2026-10-09")` from the repo root.
At the base the builder REFUSES ("source 'yahoo' is not a systems.json key"); after the cell adds the `yahoo` VENDOR row
to infra/logic/registry/systems.json it returns an s3:// address ending `/yahoo/global/bronze/demand_ledger/dt=2026-10-09`.
HOME-OK <address>; else HOME-BAD <reason>. Control arm: the bloomberg address must resolve on both sides (a builder that
refuses everything fails here, not silently).
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.getcwd())

if __name__ == "__main__":
    try:
        from lib.opal_naming import address
    except Exception as e:  # noqa: BLE001
        print("HOME-BAD builder import failed: %r" % (e,))
        sys.exit(1)
    try:
        ctl = str(address("bloomberg", "global", "bronze", "demand_ledger", "dt=2026-10-09"))
    except Exception as e:  # noqa: BLE001
        print("HOME-BAD control arm refused (bloomberg): %r" % (e,))
        sys.exit(1)
    try:
        got = str(address("yahoo", "global", "bronze", "demand_ledger", "dt=2026-10-09"))
    except Exception as e:  # noqa: BLE001
        print("HOME-BAD yahoo refused: %r (control ok: %s)" % (e, ctl))
        sys.exit(1)
    if not (got.startswith("s3://") and got.endswith("/yahoo/global/bronze/demand_ledger/dt=2026-10-09")):
        print("HOME-BAD unexpected address %s" % got)
        sys.exit(1)
    print("HOME-OK %s (control %s)" % (got, ctl))
    sys.exit(0)
