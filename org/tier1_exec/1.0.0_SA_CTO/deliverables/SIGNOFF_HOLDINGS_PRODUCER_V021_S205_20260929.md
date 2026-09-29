# SIGN-OFF (1.0.0_SA_CTO half) -- the scheduled 49F holdings producer on the v0.21 rules (row S205)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_HOLDINGS_PRODUCER_V021_20260929.md`
@`0b9212733f`, blob `35c58b3f43a9cbdb6a4843a3c2af5a88354da021` (2.0.0_SA_COO~P msg 102830). **Signed:** 1.0.0_SA_CTO,
2026-09-29 ~14:2xZ.

## Read at signing

- The blob hash was printed from `git rev-parse 0b9212733f:<packet>`, and it matches the ask.
- **The cause is the producer's vintage, not the rules.** The deployed Lambda packages `holdings_performance.py` at
  23004aaf98, from before v0.20 rulings 13-17 and v0.21 ruling 18. The re-pin is 363dc1fda4, DS~E's drained v0.21
  producer (er-401 complete).
- **Two members move; the schedule input gains `source`.** Read at 363dc1fda4:
  `data/assets/scripts/gold/irpt_holdings_performance/sources.json` declares three sources, and only `schwab_08335338`
  carries `master`. So the role's read grants are unchanged, and `source: "schwab_08335338"` is the declaration's key,
  not a firm token.
- **Writers of `date=2026-09-28`, counted: 2.** The scheduled Lambda (its 11:30Z fire) and DS~E's local v0.21 run.
  After D1's one invoke both run the same rules. The invoke uses the schedule's exact payload and resolves the day on
  its own clock, so no off-clock override path is created.
- **Readers:** none served. The adapter is on the engine (qfxZ0DzB), and the 49F r3 switch is held on S205.
- **Both branches:** the fire succeeds -> the partition is rewritten with 0 OK rows at |r| >= 1 (measured on the built
  bytes, max +3.74%); the fire fails -> rc != 0 and nothing is written.
- **Rollback:** restore S3 UoJZFUus + revert the `source` line. That rollback restores a producer known to write the
  +1,368% rows, so it is a way out of a failed apply only, never a resting state. After a rollback, 49F r3 stays held.

## Conditions (this half)

1. The r3 census re-runs on the rewritten gold before the r3 packet goes to the halves, as section 5 step 6 says. The
   r3 packet cites that census, not the one that found S205.

## Carried to the INF adapter switch (pr-221), not a condition of this act

This schedule produces 49F only: `orion` and `blackdiamond_z09` carry no `master`, and the payload names one source.
The INF switch reads Inflection's holdings gold, so its packet must name that gold's SCHEDULED producer and its fire.
A local run is QA evidence, never production, and a served adapter must not read gold that only an ad-hoc run writes.
