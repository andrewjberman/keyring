# Deploy Completion Record
**Date opened:** 2026-10-14T13:17:26.322477+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-EXERCISE-R29: the partner-advisor sitting of release 29 -- three synthetic users (A and B in 49financial, C in cottonwood) with their partner rows and one synthetic internal viewer, minted for ONE sitting; D1 upload, D2 owned analysis, D3 and D4 refusals, D5 Shares words, D6 internal viewer, C1 portal parse; every minted row removed after exp and read ABSENT by GSI and ConsistentRead; every written object listed by key and VersionId, none deleted; signed pair COO blob 5e8b3cbd95 + CTO half section (c)
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | verify | three legs read as closed (irpt-status yNpw441T.., irpt-ycharts-generate 5TRFZf6G.., resident root 0485393f3a-r29 from YC2 output); markers 0 live open entries naming opal-users-v2, a partner table or irpt-ycharts-generate; own grants simulated allowed; pre-state ABSENT by ConsistentRead and GSI; intake store listed BEFORE for 49financial and cottonwood; rows written (attribute_not_exists) and read back; tokens minted in memory | printed reads |  | OPEN |
| D | verify | D1 to D6 and C1 each answered as the order expects or recorded as FAIL with status and code; only status, code and body sha256 kept | DOOR_RESULT_R29.txt seven lines |  | OPEN |
| X | verify | after every exp: each minted users row and partner row deleted (attribute_exists), four addresses read ABSENT by GSI and ConsistentRead within a bounded 5 minutes; intake store listed AFTER; every written object listed by key and VersionId; nothing deleted | DOOR_REMOVAL_R29.txt and OBJECTS_WRITTEN_R29.txt |  | OPEN |

## Log

- 20261014T131726Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
