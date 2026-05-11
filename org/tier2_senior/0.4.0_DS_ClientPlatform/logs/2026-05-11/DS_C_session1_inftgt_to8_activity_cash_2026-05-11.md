# DS~C 2026-05-11 — ADVI_INFTGT.TO-8 close (activity_scan + cash_drag)

**Agent:** 0.4.0_DS_ClientPlatform~C (first session on this project)
**TO:** ADVI_INFTGT.TO-8 (Andrew direct via 2.0.0_SA_COO; 1hr deadline)
**Status:** SHIPPED — commit `147b85326` + S3 MATCH for both scripts

## TL;DR

INF_D_05.activity_scan + INF_D_06.cash_drag now actually compute. Two distinct
script-level bugs + one upstream-defensive guard. Local standalone validation
on current silver/gold state produces meaningful artifacts (chain rerun on
HOLD per Andrew, so artifact deploy waits for next authorized cascade).

| Artifact | Before | After (standalone local validation) |
|---|---|---|
| `activity_scan.json` | 305 rows / aua=$0 / txn=0 / score≈0.5 / all buy_and_hold | 305 rows / 293 with AUA ($189.7M) / 305 with TRN signal / median 752 txn / active=152 buy_and_hold=153 |
| `cash_drag.json` | 292 rows / aua=$0 / cash=$0 / cash_pct=0 / days_above non-zero only from history | 293 rows / 293 with AUA ($189.85M) / cash $14.51M (~7.6% firm-wide) / 92 above 5% now / 135 above any day |

## Diagnosis (3 distinct findings)

### Finding 1 — INF_D_05 tz-aware vs tz-naive Timestamp comparison (script bug)

`cutoff = pd.Timestamp.now(tz='UTC') - timedelta(days=365)` was tz-aware.
`sub['trade_date'] = pd.to_datetime(...)` is tz-naive (silver/transactions
stores trade_date as `datetime64[ns]` tz-naive).

`sub['trade_date'] >= cutoff_date` raised `TypeError: Invalid comparison between
dtype=datetime64[ns] and Timestamp`. The exception propagated up to the
`fut.result()` call inside `load_txns_12m`'s executor loop where the broad
try/except logged a `WARN` per partition and treated as `None`. Result: every
one of the 1,510 TRN partitions was silently skipped, `len(dfs) == 0`, return
empty DataFrame, downstream merge fills `txn_count_12m=0` for every account
→ every household had txn_count_12m=0 and (with all ties) activity_score
landed at the percentile-rank-with-ties value of ~0.5016 for every row.
Median-tie pushed every HH into `buy_and_hold`.

Fix: `cutoff = (pd.Timestamp.now(tz='UTC') - timedelta(days=365)).tz_localize(None)`

Empirical: post-fix, 263,812 TRN rows load in trailing 12M; 838 accounts
have at least one TRN; median per-HH txn_count_12m = 752; segments split
152 active / 153 buy_and_hold.

### Finding 2 — INF_D_05 + INF_D_06 vulnerable to upstream pricing regression (defensive gap)

The original `load_latest_holdings_aua` (INF_D_05) and `list_holdings_keys`
(INF_D_06) took `keys[-1]` from `gold/holdings/` as the "current" snapshot
without verifying upstream health. Empirically:

| Date | rows | mv_sum | mv_nonzero | price_nonzero |
|---|---|---|---|---|
| 2026-05-04 | 9,315 | $189.6M | 9,311/9,315 | 9,311 |
| 2026-05-05 | … | $189.85M | … | … |
| **2026-05-06** | … | **$0** | **0** | **0** |
| **2026-05-07** | 9,351 | **$0** | **0** | **0** |
| **2026-05-08** | 9,348 | **$0** | **0** | **0** |

Three consecutive days of zero-MV (price=0, units populated) starting
2026-05-06. Pre-2026-05-06 is healthy ($188–190M firm AUA). This is an
upstream INF_B_01 (priced daily holdings) regression — out of scope for
TO-8 but surfaced separately to COO.

Fix in INF_D_05 (also takes COO's canonical-source directive): switch
AUA source from `gold/holdings/{latest}.parquet` to canonical
`gold/timeseries/client_performance.parquet`. Walk back to the latest
`date` where `total_aua > 0`. This guarantees partner-facing total_aua
aligns with the canonical AUA source per COO architectural-parity note.

Fix in INF_D_06: bounded walk-back (up to the 14 most-recent window keys)
to find the latest snapshot with `market_value` sum > 0. days_above_threshold
continues to use the full trailing-90-day window (history is fine — only
the most recent 3 dates are zero).

### Finding 3 — PRD §4.3 empty-state convention codified

Both scripts now emit `[]` per PRD §4.3 when no signal is recoverable:

- INF_D_05: `if txns.empty and hh_aua.empty: return []`
- INF_D_06: full-window zero-MV → `return []`; no healthy snapshot in
  bounded walk-back → emit [] downstream.

Avoids the original failure mode of emitting 305 rows of ambiguous zeros
that the frontend treats as "real but uninteresting" data instead of
"awaiting data."

## Files Modified

| File | Change |
|---|---|
| `data/orion/scripts/gold/INF_D_05.activity_scan.py` | tz-naive cutoff fix; AUA source switched from gold/holdings to canonical client_performance with healthy-date walk-back; empty-state gate when both signals collapsed |
| `data/orion/scripts/gold/INF_D_06.cash_drag.py` | bounded walk-back to latest healthy snapshot for the "current" panel; full-window zero-MV → emit [] per PRD §4.3 |

Net diff: +108 / -34 across the two files (commit `147b85326`).

## Deploy + verify

| Step | Result |
|---|---|
| `.tools/ds-commit-gate.sh` | PASS — py_compile + AST + ruff py39 for both files |
| `.tools/safe-commit.sh` | OK — scoped to 2 files, no contamination |
| Commit | `147b85326` (author 0.4.0_DS_ClientPlatform~C) |
| Push to CLOUD | `345401612..147b85326` |
| `.tools/safe-deploy.sh` (pre-push hook) | DEPLOYED + verified both files |
| Manual SHA cross-check | INF_D_05 local `79f8b45d3e139459` == s3 `79f8b45d3e139459` MATCH; INF_D_06 local `f1f9eed38339ec95` == s3 `f1f9eed38339ec95` MATCH |

The new ADHC_DSFLOW.005 safe-deploy pre-push hook (DS~B / AE 0.7
ratified earlier today) auto-ran the S3 cp + SHA verify on `git push`.
Manual SHA cross-check captured above for the audit trail.

## Compiler Tools

| Tool | Run | Findings |
|---|---|---|
| `comp-pipescript io INF_D_05` | once | Catalog naming-collision: returns INF_D_05.client_top_holdings.py (group I order 430), not INF_D_05.activity_scan.py (group D). Same for INF_D_06 → client_timeseries. Reads-only manifest insufficient for activity_scan/cash_drag pair; manual source reads sufficed. |
| `comp-pipescript io INF_D_06` | once | Same catalog naming-collision (group I order 440). |
| `.tools/ds-commit-gate.sh` | once on 2 files | PASS for both |
| Manual `hashlib.sha256` | 2 cross-checks | Both MATCH |
| Standalone python re-run (boto3 fetch) | 2 (one per script) | TRN 263,812 rows / median 752 / segments balanced; cash $14.5M / 92 above threshold |

Catalog naming-collision is a real surface (two scripts share `INF_D_05.`
prefix because `.activity_scan.py` and `.client_top_holdings.py` both
parse to the same `INF_D_05` identifier in `comp-pipescript`'s INF tooling).
Out-of-scope for TO-8 but worth surfacing as a follow-up for the
`INF_COMP_PIPESCRIPT_DEPLOYED_COVERAGE` queued sibling.

## Upstream finding (NOT my scope — surfacing to COO)

INF_B_01 has a regression spanning **three consecutive days** (2026-05-06,
2026-05-07, 2026-05-08). All `gold/holdings/{date}.parquet` rows for those
dates have `price = 0` (units populated). Downstream impact (already observed):

- `gold/holdings/2026-05-08.parquet`: 9,348 rows / $0 firm MV
- `gold/timeseries/client_performance.parquet` 2026-05-08 row: 292 HHs / $0 AUA
- `platinum/firm/activity_scan.json` 2026-05-08 emit: 305 rows / all aua=0
- `platinum/firm/cash_drag.json` 2026-05-08 emit: 292 rows / all aua=0

Pre-2026-05-06 is healthy ($188–190M firm AUA). My defensive walk-back in
both fixed scripts makes them tolerate this regression gracefully (next
authorized cascade rerun will produce meaningful artifacts even if INF_B_01
still emits zero-MV). But the regression itself needs to be addressed
separately — this is a partner-facing AUA on every downstream consumer that
takes `keys[-1]` from `gold/holdings/`.

Flagged to COO in RAVC4 message for routing.

## Andrew's chain-rerun-HOLD

Chain rerun is on HOLD per Andrew. My local standalone runs are the
correctness gate (per COO message). Artifacts on S3 (`platinum/firm/
activity_scan.json` + `cash_drag.json`) remain the pre-fix all-zero versions
— next authorized cascade rerun will produce the corrected artifacts via
the deployed code.

## RAVC

- RAVC2 ACK: sent 20:45Z
- COO add at 20:50Z (architectural-parity directive: align with canonical
  AUA source — applied via cp switch)
- RAVC4 close: sent on session-log commit (this commit + commit `147b85326`)

## MCP / inbox

- Registered at session start 20:43Z
- Watcher launched + relaunched once on delivery
- All COO messages acted on within 1 turn (RAVC discipline held)

## Next session pickup

Per COO message: "Standdown after RAVC4 close authorized."
- INF_B_01 zero-MV regression: surfaced to COO for routing (not DS~C's lane)
- `INF_D_05` catalog-collision in `comp-pipescript io`: surfaced separately
- DS~C IDLE pending further routing

No active blockers.
