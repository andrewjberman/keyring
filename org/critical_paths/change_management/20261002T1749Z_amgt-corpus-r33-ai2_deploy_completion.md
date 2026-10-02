# Deploy Completion Record
**Date opened:** 2026-10-02T17:49:39.111427+00:00
**Status:** OPEN
**Deploy:** AMGT_CORPUS round 33 CRPS-ai-2: scoped remeasure of the 11 DECIMAL-by-magnitude names + one re-derive each + their dossiers (pair COO e748581d10 / CTO 45a11d1ea8)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| a | activation | build_unit_map --securities <the 11> --remeasure on field_map.json | m33 vs HEAD: fields_unit 7, status_moves 12, other_keys 10, unit_evidence 323, raw_stamp 123, value_sampled 27, other_securities 0 | build_unit_map --securities <the 11> --remeasure at a48c546a1c, rc 0, 11 x 66 field entries; m33 vs HEAD: fields_unit 7 (13 labels: 9 -> PERCENT, 6 -> UNRESOLVED-ON-), status_moves 12, other_keys 10, unit_evidence 323, raw_stamp 123, value_sampled 27, other_securities 0 -- equal to the signed table. The 3 producer-path files that landed after the gate (RESAPP am-1 59c2ef1b23: lib/research/api/scoped_amgt.py + 2 tests) are outside the act's import closure (re-read at leg a) (evidence/r33_ai2_leg_a.txt) | CLOSED 20261002T175759Z |
| b | git | field_map.json commit on CLOUD | commit hash |  | OPEN |
| c | activation | model_block_pull derive --no-sa-fallback over the 11 names | each block == its captured dry-run block (vintage stripped); 0 value moves; exactly 11 new block objects |  | OPEN |
| d | activation | dossier write_one over the 11 | at most one new object per name; inputs_equal_now |  | OPEN |
| v | verify | served census over 100 keys + negative arms + per-family figures | DECIMAL 77 -> 0; UNRESOLVED 11 -> 19; moved keys = the 11; value_moves 0; BA BEST_DIV_YLD PERCENT; ORA ROIC / BP ROE / JD OPER_MARGIN value+unit printed |  | OPEN |

## Log

- 20261002T174939Z OPENED by 2.0.0_SA_COO~X with 5 leg(s)
- 20261002T175759Z LEG a closed: build_unit_map --securities <the 11> --remeasure at a48c546a1c, rc 0, 11 x 66 field entries; m33 vs HEAD: fields_unit 7 
