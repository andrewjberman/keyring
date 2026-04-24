# ADVI_49EXEC.POSITIONS — Session closeout log
# 0.4.0_DS_ClientPlatform — 2026-04-24
# Commit: 13eaca78 (CLOUD, pushed)

## Compiler Tools Run Log

| Step | Command | Observed | Pass? |
|------|---------|----------|-------|
| P0 | comp-pipescript io D_04 | READS include HOLDINGS_LOTS_PREFIX + ACCOUNT_TEAM + ACCOUNTS_DIMENSION + books (batch). No new reads needed. | PASS |
| P1.1 | comp-platinum reverse 'platinum/advisors/*/positions.json' | PRODUCER=empty; SERVED_VIA shows existing wildcard route (correct pre-ship) | PASS |
| P1.2 | comp-blast D_04.client_portal_summary | "No downstream consumers found" (graph node naming; expected) | OK |
| P1.3 | python -m py_compile D_04 | exit 0 | PASS |
| P1.4 | .tools/ds-commit-gate.sh D_04 | OK: pre-commit gate clean | PASS |
| P2.1 | dry-run travis_penfield spot-check | 642 tickers, 35,930 lots; sum(top25 MV)=$320M <= AUM=$431M; 13 fields; sorted desc | PASS |
| P2.2 | comp-validate D_04_positions_output | 7 PASS, 0 ERROR, 3 SKIP; exit 0 | PASS |
| P2.3 | comp-pipescript deployed D_04 (post S3 upload) | MATCH | PASS |
| P3   | pending 23:00Z nightly | aws s3 ls + comp-platinum reverse + 3-advisor spot-check | PENDING |

## Key decisions

- Aggregation grain: (advisor_id, ticker) — book_name from book.json used as bridge to account_team names
- total_aum source: book.summary.tagged_aua (consistent with rest of portal)
- asset_class: ETFClassifier.instance() (same as build_account_summaries at L1257) — pre-computed at (ticker, asset_name) grain to avoid O(N_lots) calls
- account_id join: account_team via all 5 role columns (architect, implementor, consultant, local_ops, additional_advisor) — same mechanic as _build_advisor_accts_aua
- _TOP_N_POSITIONS = 25 (module-level constant, not buried in function)
- CTO redline 1: cb == 0.0 → gain_pct = None
- CTO redline 2: acquisition_date dropna() before min/max; valid_dates.empty → all three date fields None

## Spot-check: Travis Penfield (top-AUM advisor)
- AUM: $431,609,008; Accounts: 509; Open lots: 35,930; Unique tickers: 642
- Top 5: IEFA ($41.7M, 12.2% gain), DIVZ ($38.3M, 3.4%), IDVZ ($32.7M, 17.2%), SPYM ($27.9M, 9.3%), PFDE ($25.7M, 3.6%)
- sum(top25 MV) = $320.6M <= total_aum $431.6M ✓

## Phase 3 pending (23:00Z tonight)
- aws s3 ls s3://opal-data-bd/platinum/advisors/ --recursive | grep '/positions.json$' | head -5 (expect ~45+)
- comp-platinum reverse 'platinum/advisors/*/positions.json' → PRODUCER=D_04
- 3-advisor spot-check (top/median/tail AUM reconciliation)
