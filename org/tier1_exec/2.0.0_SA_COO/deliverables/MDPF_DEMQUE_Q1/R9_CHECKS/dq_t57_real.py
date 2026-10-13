"""MDPF_DEMQUE round 9, DQ-t-57 criterion AC2 (REAL active-set file or its commit, S3 read only, NO vendor call, writes only the scratch path it is given).

Arm 1: `active_set.py --census` prints ONE JSON line {"sha256_ok", "accounts", "securities", "windows", "open_held"} with sha256_ok true, accounts 769, securities 3357,
windows >= 3300 and open_held >= 1. The line carries counts only: no key containing "account_key" and no account number.
Arm 2: `b1_request.py --build --out <scratch>` prints the B1 line with "securities" 613 (the 606 priced P1 names plus the 7 of the 8 funds that are P1; the P2 fund held back),
"clipped_cusips" >= 90, "held_back" >= 1, and "cells" between 33,000 and 35,500 and strictly below 37,439 (the filed request before the active windows).
Arm 3: a second `--build` writes a byte-identical file; the written request validates under `bbg_quote._validate`; no entry starts before 2012-01-01; no key naming an account.
WIN-REAL-OK; else WIN-REAL-BAD <why>.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile

D = os.path.join("data", "mdpf", "scripts", "demque")


def _line(cmd, timeout=55):
    r = subprocess.run([sys.executable] + cmd, capture_output=True, text=True, timeout=timeout, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-260:].strip())
    return json.loads(ls[-1]), ""


def _bad(why):
    print("WIN-REAL-BAD " + why)
    return 1


def main() -> int:
    a, e = _line([os.path.join(D, "active_set.py"), "--census"])
    if a is None:
        return _bad("arm1 " + e)
    print("arm1 " + json.dumps(a, sort_keys=True)[:300])
    if "account_key" in json.dumps(a):
        return _bad("arm1 the census names an account key")
    ok1 = (a.get("sha256_ok") is True and a.get("accounts") == 769 and a.get("securities") == 3357
           and isinstance(a.get("windows"), int) and a["windows"] >= 3300 and isinstance(a.get("open_held"), int) and a["open_held"] >= 1)
    if not ok1:
        return _bad("arm1 census does not match the published set")
    d = tempfile.mkdtemp(prefix="dq_t57_")
    o1, o2 = os.path.join(d, "a.json"), os.path.join(d, "b.json")
    b, e = _line([os.path.join(D, "b1_request.py"), "--build", "--out", o1])
    if b is None:
        return _bad("arm2 " + e)
    print("arm2 " + json.dumps(b, sort_keys=True)[:360])
    ints = all(isinstance(b.get(k), int) for k in ("securities", "cells", "clipped_cusips", "held_back"))
    if not (ints and b["securities"] == 613 and b["clipped_cusips"] >= 90 and b["held_back"] >= 1 and 33000 <= b["cells"] <= 35500 and b["cells"] < 37439):
        return _bad("arm2 B1 line does not show the active-window clip")
    c, e = _line([os.path.join(D, "b1_request.py"), "--build", "--out", o2])
    if c is None:
        return _bad("arm3 " + e)
    same = hashlib.sha256(open(o1, "rb").read()).hexdigest() == hashlib.sha256(open(o2, "rb").read()).hexdigest()
    req = json.load(open(o1, encoding="utf-8"))
    sys.path.insert(0, D)
    try:
        import bbg_quote
        bbg_quote._validate(req)
        valid = True
    except Exception as exc:  # noqa: BLE001
        print("validate: %s" % str(exc)[:200])
        valid = False
    starts = [s.get("start") for s in req.get("securities") or [] if isinstance(s, dict) and s.get("start")]
    dates = [x for s in req.get("securities") or [] if isinstance(s, dict) for x in (s.get("dates") or [])]
    arms = {
        "deterministic": same,
        "valid": valid,
        "floor": all(x >= "2012-01-01" for x in starts + dates),
        "no_account_key": "account" not in json.dumps(req).lower(),
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arm3 " + ",".join(bad))
    print("WIN-REAL-OK active set verified (769 accounts, 3357 securities); B1 clipped %d CUSIPs to %d cells from 37,439, %d held back" % (b["clipped_cusips"], b["cells"], b["held_back"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
