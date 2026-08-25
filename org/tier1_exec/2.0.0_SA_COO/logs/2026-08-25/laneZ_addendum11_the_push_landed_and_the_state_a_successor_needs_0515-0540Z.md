# 2.0.0_SA_COO~Z — ADDENDUM 11: the push landed, and the state a successor needs (0515–0540Z)

**archetype:** COORDINATE · **secondary:** VALIDATE, SCRIBE
Continues `laneZ_addendum10_...md` @e0a6ad24f8. **Weighted toward STATE, not narrative — the earlier
ten carry the story.** **Zero crons, whole session.**

---

## 1. ▶ STATE OF PLAY — READ THIS FIRST

```
DATA HALF      DELIVERED AND SERVED
  platinum/etfs/positioning_data.json  126,863 B @04:53:51Z  vid vJ1OASSl
  169 distinct securities: 161 @8/8 · 2 @7/8 · 1 @6/8 (SALXX, missing YTD+1Y) · 5 @0/8
  177 of 187 holding rows @8/8 · 1,442 filled values
  alloc reconciles to each book's OWN holdings total: 99.80 · 99.51 · 100.01 · 99.99

FRONTEND HALF  MERGED + PUSHED, PROMOTE IN FLIGHT
  origin/DEV 063ff4d7 -- CARRIES THE FIX (753b62a0 remote=1, spread confirmed)
  local DEV 0 ahead / 0 behind. Nine commits now have a second copy.
  origin/PROD 8a96c916 -- FIVE DAYS OLD, NO ETF ADAPTER AT ALL

STILL TRUE     *** 13:00Z IS THE PRODUCTION NUMBER. Tonight's publish was THE PROOF. ***
               11:00Z is a CONFIRMATION, not a dependency (CTO~Z's 04:35Z pull supplied 08-24).

PARKED         ICT · MER · 2602335D · RBGLD -- one identifier workstream, SIX independent surfacings
               sector-vs-geography axis treatment (surface the failure vs absorb it) -- product call
               sub-1Y-fund rendering: PFDE/PFOE 1Y blank BY INCEPTION (launched 2025-12-31)
               SALXX YTD/1Y: UNFILLABLE by any pull -- same-class control (FXFXX has all 3 dates)
CLOSED         Phase 2 deep backfill -- UNNECESSARY. 1,569,204 rows -> 16,265 (1.0%).
```

---

## 2. ✅ THE PROMOTE GATE, AND WHY IT WAS SHAPED THAT WAY

```
git show origin/DEV:src/pages/Positioning/shared/etfAdapter.ts | grep -q '\.\.\.h\.returns'
   HIT  -> promote      MISS -> wait for the push
```
⛔ **`0.0.0_AB_MSTR~Z` caught that a promote cuts from `origin/DEV`, not the working tree — so a cut
at 05:30Z would have shipped to PROD the exact three-key defect Andrew watched get fixed at 05:06Z.**
⭐ **AND IT WOULD HAVE PASSED ALL SIX LEDGER LEGS: parity diff empty, CI green, tag peels, pointer
correct, teardown clean. THE PROMOTE MACHINERY CANNOT SEE A COMMIT THAT IS NOT ON THE BRANCH IT CUTS
FROM.** Nobody would have caught it afterward.
✅ **I FENCED MY OWN HOLD TO ONE MECHANICALLY-CHECKABLE CONDITION and said so explicitly: not held on
the retrieval finding, the identifier workstream, SALXX, re-verification, or my confidence.** >> **A
HOLD ACCRETES JUSTIFICATIONS IF YOU LET IT — each addition feels like diligence and the aggregate
becomes unliftable.** << **Discharged at 05:39Z by the grep, with no COO in the loop.**
⭐ **My warning to the DT seat came back QUEUED — no live session — so the protection was a message
nobody had read. THE FIX WAS NOT TO RACE THE RUNNER BUT TO REMOVE THE REASON TO WARN: get the
commits onto the branch and the promote is correct whenever it fires, read or unread.**

---

## 3. ⛔ MY DEFECTS THIS STRETCH — AND #39 IS THE WORST OF THE NIGHT

| # | defect | caught by |
|---|---|---|
| 38 | **My registered broker summary was hours stale** — still describing ETFS_INGEST round-1 dispatch, a different project. Any seat reading it to learn what the COO was doing got a confidently wrong answer | reading the live roster for another reason |
| 39 | **I fixed that stale summary by writing a NEW one that mixed vintages** — the 04:53Z SIZE beside the 04:45Z BREAKDOWN ("105 at 8/8", stale by one publish) | `3.0.0_SA_CVO~Z`; I re-derived it |
| 40 | Quoted "seven portal commits" from a message while the tree said eight | my own `git` read |

>> **#39 IS THE SHARPEST FAILURE I HAD TONIGHT: I COMMITTED A CROSS-VINTAGE MIX INSIDE THE ARTIFACT
>> I WAS REPAIRING FOR BEING STALE — thirty-three minutes after correcting another seat for exactly
>> that error. THE MECHANISM: I carried the vintage forward on the field I RE-READ and not on the
>> field I REMEMBERED. Re-measuring one number does not refresh the ones beside it, and a
>> PARTIALLY-REFRESHED RECORD READS AS FULLY CURRENT.** <<
⭐ **#38's general form is worth more than the instance: NOBODY READS THEIR OWN SUMMARY. It is a
derived value stored apart from the work that derives it, true when written, and invisible to its
author by construction — the night's defect class, on the record every other seat uses to model you.**

---

## 4. ⭐ THE ONE-LINE DESIGN DECISION THAT MADE TONIGHT SURVIVABLE

```
etf_positioning_gold.py:589-592
  if not need or not set(need).issubset(have):  continue   <- INCOMPLETE -> NULL, never computed
  if sel.isna().any():                          continue   <- second guard, same direction
```
>> **THE PRODUCER REFUSES TO COMPUTE RATHER THAN COMPUTE BADLY. A dropped row makes a window NULL; it
>> can never produce a number over a partial series.** << ⭐ **That converts a retrieval defect from
*a plausible wrong return on a client page* into *a visible absence* — and it is why CTO~Z's
range-query finding, real and serious, could not hold the promote.** **DS~Z chose it earlier; it paid
off tonight under four separate failures.**

---

## 5. WHAT I WOULD TELL THE NEXT COO

⛔ **SAY THE QUALIFIER.** Five errors tonight, not one a wrong fact: *landed WHERE · deployed but
PUBLISHED · stale BY WHICH CALENDAR · counted in WHICH TREE · confirmed ON WHICH SURFACE.* Each was a
true statement missing the word that made it actionable.
⛔ **A SOVEREIGN CONFIRMATION NAMES A SURFACE.** Andrew's *"full performance for everything"* was a
LOCAL RENDER. Four seats reported a frontend fix as delivered on the strength of it while it sat on
zero remote branches. **His approval is the one input nobody re-examines — which is exactly what
makes it dangerous.**
⛔ **COUNT WHAT YOU GENERATE, NOT JUST WHETHER IT IS RIGHT.** Twice tonight six seats produced correct,
well-founded analysis while the deliverable sat — once a 538-file ledger census I generated, once 78
messages in three hours to the single executor of both asks. **Both times every individual act was
defensible.**
⭐ **AND THE COUNTERWEIGHT, SO THIS DOES NOT READ AS ONLY FAILURE: every defect above was caught,
most within minutes, and most by the seat that authored it.** DS~Z filed three of the six carrier
instances against themselves; DE~Z filed the adapter defect against code they wrote that morning;
CTO~Z posted a control instead of a mechanism they believed; MSTR~Z owned moving an artifact under
four measuring seats. **A fabric that self-corrects this fast can afford to move this fast. The two
properties are the same property.**
