# Deploy Completion Record
**Date opened:** 2026-10-21T03:29:12.927090+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T034802Z
**Deploy:** TCKT_VNEXT TO-R23-F51 AMENDMENT 4 (V2 GO 11821; CTO ruling 11820): the ONE FINAL FWD-5 run on DEV (http://localhost:5174), staff-shaped identities, ids read back from the table: filer files a Service Request and an Other ticket, the picker (separate context) claims one FROM THE BOARD without opening either; full-board shots go OUTSIDE the repo (C:/dev/_tckt_private_evidence/r23_f51/, sha256 only in the result), committed shots are clipped to the two synthetic rows and read for client data before written; both tickets saved whole then deleted by key after exp, both rows deleted; surfaces opal-tickets (2 created, 1 claimed, deleted), opal-users-v2 (2 rows created, deleted); no S3, no PROD; check 885e8526eb; earlier_attempts lists the three earlier runs
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | gate re-read; rows and tickets ABSENT; protected and real tickets present | all printed | GO 11821 (AMENDMENT 4, CTO 11820), updated check at V2 11828 measured c3efc11f3d (32 mutants, selftest OK); precondition: the f51c tickets and rows ABSENT (read 03:21:30Z), protected and Andrew's tickets present; preflight 03:32:43Z: served tree 539b1ee70ba1 clean (29 TicketCenter files behind origin/DEV), rows ABSENT, open tickets on the table 1 of 38 | CLOSED 20261021T034800Z |
| M1 | activation | two staff-shaped rows written, PRESENT; two tokens in memory | iat and exp at most 20 min | 03:32:43Z two staff-shaped rows written (firmId opal-capital, scope_all_firms BOOL true, no allowedFirmIds), PRESENT; first tokens exp 03:40:43Z; DEVIATION: a second PICKER token minted 03:36:18Z (exp 03:46:18Z, GETs only) with the CTO's approval (msg 11835); no token printed; rows deleted 03:46:23Z, ConsistentRead ABSENT | CLOSED 20261021T034800Z |
| F1 | activation | filer files one service_request and one other ticket; ids read back | two ticket ids, no engine call | filer filed TCK-20261021-cf3af782 (service_request 03:33:00Z) and TCK-20261021-1bff6c63 (other 03:33:10Z) through the New Ticket form, ids read back from opal-tickets; no engine call, no third ticket | CLOSED 20261021T034801Z |
| C1 | activation | picker reads the board, private full-board shots, committed clipped shots, claims one from the board | chosen in_progress under picker, other open | picker (own context) read both rows from the board (Service Request and Other, under a minute, Claim control), private full-board shots r23_board_full and r23_board_claimed written OUTSIDE the repo (273533 and 276086 bytes, 1440x2081, sha256 92efaacf... and 8fa63084...), committed clips r23_rows_before (two synthetic rows), r23_rows_claimed (chosen row on In Progress, reads in progress under the picker) and r23_other_row_after_claim; each clip's row text read before written and the images viewed after; claim from the board 200 without opening either ticket. Part 1 stopped on this seat's stale-DOM read after the claim; part 2 (second token) took the two clips. Items saved whole by hand 03:34:02Z: chosen in_progress under the picker events created,claimed; other open | CLOSED 20261021T034801Z |
| D1 | verify | both tickets saved whole then deleted by key after both exp; both rows deleted; each ABSENT | 404 only | 03:46:23Z after both token exps: both tickets deleted by key (condition created_by the filer) and both rows deleted; ConsistentRead ABSENT for all four, re-read 03:47Z; protected tickets and Andrew's TCK-20261020-b1d61f80 present; private shots stay outside the repo, never staged | CLOSED 20261021T034801Z |
| V1 | verify | r23_fwd5_check.py with its self-test | RUN-OK (fwd5) | r23_fwd5_check.py (blob c3efc11f3d): R23-FWD5-SELFTEST-OK (32 mutants) beside RUN-OK (fwd5) tckt-r23-picker-20261021@opal.invalid read the board, saw TCK-20261021-cf3af782 and TCK-20261021-1bff6c63, and claimed TCK-20261021-cf3af782 from the board without opening either; both tickets and both rows ABSENT; the protected tickets present | CLOSED 20261021T034802Z |

## Log

- 20261021T032912Z OPENED by 0.7.0_AE_CloudOps~TV2 with 6 leg(s)
- 20261021T034800Z LEG S1 closed: GO 11821 (AMENDMENT 4, CTO 11820), updated check at V2 11828 measured c3efc11f3d (32 mutants, selftest OK); precondition
- 20261021T034800Z LEG M1 closed: 03:32:43Z two staff-shaped rows written (firmId opal-capital, scope_all_firms BOOL true, no allowedFirmIds), PRESENT; fi
- 20261021T034801Z LEG F1 closed: filer filed TCK-20261021-cf3af782 (service_request 03:33:00Z) and TCK-20261021-1bff6c63 (other 03:33:10Z) through the Ne
- 20261021T034801Z LEG C1 closed: picker (own context) read both rows from the board (Service Request and Other, under a minute, Claim control), private f
- 20261021T034801Z LEG D1 closed: 03:46:23Z after both token exps: both tickets deleted by key (condition created_by the filer) and both rows deleted; Con
- 20261021T034802Z LEG V1 closed: r23_fwd5_check.py (blob c3efc11f3d): R23-FWD5-SELFTEST-OK (32 mutants) beside RUN-OK (fwd5) tckt-r23-picker-20261021@opa
- 20261021T034802Z CLOSED -- all 6 legs proven
