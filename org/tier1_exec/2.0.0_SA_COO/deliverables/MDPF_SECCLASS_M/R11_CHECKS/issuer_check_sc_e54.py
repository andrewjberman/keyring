#!/usr/bin/env python3
"""issuer_check_sc_e54.py -- MDPF_SECCLASS round 9 issuer check for cell SC-e-54 (the contract edits, analysis rulings 2.5-2.7).

READ-ONLY. Reads org/standards/MDPF_SECCLASS_CONTRACT.json (the repo file) and the round-8 measured values
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/SECTOR_INDUSTRY_GROUP_VALUES_20261007.json. PASSES only if:
  - contract_version is above 0.5.0;
  - fields.gics_sector.values is exactly the 11 GICS sectors (the 10 measured plus Real Estate; ruling 2.6);
  - fields.gics_industry_group.values is exactly the 25 full GICS industry-group names (ruling 2.7), and
    fields.gics_industry_group.vendor_decode is a dict whose keys include every vendor spelling of contract 0.5.0's 23 values and
    whose every value is one of the 25 names (a spelling outside the table leaves the field empty: that rule is the writer's);
  - fields.sub_asset_class.values_by_class is a dict over exactly the six classes {cash, fixed_income, equity, structured,
    alternatives, commodities}, each a non-empty list of distinct strings (ruling 2.5: the closed list is the bound for every class).
Prints SC-E54-CONTRACT ok=True|False with the first problem. Run from the repo root.
"""
import json
import sys

CONTRACT = "org/standards/MDPF_SECCLASS_CONTRACT.json"
CLASSES = {"cash", "fixed_income", "equity", "structured", "alternatives", "commodities"}
SECTORS = {
    "Communication Services", "Consumer Discretionary", "Consumer Staples", "Energy", "Financials", "Health Care",
    "Industrials", "Information Technology", "Materials", "Real Estate", "Utilities",
}
GROUPS = {
    "Energy", "Materials", "Capital Goods", "Commercial & Professional Services", "Transportation", "Automobiles & Components",
    "Consumer Durables & Apparel", "Consumer Services", "Consumer Discretionary Distribution & Retail",
    "Consumer Staples Distribution & Retail", "Food, Beverage & Tobacco", "Household & Personal Products",
    "Health Care Equipment & Services", "Pharmaceuticals, Biotechnology & Life Sciences", "Banks", "Financial Services",
    "Insurance", "Software & Services", "Technology Hardware & Equipment", "Semiconductors & Semiconductor Equipment",
    "Telecommunication Services", "Media & Entertainment", "Utilities", "Equity Real Estate Investment Trusts (REITs)",
    "Real Estate Management & Development",
}
# contract 0.5.0's industry-group values, as measured in round 8 (vendor spellings, some cut at 30 characters)
VENDOR_050 = [
    "Automobiles & Components", "Banks", "Capital Goods", "Commercial & Professional Serv", "Consumer Discretionary Distrib",
    "Consumer Durables & Apparel", "Consumer Services", "Consumer Staples Distribution", "Energy", "Financial Services",
    "Food, Beverage & Tobacco", "Health Care Equipment & Servic", "Household & Personal Products", "Insurance", "Materials",
    "Media & Entertainment", "Pharmaceuticals, Biotechnology", "Semiconductors & Semiconductor", "Software & Services",
    "Technology Hardware & Equipmen", "Telecommunication Services", "Transportation", "Utilities",
]


def vtuple(v):
    try:
        return tuple(int(x) for x in str(v).split("."))
    except ValueError:
        return (0,)


def problem(c):
    if vtuple(c.get("contract_version")) <= (0, 5, 0):
        return f"contract_version {c.get('contract_version')} not above 0.5.0"
    f = c.get("fields", {})
    sec = set((f.get("gics_sector") or {}).get("values") or [])
    if sec != SECTORS:
        return f"gics_sector values differ: missing={sorted(SECTORS - sec)} extra={sorted(sec - SECTORS)}"
    ig = f.get("gics_industry_group") or {}
    vals = set(ig.get("values") or [])
    if vals != GROUPS:
        return f"gics_industry_group values differ: missing={len(GROUPS - vals)} extra={sorted(vals - GROUPS)[:3]}"
    dec = ig.get("vendor_decode")
    if not isinstance(dec, dict):
        return "gics_industry_group.vendor_decode absent"
    miss = [s for s in VENDOR_050 if s not in dec]
    if miss:
        return f"vendor_decode lacks {len(miss)} measured spellings, first={miss[0]!r}"
    bad = [k for k, v in dec.items() if v not in GROUPS]
    if bad:
        return f"vendor_decode maps {bad[0]!r} outside the 25 names"
    sac = (f.get("sub_asset_class") or {}).get("values_by_class")
    if not isinstance(sac, dict) or set(sac) != CLASSES:
        return f"sub_asset_class.values_by_class must cover exactly {sorted(CLASSES)}"
    for cls, lst in sac.items():
        if not isinstance(lst, list) or not lst or len(set(lst)) != len(lst) or not all(isinstance(x, str) and x for x in lst):
            return f"sub_asset_class list for {cls} empty or not distinct strings"
    return None


def main():
    with open(CONTRACT, encoding="utf-8") as fh:
        c = json.load(fh)
    p = problem(c)
    print(f"SC-E54-CONTRACT ok={p is None} version={c.get('contract_version')} {p or ''}".rstrip())
    return 0 if p is None else 1


if __name__ == "__main__":
    sys.exit(main())
