# POSN_ASTTAX -- ROUND 2 DECOMPOSITION: the curated-list reconciliation (5 cells)

**archetype:** DIAGNOSE

**Owner (L5-L6):** `2.0.0_SA_COO~Z` · **Date:** 2026-09-11 ~07:4xZ · **Directive:** D4 · **Macro:** POSN
**PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.4**, content pin `bcc2061b549a`, read at this version
**Cut from:** `ledger/ROUND_ANALYSIS.round1-addendum.md` @`7f20d4f2d9` s.A3 -- which SUPERSEDES
`ROUND_ANALYSIS.round1.md` @`1eb5f44a2c` s.4. **The addendum is the operative routing.**
**Project rectangle:** `POSN_ASTTAX_DECOMP.md` · **Round 1:** `POSN_ASTTAX_DECOMP_round1.md` (CLOSED)

---

## 0. THE FRAME CHANGED BETWEEN ROUNDS, AND THIS SEAT'S ROUND-1 EMPHASIS WAS PART OF WHAT MOVED

`C-CLASSIFIER-PURPOSE` (v0.4, Andrew-direct via `3.0.0_SA_CVO~Z` C-S3 @`4275402ec2`) rules that
ETFClassifier is a **CURATED TAGGING LIST** a person extends on acquisition -- not a single-source-of-truth
architecture. ⛔ **THAT COLLAPSES TWO THINGS THIS SEAT PUT FORWARD AS EVIDENCE AT DRAIN-END, AND THE
RECORD SHOULD SAY SO PLAINLY:**

- I reported the seed trigger measuring **ZERO** (0 of 45) and **169 table-only tickers**, and wrote that
  "both facts point the same direction." **They do not point at a defect.** For a list a person extends,
  the person IS the mechanism, and `updated_by` attributes all 285 rows with ZERO unattributed.
- ⚠ **THE MEASUREMENTS STAND -- ONLY THE EMPHASIS WAS WRONG.** The addendum says this in terms ("the
  correction is to the FRAME, not the measurements"), and every set figure survives: DICT 136 / TABLE 285
  / BOTH 116 / dict-only 20 / table-only 169 / union 305 / disagreement 189, zero value-level mismatches.
  I labelled it "evidence, not a ruling" and deferred the verdict, which was right; the sentence that
  carried an implication was "both facts point the same direction", and that is the one to retract.

⛔ **SO THIS DECOMPOSITION CARRIES A NEGATIVE BOUNDARY, NOT JUST POSITIVE CELLS.** `C-CLASSIFIER-PURPOSE`
(b) FORBIDS two pieces of work outright: **"give the seed a trigger"** and **"account for the 169"**. No
cell below may drift into either, and a worker that finds itself scheduling anything has left its cell.

**FWD-5's one place is SETTLED: the served TABLE** (`C-CLASSIFIER-PURPOSE` (a)). The dict is a superseded
seed input to retire/reconcile, never a competing source. Round 1's question is answered and closed.

---

## 1. THE CELLS -- 5: four additive to a curated list, plus one SAFETY cell added mid-cut

| cell id | readable name | serves | from addendum |
|---|---|---|---|
| **`AT2-s-1`** | UNKNOWN IS NOT `equity` | FWD-1 | A3(1) PRIMARY |
| **`AT2-s-2`** | ADDITIVE FIVE-CLASS RECONCILIATION | FWD-1, FWD-2 | A3(2) |
| **`AT2-s-3`** | `is_hedge()` RECONCILIATION | FWD-1 | A3(3), disarms C-S1 |
| **`AT2-s-4`** | THE THREE BLANK SUB-ASSET-CLASS ROWS | FWD-1 | A3(4) |

### `AT2-s-1` -- UNKNOWN IS NOT `equity` (PRIMARY)

`equity` is BOTH a ratified class AND the positioning lambda's unknown-default
(`yang-generate-positioning/lambda_function.py:359`, with a second at `:520` and a THIRD defaulting to
`fixed_income` at `:209` -- measured round 1, `S1a-AC8`). ⛔ **A registry whose job is keeping securities
PROPERLY TAGGED cannot let "properly tagged equity" and "not recognised" be the same string**
(`C-CLASSIFIER-PURPOSE` (c)). The cell makes the two distinguishable and makes an unrecognised holding
VISIBLE as unrecognised.
⚠ **IT TOUCHES THE POSITIONING LAMBDA, NOT ONLY THE REGISTRY** -- the defaults live in the lambda. That
is a wider write surface than the other three cells and its order must name it.
⭐ **AND IT IS THE ONE CELL WHOSE OUTCOME A BROKEN SYSTEM ALREADY PASSES:** FWD-1's bar, "every holding
lands in exactly one class", is satisfied today by a default that files everything unrecognised as
Equity. Its criteria must assert the unknown case explicitly or they cannot grade the fix.

### `AT2-s-2` -- ADDITIVE FIVE-CLASS RECONCILIATION

ADD `Commodities` and `Alternatives` to the stored vocabulary (stored THREE, ratified FIVE), and move the
SEVEN served `hedge` tickers to ratified classes per `C-VOL-HEDGE-STRUCTURED` as disambiguated at v0.3:
**SIX -> Commodities (DBC, GLD, GSG, IAU, SLV, USO); VIXY -> Structured.** `sub_asset_class` is the
authoritative signal and already reads Gold/Silver/Oil/Commodities/Volatility, so no edge needs ruling.
⛔ **THE `hedge` VALUE DISSOLVES; IT DOES NOT RENAME WHOLESALE.** A wholesale rename mis-files the six --
the error caught at the issuer this round and now named in the constraint itself.
⚠ **VXX IS NOT ONE OF THE SERVED SEVEN.** It is served `equity` and is in Andrew's satellite file; whether
it is a current holding is the cell's to establish, not to assume.

### `AT2-s-3` -- `is_hedge()` RECONCILIATION

Channel row **C-S1** (BLOCKING, ARMED, disarm_owner `1.0.0_SA_CTO~Z`): the module documents three values
including `'other'`, 0 of 136 use `'other'`, 7 use an undocumented `'hedge'` -- which empties
`HEDGE_TICKERS` and makes `is_hedge()` always false. Measured DORMANT (no live caller). Populate or retire
per the vocabulary `AT2-s-2` settles; the two access paths must stop disagreeing.
**Depends on `AT2-s-2`** -- reconciling a predicate against a vocabulary that is still moving is a rewrite
twice.

### `AT2-s-4` -- THE THREE BLANK SUB-ASSET-CLASS ROWS

`sub_asset_class` is populated on **282 of 285**; three blanks are the real coverage gap in what the
registry exists to do. ⛔ **RE-TAKE THE COUNT; DO NOT INHERIT IT** -- the figure is the CTO's at its
vintage and the table is a live curated list a person may have extended since. Independent of the other
three cells.

### `AT2-s-5` -- THE `management_style: "unknown"` PRODUCTION LANDMINE (SAFETY, ADDED AFTER THE CUT)

⛔ **ADDED 2026-09-11 ~07:5xZ, BEFORE THIS DECOMPOSITION WAS COMMITTED, ON A BRIEF THAT ARRIVED MID-CUT**
-- `docs/briefs/positioning-gld-vxx-satellites-20260911.md` (`0.4.0_DT_ClientPlatform`, Andrew-direct
"this needs to get folded into the work on POSN_ASTTAX", relayed 21264).

The brief's conclusion 5: adding GLD to the models TODAY crashes the positioning generator with a
KeyError and **BLANKS THE PAGE FOR ALL FOUR PARTNER FIRMS**, because GLD's registry row carries
`management_style: "unknown"` and the default-to-passive guard cannot fire on a non-empty string.

⭐ **VERIFIED INDEPENDENTLY BY THIS SEAT AT THE CUT, and the result is that the unsafe set IS this
round's move set:** `batch-get-item` over the seven served `hedge` tickers returns
`management_style: "unknown"` on **DBC, GLD, GSG, IAU, SLV and USO -- all six going to Commodities** --
and `passive` on VIXY, the one going to Structured.

**The cell:** make those rows safe to hold -- populate `management_style` (or make the guard fire on
`"unknown"`), so that a later allocation decision cannot take the page down. ⛔ **IT DOES NOT ADD ANY
HOLDING AND DOES NOT TOUCH YANG'S MODELS**; whether GLD is ever held is an ALLOCATION decision and
explicitly not this project's (brief conclusion 2).
⚠ **ORDERING IS THE POINT AND IT COMES FROM THE BRIEF: "one DynamoDB field plus a decision from Yang --
IN THAT ORDER."** This cell is a PRECONDITION to any allocation act, not a follow-up to one.
⚠ It writes the SAME ROWS as `AT2-s-2` but a DIFFERENT FIELD. The two orders must name disjoint fields
and state the shared row set, or they race.

**COVERAGE BY SUBTRACTION:** addendum A3 routes FOUR pieces; the mid-cut brief adds a FIFTH (safety).
Cells cover A3(1)->`AT2-s-1`, A3(2)->`AT2-s-2`, A3(3)->`AT2-s-3`, A3(4)->`AT2-s-4`, brief-5->`AT2-s-5`.
**5 declared MINUS 5 covered = 0 uncovered.** A measurement at this cut, not an invariant.

⛔ **AND TWO PIECES OF THE BRIEF ARE EXPLICITLY NOT CUT, because it says they are not work:**
**VXX needs nothing built** (conclusion 1 -- already in, correct weights, sub_asset_class Volatility,
flowing into Satellites 70/80/90/98), and **GLD's absence is an ALLOCATION decision, not an engineering
gap** (conclusion 2 -- every piece of plumbing including its registry row already exists). ⚠ Conclusion 3
also falsifies a premise this project never held but a reader might: the Satellites toggle reads the
MODELS payload, NOT the Bloomberg ETF pull, so nothing here should touch the ETFS pull.

---

## 2. DEPENDENCY CHAIN (the input to L6's `fanout:`)

```
  AT2-s-5  management_style SAFETY    [independent -- HIGHEST PRIORITY, a live page-down precondition]
  AT2-s-1  UNKNOWN IS NOT equity      [independent -- PRIMARY, the registry's auditability]
  AT2-s-2  ADDITIVE FIVE-CLASS  --->  AT2-s-3  is_hedge() RECONCILIATION
  AT2-s-4  THREE BLANK SUB ROWS       [independent]
```

Four chain heads: `AT2-s-5`, `AT2-s-1`, `AT2-s-2`, `AT2-s-4`. **`fanout: 4 of 4 chains, cap 8`** -- unlike
round 1, this round CAN run in parallel and nothing forces a single-cell round.
⛔ **`AT2-s-5` GOES FIRST AMONG EQUALS.** It is not a dependency of the others in the graph sense, but it
is the only cell standing between a routine allocation decision and a blank page for four partner firms.
⚠ `AT2-s-1` and `AT2-s-2` both touch classification and must not be given the same write surface: `s-1`
owns the lambda's DEFAULTS, `s-2` owns the stored VOCABULARY and the seven rows. Their orders must name
disjoint `<paths>`.

## 3. HOW THIS RELATES TO THE PROJECT RECTANGLE

Round 2's cells RE-SHAPE three of the rectangle's round-1-era cells -- the five-class vocabulary, the
unknown-is-visible and the vol/hedge/commodity cells (rectangle rows 2, 3 and 4) -- which the corrected
routing merges and re-cuts; and ADD `AT2-s-4`, which the rectangle did not carry at all (the blank
sub-asset-class rows were not known at L5). **The rectangle's rows 5, 6 and 7 -- canonical order,
canonical color and the two-surface agreement -- are NOT in round 2** and remain for a later round.

⛔ **THE RECTANGLE'S CELL IDS ARE DELIBERATELY NOT WRITTEN HERE AS LITERALS.** The gate scrapes cell ids
from the WHOLE document, so naming another round's ids in prose would declare them as THIS round's cells
and refuse the issuance for failing to cover them. Measured on this very file before it was committed:
the first draft scraped **10** ids where the round declares **4**. Same trap as round 1's, caught this
time by re-scraping with the gate's own regex before committing rather than by a refusal.
⛔ **THE RECTANGLE IS NOT SILENTLY REWRITTEN:** it stands as authored, this file states the re-shape, and
a reader comparing the two gets the delta rather than a contradiction.

## 4. WHAT THIS ROUND DOES NOT DO

- ⛔ **No scheduler, trigger, monitor or alert of any kind.** `C-CLASSIFIER-PURPOSE` (b) forbids it and
  the estate's standing moratorium forbids it independently. Two bars, not one.
- ⛔ **No "account for the 169".** Explicitly struck by the same constraint.
- No retirement of the dict beyond what `AT2-s-2`/`AT2-s-3` reconcile -- a superseded input is retired
  deliberately, and nothing here authorises deleting it.
- No class-edge rulings beyond what `sub_asset_class` already carries (`C-MEMBERSHIP-AT-L5`).
- No surface work -- order, color and the two-surface agreement are a later round's.

## 5. THE GATE, READ WITH THE TOOL THAT NOW OWNS IT

⛔ **THE L4-R RULE CHANGED WHILE THIS FILE WAS BEING WRITTEN (spine v3.15), AND MY FIRST DRAFT OF THIS
SECTION WAS ALREADY WRONG.** It said "both sign-offs read SIGNED at v0.4". **Sign-offs are no longer
bound to `prd_version` -- they bind to the HASH OF EACH HALF'S SECTIONS**, and the PRD now has TWO
HALVES with different owners:
- **ratified-text** (ENDPOINT + CONTRACTS) -- `3.0.0_SA_CVO`, **always**;
- **brief** (everything else) -- `4.0.0_SA_CRO`, or a live `2.0.0_SA_COO` **not holding the round** in
  its stead (Andrew-direct 2026-09-11 ~05:3xZ: *"CVO should always be included. If CRO is not online,
  can do COO in their stead"*).

⛔ **THIS SEAT CANNOT SIGN THE BRIEF HALF FOR THIS PROJECT.** It holds the round. The stand-in clause
is for a COO that does not, and reading it otherwise would be a seat signing off its own work.

**MEASURED at this write with the tool that owns it, `python .tools/prd-signoff.py status POSN_ASTTAX`:**

```
  POSN_ASTTAX  v0.4 @65844d868c  dep_stage=EXECUTING  ->  WITHHELD
    ratified-text  STALE   3.0.0_SA_CVO~Z   signed at v0.3; the half's bytes have changed since
    brief          STALE   4.0.0_SA_CRO~Z   signed at v0.1; the half's bytes have changed since
```

Both halves OWED, both owners LIVE, `.tools/to-pipeline-gate.py` LIMB 6 refuses a task order while
either is unsigned. ⚠ The brief half has been stale since **v0.1** -- four versions -- which the old
version-bound reading would have shown as simply "not signed at v0.4" and the hash-bound one explains:
its bytes moved under a signature that was never renewed.

**THIS DECOMPOSITION IS L5 AND IS NOT GATED. THE ISSUANCE IS**, and this seat holds it rather than
working around it. ⚠ A merge window (`0.0.0_AB_MSTR~Z` 21266) is also open at this write, so this file
is authored now and committed after the CLOSE line.

⚠ The round-1 L5/L6/L8/L9/L10 stamps all read STALE-PIN and MUST NOT be re-stamped -- they record acts
against v0.1-v0.3 that genuinely happened there. Round 2 mints its own.

**Push state:** LOCAL at authorship; `0.0.0_AB_MSTR~Z` holds all pushes.
