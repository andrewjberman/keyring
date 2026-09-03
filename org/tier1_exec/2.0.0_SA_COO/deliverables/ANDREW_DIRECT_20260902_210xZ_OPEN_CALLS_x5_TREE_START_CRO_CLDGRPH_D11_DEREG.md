# ANDREW-DIRECT 2026-09-02 ~21:0xZ -- /open-calls x5 at the COO terminal: rulings on all five

**Channel:** Andrew, in person, at the `2.0.0_SA_COO` (base, laptop) terminal, answering the
`/open-calls` render of 2026-09-02 ~20:55Z (five cards). **Recorded by:** `2.0.0_SA_COO`.
**The phrasing IS the ruling** -- verbatim below; readings are marked as readings.

## VERBATIM

> Project tree prereq builds are mandatory start point (call 3), split up work with CTO on that,
> and when you guys are completely done issue it to CVO for review. On call 2, 4.0.0_SA_CRO Base
> can look into that they are already online. Call 1, once we're completely good to go on Call 3
> setup and validated, we can use CLDGRPH as a water test, more details on that at that time.
> Call 4, yes compefficacy is laptop under D11. Call 5, yeah sure deregister CVO~A, any excess
> work they're dealing with can be reallocated to 0.8.0_AE_CloudComp Base, they are online and
> available.

## The five cards, as put (so the ruling binds on what was asked)

| # | call as rendered | ruling (verbatim fragment) |
|---|---|---|
| 1 | Open NFRA_CLDGRPH step 6: cut S10-S13? | *"once we're completely good to go on Call 3 setup and validated, we can use CLDGRPH as a water test, more details on that at that time."* |
| 2 | Re-route the custodian residual? (a) CRO~Y now (b) hold for CRO base | *"4.0.0_SA_CRO Base can look into that they are already online."* |
| 3 | Start the project-tree prerequisite builds? | *"Project tree prereq builds are mandatory start point (call 3), split up work with CTO on that, and when you guys are completely done issue it to CVO for review."* |
| 4 | NFRA_COMPEFFICACY's fabric at registration: "laptop"? | *"yes compefficacy is laptop under D11."* |
| 5 | GO on deregister CVO~A + sequence CloudComp Unit 3? | *"yeah sure deregister CVO~A, any excess work they're dealing with can be reallocated to 0.8.0_AE_CloudComp Base, they are online and available."* |

## Readings (mine, marked; the verbatim above governs on any conflict)

- **Call 3 is the MANDATORY START POINT.** The tree's prerequisite builds (spec s.10 / the four
  RULED calls @5f8b774a5d) start NOW, the work is SPLIT between `2.0.0_SA_COO` and `1.0.0_SA_CTO`,
  and the finished set goes to `3.0.0_SA_CVO` for review ONLY when it is COMPLETELY done -- not
  piecewise. The split is the two seats' to agree; this record does not fix it.
- **Call 1 is SEQUENCED BEHIND call 3.** NFRA_CLDGRPH stays at L5. Its step 6 opens only after the
  tree setup is complete AND validated (CVO's review is the natural validation carrier; Andrew's
  "more details at that time" means the water-test shape is still HIS to give -- no seat designs
  it in advance). Nothing on NFRA_CLDGRPH moves before then.
- **Call 2: the custodian residual STAYS routed to `4.0.0_SA_CRO` base** -- Andrew states the seat
  is online. MEASURED at 21:0xZ on the broker: `4.0.0_SA_CRO` base is NOT in the live list (only
  `4.0.0_SA_CRO~Y`); the 20:05Z routing message is QUEUED for it and a fresh nudge is sent the same
  turn. The broker not seeing a seat Andrew says is online is a registration-timing fact, not a
  contradiction of his word; the ruling stands as given.
- **Call 4: NFRA_COMPEFFICACY = fabric `laptop`, directive `D11`.** Registration is
  `0.0.0_AB_MSTR`'s act (the standing ask). Under call 3 the tree is the start point, so the row's
  HOME is a tree question the split resolves; if the row is cut before the tree's roots exist it
  lands flat and MOVES in (call-2 ruling of @5f8b774a5d: project.json moves in).
- **Call 5: `3.0.0_SA_CVO~A` deregistered** (this seat, this turn; result stated in the log).
  Andrew ADDS: ~A's excess work may be reallocated to `0.8.0_AE_CloudComp` BASE, which is online and
  available. The allocation act is `3.0.0_SA_CVO` base's (it holds ~A's inherited lanes); this seat
  relays the authorization, it does not pick the items. The CloudComp Unit 3 sequencing half of the
  card was not separately addressed; Unit 2 LANDED @dffbee781c at 21:01Z, so the only order left is
  3a then 3b, applied as CVO's stated preference and mine.

## Standing bounds this ruling does NOT touch

- `/drive` OFF, D2 HELD (Andrew, @357df5bf9b). Zero crons.
- Tooling work is NOT this seat's (Andrew ~17:1xZ): the tree builds are ORG-STRUCTURE work
  (`org/missions/**`, register, gates), not comp-tool work; where a build touches a comp-tool, that
  limb goes to `0.8.0_AE_CloudComp`.
- No project past L5 except the three water tests; no broadcasting via XXX.md; unfabricked
  projects held for review.
- The default-off rule for fabric engagement at this terminal (Andrew 2026-09-01) is LIFTED for
  exactly the acts these five rulings name, and nothing wider.
