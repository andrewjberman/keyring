# work-cycle 0009 — EXPEDITED yield-curve clobber-fix deploy (live FE breakage)

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE
**Date:** 2026-06-05 ~1539-1552Z
**Trigger:** CTO [DEPLOY] expedited — Andrew-escalated Macro page yield-curve 1Y-ago line missing 1Y node

## The fix (DS-authored, CTO-GO'd 06-01, stranded 4 days)
yield_curve_fred.json partial-overwrite clobber: US Treasury 1Y = 0 obs while 9 others = 498, old code (fae806585) still clobbering. Fix = fetch_series retry+backoff(3x) + run() merge-preserve no-regression guard (carry forward prior tenors empty-after-retry; 1Y-ago = immutable historical = zero fabrication) + preserved_tenors metadata. In my lane (infra/aws/lambda = AE); DS couldn't push.

## Found it STAGED, not lost
Session-start showed it unstaged-M; this tick git diff empty -> investigated -> it was STAGED (CTO's blocked DS-author commit attempt left it git-add'd). Fix present (merge-preserve markers), HEAD still old fae806585. Committed under AE author (38c45d108, 98+/33-, cites DS authorship + CTO-GO + Andrew escalation). ds-commit-gate clean.

## IAM GAP CAUGHT (brief assumed present, was ABSENT)
The merge-preserve guard READS yield_curve_fred.json (GetObject). FredIngestionLambdaRole (the real role; NOT FredMacroIngestionLambdaRole = separate macro lambda) had PutObject on that key but NO GetObject -> would AccessDenied at runtime. Added s3:GetObject to the yield-curve-artifact-write inline policy via fred-pipeline/iam.tf (same single key). This is exactly why the IAM pre-check is a deploy step.

## Deploy (Option Y zip-swap)
Downloaded deployed zip (195 entries) -> python-zipfile swap of repo ingest_yield_curve_fred.py (verified deployed=old/no-merge-preserve, repo=fix; lambda_fred_ingestion.py IDENTICAL=no drift) -> re-zip (193 deps byte-identical) -> upload w/ content-sha256 metadata (G/ITO->ztoby) -> safe-apply fred-pipeline (HALTGT, 2 changed: IAM GetObject + lambda source_code_hash) -> 0-diff verify -> live CodeSha256=ztoby confirmed. source-map sha updated (4d62826e0).

## VERIFY (daily invoke; AWS CLI v1 -> inline payload, no --cli-binary-format)
yield-curve folds into lambda_fred_ingestion frequency==daily branch. Invoked {"frequency":"daily"} -> yield_curve {success:True, series_count:10}. Artifact: data_as_of 2026-06-05, ALL 10 tenors=498 obs, **US Treasury 1Y=498 (was 0)**, latest 1Y 2026-06-03 v3.84. preserved_tenors=[] (retry+backoff got 1Y directly; merge-preserve = backstop). Live FE breakage RESOLVED.

## RAVC2 + open
RAVC2 -> CTO (full) + COO. CTO-accept pending. FE: flagged possible CloudFront invalidation for immediate visibility. R2 lifecycle apply HELD on DS side (safety-proof tripped; DS scoping gold/+platinum/, will hand cleared diff). Standing by for R2.

## Compiler Tools
comp-iam service (attempted; resolved via direct role-policy inspection — caught the GetObject gap). terraform plan/safe-apply (fred-pipeline). No comp-iam gaps run (single targeted policy add; will run if broader iam.tf touched).
