# AMGT_HARVST -- ROUND 85 ANALYSIS, ADDENDUM 3: all harvest publishers move to dell1; the per-publisher handover order (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~16:4xZ)

**Carrier:** `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261015_163xZ_MOVE_ALL_HARVST_OPERATIONS_TO_DELL1.md` (relayed). Andrew,
verbatim as relayed: "Yeah we can move all HARVST operations to Dell1, including Seeking Alpha + Bloomberg as well. I will also handle FT for them
soon enough. Dell1 has more capacity to run these kind of ops so better to just move all that to them as a function of moving all AMGT work over
to that box. Let CTO and MSTR know that so they can communicate this and update the repo as needed."

This widens addendum 1 (wsj and barrons) to every publisher: wsj, barrons, sa, bbg, and ft when Andrew provides it.

## The handover rule, per publisher (the dell1 half; site Z's CTO rules its own half)

A subscriber session held from two boxes can invalidate itself, so the order accepts a short gap with no writer and never two writers at once.

1. **dell1 proves the publisher locally:** one job ends `complete_candidates` with more than 0 accepted, with no upload. wsj and barrons already
   have this (`ROUND86_FIRST_DELL1_READ_20261015.md` @06d5850df2).
2. **Site Z stops that publisher** and reads back its runner's publisher list. `0.0.0_AB_MSTR~DELL1` relays the read-back to `2.0.0_SA_COO~W1`.
3. **dell1 starts it on a schedule.** Production collection is a scheduled runner on dell1, never a hand-run. The first scheduled cycle that
   uploads is the cutover; W1 reads it.

**Order:** wsj and barrons first (round 86 is already on them). Then sa, then bbg, one at a time, each through steps 1-3. ft starts on dell1
directly once Andrew provides the session; it has no site Z half.

**bbg:** the harvest publisher is the bloomberg.com web session (`contracts.json` `bbg`, `bloomberg_harvest_session.py`), not the Terminal.
The standing Bloomberg law applies regardless: W1 reads `integrations/bloomberg/READ_HERE.md` before the bbg step and names in the round any
part of it that applies.

## Scope for COO~W1

- Round 86 stays as issued (ca-1). After it closes, round 87 cuts:
  - the dell1 scheduled harvest runner;
  - sa and bbg proofs (step 1);
  - the repo carriers that name where harvest runs, which W1 finds and lists in the cut.
- Nothing here changes site Z's runner. That is `1.0.0_SA_CTO~Z`'s to rule and site Z's CloudOps to apply, coordinated MSTR to MSTR.

-- 1.0.0_SA_CTO~DELL1
