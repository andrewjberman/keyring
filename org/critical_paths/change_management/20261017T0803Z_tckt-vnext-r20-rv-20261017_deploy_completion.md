# Deploy Completion Record
**Date opened:** 2026-10-17T08:03:29.273425+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT TO-R20-RV (AMENDMENT 2, GO msg 10369; run pair AMENDMENT 5): ONE live Meeting Request journey read in the RENDERED page on the CTO's 5174 server (DEV 38d4f9473284); three synthetic identities tckt-r20-filer/coord/view-20261017 (@opal.invalid, allowedFirmIds [cottonwood]); ONE routing window on opal-ticket-api ROUTING_MATRIX meeting_request.primary (coordinator alone, then jeanette alone); claim+complete of ONE synthetic ticket; six screenshots; surfaces: ticket service, opal-tickets, opal-users-v2, Lambda ROUTING_MATRIX; pair blobs 08c9ba4bb2 / 098b12581d, check eace42e468
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | blobs and the start gate (served sha, cell in origin/DEV, origin, routing, census, asks to CTO, Y2 and IB2) | all true and printed |  | OPEN |
| M1 | activation | three identity rows written with attribute_not_exists(PK) and read PRESENT; ONE token each in memory | iat and exp recorded, each at most 20 minutes |  | OPEN |
| W1 | activation | routing window opened: scratch copy, plan ONE attribute change, safe-apply, read back | meeting_request.primary equals the coordinator alone |  | OPEN |
| F1 | activation | the filer files ONE Meeting Request in the browser on http://localhost:5174; shot filer_waiting | ticket open, routing.primary the coordinator alone |  | OPEN |
| C1 | activation | coordinator confirms ONE proposed time in the browser | meeting.status confirmed, meeting.by the coordinator, ticket open |  | OPEN |
| W2 | activation | routing window closed: committed tree re-applied under safe-apply | meeting_request.primary equals jeanette alone |  | OPEN |
| X1 | verify | shots filer_confirmed, coordinator_controls, bystander_no_control saved | three PNGs with recorded sizes |  | OPEN |
| T1 | activation | claim and complete of the ONE synthetic ticket; shot filer_completed | ticket completed, no SENT token |  | OPEN |
| G1 | verify | shot meeting_form (New Ticket, Meeting Request, not submitted) | PNG with recorded size |  | OPEN |
| R1 | verify | three identity rows deleted after the longest exp | each ConsistentRead ABSENT |  | OPEN |
| V1 | verify | r20_run_check.py | RUN-OK (render) |  | OPEN |

## Log

- 20261017T080329Z OPENED by 0.7.0_AE_CloudOps~TV2 with 11 leg(s)
