# Session log — 0.4.0_DE_ClientPlatform~A — MDPF_COUNTS — 2026-06-05T18:06Z

**Lane:** ~A (dedicated MDPF_COUNTS lane; base 0.4.0_DE owns MDLP_DISTFIX on the overlapping
MDPF-timeseries/ModelPortfolios surface — ~A prevents split-brain per PRD §6).
**Project:** MDPF_COUNTS (Andrew-direct, PRD v0.1 APPROVED 46e7f5285). DE-half = artifact-shape + FE read.
**Mode:** Investigation-first / read-only → design coordination. No fix shipped (gated).

## Outcome (one line)
DE-half investigation COMPLETE + COO-ACCEPTED; root cause discriminated to producer-side (b)/(c) and
dated; both halves now fully designed at the producer↔FE boundary; my FE re-point is GO but
sequenced-gated on AE~A's rollup landing + COO's sequencing ping. No blocker.

## Startup
- `/watcher`: registered LIVE (`0.4.0_DE_ClientPlatform~A`, PID 5468), persistent inbox Monitor armed
  (task `bqbrt06uh`). Picked up the COO investigation TO + an informational AE ADVI_49PUSH RAVC-close.
- Armed `/work` 20m cron (738dda6e) — later RETIRED this session per LD-0157 (workers now event-driven
  via the Monitor; COO /drive is the centralized tick driver).

## Investigation (DE-half §4 confirm-tasks) — verdict + evidence
**VERDICT: NOT (a) FE field-map break. Producer/rollup-side — (b)/(c). TWO distinct mechanisms.**

1. **Per-firm (49F + Inflection):** served `json/mdpf/{firm}/aggregate-aua-timeseries.json` has
   `account_count` KEY ENTIRELY ABSENT (grep 0) in current 6/03+ nightly builds; `model_value` present
   to 6/05 (**Value unaffected**, confirmed). S3 object-versions PIN the regression: the 6/02T17:13Z
   build (152KB) HAD `account_count` to 6/02 — the ADVI_INFOTD.W2D dev run, **1 min after commit
   `6de57eddc`** (2026-06-02 13:12 EDT "add per-model account_count[] to rollup"). The 6/03 nightly
   clobbered it to the no-count 112KB shape; every run since the same. **Upstream partitions STILL carry
   real `account_count`** (6/05 partition v0_9_1: 49F LTC=3038, Inflection Intermediate=177). →
   **DATA EXISTS UPSTREAM; the nightly rollup drops it.** Root cause = DEPLOY/RUN GAP: the rollup
   `build_aggregate_aua_timeseries.py` is a `backfill/` script, NOT in the gold/silver deploy map, so the
   W2D `account_count` change never reached the scheduled nightly producer. RECENT 6/03 regression, not
   the original 5/15 split (this CORRECTED the PRD's "onset = 5/15 split" framing for the per-firm half).
2. **Global:** the Global view uses a SEPARATE legacy source `portfolios/aum-timeseries.json`
   (`getAUMTimeSeries`), not the per-firm slice. Its per-model `account_count` stops at 2026-05-15.

FE confirm: reads the correct field name (`account_count`) in BOTH paths; the `?? 0` / `|| 0` fallback is
what masks the producer gap as an empty chart. No FE field-map break.

## Deliverables
- Brief: `docs/briefs/mdpf-counts-de-half-artifact-shape-fe-read-findings-20260605.md` (commit `86d77d8f5`).
- RAVC2 → COO + CTO (accepted; COO called the S3-version pinning "decisive").

## Coordination arc (artifact↔producer boundary with 0.7.0_AE_CloudOps~A)
- **AE~A corroborated byte-for-byte** (brief `5418ad8c0`): pinned the exact mechanism — the EC2 nightly
  (`mdpf-daily-dispatch.sh` on i-02448edb) syncs the rollup from
  `s3://opal-data-mdpf/code/scripts/backfill/build_aggregate_aua_timeseries.py`, and that S3 copy is
  dated 2026-06-01 14:20 (pre-W2D, 0 `account_count` refs) vs the committed 8 refs. My "comp NO MATCH"
  was a bucket-coverage gap (comp checks opal-data-bd only, not opal-data-mdpf) — resolved.
- **Pre-5/18 backfill:** AE~A found + validated `s3://opal-data-smartx-v2/consolidated/smartx_allocations.parquet`
  (nunique(AllocationId WHERE Open) per ModelName per Period, step-carried, validated Ultra-Short=169) →
  restores pre-5/18 NULL-count history that a redeploy alone leaves null.
- **FE-shape requirement (my lane, decisive):** the `global` slice currently has no `by_model`/`account_count`,
  but the Global Count chart renders PER-MODEL STACKED → migrate-Global needs per-model **aggregate-union**
  `account_count` in the rollup (not a flat total). AE~A accepted + folded in (brief `4577529b5`): global
  `by_model[canonical model_key] = {model_value[], account_count[]}` cross-partner-summed. Cheap (single-firm
  accounts → clean sum).
- **F5 seam catch (my lane):** the merged Global series spans a producer seam — legacy-daily history ≤5/14
  (pre-F5 display_names) + MDPF-aggregate ≥5/18 (canonical model_key, F5-renamed). Flagged the
  two-non-stacking-legend-entries risk. AE~A CONFIRMED single-canonical-identity emission across the full
  range (legacy history re-keyed via a deterministic 5-row crosswalk + current F5 display_names) → **zero FE
  seam-normalization needed.**

## Decision
**Andrew ruled MIGRATE-Global** (not restore-legacy), shaped by my FE-shape constraint (COO relay). My Global
FE re-point (`getAUMTimeSeries` → `getMdpfAggregateAUATimeSeriesByFirm('global')`, same `account_count?.[i]`)
is GO. COO sequences my `ModelPortfolios.tsx` Global-branch edit vs the DISTFIX edit. Per-firm half needs no FE edit.

## Current state (IDLE-STANDBY, no action owed to me)
- **Gate CLOSED** (confirmed by artifact): global slice unchanged (15:03:48Z/37945B) — AE~A's rollup shape
  not yet landed (lands on the next scheduled nightly ~6/06 per cost-discipline; no manufactured runs).
- **Waiting on:** (1) AE~A's per-model-union rollup shipping + (2) COO's sequencing ping.
- **Ready:** FE re-point read-only scoped — serving fn + type (`MdpfPerFirmTimeSeries.by_model`) already
  shape-ready; edit re-points the Global COUNT path only (Value stays on its source = low blast radius);
  zero seam-handling (producer-clean). Visual-smoke all 3 Count views at close.

## LD-0157 alignment
Retired the `/work` 20m cron (738dda6e). Reachability = persistent Monitor; work = event-driven on
Monitor-delivered dispatches; broker status kept accurate (IDLE-STANDBY) so COO's /fabric-check classifies me.

## Commits this session
- `86d77d8f5` — DE-half findings brief (under ~A serial author line).
