# Deploy Completion Record
**Date opened:** 2026-09-22T15:14:22.899540+00:00
**Status:** OPEN
**Deploy:** FIX-FORWARD of mdpf-gold-lambda Cottonwood auto-custom: pin 48b8671569 -> 5991626d4f (the signed 09-21 pin 74d7efe144 + roll-forward carry fix + Andrew's 09-11 null-tail guard 1465fd3f7d). Andrew-direct at the 0.7.0_AE_CloudOps~V terminal 2026-09-22 ~13:4xZ ('fix forward ... deploy, and issue a manual run. When this is done, ping me, I will visual smoke'). Never-widen halves on packet blob 6325fded1415: CTO @9e7f36b904, CRO @2ba4230f64. Built zip 872,699 B sha256 e5a28d1f9581bda84c43cddf63425a34c8ce96aa2aea90803491d588b445c194 (.scratch/mdpf_cot/built_fix2.zip, not rebuilt). Rollback per key by prior VersionId as signed: LEG A uYOduyR_y0a0IH8bEnA8Lukn4qQRzcAR + literal back to 48b8671569; LEG B FjrdsfCycvPskUPoDXPsBdDggc1WMsy.; staged cottonwood keys Ck8Yka0Y.../T7zvya5j.../5PdffIm_.../6X6tPnax.../JAYwgtMD...; portal + serve keys by prior version (versioning Enabled on all three buckets).
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | s3-prefix | opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip | upload of built_fix2.zip with metadata content-sha256=e5a28d1f...; new VersionId read; re-download sha256 == e5a28d1f...; byte-identical to the signed file |  | OPEN |
| A2 | git | infra/aws/terraform/mdpf-pipeline/gold-lambda.tf MDPF_GOLD_COMMIT -> 5991626d4f | CLOUD commit hash; literal == the built zip's in-zip source_vintage.commit; comment block cites packet blob 6325fded1415 and both halves |  | OPEN |
| A3 | activation | aws_lambda_function.mdpf_gold (safe-apply -target) | targeted plan gated in code (gate_ff_plan.py PASS: exactly 1 update, env diff exactly MDPF_GOLD_COMMIT 48b8671569 -> 5991626d4f, source_code_hash -> e5a28d1f..., s3_object_version -> the uploaded VersionId); .tools/safe-apply.sh rc=0 'Apply complete! 0 added, 1 changed, 0 destroyed' |  | OPEN |
| A4 | verify | mdpf-gold-lambda running plane | CodeSha256 == b64(e5a28d1f...) 5aKNH5WBvahMQ83fY0JaNMjOlqoq6pCANJHViLRFwZQ=, CodeSize 872,699, MDPF_GOLD_COMMIT 5991626d4f...; live bundle re-downloaded == signed zip; in-zip source_vintage 5991626d4f; member controls (name_discovery present, 09-11 guard phrase present, reader-2 phrase present) |  | OPEN |
| B | s3-prefix | opal-data-mdpf/code/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py (the ONE key CLOUD HEAD ac571ef0c7 changes) | MSTR's push lands; the hook's printed synced-key list checked against CTO s.4 branch (a) spine only / (b) spine + tests file; key ETag reads a2b5f5980e9f66c9b1cfc2f67c8586dd (195,258 B); any other pipeline script in the list is raised, not closed over |  | OPEN |
| C1 | activation | mdpf-gold-lambda ONE real manual invoke ({} -> kind=manual, NOT qa_local) | invoke rc=0 and the run manifest read: a4_objects_built, data_as_of per scope, per-scope errors; outcome named as 16/16, 15/16 or 14/16 with every ABSENT by name (packet s.3) |  | OPEN |
| C2 | activation | opal-assets-mdpf-portal-publisher ONE manual invoke ({}) | invoke rc=0 and its publish manifest read: keys projected to opal-data-portal-v2/platinum/mdpf/* |  | OPEN |
| C3 | verify | served read + ping to Andrew | head-object of the served platinum/mdpf keys (LastModified after C2); the ping to Andrew naming scopes, dates, N of 16 and every per-scope ABSENT; Andrew's visual smoke is his act, not this leg's |  | OPEN |

## Log

- 20260922T151422Z OPENED by 0.7.0_AE_CloudOps~V with 8 leg(s)
