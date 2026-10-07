#!/usr/bin/env python3
"""issuer_check_sc_e29.py -- MDPF_SECCLASS round 8 issuer check for cell SC-e-29 (FWD-12: the ETF view from the shared list).

Modes (one verdict token each; run from the repo root; read-only against DynamoDB):
  beforeafter -- the newest M/ETF_VIEW_BEFORE_AFTER_*.json carries a denominator of holdings > 0, one row per holding, and for
                 every row with a shared-list entry its `after` sector and industry group EQUAL its `shared_list` values; and a
                 fresh consistent read of etf-classifications (us-east-1) for up to 25 of those keys returns the same values
                 under the two field names the JSON declares (the seam probe against the rows the sector write filled).
                 Prints SC-E29-BEFOREAFTER ok=True|False.
  half        -- the newest M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_ETF_VIEW_*.md names ETFS_POSITIONING, carries a BLAST RADIUS
                 section, a rollback, both branches (lines starting 'BRANCH A:' and 'BRANCH B:'), and the two headings
                 '## ETFS_POSITIONING COO half -- UNSIGNED' and '## ETFS_POSITIONING CTO half -- UNSIGNED'.
                 Prints SC-E29-HALF ok=True|False.

Expected JSON shape (the worker's deliverable):
  {"read_at": "...", "fields": {"sector": "<contract field name>", "industry_group": "<contract field name>"},
   "denominator": N, "rows": [{"book": "...", "ticker": "...", "key": "<etf-classifications key or null>",
     "before": {"sector": ..., "industry_group": ...}, "after": {"sector": ..., "industry_group": ...},
     "shared_list": {"sector": ..., "industry_group": ...} or null}]}
"""
import glob
import json
import os
import sys

M = os.path.join("org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M")
PROBE = 25


def newest(pattern):
    hits = sorted(glob.glob(os.path.join(M, pattern)))
    return hits[-1] if hits else None


def check_beforeafter():
    path = newest("ETF_VIEW_BEFORE_AFTER_*.json")
    if not path:
        return False, "no ETF_VIEW_BEFORE_AFTER_*.json"
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    fields = doc.get("fields") or {}
    if not fields.get("sector") or not fields.get("industry_group"):
        return False, "fields not declared"
    rows = doc.get("rows") or []
    n = doc.get("denominator")
    if not isinstance(n, int) or n <= 0 or n != len(rows):
        return False, f"denominator {n!r} != rows {len(rows)}"
    keyed = [r for r in rows if r.get("key") and r.get("shared_list")]
    if not keyed:
        return False, "no row carries a shared-list entry"
    for r in keyed:
        for f in ("sector", "industry_group"):
            if (r.get("after") or {}).get(f) != r["shared_list"].get(f):
                return False, "row {}/{} after.{} != shared_list.{}".format(r.get("book"), r.get("ticker"), f, f)
    import boto3
    ddb = boto3.client("dynamodb", region_name="us-east-1")
    for r in keyed[:PROBE]:
        item = ddb.get_item(TableName="etf-classifications", Key={"ticker": {"S": r["key"]}},
                            ConsistentRead=True).get("Item")
        if item is None:
            return False, "key {} absent from etf-classifications".format(r["key"])
        for f in ("sector", "industry_group"):
            live = (item.get(fields[f]) or {}).get("S")
            if live != r["shared_list"].get(f):
                return False, "key {} live {}={!r} != shared_list {!r}".format(r["key"], fields[f], live, r["shared_list"].get(f))
    return True, f"file={os.path.basename(path)!s} denominator={int(n)} keyed={len(keyed)} probed={int(min(PROBE, len(keyed)))}"


def check_half():
    path = newest("NEVER_WIDEN_HALF_REQUEST_SECCLASS_ETF_VIEW_*.md")
    if not path:
        return False, "no NEVER_WIDEN_HALF_REQUEST_SECCLASS_ETF_VIEW_*.md"
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    lines = text.splitlines()
    need = ("## ETFS_POSITIONING COO half -- UNSIGNED", "## ETFS_POSITIONING CTO half -- UNSIGNED")
    for h in need:
        if h not in lines:
            return False, f"heading missing: {h}"
    if "blast radius" not in text.lower() or "rollback" not in text.lower():
        return False, "no BLAST RADIUS or rollback"
    for b in ("BRANCH A:", "BRANCH B:"):
        if not any(ln.startswith(b) for ln in lines):
            return False, f"no line starting {b}"
    return True, f"file={os.path.basename(path)}"


def main(argv):
    mode = argv[0] if argv else ""
    if mode == "beforeafter":
        ok, why = check_beforeafter()
        print(f"SC-E29-BEFOREAFTER ok={ok} {why}")
    elif mode == "half":
        ok, why = check_half()
        print(f"SC-E29-HALF ok={ok} {why}")
    else:
        print("usage: issuer_check_sc_e29.py beforeafter|half")
        return 2
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
