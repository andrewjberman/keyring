# Deploy Completion Record
**Date opened:** 2026-10-14T03:32:04.830293+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-EXERCISE-R28: release-28 synthetic sitting (FA 49financial, CW cottonwood, svc-irpt-packager) against opal-ticket-api and the upload door; two users rows and one partner row for the sitting, removed after exp; one synthetic ticket stays; pair COO blob e9bb20d7fe + CTO half @d3adae2fc8, AMENDMENTS 1-2
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | activation | step 1 reads (COO half hash, three legs at expected CodeSha256, grants, census); FA and CW keys and GSI ABSENT; write FA and CW users rows and the FA partner row (attribute_not_exists); read back; mint one token per identity (FA, CW, PK), memory only | rows PRESENT, tokens minted |  | OPEN |
| T4 | verify | T4a, T4b, LIST-A, LIST-B, GET-B (status, code, body sha256 only) | per-request record |  | OPEN |
| D | verify | D1 to D4 through the upload door as FA, then C1 parseIrEnvelope from portal origin/PROD | per-arm record |  | OPEN |
| P5 | verify | PKG-1, PKG-2, PKG-3 as svc-irpt-packager; report_ref once; item sha unchanged on 2 and 3; per-window invocation and token counts | per-request record |  | OPEN |
| X | activation | after the later exp: delete the written rows (attribute_exists); FA and CW ABSENT by GSI and ConsistentRead (bounded 5 min); partner row ABSENT | four ABSENT lines |  | OPEN |

## Log

- 20261014T033204Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 5 leg(s)
