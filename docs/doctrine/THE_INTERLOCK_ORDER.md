# THE INTERLOCK ORDER

**A CORRECT FIX, APPLIED BEFORE THE HAZARD IT UNCOVERS IS CLOSED, CONVERTS A LOUD REFUSAL INTO A
SILENT SHIP. THE DEFECT IS NEVER THE REPAIR -- IT IS THE ORDER.**

Before you remove a thing that is failing, ask: **WHAT IS THIS FAILURE CURRENTLY PREVENTING?**
If the answer is *"a broken artifact from shipping"*, the failure is an **INTERLOCK**, and removing it
is the second half of a two-part act whose first half is closing the hazard.

---

## The mechanism, which is why care does not catch it

A blocking failure is **indistinguishable in the log from a defect**. It reads as broken because it
*is* broken. So the reflex -- fix what is failing -- is correct in isolation and wrong in sequence,
and **every gate, review and test agrees with the reflex**, because each one is scoped to the thing
being repaired and none is scoped to what its failure was holding back.

Three properties make it invisible rather than merely subtle:

1. **THE INTERLOCK IS USUALLY ACCIDENTAL.** Nobody designed it, nobody documented it, and nothing
   names it as load-bearing. It protects by side effect.
2. **THE REPAIR IS GENUINELY CORRECT.** There is no version of this where the fix was a mistake, which
   is why "be more careful" is not the remedy and why the repairing seat is not at fault.
3. **THE MET HALF EMITS A SUCCESS SIGNAL THAT OCCUPIES THE UNMET HALF'S CHANNEL.** After the repair,
   the place where a loud refusal used to appear now prints a confident green line. **A gate's green
   is read as proportional to its PERCEIVED scope, not its actual one** -- so the next person is not
   merely missing a warning, they are handed a reassurance standing exactly where the refusal stood.

⛔ **COROLLARY ON TWO-CONJUNCT ORACLES: A PARTIAL SATISFACTION IS NOT PARTIAL SAFETY.** An oracle of
the form *"X AND Y"* can be half-met, and when the unmet conjunct is the one that was failing loud,
meeting the other one **removes the signal and keeps the hazard**. Report such a cell as
`X: PASS / Y: NOT MET` -- never as progress, never as a satisfied cell.

## The sharpest form: a protection indistinguishable from a defect

Once an interlock is recognised and deliberately *kept*, it becomes something worse than an accident:
**a protection that looks exactly like a bug.** It will be removed -- not by carelessness, but by a
competent person doing something that looks obviously correct, in a one-line commit that passes every
gate and reads as hygiene in the log.

**A DELIBERATELY-KEPT INTERLOCK MUST CARRY ITS OWN EXPLANATION ON THE ARTIFACT THE BREAKER WILL HAVE
OPEN.** Not in a ruling, not in a commit message, not in a thread: a commit message is not consulted
before an edit. The note states that the state is deliberate, cites the ruling, names the disarm
condition, **names the remedy the reader will otherwise reach for as the forbidden act**, and
instructs its own deletion in the commit that lifts the hazard. *A tripwire that outlives its hazard
becomes the next reader's confusion.*

⚠ **AND WATCH WHERE THE REFUSAL POINTS.** A refusal that "names its own fix" may name the *sanctioned
workaround* while the reader's eye goes to the *underlying default*. Those are different acts and only
one of them is safe.

## Inventory, not instance

**"THE INTERLOCK IS GONE" IS A CLAIM ABOUT A SET.** Finding one barrier and confirming its removal
does not license it. **Enumerate the barriers, print the count, and label what is NOT one** -- the
hazard itself is not a barrier, and the currently-safe deployed state is not a barrier.
**Then ask which remaining members expire without a decision.** An interlock that dissolves under
ordinary operation -- an unpushed commit, an unrenewed credential, a queue that drains -- is weaker
than one that requires a deliberate act, and **the risk must be priced against what remains after the
normal flow runs, not against today's count.**

## What this doctrine is NOT

- **NOT an argument for leaving broken things broken.** Repairing an accidental interlock is correct
  work and the estate needs it. The obligation is to close the hazard first, or to keep the interlock
  *deliberately and visibly* until it can be.
- **NOT a licence to manufacture gates.** Declining to CHANGE a default is not a gate -- nothing new
  blocks anyone. **Adding a refusal, a check, or an approval step IS**, and that requires Andrew's
  explicit word (CLAUDE.md). The distinction is whether a NEW affordance can now block work.
- **NOT applicable when the failure prevents nothing.** Most broken things are just broken. The
  question costs one sentence at the moment of repair; asking it of every fix is waste, and asking it
  of a fix whose failure mode is a crash with no artifact is answered immediately.

**COST: one question, asked once, by the person doing the repair.** *What is this failure currently
preventing?* If the answer is "nothing", proceed and do not think about it again.

## Measured instances

Three in six hours across three seats, 2026-08-25/26. **A class that recurs three times in one night
is a missing sequencing rule, not three incidents.** Records, not retold here:

| # | subject | record |
|---|---|---|
| 1 | D1_CATVIEWS packaging remediation predicted in advance | ruling ~21:14Z; `org/tier1_exec/1.0.0_SA_CTO/deliverables/ORPHANED_BY_THE_MSTR_COO_CVO_CLOSE_20260825.md` s9 |
| 2 | the packaging fix removing the accidental import barrier | msg 72058 (surfaced), 72063 (disarmed + ruled), record s9 @`63c60c65d5` |
| 3 | the builder's pin default as the last standing interlock | ruling @`db9ab86c32`, record s10 |

**Interlock inventory for that hazard at 2026-08-26T03:44Z: 2 of 3 standing** -- packaging REMOVED,
pin default STANDING, push state STANDING **but self-expiring on the next ordinary integration.**

## Provenance

Named by `1.0.0_SA_CTO` after ruling the class twice in one night. The **three-instances-is-a-missing-rule**
framing and the **inventory-not-instance** discipline are `3.0.0_SA_CVO`'s (72084), reached by
correcting their own one-member generalisation. The **success-signal-occupies-the-channel** property
and the **protection-indistinguishable-from-a-defect** argument are `0.5.0_AE_OpalETL~B`'s (72073,
72078). The **order, not the repair** formulation is `2.0.0_SA_COO`'s (72063).
