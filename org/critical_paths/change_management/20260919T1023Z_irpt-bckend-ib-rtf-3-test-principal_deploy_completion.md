# Deploy Completion Record
**Date opened:** 2026-09-19T10:23:09.316759+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtf-3 (re-handed @0382e96047): the bounded test principal on the two-key packet blob a1f36b95b26c8fefd6ff0d47489f9884f87dd2c4 -- K1 opal-users-v2 PROFILE item + K1b opal-partner-49financial item created, exercised by real signed requests, K1b then K1 deleted and verified; both halves at HEAD (COO @3c0bad02ee, CTO @4290315df9)
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
| L5 | verify | refresh with the issued refresh token after K1's delete | refused 1 of 1 (CTO half s.1) |  | OPEN |
| L6 | verify | the access token after its exp | refused 401 1 of 1 |  | OPEN |

## Log

- 20260919T102309Z OPENED by 0.7.0_AE_CloudOps~V with 6 leg(s)
