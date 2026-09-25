# THE GOAL'S THIRD CLAUSE, MEASURED -- and the instrument that would answer it covers 53 of 94 -- `1.0.0_SA_CTO~Z`, 2026-09-25 ~23:0xZ

**The clause, verbatim:** *"followed by complete backfill for all of these securities through the
opal-data-harvest channels."* **Three of the goal's four clauses were measured today; this was the one that
was not.** It is now partly measured, and the reason it is only partly measured is itself the finding.

## 1. THE POPULATION, and it moved again -- 93 -> 94 -> 95

`library.list_folders(library.library_root())` at 22:5xZ: **95 folders.** It read **94** at 14:4xZ (mine) and
15:2xZ (`3.0.0_SA_CVO~Z`'s), and the ratified contract says **93**. **Three readings, three values, one day** --
which is exactly why `C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER` requires *"a subtraction from a FRESH
READ ... with the denominator printed"* rather than a constant.

**AND THE NEW NAME IS IDENTIFIED: `AIA Group`.** The served crosswalk (`crosswalk/v1/2026-09-25.json`,
235 records, `folders_in_records 94`, `UNRESOLVED 0`) resolves **94 of the 95**, and the single miss is
`AIA Group` -- a folder added after the crosswalk was built. **Not a resolution failure; a new arrival.** The
crosswalk re-mint picks it up, and the contract's method is what made that distinguishable.

## 2. THE MEASUREMENT, over the population the contract names

| | count | of |
|---|---|---|
| live research folders | **95** | the ratified population, read fresh |
| resolved by the estate's own crosswalk | **94** | 95 |
| **...that have a row on the `freshness` route** | **53** | 94 |
| bloomberg landed | **53** | **53 (100%)** |
| seekingalpha landed | **3** | 53 (6%) |
| serp landed | **0** | 53 (0%) |
| names with ZERO channels landed | **0** | 53 |

**Over the 53 the instrument can see: the bloomberg channel is COMPLETE, and it is the only one that is.**
`seekingalpha` reaches 6%, `serp` reaches nothing, and **50 of 53 names carry exactly ONE channel.**

> **So clause 3 is ONE CHANNEL DEEP.** *"Complete backfill ... through the opal-data-harvest channels"* is
> plural; what exists is one channel complete over a partial population. **That is real progress and it is not
> the clause.**

## 3. THE PART THAT BLOCKS THE ANSWER -- and it is a defect my own `FWD-7` grade missed

**41 of the 94 crosswalk-resolved folders have NO ROW on the `freshness` route at all** -- among them
`Adobe ADBE US`, `Air Liquide AI FP`, `America Movil AXMB MM`, `AstraZeneca AZN`.

**The route is not short of rows: it serves 250 of them, over 191 distinct keys.** It is short of THESE rows.
Its own `universe_denominators` read `coverage 89, holdings_distinct 167, union 250` -- **so it is built from
the coverage snapshot plus holdings, and 41 names in the research folder are in neither.**

**THIS SHARPENS A GRADE I GAVE TODAY AND I GOT THE REASON WRONG.** I graded `FWD-7` NOT_REALIZED
(@`af11e91097`) on two grounds: no client call, and a denominator of 250 where the fence says *"every company
the team covers"*. **I recorded the 250 as TOO WIDE. It is also too NARROW, on a different axis** -- wide on
holdings, narrow on the research folder, **missing 41 of the names the fence actually names.** A census
scoped to where the question is filed missed the answer filed elsewhere, and I was the one who filed it.

> **CONSEQUENCE, stated plainly: NO SEAT CAN CURRENTLY STATE CLAUSE 3's STATUS OVER THE RATIFIED
> POPULATION**, because the only instrument that reports per-channel landing covers **56%** of it. **The 53 of
> 53 bloomberg result is true and its denominator is not the goal's.**

## 4. WHAT I AM NOT CLAIMING

- **Not that 41 names have no data.** They have no ROW on this route. Whether raw landed for them is a
  different query against the bronze prefixes, and I did not run it over 41 names.
- **Not that `serp` 0 and `seekingalpha` 3 are failures rather than scope.** `AMGT_HARVST` holds the publisher
  work, four publishers carry zero `listing_hit` rows by its own measurement, and `ft`/`barrons` are the
  diagnostic cell I re-classed tonight. **These numbers are consistent with that project's own state**, not a
  new discovery about it.
- **And I discarded my own first denominator.** A string-matching resolver returned **61 of 95** and left
  `Adobe ADBE US` and `BNP Paribas BNP FP` unresolved -- obviously my bug, since both carry their ticker in the
  folder name. **61 was an artifact of my matcher.** The estate's own crosswalk resolves 94. **Reading the
  producer's mapping instead of inventing one is the fourth time today that correction has applied.**

## 5. WHAT THIS IS FOR

1. **`FWD-7`'s fix is wider than the client call.** Its route must cover the research folder, not the
   coverage-plus-holdings union. Routed to `2.0.0_SA_COO~Z` as a round-43/44 input, superseding the
   denominator half of my `af11e91097` grade.
2. **A crosswalk re-mint picks up `AIA Group`** and takes `folders_in_records` to 95. `2.0.0_SA_COO~X`'s
   round-5 disclosure machinery already does this on its own fresh read.
3. **Clause 3 needs a channel-by-channel target.** "Complete backfill" over five channels where one is
   complete and one is at 6% is not a number anybody has agreed. **That is a scope question and it is
   Andrew's** -- but it is not a blocking card, because the work that would move it (`AMGT_HARVST`'s
   publishers) is already cut and running.

## 6. INSTRUMENTS

`library.list_folders(library.library_root())` for the population -- the served `crosswalk/v1/2026-09-25.json`
for folder-to-key resolution, **the estate's own mapping rather than a matcher of mine** -- the served
`freshness` route for per-channel landing, read through `lambda:Invoke` of Opal's own function -- a discarded
first run whose 61-of-95 denominator was my resolver's defect and not the world's. **No vendor call: every
read is Opal's own store or Opal's own function.**
