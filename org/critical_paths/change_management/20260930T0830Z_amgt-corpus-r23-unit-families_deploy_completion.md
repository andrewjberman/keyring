# Deploy Completion Record
**Date opened:** 2026-09-30T08:30:51.643535+00:00
**Status:** OPEN
**Deploy:** AMGT_CORPUS round 23 y-4: unit-map rebuild (families) + commit, re-derive of 97 blocks under --no-sa-fallback, 93-dossier refresh, in order; pair COO 13f78a2b1b / CTO badff0ef3b; BP/_LN and NG/_LN excluded (Z-S64)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| a | activation | PYTHONPATH=<root> build_unit_map.py --population crosswalk on the committed map | 3012 entries, 66 fields, 0 shared, +NVDA, 0 top-level; round-22 8 entries unchanged | 08:33:21Z PYTHONPATH=<root> build_unit_map.py --population crosswalk rc 0; diff vs pre-image: entries_changed 3012 fields_touched 66 shared_changed 0 securities_added [NVDA US Equity] top_level_changed 0 round22_entries_unchanged 8 of 8 lf_only True (evidence/r23_y4_leg_a.txt) | CLOSED 20260930T083616Z |
| b | git | field_map.json commit | commit hash | field_map.json committed 67568b59c4 | CLOSED 20260930T083616Z |
| c | activation | model_block_pull derive --no-sa-fallback over the 97 | 97 new stamps; per-block unit-change counts = BLOCK lines; 0 value moves; filled_by_sa 0 | unit pass 08:37-08:41Z: 97 stamps, unit_changes 15425 = expected, 0 value moves, filled_by_sa 0 (r23_y4_leg_c_verify.txt); stop limb 2 fired on signs -> VERDICT B (msg 27053) -> reader fix y-5 merged 94301d5a9c -> sign pass (s) under pair COO 79ea7ae4ae / CTO bb3280c97e, 09:36-09:40Z: 50 blocks matching 50, sign_changes 1569 = expected, unit 0 value 0 other 0 case/formula 0 filled_by_sa 0; y5 over 97: plain_disagree 0 convention_disagree 0 (r23_sign_leg_s*.txt) | CLOSED 20260930T094311Z |
| d | activation | dossier write_one over the 93 | 93 puts; inputs_equal_now True; other_moves 0 outside model_rows |  | OPEN |
| v | verify | y1 census + one served read of a moved unit | no_family 0 crncy 0; served route shows the new unit |  | OPEN |

## Log

- 20260930T083051Z OPENED by 2.0.0_SA_COO~X with 5 leg(s)
- 20260930T083616Z LEG a closed: 08:33:21Z PYTHONPATH=<root> build_unit_map.py --population crosswalk rc 0; diff vs pre-image: entries_changed 3012 field
- 20260930T083616Z LEG b closed: field_map.json committed 67568b59c4
- 20260930T094311Z LEG c closed: unit pass 08:37-08:41Z: 97 stamps, unit_changes 15425 = expected, 0 value moves, filled_by_sa 0 (r23_y4_leg_c_verify.txt
