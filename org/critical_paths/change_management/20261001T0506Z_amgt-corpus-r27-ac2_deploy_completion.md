# Deploy Completion Record
**Date opened:** 2026-10-01T05:06:06.228666+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T053145Z
**Deploy:** AMGT_CORPUS round 27 CRPS-ac-2: map rebuild carrying ac-1 (ZERO-DOMINATED) + BBSE3 re-derive + BBSE3 dossier (pair COO e4b31a6f28 / CTO 3e49e4a8dc)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| a | activation | PYTHONPATH=<root> build_unit_map.py --population crosswalk | 1 entry (BBSE3 CAPITAL_EXPEND), map byte-identical to the dry run's temp map | PYTHONPATH=<root> build_unit_map.py --population crosswalk rc 0 at 0e41f14441; diff vs pre-image: 1 entry (CAPITAL_EXPEND) and only its BBSE3 texts (per-security unit/sign + the entry's BBSE3 status lines), top_level 0, added 0, removed 0; the rebuilt map is BYTE-IDENTICAL to a temp-map rebuild by the dry run's method (sha256 2b1b5836...279f both) (evidence/r27_ac2_leg_a{,_temp,_diff}.txt) | CLOSED 20261001T051235Z |
| b | git | field_map.json commit | commit hash | field_map.json committed 767b4e8c50 (working copy == HEAD after commit); the first attempt was refused only because a peer's drain merge was in progress in the shared tree (MERGE_HEAD gone at 05:13Z) | CLOSED 20261001T051529Z |
| c | activation | model_block_pull derive --no-sa-fallback BBSE3 only | block == captured dry-run block (vintage stripped); 0 value; 1 block written | capture (c27.py, predecessor 20260930T231715Z) then model_block_pull derive --securities 'BBSE3 BZ Equity' --no-sa-fallback rc 0 at 950ae4bb4f (0 producer diff since 767b4e8c50): stamp 20261001T051828Z, 0 ERROR; compare: new_stamps 1, equal_dry_run 1/1 (vintage stripped), value_moves 0, case_value_moves 0; S3 census: exactly 1 new model_block object since 05:17Z (evidence/r27_ac2_leg_c{,_capture,_verify}.txt) | CLOSED 20261001T052019Z |
| d | activation | dossier write_one BBSE3 only | at most one new object; inputs_equal_now | pre-act inputs equal_now False after (c) (the block moved); d25.py write BBSE3 only: 1 wrote, 0 errors (as_of=2026-10-01.bdbee5d60d0e5216); S3 structure since 05:21:51Z: exactly one new object 1/1, 0 other names, changed keys fields.model_rows + inputs + content_sha256 + as_of (the build date is 10-01; predecessor 09-30); inputs_equal_now 1/1 (evidence/r27_ac2_leg_d{,_pre_inputs,_structure,_inputs}.txt) | CLOSED 20261001T052914Z |
| v | verify | census + negative arm | UNRESOLVED 1 / ZERO-DOMINATED 10 over 100 keys; TSM CURR_ENTP_VAL UNRESOLVED; BA EQY_DPS unit byte-unchanged | v27.py over the newest block of 100 keys (37746 figures): UNRESOLVED units 1 (TSM CURR_ENTP_VAL), ZERO-DOMINATED 10 (BBSE3 CAPITAL_EXPEND, UNRESOLVED -> ZERO-DOMINATED); negative arms (CTO condition): TSM CURR_ENTP_VAL stays UNRESOLVED; BA EQY_DPS newest stamp 20260930T165623Z (not re-derived), unit PER SHARE byte-unchanged (evidence/r27_ac2_leg_v_census.txt) | CLOSED 20261001T053145Z |

## Log

- 20261001T050606Z OPENED by 2.0.0_SA_COO~X with 5 leg(s)
- 20261001T051235Z LEG a closed: PYTHONPATH=<root> build_unit_map.py --population crosswalk rc 0 at 0e41f14441; diff vs pre-image: 1 entry (CAPITAL_EXPEN
- 20261001T051529Z LEG b closed: field_map.json committed 767b4e8c50 (working copy == HEAD after commit); the first attempt was refused only because a pe
- 20261001T052019Z LEG c closed: capture (c27.py, predecessor 20260930T231715Z) then model_block_pull derive --securities 'BBSE3 BZ Equity' --no-sa-fallb
- 20261001T052914Z LEG d closed: pre-act inputs equal_now False after (c) (the block moved); d25.py write BBSE3 only: 1 wrote, 0 errors (as_of=2026-10-01
- 20261001T053145Z LEG v closed: v27.py over the newest block of 100 keys (37746 figures): UNRESOLVED units 1 (TSM CURR_ENTP_VAL), ZERO-DOMINATED 10 (BBS
- 20261001T053145Z CLOSED -- all 5 legs proven
