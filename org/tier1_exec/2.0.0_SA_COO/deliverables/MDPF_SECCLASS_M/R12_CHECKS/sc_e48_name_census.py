#!/usr/bin/env python3
"""sc_e48_name_census.py -- MDPF_SECCLASS SC-e-48 re-request (CTO half REFUSED @cadf21e1f1, items 1-4): the clean-name set's WRITE
rows carry no visibly wrong casing.

READ-ONLY. Reads CLEAN_NAME_ROW_SET_V2_20261007.tsv (columns key, classified_by, current_name, source_name, clean_name, action, source)
from the tree it is run from. Over the rows whose action is WRITE it counts, word-boundary and case-sensitive:
- `acronym_titled`: a title-cased depositary/fund/foreign form (Adr, Ads, Etf, Sa, Se, Ag, Nv);
- `form_upper`: an all-caps corporate form that the rule writes title-case (INC, CORP, CO);
- `ltd_plc_titled`: LTD or PLC written title-case (Ltd, Plc), which the rule writes upper.
Over ALL rows it counts `dual`: forms appearing in both casings across the set (LTD/Ltd, PLC/Plc, ADR/Adr, ETF/Etf).
Prints SC-E48-CENSUS ok=<bool> with each count and the totals per action. ok means every count is 0.
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

TSV = Path.cwd() / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_V2_20261007.tsv"
ACRONYM_TITLED = re.compile(r"\b(Adr|Ads|Etf|Sa|Se|Ag|Nv)\b")
FORM_UPPER = re.compile(r"\b(INC|CORP|CO)\b")
LTD_PLC_TITLED = re.compile(r"\b(Ltd|Plc)\b")
DUAL = [("LTD", "Ltd"), ("PLC", "Plc"), ("ADR", "Adr"), ("ETF", "Etf")]


def main():
    with TSV.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    actions = Counter(r["action"] for r in rows)
    writes = [r for r in rows if r["action"] == "WRITE"]
    a = sum(1 for r in writes if ACRONYM_TITLED.search(r["clean_name"] or ""))
    f = sum(1 for r in writes if FORM_UPPER.search(r["clean_name"] or ""))
    t = sum(1 for r in writes if LTD_PLC_TITLED.search(r["clean_name"] or ""))
    names = [r["clean_name"] or "" for r in rows]
    dual = [f"{u}/{lo}" for u, lo in DUAL
            if any(re.search(r"\b" + u + r"\b", n) for n in names) and any(re.search(r"\b" + lo + r"\b", n) for n in names)]
    ok = a == 0 and f == 0 and t == 0 and not dual
    print(f"SC-E48-CENSUS ok={ok} rows={len(rows)} actions={dict(actions)} acronym_titled={a} form_upper={f} "
          f"ltd_plc_titled={t} dual={dual}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
