# INF Pipeline — Incremental Architecture Design Brief

**Author:** 0.6.1_AE_PartnerETL (AWS Engineer, Inflection)
**Date:** 2026-05-14
**Audience:** 2.0.0_SA_COO (for distribution to 0.4.0_DS_ClientPlatform~A, ~B)
**Status:** Design proposal — DS implementation required
**Trigger:** Andrew directive 2026-05-14: "make a truly incremental version of this flow rather than having to rebuild 7 years of history every single day"

---

## TL;DR

The INF gold chain rewrites every historical date partition on every run (~7 years × ~250 trading days ≈ 1,750 partitions for B_00 alone). Per the live `chain_full_20260514_131842` baseline below, the heavy historical-rewrite stages (B_00, B_01, B_02, B_03, C_00, C_01, C_02, C_03) consume **~35–40 min** of the total ~70 min chain. None of that recomputation is needed for past dates — silver partitions for 2024-07-20 do not change between today and tomorrow, so `holdings_2024-07-20.parquet` is deterministic and rewriting it daily is pure waste.

The proposal: introduce a **per-partition idempotence gate** at every date-partitioned gold script and a **append-only cumulative-state pattern** for the timeseries-blob scripts. Expected steady-state daily chain cost: **~8–12 min** (silver + new-date gold + platinum rebuilds), down from ~70 min. Full-rebuild remains available behind an explicit `--rebuild` flag for backfills and schema migrations.

---

## 1. Current-state baseline

### 1.1 Live chain `chain_full_20260514_131842` — empirical step durations

Captured from `s3://opal-data-inf/telemetry/inf-gold-layer-runner/history/`. Started 13:18:42Z 2026-05-14.

| Stage | Script | Duration | Pattern |
|---|---|---|---|
| API pull | INF_API_PULL_REPS | ~5 s | Today only (small) |
| API pull | INF_API_SILVER_REPS/HHREP | 1 s each | Single-date silver convert |
| API pull | INF_API_PULL_ASSETS_V2 | 1 s | **Skipped** — today's bronze exists |
| API pull | INF_API_PULL_NEW_PORTFOLIO | 2 s | Same |
| API pull | INF_API_SILVER_ACCOUNTS_V2 | 1 s | Single-date |
| API pull | **INF_API_PULL_TXN** | ~7 min | **Unconditional re-pull** — full snapshot |
| API pull | INF_API_SILVER_TXN | 5 s | Single-date |
| API pull | **INF_API_PULL_PERF** | ~9 min | **Unconditional re-pull** |
| API pull | INF_API_SILVER_PERF | 1 s | Single-date |
| A-stage | INF_A_-1 + A_00..A_04 | ~1 min total | Latest-state dims |
| API pull | INF_API_PULL_POSITIONS_DAILY | ~3 min | Snapshot pull |
| API pull | INF_API_SILVER_POSITIONS_MV | 1 s | Single-date |
| B-stage | **INF_B_00 canonical_holdings** | **~10.6 min** | **Walks ALL positions_mv dates, rewrites every `holdings_{date}.parquet`** |
| B-stage | INF_B_01 holdings_lots | ~1 min | Lots reconstruction from full transactions |
| B-stage | INF_B_01b classify_new_securities | ~12 s | Latest-only |
| B-stage | INF_B_02 canonical_lots | ~1.5 min | Lots latest snapshot |
| B-stage | INF_B_03 account_gains | ~5 min | Walks ALL holdings dates, rewrites every gains partition |
| C-stage | **INF_C_00 canonical_performance** | **~6.5 min** | **Walks ALL holdings dates** |
| C-stage | **INF_C_01 canonical_nna** | ~50 s | **Walks ALL transaction dates** |
| C-stage | INF_C_01b role_aua_backfill | ~3 min | Backfill scan |
| C-stage | INF_C_02 client_performance | ~20 s | Assembles full timeseries blob from all perf partitions |
| C-stage | INF_C_03 account_performance | ~30 s | Same |
| C-stage | INF_C_05..C_09 | ~3 min total | Mix of latest + timeseries assembly |
| D-stage | INF_D_00..D_06a + D_09 + INF_09 | ~7 min total | Mix of latest snapshot + per-HH historical |

**Total wall:** ~70 min daily, even when only one new trading day's worth of data has changed.

### 1.2 Cost distribution

| Cost class | Scripts | Daily wall |
|---|---|---|
| **Wasteful historical rewrites** (would be no-op for past dates) | B_00, B_03, C_00, C_01 partition writes; C_06/D_00b/D_00d/D_06/D_09 historical replays | **~35–40 min** |
| **Necessary API pulls** (cannot avoid — live data) | PULL_TXN, PULL_PERF, PULL_POSITIONS | ~19 min |
| **Necessary dim + latest-state recompute** | A-stage, B_01/B_02, C_02 assembly, latest-only D-stage | ~12 min |
| **Already-incremental** (latest snapshot only) | D_07, D_07a, D_00, D_00c, D_05 | ~3 min |

The 35–40 min of "wasteful historical rewrites" is the recoverable budget.

### 1.3 Why this matters beyond wall time

- **S3 PUT cost**: ~2,000 partition writes/day × 365 = 730k PUTs/year that produce identical content
- **EC2 cost**: 70 min/day vs ~10 min/day means ~7× compute waste at a fixed instance type
- **Operational fragility**: longer chain → wider failure surface (INF_D_00c failure today after 1+ hour wasted re-rebuilding 2020-2024 data that hadn't changed). Faster chain → tighter feedback loop, faster RAVC2.
- **Backfill blast radius**: with the current pattern, an upstream silver fix forces a full ~70min chain. With deterministic per-partition gates, we can rerun only the affected date range.

---

## 2. Architectural patterns

Five distinct patterns cover the entire chain. Each script maps to exactly one.

### 2.1 Pattern A — Date-partitioned canonical (`gold/canonical/{name}_{date}.parquet`)

**Current behavior:** script lists all available silver partitions, iterates every date, writes every output partition.

**Target behavior:** for each candidate date, `head_object` the expected output key. If exists AND upstream silver mtime ≤ output mtime, **skip**. Otherwise compute and write.

**Key invariant:** the output for a past date is a deterministic function of silver inputs for that date plus the latest `accounts_dimension_latest.parquet` (advisor attribution dim). When silver for a past date changes (corrections, dim refresh), invalidate via `--rebuild --start-date X` or by deleting the output key.

**Scripts in this pattern:**

| Script | Output partition pattern |
|---|---|
| INF_B_00 | `gold/canonical/holdings_{date}.parquet` |
| INF_B_03 | `gold/account_gains/{date}.parquet` |
| INF_A_03 | `gold/positions_cube/{date}.parquet` |
| INF_C_00 | `gold/canonical/canonical_performance_{date}.parquet` |
| INF_C_01 | `gold/canonical/canonical_nna_{date}.parquet` |

**Edge case — advisor reassignment.** When a rep changes for an account, `accounts_v2` snapshot updates, then `accounts_dimension_latest` flips, then **past holdings partitions retain the OLD advisor_key in their files**. Today this is masked because B_00 re-writes everything daily with the latest dim. Under the incremental pattern, past partitions become "stuck" at the dim-at-time-of-write. Two options:
1. **Accept and document**: holdings partitions reflect historical advisor attribution at the time the data was first ingested (point-in-time correct).
2. **Bifurcate**: keep `gold/canonical/holdings_{date}.parquet` as the raw position layer (no advisor key), do the advisor join downstream at query time. Cleaner separation but requires consumer updates.

Recommend (1) for v1 — current behavior already "freezes" advisor attribution at first-write moment; switching to skip-if-exists makes that frozen state per-date instead of per-chain. Add a `--rebuild-advisor-attribution-only` flag that re-writes partitions with just the advisor_key column updated, when needed (rare).

### 2.2 Pattern B — Cumulative timeseries blob (`gold/timeseries/{name}.parquet`)

**Current behavior:** script lists all canonical date partitions, reads each, concatenates, writes single blob to `gold/timeseries/...parquet`.

**Target behavior:** read the existing blob, identify max date present (`existing_max_date`), compute new rows for dates > `existing_max_date` from new canonical partitions, append + dedupe + write back.

**Idempotence:** must dedupe by primary key (e.g., `(date, household_id)`) on write to handle reruns.

**Scripts in this pattern:**

| Script | Output |
|---|---|
| INF_C_02 | `gold/timeseries/client_performance.parquet` |
| INF_C_03 | `gold/timeseries/account_performance.parquet` |

**Why this matters:** `client_performance.parquet` is the central upstream for the entire D-stage. Today C_02 lists ~1,750 canonical_performance partitions, reads each, concats. With append-only it reads existing blob + only new partitions. Same for C_03.

### 2.3 Pattern C — Per-HH historical-replay artifacts (`platinum/clients/{hh}/timeseries.json` etc.)

**Current behavior:** for each HH, replay full historical holdings to derive quarterly mix periods or top-holdings; rewrite every HH artifact on every chain.

**Target behavior:** maintain a manifest of "last-written-quarter per HH". On each run:
- Identify the current quarter end (e.g., 2026-Q2).
- If the current quarter is already up-to-date in all HH artifacts (compare `data_as_of` field) AND no historical correction was applied (silver partitions for past quarter-ends unchanged), **skip the HH entirely**.
- Otherwise compute and write.

**Scripts in this pattern:**

| Script | Output |
|---|---|
| INF_D_06 client_timeseries | `platinum/clients/{hh}/timeseries.json` |
| INF_D_05 client_top_holdings | `platinum/clients/{hh}/top_holdings.json` |
| INF_D_09 account_timeseries | `platinum/clients/{hh}/accounts/{acct}/timeseries.json` |

**Subtlety:** these scripts already use the latest holdings snapshot as the floor; the "history" they walk is finding the nearest holdings date per past quarter end. Once a past quarter's "anchor" holdings_{date}.parquet exists and hasn't changed, the historical periods for that HH artifact are stable. Only the CURRENT (in-progress) quarter needs daily recomputation, plus any HH whose composition shifted.

**v1 optimization (cheap):** keep current "rebuild all HHs" but skip the per-quarter historical anchor reads if a cached `gold/cache/hh_timeseries_anchors.parquet` exists (one cache parquet keyed by HH × period). Big win because the loop today does ~25 quarters × 300 HHs = 7,500 historical anchor lookups per script.

### 2.4 Pattern D — Latest-state firm-level artifacts (`platinum/firm/*.json`, `gold/artifacts/*.json`)

**Current behavior:** read latest snapshot inputs, write a single artifact. No historical walk.

**Target behavior:** already incremental in the structural sense. Only optimization is **dependency-skip**: if no upstream timeseries blob mtime changed since last successful write, skip.

**Scripts in this pattern:**

| Script | Output |
|---|---|
| INF_D_00 | `platinum/firm/leaderboard.json`, `gold/artifacts/header_metrics.json` |
| INF_D_00b | `platinum/firm/timeseries_chart.json` |
| INF_D_00c | `platinum/firm/employee_leaderboard.json` |
| INF_D_00d | `platinum/firm/cumulative_chart.json` |
| INF_D_07/D_07a | `platinum/firm/concentration_risk.json`, `firm_concentrations.json` |
| INF_D_05a (activity_scan) | `platinum/firm/activity_scan_{window}.json` |
| INF_D_06a (cash_drag) | `platinum/firm/cash_drag_{window}.json` |
| INF_D_08 | NMEC/NMNC artifacts |
| INF_09 | partner_analytics.json |

These run in <30s each today. No big win available beyond dependency-skip. Leave as-is in v1.

### 2.5 Pattern E — API pulls (`bronze/{source}/{date}.parquet`)

**Current behavior:**
- PULL_REPS / PULL_ASSETS_V2 / PULL_NEW_PORTFOLIO / PULL_POSITIONS: write today's snapshot, no de-dup. ASSETS_V2 has internal "skip if today's bronze exists" (~1s on this chain).
- **PULL_TXN / PULL_PERF: unconditional full re-pull of the entire transaction/performance history each run** — ~7 min and ~9 min respectively.

**Target behavior for PULL_TXN / PULL_PERF:** Orion REST supports date-windowed queries. Read max(`transDate`) from existing `bronze/transactions/{latest}.parquet`, pull only `[max_date, today]`, append + dedupe by transaction_id.

**Risk: backdated corrections.** Orion can backdate a correction transaction (e.g., a Sell from 60 days ago booked today). A pure incremental-from-max approach would miss it. Two mitigations:
1. **Trailing window**: always re-pull the last N days (N=90 covers most backdating patterns observed) plus everything since `last_pull_max`. Dedupe by transaction_id.
2. **Periodic full-pull**: incremental Mon–Sat; full-pull Sunday weekly. Catches anything that slipped through the 90-day window.

Recommend both: 90-day trailing window + weekly full-pull. This drops PULL_TXN+PULL_PERF combined from ~16 min daily to ~2 min daily (Mon–Sat) with one ~16 min weekly catch-up.

**Edge case:** the morning cron at 06:00 UTC already wrote today's bronze. If a chain re-fires later in the day (like Andrew's 13:17Z direct fire today), the live behavior should be: re-pull TXN to catch the day's intraday activity. Today this happens accidentally (unconditional re-pull); under the incremental scheme it would be explicit — `--since {last_pull_ts}` rather than `--start-date {today-90d}` if a refresh is wanted intraday.

---

## 3. Per-script migration map

| ID | Script | Pattern | Daily wall now | Daily wall target | Migration effort |
|---|---|---|---|---|---|
| INF_API_PULL_TXN | pull_inflection_transactions_rest.py | E | 7 min | <1 min (Mon-Sat) | M — add date-windowed pull |
| INF_API_PULL_PERF | pull_inflection_performance_rest.py | E | 9 min | <1 min (Mon-Sat) | M |
| INF_API_PULL_POSITIONS_DAILY | pull_inflection_positions_daily.py | E | 3 min | 3 min (unchanged — only pulls today anyway) | none |
| INF_A_-1..A_04 | A-stage | latest-only | 1 min | 1 min | none |
| **INF_B_00** | canonical_holdings | **A** | **10.6 min** | **<1 min** | **L — touch every snapshot loop** |
| INF_B_01 | holdings_lots | A-like (latest lots view) | 1 min | 1 min | S — already latest-focused |
| INF_B_01b | classify_new_securities | latest | 12 s | 12 s | none |
| INF_B_02 | canonical_lots | latest | 1.5 min | 1.5 min | none |
| **INF_B_03** | account_gains | **A** | **5 min** | **<1 min** | **M** |
| **INF_C_00** | canonical_performance | **A** | **6.5 min** | **<1 min** | **M** |
| **INF_C_01** | canonical_nna | **A** | **50 s** | **<10 s** | **M** |
| INF_C_01b | role_aua_backfill | A-like | 3 min | 1 min | M — already a "backfill" but full-scan |
| **INF_C_02** | client_performance | **B** | **20 s** | **5 s** | **M — append-only rebuild** |
| **INF_C_03** | account_performance | **B** | **30 s** | **5 s** | **M** |
| INF_C_04 | validate_aua | gate | <10 s | <10 s | none |
| INF_C_05 | client_tax_liability | latest | 30 s | 30 s | none |
| INF_C_06 | client_mix_timeseries | derived from C_02 | 1 min | 30 s | S — only rebuild if C_02 changed |
| INF_C_07 | advisor_attribution | latest | 30 s | 30 s | none |
| INF_C_08 | advisor_fee_efficiency | latest | 30 s | 30 s | none |
| INF_C_09 | fee_status_audit | latest | 20 s | 20 s | none |
| INF_D_00 | portal_aggregates | D | 30 s | 30 s | none |
| INF_D_00b | portal_timeseries | derived from C_02 | 1 min | 30 s | S |
| INF_D_00c | portal_leaderboard | D | 20 s | 20 s | none |
| INF_D_00d | cumulative_chart | derived from C_02 | 1 min | 30 s | S |
| INF_D_02 | advisor_client_detail | per-HH latest | 1.5 min | 1.5 min | none |
| INF_D_02b/c/d/04/04b | book/detail/directory artifacts | per-HH latest | 1 min total | 1 min | none |
| INF_D_05 | client_top_holdings | C (latest only — no history walk) | 30 s | 30 s | none |
| INF_D_05a (activity_scan) | window aggregates | latest+window | 30 s | 30 s | none |
| **INF_D_06** | client_timeseries (per-HH quarterly mix) | **C** | **2 min** | **<30 s** | **L — anchor cache** |
| INF_D_06a (cash_drag) | window aggregates | latest+window | 30 s | 30 s | none |
| INF_D_07 / D_07a | concentration risk | latest | 30 s | 30 s | none |
| INF_D_08 | nmec_nmnc_nna | latest | 30 s | 30 s | none |
| **INF_D_09** | account_timeseries (per-account quarterly AUA) | **C** | **2 min** | **<30 s** | **L — anchor cache** |
| INF_09 | partner_analytics | aggregator | 1 min | 1 min | none |

**Total target daily wall: ~8–12 min** (down from ~70 min). Steady-state Mon–Sat. Weekly full-pull Sunday: ~30–40 min.

---

## 4. Risks + mitigations

### 4.1 Backfill correctness

**Risk:** a silver-side correction lands for a past date (e.g., 2024-07-20 transactions re-pulled from Orion after a vendor fix), but downstream gold partition `holdings_2024-07-20.parquet` already exists, so the head-object skip-gate keeps the stale gold output.

**Mitigation:**
- All skip-gates compare silver mtime against gold mtime — if silver is newer, recompute.
- Provide `--rebuild --start-date X --end-date Y` flag that forces overwrite within a window.
- Provide `gold/meta/partition_provenance.json` per partition recording silver input mtimes — auditable.
- Andrew/DS escalation: any backfill operation must run with explicit `--rebuild` and log the reason.

### 4.2 Signal-bounded emit (ADHC_DSFLOW pattern)

**Risk:** several scripts emit only on dates where signal exists (e.g., canonical_nna only on dates with non-zero transactions). The incremental version must preserve this. A naive head-object check on `canonical_nna_2024-07-20.parquet` returning 404 could be interpreted as "needs rebuild" — but actually that's the correct empty-signal state and should stay empty.

**Mitigation:**
- Emit a "ran-and-empty" sentinel: `gold/meta/empty/{script_id}/{date}.empty` when computation runs but yields no rows.
- Skip-gate checks: output exists OR empty-sentinel exists.
- Empty-sentinel invalidation via `--rebuild` same as data partitions.

Reference: `memory/feedback_signal_bounded_vs_time_bounded_emit.md` (DS~D 2026-05-13).

### 4.3 Advisor attribution lag

**Risk (Pattern A subtlety):** as detailed in §2.1, past partitions encode advisor_key at write-time. Under incremental, if a rep changes for an account today, past partitions retain the OLD advisor.

**CTO Q1 ruling (2026-05-14):** **(a) point-in-time-correct freezing is the v1 default + `--rebuild-advisor-attribution-only` is the explicit escape hatch.** Bifurcation (raw position layer + advisor join at query time) is the v2 path, deferred until a business surface needs query-time advisor flexibility.

**Mitigation:**

Past partitions encode advisor attribution at write-time. This matches today's accidental behavior in spirit — the current chain rewrites with the latest dim, but the "latest dim" of last week's run was different from this week's run, so historical partitions are NOT consistent across chains anyway. Switching to skip-if-exists makes the frozen state per-date instead of per-chain, which is cleaner.

**`--rebuild-advisor-attribution-only` flag scope:**
- Forces re-write of partitions affected by Pattern A scripts (B_00, B_03, A_03, C_00, C_01)
- Re-applies the LATEST `accounts_dimension_latest.parquet` advisor_key to each affected partition
- Skips silver-input re-computation (positions_mv, transactions, etc) — only the advisor_join step is re-run
- Env var: `INFINC_REBUILD_ADVISOR_ATTRIBUTION_ONLY=1` (already in DS~D Phase 1 lib contract — `d88b7a7a4`)

**Operational runbook — rep change mid-day:**
1. **Detection signal:** `silver/api_dims/accounts_v2/snapshot_date={today}/data.parquet` rep_id or representative_name changes for one or more accounts (compared to yesterday's snapshot).
2. **Standard daily chain handles forward:** today's chain writes today's partition with the new rep. No special action.
3. **Past-partition correction:** if business surfaces (advisor leaderboard YTD, advisor book.json roll-up) need to retroactively re-attribute past partitions to the new rep:
   ```bash
   bash orion-gold-dispatch.sh --chain gold-cd \
       --rebuild-advisor-attribution-only \
       --rebuild-start-date YYYY-MM-DD \
       --rebuild-end-date YYYY-MM-DD
   ```
4. **Audit log:** every `--rebuild-advisor-attribution-only` run writes a row to `org/inf-rebuild-attribution-audit.log` with reason, date range, account_ids affected. AE 0.6.1 owns the audit log; reason must be non-empty per `safe-deploy.sh` discipline pattern.

**v2 bifurcation path (deferred):**
- Future business need: "show all accounts under Joe's book as of today, across historical partitions where his book has churned" — point-in-time freeze breaks this.
- Mitigation: separate `gold/canonical/holdings_{date}.parquet` from advisor attribution. Move the advisor_join to a downstream view (`gold/views/holdings_advisor_resolved/{date}.parquet`) that re-joins against latest `accounts_dimension_latest.parquet` at view-build time.
- Cost: ~2 new scripts (latest-state advisor-resolution view + INF_A_00 schema-change to expose a stable historical advisor map). Estimated 1-week DS effort.
- Decision criterion: when an RD-side product PRD explicitly requires "as-of-today advisor across historical holdings" — file v2 then. Not before.

### 4.4 Schema migration

**Risk:** if a script adds a column (e.g., `INF_D_02c` adding `tax_structure_reason`), past partitions don't have it. Cumulative-blob assemblers (Pattern B) reading the existing blob would emit a mixed-schema result.

**Mitigation:**
- Schema version stamp in `gold/meta/schemas/{script_id}.json`. Bump on every column add.
- Skip-gate also compares schema version: output schema version < current → rebuild.
- Pattern B append-and-dedupe must use `pd.concat(..., sort=False)` and tolerate NaN-fill on new columns.

### 4.5 Concurrent chain firing

**Risk:** if two chains run concurrently (one manual, one cron), head-object racing on partition writes could produce torn writes.

**Mitigation:**
- Single-writer guard: `bash /tmp/orion-gold-dispatch.sh --status` checks for in-flight dispatcher PID before allowing a second fire.
- Already addressed structurally: EC2 watchdog-shutdown + Lambda's "EC2 already running" pending-marker path. Tighten: dispatcher writes a lock to `s3://opal-data-inf/gold/meta/dispatcher.lock` and refuses to start if held.

### 4.6 Validation drift

**Risk:** after migration, behavior diverges from the original full-rebuild output by epsilon (FP drift, dedupe order, dim-as-of subtleties).

**CTO Q6 ruling (2026-05-14):** **PK-stable sort on write + byte-equal (md5) validation contract.** For Pattern A, partition-by-partition byte-equality is the gate. For Pattern B, dedupe-then-sort-then-write — same byte-equal contract applies once the dedupe order is locked.

**Mitigation — write-time discipline:**

Every Pattern A and Pattern B writer MUST sort by primary key immediately before `.to_parquet(...)`:
```python
df.sort_values(PK).reset_index(drop=True).to_parquet(buf, index=False, engine='pyarrow', compression='snappy')
```

Where `PK` is the script-specific primary-key tuple (see table below). This is a one-line discipline that makes outputs byte-stable across runs given identical inputs. Without it, pandas groupby internal hashing order can produce row-permutations that change the md5 even when row content is identical — breaking the byte-equal validation gate without a real semantic delta.

**Per-script PK sort-key map:**

| Script | Pattern | Output | PK (sort-keys, in order) |
|---|---|---|---|
| INF_B_00 | A | `gold/canonical/holdings_{date}.parquet` | `(date, account_id, ticker)` |
| INF_B_03 | A | `gold/account_gains/{date}.parquet` | `(date, account_id, ticker)` |
| INF_A_03 | A | `gold/positions_cube/{date}.parquet` | `(date, account_id, ticker)` |
| INF_C_00 | A | `gold/canonical/canonical_performance_{date}.parquet` | `(date, account_id)` |
| INF_C_01 | A | `gold/canonical/canonical_nna_{date}.parquet` | `(date, account_id)` |
| INF_C_02 | B | `gold/timeseries/client_performance.parquet` | `(date, household_id)` |
| INF_C_03 | B | `gold/timeseries/account_performance.parquet` | `(date, account_id)` |

Pattern C/D scripts emit JSON (not parquet); the byte-equal validation applies to the JSON body after `json.dumps(..., sort_keys=True)` discipline (already in place per most platinum publishers — confirm during Phase 4 migration).

**Pattern A validation contract (per partition):**
1. Pre-migration run: capture `md5sum gold/canonical/holdings_{date}.parquet` for every date.
2. Post-migration run with `--rebuild`: re-capture md5sum.
3. Diff: `(date, expected_md5, actual_md5, status)` — every row must show `status=match`. Zero tolerance.
4. ETag check on S3 side: `aws s3api head-object` ETag matches the local md5 (validates upload integrity too).

**Pattern B validation contract (cumulative blob):**

Append-only writes are sensitive to dedupe order — `pd.concat([existing, new]).drop_duplicates(PK)` keeps FIRST-seen by default, but if existing + new have overlapping (date, household_id) keys with different values (which they shouldn't, given input determinism), the result depends on concat order.

Discipline:
1. Read existing blob → `existing_df`
2. Compute today's rows from new canonical partitions → `today_df`
3. `combined = pd.concat([existing_df, today_df], ignore_index=True)`
4. `deduped = combined.drop_duplicates(subset=PK, keep='last')` — `keep='last'` ensures today_df overwrites any overlapping rows (the new computation is authoritative)
5. `sorted_df = deduped.sort_values(PK).reset_index(drop=True)`
6. `sorted_df.to_parquet(...)` with byte-stable engine settings

Byte-equal validation: pre-migration full-rebuild produces `client_performance.parquet` with md5 `X`. Post-migration incremental run on the same inputs (idempotent — no new dates) must also produce md5 `X`. The dedupe-then-sort discipline makes this achievable.

**Cutover gates:**
- **One-shot validation chain**: before flipping the cron, run `--rebuild` once to regenerate everything, then run incremental once, diff every output md5. All deltas must be zero or explicitly accepted (timestamp fields like `generated_at` in JSON artifacts exempt — handle via `--ignore-fields generated_at,data_as_of` flag on the diff tool).
- Maintain a `--validate-against-rebuild` flag that for one chain run produces both outputs side-by-side and emits `gold/meta/validation/{run_id}/diff_report.json` with per-partition status.
- Phase 6 cutover gate: zero non-exempt deltas across all 55 chain outputs. Hard block on any delta — investigate or accept-with-rationale documented in `gold/meta/validation/exemptions.md`.

**Why this matters operationally:** byte-equal validation is also the foundation for **change-detection-driven downstream consumers**. If a Pattern B blob's md5 doesn't change run-over-run, downstream platinum publishers (INF_D_00b, INF_D_00d, INF_C_06) can skip recomputation entirely — extending the incremental savings into Pattern D territory at no design cost. This makes the PK-sort discipline a force multiplier, not just a validation gate.

---

## 5. Implementation sequencing (DS~A + DS~B coordination)

Phased delivery to minimize blast radius. Each phase is independently shippable + reversible (skip-gate logic guards behind a per-script env flag).

### Phase 1 — Skip-existing infrastructure (DS~A, ~3 days)

Foundational. No script behavior changes yet — just adds the gate.

- New shared lib: `data/orion/scripts/gold/lib/skip_gate.py`
  - `should_skip(script_id, partition_date, output_key, silver_input_keys)` returns bool
  - Reads `head_object` on output_key + each silver_input_key, compares mtime + schema version
  - Returns False if output missing, silver newer, schema bump, or `--rebuild` set
- New shared lib: `lib/empty_sentinel.py` for signal-bounded emit
- Schema-version manifest: `gold/meta/schemas/{script_id}.json`
- `--rebuild`, `--rebuild-start-date`, `--rebuild-end-date` flags wired through dispatch.sh

**Deliverable:** PR with the lib + dispatch.sh flag plumbing. No production scripts touched yet.

### Phase 2 — Pattern A migration (DS~B, ~5 days)

Heavy historical-rewrite scripts. Biggest wall-time win.

- INF_B_00 canonical_holdings (highest priority — 10.6 min)
- INF_B_03 account_gains (5 min)
- INF_C_00 canonical_performance (6.5 min)
- INF_C_01 canonical_nna (50s + signal-bounded emit — exercise sentinel pattern)
- INF_A_03 positions_cube (touched on chain)

For each: wrap the inner per-date loop with `should_skip(...)`. Add `--rebuild` honor. Validate with `--validate-against-rebuild` once per script.

**Deliverable:** 5 PRs (one per script), shipped serially. After all 5: full chain target wall ~30 min (cut ~25 min from B/C-stage history rewrite waste).

### Phase 3 — Pattern B migration (DS~B, ~3 days)

Cumulative timeseries blobs.

- INF_C_02 client_performance — append-only rebuild
- INF_C_03 account_performance — same

Pattern: read existing blob → compute new partition rows → concat + dedupe → write back.

**Deliverable:** 2 PRs. Cuts another ~10s + reduces S3 read load on the C-stage by ~95%.

### Phase 4 — Pattern C migration (DS~A, ~4 days)

Per-HH historical-replay artifacts.

- INF_D_06 client_timeseries — anchor cache + quarter-skip
- INF_D_09 account_timeseries — same

Build `gold/cache/hh_timeseries_anchors.parquet` materialized once per quarter. D_06/D_09 read from cache instead of replaying full historical holdings per HH.

**Deliverable:** 2 PRs + new gold materializer script (`INF_X_00.timeseries_anchors.py`). Cuts ~3 min from D-stage.

### Phase 5 — Pattern E migration (DS~B, ~2 days)

API pull windowing.

- pull_inflection_transactions_rest.py — `--since {date}` + 90-day trailing window
- pull_inflection_performance_rest.py — same
- Weekly cron: full-pull Sundays at 06:00 UTC; incremental Mon–Sat

**Deliverable:** 2 PRs + EventBridge cron split. Cuts ~15 min from daily pull.

### Phase 6 — Validation + cutover (AE 0.6.1 + DS~A + DS~B, ~2 days)

- Run `--validate-against-rebuild` on the full chain. Diff every output vs rebuild reference.
- Update `gold_validate_config.yaml` AC thresholds where epsilon drift is expected.
- Flip dispatcher default to incremental mode. Keep `--rebuild` available behind explicit flag.
- Update `org/modules/graph/comp-tools.yaml` + `comp-pipescript` to surface "would skip" vs "would compute" per partition.

**Deliverable:** validation report + cutover PR. After cutover: daily chain ~8–12 min.

### Total: ~3 weeks calendar, ~19 dev-days across DS~A + DS~B.

---

## 6. Open questions for COO routing

These need disposition before DS work begins:

1. **Advisor attribution lag (§2.1, §4.3)** — accept point-in-time-correct freezing, or bifurcate raw position + advisor join? CTO call needed.
2. **PULL_TXN/PERF trailing window size** — 90 days proposed. Empirical Orion backdate distribution should be confirmed by DS~B before lock-in. AE can run a probe.
3. **Schema version stamping** — should this be opt-in per script (DS chooses when to bump) or automatic via diff vs prior write? Recommend opt-in (DS judgment) but documented in commit messages.
4. **`gold/meta/partition_provenance.json` storage** — one file per partition (cleanest) or one rolling manifest (cheaper)? Recommend per-partition for forensic clarity; estimate ~1,750 small JSON × ~200 bytes = 350KB total, negligible.
5. **DIAGFIX path during migration** — current DIAGFIX TOs assume full-rebuild. During the migration window, any DIAGFIX must use `--rebuild --start-date X` explicitly. Worth a banner in DIAGFIX TO template.
6. **Validation epsilon budget** — for a Pattern A migration, post-vs-pre numeric diff per partition must be zero (it's the same computation on the same inputs). For Pattern B blob assembly, append-vs-rebuild may produce row-order differences that affect downstream hashing — accept or sort?

---

## 7. Concrete next steps

**This brief → COO:** route Phase 1 (skip-gate infrastructure) to DS~A as a TO. DS~A authors the lib + flag plumbing. AE 0.6.1 reviews the lib design + handles dispatch.sh integration.

**Then sequentially:** Phase 2 → 3 → 4 → 5 → 6, each phase a small set of TOs to DS~A or DS~B as mapped above.

**Tracking project code:** propose `ADVI_INFINC` (Inflection Incremental) for the multi-phase initiative. Standard project JSON + REGISTRY row + PRD link to this brief.

**Validation gate:** after every phase, `comp-validate` on every affected script + diff against pre-migration last-good chain artifacts. No phase merges until validation passes.

**AE 0.6.1 responsibilities throughout:**
- dispatch.sh flag plumbing (Phase 1)
- EventBridge cron split for incremental vs weekly full-pull (Phase 5)
- Telemetry instrumentation for "skipped" vs "computed" partition counts (visibility into how much each chain actually does)
- Cutover orchestration + rollback plan (Phase 6)

---

## Appendix A — Live chain reference data

Empirical baseline pulled from `s3://opal-data-inf/telemetry/inf-gold-layer-runner/history/chain_full_20260514_060154.json` (today's failed cron — failed at INF_D_00c step 39 due to DS~A's now-fixed dtype bug `fd11a33c2`; all upstream step durations are valid baseline data).

Pull this brief's "Daily wall now" column directly from those step durations. Live chain `chain_full_20260514_131842` (Andrew-direct 13:17Z fire) will replace the baseline with a clean-success number once it terminates (~14:21Z ETA).

---

## Appendix B — Why not just turn on `--skip-existing` everywhere

dispatch.sh has a `--skip-existing` flag that gates per-script-execution on a marker file at `gold/artifacts/{SCRIPT_ID}/{RUN_DATE}`. **That's per-chain-run gating, not per-partition gating.** It skips an entire script execution if any marker exists. Useful for backfill orchestration, not for "skip 1,749 of 1,750 partitions inside this script's loop."

The proposal here is per-partition idempotence INSIDE each script's main loop, not per-script skip at the dispatcher level. These are complementary: `--skip-existing` remains useful for orchestrating partial chain reruns; the per-partition gate solves the actual cost problem.
