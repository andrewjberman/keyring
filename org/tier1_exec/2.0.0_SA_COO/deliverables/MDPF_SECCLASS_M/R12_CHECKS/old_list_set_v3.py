"""old_list_set_v3.py -- MDPF_SECCLASS SC-e-32/SC-e-50 rebuild: the old-list reclassification set V3 from V2.

READ-ONLY against AWS (consistent paginated scans of bd-securities and etf-classifications). NO model call, NO table write.
From M/OLD_LIST_RECLASSIFY_SET_V2_20261007.tsv (held and routes kept), three changes:
  1. clean_name is recomputed for every row by the fixed security_name.clean_name (R12 + R12b, the SC-e-48 refusal) from the
     live bd-securities row's name;
  2. row S58's re-plan under contract 0.8.0: CSHI -> cash/T-Bill; FIGXX, FISXX -> cash/Money Market (DIRECT);
  2b. every other DIRECT fixed_income/Cash row -> cash/Cash (ruling 2.4: Cash is a sub-class of cash only; the SC-e-49
      condition's own re-plan). The V2 checker printed problems[:3], so row S58 counted 3 of these; the set holds 313;
  3. a DIRECT or AI row whose shared_key is now a key of etf-classifications becomes PRESENT (e.g. SC-e-49's DIRECT leg).
  python old_list_set_v3.py           # build, then check
  python old_list_set_v3.py check     # check only
Prints  OLD-LIST-SET-V3 ok=<bool> rows=<n> live=<n> routes=<..> renamed=<n> to_present=<n> problems=[..]
"""
import csv
import json
import sys
from collections import Counter
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
M = HERE.parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / "infra/aws/lambda/v2_portal/_shared"))
from security_name import clean_name  # noqa: E402

V2 = M / "OLD_LIST_RECLASSIFY_SET_V2_20261007.tsv"
V3 = M / "OLD_LIST_RECLASSIFY_SET_V3_20261007.tsv"
COLS = ["old_key", "shared_key", "held", "route", "asset_class", "sub_asset_class", "clean_name"]
S58 = {"CSHI": ("cash", "T-Bill"), "FIGXX": ("cash", "Money Market"), "FISXX": ("cash", "Money Market")}


def scan(table_name):
    t = boto3.resource("dynamodb", region_name="us-east-1").Table(table_name)
    items, kw = [], {"ConsistentRead": True}
    while True:
        r = t.scan(**kw)
        items += r.get("Items", [])
        if "LastEvaluatedKey" not in r:
            return items
        kw["ExclusiveStartKey"] = r["LastEvaluatedKey"]


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE)
        assert rd.fieldnames == COLS, rd.fieldnames
        return list(rd)


def build(old, shared):
    rows = read_tsv(V2)
    renamed = to_present = recashed = 0
    for r in rows:
        o = old.get(r["old_key"], {})
        nm = clean_name(o.get("name") or o.get("asset_name_raw") or None) or ""
        if nm != r["clean_name"]:
            renamed += 1
            r["clean_name"] = nm
        if r["old_key"] in S58 and r["route"] == "DIRECT":
            r["asset_class"], r["sub_asset_class"] = S58[r["old_key"]]
        elif r["route"] == "DIRECT" and (r["asset_class"], r["sub_asset_class"]) == ("fixed_income", "Cash"):
            r["asset_class"] = "cash"
            recashed += 1
        if r["route"] in ("DIRECT", "AI") and r["shared_key"] and r["shared_key"] in shared:
            r["route"], r["asset_class"], r["sub_asset_class"] = "PRESENT", "", ""
            to_present += 1
    with V3.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, delimiter="\t", quoting=csv.QUOTE_NONE, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(f"RE-PLANNED fixed_income/Cash -> cash/Cash: {recashed} (plus the 3 S58 rows)", flush=True)
    return renamed, to_present


def check(old, shared, renamed=None, to_present=None):
    contract = json.loads((ROOT / "org/standards/MDPF_SECCLASS_CONTRACT.json").read_text(encoding="utf-8"))
    closed = {c: set(v) for c, v in contract["fields"]["sub_asset_class"]["values_by_class"].items()}
    rows = read_tsv(V3)
    probs = []
    keys = [r["old_key"] for r in rows]
    if len(set(keys)) != len(keys) or set(keys) != set(old):
        probs.append(f"keys:set={len(set(keys))} live={len(old)}")
    for r in rows:
        if r["route"] == "DIRECT" and r["sub_asset_class"] not in closed.get(r["asset_class"], set()):
            probs.append("bound:" + r["old_key"])
        if r["route"] in ("DIRECT", "AI") and r["shared_key"] in shared:
            probs.append("present:" + r["old_key"])
        o = old.get(r["old_key"], {})
        if r["clean_name"] != (clean_name(o.get("name") or o.get("asset_name_raw") or None) or ""):
            probs.append("name:" + r["old_key"])
        if not r["clean_name"].isascii():
            probs.append("ascii:" + r["old_key"])
    for k, pair in S58.items():
        r = next((x for x in rows if x["old_key"] == k), None)
        if r and r["route"] == "DIRECT" and (r["asset_class"], r["sub_asset_class"]) != pair:
            probs.append("s58:" + k)
    routes = dict(Counter(r["route"] for r in rows))
    print(f"OLD-LIST-SET-V3 ok={not probs} rows={len(rows)} live={len(old)} contract={contract.get('contract_version')} "
          f"routes={routes} renamed={renamed} to_present={to_present} problems={probs[:5]} n_problems={len(probs)}")
    return 0 if not probs else 1


if __name__ == "__main__":
    old = {r["ticker"]: r for r in scan("bd-securities")}
    shared = {r["ticker"] for r in scan("etf-classifications")}
    print(f"DENOMINATOR bd-securities={len(old)} etf-classifications={len(shared)}", flush=True)
    if sys.argv[1:] == ["check"]:
        sys.exit(check(old, shared))
    rn, tp = build(old, shared)
    sys.exit(check(old, shared, rn, tp))
