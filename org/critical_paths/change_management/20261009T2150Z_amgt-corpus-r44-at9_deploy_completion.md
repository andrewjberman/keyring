# Deploy Completion Record
**Date opened:** 2026-10-09T21:50:16.971133+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T222932Z
**Deploy:** AMGT_CORPUS r44 at-9: dossier re-write at METHOD /10 with real fitz (fix forward for D1-S2)
**Authored by:** 2.0.0_SA_COO~C1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| Lw | activation | dossier.write_one per name at METHOD /10, 6 threads, fitz asserted REAL in-process (a stub aborts) | 95 names written once (or each failure listed, Branch B) | 95 of 95 written once at METHOD amgt-corpus-dossier/10 by dossier.write_one in 6 threads of one process, 22:0xZ-22:2xZ; the driver asserted fitz REAL in-process before any write ('fitz real version 1.28.2 file ...site-packages\fitz\__init__.py', 'method amgt-corpus-dossier/10'), no stub anywhere (CTO half condition 1); FAIL 0; nothing overwritten; /7 /8 /9 kept. | CLOSED 20261009T222504Z |
| Lv | verify | at9_diff.py --post on the WRITTEN /10 objects: every field of all 95 vs /7 and /9 | both_differ 0; GAIN9 == the 12; cases restored 6/6; every ALL-DIFFER and changed-input field printed whole | at9_diff.py --post on the WRITTEN /10 objects (fitz real 1.28.2): names 95 fields 2185 same 2072 gain9 107 restore7 6 both_differ 0 all_differ 0 cases_restored 6/6; GAIN-MISSING 0 (all 12 /9 gains kept); the 95 extra GAIN9 are every name's model_rows equal to /9 (the daily model block changed since /7), the half's named changed-input class, printed WHOLE (condition 2). evidence/r44_at9_leg_v_20261009.txt. Branch A on the half's terms; leg p (RESAPP mm-4) waits on the CVO's grade (condition 3). | CLOSED 20261009T222932Z |

## Log

- 20261009T215016Z OPENED by 2.0.0_SA_COO~C1 with 2 leg(s)
- 20261009T222504Z LEG Lw closed: 95 of 95 written once at METHOD amgt-corpus-dossier/10 by dossier.write_one in 6 threads of one process, 22:0xZ-22:2xZ; 
- 20261009T222932Z LEG Lv closed: at9_diff.py --post on the WRITTEN /10 objects (fitz real 1.28.2): names 95 fields 2185 same 2072 gain9 107 restore7 6 bo
- 20261009T222932Z CLOSED -- all 2 legs proven
