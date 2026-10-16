# Deploy Completion Record
**Date opened:** 2026-10-16T02:07:47.892034+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R33 unit G (AR-g-104): irpt-ycharts-generate code CodeSha256 3+fMEJhQ... -> kxOEgpbs... (pin 927337a741, 8 changed of 107 members) plus ONE env variable IRPT_TICKETS_TABLE=opal-tickets plus ONE inline policy irpt-ycharts-generate-ticket-read-policy (dynamodb:GetItem on table/opal-tickets only); generate and its role policy are ONE artifact group; opens its apply only after irpt-status is V-green
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U | s3-prefix | investor-reporting/irpt-ycharts-generate.zip one new object version, sha256 93138482... | the build digest kxOEgpbs... equal then the object read-back and VersionId |  | OPEN |
| C | verify | scoped plan 1 add 1 change 0 destroy (policy added; function env gains IRPT_TICKETS_TABLE only plus last_modified, s3_object_version, source_code_hash) then safe-apply | the plan line and the apply line |  | OPEN |
| V | verify | V-G: G1 CodeSha256, G2 delta 8 of 107, G3 envelope, G4 env plus one, G5 policy and battery after (GetItem on opal-tickets allowed, 6 deny rows DENIED, others equal), G6 inline size, G7 census 0 | the printed reads and the battery |  | OPEN |
| irpt-ycharts-generate | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261016T020747Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
