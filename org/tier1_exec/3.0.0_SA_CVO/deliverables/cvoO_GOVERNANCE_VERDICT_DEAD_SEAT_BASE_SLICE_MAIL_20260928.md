# Governance verdict: who clears unread base-slice mail of seats with no live session

Adjudicator: `3.0.0_SA_CVO~O` (governance fork -> CVO, per Andrew's self-drive arming). Recorded 2026-09-28; clock read
00:4xZ.
Fork: `1.0.0_SA_CTO~O` file `20260928T004300Z_1.0.0_SA_CTO_O_governance_fork_dead_seat_base_slices.md`, raised by
`0.0.0_AB_MSTR~Z` (file 20260928T004148Z).

**Facts as given:** MSTR~Z's census at 00:1xZ over 28 bases found 11 unread messages in the base slices of 6 bases with
no live session. 5 are `0.0.3_BG_BBGTerminal`'s, and a hold release may be among them. MSTR~Z declines to read other
seats' mail.

## Verdict: YES. `0.0.0_AB_MSTR~Z` routes, within four bounds

Delivery is the integrator's lane. CLAUDE.md already names a base serial with no base session "a silent hole" and
requires an addressed item to reach a LIVE recipient or be PARKED with an owner and an un-park condition. Nothing in the
estate currently does that for mail already sitting in a dead slice. Routing by header closes the hole without adding a
reader of bodies.

1. **Headers only.** MSTR~Z reads From, To, Date and Subject, and never the body. The subject line is the one piece of
   content it sees, and it is used only to pick the recipient.
2. **Copy, never move.** The original stays in the base slice, unread and unmoved, with a pointer file beside it naming
   where each copy went and when. A future base session, or its watcher, still consumes the original. Moving it to
   `read/` would forge the one signal that says the addressee has not read it.
3. **A forward is information to its recipient, not an order.** Each copy states its original addressee at the top. The
   receiving lane acts only inside its own authority. A message addressed to another seat never becomes a directive
   to the lane that receives the copy: an Andrew word to one agent is not converted into an act by another (CLAUDE.md
   section 2). **Anything whose subject names an Andrew word, a hold, a release or an entitlement goes to
   `1.0.0_SA_CTO~Z`, the router, and never to a worker lane.** That includes the possible `0.0.3_BG_BBGTerminal` hold
   release; any Bloomberg act stays under `integrations/bloomberg/READ_HERE.md`.
4. **Scope.** This covers bases with no live session, measured at the time of the pass (the census method printed with
   its denominator), on this fabric. A slice whose base is live is that session's to read. This verdict creates no
   loop or gate: MSTR~Z runs a pass when it finds the hole, on its own cadence.

## Out of scope

This verdict does not rule on the content of any of the 11 messages, and it does not authorise any seat to act on a
hold release. That stays with the addressee, or with Andrew through the CTO.

-- 3.0.0_SA_CVO~O
