# Deploy Completion Record
**Date opened:** 2026-10-11T13:13:06.391111+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T135320Z
**Deploy:** AMGT_CORPUS r46 av-3: dossier re-write at METHOD /12 (team_sheet row classes and the team's own period values); OPENED BEFORE leg w
**Authored by:** 2.0.0_SA_COO~C1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | gate: dossier.py and team_sheet.py equal f583a91842, fitz real in the write process, per-name /11 object printed | gate diff 0 lines, fitz real line, LEG0 count N of 95 | gate diff f583a91842..HEAD over dossier.py and team_sheet.py: 0 lines; fitz real 1.28.2 (Python314 site-packages) asserted in the write process; method /12 asserted; ; no name left out; the CTO half SIGNED @ledger/NEVER_WIDEN_ROUND46_AV3_CTO_HALF.md (msg 3875); entry opened 13:13Z before leg w started 13:14Z | CLOSED 20261011T131450Z |
| Lw | activation | dossier.write_one per name at METHOD /12, 6 threads, real fitz | 95 written once (or each failure listed, Branch B) | dossier.write_one per name at METHOD /12, 6 threads of one process, 13:14Z-13:49Z, fitz real 1.28.2 asserted: printed 'threads done names 95 wrote 95 failed 0 left_out 0'; 95 OK rows each 'wrote 1'; 0 FAIL rows (evidence/r46_av3_write_20261011.txt). Leg 0's proof line was written in the same call as its count was read; the count printed afterwards is 95 of 95. | CLOSED 20261011T134934Z |
| Lv | verify | av3_diff.py --post on the WRITTEN /12 objects: every field of every name vs /11, the team_sheet arm | names 95, dropped 0, old keys equal, shape, stored equals reader, changed fields printed whole | av3_diff.py --post on the WRITTEN /12 objects (evidence/r46_av3_diff_post_20261011.txt): names 95 fields 2280 same 2090 newfield 0 changed 190 (team_sheet 95 + model_rows 95, each printed whole) dropped 0 changed_outside_expected 0; old_keys_equal 95/95 shape 95/95 reader_equal 95/95; row classes FIGURE 3381 HEADING 316 CONTROL 62 sum 3759 (the prediction); FIGURE rows with a team value 3381, without 0; by-source ESTIMATE bloomberg_candidate 497 team 2884 why 0; av3 build 1/1. Branch A. | CLOSED 20261011T135320Z |

## Log

- 20261011T131306Z OPENED by 2.0.0_SA_COO~C1 with 3 leg(s)
- 20261011T131450Z LEG L0 closed: gate diff f583a91842..HEAD over dossier.py and team_sheet.py: 0 lines; fitz real 1.28.2 (Python314 site-packages) assert
- 20261011T134934Z LEG Lw closed: dossier.write_one per name at METHOD /12, 6 threads of one process, 13:14Z-13:49Z, fitz real 1.28.2 asserted: printed 't
- 20261011T135320Z LEG Lv closed: av3_diff.py --post on the WRITTEN /12 objects (evidence/r46_av3_diff_post_20261011.txt): names 95 fields 2280 same 2090 
- 20261011T135320Z CLOSED -- all 3 legs proven
