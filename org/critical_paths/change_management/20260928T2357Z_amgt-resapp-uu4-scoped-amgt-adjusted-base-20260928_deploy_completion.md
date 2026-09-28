# Deploy Completion Record
**Date opened:** 2026-09-28T23:57:25.843791+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 46 AMGT-uu-4: opal-amgt-scoped-api carries the adjusted Base case (ONE artifact write + ONE safe-apply, bounded by both never-widen halves)
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | S3 artifact research/opal-amgt-scoped-api.zip in opal-313476888478-lambda-artifacts (prior VersionId 0XDw5hJWOYgx3P8CSA42oAlkLuTlupkS recorded at build) | head-object new VersionId + content-sha256 metadata |  | OPEN |
| V1 | verify | AC1 deployed CodeSha256 moved off vBSCqd71wGn1GNOpaWGKr+KdI6t+zo3QVovzEd9Mrew= and LastUpdateStatus=Successful | uu-4.AC1.py exit 0 |  | OPEN |
| V2 | verify | AC2 FWD-30 on the served plane: absences missing=0 on N of N and EXPORT-COMPARE OK on N of N | uu-4.AC2.sh exit 0 |  | OPEN |
| V3 | verify | AC3 served bases ADJUSTED AND BASIS-CARRYING M of M, both halves' expected M=70 | uu-4.AC3.py exit 0 |  | OPEN |
| V4 | verify | stop-limb 5: served /print pdf OUTPUT byte-unchanged, pre-apply capture vs post-apply | sha256 equality over the pre/post pdf captures |  | OPEN |
| V5 | verify | terraform 0-diff replan after the apply | plan reports no changes |  | OPEN |
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260928T235725Z OPENED by 0.7.0_AE_CloudOps~A with 7 leg(s)
