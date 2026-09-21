# Deploy Completion Record
**Date opened:** 2026-09-19T14:33:07.328126+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260919T145345Z
**Deploy:** IRPT_BCKEND IB-rtf-10 fourth pass arm (f): the bounded test principal on the rtf-9 two-key packet blob a1f36b95b26c8fefd6ff0d47489f9884f87dd2c4 (both halves at HEAD), NEW EPOCH -- K1 opal-users-v2 PROFILE item + K1b opal-partner-49financial item created, real HTTP requests through the deployed routes under each function's execution role, K1b then K1 deleted and verified, refresh refused, 401 after exp
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | opal-users-v2 K1 PROFILE item USER#usr_irptrte_<epoch> create | consistent GetItem read-back + digest (passwordHash excluded) | K1 created 2026-09-19T14:36:23Z, PK USER#usr_irptrte_1789828583, consistent GetItem read-back True, 10 attributes, digest (passwordHash excluded) ed430d7a4981435d302e05332e4c7afe221f71d39422ab4b18a74f51fe339683 | CLOSED 20260919T145343Z |
| L2 | activation | opal-partner-49financial K1b item {email, advisorKey=abby_horton} create | consistent GetItem read-back + digest | K1b created 2026-09-19T14:36:23Z in opal-partner-49financial, consistent read-back True, attributes [advisorKey, email] exactly, digest 1d95dadcae1d488720a34ae7d95853f3d3b60e0311b05e8da19b85c3e801be6e | CLOSED 20260919T145344Z |
| L3 | verify | K1b DELETED FIRST | consistent base-table GetItem returns no Item | K1b DeleteItem FIRST -> consistent base-table GetItem returns no Item: True at 2026-09-19T14:36:47Z | CLOSED 20260919T145344Z |
| L4 | verify | K1 DELETED | consistent base-table GetItem returns no Item | K1 DeleteItem -> consistent base-table GetItem returns no Item: True at 2026-09-19T14:36:47Z; deletions verified 2 of 2 | CLOSED 20260919T145344Z |
| L5 | verify | refresh with the issued refresh token after K1's delete | refused 1 of 1 | POST /auth/refresh with the issued refresh token after K1's delete: HTTP 404, no access token minted -> REFUSED 1 of 1 | CLOSED 20260919T145345Z |
| L6 | verify | the access token after its exp | refused 401 1 of 1; residue 0 on the three prefix scans | GET /api/scoped/investor-reporting/status with the access token after its exp 14:51:31Z: HTTP 401 -> REFUSED 1 of 1; interval [14:36:23Z, 14:51:31Z]; residue after 0 of 79 / 0 of 79 / 0 of 11; no throttle counter | CLOSED 20260919T145345Z |

## Log

- 20260919T143307Z OPENED by 0.7.0_AE_CloudOps~V with 6 leg(s)
- 20260919T145343Z LEG L1 closed: K1 created 2026-09-19T14:36:23Z, PK USER#usr_irptrte_1789828583, consistent GetItem read-back True, 10 attributes, diges
- 20260919T145344Z LEG L2 closed: K1b created 2026-09-19T14:36:23Z in opal-partner-49financial, consistent read-back True, attributes [advisorKey, email] 
- 20260919T145344Z LEG L3 closed: K1b DeleteItem FIRST -> consistent base-table GetItem returns no Item: True at 2026-09-19T14:36:47Z
- 20260919T145344Z LEG L4 closed: K1 DeleteItem -> consistent base-table GetItem returns no Item: True at 2026-09-19T14:36:47Z; deletions verified 2 of 2
- 20260919T145345Z LEG L5 closed: POST /auth/refresh with the issued refresh token after K1's delete: HTTP 404, no access token minted -> REFUSED 1 of 1
- 20260919T145345Z LEG L6 closed: GET /api/scoped/investor-reporting/status with the access token after its exp 14:51:31Z: HTTP 401 -> REFUSED 1 of 1; int
- 20260919T145345Z CLOSED -- all 6 legs proven
