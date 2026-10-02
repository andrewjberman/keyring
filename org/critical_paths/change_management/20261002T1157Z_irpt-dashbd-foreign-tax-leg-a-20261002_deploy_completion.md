# Deploy Completion Record
**Date opened:** 2026-10-02T11:57:39.504956+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T121821Z
**Deploy:** IRPT_DASHBD E3 leg (a): retire the adapter's foreign-tax override in account_return_daily.py + re-pin and redeploy irpt-49f-reporting-gold-lambda (output-neutral; packet blob 139ac6b40d, COO + CTO halves signed)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G1 | git | CLOUD commit of ADAPTER_OVERRIDE_RETIREMENT_R3.patch + source-map re-pin of producer AND table to one commit | commit hashes | 4ad4008907 (override retired, 7+/8-) + d8f56b9add (staged_from producer e1b160d340->4ad4008907 and Schwab table 5bb3b2626d->4ad4008907 together; only commits between: the patch and 4.0.0_SA_CRO 3cb9f9b6d5) | CLOSED 20261002T120729Z |
| B1 | activation | build-and-upload.sh investor-reporting irpt-reporting-gold-lambda | new artifact_sha256 in lambda-source-map.json | build-and-upload 12:05:25Z S3 version Q49yaWRJgeu02g5mceWkxH3If81hxAEG; artifact_sha256 RLOFPe0lYEBKKvQw69r8oqB5DeCfnZMBeukFJ0AZzN8= (zip read back: producer dec44e07c315 = pin blob, override absent; table 8b803eecfd14 = pin blob) | CLOSED 20261002T120729Z |
| P1 | verify | terraform plan of infra/aws/terraform/investor-reporting/reporting-gold | 0 to add, 1 to change (function code), 0 to destroy | terraform plan -lock=false at CLOUD 5ed86ef046 (12:0xZ): Plan: 0 to add, 1 to change, 0 to destroy -- module.irpt_reporting_gold.aws_lambda_function.this s3_object_version 2xWk24l9wR8n7T2kFmL00H4Ys_.FT88z -> Q49yaWRJgeu02g5mceWkxH3If81hxAEG, source_code_hash 7eCQtWhs... -> RLOFPe0l...; saved as lega.tfplan | CLOSED 20261002T121506Z |
| D1 | activation | targeted safe-apply of the reporting-gold root, saved plan | Apply complete 0/1/0 | HALT_ACK=1 .tools/safe-apply.sh apply lega.tfplan (12:17Z): 0 added, 1 changed, 0 destroyed -- the function's code only; outputs unchanged (schedule irpt-49f-reporting-gold-daily ENABLED, write ARN account_return_daily only) | CLOSED 20261002T121820Z |
| V1 | verify | get-function-configuration irpt-49f-reporting-gold-lambda + re-plan | CodeSha256 = map artifact_sha256; re-plan No changes | get-function-configuration irpt-49f-reporting-gold-lambda 12:17:33Z: CodeSha256 RLOFPe0lYEBKKvQw69r8oqB5DeCfnZMBeukFJ0AZzN8= (= map artifact_sha256), LastModified 2026-10-02T12:17:04Z, Active, Successful; terraform plan: No changes | CLOSED 20261002T121820Z |

## Log

- 20261002T115739Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20261002T120729Z LEG G1 closed: 4ad4008907 (override retired, 7+/8-) + d8f56b9add (staged_from producer e1b160d340->4ad4008907 and Schwab table 5bb3b262
- 20261002T120729Z LEG B1 closed: build-and-upload 12:05:25Z S3 version Q49yaWRJgeu02g5mceWkxH3If81hxAEG; artifact_sha256 RLOFPe0lYEBKKvQw69r8oqB5DeCfnZMB
- 20261002T121506Z LEG P1 closed: terraform plan -lock=false at CLOUD 5ed86ef046 (12:0xZ): Plan: 0 to add, 1 to change, 0 to destroy -- module.irpt_report
- 20261002T121820Z LEG D1 closed: HALT_ACK=1 .tools/safe-apply.sh apply lega.tfplan (12:17Z): 0 added, 1 changed, 0 destroyed -- the function's code only;
- 20261002T121820Z LEG V1 closed: get-function-configuration irpt-49f-reporting-gold-lambda 12:17:33Z: CodeSha256 RLOFPe0lYEBKKvQw69r8oqB5DeCfnZMBeukFJ0AZ
- 20261002T121821Z CLOSED -- all 5 legs proven
