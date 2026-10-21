# Deploy Completion Record
**Date opened:** 2026-10-21T03:01:57.860228+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T031218Z
**Deploy:** TCKT_VNEXT TO-R23-F51 AMENDMENT 1 re-run (GO msg 11795; CTO ruling 11794 on S65): FWD-5 exercised ONCE on DEV (http://localhost:5174) with STAFF-SHAPED identities (rows: firmId opal-capital, scope_all_firms BOOL true, no allowedFirmIds): filer files a Service Request and an Other ticket, the picker (separate context) claims one FROM THE BOARD without opening either; both tickets saved whole then deleted by key after exp, both rows deleted; surfaces: opal-tickets (2 created, 1 claimed, deleted), opal-users-v2 (2 rows created, deleted); no S3 write; no PROD origin; check d4c6c9680c; if the create still returns 400 the body is captured and the run stops (S65 a product defect)
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | gate re-read: census, served HEAD, type list, rows ABSENT, protected tickets, open count | all printed | gate re-read 03:02:57Z: served tree HEAD 539b1ee70ba1 clean; rows ABSENT; protected tickets present; open tickets on the table 1 of 38; census as for f51 (no other live ledger on the surfaces) | CLOSED 20261021T031217Z |
| M1 | activation | two staff-shaped identity rows written attribute_not_exists(PK), PRESENT; two tokens in memory | iat and exp at most 20 min | 03:02:58Z two STAFF-SHAPED rows written attribute_not_exists(PK), ConsistentRead PRESENT firmId opal-capital, scope_all_firms BOOL true, no allowedFirmIds; two tokens in memory exp 03:10:58Z; both rows deleted 03:11:03Z, ConsistentRead ABSENT. Token note: tier internal, the authorizer computes allowedFirmIds=ALL, no claim in the token | CLOSED 20261021T031217Z |
| F1 | activation | filer files one service_request and one other ticket on DEV | two ticket ids, no engine call | Service Request create SUCCEEDED: TCK-20261021-c31f5347 service_request open by the filer 03:03:05Z (S65 resolved: the identity shape was the cause, MEASURED). The script then STOPPED 03:03:05Z: the create response id was not captured because the page notice beat my response listener (script defect, fixed: id read back from the table). No Other ticket filed. The ticket was found by the removal census and deleted by key 03:11:03Z WITHOUT being saved whole first (a disclosed omission on a stopped run) | CLOSED 20261021T031217Z |
| C1 | activation | picker reads the full board, shot r23_board_full, claims one from the board, shot r23_board_claimed | chosen in_progress under picker, other open unassigned | NOT REACHED: no second ticket, no picker session, no claim, no shot | CLOSED 20261021T031217Z |
| D1 | verify | both tickets saved whole then deleted by key after both exp; both rows deleted; each ABSENT | 404 only | 03:11:03Z after both exp: TCK-20261021-c31f5347 deleted by key (condition created_by the filer), both rows deleted; ConsistentRead ABSENT for all three, re-read 03:11:22Z; protected tickets and Andrew's TCK-20261020-b1d61f80 present | CLOSED 20261021T031218Z |
| V1 | verify | r23_fwd5_check.py with its self-test | RUN-OK (fwd5) | r23_fwd5_check.py NOT RUN: no result file (the run stopped at the first create's id capture). Ledger closed STOPPED at F1, FWD-5 UNPROVEN; the CTO (11808) and V2 (11809) authorized one more run under f51c | CLOSED 20261021T031218Z |

## Log

- 20261021T030157Z OPENED by 0.7.0_AE_CloudOps~TV2 with 6 leg(s)
- 20261021T031217Z LEG S1 closed: gate re-read 03:02:57Z: served tree HEAD 539b1ee70ba1 clean; rows ABSENT; protected tickets present; open tickets on the
- 20261021T031217Z LEG M1 closed: 03:02:58Z two STAFF-SHAPED rows written attribute_not_exists(PK), ConsistentRead PRESENT firmId opal-capital, scope_all_
- 20261021T031217Z LEG F1 closed: Service Request create SUCCEEDED: TCK-20261021-c31f5347 service_request open by the filer 03:03:05Z (S65 resolved: the i
- 20261021T031217Z LEG C1 closed: NOT REACHED: no second ticket, no picker session, no claim, no shot
- 20261021T031218Z LEG D1 closed: 03:11:03Z after both exp: TCK-20261021-c31f5347 deleted by key (condition created_by the filer), both rows deleted; Cons
- 20261021T031218Z LEG V1 closed: r23_fwd5_check.py NOT RUN: no result file (the run stopped at the first create's id capture). Ledger closed STOPPED at F
- 20261021T031218Z CLOSED -- all 6 legs proven
