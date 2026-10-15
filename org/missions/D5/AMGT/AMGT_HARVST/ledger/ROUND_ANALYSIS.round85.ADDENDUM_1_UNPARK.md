# AMGT_HARVST -- ROUND 85 ANALYSIS, ADDENDUM 1: the park lifts; round 86 runs the wsj and barrons refresh on dell1 (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~16:1xZ)

**Carrier:** `org/tier1_exec/2.0.0_SA_COO~W1/ANDREW_DIRECT_20261015_160xZ_WSJ_BARRONS_OPS_RUN_ON_DELL1.md` @94086281f2. Andrew, verbatim: "We can
run the WSJ and Barron's ops on this device. You shouldnt need me to sign in because you have scripts for that, but if you need me to do it for
whatever reason to get the long term trust token or etc, open a Chromium and I will handle it."

## Ruling

- **The un-park condition of round 85 section 3 is met** on its first limb ("Andrew re-seats AMGT_HARVST"): he places the wsj and barrons ops on
  dell1. `2.0.0_SA_COO~W1` cuts round 86.
- **Round 86 scope:** the wsj and barrons session refresh and one completed cycle each, run on dell1. Nothing else from the enrichment list rides
  this round.
- **Order inside the round:**
  1. The existing sign-in scripts first, on dell1.
  2. Read the first dell1 cycle BEFORE any code change, as round 85 section 3 requires: it tells "a fresh session cures it" from "the job reads
     another cookie jar" (Z-S121).
  3. Only if a script cannot get the long-term trust token: open a Chromium on dell1 and ask Andrew to sign in, naming the publisher.
- **One writer per publisher.** wsj and barrons collection at site Z (`~ZW`) stops before the first dell1 cycle, so two boxes never hold the same
  subscriber session. That touches site Z's seat, so `0.0.0_AB_MSTR~DELL1` coordinates it with site Z's MSTR. The dell1 cycle does not start until
  that stop is confirmed. Other publishers stay at site Z.
- **Z-S121** stays this seat's row. The round-86 first-cycle read is its evidence.

-- 1.0.0_SA_CTO~DELL1
