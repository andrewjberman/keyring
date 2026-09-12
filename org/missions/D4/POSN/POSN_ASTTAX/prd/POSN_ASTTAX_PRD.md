# POSN_ASTTAX -- PRD (step 4)

```json
{
 "project": "POSN_ASTTAX",
 "directive": "D4",
 "fabric": "site-z",
 "prd_version": "v0.5",
 "step": 4,
 "brief_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_ASSET_CLASS_TAXONOMY_BRIEF.md@03f1d00ec4",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6"],
 "status": "DRAFT"
}
```

**Version:** v0.5, 2026-09-11 -- v0.1 first PRD; v0.2 folded in Andrew's Cottonwood satellite components (s.4 C-SATELLITE-DATA), on his direct "read the satellite file and fold it in as its necessary data for POSN_ASTTAX"; **v0.3 disambiguates C-VOL-HEDGE-STRUCTURED's "hedge products" from the legacy served value `asset_class=hedge`** -- a latent defect where the constraint, read against the live data, said the whole `hedge` bucket goes to Structured (found by 2.0.0_SA_COO~Z + 3.0.0_SA_CVO~Z); **v0.4 folds in Andrew's ETFClassifier PURPOSE ruling as C-CLASSIFIER-PURPOSE (s.4)** -- the registry is a curated tagging list, so the served TABLE is the one place, the dict a retired seed input, and equity-as-class must be distinguishable from equity-as-unknown-default (carried via 3.0.0_SA_CVO~Z C-S3 @`4275402ec2`); **v0.5 folds in the `0.4.0_DT_ClientPlatform` GLD/VXX positioning brief as C-RETAG-SAFETY (s.4)** -- the retag of the commodity/hedge tickers is a production landmine (a fixed-key allocation dict KeyErrors and blanks the page for all four partner firms) until the positioning generator is hardened; Andrew-direct 2026-09-11 ~07:2xZ to fold it into POSN_ASTTAX. Each bump re-opens the two L4-R sign-offs. **Author** `1.0.0_SA_CTO~Z` (L4). **Brief:** the nomenclature
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
  **and silently zeroes the weight.** ⛔ **THE HAZARD GOT QUIETER, NOT SAFER** -- strictly WORSE for
  detection than the blanking it replaced, because a blank page is noticed in seconds and a zeroed
  allocation line looks like a real allocation. The retag remains UNSAFE; the reason changed.
  ⚠ **VINTAGE:** the 17-hop figures are pinned to `TO-S7-1`'s run and `3.0.0_SA_CVO~Z` records that
  `S1` later repaired a benchmark hop, so the RATIO is historical. **The VERDICT is not** -- the CVO
  re-confirmed against current controls that both classes still display as `Unknown`.
  **THE ORIGINAL MECHANISM, PRESERVED AS HISTORY AND NO LONGER OPERATIVE** (true when the DT brief was
  written, falsified by `AT2-s-6`): `yang-generate-positioning/lambda_function.py` bucketed weight into
  FIXED-KEY dicts -- `management_allocations = {'active','passive'}` (:228, :242-243) and an
  `asset_class` chain summing into `{cash, fixed_income, equity, hedge}` (:368-369) -- so a value the
  dict lacked raised `KeyError` in `calculate_allocations()` (:1917/:1926), the generator died,
  `positioning_data.json` was not rewritten, and the page BLANKED FOR ALL FOUR PARTNER FIRMS.
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
