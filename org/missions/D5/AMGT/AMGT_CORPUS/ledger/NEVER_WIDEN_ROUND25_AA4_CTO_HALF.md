# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 25, `CRPS-aa-4` (the BP/_LN and NG/_LN re-derive on encoded keys, plus 2 dossiers) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~17:3xZ

**Against:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND25_BPNG_PASS_SERVED_ACT.md` @`dc5cd3a3c3` (msg 27294, READ-acked; read to
EOF, 6,719 B).
**Ruling it serves:** round-24 analysis ruling 4.

## VERDICT: SIGNED, with items 1-3 ACCEPTED and one item the COO half left unexplained, now explained

## 1. RE-MEASURED BY THIS SEAT (own instrument, not the issuer's)

**The script:** `ctoz_aa4_signs.py`, in this seat's scratchpad.
- It runs the producer's `stage_derive` with a write-capturing client, so it writes nothing.
- It pages the stamp listing client-side.
- It prints each sign transition with its figure's value, each PERCENT -> UNRESOLVED transition, and both `cases.base` in full.
- It ran at HEAD `9ba4e7da1c`. `git diff --name-only d66497aec3 HEAD -- integrations/bloomberg/research lib/research` is **empty**, so
  the code at signing is the code the COO half signed.

**Results:**
- **Writes:** 1 per name, at the encoded keys only (`BP-SLASH-_LN_Equity`, `NG-SLASH-_LN_Equity`). The predecessors are the newest of 6
  stamps each (`200039Z`, `200133Z`), which equals the half.
- **The sign changes (BP 14, NG 4), not explained in the COO half: all 18 are CORRECTIONS.** Every new label matches the sign of the
  unchanged value, and every old label did not:
  - BP: POSITIVE -> NEGATIVE on 14 negative values. Examples: IS_OPER_INC FY2020 -22,000; IS_EPS FY2020 -1.0042; RETURN_COM_EQY FY2022
    -3.4793.
  - NG: NEGATIVE -> POSITIVE on 4 positive CF_FREE_CASH_FLOW values (FY2016 2,973; FY2017 1,244; FY2018 11; FY2022 327).
  - The 09-25 predecessors predate the current `_resolved_sign` (the predecessor-code drift this seat missed at y-4, AMENDMENT 1).
  - The act FIXES 18 served wrong labels. It is named here so the verify reads them as expected.
- **Item 1 (BP `PROF_MARGIN`, 10 figures to UNRESOLVED):** the values FY2016-2025 are 0.0628, 1.4109, 3.1407, 1.4461, -19.1658, 4.7959,
  -1.0303, 7.2522, 0.2014 and 0.029.
  - That is a PERCENT series. FY2024's 0.2014 is a 0.2% margin, consistent with a thin year.
  - The classifier's DECIMAL reading of FY2025's 0.029 is a small-sample misread.
  - **ACCEPT:** UNRESOLVED serves no wrong fact. The classifier defect goes to the round-25 analysis.
- **Item 2 (BP `cases.base.inputs.trailing_median_pe` 24.65 -> 778.5714):** the status stays ABSENT (`currency_mismatch`) and no value is
  served.
  - The new input is GBp `PX_LAST` over USD `IS_COMP_EPS_ADJUSTED`, a currency-mixed number.
  - `git -C portal grep` for `trailing_median_pe` in `src/` finds **0 non-fixture readers**. The page renders `team_cases`, not these
    inputs (`ModelTab.tsx:377`).
  - **ACCEPT, with the issuer's row:** `case_rule` refuses the INPUT as well as the value when currencies are mixed.
- **Item 3 (NG `cases.base` ABSENT -> SERVED 1,298.21 GBp):**
  - BEST_EPS FY1 2027 0.897 × trailing-median P/E 14.472797 (n 10, FY2017-2026) × `unit_factor` 100 = **1,298.21**. Recomputed here to
    the cent.
  - The quote (GBp) and reporting (GBP) currency are the same. The ratio to `PX_LAST` 1,135.5 is 1.14, inside [0.33, 3.0].
  - **ACCEPT.** It is `case_rule` as served for every same-currency name since round 23.

## 2. CONDITIONS

1. **Act-start:** ledger `amgt-corpus-r25-labels-units` is CLOSED (ruling 1: one producer pass at a time), and the diff from
   `d66497aec3` over the producer dirs is empty. Otherwise STOP.
2. **Verify leg 1 adds the sign transitions:** they equal the 18 above, each new label matching its value's sign. Any sign change
   outside these 18: STOP.
3. **The served read (leg v item 3) adds one negative arm:**
   - BP's `/thesis` case stays ABSENT with no value;
   - no served page string carries 778.57.

## 3. ROLLBACK

The COO half stands: the prior stamps stay, and the rollback is a forward re-derive. A delete is Andrew's act.

## 4. NOT COVERED

- BP/NG header currency labels. The unmeasured `Z-S69` class on BP goes to the round-25 analysis.
- Every other block.
- The scoped API.
