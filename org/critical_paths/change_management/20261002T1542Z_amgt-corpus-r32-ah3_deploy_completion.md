# Deploy Completion Record
**Date opened:** 2026-10-02T15:42:17.123205+00:00
**Status:** OPEN
**Deploy:** AMGT_CORPUS round 32 CRPS-ah-3: scoped remeasure of the 4 DECIMAL-labelled BEST_DIV_YLD names + one re-derive each + their dossiers (pair COO c216d1a52f / CTO b859ebff4c)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| a | activation | build_unit_map --securities BA/GOOGL/HEI/PWR US Equity --remeasure on field_map.json | m32 vs HEAD: fields_unit 2, unit_evidence 146, raw_stamp 31, derived_by 31, value_sampled 7, status_moves 0, other_securities 0 |  | OPEN |
| b | git | field_map.json commit on CLOUD | commit hash |  | OPEN |
| c | activation | model_block_pull derive --no-sa-fallback over the 4 names | each block == its captured dry-run block (vintage stripped); 0 value moves; exactly 4 new block objects |  | OPEN |
| d | activation | dossier write_one over the 4 | at most one new object per name; inputs_equal_now 4/4 |  | OPEN |
| v | verify | served census over 100 keys + negative arms | BEST_DIV_YLD DECIMAL 12 -> 0; EQY_DVD_YLD_IND DECIMAL 16 -> 13; value_moves 0; moved keys = the 4; HEI EQY_DVD_YLD_IND DECIMAL; JD OPER_MARGIN unchanged |  | OPEN |

## Log

- 20261002T154217Z OPENED by 2.0.0_SA_COO~X with 5 leg(s)
