# Deploy Completion Record
**Date opened:** 2026-10-09T17:07:22.994128+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT SA-r-1b RUN 3 under AMENDMENT 4: full census with the new leak criterion, then the FWD-1 hops a-g
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ROW | verify | opal-users-v2 | fresh filer row: conditional put attribute_not_exists(PK) + ConsistentRead read-back present |  | OPEN |
| TOK | verify | opal/auth/jwt-private-key | fresh ONE RS256 token, CURRENT slot, v2.2 claims (tier internal, userType test-filer), exp=iat+2h, memory only; key read reported after via MSTR~DELL2 |  | OPEN |
| CEN | verify | live /api/scoped census | full census over every live /api/scoped route with the denominator PRINTED, data-refresh host skipped; AMENDMENT 4 leak criterion: an off-list payload DIFFERING from the own-firm answer, OR code that reads the selector for an off-list target; a selector-ignoring route whose firm comes only from the token is NOT a STOP |  | OPEN |
| HOP | verify | the FWD-1 journey | hops (a)-(g) through the real CloudFront entry into R1_RUN/sa_r1b_trace.json run_3 section: upload door, ticket, claim, analysis submit, READY poll, report onto the ticket, open it from the ticket. Status and artifact id only, NO client figures. A hop that cannot run is NAMED and never retried into a pass |  | OPEN |
| CLN | verify | cleanup same session | row REMOVEd and read back absent; EVERY ticket this run created completed (the journey's and the 49financial census CREATE arm); token left to expire |  | OPEN |
| DRZ | verify | /aws/lambda/opal-data-refresh-api | AMENDMENT 2's negative proof for run 3's window, with the positive control that the filter finds the filer when it did call |  | OPEN |

## Log

- 20261009T170722Z OPENED by 0.7.0_AE_CloudOps~TV2 with 6 leg(s)
