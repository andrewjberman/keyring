# Deploy Completion Record
**Date opened:** 2026-10-01T17:59:08.796645+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T180506Z
**Deploy:** MDPF_TAXSMA first-day rule (Andrew-direct ~17:4xZ): mdpf-gold-lambda from pin 8ade880fad (CodeSha256 eZ6Rtm+2.., S3 version O09x_Btrx4EEuu_fI2uwz5Jkf8YlV8xL) to pin 335430e793 (zip sha256 f582f8e7.., expected CodeSha256 9YL45zw0..), Tax still DISABLED; covered by the TX-r-3 never-widen halves (CTO @1b43d6f201, COO @07d269eb28)
**Authored by:** 4.0.0_SA_CRO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | the built zip uploaded to s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip | downloaded back, sha256 f582f8e73c34549ef6c97720a5198d7f6bce13bc629b7a5977a6d9c6e3619289 equal to the built zip and the metadata; prior version recorded | Uploaded 18:01Z: VersionId J34f45wQHVHOaZUAvogvIKJJRxjaWCzd, 1,628,877 bytes, metadata content-sha256 f582f8e7..; downloaded back by that VersionId and re-hashed: f582f8e73c34549ef6c97720a5198d7f6bce13bc629b7a5977a6d9c6e3619289, equal to the built zip (pin 335430e793, 41 entries, the first-day rule and one catchup call present). Prior version O09x_Btrx4EEuu_fI2uwz5Jkf8YlV8xL is the rollback target. | CLOSED 20261001T180505Z |
| P1 | verify | a fresh saved plan of mdpf-pipeline | 0/1/0: the function's code, hash and MDPF_GOLD_COMMIT only | Saved plan 18:02Z, vendored terraform 1.9.8: 0 to add, 1 to change, 0 to destroy = aws_lambda_function.mdpf_gold: s3_object_version O09x.. to J34f.., source_code_hash 799e91b6.. to f582f8e7.., MDPF_GOLD_COMMIT 8ade880fad.. to 335430e793..; nothing else. | CLOSED 20261001T180505Z |
| D1 | activation | safe-apply mdpf-pipeline (mdpf-gold-lambda) | deployed CodeSha256 9YL45zw0VJ72yXcgpRmNf2vOE7xim3pZd6bZxuNhkok=; environment the pin only; re-plan No changes | safe-apply of the saved plan, complete 18:03:11Z: 0 added, 1 changed, 0 destroyed. get-function-configuration: CodeSha256 9YL45zw0VJ72yXcgpRmNf2vOE7xim3pZd6bZxuNhkok= = base64 of the zip sha256; Active; Successful; environment MDPF_GOLD_COMMIT 335430e793 only (Tax DISABLED). | CLOSED 20261001T180505Z |
| V1 | verify | the deployed qa_local dry run before and after | both green 16 of 16; AFTER equal to BEFORE outside process-time paths (Tax DISABLED, so the rule cannot move a value) | Deployed qa_local dry runs (zero writes): BEFORE 18:0xZ code eZ6Rtm+2.. request b20f0980-6c24-4807-9566-91a7eabc2c42 green 16 of 16; AFTER 18:0xZ code 9YL45zw0.. request ecba3f98-b0dc-42a5-9e90-ffead3864628 green 16 of 16. 16 documents compared: byte-identical 0, process-time only 16, other 0. | CLOSED 20261001T180505Z |

## Log

- 20261001T175908Z OPENED by 4.0.0_SA_CRO with 4 leg(s)
- 20261001T180505Z LEG U1 closed: Uploaded 18:01Z: VersionId J34f45wQHVHOaZUAvogvIKJJRxjaWCzd, 1,628,877 bytes, metadata content-sha256 f582f8e7..; downlo
- 20261001T180505Z LEG P1 closed: Saved plan 18:02Z, vendored terraform 1.9.8: 0 to add, 1 to change, 0 to destroy = aws_lambda_function.mdpf_gold: s3_obj
- 20261001T180505Z LEG D1 closed: safe-apply of the saved plan, complete 18:03:11Z: 0 added, 1 changed, 0 destroyed. get-function-configuration: CodeSha25
- 20261001T180505Z LEG V1 closed: Deployed qa_local dry runs (zero writes): BEFORE 18:0xZ code eZ6Rtm+2.. request b20f0980-6c24-4807-9566-91a7eabc2c42 gre
- 20261001T180506Z CLOSED -- all 4 legs proven
