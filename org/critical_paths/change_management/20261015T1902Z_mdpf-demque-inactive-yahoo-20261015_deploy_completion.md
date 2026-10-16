# Deploy Completion Record
**Date opened:** 2026-10-15T19:02:28.978951+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T011057Z
**Deploy:** MDPF_DEMQUE: Yahoo gate is the V2 active set, use_class index column, inactive-only Yahoo backfill (never-widen pair 5e62883899 / 55b747d57c)
**Authored by:** 2.0.0_SA_COO~Q1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 48.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | DQ-t-66 merged 6a557f1206 and DQ-t-68 merged 34bcd8390e on box/dell1 (folder 238 passed) | both merge hashes and the folder count | DQ-t-66 merged 6a557f1206, DQ-t-68 merged 34bcd8390e; pytest data/mdpf/scripts/demque 238 passed; py_compile OK; ruff F,E9 clean | CLOSED 20261015T190501Z |
| L2 | activation | YAHOO-INACTIVE-BACKFILL-01..04 placed in the draw queue (C:/Users/Test/.opal/demque/queue) | ls of the queue and sha256 of the four files | queue C:/Users/Test/.opal/demque/queue holds YAHOO-INACTIVE-BACKFILL-01..04 (sha256 prefixes 673829c1ddd5d734 83d0e6b1aab8c19a 0b5a1b6b67cdc536 5133ea08bd9d0aa5; cmp identical to the build); demand_queue._load_requests reads 11 requests, backfill last, after the tier-1 standing request | CLOSED 20261015T190502Z |
| L3 | verify | the first nightly run after the merge: exit code 0, keys written equal the store's changed versions and fall inside the permitted table | the run log line, ledger.jsonl rows and the S3 version list read | first run under the gate, started by hand 2026-10-15 23:54:42Z (schtasks /Run, same wrapper), OK: daily draw complete exit 0; S3 version list vs STORE_BASELINE_AFTER_2026-10-14: 9 keys changed on baseline names (6 lock, 3 prices), all in the run's appended list; 158 new names x 4 files; only other keys index.parquet and index.csv; 0 V2-held names touched; index 696 rows, use_class 528 NOT_FOR_ACTIVE / 168 INACTIVE_USE with 0 disagreeing; 400 of 400 requests, no pushback; receipt org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ROUND9_MANUAL_RUN_RECEIPT_20261015.md | CLOSED 20261016T011057Z |

## Log

- 20261015T190228Z OPENED by 2.0.0_SA_COO~Q1 with 3 leg(s)
- 20261015T190501Z LEG L1 closed: DQ-t-66 merged 6a557f1206, DQ-t-68 merged 34bcd8390e; pytest data/mdpf/scripts/demque 238 passed; py_compile OK; ruff F,
- 20261015T190502Z LEG L2 closed: queue C:/Users/Test/.opal/demque/queue holds YAHOO-INACTIVE-BACKFILL-01..04 (sha256 prefixes 673829c1ddd5d734 83d0e6b1aa
- 20261016T011057Z LEG L3 closed: first run under the gate, started by hand 2026-10-15 23:54:42Z (schtasks /Run, same wrapper), OK: daily draw complete ex
- 20261016T011057Z CLOSED -- all 3 legs proven
