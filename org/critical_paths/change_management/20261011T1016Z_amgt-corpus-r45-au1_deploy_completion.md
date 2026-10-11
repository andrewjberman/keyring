# Deploy Completion Record
**Date opened:** 2026-10-11T10:16:32.877409+00:00
**Status:** OPEN
**Deploy:** AMGT_CORPUS r45 au-1/au-2: bronze ingest at site Z (LATE-OPENED: the act ran 2026-10-11T09:47:52Z-09:59:50Z under order TO-WRITE-R45-au1; the issuer opened this entry after the fact, at ~10:2xZ, and says so)
**Authored by:** 2.0.0_SA_COO~C1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | ingest --write at site Z (write-once bronze_put, resolved-folder files) | resolved_folders ... stored N (put_performed P existed E) read_failed 0, evidence @cc1f7b2dfa |  | OPEN |
| L2 | verify | ingest --verify and the accounting script on the committed bytes | objects N files N match N mismatch 0; au1 accounting ... identity OK |  | OPEN |
| L3 | verify | issuer's independent read: the put_performed keys exist in S3 and AC1-AC4 re-run on the committed evidence | head_object ok P of P; AC1 1, AC3 2, AC4 1 |  | OPEN |

## Log

- 20261011T101632Z OPENED by 2.0.0_SA_COO~C1 with 3 leg(s)
