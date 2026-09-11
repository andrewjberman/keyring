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

---

## 6. THIRD REVIEW, ~16:3xZ -- `26f942429c6a`. SIGNED, AND THE REMEDY PROVED ITSELF

**Supersedes section 5d's verdict. Sections 1-5 stand.**

### 6a. What moved, and why it is one paragraph

`1.0.0_SA_CTO~Z` withdrew a SECOND overclaim from the same s.5 paragraph at `f0ff95cfac` -- the
*"re-read here on a second instrument"* independence claim, which section 5c of this review had
named. Both reads were `s3api head-bucket`: one method run twice, which Rule 22 calls REPETITION.
The replacement names the genuinely different instrument (`comp-find --corpus aws`, 1 hit across
2445 nodes, drift `DECLARED`) and carries the 403-renders-as-404 limit on the negative control that
section 5c also raised.

Verified here rather than accepted: brief `26f942429c6a` (matches), **ratified-text UNCHANGED at
`4eb997ed71ee`** -- checked BEFORE signing for the third consecutive amendment, so the CVO's
signature was never at risk -- worktree clean against HEAD, and the diff at `f0ff95cfac` touches
exactly that one paragraph.

**THE OPERATIVE CLAIM DID NOT MOVE.** `rc=0` with a real ARN and region proves the bucket exists
whatever the control does. What changed is the sentence describing HOW WELL the fact is known.
Nothing downstream needs re-deciding.

### 6b. ⭐ THE S6 REMEDY IS NOW EXERCISED, NOT MERELY ARGUED

`f0ff95cfac` moved the brief half and `prd-signoff.py status` reported **STALE** against it.
**Before the content-bound re-sign, this exact commit would have printed "brief SIGNED current"** --
the S6 false green, firing on a real edit within an hour of being filed. It did not fire, because a
hash-bearing record now exists.

**This is a POSITIVE CONTROL nobody had to construct.** Row `AMGT_RESAPP-Z-S7`'s disarm claimed the
instance was repaired; a live edit has now demonstrated it. The row's three non-claims are
UNCHANGED and are not softened by this: the library is untouched, the old-format carrier
`4.0.0_SA_CRO.json` is still present and merely shadowed, and the estate-wide class is uncounted.

### 6c. WHY THIS SEAT SIGNS NOW RATHER THAN LETTING IT RIDE

`1.0.0_SA_CTO~Z` explicitly offered the option of deferring this review onto the next brief-half
amendment and said it would not push the point. Declined, for a stated reason rather than reflex:
**`2.0.0_SA_COO~ZZZ`'s round v5 is blocked on this signature**, so deferring would stall a real
consumer over a one-paragraph improvement that this seat itself requested. The cost of a third
review is real and `1.0.0_SA_CTO~Z` named it without dressing it up; it is small, and smaller than
leaving an evidence-grade overstatement inside a ratified spec.

⚠ **THE CHURN IS WORTH NAMING AS A PATTERN, NOT AS A COMPLAINT.** Three brief-half edits inside one
hour, each a genuine improvement, each found by a reviewer rather than the author, and **both
overclaims caught by the reviewer of the OTHER half.** That last fact is the useful one: it is
evidence against any future argument that a half's reviewer need only read its own half. Recorded
here rather than sent as a message, because nobody needs to act on it.

### 6d. VERDICT

**SIGNED** -- brief half, `half_hash 26f942429c6a`, PRD v0.4, tree clean at sign.

Carriage holds and is now stated more honestly than in either prior version: the instrument is named
and its independence is NOT overstated, the negative control's 403/404 limit is disclosed, the
positive read carries the bullet on its own, and both withdrawals sit in the PRD's own text naming
themselves rather than being silently edited away -- so a future reader sees what was claimed and
what replaced it.

⛔ Certification scope UNCHANGED from sections 4 and 5d: brief CONTENT CARRIAGE only. Not the
ratified half, not any FWD outcome, not the S6 access/configuration question, not round 5 readiness.

---

## 7. FOURTH REVIEW, ~16:5xZ -- `c90934a3d620`. SIGNED, AND THIS ONE IS NOT A CORRECTION

**Supersedes section 6d's verdict. Sections 1-6 stand.**

### 7a. Why this one is different from the previous three

The first three re-signs chased the author's own withdrawals. **This one folds in NEW EVIDENCE from
another seat's round-4 work** (row `AMGT_RESAPP-Z-S8`, `2.0.0_SA_COO~ZZZ`'s discharge of S5's COO
half), and it changes the spec materially rather than tidying a sentence.

Verified here: brief `c90934a3d620` (matches), **ratified-text UNCHANGED at `4eb997ed71ee`** --
fourth consecutive brief-half edit that left the CVO's signature untouched -- worktree clean, and
the diff at `6c52a4e380` is exactly two brief-half hunks (the s.4 S6 row, the s.5 bullet).

### 7b. THE SPEC CHANGE, AND WHY IT MATTERS MORE THAN THE SIGNATURE

`S6` flips **`build` -> `INTEGRATE -- no create cell`**, and its state flips `absent` ->
`STORE EXISTS; surface absent`.

⛔ **A ROUND-5 CUT AGAINST THE OLD ROW WOULD HAVE CUT A CREATE CELL FOR A BUCKET THIS PROJECT
CREATED YESTERDAY.** That is the kind of defect that produces a confident, passing cell doing
exactly the wrong thing, and it would have been cut from a row that read `build` in a ratified spec.
**The amendment is worth four signatures on its own.**

### 7c. EVERY SUBSTANTIVE CLAIM RE-DERIVED ON THIS SEAT'S OWN INSTRUMENTS

Not accepted from the message -- the S6 row is about to drive a cut:

| claim | this seat's read | result |
|---|---|---|
| declared, and this project's own | `infra/aws/terraform/research/s3.tf` | `aws_s3_bucket.research`, tags `project = AMGT_RESAPP`, `directive = D5` -- CONFIRMED |
| versioning `Enabled` | `get-bucket-versioning` | `{"Status": "Enabled"}` -- CONFIRMED |
| no lifecycle | `get-bucket-lifecycle-configuration` | `NoSuchLifecycleConfiguration` -- CONFIRMED |
| no bucket policy | `get-bucket-policy` | `NoSuchBucketPolicy` -- CONFIRMED, so access is IAM-only |
| read/list access MEASURED | `list-objects-v2` | SUCCEEDS, returns this project's own `derived/model_block/` output -- CONFIRMED |
| creation recorded | the CLOSED deploy-completion entry | present at the cited path -- CONFIRMED |

⭐ **ONE PIECE OF EVIDENCE THE AMENDMENT DOES NOT CITE, FOUND IN THIS SEAT'S OWN LISTING AND OFFERED
AS A STRENGTHENING:** the listing shows `BABA_US_Equity` carrying **two distinct timestamped
snapshots** -- `20260910T224432Z` and `20260910T225428Z` -- both present, neither overwritten. So
FWD-6's *"snapshots accumulate rather than overwrite"* bar is demonstrated **IN THE DATA**, not only
by the `Enabled` flag and the path grammar. That is a stronger form of the same claim: config makes
overwriting hard, but the objects show the grammar was actually followed. Offered to whoever grades
FWD-6; this seat is not grading it.

### 7d. ON THE WITHDRAWAL THAT TURNED OUT TO BE TRUE -- THE SEQUENCE WAS RIGHT

`1.0.0_SA_CTO~Z` withdrew *"the ABSENT reading was correct when taken"* as unmeasured; S8 has since
established it IS true (absent measured twice, the second time by `AMGT-s-6`'s own AC1 three minutes
before that cell created the bucket). **The withdrawal was still correct and this seat endorses the
reasoning without reservation: a claim is not made true retroactively by later evidence arriving.**
It was unsupported when asserted and is supported now, and those are different facts about different
moments. Withdrawing it and then RE-ADDING IT ON EVIDENCE is the right sequence, not a reversal --
and the PRD now carries it as a measurement rather than as a courtesy to the brief's author.

⚠ **The correction in section 5b of this review therefore stands unchanged.** This seat's error was
never that the claim was false; it was endorsing an unmeasured claim as measured. That error is
identical whether or not the claim later turned out true -- and if anything the outcome makes it
more instructive, because a lucky guess is the case where this failure mode is hardest to see.

### 7e. VERDICT

**SIGNED** -- brief half, `half_hash c90934a3d620`, PRD v0.4, tree clean at sign.

Carriage holds and is now the strongest of the four versions: brief PART V is SUPERSEDED on
MEASUREMENT rather than asserted over, access is measured rather than assumed, the still-open item
(write access, not exercised, not granted) is named, and S6 tells a cutter to integrate rather than
create.

⛔ Certification scope UNCHANGED: brief CONTENT CARRIAGE only.

---

## 8. FIFTH REVIEW -- PRD **v0.5** @`5517e071e8`, brief `c977c8c275ce`. SIGNED

**Supersedes section 7e's verdict. Sections 1-7 stand.** First review against a NEW PRD VERSION
rather than an amendment of v0.4: the L4 ADDENDUM carrying the HARVEST ESTATE.

### 8a. Verified before reading a word of the substance

| check | result |
|---|---|
| brief half | `c977c8c275ce` -- matches the hash the addendum names |
| ratified-text half | `4eb997ed71ee` **UNMOVED** -- `3.0.0_SA_CVO~Z`'s signature stands; fifth consecutive brief-half edit that left it alone |
| `endpoint_outcomes` | **15 ids, `FWD-1`..`FWD-15`, the set UNCHANGED** -- the load-bearing one |
| worktree | clean against HEAD at sign |

⭐ **THE OUTCOME-SET CHECK IS WHAT MAKES THIS A ONE-HALF REVIEW, AND IT WAS RUN RATHER THAN
ASSUMED.** The addendum claims *"no outcome changed; only HOW and BY WHOM two of them are served."*
Had an `FWD` been added, renumbered or reworded, the ratified half would have moved and
`3.0.0_SA_CVO~Z` would owe a re-sign too. It did not. **The claim is true at the header, and that is
why this costs one review instead of two.**

### 8b. Carriage verdict: SIGN

- **`C-HARVESTER-COMPUTE` amended** from four harvesters on a shared box to ONE box and ONE lambda in
  the ONE harvester module, with Andrew's EC2-not-site-Z ruling carried VERBATIM and its reason
  stated: a local server cannot sit inside a canonical, self-contained, terraformed estate.
- ⭐ **`C-VENDOR-WORD-HARVESTERS` RE-HOMED -- the single most consequential line in the addendum.**
  It had no cell of its own; decomp s.13d carried it as a time-scoped BOUND on `rd-4`, so
  superseding `rd-4` would have removed its only carrier. It now sits on the harvest estate's
  acquisition surface **with all three limits intact**, and the PRD states in terms that Andrew's
  "full egress and override authority" is authority to REALIZE THE ESTATE and **NOT** a widening of
  `C-VENDOR-EGRESS`. ⚠ **This seat is the BENEFICIARY of that grant and is therefore the wrong party
  to have been the only one watching it narrow. That `1.0.0_SA_CTO~Z` wrote the narrowing into the
  spec is the actual control**, and it is worth more than this seat's own assurance.
- **The proxy-vendor question is written in as OPEN** -- never inferable from an EC2 IP failing
  against PerimeterX.
- **This seat's error is recorded AS an error:** the bot-wall reasoning was sound about PerimeterX
  and wrong about the estate -- a correct local fact deciding a question it does not govern.

### 8c. ONE OBLIGATION THIS SEAT INHERITS AND HAD NOT STATED

> *"Refresh must still WAKE the stopped box (SSM / inf-jwt-trigger shape) or it silently no-ops."*

**Accepted, and it is a genuine gap in the drawn architecture.** This seat MEASURED that all three
existing scraper boxes read `stopped` -- including `astn-wsjft-scraper`, launched only today at
07:00Z -- so **a stopped harvester box is the NORMAL state under the auto-shutdown regime, not an
edge case.** A scheduled refresh against a stopped box does not fail loudly; it silently does
nothing, which is the freshness failure that looks like healthy quiet. The wake step is part of what
the box cell must build, and it is named here so it cannot be lost between the addendum and the
build.

### 8d. VERDICT

**SIGNED** -- brief half, `half_hash c977c8c275ce`, PRD **v0.5**, tree clean at sign.

⛔ Certification scope UNCHANGED: brief CONTENT CARRIAGE only. Not the ratified half, not any FWD
outcome, not round 5's readiness, and **not the supersede itself** -- that status flip is
`2.0.0_SA_COO~ZZZ`'s act and must ride the same commit as the decomp s.13c repair.

Push state: LOCAL at write; this seat does not push.
