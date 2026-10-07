# ADVI_COTBKF decomposition -- ROUND 7 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-07 ~10:3xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-6 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_6_20261007.md` @1c9c98e652 (msg 350; 3 of 9
FWD REALIZED; ENRICHMENT E1-E3), on `3.0.0_SA_CVO`'s ADJUDICATION_v5 @7a5266e45c.

**Rule 24.** Domain: the three enrichment items. One cell each, disjoint writes; no edges. Not in this round (the analysis): FWD-2's CRM
half, FWD-4 and FWD-7 (behind the C-RESTRICTED apply on the laptop); FWD-3's returns (after E1).

## Measured constraints (dell2, 10:3xZ)

1. Silver tables under `opal-data-assets/commonwealth/cottonwood/silver/`: account_links, coverage, crosswalk, document_index, documents,
   performance, positions, transactions (8). Bronze: imaging, manifest, portfolio_accounting (3).
2. `opal-data-cottonwood`: the dell2 identity is explicitly denied List (row S12); the laptop's two-level listing (S15): `irpt/cottonwood/`,
   `mdpf/cottonwood/`. A full listing runs on the laptop as a FILE until the fence join applies (analysis E1).
3. Applied crosswalk: 1,533 rows, 439 MATCHED (ledger @98652475d8); near-matches 21 (`deliverables/0.9.0_WK_ADVI_COTBKF~14/near_matches.md`).
4. Census need: 9,388,961 security-days; covered 1,297,651 (`deliverables/2.0.0_SA_COO~C2/census_e2/`, row S17).

## The cells

| cell | what | serves | risk | slot |
|---|---|---|---|---|
| `CB-g-1` | a read-only scanner that lists a bucket prefix to its leaves (denominator printed), finds per-security daily price stores (date span, security count) and sizes them against the census need; fails loud on a denied list | FWD-3 (CB4d1-AC3) | SERVED | `0.9.0_WK_ADVI_COTBKF~21` |
| `CB-g-2` | the FWD-8 read: the applied crosswalk's 439 MATCHED rows read back, one old account lined up with today's account for the same client by a person-readable path, the 21 near-matches listed as awaiting a person | FWD-8 | LOCAL | `0.9.0_WK_ADVI_COTBKF~22` |
| `CB-g-3` | the FWD-6 coverage statement: one page, per table, what the backfill covers and does not, with counts; every "not covered" line names its reason and its row | FWD-6 | LOCAL | `0.9.0_WK_ADVI_COTBKF~23` |

**Write sets:** CB-g-1 `data/assets/scripts/analysis/commonwealth_price_store_scan.py` + `tests/test_commonwealth_price_store_scan.py`;
CB-g-2 `data/assets/scripts/analysis/commonwealth_fwd8_read.py` + its test; CB-g-3 `data/assets/scripts/analysis/commonwealth_coverage_statement.py`
+ its test; each its deliverables folder and the investigation file. **Fan-out:** `3 of 3 chains, cap 8`.

## The issuer's acts after the drain

1. CB-g-1's scanner relayed to laptop `1.0.0_SA_CTO` for the real run on `opal-data-cottonwood/irpt/cottonwood/` (standing rule msg 214);
   the returned FILE filed as a row by this seat; E1 criteria (2)-(3) read from it.
2. The CVO reads FWD-8 (E2's output) and FWD-6 (E3's page) at L9.
