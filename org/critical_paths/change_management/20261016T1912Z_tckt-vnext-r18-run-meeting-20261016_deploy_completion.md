# Deploy Completion Record
**Date opened:** 2026-10-16T19:12:18.234936+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT TO-R18-RUN PART 1 (FWD-11, AMENDMENTS 5 and 6): ONE Meeting Request on the reused localhost:5174 server; synthetic filer tckt-r18-filer-20261016 and coordinator tckt-r18-coord-20261016 (@opal.invalid, allowedFirmIds [cottonwood]); ONE routing window on opal-ticket-api ROUTING_MATRIX meeting_request.primary set to the coordinator alone then restored to jeanette alone; pair blobs 000c3467f5 / 5e89bca0c2 / cf7c856072, criterion d4a45af2d5
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | four blobs, start gate items 1 to 4 and the reused server's checkout read by the applier | all true and printed |  | OPEN |
| M1 | activation | filer identity row written with attribute_not_exists(PK), ConsistentRead PRESENT, ONE token minted in memory | iat and exp recorded, exp at most 20 minutes |  | OPEN |
| W1 | activation | routing window opened: scratch copy of the stack, plan shows ONE attribute change, safe-apply, ROUTING_MATRIX read back | meeting_request.primary equals the coordinator alone |  | OPEN |
| F1 | activation | the Meeting Request filed in the browser on http://localhost:5174 by the filer | ticket open, ticket_type meeting_request, routing.primary equals the coordinator alone |  | OPEN |
| C1 | activation | coordinator confirms ONE proposed time in the browser | meeting.status confirmed, meeting.time the clicked one, meeting.by the coordinator, ticket status open |  | OPEN |
| W2 | activation | routing window closed: committed tree re-applied under safe-apply | ROUTING_MATRIX read back meeting_request.primary equals jeanette alone |  | OPEN |
| R1 | verify | both identity rows deleted after the later exp | each read ABSENT with ConsistentRead |  | OPEN |
| V1 | verify | r18_run_check_meeting.py | RUN-OK (meeting only) |  | OPEN |

## Log

- 20261016T191218Z OPENED by 0.7.0_AE_CloudOps~TV2 with 8 leg(s)
