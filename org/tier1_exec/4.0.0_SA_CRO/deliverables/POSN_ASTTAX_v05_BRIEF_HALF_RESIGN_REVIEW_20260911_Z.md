# POSN_ASTTAX PRD v0.5 -- BRIEF HALF, RE-REVIEW AND RE-SIGN

`4.0.0_SA_CRO~Z`, 2026-09-11 ~21:1xZ. L4-R brief half (spine v3.15).
Subject: `org/missions/D4/POSN/POSN_ASTTAX/prd/POSN_ASTTAX_PRD.md`, brief `half_hash 3c1c3202ca9e`,
amendment `@49ddcc481d`.

## 1. VERIFIED BEFORE READING THE SUBSTANCE

| check | result |
|---|---|
| brief half | `3c1c3202ca9e` -- matches the hash the gate names |
| ratified-text | `1c60358b916e`, SIGNED by `3.0.0_SA_CVO~Z` and **current** -- the amendment did not reach it |
| `endpoint_outcomes` | 6, unchanged |
| worktree | clean at sign |

## 2. WHAT CHANGED: `C-RETAG-SAFETY` RE-FOUNDED, NOT RE-SEQUENCED

The constraint's stated mechanism was **falsified by the measurement the constraint itself ordered**.
`AT2-s-6` hardened the generator and killed the `KeyError`: `TO-S7-1` measured **0 of 17 hops RAISE**.

- **LIVE mechanism now stated:** a retag renders `'Unknown'` and **silently zeroes the weight**. The
  page still renders.
- **ORIGINAL mechanism preserved as history**, explicitly marked non-operative -- the fixed-key
  dicts, the `KeyError`, the page blanking for all four partner firms.
- **The constraint still BINDS.** Only its reason changed.

⭐ **THE HAZARD GOT QUIETER, NOT SAFER, AND THE AMENDMENT SAYS SO IN THOSE TERMS.** A blank page is
noticed in seconds; a zeroed allocation line looks like a real allocation. That is strictly worse for
detection than what it replaced, and a reader of the OLD text would have gone looking for a crash
that can no longer happen.

## 3. THE REPAIR THIS SEAT RATES HIGHEST -- STEP (2) IS NOW A CONDITION, NOT AN ACT

> *"for EVERY ticker in the retag set, the SERVED `asset_class` value equals its ratified five-class
> label AND its allocation weight is NON-ZERO and equal to its pre-retag weight, read from the served
> artifact."* — and, stated outright: **"Step (2) is currently NOT MET."**

⛔ **A STEP THAT NAMES A TASK IS SATISFIED BY DOING THE TASK; A STEP THAT NAMES A CONDITION IS
SATISFIED ONLY BY THE WORLD.** The old wording ("verify the chain") is what let a completed
verification cell be read as a passed one -- an error `1.0.0_SA_CTO~Z` made, withdrew, and has now
designed out of the spec rather than merely apologised for. **The bar also fails in the broken
world**, which "confirm the page still renders" never could: a retagged ticker at a zeroed weight
renders fine and fails this bar.

## 4. CARRIAGE VERDICT -- SIGN

The brief half's test is CONTENT CARRIAGE, and the amendment is explicit about the one thing that
could have broken it: **"Andrew's ruling and the DT brief are UNCHANGED; only the mechanism the
round-3 cells will read."** The brief's `KeyError`/page-blank account is not deleted and not
re-graded -- it is preserved as what was true when the DT brief was written, and marked as
superseded by a later measurement. That is the correct treatment and the same one this project
adopted for `opal-data-research`'s ABSENT reading.

⭐ **AND THE AMENDMENT CREDITS ITS OWN CONTRADICTION:** *"THE PRD ASKED FOR THE MEASUREMENT THAT
CONTRADICTED IT, AND GOT IT -- that is the instruction working, not failing."* Correct, and the
generalisation it draws is the durable part: **prose predates its own instrument's answer, so a spec
that ORDERS a measurement must be RE-READ WHEN THE ANSWER LANDS.**

⚠ **ONE QUALIFIER CARRIED CORRECTLY AND WORTH NAMING:** the 17-hop figures are pinned to `TO-S7-1`'s
run, and `3.0.0_SA_CVO~Z` records that `S1` later repaired a benchmark hop -- so **the RATIO is
historical while the VERDICT is not**, re-confirmed against current controls. Distinguishing a stale
NUMBER from a still-live CONCLUSION is exactly the discipline this project keeps needing.

## 5. VERDICT

**SIGNED** -- brief half, `half_hash 3c1c3202ca9e`, PRD v0.5, tree clean at sign.

⛔ Certification scope: brief CONTENT CARRIAGE only. **NOT certified:** the ratified-text half
(`3.0.0_SA_CVO~Z`'s, untouched and current), whether step (2) can be met, the retag itself, or
round 3's readiness. Step (2) is NOT MET by the spec's own words and `TO-S2-1`/`TO-S3-1` remain
correctly uncut.

Push state: LOCAL at write; this seat does not push.

---

## 6. SECOND REVIEW -- brief `0cc8a7d2dd9d` @`71a376b98e`. SIGNED

**Supersedes section 5's verdict. Sections 1-5 stand.** The bar this seat signed two hours ago was
NARROWER THAN THE HAZARD, and the defect was in the re-founding itself.

| check | result |
|---|---|
| brief half | `0cc8a7d2dd9d` -- matches |
| ratified-text | `1c60358b916e` **UNCHANGED** -- CVO signature intact |
| `endpoint_outcomes` | 6, unchanged |
| worktree | clean at sign |

### 6a. ⛔ A NEW FAILURE MODE, AND IT IS NOT THE ONE SECTION 3 PRAISED

Section 3 rated step (2) highly for being a CONDITION rather than an act, and for FAILING IN THE
BROKEN WORLD where `S2-AC5` could not. **Both of those remain true and both were insufficient.**
The bar read *"from the served artifact"* -- meaning `positioning_data.json` alone -- and
`2.0.0_SA_COO~Z`'s wave-1 cells measured **both collapse sites OUTSIDE that artifact**:

- **DOWNSTREAM:** `HoldingsTab.tsx:1392-1394` iterates a HARDCODED
  `assetClassOrder = ['Fixed Income','Equity']`. A `Commodities`/`Structured`/`Alternatives` group is
  **NEVER ITERATED** -- the row renders NOWHERE while its weight stays in the grand total. 42 of 42
  consumers, 12 sites, 8 files.
- **A DIFFERENT ARTIFACT:** `yang-generate-allocation-summary` carries `Commodities` through all 88
  hops, then draws `policy_weight 0.0` from a two-key `BENCHMARK_ALLOCATIONS`, writing
  `holdings_attribution_data.json`.

⭐ **SO THE CELL COULD HAVE RETURNED GO -- CORRECTLY, ABOUT THE ARTIFACT IT WAS POINTED AT -- WHILE
THE PAGE DROPPED THE ROW.** `TRUE AND INSUFFICIENT`. That is a THIRD criterion pathology, distinct
from the two this project already names: not always-passes (`S2-AC5` could not fail at all), and not
unsatisfiable -- **a criterion that discriminates correctly over the WRONG DOMAIN.** It is Rule 24's
wrong-domain subtraction wearing a criterion's clothes, and it reads as rigorous precisely because it
*can* fail.

### 6b. THE EVIDENCE THAT MAKES (c) AND (d) BARS RATHER THAN ADVICE

**This exact bug has already SHIPPED.** The same file documents it for `Cash` at `:1364-1372`,
measured on PROD v2.1.167: **PFDE 90 -> 89 served-vs-DOM rows, subtotals 99.98 under a grand total of
100.01.** The remedy folded only `Cash` and `Hedge` -- **so a retag reproduces it with a new value.**
A bar that did not check RENDER and SUBTOTAL would have certified the reproduction.

⭐ **THE MECHANISM IN THE MEASURING WORKER'S OWN WORDS:** *"Data reaches three lambdas; the code
hardening reaches one."* That sentence is why hardening one write surface never bounded this.

### 6c. VERDICT

**SIGNED** -- brief half, `half_hash 0cc8a7d2dd9d`, PRD v0.5, tree clean at sign.

Carriage holds and is materially better than what section 5 signed: the bar now spans **every served
surface the retagged value reaches**, with (a) served value, (b) non-zero unchanged weight,
(c) **the row RENDERS** -- served row count equals DOM row count -- and (d) **class subtotals sum to
the grand total**.

⚠ **AND MY OWN SECTION 3 IS CORRECTED BY THIS, NOT MERELY SUPERSEDED.** I praised the bar for failing
in the broken world without asking WHICH broken worlds it could see. "Fails in the broken world" is
necessary and not sufficient; the next question is **"over what domain?"** -- and I did not ask it.
`2.0.0_SA_COO~Z` did, by measuring the consumers rather than reasoning about the artifact.

⛔ Scope unchanged: brief CONTENT CARRIAGE only. Step (2) is still NOT MET; `TO-S2-1`/`TO-S3-1`
remain correctly uncut and ADMITTED is not a retag GO.
