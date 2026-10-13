"""MDPF_DEMQUE round 9, DQ-t-48 criterion AC2 (REAL price index, S3 read only, NO vendor call, nothing written): `incremental_plan.py --plan` prints ONE JSON
line {"frontier", "names", "incremental", "refill_gap", "refill_split", "requests", "cells_full_repull", "cells_incremental", "window_trading_days"}.
Required: window_trading_days == 5; incremental + refill_gap + refill_split == names; requests == names (one request per name, the Yahoo request count does not rise);
names >= 140; cells_incremental * 5 <= cells_full_repull (the writes are at least five times smaller). INCPLAN-OK; else INCPLAN-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "incremental_plan.py")


def _bad(why):
    print("INCPLAN-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    r = subprocess.run([sys.executable, TOOL, "--plan"], capture_output=True, text=True, timeout=115, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return _bad("rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip()))
    d = json.loads(ls[-1])
    print(json.dumps({k: d.get(k) for k in ("frontier", "names", "incremental", "refill_gap", "refill_split", "requests", "cells_full_repull",
                                           "cells_incremental", "window_trading_days")}, sort_keys=True))
    ints = all(isinstance(d.get(k), int) for k in ("names", "incremental", "refill_gap", "refill_split", "requests", "cells_full_repull",
                                                   "cells_incremental", "window_trading_days"))
    arms = {
        "ints": ints,
        "window": ints and d["window_trading_days"] == 5,
        "partition": ints and d["incremental"] + d["refill_gap"] + d["refill_split"] == d["names"],
        "requests": ints and d["requests"] == d["names"],
        "names": ints and d["names"] >= 140,
        "smaller": ints and d["cells_incremental"] * 5 <= d["cells_full_repull"],
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms=" + ",".join(bad))
    print("INCPLAN-OK %d names, %d requests (unchanged), writes %d cells instead of %d" % (d["names"], d["requests"], d["cells_incremental"], d["cells_full_repull"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
