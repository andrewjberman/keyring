# Deploy Completion Record
**Date opened:** 2026-10-07T18:25:48.324420+00:00
**Status:** OPEN
**Deploy:** IB-pr-350 pass 2: back-fill covered_account_ids into ONE pre-343 receipt (49financial, EXP-e29b5415), both halves signed against packet blob 2e073c2d3e
**Authored by:** 0.7.0_AE_CloudOps~I
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | preconditions: both halves at the published HEAD naming packet blob 2e073c2d3e (COO @295835f61f, CTO @c48b2d2442, ref 84bc3c379c); CTO ADDED CONDITION bundle-set == pending-set; identity arn:aws:iam::313476888478:user/Andrew_Berman. ROLLBACK SOURCE = s3://opal-data-ycharts/firms/49financial/generations/EXP-e29b5415a06f90f943481c41a1a4821b/receipt.json?versionId=3BN57Lb6hJ7._Nn0hGZ4Yj7NEFYOV_Qa | the two halves' paths+commits, the set-equality read, and the version id |  | OPEN |
| L2 | activation | backfill_covered_account_ids.py --apply --bucket opal-data-ycharts on the ONE signed key; tool blob 23cea9f84a | apply output with wrote=1 denied=0, and the new object version id |  | OPEN |
| L3 | verify | after-reads: the written receipt re-reads with a non-empty facts.covered_account_ids; a back-filled export is ADMITTED for an in-scope Opal principal through the DEPLOYED bytes and REFUSED for an out-of-scope one; counts unmoved | IB69-1_backfill_after_reads.json + IB69-1-AC1 last line |  | OPEN |

## Log

- 20261007T182548Z OPENED by 0.7.0_AE_CloudOps~I with 3 leg(s)
