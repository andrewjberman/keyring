# Briefing: Gold Pipeline — True Incremental Processing
**Date:** 2026-04-09
**Author:** 0.6.0_AE_PartnerETL
**Status:** Investigation needed — no work scheduled yet

---

## Current State (What We Actually Have)

The pipeline has two named modes — `incremental` and `full` — but they are functionally identical for almost every script.

`run_gold_layer.sh incremental` → `gold_dispatch.sh --chain full --incremental`

The `--incremental` flag is stripped from all scripts except **A_00** (accounts_dimension) and **C_06** (client_mix_timeseries) inside `gold_dispatch.sh`. Every other script — all of Groups B, C (except C_06), and D — runs a full recompute regardless of whether the nightly or monthly trigger fired.

Additionally, **B_00** (canonical_holdings) has its own sealed-date watermark system, but its catalog entry hardcodes `--force`, which overrides the sealing on every run. The mechanism exists but is disabled by default.

**Observed evidence:** Today's three gold runs (all labeled `incremental`) each took 63-69 minutes. If any meaningful watermarking were in effect, later runs would be shorter. They were all the same duration, which is consistent with full reprocessing on every run.

The monthly "full rebuild" (`cron(0 8 1 * ?)`) invokes `--chain rebuild`, which is defined as an alias for `--chain full`. There is no behavioral difference between nightly and monthly runs.

---

## What True Incremental Should Look Like

The gold pipeline has a clear dependency DAG. A properly incremental run only reprocesses dates where upstream data changed since the last run. The patterns break down by group:

### Group A — Dimension tables (A_00 through A_04)

**A_00** already has watermark logic — reads only new transaction files since `_last_txn_file_date`. This is the correct pattern. A_01 through A_04 (advisor assignments, fee rate history, positions cube, client dimension) have no incremental logic at all and do full rebuilds every night even though these tables are mostly stable.

**What's needed:** Watermark-gate A_01 through A_04 on their upstream file dates. These tables change infrequently (advisor reassignments, fee schedule changes) — reprocessing them nightly is pure waste.

### Group B — Holdings stack (B_00, B_01, B_02, B_03)

**B_01** (holdings_lots) is inherently daily — it builds a snapshot for today's date. It's already correct. No incremental needed.

**B_00** (canonical_holdings) has a sealing system that works correctly but is neutralized by `--force` in the catalog. The intent was right: sealed dates don't need to be reprocessed. Removing `--force` from the default catalog flags and letting the watermark do its job would make B_00 skip all historical dates on nightly runs.

**B_02** (canonical_lots) and **B_03** (account_gains) process all dates from B_00/B_01 output. They need start-date filtering tied to B_00's watermark — process only dates where holdings changed.

### Group C — Performance and analytics (C_00 through C_08)

Most C scripts process the full date range on every run. **C_00** (canonical_performance), **C_01** (canonical_nna), **C_02** (client_performance), **C_03** (account_performance) are the most expensive and have no watermarking at all.

**What's needed:** A shared watermark file (e.g., `gold/manifests/chain_watermark.json`) that tracks the last fully processed date for each script independently. Each script reads this on startup and skips dates already processed. On nightly runs, only process yesterday and today.

**C_06** (client_mix_timeseries) already has working watermark logic — use it as the reference implementation for the others.

### Group D — Portal publishers (D_00 through D_04)

D scripts are aggregation + S3 publish steps. Most read from C outputs and produce JSON artifacts for the portal. They run fast relative to C but still do full rebuilds.

**D_01** (partner_analytics) and **D_02** (advisor_client_detail) load multiple years of account_performance.parquet (6M+ rows in today's logs) on every run. These should be gated on the C_03 watermark — only rerun if C_03 produced new dates.

**D_00/D_00b/D_00c** (aggregates, timeseries, leaderboard) are genuinely time-sensitive and should always run. No incremental gate needed here.

---

## The Right Architecture

A proper incremental run should:

1. **Check upstream watermarks before running each script.** If the script's upstream inputs haven't changed since the last successful run, skip it entirely.

2. **Use a single shared watermark file** (`gold/manifests/chain_watermark.json`) with per-script entries. Each script reads and writes its own entry. Scripts that depend on other scripts use the upstream entry to decide whether to run.

3. **Never use `--force` as a default flag.** Force should be an explicit operator override, not the default behavior.

4. **Separate date-range reprocessing from full rebuilds.** Nightly incremental = process new dates only. Monthly full = reprocess all dates from inception. These are different operations and should use different code paths.

5. **Make the distinction observable.** The current logs don't distinguish whether a script actually processed new data or skipped. Watermark-gated scripts should log clearly: `SKIP: no new dates since 2026-04-08` or `PROCESS: 1 new date (2026-04-09)`.

---

## Why This Matters

**Cost:** The gold runner is a `c6i.16xlarge` (~$2.75/hr on-demand). Each run today took ~65 minutes. Three runs = ~$8-9 today. If nightly runs were truly incremental (processing one new date instead of the full history), they should complete in 10-15 minutes rather than 65. That's a 4-5x cost reduction on compute, plus proportional reduction in data transfer and S3 API calls.

**Stability:** Shorter runs mean less exposure time. The IAM/pending-marker bug we fixed today caused the machine to stay up for 2+ hours. With 10-minute runs, the blast radius of any similar failure is much smaller.

**Data correctness:** The current model recomputes everything on every run, which means errors introduced by schema changes or bad upstream data propagate into the full history on the next nightly run. True incremental means historical dates are sealed and stable — you know exactly what changed and when.

---

## What We Don't Know Yet

- Whether removing `--force` from B_00 immediately breaks anything (it might, if downstream scripts depend on full regeneration).
- Whether the C script watermark approach is feasible without significant refactoring — some C scripts have complex cross-date dependencies (e.g., C_00 does t-1 lookbacks).
- Whether A_01 through A_04 are safe to watermark — advisor assignments and fee histories can change retroactively, which might require reprocessing historical dates even on a "nightly" run.
- The actual breakdown of where the 65 minutes goes. We need a per-script timing profile from a production run before designing watermarks.

---

## Recommended Next Steps

1. **Profile first.** Pull a production run log, extract per-script timings, rank by cost. Focus watermarking effort on the top 3-4 most expensive scripts. Don't optimize everything at once.

2. **Remove `--force` from B_00's catalog default.** This is a one-line change with immediate impact. B_00's sealing mechanism is already built and tested — just stop disabling it. Verify output correctness before deploying.

3. **Design the shared watermark spec.** What does `chain_watermark.json` look like? What's the schema? How do scripts handle a missing watermark (first run fallback)? This is a DS + AE design task.

4. **Implement one C script as a prototype.** C_07 (advisor_attribution) or C_08 (advisor_fee_efficiency) are good candidates — important but self-contained, not depended on by other C scripts. Implement watermark there, verify behavior, then roll out.

5. **Add a `--dry-run-incremental` flag** that shows what each script WOULD skip without actually skipping it. Useful for validating watermark logic before trusting it in production.

**Owner:** DS (watermark design, script-level changes) + AE (dispatch changes, manifest schema, deployment). CTO to approve design before implementation.

---

## Files Relevant to This Work

| File | Relevance |
|------|-----------|
| `data/black_diamond/scripts/gold/gold_dispatch.sh` | Chain definitions, `--incremental` stripping logic, catalog |
| `data/black_diamond/scripts/gold/run_gold_layer.sh` | Mode translation (incremental → dispatch flags) |
| `data/black_diamond/scripts/gold/A_00.accounts_dimension.py` | Reference watermark implementation |
| `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py` | Reference watermark implementation |
| `data/black_diamond/scripts/gold/B_00.canonical_holdings.py` | Has sealing but neutralized by --force |
| `infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh` | Outer EC2 runner, mode passing |
| `infra/aws/terraform/bd-pipeline/eventbridge.tf` | Trigger schedules (nightly, monthly) |
