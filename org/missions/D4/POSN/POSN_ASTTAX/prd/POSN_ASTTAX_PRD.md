# POSN_ASTTAX -- PRD (step 4)

```json
{
 "project": "POSN_ASTTAX",
 "directive": "D4",
 "fabric": "site-z",
 "prd_version": "v0.9",
 "step": 4,
 "brief_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_ASSET_CLASS_TAXONOMY_BRIEF.md@03f1d00ec4",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "status": "DRAFT"
}
```

## s.0 ADDENDUM v0.9 -- THE SATELLITES MODE, COMPLETE: EACH HOLDING'S MEASURES (FWD-7), ONLY THE CLASSES A VIEW HOLDS, THE SUMMARY'S OWN DATE

**Author** `1.0.0_SA_CTO~Z` (L4, as the L10 answer to `3.0.0_SA_CVO~Z`'s round-5 slug `surprise-channel/remediations/REMEDIATION_v5.Z.md` @`1edf35dbc3`; L9 `ADJUDICATION_v7.Z.md`), 2026-09-15. **Carries** three
Andrew-direct words at the `1.0.0_SA_CTO~Z` terminal, VERBATIM:
- ~00:4xZ: *"There is no need to display the different legend categories if they do not appear in the view"* (record
  `ANDREW_DIRECT_20260915_004xZ_POSITIONING_LEGEND_ONLY_PRESENT_CLASSES_AND_SATELLITES_VIEW_DEFECTS.md` @`85621749e2`)
- ~02:1xZ: *"if none of the models/ETFs/satellites have a given asset class (e.g. Alternatives) then no Alternatives row should be
  shown ... the Satellites section is still broken; not displaying data [Image #3] showing all the floats in this case. and no
  characteristics or performance in the "Holdings Breakdown" panel."* (record `ANDREW_DIRECT_20260915_021xZ_...` @`65410eedaf`)
- ~02:3xZ: *"i want to do an ad hoc pul on this and just fix it completely, we're not waiting for the next day to deal with ths."*
  (record `ANDREW_DIRECT_20260915_023xZ_ADHOC_FIX_SATELLITES_TONIGHT_NO_WAITING.md` @`0553548fe2`)

**WHAT THIS ADDENDUM CHANGES:** `ENDPOINT` gains `FWD-7` (appended at the next unused number; nothing renumbered) and the header's
`endpoint_outcomes` gains it, so `3.0.0_SA_CVO~Z` re-signs the ratified-text half. Four constraints are added below, so
`4.0.0_SA_CRO~Z` re-signs the brief half. Everything in v0.6 / v0.7 / v0.8 stands.

**THE NEW OUTCOME (appended to ENDPOINT):**
```
  FWD-7  The Satellites mode shows each holding's characteristics and performance
         DONE WHEN  EXERCISED -- the Positioning page's Satellites mode has been read
                    and every satellite's Holdings Breakdown rows carry the same
                    characteristic and performance columns a Models row carries,
                    from the served satellites data, with a value wherever a source
                    prices the ticker
         ACCEPT     An analyst opens a satellite's Holdings Breakdown and sees each
                    fund's fee, size, yield, beta and returns the way a model shows
                    them -- blank only where nothing prices that holding, never a
                    blank column.
```

**NEW CONSTRAINTS:**

- **C-HOLDING-MEASURES** (FWD-7; disarm route for `Z-S132`). B4's `characteristics.json` ALSO publishes, once per artifact, a
  `tickers` block keyed by ticker for every ticker any satellite holds: `fee`, `aum`, `active`, `yield`, `duration`, `credit`,
  `beta`, `returns` (the input's windows) and `source`. Precedence is B4's existing per-ticker rule, unchanged: Yang's
  `current_holdings` row, else the Bloomberg partition, else none (all NULL). Every existing field of the artifact is unchanged
  for the same inputs. The satellite adapter attaches each row's served values to that row -- no arithmetic, no borrowing from
  another artifact. **Measured basis (2026-09-15 ~02:5xZ):** 25 distinct tickers across the nine satellites; 23 priced by
  Yang (all seven panel fields and returns ride its rows), GLD by Bloomberg only, CASH by neither. On the 5 tickers both sources
  carry (DIVZ, IDVZ, PFDE, PFOE, VXX) Yang's `aum` EQUALS Bloomberg `FUND_TOTAL_ASSETS` and `fee` EQUALS `FUND_EXPENSE_RATIO`,
  5 of 5, so the Bloomberg fallback maps `aum <- FUND_TOTAL_ASSETS` in the same unit. `active` and `credit` have no Bloomberg
  column and publish NULL for a Bloomberg-sourced ticker. **DISCLOSED GAP:** B4's `bbg_return_columns` is `{}` -- the ETF pull
  carries no return field -- so GLD's performance cells publish NULL; closing that is a vendor-pull change and Andrew's word.
- **C-PRESENT-CLASSES** (FWD-3, FWD-6; disarm route for `Z-S118`, `Z-S131`). The Positioning Summary derives ONE presence set per
  render -- the classes with a non-zero value in any column the current view draws -- and the legend, the Asset Class rows and
  the section count list exactly that set, in `ASSET_CLASSES` order and colours. The zero-row design comment goes with the
  behaviour. Colours stay keyed by class name, so hiding a class shifts no other colour (compatible with the laptop name-keyed
  colour rule relayed in msg 22957). **FWD-6 READS THROUGH THIS:** its "all show the same five classes" is graded as "no mode
  shows a class outside the five, and a class shown in two modes has the same order and colour in both"; a class no book in a
  view holds is not shown in that view, by Andrew's word ~02:1xZ. The ratified text is not edited; this is the grading rule.
- **C-SUMMARY-COPY** (FWD-6; disarm route for `Z-S115`, `Z-S117`, `Z-S119`). The third percent label rounds like its two siblings
  (`PositioningSummary.tsx:1011`, `Z-S117`); the Satellites mode's footer names `holdings.json`'s `as_of` and Black Diamond as the
  source, Models and ETFs unchanged (`Z-S119`); the Satellites subtitle and unresolved notice stop describing the removed blend
  (`Z-S115`).
- **C-B4-SCHEDULE** (FWD-7 on schedule; disarm route for `Z-S120` / `Z-S130`). B4's rule fires on its own clock AFTER the
  07:00 America/New_York Bloomberg pull in both DST states -- `cron(30 12 * * ? *)` UTC (08:30 EDT / 07:30 EST) -- never
  success-of-upstream. Andrew-direct 2026-09-10's no-wait rule applies: the deploy is followed by a driven run with an explicit
  `bbg_as_of`, covered by its own never-widen halves; the scheduled fire is the organic leg.

**THE CELLS THIS IMPLIES (guidance for `2.0.0_SA_COO~Z`'s decomposition, not a dispatch):**
- **B6** -- `data/assets/scripts/gold/build_satellites_characteristics.py` (+ its tests) and the rule in its Terraform: the
  `tickers` block and the schedule. Deploy through Terraform, then a driven run. Bar: every satellite ticker appears once with its
  `source`; the prior fields parse-identical on the same inputs; the rule reads `cron(30 12 * * ? *)`.
- **F4** -- `satelliteAdapter.ts` (+ the served-characteristics type in `satelliteSet.ts` / `satelliteRegistry.ts`): attach the
  per-ticker values. Bar: in every displayed satellite, every Holdings Breakdown row's Characteristics and Performance cells equal
  that ticker's served `tickers` values, a NULL rendering blank; CASH blank throughout, GLD's returns blank (the disclosed gap).
  Depends on B6 DEPLOYED.
- **F5** -- `PositioningSummary.tsx` and `Positioning.tsx`: C-PRESENT-CLASSES and C-SUMMARY-COPY. Bar: Models lists 3 classes
  (Fixed Income, Equity, Structured) in the legend and the Asset Class rows; Satellites after the relabel lists 4 (Fixed Income,
  Equity, Structured, Commodities); no raw float; the Satellites footer reads `2026-09-14` and Black Diamond.
F4 and F5 are disjoint files and may run in parallel; B6 precedes F4's bar. Portal commits land on the round's own drain ref;
no promote, push or gitlink move (the freeze).

## s.0 ADDENDUM v0.8 -- JEPI IS THE THIRTEENTH MEMBER (Structured / Options Income); STRUCTURED IS THE PINK FAMILY

**Author** `1.0.0_SA_CTO~Z` (L4), 2026-09-14. **Carries** three Andrew-direct words at the `1.0.0_SA_CTO~Z` terminal, VERBATIM:
- ~19:5xZ: *"Yeah "Structured" is going to be a pink base, as all volatility/options/overlay etc assets will be grouped into
  there, regardless if its a Fixed Income or an Equity Hedge or etc."* (record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_195xZ_STRUCTURED_IS_PINK_ALL_VOL_OPTIONS_OVERLAY.md` @`edbee96c07`)
- ~20:0xZ: *"Also JEPI I would put in Structured, yes."* (record `ANDREW_DIRECT_20260914_200xZ_JEPI_TO_STRUCTURED_AND_FRONTEND_VIEW_ON_5173.md`
  @`114a697fca`)
- ~20:2xZ: *"b, Options Income"* (record `ANDREW_DIRECT_20260914_202xZ_JEPI_SUB_ASSET_OPTIONS_INCOME.md`)

**SUPERSEDES, in s.0 ADDENDUM v0.7, exactly these three constraints; everything else in v0.7 stands:**

- **C-RETAG-SET is THIRTEEN:** Commodities -- DBC, GLD, GSG, IAU, SLV, USO, PDBC; Structured -- VXX, VIXY, UVXY, QBER,
  **JEPI**; Alternatives -- VNQ. BIPC stays Equity. Both stores, LAST, and `C-RETAG-SAFETY`'s bar binds unchanged.
- **C-SUB-ASSET:** `Metals` = GLD, IAU, SLV; `Hedge` = VXX, VIXY, UVXY, QBER; **`Options Income` = JEPI**; `Real Estate` = VNQ;
  DBC, GSG, USO, PDBC keep their current sub-asset. The encoding rule is unchanged: sub-asset values sit in
  `sub_asset_class`, the legacy top-level `hedge` dissolves, and every write names its level.
- **C-COLOURS:** Structured is the PINK family. Every Structured sub-asset (`Hedge`, `Options Income`, and the existing
  `Volatility` key) renders on a pink token DISTINCT from the class base `pink500`, minted where the palette lacks one. The
  portal's existing `SUB_ASSET_COLORS` keys `Hedge` (green900, Fixed Income block) and `Volatility` (blue900, Equity block)
  RE-BIND to that family. Commodities stays the new yellow; amber stays Cash.

**Basis for membership, measured so it is not re-derived:** `etf-classifications` scanned whole (285 rows, one page, 31
distinct `sub_asset_class`). The only volatility-shaped sub-asset is `Volatility`, on exactly the four `Hedge` members. JEPI is
the one options-overlay name. `Structured Credit` (JAAA, LONZ) is Fixed Income credit and stays there despite the shared word.
JEPI is held by no Cottonwood satellite component and no Yang served book, so its retag moves no served Positioning figure today.

**WHAT THIS ADDENDUM CHANGES:** brief half only -- `4.0.0_SA_CRO~Z` re-signs. The `ENDPOINT` section is untouched, so
`3.0.0_SA_CVO~Z`'s ratified-text signature stands. It cuts no order: `TO-V8-1` (member table) and `TO-V5-1` (the pink
sub-asset keys) are amended by their issuer before hand-off.

## s.0 ADDENDUM v0.7 -- ANDREW'S CLOSE-OUT RULINGS (2026-09-14): POSITIONING PAGE ONLY, SATELLITES FROM BLACK DIAMOND

**Author** `1.0.0_SA_CTO~Z` (L4), 2026-09-14. **Carries** Andrew's words of ~16:5xZ (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_165xZ_SITEZ_POSN_ASTTAX_ONLY_BREAKDOWN_BEFORE_WORKERS.md`
@`f529179076`), ~16:34Z, ~17:2xZ and ~17:3xZ (records by `4.0.0_SA_CRO~Z` under
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260914_1634Z_*`, `_172xZ_*`, `_173xZ_*`), and the aligned
breakdown `org/tier1_exec/1.0.0_SA_CTO/deliverables/POSN_ASTTAX_CLOSEOUT_BREAKDOWN_20260914_Z.md` (v0.5), which is the
CELL-LEVEL authority for round 5. The measured premise is `4.0.0_SA_CRO~Z` brief
`org/tier1_exec/4.0.0_SA_CRO~Z/briefs/POSN_ASTTAX_COMPLETION_BRIEF_20260914_Z.md` and row `POSN_ASTTAX-Z-S65`.

**HIS WORDS, VERBATIM:**
- ~17:2xZ: *"Call 1, they should be summed because the goal is not to see what's yangs models versus what's external
  residuual in the satellite; it is to see total GLD listed as Commodity Asset, Metals Sub-Asset, and to see Total VXX
  (or whatever hedge securities) as Structured Asset, Hedge Sub-Asset. Call 2 Yes. Call 3, mint some yellow color, yes.
  Call 4 Yes. Call 5 Yes. Call 6, definitely B, models do not get updated because they are not changing, Satellites
  simply need to have an additional lambda to do weighted characteristics aggregates ."*
- ~17:3xZ: *"All recs approved. Keep in mind that attribution, for now at least, is staying to just Equities and Fixed
  Income on asset classes, because those are the only ones Yang uses, and we stick to his layout. Eventually that may
  change, but need to keep in mind that the work we're doing here is very much contained to "Positioning", we do not
  touch "Attribution""*

**CONSTRAINTS THIS ADDENDUM ADDS -- they BIND round 5 and SUPERSEDE the named s.4 text where they differ:**

- **C-POSITIONING-ONLY** (supersedes `C-TWO-SURFACES`). The surfaces are the Positioning page only -- 14 files at portal
  pin `e85f6eb84f` (`src/pages/Positioning/`) plus the shared colour registry `src/lib/chartColors.ts` it imports, in
  all three modes (Models, ETFs, Satellites). **The Attribution page is NOT touched** (two classes, Yang's layout);
  Philosophy/CMA is not a focus (Yang's sheet, later); AdvisorIntelligence is out. ACCEPTED CONSEQUENCE, not a defect:
  after the retag, a retagged ticker that Yang's models hold (VXX) drops out of Attribution's per-class groups while
  its weight stays in Attribution's totals. This settles `Z-W15-S2` (eleven readers, four families): the domain is
  declared as the Positioning page, and the other families are out of scope by Andrew's word, not by omission.
- **C-SATELLITE-SOURCE** (new; disarm route for `Z-S65`; supersedes the "touches NO holding, weight or satellite
  placement" clause of `C-SATELLITE-DATA` for the Satellites mode). The Satellites mode shows, per satellite, ONE total
  weight per ticker from Black Diamond's rebalancer holdings, summed across the satellite's sleeves; **Yang's copy of a
  model is never added** (LT VXX: BD 1.87, not 1.87 + 1.50). Each ticker carries `asset_class` and `sub_asset_class`
  from the served ETFClassifier table. Weighted characteristics (fee, yield, duration, beta, returns) are aggregated
  server-side by **an additional lambda**; per-ticker inputs from Yang's `current_holdings` where a Yang book holds the
  ticker, from the Bloomberg ETF pull where it does not, NULL otherwise with the null-weight share disclosed. **The
  Models mode and Yang's model data are unchanged.**
- **C-SUB-ASSET** (new). Sub-asset labels for the retag set: `Metals` = GLD, IAU, SLV; `Hedge` = VXX, VIXY, UVXY, QBER;
  `Real Estate` = VNQ; DBC, GSG, USO, PDBC keep their current sub-asset. **ENCODING (L4):** `Hedge` is a
  `sub_asset_class` value under `Structured`; the legacy TOP-level `asset_class` value `hedge` dissolves. The two never
  share a field, and every retag write names its level.
- **C-RETAG-SET** (settles `C-MEMBERSHIP-AT-L5` for this project, on Andrew's approval of the U4 derivation). The retag
  set is TWELVE: Commodities -- DBC, GLD, GSG, IAU, SLV, USO, PDBC; Structured -- VXX, VIXY, UVXY, QBER; Alternatives --
  VNQ. BIPC stays Equity. The retag lands in BOTH stores (DynamoDB `etf-classifications` and `ETF_CLASSIFICATIONS`) and
  runs LAST, after the generator deploy, the seeder guard, the satellite artifacts and the Positioning frontend are in
  place (`C-RETAG-SAFETY`'s bar still binds).
- **C-COLOURS** (refines s.3's colour column; no s.3 byte changes). Commodities' gold is rendered by a NEW yellow token,
  never amber (amber is Cash); Structured is pink; sub-asset colours exist for `Metals` and `Hedge`.
- **C-BENCHMARK** (new). The three new classes' benchmark rows are an explicit zero labelled "no benchmark", in both
  `yang-generate-positioning` and `yang-generate-allocation-summary`, under ONE never-widen sign-off naming both
  functions and both served artifacts (this widens the 2026-09-13 deploy approval to the second function, by Andrew's
  "Call 5 Yes" / "All recs approved").
- **C-CUTS** (new). Not in this project: reconciling the dormant `is_hedge()` / `HEDGE_TICKERS` helper -- row
  `Z-W1-S1` / `Z-C-S1` is dispositioned CARRIED-OUT-OF-SCOPE (no live caller; the helper keys on `asset_class`, which
  `C-SUB-ASSET` keeps apart from the `Hedge` sub-asset) -- and reconciling the second store `bd-securities` (`Z-W17-S3`
  settled the same way: the one place stays the served `etf-classifications` table; only the seeder that writes both
  gets the preserve-don't-clobber guard).
- **C-DONE** (new). The project is DONE when the backend is deployed and the Positioning frontend is built and committed
  behind the freeze (Andrew 2026-09-14 05:31Z); the portal promote is Andrew's separate word and is not a bar here.

**SURFACE MANIFEST, as amended:** S1 now includes the satellite holdings producer and the characteristics lambda that
apply the classification to satellites (they carry FWD-1 / FWD-2 on the Satellites mode; no new outcome); S3 is the
Positioning page's three modes. MECE unchanged: 6 outcomes, each carried by exactly one row -- and, per the v0.6
qualifier, that is ASSIGNMENT; round 5's eight cells are what serve them.

**WHAT THIS ADDENDUM CHANGES IN RATIFIED TEXT:** `ENDPOINT` FWD-6 only (narrowed to the Positioning page), so
`3.0.0_SA_CVO~Z`'s half re-signs; this addendum re-opens `4.0.0_SA_CRO~Z`'s brief half. **WHAT IT DOES NOT DO:** it
cuts no order, grades no outcome REALIZED, and authorizes no promote.

## s.0 ADDENDUM v0.6 -- THE ROUND-3 L10 ANSWER

**Author** `1.0.0_SA_CTO~Z`, 2026-09-13, answering `3.0.0_SA_CVO~Z`'s round-3 slug
`surprise-channel/remediations/REMEDIATION_v3.md` @`c89c0e45a2`. Full reasoning and denominators:
`ledger/ROUND_ANALYSIS.round3.md`.

**FOUR CHANGES, AND EVERY ONE IS A DEFECT IN TEXT THIS SEAT AUTHORED AT L4.**

1. ⛔ **TWO DECLARED OUTCOMES HAVE BEEN SERVED BY ZERO CUT ORDERS ACROSS THREE ROUNDS.** Measured
   over the 15 cut orders: declared 6, covered 4, **UNCOVERED = { `FWD-4`, `FWD-6` }**, with a
   run-time-generated synthetic control verified absent from the corpus before use. `FWD-4` is
   *"each class has one color, the same everywhere"*; `FWD-6` is *"the places that show asset classes
   agree with each other"* -- **which is the ASTTAX frontend outcome Andrew named on 2026-09-13
   03:21:46Z.** Not deprioritised and not blocked: never issued. **Round 4 must cover both.**
2. **The MECE check's "0 uncovered" is qualified** where it appears -- it is about ASSIGNMENT to a
   surface row, never about issuance, and reading it as coverage is what hid item 1 for three rounds.
3. **s.4's live-mechanism sentence is corrected** -- the weight is lost at the served view and the
   delta/spread rows, NOT in the allocation dict, which serves 2.5. The line states what it used to
   say. Its consumer is `AT3-s-5`, the bar that gates the retag.
4. **The surface list discloses a third, non-owned reader** of class values, with its measured
   zero-candidate state and the condition that ends it.

**WHAT THIS ADDENDUM DOES NOT DO:** it does not change the endpoint -- the outcome set is still
FWD-1..FWD-6 and no bar is weakened, added or renumbered. It does not authorize the retag (NO-GO), the
positioning deploy (approved 2026-09-13 04:08:22Z LD-0562 **conditional on a two-seat never-widen
sign-off that has not landed**), or any portal act (**frozen**). It grades no outcome REALIZED.

⚠ **THIS BUMP RE-OPENS THE BRIEF HALF ONLY**, and LIMB 6 refuses a newly-added task order against a
half not SIGNED at current bytes -- so that ONE re-sign sits in front of round 4's FWD-4/FWD-6 cells.
> ⛔ **CORRECTED 05:4xZ. THIS LINE SHIPPED SAYING "BOTH L4-R HALVES" IN THE SAME COMMIT AS THE
> VERSION-LINE CORRECTION THAT CALLS THAT CLAIM FALSE** -- the two statements sat four lines apart and
> contradicted each other. Found by `4.0.0_SA_CRO~Z` on review. **The gate settles it:** only the
> brief half went STALE; `3.0.0_SA_CVO~Z`'s ratified-text half was never touched and owes nothing.
> The cost of the contradiction was precise and worth naming -- a reader of this section chases a
> signature that is not outstanding.
> ⭐ **AND IT IS THE SHARPEST FORM OF A SHAPE THIS DOCUMENT HAS NOW PRODUCED TWICE:** the v0.5
> changelog went stale by omission across five amendments; this one shipped the correction and the
> stale claim **in one diff.** Correcting a rule is not finished until every place that RESTATES it
> has been re-read -- a fix scoped to where the error was noticed leaves its own restatements
> standing.

**Version:** v0.5, 2026-09-11 -- v0.1 first PRD; v0.2 folded in Andrew's Cottonwood satellite components (s.4 C-SATELLITE-DATA), on his direct "read the satellite file and fold it in as its necessary data for POSN_ASTTAX"; **v0.3 disambiguates C-VOL-HEDGE-STRUCTURED's "hedge products" from the legacy served value `asset_class=hedge`** -- a latent defect where the constraint, read against the live data, said the whole `hedge` bucket goes to Structured (found by 2.0.0_SA_COO~Z + 3.0.0_SA_CVO~Z); **v0.4 folds in Andrew's ETFClassifier PURPOSE ruling as C-CLASSIFIER-PURPOSE (s.4)** -- the registry is a curated tagging list, so the served TABLE is the one place, the dict a retired seed input, and equity-as-class must be distinguishable from equity-as-unknown-default (carried via 3.0.0_SA_CVO~Z C-S3 @`4275402ec2`); **v0.5 folds in the `0.4.0_DT_ClientPlatform` GLD/VXX positioning brief as C-RETAG-SAFETY (s.4)** -- the retag of the commodity/hedge tickers is a production landmine (a fixed-key allocation dict KeyErrors in the DEPLOYED generator, establishing an UNSAFE GENERATION PRECONDITION -- page-blanking is the brief's PREDICTED consequence and is NOT measured; see s.4) until the positioning generator is hardened; Andrew-direct 2026-09-11 ~07:2xZ to fold it into POSN_ASTTAX. **v0.6 is the round-3 L10 ADDENDUM (`ledger/ROUND_ANALYSIS.round3.md`) -- see s.0 ADDENDUM below.** ⛔ **THIS LINE USED TO READ "Each bump re-opens the two L4-R sign-offs" AND THAT IS FALSE -- CORRECTED AT v0.6.** A bump re-opens ONLY the half whose SECTION BYTES changed. `prd_signoff_lib.RATIFIED_SECTIONS` is `("ENDPOINT", "CONTRACTS")` matched on a heading's FIRST WORD, so in THIS document exactly one section -- `ENDPOINT` -- is ratified-text and everything else, s.4 included, is the brief half. The library's own self-test asserts it: *"an ENDPOINT edit re-opens the CVO half only"*. Measured at v0.6: these edits touched no ENDPOINT byte, so `3.0.0_SA_CVO~Z`'s half stayed SIGNED/current and only `4.0.0_SA_CRO~Z`'s went STALE. ⚠ **The old wording stated a rule STRONGER than the tool behaves, and this seat quoted it as authority in its own round-3 analysis before the gate contradicted it** -- the same shape CLAUDE.md Rule 27 records against LIMB 6. **Author** `1.0.0_SA_CTO~Z` (L4). **Brief:** the nomenclature
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

  FWD-6  The places on the Positioning page that show asset classes agree
         with each other
         DONE WHEN  EXERCISED -- the Positioning page's Models, ETFs and Satellites
                    modes have each been read and all show the same five classes,
                    in the same order and colors
         ACCEPT     An analyst switches between the three Positioning modes and
                    cannot find a disagreement about what the asset classes are,
                    what order they come in, or what color each one is.

  FWD-7  The Satellites mode shows each holding's characteristics and performance
         DONE WHEN  EXERCISED -- the Positioning page's Satellites mode has been read
                    and every satellite's Holdings Breakdown rows carry the same
                    characteristic and performance columns a Models row carries,
                    from the served satellites data, with a value wherever a source
                    prices the ticker
         ACCEPT     An analyst opens a satellite's Holdings Breakdown and sees each
                    fund's fee, size, yield, beta and returns the way a model shows
                    them -- blank only where nothing prices that holding, never a
                    blank column.
         (appended v0.9 at L10 on Andrew-direct ~02:1xZ / ~02:3xZ, records @65410eedaf / @0553548fe2)
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
  NOT hard-pre-judged here. **SETTLED at v0.4 by C-CLASSIFIER-PURPOSE: the ONE place is the served
  TABLE; the dict is a retired seed input, not a competing source.**
- **C-CLASSIFIER-PURPOSE** (Andrew-direct 2026-09-11 ~07:1xZ, via `3.0.0_SA_CVO~Z` C-S3 @`4275402ec2`) --
  ETFClassifier is a **CURATED TAGGING LIST**, not a single-source-of-truth architecture. VERBATIM:
  *"ETFClassifier is basically a developing list of how we tag securities we own. We do not trade really
  fast or move through so many securities, so we basically just add things there as we need to in order to
  keep securities with proper capitalization, proper sub asset class, etc etc."* This SETTLES C-ONE-SOURCE
  and BINDS the cells three ways:
  - **(a) the ONE place is the served TABLE** (DynamoDB `etf-classifications`, read via ETFClassifier by
    the positioning and CMA lambdas). The dict `_shared/etf_classification.py` (136 entries) is a
    **SUPERSEDED seed input** that fell behind the table (285) -- to be retired/reconciled, NOT treated as
    a competing source.
  - **(b) a missing scheduler is NOT a defect and the 169 table-only rows are NOT unexplained.** A person
    extends a curated list on acquisition (the person IS the mechanism), and `updated_by` attributes all
    285 rows with ZERO unattributed. ⛔ Do NOT cut "give the seed a trigger" or "account for the 169" as
    work.
  - **(c) `equity` as a CLASS must be distinguishable from `equity` as the positioning lambda's
    unknown-DEFAULT** (`lambda_function.py:359`). A registry whose job is keeping securities PROPERLY
    TAGGED cannot let "properly tagged equity" and "not recognised" be the same string -- that bucket is
    unauditable. This is **FWD-5's PRIMARY round-2 work.**
  The reconciliation is ADDITIVE to the list (add Commodities + Alternatives to the stored vocabulary; move
  the seven `hedge` tickers per C-VOL-HEDGE-STRUCTURED; fill the 3 blank `sub_asset_class` rows -- the real
  coverage gap, 282 of 285 populated), NOT a migration of something broken.
- **C-VOL-HEDGE-STRUCTURED** -- volatility and hedge products classify to **Structured**, not Equity,
  and physical/crypto/commodity-index positions to **Commodities**, not Equity. This is the Cottonwood
  catalyst and it is a CLASSIFICATION change, verified on a surface but driven by the classifier.
  ⛔ **"HEDGE PRODUCTS" HERE MEANS VOLATILITY AND DERIVATIVE INSTRUMENTS (e.g. VXX, VIXY) -- NOT the
  legacy served value `asset_class=hedge`.** The word "hedge" does two jobs -- a product CATEGORY (this
  constraint) and a legacy DATA VALUE -- and their memberships DIFFER. The `asset_class=hedge` bucket,
  enumerated over the live table by two seats on two instruments (2.0.0_SA_COO~Z, 3.0.0_SA_CVO~Z), holds
  SEVEN tickers: SIX commodities (DBC, GLD, GSG, IAU, SLV, USO) and ONE volatility (VIXY). It DISSOLVES;
  it does NOT rename wholesale to Structured. It splits by `sub_asset_class`: {Gold, Silver, Oil,
  Commodities} -> **Commodities**; Volatility -> **Structured** (VIXY, plus VXX currently mis-served
  `equity`). Reading this constraint as "the `hedge` bucket -> Structured" mis-files the six commodities
  and is the exact error to avoid.
- **C-RETAG-SAFETY** (measured, `0.4.0_DT_ClientPlatform` brief
  `docs/briefs/positioning-gld-vxx-satellites-20260911.md@46f7e03df8`; Andrew-direct 2026-09-11 ~07:2xZ to
  fold into POSN_ASTTAX, via `0.0.0_AB_MSTR` msg 21263) -- ⛔ **THE RETAG OF THE COMMODITY/HEDGE TICKERS IS
  A PRODUCTION LANDMINE UNTIL THE POSITIONING GENERATOR IS HARDENED; the round-2 SEQUENCE is load-bearing.**
  ⛔ **RE-FOUNDED TWICE, AND THE SECOND RE-FOUNDING REVERSES THE FIRST. READ THIS BLOCK BEFORE THE
  ONE BELOW IT.**
  **THE ORIGINAL `0.4.0_DT_ClientPlatform` MECHANISM -- the KeyError and the generator dying -- IS
  WHAT IS RUNNING IN PRODUCTION RIGHT NOW.**
  ⛔ **AND THE SEVERITY CLAUSE IS NARROWED, ON `3.0.0_SA_CVO~Z`'s `C-S52`: WHAT IS ESTABLISHED IS AN
  UNSAFE GENERATION PRECONDITION, *NOT* DEMONSTRATED PAGE-BLANKING.** Its words: *"This establishes
  an unsafe generation precondition; it does not demonstrate live page blanking or a performed
  retag."* **No retag was performed and no live page was read.** Page-blanking is the DT brief's
  PREDICTED consequence of the precondition, and this seat carried that phrasing forward as though
  the measurement had reached it. It had not. The precondition is measured; the consequence is
  inferred, and the two must not be written as one sentence. It was declared
  falsified at ~20:0xZ by this seat on a measurement taken against **HEAD**, and HEAD was never the
  plane this constraint is about. Measured 2026-09-11 ~23:4xZ by `AT3-s-5`, TWO INSTRUMENTS, TWO
  SEATS, TWO METHODS:
  - the worker DROVE THE DOWNLOADED DEPLOYED BYTES: `KeyError: 'Structured'` at
    `calculate_allocations():239`, **11 of 11 members**. Deployed `lambda_function.py` 94,164 B
    `md5 cc79aff...` vs HEAD 115,411 B `md5 96aedb5...`; `Commodities` 0/12, `Alternatives` 0/7,
    `normalize_asset_class` 0/13, positive control `def lambda_handler` 1/1, negative control 0/0.
  - `2.0.0_SA_COO~Z` read the AWS CONTROL PLANE instead: `get-function-configuration` ->
    `LastModified 2026-08-18T18:34:43Z`, `CodeSha256 PRg64EGzQtLw7/HAhyN/jNP6rd01PrcLK4wKqCHAKfQ=`.
  - **A THIRD, ADDED 2026-09-12: `3.0.0_SA_CVO~Z`'s `C-S52` INDEPENDENTLY REPRODUCED** 11/11
    candidate AFTER-exceptions against 11/11 successful repaired-source arms, on the downloaded
    bytes (94,164 B, `md5 cc79aff7506f8c39e17453f386c69551`). **Three methods, three seats, one
    answer** -- so the DEPLOY GAP is stronger than when it was first written, even as the severity
    clause above is weaker.
  ⛔ **THE DEPLOYED BYTES WERE BUILT 2026-08-18. `AT2-s-6`, `AT2-s-1` AND `AT3-s-1` ALL POST-DATE THAT
  DEPLOY, SO EVERY REPAIR THIS PRD CITED AS HAVING KILLED THE KeyError IS COMMITTED-NOT-DEPLOYED.**
  ⭐ **THE DT BRIEF WAS RIGHT THE WHOLE TIME**, and was declared falsified by a measurement on the
  wrong plane. A `git` read cannot falsify a claim about a running lambda: DESIRED != APPLIED !=
  EXERCISED (Rule 22), and `deployed bytes` has three referents. **A CONSTRAINT ABOUT THE SERVED
  PLANE IS ONLY EVER FALSIFIED BY A SERVED-PLANE READ.**
  ⚠ **SO THE BLOCK BELOW IS TRUE OF HEAD AND FALSE OF PRODUCTION, and it is kept rather than deleted
  because the two-plane split IS the finding:** after a deploy of HEAD the failure mode changes from
  BLANKING to SILENT ZEROING, so both mechanisms are live-in-waiting on different planes and a retag
  is unsafe under either. Read "LIVE MECHANISM" below as "THE MECHANISM AT HEAD, POST-DEPLOY".
  **THE LIVE MECHANISM (measured by `TO-S7-1`, round 2): SILENT ZEROING, NOT BLANKING.**
  `AT2-s-6` hardened the generator and KILLED the KeyError -- **0 of 17 hops RAISE**. A retag today
  does NOT blank the page. It renders `Commodities`/`Structured` as the literal string `'Unknown'`
  **and the weight is lost -- but NOT in the allocation dict.**
  > ⚠ **CORRECTED AT v0.6 (round-3 L10). THIS LINE USED TO READ "and silently zeroes the
  > weight", AND THAT HALF WAS FALSE AT HEAD.** `AT2-s-1` added an `else` to all three
  > `asset_class` chains, so a Commodities holding served allocation **2.5, not 0.000**
  > (measured by `Z-W10-S1` on the real generator at base commit `651ffd4f16`, with a probe
  > ticker at weight 0.025). The loss is real and sits ELSEWHERE: at the **five-class served
  > view** (the label is `'Unknown'`, so the Commodities line holds nothing and reads 0.000)
  > and at the **delta and benchmark-spread rows, which carried NO ROW AT ALL** rather than a
  > zero. ⛔ **A BAR WRITTEN AS "confirm the weight zeroes in the allocation dict" RETURNS
  > THE SAME ANSWER BEFORE AND AFTER A RETAG** and cannot gate it -- which matters because
  > `AT3-s-5` is the gating bar and reads this paragraph. ⛔ **THE HAZARD GOT QUIETER, NOT SAFER** -- strictly WORSE for
  detection than the blanking it replaced, because a blank page is noticed in seconds and a zeroed
  allocation line looks like a real allocation. The retag remains UNSAFE; the reason changed.
  ⚠ **VINTAGE:** the 17-hop figures are pinned to `TO-S7-1`'s run and `3.0.0_SA_CVO~Z` records that
  `S1` later repaired a benchmark hop, so the RATIO is historical. **The VERDICT is not** -- the CVO
  re-confirmed against current controls that both classes still display as `Unknown`.
  ⛔ **THE DT BRIEF'S MECHANISM -- AND ITS HEADER USED TO READ "PRESERVED AS HISTORY AND NO LONGER
  OPERATIVE ... falsified by `AT2-s-6`", WHICH CONTRADICTED THE BLOCK ABOVE IT.** That contradiction
  was this seat's: the reversal was ADDED as a new paragraph without reconciling the old one, so the
  spec asserted both that this mechanism is dead and that it is running. **IT IS FALSIFIED AT HEAD
  ONLY. IT IS WHAT THE DEPLOYED BYTES RUN.**
  `yang-generate-positioning/lambda_function.py` buckets weight into FIXED-KEY dicts --
  `management_allocations = {'active','passive'}` (:228, :242-243) and an `asset_class` chain summing
  into `{cash, fixed_income, equity, hedge}` (:368-369) -- so a value the dict lacks raises `KeyError`
  in `calculate_allocations()` (:1917/:1926), the generator dies, and `positioning_data.json` is not
  rewritten. ⚠ **THE BRIEF THEN PREDICTED THE PAGE WOULD BLANK FOR ALL FOUR PARTNER FIRMS. THAT
  CONSEQUENCE WAS NEVER MEASURED -- not by the brief, and not since** (`C-S52`). The generator death
  is measured on four instruments; what the page does after it is inferred.
  - **`management_style` half -- ARMED and LATENT.** `management_style="unknown"` is a TRUTHY placeholder the
    default-to-passive guard (:72 `value if value else default`, :81) CANNOT fire on; 187 of 285 rows carry
    it, 0 of the 30 currently-held tickers do (the only reason the page works today). GLD, IAU, SLV, USO,
    DBC, GSG -- every commodity/hedge instrument -- trip=TRUE; VXX is `passive` (trip=FALSE), which is
    precisely why VXX works today. (`2.0.0_SA_COO~Z` independently verified: the unsafe six ARE the six
    Commodities moves; VIXY, the Structured move, is the safe one.)
  - **`asset_class` half -- MEASURED, and the prediction was WRONG.** This bullet used to say the
    asset_class KeyError "is the same fixed-key pattern" and ordered a round-2 cell to measure it
    "never assume it". `TO-S7-1` did exactly that and returned **NO-GO with 0 of 17 hops RAISING**:
    the hardening removed the raise, so moving GLD `hedge`->Commodities or VXX `equity`->Structured
    yields `'Unknown'` and a **zeroed weight**, not a crash. ⭐ **THE PRD ASKED FOR THE MEASUREMENT
    THAT CONTRADICTED IT, AND GOT IT** -- that is the instruction working, not failing. The reason
    the wrong mechanism survived is that prose predates its own instrument's answer, so a spec that
    orders a measurement must be re-read WHEN THE ANSWER LANDS.
  ⛔ **SEQUENCE (round 2): (0) HARDEN the generator -- treat `"unknown"` as falsy in the guard AND make both
  allocation dicts tolerate an unexpected key (DT Step 3, the durable class fix); (1) set the affected
  tickers' `management_style` to the factually-correct value (passive for a bullion trust) -- DT Step 1;
  (2) **THE BAR, stated as a CONDITION and not as an act:** for EVERY ticker in the retag set, ACROSS
  **EVERY SERVED SURFACE THE RETAGGED VALUE REACHES**, (a) the served `asset_class` equals its
  ratified five-class label, (b) **its LABEL-GROUPED weight** is NON-ZERO and equal to its pre-retag
  weight, (c) **its row RENDERS** -- served row count equals DOM row count -- and (d) **the class
  subtotals sum to the grand total.**
  ⛔ **(b) SAYS "LABEL-GROUPED" BECAUSE THE ALLOCATION-DICT ENTRY DOES NOT DISCRIMINATE, AND READING
  IT WOULD BE THE `S2-AC5` SHAPE A THIRD TIME -- INSIDE THIS BAR.** Measured by `AT3-s-1` (row
  `W10-S1`) on the real `generate_positioning_data`, same input:
  | | served label | LABEL-GROUPED weight | `allocation['commodities']` |
  |---|---|---|---|
  | BEFORE | `'Unknown'` | **0.000** | 2.5 |
  | AFTER | `'Commodities'` | **0.025** | 2.5 |
  **THE ALLOCATION-DICT COLUMN DOES NOT MOVE.** At base `651ffd4f16` all three `if/elif` chains
  ALREADY carried an `else` from `AT2-s-1` and the accumulator ALREADY served 2.5, so a clause reading
  "the weight zeroes in the allocation dict" reads IDENTICALLY in the healthy world and the broken
  one. What was broken is the SERVED LABEL and the LABEL-GROUPED weight -- and those are what (a) and
  (b) now name.
  ⚠ **AND THIS IS THE SECOND TIME THIS CONSTRAINT'S MECHANISM HAS BEEN OVERTAKEN BY A REPAIR** --
  `AT2-s-6` killed the KeyError, then `AT2-s-1` filled the `else` branches. A constraint that names a
  mechanism must be re-read against the repairs that land after it, every round, or it silently
  describes a world that no longer exists.
  ⛔ **WIDENED 2026-09-11 BECAUSE THE FIRST CUT OF THIS BAR WAS NARROWER THAN THE HAZARD.** It read
  "from the served artifact", meaning `positioning_data.json` alone. `2.0.0_SA_COO~Z`'s wave-1 cells
  measured BOTH collapse sites OUTSIDE that artifact, so a GO would have been TRUE AND INSUFFICIENT:
    - DOWNSTREAM (`W11-S1`): `portal/src/pages/Positioning/tabs/HoldingsTab.tsx:1392-1394` iterates a
      HARDCODED `assetClassOrder = ['Fixed Income','Equity']`. A group keyed `Commodities` /
      `Structured` / `Alternatives` is **NEVER ITERATED** -- the row renders NOWHERE while its weight
      stays in the grand total. 42 of 42 consumers examined; 12 sites across 8 files.
    - A DIFFERENT ARTIFACT (`W12-S2/S3`): `yang-generate-allocation-summary` carries `Commodities`
      through all 88 hops, then draws `policy_weight 0.0` from a fixed two-key `BENCHMARK_ALLOCATIONS`
      -- and writes `holdings_attribution_data.json`, not `positioning_data.json`.
  ⛔ **AND THIS EXACT BUG HAS ALREADY SHIPPED ONCE**, which is why (c) and (d) are bars and not
  advice: the same file documents it for `Cash` at `:1364-1372`, measured on PROD v2.1.167 -- PFDE
  90 -> 89 served-vs-DOM rows, subtotals 99.98 under a grand total of 100.01. The remedy folded only
  `Cash` and `Hedge`, so **a retag reproduces it with a new value.**
  ⭐ **THE MECHANISM, in the measuring worker's own words: "Data reaches three lambdas; the code
  hardening reaches one."** `AT3-s-1`'s write surface is ONE code path; the retagged DATA reaches the
  siblings through a second door -- a consumer importing `ETFClassifier` directly, all three copies
  byte-identical (`md5 e62906eff240a853029181715fc9b451`).
  ⚠ **THE SURFACE LIST IS A SUBTRACTION, NOT A RECALL LIST:** enumerate every artifact and rendered
  surface a retagged `asset_class` reaches and subtract the ones proven unreachable; do not re-use
  the three named above as if they were the whole set. That error -- writing an enumeration from
  memory after subtracting correctly over the population -- is the one this project keeps paying for.
  ⛔ **WRITTEN AS AN ACT
  ("verify the chain") THIS STEP INVITED A READER TO TREAT A COMPLETED VERIFICATION CELL AS A PASSED
  ONE -- an error this seat made and withdrew.** A step that names a TASK is satisfied by doing the
  task; a step that names a CONDITION is satisfied only by the world. **Step (2) is currently NOT
  MET: `TO-S7-1` measured it and returned NO-GO.** ONLY THEN
  (3) retag **IN BOTH STORES.** ⛔ **A DYNAMODB-ONLY RETAG IS NOT A RETAG: it is ANNOUNCED AND
  REFUSED (`rc=3`) by `AT3-s-4`'s durability fix, so the retag MUST ALSO land in
  `ETF_CLASSIFICATIONS`.** ⭐ And the finding under that is sharper than the rule: the revert hazard
  was MASKED. The seeder at HEAD **cannot complete a run at all** -- it writes `sub_asset_class=""`
  for 16 of 136 tickers and that is a GSI hash key, so batch 1 is rejected and ZERO items are
  written (measured on the real table with a control, first offender at sorted index 0). **Anyone who
  fixed only the crash would have converted a dead script into a working revert**, which is why the
  durability fix and the crash fix had to land together.**
  A retag before (0)-(2) serves `'Unknown'` at a ZEROED weight on a page that still
  renders -- which is why "confirm the page still renders" can never discharge this step. This is
  the SAME defect class as C-CLASSIFIER-PURPOSE(c) -- a placeholder value indistinguishable from a real one
  -- at the `management_style` grain. ⭐ VXX is ALREADY correctly flowing into Satellites 70/80/90/98 via the
  MODELS path (LT 1.5% / ULT 2.0%, `sub_asset_class` Volatility); POSN only retags VXX's served top-level
  `asset_class`, and touches NO holding, weight or satellite placement.
- **C-TWO-SURFACES** -- there are **TWO** surfaces that show asset classes: **Positioning**, and the
  **combined Philosophy / Capital-Market-Assumptions** view. (Andrew-direct 2026-09-11: Philosophy and
  CMA are the same page now.) Both must agree; FWD-6 is graded over the two.
- **C-MEMBERSHIP-AT-L5** -- the exact membership RULES (which instrument is Structured vs Commodities
  vs Alternatives at the edges) are the classifier's substance and are decided in the cells at L5, not
  pre-judged here. FWD-1's bar is only that every holding lands in exactly one class.
- **C-SATELLITE-DATA** -- the classifier's NECESSARY DATA input is the Cottonwood satellite components,
  `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_SOURCE_SATELLITE_COMPONENTS_20260911.md@3685cd9c1e`
  (9 satellites, 228 component rows; ticker = `metadata.symbol`, the AUTHORITATIVE field, never the
  display name; weight = `absoluteAllocation`). Andrew-named necessary data 2026-09-11 ("the whole
  reason we are doing POSN_ASTTAX is to get these included in Cottonwood's satellites in a clean visible
  manner" / "fold it in as its necessary data"). Every one of the 228 components MUST sort into exactly
  one of the five classes (FWD-1) and be VISIBLE as such on the surfaces (FWD-6). The MEASURED
  served-plane gap this project closes (2.0.0_SA_COO~Z, DynamoDB `etf-classifications`): `VXX`
  (VIX-futures ETN) is served `asset_class=equity` and must move to **Structured**; `GLD` (physical
  gold) is served `asset_class=hedge` and must move to **Commodities** (C-VOL-HEDGE-STRUCTURED, FWD-2).
  `sub_asset_class` already reads `Volatility`/`Gold`, so the remedy is a TOP-LEVEL retag, not a
  from-scratch ruling. Identity resolves BY TICKER (metadata.symbol); the display-name irregularity
  (GLD/VXX carry no ticker prefix) is NOT the failure mode -- the wrong top-level class is.

## 5. Rulings that BIND (Andrew-direct)

- **2026-09-11 ~07:1xZ, Andrew-direct, VERBATIM (via `3.0.0_SA_CVO~Z` C-S3 @`4275402ec2`):**
  *"ETFClassifier is basically a developing list of how we tag securities we own. We do not trade really
  fast or move through so many securities, so we basically just add things there as we need to in order to
  keep securities with proper capitalization, proper sub asset class, etc etc"* -- the PURPOSE ruling,
  folded in at v0.4 as **C-CLASSIFIER-PURPOSE** (s.4). It settles C-ONE-SOURCE (the served TABLE is the one
  place) and strikes "give the seed a trigger" / "account for the 169" from round-2 work (neither is a
  defect for a curated list a person extends).
- **2026-09-11 ~07:2xZ, Andrew-direct (laptop terminal, relayed via `0.0.0_AB_MSTR` msg 21263):**
  *"i need this brief sent over to sitez, specifically to CTO~Z ... this needs to get folded into the work
  on POSN_ASTTAX"* -- the `0.4.0_DT_ClientPlatform` GLD/VXX positioning brief
  (`docs/briefs/positioning-gld-vxx-satellites-20260911.md@46f7e03df8`), folded at v0.5 as
  **C-RETAG-SAFETY** (s.4). It names a production landmine the round-2 retag must sequence behind.
  ⚠ **The constraint was RE-FOUNDED 2026-09-11 on `TO-S7-1`'s measurement** -- still binding, and the
  brief's KeyError/page-blank mechanism is preserved there as history rather than as the live reason.
  Andrew's ruling and the DT brief are UNCHANGED; only the mechanism the round-3 cells will read.
- **2026-09-11, Andrew-direct, VERBATIM:** *"Confirmed, just note that Philosophy/CMA are the same page
  now. Also this should likely be heavily involved with ETFClassifier."* -- confirming the six DONE WHEN
  bars (his reserved L2 step), and adding the two refinements now carried as C-TWO-SURFACES and
  C-ONE-SOURCE.
- **2026-09-11, Andrew-direct, VERBATIM:** *"read the satellite file and fold it in as its necessary
  data for POSN_ASTTAX"* (relayed via `0.0.0_AB_MSTR`, bus ef105705) -- the Cottonwood satellite
  components are folded in at v0.2 as **C-SATELLITE-DATA** (s.4), binding the classifier to
  `ANDREW_SOURCE_SATELLITE_COMPONENTS_20260911.md@3685cd9c1e` as its necessary dataset.
- **2026-09-01, Andrew-direct (register):** the taxonomy goes in D4, owned by the site-z fabric;
  `1.0.0_SA_CTO~Z` takes the transcript and authors this PRD.

## 6. Out of scope

- The membership rules at the class edges (C-MEMBERSHIP-AT-L5 -- L5/the cells).
- Any surface's content beyond the asset-class breakdown itself.
- The TAX SMA Teams thread (a second source Andrew named; deferred on "the transcript is fine for now"
  -- MAY refine scope at L4 if read, but does not block this PRD).
- Whether GLD (or any instrument) is ADDED to Yang's MODEL HOLDINGS -- an ALLOCATION decision (Yang +
  Andrew), not classification. POSN_ASTTAX classifies the registry rows; it does not decide holdings.
- Adding GLD/VXX to the Bloomberg ETF daily pull for CHARACTERISTICS accrual -- `0.0.3_BG_BBGTerminal` /
  site-Z's surface (the pull file is a Bloomberg-box working-tree deploy), NOT this lane. ⚠ TIME-SENSITIVE
  (Bloomberg derived fields are current-day-only, no backfill; DT "step 0") -- CARRIED to Andrew / the BBG
  lane, not a POSN cell.
- The SPYM-duplicate-in-INT count defect and the VXX beta 0.9968 anomaly (DT brief, "found in passing") --
  separate defects for the PKL-to-JSON owner; surfaced, not folded here.

## 7. SURFACE MANIFEST (step 4 -> step 5) -- one row per ENGINE

Coverage by SUBTRACTION from the printed denominator (rule 24(i)): **endpoint_outcomes = 6
(FWD-1..FWD-6); covered = 6; uncovered = declared MINUS covered = 0.**

| row | ENGINE | what it is | outcomes it carries |
|---|---|---|---|
| **S1** | **ETFClassifier** -- the one classification source | the single function/module that assigns every holding to exactly one of the five classes, and where the Cottonwood reassignment (vol/hedge -> Structured, gold/commodities -> Commodities) lives | **FWD-1, FWD-2, FWD-5** |
| **S2** | **Class registry** -- order + color | the single definition of the five classes' canonical order and their colors, read by every surface | **FWD-3, FWD-4** |
| **S3** | **The two surfaces** -- Positioning; Philosophy/CMA | the views that render the breakdown, reading class + order + color from S1 and S2 rather than re-deriving them | **FWD-6** |

> ⛔ **S3 IS SCOPED TO TWO SURFACES AND THE WORLD HAS AT LEAST THREE READERS -- DISCLOSED AT v0.6 per the CTO ruling `POSN_ASTTAX-Z-S42` @`9d7b09987f`, which settles `Z-C-S55`.** An ADDITIONAL ETF publisher outside this two-sibling set copies gold holding class values and emits a four-key book allocation at its source lines 469-472. **It is OUT of POSN's WRITE scope** -- it belongs to another project and no POSN worker may rewrite it -- **and IN this project's DISCLOSURE scope**, because Rule 24's subtraction is over the surfaces a class value REACHES, not the surfaces this project may EDIT.
> **MEASURED STATE, WITH THE CONDITION THAT ENDS IT:** 189 rows over four books and **ZERO candidate members** at the pin `Z-C-S55` cites, so its current bytes cannot exercise post-retag loss. ⚠ **That zero is a STATE, not a property.** It flips the first time a candidate member appears in any of those four books, and a zero recorded without its expiry is the same shape as a criterion that returns the same answer in both worlds.
> ⭐ **AND THIS IS THE SAME DEFECT AS FWD-6's EMPTY COVERAGE, SEEN FROM THE OTHER SIDE:** a row scoped to two surfaces cannot generate a cell that checks three.

**MECE check:** FWD-1 -> S1 · FWD-2 -> S1 · FWD-3 -> S2 · FWD-4 -> S2 · FWD-5 -> S1 · FWD-6 -> S3.
**6 of 6 outcomes carried by exactly one row, 0 uncovered.**
> ⛔ **READ THAT AS ASSIGNMENT, NEVER AS ISSUANCE -- QUALIFIED AT v0.6 AFTER IT MISLED THREE SEATS FOR THREE ROUNDS.** Its domain is *outcomes assigned to a surface row*, and it is true of that domain. It says NOTHING about whether a cell was ever cut. Measured at the round-3 L10 over the 15 cut orders: **`FWD-4` and `FWD-6` are named by ZERO orders.** Assigned and unserved. **A surface row owning an outcome is not a cell serving it**, and this line's "0 uncovered" is exactly the green that made the gap invisible -- an empty subtraction gets acted on rather than argued with, and this one printed a denominator so it read as measured. (The surfaces DISPLAY S1/S2's results, but
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
