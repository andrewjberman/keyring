"""MDPF_DEMQUE round 9, DQ-t-53 criterion AC2 (REAL price index, request and queue files, unresolved list and the live DynamoDB table `etf-classifications`, READ ONLY: one
get_item, never a write, no vendor call): `secclass_sync.py --prove` prints ONE JSON line {"security": {"cusip","symbol"}, "request_row": {"file","key"}, "unresolved": {"state":
"resolved"|"listed","key"}, "classification_row": {"table","key","present"}, "equal": true|false, "negative_arm": {"second_request_rows","classification_rows_for_key"}}. Required: equal
true; the three keys printed and equal; classification_row.present true and table `etf-classifications`; negative_arm.classification_rows_for_key == 1; the proof wrote nothing.
SYNC-REAL-OK; else SYNC-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "secclass_sync.py")


def _bad(why):
    print("SYNC-REAL-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    r = subprocess.run([sys.executable, TOOL, "--prove"], capture_output=True, text=True, timeout=115, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return _bad("rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip()))
    d = json.loads(ls[-1])
    print(json.dumps({k: d.get(k) for k in ("security", "request_row", "unresolved", "classification_row", "equal", "negative_arm")}, sort_keys=True)[:700])
    rr, un, cr, ng = d.get("request_row") or {}, d.get("unresolved") or {}, d.get("classification_row") or {}, d.get("negative_arm") or {}
    keys = [rr.get("key"), cr.get("key")] + ([un.get("key")] if un.get("state") == "listed" else [])
    arms = {
        "equal": d.get("equal") is True,
        "keys_equal": all(isinstance(k, str) and k for k in keys) and len(set(keys)) == 1,
        "classified": cr.get("present") is True and cr.get("table") == "etf-classifications",
        "unresolved_state": un.get("state") in ("resolved", "listed"),
        "one_row": ng.get("classification_rows_for_key") == 1,
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms=" + ",".join(bad))
    print("SYNC-REAL-OK key %s equal on the request row, the unresolved list (%s) and the classification row; one row for the key" % (keys[0], un.get("state")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
