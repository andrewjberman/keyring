"""MDPF_DEMQUE round 9, DQ-t-67 criterion AC2 (REAL S3 rank inputs, the price index and the V2 active set: READ ONLY, NO vendor call, writes only the scratch directory it makes).

`inactive_set.py --census --out <names.json>` then `inactive_request.py --build --names <names.json> --out-dir <dir>` build the Yahoo backfill requests for the inactive-only names that have a symbol.
The build line (one JSON line) must hold the integers names_in, with_symbol, without_symbol, requests, securities_total, max_chunk, cells and nights; with_symbol + without_symbol == names_in, securities_total == with_symbol,
requests == ceil(with_symbol / 300), 1 <= max_chunk <= 300.
The files in <dir>: exactly `requests` files named YAHOO-INACTIVE-BACKFILL-<nn>.json (nn from 01); each validates under demand_queue.validate, has tier 2, need_class "client", start "2012-01-01", an end that is a trading day on or before today,
fields ["close"], 1..300 securities each {cusip, symbol} with a non-blank symbol; the union of the CUSIPs equals the names file's non-null-symbol CUSIPs, each once; none is in the V2 active set; no key naming an account; two builds are byte-identical.
REQUEST-REAL-OK; else REQUEST-REAL-BAD <why>.
"""
from __future__ import annotations

import glob
import json
import math
import os
import subprocess
import sys
import tempfile
from datetime import date

D = os.path.join("data", "mdpf", "scripts", "demque")
INTS = ("names_in", "with_symbol", "without_symbol", "requests", "securities_total", "max_chunk", "cells", "nights")


def _bad(why):
    print("REQUEST-REAL-BAD " + why)
    return 1


def _py(script, *args):
    env = dict(os.environ)
    env["PYTHONPATH"] = os.getcwd()
    r = subprocess.run([sys.executable, os.path.join(D, script)] + list(args), capture_output=True, text=True, timeout=200, check=False, env=env)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "%s rc=%d %s" % (script, r.returncode, (r.stderr or r.stdout)[-260:].strip())
    return json.loads(ls[-1]), ""


def _keys(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield str(k)
            yield from _keys(v)
    elif isinstance(o, list):
        for v in o:
            yield from _keys(v)


def _snapshot(d):
    return {os.path.basename(p): open(p, "rb").read() for p in sorted(glob.glob(os.path.join(d, "*.json")))}


def main() -> int:
    sys.path.insert(0, D)
    sys.path.insert(0, os.getcwd())
    import active_set  # noqa: E402
    import demand_queue as dq  # noqa: E402
    from lib import trading_calendar as cal  # noqa: E402
    v2 = set(active_set.load().keys())
    d = tempfile.mkdtemp(prefix="dq_t67_")
    names = os.path.join(d, "names.json")
    c, e = _py("inactive_set.py", "--census", "--out", names)
    if c is None:
        return _bad(e)
    d1, d2 = os.path.join(d, "a"), os.path.join(d, "b")
    b, e = _py("inactive_request.py", "--build", "--names", names, "--out-dir", d1)
    if b is None:
        return _bad(e)
    print("build " + json.dumps(b, sort_keys=True)[:400])
    if not all(type(b.get(k)) is int for k in INTS):
        return _bad("a build key is missing or not an integer")
    if b["with_symbol"] + b["without_symbol"] != b["names_in"] or b["securities_total"] != b["with_symbol"]:
        return _bad("the build counts do not add up")
    if b["requests"] != math.ceil(b["with_symbol"] / 300) or not (1 <= b["max_chunk"] <= 300):
        return _bad("requests != ceil(with_symbol / 300) or max_chunk is out of 1..300")
    snap = _snapshot(d1)
    want = ["YAHOO-INACTIVE-BACKFILL-%02d.json" % (i + 1) for i in range(b["requests"])]
    if sorted(snap) != want:
        return _bad("the files are not exactly %s" % want[:3])
    named = {n["cusip"] for n in json.load(open(names, encoding="utf-8"))["names"] if n.get("symbol")}
    seen = []
    for fn in want:
        req = json.loads(snap[fn])
        try:
            dq.validate(req)
        except Exception as exc:
            return _bad("%s does not validate: %s" % (fn, str(exc)[:120]))
        end = date.fromisoformat(str(req["end"])[:10])
        if req["tier"] != 2 or req.get("need_class") != "client" or str(req["start"])[:10] != "2012-01-01" or req["fields"] != ["close"]:
            return _bad("%s: tier, need_class, start or fields is wrong" % fn)
        if end > date.today() or not cal.is_trading_day(end):
            return _bad("%s: end is not a trading day on or before today" % fn)
        secs = req["securities"]
        if not (1 <= len(secs) <= 300) or not all(set(s) >= {"cusip", "symbol"} and str(s["symbol"]).strip() for s in secs):
            return _bad("%s: securities are not 1..300 entries with a symbol" % fn)
        seen += [s["cusip"] for s in secs]
        if [k for k in set(_keys(req)) if "account" in k.lower()]:
            return _bad("%s carries a key naming an account" % fn)
    if sorted(seen) != sorted(named) or len(set(seen)) != len(seen):
        return _bad("the union of the requests is not the symbolled names, each once")
    if set(seen) & v2:
        return _bad("a V2 active-set CUSIP is in a request")
    b2, e = _py("inactive_request.py", "--build", "--names", names, "--out-dir", d2)
    if b2 is None:
        return _bad("second build " + e)
    if _snapshot(d2) != snap:
        return _bad("two builds wrote different bytes")
    print("REQUEST-REAL-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
