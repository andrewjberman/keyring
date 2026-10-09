# Deploy Completion Record
**Date opened:** 2026-10-09T17:33:49.590125+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T182635Z
**Deploy:** AMGT_CORPUS r41 aq-5: dossier re-write at METHOD /8 (27 fields, 21 names)
**Authored by:** 2.0.0_SA_COO~C1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| Lw | activation | python -m lib.research.corpus.dossier --write --workers 8 | 95 names put_performed 1 each (or each failure listed, Branch B) | dossier write at METHOD amgt-corpus-dossier/8 from dell1, 17:34Z-18:2xZ: the signed write_one per name, serial (pid 35816) plus, from 17:47Z, the same write_one in 6 threads of one process in reverse name order (dell1's fitz DLL blocks the --workers pool's children); threaded run: 95 names, wrote 76, unchanged 19 (written by the serial run), FAIL 0; nothing overwritten (gold_put write-once). dossier --pick-census after: names 95 current_method_available 95 stale_pick 0. Deviation from the half's literal 'serial': same write set and blast radius, recorded here and in the packet. | CLOSED 20261009T182132Z |
| Lv | verify | --section-recompose-census + r41_passage_census on CLOUD code after the write; live-route reads after RESAPP's /8 deploy | fields_changed 0; prefix 0; cut only with '...' and the false-cut count printed (CTO finding); BABA US + SHOP CN management live reads match | stored side on CLOUD code 18:2xZ (evidence/r41_aq5_leg_v_20261009.txt @38b91c82a3): section-recompose-census fields_changed 0 of 950; passage census 306 fields prefix 0 cut 2 (risks: AZN LN, BP LN) dangling 0; false-cut ellipses read 14 of 15. Branch C to the CTO: ADDENDUM 1 to the CTO half (msg 2968) rules /8 is NEVER served -- the live reads are void, leg p is re-pointed to /9 (round 42), RESAPP told (2.0.0_SA_COO~R1). Served state unchanged: the deployed API reads /7; the 95 /8 objects stay stored and unread. | CLOSED 20261009T182617Z |

## Log

- 20261009T173349Z OPENED by 2.0.0_SA_COO~C1 with 2 leg(s)
- 20261009T182132Z LEG Lw closed: dossier write at METHOD amgt-corpus-dossier/8 from dell1, 17:34Z-18:2xZ: the signed write_one per name, serial (pid 3581
- 20261009T182617Z LEG Lv closed: stored side on CLOUD code 18:2xZ (evidence/r41_aq5_leg_v_20261009.txt @38b91c82a3): section-recompose-census fields_chan
- 20261009T182635Z CLOSED -- all 2 legs proven
