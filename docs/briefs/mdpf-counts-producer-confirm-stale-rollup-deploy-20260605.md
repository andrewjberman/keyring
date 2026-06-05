# MDPF_COUNTS — AE producer/pipeline confirm: stale-deployed rollup (b) + unbuilt aggregate count (c)

**Agent:** 0.7.0_AE_CloudOps~A · **Date:** 2026-06-05 · **archetype:** DIAGNOSE
**Project:** MDPF_COUNTS (PRD docs/architecture/MDPF_COUNTS_PRD.md v0.1, JSON org/projects/MDPF_COUNTS.json)
**Scope:** AE-half confirm-tasks (PRD §4 / COO TO) — producer + pipeline + rollup + backfill. **Investigation-only, read-only, no fix.** Validated against LIVE served artifacts + the deployed S3 code copy (constraint C1 honored — NO manufactured/ad-hoc gold runs).

---

## Verdict — (b) + (c), discriminated at the producer

| Hypothesis | Status | Where |
|---|---|---|
| **(a)** FE count-field-map broke | **NOT the producer-side cause** (DE owns FE confirm) | — |
| **(b)** Backend stopped emitting `account_count` post-split | **CONFIRMED — but NOT in the code; in the DEPLOY.** The nightly Stage-4 rollup runs a **STALE deployed copy** that predates the `account_count` add. | deployed S3 rollup |
| **(c)** Aggregate ("Global") count rollup never built | **CONFIRMED — structural.** The `global` slice carries no `by_model`/`account_count` by construction; no aggregate-level count exists anywhere. | `slice_per_firm()` |

**One-line:** the partitions carry `account_count` (live region, both firms), the committed rollup carries it (since 6/2), **but the EC2 nightly runner executes a 6/01 pre-W2D copy of the rollup that has no `account_count` logic at all** → served artifact drops the field for every firm → FE `account_count?.[i] ?? 0` renders 0/empty everywhere. Global is additionally empty by construction (no aggregate count built).

---

## Evidence chain (all ground-truth)

**Lineage:** `mdpf_aggregate_aua.py` (partition `by_model[].account_count`) → `build_aggregate_aua_timeseries.py` (rollup per-model `account_count[]`) → `json/mdpf/{firm}/aggregate-aua-timeseries.json` → `ModelPortfolios.tsx` `account_count?.[i] ?? 0`.

1. **Partition producer emits count, always.** `mdpf_aggregate_aua.py:325` `"account_count": int(mdf["account_id"].nunique())` — present since script creation (`1757fe364`, MDPF_ASSETS.004, 2026-05-18). Never removed by the split.

2. **Live partitions DO carry real counts, both firms.** Raw `platinum/mdpf/aggregate_aua/{date}.json`:
   - `2026-06-05` 49financial `account_count=[3038,1580,1420,676,171,43,50]`; inflection `[177,143,70,23,12,24,7]`.
   - `2026-05-18` 49financial `[2952,1560,1421,656,169,43,51]`; inflection `[159,127,54,21,10,23,5]`.
   - `2026-05-15` (pre-split backfill) 49financial `[None×5]`; inflection `by_model=[]` (launched ~5/15, no history). → backfill region legitimately null; live region (5/18→now) is real.

3. **Committed rollup carries count, since 6/2.** `6de57eddc` (ADVI_INFOTD.W2D, 2026-06-02 13:12) adds the columnar `account_count[]` accumulate+pad in lockstep with `model_value` at all 3 pad sites. Local copy: **8** `account_count` refs.

4. **Served artifact has NO `account_count` key.** `json/mdpf/{49financial,inflection}/aggregate-aua-timeseries.json` (FRESH today, generated_at 2026-06-05T15:03:47Z): every `by_model` entry has keys `['cohort_class','display_name','model_value']` — **`account_count` absent**. `model_value` full (405 pts); count missing entirely.

5. **Smoking gun — the deployed rollup is stale.** `s3://opal-data-mdpf/code/scripts/backfill/build_aggregate_aua_timeseries.py` = **2026-06-01 14:20, 18491 B, 0 occurrences of `account_count`**. The W2D commit landed **2026-06-02 13:12** (local 20587 B, 8 refs). The runner pulls code from `s3://opal-data-mdpf/code/...` (RUNBOOK_AE_mdpf_daily_chain.md Stage 4) → it has been running pre-W2D code on every nightly since.

6. **Global is structurally count-less.** `slice_per_firm()` global slice (build_aggregate_aua_timeseries.py:347-353) spreads only `**artifact["aggregate"]` = `opal_aggregate_aua/model_aua/sma_aua/non_model_aua` — no `by_model`, no `account_count`. Served `global.json` confirms: only those 4 series, no count. **Even a fresh rollup deploy will NOT populate Global count** — an aggregate-level count rollup must be authored.

---

## THE SOLUTION (3 parts — NOT executed; investigation-first, lands as the fix-phase plan)

### Part 1 — (b) Live region 5/18→now: REDEPLOY the committed rollup. No new code, no backfill.
Re-upload the committed (6/2 `6de57eddc`) `build_aggregate_aua_timeseries.py` to `s3://opal-data-mdpf/code/scripts/backfill/` (the EC2 nightly runner pulls from there). The next **scheduled nightly** Stage-4 rollup re-reads every partition and emits `account_count[]` for **both** 49F + Inflection (5/18→now is real; the partitions already carry it). **Zero compute beyond the normal nightly; validate on the SCHEDULED run per C1 — NO manufactured run.** This alone restores 49F + Inflection live-region counts.

### Part 2 — (c) Global aggregate count: AUTHOR a PER-MODEL aggregate-union count in the global slice. New code.
`slice_per_firm()`'s global slice spreads only `**artifact["aggregate"]` — no `by_model`, no count. **FE-shape requirement (DE~A, confirmed):** the Global Count chart renders **per-model stacked** (same `modelData.account_count?.[i]` path as the firm views), so the global slice must carry a **`by_model` with per-model `account_count[]` summed cross-partner per CANONICAL `model_key`** (parallel to `model_value[]`) — a flat aggregate total alone would NOT feed the stacked chart (would force a separate FE product change). Implementation = group the per-firm `by_model` across partners by canonical `model_key`, per date sum `account_count` (an account is in exactly one firm → non-double-counting) and sum `model_value`; emit as `global.by_model[model_key] = {model_value[], account_count[]}`. **Cheap** (a cross-firm groupby on the already-built per-firm series; not expensive — confirmed back to DE). DE~A then re-points the FE Global branch `getAUMTimeSeries → getMdpfAggregateAUATimeSeriesByFirm('global')`, reading the same shape. Author + gate + deploy with Part 1.

### Part 3 — Backfill pre-5/18 49F (= pre-5/18 Global) count. TWO sources; the count history is NOT lost.
**Andrew-confirmed framing:** 49F holdings are **all SmartX**; **pre-5/18 Global == 49F** (Inflection hadn't onboarded), so backfilling 49F backfills historical Global too. Andrew's insight — *"we get holdings count from SmartX reliably every trading day; it's saved somewhere, we lost where in the global→firm-id migration"* — is exactly right: the count was **emitted daily into the legacy Global artifact** and is preserved.

**PRIMARY source (preferred — daily grain, already-computed, IS Andrew's chart):** the **legacy `json/portfolios/aum-timeseries.json` noncurrent S3 versions.** The bucket is versioned (144 versions back to 2026-03-05). The version at the ~5/15 cliff (e.g. vid `br4CMwG6jtdjwfdSO82DozELVIjUoCNX`, periods 2024-11-01→2026-05-14) carries **real DAILY per-model `account_count`** in its row-oriented `by_model` (`{period, aum, account_count}` per model) — e.g. Long-Term Conservative 869 (2024-11-01) → 3008 (2026-05-14); Intermediate 1049→1618; Ultra-Short from 2025-01-16. **Backfill = lift `account_count` from that noncurrent version, map legacy `display_name → canonical model_key`, inject into the historical 49F `by_model.account_count` for dates ≤5/14** (daily — no interpolation needed). The current served legacy file has `account_count: null` (the leg dropped at the migration); the data lives in the noncurrent versions.

**SECONDARY source (cross-validation + authoritative re-derive):** `s3://opal-data-smartx-v2/consolidated/smartx_allocations.parquet` — 98,477 rows, 8,950 account-level `AllocationId`, `ModelName`, `AllocationStatus`, monthly `Period` back to 202409. `account_count = nunique(AllocationId WHERE Open)` per `ModelName` per `PeriodEnd`. **Cross-validation:** allocations-derived 202605 `{ConsGrowth 3008, Int 1576, LTA 1419, ST 668, UST 169}` == legacy-version 5/14 `{LTC 3008, Int 1618(±), UST 191(±)}` and live 5/18 partition `[2952,1560,1421,656,169]` — all three agree within snapshot drift (LTC exact 3008 across legacy+allocations; UST exact 169 across allocations+partition). Use as the authoritative re-derive if the legacy noncurrent version is incomplete, or to fill any micro-gap.

- **Method note:** legacy daily ≤5/14 + live partitions ≥5/18; bridge the 5/15–5/17 micro-gap (3 trading days) from either source (step-carry the 5/14 value or pull allocations May). Integer counts — step-carry, never fractional-interpolate.
- **Caveats:** (1) the **2 SMA cohorts** (`opal_div_sma`/`opal_growth_sma`, live `43/51`) are NOT in the legacy by_model nor the allocations parquet → SMA count stays null pre-5/18 (separate cohort, launched ~5/18); (2) legacy model `display_name`s are pre-F5 (`Long-Term Conservative` etc.) → map to canonical `model_key` via `mdpf_model_registry.json`; (3) `HasDuplicate`/`DuplicateType` in the allocations parquet — dedup on `AllocationId`, ignore `value_conflict` double-count.
- **Inflection pre-5/18:** tracked via **Eclipse** (Orion portfolio accounting), not SmartX. Inflection launched ~5/15, so pre-5/18 is ~3 trading days of a brand-new book = immaterial; its count legitimately starts 5/18 (live `model_aua_positions`). If Andrew wants the 5/15–5/17 sliver, the source is Eclipse — flag as a small separate task, not on the critical path.

**Net:** Part 1 (deploy) + Part 2 (aggregate code) restore live + Global counts on the next nightly; Part 3 (SmartX-allocations backfill, validated) extends 49F + Global count history back to Sept 2024 at monthly→step-carried grain. SMA + Inflection pre-5/18 are the only legitimately-null regions.

## Coordination (PRD §6)
- DE~A owns the artifact-shape + FE-read half + reconciling the screenshot's "49F count ends 5/15" against the served shape. **Note for DE:** the CURRENT served artifact has NO `account_count` key for ANY firm (the stale rollup never wrote it) — so the screenshot's "49F count populated to 5/15" reflects an EARLIER served state (a prior partial/transient deploy), NOT the current artifact. DE confirm the FE Count read-key (`account_count?.[i]`) matches the post-fix shape (per-firm `by_model.account_count` + the new Global aggregate count).
- Producer fix (rollup redeploy + aggregate-count code + backfill) is AE; the only shared FE surface is the Count-toggle read in `ModelPortfolios.tsx` (distinct section from MDLP_DISTFIX histogram). No producer-artifact collision with MDLP_DISTFIX (`account_distribution.json` is a separate producer).
