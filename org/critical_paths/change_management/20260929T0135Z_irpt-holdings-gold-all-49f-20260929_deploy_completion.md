# Deploy Completion Record
**Date opened:** 2026-09-29T01:35:00.199159+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T015845Z
**Deploy:** IRPT_BCKEND.TO-IB-er-202: holdings-basis gold for EVERY 49F account, full history 2024-07-09..2026-09-25 (ad-hoc QA run; no reader switched)
**Authored by:** 0.4.0_DS_ClientPlatform~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of the round-2 producer changes (vectorized core, manifest completeness fields, manifest parquet, 4 new tests) | commit hash, 13 unit tests passing | commit e29adc9fa7 on CLOUD by 0.4.0_DS_ClientPlatform~E, 6 files, 417 insertions; 13 unit tests pass; naming gate PASS 0 REFUSE; msg-verify MATCH len=6120 | CLOSED 20260929T015844Z |
| L2 | s3-prefix | s3://opal-data-49financial/irpt/49financial/gold/holdings_performance_daily/ 557 partitions over every 49F account | ListObjectsV2 partition count + per-partition stream_parquet ETag==MD5 | ListObjectsV2: 557 partitions on each of holdings_performance_daily and holdings_performance_manifest, expected 557 trading days 2024-07-09..2026-09-25, missing 0, extra 0; 3,188,339 rows read back from the 557 parquet footers, equal to the producer tally; 0 empty partitions (min 4075, max 7540); every partition ETag==local MD5 inside stream_parquet.finalize() | CLOSED 20260929T015845Z |
| L3 | verify | E2-AC1 all-accounts completeness and E2-AC2 full-history coverage | the two PASS lines from the COO checks in deliverables/2.0.0_SA_COO~P/checks/r2e/ | E2-AC1 PASS (6341 silver accounts, 7540 gold rows, 0 missing, 0 duplicated, manifest 6341/6338/3 complete=True) exit 0 unpiped; E2-AC2 PASS (557 of 557 trading days, 0 missing) exit 0 unpiped; completeness mutant dropped one held account -> AC1 FAIL with the manifest still claiming complete, restored -> PASS and AC2 PASS; proof-of-spec VALID rc=0 | CLOSED 20260929T015845Z |

## Log

- 20260929T013500Z OPENED by 0.4.0_DS_ClientPlatform~E with 3 leg(s)
- 20260929T015844Z LEG L1 closed: commit e29adc9fa7 on CLOUD by 0.4.0_DS_ClientPlatform~E, 6 files, 417 insertions; 13 unit tests pass; naming gate PASS 0
- 20260929T015845Z LEG L2 closed: ListObjectsV2: 557 partitions on each of holdings_performance_daily and holdings_performance_manifest, expected 557 trad
- 20260929T015845Z LEG L3 closed: E2-AC1 PASS (6341 silver accounts, 7540 gold rows, 0 missing, 0 duplicated, manifest 6341/6338/3 complete=True) exit 0 u
- 20260929T015845Z CLOSED -- all 3 legs proven
