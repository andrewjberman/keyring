# Deploy Completion Record
**Date opened:** 2026-10-07T00:42:44.839221+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261007T033243Z
**Deploy:** ADVI_COTBKF round 3: the three imaging archives (HKE, HJH, 4XF) to bronze + manifest; then silver document_index, crosswalk, account_links (one-time backfill, prefix opal-data-assets/commonwealth/cottonwood/)
**Authored by:** 2.0.0_SA_COO~C
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | bronze imaging: HKE.zip, HJH.zip, 4XF.zip under .../bronze/imaging/date=2026-06-23/ + manifest gains 3 files | head-object size + SHA-256 read back per zip | land_imaging_plan_id.py --apply rc=0 (bg bh6kaz137, 01:2xZ-03:27Z); independent head_object read-back: plan_id=HKE/HKE.zip 1,554,270,895 B etag a24d52e0...-24, plan_id=HJH/HJH.zip 1,503,993,172 B etag 88a62f25...-23, plan_id=4XF/4XF.zip 113,362,389 B etag 301f4578...-2 -- 3/3 match the expected multipart etags; 0 dangling multipart uploads; bronze manifest date=2026-06-23 holds 4 entries with matching sha256 | CLOSED 20261007T033242Z |
| L2 | verify | silver document_index | read back unique documents and pdfs accounted | document_index --apply (source the delivered archives, 3 archives, 51 listings, 24,489 PDFs accounted); boto3+pyarrow read-back 02:4xZ: silver/document_index/date=2026-06-23/document_index.parquet 11,119 rows 15 columns + archives.parquet | CLOSED 20261007T024341Z |
| L3 | verify | silver crosswalk | read back 1533 rows | crosswalk --apply; read-back 02:4xZ: silver/crosswalk/date=2026-06-23/crosswalk.parquet 1,533 rows 14 columns (+ csv); 439 MATCHED by R2, 1,094 NOT_MATCHED with reasons, 36 ambiguous | CLOSED 20261007T024342Z |
| L4 | verify | silver account_links | read back 459 old accounts | account_links --apply; read-back 02:4xZ: silver/account_links/date=2026-06-23/account_links.parquet 459 rows 13 columns (+ csv); 180 LINKED, 279 NOT_LINKED (13 ambiguous), 5 chains | CLOSED 20261007T024342Z |

## Log

- 20261007T004244Z OPENED by 2.0.0_SA_COO~C with 4 leg(s)
- 20261007T024341Z LEG L2 closed: document_index --apply (source the delivered archives, 3 archives, 51 listings, 24,489 PDFs accounted); boto3+pyarrow re
- 20261007T024342Z LEG L3 closed: crosswalk --apply; read-back 02:4xZ: silver/crosswalk/date=2026-06-23/crosswalk.parquet 1,533 rows 14 columns (+ csv); 4
- 20261007T024342Z LEG L4 closed: account_links --apply; read-back 02:4xZ: silver/account_links/date=2026-06-23/account_links.parquet 459 rows 13 columns 
- 20261007T033242Z LEG L1 closed: land_imaging_plan_id.py --apply rc=0 (bg bh6kaz137, 01:2xZ-03:27Z); independent head_object read-back: plan_id=HKE/HKE.z
- 20261007T033243Z CLOSED -- all 4 legs proven
