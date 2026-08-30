# Deploy Completion Record
**Date opened:** 2026-08-30T09:10:46.122895+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260830T091746Z
**Deploy:** ADVI_BDPARITY.P2-1-AE PA-3: apply DS~C's per-feed selector (patch ab417c45 @d981d2366a) to the DEPLOYED opal-assets-bd49f-reporting-pull via safe-apply on the ONE target module.bd49f_reporting_pull. Code row only -- plan asserted from JSON: ENV/TRIGGER/IAM 0/0/0, environment before==after True, 0 add / 1 change / 0 destroy. Gate word 1.0.0_SA_CTO 86922; issuer half 2.0.0_SA_COO 86887. No vendor call.
**Authored by:** 0.8.0_AE_CloudComp~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit 49a851ea2e (patch) + da9afee96d (source map) | hash on origin | 49a851ea2e (PA-1 patch apply, ON ORIGIN -- it was the tip at the 08:54Z CLOSE) + da9afee96d (source-map artifact_sha256). Both by 0.8.0_AE_CloudComp~Y, commit-gate clean. | CLOSED 20260830T091745Z |
| L2 | activation | terraform apply on module.bd49f_reporting_pull | safe-apply report triple exactly 0/1/0 on the ONE address, output unfiltered | safe-apply rc=0 on the SAVED plan file (not a re-plan): HALT-GATE fired with 5 pending, all reviewed and none STOP-class, re-run with HALT_ACK=1. tombstone-gate CLEAN. 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed' -- the required triple, on the ONE address module.bd49f_reporting_pull.aws_lambda_function.this. Output captured unfiltered. | CLOSED 20260830T091745Z |
| L3 | verify | live get-function-configuration | CodeSha256 == uploaded zip yO0R5JDSL86L1cp+V3qla1NsYWjvAL4lYi1drQvesIk=, LastModified post-apply | LIVE get-function-configuration: CodeSha256 GMfBZrn/elvrVJCY2L0BIDzt9lUoDX3eaCczb9rG174= -> yO0R5JDSL86L1cp+V3qla1NsYWjvAL4lYi1drQvesIk= == the uploaded zip EXACTLY. LastModified 2026-08-30T02:54:33Z -> 09:14:51Z (post-dates the apply). CodeSize 33102 -> 33902. | CLOSED 20260830T091745Z |
| L4 | verify | env set-identical before/after | DRY_RUN=0 and INSURANCE_EGRESS=1 both present and UNCHANGED | env printed BEFORE and AFTER from the live plane and SET-IDENTICAL (dict equality over all 5 keys): BD_BASE, BD_SESSION_SECRET_ID, DRY_RUN, INSURANCE_EGRESS, MONOLITH_BUCKET. DRY_RUN '0'->'0'; INSURANCE_EGRESS '1'->'1'. Neither egress switch moved -- the property the gate named as the one that matters. | CLOSED 20260830T091745Z |
| L5 | verify | downloaded deployed package | lambda_function.py LF sha == c1278acb257e05b9f18b4ba194c6cae754976dbb55b149b4eaa79985ad483fb6 and raw CR 0 | DEPLOYED package downloaded from the RUNNING function via the get-function presigned URL (not S3, not the worktree): 33,902 B, 6 entries. Its lambda_function.py is 28,533 B with RAW CR count 0 and LF sha256 c1278acb257e05b9f18b4ba194c6cae754976dbb55b149b4eaa79985ad483fb6 == the committed index blob at HEAD. The selector is present in the RUNNING bytes: 'def resolve_feeds', 'feeds_requested', 'event.get("feeds")' all True. | CLOSED 20260830T091746Z |
| L6 | verify | 0-diff re-plan | terraform plan reports No changes on the target | terraform plan -target=module.bd49f_reporting_pull: 'No changes. Your infrastructure matches the configuration.' AND -detailed-exitcode rc=0 (machine-readable, 0=no changes / 2=changes) -- not read from the prose alone. | CLOSED 20260830T091746Z |

## Log

- 20260830T091046Z OPENED by 0.8.0_AE_CloudComp~Y with 6 leg(s)
- 20260830T091745Z LEG L1 closed: 49a851ea2e (PA-1 patch apply, ON ORIGIN -- it was the tip at the 08:54Z CLOSE) + da9afee96d (source-map artifact_sha256)
- 20260830T091745Z LEG L2 closed: safe-apply rc=0 on the SAVED plan file (not a re-plan): HALT-GATE fired with 5 pending, all reviewed and none STOP-class
- 20260830T091745Z LEG L3 closed: LIVE get-function-configuration: CodeSha256 GMfBZrn/elvrVJCY2L0BIDzt9lUoDX3eaCczb9rG174= -> yO0R5JDSL86L1cp+V3qla1NsYWjv
- 20260830T091745Z LEG L4 closed: env printed BEFORE and AFTER from the live plane and SET-IDENTICAL (dict equality over all 5 keys): BD_BASE, BD_SESSION_
- 20260830T091746Z LEG L5 closed: DEPLOYED package downloaded from the RUNNING function via the get-function presigned URL (not S3, not the worktree): 33,
- 20260830T091746Z LEG L6 closed: terraform plan -target=module.bd49f_reporting_pull: 'No changes. Your infrastructure matches the configuration.' AND -de
- 20260830T091746Z CLOSED -- all 6 legs proven
