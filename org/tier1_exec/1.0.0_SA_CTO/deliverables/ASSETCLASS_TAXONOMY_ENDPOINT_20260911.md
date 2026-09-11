# ASSETCLASS_TAXONOMY -- ENDPOINT (step 2, `/endpoint --forward`)

**archetype:** SCRIBE (spec) · **author** `1.0.0_SA_CTO~Z` (L2) · **2026-09-11 ~01:4xZ**

| | |
|---|---|
| **Source brief** | `Asset class nomenclature_6911.txt` -- a Whisper transcript in `1.0.0_SA_CTO~Z`'s downloads (3,213 chars). ⛔ **NOT IN THE REPO.** Andrew-direct this session: *"if its just a transcript that is fine we can use that for now to get it onto the /canonical-flow path"* |
| **Directive** | D4 (renamed "Positioning" 2026-09-10; the transcript names the next phase "Asset Class Nomenclature") |
| **Project** | `ASSETCLASS_TAXONOMY` (macro `ASSETCLASS`, site-z) |
| **Status** | ⛔ **NOT YET LANDED IN A PRD.** The project is `REGISTERED` with no PRD; this block is the endpoint the PRD's `ENDPOINT` section will carry. |

> **THIS IS A CARRIER, NOT THE HOME.** The block in section 2 goes into the PRD's `ENDPOINT` section
> verbatim once that PRD is authored. It is emitted here because the endpoint must exist before the
> PRD, and the project has none yet.

---

## 1. WHAT THE TRANSCRIPT ESTABLISHES

Cottonwood asked to break **volatility products and gold** out as their own line items -- to pull
hedge/volatility out of the equity bucket. Andrew and Young generalised that into **five asset
classes**, replacing the old scheme, applied consistently across every page that shows asset classes.

**The five classes, in canonical order, with their colors** (these are L4 constraints, recorded here
so the endpoint is legible; the ACCEPT lines below carry none of this jargon):

| # | class | color | what it holds (transcript) |
|---|---|---|---|
| 1 | Fixed Income / Cash | green | -- |
| 2 | Equity | blue | (volatility/hedge REMOVED to Structured) |
| 3 | Structured | pink | options, VIX futures, overlays, VXX -- "all this kind of stuff" |
| 4 | Commodities | gold | physical (gold, nickel, silver), crypto, commodity indices (e.g. GSCI) |
| 5 | Alternatives | orange | remaining alts -- real assets (not commodities), private equity, private credit, real estate |

It spans **three surfaces**: the positioning page, the philosophy page, and the capital market
assumptions -- and Andrew stressed a **generalisable, consolidated** approach: the classification
should originate in one central place (the ETF classifier function, or wherever it truly lives),
not be re-implemented per page.

---

## 2. THE BLOCK -- paste into the PRD verbatim

```
ENDPOINT (step 2, /endpoint --forward)

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
         DONE WHEN  APPLIED -- the agreed color for each class is used on every page
                    that shows the classes
         ACCEPT     The same class is the same color on every page, and no page
                    shows a class in a color another page uses for something else.

  FWD-5  The classification is defined in one place and flows everywhere
         DONE WHEN  EXERCISED -- someone changed where a class boundary sits in the
                    single source, and every page reflected it without being edited
                    itself
         ACCEPT     A person changes an asset-class definition once, in one place,
                    and every page that shows asset classes updates on its own --
                    nobody edits each page by hand.

  FWD-6  The pages that show asset classes all agree with each other
         DONE WHEN  EXERCISED -- the positioning page, the philosophy page and the
                    capital-market-assumptions page have each been read and all
                    show the same classes, in the same order and colors
         ACCEPT     An analyst opens all three pages and cannot find a disagreement
                    between them about what the asset classes are, what order they
                    come in, or what color each one is.
```

---

## 3. WHAT L2 READ, AND WHAT IT DELIBERATELY DID NOT

⚠ **`FWD-1`, `FWD-2`, `FWD-5`, `FWD-6` carry EXERCISED bars; `FWD-3`, `FWD-4` carry APPLIED.** Order
and color are configuration a reader can verify without anyone using the page; sorting, separation,
central propagation and cross-page agreement are only real when exercised.

⛔ **THE FIVE-CLASS MEMBERSHIP RULES ARE L4/L5, NOT OUTCOMES.** *Which* instruments count as
Structured vs Commodities vs Alternatives (VXX here, GSCI there, crypto under Commodities) is the
substance of the classifier and belongs in the PRD's constraints and the decomposition's cells --
not in `FWD-1`, whose bar is only that every holding lands in exactly one class.

⛔ **"WHERE THE NOMENCLATURE ORIGINATES" IS A FIRST INVESTIGATION, NOT AN OUTCOME.** The transcript
asks whether the source is the ETF classifier function or elsewhere. That is `FWD-5`'s first cell to
establish; the outcome is "one source that flows," not "it is the ETF classifier" -- naming the
mechanism now would pre-judge what L4/L5 must measure.

```
GROUNDED ON:  Asset class nomenclature_6911.txt (the downloads transcript), read IN FULL
              org/projects/ASSETCLASS_TAXONOMY.json (register row: D4, macro ASSETCLASS, REGISTERED,
                prds: [], PRD named as 1.0.0_SA_CTO~Z's first act by Andrew 2026-09-01)

NOT READ:     the TAX SMA Teams thread -- Andrew named it as a second source 2026-09-01 but said this
              session the transcript is enough "for now"; deferred, and it MAY refine scope at L4.
                (The gateway IS reachable from site Z -- whoami confirmed -- so no ferry is needed
                when it is time to read it.)
              the ETF classifier function / any page code -- that is L4/L5 investigation, and reading
                it now would let the implementation shape the endpoint instead of the reverse.

DISCLOSED:    the transcript is NOT in the repo, so a future PRD's brief_ref cannot cite it by
              path@vintage. Before the PRD lands, either the transcript is committed into the
              project's brief/ folder, or an ANDREW_DIRECT record carrying its substance is, so the
              PRD has an in-repo, vintaged source to cite. Named now so it is not discovered at L4.
```

**NEXT:** this endpoint goes to Andrew for his `DONE WHEN` confirmation (his reserved step). On his
word, `1.0.0_SA_CTO~Z` authors the L4 PRD (his named first act), and `2.0.0_SA_COO~Z` can then be
seated at L5. **Push state:** LOCAL at write time. `0.0.0_AB_MSTR~Z` pushes.
