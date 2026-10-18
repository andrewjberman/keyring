# Deploy Completion Record
**Date opened:** 2026-10-18T00:55:32.016166+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cg-2: ADD-ONLY silver rewrite in s3 opal-data-harvest, table prefix amgt/harvest/silver/research-report/, 3 new parquet parts (date=2026-09-25 84 rows, 2026-09-23 121, 2026-09-24 148; 353 rows) adding fund_relation; window 2026-10-18 00:30Z to 02:30Z (site Z cleared, msg 7796); manifest cg2_written.out; rollback = S3 delete of the 3 keys, Andrew's act
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.5h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | worktree at a9aecdd593 (empty lib/research diff); census equals the COO half; dry run REBUILD-PLAN rows=353 new_parts=3; no scheduled typed.main task; UNH and CPA BEFORE reads | cg2_before.out |  | OPEN |
| C1 | activation | canary date 2026-09-25 (84 rows) written and read back equal=PASS | cg2_written.out + cg2_run.log |  | OPEN |
| R1 | activation | 2026-09-23 (121) then 2026-09-24 (148), one foreground command each, manifest checked after each | cg2_written.out + cg2_run.log |  | OPEN |
| V1 | verify | newest-per-report equals census (353), UNH and CPA gateway reads equal to step 0; cg2_served.out ends PARTS_WRITTEN_AND_READ_BACK, NEWEST_PER_REPORT_EQUALS_CENSUS, GATEWAY_READS_UNCHANGED | cg2_served.out |  | OPEN |
| Z1 | git | proof instance VALID, manifest and ledger close committed, report to the issuer | checker last line + commit hash |  | OPEN |

## Log

- 20261018T005532Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
