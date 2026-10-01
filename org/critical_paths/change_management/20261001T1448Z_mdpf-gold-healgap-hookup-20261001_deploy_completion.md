# Deploy Completion Record
**Date opened:** 2026-10-01T14:48:34.197019+00:00
**Status:** OPEN
**Deploy:** MDPF_HEALGAP cell 1 hookup: mdpf-gold-lambda from pin e8994f23af (CodeSha256 7hI4flW5.., S3 version U4JsC9gYCgaKgm8kRbF1dL.2JgIPESxk) to pin 8ade880fad (zip sha256 799e91b6.., expected CodeSha256 eZ6Rtm+2..), Tax DISABLED; packet DEPLOY_PACKET_GOLD_HEALGAP_HOOKUP_20261001.md signed by 1.0.0_SA_CTO at cb0aa93c78 with four conditions; what the catch-up writes is ledger healgap-cottonwood-catchup-m-20261001
**Authored by:** 4.0.0_SA_CRO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 26.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | the built zip uploaded to s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip | downloaded back, sha256 799e91b66fb65ce2a6e1415681d621169358c428e228356d44e355e84c2ddb5b equal to the built zip and to the content-sha256 metadata; prior version recorded |  | OPEN |
| P1 | verify | a fresh saved plan of mdpf-pipeline | 0 to add, 1 to change, 0 to destroy: the function's code, hash and MDPF_GOLD_COMMIT only |  | OPEN |
| D1 | activation | safe-apply mdpf-pipeline (mdpf-gold-lambda) | deployed CodeSha256 eZ6Rtm+2XOKm4UFWgdYhFpNYxCjiKDVtRONV6Ewt21s=; environment MDPF_GOLD_COMMIT only; re-plan No changes |  | OPEN |
| V1 | verify | the deployed function's qa_local dry run before and after the apply, both after 13:30Z (CTO conditions 1 and 2) | BEFORE green 16 of 16; AFTER equal to BEFORE document by document outside process-time paths, 16 of 16, comparison printed; any other difference is a rollback in the same window |  | OPEN |
| V2 | verify | the 2026-10-02 13:30Z scheduled run (CTO condition 3) | status green on every scope; the cottonwood family report carries a catchup block; no served change outside the five cottonwood dates and global's same five; otherwise same-day rollback, the five objects first, then this function |  | OPEN |

## Log

- 20261001T144834Z OPENED by 4.0.0_SA_CRO with 5 leg(s)
