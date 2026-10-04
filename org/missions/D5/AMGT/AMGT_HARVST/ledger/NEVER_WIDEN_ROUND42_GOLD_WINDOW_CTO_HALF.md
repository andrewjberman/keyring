# AMGT_HARVST round 42 -- HVST-ao-1 never-widen pair, CTO half (the first served `chatter_window` part, FWD-17)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-04 ~00:1xZ. **COO half:** `deliverables/2.0.0_SA_COO_H/round42/NEVER_WIDEN_HALF_COO_GOLD_WINDOW.md`
@f0eb10b97d (msg 29076). **Authority:** round-41 analysis ruling 2 (@98f36bf49a), under Andrew's card 2 (@9fe6e6f111).

## What I read

- **The rule:** a first mint (0 parts before); 3 rows per universe security; `window_end` = the last trading day; every row equal to
  an independent recompute from FWD-17's words (articles_total, scored, voters = non-neutral labels with no threshold, tone over voters
  only); tone null exactly when voters is 0. The act re-checks it before and after the write, and the written digest must equal the
  dry run's.
- **`round42/gold_window_signing.json`, read by this seat:** 618 rows on 206 securities; window_end 2026-10-02; 496 with tone;
  mismatch 0; window_end wrong 0; tone-null-not-iff-0-voters 0; shape bad 0; 40 real all-neutral windows; 0 puts.
- **The plant:** `test_i_all_neutral_name_is_voters_zero_tone_none_in_every_window` passes (`round42/ao-1.plant.out`).
- **Writers:** 1 (`window_tone.build_window` via `write_gold`, never-overwrite); no scheduled producer.
- **Served effect today:** none. No route reads the table until RESAPP's own cell, under its own pair.

## Conditions

1. The act's gate holds on the WRITTEN part, and its digest equals the dry run's. If it fails, ROLLBACK as the half states (an empty
   newer part; nothing deleted).
2. One act, once.

**CTO HALF: SIGNED** for HVST-ao-1.
