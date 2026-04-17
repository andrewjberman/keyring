# Session E — C_03 Phantom Outflow Pulse Fix

**Agent:** 0.4.0_DS_ClientPlatform~E
**Date:** 2026-04-17
**Started:** ~13:32 UTC
**Status:** Fix committed + pushed + S3-uploaded. QA run deferred (Andrew: "not yet we're busy").

## Origin

Andrew-directed handoff from 0.4.2_RD_AdvisorIntelligence at 13:32 UTC.
RD flagged phantom outflow pulse pattern on `platinum/accounts/z0820277481/summary.json` timeseries:
every Friday showed a ~$4M negative `nna_canonical` + positive `outflows_canonical`, and the following
Saturday reverted with a negative `outflows_canonical` of equal magnitude. AUA was continuous across
the pairs (no real asset movement), so the flows were synthetic artifacts.

## Investigation

1. `comp-platinum reverse platinum/accounts/{account_id}/summary.json` -> producer `D_04.client_portal_summary.py` (function `_account_ts_to_canonical`, line 938).
2. Downloaded D_04's platinum output + D_02's aua_timeseries input for z0820277481. The D_02 file's `cum_inflows` / `cum_outflows` values were NOT monotonic non-decreasing, despite field names and C_03 docstring (line 32-33) both asserting "cumulative since inception".
3. Traced to C_03 writer. D_02 just passes the column through; C_03 is the producer of `gold/timeseries/account_performance.parquet`.
4. Parquet-verified for z0820277481 (166MB download):

| date       | daily_outflow | cum_outflows |
|------------|---------------|--------------|
| 2026-01-08 | 0             | 0            |
| 2026-01-09 | 300000        | 4016138      |
| 2026-01-10 | 0             | 0            |
| 2026-01-11 | 0             | 0            |
| 2026-03-27 | 0             | 4376138      |
| 2026-03-28 | 0             | 0            |
| 2026-04-13 | 6985000       | 11361138     |

`cum_outflows.diff().min()` < 0 across the 714-row account history. Cumulative is oscillating, not monotonic.

5. RD independently confirmed pipeline-wide scope: 14/19 sampled 49financial accounts show the pattern, and in 14 of those, negative-flow-day count equaled exactly half of nonzero-flow-day count — the pulse-and-revert signature.

## Root Cause

`C_03.account_performance.py` lines 214-219 (pre-fix):

```python
if not flows.empty:
    result = result.merge(flows, on=['date', 'account_id'], how='left')
for col in ['daily_inflow', 'daily_outflow', 'cum_inflows', 'cum_outflows']:
    if col not in result.columns:
        result[col] = 0.0
    result[col] = result[col].fillna(0.0)
```

- `flows` is transaction-sparse: rows exist only for (date, account_id) pairs where a transaction actually occurred. `flows.cum_*` were correctly cumsum'd at line 163-164, but only over the sparse subset.
- `result` (from `gains`) is dense: one row per (date, account_id) across the full date grid.
- Left-merge places correct `cum_*` on transaction days and NaN on non-transaction days.
- `fillna(0)` on `cum_*` then zero-gaps the cumulative state on non-transaction days, breaking monotonicity.

Downstream amplification in `D_04._account_ts_to_canonical` (line 961-962) takes first-difference of
`cum_*` to emit `outflows_canonical`. When the "cumulative" input goes `0 -> 4M -> 0`, the first-diff
emits `+4M` on the transaction day and `-4M` the day after — the exact Fri-post / Sat-revert pulse
signature RD observed in the platinum summary.

## Fix

C_03 lines 214-219 replaced with:

```python
if not flows.empty:
    result = result.merge(
        flows[['date', 'account_id', 'daily_inflow', 'daily_outflow']],
        on=['date', 'account_id'], how='left',
    )
for col in ['daily_inflow', 'daily_outflow']:
    if col not in result.columns:
        result[col] = 0.0
    result[col] = result[col].fillna(0.0)
# Recompute cum_* on the dense (date x account) grid AFTER the merge.
# flows.cum_* only covers transaction days; fillna(0) on the merged grid
# would zero-gap cum_* on non-transaction days, breaking monotonicity and
# causing D_04 first-diff to emit phantom +X / -X pulse-revert pairs
# (RD 2026-04-17 platinum/accounts/*/summary.json investigation).
result = result.sort_values(['account_id', 'date'])
result['cum_inflows']  = result.groupby('account_id')['daily_inflow'].cumsum()
result['cum_outflows'] = result.groupby('account_id')['daily_outflow'].cumsum()
```

- Merge now carries only `daily_*` from `flows`; `flows.cum_*` columns are dropped (they were stale anyway, covering only the sparse subset).
- `fillna(0)` on `daily_*` is legitimate — non-transaction days really do have zero daily flow.
- `cum_*` recomputed via `groupby.cumsum()` across the dense date grid per account. Guarantees monotonic non-decreasing.

Side-effects resolved automatically by this single-site fix:
- D_04 first-diff (`_account_ts_to_canonical`): `outflows_canonical` no longer goes negative.
- D_02 TTM / QTD / YTD window deltas (`end_cum - start_cum` at lines 950-951, 1290-1291, 2410-2411): now reflect true inception-to-date cumulative.
- C_01b / C_06 / C_07 / D_00 / D_00b / D_00c / D_01 / D_03: all consume `account_performance.parquet`; whichever of them reads `cum_*` as cumulative now gets correct values.

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/C_03.account_performance.py` | Lines 214-219: post-merge `groupby.cumsum()` replaces pre-merge `fillna(0)` on `cum_inflows` / `cum_outflows`. +13 / -2. |

## Deploy State

| Step          | Result                                                         |
|---------------|----------------------------------------------------------------|
| Commit SHA    | 85bb2daa                                                       |
| Author        | 0.4.0_DS_ClientPlatform~E                                      |
| Branch        | CLOUD                                                          |
| Push          | origin/CLOUD up to date                                        |
| S3 upload     | s3://opal-data-bd/code/gold/C_03.account_performance.py (10.2 KiB, 2026-04-17 09:42:43 local) |
| Deployed MATCH| comp-pipescript deployed C_03: 1 MATCH / 0 STALE               |
| QA run        | DEFERRED per Andrew — CP-DS1 is active on ops lane             |
| PROD trigger  | NOT INVOKED — lane separation with CP-DS1, fix will pick up on next scheduled PROD run |

## Compiler Tools

| Tool | Invocation | Result |
|------|-----------|--------|
| comp-platinum reverse | `platinum/accounts/{account_id}/summary.json` | Identified producer D_04::build_firm_mix_summary() (prefix match); actual function `_account_ts_to_canonical` confirmed via grep. |
| comp-pipescript io | `C_03` | Confirmed reads (ACCOUNTS_DIMENSION from A_00, CANONICAL_ACCOUNT_GAINS_PREFIX from silver, CLIENT_PERFORMANCE from C_02) and writes ACCOUNT_PERFORMANCE. |
| comp-pipescript consumers | `C_03` | 10 downstream consumers (C_01b, C_06, C_07, D_00, D_00b, D_00c, D_01, D_02, D_03, D_04). |
| comp-blast | `C_03.account_performance` | No direct function-level downstream; confirms artifact-level blast is via account_performance.parquet. |
| comp-pipescript deployed | `C_03` | MATCH. |
| py_compile | `C_03.account_performance.py` | OK. |

`comp-validate C_03 --artifact ...` deferred to QA phase — no QA output yet.

## Handoffs / Messages Sent

| Timestamp (UTC) | To | Subject |
|-----------------|-----|--------|
| 13:33:14 | 0.4.2_RD_AdvisorIntelligence | ACK — phantom outflow pulse investigation |
| 13:33:37 | 2.0.0_SA_COO | HEADS-UP — ~E picked up phantom outflow investigation |
| 13:38:34 | 0.4.2_RD_AdvisorIntelligence | ROOT CAUSE — C_03 merge+fillna(0) breaks cumulative invariant |
| 13:38:50 | 2.0.0_SA_COO | ROOT CAUSE + proposed fix — pipeline-wide scope |
| 13:43:20 | 0.6.0_AE_PartnerETL | QA request — --single C_03 + D_02 + D_04 on bd-gold-qa-runner |
| 13:43:27 | 2.0.0_SA_COO | PROGRESS — committed + pushed + S3-uploaded |
| 13:44:04 | 0.6.0_AE_PartnerETL | HOLD — stand down on C_03 QA request per Andrew |

RAVC loop with RD is closed — RD ACK'd root cause, stood down on portal work-arounds.

## Current State

- Fix is shipped to S3 as the canonical script; next scheduled PROD run (post-CP-DS1 unhalt) will auto-apply the fix across the full pipeline.
- QA on bd-gold-qa-runner is DEFERRED per Andrew. AE acknowledged stand-down.
- Zero downstream portal code changes required — D_04 first-diff is structurally correct; it was emitting garbage because its input was garbage.
- `cum_*` consumers elsewhere (D_02 TTM / QTD / YTD) will also self-correct on the next rebuild.

## Next Steps

- [0.6.0_AE_PartnerETL] No action — stood down.
- [2.0.0_SA_COO] Once CP-DS1 ships and PROD is unhalted, C_03 fix will be picked up on the next regular PROD run. Optionally invoke bd-gold-trigger manually once CP-DS1 completes.
- [0.4.2_RD_AdvisorIntelligence] Await next fresh platinum regen. Post-fix, the daily AUA+NNA overlay on the main chart will stop cliffing on the most-recent unreverted pulse date.
- [~E] Standing by for next ~E-targeted task order. Will re-verify z0820277481 + sample accounts once post-fix platinum is available.

## Do NOT

- Do NOT touch base-serial CP-DS1 work (~B's lane).
- Do NOT invoke bd-gold-trigger for this fix ahead of CP-DS1 — coordinate via COO.
- Do NOT re-request AE QA run without Andrew re-authorizing.
