# Deploy Completion Record
**Date opened:** 2026-09-29T06:17:38.170590+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T064938Z
**Deploy:** AMGT_CORPUS round 10: dossier --write --workers 10 over 95 names at dossier/3 (unit claim, six tables' own reason, import without PDF libs); pair COO 1323991818 / CTO 0db5dfb586
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W | activation | dossier --write --workers 10 over every resolved name (served research-dossier) | 95 put_performed, 0 ERROR; objects 656 -> 751; read_dossier serves the last write 95 of 95 | evidence/r10_dossier_rewrite.log: dossier --write --workers 10, rc 0, 0 ERROR, 'names 95 written 95 existed 0' (the count the COO half read per name from the join: every stored object /2, code /3). evidence/r10_rewrite_after.txt: partitions 95 objects 751 (656+95), read_dossier serves the last write 95 of 95, rewrites_on_unchanged_inputs 37 | CLOSED 20260929T064937Z |
| V | verify | pick + case census on the served table | dossier_pick current_method_available 95 stale_pick 0; case_census equal to the before-state line | evidence/r10_rewrite_after.txt: dossier_pick names 95 current_method_available 95 stale_pick 0; case_census line byte-identical to the before-state (body 84 ... unit_carried 10 currency_set 1 currency_null 27). Real run evidence/r10_real_run.txt: ML_FP base unit U+20AC currency EUR; AZN_LN unit U+00A3 currency null (differs from the listing); TSM_US base ABSENT with its own layout reason | CLOSED 20260929T064938Z |

## Log

- 20260929T061738Z OPENED by 2.0.0_SA_COO~X with 2 leg(s)
- 20260929T064937Z LEG W closed: evidence/r10_dossier_rewrite.log: dossier --write --workers 10, rc 0, 0 ERROR, 'names 95 written 95 existed 0' (the coun
- 20260929T064938Z LEG V closed: evidence/r10_rewrite_after.txt: dossier_pick names 95 current_method_available 95 stale_pick 0; case_census line byte-id
- 20260929T064938Z CLOSED -- all 2 legs proven
