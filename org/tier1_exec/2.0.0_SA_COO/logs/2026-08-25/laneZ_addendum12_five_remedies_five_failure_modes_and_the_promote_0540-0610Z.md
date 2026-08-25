# 2.0.0_SA_COO~Z — ADDENDUM 12: five remedies, five failure modes, and the promote (0540–0610Z)

**archetype:** COORDINATE · **secondary:** VALIDATE, SCRIBE
Closing record. Continues `laneZ_addendum11_...md` @7a128af90a. **Zero crons, whole session.**

---

## 1. ✅ DELIVERED — AND FOR THE FIRST TIME TONIGHT I CAN NAME A SURFACE FOR BOTH HALVES

```
FRONTEND   origin/PROD  d9a98bcc  @2026-08-25T01:47:35-04:00
           "merge DEV->PROD: v2.1.165 -- ETFS_POSITIONING goes to ..."
           was 8a96c916 @2026-08-20 -- FIVE DAYS OLD, NO ETF ADAPTER AT ALL
           `grep '\.\.\.h\.returns'` on origin/PROD -> PRESENT. All 8 windows reach the panel.
DATA       platinum/etfs/positioning_data.json  126,863 B @04:53:51Z  vid vJ1OASSl
           169 distinct securities: 161 @8/8 · 2 @7/8 · 1 @6/8 (SALXX) · 5 @0/8
```
⭐ **THE ETFs PRODUCT IS IN PRODUCTION FOR THE FIRST TIME.** The fix Andrew watched at a LOCAL RENDER
at 05:06Z is on the branch every viewer gets, ninety minutes later.
⚠ **`git tag --points-at origin/PROD` is EMPTY.** Rule 6 wants `{pipeline}-v{X.Y.Z}`; the merge
SUBJECT says `v2.1.165`. **A version named in a commit message is not a tag** — the qualifier problem
on the last leg of the night. DT's to close or declare N/A.

---

## 2. ⭐⭐ THE SALXX CHAIN — FIVE REMEDIES, FIVE FAILURE MODES, NONE SHIPPED

Andrew asked for one row to be recapitalised. **Every obvious remedy was wrong, and each presented as
success.**
```
1  fix the row only          NO EFFECT -- producer takes silver's raw string      (DE~Z)
2  wire producer -> bd-securities   142 OF 150 NAMES WORSE, 0 BETTER              (DS~Z; MY PROPOSAL)
      "Apple Inc" -> "APPLE INC COM" on his page. The field is named
      `asset_name_raw` AND IT IS RAW -- I quoted the identifier twice without reading it.
3  seed etf-classifications now     writes `name = "SALXX"`, worse than today     (DS~Z)
      seed:62 `ETF_NAME_OVERRIDES.get(ticker, ticker)`; SALXX absent from the 115
4  title-case the all-caps          `Bp Plc` · `Gsk Plc` · `Mplx Lp`              (CVO~Z)
      BP/GSK/MPLX are ACRONYM COMPANIES. All-caps is NOT a defect class.
5  wire producer -> etf-classifications   0 OF 7 COVERAGE                         (DS~Z, on their OWN act)
      116 HELD-ETF rows; all 7 all-caps names are common stocks or MMFs
```
>> **EVERY ONE CAUGHT BY THE SEAT THAT OWNED THE SURFACE IT WOULD DAMAGE — AND #5 BY THE SEAT ABOUT
>> TO BUILD IT, BEFORE WRITING A LINE.** <<

### The two structural findings under it
⛔ **(a) THERE IS NO NAMING AUTHORITY FOR NON-ETF HOLDINGS INSIDE AN ETF.** `bd-securities` is
raw-by-name; `etf-classifications` is ETF-scoped and does not contain them; the producer takes the
raw vendor string **because there is nothing else to take.** JPM, MRVL and VZ stay ugly on PROD.
⭐ **(b) NO FUNCTION CAN DO THIS.** *(CVO~Z)* `BP PLC` is correct and `VERIZON COMMUNICATIONS INC` is
not, and no string predicate separates them. **So a hand-curated 115-entry dict is NOT technical debt
— it is the only correct shape, and the design already knew.** The reflex on seeing 115 hand-written
entries is *"automate this"*; tonight is the proof that it cannot be.
✅ **AND THE PLAN STILL DELIVERS HIS ASK: DS~Z's own line — *"exactly ONE (SALXX) after act 1"* —
and that one is the one he ruled on.** The danger was never that it fails; it is selling a
one-security special case as a naming system. **CTO~Z ruled it does not ship tonight.**

---

## 3. ⛔ MY DEFECT — AND IT IS THE WORST NEAR-MISS OF MY NIGHT

**Remedy #2 was mine.** I wrote at 05:42Z: *"the producer must consume it"* — `it` = `bd-securities`.
>> **142 of 150 display names WORSE, 0 better, to fix a complaint about 6. On Andrew's page.** <<
```
04:23Z  bond-calendar mechanism        shipped as a HYPOTHESIS -- falsified by a same-class control
05:42Z  "wire it to bd-securities"     shipped as a REMEDY     -- and it was catastrophic
```
⛔ **BOTH TIMES I TOOK ANOTHER SEAT'S CORRECT FINDING AND BUILT AN ACTION ON IT WITHOUT MEASURING
WHAT THE ACTION WOULD DO.** The first cost a hypothesis. **The second was stopped only by DE~Z
self-correcting the table and DS~Z censusing the route unprompted — two independent saves on one bad
proposal of mine.** ✅ **My own banked rule, violated: *a finding and its remedy are two claims.***

---

## 4. ⚠ TWO CONDITIONS CARDED, NOT CHASED

⛔ **`origin/DEV`'s CI HAS BEEN RED SINCE BEFORE OUR MERGE** (`8ecb6b68` failed it too; one unused
type import in an ADVI file). ⭐ **A branch whose CI is permanently red cannot signal anything —
every future promote finds it failing, correctly concludes "not ours," and that is exactly how it
stays red forever.** Trivial fix, nobody's lane. **CTO~Z, daylight.**
⚠ **L3 GREEN AT THE LETTER:** only ONE of three workflows fires on a PROD push, and the build
validation runs on DEV — **so a headSha-scoped CI check on a PROD merge STRUCTURALLY CANNOT SEE THE
WORKFLOW THAT VALIDATES THE CODE.** *(MSTR~Z)* **Close L3 WITH that line, never as "all green."**

---

## 5. ⭐ THE THROUGH-LINE, STATED ONCE

>> **ALMOST EVERY DEFECT TONIGHT WAS AN INSTRUMENT ANSWERING CORRECTLY ABOUT A DOMAIN NARROWER THAN
>> THE QUESTION.** Six promote-ledger legs green on the wrong content · a CI check blind to the
>> validating workflow · a ledger census counting untracked files · `comp-iam` modelling `(action)`
>> not `(action, resource)` · a working-tree grep answering for the repo · `run_class` absent from a
>> report. **Not one was a false statement.** <<
⭐ **AND THE COUNTERWEIGHT IS THE REAL RESULT: nearly every one was caught by the seat that owned the
surface, most within minutes, many BEFORE the act.** DS~Z filed three carrier instances against
themselves and stopped their own act-3 before writing it; DE~Z found the adapter defect in code they
wrote that morning and corrected their own handoff two minutes after sending it; CTO~Z posted a
control instead of a mechanism they believed; MSTR~Z owned moving an artifact under four measuring
seats and caught the promote that would have shipped the defect Andrew watched get fixed.
>> **A FABRIC THAT SELF-CORRECTS THIS FAST CAN AFFORD TO MOVE THIS FAST. THEY ARE THE SAME
>> PROPERTY.** <<

---

## 6. STATE AT CLOSE

```
DELIVERED   frontend origin/PROD d9a98bcc · data 126,863 B @04:53:51Z  -- BOTH SURFACES NAMED
STILL OPEN  *** 13:00Z IS THE PRODUCTION NUMBER FOR THE DATA. Tonight's publish was THE PROOF. ***
            The scheduled fire has NOT been observed.
CARDED      SALXX naming (act 1 unwritten; 5 failed remedies documented) · no naming authority for
            non-ETF holdings · ICT/MER/2602335D/RBGLD identifier workstream (6 surfacings) ·
            sector-vs-geography axis treatment · sub-1Y-fund rendering · origin/DEV red CI ·
            missing PROD tag
MINE        12 addenda, ~59 commits, ALL ON origin. Inbox 0. MEMORY.md repaired + 6 new lessons.
            ZERO CRONS, WHOLE SESSION.
```
---

## 7. ✅ Z-S46 DISARMED — THE 13-MONTH RULE, RECORDED WITH ITS CONSTANT

**The rule minted tonight (from Andrew's display-ceiling read):**
> **PULL TO THE LONGEST WINDOW THE PRODUCT RENDERS, PLUS MARGIN — NOT TO WHAT EXISTS.**
> `compute_returns` caps at `1Y`, so **~13 months is the product's true data horizon.** It is what
> collapsed a 1,569,204-row vendor pull to 16,265.

⛔ **AND THE COUPLING, WHICH IS THE WHOLE POINT OF RECORDING IT HERE: the enforcing floor is
`HISTORY_LOOKBACK_DAYS = 400`, and it lives in a DIFFERENT FILE under a comment that truthfully says
it is NOT a business rule.**
```
THE RULE       "pull to the longest rendered window + margin"   <- this document, tonight
THE CEILING    compute_returns' longest window = 1Y             <- etf_positioning_gold.py
THE FLOOR      HISTORY_LOOKBACK_DAYS = 400                       <- a third file, comment says
                                                                    "not a business rule"
400 days correctly bounds a 1Y window with margin. NOTHING IS WRONG TODAY.
```
>> **THREE CARRIERS OF ONE DECISION, IN THREE FILES, AND THE ONE THAT ENFORCES IT DISCLAIMS BEING A
>> RULE. That disclaimer is honest and it is exactly what makes a future reader skip the line when
>> the ceiling moves.** << **If the product ever renders a window longer than 1Y, the rule says widen
>> the pull and the 400 silently does not follow.**
✅ **DISARM TAKEN: the rule now carries its own constant and its own coupling, in the same
paragraph, in the place the rule is written down.** *(`ETFS_INGEST-Z-S46`, OBSERVATION, surfaced by
`0.4.0_DS_ClientPlatform~Z`, disarm owner `2.0.0_SA_COO~Z`.)*
⚠ **NOT REMEDIATED and deliberately not: nothing is defective, no constant should move, and
consolidating three files tonight would be a change nobody asked for.** DISARMED ≠ REMEDIATED —
two states, two clocks.
