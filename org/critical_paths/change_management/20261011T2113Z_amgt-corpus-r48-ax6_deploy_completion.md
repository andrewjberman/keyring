# Deploy Completion Record
**Date opened:** 2026-10-11T21:13:44.722384+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T215738Z
**Deploy:** AMGT_CORPUS r48 CRPS-ax-6: re-write the 95 research dossiers at method /14 (cross-workbook FactSet labels held; own-sheet measured wins), under the signed pair
**Authored by:** 2.0.0_SA_COO~C1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | gate: both halves signed, closure blobs equal the pair's, fitz real, every name holds a /13 object, none a /14 object | the leg-0 and --pre lines | r48_ax6_pre_20261011.txt: 'ax6 pre names 95 without_a_/13_object 0 with_a_/14_object 0'; r48_ax6_write_20261011.txt: fitz real 1.28.2, method /14, 'LEG0 names_with_a_/13_object 95 of 95', 0 left out; CTO half SIGNED msg 4121; closure blobs equal the pair's (git diff 805af73ebb HEAD empty over dossier.py, team_sheet.py, factset_descriptions.json) | CLOSED 20261011T215737Z |
| Lw | s3-prefix | opal-data-harvest gold research-dossier 95 partitions one new /14 object each | dossier_write_v14.py threads-done line (wrote 95 failed 0) | r48_ax6_write_20261011.txt 21:18:13Z-21:53:11Z: 'threads done names 95 wrote 95 failed 0 left_out 0', rc=0; OK 95 FAIL 0, each ' wrote 1 ' with its gold research_dossier uri | CLOSED 20261011T215737Z |
| Lv | verify | the written /14 objects read back and diffed against /13 by ax6_diff.py --post | ax6 build 1/1 and the changed_outside_team_sheet line | r48_ax6_diff_post_20261011.txt: 'ax6 names 95 fields 2280 same 2197 newfield 0 changed 83 dropped 0 changed_outside_team_sheet 0'; 'ax6 keys_equal 95/95 labels_as_predicted 95/95 shape 95/95 reader_equal 95/95 master_without_value 63'; 'ax6 build 1/1' rc=0; labels moved absent->held 252 over 83 names by code FF_COM_SHS_OUT 83 FF_NET_INC 82 FF_EPS_DIL_BEF_UNUSUAL 74 FF_CAPEX 4 FF_FREE_CF 3 FF_EBITDA_OPER 2 FF_EBIT_OPER 2 FF_BPS 1 FF_COM_SHS_OUT_EPS_DIL 1 | CLOSED 20261011T215738Z |

## Log

- 20261011T211344Z OPENED by 2.0.0_SA_COO~C1 with 3 leg(s)
- 20261011T215737Z LEG L0 closed: r48_ax6_pre_20261011.txt: 'ax6 pre names 95 without_a_/13_object 0 with_a_/14_object 0'; r48_ax6_write_20261011.txt: fit
- 20261011T215737Z LEG Lw closed: r48_ax6_write_20261011.txt 21:18:13Z-21:53:11Z: 'threads done names 95 wrote 95 failed 0 left_out 0', rc=0; OK 95 FAIL 0
- 20261011T215738Z LEG Lv closed: r48_ax6_diff_post_20261011.txt: 'ax6 names 95 fields 2280 same 2197 newfield 0 changed 83 dropped 0 changed_outside_team
- 20261011T215738Z CLOSED -- all 3 legs proven
