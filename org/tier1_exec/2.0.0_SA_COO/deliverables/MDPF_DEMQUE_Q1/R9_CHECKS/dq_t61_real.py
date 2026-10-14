"""MDPF_DEMQUE round 9, DQ-t-61 criterion AC2 (REAL S3 and the active-set V2 commit, READ ONLY, NO vendor call, writes only the scratch path it is given).

`b1_request.py --build --names <YAHOO_FAILED_14_NAMES.json> --request-id MDPF_SECHIST-CARD-A-B1-YAHOO-FAILED-14 --out <scratch>` builds the Bloomberg request for the 14 daily-tier names whose Yahoo lock fails (CTO msg 5411):
depth c, windows clipped to the V2 active Cottonwood set, priced and quoted. The build line must read "securities" between 1 and 14, "priced_names" 14, and held_back + securities + emptied_cusips == 14 (a name is in the request, held back,
or emptied; none vanishes), "cells" > 0 and < 20000, a finish_date. The written request: request_id equals the --request-id value, every CUSIP is one of the 14 (read from the names file), every entry has a window or dates starting on or after 2012-01-01,
it validates under `bbg_quote._validate`, two builds are byte-identical, no KEY naming an account and zero hits from the account-id oracle where its hash list is present.
NAMES-REAL-OK; else NAMES-REAL-BAD <why>.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile

D = os.path.join("data", "mdpf", "scripts", "demque")
NAMES = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "deliverables", "2.0.0_SA_COO~Q1", "YAHOO_FAILED_14_NAMES.json")
RID = "MDPF_SECHIST-CARD-A-B1-YAHOO-FAILED-14"


def _bad(why):
    print("NAMES-REAL-BAD " + why)
    return 1


def _build(out):
    r = subprocess.run([sys.executable, os.path.join(D, "b1_request.py"), "--build", "--names", NAMES, "--request-id", RID, "--out", out],
                       capture_output=True, text=True, timeout=110, check=False)
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
    names = {n["cusip"] for n in json.load(open(NAMES, encoding="utf-8"))["names"]}
    if len(names) != 14:
        return _bad("the names file does not hold 14 CUSIPs")
    d = tempfile.mkdtemp(prefix="dq_t61_")
    o1, o2 = os.path.join(d, "a.json"), os.path.join(d, "b.json")
    b, e = _build(o1)
    if b is None:
        return _bad("build " + e)
    print("build " + json.dumps(b, sort_keys=True)[:420])
    ints = all(isinstance(b.get(k), int) for k in ("securities", "priced_names", "held_back", "emptied_cusips", "cells"))
    if not (ints and 1 <= b["securities"] <= 14 and b["priced_names"] == 14 and b["held_back"] + b["securities"] + b["emptied_cusips"] == 14
            and 0 < b["cells"] < 20000 and b.get("finish_date")):
        return _bad("the build line does not add up to the 14 names")
    c, e = _build(o2)
    if c is None:
        return _bad("second build " + e)
    req = json.load(open(o1, encoding="utf-8"))
    same = hashlib.sha256(open(o1, "rb").read()).hexdigest() == hashlib.sha256(open(o2, "rb").read()).hexdigest()
    sys.path.insert(0, D)
    try:
        import bbg_quote
        bbg_quote._validate(req)
        valid = True
    except Exception as exc:  # noqa: BLE001
        print("validate: %s" % str(exc)[:200])
        valid = False
    secs = req.get("securities") or []
    starts = [s.get("start") for s in secs if s.get("start")] + [x for s in secs for x in (s.get("dates") or [])]
    oracle = True
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("cdc", os.path.join(".tools", "git-hooks", "client-data-check.py"))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        hashes = m._load_hashes(m._hash_list_path())
        hits = len(m.hits_in(json.dumps(req).encode("utf-8"), hashes))
        print("account-id oracle: %d hit line(s) against %d hashes" % (hits, len(hashes)))
        oracle = hits == 0
    except Exception as exc:  # noqa: BLE001
        print("account-id oracle NOT RUN on this device (%s)" % str(exc)[:80])
    arms = {
        "request_id": req.get("request_id") == RID,
        "only_the_14": all(s.get("cusip") in names for s in secs) and bool(secs),
        "floor": all(x >= "2012-01-01" for x in starts),
        "valid": valid,
        "deterministic": same,
        "no_account_key": not any("account" in k.lower() for k in _keys(req)) and oracle,
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms failed: " + ",".join(bad))
    print("NAMES-REAL-OK %d of the 14 names in the request (%d held back, %d emptied), %d cells, finish %s" % (b["securities"], b["held_back"], b["emptied_cusips"], b["cells"], b["finish_date"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
