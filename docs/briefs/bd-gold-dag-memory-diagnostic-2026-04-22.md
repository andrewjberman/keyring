# Brief: BD Gold Parallel-DAG Memory + Correctness Diagnostic

**Date:** 2026-04-22
**Author:** 0.4.0_DS_ClientPlatform
**Follow-on to:** `docs/briefs/bd-b-chain-dispatch-ordering-fix-2026-04-22.md` (DT 0.4.0)
**Status:** Diagnostic complete. Fix drafted. Dispatching under time pressure.

---

## Executive Summary

DT's 2026-04-22 fix (commit `c610630b`) corrected `CHAIN_CANONICAL` / `CHAIN_FULL`
but those variables are ONLY consumed by the **sequential** `run_chain` path
(i.e. `--chain canonical`). The nightly `--chain full` path (and `--chain bcd`)
is routed to `run_chain_parallel` at `gold_dispatch.sh:885`, which drives a
14-phase DAG whose B-group phases DT's fix did NOT touch.

The parallel DAG has two problems that have been compounding into the
OOM / slow-B regime observed over the past week:

1. **Correctness:** `PHASE_B1` runs `B_00 || B_01` concurrently. `B_01`'s HLOT2
   reopen/topup logic reads `gold/canonical/holdings/{today}.parquet` (written
   by B_00), wrapped in `try/except` that silently degrades on failure. Because
   B_01 launches at the same moment as B_00, `{today}.parquet` is not yet
   present on S3 when B_01 reaches the read — so `B_01` silently falls back
   to the empty path, losing HLOT2 reopen coverage for every nightly run.

2. **Memory pressure / wall-clock loss:** `PHASE_B1` concurrency stacks the
   two highest-RAM scripts in the chain. Measured summed-RSS peaks (from
   `perf_report.json` on S3, `gold_prof.py` D1 instrumentation):

   | Date | Script (concurrent) | wall_s | mem_peak_mb (summed RSS) |
   |------|---------------------|-------:|-------------------------:|
   | 2026-04-17 nightly | B_00 (PHASE_B1) | 200.1 | 775,629 |
   | 2026-04-17 nightly | B_01 (PHASE_B1) | **549.4** | 537,953 |
   | 2026-04-18 nightly | B_00 (PHASE_B1) | 200.8 | 805,141 |
   | 2026-04-18 nightly | B_01 (PHASE_B1) | **542.7** | 576,918 |
   | 2026-04-17 QA | B_01 isolated (`single:B_01`) | **117.2** | 529,215 |
   | 2026-04-17 QA | B_01 PHASE_B1 concurrent (crash) | 1385.6 | 530,586 |

   B_01 takes **4.6x longer** concurrent with B_00 than isolated
   (542s vs 117s). CPU during concurrent B_01 averages 2.3% — it's not doing
   work, it's waiting on I/O contention and paging pressure from B_00's
   forked worker pool.

   The 2026-04-17 QA `--chain bcd` run ALSO failed outright in PHASE_B1:
   `B_01` tripped SAFETY_HALT (1,169 accounts > limit 200, pre-close MV $182M)
   — this is the stale-canonical-read failure mode in production: `B_01` saw
   yesterday's canonical_holdings, today's allocations, and the mismatch
   blew past the safety threshold.

---

## Dependency Ground Truth (from comp-pipescript io)

```
B_00   reads:  positions_cube, Schwab RPS, silver/unrealized, silver/realized,
               canonical_prices, accounts_dimension, schwab_bd_account_mapping
       writes: gold/canonical/holdings/{date}.parquet

B_01   reads:  accounts_dimension, silver/bd_assets_dim, silver/transactions,
               (DYNAMIC) gold/canonical/holdings/{date}.parquet  <-- B_00 output
       writes: gold/timeseries/holdings_lots/{date}.parquet

B_01b  reads:  B_01 holdings_lots output (scans for new ticker/asset_name pairs)
       writes: DynamoDB bd-securities table
       (per docstring: "Runs between B_01 and B_02 in the gold dispatch chain.")

B_02   reads:  canonical_holdings (from B_00), silver uln/rld/ult, canonical_prices,
               DynamoDB bd-securities (populated by B_01b)
       writes: canonical/lots_realized, canonical/lots_unrealized

B_03   reads:  canonical_holdings (B_00), canonical_lots_realized/unrealized (B_02)
       writes: canonical/account_gains -> C_00, C_01, C_02

C_05   reads:  canonical_lots_unrealized (B_02), holdings_lots (B_01)
       writes: client_tax_liability.parquet -> D_00, D_02
```

Note: `comp-pipescript io B_01` does NOT show `canonical/holdings` as a read
because the read is constructed at runtime (`canonical_key = f'.../{date}.parquet'`)
inside a try/except. Static analysis misses it. This is WHY the backwards
dependency comment at `bd-v2.24.2` survived — the standard tool doesn't
catch this dependency class.

**Strict sequential order required:** `B_00 → B_01 → B_01b → B_02 → B_03`.
No safe parallelism exists within this sub-chain. `B_03 || C_05` pairing
after B_02 is safe (both read already-written artifacts; C_05 is trivial
memory at 1,373 MB).

---

## Proposed DAG (PHASE_B1 through PHASE_B5)

```bash
echo "--- PHASE_B1: B_00 ---"                     # ~200s, peak ~800 GB summed RSS
run_background B_00
wait_phase PHASE_B1

echo "--- PHASE_B2: B_01 ---"                     # ~117s isolated, ~530 GB peak
run_background B_01
wait_phase PHASE_B2

echo "--- PHASE_B3: B_01b ---"                    # ~1s, trivial memory
run_background B_01b
wait_phase PHASE_B3

echo "--- PHASE_B4: B_02 ---"                     # ~125s, ~1375 GB peak
run_background B_02
wait_phase PHASE_B4

echo "--- PHASE_B5: B_03 || C_05 ---"             # ~119s, ~1452 GB peak (unchanged)
run_background B_03; run_background C_05
wait_phase PHASE_B5
```

**Wall-clock comparison (B-group only, measured 2026-04-18 nightly):**

| Layout | PHASE_B1 | PHASE_B2 | PHASE_B3 | PHASE_B4 | PHASE_B5 | Total B |
|--------|---------:|---------:|---------:|---------:|---------:|--------:|
| Current (concurrent, broken) | 544s | 127s | — | — | 119s | **790s** |
| Proposed (serialized monsters) | 200s | 117s | 1s | 125s | 119s | **562s** |

**Savings: 228s (29%)** — plus eliminates the silent HLOT2 read-stale bug
AND eliminates the SAFETY_HALT failure class that hit 2026-04-17.

Peak summed-RSS per phase is never worse than current worst phase
(PHASE_B5 B_03 at 1,452 GB, unchanged).

---

## Why This DAG Is Safe vs. The More Aggressive Alternative

`B_01` and `B_02` both depend only on `B_00` (not on each other). An
aggressive layout could run `B_01 || B_02` to save another ~117s. **I did
not take that path** because summed-RSS would jump from 1,375 GB (current
PHASE_B2 B_02 alone) to ~1,950 GB (B_01 + B_02 concurrent), and B_01b must
run between them per the strict `B_00 → B_01 → B_01b → B_02` order anyway.
The safe layout gives 29% savings on its own without stacking new memory
risk; aggressive parallelism can be evaluated after the safe layout
stabilizes and we have more perf_report history.

---

## Other DAG Observations (Not Fixed In This Brief)

These are worth reviewing separately but are **not** part of the urgent fix:

- **PHASE_B5 (B_03 || C_05):** C_05 only takes ~10s and uses <2 GB. B_03
  dominates at 1,452 GB. The concurrency saves ~10s. Could flatten if
  B_03's memory profile grows further, but currently safe.
- **PHASE_C1 (C_00 || C_01):** C_01 peaks at ~440 GB, C_00 at ~7 GB.
  Safe pairing.
- **PHASE_D1 (D_00 || D_00c || D_03):** Gated on `gold/validation/aua_certification/`.
  Fine.
- **PHASE_D2 (D_00b || D_01):** Gated on `gold/canonical/role_aua/`. Fine.

---

## Recommended Follow-On Work (after tonight's run)

1. **Add boto3 `s3_reads` / `s3_writes` counts to `gold_prof.py`.** Currently
   both fields are `null`. Would let us classify bottleneck type more
   precisely.
2. **RSS vs. USS for memory metric.** `memory_info().rss` summed across CoW
   forked workers overstates physical memory usage. Switching to USS
   (unique set size) would give a clearer picture of true pressure.
3. **Add dependency edges to `gold_pipeline_deps.yaml`.** The file today
   only declares post-steps + preconditions — no inter-script edges.
   The DAG is implicit in `gold_dispatch.sh`. Making it declarative would
   let comp-pipescript validate the dispatcher against declared deps.
4. **Static scan for dynamic S3 reads.** The B_01 → B_00 dependency was
   invisible to comp-pipescript because the S3 key is f-string-constructed
   inside a try/except. A pre-commit scan that flags `f'.../{var}.parquet'`
   patterns inside gold scripts would catch this class.

---

## Evidence Files

- `perf_report.json` (S3): `s3://opal-data-bd/gold/perf_report.json`
- `perf_report_qa_bcd_2026-04-17.json` (S3): `s3://opal-data-bd/gold/perf_report_qa_bcd_2026-04-17.json`
- `perf_report_qa_2026-04-17_single_b01.json` (S3): isolated-B_01 baseline
- Nightly logs: `s3://opal-data-bd/gold/logs/chain_full_20260418_040055.log`, `chain_full_20260417_220409.log`
- DT's initial brief: `docs/briefs/bd-b-chain-dispatch-ordering-fix-2026-04-22.md`
- PRD: `docs/architecture/GOLD_PERF_PRD.md`
