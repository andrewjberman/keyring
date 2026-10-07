# Deploy Completion Record
**Date opened:** 2026-10-07T00:42:44.839221+00:00
**Status:** OPEN
**Deploy:** ADVI_COTBKF round 3: the three imaging archives (HKE, HJH, 4XF) to bronze + manifest; then silver document_index, crosswalk, account_links (one-time backfill, prefix opal-data-assets/commonwealth/cottonwood/)
**Authored by:** 2.0.0_SA_COO~C
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | bronze imaging: HKE.zip, HJH.zip, 4XF.zip under .../bronze/imaging/date=2026-06-23/ + manifest gains 3 files | head-object size + SHA-256 read back per zip |  | OPEN |
| L2 | verify | silver document_index | read back unique documents and pdfs accounted |  | OPEN |
| L3 | verify | silver crosswalk | read back 1533 rows |  | OPEN |
| L4 | verify | silver account_links | read back 459 old accounts |  | OPEN |

## Log

- 20261007T004244Z OPENED by 2.0.0_SA_COO~C with 4 leg(s)
