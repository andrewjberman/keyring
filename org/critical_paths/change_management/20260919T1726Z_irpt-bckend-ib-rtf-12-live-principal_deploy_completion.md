# Deploy Completion Record
**Date opened:** 2026-09-19T17:26:57.313971+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260919T174957Z
**Deploy:** IRPT_BCKEND IB-rtf-12 third pass arm (f): the bounded test principal on the rtf-9 two-key packet blob a1f36b95b26c8fefd6ff0d47489f9884f87dd2c4 (both halves at HEAD), NEW EPOCH -- K1 opal-users-v2 PROFILE item + K1b opal-partner-49financial item created, rtf-10's arm (f) requests through the deployed routes under each function's execution role, K1b then K1 deleted and verified, refresh refused, 401 after exp
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | opal-users-v2 K1 PROFILE item USER#usr_irptrte_<epoch> create | consistent GetItem read-back + digest (passwordHash excluded) | K1 created 2026-09-19T17:31:20Z, PK USER#usr_irptrte_1789839080, consistent GetItem read-back True, 10 attributes, digest (passwordHash excluded) 5f2c02e8568842922ef943e9665840391719a7cf6fa45f58e1077a124d71a8bd | CLOSED 20260919T174954Z |
| L2 | activation | opal-partner-49financial K1b item {email, advisorKey=abby_horton} create | consistent GetItem read-back + digest | K1b created 2026-09-19T17:31:20Z in opal-partner-49financial, consistent read-back True, attributes [advisorKey, email] exactly, digest d7cee80029b543c3782f1a8476f0d9b8a916ef49164676686fdfa323be0cf644 | CLOSED 20260919T174955Z |
| L3 | verify | K1b DELETED FIRST | consistent base-table GetItem returns no Item | K1b DeleteItem FIRST -> consistent base-table GetItem returns no Item: True at 2026-09-19T17:31:46Z | CLOSED 20260919T174956Z |
| L4 | verify | K1 DELETED | consistent base-table GetItem returns no Item | K1 DeleteItem -> consistent base-table GetItem returns no Item: True at 2026-09-19T17:31:46Z; deletions verified 2 of 2 | CLOSED 20260919T174956Z |
| L5 | verify | refresh with the issued refresh token after K1's delete | refused 1 of 1 | POST /auth/refresh with the issued refresh token after K1's delete: HTTP 404, no access token minted -> REFUSED 1 of 1 | CLOSED 20260919T174956Z |
| L6 | verify | the access token after its exp | refused 401 1 of 1; residue 0 on the three prefix scans | GET /api/scoped/investor-reporting/status with the access token after its exp 17:46:28Z: HTTP 401 -> REFUSED 1 of 1; interval [17:31:20Z, 17:46:28Z]; residue after 0 of 79 / 0 of 79 / 0 of 11; no throttle counter | CLOSED 20260919T174956Z |

## Log

- 20260919T172657Z OPENED by 0.7.0_AE_CloudOps~V with 6 leg(s)
- 20260919T174954Z LEG L1 closed: K1 created 2026-09-19T17:31:20Z, PK USER#usr_irptrte_1789839080, consistent GetItem read-back True, 10 attributes, diges
- 20260919T174955Z LEG L2 closed: K1b created 2026-09-19T17:31:20Z in opal-partner-49financial, consistent read-back True, attributes [advisorKey, email] 
- 20260919T174956Z LEG L3 closed: K1b DeleteItem FIRST -> consistent base-table GetItem returns no Item: True at 2026-09-19T17:31:46Z
- 20260919T174956Z LEG L4 closed: K1 DeleteItem -> consistent base-table GetItem returns no Item: True at 2026-09-19T17:31:46Z; deletions verified 2 of 2
- 20260919T174956Z LEG L5 closed: POST /auth/refresh with the issued refresh token after K1's delete: HTTP 404, no access token minted -> REFUSED 1 of 1
- 20260919T174956Z LEG L6 closed: GET /api/scoped/investor-reporting/status with the access token after its exp 17:46:28Z: HTTP 401 -> REFUSED 1 of 1; int
- 20260919T174957Z CLOSED -- all 6 legs proven
