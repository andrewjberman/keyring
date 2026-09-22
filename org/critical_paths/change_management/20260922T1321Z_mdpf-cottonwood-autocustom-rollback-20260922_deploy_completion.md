# Deploy Completion Record
**Date opened:** 2026-09-22T13:21:16.448380+00:00
**Status:** OPEN
**Deploy:** ROLLBACK of mdpf-gold-lambda Cottonwood auto-custom deploy (ledger 20260921T1957Z, pin 74d7efe144) on Andrew-direct 'Go' at the 0.7.0_AE_CloudOps~V terminal 2026-09-22 ~13:08Z, CTO concurring (msg 99481). Cause: the deployed bytes crash pre-write in _shape_category_views (_last on cottonwood's trailing None, axis to 2026-09-21 vs values to 09-18) -- reproduced offline; the 13:30Z fire would write 0 of 16 vs yesterday's 8. The rollback is the branch both signed halves cover (packet blob 2c59f07389 s.3): artifact back to VersionId 9GsracvIPvfBMzF1dttMpew0TkQtt.qg (sha 7af2180975...), MDPF_GOLD_COMMIT back to 48b8671569b72efb4eca64ef41ded4de9c54e84c, safe-apply -target=aws_lambda_function.mdpf_gold; served CodeSha256 must read evIYCXURor4V++Ci4HsgwE8zIPZva/BAL+ICaLJIiAE=, CodeSize 835,383.
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip | copy of version 9GsracvI... becomes latest; new latest re-downloaded sha256 == 7af2180975...; content-sha256 metadata set |  | OPEN |
| L2 | git | infra/aws/terraform/mdpf-pipeline/gold-lambda.tf MDPF_GOLD_COMMIT -> 48b8671569 | CLOUD commit |  | OPEN |
| L3 | activation | aws_lambda_function.mdpf_gold (safe-apply -target) | targeted plan EXACTLY 1 update (s3_object_version, source_code_hash, env MDPF_GOLD_COMMIT back), 0 add 0 destroy; safe-apply rc=0 |  | OPEN |
| L4 | verify | mdpf-gold-lambda running plane | CodeSha256 == evIYCXUR..., CodeSize 835,383, MDPF_GOLD_COMMIT == 48b8671569; targeted replan 0-diff; before 13:30Z |  | OPEN |

## Log

- 20260922T132116Z OPENED by 0.7.0_AE_CloudOps~V with 4 leg(s)
