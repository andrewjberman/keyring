# Deploy Completion Record
**Date opened:** 2026-10-13T01:11:20.711965+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-21 (client-facing, INFLFENCE): admit irpt-performance-adapter-role to opal-data-inflection, READ-ONLY, ONE prefix irpt/inflection/gold/holdings_performance_daily/, via safe-apply on shared-infra -target='aws_s3_bucket_policy.lgic_firm["opal-data-inflection"]' (ONE resource, 1 to change: THREE added statements DenyScopedExemption1AnyOtherAction/ObjectsOutsidePrefix/ListingOutsidePrefix); pair SIGNED: CTO half @354a12bc04 + COO half NEVER_WIDEN_INFLECTION_FENCE_ADMIT_IRPT_PERFORMANCE_ADAPTER; registry row commit 61cc536c29 (ancestor of HEAD d18ce12e3c), lib/opal_naming.py validate rc=0. PRE-ACT: bucket policy saved as the rollback document deliverables/0.7.0_AE_CloudOps~FBL/evidence_f21/PRIOR_bucket_policy_opal-data-inflection.json (1 statement DenyForeignFirmPrincipals, 642 B, last put 2026-10-08 05:17Z); identity side (no resource policy): ListBucket on the prefix allowed, GetObject on one partition key allowed, ListBucket on irpt/inflection/silver/ implicitDeny. ROLLBACK = put-bucket-policy of the saved prior policy, read back. Cause: DenyForeignFirmPrincipals refused s3:ListBucket to the role since 2026-10-13 00:04:48Z (latent, not a deploy effect). NO other bucket, principal, action or prefix.
**Authored by:** 0.7.0_AE_CloudOps~FBL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 0 gate and step 1 pre-reads: halves SIGNED, 61cc536c29 ancestor, registry row, validate rc=0, prior policy saved, identity-side simulate | evidence_f21/step0_*, step1_identity_side.txt, PRIOR_bucket_policy_*.json |  | OPEN |
| L2 | verify | step 3 scoped plan: Plan 0 to add, 1 to change, 0 to destroy and the policy diff is exactly THREE added statements | plan JSON read, statement sids named |  | OPEN |
| L3 | activation | step 4 safe-apply of the saved plan, start and end times | apply summary rc=0 with times |  | OPEN |
| L4 | verify | step 5 read after: three statements live, simulate WITH resource policy (allowed on prefix; denied on another prefix; PutObject denied; foreign principal explicitDeny), request 2xx or stated not run, explicit-deny lines stop; AC1-AC3 | AC1 No changes, AC2 the three sids, AC3 0 |  | OPEN |

## Log

- 20261013T011120Z OPENED by 0.7.0_AE_CloudOps~FBL with 4 leg(s)
