"""MDPF_DEMQUE round 9, DQ-t-68 criterion AC2 (REAL S3 index READ ONLY via `price_store.py --index-preview`, and the V2 active set; NO write, NO vendor call).

`price_store.py --index-preview` prints ONE JSON line. It must carry `columns` ending in [..., "porting_verdict", "use_class"] (eleven columns; the ten old ones keep their order), `rows` == the row count read straight from price_store.index(s3_root()),
`use_class` {value: count} whose keys are within {NOT_FOR_ACTIVE, INACTIVE_USE}, NOT_FOR_ACTIVE equal to the number of index CUSIPs in the V2 active set and INACTIVE_USE equal to the rest (both computed here, independently),
`active_source` == "read", and `old_columns_digest` identical across two runs. `--index-preview --active-set-path <a path that cannot be read>` must print `active_source` == "unreadable" and every row NOT_FOR_ACTIVE.
USECLASS-REAL-OK; else USECLASS-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

D = os.path.join("data", "mdpf", "scripts", "demque")


def _bad(why):
    print("USECLASS-REAL-BAD " + why)
    return 1


def _run(*args):
    env = dict(os.environ)
    env["PYTHONPATH"] = os.getcwd()
    r = subprocess.run([sys.executable, os.path.join(D, "price_store.py"), "--index-preview"] + list(args), capture_output=True, text=True,
                       timeout=200, check=False, env=env)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-260:].strip())
    return json.loads(ls[-1]), ""


def main() -> int:
    sys.path.insert(0, D)
    sys.path.insert(0, os.getcwd())
    import active_set  # noqa: E402
    import price_store  # noqa: E402
    v2 = set(active_set.load().keys())
    idx = price_store.index(price_store.s3_root())
    n_act = int(sum(1 for c in idx["cusip"] if c in v2))
    p, e = _run()
    if p is None:
        return _bad("preview " + e)
    print("preview " + json.dumps({k: p.get(k) for k in ("rows", "use_class", "active_source")}, sort_keys=True))
    cols = p.get("columns")
    if not isinstance(cols, list) or cols[-2:] != ["porting_verdict", "use_class"] or len(cols) != 11:
        return _bad("columns do not end in porting_verdict, use_class with 11 columns")
    uc = p.get("use_class")
    if p.get("rows") != len(idx) or not isinstance(uc, dict) or not set(uc) <= {"NOT_FOR_ACTIVE", "INACTIVE_USE"}:
        return _bad("rows or the use_class keys are wrong")
    if uc.get("NOT_FOR_ACTIVE", 0) != n_act or uc.get("INACTIVE_USE", 0) != len(idx) - n_act:
        return _bad("use_class counts differ from the independent V2 count (%d of %d)" % (n_act, len(idx)))
    if p.get("active_source") != "read":
        return _bad("active_source is not read")
    p2, e = _run()
    if p2 is None or p2.get("old_columns_digest") != p.get("old_columns_digest"):
        return _bad("old_columns_digest differs across runs")
    q, e = _run("--active-set-path", os.path.join("nonexistent", "none.csv"))
    if q is None:
        return _bad("unreadable run " + e)
    if q.get("active_source") != "unreadable" or q.get("use_class") != {"NOT_FOR_ACTIVE": len(idx)}:
        return _bad("an unreadable active set did not fail closed to NOT_FOR_ACTIVE for every row")
    print("USECLASS-REAL-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
