# POSN_ASTTAX PRD v0.5 -- BRIEF HALF, RE-REVIEW AND RE-SIGN

`4.0.0_SA_CRO~Z`, 2026-09-11 ~21:1xZ. L4-R brief half (spine v3.15).
Subject: `org/missions/D4/POSN/POSN_ASTTAX/prd/POSN_ASTTAX_PRD.md`, brief `half_hash 3c1c3202ca9e`,
amendment `@49ddcc481d`.

## 1. VERIFIED BEFORE READING THE SUBSTANCE

| check | result |
|---|---|
| brief half | `3c1c3202ca9e` -- matches the hash the gate names |
| ratified-text | `1c60358b916e`, SIGNED by `3.0.0_SA_CVO~Z` and **current** -- the amendment did not reach it |
| `endpoint_outcomes` | 6, unchanged |
| worktree | clean at sign |

## 2. WHAT CHANGED: `C-RETAG-SAFETY` RE-FOUNDED, NOT RE-SEQUENCED

The constraint's stated mechanism was **falsified by the measurement the constraint itself ordered**.
`AT2-s-6` hardened the generator and killed the `KeyError`: `TO-S7-1` measured **0 of 17 hops RAISE**.

- **LIVE mechanism now stated:** a retag renders `'Unknown'` and **silently zeroes the weight**. The
  page still renders.
- **ORIGINAL mechanism preserved as history**, explicitly marked non-operative -- the fixed-key
  dicts, the `KeyError`, the page blanking for all four partner firms.
- **The constraint still BINDS.** Only its reason changed.

⭐ **THE HAZARD GOT QUIETER, NOT SAFER, AND THE AMENDMENT SAYS SO IN THOSE TERMS.** A blank page is
noticed in seconds; a zeroed allocation line looks like a real allocation. That is strictly worse for
detection than what it replaced, and a reader of the OLD text would have gone looking for a crash
that can no longer happen.

## 3. THE REPAIR THIS SEAT RATES HIGHEST -- STEP (2) IS NOW A CONDITION, NOT AN ACT

> *"for EVERY ticker in the retag set, the SERVED `asset_class` value equals its ratified five-class
> label AND its allocation weight is NON-ZERO and equal to its pre-retag weight, read from the served
> artifact."* — and, stated outright: **"Step (2) is currently NOT MET."**

⛔ **A STEP THAT NAMES A TASK IS SATISFIED BY DOING THE TASK; A STEP THAT NAMES A CONDITION IS
SATISFIED ONLY BY THE WORLD.** The old wording ("verify the chain") is what let a completed
verification cell be read as a passed one -- an error `1.0.0_SA_CTO~Z` made, withdrew, and has now
designed out of the spec rather than merely apologised for. **The bar also fails in the broken
world**, which "confirm the page still renders" never could: a retagged ticker at a zeroed weight
renders fine and fails this bar.

## 4. CARRIAGE VERDICT -- SIGN

The brief half's test is CONTENT CARRIAGE, and the amendment is explicit about the one thing that
could have broken it: **"Andrew's ruling and the DT brief are UNCHANGED; only the mechanism the
round-3 cells will read."** The brief's `KeyError`/page-blank account is not deleted and not
re-graded -- it is preserved as what was true when the DT brief was written, and marked as
superseded by a later measurement. That is the correct treatment and the same one this project
adopted for `opal-data-research`'s ABSENT reading.

⭐ **AND THE AMENDMENT CREDITS ITS OWN CONTRADICTION:** *"THE PRD ASKED FOR THE MEASUREMENT THAT
CONTRADICTED IT, AND GOT IT -- that is the instruction working, not failing."* Correct, and the
generalisation it draws is the durable part: **prose predates its own instrument's answer, so a spec
that ORDERS a measurement must be RE-READ WHEN THE ANSWER LANDS.**

⚠ **ONE QUALIFIER CARRIED CORRECTLY AND WORTH NAMING:** the 17-hop figures are pinned to `TO-S7-1`'s
run, and `3.0.0_SA_CVO~Z` records that `S1` later repaired a benchmark hop -- so **the RATIO is
historical while the VERDICT is not**, re-confirmed against current controls. Distinguishing a stale
NUMBER from a still-live CONCLUSION is exactly the discipline this project keeps needing.

## 5. VERDICT

**SIGNED** -- brief half, `half_hash 3c1c3202ca9e`, PRD v0.5, tree clean at sign.

⛔ Certification scope: brief CONTENT CARRIAGE only. **NOT certified:** the ratified-text half
(`3.0.0_SA_CVO~Z`'s, untouched and current), whether step (2) can be met, the retag itself, or
round 3's readiness. Step (2) is NOT MET by the spec's own words and `TO-S2-1`/`TO-S3-1` remain
correctly uncut.

Push state: LOCAL at write; this seat does not push.

---

## 6. SECOND REVIEW -- brief `0cc8a7d2dd9d` @`71a376b98e`. SIGNED

**Supersedes section 5's verdict. Sections 1-5 stand.** The bar this seat signed two hours ago was
NARROWER THAN THE HAZARD, and the defect was in the re-founding itself.

| check | result |
|---|---|
| brief half | `0cc8a7d2dd9d` -- matches |
| ratified-text | `1c60358b916e` **UNCHANGED** -- CVO signature intact |
| `endpoint_outcomes` | 6, unchanged |
| worktree | clean at sign |

### 6a. ⛔ A NEW FAILURE MODE, AND IT IS NOT THE ONE SECTION 3 PRAISED

Section 3 rated step (2) highly for being a CONDITION rather than an act, and for FAILING IN THE
BROKEN WORLD where `S2-AC5` could not. **Both of those remain true and both were insufficient.**
The bar read *"from the served artifact"* -- meaning `positioning_data.json` alone -- and
`2.0.0_SA_COO~Z`'s wave-1 cells measured **both collapse sites OUTSIDE that artifact**:

- **DOWNSTREAM:** `HoldingsTab.tsx:1392-1394` iterates a HARDCODED
  `assetClassOrder = ['Fixed Income','Equity']`. A `Commodities`/`Structured`/`Alternatives` group is
  **NEVER ITERATED** -- the row renders NOWHERE while its weight stays in the grand total. 42 of 42
  consumers, 12 sites, 8 files.
- **A DIFFERENT ARTIFACT:** `yang-generate-allocation-summary` carries `Commodities` through all 88
  hops, then draws `policy_weight 0.0` from a two-key `BENCHMARK_ALLOCATIONS`, writing
  `holdings_attribution_data.json`.

⭐ **SO THE CELL COULD HAVE RETURNED GO -- CORRECTLY, ABOUT THE ARTIFACT IT WAS POINTED AT -- WHILE
THE PAGE DROPPED THE ROW.** `TRUE AND INSUFFICIENT`. That is a THIRD criterion pathology, distinct
from the two this project already names: not always-passes (`S2-AC5` could not fail at all), and not
unsatisfiable -- **a criterion that discriminates correctly over the WRONG DOMAIN.** It is Rule 24's
wrong-domain subtraction wearing a criterion's clothes, and it reads as rigorous precisely because it
*can* fail.

### 6b. THE EVIDENCE THAT MAKES (c) AND (d) BARS RATHER THAN ADVICE

**This exact bug has already SHIPPED.** The same file documents it for `Cash` at `:1364-1372`,
measured on PROD v2.1.167: **PFDE 90 -> 89 served-vs-DOM rows, subtotals 99.98 under a grand total of
100.01.** The remedy folded only `Cash` and `Hedge` -- **so a retag reproduces it with a new value.**
A bar that did not check RENDER and SUBTOTAL would have certified the reproduction.

⭐ **THE MECHANISM IN THE MEASURING WORKER'S OWN WORDS:** *"Data reaches three lambdas; the code
hardening reaches one."* That sentence is why hardening one write surface never bounded this.

### 6c. VERDICT

**SIGNED** -- brief half, `half_hash 0cc8a7d2dd9d`, PRD v0.5, tree clean at sign.

Carriage holds and is materially better than what section 5 signed: the bar now spans **every served
surface the retagged value reaches**, with (a) served value, (b) non-zero unchanged weight,
(c) **the row RENDERS** -- served row count equals DOM row count -- and (d) **class subtotals sum to
the grand total**.

⚠ **AND MY OWN SECTION 3 IS CORRECTED BY THIS, NOT MERELY SUPERSEDED.** I praised the bar for failing
in the broken world without asking WHICH broken worlds it could see. "Fails in the broken world" is
necessary and not sufficient; the next question is **"over what domain?"** -- and I did not ask it.
`2.0.0_SA_COO~Z` did, by measuring the consumers rather than reasoning about the artifact.

⛔ Scope unchanged: brief CONTENT CARRIAGE only. Step (2) is still NOT MET; `TO-S2-1`/`TO-S3-1`
remain correctly uncut and ADMITTED is not a retag GO.

---

## 7. THIRD REVIEW -- brief `f5bbef8c9ca9` @`3832ac543c`. SIGNED

**Supersedes section 6c. Sections 1-6 stand.** Folded in BEFORE this seat signed `0cc8a7d2dd9d`, so
it costs ONE review rather than two -- the right call by the author.

| check | result |
|---|---|
| brief half | `f5bbef8c9ca9` -- matches |
| ratified-text | `1c60358b916e` **UNCHANGED** |
| `endpoint_outcomes` | 6, unchanged |
| worktree | clean at sign |

### 7a. THE ALWAYS-PASSES SHAPE, A THIRD TIME, INSIDE THE BAR THAT FIXED THE SECOND

Clause (b) read *"its ALLOCATION WEIGHT is NON-ZERO and equal to its pre-retag weight"*. `AT3-s-1`
measured the real `generate_positioning_data` on the same input:

| | served label | LABEL-GROUPED weight | `allocation['commodities']` |
|---|---|---|---|
| BEFORE | `'Unknown'` | **0.000** | 2.5 |
| AFTER | `'Commodities'` | **0.025** | 2.5 |

⛔ **THE ALLOCATION-DICT COLUMN DOES NOT MOVE.** At base `651ffd4f16` all three `if/elif` chains
already carried an `else` from `AT2-s-1` and the accumulator already served 2.5 -- so a reader
satisfying (b) against that column reads **IDENTICALLY in the healthy world and the broken one**.
(b) now says **LABEL-GROUPED** and names the non-discriminating column outright so nobody picks it.

⭐ **THIS IS THE FINDING, NOT THE FIX:** the `S2-AC5` always-passes shape appeared *inside the very
clause written to repair its second instance*. Widening a criterion's DOMAIN (section 6) does not
make its MEASURE discriminate -- they are independent failures and a bar can carry both at once.
⚠ **AND THE CONSTRAINT'S MECHANISM HAS NOW BEEN OVERTAKEN BY A REPAIR TWICE** -- `AT2-s-6` killed the
KeyError, then `AT2-s-1` filled the `else` branches. **A constraint that names a mechanism ages every
time someone fixes the code underneath it**, which is an argument for naming the OBSERVABLE
(what the page serves) rather than the MECHANISM (how it breaks).

### 7b. VERDICT

**SIGNED** -- brief half, `half_hash f5bbef8c9ca9`, PRD v0.5, tree clean at sign.
⛔ Scope unchanged: brief CONTENT CARRIAGE only. Step (2) still NOT MET; `TO-S2-1`/`TO-S3-1` uncut;
ADMITTED is not a retag GO.

---

## 8. FOURTH REVIEW -- brief `d64247e7fd58` @`f9458a7e43`. SIGNED. **THE RE-FOUNDING IS REVERSED.**

**Supersedes sections 5, 6 and 7 in substance.** They stand as the record of three signatures this
seat gave to a premise that was measured on the wrong plane.

| check | result |
|---|---|
| brief half | `d64247e7fd58` -- matches |
| ratified-text | `1c60358b916e` **UNCHANGED** -- CVO signature intact through all four |
| `endpoint_outcomes` | 6, unchanged |
| worktree | clean at sign |

### 8a. WHAT REVERSED, AND IT RESTORES THE ORIGINAL BRIEF

`C-RETAG-SAFETY` was re-founded at ~20:0xZ on `TO-S7-1`'s *"0 of 17 hops RAISE -- `AT2-s-6` killed
the KeyError; the live mechanism is SILENT ZEROING"*, and the DT brief's page-blanking mechanism was
written into the PRD as **"PRESERVED AS HISTORY AND NO LONGER OPERATIVE."**

⛔ **THAT MEASUREMENT WAS TAKEN AGAINST `HEAD`. `HEAD` WAS NEVER THE PLANE THIS CONSTRAINT IS ABOUT.**

```
deployed yang-generate-positioning   LastModified 2026-08-18T18:34:43Z
                                     CodeSha256   PRg64EGzQtLw7/HAhyN/jNP6rd01PrcLK4wKqCHAKfQ=
AT2-s-6, AT2-s-1, AT3-s-1            ALL September -- COMMITTED, NOT DEPLOYED
```

**So a retag today BLANKS THE PAGE for all four partner firms. Not silent zeroing. Blanking --
exactly as `0.4.0_DT_ClientPlatform` wrote it in the first place. The DT brief was right the whole
time.**

### 8b. THE EVIDENCE IS CORROBORATION, AND I CHECKED WHICH PART OF IT WAS

- **Genuinely different instrument:** the worker DROVE THE DOWNLOADED DEPLOYED BYTES ->
  `KeyError: 'Structured'` at `calculate_allocations():239`, 11 of 11 members, with a positive
  control (`def lambda_handler` 1/1) and a negative control (0/0). Deployed 94,164 B vs HEAD
  115,411 B, different md5s.
- **Control plane:** `2.0.0_SA_COO~Z` read `LastModified` / `CodeSha256`.
- ⚠ **MY OWN READ IS THE SECOND METHOD AGAIN, NOT A THIRD.** I ran
  `lambda get-function-configuration` and got byte-identical values to `2.0.0_SA_COO~Z`. That is
  **REPETITION of the control-plane read, not independent corroboration** -- it confirms the date, it
  does not add an instrument. The worker's execution of the deployed bytes is the one that carries
  the finding.

### 8c. ⛔ MY OWN FAILURE, AND THE LAW ALREADY NAMED IT

I signed this re-founding **three times** (sections 5, 6, 7). Across those reviews I asked:
*is it a CONDITION rather than an act?* (yes) · *over WHAT DOMAIN?* (only after being corrected) ·
*does the MEASURE discriminate?* (only after being corrected).

**I never once asked: MEASURED AGAINST WHICH PLANE -- `HEAD` OR DEPLOYED?**

⭐ **AND CLAUDE.md RULE 22a STATES THIS EXACT TRAP, IN THESE WORDS:** *"diff deployed bytes against
the BUILD INPUT ... **running-bytes-older-than-built passes every rung.**"* That is precisely what
happened: every rung passed. A criterion can be a condition, discriminate correctly, span every
consumer, and still be measured on a plane that does not serve anyone.

**So the plane question belongs BEFORE the domain question, not after it.** Domain asks *which
consumers does this reach?* Plane asks *does the thing I measured actually run?* A perfect answer on
the wrong plane is worth nothing, and it is the cheapest of all these checks -- one
`get-function-configuration`.

### 8d. VERDICT

**SIGNED** -- brief half, `half_hash d64247e7fd58`, PRD v0.5, tree clean at sign.

Carriage is now CORRECT for the first time in four versions: the DT brief's blanking mechanism is
restored as LIVE rather than buried as history, and the repairs are recorded as
**committed-not-deployed** rather than as done.

⛔ Scope unchanged: brief CONTENT CARRIAGE only. Step (2) remains NOT MET, `TO-S2-1`/`TO-S3-1` remain
correctly uncut, and ADMITTED is emphatically not a retag GO -- **the retag is now known to blank
four partner firms' pages, which is worse than anything the three prior versions described.**

---

## 9. TENTH REVIEW -- brief half `219a6113f` @`b6dfc68ff1`: SIGN

**Verified first.** Brief half `219a6113f` (was `d64247e7fd58`). Ratified-text half
`1c60358b916ed6f395a38a1ed74dabe5641e41ee9b02a9c464e94e27f0a0d503` **UNCHANGED -- now across FIVE
brief-half versions**, still signed at the v0.4 pin `65844d868c`. `git diff f9458a7e43 b6dfc68ff1`
on the PRD is **two hunks, both inside s.4**, so the brief half is the only half that moved.

### What changed, and it corrects a sentence THIS SEAT SIGNED

The severity clause is narrowed on `3.0.0_SA_CVO~Z`'s `C-S52`: **an unsafe generation PRECONDITION,
not demonstrated page-blanking.** Section 8 above records the wider sentence as signed substance; it
is left standing because a review records what was reviewed when it was signed. The narrowing is
right and this seat accepts it without reservation -- the consequence was measured by nothing.
⭐ The amendment also adds the rule in the PRD's own words: *"The precondition is measured; the
consequence is inferred, and the two must not be written as one sentence."* That is the correct
generalisation and it is now in the spec rather than only in a message.

### THE ONE FINDING, AND IT IS IN THE SAME PARAGRAPH AS THE CORRECTION

The block now claims **"Three methods, three seats, one answer"**. Measured against what the three
arms actually did, that is **TWO methods and three seats**:

| arm | seat | what it read | method |
|---|---|---|---|
| 1 | worker `AT3-s-5` | downloaded deployed bytes, 94,164 B `md5 cc79aff...` | **execution** of the deployed artifact |
| 2 | `2.0.0_SA_COO~Z` | `get-function-configuration` | **control-plane metadata** -- genuinely different |
| 3 | `3.0.0_SA_CVO~Z` `C-S52` | downloaded bytes, **94,164 B, `md5 cc79aff7506f8c39e17453f386c69551`** | **execution** -- the SAME method on a BYTE-IDENTICAL artifact |

⛔ **ARM 3 IS AN INDEPENDENT REPRODUCTION, NOT A THIRD METHOD.** The md5 is stated in the PRD itself
and it matches arm 1's. This estate's Rule 22 names exactly this: *"A second seat's confirmation via
the FIRST seat's method is REPETITION, not corroboration -- name your instrument and whether it
differs."*
⭐ **AND THE LABEL UNDERSELLS ARM 3'S REAL CONTRIBUTION, WHICH IS THE BEST EVIDENCE IN THE BLOCK.**
What arm 3 added that neither prior arm had is a **DISCRIMINATING NEGATIVE ARM**: 11/11 candidate
AFTER-exceptions on the deployed bytes *against 11/11 SUCCESSFUL repaired-source arms*. That is what
rules out "the eleven inputs are bad" and "the harness is broken" -- the alternative hypotheses a
bare 11/11 cannot exclude. Calling it "a third method" hides a real discriminator behind a weaker and
inaccurate claim.
⚠ **NOTHING ABOUT THE VERDICT MOVES.** Two independent methods, an independent reproduction, and a
discriminating negative arm is a *strong* evidentiary position -- stronger, read correctly, than
"three methods" asserts. The deploy gap stands, the retag stays NO-GO, and the sequence is unaffected.

### Verdict and why it is SIGN and not REFUSE

**SIGN.** The defect is a precision error in an EVIDENCE LABEL inside a supporting clause -- not in a
constraint, a criterion, an acceptance bar or a sequence. Refusing would hold POSN_ASTTAX's
round-close over a label while the substance it labels is correct and improved. Proportionality is
the call here, and the finding is recorded for the next amendment rather than used as a block.

### Residual for `1.0.0_SA_CTO~Z` -- two items, neither urgent, neither blocking

1. **"Three methods" -> "two methods, three seats, one independent reproduction with a discriminating
   repaired-source arm."** One sentence, and it makes the evidence read stronger, not weaker.
2. **Changelog line 16 is still `md5 611998b2e3`** -- unqualified and present-tense -- and has now
   survived **FIVE** amendments *including this one, whose entire purpose was to narrow that exact
   claim.* `2.0.0_SA_COO~Z` measured the md5 chain across all five.

⛔ **THE PATTERN, STATED ONCE BECAUSE IT IS NOW THREE-FOR-THREE TONIGHT AND NOT AS CRITICISM:** the
amendment that corrects an overclaim (a) carries a smaller overclaim **of the same family** -- an
evidence-strength claim outrunning what the instruments show -- and (b) leaves the corrected
sentence's own SUMMARY untouched 140 lines above. A remedy scoped to where the defect was caught
does not cover the class, and here the fix and the leak are in the same commit.

**Push state:** LOCAL at the time of writing; `0.0.0_AB_MSTR~Z` holds the push.

---

## 10. I SIGNED BYTES I HAD NOT READ -- the eleventh review, and the process failure that made it necessary

⛔ **SECTION 9 REVIEWED `219a6113f` @`b6dfc68ff1`. THE SIGNATURE IT PRODUCED BOUND TO
`590ba0cbf3ae268032aea4c9267dc7b12669e589e5dccebe58406fda81dc8a66` @`5840cc12ac`.** The PRD moved in
the gap between writing the review and running the stamp, and `prd-signoff.py sign` bound my name to
**whatever was current at stamp time**, not to what section 9 examined. The gate read `ADMITTED /
brief SIGNED / current` immediately, and it was telling the truth about the HASH while my review
covered different bytes.
**Caught by reading the stamp's own output**: it printed `@5840cc12ac` where the review said
`b6dfc68ff1`. Nothing else would have surfaced it -- every downstream reader sees a signature, a
`review_ref` and a matching hash.

### THE TOOL GAP, for `1.0.0_SA_CTO~Z` as owner of `prd_signoff_lib`

`prd-signoff.py sign` takes `--half`, `--review <path>@<pin>`, `--reason`, `--for`. **It has no
`--expect-half-hash`.** So nothing anywhere binds THE REVIEW to THE BYTES:
- the `review_ref` proves a review EXISTS, never that it examined what was signed;
- the `half_hash` proves the bytes were CURRENT AT STAMP TIME, never that anyone read them;
- and the two fields are recorded side by side, which makes the record *look* like it carries the
  link it does not carry.
⭐ **SAME FAMILY AS TONIGHT'S EARLIER FALSE GREEN** (a record with no `half_hash` graded on a version
string): in both, the gate is honest about what it measures and the DEFECT IS THAT NOBODY MEASURES
THE THING THE SIGNATURE IS SUPPOSED TO MEAN. **REC:** `sign` accepts an optional
`--expect-half-hash <hash>` and REFUSES on mismatch, naming both values. A reviewer who reads the
half necessarily knows its hash, so the cost is one argument and the failure mode becomes loud.
Not built here -- the tool is `1.0.0_SA_CTO~Z`'s.

### THE ACTUAL REVIEW OF `590ba0cbf3ae` @`5840cc12ac`, now genuinely performed

Re-measured at the moment of signing: current pin `5840cc12ac`, no further movement, ratified-text
half `1c60358b916e` still UNCHANGED. `git diff b6dfc68ff1 5840cc12ac` is **two hunks, both brief-half**:

1. **Changelog line 16 -- FIXED, and it was residual (2) of section 9.** Now reads *"a fixed-key
   allocation dict KeyErrors in the DEPLOYED generator, establishing an UNSAFE GENERATION PRECONDITION
   -- page-blanking is the brief's PREDICTED consequence and is NOT measured; see s.4"*. The line that
   survived five amendments at `md5 611998b2e3` is corrected on the sixth.
2. **s.4 SELF-CONTRADICTION -- FIXED, and nobody had reported this one.** The old header read
   *"PRESERVED AS HISTORY AND NO LONGER OPERATIVE ... falsified by `AT2-s-6`"* directly beneath a block
   asserting the same mechanism IS what production runs. **The spec asserted both that the mechanism is
   dead and that it is running.** Now scoped correctly: *"IT IS FALSIFIED AT HEAD ONLY. IT IS WHAT THE
   DEPLOYED BYTES RUN."* ⭐ This is the better catch of the two and it is `1.0.0_SA_CTO~Z`'s own --
   a reversal added as a NEW paragraph without reconciling the paragraph under it, which is the
   append-don't-reconcile shape rather than the leaks-one-field-over shape.
3. The consequence/precondition split is now stated a third time in the right place: *"The generator
   death is measured on four instruments; what the page does after it is inferred."*

⚠ **ONE NOTE, DELIBERATELY NOT RE-OPENED:** that sentence says **four instruments** where section 9
measured **two methods across three seats** (the fourth arm being `0.0.0_AB_MSTR~Z`'s vintage
comparison). "Instruments" is the looser word and four arms do exist, so this is not the same error --
but the number has gone 2 -> 3 -> 4 across three paragraphs written tonight, and **this seat has
already asked the fabric to stop re-tallying that count.** Recording it once, here, and not sending it.

**VERDICT: SIGN `590ba0cbf3ae`.** The amendment repairs both residuals section 9 raised plus a
self-contradiction nobody had caught, and changes no constraint, criterion, bar or sequence. Retag
stays NO-GO; `TO-S2-1` and `TO-S3-1` stay correctly uncut.

⛔ **AND THE LESSON THAT IS MINE, NOT THE TOOL'S: A REVIEW AND ITS SIGNATURE ARE TWO ACTS AT TWO
TIMES, AND THE BYTES CAN MOVE BETWEEN THEM.** The estate's own rule -- *a staleness verdict needs a
fresh read at the moment of ACTING* -- is banked in this seat's memory, and I applied it to other
seats' gate reports twice tonight before failing it on my own signature. **RE-READ THE HALF HASH
IMMEDIATELY BEFORE THE STAMP, AND ABORT IF IT MOVED.**

---

## 11. TWELFTH REVIEW -- v0.6 ADDENDUM, brief half `7f815fff5` @`ae66157381`: SIGN

**Verified first.** Ratified-text half UNCHANGED and still SIGNED/current -- `3.0.0_SA_CVO~Z` owes
nothing. Diff v0.5 -> v0.6 is **50 insertions, 4 deletions, one file**, and touches **no ENDPOINT
byte**, which is why only this half went STALE.

### THE LOAD-BEARING CLAIM, RE-MEASURED INDEPENDENTLY RATHER THAN ACCEPTED

Item 1 says `FWD-4` and `FWD-6` are served by ZERO cut orders across three rounds. **Measured here
over the 15 order files directly:**
```
FWD-1  19      FWD-2   5      FWD-3   1
FWD-4   0      FWD-5   7      FWD-6   0
```
**CONFIRMED, and the other four outcomes are the control** -- a sweep that returned zero for all six
would indicate a broken matcher; four non-zero counts prove it discriminates. **`FWD-6` is the ASTTAX
frontend outcome Andrew named by name at 03:21:46Z, and it has never been issued.**
⭐ **AND THE DIAGNOSIS IS THE BETTER HALF OF THE ITEM:** the surface table's *"0 uncovered"* was true
about ASSIGNMENT and silent about ISSUANCE. **An empty subtraction gets ACTED ON rather than argued
with, and this one printed a denominator so it read as measured.** That is Rule 24's wrong-domain
failure in the form the estate has now met five times tonight, and the CTO names it as its own.

### ⛔ ONE DEFECT, AND IT IS INTERNAL TO THE ADDENDUM

    line 43 (s.0)  "THIS BUMP RE-OPENS BOTH L4-R HALVES"
    line 47 (vers) "THIS LINE USED TO READ 'Each bump re-opens the two L4-R sign-offs' AND THAT IS
                    FALSE -- CORRECTED AT v0.6 ... only the half whose SECTION BYTES changed"
**THE SAME COMMIT ASSERTS A RULE AND, FOUR LINES LATER, DECLARES THAT RULE FALSE.** The gate settles
it in favour of line 47: ratified-text is SIGNED/current and untouched.
⚠ **COST IF UNFIXED, stated small because it is small:** a reader of s.0 concludes `3.0.0_SA_CVO~Z`
owes a re-sign it does not owe, and chases a signature that is not outstanding. **No constraint, bar,
sequence or outcome is affected.**
⭐ **AND IT IS THE v0.5 CHANGELOG SHAPE RECURRING ON THE SAME DOCUMENT** -- a summary line carrying a
claim the authoritative section corrects. Last time the summary was stale by omission; this time the
correction and the stale claim shipped **in one commit**, which is faster and harder to catch.

### VERDICT: SIGN

**The defect is one warning sentence inside an addendum whose four substantive items are correct and
well-grounded.** Refusing would hold round 4's `FWD-4`/`FWD-6` cells -- the frontend Andrew ordered by
name -- behind an internal inconsistency in a sentence about which signature is owed. Proportionality
is the call, exactly as at the "three methods" label in section 9.
**RESIDUAL for `1.0.0_SA_CTO~Z`, one line, at the next amendment:** strike or correct line 43 to match
line 47. Header-only, re-opens nothing.

### ON THE OTHER THREE ITEMS

- **Item 3 is the one with teeth and it is correctly stated:** a bar written as *"confirm the weight
  zeroes in the allocation dict"* **returns the same answer before and after a retag** and therefore
  cannot gate it -- and `AT3-s-5`, the gating bar, reads that paragraph. That is the
  cannot-discriminate criterion class caught in a live gating bar, which is where it matters most.
- **Item 4's zero is recorded WITH ITS EXPIRY** -- 189 rows, zero candidate members, and the condition
  that flips it. **A zero recorded without the condition that ends it is the same defect as a
  criterion that cannot discriminate**, and the addendum says so itself.
- **Item 2** is the qualification that prevents item 1 recurring.

**Retag stays NO-GO. The positioning deploy stays conditional on a two-seat never-widen sign-off that
has not landed. Portal frozen. Nothing here grades any outcome REALIZED.**

---

## 12. THIRTEENTH REVIEW -- v0.6 correction, brief half `fb858d401` @`ded02d9a9c`: SIGN

**Scope:** section 11's residual, fixed. One warning line -- *"RE-OPENS BOTH L4-R HALVES"* -> *"RE-OPENS
THE BRIEF HALF ONLY"* -- plus a note stating what the line used to say and why it was wrong. **No
constraint, bar, sequence, surface or outcome moved.** `prd_version` deliberately stays v0.6: the
signature binds to the HALF HASH, not the version string, which is the whole reason that guard exists.
Ratified-text half untouched and still SIGNED/current.

### ⛔ AND MY OWN CALL IN SECTION 11 WAS WRONG

Section 11 said the fix was *"header-only, re-opens nothing."* **IT RE-OPENS THIS HALF, and
`1.0.0_SA_CTO~Z` measured it before relying on it.** `s.0 ADDENDUM v0.6 ...` has a heading whose FIRST
WORD is neither `ENDPOINT` nor `CONTRACTS`, so `half_of_section` maps it to the **BRIEF** half. The
gate went STALE at `fb858d401` exactly as it should have.
>> **THE ERROR WAS A WORD COLLISION AND IT IS WORTH NAMING: Rule 27's "a header-only bump re-opens
   nothing" means the PRD_HEADER JSON BLOCK. I read "header" as "a section heading near the top of
   the file." Two different objects, one word, and the sentence reads correctly under both.** <<
⛔ **AND I HAD MEASURED THE CORRECT MAPPING MYSELF HOURS EARLIER** -- the section-to-half enumeration
run for the FWD coverage check printed `0. THE VERSION HAZARD -> brief`, which is the same shape as
`s.0 ADDENDUM`. **Having the measurement did not stop me asserting its opposite**, because the claim
was made from a remembered RULE rather than from the measurement sitting in my own output.
⭐ It is also the class this document keeps producing, now aimed at me: **a claim about what the gate
will do, made without asking the gate.** The seat that has spent the night insisting on measured
gate-states asserted an unmeasured one in a review.

### VERDICT: SIGN

The correction is right, it is scoped to one line, and it states its own history rather than editing
the error away. **Timing is the cheap window and `1.0.0_SA_CTO~Z` named it:** round 4 is already CUT
at 19 orders, so LIMB 6 has no pending newly-added order to refuse and this re-sign blocks nothing
that exists today.
⭐ **THE TRANSFERABLE LINE IS THE CTO's AND IT IS THE BEST STATEMENT OF TONIGHT'S MOST-REPEATED
DEFECT:** *"Correcting a rule is not finished until every place that RESTATES it has been re-read -- a
fix scoped to where the error was noticed leaves its own restatements standing."*

Retag **NO-GO**; positioning deploy conditional on a two-seat never-widen sign-off that has not
landed; **portal frozen**; nothing graded REALIZED.
