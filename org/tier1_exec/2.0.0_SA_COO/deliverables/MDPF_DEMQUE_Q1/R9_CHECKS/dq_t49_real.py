"""MDPF_DEMQUE round 9, DQ-t-49 criterion AC2 (REAL price store, S3 read only, NO vendor call, writes only the scratch path it is given): `porting_test.py --build --out
<scratch.json>` prints ONE JSON line {"securities", "intervals_total", "cells", "max_cells_per_security", "short_window_securities", "need_class", "window_start"} and writes
the request. Required: securities >= 300; max_cells_per_security <= 10; cells <= 10 * securities; need_class client and window_start on or after 2012-01-01; two runs
write byte-identical files (deterministic draw); the request validates under `bbg_quote._validate`; every written entry is a single trading day (start == end) with
no key naming an account. PORT-REAL-OK; else PORT-REAL-BAD <why>.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "porting_test.py")


def _bad(why):
    print("PORT-REAL-BAD " + why)
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
    d = tempfile.mkdtemp(prefix="dq_t49_")
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
    secs = req.get("securities") or []
    sys.path.insert(0, os.path.join("data", "mdpf", "scripts", "demque"))
    try:
        import bbg_quote
        bbg_quote._validate(req)
        valid = True
    except Exception as exc:  # noqa: BLE001
        print("validate: %s" % str(exc)[:200])
        valid = False
    ints = all(isinstance(a.get(k), int) for k in ("securities", "cells", "max_cells_per_security"))
    arms = {
        "ints": ints,
        "count": ints and a["securities"] >= 300,
        "cap": ints and a["max_cells_per_security"] <= 10 and a["cells"] <= 10 * a["securities"],
        "declared": a.get("need_class") == "client" and isinstance(a.get("window_start"), str) and a["window_start"] >= "2012-01-01",
        "deterministic": same,
        "valid": valid,
        "single_days": bool(secs) and all(isinstance(s, dict) and s.get("start") == s.get("end") for s in secs),
        "no_account_key": "account" not in json.dumps(req).lower(),
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms=" + ",".join(bad))
    print("PORT-REAL-OK %d securities, %d cells (at most 10 each), deterministic, valid under the queue's rule" % (a["securities"], a["cells"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
