# Investor Reporting -- manual walk 2 guidance brief, 2026-09-29

**Mode:** midstream on DSGN_IRPTV1 (with IRPT_BCKEND rows). **By:** 4.0.0_SA_CRO on Andrew's word (terminal, 2026-09-29 ~18:1xZ): "analyze [the walk] in tandem with the reference images ... first transcribe the audio, using openai-whisper ... an additional /ui-walk of the mentioned IRPT page and underlying tabs and functions ... synthesized into a new brief, which I will review with you and ultimately approve to issue to CTO and COO~D."
**Relay: RELAYED to 1.0.0_SA_CTO on Andrew's word (terminal, 2026-09-29 ~19:4xZ: "send to CTO and have them assess state with COO~D and they can handle how to thread this into their workflow").** **Register (the source of every item here):** `docs/briefs/irpt-manual-walk-v2-findings-20260929.json`.
**Inputs:** Andrew's second manual walk -- one recording (12 min 20 s, transcribed locally with openai-whisper large-v3-turbo on CPU, no network; `tmp/ui-guidance/20260929/`, gitignored) and 17 screenshots (`C:\Users\AndrewBerman\Pictures\Screenshots\irpt_manual_walk_v2`) -- plus this seat's deep `/ui-walk --periods-per-account` of the same client on the local build (`tmp/ui-walk/20260929T190228Z/`, portal working copy 3e2233de92, dev-live), the 09-28 master guidance register (AD-01..15) and the 35 carried walk findings.
**Placed elsewhere today, not re-opened here:** the CTO's placement of one canonical per-security table (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20260929_182xZ_ONE_CANONICAL_SECURITY_TABLE.md`): (a)+(b) Investor Reporting's producer onto `etf-classifications` with the PHYS row (IRPT_BCKEND ~M), (c) the retirement project (this seat's L1 brief `docs/briefs/canonical-security-table-brief-20260929.md`), (d) the portal half (~D). Five of Andrew's holdings points land there (W2-12, W2-13, W2-14 and the O7/O8 outcomes).

## Part 0 -- what Andrew asked for, in one screen

- **Performance:** the account picker is fixed; the COT dependency refusal is a backend gap, not the front end -- name it and make it answer (W2-01).
- **Analysis:** the Client / Prospect step gets the hero-card fixture (W2-02); the prospect modal gets real buttons and a proceed / decline pair (W2-03); a comparison is resolved and NAMED before it is added (W2-04); picking a card drops straight into the model / ETF picker as the modal's second page, and the loose input box goes (W2-05); a request opens where the advisor is looking and says what to change (W2-06); Generate leads somewhere visible (W2-07).
- **Holdings:** the card's pie takes an ordinal brand-hex scale (W2-08); the drill's bar aggregates to asset classes (W2-09); the smaller-holdings rule is stated and the group is 'Various' (W2-10); the aggregate table has one row per security with the prorated weight (W2-11); 'Other' rows are missing canonical rows, kept current by a scheduled path (W2-12); single securities read sector and industry, are marked as such and follow the ETFs (W2-13); Alternatives come from the canonical table with no new suite (W2-14); Positioning's Holdings Breakdown is ported as-is (W2-15).
- **This seat's additions:** five observations from the screenshots (W2-16..W2-20) and two from the walk (W2-21 one-slice card at account scope; W2-22 three scope controls on one tab).

Priorities: P0 5, P1 13, P2 4. **Corroboration:** every one of Andrew's fifteen points cites his screenshot(s), read and described in words; every walk check hit kept was confirmed on its screenshot; W2-16 is PARTIAL (viewport-dependent).

## Part I -- what moved since the 09-28 brief (read on the page today)

- **AD-10 met** on the walked client: each account's own tail on Identity, both pickers and Analysis (performance_1, shot 005). **AD-13 met:** 'About this scope' is gone. **AD-08 landing:** the VARIANT cards open the canonical modal with 'Select this analysis' (shot 051). **AD-07 progress:** the prospect modal exists (analysis_3). **AD-01 progress:** the accounts sit inside the canonical card as L-1 (holdings_1) -- still labelled 'Rebalancer strategy' (AD-02 NOT MET, W2-20).
- **Still owed from 09-28:** UIC-05 (picker 'pending'), UIC-14 (producer name in the footer), UIC-15 (ticker repeated in the name), UIC-18 (card and count disagree -- now explained in words, not removed), UIR-40 (bands: 3 on the empty page, 5 on Holdings), UIW-0928-05.
- **Stop-work note:** nothing here re-opens the canonical-table placement; W2-12..W2-14 cite it and add acceptance on the page only.

## Part II -- Andrew's direction, corroborated (W2-01..W2-15), then this seat's observations (W2-16..W2-22)

### W2-01 [P0] Performance: COT performance still answers a dependency refusal; the account picker is fixed

**Direction.** Name the upstream the COT performance answer depends on and make it answer; until then the refusal stays a named one. The picker's per-account tails are right now.

> "So as we can see from the initial drop down, we fixed the account recognition issue. That's great. However, there's still an unavailable dependency on the drop down ... we need to assess whether the back end agent is working on the port or the adapter, if that is a data breakage or if it's a front end adapter issue." (transcript l.2-5 [11-40 s])

**Screenshots.**

- `performance_1.png` -- CONFIRMED: The picker lists each of the client's two accounts with its own tail and type and a value; both options still end in 'YTD pending' (UIC-05). Below the presets, a refusal panel reads 'Performance for this account is temporarily unavailable right now. It becomes available again once the upstream data source Opal Capital relies on for this account answers', with the raw code DEPENDENCY_UNAVAILABLE under Details.

**Measured / current state.** [measured] The refusal is the adapter's own named answer for COT: ~D's BEFORE read for the r3 window (ledger org/critical_paths/change_management/20260929T1223Z_irpt-adapter-holdings-gold-49f-r3-20260929_deploy_completion.md, D1) reads a COT account as DEPENDENCY_UNAVAILABLE with business date 2026-09-22, and the same after the r3 apply (UNCHANGED). The page renders that refusal as designed; nothing in the front end adapter is broken on this path. [inferred] The upstream is the COT performance source the adapter reads today, whose latest business day is 2026-09-22 (five trading days behind Monday's T-1). The CTO's placement of 2026-09-29 orders the COT holdings-basis re-point (row S173) after the canonical-table cells (a)+(b); until it lands, COT performance has no answering source.

**Reuse (do not rebuild).** The 49F holdings-basis adapter path (r3, live since 16:40Z today) is the pattern the COT re-point follows.

**Absorbs:** UIC-05, AD-14. **Owners:** IRPT_BCKEND (2.0.0_SA_COO~M for the COT re-point, S173), 2.0.0_SA_COO~D (the picker's 'pending' word, UIC-05).

**Acceptance.** A COT account answers a YTD figure on the Performance tab from the holdings basis, or its refusal names the upstream day that is missing; the picker option carries no 'pending' after the figure renders.

**Decision for the CTO.** None new: S173's order is placed. Confirm that AD-14 ('a working performance report, and the dependency named') closes on S173 for COT.

### W2-02 [P1] Analysis: Portfolio step: give the Client / Prospect choice the hero-card fixture the estate already has

**Direction.** The two cards are plain rectangles. Use the shared hero-card fixture (the VARIANT cards of the analysis-type step; the Philosophy page's cards) so the first step reads like the second.

> "the initial bifurcation between client and prospect cards. This is fine, but we can jazz this up a little bit because we're lacking ... a lot of the fixture design that we brought in with the philosophy UI, the philosophy UI cards. So this is an opportunity to bring in some of those shared fixtures and preexisting components." (transcript l.7-10 [48-70 s])

**Screenshots.**

- `analysis_1.png` -- CONFIRMED: 'Select the portfolio' over two white boxes: 'Client -- Choose a client in the search above to analyze their portfolio' greyed, and 'Prospect -- Upload a prospect's holdings to analyze a portfolio not yet at Opal'. No band, no icon, no selected state.
- `analysis_4.png` -- CONFIRMED: The analysis-type step already uses the hero-card fixture: three VARIANT cards with a navy band, an icon and a SELECTED state.

**Measured / current state.** [measured] GenerateComposer.tsx:315-319 renders the type step through VariantCards; the portfolio step (page 1 of the AD-06 flow) is a different component without the fixture.

**Reuse (do not rebuild).** VariantCards (GenerateComposer.tsx:316) -- the same fixture, two cards; portal/src/ui/components/graphic/HeroGraphic.tsx (the canonical card)

**Absorbs:** AD-06 (page 1 of the three-page flow), AD-08 (cards show which one is selected). **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** The Client and Prospect choices are two hero cards of the same fixture as the analysis-type step, with a selected state; the disabled Client card says in words why it is disabled.

### W2-03 [P1] Analysis: Prospect upload modal: the template is a button, and the file choice ends in a proceed / decline pair

**Direction.** 'Download the template' becomes an indigo button from the button library; the native 'Choose File / No file chosen' becomes a chooser with two footer actions, proceed (blue) bottom-right and decline (red) bottom-left, once a file is chosen.

> "the underscored download template should be a expanded UI components, probably Indigo. There's a lot of existing button component architecture that we can source for this segment ... If these are intended to be hyperlinks in the bottom left, then we need to review a more cogent structure for that. I would suggest something on the bottom left and bottom right, probably blue or red. If there's going to be proceeding or declining on the basis of that file." (transcript l.16-21 [96-133 s])

**Screenshots.**

- `analysis_3.png` -- CONFIRMED: The modal 'Upload a prospect's holdings' has the band, the rules as five bullets, an underlined 'Download the template (holdings-template.csv)' link, then 'Choose the holdings file' over a native 'Choose File  No file chosen' control. No footer, no primary action, no cancel.

**Measured / current state.** [measured] AD-07's modal exists (progress on the 09-28 brief); its actions are a text link and a native file input.

**Reuse (do not rebuild).** The button library (one #5F3BE3 primary per view, C8) and the panel footer slot (PanelFooter) already on the Holdings panels.

**Absorbs:** AD-07. **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** The template is a button; after a file is chosen the modal footer shows a primary 'Use this file' bottom-right and a 'Cancel' bottom-left; no native file-input text is on the face.

### W2-04 [P0] Analysis: Comparison entries are never resolved or named: the list reads 'Comparison 1', 'Comparison 2'

**Direction.** Resolve what the advisor typed BEFORE it is added -- an Opal model against the catalog, an ETF against the estate's security master -- and show the resolved name in the list; refuse an unresolved entry in words.

> "when a comparison is selected, there's no recognition of whether a ticker, whether an Opal model or a third party ETF or symbol is actually matched successfully. That needs to be clarified and not only visually displayed, but on the engineering side confirmed prior to being able to add it. I recommend some kind of ticker lookup system." (transcript l.23-29 [136-181 s])

**Screenshots.**

- `analysis_4.png` -- CONFIRMED: 'Compare with an Opal model (2 of 5)' over '1. Comparison 1 remove / 2. Comparison 2 remove', then the input 'Opal model or ETF symbol' and Add. Neither entry says what it is.

**Measured / current state.** [measured] GenerateComposer.tsx:321-339 prints 'Comparison {index + 1}' by design ('the opaque catalog key is carried as data ... never printed as text'); composer.ts:187-204 addComparison refuses only the cap of five and a duplicate -- no existence check; composer.ts:31-35: 'the vendor's typed security ids are resolved SERVER-SIDE'. A mistyped symbol therefore reaches submission and fails at the producer.

**Reuse (do not rebuild).** The Opal model catalog the page already resolves against server-side; DynamoDB etf-classifications (the canonical security table: ticker -> name, class, sub-asset) for ETFs and single securities -- no external lookup needed for anything the estate already holds

**Absorbs:** UIC-21 (the cut placeholder goes with the input). **Owners:** 2.0.0_SA_COO~D (the resolve-before-add and the named row), IRPT_BCKEND (a resolve endpoint if the catalog read is not already served to the page).

**Acceptance.** After Add, the list row reads the resolved name (an Opal model's name, or an ETF's name with its ticker); an entry that resolves to nothing is refused at Add with words and never reaches Generate.

**Decision for the CTO.** Andrew's 'ticker lookups without authentication' is an external call. The estate's own canonical security table already carries the name per ticker; place the lookup on it, and only an instrument it lacks would need egress (Andrew's per-use word).

### W2-05 [P1] Analysis: One flow for comparisons: the card opens the picker, and the loose input box goes

**Direction.** Choosing Comparison or Multi-Comp takes the advisor straight into picking Opal models (a clear dropdown of presets) or entering an ETF, as the modal's second page; the card pick and the comparison count are one input, not two that can disagree.

> "There shouldn't be a need to select one of these cards and then on top of that have to add symbols ... There should be one smooth flow, not kind of a card sequence, and then this input box. Really, if you select comparison, it should immediately drop you into picking out an Opal model with a clear dropdown. I would recommend a second page to the modal." (transcript l.37-42 [227-272 s])

**Screenshots.**

- `analysis_5.png` -- CONFIRMED: Multi-Comp card marked SELECTED while the page reads 'Variant Overview (0 comparisons)' and the refusal 'Add at least two Opal models to compare against.' The card and the count disagree on the same screen.

**Measured / current state.** [measured] composer.ts:71-90: the variant is DERIVED from the comparison count (0 Overview, 1 Comparison, 2-5 Multi-Comp); the card pick is a second input (variantChoice) that the count can contradict, which is the UIC-18 shape the words now explain but do not remove.

**Reuse (do not rebuild).** The canonical HeroDialog modal (HeroGraphic.tsx) for the second page; The Opal model catalog for the preset dropdown

**Absorbs:** UIC-18. **Supersedes:** The separate 'Opal model or ETF symbol' input + Add under the cards. **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** Picking Comparison opens a picker for one Opal model or ETF; picking Multi-Comp opens the same picker for two to five; the variant label can never contradict the card; there is no input box outside the picker.

### W2-06 [P1] Analysis: Your analysis requests: 'Open' lands below a long list and a needs-attention request says only its code

**Direction.** Opening a request shows it in the canonical modal (or scrolls to it), newest first in the list; a needs-attention request says in words what to change and offers the one action. The id stays behind Technical details.

> "there's a lot of inexplicable request IDs and strings. If you try to proceed through any of these hyperlinks, particularly the unavailable ones or needs attention, there is no modal popup. These request execution IDs go nowhere as far as I can tell ... assess whether this is a backend data gap or if it is a frontend adapter gap." (transcript l.44-48 [276-305 s])

**Screenshots.**

- `analysis_6.png` -- CONFIRMED: Thirteen rows '<client> requested <date> Open <status>' in no date order (27th, 29th, 26th, 28th ...); statuses 'Unavailable -- needs attention. Open it to see what to change.', 'Loading -- Running -- in progress', 'Ready'. Below: 'Job status: Unavailable', Technical details 'Request REQ-2119def...' and 'ANALYSIS_REQUIRES_ATTENTION', a 'Check status' button, and 'Report sections are not available. Reopen this request to check again.' Nothing says what to change.

**Measured / current state.** [measured] OwnedRequestHistory.tsx:279-283: Open sets the selected id and renders ProspectJobStatus plus the sections INLINE at :292-302, below the whole list -- no modal, no scroll; the row's promise 'Open it to see what to change' is composed at :110 for every non-READY/LOADING state. Reason words are one mapping, ANALYSIS_REQUIRES_ATTENTION -> 'needs attention' (:84-86). The request id prints only inside Technical details (AD-09 met there). [inferred] The correction itself is not on the wire the page reads: the producer marks a job NEEDS_CORRECTION with a job_detail code (this seat's W22/W24 halves: RESOLVE_RETRY_EXHAUSTED under the S206 concurrency cause), and the page's status read carries the public code only. Half front end (where Open lands, the order, the verb), half backend (the words to show).

**Reuse (do not rebuild).** HeroDialog for the opened request; ProspectJobStatus (already renders the status words)

**Absorbs:** AD-09 (residue), UIC-23 (landed: rows in words). **Owners:** 2.0.0_SA_COO~D (open-in-modal or scroll, newest-first order), IRPT_BCKEND (~P/~Y: the correction words on the status wire).

**Acceptance.** Rows are newest first; Open shows the request where the advisor is looking; a needs-attention request reads what to change in a sentence and the one action (re-submit, replace the file, or wait), with the id and code behind Technical details.

**Decision for the CTO.** Which seat owns the correction words on the wire: the resident's job_detail already carries a code; the CTO names whether the words are minted by the producer (IRPT_BCKEND) or mapped by the page (DSGN_IRPTV1).

### W2-07 [P1] Analysis: Generate submits, but the page shows only a one-line state beside the button and the list needs a manual refresh

**Direction.** After Generate, take the advisor to the request's own status (progress in words, then the report); the request list updates itself.

> "The generate function here currently does not do anything. So we need to assess if that is on COO tilde D task order list, if that has been preceded, or if it is scoped, or if that is just a missing hole there." (transcript l.50-52 [308-325 s])

**Screenshots.**

- `analysis_7.png` -- CONFIRMED: Output step filled (a test title, prepared for an internal test recipient); to the right of Generate a small grey line 'Needs attention -- areq-f7048d4e' -- a job submitted from this browser, already in the needs-attention state.
- `analysis_2.png` -- CONFIRMED: Before any press the same slot reads 'No job submitted from this browser yet.'

**Measured / current state.** [measured] GenerateComposer.tsx:286-298 onGenerate -> submitComposition -> setJob; :555-562 the only feedback is the job-state line (label, reason code, request id) beside the button. The history list (OwnedRequestHistory.tsx:264-265) refreshes on 'Refresh request list' or page load only. So the press did submit (areq-f7048d4e exists); what is missing is a visible journey: no navigation, no progress surface, no automatic list update. Not on the 09-28 brief: AD-09 covers what a result says, not what happens after the press. [measured] The submitted job went to needs-attention -- the same producer state W2-06 opens; its cause is the backend's (W2-06 inferred claim).

**Reuse (do not rebuild).** ProspectJobStatus (the prospect flow already polls one request's status in words)

**Owners:** 2.0.0_SA_COO~D (the post-press journey), IRPT_BCKEND (why this job needs attention).

**Acceptance.** Pressing Generate opens the request's status view with progress in words, and the report when READY; 'Your analysis requests' shows the new row without a manual refresh.

### W2-08 [P1] Holdings: The card's accounts pie is grey on grey: use an ordinal brand-hex scale

**Direction.** Colour the L-1 (accounts) slices by an ordinal scale anchored to Opal brand hexes -- starting light (a light blue) and scaling through blue variants, not indigo -- one canonical ramp reused wherever N unnamed-class slices are drawn.

> "the pie chart that displays on the left of the card. We need a standard ordinal method for how we display these colors. Gray is not going to be enough. I recommend using opal brand guidelines, canonical hexes, potentially starting with some of the lighter colors, perhaps like a light blue ... Probably stay away from indigo, maybe make these blue scaling variants." (transcript l.54-60 [331-366 s])

**Screenshots.**

- `holdings_1.png` -- CONFIRMED: The canonical All Categories card now holds Total Assets, a two-slice pie in two greys, and two account tiles with values and shares. The tiles read 'Rebalancer strategy: <client> ****9238 / ****9237' -- the L-1 level is the accounts (AD-01 progress), still labelled as a strategy (AD-02 not met; W2-20).

**Measured / current state.** [measured] Progress on AD-01: the accounts sit inside the card as L-1. The slice fills were not read in code by this seat; the screenshot shows two greys.

**Reuse (do not rebuild).** portal/src/lib/chartColors.ts (PALETTE, the brand blues) -- one ordinal ramp exported once

**Absorbs:** UIC-11 (narrow grey ramp), UIC-10 (labels: an ordinal ramp with a legend replaces slice labels). **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** With 2, 4 and 11 accounts the slices are distinguishable and legend-labelled from one exported ramp; no slice is grey unless it is the 'Various' remainder.

**Decision for the CTO.** The ramp's length: COT clients reach eleven accounts. Name the rule for N above the ramp (group the tail as 'Various', or extend the ramp), so the same ramp serves the map's legend and the drill bars.

### W2-09 [P1] Holdings: The drill modal's top bar is one sliver per security; aggregate it to the asset classes

**Direction.** The allocation bar at the top of the account / model drill is a few-segment horizontal bar by asset class (Cash, Fixed Income, Equity, Alternatives -- Positioning's order and colours), not one divider per security or sleeve.

> "the initial bar that displays the asset allocation breakdowns by color is very staggered. This needs to be aggregated into those classes ... not have all of these vertical dividers for the various underlying securities or sleeves. This should be a clean several unit horizontal bar." (transcript l.62-66 [376-411 s])

**Screenshots.**

- `holdings_2.png` -- CONFIRMED: The 'Rebalancer strategy' drill: a thin bar of roughly forty green / blue / orange slivers with white dividers, then 'Opal Conservative Growth' and its sixteen constituents with coloured dots and amounts.

**Measured / current state.** [inferred] The bar is drawn per constituent in the drill's own component (DrillTree.tsx's dialog); not read line-by-line by this seat.

**Reuse (do not rebuild).** Positioning's asset-class bar and colours (lib/chartColors ASSET_CLASS); the MDPF HeroDialog's colour bar (mdpf_3 in the 09-28 brief)

**Owners:** 2.0.0_SA_COO~D.

**Acceptance.** The drill's bar has one segment per asset class present, in canonical order and colour, with a legend; no per-security dividers.

### W2-10 [P1] Holdings: Securities map: say the smaller-holdings rule, keep it one rule, and call the group 'Various'

**Direction.** State the grouping rule on the face and in the tooltip; the group's label and its tooltip 'asset class' read 'Various', never 'Smaller holdings' as a class.

> "What is the basis for delineating to smaller holdings? Is it an absolute count? Is it a prorated rate? ... there should be a consistent rule across all sleeves in the securities map component. And with that in mind, for the asset class listing in the tooltip, smaller holdings should be changed to various." (transcript l.76-81 [453-499 s])

**Screenshots.**

- `holdings_4.png` -- CONFIRMED: Map filtered to one model; a purple tooltip 'Smaller holdings - Smaller holdings (3 securities) / Weight 1.41% / Asset Class Smaller holdings' over a grey tile.
- `holdings_3.png` -- CONFIRMED: All securities: a grey 'Smaller holdings 15.2%' tile at the right; legend 'Fixed Income, Equity, Alternatives, Smaller holdings'.

**Measured / current state.** [measured] HoldingsTreemap.tsx:174-176 SMALL_TILE_SHARE_THRESHOLD = 0.02 -- a leaf below 2% of the DISPLAYED set's own total weight is grouped. It is a prorated rate relative to the current chip, so the rule already holds across sleeves; :171 OTHER_TILE_LABEL = 'Smaller holdings', :173 fill slate400, and the group's internal bucket is assetClass 'Other' (:76), which is why the tooltip prints it as an asset class.

**Reuse (do not rebuild).** The existing threshold; only the words and the tooltip's class line move

**Owners:** 2.0.0_SA_COO~D.

**Acceptance.** The grouped tile reads 'Various (n securities under 2% each)'; the tooltip's asset class reads 'Various'; the legend entry reads 'Various'; a footnote states the 2% rule; the same rule applies under every chip.

### W2-11 [P0] Holdings: Aggregate securities table: one row per security with the prorated collective weight, not one row per account and sleeve

**Direction.** With Account All and Sleeve All, a ticker appears once; its weight is the sum of its instances' shares of the client total and its value the sum of their values. Rows are monotonic, never additive duplicates. Choosing one account or sleeve shows that scope's own rows.

> "As you can see, there are five rows of cash holdings. There is no need for there to be five in an aggregate view. Those should be aggregated to one row with the collective weight as a function of the percentage that occupies on a prorated basis of that given sleeve and account combination. This also applies to all other asset classes anywhere where a keyed asset rows identified. Those should be monotonic. They should not be additive rows." (transcript l.85-90 [516-548 s])

**Screenshots.**

- `holdings_5.png` -- CONFIRMED: Sleeve All / Account All: five Cash rows (CASH x4, FCASH), then CLIP three times and JPST three times among the Ultra Short Duration rows, each with its own weight and value.
- `holdings_6.png` -- CONFIRMED: JAAA four times, USHY twice, DIVZ / PFDE / SPYM repeated under Equity Large.
- `holdings_7.png` -- CONFIRMED: IDVZ, VEA, IEMG, VUG each twice.

**Measured / current state.** [measured] The securities table lists the snapshot's security nodes, one per sleeve instance (SecurityList.tsx; the map already sums instances per model chip via nodeRefs, HoldingsTreemap.tsx:60-69 and splitCount :161-163), so the map aggregates and the table does not.

**Reuse (do not rebuild).** HoldingsTreemap.tsx's per-identity aggregation (accountGroupsFrom / splitCount) -- the same fold for the table

**Absorbs:** UIW-0928-05 (dozens of constituents at 0.00%), UIC-15 (the ticker repeated in the name column). **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** Under Account All and Sleeve All each ticker has one row whose weight equals the sum of its instances' weights (to the displayed precision) and whose value equals the sum; the name column does not repeat the ticker; under one account or sleeve the rows are that scope's.

### W2-12 [P0] Holdings: Sub-asset 'Other' rows come from the canonical table, and new securities get rows continuously

**Direction.** Every 'Other' sub-asset on the tab is a missing canonical row, not a display choice. Add the rows in the canonical table (an ad hoc classification run as the QA run) and keep them current with a scheduled path that classifies securities as they appear day over day.

> "Any rows that, as you can see, list with other in the sub-asset class, we will need to add a new row in that canonical table and draw from that canonical table. So if that requires a rerun of any open AI classification logic ... we will need to not only run an ad hoc run, but also likely structure a continuous pipeline as new securities become apparent in day-over-day draws." (transcript l.94-96 [564-609 s])

**Screenshots.**

- `holdings_6.png` -- CONFIRMED: Fixed Income rows with sub-asset 'Other' (USHY) drawn as near-black cells beside the green class cells.
- `holdings_7.png` -- CONFIRMED: Equity 'Other' for VUG and for every single stock (PM, VZ, UNH, MPLX, JNJ, CVX, MSFT ...).

**Measured / current state.** [measured] Placed today: the CTO's cell (a) moves Investor Reporting's producer from bd-securities to etf-classifications; this seat's L1 brief (docs/briefs/canonical-security-table-brief-20260929.md) carries the continuous path as O7 and the ad hoc backfill as its QA run.

**Reuse (do not rebuild).** etf-classifications, its seed source and client (see the L1 brief)

**Owners:** 2.0.0_SA_COO~M (cell (a)), the new canonical-table project (O7).

**Acceptance.** No ETF row on the Holdings tab reads 'Other' where the canonical table holds a sub-asset; a ticker new to a day's holdings has its row after the scheduled run, and the QA backfill is not the acceptance evidence.

**Decision for the CTO.** Whether the classification of a new ticker calls a vendor model (Andrew's 'open AI classification logic') -- per-use word at the PRD, never a pipeline default.

### W2-13 [P0] Holdings: Single securities: sector and industry from the canonical table, marked as single securities, ordered after the ETFs

**Direction.** A single stock reads its sector and industry (the canonical table has them), carries an instrument-type mark (ETF or single security) from the canonical row, and sits after the last ETF class in the table so the sub-asset colour gradient is reused, not re-invented.

> "The other category, which is being used liberally here for the individual securities, we have already tracked the sub-asset class and even industry class for those securities. This is also contained within that positioning table ... individual securities should be marked as such. That likely should be a field in that DynamoDB table ... individual securities are always secondary ... And that is then we can reuse the same gradient logic with regard to the sub-asset taxonomy." (transcript l.99-105 [620-687 s])

**Screenshots.**

- `holdings_7.png` -- CONFIRMED: Fourteen single stocks as Equity / Other.
- `ref_1.png` -- CONFIRMED: Positioning's Holdings Breakdown: Equity rows read Consumer Discretionary, Information Technology, Financials with industry sub-lines, coloured by sub-asset.

**Measured / current state.** [measured] ~D's record @099316efdd: SecurityList.tsx:149 calls getSubAssetClass(ticker, undefined), discarding the served sub-asset, so GLD / PHYS / VXX and the single stocks fall to 'Other'. The CTO placed the order ('single stocks after the last ETF class') as the portal half (d); the instrument-type FIELD is O8 of this seat's L1 brief.

**Reuse (do not rebuild).** portal/src/components/holdings/HoldingsBreakdownTable.tsx (Positioning's table, sub-asset gradient); etf-classifications (sector, sub-asset per ticker)

**Absorbs:** AD-04 (partly). **Owners:** 2.0.0_SA_COO~D (placement (d)), the new canonical-table project (O8).

**Acceptance.** A single stock row reads its sector and industry from the canonical row; single stocks are listed after the last ETF class; their colours follow the sub-asset gradient; no row reads 'Other' for a ticker whose canonical row has a sub-asset.

### W2-14 [P1] Holdings: Alternatives and the map's classes come from the canonical table; no new suite

**Direction.** GLD and PHYS are Commodities / Metals, VXX is Structured / Hedge, on the map and in the table, read from the canonical table Positioning reads. Nothing new is built for it.

> "we do need to make sure that the canonical positioning table that holds all of our labeled securities, that should be a shared utility for this function. This should not be a duplicative effort. There should be no new resources created ... So we already have it in positioning." (transcript l.69-74 [425-449 s])

> "The alternatives here, I already covered this with group D. This needs to be running through that same table for the purpose of maintaining a unified taxonomy." (transcript l.107-108 [690-704 s])

**Screenshots.**

- `holdings_3.png` -- CONFIRMED: All-securities map: PHYS in orange (Alternatives); legend Fixed Income / Equity / Alternatives / Smaller holdings.
- `holdings_8.png` -- CONFIRMED: Alternatives / Other: PHYS twice, GLD twice, VXX twice; the footer reads 'Source: holdings_snapshot.build_cot.' (UIC-14 still not met).

**Measured / current state.** [measured] Placed today as cells (a)+(b) under halves (served figures move) before the COT re-point S173; the portal half (d) stops discarding the served sub-asset.

**Reuse (do not rebuild).** etf-classifications and its client; Positioning's ASSET_CLASS colours (commodities gold, structured its own hue)

**Absorbs:** AD-05 (superseded by the placement), UIC-14 (the source line -- still owed). **Owners:** 2.0.0_SA_COO~M (cells (a)+(b)), 2.0.0_SA_COO~D (portal half (d); the source line).

**Acceptance.** After cell (a) and the portal half, GLD and PHYS read Commodities / Metals and VXX Structured / Hedge on the map, the table and the drill, in Positioning's colours; the footer names no producer function.

### W2-15 [P1] Holdings: Port Positioning's Holdings Breakdown to every Investor Reporting holdings view

**Direction.** The securities table on Investor Reporting is Positioning's Holdings Breakdown (asset class, sub-asset with industry sub-line, ticker, name, weight, class total rows), used as-is.

> "This is a reference for the purpose of visually depicting that taxonomy. As you can see in the holdings breakdown, we've already covered the not only sub-asset class but industry. So clearly, it should be a very short hop to link this function for all investor reporting application views." (transcript l.110-112 [714-738 s])

**Screenshots.**

- `ref_1.png` -- CONFIRMED: Positioning's HOLDINGS BREAKDOWN: dark header, BASIC INFO group, ASSET CLASS / SUB ASSET / TICKER / NAME / WEIGHT, class-coloured cells with lighter sub-asset tints, a FIXED INCOME TOTAL row.
- `holdings_5.png` -- CONFIRMED: Investor Reporting's SECURITIES table has the same columns plus VALUE and the Sleeve / Account filters, but no class total rows, no industry sub-line, and the duplicates of W2-11.

**Measured / current state.** [measured] The component exists: portal/src/components/holdings/HoldingsBreakdownTable.tsx (named in ~D's census as carrying its own ticker map at :69,129 -- that map is a copy the canonical-table project retires).

**Reuse (do not rebuild).** HoldingsBreakdownTable.tsx

**Absorbs:** AD-04. **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** Investor Reporting's securities table is the Positioning component with the class total rows and industry sub-lines, fed by the canonical classes; the Sleeve / Account filters and the VALUE column are its only additions.

### W2-16 [P2 (PARTIAL: viewport-dependent)] Analysis: CRO observation: the 'Next' button is clipped at the right edge of the analysis-type step

**Direction.** The step's footer must fit the panel; no control is cut by the viewport.

**Screenshots.**

- `analysis_4.png` -- CONFIRMED: Bottom-right 'Nex' with the button's right edge outside the capture; 'Back' bottom-left is whole.

**Measured / current state.** [measured] Not reproduced at the walk's 1440 px viewport (shot 052: Back and Next whole); clipped in Andrew's narrower capture. A responsive-layout check for the step footer, not a fixed defect.

**Owners:** 2.0.0_SA_COO~D.

**Acceptance.** Back and Next are whole at the walk's viewport and the page does not scroll sideways.

### W2-17 [P2] Analysis: CRO observation: Output step wording -- 'Client: the client selected above', a title input narrower than its own placeholder

**Direction.** Name the client on the Output step; size the title input to its placeholder; do not repeat the title under the input.

**Screenshots.**

- `analysis_2.png` -- CONFIRMED: 'Client: the client selected above'; the title input shows '<client> -- Multi-C' cut, and the same title in full as a helper line beneath. (UIC-19 improved: the title names the client, not one account.)

**Measured / current state.** [measured] GenerateComposer.tsx:500-511: the placeholder is the derived title and a helper paragraph prints it again; the client label falls back to 'the selected client' when the header row is absent (:270).

**Absorbs:** UIC-19 (residue). **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** The Output step names the client; the title input shows the whole derived title; the helper line is dropped or says only that the title can be overridden.

### W2-18 [P2] Analysis: CRO observation: request rows in no date order; 'Loading — Running -- in progress' mixes two dashes in one phrase

**Direction.** Newest first; one dash convention on the row; a LOADING row reads 'Running' once.

**Screenshots.**

- `analysis_6.png` -- CONFIRMED: Dates run 27th 10:14a, 29th 1:26p, 26th 8:12p, 28th 11:32p ...; two rows read 'Loading — Running -- in progress'.

**Measured / current state.** [measured] OwnedRequestHistory.tsx:105-110 composes label + ' — ' + note, and the producer's note for LOADING is 'Running -- in progress', so the row carries both an em dash and a double hyphen; the page renders the served order.

**Absorbs:** W2-06 (ordering). **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** Rows newest first; a LOADING row reads 'Running' and nothing twice; one dash convention.

### W2-19 [P2] Holdings: CRO observation: the securities footer names a producer function

**Direction.** The source line names the data source in words, never a module or function name.

**Screenshots.**

- `holdings_8.png` -- CONFIRMED: 'September 28th, 2026, 5:00p ET | Source: holdings_snapshot.build_cot.'

**Measured / current state.** [measured] UIC-14 carried NOT MET from the 09-28 register; the map's footer above reads 'Source: Opal Capital Analysis.' so the two footers on one tab disagree.

**Absorbs:** UIC-14. **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** Every footer on the tab reads the same source words; no module or function name on the face.

### W2-20 [P1] Holdings: CRO observation: the card's L-1 tiles are the accounts but read 'Rebalancer strategy: <client> ****9238'

**Direction.** An account tile reads the account's own tail and type ('****9238 / Trust'); 'Rebalancer strategy' is not a level of the taxonomy (AD-02).

**Screenshots.**

- `holdings_1.png` -- CONFIRMED: Two tiles 'Rebalancer strategy: <client> ****9238' and '****9237' with values and '57% / 43% of total'.
- `holdings_3.png` -- CONFIRMED: The map's chips repeat it: 'Model: Rebalancer strategy: <client> *9238' beside real models.

**Measured / current state.** [measured] AD-02 carried NOT MET; the 09-28 brief's measured state (DrillTree.tsx feeding one card per top-level category the snapshot names) still holds for the label.

**Reuse (do not rebuild).** slices.ts#maskedLabelFor (the one masked-label rule)

**Absorbs:** AD-02. **Owners:** 2.0.0_SA_COO~D, IRPT_BCKEND (if the snapshot names the category).

**Acceptance.** L-1 tiles and map chips read the account's tail and type; L0 reads Models / SMAs / Client; the words 'Rebalancer strategy' appear nowhere on the tab.

### W2-21 [P1] Holdings: Walk finding: at one-account scope the card is a one-slice pie and a single '100% of total' tile

**Direction.** When the page picker holds one account, the canonical card opens at L0 (Models / SMAs / Client) for that account; a level with one member is not drawn.

**Screenshots.**

- `tmp/ui-walk/20260929T190228Z/shots/030-...-holdings-Account-9237-Brokerage.png` -- CONFIRMED: One grey disc with a single divider line, one tile '100% of total'.

**Measured / current state.** [measured] Walk check chart:single-slice (UIW-20260929T190228Z-010) on shots 029 and 030; the same shape UIR-34 recorded for the INF drill in the 09-28 register (a level with one child drawn as a one-slice pie).

**Reuse (do not rebuild).** CategoryViewTree (the MDPF fixture) already renders L0 directly

**Absorbs:** UIR-34. **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** With one account selected the card shows Models / SMAs / Client tiles for that account and no accounts pie; a level with one member is skipped at every depth.

### W2-22 [P1] Holdings: Walk finding: three scope controls on one tab (page picker, map chips, table selects) that do not follow each other

**Direction.** One selection drives the tab: the card's current selection (AD-01) scopes the map and the table; the table's own Sleeve / Account selects and the map's chip rows collapse into that one selection or read it back.

**Screenshots.**

- `tmp/ui-walk/20260929T190228Z/shots/042-...-holdings-press-Model-DIVZ-SMA.png` -- CONFIRMED: Page picker: one account. Map chip: 'Model: DIVZ SMA' (its single stocks). Table Sleeve: 'Opal Ultra Short-Term Income'. Three scopes on one screen.

**Measured / current state.** [measured] HoldingsTab.tsx composes AccountFilter, HoldingsTreemap (its own chips: HoldingsTreemap.tsx accountGroupsFrom / modelOptionsFrom) and SecurityList (its own selects) as siblings (09-28 brief, AD-01 measured state); nothing binds the three.

**Reuse (do not rebuild).** The card's selection state (AD-01's component 1) as the single source

**Absorbs:** AD-01 (the 'updates from whatever is selected' clause). **Supersedes:** The table's separate Sleeve / Account selects; The map's per-account chip rows. **Owners:** 2.0.0_SA_COO~D.

**Acceptance.** Choosing a tile, a model or an account in the card re-scopes the map and the table in one step; no second selector on the tab can show a different scope than the card.

## Part III -- the walk delta (this seat's deep walk, read shot by shot)

Walk `20260929T190228Z`: DONE 19:02:34-19:06:03Z; 3.6 min; 54 screenshots; 21 unique findings from 122 observations; 0 guard aborts; 24 API answers not READY (all DEPENDENCY_UNAVAILABLE on performance); 3 console errors (two login 401 probes, one hydration whitespace warning on Holdings); account DISARMED and a login with the walk password REFUSED (401). Coverage: Investor Reporting for the walked client: search, identity expand, Performance (both accounts x YTD/1Y/3Y/Since inception via --periods-per-account, then the deep presses incl. Refresh), Holdings (page picker All/each account; the securities table's Sleeve and Account selects; every map chip pressed; the card tile opened), Analysis (Client card, the three VARIANT cards, Add, Back, Refresh request list). Generate, Export and the file chooser are never pressed (write guard).

| id | maps to | read | what the screenshot shows |
|---|---|---|---|
| WD-01 | W2-01 | CONFIRMED | Every performance read on the page answered DEPENDENCY_UNAVAILABLE: 24 of 24 API answers, both accounts, all four presets and the deep presses (shots 009-026). The refusal panel and the raw code under Details are on every one. No COT figure exists on the page at any period. |
| WD-02 | W2-08 | CONFIRMED | The card's pie draws two slices in one colour (#94a3b8 twice) at All accounts (shot 027). |
| WD-03 | W2-21 | CONFIRMED | With one account chosen in the page picker, the card draws a ONE-slice pie and one tile reading '100% of total' (shot 030, shot 029 likewise). At account scope the L-1 level has one member and adds a layer; the card should open at L0 (Models / SMAs / Client) for that account. |
| WD-04 | W2-22 | CONFIRMED (this seat's read, not a check hit) | Three scope controls on one tab do not follow each other: the page's Account picker, the map's chips (one row per account, one chip per model), and the securities table's own Sleeve and Account selects. Shot 042: the page picker reads one account, the map chip reads 'Model: DIVZ SMA', the table's Sleeve reads 'Opal Ultra Short-Term Income' -- three scopes on one screen. AD-01 says the map and the table follow the card's selection. |
| WD-05 | W2-19 | CONFIRMED | Two source footers disagree on one tab: the card's reads 'Source: Opal Capital Analysis.' and the map's and table's read 'Source: holdings_snapshot.build_cot.' (shots 027, 030, 042). |
| WD-06 | W2-10 | CONFIRMED | The map's tile labels are the share of the CLIENT total (0.2%-0.4% per single stock under the DIVZ SMA chip, shot 042) while the grouping rule is the share of the DISPLAYED set (none of those tiles is grouped although each is under 2% of the client). Two bases on one map; the stated rule must say which. |
| WD-07 | W2-09 | CONFIRMED | The opened tile's dialog (shot 039) carries the sliver bar Andrew flagged, over the SMA's single stocks listed with blue dots; the dialog's text is what the contrast check flags (24 elements) on the band gradient. |
| WD-08 | W2-16 | NOT REPRODUCED at 1440 px | Back and Next are whole at the walk's viewport (shot 052); Andrew's capture (analysis_4) clips Next at a narrower window. Viewport-dependent: a responsive check, not a fixed defect. W2-16 is downgraded to PARTIAL. |
| WD-09 | W2-05 | CONFIRMED (progress) | Pressing a VARIANT card opens the canonical HeroDialog -- 'Multi-Comp: WHAT IT IS / WHAT IT NEEDS: Two to 5 comparisons ... each an Opal model, or an external ETF by its symbol' with a 'Select this analysis' action (shot 051). AD-08 is landing; the comparisons picker Andrew asks for is this modal's second page. |
| WD-10 | W2-06 | CONFIRMED | Eleven of thirteen request rows still read 'Checking status...' after the page's settle (shot 052): the list's per-row status reads are in flight one by one. Two rows read 'Unavailable -- needs attention. Open it to see what to change.' (the check's unconnected-field hit) and one 'Loading -- Running -- in progress'. |
| WD-11 | AD-13 | CONFIRMED (progress) | Identity shows WHO / HOW MUCH / AS OF / OVER WHAT and nothing else; 'About this scope' is gone (shot 005). AD-13 is met on this client; AD-10 is met on it too (each account's own tail on Identity, the pickers and Analysis). |
| WD-12 | carried | CARRIED | Known classes, not re-litigated: the empty page's 'Illustrative sample' block (3 bands on the empty page, 5 on Holdings -- UIR-40, C3); the contrast heuristic on tile text over the band gradient and on the dialog (7 hits); ellipsized names in the securities table and the map (6 truncated-label hits -- W2-15's port removes the ticker-in-name that causes most of them). |

Dropped as false positives: none -- every kept hit is above; the contrast and truncation hits are carried classes, not new findings.

## Part IV -- crosswalk to the 09-28 registers

| prior id | this brief |
|---|---|
| AD-01 | progress (accounts inside the card as L-1: holdings_1); W2-08, W2-20 |
| AD-02 | NOT MET; W2-20 |
| AD-04 | W2-15, W2-13 |
| AD-05 | superseded by the CTO placement of 2026-09-29 (one canonical table); W2-14 |
| AD-06 | W2-02, W2-05 |
| AD-07 | progress (the modal exists); W2-03 |
| AD-08 | W2-02, W2-05 |
| AD-09 | W2-06 (residue) |
| AD-10 | MET on the two-account COT client (performance_1); the 49F / INF re-check is the walk's |
| AD-14 | W2-01 |
| UIC-05 | W2-01 |
| UIC-10 | W2-08 |
| UIC-11 | W2-08 |
| UIC-14 | W2-19 |
| UIC-15 | W2-11 |
| UIC-18 | W2-05 |
| UIC-19 | improved; W2-17 |
| UIC-21 | W2-04 |
| UIC-23 | landed; W2-06 |
| UIW-0928-05 | W2-11 |
| UIR-34 | W2-21 |
| UIR-40 | carried (walk: 3 bands empty page, 5 on Holdings) |
| AD-13 | MET on the walked client (shot 005) |

## Part V -- what this brief does not claim

- It did not read the Holdings card's slice fills or the drill bar's component line by line (W2-08, W2-09 are inferred on the code side; confirmed on the screen).
- It did not name the COT performance upstream beyond what the served refusal and ~D's read carry (W2-01: the producer's identity is IRPT_BCKEND's to name).
- It did not verify whether the correction words for a needs-attention request exist anywhere on the wire (W2-06 inferred: the page reads a code only).
- The walk covered one COT client at one viewport; the 49F and INF re-checks of AD-10 and the eleven-account COT client are not in it.
- Generate, Export and the prospect file chooser were never pressed (write guard), so W2-07 rests on the code path and Andrew's screenshot, not on a press.
- It does not decompose or sequence; owners are named, not ordered.

## Refs to carry

```
  BRIEF PATH        docs/briefs/irpt-manual-walk-v2-brief-20260929.md
  REGISTER          docs/briefs/irpt-manual-walk-v2-findings-20260929.json
  PROJECT           DSGN_IRPTV1 (front end, 2.0.0_SA_COO~D); IRPT_BCKEND (W2-01, W2-06/07 wire, W2-12/14 cells (a)+(b))
  EXISTING PRD      org/missions/D9/DSGN/DSGN_IRPTV1/prd/ (the master guidance brief's addendum carries AD-01..15)
  SIBLING           the canonical-security-table project (L1 brief docs/briefs/canonical-security-table-brief-20260929.md)
  PRIOR ART         VariantCards + HeroDialog (analysis cards and modal); CategoryViewTree (MDPF card); HoldingsBreakdownTable.tsx (Positioning);
                    HoldingsTreemap.tsx per-identity aggregation; ProspectJobStatus; chartColors.ts PALETTE
  MEASURED AT       transcript 18:20-18:53Z; screenshots 17:2x-17:40Z (Andrew); walk 19:02-19:06Z; code reads 19:0x-19:1xZ, portal 3e2233de92
  RELAY             HELD -- to 1.0.0_SA_CTO and 2.0.0_SA_COO~D on Andrew's word only
```
