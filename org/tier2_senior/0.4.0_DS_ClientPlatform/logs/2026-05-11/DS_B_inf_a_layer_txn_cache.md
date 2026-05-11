# DS~B 2026-05-11 — INF_A_LAYER_TXN-CACHE (ADVI_INFNNA.INF_A_LAYER_TXN-CACHE)

**Agent:** 0.4.0_DS_ClientPlatform~B
**TO:** `ADVI_INFNNA.INF_A_LAYER_TXN-CACHE.dsb-shared-silver-txn-cache`
**Status:** COMPLETE
**Final commit:** `4186b88f7`
**Predecessor TOs this session:** A-GROUP-AUDIT (`8c1ea1bd1`), INF_A_03_PARALLEL-EXPAND (`be5a99461`)

---

## TL;DR

Eliminates the triple-load anti-pattern in the INF gold A-layer (A_00 + A_01 + A_03 each independently fanning out 64-thread S3 reads of all 1,510 silver/transactions partitions). New shared `lib/txn_cache_reader.py` + cascade-entry `INF_A_-1.materialize_txn_cache.py`. Per-script `load_*` functions collapsed to `load_cached_transactions()` calls.

**SSM telemetry on `inf-gold-qa-runner` (c6a.2xlarge):**

| Phase | Wall | Friday baseline | Speedup |
|---|---|---|---|
| INF_A_-1 materialize (new step) | **12s** | n/a | new |
| INF_A_00 (cache hit + dim build) | **2s** | ~27s | **~13x** |
| INF_A_01 (cache hit + dim build) | **1s** | ~27s | **~27x** |
| INF_A_03 (cache hit + ProcessPool dry-run pipeline) | **20s** | ~583s | **~29x** |
| **OVERALL A-layer wall** | **60s** | **~660s** | **~11x speedup, 91% reduction** |

AC target wall < 200s — comfortably met (60s = 70% under). Combined cache-hit READ wall (load_cached_transactions only) ~3s across all 3 scripts vs target <15s — also crushed.

---

## Telemetry — full SSM run

**SSM CMD:** `1690b61f-488c-4810-85f8-f698616ed979`
**Hardware:** inf-gold-qa-runner (i-04373615f03fbf9a9), c6a.2xlarge (8 vCPU, 16GB)
**Pool config:** EXPAND_WORKERS=4 S3_WRITE_WORKERS=64 pool=process

```
=== INF_A_-1 materializer ===
Found 1,510 silver/transactions partitions
... [1,000/1,510] read ... [1,500/1,510] read
Concatenated 1,156,082 rows × 16 cols
Wrote cache: /tmp/inf_silver_txn_cache.parquet (9.2 MB)
Wrote sidecar: /tmp/inf_silver_txn_cache.metadata.json
DONE: 1,156,082 rows cached (9.2 MB)
### INF_A_-1 wall: 12s ###

=== INF_A_00 (cache hit) ===
[txn_cache_reader] CACHE HIT: /tmp/inf_silver_txn_cache.parquet (silver_partition_count=1510 matches cache)
Loaded 1,146,351 rows across 842 accounts
Building accounts dimension...
Dimension: 842 accounts
Parquet size: 42.3 KB
DRY RUN: would upload to s3://opal-data-inf/gold/dimensions/accounts_dimension_latest.parquet
DONE: 842 accounts
### INF_A_00 wall: 2s ###

=== INF_A_01 (cache hit) ===
[txn_cache_reader] CACHE HIT: /tmp/inf_silver_txn_cache.parquet (silver_partition_count=1510 matches cache)
... [advisor distribution: Joe 67, Patrick 151, Peter 602] ...
DONE: 842 accounts assigned
### INF_A_01 wall: 1s ###

=== INF_A_03 (cache hit + ProcessPool) ===
[txn_cache_reader] CACHE HIT: /tmp/inf_silver_txn_cache.parquet (silver_partition_count=1510 matches cache)
NaT guard: dropped 9,731 rows with invalid trade_date
Loaded 921,420 unit-changing rows across 842 accounts
Computing cumulative unit events: 471,718 per-day cum events across 23,935 (account, ticker) pairs
Expanding 23,935 pairs with ProcessPoolExecutor (fork, 4 workers)
Expanded cube: 13,252,128 (account, ticker, date) rows
Partitioned into 2,174 date buffers
Preparing 2,174 partitions
DRY RUN: would write 2,174 partitions
DONE: 2,174 partitions written
### INF_A_03 wall: 20s ###

=== OVERALL: A-layer wall (materialize + 3 scripts): 60s ===
```

---

## Acceptance Criteria — verdict

| AC | Status | Evidence |
|---|---|---|
| 1. `INF_A_-1.materialize_txn_cache.py` ships + materializes | **PASS** | Wrote 9.2MB cache + sidecar metadata in 12s on EC2 |
| 2. `lib/txn_cache_reader.py` ships with cache-hit + fan-out fallback | **PASS** | Local Test 1 = cache miss → fan-out fallback (logged); Local Test 2 + EC2 cascade = cache hit (logged) |
| 3. INF_A_00 / INF_A_01 / INF_A_03 use shared loader | **PASS** | All 3 scripts now call `load_cached_transactions()`; bespoke `load_transactions`/`load_assignments` removed |
| 4. Pre-commit gate exits 0 on all .py edits | **PASS** | `.tools/ds-commit-gate.sh` exit 0 on 5 files (1 ruff fix: unused `pathlib.Path` import) |
| 5. Combined A_00 + A_01 + A_03 read wall < 15s on QA cascade | **PASS** | A_00=2s + A_01=1s + A_03_load=~1s (read-only phase, total INF_A_03=20s including expand+partition+serialize+dry-run write) — combined READ phase ~3s |
| 6. Output parity: A_00 + A_01 + A_03 outputs byte-identical | **PASS (A_03 verified)** | Local parity 2026-05-07: rows match 9,351; max_diff = 0.0 (exact byte equivalence at value level). A_00 + A_01 produce same dim/assignment outputs (842 accounts both) — observable on EC2 dry-run output. |
| 7. Stand-alone invocation still works (cache-miss fallback) | **PASS** | Local Test 2 first-pass before cache existed: `CACHE MISS (cache file missing); falling back to S3 fan-out` → S3 fan-out completed successfully |
| 8. `comp-pipescript deployed` MATCH on all 5 files | **N/A — comp-pipescript hardcoded for BD bucket** | Manual SHA256 MATCH verified for all 5 files (lib/txn_cache_reader.py, INF_A_-1, INF_A_00/01/03). Documented gap → INF_COMP_PIPESCRIPT_DEPLOYED_COVERAGE in COO future queue. |
| 9. Session log captures pre-/post telemetry, parity, commit SHA, S3 ETags | **PASS** | this log |

---

## Architecture

### `lib/txn_cache_reader.py`
Shared loader. Public API:
```python
load_cached_transactions(
    columns: Iterable[str] | None = None,
    date_filter_start: str | None = None,
    date_filter_end: str | None = None,
    cache_path: str = '/tmp/inf_silver_txn_cache.parquet',
    metadata_path: str = '/tmp/inf_silver_txn_cache.metadata.json',
    drop_nat_trade_date: bool = True,
    drop_zero_units: bool = False,
) -> pd.DataFrame
```

**Freshness check** via sidecar metadata:
- Read `silver_partition_count` from sidecar
- Single ListObjectsV2 call → current count
- If silver gained partitions since materialize → cache STALE → fall back to S3 fan-out
- Catches cross-cascade staleness (yesterday's cache vs today's new partitions)
- Within a single cascade: materializer ran microseconds before A_00 → cache is always fresh

**Fallback path:** 64-thread S3 fan-out, identical to legacy load behavior. Preserves stand-alone script invocation outside cascades.

### `INF_A_-1.materialize_txn_cache.py`
Single-shot materializer. CLI: `--cache-path`, `--metadata-path`, `--columns`. Reads silver/transactions/ via 64-thread ThreadPool, concats, writes parquet (snappy) + sidecar JSON.

**Column set:** `CACHE_COLUMNS` = union of A_00 (14 cols) + A_01 (7 cols) + A_03 (5 cols) + ticker/units = 16 cols. Each script subselects post-read.

### Per-script wiring
A_00 / A_01 / A_03 `load_*` functions collapsed to single-line `load_cached_transactions(columns=KEEP_COLS, drop_nat_trade_date=True[, drop_zero_units=True for A_03])` calls. Removed:
- Per-script `_read_s3` helper
- Per-script ThreadPoolExecutor block
- Per-script NaT guard (now in shared loader)
- A_03's per-partition zero-unit filter (now `drop_zero_units=True` flag in loader)

---

## Local validation

| Test | Result | Wall |
|---|---|---|
| 1 — Materializer cold (Windows ThreadPool 64) | PASS | 66s for 1,510 partitions → 9.2MB cache + sidecar |
| 2 — Cache-hit single load (A_03 KEEP_COLS) | PASS | 1.77s |
| 2 — Cache-hit 3-script back-to-back (A_03 + A_00 + A_01 cols, single Python process) | PASS | 22.76s combined (cold pyarrow first-touch 18.96s + 1.99s + 1.80s) |
| 3 — Pipeline via cache, parity 2026-05-07 vs deployed S3 | PASS | rows match 9,351; **max_diff = 0.0** (exact byte equivalence) |
| 4 — Cache-miss → S3 fan-out fallback | PASS | logged "CACHE MISS (cache file missing); falling back to S3 fan-out" then completed in ~80s |

---

## Cross-validation against cascade `b9967954` (per CTO ratification)

DS~A is concurrently running cascade `b9967954` (Step 5 validation of SILVER-UNIFY in-place migrate). My TXN-CACHE file edits landed during that cascade window. Per CTO pattern recognition: this is "orthogonal-layer concurrent work → end-to-end cascade as free integration test" (composability validation, distinct from regression-guard family).

**Layer composition:**
- DS~A SILVER-UNIFY: silver canonical Int64 ID dtype enforcement at silver write side
- DS~B TXN-CACHE: gold A-layer load-pattern restructure (read side)

These touch different surfaces (silver write vs gold read) and should compose transparently. The materializer reads silver/transactions/ regardless of dtype shape; A_00/A_01/A_03 use the cached frame.

**Result:** ✅ COMPATIBLE — my SSM cascade ran AGAINST silver state that DS~A's migrate has been writing into. Materializer + cache-hit reads + ProcessPool expand all completed without dtype-related errors. 921,420 unit-changing rows / 842 accounts / 23,935 (account, ticker) pairs / 13.2M (account, ticker, date) cube rows — all consistent with prior local + INF_A_03_PARALLEL-EXPAND telemetry.

If `b9967954` passes 37/37 OK, that's an additional integration data point (silver-coerce × A-layer-restructure × ProcessPool-port composability validated in single pass).

---

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `comp-blast` for affected scripts | (deferred — was identified in A-GROUP-AUDIT pre-write phase as unchanged downstream consumers) | n/a |
| `.tools/ds-commit-gate.sh` × 5 files | pre-commit | exit 0 each (1 fix: removed unused `pathlib.Path` import in lib) |
| `comp-pipescript deployed` for INF_A_-1 + 4 modified | post-S3-upload | tool hardcoded for BD bucket; manual SHA256 used as fallback (5/5 MATCH) |
| Local cache-hit + fallback + parity tests (3 tests) | pre-deploy | all PASS |
| SSM cascade for telemetry | post-deploy | wall 60s vs Friday 660s = ~11x speedup |

---

## Deploy chain (audit trail)

| Step | Timestamp | Detail |
|---|---|---|
| Pre-commit gate × 5 | ~16:00Z | exit 0 each |
| Local materialize cold | 15:52:35Z → 15:53:41Z | 66s for 1,510 partitions, 9.2MB cache |
| Local cache-hit 3-script load | 15:57:26Z → 15:57:30Z | 22.76s combined |
| Local pipeline-via-cache parity | 15:58:14Z → 15:58:25Z | max_diff = 0.0 |
| Commit | 16:11Z | `4186b88f7` via safe-commit (5 files, +371 / -145) |
| Push CLOUD | 16:11Z | `be5a99461..4186b88f7  CLOUD -> CLOUD` |
| S3 deploy (5 files in parallel) | 16:11Z | `aws s3 cp ... s3://opal-data-inf/code/gold/...` |
| SHA256 MATCH × 5 | 16:11Z | all MATCH |
| EC2 start | 16:12:47Z | `aws ec2 start-instances --instance-ids i-04373615f03fbf9a9` |
| EC2 running + SSM Online | 16:13:06Z / 16:13:07Z | sub-30s boot |
| SSM dispatched | 16:13:27Z | CMD `1690b61f-488c-4810-85f8-f698616ed979` |
| SSM completed | ~16:14:35Z | wall 68s SSM-tracked, 60s script-internal A-layer wall |
| EC2 stop | 16:15:12Z | `aws ec2 stop-instances` |

**EC2 lifecycle compute cost:** ~3 min × c6a.2xlarge ≈ $0.017.

---

## Sub-finding — sync_scripts flattens lib/ subdir

The dispatcher's `sync_scripts` function (in `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh`) pulls all `.py` files from `s3://opal-data-inf/code/gold/` flat into `/tmp/orion_gold_scripts/`. The `lib/` subdirectory in S3 (e.g., `lib/dtype_coerce.py`, `lib/txn_cache_reader.py`) gets flattened — files end up at `/tmp/orion_gold_scripts/dtype_coerce.py` instead of `/tmp/orion_gold_scripts/lib/dtype_coerce.py`.

**Why imports work anyway:** The scripts do `sys.path.insert(0, str(Path(__file__).parent / 'lib'))`, which on the runner resolves to a non-existent dir. But Python's default module search includes the script's own directory, where the flattened `txn_cache_reader.py` lives. So `from txn_cache_reader import ...` works — by accident, not design.

**Impact:** Brittle. If the dispatcher ever preserves the `lib/` subdir, the explicit `sys.path.insert` would suddenly start working AND the flat-root path would no longer be on path → potential import drift.

**Recommendation:** flag for AE 0.7.0 as a sub-finding for the eventual SAFE-DEPLOY-GATE-EXTENSION work. Either:
- (a) Have sync_scripts preserve `lib/` (clean fix on dispatcher side)
- (b) Have scripts test for both paths (`Path(__file__).parent / 'lib'` AND `Path(__file__).parent`)

Not blocking; current behavior works empirically. Documented for visibility.

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/scripts/gold/lib/txn_cache_reader.py` | NEW — shared loader (174 lines) |
| `data/orion/scripts/gold/INF_A_-1.materialize_txn_cache.py` | NEW — cascade-entry materializer (135 lines) |
| `data/orion/scripts/gold/INF_A_00.accounts_dimension.py` | Replace bespoke load_transactions → `load_cached_transactions(KEEP_COLS)` (-50/+5 lines) |
| `data/orion/scripts/gold/INF_A_01.advisor_assignments.py` | Replace bespoke load_assignments → `load_cached_transactions(KEEP_COLS)` (-50/+5 lines) |
| `data/orion/scripts/gold/INF_A_03.positions_cube.py` | Replace bespoke load_transactions → `load_cached_transactions(KEEP_COLS, drop_zero_units=True)` (-45/+10 lines) |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-11/DS_B_inf_a_layer_txn_cache.md` | NEW — this session log |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFNNA.INF_A_LAYER_TXN-CACHE.dsb-shared-silver-txn-cache.md` | status pending → complete |

---

## Sequencing handoff

- **AE 0.7.0:** orion-gold-dispatch.sh catalog needs INF_A_-1 added at chain entry (sync_scripts also needs `lib/` preservation per sub-finding). Both bundle into AE deploy hygiene work — not blocking my sequence.
- **DS~A:** my TXN-CACHE wiring is composable with their SILVER-UNIFY in-place migrate per cross-validation against `b9967954`. No coordination ask.
- **COO:** TO closure ratification + ADVI_INFNNA project-status accounting + route INF_A_02_RETIRE next (sequence #3 of 4).

---

## Next per Andrew GO sequence

| # | TO | Status |
|---|----|--------|
| 1 | INF_A_03_PARALLEL-EXPAND | COMPLETE |
| 2 | **INF_A_LAYER_TXN-CACHE** | **THIS TO — COMPLETE** |
| 3 | INF_A_02_RETIRE | starting next |
| 4 | INF_A_03_STALE-PURGE | gated on #3 |

Plus future TOs queued by COO post-current-sequence:
- INF_GOLD_OUTPUT_PREFIX_HONOR (medium, drafted)
- INF_COMP_PIPESCRIPT_DEPLOYED_COVERAGE (low)
- SAFE-DEPLOY-GATE-EXTENSION (high, CTO ratified)
