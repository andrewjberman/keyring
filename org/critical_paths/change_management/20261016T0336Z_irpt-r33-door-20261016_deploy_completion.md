# Deploy Completion Record
**Date opened:** 2026-10-16T03:36:31.287235+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-EXERCISE-R33 (AR-y-369): the release-33 sitting, synthetic only: four minted users rows (A, B in 49financial, C in cottonwood, one internal viewer) with three partner rows, six arms D1 to D4 and P2 P1 P1M, log reads in printed windows, removal after exp read ABSENT by GSI and ConsistentRead; no object deleted
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | verify | four users rows and three partner rows written with attribute_not_exists and read back; tokens minted in memory only | the trace lines |  | OPEN |
| D | verify | arms D1 D2 D3 D4 P2 P1 P1M answered as expected, the priceDate arms counted by the exact log string in printed windows, objects listed | DOOR_RESULT_R33.txt and OBJECTS_WRITTEN_R33.txt |  | OPEN |
| X | verify | every minted row deleted after exp and read ABSENT by the email GSI and a ConsistentRead, bounded 5 minute window | DOOR_REMOVAL_R33.txt |  | OPEN |

## Log

- 20261016T033631Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
