# Deploy Completion Record
**Date opened:** 2026-09-23T06:31:31.264662+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: sovereign / Andrew authenticated CloudFront scope and browse smoke on portal-v2.1.185 (held since 2026-09-23T06:46:58.968906+00:00)
**Deploy:** IRPT P bounded live scope repair and canonical Portal publication
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| API | activation | two IRPT CUSTOM routes | exact route bindings and zero diff | Exact plan1ff3899e:2create0change0destroy; live4ybqnt2 GETbrowse and k8em63s POSTselections both CUSTOMnaqxlm integrations/g9302sp; targeted replan exit0 no changes. | CLOSED 20260923T063245Z |
| RECORD | git | scoped deploy records | committed ledger map changelog receipt | Scoped map, directory/API changelogs, live receipts and open sentinel committed0da45df0c6e185aa7dbe6d877b2202121f85f259; MSTR readback originCLOUD equals0da45df0. Recorder exception1c686165e1. | CLOSED 20260923T064350Z |
| DEV | git | Portal DEV and backend CLOUD | MSTR pushed ancestry-preserving pins | MSTR99646 published Portal originDEV fac3b6a0c7cb55dd75d3c190a1382ce710030381 and backend originCLOUD0da45df0c6e185aa7dbe6d877b2202121f85f259. Preserves prior shared ancestors; frontend tree identical reviewed dcf5; DEV CI35827638465 SUCCESS. | CLOSED 20260923T064350Z |
| PROD | activation | canonical Portal PROD | successful deploy CI and peeled tag | Canonical PROD a0690a03d7bee06380fec8a49159fa78761fa985; peeled tag portal-v2.1.185 equals PROD; exactsha workflow35828019440 Build/DeployS3CloudFront/Tag SUCCESS. CloudFront www.opalinvest.dev index and6referencedassets HTTP200 byte-identical CI artifact. | CLOSED 20260923T064658Z |
| HTTP | verify | CloudFront authenticated scope browse | legitimate authorized HTTP and Andrew smoke |  | OPEN |
| irpt-directory-search | tf-lambda | module.irpt_directory_search.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | CTO f6f34824d4 exact plan d5307a61:1create1update0destroy; replan exit0 no changes; live CodeSha256 iqLKa1RWk9hlcSlAheuoAMgIY4R3VrStPX1eG5Qwq/s= Active Successful; S3 version RXChd66RsDjV1jhG1ZsFlOGnXeIDxApp bytes17/17 matched. Authenticated HTTP is separate OPEN leg. | CLOSED 20260923T063245Z |

## Log

- 20260923T063131Z OPENED by 2.0.0_SA_COO~P with 6 leg(s)
- 20260923T063245Z LEG irpt-directory-search closed: CTO f6f34824d4 exact plan d5307a61:1create1update0destroy; replan exit0 no changes; live CodeSha256 iqLKa1RWk9hlcSlAheuo
- 20260923T063245Z LEG API closed: Exact plan1ff3899e:2create0change0destroy; live4ybqnt2 GETbrowse and k8em63s POSTselections both CUSTOMnaqxlm integratio
- 20260923T064350Z LEG RECORD closed: Scoped map, directory/API changelogs, live receipts and open sentinel committed0da45df0c6e185aa7dbe6d877b2202121f85f259;
- 20260923T064350Z LEG DEV closed: MSTR99646 published Portal originDEV fac3b6a0c7cb55dd75d3c190a1382ce710030381 and backend originCLOUD0da45df0c6e185aa7db
- 20260923T064658Z LEG PROD closed: Canonical PROD a0690a03d7bee06380fec8a49159fa78761fa985; peeled tag portal-v2.1.185 equals PROD; exactsha workflow358280
- 20260923T064658Z HELD-SOVEREIGN-GATED gate=sovereign/Andrew authenticated CloudFront scope and browse smoke on portal-v2.1.185
