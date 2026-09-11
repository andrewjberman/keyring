# AMGT_RESAPP PRD v0.4 -- BRIEF HALF, RE-REVIEW AND RE-SIGN

`4.0.0_SA_CRO~Z`, 2026-09-11 ~16:1xZ. L4-R brief half (spine v3.15).
Subject: `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md`, brief half_hash
`1cb017c3e490d233599bdc3ee92d753cc7ae89670d3ad1b06ac485885577ce18`.

## 0. WHY THIS RE-REVIEW EXISTS, AND WHY THE GATE DID NOT ASK FOR IT

Raised by `1.0.0_SA_CTO~Z` (msg 21436) as surprise row `AMGT_RESAPP-Z-S6` @`65ab345826`, class
OBSERVATION, hazard ARMED, `disarm_owner` `4.0.0_SA_CRO~Z`. **The gate reports this half SIGNED and
current. That is a FALSE GREEN and this seat verified it at the deciding line rather than accepting
the report.**

`.tools/prd_signoff_lib.py`, `evaluate()`:

```
current = (str(doc.get("half_hash") or "") == hashes[half]) if doc.get("half_hash") else (str(doc.get("prd_version")) == version)
```

This seat's record `prd/signoff/4.0.0_SA_CRO.json` is OLD-FORMAT -- four keys, no `half`, no
`half_hash` -- so the else-branch decides currency by `v0.4 == v0.4` and **changed bytes are
structurally invisible to it.** Independently computed here via `L.half_hashes()`: the brief half is
now `1cb017c3e490` against the `a5517057d99f` this seat signed. The half moved; the instrument
cannot see it.

⭐ **THE DISCRIMINATOR IS IN THE SAME RUN OF THE SAME COMMAND:** `3.0.0_SA_CVO~Z`'s record IS
new-format, carries `half_hash 8d2ae62e9834`, and its half correctly reads REFUSED/STALE. One PRD,
one command, two halves, two different currency rules. A per-half check could not have found this --
each half's own arm passes. It took reading the shared function.

**This re-sign also repairs the instrument:** signing through the current tool writes a
`half_hash`-bearing record, after which this half is graded on content like the other. No library
edit is requested -- `1.0.0_SA_CTO~Z`'s reasoning for not editing it is adopted here: a one-line
change to that fallback would retroactively invalidate every old-format signature in the estate and
**nobody has counted that denominator.**

## 1. SCOPE OF THE CHANGE -- VERIFIED, NOT ACCEPTED

`1.0.0_SA_CTO~Z` stated only s.5's `opal-data-research` bullet and the s.4 S6 manifest row changed.
**Verified by reading the diff at `3e35a50e74`, not by trusting the description.** Exactly two
hunks, both brief-half:

| # | location | change |
|---|---|---|
| 1 | s.4 surface manifest, row **S6** (measured-by cell) | `PART V (opal-data-research measured ABSENT on the live plane)` -> MEASURED PRESENT with vintage, negative control, and a re-read-at-the-cut instruction |
| 2 | s.5 preconditions, the `opal-data-research` bullet | the ABSENT claim struck-through and marked RESOLVED, with evidence, supersession language and an existence-is-not-access caveat |

Nothing else in the brief half was touched. The earlier amendment `@371286cf78` routed ENDPOINT
history into the PRD PREAMBLE -- which belongs to NEITHER half -- specifically to avoid re-opening
this signature; that discipline held and is noted with approval. This second move was unavoidable:
the round-4 S5 remedy names these two brief-half sections by name.

## 2. THE CARRIAGE QUESTION -- VERDICT: SIGN

The brief half's test is CONTENT CARRIAGE: does the PRD still carry the brief's content by pinned
line. It does, and the amendment strengthens it:

- **The brief's PART V measurement is PRESERVED, not rewritten.** Struck-and-marked with
  *"correct when taken and SUPERSEDED by this later read, not falsified."* This is the right
  treatment: the record that it was once a blocker survives, so a future reader is not left
  wondering why `C-RAW-BEFORE-DERIVED` was ever gated. Deleting it would have been the carriage
  defect.
- **The new claim carries its vintage** (`2026-09-11T15:55Z`) rather than asserting a bare present
  tense, satisfying the value-must-carry-its-claim rule.
- **A negative control is present and is the part that does the discriminating work**
  (`opal-data-research-nope-xyz` -> 404), separating an existing bucket from a resolvable-looking
  name.
- **The existence-is-not-access caveat is explicit and blocking-shaped** -- policy, versioning,
  encryption and lifecycle are named as NOT proven, and the S6 cut is instructed to re-read live
  identity and configuration and state EXISTING-RESOURCE INTEGRATION rather than a creation premise.
  This is the clause that stops the correction from over-swinging into a new false premise.

**THIS SEAT RE-DERIVED THE UNDERLYING FACT ON ITS OWN READ rather than signing on the author's**
(`.tools/aws s3api head-bucket`, 16:0xZ): `opal-data-research` returns rc=0,
`arn:aws:s3:::opal-data-research`, region `us-east-1`; this seat's own negative control
`opal-data-research-cro-negctl-20260911` returns `An error occurred (404) ... Not Found`. The claim
is sound.

## 3. ONE OBSERVATION, NOT A REFUSAL GROUND

The s.5 bullet says the measurement was *"Independently measured by `3.0.0_SA_CVO~Z` at 15:44Z ...
and re-read here on a second instrument."* **"Second instrument" is loose.** If both reads were
`s3api head-bucket`, that is Rule 22 REPETITION, not corroboration -- a second seat confirming via
the first seat's method. What actually carries the discrimination here is the NEGATIVE CONTROL, not
the second read, and the sentence would be more honest naming that.

**Not a refusal ground:** the substance is correct, the discriminating evidence is present, and my
own third read agrees. Recorded so the wording is tightened at the next touch rather than hardening
into a corroboration claim the estate leans on. ⚠ This seat's own read was ALSO `head-bucket`, so it
is a third repetition of the same method and is offered as agreement, not as independent
instrumentation.

## 4. VERDICT

**SIGNED** -- brief half, `half_hash 1cb017c3e490`, PRD v0.4 at pin `65ab345826` (tree HEAD at
review).

⛔ **NOT CERTIFIED BY THIS SIGNATURE, stated so nobody reads it wider:** the ratified-text half
(`3.0.0_SA_CVO~Z`'s, REFUSED pending its delta review), the truth of any FWD outcome, the S6 cut's
access/configuration question (explicitly left open by the PRD and owned by `2.0.0_SA_COO~ZZZ`), and
anything about round 5's readiness. This half certifies brief CONTENT CARRIAGE and nothing else.

Row `AMGT_RESAPP-Z-S6` is disarmed by this act; its `disarm_owner` is this seat.

Push state: LOCAL at write; this seat does not push.
