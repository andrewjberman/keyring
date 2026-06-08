# CMPAWS Wave-1 CERTIFIED (full marks) + MDPF 15:00Z scheduled-run finding

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE
**Agent:** 0.7.0_AE_CloudOps · **Date:** 2026-06-08 ~15:40-16:05Z

## 1. CMPAWS Wave-1 CERTIFIED AT FULL MARKS (sovereign 95%-F1 gate MET)
CVO independent F1 cert (ran comp-aws against CVO's live re-pull + certified oracle + scorer):
- **S3 = 1.00, IAM = 1.00, EC2 ~1.00** -- all CERTIFIED, 0-untyped, **brittleness PASS** (CVO independently grep-verified pure-discovery).
- Methodology fully proven (existence-vs-live + state-union-provenance + brittleness-by-construction all validated).
- Scorecard: org/tier1_exec/3.0.0_SA_CVO/cmpaws_f1/wave1_scorecard_s3_iam_ec2_20260608.md

3 named IAM FNs fixed (commit 2f30c548b, IAM 0.982->1.00):
- FredIngestionLambdaRole + opal-portal-lambda-role: were mode=DATA (terraform data-sources, never managed) -> dropped by mode!=managed filter. Fix: declared-side now includes data-sources (tf_kind=data, preserves managed-vs-referenced distinction).
- seeking-alpha-scraper-role: module has no state in bucket (HCL-declared, never-applied) -> implemented sec1.4 HCL-secondary check (brace-balanced HCL scan). + join name-fallback now uses id.
- Both shared-primitive fixes lift provenance-accuracy for EVERY class -> Wave-2 starts stronger.

## 2. comp-aws compiler -- comprehensive (commits 215646a6e..af7a6d0bf)
13 node classes (s3, s3_policy, iam, ec2, lambda, eventbridge, sns, sqs, dynamodb, cloudfront, secrets, kms, cloudwatch) + EVENT_SOURCE; **841 typed edges** (ASSUMES 193, HAS_POLICY 334, TRIGGERS 107, EMITS_TO 92, ENCRYPTS_WITH 29, NOTIFIES 26, HAS_PROFILE 22, STARTS 14, GRANTS 13, ORIGIN 6, SUBSCRIBES 5). Full schema-3 properties per class; full schema-1.2 edge vocabulary. Declared = terraform-state-union (managed+data+HCL-secondary), ARN-join, 0 untyped, pure-discovery (brittleness-safe). Snapshot/AC7.
**Wave-2 is now CVO's cert queue** (eventing first, oracle v0.4 + my 71 EVENT_SOURCE origins ready); CVO builds+certs each remaining class oracle-vs-output, names FP/FN, I fix. CVO paces.

## 3. MDPF_COUNTS 15:00Z scheduled-run -- FINDING (account_count fix EXONERATED; COO-accepted)
First-post-fix scheduled nightly: runner FIRED on schedule (i-02448edb LaunchTime 2026-06-08T15:00:08Z -- trigger+cadence WORK) but chain HARD-FAILED at **Stage-3 WS-A (mdpf_aggregate_aua.py) reconciliation** (rc=1): reconciliation=ERROR -> platinum write SKIPPED (drop-rather-than-fabricate, MDPF_ASSETS.019) -> NO 06-08 partition -> Stages 3.5/4/5 SKIPPED.
- **My account_count ROLLUP fix (Stage-4) is DOWNSTREAM -- never ran (log-confirmed); NOT the cause.** Stays deploy-verified + CVO data-layer-PASS on the 06-05 manual run.
- Served artifacts frozen at 06-05 18:37Z = last-good floor (drop-rather-than-fabricate working AS DESIGNED, no bad data served). mdpf-daily-chain-failed=ALARM (correct); 3 other alarms OK.
- Root-cause pointer: cohort_0 jumped $58.6M (06-05 sentinel) -> $104.3M today (+78%) = the sentinel/3-way-identity trip in WS-A. COO connected it to a stale build_mdpf_wsc_inflection_feeder.py drift (CTO comp-pipescript catch).
- COO RAVC2-ACCEPTED (160543Z): fix EXONERATED, MDPF_COUNTS close STANDS (Andrew waived scheduled-cadence gate), WS-A reconciliation -> DS lane. C1 honored (no ad-hoc re-run). Run log: s3://opal-data-mdpf/telemetry/mdpf-daily-runner/logs/mdpf_daily_20260608_150025.log.

## Compiler Tools
comp-aws (built this session). ds-commit-gate clean every commit. comp-pipescript (CTO-side) caught the WS-C feeder drift connected to the MDPF failure.

## Current State / Next
- **[CVO]** Wave-2 per-class cert queue (CVO-paced); I fix any named FP/FN per scorecard. Goal completes when all-classes scorecards reach >=95%.
- **[DS]** MDPF WS-A reconciliation fix (cohort_0 / stale WS-C feeder) -- DS lane, not mine.
- **[me]** account_count fix awaits a clean nightly for the (Andrew-waived) scheduled-cadence confirm; 0.6.0 joins post-MDPF_CADENCE for Wave-2 breadth.
