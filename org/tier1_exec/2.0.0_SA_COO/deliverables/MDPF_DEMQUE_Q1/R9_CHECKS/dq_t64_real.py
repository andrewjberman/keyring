"""MDPF_DEMQUE round 9, DQ-t-64 criterion AC2 (REAL S3 rank inputs and the price index, the V2 active set: READ ONLY, NO vendor call, writes only the scratch path it is given).

`inactive_set.py --census --out <scratch>` measures the INACTIVE-ONLY set (Andrew-direct 2026-10-15 via CTO msg 6105: active accounts get Bloomberg only, inactive accounts may use Yahoo): the CUSIPs any
Cottonwood account has traded that are NOT in the V2 active set. The census line must hold the integer keys held_total, active_held, inactive_only, class_p1, class_p2, class_p3, with_symbol, no_symbol, inactive_stored,
inactive_unstored, active_stored, requests_one_pass, nights_at_cap, request_cap and these identities: held_total == active_held + inactive_only; class_p1 + class_p2 + class_p3 == inactive_only; with_symbol + no_symbol == inactive_only;
inactive_stored + inactive_unstored == inactive_only; requests_one_pass == with_symbol; request_cap == 380; nights_at_cap == ceil(with_symbol / 380); inactive_only > 0.
The written names file: a JSON object with a `names` list of exactly inactive_only entries, each {cusip, symbol (string or null), priority}; sorted by cusip; no CUSIP of it is in the V2 active set; no key naming an account; two runs are byte-identical;
zero hits from the account-id oracle where its hash list is present.
INACTIVE-REAL-OK; else INACTIVE-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import math
import os
import subprocess
import sys
import tempfile

D = os.path.join("data", "mdpf", "scripts", "demque")
INTS = ("held_total", "active_held", "inactive_only", "class_p1", "class_p2", "class_p3", "with_symbol", "no_symbol",
        "inactive_stored", "inactive_unstored", "active_stored", "requests_one_pass", "nights_at_cap", "request_cap")


def _bad(why):
    print("INACTIVE-REAL-BAD " + why)
    return 1


def _run(out):
    env = dict(os.environ)
    env["PYTHONPATH"] = os.getcwd()
    r = subprocess.run([sys.executable, os.path.join(D, "inactive_set.py"), "--census", "--out", out],
                       capture_output=True, text=True, timeout=200, check=False, env=env)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-260:].strip())
    return json.loads(ls[-1]), ""


def _keys(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield str(k)
            yield from _keys(v)
    elif isinstance(o, list):
        for v in o:
            yield from _keys(v)


def main() -> int:
    d = tempfile.mkdtemp(prefix="dq_t64_")
    o1, o2 = os.path.join(d, "a.json"), os.path.join(d, "b.json")
    c, e = _run(o1)
    if c is None:
        return _bad("census " + e)
    print("census " + json.dumps(c, sort_keys=True)[:520])
    if not all(type(c.get(k)) is int for k in INTS):
        return _bad("a census key is missing or not an integer")
    if c["inactive_only"] <= 0:
        return _bad("inactive_only is not above 0")
    if c["held_total"] != c["active_held"] + c["inactive_only"]:
        return _bad("held_total != active_held + inactive_only")
    if c["class_p1"] + c["class_p2"] + c["class_p3"] != c["inactive_only"]:
        return _bad("the classes do not add up to inactive_only")
    if c["with_symbol"] + c["no_symbol"] != c["inactive_only"]:
        return _bad("with_symbol + no_symbol != inactive_only")
    if c["inactive_stored"] + c["inactive_unstored"] != c["inactive_only"]:
        return _bad("stored + unstored != inactive_only")
    if c["requests_one_pass"] != c["with_symbol"] or c["request_cap"] != 380:
        return _bad("requests_one_pass != with_symbol, or request_cap != 380")
    if c["nights_at_cap"] != math.ceil(c["with_symbol"] / 380):
        return _bad("nights_at_cap is not ceil(with_symbol / 380)")
    names = json.load(open(o1, encoding="utf-8")).get("names")
    if not isinstance(names, list) or len(names) != c["inactive_only"]:
        return _bad("the names file does not hold inactive_only entries")
    cus = [n.get("cusip") for n in names]
    if cus != sorted(cus) or len(set(cus)) != len(cus) or not all(isinstance(x, str) and x for x in cus):
        return _bad("the names are not unique, non-blank CUSIPs sorted ascending")
    if not all(set(n) == {"cusip", "symbol", "priority"} and n["priority"] in ("P1", "P2", "P3") for n in names):
        return _bad("an entry does not carry exactly cusip, symbol and priority")
    sys.path.insert(0, D)
    import active_set  # noqa: E402
    if set(cus) & set(active_set.load().keys()):
        return _bad("a CUSIP of the names file is in the V2 active set")
    bad_keys = [k for k in set(_keys(json.load(open(o1, encoding="utf-8")))) if "account" in k.lower()]
    if bad_keys:
        return _bad("the names file carries a key naming an account: %s" % bad_keys[:3])
    c2, e2 = _run(o2)
    if c2 is None:
        return _bad("second census " + e2)
    if open(o1, "rb").read() != open(o2, "rb").read():
        return _bad("two runs wrote different bytes")
    print("INACTIVE-REAL-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
