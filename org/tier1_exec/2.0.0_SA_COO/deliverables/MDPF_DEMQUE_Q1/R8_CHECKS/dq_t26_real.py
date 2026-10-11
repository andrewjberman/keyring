"""MDPF_DEMQUE round 8, DQ-t-26 criterion AC2: the REAL TR request re-frozen in a scratch copy of the requests folder (the real folder is
never written here), then graded by quote_vs_actual against the real actuals ledger.
Re-freeze as of 2026-10-09 under the rule in force: finish 2026-10-17 (Sat 10-10, Sun 10-11, Sat 10-17 at 5,858 a day), the superseded
quote (finish 2026-10-13, weekday rule) kept beside it with the reason "rule changed, round 6 R1". quote_vs_actual on 2026-10-11 reads
OPEN against 2026-10-17 with 5,858 drawn and prints the superseded finish. REFRZ-OK; else REFRZ-BAD <why>.
"""
from __future__ import annotations

import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

DEMQUE = os.path.join("data", "mdpf", "scripts", "demque")
MISSION = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE")
RID = "DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS"
REASON = "rule changed, round 6 R1"


def _run(args):
    r = subprocess.run([sys.executable] + args, capture_output=True, text=True, timeout=100, check=False)
    return r.returncode, r.stdout, r.stderr


def _bad(why):
    print("REFRZ-BAD " + why)
    return 1


def main() -> int:
    tool = os.path.join(DEMQUE, "refreeze.py")
    if not os.path.isfile(tool):
        return _bad("no file " + tool)
    tmp = tempfile.mkdtemp(prefix="refreeze_")
    try:
        for suffix in (".json", ".quote.json"):
            shutil.copy(os.path.join(MISSION, "requests", RID + suffix), os.path.join(tmp, RID + suffix))
        rc, out, err = _run([tool, "--request-id", RID, "--requests-dir", tmp, "--as-of", "2026-10-09", "--reason", REASON])
        if rc != 0:
            return _bad("refreeze rc=%d %s" % (rc, (err or out)[-300:].strip()))
        new = json.load(open(os.path.join(tmp, RID + ".quote.json"), encoding="utf-8"))
        kept = sorted(glob.glob(os.path.join(tmp, RID + ".quote.superseded-*.json")))
        if len(kept) != 1:
            return _bad("expected one superseded file, found %d" % len(kept))
        old = json.load(open(kept[0], encoding="utf-8"))
        print("new: finish=%s supersedes=%s" % (new.get("finish_date"), new.get("supersedes")))
        print("old: finish=%s reason=%s" % (old.get("finish_date"), old.get("superseded_reason")))
        rc2, out2, err2 = _run([os.path.join(DEMQUE, "quote_vs_actual.py"), "--request", RID, "--requests-dir", tmp,
                                "--actuals", os.path.join(MISSION, "ledger", "BBG_ACTUALS.jsonl"), "--today", "2026-10-11"])
        if rc2 != 0:
            return _bad("quote_vs_actual rc=%d %s" % (rc2, (err2 or out2)[-300:].strip()))
        lines = [ln for ln in out2.splitlines() if ln.strip().startswith("{")]
        qva = json.loads(lines[-1]) if lines else {}
        print("qva: " + json.dumps(qva, sort_keys=True))
        sup = qva.get("superseded") or []
        arms = {
            "new_finish": new.get("finish_date") == "2026-10-17" and bool(new.get("supersedes")),
            "old_kept": old.get("finish_date") == "2026-10-13" and REASON in str(old.get("superseded_reason")),
            "graded_on_new": qva.get("finish_date") == "2026-10-17" and qva.get("verdict") == "OPEN" and qva.get("cells_drawn") == 5858,
            "prints_both": any(str(s.get("finish_date")) == "2026-10-13" for s in sup if isinstance(s, dict)),
        }
        bad = [k for k, v in arms.items() if not v]
        if bad:
            return _bad("arms=" + ",".join(bad))
        print("REFRZ-OK re-frozen finish 2026-10-17, superseded 2026-10-13 kept with its reason, graded OPEN on the new quote with both printed")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
