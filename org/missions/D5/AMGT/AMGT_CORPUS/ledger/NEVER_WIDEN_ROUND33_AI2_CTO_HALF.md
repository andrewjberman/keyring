# AMGT_CORPUS round 33 -- CRPS-ai-2 never-widen pair, CTO half (scoped remeasure of the 11 DECIMAL-by-magnitude names + one re-derive each)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~17:2xZ.
**COO half:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND33_AI2_SERVED_ACT.md` @e748581d10 (msg 28589).
**Authority:** round-32 analysis @ac45eeeef8, rulings 1-3 (row Z-S81).

## What I read

- **The act:** `build_unit_map --securities <11> --remeasure` at code >= f64efce667 (ai-1: `_row_yield_identity` and the no-ground
  UNRESOLVED branch). Then one `stage_derive` per name, then `write_one` for those 11.
- **The dry run covered every one of 100 keys,** through the producer's own `stage_derive` with a write-capturing client:
  - 11 blocks move: 77 unit labels and 8 signs;
  - 0 value, currency, case or top-level moves;
  - one write per block.
  The 77 split three ways:

  | how decided | figures | names |
  |---|---|---|
  | the series-median rule -> PERCENT | 60 | ORA ROIC median 4.47; RWE series -18.2..4.0; BP ROE / ROA / ROTA 3.78 / 1.33 / 1.48; JD OPER_MARGIN 1.06 |
  | ai-1's row identity -> PERCENT | 9 | PWR EQY_DVD_YLD_IND, 5 of 6 computable rows in the percent band |
  | no ground -> UNRESOLVED | 8 | HEI and MELI EQY_DVD_YLD_IND; AZN, RKT, TTE and ULVR SI_PERCENT_EQUITY_FLOAT |

  The 8 signs go UNRESOLVED with their units, under the standing M-DISAGREE-1(a) split.
- **Every one of the 77 is decided by a ground or marked UNRESOLVED.** None is decided by magnitude, which is exactly ruling 1.
- **The map diff, key by key:** 12 status moves (the 6 no-ground entries, unit and sign); 0 entries of any other security.
- **Writers:** the map is written by one rule (`build_entries` / `_row_yield_identity`) and the blocks by one (`stage_derive`). Both
  are read against f64efce667.
- **The negative arm is EMPTY and named so.** No figure's ground confirms DECIMAL among the 11, and the half prints its count of 0
  rather than claiming it passed. That is accepted.

## Served reach, accepted

- **`/thesis`:** 77 unit texts and 8 sign texts change; every value is byte-unchanged.
- **The 8 UNRESOLVED figures** move into the check face's not-measured bucket. That is the honest state Z-S81 asked for: a small
  value with no ground is no longer claimed MEASURED.
- **The Model tab** prints by row type and reads no unit field.

## Blast radius and rollback

- **Touches:** `field_map.json`, the 11 names' entries only, in one commit; 11 new block stamps (BP at its slash-safe key); at most
  11 dossier objects. There is no overwrite and no delete.
- **Rollback:** revert the map commit and ai-1, then re-derive the 11 names forward (newest wins). The prior stamps stay.

## Conditions

1. The gate re-runs the per-key map diff and the block capture immediately before (a) and (c). A moved count is re-signed, never
   absorbed.
2. **Leg v reads the SERVED state and a plausibility sample:**
   - the census over 100 keys: DECIMAL-by-magnitude 77 -> 0; UNRESOLVED +8; moved keys exactly 11; value moves 0;
   - BA's BEST_DIV_YLD stays PERCENT, and one name outside the 11 keeps its stamp;
   - the DECIMAL-confirmed arm is printed with its count of 0;
   - **plus ONE served figure per series-median family, with value and unit printed** (ORA ROIC, BP ROE, JD OPER_MARGIN), so a
     reader can see the percent reading is sane (e.g. 4.47 -> "4.47%"). Labels alone are not the grade.
3. The stop limbs stand as written. Leg v's commit records on Z-S81 that its population is decided: 69 PERCENT and 8 UNRESOLVED.

**CTO HALF: SIGNED** for gate, (a), (b), (c) (11 blocks) and (d) (at most 11 dossiers) at f64efce667, including the 8 sign moves
by name.
