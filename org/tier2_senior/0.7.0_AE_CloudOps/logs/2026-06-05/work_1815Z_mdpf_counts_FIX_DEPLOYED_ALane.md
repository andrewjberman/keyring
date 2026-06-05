# MDPF_COUNTS — FIX BUILT + DEPLOYED (Parts 1+2+3) — AE~A

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE

---

## TAGS (record-keeping index)

- **project:** `MDPF_COUNTS`
- **macro:** `MDPF`
- **agent:** `0.7.0_AE_CloudOps~A` (dedicated ~A lane; base `0.7.0_AE_CloudOps` owns MDLP_DISTFIX — no overlap, see §Overlap-check)
- **authorization:** Andrew-direct GO 2026-06-05 ("GO now, do your recommended paths") — supersedes investigation-first hold
- **phase:** Phase 1 FIX (was Phase 0 INVESTIGATION)
- **commits:** `b25ed02a2` (fix: rollup + builder + backfill artifact) — on `origin/CLOUD`
- **prior-investigation-commits:** `5418ad8c0`, `4577529b5` (confirm briefs)
- **PRD:** `docs/architecture/MDPF_COUNTS_PRD.md` v0.1
- **JSON:** `org/projects/MDPF_COUNTS.json`
- **doc-of-record brief:** `docs/briefs/mdpf-counts-producer-confirm-stale-rollup-deploy-20260605.md`
- **root-cause:** (b) stale-deployed rollup + (c) Global structurally count-less
- **rules-applied:** Rule 12 (S3-artifact EC2 deploy), Rule 14 (ds-commit-gate), Rule 14a (safe-commit), Rule 15 (future-annotations), Rule 18 (HALTGT on push)
- **constraint:** C1 (no manufactured/ad-hoc gold run; validate on SCHEDULED nightly)
- **deploy-target:** `s3://opal-data-mdpf/code/scripts/backfill/` (mdpf-daily-runner `i-02448edb`)
- **nightly-chain:** `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:318` `run_step ROLLUP backfill/build_aggregate_aua_timeseries.py --upload`
- **backfill-source-version:** legacy `s3://opal-data-portal-v2/json/portfolios/aum-timeseries.json` noncurrent `VersionId=br4CMwG6jtdjwfdSO82DozELVIjUoCNX`
- **validation-status:** local `--out` PASS (no upload/SSM/c6i); production validation pending SCHEDULED nightly ~2026-06-06 11:03Z
- **coordination:** DE~A (FE re-point Part 4 + canonical-key seam); COO+CTO (RAVC2)

---

## §What the bug was (one line)

The nightly MDPF count rollup ran a **stale-deployed** copy of `build_aggregate_aua_timeseries.py` (S3 `2026-06-01`, pre-W2D `6de57eddc`, **0** `account_count` refs) → served `aggregate-aua-timeseries.json` dropped the `account_count` key for every firm → FE `account_count?.[i] ?? 0` rendered all Count toggles empty. Plus the `global` slice never carried a per-model count by construction.

## §What I changed (3 files, commit `b25ed02a2`)

### File 1 — `data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py` (MODIFIED)
- **Part 1 (redeploy):** the committed rollup already had `account_count` (`6de57eddc`); deploying this file past the stale `06-01` runner copy is the core fix. Deployed copy now has **20** `account_count` refs (was 0).
- **Part 2 (c) — `build_global_by_model()`** (NEW fn) + wired into `slice_per_firm()` global slice: emits a cross-partner-union `by_model` keyed by canonical `model_key`, with per-date `account_count[]` + `model_value[]` **summed across all firms** (an account is in exactly one firm → non-double-counting; `None` preserved where ALL firms null on a date). Additive — the existing aggregate-`$` spread (`opal_aggregate_aua`/`model_aua`/`sma_aua`/`non_model_aua`) the value chart reads is **untouched**. Satisfies DE~A's "Global Count renders per-model stacked" FE requirement.
- **Part 3 (backfill) — `load_count_backfill()` + `apply_count_backfill()`** (NEW fns) + wired into `build()`: loads the static backfill artifact (graceful-degrade — a missing artifact WARNs + continues, never breaks the nightly), and overlays pre-5/18 49F per-model `account_count` onto the assembled series **only where the partition value is `None`** (live ≥5/18 partition counts never overwritten). Global inherits the historical count automatically because the union (Part 2) sums the per-firm series after this overlay.

### File 2 — `data/mdpf/scripts/backfill/build_mdpf_count_backfill_pre0518.py` (NEW, one-shot builder)
Lifts the pre-5/18 49F daily per-model `account_count` from the legacy `aum-timeseries.json` noncurrent version (`vid br4CMwG6...`, periods 2024-11-01..2026-05-14), maps legacy `display_name → canonical model_key` (deterministic 5-row crosswalk, by duration), step-carries the `2026-05-14` value across the `5/15` trading day + `5/16-17` weekend to bridge to the `5/18` live start, writes the static artifact. NOT part of the nightly chain (one-shot, reproducible/audit).

### File 3 — `data/mdpf/scripts/backfill/aggregate_aua_count_backfill_pre0518.json` (NEW, generated artifact)
The static backfill data: `{firm_id:49financial, cutoff_date:2026-05-17, counts:{model_key:{date:count}}}` — 5 core models × 403 dates (2024-11-01..2026-05-17). Committed (durable regardless of S3 version retention) + deployed (the runner reads it via relative path).

## §Canonical-key seam (DE~A F5-rename requirement — honored)
The merged Global series spans a producer seam: legacy-daily ≤5/14 (pre-F5 `display_name` keys) + MDPF-aggregate ≥5/18 (canonical `model_key`). The backfill artifact is keyed by **canonical `model_key`**, and the rollup stamps the **current F5 `display_name`** from `mdpf_model_registry.json` for both halves → **one identity per model across the seam** → FE stacks one continuous series. No FE seam-normalization needed.

## §Validation (local `--out`, C1-safe — no upload/SSM/c6i)
Ran `python build_aggregate_aua_timeseries.py --out ... --out-per-firm-dir ...` (reads partitions from S3 read-only, writes local files):
- backfill loaded (49financial, cutoff 2026-05-17, 5 models); **470** pre-5/18 49F points overlaid (5 models × ~94 weekly-grid pre-5/18 dates).
- **49financial:** all 5 core models `account_count` populated for ALL 405 dates (2024-11-01..2026-06-05); SMA correctly live-only (14 dates ≥5/18); `model_value` unchanged.
- **inflection:** count live ≥5/18 (14 dates) — correct (launched 5/15; Eclipse-tracked pre-5/18 negligible).
- **global:** 9-model union; cross-partner sums verify arithmetically — LTC `3038(49F)+70(INF)=3108`, Intermediate `1580+177=1757`, Ultra-Short `171+7=178`.
- **aggregate-`$`** series intact (405/405 non-null) — value chart unaffected.

Cross-validation chain (from confirm phase): legacy `5/14` LTC=3008 == `smartx_allocations.parquet` 202605 == live `5/18` partition (within month-vs-daily drift; Ultra-Short 169 exact).

## §Deploy sequence (Rule 12 S3-artifact EC2 model)
1. `ds-commit-gate.sh` (Rule 14): py_compile + ds-precommit-check + ruff — all PASS (fixed: unused `os` import; renamed `FIRM_ID`→`BACKFILL_FIRM_ID` to clear a comp-constants name-collision with canonical `FIRM_ID='inflection'`).
2. `safe-commit.sh` (Rule 14a) → `b25ed02a2` (3 files, scoped pathspec). [stale `.git/*.lock` from May 5/27 caused one transient abort; retry clean.]
3. `git push origin CLOUD` → blocked by HALTGT pre-push checkpoint (Rule 18) on 5 routine pending messages (all this-session, already-processed, **none STOP/HALT-prefixed**) → re-pushed `HALT_ACK=1` → on `origin/CLOUD`.
4. `aws s3 cp` × 3 → `s3://opal-data-mdpf/code/scripts/backfill/` (rollup + builder + artifact).
5. **Verified deployed:** rollup now **20** `account_count` refs (was 0); all 3 files present (timestamps 14:16 EDT). Runner sync = full `aws s3 sync .../scripts/ $SCRIPTS_DIR/ --delete` (dispatch:125) → the JSON lands beside the script for the relative-path read.

## §What happens next (no manual run — C1)
Tonight's **SCHEDULED** nightly (~2026-06-06 11:03Z) runs the ROLLUP step against the updated code → uploads per-firm + global `aggregate-aua-timeseries.json` with `account_count`. **Validate on that run** (read served artifacts tomorrow): 49F + Inflection + Global Count toggles populated. NO manufactured run today (the c6i is not involved, but the rollup is gold-tier; C1 binds — validate on the scheduled cadence).

## §Overlap-check (Andrew-direct, pre-execution)
Confirmed base `0.7.0_AE_CloudOps` is on **MDLP_DISTFIX** (`data/smartx/scripts/compute_account_distribution.py` + `compute_per_firm_account_distribution.py` + `floored_percentiles.py` → `account_distribution.json`; deploy HELD on COO). DISJOINT from my files (`build_aggregate_aua_timeseries.py` + backfill artifact → `aggregate-aua-timeseries.json`). Different script, output artifact, producer. No file collision; my targets had no uncommitted changes. Coordinated via MCP (180907Z) + CC COO.

## §Remaining (not mine)
- **Part 4 — FE re-point (DE~A):** `getAUMTimeSeries → getMdpfAggregateAUATimeSeriesByFirm('global')` for the Global Count branch (reads the new `global.by_model.account_count`). COO sequences vs the MDLP_DISTFIX `ModelPortfolios.tsx` edit per PRD §6.
- **Visual smoke gate** on all 3 views' Count toggle at close (PRD §5; data-valid ≠ renders).
- **Closeout-verify** (CVO) post-nightly.

## §Compiler Tools
- `comp-pipescript deployed build_aggregate_aua_timeseries.py` → NO MATCH (coverage gap: only checks `s3://opal-data-bd/code/{gold,silver}/`, blind to `opal-data-mdpf` + `backfill/`). Substituted with direct `aws s3 cp ... | grep -c account_count` to verify deploy (20 refs). **Gap routed to CTO/COO** (govern note (i), elevated `172928Z`) for a comp-pipescript-deployed coverage widen.
- `ds-commit-gate.sh` (py_compile + ds-precommit-check + ruff + comp-constants) — ran 3×, final PASS.

## §RAVC
RAVC2 → COO + CTO (fix deployed, validates on scheduled nightly) — sent this turn. DE~A notified (global by_model shape live, seam honored). Heartbeat updated.
