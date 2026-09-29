# Deploy Completion Record
**Date opened:** 2026-09-29T02:01:10.154271+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T022847Z
**Deploy:** AMGT_CORPUS round 9: dossier --write --workers 10 over 95 names at dossier/2 (table-aware cases); pair COO b98e09953e / CTO 9ffd945889; lifts Z-S53
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W | activation | dossier --write --workers 10 over every resolved name (served research-dossier) | 95 put_performed, 0 ERROR; objects 468 -> 563; read_dossier serves the last write 95 of 95 | evidence/r9_dossier_rewrite.log: dossier --write --workers 10 at 19458b6130-equivalent code, 02:02-02:25:08Z, 'names 95 written 95 existed 0', 95 put_performed 1, 0 ERROR, rc 0. evidence/r9_rewrite_after.txt: partitions 95 objects 563 (468+95), read_dossier serves the last write 95 of 95, rewrites_on_unchanged_inputs 37 (unchanged) | CLOSED 20260929T022846Z |
| V | verify | pick + case census on the served table | dossier_pick current_method_available 95 stale_pick 0; case_census body 84 heading_only 0 absent 201 ordering_violated 0 unit_carried 10 | evidence/r9_rewrite_after.txt: dossier_pick names 95 current_method_available 95 stale_pick 0; case_census names 95 slots 285 body 84 heading_only 0 absent 201 sum 285 ordering_held 28 ordering_violated 0 ordering_na 67 unit_carried 10 (equal to the in-memory census at 19458b6130). Real run evidence/r9_real_run_read_dossier.txt: ADBE Price 2026 416/233/143 at 16.0x/9.0x/6.0x unit null; AZN 227.08/131.91/45.24 unit U+00A3; page 0 | CLOSED 20260929T022846Z |

## Log

- 20260929T020110Z OPENED by 2.0.0_SA_COO~X with 2 leg(s)
- 20260929T022846Z LEG W closed: evidence/r9_dossier_rewrite.log: dossier --write --workers 10 at 19458b6130-equivalent code, 02:02-02:25:08Z, 'names 95 
- 20260929T022846Z LEG V closed: evidence/r9_rewrite_after.txt: dossier_pick names 95 current_method_available 95 stale_pick 0; case_census names 95 slot
- 20260929T022847Z CLOSED -- all 2 legs proven
