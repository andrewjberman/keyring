# Deploy Completion Record
**Date opened:** 2026-09-13T23:26:28.276204+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260914T012943Z
**Deploy:** card 3 read logging: org trail imported to shared-infra TF at 0-diff; FIRMSEP drops opal-data-cot (portal-auth FIRST); trail ReadOnly selector += opal-data-cot/ + opal-data-49financial/ (shared-infra SECOND); firm-bucket template born-with read logging. Order card3-read-logging @9674549204 (2.0.0_SA_COO~E). Trail HomeRegion=us-east-1 S3BucketName=opal-cloudtrail-logs-313476888478. Module: shared-infra.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit(s) carrying the Terraform: S2 trail declaration + S3 change | commit hash(es) + push state from ls-remote | 926e18a2ce (row ADVI_FIRMBKTS-S1), 9f3fd2cf4a (S2: the trail declaration, the ledger, the probe and the pre-captures) and 37931439cf (S3: the FIRMSEP narrow, the selector values, the template postcondition). All three are ancestors of origin/CLOUD 37931439cfd58d15fbc35721248696ffbe65d65c (git ls-remote 2026-09-14T01:20:00Z) -- ON ORIGIN via 0.0.0_AB_MSTR's push window. | CLOSED 20260914T012942Z |
| L2 | activation | portal-auth: FIRMSEP-s3-direct-access-bypass bucketName narrowed to [opal-data-bd, opal-data-inf]. ROLLBACK: restore the event pattern from rule_pre.json | R-AC3 read + R-AC4 RULE_UNCHANGED_EXCEPT_BUCKETS=true | R-AC3: describe-rule EventPattern bucketName [opal-data-bd, opal-data-inf] at 2026-09-14T00:48:51Z. R-AC4: card3_probe.py same-rule rule_pre.json rule_post.json targets_pre.json targets_post.json -> RULE_UNCHANGED_EXCEPT_BUCKETS=true (rule_post captured 00:48:46Z). Applied: .tools/safe-apply.sh -chdir=infra/aws/terraform/portal-auth apply of the saved plan made with -target=aws_cloudwatch_event_rule.firmsep_s3_bypass, 00:37:41Z-00:39:22Z rc=0, 0 added 1 changed 0 destroyed (commit 37931439cf). R-AC12 targeted plan PLAN_RC=0 at 00:50:50Z. | CLOSED 20260914T005923Z |
| L3 | activation | shared-infra: terraform import of aws_cloudtrail opal-organization-trail ONLY (state-only, no AWS change). ROLLBACK: terraform state rm | R-AC2 PLAN_RC=0 after import | R-AC2: terraform -chdir=infra/aws/terraform/shared-infra plan -detailed-exitcode -input=false -> PLAN_RC=0 'No changes.' at 2026-09-13T23:37:47Z, after terraform import aws_cloudtrail.organization arn:aws:cloudtrail:us-east-1:313476888478:trail/opal-organization-trail 23:37:27Z-23:37:35Z rc=0 (state-only; no AWS call beyond reads) | CLOSED 20260913T234344Z |
| L4 | activation | shared-infra: org trail ReadOnly data selector gains arn:aws:s3:::opal-data-cot/ and arn:aws:s3:::opal-data-49financial/. ROLLBACK: put-event-selectors from selectors_pre.json | R-AC6 read + R-AC7 TRAIL_UNCHANGED_EXCEPT_READ_VALUES=true | R-AC6: ReadOnly selector values = arn:aws:s3:::opal-data-49financial/ arn:aws:s3:::opal-data-bd/ arn:aws:s3:::opal-data-cot/ arn:aws:s3:::opal-data-inf/ (read right after the apply). R-AC7: card3_probe.py same-trail selectors_pre.json selectors_post.json trail_pre.json trail_post.json -> TRAIL_UNCHANGED_EXCEPT_READ_VALUES=true (post captured 00:46:54Z). Applied: .tools/safe-apply.sh -chdir=infra/aws/terraform/shared-infra apply of the saved plan, 2026-09-14T00:45:02Z-00:46:26Z rc=0, comp-tagauthz gate PASSED, 0 added 1 changed 0 destroyed (commit 37931439cf), AFTER the portal-auth apply ended 00:39:22Z. | CLOSED 20260914T005923Z |
| L5 | verify | R-AC6 through R-AC13 after both applies | each criterion output matching its expect | All after both applies. R-AC6 selector values = opal-data-49financial/ opal-data-bd/ opal-data-cot/ opal-data-inf/ (00:46Z). R-AC7 TRAIL_UNCHANGED_EXCEPT_READ_VALUES=true (00:46:54Z). R-AC8 opal-data-bd n=1 first=00:37:39Z over T0..T0+30min (the driven T0 read, row ADVI_FIRMBKTS-S4). R-AC9 opal-data-cot n=0 over T0 00:37:31Z .. trail apply start 00:45:02Z. R-AC10 opal-data-cot n=3 first=2026-09-14T01:02:35Z (organic, opal-cot-value-parity). R-AC11 opal-data-49financial n=1 first=01:11:38Z (T1b probe; row ADVI_FIRMBKTS-S5). R-AC12 targeted portal-auth plan PLAN_RC=0 (00:50:50Z). R-AC13 shared-infra plan PLAN_RC=0 (01:00:35Z). R-AC16 untargeted portal-auth plan = exactly '  # aws_wafv2_web_acl.opal_cloudfront_protection will be updated in-place\|' (00:51Z). R-AC5 ORDER putrule=00:39:23Z puteventselectors=00:46:28Z rule_first=true. | CLOSED 20260914T012941Z |

## Log

- 20260913T232628Z OPENED by 0.7.0_AE_CloudOps with 5 leg(s)
- 20260913T234344Z LEG L3 closed: R-AC2: terraform -chdir=infra/aws/terraform/shared-infra plan -detailed-exitcode -input=false -> PLAN_RC=0 'No changes.'
- 20260914T005923Z LEG L2 closed: R-AC3: describe-rule EventPattern bucketName [opal-data-bd, opal-data-inf] at 2026-09-14T00:48:51Z. R-AC4: card3_probe.p
- 20260914T005923Z LEG L4 closed: R-AC6: ReadOnly selector values = arn:aws:s3:::opal-data-49financial/ arn:aws:s3:::opal-data-bd/ arn:aws:s3:::opal-data-
- 20260914T012941Z LEG L5 closed: All after both applies. R-AC6 selector values = opal-data-49financial/ opal-data-bd/ opal-data-cot/ opal-data-inf/ (00:4
- 20260914T012942Z LEG L1 closed: 926e18a2ce (row ADVI_FIRMBKTS-S1), 9f3fd2cf4a (S2: the trail declaration, the ledger, the probe and the pre-captures) an
- 20260914T012943Z CLOSED -- all 5 legs proven

## Notes (0.7.0_AE_CloudOps) -- restated after close

`deploy_ledger.py` regenerates this entry on close-leg and close. The notes first appended after L3 (committed
@`9f3fd2cf4a`) did not survive, so they are restated here and carried through S3 and the close.

- **Module chosen: `infra/aws/terraform/shared-infra`**, as the order names it. Two reasons: the 2026-06-30
  1.0.0_SA_CTO ruling (`globgrph/item2e_served_write_trail.tf:15-18`) calls the org trail "shared-infra/security-TF",
  and the firm-bucket template the S3(c) mechanism binds to lives there. File
  `shared-infra/cloudtrail-organization-trail.tf`, resource `aws_cloudtrail.organization`, provider alias
  `aws.untagged`: the live trail carries 0 tags, and this module's default_tags would add Project/System, which are
  authorization keys here -- not ruled, and not 0-diff. `prevent_destroy` is set.
- **Phase 1, 2026-09-13 ~23:02Z:** comp-blast -> 1 downstream node, SNS_TOPIC opal-infrastructure-alerts (graph
  vintage 12:15:54Z). describe-trails -> 1 trail, multi-region true, organization false, HomeRegion us-east-1,
  S3BucketName opal-cloudtrail-logs-313476888478. R-AC1 -> bd/ and inf/ only, at 23:01:59Z.
- **L3 import:** 23:37:27Z-23:37:35Z rc=0; R-AC2 PLAN_RC=0 at 23:37:47Z. shared-infra was initialised on this device
  from the locally installed hashicorp/aws 5.100.0 (`-plugin-dir`, no registry download).
- **Import exposure:** a checkout whose config predates `9f3fd2cf4a` plans the trail's DESTROY on a full
  shared-infra apply. Carried as row ADVI_FIRMBKTS-S2 (ARMED, disarm owner 0.0.0_AB_MSTR) and re-measured by
  3.0.0_SA_CVO as -S3: origin/CLOUD now carries it; 22 older linked worktrees still do not.
- **HOLD and route:** before any edit, portal-auth planned 1 unrelated WAF update (row ADVI_FIRMBKTS-S1
  @`926e18a2ce`). Routed (a) by 2.0.0_SA_COO~E @`56941e3366`: portal-auth applied TARGETED at the rule.
- **Applies, both from SAVED plans through safe-apply (commit `37931439cf`):**
  - portal-auth (plan made with `-target=aws_cloudwatch_event_rule.firmsep_s3_bypass`): 2026-09-14
    00:37:41Z-00:39:22Z, 0 added / 1 changed / 0 destroyed; PutRule eventTime 00:39:23Z;
  - shared-infra: 00:45:02Z-00:46:26Z, comp-tagauthz PASSED, 0 added / 1 changed / 0 destroyed;
    PutEventSelectors eventTime 00:46:28Z.
- **T0 deferred** to immediately before the S3 applies, so R-AC9's window stayed inside R-AC8's. The pre-captures were
  re-diffed against live first: all four UNCHANGED.
- **S3(c) MECHANISM AND COPY STEP (R-AC15):** a `lifecycle { postcondition }` on
  `aws_s3_bucket.opal_data_49financial` in `shared-infra/s3-49financial.tf`, with
  `condition = contains(local.org_trail_read_logged_buckets, self.bucket)`. The list lives in
  `shared-infra/cloudtrail-organization-trail.tf` and is the ONLY source of the trail's ReadOnly data_resource values.
  - COPY STEP: copy `s3-49financial.tf` to `s3-<firm>.tf`, and rename the resources and the bucket literal. The plan
    then fails with "BORN-WITH CONTROL (read logging): opal-data-<firm> is not in local.org_trail_read_logged_buckets.
    Add "opal-data-<firm>" to that list in infra/aws/terraform/shared-infra/cloudtrail-organization-trail.tf in this
    same change ...". Add the name, and the single apply mints the bucket and extends the selector.
  - Exercised in scratch copies of the module (plan only) before commit: A (49financial off the list) -> fails,
    naming the list; B (a copier mints opal-data-card3-mutant-zz) -> fails on the new bucket; B2 (the copier adds the
    name) -> 5 to add, 1 to change, no error.
  - UNTESTED RESIDUALS: (1) whether CloudTrail accepts a data-resource ARN for a bucket not yet created, when the
    trail update and the bucket create land in the same apply (no dependency edge orders them) -- if it refuses, a
    second apply completes the change; (2) a new bucket's first reads can come minutes before recording starts
    (row ADVI_FIRMBKTS-S5).
- **Probe reads, all by arn:aws:iam::313476888478:user/Andrew_Berman (aws-cli, 1-byte ranged GetObject):**
  - opal-data-bd: T0 started 00:37:31Z, eventTime 00:37:39Z (row S4);
  - opal-data-cot: T0 started 00:37:37Z, no record; T1 started 00:46:33Z, no record; T1b started 01:11:18Z,
    eventTime 01:11:30Z;
  - opal-data-49financial: T1 started 00:46:41Z, no record; T1b started 01:11:28Z, eventTime 01:11:38Z.
- **First observed recording:** opal-data-cot 01:02:35Z, organic (assumed-role/opal-cot-value-parity);
  opal-data-49financial 01:11:38Z, the T1b probe.
