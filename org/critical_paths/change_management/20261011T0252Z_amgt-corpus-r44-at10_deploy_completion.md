# Deploy Completion Record
**Date opened:** 2026-10-11T02:52:48.919370+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T034138Z
**Deploy:** AMGT_CORPUS r44 at-10: dossier re-write at METHOD /11 (team_sheet stored in the dossier)
**Authored by:** 2.0.0_SA_COO~C1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | leg 0 gate: dossier.py and team_sheet.py equal 3bff293266, fitz real in the write process, per-name /10 object printed | diff empty, fitz real line, LEG0 count N of 95 | gate diff 0 lines vs 3bff293266; fitz real 1.28.2 (Python314 site-packages); method /11 asserted; LEG0 names_with_a_/10_object 95 of 95, 0 left out (evidence/r44_at10_leg0_20261011.txt) | CLOSED 20261011T025455Z |
| Lw | activation | dossier.write_one per name at METHOD /11, 6 threads, real fitz | 95 written once (or each failure listed, Branch B; names without a /10 object left out and listed) | 95 of 95 written once at METHOD /11 by dossier.write_one, 6 threads of one process, 02:54Z-03:3xZ, fitz real 1.28.2 asserted in-process; failed 0, wrote0 0, left_out 0 (evidence/r44_at10_leg_w_write_log_20261011.txt) | CLOSED 20261011T033128Z |
| Lv | verify | at10_diff.py --post on the WRITTEN /11 objects: every field of every name vs /10, stored team_sheet vs the reader | newfield team_sheet on all, changed only model_rows printed whole, dropped 0, stored equals reader n/n | at10_diff.py --post on the WRITTEN /11 objects: names 95 fields 2280 same 2090 newfield 95 (team_sheet on all, nothing else) changed 95 (model_rows only: 7135 rows stamp-only 20261009T13xxZ->20261010T13xxZ, 572 rows stamp+value; each printed whole) dropped 0 changed_outside_inputs 0 ts_equal_reader 95/95; team_sheet classes own_new 21 own_model 11 master_absent 63; build 1/1 (evidence/r44_at10_leg_v_diff_20261011.txt) | CLOSED 20261011T034138Z |

## Log

- 20261011T025248Z OPENED by 2.0.0_SA_COO~C1 with 3 leg(s)
- 20261011T025455Z LEG L0 closed: gate diff 0 lines vs 3bff293266; fitz real 1.28.2 (Python314 site-packages); method /11 asserted; LEG0 names_with_a_/10_
- 20261011T033128Z LEG Lw closed: 95 of 95 written once at METHOD /11 by dossier.write_one, 6 threads of one process, 02:54Z-03:3xZ, fitz real 1.28.2 asse
- 20261011T034138Z LEG Lv closed: at10_diff.py --post on the WRITTEN /11 objects: names 95 fields 2280 same 2090 newfield 95 (team_sheet on all, nothing e
- 20261011T034138Z CLOSED -- all 3 legs proven
