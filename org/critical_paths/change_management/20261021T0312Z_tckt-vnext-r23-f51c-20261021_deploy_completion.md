# Deploy Completion Record
**Date opened:** 2026-10-21T03:12:31.167516+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT TO-R23-F51 AMENDMENT 2 (V2 GO 11809; CTO 11808): the ONE more FWD-5 run on DEV (http://localhost:5174), staff-shaped identities (firmId opal-capital, scope_all_firms BOOL true, no allowedFirmIds), ticket ids read back from the table: filer files a Service Request and an Other ticket, the picker (separate context) claims one FROM THE BOARD without opening either; both tickets saved whole then deleted by key after exp, both rows deleted; earlier attempts recorded in the result; surfaces opal-tickets (2 created, 1 claimed, deleted), opal-users-v2 (2 rows created, deleted); no S3, no PROD; check d4c6c9680c; no third run without a word
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | precondition: TCK-20261021-c31f5347 and both rows ABSENT; gate re-read | all printed |  | OPEN |
| M1 | activation | two staff-shaped rows written, PRESENT; two tokens in memory | iat and exp at most 20 min |  | OPEN |
| F1 | activation | filer files one service_request and one other ticket; ids read back | two ticket ids, no engine call |  | OPEN |
| C1 | activation | picker reads the full board, shot r23_board_full, claims one from the board, shot r23_board_claimed | chosen in_progress under picker, other open unassigned |  | OPEN |
| D1 | verify | both tickets saved whole then deleted by key after both exp; both rows deleted; each ABSENT | 404 only |  | OPEN |
| V1 | verify | r23_fwd5_check.py with its self-test | RUN-OK (fwd5) |  | OPEN |

## Log

- 20261021T031231Z OPENED by 0.7.0_AE_CloudOps~TV2 with 6 leg(s)
