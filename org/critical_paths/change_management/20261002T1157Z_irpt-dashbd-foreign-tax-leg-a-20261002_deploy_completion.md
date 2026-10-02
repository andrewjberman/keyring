# Deploy Completion Record
**Date opened:** 2026-10-02T11:57:39.504956+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD E3 leg (a): retire the adapter's foreign-tax override in account_return_daily.py + re-pin and redeploy irpt-49f-reporting-gold-lambda (output-neutral; packet blob 139ac6b40d, COO + CTO halves signed)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G1 | git | CLOUD commit of ADAPTER_OVERRIDE_RETIREMENT_R3.patch + source-map re-pin of producer AND table to one commit | commit hashes |  | OPEN |
| B1 | activation | build-and-upload.sh investor-reporting irpt-reporting-gold-lambda | new artifact_sha256 in lambda-source-map.json |  | OPEN |
| P1 | verify | terraform plan of infra/aws/terraform/investor-reporting/reporting-gold | 0 to add, 1 to change (function code), 0 to destroy |  | OPEN |
| D1 | activation | targeted safe-apply of the reporting-gold root, saved plan | Apply complete 0/1/0 |  | OPEN |
| V1 | verify | get-function-configuration irpt-49f-reporting-gold-lambda + re-plan | CodeSha256 = map artifact_sha256; re-plan No changes |  | OPEN |

## Log

- 20261002T115739Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
