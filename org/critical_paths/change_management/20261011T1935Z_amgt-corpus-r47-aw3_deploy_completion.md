# Deploy Completion Record
**Date opened:** 2026-10-11T19:35:42.041664+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T201937Z
**Deploy:** AMGT_CORPUS r47 CRPS-aw-3: re-write the 95 research dossiers at method /13 (labels, corrected header, number formats, master rows), under the signed pair
**Authored by:** 2.0.0_SA_COO~C1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | gate: both halves signed, closure blobs equal the pair's, fitz real, every name holds a /12 object, none a /13 object | the leg-0 and --pre lines | evidence r47_aw3_pre_20261011.txt: 'aw3 pre names 95 without_a_/12_object 0 with_a_/13_object 0'; r47_aw3_write_20261011.txt: fitz real 1.28.2, method /13, 'LEG0 names_with_a_/12_object 95 of 95', 0 left out; both halves signed (CTO half msg 4086); closure blobs equal the pair's (git diff 7a58fb83fc HEAD empty over dossier.py, team_sheet.py, template.py) | CLOSED 20261011T201937Z |
| Lw | s3-prefix | opal-data-harvest gold research-dossier 95 partitions one new /13 object each | dossier_write_v13.py threads-done line (wrote 95 failed 0) | r47_aw3_write_20261011.txt 19:40:27Z-20:14:45Z: 'threads done names 95 wrote 95 failed 0 left_out 0', rc=0; OK 95 FAIL 0, each line ' wrote 1 ' with its gold research_dossier uri | CLOSED 20261011T201937Z |
| Lv | verify | the written /13 objects read back and diffed against /12 by aw3_diff.py --post | aw3 build 1/1 and the changed_outside_expected line | r47_aw3_diff_post_20261011.txt: 'aw3 names 95 fields 2280 same 2185 newfield 0 changed 95 dropped 0 changed_outside_expected 0'; 'aw3 own_old_keys_equal 32/32 master_as_predicted 63/63 shape 95/95 reader_equal 95/95'; 'aw3 build 1/1' rc=0; own FIGURE 3529 HEADING 107 CONTROL 123, master FIGURE 7938 HEADING 252 CONTROL 315, rows with a team value own 3529 master 0 | CLOSED 20261011T201937Z |

## Log

- 20261011T193542Z OPENED by 2.0.0_SA_COO~C1 with 3 leg(s)
- 20261011T201937Z LEG L0 closed: evidence r47_aw3_pre_20261011.txt: 'aw3 pre names 95 without_a_/12_object 0 with_a_/13_object 0'; r47_aw3_write_20261011
- 20261011T201937Z LEG Lw closed: r47_aw3_write_20261011.txt 19:40:27Z-20:14:45Z: 'threads done names 95 wrote 95 failed 0 left_out 0', rc=0; OK 95 FAIL 0
- 20261011T201937Z LEG Lv closed: r47_aw3_diff_post_20261011.txt: 'aw3 names 95 fields 2280 same 2185 newfield 0 changed 95 dropped 0 changed_outside_expe
- 20261011T201937Z CLOSED -- all 3 legs proven
