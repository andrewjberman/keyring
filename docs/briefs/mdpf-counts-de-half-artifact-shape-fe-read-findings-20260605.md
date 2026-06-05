# MDPF_COUNTS — DE-half investigation findings (artifact-shape + FE read)

**Author:** 0.4.0_DE_ClientPlatform~A (Andrew-named MDPF_COUNTS FE/serving + data-shape owner)
**Date:** 2026-06-05
**Mode:** Investigation-first, READ-ONLY (no fix). PRD: `docs/architecture/MDPF_COUNTS_PRD.md` v0.1.
**Pair:** 0.7.0_AE_CloudOps~A (producer/pipeline half).

## TL;DR — discrimination verdict

**NOT (a) FE field-map break. This is producer/rollup-side — (b)/(c).** The FE reads the
correct field name (`account_count`); the served data either lacks the key entirely (per-firm)
or stops populating it (Global). Two distinct mechanisms, matching Andrew's split symptom:

1. **Per-firm (49F + Inflection)** — served `json/mdpf/{firm}/aggregate-aua-timeseries.json`
   has the `account_count` key **ENTIRELY ABSENT** in current builds (0 occurrences). It was
   **PRESENT and current (to 2026-06-02)** in the 2026-06-02T17:13Z build (152KB) and was
   **dropped on the 2026-06-03 nightly rebuild** (→112KB, none) and every run since. The
   upstream daily partitions STILL carry real `account_count` → **the data exists upstream;
   the daily rollup/slice step drops it.** This is a **recent regression (6/03), NOT the
   original 5/15 split.**
2. **Global** — the Global view uses a SEPARATE legacy source `json/portfolios/aum-timeseries.json`
   (`getAUMTimeSeries`), not the per-firm slice. Its per-model `account_count` is present
   historically but **stops at 2026-05-15** (the split onset) — the legacy global timeseries
   stopped carrying per-model count post-split.

**Value is unaffected** — `model_value` / `model_aua` are present through 2026-06-05 in all
served slices. The bug is isolated to the count field. ✓

## Method — live-artifact pulls (bucket `opal-data-portal-v2`)

| Artifact | What I read |
|---|---|
| `json/mdpf/49financial/aggregate-aua-timeseries.json` | served per-firm (FE: `getMdpfAggregateAUATimeSeriesByFirm`) |
| `json/mdpf/inflection/aggregate-aua-timeseries.json` | served per-firm |
| `json/mdpf/global/aggregate-aua-timeseries.json` | per-firm "global" slice (NOT used by Global view — see below) |
| `json/portfolios/aum-timeseries.json` | legacy Global source (`getAUMTimeSeries`) |
| `platinum/mdpf/aggregate_aua/{2026-05-14,05-15,05-18,06-05}.json` | upstream daily partitions |
| S3 object-version history of the served 49F artifact | to pin the regression timing |

## Findings in detail

### 1. FE read (ModelPortfolios.tsx)
- The page has **two count paths**, both reading the field `account_count`:
  - **Per-firm** (`effectiveFirmId !== 'global'`, 49F/Inflection): `perFirmMdpfData` ←
    `getMdpfAggregateAUATimeSeriesByFirm`; count = `modelData.account_count?.[i] ?? 0`
    (line ~499). Chart consumes `periodData.account_count || 0` (lines ~1381 / ~1519).
  - **Global** (`effectiveFirmId === 'global'`): `rawTimeSeriesData` ← `getAUMTimeSeries`
    (legacy `portfolios/aum-timeseries.json`); count = each point's `account_count`.
- **The FE field name is correct in both paths.** The `?? 0` / `|| 0` fallback is exactly why
  a missing/unpopulated `account_count` renders as a flat-zero / empty chart — masking the
  producer gap as "empty" (this is the `?? 0` the PRD §2 called out).

### 2. Served per-firm artifacts (current, fresh 2026-06-05 11:03:48 ET)
- 49financial: 7 models, `model_value` → 2026-06-05; **`account_count` KEY ABSENT (grep: 0)**.
- inflection: 7 models, `model_value` → 2026-06-05; **`account_count` KEY ABSENT (grep: 0)**.
- global slice: no `by_model` at all (aggregate columns only — by design; not consumed by the
  Global view anyway).
- **Key is ABSENT, not renamed/nested → rules out (a) a FE field-map rename.**

### 3. Regression timing (S3 object versions of served 49F artifact)
- `2026-06-02T17:13:19Z` — **152,137 B, `account_count` PRESENT (7 models), populated to 2026-06-02.**
- `2026-06-03T15:03:51Z` — 112,615 B, `account_count` GONE.
- `2026-06-04`, `2026-06-05` — ~112–113 KB, `account_count` GONE.
- The 17:13Z good build is **1 minute after** commit `6de57eddc` (2026-06-02 13:12 EDT,
  `feat(ADVI_INFOTD.W2D): add per-model account_count[] series to MDPF aggregate-aua rollup`)
  → that build was the W2D dev/manual run of the new rollup code. The **automated nightly
  since 6/03 clobbered it with a no-count version.**

### 4. Upstream partitions DO carry count (AE boundary)
- `2026-06-05.json` (v0_9_1): 49F 7/7 models with real `account_count` (e.g. LTC=3038);
  Inflection 7/7 with real count (e.g. Intermediate=177).
- `2026-05-18.json` (v0_9_1, first post-split): 49F=2952, Inflection=159 — real.
- `2026-05-14`/`2026-05-15.json` (v0_8_ruling2, pre-split): `account_count` key present but
  **value = null**; Inflection had 0 models pre-split.
- **Producer alignment:** `mdpf_aggregate_aua.py` (gold daily) emits `account_count` per model
  (`int(mdf["account_id"].nunique())`, line ~325) → partitions are correct.
  `build_aggregate_aua_timeseries.py` (rollup) has the `account_count[]` code (commit
  `6de57eddc`, top of its log). **Both the partitions and the committed rollup code carry
  count — yet the served artifact does not.**

### 5. Global legacy source (`portfolios/aum-timeseries.json`)
- `account_count` present (2484 occurrences); aggregate points carry it through 2026-06-05.
- **Per-model `account_count` last-non-null = 2026-05-15 for every model** (Ultra Short-Term,
  Short-Term, Intermediate, …) → the legacy global per-model count stops at the split onset.

## Handoff to AE (producer/pipeline half)

1. **Per-firm regression (primary, fix first):** the nightly job that regenerates
   `json/mdpf/{firm}/aggregate-aua-timeseries.json` at ~11:03 ET is producing the **no-count**
   shape despite (i) partitions carrying `account_count` and (ii) the rollup code (`6de57eddc`)
   carrying the emit. **Pin which producer/copy the nightly actually runs** — `build_aggregate_aua_timeseries.py`
   is a `backfill/` script and is **NOT in the gold/silver deploy map** (`comp-pipescript deployed`
   returns no match), so the standard deploy-cycle didn't carry the W2D change to the scheduled
   runner. Classic deploy/run gap: committed + dev-run on 6/02, never redeployed to the nightly →
   6/03 nightly overwrote with the stale (no-count) producer. Confirm via the EventBridge/cron that
   fires the 11:03 rebuild + `comp-pipescript deployed` against the *actual* scheduled producer.
2. **Global legacy source (secondary):** `portfolios/aum-timeseries.json` per-model
   `account_count` stops at 5/15 — its producer stopped carrying per-model count post-split.
   Decide: backfill/restore on the legacy source, OR (cleaner) migrate the Global Model-Portfolios
   count to the MDPF per-firm 'global' slice once the per-firm rollup count is restored.

## Fix-direction (post-confirm; no fix yet)
- **(b)-flavored, per-firm:** restore `account_count` emission into the **nightly-run** rollup
  (deploy `6de57eddc`'s code to the scheduled producer / re-point the nightly at the updated
  rollup). No backfill of history needed — the rollup rebuilds the full series from partitions
  which already hold count; one corrected nightly run restores the whole 49F + Inflection series.
- **Global:** per §Handoff item 2.
- **No FE change required for the per-firm fix** (field name already correct). A Global-path FE
  edit would only be needed if we migrate Global off the legacy source — FLAG COO to sequence vs
  MDLP_DISTFIX's ModelPortfolios.tsx edit per PRD §6 (read-only investigation collided with nothing).
- **Cost discipline:** validate on the SCHEDULED nightly (no manufactured runs) — confirm on the
  6/06 nightly's served artifact + visual smoke on all 3 Count views at close (data-valid ≠ renders).

## Screenshot reconciliation (honest caveat)
Andrew's 2026-06-05 screenshots ("49F ends 5/15; Global empty; Inflection empty") are a
point-in-time/cached view whose exact per-view cutoffs don't perfectly match the current live
artifacts (the per-firm artifact regressed further between the screenshot and now — count-to-6/02
on the 6/02 build → count-absent on 6/03+). What is **ground-truth from live artifacts** is the two
mechanisms above. The "ends 5/15" cutoff is exactly the Global legacy source's per-model behavior;
"Inflection empty" matches the per-firm key-absent state. The precise screenshot temporal mapping is
not load-bearing for the fix — the producer-side root cause is established either way.
