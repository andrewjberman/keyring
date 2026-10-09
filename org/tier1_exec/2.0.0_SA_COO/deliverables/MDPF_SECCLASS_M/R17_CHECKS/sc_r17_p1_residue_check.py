"""sc_r17_p1_residue_check.py -- MDPF_SECCLASS round 17, cell SC-e-85. READ-ONLY.

Grades ../P1_RESIDUE_UNPLACED_20261009.json, the listing that joins the p1 ledger's 11 residue keys (never in FWD-15's plan)
to FWD-15's UNPLACED-KEY census. ok=True when ALL hold:
  1. the record's keys are exactly the 11 below, once each;
  2. every entry carries pattern, table_row_present, bd_positions, bd_mv, cot_positions, cot_mv, as_of_bd, as_of_cot;
  3. `pattern` equals the census's own pattern_of(key, {}) (R12_CHECKS/unplaced_key_census.py);
  4. `table_row_present` equals a consistent get-item on etf-classifications, re-read now;
  5. positions are non-negative integers and mv values are numbers.
Prints: P1-RESIDUE ok=<bool> keys=<n> present_now=<n> held_bd=<n> held_cot=<n> problems=<list>
"""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REC = HERE.parent / "P1_RESIDUE_UNPLACED_20261009.json"
KEYS = [
    "ETHA",
    "NAME::AST INVESTMENT GRADE BOND PORTFOLIO",
    "NAME::AXA MODERATE ALLOCATION",
    "NAME::BENEFIT FIXED RATE OPTION",
    "NAME::CALAMOS STRATEGIC TOTAL RETURN COM SH BEN INT",
    "NAME::GRAYSCALE ETHEREUM STAKING MINI ETF",
    "NAME::JOHN HANCOCK LIFE INSURANCE CO 5 06 15 2028",
    "NAME::MFS MULTIMARKET INCOME TR SH BEN INT",
    "NAME::MORGAN STANLEY 6 25 08 09 2026",
    "NAME::PATRIOT BK N A 4 5 2026",
    "NAME::PRUDENTIAL ANNUITY",
]
FIELDS = ("pattern", "table_row_present", "bd_positions", "bd_mv", "cot_positions", "cot_mv", "as_of_bd", "as_of_cot")


def main() -> int:
    if not REC.exists():
        print(f"P1-RESIDUE ok=False keys=0 present_now=0 held_bd=0 held_cot=0 problems=['record absent: {REC.name}']")
        return 1
    spec = importlib.util.spec_from_file_location("ukc", HERE.parent / "R12_CHECKS" / "unplaced_key_census.py")
    ukc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ukc)
    rec = json.loads(REC.read_text(encoding="utf-8"))
    entries = rec.get("entries") or []
    probs = []
    got = [e.get("key") for e in entries]
    if sorted(got) != sorted(KEYS) or len(set(got)) != len(got):
        probs.append(f"keys differ: missing={sorted(set(KEYS) - set(got))} extra={sorted(set(got) - set(KEYS))} dup={len(got) - len(set(got))}")
    import boto3
    ddb = boto3.client("dynamodb", region_name="us-east-1")
    present_now = held_bd = held_cot = 0
    for e in entries:
        k = e.get("key")
        miss = [f for f in FIELDS if f not in e]
        if miss:
            probs.append(f"{k}: missing {miss}")
            continue
        if e["pattern"] != ukc.pattern_of(k, {}):
            probs.append(f"{k}: pattern {e['pattern']!r} != census {ukc.pattern_of(k, {})!r}")
        now = "Item" in ddb.get_item(TableName="etf-classifications", Key={"ticker": {"S": k}}, ConsistentRead=True)
        present_now += int(now)
        if bool(e["table_row_present"]) != now:
            probs.append(f"{k}: table_row_present={e['table_row_present']} but live read={now}")
        for f in ("bd_positions", "cot_positions"):
            if not isinstance(e[f], int) or e[f] < 0:
                probs.append(f"{k}: {f} not a non-negative int")
        for f in ("bd_mv", "cot_mv"):
            if not isinstance(e[f], (int, float)):
                probs.append(f"{k}: {f} not a number")
        held_bd += int(isinstance(e["bd_positions"], int) and e["bd_positions"] > 0)
        held_cot += int(isinstance(e["cot_positions"], int) and e["cot_positions"] > 0)
    ok = not probs
    print(f"P1-RESIDUE ok={ok} keys={len(entries)} present_now={present_now} held_bd={held_bd} held_cot={held_cot} problems={probs}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
