# Deploy Completion Record
**Date opened:** 2026-10-18T00:55:32.016166+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T012539Z
**Deploy:** AMGT_HARVST HVST-cg-2: ADD-ONLY silver rewrite in s3 opal-data-harvest, table prefix amgt/harvest/silver/research-report/, 3 new parquet parts (date=2026-09-25 84 rows, 2026-09-23 121, 2026-09-24 148; 353 rows) adding fund_relation; window 2026-10-18 00:30Z to 02:30Z (site Z cleared, msg 7796); manifest cg2_written.out; rollback = S3 delete of the 3 keys, Andrew's act
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.5h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | worktree at a9aecdd593 (empty lib/research diff); census equals the COO half; dry run REBUILD-PLAN rows=353 new_parts=3; no scheduled typed.main task; UNH and CPA BEFORE reads | cg2_before.out | PASS. cg2_before.out: worktree C:/tmp/cg2-build at a9aecdd593, 0 status lines, empty lib/research diff; COO half sha256 11cf6bd0.. equal; census CENSUS-FUND-RELATION rows=355 reports=353 securities=94 holding=121 candidate=14 initiate=2 interest=2 template=1 unclassified=0 none=213 and PROOF-NAMES equal to the order; dry run REBUILD-PLAN rows=353 skipped_unchanged=0 new_parts=3 dates=3 puts_recorded=3 puts_performed=0 with WOULD_PUT 121/148/84; scheduled-task read (second read with positive control; first void): no task runs typed.main or the induction; UNH and CPA BEFORE gateway reads | CLOSED 20261018T012539Z |
| C1 | activation | canary date 2026-09-25 (84 rows) written and read back equal=PASS | cg2_written.out + cg2_run.log | PASS. Canary date 2026-09-25 written 01:00:35Z (cg2_written.out): part-20261018T010034Z.parquet 84 rows 29937 B VersionId yBc6EvZM.kO9dg9EGIwLt2yJ1Rohe7UK; READBACK date=2026-09-25 rows=84 equal=PASS; issuer told 01:00:41Z; window 2026-10-18 00:30Z to 02:30Z (site Z cleared, msg 7796) | CLOSED 20261018T012539Z |
| R1 | activation | 2026-09-23 (121) then 2026-09-24 (148), one foreground command each, manifest checked after each | cg2_written.out + cg2_run.log | PASS. 2026-09-23 written 01:00:57Z (121 rows, 39348 B, VersionId jbGhhPNbW1LUml6sAJXjAP87SNItcFNx, READBACK equal=PASS) then 2026-09-24 written 01:01:14Z (148 rows, 44617 B, VersionId fm_D9nDO1V5iTTToDHQURpxo2iCfOx7V, READBACK equal=PASS), one foreground python -u command each, manifest read after each; manifest closes WRITTEN parts=3 rows=353 | CLOSED 20261018T012539Z |
| V1 | verify | newest-per-report equals census (353), UNH and CPA gateway reads equal to step 0; cg2_served.out ends PARTS_WRITTEN_AND_READ_BACK, NEWEST_PER_REPORT_EQUALS_CENSUS, GATEWAY_READS_UNCHANGED | cg2_served.out | PASS. cg2_newest.out: 353 of 353 newest rows from the new parts carry fund_relation, counts equal the census, six PROOF-NAMES equal; cg2_after_reads.out: UNH and CPA content_sha256 and field entries equal; the two differences (research_reports[].part and source_keys name the new parts) ruled EXPECTED by the issuer in AMENDMENT 2 (commit 17ede77bad, msg 7811); cg2_served.out ends PARTS_WRITTEN_AND_READ_BACK=PASS, NEWEST_PER_REPORT_EQUALS_CENSUS=PASS, GATEWAY_READS_UNCHANGED=PASS | CLOSED 20261018T012539Z |
| Z1 | git | proof instance VALID, manifest and ledger close committed, report to the issuer | checker last line + commit hash | PASS. proof instance VALID (rc=0) at the cg-2 commit 5576a9c77b; manifest and ledger close committed; report to the issuer. Push state LOCAL (ls-remote origin box/dell1 = c36ae2cda8; push is integrator-only) | CLOSED 20261018T012539Z |

## Log

- 20261018T005532Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
- 20261018T012539Z LEG S0 closed: PASS. cg2_before.out: worktree C:/tmp/cg2-build at a9aecdd593, 0 status lines, empty lib/research diff; COO half sha256 
- 20261018T012539Z LEG C1 closed: PASS. Canary date 2026-09-25 written 01:00:35Z (cg2_written.out): part-20261018T010034Z.parquet 84 rows 29937 B VersionI
- 20261018T012539Z LEG R1 closed: PASS. 2026-09-23 written 01:00:57Z (121 rows, 39348 B, VersionId jbGhhPNbW1LUml6sAJXjAP87SNItcFNx, READBACK equal=PASS) 
- 20261018T012539Z LEG V1 closed: PASS. cg2_newest.out: 353 of 353 newest rows from the new parts carry fund_relation, counts equal the census, six PROOF-
- 20261018T012539Z LEG Z1 closed: PASS. proof instance VALID (rc=0) at the cg-2 commit 5576a9c77b; manifest and ledger close committed; report to the issu
- 20261018T012539Z CLOSED -- all 5 legs proven
