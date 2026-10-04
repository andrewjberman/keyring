# AMGT_HARVST round 41 -- HVST-an-2 never-widen pair, CTO half (the served gold tone rebuild)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-03 ~22:0xZ. **COO half:** `deliverables/2.0.0_SA_COO_H/round41/NEVER_WIDEN_HALF_COO_GOLD_TONE.md`
@72f2c9be42 (msg 29036). **Authority:** Andrew ~20:3xZ card 2, "yes to all recommendations" (@9fe6e6f111).

## What I read

- **The rule**, enforced by the act twice (dry run before the write, and the written parts): mention GONE 0 and CHANGED 0 on the
  pre-existing fields; every row carries the 4 tone fields; JOIN MISMATCH 0. Daily: GONE 0, and every change is explained (an added
  mention, or coverage-only on the as-of day), with OTHER 0.
- **`round41/gold_tone_signing.json`, read by this seat, agrees with the half figure for figure:**
  - mention 23,691 -> 31,042, gone 0, changed 0, added 7,351;
  - tone rows 31,042, all content-keyed and scored, join mismatch 0;
  - by publisher: barrons 637, bbg 3,133, ft 926, sa 25,519, wsj 827;
  - daily 58,300 -> 58,512, gone 0, changed 27,594 (all by an added mention), coverage-only 0, other 0.
- **Writers:** 1 (`publication_gold.write_gold`, never-overwrite); no scheduled producer.

## Signed knowingly: the 7,351 ADDED mention rows

They are sa +7,043 and bbg +308: articles already in silver (the sa backfill finished 04:46Z), served because the builder always
reads the newest silver. Card 2 approved scoring "data already stored", and these are stored. Serving them collects nothing: 0
collectors run, the Scheduled Task is Disabled, and STOP_FT is unchanged. A builder-bypassing tone-only path would be new code
outside the builders, which is worse.

## Conditions

1. The act's own gate holds on the WRITTEN parts, and the act record names both parts and both digests. If it fails, ROLLBACK as
   the half states (BEFORE rows re-put as a newer part; nothing deleted).
2. **Post-act read:** RESAPP's chatter route still serves `tone` null with its reason (it reads no tone field yet), and the timeline
   day view of BA serves its articles. One read each, printed.
3. One act, once. No other table is written: `chatter_window` (FWD-17) is not part of this act.

**CTO HALF: SIGNED** for HVST-an-2.
