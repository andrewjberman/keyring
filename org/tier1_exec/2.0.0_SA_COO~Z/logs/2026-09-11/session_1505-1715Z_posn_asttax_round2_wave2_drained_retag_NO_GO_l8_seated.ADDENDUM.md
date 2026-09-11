# ADDENDUM -- I asserted a measured absence that was wrong, and two seats moved on it

**archetype:** DIAGNOSE
**Date:** 2026-09-11, ~17:2x-17:3xZ (after the parent log was committed at `cbf8c145fc`)
**Parent:** `session_1505-1715Z_posn_asttax_round2_wave2_drained_retag_NO_GO_l8_seated.md`
**Status:** correction landed; nothing in the parent log's WORK is affected

> **THE PARENT LOG IS NOT CONTAMINATED.** It was written before this exchange and contains no claim
> about an L10 refuser. Every commit, drain, row and disposition it records stands. What follows is a
> separate error made in MESSAGES after it was committed.

---

## What I claimed, and what was true

`1.0.0_SA_CTO~Z` (msg 21487) raised whether two deliberately-undispatched orders block round 2's close,
and named the one read that would settle it: does anything MECHANICALLY refuse an L10 close on a
non-terminal order? It said it had not run that read. I ran it and reported **no refuser exists** (21488)
-- to the CTO and the CVO, as a measured fact.

**It was wrong.** The refuser exists:
`.tools/surprise-row-gate.py` `_route_precondition_violations` (:774-809) with `_open_tos_for_project`
(:744), refusing a new remediation row while any task order under the project is non-terminal at HEAD,
citing **Andrew-direct LD-0521, @716a9bc7ce call 3: "We do not route until the job is over."**
Confirmed at source by this seat rather than accepted on the correcting seat's report.

## The error, precisely -- it is a reusable shape and that is why it is written down

```
  comp-find 'L10' --all        ->  4117 hit(s) across 56221 file(s)      <- printed, and persuasive
  reasoned: "only a DEFINITION line can hold a refuser"
  comp-find 'L10' --all --band DEF  ->  5 hits, 3 of them rendered HTML
  concluded: NO REFUSER EXISTS
```
⛔ **`.tools/surprise-row-gate.py` contains "L10" TWENTY-EIGHT times. It was inside my 4117. My own band
filter discarded it.** A refuser is a `return [...]` inside a predicate -- CODE, never DEF -- so the
filter excluded the only band it could occupy. I had opened and `--self-test`ed that exact file three
times earlier in the same session.

**A BAND FILTER IS A HYPOTHESIS ABOUT WHERE THE ANSWER LIVES, AND IT IS PART OF THE CLAIM.** I printed a
four-figure denominator and acted on five hits. The denominator is what made it look thorough -- to me
first, then to a second seat. CLAUDE.md states this exact rule and I did the opposite of it: *an unscoped
read only falsifies a domain if you then INSPECT what it found outside it.*

**Absence claims propagate furthest.** "No gate exists" licensed a second inference -- "so the absence is
deliberate and nobody should build one" -- which `1.0.0_SA_CTO~Z` adopted and which was wrong in a SAFETY
direction. It also caused that seat to withdraw a testable alternative of its own on my evidence.

⭐ **The method that worked was not mine.** `3.0.0_SA_CVO~Z` went at the BEHAVIOUR -- *what refuses a
remediation row* -- and opened the gate that does it. A concept census finds a concept; it does not find
an implementation, and here it did not even need to, because the file DID spell the concept and my filter
removed it anyway. Banked as `a-band-filter-discarded-the-answer-my-own-census-found`; the false memory I
had already written was DELETED rather than amended.

## What I added afterwards, measured at the call site

Offered because the function's own docstring would have misled a reader a second time. It says the limb
is "for ONE new tree row carrying a ROUTE". **The production call site (:1303-1315) governs and says
otherwise:**
- `kind == "REMEDIATION" and folder_kind == "REMEDIATION"` -> fires on **EVERY new remediation row**,
  route-carrying or not (the call-site comment corrects the docstring in terms: *"spine v3.0 L10 carrier
  6 ... not only to a route-carrying one"*).
- **OR** an INVESTIGATION row with `disposition == "DECOMP_INVALIDATING"`, in an INVESTIGATION **or
  ADJUDICATION** folder -- "waits the same way".
- Otherwise the limb does not run.

**So the round is not frozen; only the routing act is.** L8 compile and ordinary L9 adjudication are not
gated. ⚠ The live trap, flagged to the CVO: a `DECOMP_INVALIDATING` disposition trips the same gate from
inside the adjudication plane, and this round's findings make that a plausible disposition to reach for
-- it would refuse in the middle of L9 rather than at the slug. The twin limb
`_investigations_precondition_violations` (:704) fires on the same trigger and additionally requires every
investigation item dispositioned.

## Where the round now stands

A **RESERVED card at Andrew**, raised by `1.0.0_SA_CTO~Z` and pitched to `3.0.0_SA_CVO~Z` for
classification review. The bind: the gate refuses the slug; the two cells must not run (TO-S7-1's NO-GO
is measured); flipping them terminal is the denominator-shrink all three seats refuse; and the audited
`# surprise-row-override:` is **not ours to take** -- the precondition is Andrew's word, and overriding it
would convert his word by agent judgment, which CLAUDE.md forbids. My own row `Z-S1` measured that escape
as all-or-nothing (6 suppressed, 1 explained).

**My positions that still stand, unchanged:** the cut (S2-1/S3-1 not dispatched), the refusal to flip them
terminal, and the issuance-coverage evidence (same commit `f60de462ae`, `fanout: 3 of 3`, 7 declared MINUS
7 covered = 0 uncovered). Only the "no refuser" claim falls, and it falls entirely.

**One route I named and do not own:** `TERMINAL_TO_WORDS` includes `superseded`. My objection was never to
the vocabulary but to a terminal status *without a real pointer*. If the CTO's round-2 analysis produces a
genuine successor for S2-1 and S3-1 to point AT, `superseded` becomes honest and the bind dissolves with
nobody shrinking anything. That is the L10 owner's call.
