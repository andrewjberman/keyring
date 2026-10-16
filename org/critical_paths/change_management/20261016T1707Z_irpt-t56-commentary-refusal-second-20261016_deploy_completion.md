# Deploy Completion Record
**Date opened:** 2026-10-16T17:07:35.851195+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-t56 (AR-tf-79): ONE direct refused-body invoke of outlook-global-commentary-draft-lambda on the synthetic row REQ-d47252fe74634d0c5cdd8067 (irpt-jobs, tenant 49financial) so the live fail op sets hop_failure COMMENTARY/COMMENTARY_DRAFT_REFUSED; the attribute stays until 2.0.0_SA_COO~V2 reads the ticket page, then ONE conditional REMOVE of that attribute (leg B, on the issuer's message); PRE item sha256 e7ff82b5dc07..
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| LA1 | verify | preconditions: commentary digest I/6mirBT.., draft-store digest RizVjaXi.., row READY with hop_failure absent and PRE hash, ticket TCK-20261015-944c84f8 with no package pointer, r55 hopabsent OK | the printed reads |  | OPEN |
| LA2 | verify | ONE direct invoke (RequestResponse, payload t56-1 forced refusal): parsed answer failed WRONG_KIND and batchItemFailures t56-1; the log line HOP-FAILURE-REPORTED written=true a SECOND time; the row hop_failure COMMENTARY/COMMENTARY_DRAFT_REFUSED with its at stamp, state READY, item hash without the attribute equals PRE; r55 hoplog2 OK | the invoke time, the at value, the check lines |  | OPEN |
| LB1 | verify | leg B (only on the issuer's message): the ONE conditional REMOVE of hop_failure (condition: its code equals the recorded one), read back ABSENT, item sha256 equal to PRE, r55 hopabsent OK | the read-backs |  | OPEN |

## Log

- 20261016T170735Z OPENED by 0.7.0_AE_CloudOps~IB2 with 3 leg(s)
