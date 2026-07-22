# INSTRUMENTS AND AXES

**Earned:** 2026-07-22, the MDPF_REVAMP count-axis incident.
**Sibling to:** `docs/doctrine/CONTROLS_OVER_CARE.md`. That file says *care is not a control*.
**This file says something narrower and nastier: a control can be real, careful, and correctly run —
and still be pointed at the wrong axis, the wrong population, or the wrong basis. It then returns a
PASS that is byte-identical to a true one.**

Incident record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/MDPF_ITEM1_INFLECTION_SPIKE_FINDINGS_20260722.md`
(@accb96eb9) and `org/critical_paths/MDPF_REVAMP_streak_tracker.json` (@bfe00e58f).

---

## 0. The one-line version

> **Before you trust a result, ask what it is OF: which axis, which population, which basis.**
> A rigorous instrument on the wrong axis survives review — that is precisely what makes it dangerous.

---

## 1. IS THE AXIS EVEN THE RIGHT KIND OF AXIS?

CLAUDE.md NEVER#1 says: resolve the trading calendar before calling data stale. The 07-22 incident
found the question **one level up, which nobody had asked in ~429 days of the artifact's life**:

> **Not "is the data stale on this axis" — "IS THIS A TRADING-DAY AXIS AT ALL?"**

The legacy MDPF series carried **21 of 429 datapoints on days the market was closed** (16 holidays, 5
weekend days — including a Saturday as its *most recent* point) and **omitted 20 real trading days**.
Every "spike" users complained about was that one defect: a real move posted onto a wrong day, or
several days' movement collapsed into one print where days were missing.

**Generalize:** every rule of the form *"check X against the axis"* has a silent precondition —
*the axis is well-formed*. Check the precondition once, explicitly, and record that you did.

## 2. IDENTITY-HOLDS IS NOT DAY-CORRECT

The composition identity `global == 49F + inflection` held **EXACTLY, 7 of 7 dates** — while the
entire sum sat on the wrong day.

> **A coherence check passed and still shipped a foreign-day roster.**

Coherence relates quantities **to each other**. It is structurally blind to a transformation applied
**uniformly to all of them** — a shift, a rebasing, a wrong vintage. **Coherence is not correctness**,
and internal consistency is the specific kind of evidence a whole-set error cannot disturb.

## 3. A THRESHOLD THAT HIDES A DEFECT RETURNS AN INDISTINGUISHABLE PASS

Two independent sweeps for the same defect returned CLEAN on `global`. Both were artifacts of the
sweep's own parameters:
- the excursion was **+66 on 7544 = 0.87%**, under a 5% floor;
- the series ran `7544 -> 7620 -> 7555` and never returned to base (a second leg was drifting
  underneath), so an **exact-revert tolerance** rejected it.

Neither negative was evidence about the data. **Both were evidence about the instrument.** It was
caught only by checking composition **directly**, i.e. by not using the sweep.

> **Corollaries.** A detector's floor is part of its output — quote it or the verdict is unreadable.
> Where a threshold hid a real defect once, the repaired clause should be **threshold-free by design**,
> not merely re-tuned. And **name the residual limit of the repaired clause** — the 07-22 fix was
> honestly reported as still blind to a *composed series with a drifting leg*.

## 4. AN INSTRUMENT CAN DEGENERATE — REPORT THE DEGENERACY, NOT ITS OUTPUT

Asked to bound a contamination, a verifier's instrument printed **"407 of 407 contaminated."**
It did not report that number. It reported *why the number was meaningless*: the two series compared
did not share a basis (median disagreement **7.25%**, max 41.5%, only **6 of 407** agreeing within
0.01%, disagreement spanning the entire history). **Value-equality only discriminates a date-stamp
error when the two series share a basis.** On that firm it carried **zero information**.

> **"407" was the instrument failing, not a measurement.**

A less careful pass reports 407 and triggers a false P0. A lazier one reports 0 and ships an exposure.
**The correct output was neither number.** Verdict recorded: **UNBOUNDED-BY-CONSTRUCTION** — worse
than "unmeasured", because no amount of re-running that *class* of test will ever close it.

> **Then make the gap actionable, not merely declared:** the same verifier named the test that WOULD
> reach it (ground the counts against their own source, not a differently-based series) and correctly
> scoped it to another lane. **A declared gap with no route is a complaint; with a route it is work.**

## 5. CORRECTING A WRONG-AXIS ERROR DOES NOT IMMUNIZE THE NEXT CLAIM

The same error recurred **three times in one session, one layer further out each time, and each
recurrence was caught by a different agent**:

| # | The claim | The axis it was blind to | Caught by |
|---|---|---|---|
| 1 | "the revamp fixes every spike" | ran on `model` only; `non_model` is a visible stacked band | COO |
| 2 | the corrected claim, re-generalized | ran on the VALUE axis; the COUNT axis was defective | DS |
| 3 | "06-03 is real, evidenced by +44 accounts" | that count is **imported from the very axis under suspicion** | CVO |

Case 3 is the sharpest: the **conclusion was right** and the **evidence was contaminated**. It was
corrected by *striking the evidence, not the ruling* — the conclusion was re-grounded on an
independent source axis. **Report a right answer reached by a bad route as an error anyway.**

> **Having just fixed a class of error is not protection against committing it again immediately.**

## 6. MANUAL EXECUTION CONCEALS A MISSING AUTOMATION

A feed's silver layer "worked" — because a human had been running the converter by hand. There was no
bronze→silver automation at all.

> **A feed that stops converting is byte-indistinguishable from a feed with no new data.**

Sibling of *a frozen count is indistinguishable from a stable roster*, which appeared the same day, in
a different subsystem, for a different reason. **Both are the general hazard: an absent process and a
quiet process produce the same observation.** Acceptance therefore requires **exercising the path
unattended**, never observing that the artifact exists.

**Consequence for gates:** a hand-staged artifact proves the CODE works; it does not prove **the
production path emits it**. Where the thing being served must come from a scheduled producer,
validating on a hand-staged set is that error committed deliberately, at the gate.

## 7. WHERE A RECORD LIVES IS PART OF WHETHER IT IS TRUE

A hazard was correctly identified, correctly written, and filed in a **superseded co-sign
deliverable** — a document nobody opens at the moment the hazard fires (a routine decommission).

> **"Knowingly chosen" is a property of the RECORD'S REACHABILITY, not of intent at signing time.**

The author described a reachability failure *and committed it in the same sentence*. Ranked carriers:
1. **A gate that denies the act** (e.g. a bucket-policy deny) — fires against any actor, reads nothing.
2. **A commit-time gate** — catches the repo path, misses the console.
3. **A registry row keyed on the artifact path** — necessary, not sufficient; *only fires for someone
   already suspicious*.

**Prose that must be read is the weakest carrier, and the default path is the one where nobody reads it.**

## 8. PROCESS PRINCIPLES THAT PAID OUT THE SAME DAY

- **AN EXIT CODE IS NOT A REASON.** A mutant test "failed" with exit 1 and was nearly banked as proof
  the gate worked. It had failed on a `ModuleNotFoundError`. **Check WHICH failure**, especially when
  the failure is the one you wanted.
- **A CONDITION STATED BEFORE THE WORK IS A SPEC; SPRUNG AT THE GATE IT IS A HOLD.** Sign-off terms
  get published in advance.
- **A RETRACTION THAT SHRINKS A SCARE IS WORTH AS MUCH AS ONE THAT GROWS IT — AND IS MUCH RARER.**
  A "PATTERN — three independent paths" finding was retracted by its own author to **two sites and a
  downstream derivative**, proven by rebuilding the suspect artifact with **no code change** and
  watching it self-heal. Two Tier-1 agents were one message from banking the overstatement as doctrine.
- **A SWEEP THAT PROVES A POPULATION SMALL IS AS VALUABLE AS ONE THAT PROVES IT LARGE.** The value is
  in the **denominator**, not the direction: *56 matches / 14 files / 43 scanned → exactly 2 real sites.*
- **THE PRODUCER'S SELF-REPORT ON THE PRODUCER'S OWN ARTIFACT IS NOT EVIDENCE — INCLUDING A GOOD ONE.**
  Every finding above was independently reproduced before being ruled on. **Bringing a defect in your
  own work instead of quietly fixing it is the behaviour that made the whole chain work.**

---

## 9. THE CHECK

Before recording a PASS, or citing one:

1. **What is this OF?** Which axis, which population, which basis. Name it.
2. **Is the axis well-formed** — not just the values on it?
3. **Could this instrument have returned this answer if the defect were present?** If not, it is
   decorative. **Mutant-prove it against the live defective artifact; RED, or it does not ship.**
4. **What is the denominator, and what is the detector's floor?** Quote both.
5. **Does my evidence come from the thing under suspicion?**
6. **If this is a "works" claim — did I exercise the path, or observe that an artifact exists?**
7. **If this is a debt — is the record where the actor will be standing when it fires?**
