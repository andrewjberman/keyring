# Deploy Completion Record
**Date opened:** 2026-10-01T05:06:06.228666+00:00
**Status:** OPEN
**Deploy:** AMGT_CORPUS round 27 CRPS-ac-2: map rebuild carrying ac-1 (ZERO-DOMINATED) + BBSE3 re-derive + BBSE3 dossier (pair COO e4b31a6f28 / CTO 3e49e4a8dc)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| a | activation | PYTHONPATH=<root> build_unit_map.py --population crosswalk | 1 entry (BBSE3 CAPITAL_EXPEND), map byte-identical to the dry run's temp map |  | OPEN |
| b | git | field_map.json commit | commit hash |  | OPEN |
| c | activation | model_block_pull derive --no-sa-fallback BBSE3 only | block == captured dry-run block (vintage stripped); 0 value; 1 block written |  | OPEN |
| d | activation | dossier write_one BBSE3 only | at most one new object; inputs_equal_now |  | OPEN |
| v | verify | census + negative arm | UNRESOLVED 1 / ZERO-DOMINATED 10 over 100 keys; TSM CURR_ENTP_VAL UNRESOLVED; BA EQY_DPS unit byte-unchanged |  | OPEN |

## Log

- 20261001T050606Z OPENED by 2.0.0_SA_COO~X with 5 leg(s)
