# AMGT_RESAPP -- ROUND 36 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-23 ~15:2xZ

**Inputs:** `3.0.0_SA_CVO~Z`'s L10 slug (msg 24763, `ADJUDICATION_v44` @`1500ced6b8`) over
`2.0.0_SA_COO~Z`'s packet @`12f98aa11d`, drain @`e452864e6a`, order terminal @`2c07e79688`.

**GRADE ACCEPTED.** 1 of 1 terminal. **PASS 9 / FAIL 0 / UNVERIFIABLE 0.** rc=0 VALID, 9/9 alignment,
**111 tests in the MERGED tree on the issuer's own instrument**, **11 of 12 permitted live HKEX fetches**,
**0 Bloomberg, 0 deletes.**

⭐ **THIS IS THE LAST CANONICAL ROUND ANALYSIS FOR THIS PROJECT.** Closer mode was adopted on
Andrew's word (@`79bc33a857`) while this round was in flight; **work in flight completes under its own
spec**, and this closes it properly rather than leaving a round ungraded at the CTO level.

---

## 1. ⭐ BOTH STACKED BLOCKERS CLOSED -- AND THE CVO MEASURED THEM RATHER THAN ADOPTING THEM

| blocker | round 35 | at HEAD |
|---|---|---|
| **A** | `stockId="00992"` -> `recordCnt=0` under every combination tried | ⭐ **AN ID-SPACE ERROR:** the internal predictive-search id, wired at `:1227-1257` from `activestock_sehk_e.json` (`:1238`). **`00992` -> 0, `2325` -> 1117**, every other parameter byte-identical |
| **B** | **5 of 5** return paths `passed: False` | ⭐ **10 paths, 9 `False` and ONE `True` at `:1445`** |

⛔ **AND THE SHAPE OF B's FIX IS THE PART WORTH KEEPING.** I measured in the round-35 addendum that step
5's `seeds` are written into a list whose only reader -- step 4 -- has already executed. **The fix did NOT
try to repair that ordering.** The winning path is consumed at `:1574-1575` and **the object is built from
`battery_extra`, not from the orphaned `seeds`.** ⭐ **The defect was ROUTED AROUND rather than "fixed",
which is correct: re-ordering the step list to make `seeds` readable would have moved a shared structure
for one step's benefit.**

## 2. ⛔ THE RULING -- `FWD-3` IS **UNBLOCKED IN MECHANISM, NOT REALIZED**

The route is **CAPABLE** of resolving. ⚠ **A live win additionally requires the newest filing for the name
to be an annual report on the day**, because the adapter inherits round 35's most-recent-filing selection.

⭐ **The worker NAMED that limitation rather than silently widening its own cell to fix it** -- which is
why limb 2 is fixture-proven and why this grade can be clean. **Evidence level, per closer-contract `:66`:
offline exercise plus live interface probe. NEVER actual end-to-end.** ⛔ **`FWD-3` grades REALIZED only
on a live end-to-end win, and nothing in this round claims one.**

## 3. ⭐ `Z-W128-S1` IS VINDICATED AT THE BYTES AND DISARMS **WITH ITS REASON**

> *"should not assume query-tuning alone resolves it"*

⛔ **It was right BECAUSE TUNING VARIES THE PARAMETERS AND THE PARAMETERS WERE ALREADY CORRECT.** A
tuning pass could have run forever and never found it. ⭐ **A row that is disarmed with its reason teaches;
one that is silently dropped teaches nothing, and this one earned the difference.**

⭐ **And AC0's POSITIVE CONTROL is what made `1117` interpretable** -- no `stockId`, `searchType=0`, a date
range, **`recordCnt 14376`**, taken BEFORE any conclusion about Lenovo. **Without it, `0` and `1117` are
two numbers from two guesses.** The order made that control mandatory and refused an unmeasured zero;
**that bound is why this round closed instead of producing a fourth half-fix.**

## 4. ⭐ THE GRADER RECORDED ITS OWN WRONG PREDICTION

`3.0.0_SA_CVO~Z`'s close log said *"AC4 passing while AC5 fails is the outcome that proves the cell's
design right."* **Both passed** -- AC4 on the fixture, AC5 on `run_battery` over the same fixture
(`status: RESOLVED`).

⭐ **The separation still did its job: AC5 was independently gradeable, and a broken propagation would have
failed it with AC4 green.** ⚠ **But the direction was called wrong, and the grader said so rather than
letting the record read as though it had called it.** ⭐ **A design that survives its author's wrong
prediction about it is better evidence than one that confirms it.**

## 5. WHAT THIS CORRECTS IN MY OWN RECORD

My round-35 analysis attributed the failure to blocker A alone, and my session-close log named "one blocked
dependency with two stacked causes." **Both are superseded** -- the causal addendum @`a9163407bc` and the
close-log supersession @`1fec2f5029`. ⚠ **Nothing further is owed there; this analysis is the confirming
read, not a third correction.**

⛔ **AND MY RECOMMENDATION TO ANDREW WAS WRONG.** I told him twice to PARK this route, the second time
calling it firmer than three hours earlier. **Round 36 reversed it.** He had not acted on it. **The rec was
reasonable on the evidence I had and still wrong, because that evidence was two seats' shared assumption
that a zero meant the issuer -- and what broke it was a control nobody had run.**

## 6. ⛔ ONE CARD ROW, AFFIRMED BY EVERY SEAT THAT TOUCHED IT

**DO NOT REMOVE `C:/tmp/wk-amgt-36-129`.** The **ten** `.scratch/r129/` scripts behind AC0-AC7 were
**REFUSED by `owned-paths-check`** and exist **ONLY there**. ⭐ **The issuer declined `safe-merge`'s own
closing advice for exactly that reason and that was the right call.** ⚠ **Third instance of the
`.scratch/**` gap and the FIRST to cost LIVE RESEARCH EVIDENCE rather than convenience.**
`0.0.0_AB_MSTR~Z`: a stronger row than the previous two.

## 7. WHAT IS NOT CLOSED

- **`rk-49`** stays parked. ⭐ **The PATH opened; the FACT did not** -- `filings/v1/992_HK_Equity/` still
  holds only `UNRESOLVED-SOURCE`, because this round was research plus a fixture and **never re-ran the
  live battery.** `2.0.0_SA_COO~Z` confirmed that on a DIFFERENT instrument than mine: none of AC0-AC8 can
  write that artifact. **Corroboration, not repetition.**
- **`AMGT_CORPUS` has never been graded by any L9** -- `2.0.0_SA_COO~X`'s measurement: ten `complete`
  orders, **eight judgment criteria NOT_EVALUATED, no slug.** `3.0.0_SA_CVO~Z` is the named successor
  reviewer and has started.

---

**ROUND 36 IS CLOSED**, and the project's canonical phase closes with it. ⭐ **Four rounds at or near zero
egress, and the one that spent (11 live HKEX fetches, a public regulator) bought the finding that ended a
three-round half-fix.**

-- `1.0.0_SA_CTO~Z`
