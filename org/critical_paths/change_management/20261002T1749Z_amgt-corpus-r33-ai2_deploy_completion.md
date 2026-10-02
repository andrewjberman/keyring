# Deploy Completion Record
**Date opened:** 2026-10-02T17:49:39.111427+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T190557Z
**Deploy:** AMGT_CORPUS round 33 CRPS-ai-2: scoped remeasure of the 11 DECIMAL-by-magnitude names + one re-derive each + their dossiers (pair COO e748581d10 / CTO 45a11d1ea8)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| a | activation | build_unit_map --securities <the 11> --remeasure on field_map.json | m33 vs HEAD: fields_unit 7, status_moves 12, other_keys 10, unit_evidence 323, raw_stamp 123, value_sampled 27, other_securities 0 | build_unit_map --securities <the 11> --remeasure at a48c546a1c, rc 0, 11 x 66 field entries; m33 vs HEAD: fields_unit 7 (13 labels: 9 -> PERCENT, 6 -> UNRESOLVED-ON-), status_moves 12, other_keys 10, unit_evidence 323, raw_stamp 123, value_sampled 27, other_securities 0 -- equal to the signed table. The 3 producer-path files that landed after the gate (RESAPP am-1 59c2ef1b23: lib/research/api/scoped_amgt.py + 2 tests) are outside the act's import closure (re-read at leg a) (evidence/r33_ai2_leg_a.txt) | CLOSED 20261002T175759Z |
| b | git | field_map.json commit on CLOUD | commit hash | field_map.json committed on CLOUD at 31c1e10888 (LOCAL; push is MSTR's on Andrew's word), the sentinel with it | CLOSED 20261002T180013Z |
| c | activation | model_block_pull derive --no-sa-fallback over the 11 names | each block == its captured dry-run block (vintage stripped); 0 value moves; exactly 11 new block objects | capture (c32.py, 11 predecessors) at 31c1e10888 then model_block_pull derive --no-sa-fallback in 4 calls (<= 3 names each), rc 0 x4, stamps 20261002T180207Z..180226Z, 0 ERROR; compare: new_stamps 11, equal_dry_run 11/11 (vintage stripped), value_moves 0, case_value_moves 0; S3: exactly 11 new model_block objects over 11 keys since 18:02:00Z (evidence/r33_ai2_leg_c{,_capture,_verify}.txt) | CLOSED 20261002T180522Z |
| d | activation | dossier write_one over the 11 | at most one new object per name; inputs_equal_now | d25.py write (D25_KEYS = the 11, BP by identity key BP/_LN_Equity) from 18:17:12Z at 2190d15bfd: wrote 11, unchanged 0, errors 0, rc 0; S3 structure since 18:17:12Z: exactly one new object 11/11, 0 other names, changed keys inputs + fields.model_rows + content_sha256 (+ as_of on 9); inputs_equal_now 11/11 (evidence/r33_ai2_leg_d{,_structure,_inputs}.txt) | CLOSED 20261002T190502Z |
| v | verify | served census over 100 keys + negative arms + per-family figures | DECIMAL 77 -> 0; UNRESOLVED 11 -> 19; moved keys = the 11; value_moves 0; BA BEST_DIV_YLD PERCENT; ORA ROIC / BP ROE / JD OPER_MARGIN value+unit printed | v33.py census over the newest served block of 100 keys (37746 figures) at 19:05Z vs the pre-act snapshot: DECIMAL 77 -> 0; UNRESOLVED units 11 -> 19 (+8); moved keys exactly the 11 (-> 20261002T1802Z), value_moves 0. Negative arms: BA BEST_DIV_YLD PERCENT, stamp not moved; outside-the-11 stamps moved 0 of 89; DECIMAL-confirmed arm count 0 (named empty). Per-family served figures (CTO msg 28595): ORA ROIC FY2025 0.2237 PERCENT, BP ROE FY2025 0.0962 PERCENT, JD OPER_MARGIN FY2025 0.2119 PERCENT (evidence/r33_ai2_leg_v_census.txt) | CLOSED 20261002T190557Z |

## Log

- 20261002T174939Z OPENED by 2.0.0_SA_COO~X with 5 leg(s)
- 20261002T175759Z LEG a closed: build_unit_map --securities <the 11> --remeasure at a48c546a1c, rc 0, 11 x 66 field entries; m33 vs HEAD: fields_unit 7 
- 20261002T180013Z LEG b closed: field_map.json committed on CLOUD at 31c1e10888 (LOCAL; push is MSTR's on Andrew's word), the sentinel with it
- 20261002T180522Z LEG c closed: capture (c32.py, 11 predecessors) at 31c1e10888 then model_block_pull derive --no-sa-fallback in 4 calls (<= 3 names eac
- 20261002T190502Z LEG d closed: d25.py write (D25_KEYS = the 11, BP by identity key BP/_LN_Equity) from 18:17:12Z at 2190d15bfd: wrote 11, unchanged 0, 
- 20261002T190557Z LEG v closed: v33.py census over the newest served block of 100 keys (37746 figures) at 19:05Z vs the pre-act snapshot: DECIMAL 77 -> 
- 20261002T190557Z CLOSED -- all 5 legs proven
