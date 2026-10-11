"""MDPF_DEMQUE round 9, DQ-t-33 criterion AC2: the REAL TR request, in scratch copies only (the real requests folder and ledger are read, never
written). (1) `bbg_quote.py --quote <request> --today 2026-10-11 --actuals <ledger up to 2026-10-11>` reads the cells already drawn for the job
and prints ONE JSON line with `cells` = the FULL request priced on TRADING days (trading days in the request window x fields x securities,
counted by this check from lib/trading_calendar), `cells_remaining` = cells minus drawn, `finish_date` 2026-10-17 and `label` naming it a
remaining-cells quote; (2) `refreeze.py` run on a scratch copy of the folder (already re-frozen once) writes a SECOND superseded file and a new
`supersedes`; (3) `quote_vs_actual.py` reads the new quote OPEN with both superseded finishes printed. QR-REAL-OK; else QR-REAL-BAD <why>.
"""
from __future__ import annotations

import datetime as dt
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, ".")
DEMQUE = os.path.join("data", "mdpf", "scripts", "demque")
MISSION = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE")
RID = "DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS"


def _run(args):
    r = subprocess.run([sys.executable] + args, capture_output=True, text=True, timeout=100, check=False)
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    return r.returncode, (json.loads(lines[-1]) if lines else None), (r.stderr or r.stdout)[-300:].strip()


def _bad(why):
    print("QR-REAL-BAD " + why)
    return 1


def main() -> int:
    from lib.trading_calendar import trading_days_between
    req_dir = os.path.join(MISSION, "requests")
    req = json.load(open(os.path.join(req_dir, RID + ".json"), encoding="utf-8"))
    n_days = len(trading_days_between(dt.date.fromisoformat(req["start"]), dt.date.fromisoformat(req["end"])))
    want_cells = n_days * len(req["fields"]) * len(req["securities"])
    tmp = tempfile.mkdtemp(prefix="qr_real_")
    try:
        # The real folder is already re-frozen a second time (the issuer's round-9 act). This check's input is the folder as it stood BEFORE
        # that act: the quote held by the newest superseded copy (its superseded_* keys stripped) is the live quote, and that copy is not
        # carried. Otherwise the transition this check exercises has already happened and refreeze answers ALREADY_REFROZEN.
        live = json.load(open(os.path.join(req_dir, RID + ".quote.json"), encoding="utf-8"))
        skip = set()
        if live.get("supersedes") and live["supersedes"].endswith("-2.json"):
            prev = json.load(open(os.path.join(req_dir, live["supersedes"]), encoding="utf-8"))
            for k in ("superseded_reason", "superseded_on", "superseded_by"):
                prev.pop(k, None)
            with open(os.path.join(tmp, RID + ".quote.json"), "w", encoding="utf-8") as fh:
                json.dump(prev, fh, indent=2, sort_keys=True)
            skip = {RID + ".quote.json", live["supersedes"]}
        for f in glob.glob(os.path.join(req_dir, RID + "*.json")):
            if os.path.basename(f) not in skip:
                shutil.copy(f, os.path.join(tmp, os.path.basename(f)))
        actuals = os.path.join(tmp, "BBG_ACTUALS.upto-2026-10-11.jsonl")
        with open(os.path.join(MISSION, "ledger", "BBG_ACTUALS.jsonl"), encoding="utf-8", errors="replace") as src, \
                open(actuals, "w", encoding="utf-8") as dst:
            for ln in src:
                if ln.strip() and json.loads(ln).get("date", "9") <= "2026-10-11":
                    dst.write(ln)
        rc, q, err = _run([os.path.join(DEMQUE, "bbg_quote.py"), "--quote", os.path.join(tmp, RID + ".json"), "--today", "2026-10-11",
                           "--actuals", actuals])
        if rc != 0 or not q:
            return _bad("quote rc=%d %s" % (rc, err))
        cells = (q.get("cells") or {}).get("bloomberg_history")
        print("quote: cells=%s want=%s remaining=%s finish=%s label=%s" % (cells, want_cells, q.get("cells_remaining"), q.get("finish_date"), q.get("label")))
        drawn = sum(int(json.loads(ln).get("cells_drawn") or 0) for ln in open(actuals, encoding="utf-8")
                    if ln.strip() and json.loads(ln).get("job") == RID)
        arms = {"cells": cells == want_cells, "remaining": q.get("cells_remaining") == want_cells - drawn,
                "finish": q.get("finish_date") == "2026-10-17", "label": "remaining" in str(q.get("label")).lower()}
        before = set(glob.glob(os.path.join(tmp, RID + ".quote.superseded-*.json")))
        rc, rf, err = _run([os.path.join(DEMQUE, "refreeze.py"), "--request-id", RID, "--requests-dir", tmp, "--as-of", "2026-10-11",
                            "--reason", "cells priced on trading days, round 9 Z-S3", "--now", "2026-10-11T16:00:00Z"])
        sup = sorted(glob.glob(os.path.join(tmp, RID + ".quote.superseded-*.json")))
        arms["second_superseded"] = rc == 0 and len(sup) == 2
        new = json.load(open(os.path.join(tmp, RID + ".quote.json"), encoding="utf-8"))
        added = sorted(set(sup) - before)
        arms["supersedes_new"] = len(added) == 1 and new.get("supersedes") == os.path.basename(added[0])
        rc, qv, err = _run([os.path.join(DEMQUE, "quote_vs_actual.py"), "--request", RID, "--requests-dir", tmp, "--actuals", actuals,
                            "--today", "2026-10-11"])
        arms["qva_both"] = bool(qv) and qv.get("verdict") == "OPEN" and len(qv.get("superseded") or []) == 2
        print("refreeze rc=%s superseded_files=%d; qva=%s" % (rc, len(sup), json.dumps(qv, sort_keys=True)[:200] if qv else err))
        bad = [k for k, v in arms.items() if not v]
        if bad:
            return _bad("arms=" + ",".join(bad))
        print("QR-REAL-OK trading-day cells %d, remaining %d, chained re-freeze keeps both superseded quotes" % (cells, want_cells - drawn))
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
