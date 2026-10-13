"""MDPF_DEMQUE round 9, DQ-t-50 criterion AC2 (REAL silver transactions, holdings snapshot and ADVI request, S3 read only, NO vendor call, writes only the scratch path it is
given): `b1_request.py --build --out <scratch.json>` prints ONE JSON line {"securities", "priced_names", "skipped_one_dollar", "unread_pulled", "total_return_names", "funds_joined",
"cells", "days_to_finish", "finish_date", "claim", "window_start"} and writes the request. Required: total_return_names == 11; funds_joined == 8 and each of the 8 fund CUSIPs'
entries starts on or after 2020-07-06; window_start on or after 2012-01-01; priced_names + skipped_one_dollar == 606 + 0 (the 606 priced P1 names) and securities ==
priced_names - skipped_one_dollar + funds_joined; cells between 15,000 and 45,000 (option C, about 35k plus 2.5k plus the funds); the request validates under
`bbg_quote._validate`; no key naming an account; two runs write byte-identical files. B1-REAL-OK; else B1-REAL-BAD <why>.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "b1_request.py")
FUNDS = {"ABNFX", "AGTHX", "BALCX", "MEIIX", "NFFFX", "PRILX", "VEIRX", "VGHAX"}


def _bad(why):
    print("B1-REAL-BAD " + why)
    return 1


def _run(out):
    r = subprocess.run([sys.executable, TOOL, "--build", "--out", out], capture_output=True, text=True, timeout=55, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip())
    return json.loads(ls[-1]), ""


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    d = tempfile.mkdtemp(prefix="dq_t50_")
    o1, o2 = os.path.join(d, "a.json"), os.path.join(d, "b.json")
    a, e = _run(o1)
    if a is None:
        return _bad("run1 " + e)
    b, e = _run(o2)
    if b is None:
        return _bad("run2 " + e)
    print(json.dumps(a, sort_keys=True))
    same = hashlib.sha256(open(o1, "rb").read()).hexdigest() == hashlib.sha256(open(o2, "rb").read()).hexdigest()
    req = json.load(open(o1, encoding="utf-8"))
    sys.path.insert(0, os.path.join("data", "mdpf", "scripts", "demque"))
    try:
        import bbg_quote
        bbg_quote._validate(req)
        valid = True
    except Exception as exc:  # noqa: BLE001
        print("validate: %s" % str(exc)[:200])
        valid = False
    ints = all(isinstance(a.get(k), int) for k in ("securities", "priced_names", "skipped_one_dollar", "total_return_names", "funds_joined", "cells"))
    fund_ok = False
    if ints:
        rows = [s for s in req.get("securities") or [] if isinstance(s, dict) and s.get("symbol") in FUNDS]
        fund_ok = a["funds_joined"] == 8 and len({s.get("cusip") for s in rows}) == 8 and all(
            (s.get("start") or (s.get("dates") or ["9999"])[0]) >= "2020-07-06" for s in rows)
    arms = {
        "ints": ints,
        "tr": ints and a["total_return_names"] == 11,
        "funds": fund_ok,
        "floor": isinstance(a.get("window_start"), str) and a["window_start"] >= "2012-01-01",
        "names": ints and a["priced_names"] == 606 and a["securities"] == a["priced_names"] - a["skipped_one_dollar"] + a["funds_joined"],
        "cells": ints and 15000 <= a["cells"] <= 45000,
        "valid": valid,
        "deterministic": same,
        "no_account_key": "account" not in json.dumps(req).lower(),
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms=" + ",".join(bad))
    print("B1-REAL-OK %d securities, %d cells, %s days to finish, %d one-dollar funds skipped, %d unread pulled" % (
        a["securities"], a["cells"], a.get("days_to_finish"), a["skipped_one_dollar"], a.get("unread_pulled") or 0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
