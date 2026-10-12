# Deploy Completion Record
**Date opened:** 2026-10-11T23:50:25.101593+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T003014Z
**Deploy:** AMGT_CORPUS r49 CRPS-ay-3: re-write the 95 research dossiers at method /15 (every value under the header of its own block), under the signed pair
**Authored by:** 2.0.0_SA_COO~C1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | gate: both halves signed, closure blobs equal the pair's, fitz real, every name holds a /14 object, none a /15 object | the leg-0 and --pre lines | r49_ay3_pre_20261011.txt: 'LEG0 names_with_a_/14_object 95 of 95'; 'ay3 pre names 95 without_a_/14_object 0 with_a_/15_object 0'; fitz real 1.28.2 (r49_ay3_write_20261011.txt); closure blobs team_sheet ef4da7cdc85a dossier 7b67bf62afdd | CLOSED 20261012T003013Z |
| Lw | s3-prefix | opal-data-harvest gold research-dossier 95 partitions one new /15 object each | dossier_write_v15.py threads-done line (wrote 95 failed 0) | r49_ay3_write_20261011.txt 23:50:35Z-00:25:13Z: 'threads done names 95 wrote 95 failed 0 left_out 0', rc=0; OK 95 FAIL 0 | CLOSED 20261012T003014Z |
| Lv | verify | the written /15 objects read back and diffed against /14 by ay3_diff.py --post | ay3 build 1/1, the changed_outside_team_sheet line, master 63/63 and unread 12/12 lines | r49_ay3_diff_post_20261011.txt: 'ay3 build 1/1'; names 95 fields 2280 same 2185 changed 95 (team_sheet) dropped 0 changed_outside_team_sheet 0; team_sheet_ok 95/95 reader_equal 95/95; master 63/63 unread 12/12; split 3103 = period 401 + case 2690 + unread 12 | CLOSED 20261012T003014Z |

## Log

- 20261011T235025Z OPENED by 2.0.0_SA_COO~C1 with 3 leg(s)
- 20261012T003013Z LEG L0 closed: r49_ay3_pre_20261011.txt: 'LEG0 names_with_a_/14_object 95 of 95'; 'ay3 pre names 95 without_a_/14_object 0 with_a_/15_o
- 20261012T003014Z LEG Lw closed: r49_ay3_write_20261011.txt 23:50:35Z-00:25:13Z: 'threads done names 95 wrote 95 failed 0 left_out 0', rc=0; OK 95 FAIL 0
- 20261012T003014Z LEG Lv closed: r49_ay3_diff_post_20261011.txt: 'ay3 build 1/1'; names 95 fields 2280 same 2185 changed 95 (team_sheet) dropped 0 change
- 20261012T003014Z CLOSED -- all 3 legs proven
