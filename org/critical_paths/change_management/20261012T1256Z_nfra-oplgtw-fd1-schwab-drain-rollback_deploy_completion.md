# Deploy Completion Record
**Date opened:** 2026-10-12T12:56:26.649868+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T132412Z
**Deploy:** NFRA_OPLGTW OG-ap-11 ROLLBACK under step 5, on issuer ruling A2 @aebec97ee4 (option b): return opal-assets-silver-schwab to the PRIOR code and the PRIOR pin b3e481b261. CAUSE: the deployed per-family drain cannot complete because opal-assets-silver-schwab-role is not authorized for sqs:ChangeMessageVisibility on opal-assets-silver-dlq (row Z-S97, BLOCKING/ARMED). The order's comp-iam NOT-APPLICABLE preflight was wrong and the issuer has taken that as its own defect; the grant goes to the CTO as a NEW never-widen pair, NOT as part of this rollback.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | commit restoring the package's prior schwab_runtime.py and moving local.silver_build_commit.schwab back to b3e481b261 | commit hash | commit 7161de0da442: the package's schwab_runtime.py restored from 2bf592c84189^ and local.silver_build_commit.schwab moved a11240c01c -> b3e481b261. Verified BY BLOB IDENTITY, not by eye: the restored blob 29a71427a853b280c470747c464fc31b90c11840 equals the prior blob exactly, the drain blob 94165f4ce5 is gone, and the restored file carries 0 dlq_message_family definitions and 0 family parameters. A first comparison of md5 against an earlier SHA256 figure looked alarming and was MY algorithm mismatch, not a real difference; the blob check is the one that decides it. | CLOSED 20261012T132411Z |
| L2 | activation | rebuild + upload the prior artifact, then terraform apply via .tools/safe-apply.sh -target the one schwab function, 1 resource changed and no other row | saved-plan summary plus apply result | Rebuilt and uploaded the prior artifact, then applied via .tools/safe-apply.sh against a SAVED plan at 13:14:03Z, rc=0, 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' STRONGEST PRE-APPLY CHECK: the rollback artifact's sha256 read uibjggn93MPPtuIh33Yvehv1xECqrfhPxsWLdmcdYjE= in BUILD_ONLY mode -- byte-identical to the build that was live before OG-ap-11 -- so the artifact was confirmed to be the prior one before anything was applied. Upload write VERIFIED by head-object (size=76049, sha256 metadata match). The plan was the exact reverse of the forward one: ONE resource, the code fields plus the single OPAL_BUILD_COMMIT a11240c01c -> b3e481b261, no other row. Ran 13:14Z, outside [09:15,11:35) [12:00,12:50) [21:15,23:35)Z and at/after the 12:50Z the issuer's ruling required. No HALT_OVERRIDE. | CLOSED 20261012T132411Z |
| L3 | verify | live read-back: CodeSha256 returns to the PRIOR uibjggn93MPPtuIh33Yvehv1xECqrfhPxsWLdmcdYjE=, OPAL_BUILD_COMMIT back to b3e481b261, State Active, LastUpdateStatus Successful, and a 0-diff re-plan | get-function-configuration output | Live read-back after the apply, rc=0: CodeSha256 uibjggn93MPPtuIh33Yvehv1xECqrfhPxsWLdmcdYjE= -- back to the PRIOR build and no longer the OG-ap-11 build YeLmNn/Tkz+HYVVrCS/PeE+mISSAnH/8ilUUxPEnCmk=; OPAL_BUILD_COMMIT b3e481b261; State Active; LastUpdateStatus Successful. Targeted re-plan afterwards: rc=0, 'No changes. Your infrastructure matches the configuration.' Source map's schwab entry returned to last_deployed_commit b3e481b2617ff87f5672172b401bc48f5154379f with artifact_sha256 back to the prior artifact. The DLQ was read NON-DESTRUCTIVELY before the rollback as the ruling required, deleting nothing: exactly one distinct message, the eclipse synthetic 48264f89, still present. | CLOSED 20261012T132412Z |

## Log

- 20261012T125626Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
- 20261012T132411Z LEG L1 closed: commit 7161de0da442: the package's schwab_runtime.py restored from 2bf592c84189^ and local.silver_build_commit.schwab mo
- 20261012T132411Z LEG L2 closed: Rebuilt and uploaded the prior artifact, then applied via .tools/safe-apply.sh against a SAVED plan at 13:14:03Z, rc=0, 
- 20261012T132412Z LEG L3 closed: Live read-back after the apply, rc=0: CodeSha256 uibjggn93MPPtuIh33Yvehv1xECqrfhPxsWLdmcdYjE= -- back to the PRIOR build
- 20261012T132412Z CLOSED -- all 3 legs proven
