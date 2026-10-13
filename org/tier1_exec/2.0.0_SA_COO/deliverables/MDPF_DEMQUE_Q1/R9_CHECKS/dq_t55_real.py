"""MDPF_DEMQUE round 9, DQ-t-55 criterion AC2 (read only, no vendor call, nothing written).

`surface_e_intake.py --cost --securities 1 --trading-days 252 --fields 2 --day D` prints ONE JSON line
{"day", "history_allowance", "cap", "cells", "verdict": "ACCEPT"|"REFUSE", "message"}.
Required: history_allowance is the allowance file's MEASURED history ceiling (an int > 0, read from bbg_allowance.json, 5,858 at the time of the order);
cap == floor(0.10 * history_allowance); cells == 504; verdict is REFUSE exactly when cells > cap; a REFUSE message names the cap and the words "refused at intake".
`--check --cells 100 --day D` must print verdict ACCEPT; `--check --cells <cap + 1> --day D` must print REFUSE naming the cap.
CAP-REAL-OK; else CAP-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "surface_e_intake.py")
ALLOWANCE = os.path.join("data", "mdpf", "scripts", "demque", "bbg_allowance.json")


def _bad(why):
    print("CAP-REAL-BAD " + why)
    return 1


def _run(args):
    r = subprocess.run([sys.executable, TOOL] + args, capture_output=True, text=True, timeout=55, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip())
    return json.loads(ls[-1]), ""


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    ceiling = json.load(open(ALLOWANCE, encoding="utf-8"))["history"]["ceiling"]["value"]
    a, e = _run(["--cost", "--securities", "1", "--trading-days", "252", "--fields", "2", "--day", "2026-10-14"])
    if a is None:
        return _bad("cost " + e)
    print(json.dumps(a, sort_keys=True)[:420])
    al, cap = a.get("history_allowance"), a.get("cap")
    ok = (isinstance(al, int) and al == ceiling and cap == (al * 10) // 100 and a.get("cells") == 504
          and a.get("verdict") == ("REFUSE" if 504 > cap else "ACCEPT")
          and (a.get("verdict") != "REFUSE" or ("refused at intake" in str(a.get("message")) and str(cap) in str(a.get("message")))))
    if not ok:
        return _bad("cost line does not satisfy the cap rule against the measured ceiling %s" % ceiling)
    b, e = _run(["--check", "--cells", "100", "--day", "2026-10-14"])
    if b is None:
        return _bad("check100 " + e)
    over, e = _run(["--check", "--cells", str(cap + 1), "--day", "2026-10-14"])
    if over is None:
        return _bad("checkover " + e)
    print("check 100 cells: %s | check %d cells: %s" % (b.get("verdict"), cap + 1, over.get("verdict")))
    if b.get("verdict") != "ACCEPT" or over.get("verdict") != "REFUSE" or str(cap) not in str(over.get("message")):
        return _bad("the accept or refuse side of the cap is wrong")
    print("CAP-REAL-OK cap %d cells of a %d-cell day; a one-security one-year two-field request (504 cells) is %s" % (cap, al, a["verdict"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
