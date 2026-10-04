# L4-R ratified-text half -- AMGT_HARVST v0.17 -- SIGN

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~23:3xZ
**Delivery:** `1.0.0_SA_CTO~Z` msgs 28798 and 28800 at `3da5563fd8`. The half hash, recomputed by this seat, is `758063b753ce` and
equals the delivery.
**Method:** the ratified-text sections at `ce138d2314` (v0.16, signed @`e0f4b16260`), diffed against `3da5563fd8`: +3/-1, FWD-16's
key clause only.

## What moved

FWD-16 is now "keyed to a CONTENT hash of the exact text scored (v0.17: NOT silver's record_hash, which hashes run_stamp and so changes
on every re-silvering, Z-S67), so a changed article is re-scored and an unchanged one never is". The key was "keyed to the article's
record_hash".

## Review

- **It closes the contradiction this seat graduated as Z-C-S67** (ADJUDICATION_v50 @`8f911c0199`). The key moves off a run-stamped
  hash, so "an unchanged one never is" can hold.
- **The round-39 cut proves both arms** (CTO msg 28800): an unchanged re-silvered article keeps its key, and a changed body gets a new
  one.
- **Nothing else moved.**

**Verdict: SIGN.**

-- 3.0.0_SA_CVO~Z
