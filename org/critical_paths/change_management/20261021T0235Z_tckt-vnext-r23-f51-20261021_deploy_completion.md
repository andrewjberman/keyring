# Deploy Completion Record
**Date opened:** 2026-10-21T02:35:24.715857+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T025432Z
**Deploy:** TCKT_VNEXT TO-R23-F51 (GO msg 11773; CVO ADJUDICATION_v21 via CTO 11772): FWD-5 exercised ONCE on DEV (http://localhost:5174): two synthetic internal identities (filer, picker) in opal-users-v2, two tickets of different types (service_request, other) filed by the filer, the picker claims one FROM THE BOARD without opening either; both tickets saved whole then deleted by key after exp, both identity rows deleted; surfaces: opal-tickets (2 items created, 1 claimed, deleted), opal-users-v2 (2 rows created, deleted); no S3 write, no PROD origin; check d4c6c9680c
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | check-inbox, census, DEV served tree HEAD, type list, board reads, IB2 notice, rows ABSENT, protected tickets present, open count | all printed | GO 11773 read; check d4c6c9680c (selftest to run at close); census 50 trees, 149 distinct names, the only OPEN naming opal-ticket-api/opal-tickets/opal-users-v2 is this ledger (others CLOSED: r21-rb1b, r18-run-meeting, irpt-ycg-r33, irpt-fwd1-run); 02:40Z Wed outside the 11:30Z-14:15Z band; served tree C:/dev/smoke-template-5174 HEAD 539b1ee70ba1 (clean, the CTO's vite, run as served per V2 11777), workspace portal DEV HEAD fcbf2bce, origin/DEV fb5f5796, 29 TicketCenter files behind; served TICKET_TYPE_LABELS carries Service Request and Other; IB2 told (7H in flight on its own PROD ticket, shares no write: 11778); both identity keys ABSENT, protected tickets present, open tickets on the table before: 1 of 38 | CLOSED 20261021T025431Z |
| M1 | activation | two identity rows written attribute_not_exists(PK), PRESENT ConsistentRead; two tokens in memory | iat and exp at most 20 min | 02:41:27Z two rows written attribute_not_exists(PK), ConsistentRead PRESENT allowedFirmIds [cottonwood]; two tokens in memory exp 02:49:27Z life 480 s, never printed; both rows deleted 02:49:32Z after exp, ConsistentRead ABSENT. (A first run stopped at 02:40:26Z in preflight on a label pattern for single quotes vs the served double quotes: nothing written.) | CLOSED 20261021T025431Z |
| F1 | activation | filer files one service_request and one other ticket on DEV | two ticket ids, no engine call | STOPPED AT THE FIRST CREATE: the filer pressed Create Ticket (Service Request) 02:41:3xZ; POST /api/scoped/tickets returned HTTP 400; no ticket created (scan 02:42:49Z and removal census 02:49:32Z: 38 tickets, 0 by the filer). Cause read from source not measured: untyped create takes the firm from the token firmId (opal-capital) and checks it against allowedFirmIds [cottonwood]; the page form sends no requester_firm. Surprise row TCKT_VNEXT-D2-S65. FWD-5 not exercised. | CLOSED 20261021T025431Z |
| C1 | activation | picker reads the full board, shot r23_board_full, claims one from the board, shot r23_board_claimed | chosen ticket in_progress under picker, other open unassigned | NOT REACHED: no second ticket, no picker session, no claim, no shot (the run stopped at the first create). Nothing claimed; the board was not touched. | CLOSED 20261021T025431Z |
| D1 | verify | both tickets saved whole then deleted by key after both exp; both rows deleted; each ABSENT | 404 only | removal after both exp: 0 tickets to delete (census: 0 created_by the filer), both identity rows deleted 02:49:32Z, ConsistentRead ABSENT; protected tickets untouched | CLOSED 20261021T025432Z |
| V1 | verify | r23_fwd5_check.py with its self-test | RUN-OK (fwd5) | r23_fwd5_check.py NOT RUN: no R23_FWD5_RESULT.json exists (the run stopped at the first create); it would print RUN-BAD cannot read the result file or the saved ticket records. Ledger closed STOPPED at F1, FWD-5 UNPROVEN, per the order: remove what the run created, report the world as left, file a surprise row | CLOSED 20261021T025432Z |

## Log

- 20261021T023524Z OPENED by 0.7.0_AE_CloudOps~TV2 with 6 leg(s)
- 20261021T025431Z LEG S1 closed: GO 11773 read; check d4c6c9680c (selftest to run at close); census 50 trees, 149 distinct names, the only OPEN naming op
- 20261021T025431Z LEG M1 closed: 02:41:27Z two rows written attribute_not_exists(PK), ConsistentRead PRESENT allowedFirmIds [cottonwood]; two tokens in m
- 20261021T025431Z LEG F1 closed: STOPPED AT THE FIRST CREATE: the filer pressed Create Ticket (Service Request) 02:41:3xZ; POST /api/scoped/tickets retur
- 20261021T025431Z LEG C1 closed: NOT REACHED: no second ticket, no picker session, no claim, no shot (the run stopped at the first create). Nothing claim
- 20261021T025432Z LEG D1 closed: removal after both exp: 0 tickets to delete (census: 0 created_by the filer), both identity rows deleted 02:49:32Z, Cons
- 20261021T025432Z LEG V1 closed: r23_fwd5_check.py NOT RUN: no R23_FWD5_RESULT.json exists (the run stopped at the first create); it would print RUN-BAD 
- 20261021T025432Z CLOSED -- all 6 legs proven
