# Deploy Completion Record
**Date opened:** 2026-09-04T18:01:34.292569+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260904T182650Z
**Deploy:** TO-OP-S-17B: enable Object Lock (GOVERNANCE, 365d default retention) on opal-security-evidence in place; FORWARD-ONLY, the 839 existing case objects are NOT re-written
**Authored by:** 0.7.0_AE_CloudOps~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | PRE-ACT at this vintage: versioning Enabled, no existing lock config, cases/ object count re-measured client-side, key->LastModified map captured for the no-rewrite census | live reads with timestamps | PRE-ACT at 2026-09-04T17:4xZ, re-read rather than inherited. get-bucket-versioning: Status Enabled (the precondition the lock requires). get-object-lock-configuration: ObjectLockConfigurationNotFoundError, so a fresh enable and not a re-apply. cases/ object count 839, counted CLIENT-SIDE off the merged listing with IsTruncated absent and no continuation token -- the issuer's reading was 438 at 13:1xZ, so the prefix nearly DOUBLED in ~4.5h and the newest object landed DURING the census. A key->LastModified map of all 839 was captured as the baseline for the no-rewrite census. | CLOSED 20260904T182649Z |
| L2 | git | SITEZ commit adding aws_s3_bucket_object_lock_configuration + correcting the two comment blocks the change falsifies | commit hash | commit cb67888289 on SITEZ, VERIFIED FROM THE REPOSITORY rather than from tool stdout (git log -1, with a bogus-hash negative control that correctly failed). Adds aws_s3_bucket_object_lock_configuration and corrects the two comment blocks this change falsifies. NOTE: the first commit attempt was REFUSED by the commit-message ASCII gate for non-ASCII characters I had stripped from the .tf but left in the message -- the gate was right and is the only reason it did not land. | CLOSED 20260904T182649Z |
| L3 | activation | safe-apply on the opsec root; plan read first showing 1 to add, 0 to change, 0 to destroy and ZERO forces-replacement on the bucket | plan + apply output | Plan read as its own artifact BEFORE the act: 'Plan: 1 to add, 0 to change, 0 to destroy', the single resource being aws_s3_bucket_object_lock_configuration.security_evidence with object_lock_enabled Enabled and default_retention GOVERNANCE/365. THE CATASTROPHIC CHECK: grep counts of 'must be replaced', 'forces replacement' and 'will be destroyed' were ALL ZERO -- the bucket resource is not in the change set at all, which is why the create-time-only object_lock_enabled argument was deliberately NOT used on the bucket. Apply: 'Creation complete after 1s' / 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.' ENABLE TIMESTAMP 2026-09-04T18:09:25Z. | CLOSED 20260904T182649Z |
| L4 | verify | POST: get-object-lock-configuration read live; get-object-retention on a PRE-EXISTING object (no retention) AND a NEWLY-WRITTEN one (GOVERNANCE); LastModified census unchanged for the pre-act keys; bypass holders enumerated by SIMULATION | live reads pasted | POST, all live reads. AC1: get-object-lock-configuration returns ObjectLockEnabled=Enabled, Mode=GOVERNANCE, Days=365. AC2 (the control that could have failed): pre-existing object written 02:47:46Z returns NoSuchObjectLockConfiguration = NO retention; a REAL sentinel-written case file from 18:09:40Z returns GOVERNANCE with RetainUntilDate 2027-09-04T18:09:39Z -- enable timestamp 18:09:25Z sits between the two objects' writes. No probe object was created, so no undeletable litter was added to the evidence store. AC3: all 839 pre-act keys still present, 0 missing, ZERO LastModified changed. AC4: s3:BypassGovernanceRetention simulated over 231 principals derived at this vintage (224 roles + 7 users) -- 3 allowed, 228 denied, 0 errors, and ALL THREE ARE HUMAN/INTERACTIVE IAM USERS with ZERO roles, so no automation can bypass. AC5: unscoped re-plan 'No changes.' both after the apply and after the documentation edit. | CLOSED 20260904T182649Z |

## Log

- 20260904T180134Z OPENED by 0.7.0_AE_CloudOps~X with 4 leg(s)
- 20260904T182649Z LEG L1 closed: PRE-ACT at 2026-09-04T17:4xZ, re-read rather than inherited. get-bucket-versioning: Status Enabled (the precondition the
- 20260904T182649Z LEG L2 closed: commit cb67888289 on SITEZ, VERIFIED FROM THE REPOSITORY rather than from tool stdout (git log -1, with a bogus-hash neg
- 20260904T182649Z LEG L3 closed: Plan read as its own artifact BEFORE the act: 'Plan: 1 to add, 0 to change, 0 to destroy', the single resource being aws
- 20260904T182649Z LEG L4 closed: POST, all live reads. AC1: get-object-lock-configuration returns ObjectLockEnabled=Enabled, Mode=GOVERNANCE, Days=365. A
- 20260904T182650Z CLOSED -- all 4 legs proven
