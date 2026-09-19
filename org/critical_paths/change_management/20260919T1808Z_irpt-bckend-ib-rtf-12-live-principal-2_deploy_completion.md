# Deploy Completion Record
**Date opened:** 2026-09-19T18:08:03.105389+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260919T183423Z
**Deploy:** IRPT_BCKEND IB-rtf-12 third pass, the RE-RUN after the arm (a) battery fix (issuer ruling msg 98307): the bounded test principal on the rtf-9 two-key packet blob a1f36b95b2 (both halves at HEAD), NEW EPOCH -- K1 + K1b created, rtf-10's arm (f) requests through the deployed routes under each function's execution role, K1b then K1 deleted and verified, refresh refused, 401 after exp
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | opal-users-v2 K1 PROFILE item USER#usr_irptrte_<epoch> create | consistent GetItem read-back + digest (passwordHash excluded) | K1 created 2026-09-19T18:17:39Z, PK USER#usr_irptrte_1789841859, consistent GetItem read-back True, 10 attributes, digest (passwordHash excluded) c1997e9a3f7bb2a4caa5445cc4bd618c1d5aa0524bbfa64... | CLOSED 20260919T183422Z |
| L2 | activation | opal-partner-49financial K1b item {email, advisorKey=abby_horton} create | consistent GetItem read-back + digest | K1b created 2026-09-19T18:17:39Z in opal-partner-49financial, consistent read-back True, attributes [advisorKey, email] exactly, digest 345d3d0219330b05d02c5c76c1f509fc85248646b905632fba44c... | CLOSED 20260919T183422Z |
| L3 | verify | K1b DELETED FIRST | consistent base-table GetItem returns no Item | K1b DeleteItem FIRST -> consistent base-table GetItem returns no Item: True at 2026-09-19T18:18:04Z | CLOSED 20260919T183422Z |
| L4 | verify | K1 DELETED | consistent base-table GetItem returns no Item | K1 DeleteItem -> consistent base-table GetItem returns no Item: True at 2026-09-19T18:18:04Z; deletions verified 2 of 2 | CLOSED 20260919T183422Z |
| L5 | verify | refresh with the issued refresh token after K1's delete | refused 1 of 1 | POST /auth/refresh with the issued refresh token after K1's delete: HTTP 404, no access token minted -> REFUSED 1 of 1 | CLOSED 20260919T183422Z |
| L6 | verify | the access token after its exp | refused 401 1 of 1; residue 0 on the three prefix scans | GET /api/scoped/investor-reporting/status with the access token after its exp 18:32:47Z: HTTP 401 -> REFUSED 1 of 1; interval [18:17:39Z, 18:32:47Z]; residue after 0 of 79 / 0 of 79 / 0 of 11; no throttle counter | CLOSED 20260919T183423Z |

## Log

- 20260919T180803Z OPENED by 0.7.0_AE_CloudOps~V with 6 leg(s)
- 20260919T183422Z LEG L1 closed: K1 created 2026-09-19T18:17:39Z, PK USER#usr_irptrte_1789841859, consistent GetItem read-back True, 10 attributes, diges
- 20260919T183422Z LEG L2 closed: K1b created 2026-09-19T18:17:39Z in opal-partner-49financial, consistent read-back True, attributes [advisorKey, email] 
- 20260919T183422Z LEG L3 closed: K1b DeleteItem FIRST -> consistent base-table GetItem returns no Item: True at 2026-09-19T18:18:04Z
- 20260919T183422Z LEG L4 closed: K1 DeleteItem -> consistent base-table GetItem returns no Item: True at 2026-09-19T18:18:04Z; deletions verified 2 of 2
- 20260919T183422Z LEG L5 closed: POST /auth/refresh with the issued refresh token after K1's delete: HTTP 404, no access token minted -> REFUSED 1 of 1
- 20260919T183423Z LEG L6 closed: GET /api/scoped/investor-reporting/status with the access token after its exp 18:32:47Z: HTTP 401 -> REFUSED 1 of 1; int
- 20260919T183423Z CLOSED -- all 6 legs proven
