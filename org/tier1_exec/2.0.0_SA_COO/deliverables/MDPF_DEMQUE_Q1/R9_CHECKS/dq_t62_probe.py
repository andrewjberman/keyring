"""MDPF_DEMQUE round 9, DQ-t-62 criterion AC2 (ONE live Yahoo request on a scratch pacer; nothing written outside .scratch/).

`yahoo_pull.py --probe BRKB` must print a line `PROBE symbol=BRKB status=OK rows=<n> ...` with n >= 1000: the symbol is reported AS GIVEN (BRKB, the key the store and the pacer use) while the request goes to Yahoo in its dash form BRK-B
(row: the 2026-10-13 run recorded BRKB FAILED_EMPTY and BRK-B OK; the store's Berkshire B lock carries symbol BRKB and sat at valid_to 2026-06-22).
PROBE-OK; else PROBE-BAD <why>.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "yahoo_pull.py")


def main() -> int:
    os.makedirs(".scratch", exist_ok=True)
    r = subprocess.run([sys.executable, TOOL, "--probe", "BRKB"], capture_output=True, text=True, timeout=90, check=False)
    line = next((x for x in r.stdout.splitlines() if x.startswith("PROBE ")), "")
    print(line or (r.stderr or r.stdout)[-240:])
    m = re.match(r"PROBE symbol=(\S+) status=(\S+) rows=(\d+)", line)
    if r.returncode != 0 or not m:
        print("PROBE-BAD no probe line, rc=%d" % r.returncode)
        return 1
    sym, status, rows = m.group(1), m.group(2), int(m.group(3))
    if sym != "BRKB" or status != "OK" or rows < 1000:
        print("PROBE-BAD symbol=%s status=%s rows=%d (need BRKB, OK, >= 1000)" % (sym, status, rows))
        return 1
    print("PROBE-OK BRKB pulled through its Yahoo dash form: %d rows" % rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
