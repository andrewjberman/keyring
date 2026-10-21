# Deploy Completion Record
**Date opened:** 2026-10-21T07:19:05.641778+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T072305Z
**Deploy:** bd49f dim compaction: one rewrite of dim_advisor_fee_role/date=2026-10-20/data.parquet (NFRA_CTLPLN TO-APPLY-36)
**Authored by:** 0.7.0_AE_CloudOps~NFRA2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | s3://opal-data-assets/blackdiamond/49f/silver/dim_advisor_fee_role/date=2026-10-20/data.parquet (the ONE key) | COMPACT-APPLY readback_equal=True wrote=True; prior VersionId sha256 equals BEFORE; every other key present with equal ETag | COMPACT-APPLY date=2026-10-20 prior_version=DHV5BykUPo_kPlbZZ9Umf_dJkooaLzTH new_version=3yoa4VexY5YhzGcdRDdb6E6YKgqjusj0 rows_before=288195 rows_after=6670 readback_equal=True wrote=True (apply 2026-10-21T07:21:37Z, ONE run); plan line current_equal=True runs_equal=True merged=281525; prior version re-downloaded, sha256 27b31393615b455130411c0eac01cc68f815b3a40a1387d1ab49fc6eed838559 equals BEFORE, one-byte mutant unequal; dim_advisor_fee_role 55 -> 55 objects, 1 key changed (the compacted one), 54 others equal ETag; dim_account_xref 55 -> 55, 0 changed; key versions 1 -> 2, none deleted | CLOSED 20261021T072305Z |

## Log

- 20261021T071905Z OPENED by 0.7.0_AE_CloudOps~NFRA2 with 1 leg(s)
- 20261021T072305Z LEG L1 closed: COMPACT-APPLY date=2026-10-20 prior_version=DHV5BykUPo_kPlbZZ9Umf_dJkooaLzTH new_version=3yoa4VexY5YhzGcdRDdb6E6YKgqjusj
- 20261021T072305Z CLOSED -- all 1 legs proven
