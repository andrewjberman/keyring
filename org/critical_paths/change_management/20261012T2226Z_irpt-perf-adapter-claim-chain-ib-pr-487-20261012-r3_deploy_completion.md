# Deploy Completion Record
**Date opened:** 2026-10-12T22:26:35.481762+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T223833Z
**Deploy:** irpt-performance-adapter (a Lambda; no ECS task family pulls the artifact; 25 worktrees read, none open names it in the main tree): holdings_gold.py re-pin 05219b8444 (3381c42f13), CodeSha256 kMB8xCI9 -> abep4h7R; rollback S3 version F.G7ZDSNMeGR4mwkm7hElyoh1tLuNpGf (content-sha256 kMB8xCI9, named before upload, 64 versions listed); TO-IB-pr-487 AMENDMENT 2 @07fc32b06c fallback B (nine refs import smoke, arms UNEXERCISED-LIVE); orion-only MOVES
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-performance-adapter | tf-lambda | module.irpt_performance_adapter.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | safe-apply of a planfile (1 changed, 0 destroyed: s3_object_version F.G7ZDSN -> oI.PAFCtZLh1MQJR6sh1UZY0O0A.YAfe, source_code_hash kMB8xCI9 -> abep4h7R) Apply complete 0 added/1 changed/0 destroyed at 2026-10-12T22:35Z; live get-function-configuration CodeSha256 abep4h7RngMS9JomQUdkcOT3EZ+W953OdxeK0HkdzFo= LastModified 2026-10-12T22:35:06Z Active/Successful (equals the uploaded sha256 metadata); re-plan detailed-exitcode 0 'No changes'; verify-on-served: the nine kept refs give the SAME internal refusal class after as before (8 PathARetiredForFirm, 1 VendorEgressRefused), 0 TypeError and 0 Traceback events in the log window from 22:35:06Z (64 events); Inflection path UNEXERCISED-LIVE per CTO AMENDMENT 2 fallback B. | CLOSED 20261012T223833Z |

## Log

- 20261012T222635Z OPENED by 0.7.0_AE_CloudOps~IB2 with 1 leg(s)
- 20261012T223833Z LEG irpt-performance-adapter closed: safe-apply of a planfile (1 changed, 0 destroyed: s3_object_version F.G7ZDSN -> oI.PAFCtZLh1MQJR6sh1UZY0O0A.YAfe, source
- 20261012T223833Z CLOSED -- all 1 legs proven
