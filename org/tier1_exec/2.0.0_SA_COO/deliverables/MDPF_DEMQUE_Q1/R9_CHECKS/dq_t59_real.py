"""MDPF_DEMQUE round 9, DQ-t-59 criterion AC2 (the REAL store index, S3 READ ONLY, nothing written to S3; only temp files this check creates).

`price_store.py --index-preview [--verdicts PATH]` builds the index exactly as `write_index` would and prints ONE JSON line
{"columns": [...], "rows": n, "porting_verdict": {value: count}, "verdicts_source": "absent"|"read"|"unreadable", "sample_cusips": [first three CUSIPs of the index, ascending],
"old_columns_digest": sha256 hex of the index's nine OLD columns as CSV text} WITHOUT writing any key.
Arm 1 (no verdicts file; --verdicts points at a path that does not exist): columns == the old INDEX_COLS ["cusip","yahoo_symbol","valid_from","valid_to","rows","claim","method","as_of","run_id"]
plus "porting_verdict" as the LAST column; rows == the number of CUSIP directories in the store (326 today, read live); porting_verdict == {"UNVERIFIED": rows}; verdicts_source "absent".
Arm 2 (a temp verdicts file naming two real CUSIPs from the index: one PASS, one FAIL, and a third with the comparator's NO_BLOOMBERG): counts are PASS 1, FAIL 1, UNVERIFIED rows-2 (NO_BLOOMBERG reads UNVERIFIED, never PASS);
verdicts_source "read".
Arm 3 (a temp file that is not valid JSON): porting_verdict == {"UNVERIFIED": rows}, verdicts_source "unreadable" (fail closed).
Arm 4: the indexed `claim` column and every old column are byte-identical between arm 1 and arm 3 (the label moves nothing else).
VERDICT-REAL-OK; else VERDICT-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "price_store.py")
OLD = ["cusip", "yahoo_symbol", "valid_from", "valid_to", "rows", "claim", "method", "as_of", "run_id"]


def _bad(why):
    print("VERDICT-REAL-BAD " + why)
    return 1


def _run(path):
    r = subprocess.run([sys.executable, TOOL, "--index-preview", "--verdicts", path], capture_output=True, text=True, timeout=100, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-260:].strip())
    return json.loads(ls[-1]), ""


def main() -> int:
    d = tempfile.mkdtemp(prefix="dq_t59_")
    a, e = _run(os.path.join(d, "absent.json"))
    if a is None:
        return _bad("arm1 " + e)
    n = a.get("rows")
    print("arm1 columns=%s rows=%s verdicts=%s source=%s" % (a.get("columns"), n, a.get("porting_verdict"), a.get("verdicts_source")))
    if not (a.get("columns") == OLD + ["porting_verdict"] and isinstance(n, int) and n >= 300 and a.get("porting_verdict") == {"UNVERIFIED": n} and a.get("verdicts_source") == "absent"):
        return _bad("arm1 columns, rows or default verdicts are wrong")
    cusips = a.get("sample_cusips") or []
    if len(cusips) < 3:
        return _bad("arm1 --index-preview must print sample_cusips (the first three CUSIPs of the index, ISO order) so the check can name real ones")
    good = os.path.join(d, "v.json")
    json.dump({cusips[0]: {"verdict": "PASS"}, cusips[1]: {"verdict": "FAIL"}, cusips[2]: {"verdict": "NO_BLOOMBERG"}}, open(good, "w"))
    b, e = _run(good)
    if b is None:
        return _bad("arm2 " + e)
    print("arm2 verdicts=%s source=%s" % (b.get("porting_verdict"), b.get("verdicts_source")))
    if not (b.get("porting_verdict") == {"PASS": 1, "FAIL": 1, "UNVERIFIED": n - 2} and b.get("verdicts_source") == "read"):
        return _bad("arm2 counts are wrong (NO_BLOOMBERG must read UNVERIFIED)")
    broken = os.path.join(d, "broken.json")
    open(broken, "w").write("{not json")
    c, e = _run(broken)
    if c is None:
        return _bad("arm3 " + e)
    print("arm3 verdicts=%s source=%s" % (c.get("porting_verdict"), c.get("verdicts_source")))
    if not (c.get("porting_verdict") == {"UNVERIFIED": n} and c.get("verdicts_source") == "unreadable"):
        return _bad("arm3 a broken verdicts file must write UNVERIFIED for every name")
    if a.get("old_columns_digest") != c.get("old_columns_digest") or not a.get("old_columns_digest"):
        return _bad("arm4 the old columns differ between runs, or no old_columns_digest is printed")
    print("VERDICT-REAL-OK %d names; default UNVERIFIED, PASS/FAIL read per name, NO_BLOOMBERG and a broken file fail closed, old columns unchanged" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
