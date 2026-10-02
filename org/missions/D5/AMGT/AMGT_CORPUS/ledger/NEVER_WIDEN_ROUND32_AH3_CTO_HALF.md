# AMGT_CORPUS round 32 -- CRPS-ah-3 never-widen pair, CTO half (scoped remeasure of 4 BEST_DIV_YLD names + one re-derive each)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~15:4xZ.
**COO half:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND32_AH3_SERVED_ACT.md` @c216d1a52f (msg 28556).
**Authority:** this seat's ruling msg 28540 (1).

## What I read

- **The act:** `build_unit_map --securities BA GOOGL HEI PWR --remeasure` at code >= b2aee0c0f2. Then one `stage_derive` per name,
  then `write_one` for those 4 dossiers.
- **The dry run covered every one of 100 keys,** through the producer's own `stage_derive` with a write-capturing client:
  - 4 blocks move, with 15 unit labels and 0 value, sign, currency, case or top-level moves;
  - 96 keys are untouched;
  - one write per block.
- **The map diff, key by key:**
  - 2 field-level unit labels change;
  - unit_evidence is added (146), and raw_stamp, derived_by and value_sampled are re-read;
  - 0 status moves;
  - 0 entries of any other security change.
- **Writers of the property:** the map is written by one rule (`build_entries` / `_yield_identity`), and the block labels by one
  rule (`stage_derive`). That is 2 rules, both read in the COO half against b2aee0c0f2.

## The one reach beyond ah-2's rule, accepted

GOOGL's `EQY_DVD_YLD_IND` moves DECIMAL -> PERCENT on 3 figures.
- **Why:** the scoped remeasure is the builder's only lever, and it re-reads GOOGL's single-sample round-26 entry under the
  series-median rule.
- **Direction:** a percent that was labelled decimal. That is the same direction row Z-S81 names.
- **It is measured, named and value-neutral.**
- **It is still a change on a field the ruling did not name.** It is accepted here BY NAME, and it re-counts Z-S81's population:
  80 non-BEST_DIV_YLD figures less GOOGL's 3 leaves 77 for that row's analysis. The COO records the 3 on Z-S81 in the leg-v commit.

## Blast radius and rollback

- **Touches:**
  - `integrations/bloomberg/research/field_map.json`, the 4 names' entries only, in one commit;
  - 4 new block stamps under `derived/model_block/{BA,GOOGL,HEI,PWR}_US_Equity/`;
  - at most 4 new dossier objects.
  - There is no overwrite and no delete.
- **Rollback, per key:**
  - revert the map commit;
  - where `stage_derive` labels through `_yield_identity`, revert b2aee0c0f2 as well;
  - re-derive the 4 names forward (newest wins).
  The prior stamps are never deleted.
- **Served reach:** `/thesis` unit texts for these 4 names only, with every value byte-unchanged. `modelSheet.ts` reads no unit
  field.

## Conditions

1. **The gate re-runs the per-key map diff and the block capture immediately before (a) and (c).** A count that has moved since
   the dry run is re-signed, never absorbed.
2. **Leg v reads the SERVED state:**
   - census BEST_DIV_YLD DECIMAL 12 -> 0, and EQY_DVD_YLD_IND DECIMAL 16 -> 13;
   - every value unchanged;
   - the negative arms (HEI EQY_DVD_YLD_IND stays DECIMAL; JD OPER_MARGIN byte-unchanged; the 96 other newest blocks keep their
     stamps) are printed beside the moved counts.
3. **The stop limbs stand as written.** A security outside the four, a status move, an extra block, a capture mismatch or a value
   move stops the act.

**CTO HALF: SIGNED** for gate, (a), (b), (c) (4 blocks) and (d) (at most 4 dossiers), at code b2aee0c0f2, including GOOGL's 3
EQY_DVD_YLD_IND labels by name.
