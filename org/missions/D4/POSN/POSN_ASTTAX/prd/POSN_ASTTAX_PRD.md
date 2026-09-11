# POSN_ASTTAX -- PRD (step 4)

```json
{
 "project": "POSN_ASTTAX",
 "directive": "D4",
 "fabric": "site-z",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_ASSET_CLASS_TAXONOMY_BRIEF.md@03f1d00ec4",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6"],
 "status": "DRAFT"
}
```

**Version:** v0.1, 2026-09-11 -- first PRD. **Author** `1.0.0_SA_CTO~Z` (L4). **Brief:** the nomenclature
transcript's substance, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_ASSET_CLASS_TAXONOMY_BRIEF.md@03f1d00ec4`.
**Endpoint confirmed by Andrew** 2026-09-11 (see s.5). **Home note:** tree-homed at
`org/missions/D4/POSN/POSN_ASTTAX/prd/` as `POSN_ASTTAX` (macro POSN), renamed from
`ASSETCLASS_TAXONOMY` on Andrew's ratify of the D4 macro enum `[POSN, ETFS]` 2026-09-11 -- the former
10-char head `ASSETCLASS` matched no macro under the tree grammar `^[A-Z]{4}_[A-Z0-9]{3,18}$`. The
project now runs the full canonical flow (L4-R sign-offs in `prd/signoff/` + prd-stamps).

---

## ENDPOINT (step 2, /endpoint --forward)

```
ENDPOINT -- POSN_ASTTAX (confirmed by Andrew 2026-09-11)

  FWD-1  Every holding is sorted into exactly one of five asset classes
         DONE WHEN  EXERCISED -- real portfolios have been re-sorted under the five
                    classes and every holding lands in exactly one, including the
                    ones that used to be lumped together
         ACCEPT     Someone opens a classified portfolio and finds five buckets,
                    and every position sits in exactly one of them -- none in two,
                    and none left over.

  FWD-2  Volatility and hedge products are shown apart from equities
         DONE WHEN  EXERCISED -- a portfolio that used to fold volatility or hedge
                    into its equity total now shows it separately
         ACCEPT     A position that hedges or bets on volatility no longer inflates
                    the equity figure -- it appears under its own heading, and gold
                    likewise stands apart from the rest.

  FWD-3  The five classes always appear in the same order
         DONE WHEN  APPLIED -- every place that lists the classes renders them in
                    the one agreed order
         ACCEPT     Wherever the breakdown is shown, the classes read in the same
                    fixed order every time -- never re-sorted by size or by name.

  FWD-4  Each class has one color, the same everywhere
         DONE WHEN  APPLIED -- the agreed color for each class is used on every place
                    that shows the classes
         ACCEPT     The same class is the same color everywhere it appears, and no
                    place shows a class in a color another uses for something else.

  FWD-5  The classification is defined in one place and flows everywhere
         DONE WHEN  EXERCISED -- someone changed where a class boundary sits in the
                    single source, and every place reflected it without being edited
                    itself
         ACCEPT     A person changes an asset-class definition once, in one place,
                    and everywhere that shows asset classes updates on its own --
                    nobody edits each place by hand.

  FWD-6  The places that show asset classes agree with each other
         DONE WHEN  EXERCISED -- the Positioning view and the combined Philosophy /
                    Capital-Market-Assumptions view have each been read and both show
                    the same classes, in the same order and colors
         ACCEPT     An analyst opens both views and cannot find a disagreement
                    between them about what the asset classes are, what order they
                    come in, or what color each one is.
```

---

## 1. Purpose -- what DONE means

ONE canonical asset-class taxonomy -- **five classes**, in a fixed order, each with one color --
implemented **from a single source** and shown **consistently on every surface that displays asset
classes**. DONE is both halves: the classification is correct and single-sourced (a holding lands in
exactly one class, and a change to a class boundary flows everywhere from one place), AND the surfaces
that render it agree with each other.

## 2. Territory -- what this owns, and what it only relies on

**OWNS:** the definition of the five classes (their identity, order, and colors); the single
classification that assigns every holding to exactly one class; and the requirement that every surface
showing asset classes reads that one classification rather than re-deriving it.

**RELIES ON (does not own):** the portfolios and holdings themselves; the surfaces' broader layout and
content beyond the asset-class breakdown; and the ETF/holdings data feeding the classifier. This project
changes WHERE a holding is classified and HOW that flows, not what the holdings are.

## 3. The five classes -- the ratified taxonomy (BINDS the decomposition)

| # | class | color | holds |
|---|---|---|---|
| 1 | Fixed Income / Cash | green | fixed income and cash |
| 2 | Equity | blue | equities only -- **volatility and hedge REMOVED to Structured** |
| 3 | Structured | pink | options, VIX futures, volatility overlays, VXX and the like |
| 4 | Commodities | gold | physical (gold, nickel, silver), crypto, and commodity indices (e.g. GSCI) |
| 5 | Alternatives | orange | real assets (not commodities), private equity, private credit, real estate |

## 4. Constraints that BIND the decomposition

- **C-FIVE-CLASSES** -- the classes are exactly the five in s.3, in that canonical order, with those
  colors. This is Andrew + Young's ruling (the brief), not a decomposition choice.
- **C-ONE-SOURCE** -- the classification originates in ONE place and flows to every surface; no surface
  re-implements it. **The expected home is the shared ETF classification module**
  (`infra/aws/lambda/v2_portal/_shared/etf_classification.py` and `etf_classifications_dynamodb.py`,
  the module the positioning and CMA lambdas already share -- "ETFClassifier", Andrew 2026-09-11).
  FWD-5's FIRST L5 investigation confirms that is the source, or finds where it truly lives -- it is
  NOT hard-pre-judged here.
- **C-VOL-HEDGE-STRUCTURED** -- volatility and hedge products classify to **Structured**, not Equity,
  and physical/crypto/commodity-index positions to **Commodities**, not Equity. This is the Cottonwood
  catalyst and it is a CLASSIFICATION change, verified on a surface but driven by the classifier.
- **C-TWO-SURFACES** -- there are **TWO** surfaces that show asset classes: **Positioning**, and the
  **combined Philosophy / Capital-Market-Assumptions** view. (Andrew-direct 2026-09-11: Philosophy and
  CMA are the same page now.) Both must agree; FWD-6 is graded over the two.
- **C-MEMBERSHIP-AT-L5** -- the exact membership RULES (which instrument is Structured vs Commodities
  vs Alternatives at the edges) are the classifier's substance and are decided in the cells at L5, not
  pre-judged here. FWD-1's bar is only that every holding lands in exactly one class.

## 5. Rulings that BIND (Andrew-direct)

- **2026-09-11, Andrew-direct, VERBATIM:** *"Confirmed, just note that Philosophy/CMA are the same page
  now. Also this should likely be heavily involved with ETFClassifier."* -- confirming the six DONE WHEN
  bars (his reserved L2 step), and adding the two refinements now carried as C-TWO-SURFACES and
  C-ONE-SOURCE.
- **2026-09-01, Andrew-direct (register):** the taxonomy goes in D4, owned by the site-z fabric;
  `1.0.0_SA_CTO~Z` takes the transcript and authors this PRD.

## 6. Out of scope

- The membership rules at the class edges (C-MEMBERSHIP-AT-L5 -- L5/the cells).
- Any surface's content beyond the asset-class breakdown itself.
- The TAX SMA Teams thread (a second source Andrew named; deferred on "the transcript is fine for now"
  -- MAY refine scope at L4 if read, but does not block this PRD).

## 7. SURFACE MANIFEST (step 4 -> step 5) -- one row per ENGINE

Coverage by SUBTRACTION from the printed denominator (rule 24(i)): **endpoint_outcomes = 6
(FWD-1..FWD-6); covered = 6; uncovered = declared MINUS covered = 0.**

| row | ENGINE | what it is | outcomes it carries |
|---|---|---|---|
| **S1** | **ETFClassifier** -- the one classification source | the single function/module that assigns every holding to exactly one of the five classes, and where the Cottonwood reassignment (vol/hedge -> Structured, gold/commodities -> Commodities) lives | **FWD-1, FWD-2, FWD-5** |
| **S2** | **Class registry** -- order + color | the single definition of the five classes' canonical order and their colors, read by every surface | **FWD-3, FWD-4** |
| **S3** | **The two surfaces** -- Positioning; Philosophy/CMA | the views that render the breakdown, reading class + order + color from S1 and S2 rather than re-deriving them | **FWD-6** |

**MECE check:** FWD-1 -> S1 · FWD-2 -> S1 · FWD-3 -> S2 · FWD-4 -> S2 · FWD-5 -> S1 · FWD-6 -> S3.
**6 of 6 outcomes carried by exactly one row, 0 uncovered.** (The surfaces DISPLAY S1/S2's results, but
each outcome is owned by the layer that DETERMINES the result: classification outcomes at S1, the
order/color definition at S2, and cross-surface agreement -- the only outcome the surfaces themselves
own -- at S3.)

## 8. Sequencing input for `2.0.0_SA_COO` (not a dispatch)

A natural order for the L5 decomposition, offered not imposed:
1. **S1 first, and its first cell is the FWD-5 investigation** -- confirm the shared classification module
   is the one source (or find where it truly lives) BEFORE building on it. Everything else reads from it.
2. **S1's classification correctness** (FWD-1, FWD-2) -- every holding in exactly one class; vol/hedge
   and gold out of Equity, exercised on real portfolios.
3. **S2** (FWD-3, FWD-4) -- order and color from the single registry.
4. **S3** (FWD-6) -- the two surfaces read S1+S2 and agree, read end-to-end.

Nothing here is a task order; L5 is the COO's, and the membership rules (C-MEMBERSHIP-AT-L5) are the
cells' substance to establish.
