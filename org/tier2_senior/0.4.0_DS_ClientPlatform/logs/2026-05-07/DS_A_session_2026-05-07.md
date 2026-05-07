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

## Next Steps (Session 1 — SL-P1c / INFNNA.001)

1. **SL-P1c Night 1/3**: Check S3 ~06:00 UTC 2026-05-08. Confirm `2026-05-07.parquet` present, size > 50KB. Send RAVC4.
2. **INFNNA.001**: Await Andrew GO via COO. On GO: Phase 1 edit + commit + S3 upload immediately.
3. **INFETL TO-2**: COO may route sentinel-write TO for `orion-gold-dispatch.sh` EventBridge gap — hold until issued.

---

# Session Log — DS~A 2026-05-07 (Session 2 — ADVI_INFETL.MDR)

**Session type:** Single TO — ADVI_INFETL.MDR (Andrew-direct HIGH priority, master data registry)
**Status:** COMPLETE — all 6 ACs green; COO RAVC1 ACK received

---

## Summary

Post-compaction session continuation. COO had dispatched ADVI_INFETL.MDR with Andrew-direct priority ("we need master data registry very badly"). Completed in ~30 min per COO RAVC1 ACK. Two canonical output files landed plus comp-tools.yaml update.

Bronze historical backfill streams remain in progress (monitoring). INFNNA.SILVER and INFNNA.GOLD remain queued pending stream completion.

---

## ADVI_INFETL.MDR Work

| Step | Description | Result |
|------|-------------|--------|
| Compiler enumeration | `comp-pipescript io INF_*` + grep-based I/O harvest for inline S3 constants | INF gold scripts use inline constants (no shared layout module); compiler returned "no S3 paths"; switched to `grep -h "PREFIX\|KEY = '"` for bronze/silver scripts |
| Bronze tier | Enumerated all bronze prefixes: `orion-api/`, `orion-api-v2/`, `performance/`, `assets/`, `positions/`, `billing/`, `tax/` | 13 bronze artifacts documented |
| Silver tier | Enumerated `silver/api_dims/`, `silver/transactions/`, `silver/accounts_dim/`, `silver/aum_snapshot/`, `silver/performance/`, `silver/prices/` | 17 silver artifacts documented |
| Gold tier | Enumerated all 40 CHAIN_FULL steps (INF_A/B/C/D series) + off-chain scripts | ~20 gold artifact entries |
| Platinum tier | Enumerated `platinum/firm/`, `platinum/advisors/`, `platinum/clients/` + 7 STUBs identified | ~25 platinum entries |
| data_semantic_class | Applied taxonomy to every artifact: SINGLE_SHOT (25) / SNAPSHOT_PER_DATE (20) / LOOKBACK_WINDOW (3) / EVENT_LOG (2) | First-class field on all 75 entries |
| Gold violation cross-ref | Cross-referenced INFETL.007 portal-route audit (16 gold reads); G1-G16 all mapped to platinum targets or STUBs | Section 7 in MDR |
| 7 gaps surfaced | GAP-1 (activity_silver unpopulated), GAP-2 (entities/ BD-era remnants), GAP-3 (7 platinum STUBs), GAP-4 (INF_D_00d state bug → DS~D), GAP-5 (bronze/performance 1 file only), GAP-6 (sentinel write → AE 0.7), GAP-7 (billing/tax OFF_CHAIN) | 5 new findings surfaced to COO for Andrew prioritization |
| RAVC1 to COO | Report: 75 artifacts, all ACs green, 7 gaps, performance path correction canonical | 20260507T~19:00Z |
| COO RAVC1 ACK | All 6 ACs confirmed green. GAP-4 routed DS~D (confirmed). GAP-6 routed AE 0.7. 5 new gaps escalating to Andrew. "Excellent pace." | Received + marked read |

---

## Outputs

| File | Description | Commits |
|------|-------------|---------|
| `docs/architecture/INFETL_MASTER_DATA_REGISTRY.md` | Human-readable MDR: 10 sections, per-tier inventory tables, narrative, portal violation cross-ref | `85977d68a` (GIT_COMMIT_AUTHOR_OVERRIDE=ANY_CTO) |
| `docs/architecture/inf_data_graph.yaml` | Machine-readable canonical graph: 75 artifact entries, all fields | `85977d68a` |
| `org/modules/graph/comp-tools.yaml` | Added `inf_pipeline:` block: registry pointers, path corrections, violation counts, guard_b bounds | `31bf7e99a` (GIT_COMMIT_AUTHOR_OVERRIDE=ANY_EXEC) |

---

## Critical Path Corrections (canonical in registry)

| Artifact | Incorrect Assumption | Canonical Path |
|----------|---------------------|----------------|
| performance_dim | `bronze/orion-api/{date}/performance_dim.csv` | `bronze/performance/{date}.parquet` |
| representatives | `bronze/orion-api/{date}/representatives.json` | `bronze/orion-api-v2/{date}/representatives.json` |
| billing | In CHAIN_FULL | OFF_CHAIN — manual EC2 bronze runner |
| tax_unrealized / tax_realized | In CHAIN_FULL | OFF_CHAIN — manual EC2 bronze runner |

---

## Bronze Backfill Monitor (INFNNA.SILVER prerequisite)

| Stream | Progress | ETA | Silver gate |
|--------|---------|------|-------------|
| billing | [800/2241] at 2022-05 | ~2.5h | `build_billing_dim.py --all-dates` |
| tax_perf | [672/2247] at 2022-01 | ~3.3h | `build_tax_dim.py` + `convert_performance_to_silver.py` |
| assets_v2 | date 2178/2247, iso=2020-05-20 | ~8.6h | `run_silver_backfill_parallel.py --dims assets_v2` |
| positions | date 2182/2247, iso=2020-05-15 | ~8.1h | silver positions builder |

Silver builds launch per-stream as each completes (billing first). Monitor via `/loop` at 270s cadence.

---

## Pending (Gated on Bronze)

1. **INFNNA.SILVER** — Historical silver builds across billing, tax/perf, assets_v2, positions_daily (2020-03-11 → 2026-05-05). Launch per-stream on completion.
2. **INFNNA.GOLD** — INF_C_01 canonical_nna rebuild + INF_D_08 + INF_D_00c. Gate: INFNNA.SILVER complete + DS~D INF_D_00d fix ETag landed.
3. **ADVI_INFETL.002 RAVC2** — Confirm tonight's natural chain run writes `gold/meta/pipeline-complete.json` sentinel. S3 head-object check post-run.
4. **Session commit** — Commit this session log under 0.4.0_DS_ClientPlatform~A author.
