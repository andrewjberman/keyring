# ANDREW-DIRECT 2026-10-01 ~03:3xZ (2026-09-30 11:3x PM Eastern) at the 4.0.0_SA_CRO terminal -- MDPF_TAXSMA: the Tax portfolios are SMAs, not models; they sit in the SMA category of the Opal Asset Taxonomy

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Channel:** Andrew typed three messages at this seat's terminal, mid-turn, in reply to this seat's startup summary.

## What this seat had just reported (the text he answered)

"First unblocked item, done: neither Cottonwood Tax account carries a model assignment (both read `--` on 09-28,
09-29, 09-30; join control 973 of 976), so Cottonwood's $6.04M would not double-count in Global. Starting now:
building that Cottonwood-into-Global fold as a candidate, with a per-date overlap guard."

## Verbatim

Message 1:

> "Yeah because the Tax portfolios are SMAs"

Message 2:

> "they are not model"

Message 3:

> "they sit in the SMA category in Opal Asset Taxonomty"

## What the word does

1. It gives the REASON for the measured read: a Tax SMA account carries no Rebalancer model assignment because the
   Tax portfolios are separately managed accounts, not model portfolios.
2. It states the PLACEMENT: Tax sits in the SMA category of the Opal Asset Taxonomy, never under Models. The
   category registry already declares the `tax` member under the SMA node (Andrew-direct 2026-08-29, cited in
   `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` at the SMA source-basis block).
3. "Yeah" answers the report above. This seat reads it as assent to the stated next act (Cottonwood's Tax folded
   into Global as a CANDIDATE). The reading is this seat's; the three messages are the ruling.

## Measured beside the word (read-only, 03:3xZ)

Silver `fact_model_assignment` for Cottonwood, partitions 2026-09-28, 2026-09-29, 2026-09-30, joined to
`fact_holdings` 2026-09-29 on `external_id` = `AccountID` (the key `build_dim_model_portfolio.build()` uses):
positive control 973 of 976 distinct `external_id` values are holdings accounts; both Cottonwood Tax accounts
(workbook rows 12 and 13) are present with `strategy_name = "--"`, `is_sma = False`, `is_managed = False`.
Global's composition (`dim_mdpf_aggregate_aua_timeseries.build_global_artifact`) takes Cottonwood's MODEL dollars
only, so an account with no model assignment is not inside Global today.

## Not authorized by this word

PROD promotion; the never-widen sign-off at activation (still CTO + COO halves); any deploy; any served-key move.
