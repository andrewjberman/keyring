# POSN_ASTTAX -- L5 DECOMPOSITION **DRAFT** (pre-tree)

**archetype:** DIAGNOSE

**Author:** `2.0.0_SA_COO~Z` (L5-L6 owner) · **Date:** 2026-09-11 ~04:1xZ
**PRD:** `docs/architecture/ASSETCLASS_TAXONOMY_PRD.md` v0.1 @`a08aa0efe7`, read IN FULL (168 lines)
**Seating:** `1.0.0_SA_CTO~Z` msg 21150 on Andrew-direct **"do it"**

⛔ **THIS IS A DRAFT AND IT IS NOT AN ISSUANCE.** The decomposition artifacts live in the project TREE,
which does not exist until `POSN` is ratified (record @`425b11ccb1`) and the CTO registers
`org/missions/D4/POSN/POSN_ASTTAX/`. No task order is cut here, no cell is dispatched, no worker is
seated. This is the cell structure plus **the grounding that must not be re-derived later.**

---

## 0. PRD acceptance -- I verified its coverage before building on it

The PRD's s.7 prints *"6 of 6 outcomes carried by exactly one row, 0 uncovered."* **Re-run
independently by subtraction rather than accepted:** declared `endpoint_outcomes` = FWD-1..FWD-6 (6);
covered = FWD-1→S1, FWD-2→S1, FWD-3→S2, FWD-4→S2, FWD-5→S1, FWD-6→S3 (6); **uncovered = 0. It holds.**
Recorded because the sibling PRD I read tonight printed the same shape and was wrong by two.

---

## 1. ⛔ THE GROUNDING -- and it changes what S1 IS

The PRD's `C-ONE-SOURCE` names *"the shared ETF classification module
(`etf_classification.py` **and** `etf_classifications_dynamodb.py`, the module the positioning and CMA
lambdas already share -- 'ETFClassifier')"* and correctly says FWD-5's investigation confirms it
*"or finds where it truly lives -- it is NOT hard-pre-judged here."*

**MEASURED AT L5, so the cell starts from facts rather than from the search:**

| | `etf_classification.py` | `etf_classifications_dynamodb.py` |
|---|---|---|
| lines | 1,114 | 347 |
| the symbol Andrew named | **absent** -- module-level functions + dicts | ⭐ **`ETFClassifier` IS HERE** (class, :49-195) |
| backing store | a HARDCODED `ETF_CLASSIFICATIONS` dict (~900 lines of it) | **DynamoDB table `etf-classifications`** |
| class vocabulary | `'fixed_income' \| 'equity' \| 'other'` (**3**, stated :38) | `"fixed_income" \| "equity" \| "hedge" \| "unknown"` (**4**, stated :91) |
| unknown ticker | ⛔ **DEFAULTS TO `'equity'`** and logs a warning (:916, :928-930) | returns `"unknown"` (:94) |
| self-description | *"This is the single source of truth for ETF asset class classification"* (:39) | *"This replaces scattered inline hardcoded mappings with a single source of truth"* (:7) |

⛔ **BOTH FILES CLAIM, IN THEIR OWN TEXT, TO BE THE SINGLE SOURCE OF TRUTH** (`etf_classification.py:39`
and `etf_classifications_dynamodb.py:7`). Two self-reports, flatly contradictory, and **nothing in
either text can break the tie.**

### ⭐ SETTLED BY ANDREW-DIRECT 2026-09-11 ~04:2xZ -- and by the instrument he named

VERBATIM: *"I think ETFClassifier is the real one"* / *"check to see what is already hooked up to
Positioning page thats how youll kow for sure"*. Record:
`org/tier1_exec/2.0.0_SA_COO~Z/deliverables/ANDREW_DIRECT_20260911_04xxZ_ETFCLASSIFIER_IS_THE_REAL_ONE_CHECK_THE_POSITIONING_PAGE.md`

Executed. `yang-generate-positioning/lambda_function.py:25` `from etf_classifications_dynamodb import
ETFClassifier`, `:31` `etf_classifier = ETFClassifier()`; `yang-generate-holdings-attribution` vendors
the same module. **He is right: Positioning runs ETFClassifier.**

⛔ **AND FOLLOWING HIS INSTRUMENT ALL THE WAY FALSIFIED THIS DRAFT'S FIRST FRAMING.** I had these as
two INDEPENDENT competing sources -- which is what their headers say and what I wrote. It is wrong.
`seed-etf-classifications.py:58` reads `"asset_class": ETF_CLASSIFICATIONS.get(ticker, "unknown")` --
`ETF_CLASSIFICATIONS` being the hardcoded dict. **It is ONE CHAIN, NOT A FORK:**

```
  etf_classification.py  (hardcoded ETF_CLASSIFICATIONS)        [AUTHORING source]
        |  seed-etf-classifications.py  WRITES
        v
  DynamoDB  etf-classifications                                  [STORE]
        |  ETFClassifier (etf_classifications_dynamodb.py) READS
        v
  Positioning page                                               [SERVING source]
```

So the hardcoded module is **not a rival to retire -- it is what SEEDS what ETFClassifier serves**, and
both halves of his sentence hold at once.

⛔ **WHICH IS EXACTLY WHY FWD-5 IS STILL OPEN.** Its bar is *change a definition in ONE place and
everywhere reflects it.* There are **two candidate "one places" with different failure modes**: change
the TABLE and the next seed run silently overwrites you from the dict; change the DICT and nothing
serves it until the seed re-runs (whose trigger is UNMEASURED here). **Neither is "one place" as FWD-5
means it.** S1-a decides which becomes it -- a decision with its facts on the table, no longer a search.

⚠ **NEITHER VOCABULARY IS THE RATIFIED FIVE.** (c) has 3 categories, so `other` must SPLIT into
Structured / Commodities / Alternatives. (b) has 4 and carries `hedge` **as a class**, which
`C-VOL-HEDGE-STRUCTURED` routes to Structured -- and has no Commodities and no Alternatives at all. So
S1 is a **re-shape of the class vocabulary**, not a re-mapping of tickers within an existing one.

⭐ **AND A SECOND, INDEPENDENT CAUSE OF THE COTTONWOOD SYMPTOM, WHICH THE PRD DOES NOT CARRY.**
`get_asset_class(ticker, default='equity')` means **an unrecognised ticker is silently classified
EQUITY today.** So an unknown volatility product inflates the equity total by a route that has nothing
to do with the vol/hedge mapping `C-VOL-HEDGE-STRUCTURED` addresses. Fixing the mapping alone leaves
this open.
⛔ **AND IT MAKES FWD-1 TRIVIALLY PASSABLE:** *"every holding lands in exactly one class"* is satisfied
by a default that puts everything unrecognised in Equity. **A criterion a broken system already passes
cannot grade the fix.** Any FWD-1 cell must therefore assert the unknown case explicitly -- an
unclassified holding is VISIBLE as unclassified, never silently absorbed.

---

## 2. The cells

Rectangle over the PRD's three engine rows. Fan-out is stated as data at L6, not here.

### S1 -- ETFClassifier: the one classification source (FWD-1, FWD-2, FWD-5)

| cell | outcome | boundary | why separate |
|---|---|---|---|
| **S1-a** `MAKE ONE PLACE THE ONE PLACE` | FWD-5 | ⭐ **NARROWED by the Andrew-direct: the SERVING source is settled (ETFClassifier), so this cell no longer hunts it.** It decides the AUTHORING end -- whether the table or the seeding dict becomes FWD-5's "one place" -- and closes the loop so the other cannot silently overwrite or silently fail to serve. Deliver: the named one place, the seed trigger MEASURED (unmeasured today), and the overwrite path closed. | ⛔ **EVERY OTHER CELL DEPENDS ON ITS ANSWER**, because S1-b/-c/-d all write a class definition and must write it where it survives. A cell that edits the table before this lands is erased by the next seed run. |
| **S1-b** `FIVE-CLASS VOCABULARY` | FWD-1 | In the source S1-a names: express the five ratified classes; split `other`/`hedge` into Structured / Commodities / Alternatives per `C-FIVE-CLASSES`. | the vocabulary is a schema change and precedes any ticker moving |
| **S1-c** `UNKNOWN IS VISIBLE` | FWD-1 | Retire the silent unknown-defaults. An unrecognised holding renders as unclassified and is never absorbed into a class. ⛔ **MEASURED: `yang-generate-positioning/lambda_function.py` carries THREE unknown-defaults and they DISAGREE -- `:209` -> `fixed_income` ("Default to FI if unknown"), `:360` and `:520` -> `equity`.** Same handler, same run, opposite fallbacks. | ⭐ **the second, independent cause of the Cottonwood symptom** -- an unrecognised vol product is absorbed into Equity by `:360` today, by a route that has nothing to do with the vol/hedge MAPPING. Fix S1-d alone and this remains. Not in the PRD, and without it **FWD-1 grades green on the broken system** |
| **S1-d** `VOL / HEDGE / COMMODITY REASSIGNMENT` | FWD-2 | vol + hedge → Structured; physical / crypto / commodity-index → Commodities. `C-MEMBERSHIP-AT-L5`: **this cell establishes the edge rules and states them as data**, it does not inherit them. | the Cottonwood catalyst; graded on real portfolios, so it needs S1-b's vocabulary to exist first |

### S2 -- Class registry: order + color (FWD-3, FWD-4)

| cell | outcome | boundary | why separate |
|---|---|---|---|
| **S2-a** `CANONICAL ORDER` | FWD-3 | one definition of the fixed order (FI/Cash → Equity → Structured → Commodities → Alternatives); every renderer reads it; never re-sorted by size or name | APPLIED bar, independent of color |
| **S2-b** `CANONICAL COLOR` | FWD-4 | one definition of the five colors (green / blue / pink / gold / orange); no class shows in a color another uses | APPLIED bar. ⚠ **Separate from S2-a deliberately:** one registry may carry both, but a partial cut of a combined row is invisible to an id-scoped coverage check -- the exact defect I dissented on in `NFRA_REPORT` two hours ago |

### S3 -- The two surfaces (FWD-6)

| cell | outcome | boundary | why separate |
|---|---|---|---|
| **S3-a** `SURFACES READ, NEVER RE-DERIVE` | FWD-6 | Positioning **and** the combined Philosophy/CMA view both read class + order + color from S1/S2. `C-TWO-SURFACES`: FWD-6 is graded over **both**, read end to end. | the only outcome the surfaces themselves own; depends on S1 and S2 |

⚠ **MEASURED, AND S3-a IS WIDER THAN IT LOOKS: `yang-generate-cma/` VENDORS NO CLASSIFIER MODULE AT
ALL.** Positioning's two lambdas each vendor `etf_classifications_dynamodb.py`; the CMA lambda vendors
neither module. So the two surfaces cannot "agree" today in the way FWD-6 means -- one of them is not
wired to the classification chain. ⛔ **NOT PRE-JUDGED:** CMA may render asset classes from another
route entirely, or not render them at all; this cell establishes which before wiring anything. What is
measured is only the absence of a vendored classifier in that directory.

**COVERAGE, BY SUBTRACTION:** declared 6 − covered {FWD-1: S1-b,S1-c · FWD-2: S1-d · FWD-3: S2-a ·
FWD-4: S2-b · FWD-5: S1-a · FWD-6: S3-a} = **0 uncovered.**
⛔ **Measurement at this draft, NOT an invariant** -- if the CTO adds an outcome, this line is re-run,
not re-asserted. That is the failure I dissented on tonight and it is not repeated here.

**ONE CELL PER (row, outcome) PAIR** where a row serves several, per the sibling PRD's own
recommendation to L5 -- which is why S1 is four cells and not one.

---

## 3. Dependency chain (drives L6 `fanout:`)

```
  S1-a  SOURCE-ADJUDICATION   [no dependency -- FIRST, and alone]
    |
    +--> S1-b FIVE-CLASS VOCABULARY ---+--> S1-d VOL/HEDGE/COMMODITY
    |                                   |
    +--> S1-c UNKNOWN IS VISIBLE  ------+
    |
    +--> S2-a CANONICAL ORDER  \
    +--> S2-b CANONICAL COLOR  /  (parallel; independent of S1-b..d)
                                       |
                       S3-a  TWO SURFACES AGREE  <-- needs S1-b/-d and S2-a/-b
```

⛔ **S1-a RUNS ALONE AND NOTHING IS CUT BESIDE IT.** Its answer can move every other cell's write
surface -- a cell written against (c) is wasted if the answer is (b). The PRD's own s.8 sequencing says
the same thing in its own words: *"confirm the shared classification module is the one source ... BEFORE
building on it."*

---

## 4. What this draft does NOT do

- **No task order, no dispatch, no worker.** L6 is a separate act and needs the tree.
- **No membership rules pre-judged.** `C-MEMBERSHIP-AT-L5` reserves the edges (Structured vs
  Commodities vs Alternatives) to S1-d, and S1-d states them as data.
- **No source chosen.** §1 measures three candidates and names none authoritative -- that is S1-a's.
- **No PRD amendment proposed.** The unknown→equity finding is grounding for a cell, not a defect
  claim against the PRD; it sits inside FWD-1's existing bar.
- **No gate.**

## 5. What it is waiting on

1. **Andrew** -- ratify `D4` (record @`425b11ccb1`; REC `[POSN, ETFS]`).
2. **Andrew** -- the `ASSETCLASS_TAXONOMY` → `POSN_ASTTAX` rename (PRD s.7 open call). **The macro
   alone does not clear it** -- the current code is REFUSED by the tree grammar.
3. **`1.0.0_SA_CTO~Z`** -- tree registration, then this draft formalizes as `decompositions/`.
4. **L4-R sign-offs** (CRO + CVO) govern L6, not L5 -- LIMB 6 refuses a task order against an unsigned
   PRD, so they are on the critical path to the ISSUANCE and not to this draft.

**Push state:** LOCAL at authorship; `0.0.0_AB_MSTR~Z` holds all pushes.
