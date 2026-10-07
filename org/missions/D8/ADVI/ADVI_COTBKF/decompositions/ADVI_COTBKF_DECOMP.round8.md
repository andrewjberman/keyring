# ADVI_COTBKF decomposition -- ROUND 8 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-07 ~10:5xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-7 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_7_20261007.md` @625987b867 (msg 389; 4 of 9
REALIZED; ENRICHMENT E1-E3), on `3.0.0_SA_CVO`'s ADJUDICATION_v6 @cfd9d3c4f4 (CB7g3-AC3 NOT MET).

**Rule 24.** Domain: E1, E2, E3. Subtraction at the cut:
- **E1 + E2:** both write the coverage page (E1's criterion 3 is the page's transactions line; E2 rewrites the page), so they are ONE
  cell by write set, `CB-h-1`.
- **E3 (re-apply to 1,415,137 rows): NOT CUT.** The analysis gates it on E1's finding, and the issuer read before the cut that the
  premise contradicts the ratified PRD: `prd/ADVI_COTBKF_PRD.md:204-206` (v0.4 addendum item 1, "C-SILVER clarified: every delivered row
  is kept ... rebuilt with all 1,416,497 records") and `:114` (C-SILVER: "two identical lines are two rows"); the code agrees
  (`data/assets/scripts/silver/commonwealth_transactions.py:13-15`, "nothing is de-duplicated"). W2-S1's 1,415,137 predates the ruling.
  Put to `1.0.0_SA_CTO~DELL2` (msg 20261007T105704Z) with REC strike E3; an ENDPOINT question is the CTO's, not this seat's.

## The cell

| cell | what | serves | risk | slot |
|---|---|---|---|---|
| `CB-h-1` | the applied transactions table's exact-repeat count measured by W2-S1's key (all 20 vendor columns) and its cause cited; the FWD-6 page rewritten to lead with one plain line per kind of record, each with its own date span and count | FWD-1 (W23-S1), FWD-6 (CB7g3-AC3) | LOCAL | `0.9.0_WK_ADVI_COTBKF~24` |

**Write set:** `data/assets/scripts/analysis/commonwealth_tx_repeats.py` (new) + its test; `data/assets/scripts/analysis/commonwealth_coverage_statement.py`
+ its test; the deliverables folder; the investigation file. **Fan-out:** `1 of 1 chains, cap 8`.
