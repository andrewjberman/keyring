# Deploy Completion Record
**Date opened:** 2026-09-29T10:39:16.442303+00:00
**Status:** OPEN
**Deploy:** AMGT_CORPUS round 12: merge CRPS-n-1 (dossier TABLE/ARTIFACT -> research_dossier, builder prefix) and IMMEDIATELY dossier --write --workers 10 into amgt/harvest/gold/research_dossier/ (0 -> 95); legacy research-dossier/ untouched at 846; pair COO 700dcc6190 / CTO 4dead72211
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | git | merge wk-crps12-1 (ce3192a363) into CLOUD via safe-merge | merge commit hash; ce3192a363 an ancestor of HEAD |  | OPEN |
| W | activation | dossier --write --workers 10 from the merged code (served research_dossier) | 95 put_performed, 0 ERROR; new prefix 95 objects 95 partitions; legacy 846 |  | OPEN |
| V | verify | served at the new prefix | serves the last write 95 of 95; current_method_available 95 stale_pick 0; case_census equal to round 11's line |  | OPEN |

## Log

- 20260929T103916Z OPENED by 2.0.0_SA_COO~X with 3 leg(s)
