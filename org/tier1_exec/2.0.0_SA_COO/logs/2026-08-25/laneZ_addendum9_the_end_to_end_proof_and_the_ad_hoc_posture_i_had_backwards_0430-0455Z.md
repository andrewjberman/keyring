# 2.0.0_SA_COO~Z — ADDENDUM 9: the end-to-end proof, and the ad-hoc posture I had backwards all night (0430–0455Z)

**archetype:** COORDINATE · **secondary:** VALIDATE, SCRIBE
Continues `laneZ_addendum8_...md` @af1128ac80. **~54 commits this session.** **Zero crons, whole session.**

---

## 1. ⛔ THE SOVEREIGN POSTURE THAT REVERSED MY STANDING POSITION

> Andrew ~04:30Z, VERBATIM: *"Let's just run through this ad hoc as needed to clear it completely. I
> don't like the idea of waiting on scheduled publishes to prove something works, **I want to prove
> it works end to end with perfect numbers** and then and only then am I accepting of waiting on
> scheduled publishes just as a final confirmation."*

**PROVE AD HOC FIRST; THE SCHEDULE CONFIRMS.** I ruled the inverse at 03:16Z, 03:34Z and 04:23Z.

⛔ **AND THE ERROR IS SHARPER THAN "I WAS CAUTIOUS" — CLAUDE.md's OWN RULE HAS TWO HALVES AND I
CARRIED ONLY ONE:**
> *"**(a)** an ad-hoc run is a legitimate **QA INSTRUMENT** — fire one to test, exercise, or
> reproduce. **(b)** A PRODUCTION PIPELINE MUST HAVE A SCHEDULE."*
>> **I QUOTED (b) THREE TIMES AND NEVER (a). The permission sat in the same sentence as the
>> prohibition.** << *Same root as every failure I logged tonight — reading half of what I already
>> held — and this one cost the fabric hours of deferred proof.*
✅ **What survives, and it is the load-bearing half: NEVER#4 is RE-ORDERED, NOT DELETED. An ad-hoc
artifact is still never PRODUCTION EVIDENCE.** `0.7.0_AE_CloudOps~Z` stated it better than I did and
I adopted their words as the binding condition rather than paraphrasing: *"if we publish ad-hoc and
then call the job done, we have done the thing NEVER#4 forbids while quoting Andrew."*

---

## 2. ✅ THE LIFT — DECIDED ON MEASUREMENT, WITH THE ROLLBACK VERIFIED FIRST

```
opal-data-portal-v2  versioning ENABLED
ROLLBACK TARGET  gIvIcaCD2PCmWoMSTYyPdxosa3pDjKnx  122,825 B @02:50:38Z
lifecycle expire-noncurrent-versions-14d   <- recoverable 14 DAYS, not forever
```
⭐ **I checked rather than assumed — I had nearly carried this property over from `opal-data-etfs`,
which has NO versioning.** **My hold's original reason had EXPIRED and I said so explicitly: at
03:34Z both halves were invisible on the page; by 04:44Z they were not, and he was awake asking to
see them.** *A hold outliving its reason is the failure I logged twice tonight; this one was lifted
by measurement.*
⭐ **AE~Z REFUSED TO INFER MY HOLD AWAY from his words relayed through two seats, and asked for one
line. That is the no-inferred-gates rule run in the OTHER direction — declining to invent a LIFT is
the same discipline as declining to invent a HOLD, and almost nobody applies it symmetrically.**

---

## 3. ✅ THE PROOF — SERVED BYTES, AND THEY RECONCILE TO THE UNIT

`platinum/etfs/positioning_data.json` **125,915 B @04:45:15Z** version `sACIinjt6MH29at5W8EhhJ2nU3LDwfYB`
```
169 DISTINCT securities
  105   8/8 windows    full history
   58   2/8 (1D+WTD)   the archive gap   <- PREDICTED AS 58 BY CVO~Z **AND** DS~Z, INDEPENDENTLY
    6   0/8            ICT · MER · 2602335D · RBGLD · FXFXX · CASH&OTHER
  ---
  169  ✓
```
⭐ **THE 58 IS EXACT, PUBLISHED BEFORE THE RUN BY TWO SEATS ON TWO INSTRUMENTS.** ⭐ **AND THE 6 AT
0/8 ARE PRECISELY the four identifier failures plus the two cash sentinels — the population four
separate investigations converged on tonight, falling out of a FIFTH measurement without being
looked for.**
✅ **BOTH ASKS, ON THE SERVED BYTES:**
```
alloc_fixed_income  0.58 · 0.89 · 0.33 · 2.34     <- MY 03:15Z TABLE, EXACTLY
alloc_cash          0.00 · 0.00 · 0.03 · -0.02    <- INCLUDING THE NEGATIVE
cash+fi+eq == sum(holding weights):  99.8000 · 99.5100 · 100.0100 · 99.9900   ALL FOUR
sector members 10·11·12·8 ; IDVZ short by 2.6900 = ICT+MER EXACTLY, BY DESIGN (no "Other" bucket)
```
⭐ **`ETFS-TO1-AC8`'s invariant — buckets against the book's OWN HOLDINGS TOTAL, not against 100 —
holds to four decimals on all four books. That is precisely the criterion that would have FAILED ON A
CORRECT BUILD had I shipped the "sums to 100" version I first drafted.**

⚠ **105 ≠ 107 ≠ 109 AND NOBODY WAS WRONG:** both predictions were about the HISTORY CORPUS; the
artifact counts TODAY'S HOLDINGS UNIVERSE, and **PFDE/PFOE are the FUNDS — never holding rows, so
their inception boundary cannot appear in this count at all.** The sets differ by 4.

---

## 4. ⛔ MY DEFECT THIS STRETCH — CAUGHT ONLY BECAUSE THE RESULT WAS TOO ALARMING TO SEND

| # | defect | caught by |
|---|---|---|
| 35 | **First pass printed `book-1Y_missing = all 8 windows` on all four books** — which reads as *every book-level return is null.* **THERE IS NO `returns` FIELD AT BOOK LEVEL AT ALL**; my extraction defaulted a missing key to `{}` and rendered ABSENCE-OF-FIELD as ABSENCE-OF-DATA | the finding being too alarming to report unchecked |

>> **A fallback branch answering under the original label — my own banked trap, hit while verifying
>> someone else's work.** ⭐ **And the honest lesson is uncomfortable: THE THING THAT SAVED ME WAS THE
>> SIZE OF THE CLAIM, NOT A CONTROL. A less dramatic wrong number would have shipped.**

---

## 5. ⭐ WHAT WORKED, AND IT IS THE OPPOSITE OF HOW THE NIGHT STARTED

```
04:41Z  CVO~Z publishes the expected shape BEFORE the run   (109 long-window fills, 58 short)
04:44Z  DS~Z corrects it to 107 with a measured reason      (PFDE/PFOE inception 2025-12-31)
04:45Z  the run lands
04:51Z  measured: 58 EXACT, and the 105/107/109 spread explained by denominator
```
>> **A TWO-TICKER DISCREPANCY BETWEEN TWO SEATS WAS RESOLVED BY MEASUREMENT IN THREE MINUTES, BEFORE
>> THE ARTIFACT EXISTED — instead of becoming a discrepancy report after it.** << **Pre-registration
made a partial fill INTERPRETABLE: without it, `58 nulls` reads as "the fix failed." With it, it is
the predicted correct outcome AND the sizing number Andrew asked for at 04:09Z.**
⭐ **Phase 2's business case stopped being a projection and became a screenshot.**

---

## 6. STATE

```
DELIVERED  both asks, PROVEN END TO END on the served bytes, ad-hoc, run_class reported HONESTLY
13:00Z     STILL THE PRODUCTION NUMBER and still observed. The ad-hoc publish is THE PROOF, not the
           product. *** This is the condition that will be forgotten. ***
11:00Z     now a CONFIRMATION, not a dependency -- CTO~Z's 04:35Z pull supplied real 08-24 history
PHASE 2    HELD on Andrew's 04:09Z sizing qualification. The 58 IS the number.
PARKED     ICT · MER · 2602335D · RBGLD across five surfaces; the sector-vs-geography axis question;
           the sub-1Y-fund rendering question (PFDE/PFOE 1Y blank -- "most explainable null on the
           page and the least self-explaining")
```
