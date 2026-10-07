# resolve_tickers.py -- canonical-first switch: the gap record (SC-e-43, FWD-5)

Read-only scans of bd-securities (10,965 rows) and etf-classifications (3,507 rows), ConsistentRead, 20261007. Script: org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/resolve_tickers_switch_check.py.

## ATTRIBUTE: asset_name_raw

OLD-LIST-ROWS: 10904
CANONICAL: no -- etf-classifications rows carrying asset_name_raw: 0 of 3,507
USED-BY: _resolve_bd_securities_exact (data/black_diamond/scripts/classification/resolve_tickers.py:246); _resolve_bd_securities_prefix (data/black_diamond/scripts/classification/resolve_tickers.py:277); _resolve_individual_stock_pattern (data/black_diamond/scripts/classification/resolve_tickers.py:335); _resolve_mutual_fund_pattern (data/black_diamond/scripts/classification/resolve_tickers.py:411)

## ATTRIBUTE: name_aliases

OLD-LIST-ROWS: 6
CANONICAL: no -- etf-classifications rows carrying name_aliases: 0 of 3,507
USED-BY: _resolve_bd_securities_exact (data/black_diamond/scripts/classification/resolve_tickers.py:254)

## CANONICAL-FIRST HITS

CANONICAL-FIRST-HITS: 142

Claim `inferred` (row W25-S1): held names are the SECURITY nodes' descriptions of the Holdings producer's own local build, --as-of 2026-10-05, no --upload (the served per-firm objects are unreadable from this device); distinct normalized names 4,615 across 49financial 1,843, cottonwood 1,264, inflection 1,601 held securities. Canonical rows carrying `name`: 883 of 3,507; rows keyed NAME:: or CUSIP: and names two rows map to different tickers are not resolved by the new method.
