# Deploy Completion Record
**Date opened:** 2026-09-19T18:08:03.105389+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtf-12 third pass, the RE-RUN after the arm (a) battery fix (issuer ruling msg 98307): the bounded test principal on the rtf-9 two-key packet blob a1f36b95b2 (both halves at HEAD), NEW EPOCH -- K1 + K1b created, rtf-10's arm (f) requests through the deployed routes under each function's execution role, K1b then K1 deleted and verified, refresh refused, 401 after exp
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | opal-users-v2 K1 PROFILE item USER#usr_irptrte_<epoch> create | consistent GetItem read-back + digest (passwordHash excluded) |  | OPEN |
| L2 | activation | opal-partner-49financial K1b item {email, advisorKey=abby_horton} create | consistent GetItem read-back + digest |  | OPEN |
| L3 | verify | K1b DELETED FIRST | consistent base-table GetItem returns no Item |  | OPEN |
| L4 | verify | K1 DELETED | consistent base-table GetItem returns no Item |  | OPEN |
| L5 | verify | refresh with the issued refresh token after K1's delete | refused 1 of 1 |  | OPEN |
| L6 | verify | the access token after its exp | refused 401 1 of 1; residue 0 on the three prefix scans |  | OPEN |

## Log

- 20260919T180803Z OPENED by 0.7.0_AE_CloudOps~V with 6 leg(s)
