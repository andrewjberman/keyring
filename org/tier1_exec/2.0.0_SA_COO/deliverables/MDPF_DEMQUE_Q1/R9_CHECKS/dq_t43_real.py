"""MDPF_DEMQUE round 9, DQ-t-43 criterion AC2 (REAL served inputs, S3 read only, no Bloomberg call, writes only the scratch request path it is
given): `card_a_slice.py --priority P1 --out <scratch> --quote` prints ONE JSON line {"priority", "p1_names", "priced_names", "unresolved_names",
"cells", "days_to_finish", "finish_date", "claim", "window_end", "unresolved": [{"cusip","reason"}]}. Required: priority P1; p1_names between
500 and 700; priced + unresolved == p1_names; both FDIC cash-sweep placeholders listed unresolved; every written window ends on window_end
2026-06-23; cells > 0 and days_to_finish a positive integer; the written request carries no key naming an account. SLICE-REAL-OK; else
SLICE-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "card_a_slice.py")


def _bad(why):
    print("SLICE-REAL-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    out = os.path.join(tempfile.mkdtemp(prefix="dq_t43_"), "card_a_p1.json")
    r = subprocess.run([sys.executable, TOOL, "--priority", "P1", "--out", out, "--quote"],
                       capture_output=True, text=True, timeout=115, check=False)
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        return _bad("rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip()))
    d = json.loads(lines[-1])
    print("p1=%s priced=%s unresolved=%s cells=%s days=%s finish=%s claim=%s" % (
        d.get("p1_names"), d.get("priced_names"), d.get("unresolved_names"), d.get("cells"), d.get("days_to_finish"),
        d.get("finish_date"), d.get("claim")))
    if not os.path.isfile(out):
        return _bad("the request was not written to " + out)
    req = json.load(open(out, encoding="utf-8"))
    secs = req.get("securities") or []
    unres = {u.get("cusip") for u in d.get("unresolved") or []}
    ints = all(isinstance(d.get(k), int) for k in ("p1_names", "priced_names", "unresolved_names", "cells"))
    text = json.dumps(req).lower()
    arms = {
        "priority": d.get("priority") == "P1",
        "ints": ints,
        "p1_range": ints and 500 <= d["p1_names"] <= 700,
        "partition": ints and d["priced_names"] + d["unresolved_names"] == d["p1_names"] and len(secs) == d["priced_names"],
        "fdic_unresolved": {"FDIC66606", "FDIC66853"} <= unres,
        "windows_end": bool(secs) and all(isinstance(s, dict) and s.get("end") == d.get("window_end") == "2026-06-23" for s in secs),
        "cells_days": ints and d["cells"] > 0 and isinstance(d.get("days_to_finish"), int) and d["days_to_finish"] > 0,
        "no_account_key": "account" not in text,
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms=" + ",".join(bad))
    print("SLICE-REAL-OK P1 %d names priced, %d unresolved, %d cells, %d days to finish" % (
        d["priced_names"], d["unresolved_names"], d["cells"], d["days_to_finish"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
