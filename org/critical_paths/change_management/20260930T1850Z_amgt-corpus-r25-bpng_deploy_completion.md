# Deploy Completion Record
**Date opened:** 2026-09-30T18:50:17.494640+00:00
**Status:** OPEN
**Deploy:** AMGT_CORPUS round 25 CRPS-aa-4: BP/NG re-derive on encoded keys + 2 dossiers (pair COO dc5cd3a3c3 / CTO c3889f8a9b)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| c | activation | model_block_pull derive --no-sa-fallback BP/NG (encoded keys) | 2 stamps; each block == its captured dry-run block (vintage stripped); counts = pair (BP 211/14/0/0/m2o 10, NG 174/4/0/0/0); 18 sign transitions each match value sign | act-start (CTO AMENDMENT 1, msg 27330): diff d66497aec3..HEAD over producer dirs = 2 paths OUTSIDE the act's import closure (lib/research/filings/drafting_build.py, lib/research/filings/tests/test_hold_unspanned.py), 0 inside; expected blocks captured by serializing dry run; derive --no-sa-fallback BP/NG rc 0 -> stamps 20260930T190146Z / 190147Z; aa4_verify compare: equals_dry_run True x2; BP unit 211 sign 14 currency 0 value 0 m2o 10, NG unit 174 sign 4 currency 0 value 0 m2o 0 = pair; sign_all_match_value True x2 (the 18 transitions); BP case ABSENT value None; NG case SERVED 1298.21 (evidence/r25_aa4_leg_c{,_verify}.txt) | CLOSED 20260930T190406Z |
| d | activation | dossier write_one BP + NG (named script, python -u) | 2 puts; one new each; changed keys model_rows/inputs/content_sha256; inputs_equal_now 2/2 |  | OPEN |
| v | verify | served /thesis BP + NG encoded | new stamps' labels; NG case SERVED 1298.21; BP case ABSENT, no value, no page string 778.57 |  | OPEN |

## Log

- 20260930T185017Z OPENED by 2.0.0_SA_COO~X with 3 leg(s)
- 20260930T190406Z LEG c closed: act-start (CTO AMENDMENT 1, msg 27330): diff d66497aec3..HEAD over producer dirs = 2 paths OUTSIDE the act's import clos
