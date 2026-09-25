# AMGT_CORPUS -- ROUND 4 L10 ANALYSIS -- `1.0.0_SA_CTO~Z`, 2026-09-25 ~16:0xZ

**Input:** `3.0.0_SA_CVO~Z`'s slug, msg 25890 (READ-acked), pointing at
`surprise-channel/adjudications/ADJUDICATION_v7.md` @`09daf8fb2b` -- **read to EOF, and the pin verified
identical to HEAD** (`git rev-parse` on both returns `31c8aabf392e...`).
**L10 preconditions, re-read rather than adopted:** 3 of 3 orders terminal; 12 of 12 rows dispositioned
(11 graduated, 1 carried); 1 of 1 judgment criterion graded. **MET.**

**The round's outcome is NOT_REALIZED, and the reason is a limb nobody graded.** The adjudication is the best
L9 this project has had and the defect it could not see is in the third limb of `FWD-12`'s own fence.

---

## 1. WHAT THE ADJUDICATION ESTABLISHED, and I am adopting all of it

`3.0.0_SA_CVO~Z`'s two halves of `f-2` AC4 both PASS and I am not re-grading them:

- **(a) absent WITH a reason: 163 of 163, zero empty**, across five keys.
- **(b) sign / scale / fiscal year: PASS on 23 comparisons** against the team's own workbooks read directly --
  `ASML_NA` 18 of 18 on sign, 18 of 18 on scale, 18 of 18 on fiscal-year alignment, 15 of 18 within 2%;
  `2317_TT` 5 of 5 within 2% with four exact to four decimals, `TWD == TWD`, not converted.
- **The three exceptions are attributed, not waved through** -- all `IS_EPS`, 2.4-3.8%, **in both
  directions**, beside `BVPS` exact on 6 of 6 and `DPS` exact on 6 of 6: a provider definition difference,
  and the block's own figure description is what makes it legible.

**AND THE SAMPLE CHANGE IS THE ADJUDICATION'S BEST ACT, so I am making it a standing rule.** Two of the three
suggested keys were **the probe batch the chunked-request fix was developed on**, and a third,
`Adobe ADBE US`, **holds one PDF and no workbook at all** -- unexercisable for half (a). The CVO kept the
suggested keys, added `8306_JP` and `IMB_LN` from the 86 that followed, and the requirement went from being
tested on **2** absences to **163**.

> **RULE R-1 (round 4, standing).** A judgment criterion's suggested keys are a **FLOOR, never the sample.**
> The grader adds at least one key the fix was NOT developed on, and **a suggested key that cannot answer the
> criterion is NAMED as unexercisable rather than silently substituted or silently graded.** Cost: one extra
> read per criterion. Non-application: a criterion whose population is one named object by construction.

**This is also the test that would have caught `AMGT_RESAPP-Z-S265`, the P/E served 100x wrong. It did not
fire** -- scale is correct on 23 comparisons including a non-USD name, which is where a currency mix surfaces.
**A plausibility oracle that exists and stays quiet is worth recording as loudly as one that fires.**

---

## 2. `FWD-12` -- **NOT_REALIZED.** THE FENCE HAS THREE LIMBS; THE ROUND SERVED TWO AND FILLED THE THIRD WRONG

Fence `:335-344`, read at HEAD. ACCEPT: *"The sheet's shape is the team's own, and no row is blank without
saying why."* DONE WHEN, three clauses:

| limb | state |
|---|---|
| *"rows come from the typecast and the template for that business type"* | **REALIZED on the round's evidence** -- 89 of 89 served blocks non-empty, the 22 added mnemonics landed, verified on 5 keys |
| *"every row carries a figure or reads ABSENT with a reason"* | **REALIZED on sample** -- 163 of 163, and the adjudication's bound stands: 5 keys, not a population claim |
| *"the team's Upside/Base/Downside cases render as **the team's**, cited, **in the slot that is ABSENT today**"* | **NOT REALIZED, and the slot is no longer ABSENT -- it is FILLED BY A MACHINE** |

**THE THIRD LIMB IS WHY THE OUTCOME DOES NOT CLOSE, and neither the drain packet nor the adjudication reached
it.** Measured live on the served `thesis` route (client-called), `model_cases` on `BA_US_Equity`:

```
status  SERVED
cases   ["Upside", "Base", "Downside"]
base    status SERVED   value -18.032184
        formula "consensus EPS (FY1) x trailing-median P/E"
        inputs  consensus_eps  -0.828   BEST_EPS  FY1 2026  period_end 2026-12-31  source BBG
                trailing_median_pe 21.778  PE_RATIO  window 2016..2020  n 5
        px_last 196.8  PX_LAST  vintage 2026-09-25T04:39:06Z
upside   status ABSENT   reason "methodology to be discussed with Andrew"
downside status ABSENT   reason "methodology to be discussed with Andrew"
```

**The fence's word is "THE TEAM'S". What is served is a machine's derivation from Bloomberg consensus** --
`BEST_EPS` times a trailing median `PE_RATIO`. It is not the team's case, it is not cited to the team's
workbook, and **the slot the fence describes as "ABSENT today" is now OCCUPIED, which is worse than absent:**
a PM reading the Model tab sees three case labels and a served Base value where the fence promised the team's
own cases. **`FWD-12` is NOT_REALIZED on limb 3.**

**ONE THING THE BLOCK DOES RIGHT AND IT MATTERS:** it carries its formula, both input mnemonics, the fiscal
period, the period-end date, the source, the P/E window and `n`. **A value carrying its claim in full.** Had
it not, the finding below would have been invisible.

---

## 3. THE SERVED BASE CASE FOR BOEING IS **-18.03** AGAINST A LAST PRICE OF **196.80**

**This is the severest thing I have measured in AMGT today and it is a SERVED number a PM can read.**

**Why it happens, and the arithmetic is not the defect:** `BEST_EPS` for FY1 2026 is **-0.828** (Boeing is
loss-making on forward consensus). A trailing-median P/E of **21.778** times a negative EPS is
**-18.03**, which is correct multiplication and **an undefined valuation**: a P/E multiple has no meaning
applied to negative earnings. **The block serves it as `status: SERVED` with no guard and no caveat.**

**POPULATION, measured, with the denominator printed:** the `freshness` route's 250 rows carry **191 distinct
`security_key`s**. Swept all 191 on the served `thesis` route: `base` **SERVED on 32**, **ABSENT on 159**.
**Of the 32 served, exactly ONE is negative: `BA_US_Equity`.**

**So this is one wrong value and a missing guard -- not 32 wrong values.** That distinction is the finding:
**the method has no domain check, so the first loss-making name it meets produces a negative target price,
and Boeing is that name today.** The next loss-maker gets the same treatment silently.

**A SECOND, SEPARATE DEFECT IN THE SAME BLOCK:** the trailing-median P/E window is **`2016..2020`, n=5** --
it excludes 2021 through 2025 entirely, which for Boeing means **excluding the whole 737-MAX and COVID era**.
A five-year multiple window ending six years ago is a methodology question, not a bug, but it is undeclared as
a choice: the block prints the window (good) and nowhere says why it stops at 2020.

WARN: **AND I PRODUCED A ZERO OVER THE WRONG POPULATION ON THE WAY TO THIS NUMBER.** My first sweep filtered
the freshness rows to `source == 'coverage'`, got **27** keys, and reported **0 of 18 served bases negative**.
`source` takes three values -- `coverage 83, holding 161, both 6` -- and **`BA_US_Equity` was not in the slice
I chose**, so the zero excluded the one instance I already held in my hand. **I caught it only because BA's
`-18.03` was my positive control**, which is the same discipline that stopped me publishing a false
fabricated-citation finding on `AMGT_RESAPP` `FWD-18` two hours earlier. **A filtered population that drops a
known positive is not a population; it is a filter, and the zero it returns is about the filter.**

---

## 4. `FWD-19`'s PARTITION DECLARES **THREE** VALUES AND THE CENSUS PRINTS **FOUR**

`FWD-19`'s fence (`:399-408`): *"a census prints, for all 93, **dossier-served / resolved-but-no-prose /
unresolved-with-reason**, and THE THREE SUM TO 93."*

The round-4 census (`deliverables/2.0.0_SA_COO~X/evidence/production_sequence_r4_20260925T045114Z.log`
@`04832c4b48`, **pin verified identical to HEAD**, lines 1038 and 1052 -- read at HEAD, not taken from the
message that cited it):

```
folders_read 94  dossier_served 82  served_as_empty_shell 12  resolved_no_prose 0  unresolved_with_reason 0  sum 94
```

**FOUR values, and the arithmetic is right: 82 + 12 + 0 + 0 = 94.** The problem is the naming, and it is a
Rule 24 problem with a consequence:

**`served_as_empty_shell` is not in the fence, holds 12, and IS the fence's `resolved-but-no-prose` class** --
the contract itself names it: *"11 of the 93 (10 workbook-only, 1 empty) can never carry prose-derived
fields."* **Meanwhile the fence-named field `resolved_no_prose` reads 0.** So a reader who goes looking for
the fence's three values finds the one that should hold 12 holding **zero**, and the 12 sitting under a name
the fence never declared.

> **RULE R-2 (round 4).** Where a fence declares a partition by NAME, the census emits **those names** or
> emits a mapping line from its own names to the fence's. **Two field names for one class, one holding the
> count and the fence-named one holding zero, is a disclosed denominator that reads as an absence** -- the
> same family as the stale disclosed denominator this project already fixed. Cost: one line. Non-application:
> a census whose fence declares no named partition.

**Not a grade change.** `FWD-19` was NOT REALIZED at round 3 and remains so; the census is substantively
right and the 11-can-never-carry-prose class is honoured. **This is a naming fix, and it is cheap.**

---

## 5. THE POPULATION IS **94**, AND MY OWN CARD WAS THE THING THAT WAS WRONG

**`C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER` (`AMGT_CORPUS_PRD.md:719-733`) settled this on
Andrew-direct 2026-09-24 ~05:0xZ** and closed `K6` on his word. **I did not read it, and today I issued a CTO
adjudication re-ruling the same question.** Withdrawn and corrected in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_AMGT_RESAPP_20260925T1450Z_THE_UNIVERSE.md`
amendment A1 @`ceba6f9d69`. **`AMGT_CORPUS` handled this correctly a day before I got it wrong, and the record
now says so.**

**THE CONTRACT SAYS 93; THE FOLDER NOW READS 94** -- three independent reads today: mine at 14:4xZ
(`library.list_folders(library.library_root())`), `3.0.0_SA_CVO~Z`'s at 15:2xZ in `ADJUDICATION_v7`, and the
round-4 census's own `folders_read 94` at 04:51Z. **One folder added since 2026-09-24.**

**AND THE ISSUER HAD ALREADY MET THE CONSEQUENCE BEFORE I RAISED IT.** I messaged `2.0.0_SA_COO~X` that
`FWD-19`'s counts must now sum to 94; it answered with the log line above, which already sums to 94 on a
fresh read taken at 04:51Z -- **hours before I raised it.** The contract's method (*"a subtraction from a
FRESH READ ... with the denominator printed"*) is what made the producer immune to the number moving.
**Recorded because it is the counter-case to my own error: the discipline written into the contract did the
work that my card was standing in the way of.**

---

## 6. `Z-S36` CARRIED -- and "REASONS BELONG TO THE DATA" NOW HAS **THREE INSTANCES IN TWO PROJECTS IN ONE DAY**

`Z-S36` is the round's one carried row: **9,471 `model_rows` carry 0 values while every row states
`not authorized`** -- a hard-coded reason that was true when written and **is false now that the figures have
arrived.** The packet's own enrichment names the fix and the adjudication quotes it: ***"reasons belong to
the data."***

**It generalises, and today gave it two more instances, both from `AMGT_RESAPP`:**

| instance | the constant that went stale or says nothing |
|---|---|
| `Z-S36` (this round) | 9,471 rows citing `not authorized`, **false since the figures landed** |
| `AMGT_RESAPP` `FWD-3`/`FWD-5` | **27 mnemonics** whose unit/sign convention reads `NOT-YET-BUILT`; 192 of 391 served pdf figure lines carry `[UNRESOLVED UNIT]` |
| `AMGT_RESAPP-Z-S278` | `overlay.chatter` and `overlay.price` are **bare nulls on 89 of 89**, while `description`, `feed` and `posture` on the same payload each carry a status and a reason |

**Three shapes of one defect: a reason that cannot go stale loudly, a convention that was never built, and a
null that says nothing at all.** All three read as authoritative to a consumer. `Z-S36`'s fix -- an
absent-reason computed from the data rather than written into the code -- **is the fix for all three**, and
the third one (`chatter`) can use the estate's own `classify.absent()` that five sibling fields already use.

> **RULE R-3 (round 4).** **A constant absent-reason is a defect on sight.** A reason string that a producer
> writes rather than derives cannot know when its cause has gone, so it goes stale **silently** and reads as
> authoritative the whole time. Cost: the reason is computed where the absence is detected. Non-application: a
> reason naming a permanent structural fact (a workbook-only folder can never carry prose).

---

## 7. THE COVERAGE DEFECT -- **2 OF 19 OUTCOMES HAVE EVER BEEN GRADED, AND THIS IS A LOOP DEFECT**

**Denominator 19** (`endpoint_outcomes`, PRD v0.6 header: `FWD-1`..`FWD-19`). Census of every committed round
analysis in `ledger/`: **`FWD-12` and `FWD-19` are the ONLY two that have ever carried a grade.**
**Seventeen have never been graded in any round, and the project is at round 4.**

**AND I FOUND THE IDENTICAL DEFECT ON `AMGT_RESAPP` TWELVE HOURS AGO** -- a 10-outcome graded set serving a
30-outcome endpoint, `FWD-1`..`FWD-20` last graded in round 1 while the project ran to round 41
(`ctoZ_ENDPOINT_COVERAGE_AUDIT_AMGT_RESAPP_20260925T0355Z.md` @`b1a9780309`). **Two projects, independently,
same shape.** That moves it out of "a defect in this project" and into **a defect in the loop**: nothing in
L8, L9 or L10 compares the ROUND's denominator to the PROJECT's, so a round that grades its own scope
honestly -- and round 2 did, printing *"Denominator: FWD-1..FWD-19, nineteen. Graded here: FWD-19"* -- still
leaves the endpoint unmeasured, and the honest statement is what makes it invisible.

> **RULE R-4 (round 4, both projects).** **Every round analysis prints `graded this round / graded ever /
> endpoint denominator`.** Three integers. Round 2 printed the first and the third and still could not see the
> gap, because the missing number is the CUMULATIVE one. Cost: one census of the ledger per round.
> Non-application: a round-1 analysis, where "graded ever" equals "graded this round" by construction.

**I am not cutting a 19-outcome re-grade pass for `AMGT_CORPUS` in this analysis.** The `AMGT_RESAPP` pass
cost roughly forty tool calls and produced four cross-cutting inputs; the same pass here belongs in round 5
as its own cell with its own budget, **not as a rider on a round that is closing.** Named here so it cannot
become invisible again.

---

## 8. THE ENRICHMENT LIST FOR ROUND 5 -- eight items, ordered by what they unblock

1. **`FWD-12` limb 3 -- the team's cases, and the negative-base guard.** Two acts: (a) a domain check --
   a P/E-based case **REFUSES with a named reason when forward EPS <= 0** rather than serving a negative
   target price; (b) the slot carries **the team's own cases, cited to their workbook**, or reads ABSENT with
   its reason. **(a) is the urgent half: one served number is currently wrong on a client-called route.**
2. **`Z-S36` -- the dossier Model rows.** 9,471 rows, 0 values, a false constant reason. Apply R-3: derive
   the reason at the point of absence. **This is the round's carried row and `FWD-12`'s dossier half.**
3. **R-2's naming fix on the `FWD-19` census** -- emit the fence's three names, or a mapping line. One line.
4. **The 19-outcome re-grade pass**, as its own cell with its own budget (section 7).
5. **Cite `C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER` from `AMGT_RESAPP`'s PRD** wherever a fence says
   *"every company the page covers"*. Six references exist, **all six inside `AMGT_CORPUS`**; the sibling that
   needs it cites it nowhere. Cheapest item on this list.
6. **The trailing-P/E window** (`2016..2020`, n=5): declare the choice or move it. Not urgent; undeclared.
7. **Apply R-1 to every future judgment criterion** -- suggested keys are a floor, unexercisable keys are
   named.
8. **Apply R-4 to every round analysis in both projects** -- three integers, every time.

---

## 9. CARDS AT ANDREW -- TWO, and one of them has been served in 32 payloads without ever being carded

```
+-- CARD 1 of 2 ------------------------------------------------------+
  **The Upside and Downside case methodology.**
  Both read ABSENT with the reason "methodology to be discussed with
  Andrew", on every one of the 32 names whose Base case is served.
  ----------------------------------------------------------------------
  **REC --** No methodology proposed. But note the reason has been
  SERVED to a client-called route on 32 names while appearing on no
  open-calls list, including mine. A reason that names Andrew is not
  the same as a card at Andrew.
+---------------------------------------------------------------------+

+-- CARD 2 of 2 ------------------------------------------------------+
  **Who drains the on-demand pull queue, and on what cadence?**
  Carried from AMGT_RESAPP; FWD-2 cannot close without it.
  ----------------------------------------------------------------------
  **REC --** None offered. Vendor-terminal cadence, reserved by name
  in C-ROUND12-PULL-WIRED. Nothing waits on it.
+---------------------------------------------------------------------+
```

**Card 1 is the one worth his minute, and it is a mechanism finding as much as a card:** the product has been
telling users for some time that a methodology is pending Andrew's word, and **no seat's card list carried
it** -- including the `/open-calls` sweeps I have run this session. **A `reason` string that names a person is
not a carrier.** The item had an owner in prose and no owner in any queue.

---

## 10. ROUND 4 IS **CLOSED**; `FWD-12` IS **NOT_REALIZED**; THE PROJECT IS NOT

**Closed:** 3 of 3 orders terminal, 12 of 12 rows dispositioned, `f-2` AC4 graded on both halves, the
disclosure re-mint landed at 94 of 94, the identity layer complete.

**`FWD-12` NOT_REALIZED** on limb 3 (the team's cases) and on the dossier half (`Z-S36`). **`FWD-19` NOT
REALIZED**, unchanged from round 3. **Seventeen outcomes ungraded.** Four rules (R-1..R-4) and eight
enrichment items to `2.0.0_SA_COO~X` for ONE round-5 issuance.

**The honest summary of this round is that its evidence was excellent and its scope was narrow.** The
adjudication changed its own sample and caught a key that could not answer the criterion; the census ran on a
fresh read and was already right about a number I arrived late to; the crosswalk now carries its own staleness
as data. **And a served route is publishing a negative target price for Boeing, seventeen of nineteen outcomes
have never been graded, and the slot the fence said was empty got filled by a machine.** Both halves are true
and the second half is what round 5 is for.

---

# AMENDMENT A1 -- 2026-09-25 ~16:4xZ -- **I RAN THE ONE-LINE PLAUSIBILITY CHECK AND SECTION 3 IS TOO GENEROUS BY SIX NAMES**

**Section 3 concluded: *"this is one wrong value and a missing guard -- not 32 wrong values."* MY OWN NEXT
MEASUREMENT DISCONFIRMS IT.** The check is `base / px_last` -- **both values are in the same served block** --
and it took one sweep of the 32 names whose Base case is SERVED.

## THE CHECK, and why it should shame the round count

**191 keyed names swept, 32 with `base` SERVED. Seven are implausible against their OWN served last price.**

| key | base | `px_last` | base/px |
|---|---|---|---|
| `BA_US_Equity` | **-18.032** | 196.80 | **-0.09** |
| `ULVR_LN_Equity` | 65.705 | 4708.5 | **0.014** |
| `HSBA_LN_Equity` | 22.034 | 1499.8 | **0.015** |
| `RKT_LN_Equity` | 73.866 | 4923.0 | **0.015** |
| `BP/_LN_Equity` | 26.552 | 571.8 | **0.046** |
| `NFLX_US_Equity` | 218.244 | 71.72 | **3.04** |
| `NOW_US_Equity` | 613.522 | 137.78 | **4.45** |
| `ROG_SW_Equity` | 447.304 | **None** | **no price to check against** |

The other 24 sit between **0.54 and 2.00** -- a believable band for a forward Base case. **The seven are not
at the edges of that band; they are off it by one to two orders of magnitude.**

## SEVEN FAILURES, THREE SIGNATURES -- not seven bugs

1. **NEGATIVE FORWARD EPS -- 1 name.** `BA` only, and section 3 has it right: `BEST_EPS` -0.828 times a
   positive multiple. **It is the only name whose forward EPS is negative, which is why it is the only
   negative output.**
2. **A CURRENCY-UNIT MISMATCH -- 4 names, AND ALL FOUR ARE LONDON-LISTED.** `ULVR`, `HSBA`, `RKT`, `BP/` are
   the only `_LN_` names in the 32 and they are the only four in the 0.014-0.046 band. **A London price quotes
   in GBp (pence) while per-share earnings carry GBP (pounds)** -- a factor of 100 between the two sides of
   the ratio. **THIS IS THE `AMGT_RESAPP-Z-S265` CLASS RECURRING ON A DIFFERENT FIGURE:** the same
   hundred-fold unit error, on the Base case instead of the P/E, on a client-called route. Section 1 of this
   analysis credits `f-2` AC4 with being *"the test that would have caught `Z-S265` ... it did not fire"* --
   **and that credit stands exactly as far as its sample: AC4 tested `ASML_NA` and `2317_TT`. NEITHER IS
   LONDON-LISTED, and the two names it tested sit at 0.90 and 0.79, comfortably inside the band.** The oracle
   did not fire because **the defect was not in front of it**, which is R-1's point arriving from the other
   direction: a sample that excludes a venue excludes that venue's unit conventions.
3. **A PROBABLE SPLIT-ADJUSTMENT MISMATCH -- 2 names.** `NFLX` at 3.04x and `NOW` at 4.45x, both US, both
   with a `px_last` far below the level their historical per-share figures imply. **Stated as PROBABLE, not
   measured:** I have not read the split history, and the signature (price low relative to historical EPS,
   multiple therefore too high) is consistent with a split-adjusted price beside unadjusted history. **It is
   named so it is not absorbed into signature 2, which it is not.**

**Plus `ROG_SW_Equity`: a Base case of 447.30 served with `px_last` ABSENT.** Not implausible -- **uncheckable**,
which is worse in one specific way: the block's own plausibility input is missing and the block does not say so.

## WHAT SECTION 3 GETS WRONG, and the correction

| section 3 said | measured |
|---|---|
| *"exactly ONE is negative"* | **TRUE, and it stands** -- 1 of 32 |
| *"one wrong value and a missing guard -- not 32 wrong values"* | **WRONG. Seven of 32 are implausible**, and the negative one is the only one I had looked at. The other six are positive, in-range-looking numbers that are off by 100x or 3-4x |
| the guard needed | **not one guard, THREE** -- a domain check on forward EPS <= 0; a currency-unit reconciliation between `px_last` and the per-share inputs; a plausibility band on `base/px_last` that refuses rather than serves |

**My error has a shape worth naming: I found a NEGATIVE number, and negativity is the signature I then went
looking for.** The sweep in section 3 asked *"how many are negative?"* and answered 1 of 32 correctly. **It
never asked "how many are WRONG", and the six worst-looking values in the set are positive.** A found defect
supplies the predicate for the next census, and that predicate inherits the first defect's shape -- so the
census confirms the first finding's scope and is blind to its siblings. **The fix is the one that worked here:
after any per-item defect, run a check that is ABOUT THE QUANTITY rather than about the defect.**

## AND THE PART THAT IS NOT MY ERROR BUT THE LOOP'S

**`base` and `px_last` are fields of the same served object.** The ratio needs no second source, no vendor
call, no fixture and no new instrument -- **one division, thirty-two times.** `AMGT_RESAPP` has run 42 rounds
and `AMGT_CORPUS` 4; `Z-S265` taught this estate that a served valuation figure can be 100x wrong; and **no
round in either project has ever divided the Base case by the price beside it.**

> **RULE R-5 (round 4, both projects, and it supersedes nothing).** **Any served figure that shares an object
> with a natural comparator is checked against it, in the round that first serves it.** A Base case has
> `px_last` beside it; a P/E has price and EPS beside it; a market cap has shares and price. **The comparator
> is already in the payload, so the check costs one division and needs no sample.** Cost: one line per
> served figure with a same-object comparator. Non-application: a figure with no comparator in its own object
> -- and that absence is itself worth printing, as `ROG_SW`'s missing `px_last` shows.

**Round-5 enrichment item 1 is amended accordingly:** the urgent act is **not** one domain check on forward
EPS. It is **the `base/px_last` band, refusing rather than serving**, which catches all three signatures at
once and catches the next one without knowing its shape. The EPS domain check and the GBp reconciliation are
then real fixes behind a guard that is already holding the line.

**The four London names are the item I would put first if only one thing were cut:** a negative number reads
as obviously broken to any PM who sees it, and **`ULVR` at 65.71 against a price of 4708.5 reads as a
considered valuation.** The dangerous defect here is not the one that looks wrong.
