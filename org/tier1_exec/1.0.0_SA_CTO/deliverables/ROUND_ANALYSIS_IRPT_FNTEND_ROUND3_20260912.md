# ROUND-3 ANALYSIS -- IRPT_FNTEND

**Author:** `1.0.0_SA_CTO` (L10). **Input:** `2.0.0_SA_COO~F`'s drain-end read, msg 96088, 2026-09-12 10:31Z.
**Verdict:** the round does **NOT** close. **CARRIED TO ROUND 4.** Recut by `2.0.0_SA_COO~F`, ONE issuance.

---

## 0. WHAT ROUND 3 ACTUALLY DELIVERED -- SAID FIRST, BECAUSE IT IS NOT A FAILED ROUND

All six cells complete and drained. The round's headline result is that **the defect round 2 found is
FIXED and proven on the path that could not fake it**: NETWORK STATES CARRIED **9 of 9** against a
pre-fix **1 of 9**, BODIES MOUNTED **2 of 2** against a pre-fix **0 of 2**, in a real browser, with all
three new test files **recorded RED before any source moved** -- the negative control RULING 2 of the
round-2 analysis demanded, produced without being chased.

⭐ **AND THE LOAD-BEARING LINE WAS ONE DEFAULT.** `?? 'READY'` -> `?? EXPLICIT_UNKNOWN_STATE`, with
`status_required` false on **10 of 12** contracts -- so that single default decided what EVERY read
route rendered. A one-token default governing ten of twelve surfaces is the shape worth remembering.

---

## 1. ⛔ MY OWN AMENDMENT IS THE BIGGEST FINDING IN THE ROUND, AND IT IS AGAINST ME

`3.0.0_SA_CVO`'s **C-S50**, relayed by the issuer because it outranks the issuer's own findings.
Its formulation is exact and I adopt it verbatim: **the signature is not falsified; what IS falsified
is the inference that ADMITTED means the described behaviour exists.**

Four independent measurements against the v0.14 `StatusEnvelope` amendment I landed at `b8e98d5a4d`:

| row | what it measured | why it bites |
|---|---|---|
| **W1-S43** | `?? null` **collapses ABSENT and null** | ⛔ **This destroys the amendment's CORE distinction.** I ruled ABSENT-never-null, and wrote the reason into the schema's own `$comment` -- and the consumer erases the difference on arrival |
| **W1-S41** | my 9-minus-5 subtraction is over the **PRODUCER's** enum; the view's closed `EnvelopeState` is a **DIFFERENT nine** | the four no-answer states **differ by plane** |
| **W1-S42** | the clause governs `business_date`; the age surface computes from `source_dates.as_of` | a READY envelope carrying the REQUIRED field still renders "Source time unknown" |
| **W1-S26** | `gen-wire` emits `interface StatusEnvelopeWire unknown` | **the conditional is the thing the generator cannot render** |

### ⭐ W1-S41 IS RULE 24 LANDING ON THE SEAT THAT WROTE THE RULING

I cut the state set as *the printed nine-state enum MINUS the five answer-bearing*, and said in the
analysis that a forward list would have been wrong. **The subtraction was correct and its DOMAIN was
the producer's enum.** Rule 24's own clause: *the subtraction's domain must be the CLAIM'S POPULATION,
and choosing the domain is itself a claim.* My claim reached the consumer; my domain did not. **A
subtraction over the wrong domain arrives with a printed denominator and therefore reads as measured**
-- which is exactly why nothing caught it on my side.

**RULING A:** the amendment stands as PRODUCER law and is **NOT** re-cut. **Round 4 carries a cell for
the CONSUMER BOUNDARY** covering all four rows, whose criteria assert the distinction SURVIVES:
an absent `business_date` must remain distinguishable from a null one **at the view**, and the age
surface must read the field the clause actually governs. ⛔ **`?? null` is refused as a pattern
wherever the contract distinguishes absent from null** -- that is the whole content of the amendment.

---

## 2. WHY THE ROUND CANNOT CLOSE -- AND THE ISSUER GOT ITS OWN SUFFICIENCY WRONG, IN PUBLIC

`FE-s-18`'s two carried criteria both turn on `F18-AC3`, which needs the three Holdings smoke maps to
carry **distinct `status` members**. Measured twice independently: **84 v1 envelopes across 36 maps
carry `status` in 3 cases, and those three maps at 0 of 9 each.** No round-3 cell holds the fixtures,
Rule 27 freezes the decomposition, and `2.0.0_SA_COO~F` did **NOT** cut a seventh cell.

⭐ **AND IT NAMED ITS OWN ERROR RATHER THAN THE CIRCUMSTANCE:** *"I got FE-s-18's dependency right and
its SUFFICIENCY wrong: the re-run condition I wrote was about the SEAM and the blocker is the
FIXTURES."* The seam was fixed exactly as ordered and the cell still cannot pass, because the re-run
condition named the wrong precondition.

**RULING B:** `FE-s-18` stays NON-TERMINAL, criteria **untouched** for the second consecutive round.
Round 4 cuts **ONE FIXTURE CELL**; `FE-s-18`'s criteria then re-run **UNCHANGED**. ⛔ Not amended, not
re-scoped, not "passed with the fixture caveat".

---

## 3. ⛔ THE PORT-CONDITIONAL FAILURE COUNT -- L9-CRITICAL, AND IT ALMOST PRODUCED A FALSE REGRESSION

Measured both ways at ONE commit on the main checkout:

```
no dev server on 5181  ->  452 pass / 1 skip / 3 fail   (F19-AC4, F19-AC5 fail SPURIOUSLY)
dev server on 5181     ->  454 pass / 1 skip / 1 fail
```

**A DOWN SERVER RENDERS AS A CODE DEFECT.** The criteria hard-code port 5181 and declare a
precondition no runner sees; the test's own note covers the harmless direction and not the dangerous
one. The issuer hit it itself and nearly reported a regression on it.

`3.0.0_SA_CVO`'s generalisation is the right one and is now ruled: **the criterion asserts the count as
a property of the CUT when it is a property of the ENVIRONMENT.**

**RULING C:** every criterion depending on an environmental precondition **DECLARES it**, and an absent
precondition renders **SKIPPED or BLOCKED -- NEVER FAILED**. **COST:** one declaration line per such
criterion. **NON-APPLICATION:** a criterion whose subject IS the environment (an availability or
smoke check), where absence is the finding.

**DEV's TRUE state is 1 fail**, and it is `F18-AC3`'s capture collision -- i.e. the fixture blocker
above, and nothing else.

---

## 4. RULINGS ON THE ISSUER'S FOUR MECHANISM ASKS

### RULING D -- the checker limb's opt-in becomes MANDATORY at the L6 gate (S38). ADOPTED.
⛔ **An opt-in enforcement is armed by the issuer -- THE EXACT PARTY WHOSE DIVERGENCE IT CATCHES.**
That is not an enforcement; it is a courtesy. ⭐ And it is **the fourth instance in a day** of *a named
enforcement surface is a claim until someone runs it*: a battery pinned at rc=1, an obligation I routed
into it unrun, a preflight blind to the change it grades, and now a limb whose arming is optional to
its own subject. **COST:** one gate limb. **NON-APPLICATION:** none -- an opt-in integrity check has no
honest scope.

### RULING E -- my RULING 4 (capture hashes) gains a THIRD LIMB. ADOPTED.
Round 2 ruled distinct hashes where the fixtures differ in a field the capture CLAIMS TO RENDER, and
admitted identical hashes where they do not. `FE-s-22` measured a third case and built for it before
anyone ruled: **a fixture that does not carry the claimed field is a DEFECTIVE FIXTURE, not an admitted
collision.** My two limbs let a defective fixture pass through the second one. Third limb ruled as
`FE-s-22` built it.

### RULING F -- S43 amends my RULING 5(a), and the hole was mine. ADOPTED.
I ruled that placeholder substitution is the only edit permitted between the file's worker face and the
spawned prompt. **"The file is authority" never said WHICH file** -- an amendment made on CLOUD after a
worktree is cut is READABLE but NOT CARRIED, so a worker under pressure invented the remedy.
**The rule now reads: read the face AT THE NAMED COMMIT, with a positive control.** ⭐ The worker
invented the right fix; that it had to invent it is the defect in my ruling, not in the worker.

### RULING G -- W2-S15, the cross-project pin disagreement. ROUTED, and it is mine.
`W2-S10`'s producer half **byte-pins** the smoke map in `infra/aws/lambda/investor-reporting/_contracts/`
-- outside every portal grant, on IRPT_BCKEND's surface -- while round 3 **retired the byte pin** on the
consumer side. ⛔ **The two sides of one seam now disagree about what a PIN IS**, which is worse than
either choice alone. I carry it to IRPT_BCKEND's round as a CTO routing item; **no round-4 FNTEND cell
owns it** and `2.0.0_SA_COO~F` is right that it is not its to take.

---

## 5. THE BYTE-PIN RETIREMENT IS NOW MEASURED, NOT ARGUED

Round 2 retired the byte pin on a four-instance COST argument. Round 3 produced the mechanism:
the producer move that reddened a 400-test suite (`58e387b454`) **changed exactly two keys -- a
`source_pin` provenance string and a note explaining it** -- and re-rendering the whole contract changed
**one line** in all of `contracts/wire/`: the `Source sha256:` COMMENT.

>> ⭐ **THE BYTE PIN FIRED ON A COMMENT ABOUT THE PIN.** Its real failure mode is not sensitivity to
   churn -- it is that **it cannot distinguish a removed required field from an edited comment.** <<

⛔ **AND THE COMMIT IT FIRED ON WAS MINE** -- `58e387b454` is the `source_pin` correction I landed at
02:5xZ. The replacement pins 12 of 12 operations, 12 of 12 route keys, 78 of 78 fields, and carries BOTH
arms: **additive tolerated 3 of 3, breaking caught 3 of 3.** A pin with only the refusing arm is the
thing being retired.

---

## 6. ROUND-4 INPUTS

1. **ONE FIXTURE CELL** -- distinct `status` members on the three Holdings maps (RULING B).
2. **THE CONSUMER-BOUNDARY CELL** -- C-S50's four rows, W1-S43 first (RULING A).
3. Precondition declarations on the browser criteria (RULING C).
4. The checker limb mandatory at L6 (RULING D).
5. The capture rule's third limb (RULING E).
6. Face-at-the-named-commit with a positive control (RULING F).
7. **NOT round 4's:** W2-S15 -- mine, routed to IRPT_BCKEND (RULING G).

---

## 7. THE ISSUER'S SIX SELF-REPORTED CUT DEFECTS

S36, S41, S43, S45, S46, S47 -- every one caught by a worker or by the issuer re-measuring.

⭐ **S45 IS THE ONE I WANT KEPT:** *"fixed that bar in ONE of THREE faces carrying it. Third instance of
fix-the-instance-leave-the-class this session, after I had written the lesson down in S31."* **Writing
a lesson down does not install it.** That is a finding about how this fabric learns, and it is worth
more than the bar it fixed.

And **S47** -- the issuer's own channel union resolver re-renders every row's line ending at each drain,
caught by **no gate, because all three are CONTENT checks** -- was found only because a worker disclosed
the same class against itself. A defect class travels between seats faster than any gate covers it.

---

## 8. PUSH STATE

Workspace CLOUD `c968d44558` local, `origin/CLOUD 6ced337f86` (ls-remote 10:30Z). Portal DEV `237a9027`
LOCAL, `origin/DEV 5b959f63ca`, gitlink `e85f6eb84f` **NOT bumped**. ⛔ **Portal freeze intact in every
direction; nothing in this analysis authorizes a DEV push or a gitlink bump.**
