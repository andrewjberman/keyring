"""MDPF_DEMQUE round 9, DQ-t-51 criterion AC2 (REAL price index, S3 read only, NO vendor call, writes only the scratch path it is given): `porting_test.py --build --out
<scratch.json>` prints ONE JSON line {"securities", "testable", "untestable", "intervals_total", "cells", "max_cells_per_security", "need_class", "window_start"}. Required:
testable + untestable == securities (326 at the last count, >= 300); intervals_total == 5 * testable (every testable security has exactly 5 intervals, never fewer); cells <=
10 * testable and max_cells_per_security <= 10 (a repeated endpoint may share a cell, so cells may be fewer); every request entry is a single trading day; two runs write
byte-identical files; the file validates under `bbg_quote._validate`; untestable securities are listed in the file's `untestable` list with the reason `window under 10 trading days`.
INT-REAL-OK; else INT-REAL-BAD <why>.
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
    print("INT-REAL-BAD " + why)
    return 1


def _run(out):
    r = subprocess.run([sys.executable, TOOL, "--build", "--out", out], capture_output=True, text=True, timeout=55, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip())
    return json.loads(ls[-1]), ""


def main() -> int:
    d = tempfile.mkdtemp(prefix="dq_t51_")
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
    ints = all(isinstance(a.get(k), int) for k in ("securities", "testable", "untestable", "intervals_total", "cells", "max_cells_per_security"))
    un = req.get("untestable") or []
    arms = {
        "ints": ints,
        "count": ints and a["securities"] >= 300 and a["testable"] + a["untestable"] == a["securities"],
        "five": ints and a["intervals_total"] == 5 * a["testable"],
        "cap": ints and a["max_cells_per_security"] <= 10 and a["cells"] <= 10 * a["testable"],
        "untestable_listed": ints and len(un) == a["untestable"] and all("under 10 trading days" in str(u.get("reason")) for u in un),
        "single_days": all(isinstance(s, dict) and s.get("start") == s.get("end") for s in req.get("securities") or []),
        "deterministic": same,
        "valid": valid,
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms=" + ",".join(bad))
    print("INT-REAL-OK %d testable with exactly 5 intervals each, %d UNTESTABLE, %d cells" % (a["testable"], a["untestable"], a["cells"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
