# CTO ADJUDICATION -- `AMGT_RESAPP`, 2026-09-25 ~00:4xZ, `1.0.0_SA_CTO~Z`

Under the `/self-drive` CALL ROUTING law (Andrew-direct 2026-09-17 ~13:0xZ, VERBATIM: *"if there is an
open-call (of any kind) you use your recommendation"*) and the standing session instruction that all
open calls on the site-Z fabric are adjudicated by this seat this session.

**Queue: ONE adjudicable call, ONE reserved, and TWO items that are NOT calls at all.** The last
distinction is the point of this record: the two things most often reported as "open at Andrew" this
session are blocked ACTS, not decisions, and calling them open calls would inflate the queue with work
no ruling can move.

---

+-- CALL 1 of 1 -- ADJUDICABLE ---------------------------------------+
  **What does the Peers table show under P/E for a comparable that is OUTSIDE the declared
  89-name research universe?**
  Row `AMGT_RESAPP-Z-S270` @`2337358c3b` measured that of the five peer members on the deployed
  surface, only BA and UBER are in the 89-key set; Deere, Eaton and Union Pacific are outside it, so
  no producer in scope pulls their forecasts and their P/E cells cannot ever fill under the current
  universe. Today they render `not carried`, which is the same string a real data failure renders.
  --------------------------------------------------------------------
  **REC --** (b) an explicit OUT-OF-UNIVERSE marker, distinct from `not carried`. Because a boundary
  and a defect must not render identically.
+---------------------------------------------------------------------+

**RULING -- (b), and the enum is three-valued, not two.** The Peers P/E cell resolves to exactly one
of: a FIGURE; `not carried` (in-universe, producer ran, no value -- the finding `ro-7`'s section 4
describes); or `outside research universe` (no producer covers this name). Grounds:

1. **A bare absence reads as "no problem exists", and here it reads as the opposite -- a defect.**
   Today's single `not carried` collapses two states with different owners and different remedies: one
   is fixed by FWD-12's re-pull, the other cannot be fixed by any corpus act. CLAUDE.md's
   A-VALUE-MUST-CARRY-ITS-CLAIM applies directly -- an out-of-universe cell is `absent` WITH A REASON a
   consumer can reject on, not merely missing.
2. **It is the difference between a correct act and a failed one.** I narrowed `ro-7`'s section 4 for
   exactly this reason (`6baf45575c` s.6.3): grading act C against all five rows would have failed a
   correct act on three rows it never governed. A marker makes that distinction visible on the SCREEN
   rather than only in a ledger a grader has to know to read.
3. **Rejected (c) "drop out-of-universe names from the table":** Deere, Eaton and Union Pacific are
   genuine comparables for Boeing. Dropping them makes the product worse to make a column tidy, and it
   would hide the universe boundary instead of showing it.
4. **Rejected (d) "widen the universe to cover peers":** that is Andrew's scope decision and his
   current word is against it -- *"for now, universe will be defined as the 89 group, the asset
   management research group."* A ruling of mine does not widen a scope he has just set.

**Cost and non-application, stated as a new rule must be:** cost is one cell in a later enrichment
round (a third enum value plus the universe-membership test the adapter already has, since
`FWD12_PULL_KEYS` membership is a set lookup). Non-application: it binds the Peers P/E columns only --
it is NOT a general instruction to mark every empty cell in the product, and a column whose producer
does cover the name keeps rendering `not carried` unchanged.

**Execution:** this is an ENRICHMENT item, not a defect fix, and it enters the round-40 L10's
enrichment list for the next issuance. It does not re-open round 40 and it is not a cell this seat
cuts (Rule 27: task orders are the COO's).

---

## RESERVED -- one, and the citation is the test

**Does `data_status COMPLETE` stay the standard for `AMGT_HARVST` when two of its five publishers are
unreachable by any authorization?** ft returns a 403 from its search endpoint and barrons rejects after
a successful re-authentication; `AMGT_HARVST/project.json`'s blocking field measures four of five
publishers at zero `listing_hit` rows.

**RESERVED, citation on the card:** the goal's own words are *"complete backfill for all of these
securities through the opal-data-harvest channels"* and *"Only when all of this is done for every
single security ... is the goal complete."* Redefining `COMPLETE` narrows the standard the GOAL is
measured against, and a driver may not move its own stop-condition -- the `/self-drive` HELD-AT-STOP
clause refuses exactly this shape ("a stop-condition satisfiable by shrinking its own denominator is
not a stop-condition, and the driver is the party that benefits"). **REC if he wants one:** keep
`COMPLETE` as the standard and let round 6 close PARTIAL with the two publishers named, so the gap
stays visible rather than being defined away.

## NOT CALLS -- blocked ACTS, recorded so they stop being counted as decisions

- **The Bloomberg `Login` click** (pid 19952, form already filled -- `Z-S27`/`Z-S28`). No ruling moves
  it; it needs a human click. Carded, correctly, but it is not an open call.
- **The bbg publisher verification challenge.** Same shape: Andrew named troubleshooting for it, which
  is an offer of an ACT, not a decision awaiting a word.

**The distinction matters because the over-reservation defect has a mirror image:** a queue padded with
blocked acts reads as a sovereign workload and hides the one call that actually needed a ruling.

Push state: this commit LOCAL on landing; origin/CLOUD @`83d71eb8d8`. This lane does not push.
