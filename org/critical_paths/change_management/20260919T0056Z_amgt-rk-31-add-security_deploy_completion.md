# Deploy Completion Record
**Date opened:** 2026-09-19T00:56:17.541706+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260919T014529Z
**Deploy:** AMGT-rk-31: add-a-security entry lands identity in the pool crosswalk
**Authored by:** 0.9.0_WK_AMGT_RESAPP~35
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the safe-commit landing add_security.py, crosswalk.py, crosswalk.schema.json, registrations.json, tests | commit hash on wk-amgt-14-35 | commit 0add9d26c1 on branch wk-amgt-14-35 (0.9.0_WK_AMGT_RESAPP~35) | CLOSED 20260919T014529Z |
| L2 | verify | write_pool() receipt on crosswalk/v1/<today>.json | key, ContentLength, document-sha256 read back | write_pool() receipt: key=crosswalk/v1/2026-09-19.json ContentLength=202505 document-sha256=6668326f3d1b4d09083560c86652635c5e029eeaff56606ef5f95dfadd1c3cc7 schema-version=1 records=96 MEASURED=36 UNRESOLVED=60 registered=7 -- head_object read back inside write_pool() per crosswalk.py:638-649 | CLOSED 20260919T013625Z |
| L3 | verify | AC6 NEVER-WIDEN on the population of record | base_records_byte_identical_in_newest N of N, DELTA=0 | AC6: base 2026-09-15 records 89, newest crosswalk/v1/2026-09-19.json records 96 MEASURED 36 registered 7, base_records_byte_identical_in_newest 89 of 89 -- DELTA=0 on the 33 (89) coverage records | CLOSED 20260919T013625Z |

## Log

- 20260919T005617Z OPENED by 0.9.0_WK_AMGT_RESAPP~35 with 3 leg(s)
- 20260919T013625Z LEG L2 closed: write_pool() receipt: key=crosswalk/v1/2026-09-19.json ContentLength=202505 document-sha256=6668326f3d1b4d09083560c86652
- 20260919T013625Z LEG L3 closed: AC6: base 2026-09-15 records 89, newest crosswalk/v1/2026-09-19.json records 96 MEASURED 36 registered 7, base_records_b
- 20260919T014529Z LEG L1 closed: commit 0add9d26c1 on branch wk-amgt-14-35 (0.9.0_WK_AMGT_RESAPP~35)
- 20260919T014529Z CLOSED -- all 3 legs proven
