# Deploy Completion Record
**Date opened:** 2026-10-05T14:53:11.753599+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND release r57: the r55 re-pin set to 4 functions (49f-reporting-read, export-render, directory-search, holdings); CTO half @3d6e1ed58c, COO half; irpt-status by ~Y
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| RR1 | verify | irpt-49f-reporting-read-lambda before-read = anchor + baseline invokes | CodeSha256 + payloads |  | OPEN |
| RR2 | activation | irpt-49f-reporting-read-lambda build+upload+targeted safe-apply | live CodeSha256 = built |  | OPEN |
| RR3 | verify | irpt-49f-reporting-read-lambda change + happy invokes | payloads |  | OPEN |
| ER1 | verify | irpt-export-render before-read = anchor + baseline invokes | CodeSha256 + payloads |  | OPEN |
| ER2 | activation | irpt-export-render build+upload+targeted safe-apply | live CodeSha256 = built |  | OPEN |
| ER3 | verify | irpt-export-render change + happy invokes | payloads |  | OPEN |
| DS1 | verify | irpt-directory-search before-read = anchor + baseline invokes | CodeSha256 + payloads |  | OPEN |
| DS2 | activation | irpt-directory-search build+upload+targeted safe-apply | live CodeSha256 = built |  | OPEN |
| DS3 | verify | irpt-directory-search change + happy invokes | payloads |  | OPEN |
| HO1 | verify | irpt-holdings before-read = anchor + baseline invokes | CodeSha256 + payloads |  | OPEN |
| HO2 | activation | irpt-holdings build+upload+targeted safe-apply | live CodeSha256 = built |  | OPEN |
| HO3 | verify | irpt-holdings change + happy invokes | payloads |  | OPEN |
| R1 | git | record-terraform-deploy per function | commit |  | OPEN |

## Log

- 20261005T145311Z OPENED by 2.0.0_SA_COO~P with 13 leg(s)
