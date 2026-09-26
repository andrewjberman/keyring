# 2.0.0_SA_COO~Z -- 2026-09-25 19:25Z to 2026-09-26 00:50Z -- AMGT_RESAPP round 43: cut, landed, handed to L8/L9

## Done
- Round 42 closed at L10 @7d7dc8413d (89 of 94; the five misses had no Model block).
- Z-S279 disarm confirmed on the served plane (AMGT_CORPUS round 5's guarded re-derive), row Z-S282; no guard cell cut.
- Round 43 cut @7f0c99f5e2: rr-1 (five no-block names, scripted pull under Andrew-direct R-21 @b390c36444), rr-2 (Model Cases on
  page and export, harness grades them -- the PAGE hid the cases too), rr-3 (redeploy). CTO halves @c940964bea; rr-1 HEAD floor.
- rr-1: 5 of 5 blocks, in band. rr-2 drained @4c5225c729 (gitlink @ca12374490). rr-3: redeployed, then held when the live library
  grew to 95 mid-round; AC2 pinned to the cut's 94 (amendment 1 @a2072789f1); 94 of 94, cases 282 of 282.
- Real run on 5174: Model tab renders each case. Packet @c6183d5ab8, handed to 3.0.0_SA_CVO~Z at 00:46Z.

## Open
- L8/L9, the slug, the CTO's round-43 analysis; round 44 cut from it.
- Temp capture dirs outside the repo (amgt-r42-cache*, -close, amgt-r43-cache, /tmp/tmp.5dHqjUoZQw) need a person to delete.

## Lessons
- Equality can pass because two surfaces are wrong the same way; read what the page SAYS, not only whether the export matches it.
- A live population can move under a round; pin the cut's population in a file with its read time, and carry the newcomer as a row.
- Re-arming the watcher before the old one's expiry notice arrives creates duplicates; stop the older task when that happens.

Push state: every commit above is LOCAL (push state UNREAD).
