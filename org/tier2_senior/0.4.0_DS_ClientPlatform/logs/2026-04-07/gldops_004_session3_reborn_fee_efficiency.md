# Session Log — GLDOPS.004 Session 3 + ADVI_REBORN + ADVI_NNAFEE
**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-07 (evening) → 2026-04-08
**Projects:** ADVI_GLDOPS, ADVI_REBORN, ADVI_NNAFEE

---

## Summary

Continuation of the gold pipeline refactoring session. Completed REBORN validation chain (W1-001 through W3-004), NNAFEE fee integration, fee efficiency metric redesign, and NNA reconciliation investigation. Major bug fixes in D_00 (leaderboard NNA) and D_01 (partner_analytics zeros). Diagnosed the 14% NNA attribution gap (house_split + 49F House unresolved).

---

## Commits This Session

| Commit | Description |
|--------|-------------|
| 0eb4c0b3 | feat(NNAFEE): fee_summary in book.json + client_detail.json |
| 6469ac80 | task(REBORN.W4-001): roles already in employee leaderboard |
| 222ea359 | fix(classification): money market/sweep/cash → fixed_income |
| 780ff863 | fix(mix): cash → unclassified in period views |
| c530be00 | perf: vectorize B_00, B_02, C_02 hot paths (GPT patches) |
| ca3c57de | feat(C_08): windowed fee scorecard QTD/YTD/1Y/3Y/Max |
| db339cdc | fix(C_08): log-log regression model |
| 75338c7e | feat(C_08): regression_residual_ratio for dot coloring |
| a4ae1c57 | feat(REBORN.W1-001): data lineage manifest |
| b4c64a5c | feat(REBORN.W1-002): E_20 cross-script validation |
| f921131c | feat(REBORN.W3-002): E_21 reconciliation reference generator |
| d0b6ddf0 | fix(D_01): partner_analytics zeros (date fallback) |
| 70b12d00 | fix(D_00): leaderboard NNA uses transaction flows not residual |
| 5f485323 | fix(C_02): nna column is now transaction NNA not residual |
| 2870c567 | fix(TICKID): resolve_tickers holdings prefix |
| 4941ff27 | fix(TICKID): resolve_tickers portable for EC2 |
| 93203fc1 | feat(gold): E_22 diagnose unassigned accounts |
| 479cf479 | feat(gold): E_23 fee split integrity diagnostic |
| 2a8e5969 | feat(C_08): commission, fee_bps_weighted, efficiency_pctile |
| 5ddd4b38 | feat(gold): E_24 rebuild fee scorecard from existing parquets |

---

## Part 1: NNAFEE + REBORN Task Orders

All DS task orders completed:
- NNAFEE.000: fee_summary block in D_02 book.json (by_role) and client_detail.json (by_account)
- REBORN.W4-001: roles[] already in employee leaderboard (no code change needed)
- REBORN.W2-002: windowed fee scorecard (QTD/YTD/1Y/3Y/Max with per-window regression)
- REBORN.W1-001: data lineage manifest (gold/manifests/data_lineage.json)
- REBORN.W1-002: E_20 cross-script validation script
- REBORN.W3-002: E_21 reconciliation reference generator
- REBORN.W3-004: mismatch diagnosis (3 issues found, 1 fixed)

---

## Part 2: Classification Fix

ETFClassifier.classify() returned '' for money market/sweep/cash securities. C_06 mapped '' → 'equity' (wrong). Fixed to return 'fixed_income' for all cash-pattern matches + CASH_USD synthetic ticker. Money market = short-duration fixed income.

mix_views.py: renamed 'cash' residual → 'unclassified' since all real cash instruments are now fixed_income. The residual is settlement float / positions missing from the cube.

---

## Part 3: NNA Reconciliation

### Root cause of $75M vs $42M (44% gap)
The architect_leaderboard used the `nna` column from client_performance — which was `cumsum(aua_residual)`, the accounting residual, NOT transaction NNA. header_metrics used `cum_inflows - cum_outflows` (correct).

Fixed in three places:
- D_00: leaderboard uses cum_inflows - cum_outflows (70b12d00)
- C_02: nna column redefined as cum_inflows - cum_outflows (5f485323)
- D_01: date fallback for period boundaries on weekends (d0b6ddf0)

### Remaining 14% gap after fix
E_22 diagnostic revealed:
- 762 accounts with architect = "49F House" → Unresolved ($133M AUA)
- House split averages 5.9% across nearly all accounts
- Only 9 accounts truly missing from account_team

E_23 fee split analysis:
- 68.8% of accounts have splits summing to 100 (clean)
- 30.9% have all-zero splits (no fee structure)
- 49F House accounts: architect_split = 0%, implementor avg = 21.5%
- Unassigned accounts: architect_split = 0%, implementor avg = 66.8%

Strategies proposed for 100% NNA attribution:
1. Absorb house_split pro-rata into named advisors
2. Attribute 49F House accounts to implementor
3. Synthetic "Firm Unattributed" entry for remainder

---

## Part 4: Fee Efficiency Redesign

Andrew's new spec replaced the implied_revenue heuristic:
- fee_bps_weighted: AUA-weighted avg fee rate per advisor
- commission: fee_bps/10000 × AUA × (calendar_days/365.25)
- efficiency_pctile: rank 1-100 (lowest commission/nna = 100th = best)
- Regression: log(commission) ~ log(nna)

Implemented in C_08 (2a8e5969). E_24 script rebuilds the scorecard JSON from existing parquets without a gold re-run (5ddd4b38). E_24 ran successfully: 152 advisors, pctile range 1-99, R^2=0.86 for max window.

Portal showing 50th percentile for everyone due to CloudFront cache serving stale JSON. Full /* invalidation submitted. If still stale after propagation, issue is in portal field resolution.

---

## Key Decisions

- Money market / sweep / cash reserve → fixed_income (not equity, not a separate category)
- Mix taxonomy: 3 categories only (equity, fixed_income, alternatives). "Unclassified" residual exists but frontend ignores it
- Commission = fee × AUA × period_fraction (snapshot AUA, calendar days / 365.25)
- Efficiency percentile: lowest commission/nna ratio = 100 (best), highest = 1 (worst)
- Log-log regression on NNA vs Commission (power law model)
- House_split is internal fee revenue split — pro-rata absorption is correct for NNA attribution

---

## Pending Next Session

1. [DS] Verify CloudFront invalidation resolved the 50th percentile issue — if not, debug portal field resolution
2. [DS] Implement house_split absorption + 49F House → implementor attribution in C_07/C_08 for 100% NNA coverage
3. [AE] Run resolve_tickers.py for ticker_resolution.parquet
4. [DT] Deploy opal-partners-data Lambda (old-key fixes + deprecated routes)
5. [DT] Disable bd-portal-publisher + bd-portal-advisor-publisher Lambda triggers
