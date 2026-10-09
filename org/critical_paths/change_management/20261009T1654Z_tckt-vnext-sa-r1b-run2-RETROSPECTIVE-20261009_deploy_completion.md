# Deploy Completion Record
**Date opened:** 2026-10-09T16:54:48.588633+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T165508Z
**Deploy:** RETROSPECTIVE (opened after the fact): TCKT_VNEXT SA-r-1b RUN 2 under AMENDMENT 3 -- this seat omitted the entry at start
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ROW | verify | opal-users-v2 | the run-2 filer row: conditional put + ConsistentRead read-back present, then deleted with read-back ABSENT | conditional put accepted under attribute_not_exists(PK); ConsistentRead read-back PRESENT with allowedFirmIds={L:[{S:49financial}]}; at cleanup deleted and ConsistentRead read-back ABSENT (True) | CLOSED 20261009T165507Z |
| TOK | verify | opal/auth/jwt-private-key | run 2's FRESH RS256 token, v2.2 claims, exp 18:48:43Z, memory only; key read reported after via MSTR~DELL2 | FRESH RS256 token from the CURRENT slot (run 1's row and token were gone); v2.2 claims tier=internal userType=test-filer role=user firmId=opal-capital; iat 16:48:43Z exp 18:48:43Z; memory only, never printed/stored/committed; left to expire | CLOSED 20261009T165507Z |
| RUN | verify | limb 3 + live census | AMENDMENT 3 limb 3 on a real call, then the full census re-run because a host had changed | AMENDMENT 3 limb 3 PASSED on a real call: GET /api/scoped/investor-reporting/status -> HTTP 200 reason NOT_FOUND, non-500. It could NOT be settled from the log group, which held 0 events of ANY kind after the 16:43:21Z rollback -- absence of traffic, not health. STOP 1 re-run first: READ27 27/27 rc 0, irpt-status LastModified 16:43:21Z / CodeSha256 t6OJTCcm with member sha256 still 87d9ecc4, so the rollback kept the clamp bytes. CENSUS: 82 of 91 live /api/scoped armed (9 data-refresh skipped), live denominator 119 vs source 117. RESULT: ZERO off-list admits; ZERO arms returned another firm's data in this run or run 1 (the oracle is a differing fingerprint, count 0). All IRPT-served arms refused cottonwood and inflection with FIRM_BINDING, INCLUDING the 6 routes that were ungradeable at 500 in run 1 -- irpt-status is RESTORED. Ticket LIST n=9, requester firms ['49financial'] only. AMENDMENT 1's CREATE arms reached the clamp: own 201 TCK-20261009-8b434dde, both off-list 400 with the body NAMING the firm. HOPS: none ran. The run raised a BEHAVES-AS-ALL STOP that was this instrument's SECOND mis-specification -- it treated every selector-ignored arm as a violation although run 1 had already classified those same arms as expected. Corrected: 14 of 16 are census NO_FIRM or routes with no selector carrier. ONE deviation survives and is routed to the issuer, not tuned away: GET /api/scoped/amgt/watchlist (census ONE_FIRM) ANSWERS an off-list target 200 instead of refusing it, with an empty byte-identical body -- unrefused, but provably not a leak. | CLOSED 20261009T165507Z |
| CLN | verify | cleanup same session | row absent on read-back; the one ticket run 2 created completed | row deleted, ConsistentRead read-back ABSENT (True); ticket TCK-20261009-8b434dde COMPLETED http 200 by the same principal; token left to expire 18:48:43Z. No IAM, code or route change. The world is clean: nothing half-landed. | CLOSED 20261009T165508Z |
| DRZ | verify | /aws/lambda/opal-data-refresh-api | 0 data-refresh calls for the filer over run 2's window | /aws/lambda/opal-data-refresh-api over run 2's window filtered for the filer: 0 matches. Controls as in run 1: the group exists and is live, and the positive control over SA-r-1's window (where the filer DID call) returns 3 matches, so the filter discriminates and the zero is a TRUE NEGATIVE. | CLOSED 20261009T165508Z |

## Log

- 20261009T165448Z OPENED by 0.7.0_AE_CloudOps~TV2 with 5 leg(s)
- 20261009T165507Z LEG ROW closed: conditional put accepted under attribute_not_exists(PK); ConsistentRead read-back PRESENT with allowedFirmIds={L:[{S:49f
- 20261009T165507Z LEG TOK closed: FRESH RS256 token from the CURRENT slot (run 1's row and token were gone); v2.2 claims tier=internal userType=test-filer
- 20261009T165507Z LEG RUN closed: AMENDMENT 3 limb 3 PASSED on a real call: GET /api/scoped/investor-reporting/status -> HTTP 200 reason NOT_FOUND, non-50
- 20261009T165508Z LEG CLN closed: row deleted, ConsistentRead read-back ABSENT (True); ticket TCK-20261009-8b434dde COMPLETED http 200 by the same princip
- 20261009T165508Z LEG DRZ closed: /aws/lambda/opal-data-refresh-api over run 2's window filtered for the filer: 0 matches. Controls as in run 1: the group
- 20261009T165508Z CLOSED -- all 5 legs proven
