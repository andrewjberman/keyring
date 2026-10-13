"""MDPF_DEMQUE round 9, DQ-t-57 criterion AC2 (REAL active-set file or its commit, S3 read only, NO vendor call, writes only the scratch path it is given).

Arm 1: `active_set.py --census` prints ONE JSON line {"sha256_ok", "accounts", "securities", "windows", "open_held"} with sha256_ok true, accounts 769, securities 3357,
windows >= 3300 and open_held >= 1. The line carries counts only: no key containing "account_key" and no account number.
Arm 2: `b1_request.py --build --out <scratch>` prints the B1 line with "securities" 608 (the 606 priced P1 names plus the 7 of the 8 funds that are P1 = 613, minus the 4 names no active account holds
under any identifier the files carry (CTO msg 5227), minus the 1 name whose active window opens after all its B1 history, which is EMPTIED (AMENDED 2026-10-13, rulings on rows W49-S1..S5)),
"emptied_cusips" 1, "clipped_cusips" >= 90, "held_back" >= 5 (the P2 fund and those 4), and "cells" between 33,000 and 35,000 and strictly below 37,439. Each build call is allowed 110 seconds (a build runs about 45 s).
Arm 3: a second `--build` writes a byte-identical file; the written request validates under `bbg_quote._validate`; no entry starts before 2012-01-01; no KEY naming an account (a reason text may say the word) and zero hits from the account-id oracle where its hash list is present.
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


def _line(cmd, timeout=110):
    r = subprocess.run([sys.executable] + cmd, capture_output=True, text=True, timeout=timeout, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-260:].strip())
    return json.loads(ls[-1]), ""


def _bad(why):
    print("WIN-REAL-BAD " + why)
    return 1


def _keys(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield str(k)
            yield from _keys(v)
    elif isinstance(o, list):
        for v in o:
            yield from _keys(v)


def _no_account_key(req):
    """AMENDED 2026-10-13 (issuer, row W49-S7): the test is on KEY NAMES, not on the text of a reason (the ruled hold-back reason says 'account'), plus the
    repo's own account-id oracle (.tools/git-hooks/client-data-check.py against the hash list) when the list is present on this device."""
    if any("account" in k.lower() for k in _keys(req)):
        return False
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("cdc", os.path.join(".tools", "git-hooks", "client-data-check.py"))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        hashes = m._load_hashes(m._hash_list_path())
        hits = len(m.hits_in(json.dumps(req).encode("utf-8"), hashes))
        print("account-id oracle: %d hit line(s) against %d hashes" % (hits, len(hashes)))
        return hits == 0
    except Exception as exc:  # noqa: BLE001
        print("account-id oracle NOT RUN on this device (%s); key-name test only" % str(exc)[:80])
        return True


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
    if not (ints and b["securities"] == 608 and b.get("emptied_cusips") == 1 and b["clipped_cusips"] >= 90 and b["held_back"] >= 5 and 33000 <= b["cells"] <= 35000 and b["cells"] < 37439):
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
        "no_account_key": _no_account_key(req),
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arm3 " + ",".join(bad))
    print("WIN-REAL-OK active set verified (769 accounts, 3357 securities); B1 clipped %d CUSIPs to %d cells from 37,439, %d held back" % (b["clipped_cusips"], b["cells"], b["held_back"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
