"""sc_r15_rows_set.py -- MDPF_SECCLASS round 15 cell SC-e-77 check: the D1-S11 row set covers every no-row security and obeys
Andrew's alternatives rule.

READ-ONLY, no AWS. Inputs:
- BD_UNCLASSIFIED_TRACE_D1S11_20261008.json, groups B (ticker has no canonical row) and D (no row under any key): the denominator.
- S11_ROW_SET_20261008.tsv (the cell's set), tab-separated, header
  key, name, action, asset_class, sub_asset_class, current_class, rule, evidence
  action NEW (a row to create, put on absence) or REMAP (an existing model row whose class breaks the rule);
  rule = andrew-alternatives when the row is a hedge, private or real estate fund (Andrew-direct 2026-10-08 ~19:0xZ), else blank.
Checks:
- every B/D security appears exactly once as a NEW line, keyed by its ticker (group B) or its trace name_key (group D);
- every asset_class is one of the six;
- every rule=andrew-alternatives line reads alternatives;
- every REMAP line carries rule=andrew-alternatives and a current_class that is not alternatives.
Whether a line is really a hedge, private or real estate fund is graded by 3.0.0_SA_CVO, not here.
Run from the repo root you are grading.
Prints  S11-ROW-SET ok=<bool> bd=<n> covered=<n> new=<n> remap=<n> rule_rows=<n> bad=<n> first_bad=[...]
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path.cwd()
M = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M"
TRACE = M / "BD_UNCLASSIFIED_TRACE_D1S11_20261008.json"
SET = M / "S11_ROW_SET_20261008.tsv"
SIX = {"equity", "fixed_income", "cash", "alternatives", "structured", "commodities"}


def main():
    rows = json.loads(TRACE.read_text(encoding="utf-8"))["rows"]
    want = {}
    for r in rows:
        why = str(r.get("why", ""))
        if why.startswith("B:"):
            want[str(r.get("ticker") or "").strip().upper()] = r["name"]
        elif why.startswith("D:"):
            want[r.get("name_key")] = r["name"]
    if not SET.exists():
        print(f"S11-ROW-SET ok=False bd={len(want)} covered=0 new=0 remap=0 rule_rows=0 bad=1 first_bad=['set absent']")
        return 1
    with SET.open(encoding="utf-8", newline="") as fh:
        lines = list(csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE))
    bad, seen = [], {}
    for ln in lines:
        k, act, ac, rule = ln["key"], ln["action"], ln["asset_class"], ln.get("rule") or ""
        if ac not in SIX:
            bad.append((k, "class", ac))
        if rule == "andrew-alternatives" and ac != "alternatives":
            bad.append((k, "rule", ac))
        if act == "NEW":
            seen[k] = seen.get(k, 0) + 1
        elif act == "REMAP":
            if rule != "andrew-alternatives" or ln.get("current_class") == "alternatives":
                bad.append((k, "remap", ln.get("current_class")))
        else:
            bad.append((k, "action", act))
    covered = sum(1 for k in want if seen.get(k) == 1)
    bad += [(k, "missing-or-dup", seen.get(k, 0)) for k in want if seen.get(k) != 1]
    ok = bool(want) and covered == len(want) and not bad
    print(f"S11-ROW-SET ok={ok} bd={len(want)} covered={covered} new={sum(seen.values())} "
          f"remap={sum(1 for ln in lines if ln['action'] == 'REMAP')} "
          f"rule_rows={sum(1 for ln in lines if (ln.get('rule') or '') == 'andrew-alternatives')} bad={len(bad)} first_bad={bad[:3]}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
