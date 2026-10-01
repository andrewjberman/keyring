# Deploy Completion Record
**Date opened:** 2026-10-01T17:59:08.796645+00:00
**Status:** OPEN
**Deploy:** MDPF_TAXSMA first-day rule (Andrew-direct ~17:4xZ): mdpf-gold-lambda from pin 8ade880fad (CodeSha256 eZ6Rtm+2.., S3 version O09x_Btrx4EEuu_fI2uwz5Jkf8YlV8xL) to pin 335430e793 (zip sha256 f582f8e7.., expected CodeSha256 9YL45zw0..), Tax still DISABLED; covered by the TX-r-3 never-widen halves (CTO @1b43d6f201, COO @07d269eb28)
**Authored by:** 4.0.0_SA_CRO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | the built zip uploaded to s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip | downloaded back, sha256 f582f8e73c34549ef6c97720a5198d7f6bce13bc629b7a5977a6d9c6e3619289 equal to the built zip and the metadata; prior version recorded |  | OPEN |
| P1 | verify | a fresh saved plan of mdpf-pipeline | 0/1/0: the function's code, hash and MDPF_GOLD_COMMIT only |  | OPEN |
| D1 | activation | safe-apply mdpf-pipeline (mdpf-gold-lambda) | deployed CodeSha256 9YL45zw0VJ72yXcgpRmNf2vOE7xim3pZd6bZxuNhkok=; environment the pin only; re-plan No changes |  | OPEN |
| V1 | verify | the deployed qa_local dry run before and after | both green 16 of 16; AFTER equal to BEFORE outside process-time paths (Tax DISABLED, so the rule cannot move a value) |  | OPEN |

## Log

- 20261001T175908Z OPENED by 4.0.0_SA_CRO with 4 leg(s)
