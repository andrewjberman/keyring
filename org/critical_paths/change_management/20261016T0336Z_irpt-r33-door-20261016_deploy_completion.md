# Deploy Completion Record
**Date opened:** 2026-10-16T03:36:31.287235+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T040245Z
**Deploy:** IRPT_ANLREQ TO-EXERCISE-R33 (AR-y-369): the release-33 sitting, synthetic only: four minted users rows (A, B in 49financial, C in cottonwood, one internal viewer) with three partner rows, six arms D1 to D4 and P2 P1 P1M, log reads in printed windows, removal after exp read ABSENT by GSI and ConsistentRead; no object deleted
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | verify | four users rows and three partner rows written with attribute_not_exists and read back; tokens minted in memory only | the trace lines | 03:40:42Z to 03:41:51Z: pre-state four users keys ABSENT by ConsistentRead, four addresses 0 on the email index, three partner keys ABSENT; four users rows (attribute_not_exists) and three partner rows written and read back PRESENT; signing key read in memory only (value never printed or written); tokens minted in memory for A, B, C (exp 03:59:43Z) and for the internal viewer (exp 03:54:51Z); every log line in DOOR_TRACE_R33.txt carries status, code and sha256 only | CLOSED 20261016T040244Z |
| D | verify | arms D1 D2 D3 D4 P2 P1 P1M answered as expected, the priceDate arms counted by the exact log string in printed windows, objects listed | DOOR_RESULT_R33.txt and OBJECTS_WRITTEN_R33.txt | recorded 03:40Z to 03:47Z, each request ONCE except the RESOLVING re-posts of D1 and P2: D1 NORMALIZED, D3 REFUSED NOT_AUTHORIZED, P2 NORMALIZED price_date_ignored=0 as ordered (3 of 7); D2 FAIL 200 INVALID_INPUT (the function's own log: COMPOSITION-REFUSED step=2 error_class=ValidationError), D4 FAIL 200 NOT_FOUND (InputUnavailable), P1 and P1M FAIL 200 RESOLVING (log windows: P1 matches=1, P1M matches=1, P2 matches=0, windows printed in DOOR_RESULT_R33.txt); neither D3 nor D4 admitted; objects: 8 listed (49financial +8, cottonwood +0), none deleted | CLOSED 20261016T040244Z |
| X | verify | every minted row deleted after exp and read ABSENT by the email GSI and a ConsistentRead, bounded 5 minute window | DOOR_REMOVAL_R33.txt | after every token exp (last 03:59:43Z) the 4 users rows and 3 partner rows were deleted (attribute_exists) at 03:59:48Z; the first removal read 03:59:48Z read all four addresses ABSENT by the email GSI and by a ConsistentRead and the three partner keys ABSENT; DOOR_REMOVAL_R33.txt holds 8 ABSENT lines | CLOSED 20261016T040244Z |

## Log

- 20261016T033631Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
- 20261016T040244Z LEG M closed: 03:40:42Z to 03:41:51Z: pre-state four users keys ABSENT by ConsistentRead, four addresses 0 on the email index, three p
- 20261016T040244Z LEG D closed: recorded 03:40Z to 03:47Z, each request ONCE except the RESOLVING re-posts of D1 and P2: D1 NORMALIZED, D3 REFUSED NOT_A
- 20261016T040244Z LEG X closed: after every token exp (last 03:59:43Z) the 4 users rows and 3 partner rows were deleted (attribute_exists) at 03:59:48Z;
- 20261016T040245Z CLOSED -- all 3 legs proven
