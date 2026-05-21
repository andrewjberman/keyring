# DS~B Session Log -- MDPF emitter hotfix (5-21 2a-drop / blend / vintage)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-21
**Branch:** CLOUD
**Dispatch:** Andrew-direct (COO~B closed). Validator: 1.0.0_SA_CTO~B.

## Summary

Three-phase hotfix to `data/mdpf/scripts/backfill/build_legacy_compat_emit.py`.
Fixed a fake ~$95M chart cliff on 2026-05-21, verified the blend-fold is
correct, stated the Inflection-onset vintage. Deployed + live +
Andrew-confirmed.

## Phases

- **A (the cliff) -- FIXED.** The emitter gated Inflection inclusion on the
  `gold/eclipse/{date}/` S3 listing (`inf_dates`). Eclipse gold lags ~1 day;
  `gold/eclipse/2026-05-21` did not exist, so the gate zeroed Inflection's
  $93.08M 2a even though the 5-21 platinum partition carried it. Since
  MDPF_ASSETS.030 the emitter sources Inflection from the platinum partition
  (`derive_inflection_from_platinum`, self-guarding), so the gate was stale +
  harmful. Removed at all 4 sites. 5-21: $1,347,808,273.25 ->
  $1,440,892,723.72 (Model line); enterprise_total $1,651,107,904.20 ->
  $1,744,192,354.67.
- **B (blend fold) -- verified ALREADY CORRECT, no code change.** The emitter
  splits the 50/50 blends into pure-model components (`BLEND_SPLIT`). Verified:
  2026-05-21 Intermediate Inflection contribution $69.67M = split arithmetic,
  not $82.74M wholesale. Andrew's wholesale-into-INT observation was the
  pre-hotfix stale portal view (5-21 with Inflection zeroed); Andrew confirmed
  the portal renders correctly after the --upload + refresh.
- **C (vintage) -- stated.** 2026-05-18 onset = same-day (T-0): the platinum
  5-18 inflection block reconciles to `gold/eclipse/2026-05-18` to the cent.
  Absent pre-5-18 = platinum-tier availability boundary, not a T-1 lag.
  Recorded in `meta.inflection_onset` of both emitted files.

## Deploy

| Step | Detail |
|------|--------|
| Commit | d461414d9 (emitter + brief), origin/CLOUD |
| Daily-chain deploy | `aws s3 cp` -> s3://opal-data-mdpf/code/scripts/backfill/build_legacy_compat_emit.py -- sha256 MATCH local; the mdpf-daily-dispatch.sh Stage 3.5 S3-syncs from there |
| Live emit | `build_legacy_compat_emit.py --upload` -> aum-timeseries.json + non_model_assets.json corrected |
| Regression guard | new vs pre-overwrite backup: ONLY 2026-05-21 changed; 0 pre-2026-05-18 points changed; 0 spurious Inflection on pre-onset dates |

## Compiler Tools

| Tool | Result |
|------|--------|
| ds-commit-gate.sh | clean -- py_compile + ds-precommit-check (AST) + ruff, 1 file |
| comp-pipescript deployed | N/A -- scoped to s3://opal-data-bd/code/{gold,silver}; the MDPF emitter deploys to s3://opal-data-mdpf/code/scripts/backfill/. Verified instead by direct sha256 compare (S3 copy == local repo) |

## RAVC

RAVC2 -> CTO~B (COO~B closed); output-validation ACCEPT all 3 phases.
RAVC2-close -> CTO~B. Andrew confirmed the portal renders correctly. Phase B
resolved (pre-hotfix stale view). MDPF_ASSETS re-closes.

## Current State

Hotfix COMPLETE -- deployed, live, Andrew-confirmed, regression-clean.
Brief: `docs/briefs/mdpf-emitter-hotfix-2a-drop-blend-vintage-20260521.md`.

## Next

| Item | Detail |
|------|--------|
| Regression-check | Tomorrow 2026-05-22, after the ~14:00 UTC mdpf-daily chain run: confirm the 5-22 emit includes Inflection (no cliff) -- the fixed emitter is S3-deployed so the chain picks it up. |
