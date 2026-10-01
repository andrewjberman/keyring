# Deploy Completion Record
**Date opened:** 2026-10-01T10:26:05.408954+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T132925Z
**Deploy:** INF NNA Branch A: three date-scoped excusals (866, 769, 1096; partition 2026-09-24) deployed to the runner's code prefix under both halves (packet blob fe5d59e3e1, CTO batch 79 @4e06e44bb7; row W97-S3)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | s3-prefix | s3://opal-data-inf/code/gold/lib/nna_coverage_excusals.json | the deployed object's sha256 equals the committed blob's 3c39f52c52ba... (11,014 bytes), new version id recorded, prior version EES7HN.rqCZl44pNLJpGbt_VWvKUhwim kept; code/gold/ count stays 170 | boto3 put_object 2026-10-01T10:27:12Z of the blob at 94aff463e3 (11,014 LF bytes): new version LZ_iKlMaf_MHGtg57Wo_ZZ2waRkqpcK.; read back sha256 3c39f52c52ba9f6e9d4ef98ae12b39b1015aaf0208fb1fe92946535da7b24229 equal to the committed blob; prior version EES7HN.rqCZl44pNLJpGbt_VWvKUhwim (7,114 bytes) kept as non-latest; code/gold/ lists 170 objects before and after; the deployed bytes load through the guard's own load_excusals (10 accounts; 866, 769, 1096 scoped to 2026-09-24; 866 not excused on 2026-09-23). No comp-pipescript MATCH line: the tool does not cover lib/*.json (0 of 104 matched), so the sha256 readback is the proof, as on leg D1 of inf-silver-ids-ship-20260930. | CLOSED 20261001T102921Z |
| V1 | verify | the first chain run after the put | from its own log: three EXCUSED lines naming 866, 769, 1096 with partitions ['2026-09-24'] and the OK: NNA partition coverage line; the 09-24 partition reads 6 rows with the packet's AFTER totals; the log read to its last step and any failed step or fired guard reported (CTO half item 7) | the first chain run after the put, chain_full_20261001_113344 (status.json: complete, 65 of 65 steps, 0 non-ok, errors empty, updated 12:50:26Z). Its own log s3://opal-data-inf/diagnostic/chain_logs/chain_full_20261001_113302.log (38,477 lines, read to its last line): L36867-36869 at 12:38:43Z 'NNA COVERAGE: account 769 ($10,000.00, [2026-09-24]) is EXCUSED [partitions [2026-09-24]]', the same for 866 ($-20,000.00) and 1096 ($10,000.00); L36870 'OK: NNA partition coverage -- 1,444 partition(s) being written, no account dropped from any of them (3 excused by review).' gold/canonical/canonical_nna_2026-09-24.parquet read 12:44Z: new version xGrZgj8e... written 12:39:34Z, 6 rows, accounts 866/769/1096 absent, inflow 150,000.00, outflow 27,627.10, net 122,372.90 (the packet's AFTER column); prior version ZTo9iCPp... kept. CTO half item 7, the 32 resumed steps: no FAILED step, no traceback, no regression; one WARN line carries the word FAILED about a historic date ([2026-05-20] bronze assets dim, a requests ReadTimeout recorded by a step's own check); 2,760 WARN lines in 39 shapes, the two largest being unpriced holdings rows (2,404) and dates with no prices (260). Branch 1 of the packet's section 5. | CLOSED 20261001T132925Z |

## Log

- 20261001T102605Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20261001T102921Z LEG D1 closed: boto3 put_object 2026-10-01T10:27:12Z of the blob at 94aff463e3 (11,014 LF bytes): new version LZ_iKlMaf_MHGtg57Wo_ZZ2wa
- 20261001T132925Z LEG V1 closed: the first chain run after the put, chain_full_20261001_113344 (status.json: complete, 65 of 65 steps, 0 non-ok, errors e
- 20261001T132925Z CLOSED -- all 2 legs proven
