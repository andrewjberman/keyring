# Deploy Completion Record
**Date opened:** 2026-10-08T06:59:33.765495+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T073505Z
**Deploy:** ADVI_COTBKF r18 CB-r-2: document index re-applied with page_count from the PDFs (opal-data-assets/commonwealth/cottonwood/silver/document_index/date=2026-06-23/, 2 objects; pins document_index xS7loply3Eug2dT30ffGOyFgfQt7K8OM, archives mSZeqb29xRfJXu5aFDgtlBUUfzxH1y84; pair COO @9dfdce0b3e + CTO @606b798fc8)
**Authored by:** 2.0.0_SA_COO~C2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | document_index replaced | VersionId moved; read back 11119 rows, page_count non-null 11087, null 32, every other column equal to pin xS7loply | applied 2026-10-08 ~07:0xZ rc 0 from dell2 (drained builder @e4ab655cf9, --page-counts ~36 page_counts.csv; build hash-equal to the drained build e60f6ce5...): document_index.parquet xS7loply... -> 0aPGtfdm5pzHbMNqHP3KUHsFHGKYNS4t; read back 11119 rows, page_count non-null 11087, null 32, every other column equal to pin xS7loply | CLOSED 20261008T073459Z |
| L2 | verify | archives replaced | VersionId moved; read back 3 rows equal to pin mSZeqb29 | archives.parquet mSZeqb29... -> cjcZtTuUeOzunpowvYpqIVIKvv_.ubge; read back 3 rows, content equal to pin mSZeqb29 (same archives, sha256, sizes, counts); row ORDER differs (pin HKE,HJH,4XF; new 4XF,HJH,HKE) -- no content change, within the signed blast radius. Note: the COO half swapped the two file hashes (document_index is e60f6ce5..., archives 569d4b88...) | CLOSED 20261008T073502Z |

## Log

- 20261008T065933Z OPENED by 2.0.0_SA_COO~C2 with 2 leg(s)
- 20261008T073459Z LEG L1 closed: applied 2026-10-08 ~07:0xZ rc 0 from dell2 (drained builder @e4ab655cf9, --page-counts ~36 page_counts.csv; build hash-e
- 20261008T073502Z LEG L2 closed: archives.parquet mSZeqb29... -> cjcZtTuUeOzunpowvYpqIVIKvv_.ubge; read back 3 rows, content equal to pin mSZeqb29 (same 
- 20261008T073505Z CLOSED -- all 2 legs proven
