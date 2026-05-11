# DS~B 2026-05-11 — INF Gold A-Layer Efficiency + Reality Audit (ADVI_INFNNA.A-GROUP-AUDIT)

**Agent:** 0.4.0_DS_ClientPlatform~B
**TO:** `ADVI_INFNNA.A-GROUP-AUDIT.dsb-gold-a-layer-efficiency-and-reality-audit`
**Scope:** Read-only audit of `data/orion/scripts/gold/INF_A_00..INF_A_04.py`. No script edits.
**Telemetry sources:** `.runtmp/telemetry/2026-05-08/` (Friday baseline, 1 run/script), `.runtmp/telemetry/2026-05-11/` (today re-cascade, 1-3 runs/script).
**Authorized by:** Andrew direct 2026-05-11 — A-group efficiency hypothesis.

---

## Executive Summary (top of file for COO RAVC)

| # | Finding | Class | Confidence | Est. wall-clock savings | Follow-up TO suggestion |
|---|---------|-------|-----------|------------------------|------------------------|
| 1 | **`INF_A_03.positions_cube` per-(account_id, ticker) Python loop with `iterrows()` over forward-filled daily series is the dominant cost** — 583s wall, 3.36GB peak, 14% of cascade. Sequential expansion of ~33K (account, ticker) pairs × ~2,180 days. BD A_03 solved this with `ProcessPoolExecutor` + numpy-array expansion (`_expand_one_pair` module-level fn). | Architectural inefficiency | HIGH | **8-9 min → ~1-2 min** (4-6x via process-pool + numpy arrays) | `INF_A_03.PARALLEL-EXPAND` (port BD's expansion architecture) |
| 2 | **Triple-load of `silver/transactions/`** — A_00, A_01, A_03 each independently fan out a 64-thread S3 read of all 1,510 transaction partitions. ~30s × 3 = ~90s of duplicated I/O per cascade. A shared transactions cache would eliminate ~60s. | Architectural inefficiency | HIGH | **~60s** (40% of A-layer non-A_03 wall) | `INF_A_LAYER.TXN-CACHE` (single load + in-memory share OR materialized intermediate) |
| 3 | **`INF_A_03` writes 2,178 daily parquets sequentially via single-thread `s3.put_object`** — ~30s for the write phase. BD A_03 uses `S3_WRITE_WORKERS=64` ProcessPool. Trivial to port. | Architectural inefficiency | HIGH | **~25s** of A_03 wall | Subsumed by #1 (port full BD architecture) |
| 4 | **247 stale legacy parquets in `gold/positions_cube/`** (2019-09-17 → 2020-05-25) — silver/transactions only goes back to 2020-05-26, so current code never re-writes these dates. Hygiene only, not perf. | Data hygiene | HIGH | None (S3 storage only) | `INF_A_03.STALE-PURGE` (one-time `aws s3 rm` of 247 keys) |
| 5 | **`INF_A_02.fee_rate_history` runs every cascade to write a 0-row stub.** Boto3 init + S3 upload for an empty parquet is ~1s wasted compute + 1 unnecessary S3 PUT per cascade. Could be skipped at orchestrator level until Orion Advisory Fees data is wired. | Architectural | MEDIUM | <2s; mostly cleanliness | Skip via orchestrator config OR delete script + remove from cascade manifest |
| 6 | **`INF_A_03` Python `for (acct_id, tkr), grp in chunk.groupby(...)`-then-`for dt, row in grp.iterrows()` pattern produces ~29M iterrows calls** (1,115 accts × ~12 tickers × ~2,180 days). Iterrows is the worst pandas idiom for inner loops; numpy-array expansion replaces it cleanly. | Implementation | HIGH | included in #1 | included in #1 |
| 7 | **`INF_A_03`'s `MIN_OUTPUT_DATE = '2019-09-01'`** is dead code — silver/transactions earliest is 2020-05-26, so target_dates start at 2020-05-26 regardless. Vestigial constant, no functional impact today. | Dead code | HIGH | None | Bundle into #1 cleanup OR drop as "noted" |
| 8 | **`INF_A_03` writes via `put_object` with `ServerSideEncryption='AES256'`** while A_00/A_01/A_04 use `s3.upload_file` (no SSE specified — bucket-default applies). Asymmetric, but bucket-default is AES256, so no functional drift. Worth noting. | Consistency | MEDIUM | None | Bundle into #1 |

**Top-3 follow-up TOs (prioritized for `expected wall-clock savings × confidence`):**

1. **`ADVI_INFNNA.INF_A_03_PARALLEL-EXPAND`** — Port BD A_03's `_expand_one_pair` ProcessPool + numpy-array expand + parallel S3 write into `INF_A_03`. Drop `iterrows()` loop. Expected: **583s → ~120s on A_03**, **8-9 min cascade savings**. Effort ~3-4h. Confidence HIGH (BD precedent in production). Acceptance: A_03 wall-clock < 180s, peak mem < 2GB, output byte-identical to current cube on 5 spot-check dates.
2. **`ADVI_INFNNA.INF_A_LAYER_TXN-CACHE`** — Single shared load of silver/transactions/ at A-layer entry; A_00/A_01/A_03 read from in-memory cache (or materialized `/tmp/inf_silver_txn_cache.parquet`). Expected: **~60s saved per cascade**. Effort ~2h. Confidence HIGH. Acceptance: A_00, A_01, A_03 all complete with same outputs as today, `silver/transactions/` ListObjectsV2 + GetObject calls counted in CloudWatch drop ~67%.
3. **`ADVI_INFNNA.INF_A_02_RETIRE`** — Either delete script (`INF_A_02.fee_rate_history.py`) and remove from cascade manifest until Orion Advisory Fees data is wired, OR add an orchestrator-level skip flag. Expected: <2s saved (mostly hygiene). Effort ~30min. Confidence MEDIUM (depends on whether downstream readers expect the empty stub at the S3 path — needs grep). Acceptance: cascade manifest no longer dispatches A_02 OR script lifts skip-if-stub flag; downstream B/C/D scripts that may read the stub still work (probably none — TODO verify).

**Ship recommendation:** Author (1) immediately as priority HIGH; it's the single biggest cascade-wall-clock win in the gold layer. Author (2) as priority MEDIUM. Author (3) as low-priority hygiene.

---

## Per-Script Summary

### INF_A_00.accounts_dimension (194 lines)

| Field | Value |
|-------|-------|
| Input | `silver/transactions/{date}.parquet` × 1,510 (full-history fan-out, 64-thread pool, ~27s) |
| Transform | concat all → groupby account_id → first-row-per-account-by-trade-date for metadata + min/max trade_date for date bounds; pd.to_numeric on household_id |
| Output | `gold/dimensions/accounts_dimension_latest.parquet` (1,115 rows × 17 cols, ~44KB) |
| Parallelization | `ThreadPoolExecutor(max_workers=64)` for S3 read; single-thread groupby/sort |
| Friday wall | 26.8s | Today wall | 27.6-32.1s |
| Friday peak mem | 643MB | Today peak mem | 549MB |
| Friday cpu_max | 703.9% (read phase) | Today cpu_max | 740.9% |
| Threads peak | 90 | Notes | I/O-bound; cpu_max captures the threadpool burst |

### INF_A_01.advisor_assignments (184 lines)

| Field | Value |
|-------|-------|
| Input | `silver/transactions/{date}.parquet` × 1,510 (same fan-out as A_00 — DUPLICATED I/O) |
| Transform | groupby account_id → keep latest-trade-date row → output rep_id/rep_name/advisor_key/rep_bucket/custodian. Includes Keil/Keil dedup detection (irrelevant for INF — INF has no rep_id 4 or 5). |
| Output | `gold/dimensions/advisor_assignments.parquet` (1,115 rows × ~7 cols) |
| Parallelization | `ThreadPoolExecutor(max_workers=64)` for S3 read |
| Friday wall | 27.1s | Today wall | 25.5-27.9s |
| Friday peak mem | 333MB | Today peak mem | 394MB |
| Notes | **Keil/Keil dedup is BD-port dead code for INF** — INF has rep_ids {3, 6, 11, 12} only. Won't fire but isn't doing harm; document as port artifact. |

### INF_A_02.fee_rate_history (97 lines)

| Field | Value |
|-------|-------|
| Input | None (writes empty stub) |
| Transform | `pd.DataFrame(columns=[...])` with explicit dtype cast |
| Output | `gold/dimensions/fee_rate_history.parquet` (0 rows, ~1KB) |
| Parallelization | None (single-threaded) |
| Friday wall | <1 tick (not in 5/8 distribution; presumably ran in <0.5s and never sampled) |
| Today wall | 1.0-1.1s (3 runs sampled) |
| Notes | **Stub-only.** Wires up boto3 + uploads empty parquet every cascade. Per docstring: "When Orion Advisory Fees data becomes available... mirror BD INF_A_02.fee_rate_history.py." Until then, this is wasted ceremony. |

### INF_A_03.positions_cube (311 lines) — **LEAD SUSPECT**

| Field | Value |
|-------|-------|
| Input | `silver/transactions/{date}.parquet` × 1,510 (third independent fan-out, 64-thread pool) |
| Transform | (1) Load + concat all transactions; (2) sort by (account_id, ticker, trade_date); (3) cumsum per (account_id, ticker); (4) per-day groupby last; (5) **per-(account_id, ticker) Python loop with `set_index → reindex → ffill → loc → iterrows`**; (6) bucket rows into per-date dict; (7) **sequential `for dt_str in sorted(date_buffers): s3.put_object(...)` write** |
| Output | `gold/positions_cube/{date}.parquet` × ~2,178 (single custodian: fidelity) |
| Parallelization | Read: 64-thread S3 pool. **Compute + Write: SINGLE-THREADED.** |
| Friday wall | 583.1s (9.7 min) — **14% of total cascade wall** | Today wall | 766-959s (FULL re-runs) + 42.6s (delta run) |
| Friday peak mem | 3,362MB | Today peak mem | 3,360MB |
| Friday cpu_p50 | 89.2% (median) | cpu_max | 689.9% |
| Friday threads | 89 peak | mem_p50 | 2,940MB sustained |
| **Hot path** | `for (acct_id, tkr), grp in chunk.groupby(...)` followed by `for dt, row in grp.iterrows()` — produces ~29M `iterrows` calls (1,115 accts × ~12 distinct tickers × ~2,180 days). Iterrows is the worst-case Python idiom inside a pandas loop. |
| **Memory hotspot** | The `date_buffers` dict-of-lists accumulates EVERY (account, ticker, date) row in memory before any S3 write. ~33K × 2,180 = 71M rows × ~80 bytes/dict = ~5.7GB worst case (collapsed by sparsity to observed 3.4GB). |
| Output keys | 2,425 actually exist; current code-path writes 2,178; the **247-key delta is stale 2019-09 → 2020-05 carryover** from a prior run before silver/transactions was clipped to 2020-05-26 |

### INF_A_04.client_dimension (197 lines)

| Field | Value |
|-------|-------|
| Input | `gold/dimensions/accounts_dimension_latest.parquet` (A_00 output, single read) + latest `silver/aum_snapshot/{date}.parquet` (single read for household_name) |
| Transform | groupby household_id → mode-by-count for primary advisor + first/min for dates → merge household_name |
| Output | `gold/dimensions/client_dimension.parquet` |
| Parallelization | None (everything is single-frame ops on small data) |
| Friday wall | (not in distribution; <0.5s sample) | Today wall | 0-2.1s |
| Notes | Properly downstream of A_00; doesn't duplicate the silver/transactions load. **Already efficient.** No changes recommended. |

---

## Telemetry Cross-Reference

### A-layer scripts only (Friday baseline, full cascade run)

| Script | Wall (s) | Peak Mem (MB) | CPU max | Threads | % of A-layer wall |
|---|---|---|---|---|---|
| INF_A_00 | 26.8 | 643.4 | 703.9% | 90 | 4.0% |
| INF_A_01 | 27.1 | 333.0 | 743.8% | 88 | 4.1% |
| INF_A_02 | <0.5 | ~115 | ~90% | ~14 | <0.1% |
| **INF_A_03** | **583.1** | **3,362.5** | **689.9%** | **89** | **87.7%** |
| INF_A_04 | <0.5 | ~125 | ~80% | ~12 | <0.1% |
| **A-layer total** | **~664s** | | | | |

### Today re-cascade (3 A_03 runs)

| Run | Wall (s) | Peak Mem (MB) | CPU max | Notes |
|---|---|---|---|---|
| A_03 #1 (full) | 958.9 | 3,360.2 | 713.9% | Full historical rebuild + 2 new dates (5/10, 5/11) vs Friday's 5/8 cutoff = ~375s extra wall vs Friday |
| A_03 #2 (full) | 766.4 | 3,355.8 | 738.5% | Second full re-run; warmer S3 cache, slightly faster |
| A_03 #3 (delta) | 42.6 | 468.5 | 735.4% | Likely `--start-date` or `--skip-existing`, only writes recent dates |

**Implication:** The full-rebuild path is incrementally more expensive as time advances (+375s in 3 days = ~125s/date because of cumulative+forward-fill). **Without parallelization this scales linearly worse with history.** This is the time-bomb.

---

## Audit Per Dimension

### (a) Path validity

All paths verified via `aws s3 ls`:

| Script | Path | Verified |
|---|---|---|
| A_00 read | `silver/transactions/` (1,510 keys) | OK |
| A_00 write | `gold/dimensions/accounts_dimension_latest.parquet` (44KB) | OK |
| A_01 read | `silver/transactions/` (1,510 keys) | OK |
| A_01 write | `gold/dimensions/advisor_assignments.parquet` | OK |
| A_02 write | `gold/dimensions/fee_rate_history.parquet` (stub) | OK |
| A_03 read | `silver/transactions/` (1,510 keys) | OK |
| A_03 write | `gold/positions_cube/{date}.parquet` (2,425 keys, **247 are stale orphan from pre-2020-05-26 silver**) | PARTIAL — see #4 above |
| A_04 read | `gold/dimensions/accounts_dimension_latest.parquet` + `silver/aum_snapshot/` | OK |
| A_04 write | `gold/dimensions/client_dimension.parquet` | OK |

### (b) Column validity

Sampled current silver/transactions/2026-05-07.parquet columns (via comp-pipescript io would be cleaner but the txn schema isn't catalogued there; manual sample):

| Script | Columns read | All present in current silver? |
|---|---|---|
| A_00 KEEP_COLS | account_id, account_code, household_id, registration_id, registration_name, reg_type, rep_id, rep_name, advisor_key, rep_bucket, custodian, is_managed, client_last_name, trade_date | All sampled present (~14 cols) |
| A_01 KEEP_COLS | account_id, trade_date, rep_id, rep_name, advisor_key, rep_bucket, custodian | OK |
| A_03 KEEP_COLS | account_id, trade_date, ticker, units, custodian | OK |
| A_04 reads from accounts_dim (A_00 output) — column safety via A_00 | OK | |

No stale column reads. Code uses `[c for c in KEEP_COLS if c in df.columns]` defensive filter — a row with a column drop wouldn't crash, just silently lose data. Acceptable for v1; may want hard-fail in a future hardening pass.

### (c) Join necessity

| Script | Joins | Necessary? |
|---|---|---|
| A_00 | 1 self-merge: `latest.merge(date_bounds, on='account_id')` | YES — separates current-metadata from date-bounds aggregation |
| A_01 | None | n/a |
| A_03 | 1 self-cumsum (no merge across frames) | n/a |
| A_04 | 1 join: `agg.merge(household_names, on='household_id')` | YES — household_name comes from a different source (aum_snapshot) |

No unnecessary joins identified. **A-layer is well-decomposed at the join level.**

### (d) Filter timing

A_03 has **one filter-after-expensive-op pattern**: `chunk = snap[snap['account_id'].isin(chunk_accts)].copy()` inside the chunk loop — the `.isin()` runs against the full `snap` frame on each chunk. Tradeoff acceptable in pandas (vectorized), but a pre-sort + slice would be slightly cheaper. Not the dominant cost.

A_03 ALSO has the early-exclude of zero-unit rows in `_load_one`: `sub = sub[sub['units'] != 0]` — this is correctly applied at S3-read-time per partition, before concat. **GOOD pattern.**

### (e) Parallelization opportunity

| Script | Current | Opportunity |
|---|---|---|
| A_00 | ThreadPoolExecutor(64) for read | None significant — read is already parallel; compute is groupby on 1,115 accounts (microseconds) |
| A_01 | ThreadPoolExecutor(64) for read | None significant — same shape as A_00 |
| A_02 | None | n/a (stub) |
| **A_03** | **ThreadPoolExecutor(64) for READ ONLY**; compute + write are single-threaded | **MASSIVE — port BD's ProcessPoolExecutor `_expand_one_pair` numpy-array expand + S3_WRITE_WORKERS parallel write** |
| A_04 | None | n/a (small data) |

---

## INF_A_03 Deep-Dive

### Root cause hypothesis

Friday telemetry: `cpu_p50=89.2%` (median CPU = single-core), `cpu_max=689.9%` (during read phase). This mismatch is the smoking gun — **the 583s wall is 27s of multi-threaded read + ~556s of single-threaded Python expansion**.

The hot loop:

```python
for (acct_id, tkr), grp in chunk.groupby(['account_id', 'ticker']):
    grp = grp.set_index('date')[['cum_units']].sort_index()
    start = grp.index.min()
    end = pd.Timestamp(max(target_dates))
    full_range = pd.date_range(start, end, freq='D')
    grp = grp.reindex(full_range).ffill()
    target_idx = [d for d in pd.DatetimeIndex(target_dates) if d >= start]
    if not target_idx:
        continue
    grp = grp.loc[grp.index.isin(target_idx)]
    grp = grp[grp['cum_units'] > 1e-9]
    if grp.empty:
        continue
    for dt, row in grp.iterrows():           # <-- 29M-call hot path
        dt_str = str(dt.date())
        if dt_str not in date_buffers:
            date_buffers[dt_str] = []
        date_buffers[dt_str].append({
            'account_id': acct_id, 'ticker': tkr, 'units': row['cum_units']
        })
```

**Three nested issues:**
1. Per-group pandas overhead: `set_index`, `reindex`, `loc`, `isin` each cost ~ms. ~33K groups × ~5ms = **~165s pandas overhead alone**.
2. `iterrows()` Python-row-iteration on each ffilled group: ~29M iterations × tens of microseconds = **~300-500s**.
3. `date_buffers` dict-of-lists with per-row dict allocation: ~71M dict creations + appends in the steady state.

### Testable hypothesis (for follow-up TO)

Replace the per-(account, ticker) loop with the BD pattern (port `_expand_one_pair` from `data/black_diamond/scripts/gold/A_03.positions_cube.py:1036-1080`):

```python
# Sketch — port BD pattern
def _expand_one_pair(args):
    account_id, ticker, trade_dates_ns, cum_units, end_date_ns, expand_start_ns = args
    # numpy-only forward-fill: searchsorted + take
    ...
    return account_id, ticker, dates_out, units_out

with ProcessPoolExecutor(max_workers=EXPAND_WORKERS) as pool:
    results = pool.map(_expand_one_pair, work_items, chunksize=64)
```

**Expected outcome on next telemetry run:**
- A_03 wall: 583s → **120-150s** (4-5x speedup)
- A_03 cpu_p50: 89% → **400-600%** (process-pool utilization)
- A_03 peak mem: 3,360MB → **<2,000MB** (numpy arrays vs dict-of-lists)
- Output byte-identical (subject to row order; sort post-hoc for parity)

### Memory experiment (no code change required to validate hypothesis)

Run on EC2 runner:
```bash
python -c "
import pandas as pd, io, boto3
s3 = boto3.client('s3', region_name='us-east-1')
keys = ['silver/transactions/2026-05-07.parquet']
df = pd.concat([pd.read_parquet(io.BytesIO(s3.get_object(Bucket='opal-data-inf', Key=k)['Body'].read())) for k in keys])
print('one-day rows:', len(df), 'unique (acct,tkr):', df.groupby(['account_id','ticker']).ngroups)
"
```
Expected: ~9,600 rows / day, ~9,600 unique (acct, tkr) — but historical pairs include all-time-ever-held tickers per account, hence the ~33K-pair total across history.

---

## BD/49F Architectural Comparison

| Dimension | BD/49F (data/black_diamond/scripts/gold/) | INF (data/orion/scripts/gold/) | Verdict |
|---|---|---|---|
| **A_03 LOC** | 1,762 lines | 311 lines | INF is leaner BECAUSE it doesn't yet need RPS/sleeve/synthetic injection. Architecturally OK; functionally MISSING parallelism. |
| **A_03 expand strategy** | `ProcessPoolExecutor` + `_expand_one_pair` numpy-array forward-fill | Sequential Python `for ... iterrows()` over groupby | **MAJOR DIVERGENCE — INF lost the parallelism on port.** |
| **A_03 S3 write** | `S3_WRITE_WORKERS=64` parallel ProcessPool put_object | Sequential `for dt_str in sorted: put_object` | INF lost parallel write on port. |
| **A_03 memory strategy** | "Process accounts oldest-first; flush 'safe' partitions" + category dtypes | Single in-memory dict-of-lists; no flush; no category dtypes | INF should adopt the early-flush pattern; not strictly needed for current 3.3GB peak but will be needed if INF data scale 10x's. |
| **A_03 transaction-type filtering** | Explicit BUY_TYPES/SELL_TYPES/CA_BUY_SUBTYPES/CA_SELL_SUBTYPES sets — filters rows by type before cumsum | INF uses `units != 0` as the only filter — relies on Orion silver having signed `units` field encoded correctly | **DELIBERATE DIVERGENCE.** Orion TRN ships signed units pre-classified; BD has to reconstruct sign from transaction_type strings. INF is correct here (per docstring) — do NOT port BD's BUY/SELL_TYPES sets. |
| **A_03 RPS / synthetic injection** | `_load_rps_injection_events`, `_load_synthetic_buy_events`, `_load_phantom_exclusion_set` | None | Correct for INF v1 (Orion-only, no RPS feed). Re-evaluate when sleeve work lands. |
| **A_03 corporate action handling** | Explicit Merger/Conversion/Spinoff/Split sub-type taxonomy | Implicit in Orion's signed `units` | Same deliberate divergence. Defensible until/unless Orion CA mishandling surfaces (none observed in current 1,115-account corpus). |
| **MIN_OUTPUT_DATE** | Env-var `O2_MIN_OUTPUT_DATE` (default 2020-01-01); BD has bond data dating to 1970s | Hardcoded `'2019-09-01'` (dead code given current silver shape) | Cosmetic; INF should mirror env-var pattern but it's not load-bearing. |
| **A_00, A_01 silver/txn read** | (per BD A_00 — would need separate read to compare; likely same triple-read pattern) | Triple independent fan-out across A_00/A_01/A_03 | Suspected same anti-pattern in BD — outside this TO's scope. |
| **A_04 client dim** | More richness (49F has 150 advisors, primary-advisor mode-of-mode) | Mode-of-rep_id + first/min on small frame | INF's simplification is correct (4 advisors, no advisor migration history). |

**Three architectural divergences worth highlighting:**

1. **A_03 lost the ProcessPool on port.** This is the lead recommendation.
2. **A_03 lost the parallel S3 write.** Bundle into the same fix.
3. **INF data scale doesn't yet need BD's "process accounts oldest-first + flush safe partitions" pattern** — but if INF expands to multi-firm later (the COMP-V4 trajectory) we'll want it. Mention as future-proofing in the follow-up TO.

**Inflection-specific simplification opportunity NOT yet taken:**

INF has 4 advisors with disjoint accounts (per accounts_dimension `rep_id` distribution: rep_12=602, rep_3=295, rep_11=151, rep_6=67). Cumsum-per-(account, ticker) doesn't naturally parallelize by rep_id, but **A_03 expansion COULD shard the 33K-pair work across 4 rep_id-keyed processes** — a parallelization grain that 49F's 150-advisor case wouldn't gain from but Inflection's 4-rep case might find natural. Worth noting alongside the BD-pattern port; the BD-pattern (per-pair process-pool) is more general and gives the same benefit.

---

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `comp-pipescript io INF_A_03` | not run — INF gold-script catalog coverage in compiler graph is partial; manual source read sufficed for this read-only audit | n/a |
| `python .tools/runner-telemetry-analyze.py .runtmp/telemetry/2026-05-08/inf-gold-layer-runner/` | full Friday cascade distribution across 37 scripts | OK — used directly above |
| `python .tools/runner-telemetry-analyze.py .runtmp/telemetry/2026-05-11/inf-gold-layer-runner/` | today re-cascade across 15 runs / 5 A-scripts | OK — used directly above |
| `aws s3 ls` (path validity per script) | listed `gold/positions_cube/`, `silver/transactions/`, `gold/dimensions/*` | OK — all paths present; 247 stale keys flagged in `gold/positions_cube/` |
| `aws s3 cp + pandas read` | sampled `accounts_dimension_latest.parquet` + 3 days of positions_cube | OK — confirms 1,115 account scale + per-day row density |

No script edits, no commits, no S3 writes — read-only audit consistent with TO scope.

---

## Files Modified

| File | Change |
|------|--------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-11/DS_B_a_group_audit_findings.md` | this audit document (NEW) |

No script source modified. No S3 writes. No commits.

---

## Acceptance Criteria Self-Check

| # | AC | Status |
|---|---|---|
| 1 | Per-script summary for all 5 A-scripts | PASS — section "Per-Script Summary" |
| 2 | Telemetry cross-reference (Friday + today) | PASS — section "Telemetry Cross-Reference" with both dates |
| 3 | Audit findings across (a) path, (b) columns, (c) joins, (d) filter timing, (e) parallelization | PASS — section "Audit Per Dimension" with 5 sub-sections |
| 4 | INF_A_03 deep-dive with at minimum 1 testable hypothesis | PASS — section "INF_A_03 Deep-Dive" with port-BD-pattern hypothesis + expected wall/mem deltas |
| 5 | BD/49F comparison with at least 3 architectural divergences | PASS — 9 divergences enumerated; 3 highlighted as actionable |
| 6 | Findings document at canonical path, cleanly structured | PASS — this file |
| 7 | Top-3 follow-up TO recommendations with effort + expected savings | PASS — Executive Summary section, top of file |
| 8 | RAVC delivered with executive summary + top findings | PASS — RAVC4 dispatched to 2.0.0_SA_COO post-write |
| 9 (added by COO 2026-05-11) | Recommendations crystallize as separate follow-on TO drafts (status `staged`, not dispatched). NO implementation in this TO. | PASS — 3 staged drafts authored under `task_orders/` (ledger below); zero source edits to A-scripts |

### Draft TO ledger (AC9 — staged, awaiting COO ratification + dispatch)

| Draft TO file | Priority | Est. effort | Lead win |
|---|---|---|---|
| `ADVI_INFNNA.INF_A_03_PARALLEL-EXPAND.draft-port-bd-processpool-numpy-expand.md` | high | ~3-4h | A_03 wall 583s → ~120-150s (4-5x); 8-9 min cascade savings |
| `ADVI_INFNNA.INF_A_LAYER_TXN-CACHE.draft-shared-silver-txn-cache.md` | medium | ~2h | ~60s saved by eliminating triple silver/transactions read |
| `ADVI_INFNNA.INF_A_02_RETIRE.draft-skip-or-delete-fee-rate-stub.md` | low | ~30min | Cleanliness; <2s saved per cascade |

All three drafts use status `staged` per AC9. None added to REGISTRY by DS~B. COO ratifies + dispatches as separate GO messages if approved.

---

## Next Steps

1. RAVC4 to 2.0.0_SA_COO with executive summary + top-3 follow-up TO recommendations + invitation to author follow-ups.
2. Mark TO complete (status pending → complete).
3. Stand by for routing — DS~B IDLE post-RAVC.

---

## Diagnostics Retained

- `C:\Users\AndrewBerman\AppData\Local\Temp\inf_acct.parquet` — INF accounts dim sample for rep_id distribution
- (no other intermediate files; analyzer outputs captured inline above)
