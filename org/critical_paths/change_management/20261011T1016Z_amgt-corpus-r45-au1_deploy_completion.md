# Deploy Completion Record
**Date opened:** 2026-10-11T10:16:32.877409+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T101658Z
**Deploy:** AMGT_CORPUS r45 au-1/au-2: bronze ingest at site Z (LATE-OPENED: the act ran 2026-10-11T09:47:52Z-09:59:50Z under order TO-WRITE-R45-au1; the issuer opened this entry after the fact, at ~10:2xZ, and says so)
**Authored by:** 2.0.0_SA_COO~C1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | ingest --write at site Z (write-once bronze_put, resolved-folder files) | resolved_folders ... stored N (put_performed P existed E) read_failed 0, evidence @cc1f7b2dfa | ingest --write ran 2026-10-11T09:47:52Z-09:59:50Z at site Z (HEAD b1428d28c7, executor ~ZC): resolved_folders 96 files_in_resolved 368 stored 368 (put_performed 12 existed 356) read_failed 0; placeholders_before 11 hydrated_ok 11; unresolved_files 10 in 6 folders; evidence @cc1f7b2dfa, an ancestor of origin/box/sitez a010dd8a8e (fetch read at 10:2xZ) | CLOSED 20261011T101657Z |
| L2 | verify | ingest --verify and the accounting script on the committed bytes | objects N files N match N mismatch 0; au1 accounting ... identity OK | committed evidence: objects 368 files 368 match 368 mismatch 0; au1 accounting census 378 resolved 368 unresolved 10 objects 368 identity OK; before and after censuses read folders 102 files 378 | CLOSED 20261011T101657Z |
| L3 | verify | issuer's independent read: the put_performed keys exist in S3 and AC1-AC4 re-run on the committed evidence | head_object ok P of P; AC1 1, AC3 2, AC4 1 | issuer re-ran the criteria on git show cc1f7b2dfa bytes: AC1 1, AC2 identity OK, AC3 2, AC4 1 (schtasks_named 1 dossier_writing 0); head_object on all 12 put_performed keys ok 12 of 12, LastModified within 12h; 356 existed rows read | CLOSED 20261011T101658Z |

## Log

- 20261011T101632Z OPENED by 2.0.0_SA_COO~C1 with 3 leg(s)
- 20261011T101657Z LEG L1 closed: ingest --write ran 2026-10-11T09:47:52Z-09:59:50Z at site Z (HEAD b1428d28c7, executor ~ZC): resolved_folders 96 files_i
- 20261011T101657Z LEG L2 closed: committed evidence: objects 368 files 368 match 368 mismatch 0; au1 accounting census 378 resolved 368 unresolved 10 obj
- 20261011T101658Z LEG L3 closed: issuer re-ran the criteria on git show cc1f7b2dfa bytes: AC1 1, AC2 identity OK, AC3 2, AC4 1 (schtasks_named 1 dossier_
- 20261011T101658Z CLOSED -- all 3 legs proven
