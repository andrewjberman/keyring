# Deploy Completion Record
**Date opened:** 2026-10-21T03:12:31.167516+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T032233Z
**Deploy:** TCKT_VNEXT TO-R23-F51 AMENDMENT 2 (V2 GO 11809; CTO 11808): the ONE more FWD-5 run on DEV (http://localhost:5174), staff-shaped identities (firmId opal-capital, scope_all_firms BOOL true, no allowedFirmIds), ticket ids read back from the table: filer files a Service Request and an Other ticket, the picker (separate context) claims one FROM THE BOARD without opening either; both tickets saved whole then deleted by key after exp, both rows deleted; earlier attempts recorded in the result; surfaces opal-tickets (2 created, 1 claimed, deleted), opal-users-v2 (2 rows created, deleted); no S3, no PROD; check d4c6c9680c; no third run without a word
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | precondition: TCK-20261021-c31f5347 and both rows ABSENT; gate re-read | all printed | CTO precondition (11808) read 03:11:22Z: TCK-20261021-c31f5347 and both rows ABSENT (ConsistentRead); protected tickets and Andrew's TCK-20261020-b1d61f80 present; gate re-read 03:13:00Z: served HEAD 539b1ee70ba1 clean, rows ABSENT, open tickets on the table 1 of 38 | CLOSED 20261021T032232Z |
| M1 | activation | two staff-shaped rows written, PRESENT; two tokens in memory | iat and exp at most 20 min | 03:13:00Z two staff-shaped rows written (firmId opal-capital, scope_all_firms BOOL true, no allowedFirmIds), PRESENT; two tokens in memory exp 03:21:00Z, never printed; rows deleted 03:21:05Z, ConsistentRead ABSENT | CLOSED 20261021T032232Z |
| F1 | activation | filer files one service_request and one other ticket; ids read back | two ticket ids, no engine call | filer filed TCK-20261021-f3e6a614 (service_request, 03:13:16Z) and TCK-20261021-4606de92 (other, 03:13:26Z) through the page's New Ticket form; both ids read back from opal-tickets (the response listener lagged the page notice); no engine call; no third ticket | CLOSED 20261021T032233Z |
| C1 | activation | picker reads the full board, shot r23_board_full, claims one from the board, shot r23_board_claimed | chosen in_progress under picker, other open unassigned | picker (separate context) read both rows from the board as text (Service Request and Other, age under a minute, Claim control present), chose f3e6a614, pressed Claim in its row WITHOUT opening either ticket: POST claim status 200 (03:13:28Z); items saved whole by hand 03:14:10Z (R23_FWD5_TICKET_ITEMS.json): chosen in_progress under the picker, events created then claimed; other open, unassigned, events created. SHOTS: both full-page PNGs taken and then DELETED at step (f): the board also renders Andrew's real open analysis request's expanded panels (firm, household identifier, advisor name, commentary draft) and staff addresses, beyond the five allowed columns; not committed. Surprise row TCKT_VNEXT-D2-S66 | CLOSED 20261021T032233Z |
| D1 | verify | both tickets saved whole then deleted by key after both exp; both rows deleted; each ABSENT | 404 only | 03:21:05Z after both exp: the two tickets deleted by key (condition created_by the filer) and both rows deleted; ConsistentRead ABSENT for all four, re-read 03:21:30Z; protected tickets and Andrew's ticket present; no PNG left in the deliverables folder | CLOSED 20261021T032233Z |
| V1 | verify | r23_fwd5_check.py with its self-test | RUN-OK (fwd5) | r23_fwd5_check.py NOT RUN: no R23_FWD5_RESULT.json and no shots (step (f) STOP, shots deleted). It would print RUN-BAD cannot read the result file or the saved ticket records... Ledger closed STOPPED at the shot review; FWD-5 behaviour measured (claim 200 from the board, records saved), visual evidence not committable; no third run without a word (CTO 11808) | CLOSED 20261021T032233Z |

## Log

- 20261021T031231Z OPENED by 0.7.0_AE_CloudOps~TV2 with 6 leg(s)
- 20261021T032232Z LEG S1 closed: CTO precondition (11808) read 03:11:22Z: TCK-20261021-c31f5347 and both rows ABSENT (ConsistentRead); protected tickets 
- 20261021T032232Z LEG M1 closed: 03:13:00Z two staff-shaped rows written (firmId opal-capital, scope_all_firms BOOL true, no allowedFirmIds), PRESENT; tw
- 20261021T032233Z LEG F1 closed: filer filed TCK-20261021-f3e6a614 (service_request, 03:13:16Z) and TCK-20261021-4606de92 (other, 03:13:26Z) through the 
- 20261021T032233Z LEG C1 closed: picker (separate context) read both rows from the board as text (Service Request and Other, age under a minute, Claim co
- 20261021T032233Z LEG D1 closed: 03:21:05Z after both exp: the two tickets deleted by key (condition created_by the filer) and both rows deleted; Consist
- 20261021T032233Z LEG V1 closed: r23_fwd5_check.py NOT RUN: no R23_FWD5_RESULT.json and no shots (step (f) STOP, shots deleted). It would print RUN-BAD c
- 20261021T032233Z CLOSED -- all 6 legs proven
