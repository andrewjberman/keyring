"""ai_leg_verify.py -- post-run check of an MDPF_SECCLASS AI leg (e32 V3 old-list, or e49 missing-list) on etf-classifications.

  python ai_leg_verify.py e32|e49 <the act's snapshot.json>
Reads, ConsistentRead and paginated:
- each planned AI key that was absent at the snapshot: landed (classified_by model, classification_confidence present, its
  class/sub-class inside the contract 0.8.0 closed list) or still absent (UNRESOLVED); any other state is a problem;
- every key in the snapshot is still present (nothing deleted);
- 0 multi_asset rows in the table;
- the AI listing for today exists and its count equals the number of classified_by=model rows.
Prints  AI-LEG-VERIFY act=<e32|e49> ok=<bool> planned=<n> landed=<n> unresolved=<n> problems=<n> ...
ok needs the WHOLE plan accounted for: landed + refused == planned (row S66, CTO round-12 addendum 1 @e5befb00f1). A partial
leg reads ok=False; landed>0 alone caught only an empty act.
  --unresolved-log <run log> [...]   the executor's stdout ("UNRESOLVED <key>: <why>"); the LAST reason per key wins. A still-absent planned
  key counts as refused only when its reason is a FINAL, model-stated refusal (TO-AI-e32 amendment 7): a model reply with no class,
  a class outside the six, no sub-class, a sub-class the table does not carry, or KIMI_VOCAB_VIOLATION. A transport or vendor failure
  (refused: KIMI_TIMEOUT / KIMI_ERROR / KIMI_HTTP_* / KIMI_MALFORMED / KIMI_EMPTY / KIMI_BADJSON / KIMI_SCHEMA_INVALID /
  KIMI_LENGTH_STARVED) is NOT final: the key stays unresolved and is re-planned.
"""
import csv
import glob
import json
import sys
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
M = HERE.parent
ROOT = HERE.parents[5]


def planned(act):
    if act == "e32":
        with (M / "OLD_LIST_RECLASSIFY_SET_V3_20261007.tsv").open(encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh, delimiter="\t"))
        direct = {r["shared_key"] for r in rows if r["route"] == "DIRECT"}
        return {r["shared_key"] for r in rows if r["route"] == "AI" and r["shared_key"] not in direct}
    keys = set()
    for f in glob.glob(str(HERE / "e49_replan" / "FWD15_AI_PLAN_*_20261007.json")):
        keys |= {e.get("shared_key") or e["key"] for e in json.loads(Path(f).read_text(encoding="utf-8"))["entries"]
                 if e["route"] == "AI"}
    return keys


def scan_all(table):
    out, kw = [], {"ConsistentRead": True}
    while True:
        page = table.scan(**kw)
        out += page.get("Items", [])
        if "LastEvaluatedKey" not in page:
            return out
        kw["ExclusiveStartKey"] = page["LastEvaluatedKey"]


TRANSPORT_CODES = ("KIMI_TIMEOUT", "KIMI_ERROR", "KIMI_HTTP_", "KIMI_MALFORMED", "KIMI_EMPTY", "KIMI_BADJSON",
                   "KIMI_SCHEMA_INVALID", "KIMI_LENGTH_STARVED")


def is_final_refusal(why):
    """A model-stated refusal the next resume would not change; any transport or vendor failure is not final."""
    why = why or ""
    if "KIMI_VOCAB_VIOLATION" in why:
        return True
    if "refused:" in why and any(c in why for c in TRANSPORT_CODES):
        return False
    if why.startswith("no class (refused:"):
        return False
    return why.startswith(("no class (", "class ", "no sub-class", "sub-class "))


def read_unresolved(paths):
    last = {}
    for p in paths:
        for line in Path(p).read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("UNRESOLVED ") and ": " in line:
                key, why = line[len("UNRESOLVED "):].split(": ", 1)
                last[key.strip()] = why.strip()
    return last


def blind_log_refusal(absent_keys, reasons, logs):
    """A problem string when logs were given, keys are absent, and no absent key has a reason line (prefixed or wrong logs)."""
    if logs and absent_keys and not any(k in reasons for k in absent_keys):
        return f"blind-logs: {len(absent_keys)} absent keys, 0 reason lines in {len(logs)} log(s) (prefixed or wrong logs?)"
    return None


def grade(planned_n, landed, refused, problems, gone, multi_asset, listing_count, model_rows):
    """The verdict, as a pure function so a test can feed it a run's numbers."""
    return (planned_n > 0 and landed + refused == planned_n and problems == 0 and gone == 0 and multi_asset == 0
            and listing_count == model_rows)


def main():
    argv = sys.argv[1:]
    logs = []
    if "--unresolved-log" in argv:
        i = argv.index("--unresolved-log")
        logs, argv = argv[i + 1:], argv[:i]
    act, snap_path = argv[0], Path(argv[1])
    if not snap_path.exists():
        print(f"AI-LEG-VERIFY act={act} ok=False missing_snapshot={snap_path.name}")
        return 1
    before = set(json.loads(snap_path.read_text(encoding="utf-8"))["keys"])
    contract = json.loads((ROOT / "org/standards/MDPF_SECCLASS_CONTRACT.json").read_text(encoding="utf-8"))
    closed = {c: set(v) for c, v in contract["fields"]["sub_asset_class"]["values_by_class"].items()}
    items = scan_all(boto3.resource("dynamodb", region_name="us-east-1").Table("etf-classifications"))
    live = {i["ticker"]: i for i in items}
    keys = planned(act) - before
    landed = unresolved = 0
    probs = []
    for k in sorted(keys):
        it = live.get(k)
        if it is None:
            unresolved += 1
        elif (it.get("classified_by") == "model" and "classification_confidence" in it
              and it.get("sub_asset_class") in closed.get(it.get("asset_class"), set())):
            landed += 1
        else:
            probs.append(k)
    gone = len(before - set(live))
    ma = sum(1 for i in items if i.get("asset_class") == "multi_asset")
    model_rows = sum(1 for i in items if i.get("classified_by") == "model")
    s3 = boto3.client("s3", region_name="us-east-1")
    # The NEWEST listing, not today's: a run that crosses midnight UTC leaves the latest listing under yesterday's date until its
    # next chunk rewrites it (laptop ~SC's warning, 2026-10-08), and reading today's key then grades a false FAIL.
    prefix = "mdpf/global/gold/ai_classified_securities/"
    listings = [o["Key"] for page in s3.get_paginator("list_objects_v2").paginate(Bucket="opal-data-mdpf", Prefix=prefix)
                for o in page.get("Contents", []) if o["Key"].endswith("/index.json")]
    newest = max(listings) if listings else None
    lcount = None
    if newest:
        listing = json.loads(s3.get_object(Bucket="opal-data-mdpf", Key=newest)["Body"].read())
        lcount = listing.get("count", len(listing.get("securities", listing.get("rows", []))))
    reasons = read_unresolved(logs) if logs else {}
    absent = [k for k in keys if k not in live]
    refused = sum(1 for k in absent if is_final_refusal(reasons.get(k)))
    transport = sum(1 for k in absent if k in reasons and not is_final_refusal(reasons.get(k)))
    blind = blind_log_refusal(absent, reasons, logs)
    if blind:
        probs.append(blind)
    ok = grade(len(keys), landed, refused, len(probs), gone, ma, lcount, model_rows)
    print(f"AI-LEG-VERIFY act={act} ok={ok} planned={len(keys)} landed={landed} refused_final={refused} "
          f"refused_transport={transport} unresolved={unresolved} problems={len(probs)} "
          f"first={probs[:3]} snapshot_keys_gone={gone} multi_asset={ma} model_rows={model_rows} listing_count={lcount} listing={newest}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
