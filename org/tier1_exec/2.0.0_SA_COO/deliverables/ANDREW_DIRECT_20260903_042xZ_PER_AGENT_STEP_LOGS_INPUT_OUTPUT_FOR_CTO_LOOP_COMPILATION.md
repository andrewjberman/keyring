# ANDREW-DIRECT 2026-09-03 ~04:2xZ -- once the loop is done end to end, every involved agent writes a step-by-step INPUT/OUTPUT log; CTO compiles them into a four-quadrant read of the loop

**Channel:** Andrew, in person, at the `2.0.0_SA_COO` (base, laptop) terminal, ~04:2xZ, after this seat's report that
round 1 of `NFRA_COMPEFFICACY` is held at L9/L10. **Recorded by:** `2.0.0_SA_COO` (session
`af7a2a30-0946-4127-83c9-871c7ac970cb`). **Broadcast** same turn to `1.0.0_SA_CTO`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`,
`0.8.0_AE_CloudComp` (and `4.0.0_SA_CRO`, queued).

## VERBATIM AND ENTIRE

> What we need to do is all agents who were involved in this process, once its done end to end is basically take a /log
> that is structured step by step with what they did on an input/output basis, with the goal of essnetially having CTO
> being able to compile these logs and see where the loop executed efficiently according to the plan, where it failed
> to act efficiently while following the plan (opportunities to improve plan), where it executed efficiently outside of
> the explicit plan (potential improvement to plan or allowed flexibility), and where it failed by not following the
> plan (gate candidate).

## What it binds (readings, marked)

1. **WHO:** every agent that acted in the process -- for the `NFRA_COMPEFFICACY` water test that is `4.0.0_SA_CRO` (L1,
   the brief, pre-reboot), `1.0.0_SA_CTO` (L2-L4, and the L4 landings after the withdrawals), `2.0.0_SA_COO` (L5-L6, the
   corrections, the lane grants), `0.8.0_AE_CloudComp` (L7, the one worker), `3.0.0_SA_CVO` (L8-L9, the stamp at L10),
   `0.0.0_AB_MSTR` (the integrator's windows and the relays of his words). A seat that acted only by relay logs the
   relay as a step.
2. **WHEN:** *"once its done end to end"*. READING, marked: the first end-to-end pass is round 1 stamped at L10 (the
   loop's first full cycle L1-L10 on this project); each seat writes its step log then, not before, and again at each
   later L10 stamp if he wants the read per round. If he meant the whole project closed, the logs are later; the shape
   is the same.
3. **WHAT -- the form:** a `/log` structured STEP BY STEP on an INPUT/OUTPUT basis: for each act the seat performed,
   the limb (or "outside the limbs"), the input it acted on (artifact + hash or message id), the output it produced
   (artifact + hash or message id), and the time in/out. It is a record of what was done, not an assessment -- the
   assessment is CTO's compilation.
4. **WHY -- the compilation, CTO's:** the compiled logs are read into FOUR quadrants, his words:
   | | followed the plan | outside the explicit plan |
   |---|---|---|
   | **efficient** | executed efficiently according to the plan | executed efficiently outside the plan -> potential plan improvement, or allowed flexibility |
   | **inefficient / failed** | failed to act efficiently while following the plan -> opportunity to improve the plan | failed by NOT following the plan -> **gate candidate** |
   The plan is the spine (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`, state of record @`716a9bc7ce`).
5. **THE SCHEMA IS CTO'S TO FIX** (the compiler owns the shape it compiles against). PROPOSED, not imposed, so six
   seats write one shape -- one row per act:
   `step_id | limb (L1..L10 | X) | actor | started_at | ended_at | input (artifact@hash | msg-id) | output (artifact@hash | msg-id) | plan_clause (the spine sentence followed, or NONE) | note (one line, what happened)`
   plus the existing /log sections (archetype, Compiler Tools, Current State). The seat does NOT self-assign a quadrant;
   CTO does. If CTO fixes a different shape before the L10 stamp, that shape governs.
6. This does not change the standing mode (`/drive` OFF, zero crons), does not open a new round, and asks nothing of
   any worker before round 1's L10 stamp.

## NOT read into it

- Not an approval gate on the L10 stamp or on the next L6 round; the logs follow completion, they do not gate it.
- Not a new log every turn: one step log per seat per end-to-end pass.
- Not a change to `org/ref/SESSION_LOG_STANDARD.md` by this seat; if the step-log form is to live there, that edit is
  CTO's with the schema.
