# Deploy Completion Record
**Date opened:** 2026-09-29T00:23:16.764013+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T010544Z
**Deploy:** IRPT_BCKEND.TO-IB-er-201: holdings-basis gold thread, 49F account 0010498003, YTD 2026-01-02..2026-09-25 (ad-hoc QA run; no reader switched)
**Authored by:** 0.4.0_DS_ClientPlatform~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of data/assets/scripts/gold/irpt_holdings_performance/ (sources.json + holdings_performance.py + tests) | commit hash, local unit tests 9 passed | commit 23004aaf98 on CLOUD by 0.4.0_DS_ClientPlatform~E, 8 files, 1072 insertions; 9 unit tests pass; naming gate PASS 3 graded 0 REFUSE; msg-verify MATCH len=7312 | CLOSED 20260929T010528Z |
| L2 | s3-prefix | s3://opal-data-49financial/irpt/49financial/gold/holdings_performance_daily/ 184 YTD partitions | ListObjectsV2 partition count + stream_parquet ETag==MD5 per partition | ListObjectsV2 over both builder addresses: 184 landed partitions each on holdings_performance_daily and holdings_performance_manifest, expected 184 trading days, missing 0, extra 0, range 2026-01-02..2026-09-25; every partition ETag==local MD5 inside stream_parquet.finalize(); bucket AES256 no KMS so the identity holds | CLOSED 20260929T010528Z |
| L3 | verify | E1-AC1 recompute match and E1-AC2 YTD coverage | the two PASS lines from the COO checks in deliverables/2.0.0_SA_COO~P/checks/r1e/ | E1-AC1 PASS (recompute 0.004612117916 == gold, excluded 0) exit 0 unpiped, against the amended check @5e273c614f; E1-AC2 PASS (184 trading days, 0 missing, chained YTD 0.058285) exit 0 unpiped; planted mutant +1e-6 FIRED AC1 to FAIL and restore returned PASS; proof-of-spec VALID rc=0 | CLOSED 20260929T010528Z |

## Log

- 20260929T002316Z OPENED by 0.4.0_DS_ClientPlatform~E with 3 leg(s)
- 20260929T010528Z LEG L1 closed: commit 23004aaf98 on CLOUD by 0.4.0_DS_ClientPlatform~E, 8 files, 1072 insertions; 9 unit tests pass; naming gate PASS 3
- 20260929T010528Z LEG L2 closed: ListObjectsV2 over both builder addresses: 184 landed partitions each on holdings_performance_daily and holdings_perform
- 20260929T010528Z LEG L3 closed: E1-AC1 PASS (recompute 0.004612117916 == gold, excluded 0) exit 0 unpiped, against the amended check @5e273c614f; E1-AC2
- 20260929T010544Z CLOSED -- all 3 legs proven
