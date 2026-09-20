# Deploy Completion Record
**Date opened:** 2026-09-20T18:49:47.048498+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260920T192128Z
**Deploy:** IRPT_BCKEND IB-rtg-4 arm (e): the bounded test principal on the rtf-9 two-key packet blob a1f36b95b26c8fefd6ff0d47489f9884f87dd2c4 (both halves at HEAD), NEW EPOCH -- K1 opal-users-v2 PROFILE item + K1b opal-partner-49financial item created, a real HTTP holdings request through the deployed route under irpt-holdings-role's execution, K1b then K1 deleted and verified, refresh refused, 401 after exp
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | opal-users-v2 K1 PROFILE item USER#usr_irptrte_<epoch> create | consistent GetItem read-back + digest (passwordHash excluded) | K1 created 2026-09-20T19:03:44Z, PK USER#usr_irptrte_1789931024, consistent GetItem read-back True, 10 attributes, digest (passwordHash excluded) 3086722a95ccaa29c92c1b3eac010878d50ae5896a4cbea8b85c1a8be76ac707 | CLOSED 20260920T192104Z |
| L2 | activation | opal-partner-49financial K1b item {email, advisorKey=abby_horton} create | consistent GetItem read-back + digest | K1b created 2026-09-20T19:03:44Z in opal-partner-49financial, consistent read-back True, attributes [advisorKey, email] exactly, digest ab3cb5891c92d9e4c6c05a88738b353be83d288a6e786af6daea2db205978d22 | CLOSED 20260920T192105Z |
| L3 | verify | K1b DELETED FIRST | consistent base-table GetItem returns no Item | K1b DeleteItem FIRST -> consistent base-table GetItem returns no Item: True at 2026-09-20T19:03:56Z | CLOSED 20260920T192105Z |
| L4 | verify | K1 DELETED | consistent base-table GetItem returns no Item | K1 DeleteItem -> consistent base-table GetItem returns no Item: True at 2026-09-20T19:03:56Z; deletions verified 2 of 2 | CLOSED 20260920T192105Z |
| L5 | verify | refresh with the issued refresh token after K1's delete | refused 1 of 1 | POST /auth/refresh with the issued refresh token after K1's delete: HTTP 404, no access token minted -> REFUSED 1 of 1 | CLOSED 20260920T192105Z |
| L6 | verify | the access token after its exp | refused 401 1 of 1; residue 0 on the prefix scans | GET /api/scoped/investor-reporting/status with the access token after its exp 19:18:54Z: HTTP 401 -> REFUSED 1 of 1; residue after 0 of 79 / 0 of 79 / 0 of 11; also this pass's own R75-AC1 positive: GET /holdings/acc_a5210ef53d8323b9d106b8b1 under irpt-holdings-role -> HTTP 200 class POLICY code NOT_AUTHORIZED firm_id present, never FIRM_BINDING with firm_id absent | CLOSED 20260920T192105Z |

## Log

- 20260920T184947Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 6 leg(s)
- 20260920T192104Z LEG L1 closed: K1 created 2026-09-20T19:03:44Z, PK USER#usr_irptrte_1789931024, consistent GetItem read-back True, 10 attributes, diges
- 20260920T192105Z LEG L2 closed: K1b created 2026-09-20T19:03:44Z in opal-partner-49financial, consistent read-back True, attributes [advisorKey, email] 
- 20260920T192105Z LEG L3 closed: K1b DeleteItem FIRST -> consistent base-table GetItem returns no Item: True at 2026-09-20T19:03:56Z
- 20260920T192105Z LEG L4 closed: K1 DeleteItem -> consistent base-table GetItem returns no Item: True at 2026-09-20T19:03:56Z; deletions verified 2 of 2
- 20260920T192105Z LEG L5 closed: POST /auth/refresh with the issued refresh token after K1's delete: HTTP 404, no access token minted -> REFUSED 1 of 1
- 20260920T192105Z LEG L6 closed: GET /api/scoped/investor-reporting/status with the access token after its exp 19:18:54Z: HTTP 401 -> REFUSED 1 of 1; res
- 20260920T192128Z CLOSED -- all 6 legs proven
