# Deploy Completion Record
**Date opened:** 2026-09-23T06:31:31.264662+00:00
**Status:** OPEN
**Deploy:** IRPT P bounded live scope repair and canonical Portal publication
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| API | activation | two IRPT CUSTOM routes | exact route bindings and zero diff | Exact plan1ff3899e:2create0change0destroy; live4ybqnt2 GETbrowse and k8em63s POSTselections both CUSTOMnaqxlm integrations/g9302sp; targeted replan exit0 no changes. | CLOSED 20260923T063245Z |
| RECORD | git | scoped deploy records | committed ledger map changelog receipt |  | OPEN |
| DEV | git | Portal DEV and backend CLOUD | MSTR pushed ancestry-preserving pins |  | OPEN |
| PROD | activation | canonical Portal PROD | successful deploy CI and peeled tag |  | OPEN |
| HTTP | verify | CloudFront authenticated scope browse | legitimate authorized HTTP and Andrew smoke |  | OPEN |
| irpt-directory-search | tf-lambda | module.irpt_directory_search.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | CTO f6f34824d4 exact plan d5307a61:1create1update0destroy; replan exit0 no changes; live CodeSha256 iqLKa1RWk9hlcSlAheuoAMgIY4R3VrStPX1eG5Qwq/s= Active Successful; S3 version RXChd66RsDjV1jhG1ZsFlOGnXeIDxApp bytes17/17 matched. Authenticated HTTP is separate OPEN leg. | CLOSED 20260923T063245Z |

## Log

- 20260923T063131Z OPENED by 2.0.0_SA_COO~P with 6 leg(s)
- 20260923T063245Z LEG irpt-directory-search closed: CTO f6f34824d4 exact plan d5307a61:1create1update0destroy; replan exit0 no changes; live CodeSha256 iqLKa1RWk9hlcSlAheuo
- 20260923T063245Z LEG API closed: Exact plan1ff3899e:2create0change0destroy; live4ybqnt2 GETbrowse and k8em63s POSTselections both CUSTOMnaqxlm integratio
