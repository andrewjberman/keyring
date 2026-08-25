# 2.0.0_SA_COO~Z — ADDENDUM 10: the render defect, the six-instance class, and my falsified hypothesis (0455–0515Z)

**archetype:** COORDINATE · **secondary:** DIAGNOSE, VALIDATE, SCRIBE
Continues `laneZ_addendum9_...md` @179295a4dd. **~55 commits this session.** **Zero crons, whole session.**

---

## 1. ✅ ANDREW CONFIRMED THE DELIVERY AT THE RENDER — THE STRONGEST VERIFICATION AVAILABLE

> Andrew ~05:06Z, VERBATIM: *"We now have full performance for everything but still missing SALXX YTD
> and 1Y."*

⭐ **`0.4.0_DE_ClientPlatform~Z`'s adapter fix was confirmed BY THE SOVEREIGN ON HIS OWN SCREEN, not
by any of us at a diff.** Every ETFS_POSITIONING ask he raised tonight is now closed except one
security's two windows, and that one has a measured, controlled, permanent answer.

---

## 2. ⭐⭐ THE RENDER DEFECT — AND IT IS THE SIXTH INSTANCE OF ONE CLASS TONIGHT

```
etfAdapter.ts:90-96  @origin/DEV d43b88c5   authored 2026-08-24T08:29:56-04:00 by DE~Z
    returns: h.returns ? { QTD: ..., YTD: ..., '1Y': ... } : undefined
```
**It CONSTRUCTS a three-key object rather than passing `h.returns` through. 1D · WTD · MTD · 1M · 1Q
are dropped AT THE ADAPTER.** It explains every observation at once: three render, five blank, the
three match TO THE DECIMAL (copied verbatim), and `current_holdings` is absent from the artifact yet
present at runtime **because this adapter builds it.**

⭐ **THE VOCABULARY HAD THREE CARRIERS AND THE INVISIBLE MIDDLE ONE TRUNCATED (DS~Z):**
```
PRODUCER   RETURN_WINDOWS = 8                    declares 8
ADAPTER    QTD · YTD · 1Y                        TRUNCATES to 3   <- nobody reads this layer
COMPONENT  "Backend provides ... (8 periods)"    expects 8, IN A COMMENT
```
>> **BOTH ENDS AGREED AND SAID SO. Only the middle disagreed.** <<

### The class, six instances, six layers, one night
```
1  alloc_fixed_income: 0.0      TRUE BY CONSTRUCTION until a Fixed Income class existed
2  vocab_size == 12             true until the vocabulary widened
3  segment.sector sort_keys     discarded an order that existed one file over
4  ledger header Status: OPEN   true until the body recorded CLOSED
5  history_window_end           a copy of the as_of that READS as coverage
6  etfAdapter 3-key allowlist   RIGHT at 08:29Z; producer gained five windows at 04:19Z
```
⛔ **EVERY ONE WAS CORRECT WHEN WRITTEN AND NOT ONE HAS A DIFF ON THE DEFECTIVE LINE.** Invalidated
*from a distance* by a capability appearing elsewhere — so no review of the breaking commit catches
it and no test fails.
⭐ **AN ALLOWLIST IS THE WORST FORM: it encodes a snapshot of ANOTHER component's capability, and that
component has no idea it exists.** DE~Z's own line: *"an enumerated adapter field is a FILTER that
does not grow with its source, and it fails SILENTLY rather than loudly."*
⭐⭐ **AND THE REMEDY PRINCIPLE UNIFIES TWO OF TONIGHT'S DEFECTS: REMOVE THE CARRIER, DO NOT SYNC IT.**
`+5 keys` and `spread` are both one line and ship in thirty seconds — **same cost, different
half-life.** Syncing leaves the divergence surface intact and adds a discipline that must hold
forever; **the spread retires the failure mode.** Same for the ledger header: DERIVE it, do not
remember to update it.

---

## 3. ⛔ MY DEFECTS THIS STRETCH — AND #37 IS THE INSTRUCTIVE ONE

| # | defect | caught by |
|---|---|---|
| 36 | **First measurement printed `book-1Y_missing = all 8` on all four books** — reads as *every book-level return is null.* **There is no `returns` field at book level at all**; my extraction defaulted a missing key to `{}` and rendered ABSENCE-OF-FIELD as ABSENCE-OF-DATA | the claim being too alarming to send unchecked |
| 37 | **The bond-calendar hypothesis** — Columbus Day + Veterans Day, SIFMA closed, NYSE open, money-market fund on the wrong calendar. **FALSIFIED: FXFXX is the same fund class and HAS all three dates** | `1.0.0_SA_CTO~Z`'s same-class control |

>> **#37's LESSON IS NOT "I WAS WRONG." I wrote *"two of three fit and the third does not, which is
>> exactly the shape that should slow me down"* — CORRECT, AND PASSIVE. THE NON-FITTING DATE WAS NOT
>> A CAVEAT, IT WAS THE EXPERIMENT.** `2026-01-26` has no closure, so *market-closed* was already
>> refuted for a third of my own evidence — **and the discriminating question, *does another fund of
>> the same class have these days?*, was ONE CALL AWAY. I had everything needed to design the control
>> and published uncertainty instead of resolving it.** <<
⭐ **CTO~Z held the identical hypothesis and posted the CONTROL instead of the MECHANISM. That is a
habit, not an insight, and it is the difference between the two of us on this one.**
⚠ **#36's uncomfortable half: what saved me was the SIZE of the claim, not a control. A less dramatic
wrong number would have shipped.**

---

## 4. ✅ SALXX — A COMPLETE ANSWER, NOT A DEFERRAL

```
SALXX short exactly 3 dates: 2025-10-13 · 2025-11-11 · 2026-01-26
   YTD  need 161 days, missing 1 (2026-01-26)   <- ONE absent Monday nulls a 161-day window
   1Y   need 251 days, missing 3
CONTROL  FXFXX (same govt money-market class) HAS ALL THREE.  AAPL (equity) has them.
```
>> **SALXX YTD AND 1Y CANNOT BE FILLED BY ANY PULL — the vendor has no print for that fund on those
>> days, and a same-class control proves it is neither a market closure nor our retrieval.** <<
✅ **`issubset` (complete coverage or null, no partial credit) is CORRECT and nobody should soften
it.** ✅ **MSTR~Z's source read stands and is true: `lib/trading_calendar.py` IS NYSE-only, no SIFMA
branch, controls firing on Thanksgiving/Christmas — true, and not the cause here.**
⭐ **CTO~Z's throwaway detail is the keeper: `FXFXX 2025-10-13 = 0` is a REAL ZERO, not a missing row.
Different facts, IDENTICAL in any summary reporting "no return" — only the raw vendor response
distinguishes them. Tonight's null-vs-zero rule, one layer further upstream than we had been applying
it.**

---

## 5. ⛔ THE STALL, AND CTO~Z NAMED THEIR OWN PART IN IT

At 05:04Z: *"two small items are stalled while six seats reconcile numbers nobody disputes."* Measured
then: adapter still 3 windows, `:895` still dropping `None`, **zero portal commits in fourteen
minutes.** ⭐ **CTO~Z owned the trigger — they had republished the artifact twice mid-measurement, and
the reconciliation traffic was real work caused by their speed.**
⛔ **MY PART: I sent a synthesis at 05:06Z, two minutes AFTER their stop-reconciling call. THE RIGHT
ACT WAS A MEASUREMENT, NOT A MESSAGE — and when I ran it, both items had already shipped
(`753b62a0`, and `:895` now reads `if h["sub_asset_class"]:` with the reasoning in-comment).**
**Third time tonight the fabric produced correct, well-founded analysis while the deliverable sat.**

---

## 6. STATE

```
DELIVERED   both asks, CONFIRMED BY ANDREW AT THE RENDER
ADAPTER     753b62a0 -- five windows restored; DE~Z fixed code they wrote this morning
:895        residue guard removed; is_cash no longer decides what is PUBLISHED
SALXX       ANSWERED: unfixable, controlled, permanent. Not a deferral.
PHASE 2     CLOSED as unnecessary -- 1,569,204 rows -> 16,265 (1.0%) on Andrew's display-ceiling read
13:00Z      *** STILL THE PRODUCTION NUMBER. Tonight's publish was THE PROOF, NOT THE PRODUCT. ***
PARKED      ICT · MER · 2602335D · RBGLD (six surfacings) · sector-vs-geography axis treatment ·
            sub-1Y-fund rendering (PFDE/PFOE 1Y blank by inception)
```
⭐ **The night's best outcome is work we did NOT do: a 1.57M-row vendor pull retired by one question
about what the page actually displays. It is invisible in every artifact, which is why it is written
here.**
