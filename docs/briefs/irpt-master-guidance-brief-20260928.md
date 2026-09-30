# Investor Reporting -- master UI guidance brief, 2026-09-28

**Mode:** midstream on DSGN_IRPTV1 (with IRPT_BCKEND rows). **By:** 4.0.0_SA_CRO on Andrew's word (the record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260928_18xxZ_UI_REMAINING_BRIEF_AND_MASTER_GUIDANCE_BRIEF.md`): "take that folder, assess those points, and in line with your consolidated ui-walk points, will make a master guidance brief which shall be relayed to CTO and COO~D at my behest"; "Corroborate the points made in the transcript with the relevant photos".
**Relay: HELD** for Andrew's word. **Register (the source of every table here):** `docs/briefs/irpt-master-guidance-findings-20260928.json`.
**Inputs:** Andrew's manual walk -- three transcripts (`tmp/ui-guidance/20260928/`, gitignored: main, analysis, holdings) and 17 screenshots (`C:\Users\AndrewBerman\Pictures\Screenshots\irpt_manual_walk_v1`) -- plus the CRO's consolidated walk register (35 findings, `docs/briefs/irpt-ui-remaining-findings-20260928.json`, walk `20260928T174953Z`).

## Part 0 -- what Andrew asked for, in one screen

- **Holdings (URGENT, Andrew's word):** two components only. First, the MDPF 'All Categories' card, starting at the accounts (L-1) and drilling Models / SMAs / Client (L0) and down. Second, Positioning's tree map with the holdings table under it. Everything else goes. The taxonomy is Models / SMAs / Client. Colours and classes are Positioning's: commodities are gold and Other is grey. (AD-01..AD-05)
- **Analysis:** three pages you step through: Portfolio (Client | Prospect) -> Analysis type (cards open the canonical modal) -> Output (text fields) -> Generate. The prospect upload is obvious and ships its template. Requests and results are readable. (AD-06..AD-09)
- **Main:** each account shows its own tail everywhere. Search is search only. A client the search offers must open. 'About this scope' goes. (AD-10..AD-13)
- **Performance:** no walk has shown a working report. Name the dependency and make it answer. (AD-14)
- **Principle:** port what exists, and show only what the advisor needs. (AD-15)

Priorities: P0 4, P0 URGENT 2, P1 8, P2 1. **Corroboration:** every AD item cites at least one of Andrew's screenshots, and each screenshot was read and described in words. One item is PARTIAL: AD-11's empty-focus state is not in a screenshot.

## Part I -- stop-work notice for in-flight items

- ~D's closer-drive items for **UIC-10, UIC-12 and UIC-13** were edited in the portal working tree at 18:03-18:04Z. **AD-01 removes the accounts pie that UIC-10 and UIC-12 fix.** Stop that pie work. Its content (the accounts) becomes the L-1 level of the canonical card. UIC-13 (Over what 'Show all') stays useful.
- IR's page-local palette (IV-e-43 shifted hues, IV-e-27 Other=purple) is superseded by AD-04/AD-05: one registry, Positioning's.

## Part II -- Andrew's direction, corroborated

### AD-01 [P0 URGENT] Holdings: Holdings is TWO components, nothing else

**Direction.** Holdings shows exactly two things. (1) ONE canonical 'All Categories / Total Assets' fixture card that starts at the accounts in play (level L-1), drills to Models / SMAs / Client (L0), then to each L0 item's contents (L1, L2 ...), with the hover preview and the modal pop-up the MDPF card already has. (2) The securities tree map and, under it, the holdings table, both updating from whatever is selected in component 1. Every other card on the tab goes.

> "flag this, urgent, look here, important. What we are doing for the holdings page is there are two component structures ... That whole flow needs to be contained ... that is one component and drill down modal sequence ... Then two, we have the tree chart, which should display automatically and should update based on what is selected ... And underneath that is the holdings breakdown." (`holdings_walk_transcript.txt` l.99-110)

> "that account level needs to effectively be like L negative 1. It needs to sit before L0, where L0 is the model's, SMA's, client." (`holdings_walk_transcript.txt` l.84-88)

> "if you look at the MDPF underscore one, we already have the exact design for what this needs to look like ... It should be exactly what you see right in that picture." (`holdings_walk_transcript.txt` l.10-16)

**Screenshots.**

- `holdings_1.png` -- CONFIRMED: The Total Assets card draws a single grey slice and ONE category tile named for the account's rebalancer strategy; beneath it a second pie and table repeat the same four lines (three models and the client residual) in other colours.
- `holdings_5.png` -- CONFIRMED: The All-accounts view is a separate pie of the two accounts (near-white and grey slices, outlined labels) and a table, outside the canonical card.
- `mdpf_1.png` -- CONFIRMED: The canonical fixture: one navy card, Total Assets, a filled pie, and three nested tiles Models / SMAs / Client with their share of total.
- `mdpf_2.png` -- CONFIRMED: Hover state: the Models tile expands to a colour-coded bar with Primary and Custom and 'View breakdown'.
- `mdpf_3.png` -- CONFIRMED: 'View breakdown' opens the HeroDialog: What it is, How it is derived, a colour bar, the Primary and Custom members with amounts, and a source line naming the data vendors.

**Measured / current state.** portal `src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx:667` already renders `<CategoryViewTree ground="light" exactAmounts .../>`, but feeds it `mdpfResultFromSnapshot` (:442), which makes one card per TOP-LEVEL category the snapshot names ('Deliberately COARSE', :435-441). Below it the same file draws its own recharts donut and table. `HoldingsTab.tsx:99-105` composes AllocationBars, AccountFilter, DrillTree, HoldingsTreemap, SecurityList and HoldingsSummary. There is no L-1 account level in the card; accounts are a separate pie plus a picker.

**Reuse (do not rebuild).** `portal/src/components/CategoryViewTree.tsx (MDPF L0/L1/L2 fixture, HeroGraphic card + HeroDialog 'View breakdown'; used by src/pages/ModelPortfolios.tsx:1286)`; `portal/src/ui/components/graphic/HeroGraphic.tsx (the canonical card and modal)`; `portal/src/pages/Positioning/tabs/HoldingsTab.tsx (tree map + holdings table, see AD-04)`

**Absorbs walk findings:** UIC-10, UIC-11, UIC-12, UIR-34, UIW-0928-01, UIW-0928-02, UIW-0928-03. **Supersedes:** the accounts pie and its table (UIC-10/11/12 fix that pie; Andrew removes it); the per-account picker view (UIW-0928-01..03 live in it). **Owners:** 2.0.0_SA_COO~D, 2.0.0_SA_COO~M.

**Acceptance.** Holdings renders exactly two components: the canonical All Categories card (L-1 accounts -> L0 Models/SMAs/Client -> L1 -> L2, hover preview and HeroDialog on click), and the tree map with the holdings table beneath it, which re-scope to the card's current selection. No other card, pie, table, picker or panel is on the tab.

**Decision for the CTO.** C3 (one navy band per page): MDPF's fixture is a navy band and Identity already spends one. Andrew's word is 'exactly what you see right in that picture'. Record the departure (or retire the Identity band) rather than rendering the card light.

### AD-02 [P0 URGENT] Holdings: L0 is always Models / SMAs / Client -- never a 'rebalancer strategy'

**Direction.** The taxonomy is Models, SMAs and Client at every level, on the card, the map chips and the table. A residual outside a model is Client. 'Rebalancer strategy: <client> *<tail>' is not a category.

> "the model rebalancer strategy, that is not following correct taxonomy. As we've already established, the foundational taxonomy is models, SMAs, and clients. So the residual here, clearly that would be clients ... that residual is probably going to be PHYS. That is the gold allocation." (`holdings_walk_transcript.txt` l.27-31)

**Screenshots.**

- `holdings_1.png` -- CONFIRMED: The card's only category is 'Rebalancer strategy: <client> *9238'; its lines are three Opal models and 'Client (residual, not in a model)'.
- `holdings_3.png` -- CONFIRMED: The map chips read 'Model: Opal Conservative Growth', 'Model: Opal Fixed Income', 'Model: Opal Ultra Short-Term Income' and 'Model: Rebalancer strategy: <client> *9238'.

**Measured / current state.** The COT holdings snapshot names the account's rebalancer strategy as the node between the account and its models; `mdpfResultFromSnapshot` turns whatever the snapshot names at the top into the card's category, so the wrong word reaches the face from the data (claim: inferred from the adapter code and the two screenshots; the snapshot's node kinds were not read).

**Reuse (do not rebuild).** `portal/src/components/CategoryViewTree.tsx (its three L0 peers are exactly Models / SMAs / Client)`

**Absorbs walk findings:** UIR-48. **Supersedes:** nothing. **Owners:** 2.0.0_SA_COO~M, 2.0.0_SA_COO~D.

**Acceptance.** Every Holdings level above the models reads Models, SMAs or Client; no chip, card, row or breadcrumb carries 'Rebalancer strategy'; a residual outside a model sits under Client and is named by its holding (for example the gold position).

### AD-03 [P0] Holdings: Remove the Allocation panel and the Report details / Unique accounts / Source dates card

**Direction.** The Allocation panel is scratched. Report details, Unique accounts and the source-dates block go; anything worth keeping moves into the Total Assets card.

> "This allocation panel is useless. Just scratch it. You gain nothing from knowing this." (`holdings_walk_transcript.txt` l.21-23)

> "Report details, we don't care. Unique accounts, all this stuff, don't care. That information, if anything, could be conveyed in the total assets card." (`holdings_walk_transcript.txt` l.60-65)

**Screenshots.**

- `holdings__2.png` -- CONFIRMED: ALLOCATION: one grey 100% bar for the rebalancer strategy, footer 'Source: holdings_snapshot.build_cot.'
- `holdings_4.png` -- CONFIRMED: Report details: 'Ready Business date 2026-09-22 HOLDINGS_READY', 'Classification unknown for 116 of 116 holdings nodes -- their supervision and advisory partitions are shown as withheld, not as a classification.'; Unique accounts 2; Source dates and model coverage.

**Measured / current state.** HoldingsTab.tsx imports AllocationBars (:99) and HoldingsSummary (:104); the walk measured the same card on all three clients (#021, #086, #153).

**Absorbs walk findings:** UIW-0928-04, UIC-14. **Supersedes:** the Allocation panel; the Report details and Unique accounts card. **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** Holdings carries no Allocation panel and no Report details / Unique accounts / source-dates card; the as-of date and source appear once, on the Total Assets card, in client words.

### AD-04 [P0] Holdings: Port the tree map and holdings table from Positioning; sort by asset class, then weight

**Direction.** The securities map and the holdings table are copies of Positioning's: same classifier, same class order (Fixed Income and Cash, Equity, Structured, Commodities, Alternatives), same colours, same format. The table is ordered by the tuple (asset class, weight), not by weight alone. Keep the grey 'Smaller holdings' tile.

> "this securities tree chart map, securities map, this should be ported over from the Opal Positioning page" (`holdings_walk_transcript.txt` l.34)

> "should be organized not just by weight. It should be a tuple of weight by asset class. So starting from fixed income, then equity, and so on, following the exact same format that we use in positioning." (`holdings_walk_transcript.txt` l.94-97)

> "both the tree charts and the holdings breakdown should be almost exact copies of what's in positioning. This is not a new build ... The only addition in this case is what you built out with this other and, like, smaller holdings thing that's gray. That's fine. We can keep that." (`holdings_walk_transcript.txt` l.110-118)

**Screenshots.**

- `holdings_3.png` -- CONFIRMED: The IR map: equity blue, fixed income green, GLD orange, a grey 'Smaller holdings' tile; legend Fixed Income / Equity / Alternatives / Other(purple); tooltip 'CLIP - CLIP' (ticker repeated as name).

**Measured / current state.** IR draws its own map and list (`tabs/holdings/HoldingsTreemap.tsx`, `SecurityList.tsx`) with a page-local palette (`tabs/holdings/assetClass.ts`, IV-e-43 shifts equity/fixed income/alternatives one step and IV-e-27 makes Other purple600). Positioning (`src/pages/Positioning/tabs/HoldingsTab.tsx`) reads the shared `ASSET_CLASS` registry (:161-172), orders classes by `ASSET_CLASS_ORDER` (:183-189: Fixed Income, Equity, Structured, Commodities, Alternatives) and classifies via `constants/etf-categories.ts`.

**Reuse (do not rebuild).** `portal/src/pages/Positioning/tabs/HoldingsTab.tsx (Treemap, ASSET_CLASS_COLORS :161, ASSET_CLASS_ORDER :183)`; `portal/src/pages/Positioning/constants/etf-categories.ts (getETFCategory)`; `portal/src/lib/chartColors.ts (ASSET_CLASS, SUB_ASSET_COLORS)`

**Absorbs walk findings:** UIC-15, UIW-0928-05. **Supersedes:** IR's page-local asset-class palette (assetClass.ts IV-e-43/IV-e-27). **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** The Holdings tree map and table are rendered by the same component (or a shared extraction) as Positioning's, with Positioning's classifier, class order and colours; the table sorts by (class order, weight); names show beside tickers; zero-amount rows do not list; the grey 'Smaller holdings' tile stays.

### AD-05 [P0] Holdings: One canonical classification and colour: commodities are gold, never Alternatives; Other is grey

**Direction.** GLD and every commodity are Commodities (gold), not Alternatives; Alternatives means real estate, private equity and the like. Other is grey. One canonical form across Philosophy, Positioning and Investor Reporting.

> "We know, for example, that GLD gold is a commodity. We don't display commodities as alternatives ... A commodity in the Opal taxonomy is a gold-colored image, and that includes all commodities. Alternatives is really for real estate and stuff like that, or private equity ... So we should be using one canonical form" (`holdings_walk_transcript.txt` l.36-43)

> "I don't love other as purple. Other should be gray." (`holdings_walk_transcript.txt` l.45-47)

**Screenshots.**

- `holdings_3.png` -- CONFIRMED: GLD is orange and the legend's orange is 'Alternatives'; 'Other' is purple in the legend while 'Smaller holdings' is grey.
- `holdings_1.png` -- CONFIRMED: Colour meanings collide: 'Opal Fixed Income' is purple on the card's bar but grey in the pie below; 'Client (residual)' is purple in both.

**Measured / current state.** Served class: GLD reaches the page as alternatives (UIR-50 names the same collapse for GLD/VXX, owner ~M). Colour: the shared registry paints commodities `PALETTE.green900` (`src/lib/chartColors.ts:218`, set by CTO 101649 / IV-e-49 for a colour-distance invariant), and Positioning reads the same token (`Positioning/tabs/HoldingsTab.tsx:165`), so gold is live on NEITHER page today. IR's Other is `PALETTE.purple600` (`tabs/holdings/assetClass.ts`, IV-e-27).

**Reuse (do not rebuild).** `portal/src/lib/chartColors.ts ASSET_CLASS (the one place a class colour is decided)`; the ETF Classifier table behind Positioning (data/black_diamond/scripts/gold/lib/etf_classifier.py per assetClass.ts header)

**Absorbs walk findings:** UIR-50. **Supersedes:** IV-e-27 Other=purple600 (IR). **Owners:** 2.0.0_SA_COO~M, 2.0.0_SA_COO~D.

**Acceptance.** GLD and every commodity read Commodities in gold on Positioning and Investor Reporting alike; no commodity reads Alternatives; Other is grey; one colour means one thing on the whole tab.

**Decision for the CTO.** Andrew's transcript sets commodities = gold. The live registry (chartColors.ts:218) sets green900 under CTO 101649. Re-solve the IV-e-49/51 distance invariant around a gold commodities token and apply it in the shared registry so Positioning and IR move together.

### AD-06 [P1] Analysis: Analysis is a three-page, next/back flow: Portfolio -> Analysis type -> Output -> Generate

**Direction.** Page 1 SELECT PORTFOLIO: two big cards, Client or Prospect. Client defaults to the client chosen in the top search, or offers a search in its modal if none is chosen; Prospect opens the upload modal (AD-07). Page 2 CHOOSE ANALYSIS: the Overview / Comparison / Multi-Comp cards (AD-08). Page 3 OUTPUT: text inputs only -- title, who the report is for, any other field the output needs; firm follows the user's email (low priority: the beta runs from Global). One obvious Generate. The pages move back and forth freely.

> "There should be three primary functions here that you just click next, next, next through. The first one is the portfolio cross card ... That should effectively just give them the choice of client or prospect." (`analysis_walk_transcript.txt` [378.0]-[392.3])

> "if it's client, it will default to whatever client is already selected from the initial search bar. If there is no client selected, then in the modal it will give them the option to search for a client. The alternative button click that they can do here is prospect, which, of course, is going to pull up a card for the CSV or XLSX upload" (`analysis_walk_transcript.txt` [403.6]-[423.9])

> "the third page, which would be essentially a bunch of text inputs ... what is it going to be titled? Who is the client? ... Firm should be automatically selected based on the email." (`analysis_walk_transcript.txt` [495.6]-[522.8])

> "three clear, effectively, like, pages that you should be able to cursor right and left through" (`analysis_walk_transcript.txt` [547.6]-[561.3])

**Screenshots.**

- `analysis_1.png` -- CONFIRMED: Today: Generate shows the three variant cards, 'Client: the client selected above', the account list, 'Holdings snapshot', a collapsed 'Report title, recipient and comparisons', 'Variant Overview (0 comparisons)', a red recipient error on load, a grey Generate and 'No job submitted from this browser yet.'
- `analysis_2.png` -- CONFIRMED: 'Analyze a prospect portfolio instead' is a collapsed line below Generate, not a first choice.

**Measured / current state.** `tabs/analysis/` composes GenerateComposer, VariantCards/VariantSelector, ProspectComposer (a separate expander), RequestList and OwnedRequestHistory on one scrolling page.

**Reuse (do not rebuild).** `portal/src/pages/InvestorReporting/tabs/analysis/VariantCards.tsx`; `portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx`; `portal/src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx`; `portal/src/ui/components/graphic/HeroGraphic.tsx`

**Absorbs walk findings:** UIC-18, UIC-19, UIC-20, UIC-21, UIC-22. **Supersedes:** the single-page Generate form; the 'Analyze a prospect portfolio instead' expander. **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** Analysis opens on page 1 (Client | Prospect cards); Next leads to page 2 (the three analysis cards) and page 3 (output text fields), Back returns without losing input; one Generate on page 3; no required-field error shows before the user acts; the default title names the client and the variant, never one account.

### AD-07 [P1] Analysis: Prospect upload: an obvious Upload button, a modal with the rules and the template

**Direction.** Choosing Prospect opens a modal that states the upload rules and offers the canonical template; the template is named on the page.

> "It should be extremely clear where the upload is, that there's no button anywhere that I can see that would clearly delineate that advisors can upload. And when they click upload, they should see instructions on that modal ... And we have a CSV that already is a template that you should be able to find, that should be mentioned somewhere" (`analysis_walk_transcript.txt` [196.5]-[224.8])

**Screenshots.**

- `analysis_2.png` -- CONFIRMED: The upload lives inside the collapsed 'Analyze a prospect portfolio instead' line; no Upload button is visible.
- `20260928T174953Z#128 (CRO walk)` -- CONFIRMED (walk): Expanded, the drop zone says 'Drop the holdings template here, or choose a file: a Ticker column and one of Dollars, Shares, Target Weight or Current Weight', with no template link.

**Measured / current state.** The rules are the server reader's: `infra/aws/lambda/investor-reporting/intake/template_reader.py` -- a Ticker column plus ONE basis (Dollars, Shares, Target Weight or Current Weight), CSV or XLSX, at most 1 MB, 2,000 rows and 200 symbols. No downloadable template is served by the portal (none under portal/public). The nearest file is a test fixture, `infra/aws/lambda/investor-reporting/intake/fixtures/holdings/holdings_clean.csv` (claim: absence measured for portal/public and the analysis tab only).

**Reuse (do not rebuild).** `infra/aws/lambda/investor-reporting/intake/template_reader.py (the rules)`; `portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx`

**Absorbs walk findings:** none. **Supersedes:** nothing. **Owners:** 2.0.0_SA_COO~D, 2.0.0_SA_COO~Y.

**Acceptance.** Prospect shows an Upload button; its modal lists the reader's rules in plain words and links a downloadable CSV/XLSX template that the reader accepts unchanged.

### AD-08 [P1] Analysis: Analysis cards open the canonical modal and show which one is selected; Comparison and Multi-Comp take Opal models OR external ETFs

**Direction.** Each variant card opens the standard modal with its design notes and what the analysis does, and a 'Select this' action; the chosen card is visibly marked (a tab bar under the cards or the card itself coloured). Cards 2 and 3 accept an Opal model or an external ETF.

> "When you click on any of these cards, historically, these card figures would pop up with a modal. There is no modal here ... a modal pops up in the standard canonical form, and the modal has the design notes and explanation of what this analysis type is ... there should be a clear indication of which you're selecting here." (`analysis_walk_transcript.txt` [57.6]-[119.8])

> "some of the comparison ones may not just be compared to Opal models, they may be compared to ETFs ... there should be a clear input function to select between an Opal model or additional or external ETF" (`analysis_walk_transcript.txt` [469.1]-[485.1])

**Screenshots.**

- `analysis_1.png` -- CONFIRMED: Three navy variant cards with one-line captions; no modal, no selected state; 'Variant Overview (0 comparisons)' under them.

**Measured / current state.** The walk measured the same: pressing Multi-Comp left 'Variant: Overview (0 comparisons)' and printed 'Multi-Comp does not match 0 comparison(s); Overview does.' (UIC-18). The comparison input's placeholder already reads 'Opal model or ETF symbo[l]' (UIC-21), so the input accepts both kinds; the choice is not explained.

**Reuse (do not rebuild).** `portal/src/ui/components/graphic/HeroGraphic.tsx (HeroDialog, as CategoryViewTree's 'View breakdown')`; `portal/src/pages/InvestorReporting/tabs/analysis/VariantCards.tsx`

**Absorbs walk findings:** UIC-18, UIC-21. **Supersedes:** nothing. **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** Pressing a variant card opens a HeroDialog with what the analysis is, how it is built and a Select action; the selected card stays marked; Comparison and Multi-Comp offer a clear choice between an Opal model and an external ETF, and say how many each needs.

### AD-09 [P1] Analysis: Requests and results say what they are; a READY result is a readable report, not extraction diagnostics

**Direction.** Each request names the client, the analysis type and the date, and a status in words that says what 'needs attention' means and what to do. Opening a READY request shows the report, not SCALAR/DISCLOSURE/CHART codes, hashes or 'SUPPORTED' chips.

> "a lot of open REQs with strings attached, have no idea what any of these are, unavailable, needs attention. I don't know what needs attention. Ready, analysis ready, what analysis?" (`analysis_walk_transcript.txt` [126.1]-[143.1])

> "we see a lot of scalers and disclosures and charts. Looks like nothing is actually connected from reading those strings, or there's conflicts or missing dependencies ... incomprehensible strings with a green hashtag saying it's supported. I have no idea what that means." (`analysis_walk_transcript.txt` [147.4]-[169.5])

**Screenshots.**

- `analysis_2.png` -- CONFIRMED: Six rows '<client> Open REQ-<hash> . revision 1' with 'Unavailable -- needs attention', 'Loading -- Running -- in progress', 'Ready -- ANALYSIS_READY'.
- `analysis_3.png` -- CONFIRMED: The opened READY request: 'Extraction validation: CERTIFIED', 'Partial extraction ... 38 field or column records were not located; 7 values were withheld for conflicting units. Charts: 5 of 10. Disclosures: 44 of 60.', then dozens of lines like 'SCALAR: S14.drawdown.c0 -- UNIT_CONFLICT', 'DISCLOSURE: ... TEXT_NOT_UNIQUELY_LOCATED', 'SCALAR: unlocated_<hash> -- UNLOCATED_ON_PAGE'.
- `analysis_4.png` -- CONFIRMED: Section cards '2. S01 SUPPORTED  Label S01  Value 0.3  Unit unknown  Currency not stated  As of 2026-09-27  Vendor attribution: 2', repeated.

**Measured / current state.** The request list's rows come from RequestList.tsx / OwnedRequestHistory.tsx; the opened view from StageDisplay.tsx / NativeSections.tsx. The READY request is REQ-67e12718, the one ~Y's gate 4 names (IRPT_BCKEND~Y STATUS). Its content (38 records not located, 7 unit conflicts, 5 of 10 charts, 44 of 60 disclosures) is the backend's extraction result.

**Reuse (do not rebuild).** `portal/src/pages/InvestorReporting/tabs/analysis/RequestList.tsx`; `portal/src/pages/InvestorReporting/tabs/analysis/NativeSections.tsx`

**Absorbs walk findings:** UIC-23. **Supersedes:** the extraction-diagnostics view as the default result view. **Owners:** 2.0.0_SA_COO~D, 2.0.0_SA_COO~Y.

**Acceptance.** Each request row reads '<client> -- <analysis type> -- <date> -- <status in words>'; 'needs attention' says what is wrong and what the user can do; a READY request opens the finished report (sections, charts, figures with units) with no codes, hashes or diagnostics on its face; diagnostics, if kept, sit behind one 'technical details' control.

### AD-10 [P1] Main: One canonical account resolution everywhere: each account shows its own tail

**Direction.** Two accounts of one client show two different tails (9237 and 9238) on every surface: Over what, both pickers, the Holdings card and table, the map chips and the Analysis account list.

> "the two accounts are once again resolving to the same account listing. We're seeing 9237 brokerage for both accounts, even though we know that it's 9237 and 9238. So that account resolution function needs to be resolved." (`main_walk_transcript.txt` [149.2]-[164.8])

> "we really need to make sure that account resolutions are handled canonically throughout any place where accounts are displayed, anywhere on the investor reporting page." (`analysis_walk_transcript.txt` [26.4]-[33.1])

**Screenshots.**

- `main_3.png` -- CONFIRMED: Over what: two identical '****9237 / BROKERAGE' lines.
- `performance_1.png` -- CONFIRMED: The Performance picker: two options '****9237 / BROKERAGE' with different values.
- `analysis_1.png` -- CONFIRMED: Analysis accounts: two '****9237 / BROKERAGE' lines.
- `holdings_5.png` -- CONFIRMED: Holdings picker, pie labels, legend and table: two '****9237 / BROKERAGE'.
- `holdings_1.png` -- CONFIRMED: The breadcrumb names '<client> *9238' for the strategy under '****9237 / BROKERAGE': the data knows the second tail.

**Measured / current state.** The walk measured the same on every client: 11 identical COT labels, 3 identical 49F labels, 4 identical INF labels (UIR-26, owner ~M, open since 09-26). UIR-32/49 (two masking styles, '*9238' vs '****9237') is the same defect seen from the strategy node.

**Absorbs walk findings:** UIR-26, UIR-03, UIC-16. **Supersedes:** nothing. **Owners:** 2.0.0_SA_COO~M, 2.0.0_SA_COO~D.

**Acceptance.** Every account of every client carries its own masked tail and its full type ('Individual Retirement Account') in one masking style, identically on every Investor Reporting surface; no two accounts of one client share a label.

### AD-11 [P1] Main: Search is search only: nothing on focus, no Browse

**Direction.** Clicking the input shows nothing until the user types; the page offers no browse listing.

> "we really want the input search bar to function as a search bar. It is not a browse. When you click that input box ... nothing should appear until they start typing ... It is search only." (`main_walk_transcript.txt` [25.5]-[44.9])

**Screenshots.**

- `main_1.png` -- PARTIAL: the empty-focus state is not shown; the Browse button is.: A 'Browse' button sits beside the input; the typed query lists '13 MATCHED ACROSS FIRMS' with the exact match first.

**Measured / current state.** UIR-01 was graded MET on 09-27 with the acceptance '(Browse stays the listing)'; Andrew's word now retires Browse.

**Absorbs walk findings:** none. **Supersedes:** UIR-01's 'Browse stays the listing' clause. **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** Focusing the empty search input shows nothing; results appear only for typed text; there is no Browse button or browse list.

### AD-12 [P1] Main: A client the search offers must open; clear up whether names are truncated

**Direction.** A 49F search result whose registration name ends in a four-letter fragment opens with nothing: value pending, as-of not supplied, 0 accounts, and Holdings 'Unavailable / No source age yet / NOT_READY / Contact support'. Establish whether client names are truncated (and by what limit), and never offer a client that cannot open.

> "there is an account, [client] ... that looks strongly like a truncation. I want to clarify there are not character limits on these names or how we are handling character limits on these names ... when you click to that user or that client ... there is no information of any kind for that user. This looks like a truncation issue to me" (`main_walk_transcript.txt` [65.0]-[101.4])

**Screenshots.**

- `main_1.png` -- CONFIRMED: The search list offers the 49F result under an IRA registration.
- `main_4.png` -- CONFIRMED: Selected, WHO reads the name plus '****8387 / IRA' and '49financial -- Client' (raw firm slug, where search shows '49 Financial'); HOW MUCH 'value pending', AS OF 'not supplied', OVER WHAT '0 accounts'; Holdings 'Unavailable No source age yet NOT_READY' with 'Contact support'.

**Measured / current state.** Not measured: whether the name is truncated at the source, in the directory, or not at all (the fragment may be a real registration word). Measured on the screenshot: the directory offers a client whose scope resolves to zero accounts.

**Absorbs walk findings:** UIC-09. **Supersedes:** nothing. **Owners:** 2.0.0_SA_COO~P, 2.0.0_SA_COO~M.

**Acceptance.** The directory's name for every client matches the custodian's full registration name (a stated rule if any limit exists); every client the search offers opens with its accounts and value, or says in one plain sentence why it cannot; WHO shows the name only and the firm's display name ('49 Financial').

### AD-13 [P1] Main: Remove 'About this scope' and the extra identity fields

**Direction.** The 'About this scope' dropdown and its fields go.

> "this dropdown about this scope, quote unquote, that is surely unnecessary. There's a lot of extra visual things going on with these dropdowns, fields that we really do not need. So I want that gone." (`main_walk_transcript.txt` [168.8]-[181.3])

**Screenshots.**

- `main_3.png` -- CONFIRMED: Identity with the collapsed 'ABOUT THIS SCOPE' line.
- `20260928T174953Z#005 (CRO walk)` -- CONFIRMED (walk): Expanded: Selection, Permitted accounts, 'Scope as of unknown', Directory as of, Scope match, 'Cohort (not asserted) supervision: withheld, advisory: withheld'.

**Measured / current state.** IdentityCard.tsx renders the panel; the walk found 'unknown' and 'withheld' in it on all three clients.

**Absorbs walk findings:** UIC-17, UIR-45. **Supersedes:** UIC-17's 'show a real date or omit the field'. **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** Identity shows WHO, HOW MUCH, AS OF and OVER WHAT only; no 'About this scope' control or its fields; one date format on the card.

### AD-14 [P0] Performance: A working performance report, and the dependency named

**Direction.** No manual walk has ever shown a functioning performance report. Name the dependency behind 'temporarily unavailable', and make Performance answer.

> "performance for this account is temporarily unavailable due to what appears to be an unavailable dependency. We want to establish what that is. We need to know why we are still not able to generate performance reports ... I have never in a single visual walk seen a functioning performance report." (`main_walk_transcript.txt` [121.8]-[140.3])

**Screenshots.**

- `main_2.png` -- CONFIRMED: COT two-account client, YTD: 'Performance for this account is temporarily unavailable right now...' with Details DEPENDENCY_UNAVAILABLE; picker 'YTD unavailable'.
- `performance_1.png` -- CONFIRMED: Both accounts in the picker read 'YTD unavailable'.

**Measured / current state.** The CRO walk (20260928T174953Z) measured the whole page: COT answered DEPENDENCY_UNAVAILABLE 53 times, INF OBJECT_NOT_COVERED 25 times, 49F PERFORMANCE_PARTIAL 10 times (one account computes a YTD with no benchmark and no values) and UNSUPPORTED_OPERATION 9 times (3Y and Since inception); a second 49F account answers -100.00% (NEW-01, cause measured by ~P in IRPT_BCKEND-S177). So no firm has a complete report on the page today, which agrees with Andrew.

**Absorbs walk findings:** NEW-01, UIC-06, UIC-07, UIC-04, UIC-05, UIC-03. **Supersedes:** nothing. **Owners:** 2.0.0_SA_COO~P, 2.0.0_SA_COO~D.

**Acceptance.** For at least one client of each firm (49F, COT, INF), YTD, 1Y, 3Y and Since inception each render a complete report (period return, benchmark, beginning and ending value, series) that the CVO grades correct; a window that cannot answer names its dependency in one plain sentence; the account picker's figure follows the period.

**Decision for the CTO.** The COT dependency behind DEPENDENCY_UNAVAILABLE is not named anywhere Andrew can read it: ~P to name it in the IRPT_BCKEND record before any fix.

### AD-15 [P2] All tabs: Principle: port what exists, show only what the user needs

**Direction.** Every surface is built from the estate's existing components (MDPF category card, HeroDialog, Positioning map and table, the colour registry); no card, dropdown, code or field is on the face unless the advisor needs it.

> "this should really be porting existing work. We should not be reinventing the wheel here. It should be calling or inheriting or something, what we've already done, so we can have some consistency between the pages." (`holdings_walk_transcript.txt` l.55-58)

> "this is really not very complicated, but there's a lot of information being displayed all over the place here. Nobody has any idea what it is, and it is not user-friendly." (`analysis_walk_transcript.txt` [349.6]-[357.8])

**Screenshots.**

- `holdings_4.png` -- CONFIRMED: System words on the face (HOLDINGS_READY, 'holdings nodes', 'partitions ... withheld').
- `analysis_3.png` -- CONFIRMED: Extraction codes on the face.

**Measured / current state.** The walk register carries the no-system-words set (UIC-03, UIC-09, UIC-14, UIW-0928-04) and the design-law set (UIR-40, UIR-45).

**Reuse (do not rebuild).** the components named in AD-01, AD-04, AD-05, AD-08

**Absorbs walk findings:** UIR-40. **Supersedes:** nothing. **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** Each Investor Reporting surface either reuses the named estate component or states why it cannot; no system code, hash or internal producer name reaches the face.

## Part III -- the walk findings not absorbed above (still owed)

| id | owner | grade | observed | acceptance |
|---|---|---|---|---|
| UIC-13 | 2.0.0_SA_COO~D | NOT_MET | For the COT eleven-account client, Over what shows 10 rows and cuts the eleventh in half; there is no 'show all'. | Every account is reachable from Over what (a 'show all' or a scroll affordance); no row is clipped. |
| UIR-23 | 2.0.0_SA_COO~M | NOT_MET | Holdings read as of 2026-09-22 on Monday 2026-09-28; the trading frontier (T-1) is Friday 2026-09-25, three trading days later. | Holdings read as of the last trading day (T-1), on a scheduled publication. |
| UIW-0928-06 | 2.0.0_SA_COO~P | NOT_MET | Moving the COT eleven-account client from Performance to Holdings, POST /selections answered HTTP 500 once and the page logged 'IrRequestError: investor-reporting selection-create failed'; the next POST answered 200 and the page recovered. | Selection create answers every valid scope; a transient failure retries without a page error. |

## Part IV -- crosswalk: every walk finding to its home

| walk id | home |
|---|---|
| UIC-03 | AD-14 |
| UIC-04 | AD-14 |
| UIC-05 | AD-14 |
| UIC-06 | AD-14 |
| UIC-07 | AD-14 |
| UIC-09 | AD-12 |
| NEW-01 | AD-14 |
| UIC-10 | AD-01 |
| UIC-11 | AD-01 |
| UIC-12 | AD-01 |
| UIC-13 | CARRIED |
| UIC-14 | AD-03 |
| UIC-15 | AD-04 |
| UIC-16 | AD-10 |
| UIR-34 | AD-01 |
| UIW-0928-05 | AD-04 |
| UIW-0928-01 | AD-01 |
| UIW-0928-02 | AD-01 |
| UIW-0928-03 | AD-01 |
| UIC-17 | AD-13 |
| UIW-0928-04 | AD-03 |
| UIR-26 | AD-10 |
| UIR-03 | AD-10 |
| UIR-23 | CARRIED |
| UIR-48 | AD-02 |
| UIR-50 | AD-05 |
| UIW-0928-06 | CARRIED |
| UIR-40 | AD-15 |
| UIR-45 | AD-13 |
| UIC-18 | AD-06 |
| UIC-19 | AD-06 |
| UIC-20 | AD-06 |
| UIC-21 | AD-06 |
| UIC-22 | AD-06 |
| UIC-23 | AD-09 |

## Part V -- decisions for the CTO (surfaced, not adjudicated)

- **AD-01:** C3 (one navy band per page): MDPF's fixture is a navy band and Identity already spends one. Andrew's word is 'exactly what you see right in that picture'. Record the departure (or retire the Identity band) rather than rendering the card light.
- **AD-05:** Andrew's transcript sets commodities = gold. The live registry (chartColors.ts:218) sets green900 under CTO 101649. Re-solve the IV-e-49/51 distance invariant around a gold commodities token and apply it in the shared registry so Positioning and IR move together.
- **AD-14:** The COT dependency behind DEPENDENCY_UNAVAILABLE is not named anywhere Andrew can read it: ~P to name it in the IRPT_BCKEND record before any fix.

## Part VI -- suggested order for ~D's closer-drive

1. AD-01 + AD-02 + AD-03: the Holdings rebuild, in one arc: the card with the L-1 level, then remove the extra panels. ~M supplies the Models / SMAs / Client nodes per account.
2. AD-04 + AD-05: port Positioning's map and table. The commodities colour waits on the CTO decision; the GLD class waits on ~M.
3. AD-06..AD-09: the Analysis three-page flow, the modals and the readable results (~Y owns the result content).
4. AD-10..AD-13: account labels (with ~M), search only, clients that open (with ~P/~M), remove About this scope.
5. AD-14 runs in parallel on ~P: name the COT dependency, then make each firm answer.

## Part VII -- what this does not claim

- Screenshot descriptions are this seat's reading of Andrew's images; the images themselves stay local.
- The main and analysis transcripts are machine transcriptions (local Whisper). Quotes are verbatim from those transcripts, with client names replaced by [client].
- 'Measured' lines cite code at portal DEV `28f5118c` plus ~D's working tree as read 2026-09-28 ~20:3xZ. Where a cause is inferred, it says so.
- Nothing behind a submit was exercised.

## Refs

- REGISTER `docs/briefs/irpt-master-guidance-findings-20260928.json`; walk register `docs/briefs/irpt-ui-remaining-findings-20260928.json`; walk brief `docs/briefs/irpt-ui-remaining-brief-20260928.md`
- Coverage: `python docs/briefs/irpt-ui-review-coverage-check.py --register docs/briefs/irpt-master-guidance-findings-20260928.json docs/briefs/irpt-master-guidance-brief-20260928.md`
