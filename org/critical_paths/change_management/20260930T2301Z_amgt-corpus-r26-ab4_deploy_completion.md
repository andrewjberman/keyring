# Deploy Completion Record
**Date opened:** 2026-09-30T23:01:17.852514+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T004126Z
**Deploy:** AMGT_CORPUS round 26 CRPS-ab-4: map rebuild (ab-2) + 18-block re-derive (ab-2/ab-3/ab-5) + dossiers via fixed reader (ab-1) (pair COO ad19f49aa7 / CTO d15eea8cb6)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| a | activation | PYTHONPATH=<root> build_unit_map.py --population crosswalk | the 9 named entries, 0 other, 0 top-level | PYTHONPATH=<root> build_unit_map.py --population crosswalk rc 0 at 9661eab7ad; diff vs pre-image: entries_changed 9 = the named 9 (BP PE_RATIO/PROF_MARGIN, BBSE3 CAPITAL_EXPEND, BA/MELI/QXO EQY_DPS + IS_DIV_PER_SHR), top_level 0, added 0, lf_only True; the rebuilt map is BYTE-IDENTICAL to the m4 dry run's temp map (sha256 equal) | CLOSED 20260930T230907Z |
| b | git | field_map.json commit | commit hash | field_map.json committed 29d87a966a (working copy == HEAD after commit); re-recorded: the leg-b/leg-c closes of 23:0x-23:1xZ were lost from the sentinel's working copy, which a later read showed reverted to its committed state | CLOSED 20261001T004125Z |
| c | activation | model_block_pull derive --no-sa-fallback over the 18 (<=3 per call) | each block == its captured dry-run block (vintage stripped); 0 value; 0 case value | capture (c26.py, 1 write each) then derive --no-sa-fallback over the 18 in 6 calls, rc 0 x6, 18 stamps, 0 ERROR; compare: new_stamps 18, equal_dry_run 18/18 (vintage stripped), value_moves 0, case_value_moves 0 (evidence/r26_leg_c{,_capture,_verify}.txt); re-recorded after the sentinel's working copy reverted | CLOSED 20261001T004125Z |
| d | activation | dossier write_one over the moved names with a dossier + NG (named script, python -u) | one new object per written name; model_rows/inputs/content_sha256 only; inputs_equal_now | d25.py write over the 18 moved names + NG through the fixed reader (ab-1): 19 wrote, 0 errors; S3 structure: exactly one new object 19/19, 0 other names, changed keys fields.model_rows + inputs + content_sha256 (+ as_of on 8: the build date crossed midnight UTC); inputs_equal_now 19/19; BP dossier names BP-SLASH- block 20260930T231718Z, NG names NG-SLASH- 190147Z (evidence/r26_leg_d{,_structure,_inputs}.txt) | CLOSED 20261001T004044Z |
| v | verify | census + served /thesis BP (PE_RATIO RATIO, PROF_MARGIN PERCENT, CUR_MKT_CAP no currency, value byte-unchanged) + BA negative arm | as stated | census (ab2_check over 100 keys): 11 UNRESOLVED, bands unchanged; served /thesis 23:52Z (CodeSha256 /QP4upEV..., identity form) BP/_LN_Equity: PE_RATIO RATIO, PROF_MARGIN PERCENT, CUR_MKT_CAP currency None with value 89798586794.73 byte-equal to the predecessor (CTO condition); negative arm BA_US_Equity CUR_MKT_CAP USD; the case fix rides RESAPP's redeploy (told 23:20Z) (evidence/r26_leg_v_{census,served}.txt) | CLOSED 20261001T004044Z |

## Log

- 20260930T230117Z OPENED by 2.0.0_SA_COO~X with 5 leg(s)
- 20260930T230907Z LEG a closed: PYTHONPATH=<root> build_unit_map.py --population crosswalk rc 0 at 9661eab7ad; diff vs pre-image: entries_changed 9 = th
- 20261001T004044Z LEG d closed: d25.py write over the 18 moved names + NG through the fixed reader (ab-1): 19 wrote, 0 errors; S3 structure: exactly one
- 20261001T004044Z LEG v closed: census (ab2_check over 100 keys): 11 UNRESOLVED, bands unchanged; served /thesis 23:52Z (CodeSha256 /QP4upEV..., identit
- 20261001T004125Z LEG b closed: field_map.json committed 29d87a966a (working copy == HEAD after commit); re-recorded: the leg-b/leg-c closes of 23:0x-23
- 20261001T004125Z LEG c closed: capture (c26.py, 1 write each) then derive --no-sa-fallback over the 18 in 6 calls, rc 0 x6, 18 stamps, 0 ERROR; compare
- 20261001T004126Z CLOSED -- all 5 legs proven
