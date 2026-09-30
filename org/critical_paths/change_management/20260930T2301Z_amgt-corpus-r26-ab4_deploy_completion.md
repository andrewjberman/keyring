# Deploy Completion Record
**Date opened:** 2026-09-30T23:01:17.852514+00:00
**Status:** OPEN
**Deploy:** AMGT_CORPUS round 26 CRPS-ab-4: map rebuild (ab-2) + 18-block re-derive (ab-2/ab-3/ab-5) + dossiers via fixed reader (ab-1) (pair COO ad19f49aa7 / CTO d15eea8cb6)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| a | activation | PYTHONPATH=<root> build_unit_map.py --population crosswalk | the 9 named entries, 0 other, 0 top-level | PYTHONPATH=<root> build_unit_map.py --population crosswalk rc 0 at 9661eab7ad; diff vs pre-image: entries_changed 9 = the named 9 (BP PE_RATIO/PROF_MARGIN, BBSE3 CAPITAL_EXPEND, BA/MELI/QXO EQY_DPS + IS_DIV_PER_SHR), top_level 0, added 0, lf_only True; the rebuilt map is BYTE-IDENTICAL to the m4 dry run's temp map (sha256 equal) | CLOSED 20260930T230907Z |
| b | git | field_map.json commit | commit hash |  | OPEN |
| c | activation | model_block_pull derive --no-sa-fallback over the 18 (<=3 per call) | each block == its captured dry-run block (vintage stripped); 0 value; 0 case value |  | OPEN |
| d | activation | dossier write_one over the moved names with a dossier + NG (named script, python -u) | one new object per written name; model_rows/inputs/content_sha256 only; inputs_equal_now |  | OPEN |
| v | verify | census + served /thesis BP (PE_RATIO RATIO, PROF_MARGIN PERCENT, CUR_MKT_CAP no currency, value byte-unchanged) + BA negative arm | as stated |  | OPEN |

## Log

- 20260930T230117Z OPENED by 2.0.0_SA_COO~X with 5 leg(s)
- 20260930T230907Z LEG a closed: PYTHONPATH=<root> build_unit_map.py --population crosswalk rc 0 at 9661eab7ad; diff vs pre-image: entries_changed 9 = th
