# ENDPOINT (step 2, `/endpoint --forward`) -- THE BRIEF-TO-CUT CHAIN

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-05 ~19:0xZ
**On:** `4.0.0_SA_CRO`'s L1 brief `docs/briefs/the-brief-to-cut-chain-where-a-v3-round-spends-its-cost-brief-20260905.md`
@`fd9b987a87` (AMENDED; this endpoint was cut from @`b6c6e33060` and RE-READ against the
amendment before going anywhere -- see the amendment note below)
**Commissioned by:** Andrew-direct 2026-09-05 ~13:3xZ at the `4.0.0_SA_CRO` terminal, VERBATIM **"recs
approved"**, record @`8e89f1127f`. **He confirms the DONE WHEN lines below; that is the last point in this
project's life at which the loop waits on him.**

---

## THE ARC, in one paragraph

Two v3 rounds independently found that the round's cost lands in the **cut**, not the work. Every defect that
cost NFRA_OUTSET round 1 an amendment was **readable on the issuer's own tree before the spawn**, and every
one was **first read by an assignee at its first commit** — in the assignee's name, at the most expensive
moment, for a defect in the issuer's face. The L6 gate grades tier, committer, a non-empty grant, coverage,
grammar, presence and the stage flip; it grades **none of the six properties those defects had**. This project
moves the finding from the assignee's first commit to the issuer's own tree. It builds no new gate family and
it does not re-implement a single gate it reads.

---

## THE EIGHT LINES — seven outcomes, and what DONE means for each

```
  FWD-1  An issuer learns AT THE CUT that a face grants a tool but not the
         precondition of a gate that tool's edit will trip
         DONE WHEN  EXERCISED -- a real issuance is refused for it, in the gate's own voice
         ACCEPT     a face granting a tool without the gate-precondition its edits fire is
                    refused before the issuance lands, naming the FACE and the missing
                    precondition; measured against the 9-of-17 case that shipped (F2)

  FWD-2  An issuer knows a criterion is satisfiable BY AN HONEST IMPLEMENTATION
         before it ships
         DONE WHEN  EXERCISED -- a criterion only a dishonest implementation could pass is
                    caught before a worker is asked to meet it
         ACCEPT     on the issuer's own tree, a criterion whose expectation cannot be met by
                    a correct implementation is NAMED pre-spawn, with the honest measurement
                    beside it; O1-AC2's 5 s budget against a 6-12 s unavoidable walk (F3) is
                    the worked case and must be caught

  FWD-3  The face-level facts EVERY face shares are computed once, never typed per face
         DONE WHEN  APPLIED -- the derivation exists and the faces of an issuance come from it
         ACCEPT     the proof stem the gate globs, the invocation form for a forwarder, and
                    the artifact names a criterion cites are identical across an issuance
                    because one derivation produced them; a defect in a shared fact is ONE
                    repair, not sixteen (F4)

  FWD-4  A row filed against ONE face is graded against the POPULATION before it closes
         DONE WHEN  EXERCISED -- a real row closes with the population read
         ACCEPT     a row naming a face defect closes only with a sentence naming every face
                    sharing that trigger and their state; the 3-of-5 repaired-on-the-member
                    case (F5) would not close under it

  FWD-5  An issuer seats and re-seats slots WITHOUT amending faces
         DONE WHEN  APPLIED -- re-seating a slot changes a worker's prompt and nothing on HEAD
         ACCEPT     a fan-out re-sized or a slot re-handed costs zero HEAD amendments and zero
                    per-worktree carries; the eight addressing repairs of F6 become zero.
                    ⛔ THE MECHANISM IS NOT RULED HERE -- the brief calls binding-at-spawn "the
                    design question, not the answer", and this line grades the OUTCOME so L4 is
                    free to reach it another way.
                    BUT ONE CONSTRAINT ON THAT ANSWER IS ALREADY MEASURED AND L4 MUST NOT
                    REDISCOVER IT (brief P8): a worker's carry of an issuer's amendment is a
                    PATH-SCOPED CHECKOUT that copies CONTENT WITHOUT HISTORY, so a spawn-time
                    binding CANNOT be verified by `merge-base --is-ancestor` -- it reads CONTENT
                    or a RECORDED VINTAGE. This seat measured it from the other side today: the
                    issuer's amendment commit is NOT an ancestor of the worker's carry. A design
                    that verifies binding by ancestry WILL REFUSE THE ORDINARY DRAIN ON ITS FIRST
                    DAY, which is the exact failure a gate of this seat's was reverted for hours
                    earlier.

  FWD-6  A reader can see WHERE A ROUND'S COST WENT from one census
         DONE WHEN  EXERCISED -- run on a closed round and read by someone who did not run it
         ACCEPT     one command prints the cut / work / drain split with its DENOMINATOR, its
                    POPULATION and its CLOCK, and the issuance repairs listed BY CAUSE; two
                    rounds are comparable under it.
                    THE WORKED CASE IS F1'S OWN CORRECTION: the brief's first F1 carried neither
                    population nor clock, and FOUR HONEST READINGS OF THE SAME ROUND -- 71, 71,
                    86, 114 -- disagreed with it and with each other, every one correct for its
                    own scoping. A CENSUS WITHOUT ITS POPULATION AND CLOCK IS NOT COMPARABLE TO
                    ITSELF, let alone to the next round. That is the defect FWD-6 exists to end,
                    and the brief demonstrated it on itself while being written.

  FWD-7  A worker's first wall is the ISSUER's, and it is found BEFORE the worker exists
         DONE WHEN  EXERCISED -- an issuer runs it pre-spawn and reads a real refusal in its
                    own name
         ACCEPT     the issuer can run, on its own tree and before any spawn, the checks the
                    assignee's first commit will meet -- the grant against the paths its
                    invocations touch, the gates those paths trip, the proof stem, the flip
                    the drain needs -- and the output names the ISSUER's face
```

**FWD-1 and FWD-7 are not the same line.** FWD-1 is a REFUSAL at the neck: the issuance does not land. FWD-7
is a REHEARSAL the issuer runs earlier and iterates against, before an issuance commit exists at all. A
project could satisfy one and not the other, which is the test for whether two ids are two outcomes.

---

## THREE CANDIDATE EIGHTH IDS, TESTED AND REFUSED

A brief's outcome list is not automatically the endpoint's. Each of these was written out and then refused:

1. **"The L6 gate grades the six properties."** REFUSED — that is the MECHANISM of FWD-1, FWD-2 and FWD-3,
   and the brief's own boundary puts *where* a check lands (a gate limb, a `/dispatch` step, a derivation) at
   L4/L5. An endpoint that names the gate forecloses the design its own PRD is supposed to make.
2. **"A round's cost falls."** REFUSED — a CONSEQUENCE of FWD-1..FWD-7, and it would grade itself on other
   seats' behaviour over rounds this project does not run. Same reason the OUTSET endpoint refused "the
   deferral lifts": an outcome that grades on someone else's later act is not this project's to carry. FWD-6
   makes the cost VISIBLE, which is the part this project can own.
3. **"An assignee's first commit meets no refusal the issuer could have read."** REFUSED — that is **B1**, a
   qualitative BAR, and it states FWD-7 as an ABSENCE. An outcome phrased as "nothing bad happens" has no
   artifact and cannot be exercised; the bar belongs in the PRD's §4 where the brief put it.

---

## WHAT THIS ENDPOINT DELIBERATELY DOES NOT DECIDE

- **Where any check lands.** Gate limb, `/dispatch` step, or a derivation the issuer runs — L4's choice, and
  FWD-5's line says so explicitly for the one place the brief flagged a design fork.
- **Whether `<issued_to>` binds at spawn.** The brief names it as the question; the outcome is that
  re-seating costs nothing on HEAD, however that is reached.
- **Anything about CLDGRPH round 4's ten post-issuance L6 commits**, which the brief explicitly leaves
  unclassified (Part VII), and no hours-per-defect clock, which was never taken.

## AMENDMENT NOTE -- re-read against the brief's amendment BEFORE going to Andrew

The brief was amended at @`fd9b987a87` AFTER this endpoint was cut from @`b6c6e33060`. Re-read rather than
assumed: **confirming an endpoint built on a superseded brief is worse than a delay**, and his confirmation is
the one thing this project still waits on.

- **NO OUTCOME, BAR, BOUNDARY OR FINDING F2-F10 CHANGED.** The seven lines stand as cut.
- **F1 gained its POPULATION and CLOCK** (the project path, merges included, since the register row at
  15:00Z 09-04, read 14:0xZ) and now names the merge-carried thirteenth repair, so an auditor running
  `--no-merges` does not "correct" 13 to 12. FWD-6's ACCEPT is strengthened by it.
- **P8 was added** and is carried into FWD-5's line as a named constraint on L4's answer.

⭐ **AND THE ATTRIBUTION, because it is easy to get backwards:** the `13 / 44 / 15` that did not add up was in
the ANNOUNCING MESSAGE, not the brief -- the brief carried all eleven classes summing to 93. `2.0.0_SA_COO`
read the sentence, as any reader would, and was RIGHT to check it; two real imprecisions in the brief were
found because it did. **A SUMMARY THAT ABBREVIATES A CENSUS INHERITS NONE OF ITS DENOMINATOR AND CAN
CONTRADICT THE DOCUMENT IT SUMMARISES** -- which is FWD-6's own subject, arriving one layer up.

## THE STANDING ITEM THIS PROJECT'S PRD WILL CARRY

If its decomposition seats worker subagents, the PRD carries the worker-ambient-credentials item now mandatory
in `docs/architecture/_PRD_TEMPLATE.md` §6 (Andrew-direct 2026-09-05 "recs approved", @`8e89f1127f`,
carrier landed @`58adeff90c`). Named here so L4 does not have to rediscover it.

## NEXT

Andrew confirms these seven DONE WHEN lines. From L3 onward the loop cycles on its own: register under the
tree, the PRD at L4 with these outcomes verbatim, and the L4 notifier hands it to `2.0.0_SA_COO` for L5.
