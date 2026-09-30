# Deploy Completion Record
**Date opened:** 2026-09-29T10:39:16.442303+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T111838Z
**Deploy:** AMGT_CORPUS round 12: merge CRPS-n-1 (dossier TABLE/ARTIFACT -> research_dossier, builder prefix) and IMMEDIATELY dossier --write --workers 10 into amgt/harvest/gold/research_dossier/ (0 -> 95); legacy research-dossier/ untouched at 846; pair COO 700dcc6190 / CTO 4dead72211
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | git | merge wk-crps12-1 (ce3192a363) into CLOUD via safe-merge | merge commit hash; ce3192a363 an ancestor of HEAD | safe-merge wk-crps12-1 -> CLOUD merge d0141a6a76 (10:45:31Z); ce3192a363 an ancestor of HEAD 68cff9f6d6; working tree reads TABLE = research_dossier, ARTIFACT = research_dossier. The rewrite (leg W) started from the merged code in the same window. | CLOSED 20260929T104736Z |
| W | activation | dossier --write --workers 10 from the merged code (served research_dossier) | 95 put_performed, 0 ERROR; new prefix 95 objects 95 partitions; legacy 846 | dossier --write --workers 10 from merged d0141a6a76: names 95 written 95 existed 0, 95 put_performed 1, 0 ERROR, rc=0 ended 11:09:15Z (evidence/r12_dossier_rewrite.log); 11:16:51Z live list: research_dossier/ 95 objects 95 partitions, research-dossier/ 846 objects 95 partitions (unchanged) (evidence/r12_after_verify.txt) | CLOSED 20260929T111724Z |
| V | verify | served at the new prefix | serves the last write 95 of 95; current_method_available 95 stale_pick 0; case_census equal to round 11's line | 11:15Z reads from the new prefix: order census 'partitions 95 objects 95 / read_dossier serves the last write 95 of 95'; pick census 'names 95 current_method_available 95 stale_pick 0'; case census 'body 102 heading_only 0 absent 183 sum 285 ordering_held 34 ordering_violated 0 ordering_na 61 unit_carried 11 currency_set 5 currency_null 29' = round 11's line; read_dossier HEI/CPA/SHOP served from research_dossier/, fields+cases+inputs equal to legacy /4 object, artifact research_dossier (evidence/r12_after_*.txt) | CLOSED 20260929T111747Z |

## Log

- 20260929T103916Z OPENED by 2.0.0_SA_COO~X with 3 leg(s)
- 20260929T104736Z LEG M closed: safe-merge wk-crps12-1 -> CLOUD merge d0141a6a76 (10:45:31Z); ce3192a363 an ancestor of HEAD 68cff9f6d6; working tree re
- 20260929T111724Z LEG W closed: dossier --write --workers 10 from merged d0141a6a76: names 95 written 95 existed 0, 95 put_performed 1, 0 ERROR, rc=0 en
- 20260929T111747Z LEG V closed: 11:15Z reads from the new prefix: order census 'partitions 95 objects 95 / read_dossier serves the last write 95 of 95';
- 20260929T111838Z CLOSED -- all 3 legs proven
