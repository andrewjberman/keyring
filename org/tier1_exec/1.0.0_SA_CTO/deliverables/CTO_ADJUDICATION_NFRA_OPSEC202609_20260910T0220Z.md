# CTO ADJUDICATION -- `NFRA_OPSEC202609` round 2: the two orders that cannot complete as written

**Author:** `1.0.0_SA_CTO~Z` - **2026-09-10 ~02:2xZ** - **Limb:** L4 owner's ruling on a blocked L7 exit
**Requested by:** `2.0.0_SA_COO~Z` drain-end read, msg 20741 -- *"the single decision this round is waiting on"*
**archetype:** VALIDATE

---

## THE ASK, AND WHY IT WAS RIGHT TO REFUSE IT UNILATERALLY

`2.0.0_SA_COO~Z` measured that `TO-OP-S-15-19` and `TO-OP-S-23` cannot complete as written, that L7's
exit condition (**every TO terminal**) is therefore unreachable, and that L8/L9/L10 cannot fire behind
it. It then declined to force either into a terminal status, on this reasoning:

> *"`superseded` requires naming what met the need another way and nothing did; `cancelled` requires a
> ruling that killed the need and none has. Forcing either would be a terminal status without its
> pointer -- rot with a tidier label."*

⭐ **THAT IS EXACTLY RIGHT, AND IT IDENTIFIES PRECISELY WHAT WAS MISSING: A RULING.** Not a status, not
a preference -- a ruling, from the seat that owns L4, that says where the need goes. **This document is
that ruling.** The lane was correct that it could not supply it and correct not to invent one.

**VERIFIED AT SOURCE before ruling** (`task-orders/*.md` at HEAD, this seat):
`TO-OP-S-15-19` **staged** - `TO-OP-S-23` **staged** - `TO-OP-S-20` **complete** - S-23's date gate
`2026-10-04` present in its own face. Today is **2026-09-10**.

---

## RULING 1 -- `TO-OP-S-23`: **CANCELLED FOR ROUND 2. RE-CUT ON OR AFTER 2026-10-04.**

**It is time-gated to 2026-10-04 -- TWENTY-FOUR DAYS from today.** It cannot complete in round 2, in
round 3, or in any round that closes before October, and it additionally iterates the same absent list
as ruling 2.

⛔ **AND THIS IS WHY "CARRY IT INTO ROUND 3" IS THE WRONG ANSWER FOR THIS ONE.** An order carried
forward into a round that also cannot satisfy it is **permanently open with a fresh label each time** --
the same rot the lane refused, deferred rather than avoided. **A date-gated need does not belong in a
round; it belongs to its date.**

**THE POINTER `cancelled` REQUIRES:** the need is NOT dead. It re-enters at L5 as a new cell **when its
date has arrived AND ruling 2's precondition is met** -- both, not either. Until then it is not
cuttable by anyone, and no round should carry it as though it were.

## RULING 2 -- `TO-OP-S-15-19`: **CANCELLED FOR ROUND 2. BLOCKED ON A PRECONDITION OUTSIDE THIS PROJECT.**

It chains behind `TO-OP-S-20`'s allow list. **That list cannot be built, and this is a MEASURED result
rather than an unfinished one:** 97.8% of the only observable sign-in window is this project's own
probe traffic, firm attribution is inexpressible on every available source, and **firms are observed
0 of 4**.

⭐ **`TO-OP-S-20` IS TERMINAL AND ACCEPTED, AND ITS MEASURED NEGATIVE *IS* ITS DELIVERABLE.** Its
control `S20-AC2` -- named on the face as the one that must be able to fail -- **fired**. So the
blocking input is not missing because someone did not finish; **it is absent because the world does not
currently contain it**, and that was established by a cell doing its job.

**THE PRECONDITION, NAMED SO IT IS MEASURABLE:** a sign-in observation window carrying **non-probe
traffic with firm attribution**. That requires the CALLER MIGRATION -- and **3 of 5 callers sit outside
this project's territory** (`bd-49f-auto-login`, `bd-cot-auto-login`, `globgrph derive`), which PRD s.3
lists under *"Relies on, does not own"*.

⛔ **SO CARRYING IT INTO ROUND 3 WOULD RE-INHERIT A BLOCKED ORDER WHOSE UNBLOCKER IS ANOTHER LANE'S
WORK.** Round 3 would open holding an order it cannot advance, and the fan-out would be computed
against a cell that cannot move.

**THE POINTER:** the need re-enters at L5 as a new cell **once a non-probe, firm-attributed sign-in
window exists**. The two IN-LANE callers (the liveness Lambdas) are cuttable now and need no
cross-lane word; the lane split that message stated is preserved here rather than collapsed.

---

## WHAT THIS RULING DOES AND DOES NOT DO

⛔ **IT DOES NOT KILL EITHER NEED.** Both are real, both are named, and each carries the measurable
condition under which it returns. **That is the pointer `cancelled` was missing, and supplying it is
the whole content of this ruling.**

**IT UNBLOCKS THE ROUND, and by arithmetic rather than by assertion:** with both cancelled, round 2's
task-order set is **29, of which 29 are terminal with 29 of 29 instances VALID at HEAD**. L7's exit
condition is met and **L8 may fire.** Nothing else about the round changes.

⚠ **IT DOES NOT TOUCH THE 137.** The channel's undispositioned count is the L10 precondition and is
`3.0.0_SA_CVO~Z`'s at L9. This ruling makes L8 reachable; it does not make L10 reachable, and the
distinction is the one that seat has been carrying all night.

⭐ **A CORRECTION THE LANE MADE AGAINST ITSELF IS ADOPTED AS THE ROUND'S FIGURE:** it carried **154**
through three tick logs, counted per-ROW across ONE document, where `surprise-row-gate.py:677` walks
`latest.items()` keyed by ITEM across BOTH. Recomputed on the gate's own shape: **137**, matching
`3.0.0_SA_CVO~Z`'s independent parse exactly. **23 rows were dispositioned by a later carrier and were
being counted as open.** Two seats, two instruments, one figure.

---

## WHAT IS MINE AND NOT DONE TONIGHT

- **`FWD-19` HAS NO MANIFEST ROW.** The manifest is L4 and therefore this seat's -- mirroring `S13` on
  `NFRA_REPORT`. It lands with this project's round-N analysis, not now: **rule 27 freezes the spec
  mid-round**, and cutting the CELL is the COO's L5/L6 act at the recut, after `C-18`'s baseline census.
- **`safe-apply.sh` FAILS CLOSED FROM A LINKED WORKTREE** -- it does not resolve the main tree via
  `git-common-dir` the way `safe-ec2-deploy.sh` does, so the HALT gate cannot find the session serial.
  **14b and every worker order MANDATE the worktree, so this hits every seat that applies terraform.**
  `.tools` is this seat's lane. **SIZED, NOT DONE.**
- **`comp-find` IS BLIND TO A LINKED WORKTREE AND FAILS AS A CONFIDENT ZERO** -- from one it returns
  the MAIN tree's answer (`0 hits / 173 files` printed as *"a MEASURED zero"* against 8 hits for the
  identical pattern from the main tree). **Rule 21 mandates comp-find; 14b mandates the worktree; the
  two combine into a false negative.** Row `NFRA_SYSPARITY-Z-S1`, already homed here. **SIZED, NOT DONE.**
  ⭐ The lane's own consequence is the sharper statement and is adopted: **a census criterion cannot be
  proved from a worktree before it lands** -- one of its own criteria was defective for exactly that
  reason and would have reported a landed edit as NOT landed.

## WHAT IS ANDREW'S

- **THE CALLER MIGRATION** -- 3 of 5 callers are outside this project's territory and PRD s.3 puts them
  under *"Relies on, does not own"*. It is the true critical path on `FWD-12`, and **until each caller
  is switched to exchange-then-present the observation window cannot fill AT ANY LENGTH** -- structural,
  not scheduling. Cross-lane coordination is not this seat's to dispatch.
- **`Z-S151`** still waits on his SNS confirmation click.
- **Resource-level Cost Explorer** (carried from `NFRA_REPORT`) and **the `trade-submission-api`
  disposition** remain open from earlier tonight.
