# Deploy Completion Record
**Date opened:** 2026-10-16T02:07:29.020190+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T022945Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R33 unit S (AR-g-104): irpt-status code CodeSha256 PcGK+EpS... -> OOez8YSm... (pin 927337a741, status.py only, 49 members): BUILD_ONLY digest check, one upload, scoped plan 0/1/0, safe-apply, V-S reads; applied BEFORE irpt-ycharts-generate (CTO condition 4)
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U | s3-prefix | investor-reporting/irpt-status.zip one new object version, sha256 38e7b3f1... | the build digest OOez8YSm... equal then the object read-back and VersionId | R0 irpt-status CodeSha256 PcGK+EpS... equal, latest S3 version a2Jft9vGIzDN0IX7JsQjhX_ohuZcXzV4 (the rollback source) downloaded and hashed equal, envelope 200 588cea1d4612ef48.. 406 bytes twice; census changed_members=1 status.py of 49; BUILD_ONLY digest OOez8YSmE22btOqx28/fJdK9sxGNDGAumU5pMJ++6Ss= equal to expected, worktree porcelain 0; real upload one new version LRVpkveSkjFQiKnK0XYAcutUlBEjSMuc (366323 bytes, 68 versions from 67, 0 delete markers), read back sha256 38e7b3f184a6136d... equal | CLOSED 20261016T022304Z |
| C | verify | scoped plan 0 add 1 change 0 destroy (last_modified, s3_object_version, source_code_hash only) then safe-apply | the plan line and the apply line | scoped plan -target=module.irpt_status.aws_lambda_function.this at trunk HEAD cc6b3becbf (pin 927337a741 an ancestor, ops TF files unchanged since the pin): Plan 0 to add, 1 to change, 0 to destroy, last_modified + s3_object_version a2Jft9vG->LRVpkveS + source_code_hash PcGK->OOez8YSm only; safe-apply (comp-tagauthz passed; crossbox-deploy-check WARN no verdict rc=124 in WARN mode) Apply complete 0 added 1 changed 0 destroyed at 02:27Z; targeted re-plan No changes | CLOSED 20261016T022917Z |
| V | verify | V-S: G1 CodeSha256, G2 delta exactly status.py of 49, G3 refusal envelope equal | the printed reads | V-S 02:27Z: G1 CodeSha256 OOez8YSmE22btOqx28/fJdK9sxGNDGAumU5pMJ++6Ss= equals expected; G2 live zip sha256 38e7b3f1... 49 of 49 members compared, exactly 1 differs: status.py (490a176dddd8 live now vs 87048c7f4d00 pre-window); G3 refusal envelope invoke 200 no FunctionError body sha256 588cea1d4612ef48.. 406 bytes twice, equal to R0; memory 1024 timeout 29 handler role equal | CLOSED 20261016T022917Z |
| irpt-status | tf-lambda | module.irpt_status.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | TF apply 0 added 1 changed 0 destroyed through safe-apply on the saved plan; targeted re-plan No changes; deployed source_code_hash / CodeSha256 OOez8YSm... equals the uploaded zip's base64 sha256 (object read-back sha256 38e7b3f1...); served read: refusal envelope equal to R0 and the live zip differs from the pre-window zip in exactly status.py | CLOSED 20261016T022944Z |

## Log

- 20261016T020729Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
- 20261016T022304Z LEG U closed: R0 irpt-status CodeSha256 PcGK+EpS... equal, latest S3 version a2Jft9vGIzDN0IX7JsQjhX_ohuZcXzV4 (the rollback source) do
- 20261016T022917Z LEG C closed: scoped plan -target=module.irpt_status.aws_lambda_function.this at trunk HEAD cc6b3becbf (pin 927337a741 an ancestor, op
- 20261016T022917Z LEG V closed: V-S 02:27Z: G1 CodeSha256 OOez8YSmE22btOqx28/fJdK9sxGNDGAumU5pMJ++6Ss= equals expected; G2 live zip sha256 38e7b3f1... 4
- 20261016T022944Z LEG irpt-status closed: TF apply 0 added 1 changed 0 destroyed through safe-apply on the saved plan; targeted re-plan No changes; deployed sourc
- 20261016T022945Z CLOSED -- all 4 legs proven
