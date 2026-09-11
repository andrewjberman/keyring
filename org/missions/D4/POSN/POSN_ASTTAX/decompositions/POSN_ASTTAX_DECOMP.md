# POSN_ASTTAX -- L5 DECOMPOSITION (round 1)

**archetype:** DIAGNOSE

**Owner (L5-L6):** `2.0.0_SA_COO~Z` · **Date:** 2026-09-11 ~05:0xZ · **Directive:** D4 "Positioning" · **Macro:** POSN
**PRD:** `org/missions/D4/POSN/POSN_ASTTAX/prd/POSN_ASTTAX_PRD.md` **v0.1**, content pin `66e4398f5042`, read IN FULL
**Registered:** @`e4086f30f3` (tree), on D4 enum `[POSN, ETFS]` RATIFIED @ this seat's record `425b11ccb1`
**Former code:** `ASSETCLASS_TAXONOMY` -- records citing it resolve here (`project.json.former_codes`)
**Pre-tree draft this supersedes:** `org/tier1_exec/2.0.0_SA_COO~Z/deliverables/POSN_ASTTAX_L5_DECOMP_DRAFT_20260911.md` @`6ffdaa8ccb`

---

## 0. PRD acceptance -- re-verified AT THE NEW HOME, not carried over

The PRD MOVED between my draft and this artifact (`docs/architecture/ASSETCLASS_TAXONOMY_PRD.md` ->
the tree home), so the draft's citations were re-grounded rather than trusted. Coverage re-run by
SUBTRACTION against the moved file:

```
  header endpoint_outcomes (DENOMINATOR)   6   FWD-1..FWD-6
  outcomes named across s.7's 3 rows       6
  declared MINUS covered                   0   uncovered
  the PRD's own printed claim              "6 of 6 outcomes carried by exactly one row, 0 uncovered"
```
**It holds.** Stated as a measurement at pin `66e4398f5042`, **not as an invariant** -- if L4 adds an
outcome this line is re-run, never re-asserted.

⚠ **ONE HEADER OBSERVATION, NOT A BLOCKER AND NOT THIS SEAT'S FIELD:** the JSON header carries
`"status": "DRAFT"` while s.5 records Andrew confirming all six `DONE WHEN` bars verbatim
(2026-09-11, *"Confirmed, just note that Philosophy/CMA are the same page now. Also this should likely
be heavily involved with ETFClassifier."*). The sibling D12 PRD uses `status: RATIFIED` for exactly
that state and annotates it *"L5 may begin on this header."* Surfaced to `1.0.0_SA_CTO~Z` for the L4
edit that carries the sign-offs; **L5 proceeds on the CTO's explicit GO (msg 21183) and is not held on
a header field.**

---

## 1. GROUNDING -- measured at L5, so no cell starts from a search

`C-ONE-SOURCE` names *"the shared ETF classification module"* and correctly reserves the adjudication
to FWD-5, *"NOT hard-pre-judged here."* Measured:

⛔ **BOTH CANDIDATE MODULES SELF-DESCRIBE AS THE SINGLE SOURCE OF TRUTH** --
`_shared/etf_classification.py:39` and `_shared/etf_classifications_dynamodb.py:7`. Two contradictory
self-reports; **nothing in either text breaks the tie.**

### ⭐ SETTLED -- Andrew-direct 2026-09-11 ~04:2xZ, and by the instrument he named

VERBATIM: *"I think ETFClassifier is the real one"* / *"check to see what is already hooked up to
Positioning page thats how youll kow for sure."*
Record: `org/tier1_exec/2.0.0_SA_COO~Z/deliverables/ANDREW_DIRECT_20260911_04xxZ_ETFCLASSIFIER_IS_THE_REAL_ONE_CHECK_THE_POSITIONING_PAGE.md` @`6ffdaa8ccb`

```
  yang_pipeline/positioning/yang-generate-positioning/lambda_function.py
    :25   from etf_classifications_dynamodb import ETFClassifier
    :31   etf_classifier = ETFClassifier()
```
`yang-generate-holdings-attribution` vendors the same module. **Positioning runs ETFClassifier.**

⛔ **AND THE CHAIN IS NOT A FORK.** `seed-etf-classifications.py:58` writes the DynamoDB table FROM
`ETF_CLASSIFICATIONS` -- the hardcoded dict:

```
  etf_classification.py (hardcoded)  --seed-->  DynamoDB etf-classifications  --ETFClassifier-->  Positioning
        [AUTHORING]                                  [STORE]                        [SERVING]
```
The hardcoded module is **not a rival to retire -- it is what SEEDS what ETFClassifier serves.**

⛔ **WHICH IS WHY FWD-5 IS NOT CLOSED BY THAT ANSWER.** Its bar is *change a definition in ONE place
and everywhere reflects it.* Two candidate "one places", opposite failure modes: change the **TABLE**
and the next seed run silently overwrites you from the dict; change the **DICT** and nothing serves it
until the seed re-runs -- **and that trigger is UNMEASURED.** Neither is "one place" as FWD-5 means it.

### Three further measurements, each landing on an outcome

| # | measured | lands on |
|---|---|---|
| 1 | **The LIVE Positioning vocabulary is FOUR values and matches no document** -- `cash \| fixed_income \| equity \| hedge` (`lambda_function.py:362-368`). The hardcoded module documents THREE (`:38`), the DynamoDB module FOUR incl. `unknown` (`:91`), the PRD ratifies FIVE. Three documents, three vocabularies, none of them the ratified set. | FWD-1, FWD-2 -- S1-b is a **re-shape** of the vocabulary, not a re-mapping of tickers inside an existing one |
| 2 | ⛔ **THREE unknown-ticker defaults in ONE file, and they DISAGREE** -- `:209` -> `fixed_income` (*"Default to FI if unknown"*), `:360` and `:520` -> `equity`. | FWD-1, FWD-2 -- an unrecognised vol product is absorbed into **Equity** today by a route **independent of the vol/hedge MAPPING**. Fix `C-VOL-HEDGE-STRUCTURED` alone and the Cottonwood symptom survives it |
| 3 | **`yang-generate-cma/` vendors NO classifier module at all** (Positioning's two lambdas each vendor one). | FWD-6 -- the two surfaces cannot "agree" today in the way the outcome means. ⛔ NOT pre-judged: what CMA renders from is S3-a's to establish |

⛔ **AND MEASUREMENT 2 MAKES FWD-1 TRIVIALLY PASSABLE.** *"Every holding lands in exactly one class"*
is satisfied by a default that puts everything unrecognised in Equity. **A criterion the broken system
already passes cannot grade the fix** -- so FWD-1's cells must assert the unknown case explicitly.

---

## 2. THE RECTANGLE -- 7 cells over the PRD's 3 engine rows

### S1 -- ETFClassifier: the one classification source (FWD-1, FWD-2, FWD-5)

| cell | outcome | boundary | bound |
|---|---|---|---|
| **S1-a** `MAKE ONE PLACE THE ONE PLACE` | FWD-5 | The SERVING source is settled (ETFClassifier), so this cell does **not** hunt it. It decides the **AUTHORING** end -- table or seeding dict -- and closes the loop so neither can silently overwrite nor silently fail to serve. **Deliver:** the named one place; the seed trigger **MEASURED** (unmeasured today); the overwrite path closed. | `C-ONE-SOURCE` |
| **S1-b** `FIVE-CLASS VOCABULARY` | FWD-1 | In the source S1-a names: express the five ratified classes; split `other`/`hedge` into Structured / Commodities / Alternatives. | `C-FIVE-CLASSES` |
| **S1-c** `UNKNOWN IS VISIBLE` | FWD-1 | Retire the three disagreeing unknown-defaults. An unrecognised holding renders as unclassified and is **never** absorbed into a class. | `C-FIVE-CLASSES` |
| **S1-d** `VOL / HEDGE / COMMODITY REASSIGNMENT` | FWD-2 | vol + hedge -> Structured; physical / crypto / commodity-index -> Commodities. **This cell ESTABLISHES the edge rules and states them as data** -- it does not inherit them. | `C-VOL-HEDGE-STRUCTURED`, `C-MEMBERSHIP-AT-L5` |

### S2 -- Class registry: order + color (FWD-3, FWD-4)

| cell | outcome | boundary | bound |
|---|---|---|---|
| **S2-a** `CANONICAL ORDER` | FWD-3 | one definition of the fixed order (FI/Cash -> Equity -> Structured -> Commodities -> Alternatives); every renderer reads it; never re-sorted by size or name | `C-FIVE-CLASSES` |
| **S2-b** `CANONICAL COLOR` | FWD-4 | one definition of the five colors (green / blue / pink / gold / orange); no class shows in a color another class uses | `C-FIVE-CLASSES` |

⚠ **S2-a and S2-b are SEPARATE DELIBERATELY** even though one registry may carry both: **a partial cut
of a combined row is invisible to a coverage check scoped to row IDs.** That is the measured defect
this seat dissented on in `NFRA_REPORT` the same night (its own v0.5 entry records `FWD-4` cut into no
cell while L6 passed "12 of 12"). One cell per (row, outcome) pair.

### S3 -- The two surfaces (FWD-6)

| cell | outcome | boundary | bound |
|---|---|---|---|
| **S3-a** `SURFACES READ, NEVER RE-DERIVE` | FWD-6 | Positioning **and** the combined Philosophy/CMA view both read class + order + color from S1/S2. Establishes what CMA renders from today (measurement 3) before wiring anything. Graded over **both**, end to end. | `C-TWO-SURFACES` |

**COVERAGE, BY SUBTRACTION:** 6 declared − {FWD-1: S1-b, S1-c · FWD-2: S1-d · FWD-3: S2-a ·
FWD-4: S2-b · FWD-5: S1-a · FWD-6: S3-a} = **0 uncovered.** A measurement at this cut, not an invariant.

---

## 3. DEPENDENCY CHAIN (the input to L6's `fanout:`)

```
  S1-a  MAKE ONE PLACE THE ONE PLACE        [no dependency -- FIRST, and ALONE]
    |
    +--> S1-b FIVE-CLASS VOCABULARY --+
    |                                  +--> S1-d VOL / HEDGE / COMMODITY
    +--> S1-c UNKNOWN IS VISIBLE -----+
    |
    +--> S2-a CANONICAL ORDER  \  parallel, independent of S1-b..d
    +--> S2-b CANONICAL COLOR  /
                                            |
                        S3-a TWO SURFACES AGREE  <-- needs S1-b/-d and S2-a/-b
```

⛔ **S1-a RUNS ALONE AND NOTHING IS CUT BESIDE IT.** Every other cell writes a class definition and
must write it **where it survives the seed**. A cell that edits the table before S1-a lands is erased
by the next seed run -- and would look like it worked until then.

---

## 4. What this decomposition does NOT do

- **No task order, no dispatch, no worker seated.** L6 is a separate act and is **gated**: `.tools/to-pipeline-gate.py`
  LIMB 6 refuses a task order until **both** L4-R sign-offs are SIGNED in `prd/signoff/` at the current
  `prd_version` -- `4.0.0_SA_CRO` (coverage map) and `3.0.0_SA_CVO` (ENDPOINT vs pins). Neither is in
  at this writing. ⚠ Per `1.0.0_SA_CTO~Z` msg 21183, `3.0.0_SA_CVO~Z` is mid-grade on AMGT_RESAPP's
  judgment criteria and **its taxonomy sign-off is not urgent and must not interrupt that.**
- **No membership rule pre-judged.** `C-MEMBERSHIP-AT-L5` reserves the class edges to S1-d.
- **No source retired.** The hardcoded module is the authoring end of a live chain, not a duplicate.
- **No PRD amendment proposed.** Measurements 1-3 are grounding for cells, inside existing bars.
- **No gate invented, no approval step added.**

## 5. Open, with owners

| what | owner |
|---|---|
| the two L4-R sign-offs (gate L6, not this artifact) | `4.0.0_SA_CRO`, `3.0.0_SA_CVO` |
| PRD header `status: DRAFT` vs s.5's confirmed bars | `1.0.0_SA_CTO~Z` (L4) |
| the L4 stamp is unwritten at a tree home minted AFTER prd-stamp existed (advisory -- WARNs, never blocks) | `1.0.0_SA_CTO~Z` |
| the seed trigger, UNMEASURED | S1-a, this decomposition |

**Push state:** LOCAL at authorship; `0.0.0_AB_MSTR~Z` holds all pushes.
