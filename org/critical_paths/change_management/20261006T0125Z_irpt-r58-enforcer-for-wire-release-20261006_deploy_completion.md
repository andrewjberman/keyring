# Deploy Completion Record
**Date opened:** 2026-10-06T01:25:58.736521+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND release r58: the enforcer_for refusals reach the wire (served.py :1052, loaders.py :204) on 4 functions; CTO half @38fbca18a2; reporting-read + export-render first, directory-search + holdings on the CTO's go (condition 2)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| RR1 | verify | irpt-49f-reporting-read-lambda before-read = anchor j5R13Pnv + baseline invokes | CodeSha256 + payloads |  | OPEN |
| RR2 | activation | irpt-49f-reporting-read-lambda build, copy to the Terraform key irpt-reporting-read-lambda.zip, targeted safe-apply | live CodeSha256 = built; plan code hash only |  | OPEN |
| RR3 | verify | irpt-49f-reporting-read-lambda change invoke FIRM_BINDING on the wire + happy equals baseline | payloads + log classifier_code/exception_type |  | OPEN |
| ER1 | verify | irpt-export-render before-read = anchor QVZQo07b + head-object receipt + baseline invokes | CodeSha256 + payloads |  | OPEN |
| ER2 | activation | irpt-export-render build and targeted safe-apply | live CodeSha256 = built; plan code hash only |  | OPEN |
| ER3 | verify | irpt-export-render change invoke FIRM_BINDING + happy equals baseline | payloads + log |  | OPEN |
| DS1 | verify | irpt-directory-search before-read = anchor OmSwySst + baseline invokes (after the CTO go) | CodeSha256 + payloads |  | OPEN |
| DS2 | activation | irpt-directory-search build and targeted safe-apply | live CodeSha256 = built; plan code hash only |  | OPEN |
| DS3 | verify | irpt-directory-search change invoke FIRM_BINDING + happy equals baseline | payloads + log |  | OPEN |
| HO1 | verify | irpt-holdings before-read = anchor skOqPofT + baseline invokes (after the CTO go) | CodeSha256 + payloads |  | OPEN |
| HO2 | activation | irpt-holdings build and targeted safe-apply | live CodeSha256 = built; plan code hash only |  | OPEN |
| HO3 | verify | irpt-holdings change invoke FIRM_BINDING + happy baseline-equality (placeholder selection) | payloads + log |  | OPEN |
| R1 | git | record-terraform-deploy per function | commit |  | OPEN |

## Log

- 20261006T012558Z OPENED by 2.0.0_SA_COO~P with 13 leg(s)
