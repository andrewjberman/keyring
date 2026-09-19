# Deploy Completion Record
**Date opened:** 2026-09-19T10:23:09.316759+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260919T104300Z
**Deploy:** IRPT_BCKEND IB-rtf-3 (re-handed @0382e96047): the bounded test principal on the two-key packet blob a1f36b95b26c8fefd6ff0d47489f9884f87dd2c4 -- K1 opal-users-v2 PROFILE item + K1b opal-partner-49financial item created, exercised by real signed requests, K1b then K1 deleted and verified; both halves at HEAD (COO @3c0bad02ee, CTO @4290315df9)
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | opal-users-v2 K1 PROFILE item USER#usr_irptrte_<epoch> create | consistent GetItem read-back + digest (passwordHash excluded) | K1 created 2026-09-19T10:25:56Z, PK USER#usr_irptrte_1789813553, consistent GetItem read-back True, 10 attributes, digest (passwordHash excluded) 8b1123122d127db1e254ef64eef47b0a94783b101f9b0b648ab752af92a6f4f3 | CLOSED 20260919T104258Z |
| L2 | activation | opal-partner-49financial K1b item {email, advisorKey=abby_horton} create | consistent GetItem read-back + digest | K1b created 2026-09-19T10:25:56Z in opal-partner-49financial, consistent read-back True, attributes [advisorKey, email] exactly, digest 5d891293f2b4b72684a35c164cf0313d2ed750dddd0aa58439bd9851693be88f | CLOSED 20260919T104258Z |
| L3 | verify | K1b DELETED FIRST | consistent base-table GetItem returns no Item | K1b DeleteItem FIRST -> consistent base-table GetItem returns no Item: True at 2026-09-19T10:26:10Z | CLOSED 20260919T104258Z |
| L4 | verify | K1 DELETED | consistent base-table GetItem returns no Item | K1 DeleteItem -> consistent base-table GetItem returns no Item: True at 2026-09-19T10:26:10Z; deletions verified 2 of 2 | CLOSED 20260919T104259Z |
| L5 | verify | refresh with the issued refresh token after K1's delete | refused 1 of 1 (CTO half s.1) | POST /auth/refresh with the issued refresh token after K1's delete: HTTP 404, no access token minted -> REFUSED 1 of 1 (CTO half s.1) | CLOSED 20260919T104259Z |
| L6 | verify | the access token after its exp | refused 401 1 of 1 | GET /api/scoped/investor-reporting/status with the access token after its exp 10:41:03Z: HTTP 401 -> REFUSED 1 of 1; interval [10:25:56Z, 10:41:03Z]; residue 0 of 79 / 0 of 79 / 0 of 11; no throttle counter | CLOSED 20260919T104300Z |

## Log

- 20260919T102309Z OPENED by 0.7.0_AE_CloudOps~V with 6 leg(s)
- 20260919T104258Z LEG L1 closed: K1 created 2026-09-19T10:25:56Z, PK USER#usr_irptrte_1789813553, consistent GetItem read-back True, 10 attributes, diges
- 20260919T104258Z LEG L2 closed: K1b created 2026-09-19T10:25:56Z in opal-partner-49financial, consistent read-back True, attributes [advisorKey, email] 
- 20260919T104258Z LEG L3 closed: K1b DeleteItem FIRST -> consistent base-table GetItem returns no Item: True at 2026-09-19T10:26:10Z
- 20260919T104259Z LEG L4 closed: K1 DeleteItem -> consistent base-table GetItem returns no Item: True at 2026-09-19T10:26:10Z; deletions verified 2 of 2
- 20260919T104259Z LEG L5 closed: POST /auth/refresh with the issued refresh token after K1's delete: HTTP 404, no access token minted -> REFUSED 1 of 1 (
- 20260919T104300Z LEG L6 closed: GET /api/scoped/investor-reporting/status with the access token after its exp 10:41:03Z: HTTP 401 -> REFUSED 1 of 1; int
- 20260919T104300Z CLOSED -- all 6 legs proven
