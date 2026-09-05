# NFRA_CLDGRPH round 4 -- the GOAL this lane's /drive loop is driving to

**Set by** `2.0.0_SA_COO~A` on ANDREW-DIRECT relayed verbatim by `1.0.0_SA_CTO` (msg 94223, 2026-09-04 ~17:0xZ):
*"need you to tell all COOs to put a /goal and associated /drive loop on for their respective projects, need to
get these proceeded through the /canonical-flow with the internal subagents/dispatch drain, go get it going"*

**Scope:** NFRA_CLDGRPH only. This lane acquires no project from that message, and a /goal that would need a
scope change is an L2 re-entry through `1.0.0_SA_CTO`, not a /drive decision.

---

## THE GOAL, in one sentence

Carry NFRA_CLDGRPH round 4 through the canonical flow to **L10** -- every open cell's task order TERMINAL on a
VALID proof-of-spec instance, every surprise row DISPOSITIONED, and the ONE slug delivered to `1.0.0_SA_CTO` --
using worker subagents in their own worktrees, drained by this seat, with no push and no scope change.

## DONE looks like this, and each line is measurable

1. **Every round-4 order terminal.** 12 orders were issued (D-1..D-12). Terminal = `<status>` reads `complete`
   at HEAD **and** its proof-of-spec instance validates `rc=0` **with coverage checked against the order's own
   criterion ids at HEAD** -- not the worker's own uncovered run. TERMINAL AT THIS WRITE: D-4, D-12, D-2, D-3.
   OPEN: D-1 (live, slot ~1), D-5 (live, ~3), D-6 (live, ~2), then D-9, D-10, D-11, D-7, D-8.
2. **Every cell of decomposition v0.4 covered and DONE** -- 22 cells; the OPEN set must reach empty by orders,
   never by editing the decomposition (the spec is FROZEN mid-round).
3. **Every surprise row dispositioned.** 55 rows at this write. An ARMED row is either disarmed by its
   `disarm_owner` or carried into the L10 slug NAMED, with its owner. This seat does not disarm another seat's
   row and does not disarm its own on a build -- only on an exercise.
4. **The L10 slug sent, once,** to `1.0.0_SA_CTO`, only after 1-3 hold. The CTO answers with a PRD addendum or
   a ROUND-5 analysis; CLOSED is when every FWD grades REALIZED, which is the CTO's call and not this lane's.

## THE ORDERING THAT CANNOT BE COMPRESSED

Two dependencies bound the finish and no amount of drive shortens them:

- **CG-x-2 (TO-CG-D-9) needs ONE CALENDAR NIGHT** -- the first 02:00Z nightly fire AFTER TO-CG-D-1's digest
  pins land ("a night under pre-fix bytes is not the night FWD-2 means", ROUND_ANALYSIS.round3.md s.2 item 2).
  If D-1's pins land after 02:00Z on any given day, the earliest D-9 can be exercised is the following night.
- **CG-x-4 (TO-CG-D-10)** needs one full cycle after D-9; **CG-s-8 (TO-CG-D-7) is LAST by ruling R7**, with
  this seat's own deletion of the laptop's local Kuzu DB at that drain, and **TO-CG-D-8 closes the run.**

So the loop's honest stopping condition is not "keep going until done tonight". It is: **drive every order
whose dependencies are met, and when the only remaining work is waiting for a night, say so and hold.**

## WHAT THE LOOP MUST NOT DO

- **No push.** Every commit is LOCAL until `0.0.0_AB_MSTR`'s window on Andrew's word (LD-0522).
- **No spec or decomposition edit mid-round.** The only off-spec act is a surprise ROW.
- **No new project, no widened scope**, and no gate this lane invented.
- **No self-wind-down** and no "wait for the scheduled run" where an ad-hoc QA run is lawful -- except where
  the ad-hoc would destroy the discriminator the scheduled run exists to produce, which is exactly CG-x-2's
  night, and that exception is named above rather than used as cover.

## HOW COMPLETION IS VERIFIED, not claimed

At the point this lane believes 1-4 hold, the check is re-run from the RECORD, not from memory: each order's
`<status>` read at HEAD with `git show`; each instance re-validated with its own id list; the channel's row
count and every ARMED row's standing enumerated with its `disarm_owner`; the decomposition's OPEN set read
unscoped. A "done" that rests on this seat's recollection of its own drains is not done.
