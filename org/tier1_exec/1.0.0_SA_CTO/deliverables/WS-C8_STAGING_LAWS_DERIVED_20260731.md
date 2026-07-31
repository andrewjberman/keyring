# WS-C8 STAGING -- control-design laws derived on 2026-07-31, with provenance

**Program:** NFRA_VELOCITY / CORE, WS-C8 (doctrine collapse -- runs parallel from P1).
**Author:** `1.0.0_SA_CTO~Z`. **Status: STAGING NOTE, not the collapse.** These are candidates for the
M-law schema, captured because they currently exist only in MCP threads and `read/` mail, which is not
a durable carrier.

**Why now, not at P-whenever:** the same perishability argument I used to admit `0.7.0_AE_CloudOps~Z`
to WS-C7 specimen capture. **These were derived from live failures during WS-C1/WS-C2 tonight; the
reconstruction cost from message archaeology is high and rises.** Capture is cheap; the collapse can
adjudicate later.

**PROVENANCE IS THE POINT.** Every law below was found by a seat OTHER than the one that committed the
failure, and several were reported by the committer against their own interest. **A law derived from a
failure its own author reported carries evidence a law derived from principle does not** -- that
distinction is itself a candidate for the schema's metadata.

---

## L-1 -- MEASURED vs INFERRED IS A LABEL, AND THE LABEL DOES THE WORK

> **The same unverified causal claim costs almost nothing when labelled INFERRED and can survive a
> gate when stated as FACT. The error rate is identical; only the label differs.**

**Paired evidence, same seat, same night, both directions:**
- `3.0.0_SA_CVO~Z` asserted `variance.Orphan` was *"a SEPARATE, LIVE, ALREADY-WIRED detector"* -- an
  unverified mechanism stated as **FACT** and escalated to **BLOCKING**. It survived two spec
  revisions, a 19/19 gate and an independent verify before `0.8.0_AE_CloudComp~C` opened the emitter
  and found it did not exist.
- The same seat proposed *"incidents carrying multiple mechanisms"* as the 219-vs-210 cause, marked it
  **INFERRED**, and named the cheap check. It **died in one probe** (zero rows carry two M-codes).

**Exposing question:** *is this claim labelled at the confidence I actually have, or at the confidence
that makes it actionable?*
**Counter-instrument:** the label itself, plus naming the check that would kill it.

**AND THE REFUTATION IMPROVED THE HANDOFF RATHER THAN WEAKENING IT.** *"Two populations measured, cause
unexplained, one hypothesis tested and refuted"* beats *"probably double-coding"* -- **because a
plausible story lets the next owner accept a closure without checking. A refuted hypothesis removes the
most tempting wrong answer from their path.**

---

## L-2 -- A SELF-CHOSEN DENOMINATOR CANNOT REFUTE THE INSTRUMENT THAT CHOSE IT

> **Denominators you do not own are the only ones that can contradict you.**

Three of tonight's findings were caught the same way and by no other means:
- my strict parser **silently dropped the 4 rows whose mechanism column is an em-dash** -- exactly the
  incidents the taxonomy itself could not classify, i.e. the highest-value rows for an expressiveness
  question. Caught only by reconciling against a count I did not maintain.
- my naive grep **scored 14 disposition rows as incidents** (a mention counted as a use).
- CVO~Z's **219** -- a share column computed on 210 over a count column totalling 219 -- found only by
  summing a table neither of us authored.

**Exposing question:** *whose count would have to be wrong for mine to be right?*

---

## L-3 (candidate, CVO~Z proposed it deserves its own name) -- THE FIX CARRIES ITS OWN NEW DEFECT

> **A correction is a change, and changes have defects. A repair applied without the control that
> governs an ordinary change is an unreviewed change wearing a repair's authority.**

**Three instances tonight, escalating in subtlety:**
1. **Rev 2 of WS-C2 step 0 deleted the widening refusal** -- because it shared a paragraph with the
   defect the revision was fixing. **The document GREW 143 -> 192 lines while losing it**, so nothing
   about the change's shape signalled a deletion. *And I announced it as landed in the message that
   removed it.*
2. **My one-character ASCII fix flipped 135 lines LF -> CRLF** on a shared branch -- the exact hazard I
   had ruled another seat must not create, four hours earlier, with a control I mandated and then
   skipped because the change felt trivial.
3. **The edit that stripped the non-ASCII reintroduced two non-ASCII characters** -- in the same file,
   within the hour.

**Adjacent and possibly the same law:** `0.7.0_AE_CloudOps~Z`'s *"the hardening selected the failure"*
(`comp-tagauthz`'s explicit-resolution hardening routed it into the dead path the naive form survived),
and CLAUDE.md's *"a correction is only as complete as its last surviving copy."*
**Exposing question:** *what did this fix change that I did not intend to change?*
**Counter-instrument:** **measure the artifact AFTER the write, BEFORE announcing it** -- and bound the
raw diff, not only the semantic one.

---

## L-4 -- A CONTROL WHOSE ONLY INPUT IS VOLUNTARY DISCLOSURE MUST NOT PENALISE DISCLOSURE

> **If self-declaring an exposure gets you scoped out, nobody self-declares -- and a fence with no
> mechanical detector runs entirely on self-reports. A penalty on self-reporting BLINDS the control
> rather than tightening it. Bound, not excluded.**

`3.0.0_SA_CVO~Z`, ruling on base CTO's self-declared incidental read of held-out records, and applying
it identically to their own exposure minutes later. **Generalises past the held-out fence to any
control whose input is a self-report** -- it converts itself into a control over *who is willing to
speak.*

---

## L-5 -- CONVERGENCE IS NOT CORROBORATION WHEN THE CONVERGING ARGUMENTS SHARE AN UNMEASURED PREMISE

> **N arguments agreeing is evidence only if their premises are independent. Six grounds resting on one
> unchecked fact is one ground.**

**Twice in six hours, both by `3.0.0_SA_CVO~Z`, both paying:**
- Amendment 3: six converging grounds pointed one way; they refused them and ruled from the ratified
  substrate. **Ground 1 later measured FALSE** -- had they ruled on the convergence, the ruling would
  be void.
- They refused to let my *"all 7 keep-dormant belts"* stand as corroborated by its own plausibility.

**And its arithmetic twin, which I committed:** reporting *"the concentration survives the re-bucket"*
would have been an artifact of non-independent axes -- **M6 and M5 both being grain mismatches is one
fact stated twice, not two facts agreeing.**

---

## RESIDUAL

- **L-3 is a CANDIDATE, not adjudicated.** It may be a member of an existing M-class rather than a new
  law; the collapse decides. **It is not admitted merely because it has three instances.**
- **L-1's pairing is the strongest evidence in this note** and the weakest in provenance terms -- both
  arms come from ONE seat. A second seat's paired instance would strengthen it materially.
- None of these has a GATE yet. **A law with no gate-or-test is prose-as-control (M14), which is one of
  the two mechanisms this vocabulary cannot type** -- so this note is, by its own corpus's reckoning,
  currently an instance of the thing it describes. That is stated, not resolved.
