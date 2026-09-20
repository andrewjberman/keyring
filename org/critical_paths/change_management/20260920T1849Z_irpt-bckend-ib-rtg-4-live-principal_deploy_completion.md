# Deploy Completion Record
**Date opened:** 2026-09-20T18:49:47.048498+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtg-4 arm (e): the bounded test principal on the rtf-9 two-key packet blob a1f36b95b26c8fefd6ff0d47489f9884f87dd2c4 (both halves at HEAD), NEW EPOCH -- K1 opal-users-v2 PROFILE item + K1b opal-partner-49financial item created, a real HTTP holdings request through the deployed route under irpt-holdings-role's execution, K1b then K1 deleted and verified, refresh refused, 401 after exp
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
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
| L6 | verify | the access token after its exp | refused 401 1 of 1; residue 0 on the prefix scans |  | OPEN |

## Log

- 20260920T184947Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 6 leg(s)
