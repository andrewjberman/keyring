# AMGT_HARVST round 43 -- HVST-ap-1 never-widen pair, CTO half (explicit zero rows in `chatter_window`, FWD-17)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-04 ~01:1xZ. **COO half:** `deliverables/2.0.0_SA_COO_H/round43/NEVER_WIDEN_HALF_COO_GOLD_WINDOW_ZERO.md`
@b964ccd5f0 (msg 29101). **Authority:** round-42 analysis ruling 1 (@bad41f3f91, Z-C-S74), under Andrew's card 2 (@9fe6e6f111).

## What I read

- **The builder change @5789ad3487:** `build_window_rows` seeds `by_security` from `security_keys`, so a named key with no
  mention rows still gets its three rows. `build_window` and the dry-run CLI pass the universe keys (`wanted`). Nothing else moved.
- **The rule's measurement, `round43/gold_window_zero_signing.out`, read by this seat:** 1 part before (the 618-row
  `date=2026-10-04/part-20261004T001638Z`), built 636 = 212 x 3; gone 0, changed 0, added 18 on the 6 named zero-mention securities;
  added-not-explicit-zero 0; mismatch 0; tone null exactly when voters is 0; 0 puts.
- **Key form:** if `wanted` spelled keys differently from the mention rows, the build would add a whole duplicate set (about 1,254
  rows, not 636). The measured 636 with 18 added rules that out.
- **The plant:** passes, and fails with the fix removed (`round43/ap-1.plant.out`); lib/research/harvest 336 passed.
- **Writers:** 1 (`window_tone.build_window` via `write_gold`, never-overwrite); no scheduled producer.
- **Served effect today:** none. No route reads the table yet. RESAPP's FWD-36 tone limb (routed to `2.0.0_SA_COO~Z`) will be the
  first reader, under its own pair. When it lands, these 6 names read served zeros instead of an absence, which is what FWD-17 wants.

## Conditions

1. The act re-checks the rule before and after the write, and the written digest equals the dry run's. If the rule fails on the
   written part, ROLLBACK as the COO half states: the 618 rows go back as a newer part, and nothing is deleted.
2. One act, once.

**CTO HALF: SIGNED** for HVST-ap-1.
