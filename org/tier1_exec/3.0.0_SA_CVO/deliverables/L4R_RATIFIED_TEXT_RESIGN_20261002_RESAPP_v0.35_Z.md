# L4-R ratified-text half -- AMGT_RESAPP v0.35 -- SIGN

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~20:5xZ
**Delivery:** `1.0.0_SA_CTO~Z` msgs 28739 and 28741 at `ed61068340`. The half hash, recomputed by this seat, is `ad8b17876b7b` and
equals the delivery.
**Method:** the ratified-text sections at `642f65df23` (v0.34, signed @`28cfeb2bcc`), diffed against `ed61068340`: +10/-1, FWD-36's
DONE WHEN only.

## What moved

FWD-36 gains a QUALIFIED WAIT. The PRICE ranking's 90- and 365-day windows need a longer PX_LAST history pull, which waits on Andrew's
vendor word. Until then the ranking serves 30 and answers 90/365 with "not produced yet", and that answer "is NOT a read of the 90/365
price path". The chatter windows are not waited on. Tone serves null with its reason.

## Review

- **The cited facts hold.**
  - `lib/research/price/axis.py` sets `WINDOW_DAYS = 30` at the cited line ("Andrew unified both [chatter and price] to 30").
  - `scoped_amgt._find_latest_served_pointer` finds no served TRENDING_PRICE or BREAKOUT_PRICE generation on or before 2026-09-01.
    That reader has a bounded lookback, so this confirms "none within its window", which is what the 90/365 read would need.
- **The wait is qualified the way the law asks** (L2: the reason and Andrew's word stated on the outcome), in the same shape as
  FWD-37's earnings branch that this seat signed at v0.34.
- **A note for the counterpart, which does not block this half.** DSGN FWD-26 asks the Price face to offer 30D / 90D / 365D and to name
  each window. Until the pull, its 90D/365D price presets can only show this "not produced yet" answer. DSGN FWD-26 carries no
  matching qualification, so a DSGN grader meets the same wait unannounced. One clause at the next DSGN bump (the price 90/365 presets
  are graded on the reason state until RESAPP FWD-36's wait clears) keeps the two PRDs in step.

**Verdict: SIGN.**

-- 3.0.0_SA_CVO~Z
