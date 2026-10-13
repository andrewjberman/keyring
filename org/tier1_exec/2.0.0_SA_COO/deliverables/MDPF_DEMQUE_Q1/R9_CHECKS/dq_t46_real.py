"""MDPF_DEMQUE round 9, DQ-t-46 criterion AC2 (REAL inputs, S3 read only, NO vendor call, writes only the scratch --out path it is given):
`p1_coverage.py --out <scratch.json>` prints ONE JSON line {"p1_names", "priced_names", "yahoo": {"in_store", "rejected", "symbol_known_untried",
"no_symbol"}, "bd_units_value": {"names", "held_days", "sources": [...]}, "residual": {"names", "cells"}, "window_cells"}. Required: p1_names 609;
priced_names 607; the four yahoo classes sum to priced_names; bd_units_value.names between 0 and priced_names, sources a non-empty list of strings;
residual.names between 0 and priced_names and residual.cells between 0 and window_cells; the written JSON has no key containing 'account'.
COVER-REAL-OK; else COVER-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "p1_coverage.py")


def _bad(why):
    print("COVER-REAL-BAD " + why)
    return 1


def _keys(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield str(k)
            yield from _keys(v)
    elif isinstance(o, list):
        for v in o:
            yield from _keys(v)


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    out = os.path.join(tempfile.mkdtemp(prefix="dq_t46_"), "p1_coverage.json")
    r = subprocess.run([sys.executable, TOOL, "--out", out], capture_output=True, text=True, timeout=118, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return _bad("rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip()))
    d = json.loads(ls[-1])
    y, b, z = d.get("yahoo") or {}, d.get("bd_units_value") or {}, d.get("residual") or {}
    print("p1=%s priced=%s yahoo=%s bd_names=%s bd_days=%s residual_names=%s residual_cells=%s of %s" % (
        d.get("p1_names"), d.get("priced_names"), y, b.get("names"), b.get("held_days"), z.get("names"), z.get("cells"), d.get("window_cells")))
    ints = all(isinstance(v, int) for v in (d.get("p1_names"), d.get("priced_names"), b.get("names"), z.get("names"), z.get("cells"), d.get("window_cells")))
    ycl = [y.get(k) for k in ("in_store", "rejected", "symbol_known_untried", "no_symbol")]
    written = json.load(open(out, encoding="utf-8")) if os.path.isfile(out) else {}
    arms = {
        "ints": ints,
        "p1": d.get("p1_names") == 609 and d.get("priced_names") == 607,
        "yahoo_sum": all(isinstance(v, int) for v in ycl) and sum(ycl) == d.get("priced_names"),
        "bd": ints and 0 <= b["names"] <= d["priced_names"] and isinstance(b.get("sources"), list) and bool(b["sources"])
              and all(isinstance(s, str) for s in b["sources"]),
        "residual": ints and 0 <= z["names"] <= d["priced_names"] and 0 <= z["cells"] <= d["window_cells"],
        "no_account_key": bool(written) and not any("account" in k.lower() for k in _keys(written)),
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms=" + ",".join(bad))
    print("COVER-REAL-OK yahoo %s; Black Diamond units and value %d names, %d held days; residual %d names, %d cells" % (
        y, b["names"], b["held_days"], z["names"], z["cells"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
