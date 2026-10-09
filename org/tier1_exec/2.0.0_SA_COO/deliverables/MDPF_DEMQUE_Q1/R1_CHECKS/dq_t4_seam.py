"""MDPF_DEMQUE round 1, DQ-t-4 criterion AC2: the seam against the REAL neighbour -- Cottonwood's live silver
transactions in opal-data-cot, the input `build_canonical_prices_v2.py` builds its asset spine from. Runs
`python data/mdpf/scripts/demque/land_cot.py --probe` (read-only), which must print:
  PROBE rows=<n> assets=<m> join_key=<cusip|symbol|asset_name-only> hist_exists=<yes|no> lookup_exists=<yes|no>
LSEAM-OK when rc 0, rows > 0, assets > 0 and join_key is one of the three names; else LSEAM-BAD.
"""
from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_file import run_cli  # noqa: E402

if __name__ == "__main__":
    rc, out = run_cli([os.path.join("data", "mdpf", "scripts", "demque", "land_cot.py"), "--probe"])
    print(out[-3000:])
    m = re.search(r"^PROBE rows=(\d+) assets=(\d+) join_key=(cusip|symbol|asset_name-only) hist_exists=(yes|no) "
                  r"lookup_exists=(yes|no)", out, re.M)
    if rc != 0 or not m or int(m.group(1)) == 0 or int(m.group(2)) == 0:
        print("LSEAM-BAD rc=%d" % rc)
        sys.exit(1)
    print("LSEAM-OK " + m.group(0))
    sys.exit(0)
