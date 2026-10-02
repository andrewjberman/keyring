# Deploy Completion Record
**Date opened:** 2026-10-02T15:42:17.123205+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T161106Z
**Deploy:** AMGT_CORPUS round 32 CRPS-ah-3: scoped remeasure of the 4 DECIMAL-labelled BEST_DIV_YLD names + one re-derive each + their dossiers (pair COO c216d1a52f / CTO b859ebff4c)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| a | activation | build_unit_map --securities BA/GOOGL/HEI/PWR US Equity --remeasure on field_map.json | m32 vs HEAD: fields_unit 2, unit_evidence 146, raw_stamp 31, derived_by 31, value_sampled 7, status_moves 0, other_securities 0 | build_unit_map --securities BA/GOOGL/HEI/PWR US Equity --remeasure at 44baa06d07, rc 0, 4 x 66 field entries; m32 vs HEAD: fields_unit 2 (BEST_DIV_YLD x4 names, EQY_DVD_YLD_IND GOOGL; all DECIMAL -> PERCENT), unit_evidence 146, raw_stamp 31, derived_by 31, value_sampled 7, status_moves 0, other_keys 0, other_securities 0 -- equal to the signed table (evidence/r32_ah3_leg_a.txt) | CLOSED 20261002T154518Z |
| b | git | field_map.json commit on CLOUD | commit hash | field_map.json committed on CLOUD at 7527f440e7 (LOCAL; push is MSTR's on Andrew's word), the sentinel with it | CLOSED 20261002T154703Z |
| c | activation | model_block_pull derive --no-sa-fallback over the 4 names | each block == its captured dry-run block (vintage stripped); 0 value moves; exactly 4 new block objects | capture (c32.py, 4 predecessors BA 20261001T070950Z, GOOGL/HEI/PWR 20260930) then model_block_pull derive --no-sa-fallback in 2 calls at 7527f440e7, rc 0 x2, stamps 20261002T154901Z..154906Z, 0 ERROR; compare: new_stamps 4, equal_dry_run 4/4 (vintage stripped), value_moves 0, case_value_moves 0; S3: exactly 4 new model_block objects over 4 keys since 15:48:50Z (evidence/r32_ah3_leg_c{,_capture,_verify}.txt) | CLOSED 20261002T155024Z |
| d | activation | dossier write_one over the 4 | at most one new object per name; inputs_equal_now 4/4 | d25.py write (D25_KEYS = the 4) at 6899726ed8: wrote 4, unchanged 0, errors 0, rc 0 (BA 15:55Z, GOOGL 15:58Z, HEI 16:01Z, PWR ~16:05Z); S3 structure since 15:52:39Z: exactly one new object 4/4, 0 other names, changed keys inputs + content_sha256 + as_of + fields.model_rows; inputs_equal_now 4/4 (evidence/r32_ah3_leg_d{,_structure,_inputs}.txt) | CLOSED 20261002T160940Z |
| v | verify | served census over 100 keys + negative arms | BEST_DIV_YLD DECIMAL 12 -> 0; EQY_DVD_YLD_IND DECIMAL 16 -> 13; value_moves 0; moved keys = the 4; HEI EQY_DVD_YLD_IND DECIMAL; JD OPER_MARGIN unchanged | v32.py census over the newest served block of 100 keys (37746 figures) at 16:09Z vs the pre-act stamp snapshot: BEST_DIV_YLD DECIMAL 12 -> 0; EQY_DVD_YLD_IND DECIMAL 16 -> 13; moved keys exactly the 4 (BA/GOOGL/HEI/PWR -> 20261002T1549Z), value_moves 0. Negative arms: HEI EQY_DVD_YLD_IND stays DECIMAL; JD OPER_MARGIN unit unchanged, stamp not moved; the other 96 newest stamps unchanged. Remaining DECIMAL-by-magnitude labels 77 (row Z-S82 amends Z-S81) (evidence/r32_ah3_leg_v_census.txt) | CLOSED 20261002T161105Z |

## Log

- 20261002T154217Z OPENED by 2.0.0_SA_COO~X with 5 leg(s)
- 20261002T154518Z LEG a closed: build_unit_map --securities BA/GOOGL/HEI/PWR US Equity --remeasure at 44baa06d07, rc 0, 4 x 66 field entries; m32 vs HEA
- 20261002T154703Z LEG b closed: field_map.json committed on CLOUD at 7527f440e7 (LOCAL; push is MSTR's on Andrew's word), the sentinel with it
- 20261002T155024Z LEG c closed: capture (c32.py, 4 predecessors BA 20261001T070950Z, GOOGL/HEI/PWR 20260930) then model_block_pull derive --no-sa-fallba
- 20261002T160940Z LEG d closed: d25.py write (D25_KEYS = the 4) at 6899726ed8: wrote 4, unchanged 0, errors 0, rc 0 (BA 15:55Z, GOOGL 15:58Z, HEI 16:01Z
- 20261002T161105Z LEG v closed: v32.py census over the newest served block of 100 keys (37746 figures) at 16:09Z vs the pre-act stamp snapshot: BEST_DIV
- 20261002T161106Z CLOSED -- all 5 legs proven
