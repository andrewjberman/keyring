"""sc_r16_cot_name_share_check.py -- MDPF_SECCLASS round 16 cell SC-e-82 check (row D1-W66-S2): the read-only measure of Cottonwood's
unclassified share that a canonical NAME:: row would place exists, carries its denominator, and is internally consistent.

READ-ONLY (reads the record file only). The record is COT_NAME_SHARE_20261009.json beside this folder's parent. It must carry:
  as_of, source (the served or gold key it read), positions (denominator: every COT position read), unclassified_positions,
  unclassified_mv, total_mv, name_placeable_positions, name_placeable_mv, threshold_pct, material (bool), method (one sentence).
Consistency: 0 <= name_placeable_positions <= unclassified_positions <= positions; 0 <= name_placeable_mv <= unclassified_mv <= total_mv;
material == (100 * name_placeable_mv / total_mv >= threshold_pct).
Prints  COT-NAME-SHARE ok=<bool> positions=<n> unclassified_mv=<x> name_placeable_mv=<x> pct=<x> material=<bool> problems=[...]
"""
import json
import sys
from pathlib import Path

REC = Path(__file__).resolve().parent.parent / "COT_NAME_SHARE_20261009.json"
NEED = ("as_of", "source", "positions", "unclassified_positions", "unclassified_mv", "total_mv", "name_placeable_positions",
        "name_placeable_mv", "threshold_pct", "material", "method")


def main():
    if not REC.exists():
        print(f"COT-NAME-SHARE ok=False problems=['record absent: {REC.name}']")
        return 1
    d = json.loads(REC.read_text(encoding="utf-8"))
    probs = [f"missing {k}" for k in NEED if k not in d]
    if not probs:
        if not (0 <= d["name_placeable_positions"] <= d["unclassified_positions"] <= d["positions"]) or d["positions"] <= 0:
            probs.append("position counts out of order or empty denominator")
        if not (0 <= d["name_placeable_mv"] <= d["unclassified_mv"] <= d["total_mv"]) or d["total_mv"] <= 0:
            probs.append("market values out of order")
        pct = 100.0 * d["name_placeable_mv"] / d["total_mv"] if d["total_mv"] else 0.0
        if bool(d["material"]) != (pct >= float(d["threshold_pct"])):
            probs.append("material does not follow from pct and threshold_pct")
    else:
        pct = 0.0
    ok = not probs
    print(f"COT-NAME-SHARE ok={ok} positions={d.get('positions')} unclassified_mv={d.get('unclassified_mv')} "
          f"name_placeable_mv={d.get('name_placeable_mv')} pct={pct:.4f} material={d.get('material')} problems={probs}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
