# Deploy-Completion Ledger -- yang-varflag-check (MDPF_VARFLAG P1 SHADOW)

**Status:** OPEN
**Opened:** 2026-07-17T17:45Z
**Owner:** 0.2.0_DT_PortfolioAnalytics (TO_VARFLAG_SHADOW_01 @f70328bda)
**Lambda:** yang-varflag-check (pipeline: yang-pipeline) + YangDataPipeline SFN definition edit

## Scope
- New Lambda yang-varflag-check (stdlib+boto3 only, no layers): V1/P1/P2/V2/V3 + ts-derived
  checks per the ratified stack; baseline = last ACCEPTED execution via DDB + outputs-manifest
  (BE01 seam-join reused); Jan-YTD suppression; FM-6 registration invariant; report to
  s3://opal-data-portal-v2/data-refresh/varflag/{exec}/report.json. SHADOW: blocks nothing.
- SFN: InvalidateCloudFront -> VarflagShadowCheck -> PipelineSuccess (Catch-all to Success both
  layers); ICF's own catch also routes through the shadow.
- New scoped IAM role (DDB Query + states:DescribeExecution + versioned served reads +
  varflag-prefix writes) -- deliberately NOT the shared yang lambda role.

## Pre-deploy acceptance (exercised locally on real artifact versions)
- corrupt 07-16 vs healthy 07-12: 6/6 ST slow cells flagged (551-1151pct), servedgrain + derived
  grain agree to the decimal; healthy 07-12 vs 07-01: 0 flags.
- 49-vintage calibration (48 transitions): 1.85 false-flags/upload mean (budget <=2); corrupt 6/6;
  fat tail (max 10) sits on stale-vintage re-upload file transitions the accepted-baseline rule
  excludes in the real instrument; vol-cell separation healthy<=70pct vs corrupt>=679pct.

## Legs
- [ ] 1. Source committed (commit-gate)
- [ ] 2. build-and-upload.sh yang-pipeline yang-varflag-check
- [ ] 3. terraform plan (expect: +role/+policy/+attachment/+lambda, ~SFN definition)
- [ ] 4. safe-apply
- [ ] 5. 0-diff plan
- [ ] 6. record-terraform-deploy + tag + push --follow-tags
- [ ] 7. Behavior verify: direct invoke with the latest real execution ids -> report lands +
        summary log line; then >=3 real uploads accumulate shadow evidence before any P2 proposal.

## Rollback surface
SFN definition: revert VarflagShadowCheck edit (ICF -> PipelineSuccess) + apply. Lambda inert
without the SFN edge.
