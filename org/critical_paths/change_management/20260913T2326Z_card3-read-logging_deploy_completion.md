# Deploy Completion Record
**Date opened:** 2026-09-13T23:26:28.276204+00:00
**Status:** OPEN
**Deploy:** card 3 read logging: org trail imported to shared-infra TF at 0-diff; FIRMSEP drops opal-data-cot (portal-auth FIRST); trail ReadOnly selector += opal-data-cot/ + opal-data-49financial/ (shared-infra SECOND); firm-bucket template born-with read logging. Order card3-read-logging @9674549204 (2.0.0_SA_COO~E). Trail HomeRegion=us-east-1 S3BucketName=opal-cloudtrail-logs-313476888478. Module: shared-infra.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit(s) carrying the Terraform: S2 trail declaration + S3 change | commit hash(es) + push state from ls-remote |  | OPEN |
| L2 | activation | portal-auth: FIRMSEP-s3-direct-access-bypass bucketName narrowed to [opal-data-bd, opal-data-inf]. ROLLBACK: restore the event pattern from rule_pre.json | R-AC3 read + R-AC4 RULE_UNCHANGED_EXCEPT_BUCKETS=true |  | OPEN |
| L3 | activation | shared-infra: terraform import of aws_cloudtrail opal-organization-trail ONLY (state-only, no AWS change). ROLLBACK: terraform state rm | R-AC2 PLAN_RC=0 after import | R-AC2: terraform -chdir=infra/aws/terraform/shared-infra plan -detailed-exitcode -input=false -> PLAN_RC=0 'No changes.' at 2026-09-13T23:37:47Z, after terraform import aws_cloudtrail.organization arn:aws:cloudtrail:us-east-1:313476888478:trail/opal-organization-trail 23:37:27Z-23:37:35Z rc=0 (state-only; no AWS call beyond reads) | CLOSED 20260913T234344Z |
| L4 | activation | shared-infra: org trail ReadOnly data selector gains arn:aws:s3:::opal-data-cot/ and arn:aws:s3:::opal-data-49financial/. ROLLBACK: put-event-selectors from selectors_pre.json | R-AC6 read + R-AC7 TRAIL_UNCHANGED_EXCEPT_READ_VALUES=true |  | OPEN |
| L5 | verify | R-AC6 through R-AC13 after both applies | each criterion output matching its expect |  | OPEN |

## Log

- 20260913T232628Z OPENED by 0.7.0_AE_CloudOps with 5 leg(s)
- 20260913T234344Z LEG L3 closed: R-AC2: terraform -chdir=infra/aws/terraform/shared-infra plan -detailed-exitcode -input=false -> PLAN_RC=0 'No changes.'

## Notes (0.7.0_AE_CloudOps)

- **Module chosen: `infra/aws/terraform/shared-infra`**, as the order names it. Two reasons: the 2026-06-30
  1.0.0_SA_CTO ruling (`globgrph/item2e_served_write_trail.tf:15-18`) calls the org trail "shared-infra/security-TF",
  and the firm-bucket template the S3(c) mechanism binds to lives there. File
  `infra/aws/terraform/shared-infra/cloudtrail-organization-trail.tf`, resource `aws_cloudtrail.organization`, declared
  through provider alias `aws.untagged` (no default_tags). The live trail carries 0 tags; this module's default_tags
  would add Project/System, which are authorization keys in this account -- not ruled, and not 0-diff.
- **Phase 1, 2026-09-13 ~23:02Z:** `comp-blast FIRMSEP-s3-direct-access-bypass` -> 1 downstream node, SNS_TOPIC
  opal-infrastructure-alerts (graph vintage 2026-09-13 12:15:54Z). `describe-trails --trail-name-list
  opal-organization-trail` -> 1 trail, IsMultiRegionTrail true, IsOrganizationTrail false, HomeRegion us-east-1,
  S3BucketName opal-cloudtrail-logs-313476888478, 0 tags. R-AC1 -> `arn:aws:s3:::opal-data-bd/
  arn:aws:s3:::opal-data-inf/` at 23:01:59Z.
- **L3 import:** `terraform import aws_cloudtrail.organization
  arn:aws:cloudtrail:us-east-1:313476888478:trail/opal-organization-trail`, 23:37:27Z-23:37:35Z, rc=0. R-AC2 plan
  PLAN_RC=0 at 23:37:47Z. shared-infra was initialised on this device from the locally installed hashicorp/aws 5.100.0
  (`-plugin-dir`, lock-file hashes matched, no registry download); its pre-import baseline plan read PLAN_RC=0.
- **Residual exposure of the import (recorded, not remediated):** a checkout whose config predates the S2 commit sees
  the trail in state with no config, and would plan its DESTROY on a full shared-infra apply. `prevent_destroy`
  covers every checkout that carries the file. Measured: every recent shared-infra commit on CLOUD is a laptop lane's,
  and origin/SITEZ carries 0 shared-infra commits that are not in CLOUD. So the exposure is this device's worktrees cut
  before the S2 commit, plus any checkout of origin/CLOUD before the next push.
- **HELD at the portal-auth apply (Phase 2 step 1 mismatch):** row `ADVI_FIRMBKTS-S1` @`926e18a2ce` -- before any
  edit, portal-auth plans 1 unrelated in-place WAF update (`aws_wafv2_web_acl.opal_cloudfront_protection`). S3's edits
  are not made or committed until both applies can run back to back, because a committed-but-unapplied selector
  change would let another shared-infra apply arm cot logging before the rule narrows.
- **T0 negative-arm read deferred to immediately before the S3 applies,** so R-AC9's window (T0 to the trail apply's
  start) stays short and inside R-AC8's 30-minute positive-control window. The pre-state captures were taken at
  23:26:46Z; they are re-diffed against live immediately before S3 and re-taken if anything moved.
