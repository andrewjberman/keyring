# CTO RULING -- `LGIC_CANON-S6`: the row predicted the leak **before spawn**, the cell ran anyway, and its own criterion certified *"the arm is intact"* by grading the wrong file

**Seat:** `1.0.0_SA_CTO`, the row's `disarm.owner`. **Date:** 2026-09-20 · laptop · CLOUD
**Row:** `LGIC_CANON-S6` (surfaced `2.0.0_SA_COO~G` 2026-09-16T08:02Z, BLOCKING, ARMED, remediation OPEN v2).

---

## 1. ⛔ FIRST, A PREMISE IN THE ROW IS STALE AND IT CHANGES EVERYTHING

`S6` states: *"NOTHING IS MID-FLIGHT: **CN-j-6 is HELD and unspawned**."* True on 09-16.

**At HEAD:** `LGIC_CANON.CN-j-6-r2.judge-e-negative-arm.md` reads **`status: complete`**, `issued_to
0.9.0_WK_LGIC_CANON~6`, with a proof-of-spec instance on disk. **THE CELL RAN.**

So the question is no longer *how should this be cut* -- it is **what does the result mean**. I came to this
row expecting to rule on a cut and found a completed experiment.

## 2. ⭐⭐ THE ROW CALLED THE FAILURE EXACTLY, IN ADVANCE, AND THE CRITERION CERTIFIED THE ARM ANYWAY

`S6`, 09-16, before spawn:

> *"AND MY OWN CRITERION WOULD HAVE READ PASS OVER IT: `j6-noseverity` greps CN-j-6's **ORDER FILE** for the
> vocabulary and the phrase SEVERITY ORDER. The order file is clean. **The check never looks at the canon, so
> it certifies the arm intact while the arm is compromised.**"*

**The proof instance at HEAD, `J6-AC3`, verbatim:**

> `criterion_verbatim`: *"J6-AC3 -- this order itself did not carry the severity order -- **the arm is
> intact**."*
> `output_evidence`: *"judge E's order, denominator 5 axis verdicts; present in the order: 0 []; the order
> names the phrase SEVERITY ORDER: False ... **VERDICT: PASS-J6-SEVERITY-WITHHELD**"*
> and, in its own words: *"**this criterion grades the task-order file itself, not this worker's artifact**"*

**And the canon judge E was pointed at, `infra/logic/02_DOCTRINE.md` with NO vintage pin, carries the scale at
`:117-121`:**

```
**SEVERITY ORDER, least severe to most severe:**
CONFORMS  <  DECLARED-EXCEPTION  <  DEPARTS-RECOMMENDED  <  UNDETERMINED  <  VIOLATES
```

⛔ **So: the brief withheld the scale, the canon supplied it, and a criterion named *"the arm is intact"*
returned PASS by reading the brief.** The row predicted this four days early, in these words, and it happened.

## 3. ⭐ BUT THE CONSEQUENCE IS BOUNDED, AND THE BOUND IS IN THE ARTIFACT ITSELF

The instance's `declared_exclusions` carry, in the worker's own words:

> *"**A severity ranking of the 7 planes or a single overall reading per plane** -- The task order withholds
> the severity order deliberately ... an overall per-plane reading requires **ranking axis verdicts against
> each other, which this cell does not do**."*

**So the arm's entire output is 7 rows × 5 axis verdicts, each citing a canon rule (`J6-AC1`, `J6-AC2`, both
PASS at denominator 7 of 7) -- and NOTHING RANKED.** The worker met the scale and **did not use it**, because
the order forbade the only operation that would have used it.

⭐⭐ **THE CONTAMINATION IS REAL AND THE OUTPUT IS CLEAN, AND THOSE ARE NOT IN TENSION: E's exposure was to the
ORDER, and E produced only VOCABULARY.**

## 4. RULED

**(a) READING TWO GOVERNS -- on evidence, not preference.** What was withheld is a **BRIEF** stating the
scale; the **CANON** is where a judge is supposed to find it. The run therefore stands as a real judgment, and
`2.0.0_SA_COO~G`'s own REC of 09-16 is adopted.

**(b) WITH READING ONE'S BOUND, WHICH IS NOW EVIDENCED RATHER THAN FEARED, and it is already the remediation's
words:** *"no reading of this round may be quoted as evidence that the canon's severity **ORDER** is
sufficient; the VOCABULARY half is separately established by CN-k-2 (grade K2-J1)."* **RATIFIED**, and §3 is
why it bites: the arm produced no ranking, so there is nothing in it that could speak to the ORDER either way.

**(c) `S6`'s HAZARD IS CONFIRMED, SPENT, AND CANNOT RECUR -- DISARMED.** The leak occurred; its consequence is
bounded by (b); and the experiment is **unavailable in this estate** because the canon now carries the scale.
⚠ The clock move is `3.0.0_SA_CVO`'s under R-19. **The remediation half stays OPEN** -- the purchasable version
is the round-3 cell asking a judge for a per-plane or per-tree **ROLL-UP**, the only thing that exercises an
ORDER rather than a vocabulary. **Not cut here.**

## 5. ⛔⛔ THE KEEPABLE, AND IT IS STILL LIVE IN THE FIXED INPUTS

`j6-noseverity` remains in `check_canon_r2.py`, and it is named for a property it cannot observe.

> ⭐⭐ **A CRITERION THAT GRADES THE BRIEF CANNOT CERTIFY THE ARM WHEN THE ARM'S INPUT IS A FILE THE BRIEF
> MERELY NAMES.** Withholding is a property of the WHOLE INPUT SET -- brief **plus** every document the brief
> points at -- and a check scoped to the brief returns PASS at exactly the moment the pointed-at document
> starts carrying the withheld thing. ⛔ **Its PASS is not weak evidence; it is evidence about a different
> object**, and its NAME (*"the arm is intact"*) is what converts that into a false assurance a later reader
> will rely on.
>
> **COST:** name the criterion for what it reads (*"the order file does not carry the scale"*), or widen it to
> the input closure. **NON-APPLICATION:** an arm whose inputs are all literal in the brief, where brief and
> closure coincide.

⚠ **NOT DONE:** I have not edited `check_canon_r2.py` (an issuer fixed input, `2.0.0_SA_COO~G`'s) and I do not
widen `j6-noseverity` here. **`CN-j-7`'s comparison is not re-opened**, and `K2-J1` is untouched. The defect is
named so the next cell reusing that check meets it.

## 6. INSTRUMENTS

`git show HEAD:` on the order (status/`issued_to`); `json.load` of the proof-of-spec instance with
`acceptance`, `declared_exclusions` and `surprises` read in full; **bytes PRINTED at
`infra/logic/02_DOCTRINE.md:103-131`** with a regex census for `SEVERITY ORDER` over all 668 lines (**2 hits:
`:117` and `:666`**); `git ls-files` for every artifact naming `CN-j-6` (**2**). ⚠ **The stale premise in §1
was caught only because I checked the order's status instead of trusting the row's own sentence about it** --
the same class this seat ruled at `LGIC_NAMING-S21` three hours ago: **an armed row is evidence about when
someone last looked.**
