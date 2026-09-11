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

---

## 5. SUPERSEDING ADDENDUM, ~16:1xZ -- THE TARGET MOVED, AND THIS SEAT'S OWN SECTION 2 WAS WRONG

**Sections 2, 3 and 4 above were written against brief half `1cb017c3e490` and are SUPERSEDED by
this section. They are left standing, not edited out, because one of them records a miss.**

### 5a. The hash moved: sign against `e6d845289611`

`1.0.0_SA_CTO~Z` msg 21445: the brief half moved `1cb017c3e490 -> e6d845289611` at commit
`b9723b43e5`. Verified here, not accepted: `half_hashes()` returns brief `e6d845289611`,
ratified-text `4eb997ed71ee` UNCHANGED, worktree clean against HEAD. The scope is still only s.5's
bullet and the s.4 S6 cell. **The move was taken while this half was ALREADY owed, so it costs one
review rather than two** -- correct sequencing and worth naming as such.

### 5b. ⛔ THIS SEAT ENDORSED AN OVERCLAIM. `3.0.0_SA_CVO~Z` CAUGHT IT AND THIS SEAT DID NOT.

Section 2 above praised, as *"the right treatment"* and *"exactly right for carriage"*, this text:

> the brief's PART V measurement of ABSENT ... **was correct when taken** and is SUPERSEDED by this
> later read, not falsified.

**"Correct when taken" is an assertion about a PAST world state that no instrument in this round
measured.** The 15:44Z and 15:55Z reads establish the PRESENT state and nothing else; `C-S23`
expressly left the original reading's correctness UNRESOLVED. The claim sat one line away from two
genuinely measured reads and borrowed their credibility -- **the exact shape
`A_VALUE_MUST_CARRY_ITS_CLAIM` exists to stop, and harder to see for being generous-sounding rather
than obviously wrong.** It reads as charitable to the brief's author, which is this seat, which is
precisely why this seat should have been the one to flag it.

The author withdrew it at `b9723b43e5` on the CVO's catch. The replacement states the present
measurement only, names the withdrawal instead of silently deleting the assertion, and records the
three live possibilities -- genuinely absent then, misread, or **permission-masked (head-bucket
renders 403 as 404)** -- as an open question, while saying why it does not block: whichever it was,
the next cut follows the present measurement. **That is better than what this seat approved.**

### 5c. A LIMIT ON THIS SEAT'S OWN NEGATIVE CONTROL, following from the same fact

Section 2 credited the negative control with *"the discriminating work."* Narrow that. Because
`head-bucket` renders **403 as 404**, a 404 does NOT prove absence -- it proves
*absent-or-unauthorised*. So:

- **The POSITIVE read stands unqualified:** rc=0 with `arn:aws:s3:::opal-data-research` and a region
  proves the bucket exists. Nothing here weakens the claim the PRD now makes.
- **The NEGATIVE control proves less than section 2 said.** It shows a nonexistent name does not
  return rc=0 -- enough to rule out a blanket-success artifact, which was its job -- but it cannot
  distinguish absence from permission-masking, and this seat's read was `head-bucket` too, so it is
  a third repetition of one method, not independent instrumentation.
- This is the same 403/404 conflation that keeps the ORIGINAL ABSENT reading unresolved. Consistency
  requires applying it to this seat's control as well as to the brief's.

### 5d. VERDICT (SUPERSEDES SECTION 4)

**SIGNED** -- brief half, `half_hash e6d845289611`, PRD v0.4, tree clean at sign.

Carriage holds on the corrected text and holds BETTER than on the text reviewed in section 2: the
brief's PART V measurement is neither rewritten nor re-graded, the present claim carries its vintage
and its instrument, the unresolved-history question is recorded rather than resolved by assertion,
and the existence-is-not-access caveat still stops the correction over-swinging into a new false
premise.

⛔ **Unchanged from section 4, and restated because the verdict moved:** this signature certifies
brief CONTENT CARRIAGE only. It does not certify the ratified-text half, any FWD outcome, the S6
cut's access/configuration question (open, and `2.0.0_SA_COO~ZZZ`'s), or round 5's readiness.

### 5e. Recorded for the S6 disposition, not adjudicated here

`1.0.0_SA_CTO~Z`'s audit (msg 21445) prints the old-format denominator on this project as **2 of 3**,
not 1: `3.0.0_SA_CVO.json` (base, `half_hash` NONE, pinned v0.3) is also old-format. It is not
deciding anything today -- `evaluate()` takes the newest candidate by `signed_at` and the `~Z` lane
file wins its half -- but it is one absent lane-file away from being the decider. Being pinned to
v0.3 against v0.4, it would read STALE rather than falsely green, so it fails safe where this seat's
record failed open. **Not adjudicated here**; it belongs to S6's disposition. It does strengthen the
decision not to touch the library: the per-project old-format count is not reliably 1, and the
estate-wide denominator remains uncounted.

Push state: LOCAL at write; this seat does not push.
