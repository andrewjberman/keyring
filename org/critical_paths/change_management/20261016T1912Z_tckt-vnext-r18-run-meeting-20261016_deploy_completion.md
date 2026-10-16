# Deploy Completion Record
**Date opened:** 2026-10-16T19:12:18.234936+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T194120Z
**Deploy:** TCKT_VNEXT TO-R18-RUN PART 1 (FWD-11, AMENDMENTS 5 and 6): ONE Meeting Request on the reused localhost:5174 server; synthetic filer tckt-r18-filer-20261016 and coordinator tckt-r18-coord-20261016 (@opal.invalid, allowedFirmIds [cottonwood]); ONE routing window on opal-ticket-api ROUTING_MATRIX meeting_request.primary set to the coordinator alone then restored to jeanette alone; pair blobs 000c3467f5 / 5e89bca0c2 / cf7c856072, criterion d4a45af2d5
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | four blobs, start gate items 1 to 4 and the reused server's checkout read by the applier | all true and printed | 4 of 4 blobs equal at worktree, HEAD and GO commit (pair 000c3467f5, CTO half 5e89bca0c2, CTO amendment-1 half cf7c856072, criterion d4a45af2d5); REL-OK; routing meeting_request.primary jeanette alone; portal origin/DEV fcbf2bcecb carries c05e3dda and 12c164a0; the 5174 server's checkout C:/dev/smoke-template-5174 HEAD 1779d67606 carries c05e3dda, 12c164a0, dc057891b086, 0 dirty rows, GET / 200; sweep 89 trees read, 0 read failures, shared tree has no open entry naming opal-ticket-api, opal-tickets or opal-users-v2; server_reused true (not started, not stopped) | CLOSED 20261016T191330Z |
| M1 | activation | filer identity row written with attribute_not_exists(PK), ConsistentRead PRESENT, ONE token minted in memory | iat and exp recorded, exp at most 20 minutes | filer row tckt-r18-filer-20261016@opal.invalid written attribute_not_exists(PK), ConsistentRead PRESENT allowedFirmIds [cottonwood], no scope_all_firms; ONE token iat 2026-10-16T19:19:08Z exp 2026-10-16T19:38:08Z (life 1140s, held in memory only); coordinator row minted the same way at 19:20:28Z exp 19:39:28Z | CLOSED 20261016T192924Z |
| W1 | activation | routing window opened: scratch copy of the stack, plan shows ONE attribute change, safe-apply, ROUTING_MATRIX read back | meeting_request.primary equals the coordinator alone | scratch copy of the stack (main.tf differs from committed blob 748e680fd7f8 in one line); plan: 0 to add, 1 to change, 0 to destroy, only ROUTING_MATRIX meeting_request.primary jeanette -> tckt-r18-coord-20261016@opal.invalid; safe-apply rc=0 at 19:23:42Z; read back routing_during = coordinator alone; CodeSha256 unchanged | CLOSED 20261016T192924Z |
| F1 | activation | the Meeting Request filed in the browser on http://localhost:5174 by the filer | ticket open, ticket_type meeting_request, routing.primary equals the coordinator alone | filer filed ONE Meeting Request in the browser on http://localhost:5174 (page origin printed): ticket TCK-20261016-9d7654eb, ConsistentRead type meeting_request status open routing.primary [coordinator alone]; CREATE log token WE_DL_UNCONFIGURED only (no SENT) | CLOSED 20261016T192924Z |
| C1 | activation | coordinator confirms ONE proposed time in the browser | meeting.status confirmed, meeting.time the clicked one, meeting.by the coordinator, ticket status open | coordinator context (page origin http://localhost:5174) pressed Confirm for the first proposed time, http 200; ConsistentRead meeting.status confirmed, meeting.time '2026-10-21 14:00 ET (R18 run 20261016)', meeting.by tckt-r18-coord-20261016@opal.invalid, ticket status open; no WE_* token on the confirm | CLOSED 20261016T192925Z |
| W2 | activation | routing window closed: committed tree re-applied under safe-apply | ROUTING_MATRIX read back meeting_request.primary equals jeanette alone | committed tree (main.tf blob 748e680fd7f8, clean) planned: 0 to add, 1 to change, 0 to destroy, only coordinator -> jeanette; safe-apply rc=0 at 19:28:01Z; read back routing_after meeting_request.primary = [jeanette@opalinvest.com] alone, CodeSha256 unchanged; window open 19:23:42Z to 19:28:01Z | CLOSED 20261016T192925Z |
| R1 | verify | both identity rows deleted after the later exp | each read ABSENT with ConsistentRead | both rows deleted at 2026-10-16T19:39:33Z, after the later token exp 2026-10-16T19:39:28Z (filer exp 19:38:08Z); ConsistentRead ABSENT for tckt-r18-filer-20261016 and tckt-r18-coord-20261016 (R18_RUN_PART1_TRACE.json) | CLOSED 20261016T194120Z |
| V1 | verify | r18_run_check_meeting.py | RUN-OK (meeting only) | r18_run_check_meeting.py (blob d4a45af2d5): RUN-OK (meeting only) meeting confirmed by the synthetic coordinator inside a routing window now restored; both identity rows absent | CLOSED 20261016T194120Z |

## Log

- 20261016T191218Z OPENED by 0.7.0_AE_CloudOps~TV2 with 8 leg(s)
- 20261016T191330Z LEG S1 closed: 4 of 4 blobs equal at worktree, HEAD and GO commit (pair 000c3467f5, CTO half 5e89bca0c2, CTO amendment-1 half cf7c85607
- 20261016T192924Z LEG M1 closed: filer row tckt-r18-filer-20261016@opal.invalid written attribute_not_exists(PK), ConsistentRead PRESENT allowedFirmIds [
- 20261016T192924Z LEG W1 closed: scratch copy of the stack (main.tf differs from committed blob 748e680fd7f8 in one line); plan: 0 to add, 1 to change, 0
- 20261016T192924Z LEG F1 closed: filer filed ONE Meeting Request in the browser on http://localhost:5174 (page origin printed): ticket TCK-20261016-9d765
- 20261016T192925Z LEG C1 closed: coordinator context (page origin http://localhost:5174) pressed Confirm for the first proposed time, http 200; Consisten
- 20261016T192925Z LEG W2 closed: committed tree (main.tf blob 748e680fd7f8, clean) planned: 0 to add, 1 to change, 0 to destroy, only coordinator -> jean
- 20261016T194120Z LEG R1 closed: both rows deleted at 2026-10-16T19:39:33Z, after the later token exp 2026-10-16T19:39:28Z (filer exp 19:38:08Z); Consist
- 20261016T194120Z LEG V1 closed: r18_run_check_meeting.py (blob d4a45af2d5): RUN-OK (meeting only) meeting confirmed by the synthetic coordinator inside 
- 20261016T194120Z CLOSED -- all 8 legs proven
