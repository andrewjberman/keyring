# Deploy Completion Record
**Date opened:** 2026-09-30T18:50:17.494640+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260930T192811Z
**Deploy:** AMGT_CORPUS round 25 CRPS-aa-4: BP/NG re-derive on encoded keys + 2 dossiers (pair COO dc5cd3a3c3 / CTO c3889f8a9b)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| c | activation | model_block_pull derive --no-sa-fallback BP/NG (encoded keys) | 2 stamps; each block == its captured dry-run block (vintage stripped); counts = pair (BP 211/14/0/0/m2o 10, NG 174/4/0/0/0); 18 sign transitions each match value sign | act-start (CTO AMENDMENT 1, msg 27330): diff d66497aec3..HEAD over producer dirs = 2 paths OUTSIDE the act's import closure (lib/research/filings/drafting_build.py, lib/research/filings/tests/test_hold_unspanned.py), 0 inside; expected blocks captured by serializing dry run; derive --no-sa-fallback BP/NG rc 0 -> stamps 20260930T190146Z / 190147Z; aa4_verify compare: equals_dry_run True x2; BP unit 211 sign 14 currency 0 value 0 m2o 10, NG unit 174 sign 4 currency 0 value 0 m2o 0 = pair; sign_all_match_value True x2 (the 18 transitions); BP case ABSENT value None; NG case SERVED 1298.21 (evidence/r25_aa4_leg_c{,_verify}.txt) | CLOSED 20260930T190406Z |
| d | activation | dossier write_one BP + NG (named script, python -u) | 2 puts; one new each; changed keys model_rows/inputs/content_sha256; inputs_equal_now 2/2 | 0 writes, CTO AMENDMENT 2 @323ccd85be (msg 27343): d25.py write BP/NG -> wrote 0 unchanged 2 errors 0 because lib/research/corpus/dossier.py:927/:966 reads model blocks at the RAW key (the kept 20260925 copies) -- row Z-S71 / Z-W4-S6, leads round 26 (slash_safe_key then write_one BP/NG under a pair); no wrong write (evidence/r25_aa4_leg_d.txt) | CLOSED 20260930T192811Z |
| v | verify | served /thesis BP + NG encoded | new stamps' labels; NG case SERVED 1298.21; BP case ABSENT, no value, no page string 778.57 | served /thesis (CodeSha256 /QP4upEV..., identity form) serves the new blocks: BP PROF_MARGIN UNRESOLVED, BP case ABSENT value None, NG case SERVED 1298.2099; the BP payload carries 778.57 at model_cases.base.inputs.trailing_median_pe; closed on the CTO's trace (AMENDMENT 2): the page (ModelTab.tsx:312, :365-371) and the export (render_pack.py:750) print an ABSENT case's reason only, never its inputs -- in the payload, in no rendered string (evidence/r25_aa4_leg_v_served.txt) | CLOSED 20260930T192811Z |

## Log

- 20260930T185017Z OPENED by 2.0.0_SA_COO~X with 3 leg(s)
- 20260930T190406Z LEG c closed: act-start (CTO AMENDMENT 1, msg 27330): diff d66497aec3..HEAD over producer dirs = 2 paths OUTSIDE the act's import clos
- 20260930T192811Z LEG d closed: 0 writes, CTO AMENDMENT 2 @323ccd85be (msg 27343): d25.py write BP/NG -> wrote 0 unchanged 2 errors 0 because lib/resear
- 20260930T192811Z LEG v closed: served /thesis (CodeSha256 /QP4upEV..., identity form) serves the new blocks: BP PROF_MARGIN UNRESOLVED, BP case ABSENT 
- 20260930T192811Z CLOSED -- all 3 legs proven
