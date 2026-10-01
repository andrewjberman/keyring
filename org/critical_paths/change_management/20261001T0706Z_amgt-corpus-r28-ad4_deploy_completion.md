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
| c | activation | model_block_pull derive --no-sa-fallback over the 18 (ad4_keys.txt) | each block == its captured dry-run block (vintage stripped); 0 value/unit/case; exactly 18 new block objects | capture (c28.py, 18 predecessors) then model_block_pull derive --no-sa-fallback over the 18 in 6 calls at 53428939ca (0 producer diff since the dry run d45014a87e), rc 0 x6, 18 stamps 20261001T070946Z..071020Z, 0 ERROR; compare: new_stamps 18, equal_dry_run 18/18 (vintage stripped), value_moves 0, case_value_moves 0; S3: exactly 18 new model_block objects over 18 keys since 07:09Z (evidence/r28_ad4_leg_c{,_capture,_verify}.txt) | CLOSED 20261001T071225Z |
| d | activation | dossier write_one over the 18 | one new object per written name; inputs_equal_now | d25.py write over the 18: the first call was killed by the issuer's own timeout 900 after 7 (about 2 min per dossier; no producer ERROR), the resume over the 11 unwritten wrote 11, 0 errors, rc 0; S3 structure since 07:14:22Z: exactly one new object 18/18, 0 other names, changed keys fields.model_rows + inputs + content_sha256 (+ as_of on 16); inputs_equal_now 18/18 (evidence/r28_ad4_leg_d{,_structure,_inputs,_structure_partial,_inputs_partial}.txt) | CLOSED 20261001T080854Z |
| v | verify | check-face census over 100 keys + negative arms | refuse 364 -> 10, zero-sample 0; BBSE3 CAPITAL_EXPEND still refused; TSM stamp 20260930T165643Z unchanged |  | OPEN |

## Log

- 20261001T070645Z OPENED by 2.0.0_SA_COO~X with 3 leg(s)
- 20261001T071225Z LEG c closed: capture (c28.py, 18 predecessors) then model_block_pull derive --no-sa-fallback over the 18 in 6 calls at 53428939ca (0 
- 20261001T080854Z LEG d closed: d25.py write over the 18: the first call was killed by the issuer's own timeout 900 after 7 (about 2 min per dossier; no
