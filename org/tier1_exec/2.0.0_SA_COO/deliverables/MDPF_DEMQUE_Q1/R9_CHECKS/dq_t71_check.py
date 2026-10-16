"""MDPF_DEMQUE round 9, DQ-t-71 criterion AC2 (local, no network, no S3): the Yahoo pacer's daily cap is 600 everywhere the draw and its quotes count it.
PACER-OK when: yahoo_pull.Pacer(<temp state>).daily_cap == 600; extend_frontier.DAILY_CAP == 600 and extend_frontier._request_cap() == 580;
inactive_request.DAILY_CAP == 600; daily_draw.py builds its Pacer with the default cap (the source holds `yp.Pacer(state)` once and no `daily_cap=` argument on it).
Else PACER-BAD <why>."""
from __future__ import annotations

import os
import re
import sys
import tempfile

HERE = os.path.join("data", "mdpf", "scripts", "demque")
sys.path.insert(0, HERE)
sys.path.insert(0, os.getcwd())


def main() -> int:
    import extend_frontier as xf
    import inactive_request as ir
    import yahoo_pull as yp

    d = tempfile.mkdtemp(prefix="dq_t71_")
    got = yp.Pacer(os.path.join(d, "pacer.json")).daily_cap
    if got != 600:
        print("PACER-BAD Pacer default daily_cap is %r, not 600" % (got,))
        return 1
    if xf.DAILY_CAP != 600 or xf._request_cap() != 580:
        print("PACER-BAD extend_frontier DAILY_CAP %r and request cap %r, not 600 and 580" % (xf.DAILY_CAP, xf._request_cap()))
        return 1
    if ir.DAILY_CAP != 600:
        print("PACER-BAD inactive_request DAILY_CAP is %r, not 600" % (ir.DAILY_CAP,))
        return 1
    src = open(os.path.join(HERE, "daily_draw.py"), encoding="utf-8").read()
    if len(re.findall(r"yp\.Pacer\(state\)", src)) != 1 or re.search(r"Pacer\([^)]*daily_cap", src):
        print("PACER-BAD daily_draw.py does not build its Pacer once with the default cap")
        return 1
    print("PACER-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
