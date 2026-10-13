# ADVI_COTBKF decomposition -- ROUND 83 (issuer 2.0.0_SA_COO~C2 on dell2; drafted 2026-10-13T22:30Z) -- the last round before the PARK

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-83 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_83_20261013.md` @01ed464473 (msg 7298), section 2: three items. PRD v0.10 @4d488ab2f0, no addendum.
Binding: the backfill floor (record @82c7c92449), the ruling on row D2-S131, and the never-widen rule (nothing here moves served output without both halves of a pair).

**Rule 24.** Domain: the three items of section 2 of the analysis. -> three cells, no uncovered member. Write surfaces are disjoint (see the table).

## Measured constraints (issuer)

1. **Cell ce-2 is LOCAL build + dry-run + the COO half DRAFTED; it does NOT apply.** The minted tables are served objects (one object per prefix, 2026-10-09T12:41Z); adding a field and re-minting them moves served output, which is a CTO+COO pair and a CloudOps apply. The CTO's analysis says "It goes under a never-widen pair"; no apply order is cut this round
   because the pair does not exist yet. The park (the analysis: "PARK at the round-83 drain") is the CTO's call after the cell's count is in.
2. **dell1's `porting_verdict` column is not on the Yahoo store's index yet** (dell1 pair B, CTO half SIGNED @261ab7bbf2 on origin/box/dell1; the column is written when dell1 applies). The cell is built and tested for all three branches dell1 signed (no verdicts file / a verdicts file / unreadable), with the absent column reading UNVERIFIED (fail closed).
3. **"Yahoo-sourced" is ruled here by the issuer, inside its own decomposition:** a price whose store `source` is `yahoo_finance`, or `linear_interpolation` (derived from Yahoo prices), is Yahoo-sourced; `transaction_observed`, `transaction_observed_capped`, `scoped_override` and `bd_txn_price` are not. The worker COUNTS under this rule and ALSO the count under the narrower rule (`yahoo_finance` only), so the CTO can change it.
4. **Value-enum law:** `claim` is NOT given a new member (dell1's CTO half: that would mint a value-enum member without its TAXONOMY LAW record). The label is a separate field, `porting_verdict`, with the values UNVERIFIED | PASS | FAIL | UNTESTABLE as dell1 defines them.
5. **Cell ce-3 reads and edits only the four ticker-only readers' files;** none of them is a served-output producer (census and provenance tools), so it is LOCAL. If the worker finds one that is, it stops and files a row (the pair is then the CTO's).

## The cells

| cell | item | serves | risk | depends_on | write surface | slot |
|---|---|---|---|---|---|---|
| `CB-ce-1` | every security a matched active account traded, tested against the active set; the cause per security; the held rows with windows (the four dell1 CUSIPs first) | FWD-3 | LOCAL | none | its deliverables folder only | `0.9.0_WK_ADVI_COTBKF~164` |
| `CB-ce-2` | `porting_verdict` carried into every COTBKF figure built on a Yahoo price, built and dry-run counted locally; COO half of the pair drafted; no apply | FWD-3 | LOCAL | none | under `data/assets/scripts/silver/`: `commonwealth_price_need.py`, `commonwealth_daily_valuation.py`, `commonwealth_fwd3_serve.py`, and under `silver/tests/`: `test_commonwealth_price_need.py`, `test_commonwealth_daily_valuation.py`, `test_commonwealth_fwd3_serve.py`, plus one new test file `test_commonwealth_porting_verdict.py`; its deliverables folder | `0.9.0_WK_ADVI_COTBKF~165` |
| `CB-ce-3` | the four ticker-only readers of the price store keyed by (ticker, asset_name) | FWD-3 | LOCAL | none | `data/assets/scripts/analysis/commonwealth_price_census.py` and `data/assets/scripts/silver/{commonwealth_price_basis_census,commonwealth_bond_custodian_price,commonwealth_bd_txn_provenance}.py`; tests `analysis/tests/test_commonwealth_price_census.py`, `silver/tests/test_commonwealth_price_basis.py` and one new `silver/tests/test_commonwealth_ticker_asset_key.py`; its deliverables folder | `0.9.0_WK_ADVI_COTBKF~166` |

**Fan-out:** `3 of 3 chains, cap 8` (the write surfaces are disjoint, so the three run at once). Each carries at most three mechanical criteria and one judgment criterion graded by `3.0.0_SA_CVO` at L9.
