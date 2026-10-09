# MDPF_SECCLASS decomposition -- ROUND 16 (2.0.0_SA_COO~M1, dell1, 2026-10-09 ~09:1xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers five cells.

**Cut on:** the CTO rounds 13-15 analysis, section 3, the enrichment list
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUNDS_13_15_20261009.md`, 1.0.0_SA_CTO~DELL1 msg 2139).
There are five items, at most three mechanical criteria per build order. Not cells: D1-W65-S2 is the COO's decision, recorded @4e2c845004
(`COO_DECISION_D1_W65_S2_C06_FULL_BUILD_20261009.md`). D1-S9 and D1-W57-S1 read at the 10:30Z COT run.

**State the round starts from (measured this session, 2026-10-09):**
1. **Row D1-W66-S3:** of the 36 group-A trace securities that carry a ticker, 23 have no ticker row today and a live `NAME::` row.
   `R16_CHECKS/sc_r16_ticker_no_row.py` reads `ok=False ticker_no_row=23 resolved=0` (hop `ticker-no-row`).
2. **Row D1-S15:** `R12_CHECKS/ai_leg_verify.py` `read_unresolved` (:71-78) matches `line.startswith("UNRESOLVED ")`, so a prefixed log
   reads 0 reason lines with no error. `R16_CHECKS/test_r16_ai_leg_verify_blind.py`: 3 failed (no `blind_log_refusal`).
3. **Row D1-S18:** under `--dry-run`, `seed-etf-classifications.py` prints "Items written : N". `R16_CHECKS/test_r16_seed_dry_run_words.py`:
   the dry-run arm fails, and the real-run control arm passes.
4. **Row D1-W66-S2:** COT's lib (`data/cot/scripts/gold/lib/etf_classifier.py` `classify_position`) has no name path. The COT share a
   `NAME::` row would place is unmeasured. `R16_CHECKS/sc_r16_cot_name_share_check.py`: record absent.
5. **Row D1-W66-S1:** `CUSIP:025083882` reads equity / US Large Cap; `NAME::AMERICAN CENTURY ULTRA INV` reads fixed_income /
   Ultra Short Duration (updated_by mdpf-secclass-old-list-reclassify). Full scan: 11,361 rows, 2 rows carry the name.

## Rule 24 record

- **Domain:** the five enrichment items, each placed once, one cell each.
- **(ii) Same grain:** one write set per cell, all disjoint.
- **(iii) Intent coherence:** one intent per cell.
- **(iv) State coherence:**
  - SC-e-79 adds a fallback only for the ticker-no-row hop. A ticker with a row, and a chain that places the position, do not move.
  - SC-e-80 adds a refusal and changes no existing verdict for a readable log.
  - SC-e-81 changes words only; no put path changes.
  - SC-e-82 writes no table and no bucket.
  - SC-e-83 builds a one-line set and a half; the table write is the issuer's act under the pair.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-79` | BD `classify_with_identity`: when the position's ticker has NO row, fall back to `NAME::` + `normalize_name(asset_name)` and serve the match source (hop names the name key). Pin by test; write the half request. The lib deploy is the issuer's act. | FWD-16 | WORLD (shipped BD gold lib) | none |
| `SC-e-80` | `ai_leg_verify.py` gains `blind_log_refusal(absent_keys, reasons, logs)` and `main()` adds its problem: keys absent, logs given, and zero reason lines for them is a refusal | FWD-15 | LOCAL (issuer check) | none |
| `SC-e-81` | `seed-etf-classifications.py` dry-run summary says DRY RUN and "would write N"; the real-run summary is unchanged | FWD-14 | WORLD (an infra/ path: the L6 floor; words only) | none |
| `SC-e-82` | Measure, read-only, COT's unclassified share that a canonical `NAME::` row would place; write the record with its denominator and a materiality verdict. A port of e76's lookup to COT follows only if material, as a later cell. | FWD-16 | LOCAL (read-only) | none |
| `SC-e-83` | AMERICAN CENTURY ULTRA INV: one REMAP line setting the `NAME::` row to the `CUSIP:` row's class (equity / US Large Cap), with evidence; the half request. The write is the issuer's act. | FWD-3 | WORLD (table write by the issuer) | none |

## Write sets

- **SC-e-79:** `data/black_diamond/scripts/gold/lib/etf_classifier.py`; `data/black_diamond/scripts/gold/tests/test_etf_classifier_name_key.py`;
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_NAME_TICKER_FALLBACK_20261009.md`
- **SC-e-80:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/ai_leg_verify.py`
- **SC-e-81:** `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py`
- **SC-e-82:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_CHECKS/cot_name_share.py`;
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/COT_NAME_SHARE_20261009.json`
- **SC-e-83:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_ULTRA_ROW_SET_20261009.tsv`;
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_ULTRA_NAME_ROW_20261009.md`
- Every cell may also append to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.

## Chains

There are no edges, so M = 5 single-cell chains. Fan-out 5 of 5, cap 8. Slots ~69 (SC-e-79, worker), ~70 to ~73 (SC-e-80 to SC-e-83,
worker-light: each under 100 product lines).

## Issuer acts after the drain

- The SC-e-79 lib deploy, by a CloudOps lane under its pair. It names only `lib/etf_classifier.py` (the named-file rule).
- The SC-e-83 one-line write through `R15_CHECKS/s11_rows_write.py --set R16_ULTRA_ROW_SET_20261009.tsv --write`, under its pair.
