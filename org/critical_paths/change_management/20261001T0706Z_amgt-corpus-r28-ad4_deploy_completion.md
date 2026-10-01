# Deploy Completion Record
**Date opened:** 2026-10-01T07:06:45.255289+00:00
**Status:** OPEN
**Deploy:** AMGT_CORPUS round 28 CRPS-ad-4: re-derive of the 18 blocks the zero-sample sign fix moves + their dossiers (pair COO 971d8e5306 / CTO 8ae0146782)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| c | activation | model_block_pull derive --no-sa-fallback over the 18 (ad4_keys.txt) | each block == its captured dry-run block (vintage stripped); 0 value/unit/case; exactly 18 new block objects |  | OPEN |
| d | activation | dossier write_one over the 18 | one new object per written name; inputs_equal_now |  | OPEN |
| v | verify | check-face census over 100 keys + negative arms | refuse 364 -> 10, zero-sample 0; BBSE3 CAPITAL_EXPEND still refused; TSM stamp 20260930T165643Z unchanged |  | OPEN |

## Log

- 20261001T070645Z OPENED by 2.0.0_SA_COO~X with 3 leg(s)
