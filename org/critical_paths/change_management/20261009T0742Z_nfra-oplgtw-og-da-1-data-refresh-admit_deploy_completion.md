# Deploy Completion Record
**Date opened:** 2026-10-09T07:42:40.078329+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T082744Z
**Deploy:** OG-da-1 Phase B: opal-data-refresh-api admission fails closed (one Lambda, code only)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S3 | s3-prefix | data-refresh/opal-data-refresh-api.zip | artifact uploaded with content-sha256 user metadata; verified on size AND metadata | artifact uploaded 07:4xZ: VersionId f0pfQmR1BByh9jcBQHwYymYRSfZ2IKih, ETag 96563a6797ef4a13890778c11e7dc4aa, Size 20716 B, SSE AES256, Metadata content-sha256=qHMjXkK1/1NhmBmkK/6Q+q+WdXMRoTOprNfTixBIxaM= verified by head-object byte-equality against the built hash (EXACT MATCH), not rc=0. Built from HEAD bytes via git show (0 CRLF pairs in both members); member set equals the source map's declared set (lambda_function.py 83888 B, check_triggered_by.py 1825 B), asserted in the builder. Prior version WJQGGIAlTSMp0Vny8avvQ7LxflVuvLf6 retained for rollback. | CLOSED 20261009T075526Z |
| RB | verify | opal-data-refresh-api | post-apply read-back: CodeSha256 == built hash, State Active, LastUpdateStatus Successful, re-plan No changes | Read-back PASS on all four limbs: live CodeSha256 qHMjXkK1/1NhmBmkK/6Q+q+WdXMRoTOprNfTixBIxaM= EQUAL to the built hash by string comparison, State Active, LastUpdateStatus Successful, and the targeted re-plan reads 'No changes. Your infrastructure matches the configuration.' AC2's own instrument agrees independently by downloading the live zip: 'lambda_function.py equal-to-HEAD=True ... RESULT: PASS'. The post-apply FULL root plan did NOT read clean, and that is row NFRA_OPLGTW-Z-S72 (ARMED, @deee55b3ef): the artifact key had a SECOND yang-lambda reader, module.data_refresh_api_qa_scratch, which the signed blast radius missed. 2.0.0_SA_COO~O ruled disposition (b) in amendment A1 @888b6c9699 -- pin the clone, not ratified as a widening. Executed: the pinned version WJQGGIAlTSMp0Vny8avvQ7LxflVuvLf6 was copied to the clone's OWN key data-refresh/opal-data-refresh-api-qa-scratch.zip (19753 B, ETag 15413b4ac88881c9b0e19dae0eceb215 equal to the source version, content-sha256 E4944Imr... verified by head-object), qa-scratch-instance.tf repointed, and the plan applied from a saved full-root plan whose only non-no-op row changed s3_key and s3_object_version -- source_code_hash did NOT change, which is the proof the pin moves no executable byte. The ruling's Done test now reads both limbs PASS: the clone reads CodeSha256 E4944Imr7Y4S4//rTR6HN5sbwczbwLw5DcaH4IZ0D0E= State Active, and a FULL root plan reads 'No changes' at detailed-exitcode rc=0. The pin was deliberately a separate KEY, not a version-override variable on ../modules/yang-lambda, which would have put all 231 of that module's consumers in the blast radius to fix one clone. | CLOSED 20261009T082659Z |
| opal-data-refresh-api | tf-lambda | module.data_refresh_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | safe-apply of a SAVED targeted plan at 07:59Z -> 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Plan graded from terraform show -json, never the rendered text (which hid 28 attributes behind a redaction line): 2 resource_changes, 1 non-no-op, and its only changed attributes were source_code_hash E4944Imr7Y4S4//rTR6HN5sbwczbwLw5DcaH4IZ0D0E= -> qHMjXkK1/1NhmBmkK/6Q+q+WdXMRoTOprNfTixBIxaM=, s3_object_version WJQGGIAlTSMp0Vny8avvQ7LxflVuvLf6 -> f0pfQmR1BByh9jcBQHwYymYRSfZ2IKih, and last_modified (computed) -- zero attributes outside the three the ask's section 7 step 3 allows. Role, environment (5 keys), timeout 60, memory 256, runtime python3.11 and handler identical before and after. portal-time-machine untouched (CodeSha256 0R8pqdEvf4qvWYCYMYbuSrmekB6l9+5jd8I11b70jbk=, LastModified 2026-03-12). No HALTGT pass is cited as evidence, per cloud-ops. | CLOSED 20261009T082659Z |

## Log

- 20261009T074240Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
- 20261009T075526Z LEG S3 closed: artifact uploaded 07:4xZ: VersionId f0pfQmR1BByh9jcBQHwYymYRSfZ2IKih, ETag 96563a6797ef4a13890778c11e7dc4aa, Size 20716 
- 20261009T082659Z LEG opal-data-refresh-api closed: safe-apply of a SAVED targeted plan at 07:59Z -> 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Plan grad
- 20261009T082659Z LEG RB closed: Read-back PASS on all four limbs: live CodeSha256 qHMjXkK1/1NhmBmkK/6Q+q+WdXMRoTOprNfTixBIxaM= EQUAL to the built hash b
- 20261009T082744Z CLOSED -- all 3 legs proven
