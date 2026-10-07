# ADVI_COTBKF decomposition -- ROUND 11 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-07 ~12:3xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-10 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_10_20261007.md` (msg 549; its commit lands
with MSTR's merge): FWD-3's pull is MDPF_SECHIST's act on dell1 under Andrew's per-use word (PRD v0.4 ADDENDUM 2); round 11 E1 = the
price-need FILE that project consumes, with no fetch.

**Rule 24.** Domain: E1. One cell.

## Measured constraints

1. Census on the 2010-2027 calendar (`deliverables/2.0.0_SA_COO~C2/census_e2/`, row S17): universe 4,634, priced 1,720, security-days
   needed 9,388,961, covered 1,297,651; so 2,914 securities and 8,091,310 security-days uncovered (row S19).
2. `commonwealth_price_need.py` measures a different basis (each security's held span, 3,421,735 in total, the figure ADDENDUM 2 cites);
   the FILE must reconcile to the census basis the analysis names, from the census's own per-security arithmetic.
3. ADDENDUM 2 sources: Yahoo Finance for equity, ETF and fund securities; Bloomberg at site Z for fixed income and other.

## The cell

| cell | what | serves | risk | slot |
|---|---|---|---|---|
| `CB-k-1` | the price-need FILE: one row per unpriced security (id, asset class, ADDENDUM 2 source, first and last date needed, day count), totals per source adding to 2,914 securities and 8,091,310 security-days; no price fetched | FWD-3 | LOCAL | `0.9.0_WK_ADVI_COTBKF~27` |

**Write set:** `data/assets/scripts/analysis/commonwealth_price_need_file.py` + its test; the deliverables folder; the investigation file.
**Fan-out:** `1 of 1 chains, cap 8`. After the drain the issuer sends the FILE's path to `1.0.0_SA_CTO~DELL2`, who forwards it to dell1.
