# Deploy Completion Record
**Date opened:** 2026-10-16T02:07:47.892034+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T024904Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R33 unit G (AR-g-104): irpt-ycharts-generate code CodeSha256 3+fMEJhQ... -> kxOEgpbs... (pin 927337a741, 8 changed of 107 members) plus ONE env variable IRPT_TICKETS_TABLE=opal-tickets plus ONE inline policy irpt-ycharts-generate-ticket-read-policy (dynamodb:GetItem on table/opal-tickets only); generate and its role policy are ONE artifact group; opens its apply only after irpt-status is V-green
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U | s3-prefix | investor-reporting/irpt-ycharts-generate.zip one new object version, sha256 93138482... | the build digest kxOEgpbs... equal then the object read-back and VersionId | R0 irpt-ycharts-generate CodeSha256 3+fMEJhQ... equal, latest S3 version wJDd4Tr_Ya8CWi2CSPqgVqci4riH04lh (the rollback source) downloaded and hashed equal, envelope 200 00dd568675e0f498.. 426 bytes twice; census changed_members=8 (7 changed + ticket_confirmation.py added; 107 built, 106 live) equal to the packet table; BUILD_ONLY digest kxOEgpbspky10PYWQ28y0+7V2UXG28whJ2riMa4CkTE= equal to expected, worktree porcelain 0; real upload one new object version, read back sha256 93138482... equal (see the record for the VersionId) | CLOSED 20261016T023417Z |
| C | verify | scoped plan 1 add 1 change 0 destroy (policy added; function env gains IRPT_TICKETS_TABLE only plus last_modified, s3_object_version, source_code_hash) then safe-apply | the plan line and the apply line | scoped plan (two targets) at trunk HEAD cc6b3becbf, ycharts and modules TF files unchanged since pin 927337a741: Plan 1 to add, 1 to change, 0 to destroy; the add aws_iam_role_policy.generate_ticket_read = irpt-ycharts-generate-ticket-read-policy, one statement Allow dynamodb:GetItem on table/opal-tickets only; the change = function attributes environment (gains exactly IRPT_TICKETS_TABLE=opal-tickets, none removed or changed), last_modified, s3_object_version wJDd4Tr_->q.dgcHo9e, source_code_hash 3+fMEJhQ->kxOEgpbs only (read from terraform show -json of the saved plan); safe-apply comp-tagauthz passed, Apply complete 1 added 1 changed 0 destroyed 02:39Z; targeted re-plan No changes | CLOSED 20261016T024425Z |
| V | verify | V-G: G1 CodeSha256, G2 delta 8 of 107, G3 envelope, G4 env plus one, G5 policy and battery after (GetItem on opal-tickets allowed, 6 deny rows DENIED, others equal), G6 inline size, G7 census 0 | the printed reads and the battery | V-G 02:40Z to 02:43Z: G1 CodeSha256 kxOEgpbspky10PYWQ28y0+7V2UXG28whJ2riMa4CkTE=; G2 live zip sha256 93138482... 107 members vs pre-window 106: 7 changed + ticket_confirmation.py added = 8 of 107, hashes equal the packet table; G3 refusal envelope 200 00dd568675e0f498.. 426 bytes twice equal to R0; G4 env R0 plus exactly IRPT_TICKETS_TABLE=opal-tickets, handler timeout memory layers role runtime equal; G5 new policy document equals the packet statement, battery 11 rows differs from R0 in exactly the first row (GetItem on table/opal-tickets implicitDeny -> allowed), Query Scan PutItem UpdateItem DeleteItem BatchGetItem on it and GetItem on index/status-index (7 rows) implicitDeny, irpt-requests, opal-users-v2, s3 rows allowed as before; G6 inline policies 4 -> 5, aggregate 6000 -> 6196 compact chars (limit 10240), the other four unchanged; G7 census changed_members=0 for both functions | CLOSED 20261016T024425Z |
| irpt-ycharts-generate | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | TF apply 1 added 1 changed 0 destroyed through safe-apply on the saved plan (function + the one inline policy; ONE artifact group); targeted re-plan No changes; deployed source_code_hash / CodeSha256 kxOEgpbspky10PYWQ28y0+7V2UXG28whJ2riMa4CkTE= equals the uploaded zip's base64 sha256 (object read-back sha256 93138482...); served reads: refusal envelope equal to R0, env plus IRPT_TICKETS_TABLE only, battery moved in exactly the first row, census changed_members=0 | CLOSED 20261016T024904Z |

## Log

- 20261016T020747Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
- 20261016T023417Z LEG U closed: R0 irpt-ycharts-generate CodeSha256 3+fMEJhQ... equal, latest S3 version wJDd4Tr_Ya8CWi2CSPqgVqci4riH04lh (the rollback 
- 20261016T024425Z LEG C closed: scoped plan (two targets) at trunk HEAD cc6b3becbf, ycharts and modules TF files unchanged since pin 927337a741: Plan 1 
- 20261016T024425Z LEG V closed: V-G 02:40Z to 02:43Z: G1 CodeSha256 kxOEgpbspky10PYWQ28y0+7V2UXG28whJ2riMa4CkTE=; G2 live zip sha256 93138482... 107 mem
- 20261016T024904Z LEG irpt-ycharts-generate closed: TF apply 1 added 1 changed 0 destroyed through safe-apply on the saved plan (function + the one inline policy; ONE artif
- 20261016T024904Z CLOSED -- all 4 legs proven
