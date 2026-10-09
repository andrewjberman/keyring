# Deploy Completion Record
**Date opened:** 2026-10-09T16:54:48.588633+00:00
**Status:** OPEN
**Deploy:** RETROSPECTIVE (opened after the fact): TCKT_VNEXT SA-r-1b RUN 2 under AMENDMENT 3 -- this seat omitted the entry at start
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ROW | verify | opal-users-v2 | the run-2 filer row: conditional put + ConsistentRead read-back present, then deleted with read-back ABSENT |  | OPEN |
| TOK | verify | opal/auth/jwt-private-key | run 2's FRESH RS256 token, v2.2 claims, exp 18:48:43Z, memory only; key read reported after via MSTR~DELL2 |  | OPEN |
| RUN | verify | limb 3 + live census | AMENDMENT 3 limb 3 on a real call, then the full census re-run because a host had changed |  | OPEN |
| CLN | verify | cleanup same session | row absent on read-back; the one ticket run 2 created completed |  | OPEN |
| DRZ | verify | /aws/lambda/opal-data-refresh-api | 0 data-refresh calls for the filer over run 2's window |  | OPEN |

## Log

- 20261009T165448Z OPENED by 0.7.0_AE_CloudOps~TV2 with 5 leg(s)
