# work-cycle 0017 — aum-metrics donut $1.71B root-cause (Inflection-blind non-model) + blend-split S3 deploy

**archetype:** DIAGNOSE **secondary:** DEPLOY, VALIDATE, COORDINATE
**Date:** 2026-06-05 ~1934-2005Z
**Trigger:** COO URGENT 193403Z + addenda (Andrew caught Global donut $1.71B should be $1.81B); Andrew-direct "talk to 0.4.0_DE"; COO cyc21 GO (blend-split deploy)

## A. Donut $1.71B root-cause — DATA correct in S3; FE-computed total was Inflection-blind on non-model leg
COO/Andrew framed it as a producer bug dropping Inflection base-model accounts from the Global union. VERIFIED FIRST (verify-before-execute): the producer artifacts are CORRECT and DO include Inflection.

Trace of the served donut (portal/src/pages/ModelPortfolios.tsx:670-674):
  Global Total AUA is FE-COMPUTED, NOT read from aum-metrics.total.aum:
    totalAUM(global) = modelAUM + nonModelData.latest.non_model_aum
    modelAUM = sum(aum-metrics.json by_model slices)  [Inflection PRESENT]
    nonModel = getNonModelAssets() -> /api/general/portfolios/non_model_assets.json

Root cause: PROD served a STALE, Inflection-blind non_model_assets.json (~$218M) -> donut = $1.492B + $218M = $1.71B. The model leg always had Inflection (INT 1757 = 49F 1580 + Inf 177; LTC 3108 = 49F 3038 + Inf 70). The NON-MODEL leg dropped Inflection's ~$91M. Older quarters (Q4'25/Q3'25) matched my fresh artifact EXACTLY (pre-Inflection era) -> only the current period was short = exactly Inflection.

ALL 4 S3 artifacts verified correct + fresh (2026-06-05):
- non_model_assets.json: non_model_aum $315,836,557.82, inflection_non_model_aua $90,875,859.89, enterprise_total $1,807,839,716.27 (THE fix)
- aum-metrics.json (19:08:57Z): total.aum $1.808B, by_model 7 slices incl Inflection
- account-distribution.json (19:08:55Z): 7,301 accts, $1.492B (both firms) -- bell curve already correct
- aggregate-aua-timeseries.json (19:08:56Z): by_model union correct
Donut identity: $1.492B + $315.8M = $1,807,839,716.27 == enterprise_total. EXACT.

DE (0.4.0) independently re-derived the identity (didn't trust summary) + confirmed. DEV build correct (Andrew-confirmed, DE visual smoke PASS both Count+Value toggles). The fix = fresh non_model_assets.json + DE's trendLastPoint freshen (253045ec) + count fix (62767be0).

CLOSE PATH for PROD: DT DEV->PROD promote (carries DE FE fixes) THEN my CF-flush (EVTSA9VEHNZVH /api/general/portfolios/* + /api/general/mdpf/*). ARMED -- holding flush until promote (pre-promote flush would re-cache against PROD FE lacking the count/trend fixes). Will loop DE post-flush for co-served-verify.

## B. Blend-split deploy (COO cyc21 GO) — DEPLOYED, run deferred to nightly per C1
DS's blend-split fix (c61a45a05) folds Global blend accounts into components (Andrew ruling: 1 holding per component). Deployed build_aggregate_aua_timeseries.py to s3://opal-data-mdpf/code/scripts/backfill/ -- byte-verified deployed==local (sha 9b36a8ef, _BLEND_GLOBAL_SPLIT present). Stale-deployed discipline: prior S3 copy was 3c31f8ea (no blend-split), confirmed stale before upload.
NO ad-hoc run (C1 + memory feedback_no_adhoc_gold_runs). Scheduled nightly ~06/06 11:03Z runs it. RAVC2 PARTIAL to COO: deploy verified; by_model shape (INT 1757->1923, LTC 3108->3251, ST 688->711, blend keys removed) confirms from nightly output.
Flagged: code folds blend model_value FULL-to-each-component but L180 comment says "50/50" -- wording mismatch for DS (Andrew 50/50-vs-full ruling pending).

## Lessons reinforced
- verify-before-execute: the "producer dropping Inflection base" framing was WRONG; producer correct, the gap was a stale Inflection-blind non-model leg in a SEPARATE artifact (non_model_assets.json) consumed by an FE-computed total. Same class as feedback_stale_artifact_check_for_newer_parallel_path_before_revive: one consumer still on a dead/stale source while siblings moved to MDPF.
- FE-computed aggregates: a served donut total may not equal any stored artifact field -- trace the FE computation (modelAUM + nonModel), not just the headline JSON.

## Compiler tools
sha256 byte-verify deployed-vs-local (x3), s3api list-object-versions + get-object --version-id (prior-version diff), s3api head-object (LastModified x3), portal FE source trace (Grep/Read ModelPortfolios.tsx + aum.ts + portal-proxy.ts), Invoke-RestMethod CDN probe (401 auth-gated confirm), aws s3 cp deploy.
