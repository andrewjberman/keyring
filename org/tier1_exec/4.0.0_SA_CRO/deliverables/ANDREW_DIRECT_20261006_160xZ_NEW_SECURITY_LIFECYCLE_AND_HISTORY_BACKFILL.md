# ANDREW-DIRECT 2026-10-06 ~16:0xZ -- new-security lifecycle: classify, backfill 1Y history, then incremental

Channel: Claude Code terminal, seat 4.0.0_SA_CRO~P. Two screenshots (Positioning > ETFS > Holdings Breakdown >
Performance): QXO B row blank on every window with name "QXO INC QXO 5 1/2"; CSCO and BX blank past WTD.

## Verbatim

> Also we need a system whereby we track the adds of new securities and pull their 1Y daily history so that we can
> fill out the "Performance" toggle view on the "Positioning" page "ETFS" view. We also need that to be connected to
> the Canonical ETFClassifier positioning table. There should be a whole system that manages when new securities come
> in, they get their row filled out, and their history backfilled, then proceeeding with daily incremental pull rather
> than a whole backfill every time and recalculate based off the data we already have, to keep things efficient on
> quota. Otherwise we end up with scnearios like this: [Image #1]. Notice how QXO B is out of pattern on name field and
> has no performance. Interestingly enough, we successfully pulled CSCO and BX, however are lacking performance data
> past MTD for those, as well as for SALXX: [Image #2]. Please look into how our existing BBG daily pull handles
> situations like these, existing resources and infrastructure around these functions, and identify how we can
> structure a more robust pattern to this end.

Same session, earlier answers recorded in commit messages: "Sure MSTR can do that." (push CLOUD); "Eh, it can get
handled tomorrow automatically, right?" (no same-day Bloomberg re-pull); "I feel like it does not, as long as we have
weights" (per-holding price not needed on Positioning).

Analysis: `org/tier1_exec/4.0.0_SA_CRO/deliverables/` brief written from this record (same seat, same day).
