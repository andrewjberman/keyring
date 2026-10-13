"""MDPF_DEMQUE round 9, DQ-t-44 criterion AC2 (the REAL request files and the REAL drawn rows, S3 read only, no Bloomberg call, nothing written).
Three arms, each one command; every arm must hold:
  (1) `bbg_quote.py --check-declared` over org/missions/D8/MDPF/MDPF_DEMQUE/requests prints ONE JSON line {"checked": N, "refused": [{"request_id",
      "why"}], "accepted": N}; every `requests/*.json` that carries a `securities` list and a Bloomberg vendor must be checked; `refused` must be [] or only the ABNB model block with a reason naming the 365-day rule (amended 2026-10-13).
  (2) `standing_drawer.py --plan --request DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS` prints ONE JSON line {"request_id", "window_start", "remaining_cells",
      "securities": [...]} with window_start 2025-10-09, remaining_cells 1004 and securities exactly ["MO US Equity", "XOM US Equity"].
  (3) `card_a_slice.py --priority P1 --out <scratch> --quote` prints a window_end that is the last trading day on or before today (never 2026-06-23),
      priced_names + unresolved_names == p1_names, both FDIC placeholders unresolved, and the written request declares need_class client.
CLASS-REAL-OK; else CLASS-REAL-BAD <why>.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
import tempfile

D = os.path.join("data", "mdpf", "scripts", "demque")
REQ = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "requests")


def _line(cmd, timeout=115):
    r = subprocess.run([sys.executable] + cmd, capture_output=True, text=True, timeout=timeout, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-240:].strip())
    return json.loads(ls[-1]), ""


def _bad(why):
    print("CLASS-REAL-BAD " + why)
    return 1


def main() -> int:
    a, e = _line([os.path.join(D, "bbg_quote.py"), "--check-declared", REQ])
    if a is None:
        return _bad("arm1 " + e)
    print("arm1 checked=%s accepted=%s refused=%s" % (a.get("checked"), a.get("accepted"), [x.get("request_id") for x in a.get("refused") or []]))
    # AMENDED 2026-10-13 (issuer, after row D1-W36-S1): the ABNB model block's producer window (HIST_START 2016-01-01) is beyond the 365-day non-client rule, so the
    # queue correctly REFUSES it until the CTO or Andrew rules; it is the only refusal allowed, and its reason must name the 365-day rule.
    refused = a.get("refused") or []
    allowed = {"AMGT_RESAPP-107a-ABNB-MODEL-BLOCK"}
    ids = {x.get("request_id") for x in refused}
    if (not isinstance(a.get("checked"), int) or a["checked"] < 8 or not ids <= allowed
            or any("365" not in str(x.get("why")) for x in refused) or a.get("accepted") != a["checked"] - len(refused)):
        return _bad("arm1 refused or too few checked: %s" % json.dumps(a)[:300])
    b, e = _line([os.path.join(D, "standing_drawer.py"), "--plan", "--request", "DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS"])
    if b is None:
        return _bad("arm2 " + e)
    print("arm2 window_start=%s remaining_cells=%s securities=%s" % (b.get("window_start"), b.get("remaining_cells"), b.get("securities")))
    if b.get("window_start") != "2025-10-09" or b.get("remaining_cells") != 1004 or sorted(b.get("securities") or []) != ["MO US Equity", "XOM US Equity"]:
        return _bad("arm2 expected 2025-10-09 / 1004 / MO+XOM: %s" % json.dumps(b)[:300])
    out = os.path.join(tempfile.mkdtemp(prefix="dq_t44_"), "card_a_p1.json")
    c, e = _line([os.path.join(D, "card_a_slice.py"), "--priority", "P1", "--out", out, "--quote"])
    if c is None:
        return _bad("arm3 " + e)
    print("arm3 p1=%s priced=%s unresolved=%s cells=%s days=%s window_end=%s" % (c.get("p1_names"), c.get("priced_names"), c.get("unresolved_names"),
                                                                              c.get("cells"), c.get("days_to_finish"), c.get("window_end")))
    req = json.load(open(out, encoding="utf-8"))
    unres = {u.get("cusip") for u in c.get("unresolved") or []}
    today = dt.date.today().isoformat()
    ints = all(isinstance(c.get(k), int) for k in ("p1_names", "priced_names", "unresolved_names", "cells"))
    arms = {
        "window_end": isinstance(c.get("window_end"), str) and c["window_end"] != "2026-06-23" and "2026-10-01" <= c["window_end"] <= today,
        "partition": ints and c["priced_names"] + c["unresolved_names"] == c["p1_names"],
        "fdic": {"FDIC66606", "FDIC66853"} <= unres,
        "declares": req.get("need_class") == "client" and isinstance(req.get("window_start"), str) and req["window_start"] >= "2012-01-01",
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arm3 " + ",".join(bad))
    print("CLASS-REAL-OK 3 arms: %d requests declared, TR remainder %d cells (MO, XOM), P1 %d cells to %s" % (
        a["accepted"], b["remaining_cells"], c["cells"], c["window_end"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
