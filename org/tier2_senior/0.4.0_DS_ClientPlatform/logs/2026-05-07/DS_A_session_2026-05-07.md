# Session Log — DS~A 2026-05-07

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-07
**Session type:** Multi-TO — INFNNA.001 investigation continuation + ADVI_ROLLUP.SL-P1c shadow gap root cause + fix
**Status:** IN PROGRESS — SL-P1c fix deployed, INFNNA.001 holding COO/Andrew GO

---

## Summary

Session continued post-compaction. Two active workstreams:

1. **INFNNA.001** (Inflection NNA attribution investigation): Root cause previously identified (retroactive Orion rep_id attribution change + rolling 7-day transactions window). DS~A had sent RAVC1 and RAVC2 to COO in prior session. COO ACK received at session start with 6-phase remediation plan; all phases HELD pending Andrew's backfill scope decision (YTD 2025-01-01 vs 1y vs full). No further action taken this session.

2. **ADVI_ROLLUP.SL-P1c** (sleeve shadow gap): Investigated why `holdings_lots_shadow` partitions for 2026-05-04 and 2026-05-05 were absent from S3 despite B_01 running nightly with denominator fix deployed. Found root cause in `pd.concat` attrs-wipe, fixed, deployed, RAVC3 sent, COO ACK received.

Also completed a 49F vs Inflection ETL gap analysis for CTO (Andrew direct request, delivered to CTO inbox pre-compaction).

---

## Session Work

| Step | Description | Result |
|------|-------------|--------|
| Startup | Post-compaction re-registration on MCP, inbox-watch relaunch, inbox sweep | Registered; RAVC2 ACK + INFNNA.001 TO + prior RAVC ACKs recovered from system-reminder |
| INFNNA.001 hold | COO ACK confirmed: 6-phase plan approved, all phases holding for Andrew GO | Standing by |
| 49F ETL gap analysis | Andrew direct request: analyze BD pipeline daily ETL vs Inflection gaps | Delivered to CTO inbox 20260507T155628Z (5 gaps identified) |
| SL-P1c shadow investigation | Check S3 shadow partitions: confirmed 2026-05-04 + 2026-05-05 missing | S3 ls: last partition 2026-05-01 (created 2026-05-05 00:27) |
| Log forensics | Pulled gold log (`gold_incremental_2026-05-07_20260507_051559.log`, 87MB) — searched for shadow save lines | Found: shadow BUILT for 2026-05-04 (1,218 lots/$48M) + 2026-05-05 (1,210 lots/$48M) but NO "OK (sleeve shadow):" upload line |
| Root cause identified | HLOT2 reopen pass (B_01:2900) calls `pd.concat([df, _reopen_df], ignore_index=True)` → pandas does NOT propagate `.attrs` → `df.attrs['holdings_lots_shadow']` wiped before `save_lots()` reads it | Confirmed: 2026-05-01 HLOT2 got NoSuchKey (skipped) → attrs survived → shadow saved. 2026-05-04 HLOT2 produced 21,365 lots → concat fired → attrs wiped → shadow lost |
| Fix implemented | 2-line patch at B_01:2900: save `dict(df.attrs)` before concat, `df.attrs.update(saved)` after sort/reset_index | Edit clean, ds-commit-gate passed |
| Commit + deploy | `6424b29ab` pushed to CLOUD; S3 upload to `s3://opal-data-bd/code/gold/B_01.holdings_lots.py` | `comp-pipescript deployed B_01` → MATCH |
| RAVC3 | Sent to COO with full root cause, fix details, backfill decision request | 20260507T161102Z |
| COO ACK (RAVC3) | Decision: FORWARD-ONLY (skip 2026-05-04/05 backfill); Night 1/3 clock starts tonight ~04:00 UTC 2026-05-08 | ACK sent back 20260507T161621Z |
| Monitoring loop | CronCreate `*/5 * * * *` job `a6cc7319` maintaining liveness; inbox-watch pid 81259 | Running |

---

## Compiler Tools

| Tool | Target | Result | Notes |
|------|--------|--------|-------|
| `ds-commit-gate.sh` | `B_01.holdings_lots.py` | PASS | py_compile + AST + ruff all clean |
| `comp-pipescript deployed B_01` | B_01.holdings_lots.py | MATCH | Verified post-S3-upload |

---

## Root Cause Detail — SL-P1c Shadow Gap

**Bug class:** pandas `.attrs` not propagated by `pd.concat` (known pandas behavior).

**Sequence:**
1. B_01 `compute_lots()` line 2846: `df.attrs['holdings_lots_shadow'] = shadow_df` — stashed after ULN sleeve shadow build
2. B_01 line 2900: `df = pd.concat([df, _reopen_df], ignore_index=True)` — HLOT2 reopen pass creates new DataFrame; `.attrs = {}`
3. B_01 line 2901: `df = df.sort_values(...).reset_index(drop=True)` — two more new DataFrames; attrs still {}
4. `save_lots()` line 3015: `df_sl = df.attrs.get('holdings_lots_shadow')` → `None` → shadow save skipped silently

**Why 2026-05-01 was unaffected:** HLOT2 attempted `canonical/holdings` load but got `NoSuchKey` exception → caught → reopen skipped → `df` object unchanged → attrs intact → shadow saved.

**Why 2026-05-04+ broke:** HLOT2 found the `canonical/holdings` key and produced 21,365 lots every night → concat path hit → attrs wiped.

**Fix:**
```python
_hlot2_saved_attrs = dict(df.attrs)  # pd.concat does not propagate .attrs
df = pd.concat([df, _reopen_df], ignore_index=True)
df = df.sort_values(['account_id', 'asset_name', 'lot_index']).reset_index(drop=True)
df.attrs.update(_hlot2_saved_attrs)
```

Same attrs-wipe also suppressed `holdings_lots_v2_dryrun` saves for the same dates (confirmed in log: both V2_DRYRUN and SLEEVE_SHADOW absent from 2026-05-04 save section; both present for 2026-05-01).

---

## 49F vs Inflection ETL Gap Analysis (CTO delivery)

Five gaps identified between BD fully-automated pipeline and Inflection:

| Gap | Severity | Detail |
|-----|----------|--------|
| No `inf-gold-trigger` EventBridge rule | CRITICAL | Gold chain never auto-fires; manual SSM dispatch only |
| No portal publisher S3 trigger from gold | HIGH | Gold completion doesn't auto-push platinum |
| Transactions rolling 7d window vs BD cumulative | HIGH | INF_D_08 "YTD NNA" is a 7-day cash flow sum |
| No independent daily price refresh | HIGH | BD has 14:00 UTC EventBridge for historical prices; Inflection has none |
| No Time Machine / version capture | MEDIUM | BD gold dispatch captures per-run snapshots; Inflection has none |

---

## Commits

| Hash | Author | Subject |
|------|--------|---------|
| `6424b29ab` | 0.4.0_DS_ClientPlatform~A | fix(ADVI_ROLLUP.SL-P1c): preserve df.attrs across HLOT2 pd.concat so shadow writes on nights HLOT2 fires |

**Push:** `6ec0655b0..6424b29ab CLOUD -> CLOUD`

---

## INFNNA.001 Status (holding)

Root cause (from prior session, RAVC1+RAVC2 accepted by COO):
- `pull_inflection_transactions_v2.py:71` `INFLECTION_REP_IDS = "3,11,12"` — rep_id=6 (Joe Brandenburg) excluded from bronze pull
- Retroactive Orion attribution change: `accounts_v2` reflects new attribution, `canonical_nna` reflects old → NMNC/NNA era mismatch
- Bronze transactions `DEFAULT_INCREMENTAL_DAYS = 7` — INF_D_08 "YTD NNA" is a rolling 7-day sum

6-phase remediation plan (all phases HELD for Andrew backfill scope GO):
1. Edit `pull_inflection_transactions_v2.py:71`: `"3,11,12"` → `"3,6,11,12"` + commit + S3
2. Bronze backfill all 4 rep_ids from Andrew's chosen horizon (2025-01-01 / 2024-01-01 / 2020-01-01)
3. Rebuild `silver/transactions`
4. Rebuild `canonical_nna` (INF_C_01)
5. Re-run `INF_D_08`, `INF_D_00c`, `INF_D_04`
6. Validate portal NNA + leaderboard

---

## Current State

| Item | State |
|------|-------|
| ADVI_ROLLUP.SL-P1c | Fix deployed (`6424b29ab`), MATCH. Night 1/3 pending (~04:00 UTC 2026-05-08). S3 check ~06:00 UTC, RAVC4 to follow. |
| INFNNA.001 | Root cause confirmed. 6-phase plan ACK'd by COO. All phases HOLD — awaiting Andrew backfill scope GO. |
| 49F ETL gap analysis | Delivered to CTO inbox 20260507T155628Z. |
| Inbox | Clean |
| inbox-watch | Running pid 81259 |
| CronCreate loop | Job `a6cc7319`, `*/5 * * * *` |

## Next Steps

1. **SL-P1c Night 1/3**: Check S3 ~06:00 UTC 2026-05-08. Confirm `2026-05-07.parquet` present, size > 50KB. Send RAVC4.
2. **INFNNA.001**: Await Andrew GO via COO. On GO: Phase 1 edit + commit + S3 upload immediately.
3. **INFETL TO-2**: COO may route sentinel-write TO for `orion-gold-dispatch.sh` EventBridge gap — hold until issued.
