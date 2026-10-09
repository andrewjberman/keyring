# MDPF_SECCLASS decomposition -- ROUND 17 (2.0.0_SA_COO~M1, dell1, 2026-10-09 ~09:5xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers two cells; it is cut after e67's leg G reads clean at the
10:30Z COT run (CTO ruling R1).

**Cut on:** the CTO round-16 analysis, section 3, the enrichment list
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_16_20261009.md`, 1.0.0_SA_CTO~DELL1 msg 2187).
It has three items:
- Item 1 is `SC-e-84`.
- Item 2 is `SC-e-85`.
- Item 3 (D1-S20) is not a cell. It is the four-postulate record the CTO asked this seat to draft (msg 2168), delivered @bfabe0002d
  (`RULE24_RECORD_PROOF_KIND_TABLE_ROWS_D1_S20_20261009.md`) for the laptop CTO's ruling.

**State the round starts from (measured this session, 2026-10-09):**
1. **COT `NAME::` placeable share** (row D1-W66-S2, SC-e-82): 1,060 positions, $17,769,409.83, which is 3.2131 pct of $553,031,383.86
   (`COT_NAME_SHARE_20261009.json`, partition 2026-10-07).
2. **COT's rule.** `data/cot/scripts/gold/lib/etf_classifier.py` `classify_position(ticker, cusip=None, cash_equivalent=None)` (:137-158)
   runs cash flag, then ticker row, then `CUSIP:` row, else `('unclassified', 'none')`. It takes no name.
   - **Callers (N = 2 producers, 4 call sites):** `C_06.client_mix_timeseries.py` :185, :205, :229 and `D_03.composition_artifacts.py`
     :131 (`comp-find`, 13 hits across 121 files under `data/cot/scripts`).
   - **Docstring.** It says the class comes "never from a name" (CTO rulings batch 93 and 99). CTO ruling R1 adds a table `NAME::` hop
     and changes no rule that reads a class from a name, so the docstring line is updated with R1 cited.
3. **`R17_CHECKS/sc_r17_cot_port_check.py`.**
   - At the base: `COT-PORT ok=False ... reason=classify_position-rejects-asset_name` (rc=1, 1.8 s).
   - Positive control, a scratch port that calls BD's `normalize_name`: `COT-PORT ok=True positions=21024 placed=1060
     placed_mv=17769409.83 floor=1060 overridden=0 wrong_rule=0` in 7.5 s. That equals SC-e-82's record exactly.
4. **The p1 residue: 11 keys** (`ETHA` plus 10 `NAME::` keys).
   - They are named in the closed ledger `20260926T0321Z_bd-securities-cot-new-p1-m-20260926_deploy_completion.md` leg R1.
   - None was ever in FWD-15's plan. The census's `pattern_of` reads `other` for both forms.
   - `R17_CHECKS/sc_r17_p1_residue_check.py` at the base: record absent.

## Rule 24 record

- **Domain:** the two cell items of the enrichment list, each placed once. Item 3 is placed above as not a cell.
- **(ii) Same grain:** one write set per cell, disjoint.
- **(iii) Intent coherence:** SC-e-84 ports one hop; SC-e-85 lists 11 keys.
- **(iv) State coherence:**
  - **SC-e-84** never moves a position placed by cash flag, ticker row or `CUSIP:` row (check arm 1). A name with no `NAME::` row stays
    `('unclassified', 'none')` (arm 4). The deploy is the issuer's act under the pair.
  - **SC-e-85** writes no table and no bucket.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-84` | COT `classify_position` gains `asset_name=None`. When cash, ticker and `CUSIP:` all miss, it reads `'NAME::' + normalize_name(asset_name)` (BD's key form) and returns `(class, 'table name')`. C_06 and D_03 pass the position's name at every call site that has it. Pin by test; write the half request. The deploy is the issuer's act. | FWD-16 | WORLD (shipped COT gold lib + 2 producers) | e67 leg G clean (10:30Z COT run) |
| `SC-e-85` | Read-only listing of the p1 residue's 11 keys, joined to FWD-15's UNPLACED-KEY census: pattern, live table presence, held positions and dollars per firm | FWD-15 | LOCAL (read-only) | none |

## Write sets

- **SC-e-84:**
  - `data/cot/scripts/gold/lib/etf_classifier.py`
  - `data/cot/scripts/gold/C_06.client_mix_timeseries.py`
  - `data/cot/scripts/gold/D_03.composition_artifacts.py`
  - `data/cot/scripts/gold/tests/test_cot_position_rule.py`
  - `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_NAME_PORT_20261009.md`
- **SC-e-85:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/P1_RESIDUE_UNPLACED_20261009.json`
- Every cell may also append to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.

## Chains

There are no edges, so M = 2 single-cell chains. Fan-out 2 of 2, cap 8. Slots ~74 (SC-e-84, worker: 4 files across a lib and two
producers) and ~75 (SC-e-85, worker-light).

## Issuer acts after the drain

- **The SC-e-84 deploy**, by a CloudOps lane under its pair. It names exactly the three shipped files (the lib, C_06, D_03). The CTO's
  e79 condition "one named file" reads here as "the named files only, listed", because the producers must pass the name. Any member
  beyond the three is a STOP.
