#!/usr/bin/env python3
"""MDPF_SECCLASS round 8, cell SC-e-33 (criterion SC8-e33-AC2): the three firms' missing lists are true against the table.

READ-ONLY. Reads the newest MISSING_LIST_<firm>_<yyyymmdd>.json for each of 49financial, cottonwood, inflection under
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ and checks, against etf-classifications (consistent reads only):
  - shape: {"firm", "as_of", "source": "<served artifact read>", "held_count": <int > 0>,
            "missing": [{"key", "name", "cusip" (when known), ...}], "total": <int>} with total == len(missing) and total <= held_count;
  - every listed key, and CUSIP:<cusip> for an entry that names its cusip, is ABSENT from the table (a present one is a
    false entry);
  - POSITIVE CONTROL: AAETX, a row measured present 2026-10-07, reads present, so an absent read is not a broken client.

Prints: MISSING-LIST ok=<bool> firms=<n of 3> listed=<n> false_entries=<n> control=<present|ABSENT> problems=<n>
"""
import json
import sys
from pathlib import Path

import boto3

ROOT = Path(__file__).resolve().parents[6]
HOME = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M"
FIRMS = ("49financial", "cottonwood", "inflection")
TABLE = "etf-classifications"


def present(client, keys):
    found = set()
    keys = list(dict.fromkeys(keys))
    for i in range(0, len(keys), 100):
        req = {TABLE: {"Keys": [{"ticker": {"S": k}} for k in keys[i:i + 100]], "ConsistentRead": True,
                       "ProjectionExpression": "ticker"}}
        while req:
            resp = client.batch_get_item(RequestItems=req)
            for it in resp.get("Responses", {}).get(TABLE, []):
                found.add(it["ticker"]["S"])
            req = resp.get("UnprocessedKeys") or None
    return found


def main():
    client = boto3.client("dynamodb", region_name="us-east-1")
    control = "present" if present(client, ["AAETX"]) else "ABSENT"
    problems, listed, false_entries, firms_ok = [], 0, 0, 0
    if control != "present":
        problems.append("positive control AAETX read ABSENT: the client or table read is broken")
    for firm in FIRMS:
        files = sorted(HOME.glob(f"MISSING_LIST_{firm}_*.json"))
        if not files:
            problems.append(f"{firm}: no MISSING_LIST file")
            continue
        try:
            doc = json.loads(files[-1].read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            problems.append(f"{firm}: unreadable json: {exc}")
            continue
        missing = doc.get("missing")
        held = doc.get("held_count")
        before = len(problems)
        if doc.get("firm") != firm or not doc.get("as_of") or not doc.get("source"):
            problems.append(f"{firm}: firm/as_of/source missing")
        if not isinstance(held, int) or held <= 0:
            problems.append(f"{firm}: held_count missing or not > 0")
        if not isinstance(missing, list) or doc.get("total") != len(missing or []):
            problems.append(f"{firm}: total != len(missing)")
        elif isinstance(held, int) and len(missing) > held:
            problems.append(f"{firm}: more missing than held")
        keys = [m.get("key") for m in (missing or []) if isinstance(m, dict)]
        if any(not k for k in keys):
            problems.append(f"{firm}: an entry has no key")
        keys = [k for k in keys if k]
        listed += len(keys)
        # an entry that names its CUSIP is missing only if the CUSIP: key is absent too (the producer tries both)
        keys += [f"CUSIP:{m['cusip']}" for m in (missing or []) if isinstance(m, dict) and m.get("cusip")]
        hit = present(client, keys) if keys else set()
        for k in sorted(hit):
            print(f"FALSE-ENTRY {firm} {k} is present in the table")
        false_entries += len(hit)
        if len(problems) == before and not hit:
            firms_ok += 1
        print("FIRM {} file={} held={} total={}".format(firm, files[-1].name, held, doc.get("total")))
    for p in problems:
        print(f"PROBLEM {p}")
    ok = not problems and false_entries == 0 and firms_ok == 3
    print(f"MISSING-LIST ok={ok} firms={firms_ok} of 3 listed={listed} false_entries={false_entries} "
          f"control={control} problems={len(problems)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
