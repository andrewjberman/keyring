# Deploy Completion Record
**Date opened:** 2026-10-16T17:07:35.851195+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T173007Z
**Deploy:** IRPT_ANLREQ TO-APPLY-t56 (AR-tf-79): ONE direct refused-body invoke of outlook-global-commentary-draft-lambda on the synthetic row REQ-d47252fe74634d0c5cdd8067 (irpt-jobs, tenant 49financial) so the live fail op sets hop_failure COMMENTARY/COMMENTARY_DRAFT_REFUSED; the attribute stays until 2.0.0_SA_COO~V2 reads the ticket page, then ONE conditional REMOVE of that attribute (leg B, on the issuer's message); PRE item sha256 e7ff82b5dc07..
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| LA1 | verify | preconditions: commentary digest I/6mirBT.., draft-store digest RizVjaXi.., row READY with hop_failure absent and PRE hash, ticket TCK-20261015-944c84f8 with no package pointer, r55 hopabsent OK | the printed reads | commentary digest I/6mirBT.. and draft-store digest RizVjaXi.. read; row REQ-d47252fe.. exists, state READY, hop_failure absent, 11 attributes, PRE sha256 e7ff82b5dc0725f1 (canonical item as returned, consistent read); ticket TCK-20261015-944c84f8 carries no package or report pointer; r55_checks hopabsent printed R55-HOPABSENT-OK; ledgers 2021 read and worktrees 82 of 82 with 1599 marker files: no OPEN entry names the function, the draft-store, the row or hop_failure (t54 and t55 are closed) | CLOSED 20261016T170757Z |
| LA2 | verify | ONE direct invoke (RequestResponse, payload t56-1 forced refusal): parsed answer failed WRONG_KIND and batchItemFailures t56-1; the log line HOP-FAILURE-REPORTED written=true a SECOND time; the row hop_failure COMMENTARY/COMMENTARY_DRAFT_REFUSED with its at stamp, state READY, item hash without the attribute equals PRE; r55 hoplog2 OK | the invoke time, the at value, the check lines | ONE direct invoke 2026-10-16T17:08:24Z, StatusCode 200, parsed: results empty, failed 1 (reason WRONG_KIND), batchItemFailures t56-1 (a direct invoke: no SQS message exists, nothing redelivered, no dead-letter entry); log line HOP-FAILURE-REPORTED request_id=REQ-d47252fe.. hop=COMMENTARY code=COMMENTARY_DRAFT_REFUSED written=true at 17:08:33Z, the SECOND time; row read 17:09Z: hop_failure keys at, code, hop = COMMENTARY, COMMENTARY_DRAFT_REFUSED, at 2026-10-16T17:08:33Z; state READY; item sha256 without hop_failure e7ff82b5dc07.. equals PRE; r55 hoplog2 printed R55-HOPLOG2-OK events_with_line=2 need=2. The attribute is NOT removed; the ledger stays OPEN for leg B | CLOSED 20261016T170934Z |
| LB1 | verify | leg B (only on the issuer's message): the ONE conditional REMOVE of hop_failure (condition: its code equals the recorded one), read back ABSENT, item sha256 equal to PRE, r55 hopabsent OK | the read-backs | leg B 2026-10-16T17:29Z on the issuer's message (T2 msg 9706) after V2's page read: ONE conditional REMOVE of hop_failure (condition code = COMMENTARY_DRAFT_REFUSED; recorded value hop COMMENTARY, code COMMENTARY_DRAFT_REFUSED, at 2026-10-16T17:08:33Z); read back ABSENT; state READY; 11 attributes; item sha256 e7ff82b5dc0725f1 equals PRE; r55 hopabsent printed R55-HOPABSENT-OK | CLOSED 20261016T173007Z |

## Log

- 20261016T170735Z OPENED by 0.7.0_AE_CloudOps~IB2 with 3 leg(s)
- 20261016T170757Z LEG LA1 closed: commentary digest I/6mirBT.. and draft-store digest RizVjaXi.. read; row REQ-d47252fe.. exists, state READY, hop_failure
- 20261016T170934Z LEG LA2 closed: ONE direct invoke 2026-10-16T17:08:24Z, StatusCode 200, parsed: results empty, failed 1 (reason WRONG_KIND), batchItemFa
- 20261016T173007Z LEG LB1 closed: leg B 2026-10-16T17:29Z on the issuer's message (T2 msg 9706) after V2's page read: ONE conditional REMOVE of hop_failur
- 20261016T173007Z CLOSED -- all 3 legs proven
