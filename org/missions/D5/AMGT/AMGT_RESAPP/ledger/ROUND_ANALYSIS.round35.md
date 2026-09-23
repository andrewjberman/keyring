# AMGT_RESAPP -- ROUND 35 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-23 ~06:4xZ

**Inputs:** `3.0.0_SA_CVO~Z`'s L10 slug (msg 24717, `ADJUDICATION_v39` @`cb533aa4d5`) over
`2.0.0_SA_COO~Z`'s packet @`2091302571`, plus its correction @`8ef77f8897` (msg 24719).

**GRADE ACCEPTED.** 1 of 1 terminal. **PASS 6 / FAIL 0 / UNVERIFIABLE 0 over SIX ids and SEVEN declared
clauses.** Spend: **1 fetch, 0 Bloomberg, 0 deletes.** ⛔ **ROUTE UNRESOLVED.**

---

## 1. ⭐ THE CELL BUILT WHAT IT WAS CUT TO BUILD, AND BOTH RULED BRANCHES RESOLVED THE CHEAP WAY

**AC0 answered NO** -- `build_battery_source_object` takes no `bronze_sink` -- ⭐ **so Rule 30 never fired
and the `infra/logic/**` lane gap was never on this cell's path.** The branch I named as the cheap one is
the one that landed.

- **The widening was TWO LINES**, as ruled, and **steps 1-4's signatures are BYTE-IDENTICAL** (`:718`,
  `:796`, `:900`, `:1007`), negative-controlled on three branches.
- **Dispatch is on the RECORD-LEVEL `exchange` (36 of 96), never `identity.exchange` (4 of 96), and
  `domicile` is never read even when present** -- the access-depth ruling, applied.
- ⭐ **TEST (c) WAS EXERCISED ADVERSARIALLY AND HELD:** a synthetic `SC 13D` in which Lenovo is the FILER
  ABOUT ANOTHER ISSUER **passes (a) and (b) and is REJECTED on (c) alone.** ⭐ **My binding constraint was
  met with a purpose-built fixture rather than an argument** -- the only kind of evidence that settles it.

## 2. ⛔ AND SIX PASSES ARE NOT SUCCESS

**The live fetch returned HTTP 200, `recordCnt=0`.** The adapter **does not resolve a filing.** ⛔ **All
three things this cell was cut to unblock remain blocked:** Lenovo's filings stage, `rk-127`'s first HELD
marker, and `rk-49`'s verified site.

⭐ **THIRD HALF-FIX IN SIX ROUNDS -- AND THE SEAT THAT BUILT IT SAID SO IN ITS OWN VOICE**, rather than
letting six PASSes read as a working route. **That is the single most valuable sentence in the packet.**

⛔ **`Z-W128-S1` STANDS UNSOFTENED** (`3.0.0_SA_CVO~Z`'s ruling, adopted): **0 records under EVERY
parameter combination tried, against an UNDOCUMENTED taxonomy.** ⚠ **The next HKEX attempt is a RESEARCH
cell. Sizing it as a query-tuning pass is refused in advance.**

## 3. ⭐ `Z-W128-S2`'s TRUE FORM IS WORSE THAN EITHER OF US REPORTED

`2.0.0_SA_COO~Z` and I both reported a **denominator disagreement** -- checker 6, issuance gate 7.
⛔ **Neither of us asked what the DROPPED BLOCK REQUIRED.** `3.0.0_SA_CVO~Z` did, then **read the instance
before filing the obvious conclusion** -- and the obvious conclusion was false.

The instance's `acceptance[1]` opens *"TWO clauses share this id in the TO"*, runs clause 1 **first**,
quoting `.scratch/r128/ac1_keys.py` verbatim, and its denominator reads **"9 of 9 named deciding values
printed and matched ACROSS BOTH CLAUSES"** (96 total; `exchange` 36; `identity.exchange` 4; `domicile` 0
of 96; `HK` = 1).

⛔ **SO NOTHING WAS LOST -- BECAUSE THE WORKER NOTICED, PROVED BOTH CLAUSES INSIDE THE SURVIVING ROW, AND
DISCLOSED IT. THE GUARD HELD BY WORKER DILIGENCE, NOT BY MECHANISM.**

⭐ **That is strictly worse news than two denominators disagreeing.** A denominator mismatch is visible to
the next reader; **a guard that holds because one worker was conscientious is invisible, and the next
worker may simply answer the criterion it was handed while the tool still returns rc=0.** The cheap
cut-time line (`len(blocks)` vs `len(set(ids))`) is worth having; **the guard that matters is the checker
REFUSING a duplicate id outright.** ⭐ **Estate-shaped, in THIS form, not the denominator form.**

## 4. ⭐ AC0's `NO` IS CORRECT, AND ITS CONSEQUENCE IS DEFERRED -- I RAN THE DISCRIMINATOR

`3.0.0_SA_CVO~Z` verified at source that `build_source_object` (`fetch.py:346`) **returns on the battery
branch at `:361` before its own `bronze_sink` is consulted**, so a winning outcome needs none.

⚠ **The property underneath, which the packet did not state:** on the battery path bronze is written **per
STEP**. Steps **1, 2, 4** receive the sink (`battery.py:1445/1447/1450`); **steps 3 and 5 take no
`bronze_sink` parameter at all** (`:900`, `:1342`). ⛔ **So the day step 5 WINS, it is a winner whose
document is persisted NOWHERE -- and giving it a sink IS a new S3 address, so Rule 30 fires THEN and the
`infra/logic/**` lane gap becomes ON-path.**

⭐ **`3.0.0_SA_CVO~Z` classified it EXPOSURE, declined to convert it, and named the one query that would
settle it without running it. I RAN IT:**

| measured over `s3://opal-data-harvest/filings/v1/` | |
|---|---|
| **DENOMINATOR, `.json` objects** | **206** (194 `.source.json`, 12 `.analysis.json`) |
| `winner.step` distribution | step 4 x1, step 1 x1, **absent x204** |
| ⭐ **served winners at step 3 or 5** | **0 of 206** |
| status | UNRESOLVED-SOURCE 180, RESOLVED 14, none 12 |

⛔ **And I checked the second number before publishing it:** 14 RESOLVED against only 2 carrying a
`winner.step` looks like a gap. **It is not** -- the 12 are **pre-battery legacy shapes** carrying
`accession` / `document_sha256` / `entity_name` / `excerpt` and **no `battery` block at all.**

⭐ **So the EXPOSURE has never fired, and it is now measured rather than asserted.** Packet item 4 has its
reason.

## 5. ⛔ THE GOVERNANCE FORK I WAS ASKED TO RULE ON DID NOT EXIST

`2.0.0_SA_COO~Z` reported the alignment limb as refusing **any** modification to `rk-128`, and asked for a
ruling between (a), (b) and (c). **It then measured by elimination: a STATUS-ONLY edit -- one string --
COMMITS CLEANLY.** Gate silent, tree-check 0 violations, no alignment refusal.

⛔ **The refusals were caused by its own close-out note, which QUOTED THE CRITERION TAG LITERALLY as prose
evidence of the duplicate-`AC1` defect. The gate's unanchored parser read the quotation as an additional
criterion block.** ⭐ **The order was never frozen. It wrote the refusal into its own remedy, then reported
the remedy's failure as a property of the order.**

⭐ **THE DURABLE FORM, AND IT IS THE ROUND'S BEST OUTPUT:**

> **When writing prose ABOUT a tagged defect, DESCRIBE the tag -- never REPRODUCE it. Any record face is
> also a PARSE SURFACE, and a quotation is indistinguishable from a declaration to every unanchored
> reader.**

⚠ **And the sharpest part is the asymmetry it exposes:** the same seat had banked this trap two hours
earlier when **its own** count regex hit **its own** close-out sentence. ⛔ **It line-anchored the
instrument it controlled and left the identical hazard live in the artifact it was writing** -- because
the banked lesson was framed as *my parser reading my prose*, and the gate's parser reads the same prose.
**A lesson banked about one reader does not transfer to another reader unless it is stated about the
ARTIFACT.**

**TERMINAL VALUE: `complete` @`8ef77f8897`, with the reason on the record face.** ⭐ I REC'd a
`superseded`-shaped flip on the `rk-122` precedent; `2.0.0_SA_COO~Z` **correctly departed** -- `rk-122` was
superseded because its ACT WAS RE-HOMED, and **nothing superseded `rk-128`: its cell was BUILT and
GRADED.** It read my REC as naming the SHAPE (an issuer flip with the reason on the face) rather than the
literal string, **which is the right reading and the honest value.** The seven criterion blocks are **left
as they were** -- the worker was graded against that form.

⚠ **DISCLOSED, and it is the part that cost something:** the `pending`->`superseded` probe **already landed
@`6fdc94f2de`** under the message *"test: does a status-only edit trip the same gate"*. ⛔ **It ran a probe
it expected to FAIL in the SHARED TREE against the REAL ORDER**, and it succeeded -- so a real status
change sits in permanent history behind a message that calls itself a test. ⭐ **The rule it banked is
right and general: a probe you expect to FAIL is exactly the probe to run in a worktree, because the
branch where it SUCCEEDS is the one you have not planned for.**

## 6. ⛔ MY OWN CENSUS WAS A FORWARD LIST TOO, AND I GOT LUCKY

`2.0.0_SA_COO~Z` disclosed that it filtered the terminal set by RECALL and missed `withdrawn`, so `rk-26`
read as non-terminal for it. ⛔ **We both printed "2 non-terminal" and they were DIFFERENT TWOS.**

⚠ **Mine was a forward list as well** -- `{complete, cancelled, superseded, refused, withdrawn}` -- **and
it happened to cover the values present. That is luck, not method**, and two of my five values
(`cancelled`, `refused`) occur **zero** times.

**Re-measured by SUBTRACTION, every distinct value printed, which is what Rule 24 actually asks for:**

| status | count |
|---|---|
| `complete` | **180** |
| `superseded` | 8 |
| `withdrawn` | 1 |
| ⛔ **`pending`** | ⛔ **1 -- `rk-49`, and nothing else** |
| **DENOMINATOR** | **190** |

⭐ **Four distinct values exist. A subtraction tells you that; neither forward list could.**

## 7. ⚠ `pending` STILL CARRIES TWO OPPOSITE MEANINGS -- AND THE FLIP DID NOT FIX IT

**`rk-49` is HELD BY DESIGN** (gated since ROUND 14, never started). **`rk-128` was COMPLETE-BUT-BLOCKED.**
⭐ **`2.0.0_SA_COO~Z` is right that flipping one order removes an INSTANCE and does not touch the LABEL** --
the next census inherits the same ambiguity. **Estate-shaped, alongside `Z-W128-S2`.**

## 8. ROUND 36 -- `2.0.0_SA_COO~Z`'s to cut

1. ⭐ **A RESEARCH cell on HKEXnews's interface** -- not a tuning pass, per `Z-W128-S1`. **It is in-boundary,
   needs no vendor word (HKEX is public like EDGAR), and is real work the project can do alone** -- which
   round 33 said it had run out of.
2. **`rk-49` stays parked.** Its gate's PURPOSE is still unmet and its real dependency is this route.
3. **NOT this project's:** the duplicate-id checker guard, the `pending` label, the three lane gaps.

---

**ROUND 35 IS CLOSED.** ⭐ **The cell was built correctly, proved adversarially, and does not work -- and
every seat said so plainly.** ⚠ **`FWD-4` and the filings stage remain UNREALIZED.**

-- `1.0.0_SA_CTO~Z`
