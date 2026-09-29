# DSGN_AMGTV1 task order -- `AV-t-3` -- THE THESIS READS AS THREE CARDS UNDER THE CHART, AND THE RECOMMENDATION SAYS WHOSE VIEW IT IS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-t-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~3</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut -- AC1 reads 0 of 3 arms at the base and 3 of 3 on a scratch reference implementation; AC2 reads 0 of 8 at the base and 8 of 8 on it; AC3 reads 2 of 2 at the base with check floors 8 and 10 (a floor of 9 reads RED, so the floor bites). Blind spot, stated: static markup with the estate chrome stubbed; a window opening and the look are the walk's (AC4).
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AV-t-3` (round 1, the thread's hops 5-6)

On Security Analysis, a PM opens a name's Thesis tab (the thread's name is Valero, `VLO_US_Equity`). Today the tab is one long
panel: a recommendation highlight at the top, a description paragraph, the chart, then the full ladder of sections, each
sentence followed by a `<details>` "cites N passages" disclosure that prints the passage and its raw accession number. Andrew:
"too much text ... three solid cards (investment thesis, risks, recommendation) beneath the principal charts, each a modal,
not drop-downs"; "citations good but source unclear"; "how is the recommendation reached?".

Build:

1. **New file `portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx`** exports:
   - `ThesisCards` -- props `{ bundle }` (the Thesis bundle the tab already reads): three cards, in the order Investment
     thesis, Risks, Recommendation (`section_id` `investment_thesis`, `risks`, `recommendation`), each a `<button>` carrying
     `data-thesis-card="<section_id>"` with a short lead in an element carrying `data-thesis-card-lead` (e.g. the section
     label and how many points it makes, or its first sentence shortened on a word boundary). A section the bundle does not
     carry, or carries `absent`, still gets its card, leading with a plain-words line naming what is missing and which team
     fills it -- never a project code, serial or path. Clicking a card opens its window: the estate's `HeroDialog` from
     `@/ui/components/graphic/HeroGraphic` (props `open, onClose, eyebrow, title, subtitle?, icon?, meta?, children, footer?,
     size?`), body `ThesisCardDetail`, footer `DialogStamp` (same file; props `stamp, source`) with the drafting date and
     source in words. The pattern is the Philosophy page's card strip + HeroDialog
     (`portal/src/pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx:183-214`, `:220-292`), minus its hover
     shadow (DESIGN.md C11).
   - `ThesisCardDetail` -- props `{ sectionId: string; bundle }`, the window body: every sentence of that section, each in an
     element carrying `data-drafted-sentence="<position>"`, with its machine chip and its verdict face (`CheckFaceBadge`, as
     today), followed by each of its passages -- the passage text in an element carrying `data-thesis-passage="<evidence id>"`
     -- and, per passage, ONE citation line carrying `data-citation-document="<evidence id>"` that names the document IN WORDS:
     when the evidence's `source.accession` equals `bundle.drafting_provenance.accession`, the line reads the provenance's
     form and filing date (e.g. "Valero's 10-K, filed 2026-02-25"; the company's name may come only from the served
     identity, never typed); otherwise it reads that the passage comes from a filing this payload does not name. **No
     accession number, hash or storage path appears in visible text** (they may sit in a data attribute). Passages sit in the
     window's DOM whenever the window is rendered -- no `<details>` inside it either.
   - For `recommendation`, the window (and the card's lead) says **whose view it is**, in plain words, on an element carrying
     `data-recommendation-author="machine-draft"`: the text is a machine's draft from the company's filing, not the research
     team's recommendation, and the research team's own position is not in the pack yet (the words "research team" appear).
2. **In `portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx`**, the tab at rest (the SERVED branch) becomes: the header it
   has today (title, subtitle with drafting source and vintage -- but `thesisSubtitle` now names the filing in words, form
   and filing date, and no longer prints the accession number; its name and signature stay), the principal chart (`ThesisDriverChart`, or its empty card
   when the series is absent) inside an element carrying `data-thesis-principal-chart`, then `<ThesisCards bundle={...} />`,
   then the held-uncited footer line as today. The top recommendation highlight and the long ladder leave the face; the tab's
   face carries **no `<details>`** and no accession number. The company description, when it carries sentences, may stay as
   one summary line above the chart with no evidence disclosure on the face; its sentences and passages then render at the
   head of the Investment thesis window. `ceo_bio`, when it carries sentences, renders at the end of the Investment thesis
   window. Every drafted sentence of the bundle is reachable in exactly one window. The loading / nothing-drafted / INVALID
   states stay as they are. The three named exports stay, same signatures: `ThesisTab`, `heldUncitedLine`, `thesisSubtitle`.
3. **Re-scope the two page harnesses that walk the Thesis evidence** --
   `portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs` (8 checks at the base) and
   `portal/src/pages/SecurityAnalysis/__harness__/thesisLadder.harness.cjs` (10 checks at the base) -- so they walk what the
   PM now reaches: the tab's face plus each card's window body (`ThesisCardDetail`) rendered statically. **Keep every check's
   claim** (each machine sentence reaches the page paired, in order, with its verdict face and the passage text of every id it
   cites; no `title=` evidence carrier; the held-uncited line by basis; the light panel; the designed empty state); a check
   whose old anchor no longer exists is re-anchored, never dropped. Each keeps at least its base count of checks.

**The rule this cell must not break (C-PRESENTATION-ONLY):** the page derives nothing. It does not choose whose recommendation
a sentence is, rewrite a sentence, or invent a document name: the author line is fixed by the ruling above (the served
recommendation is a machine draft of the filing), and a document is named only from `drafting_provenance`.

**Design law (portal `DESIGN.md`, binding):** the Thesis panel is white with navy ink (C3); cards are white with the 1px
hairline, no shadow (C11); no translucent white (C5.8); the window body is HeroDialog's white reading body.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the four files in `<paths>` under `portal/` change. `ThesisDriverChart.tsx`, `CheckFaceBadge.tsx`, `types.ts`, every
   `src/ui/**` and `src/components/**` file, every other tab, page and harness: unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx
portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/thesisLadder.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~3/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts` (`DraftedSection`,
`DraftedSentence`, `DraftedEvidence`, `DraftingProvenance`), `portal/src/pages/SecurityAnalysis/components/ThesisDriverChart.tsx`,
`portal/src/pages/SecurityAnalysis/components/CheckFaceBadge.tsx`, `portal/src/ui/components/graphic/HeroGraphic.tsx`,
`portal/src/pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx`, `portal/DESIGN.md`, and the issuer's checks and
fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round1/` (never edit them; the Valero Thesis
bundle there is the served payload the checks render: 10-K filed 2026-02-25; 5 thesis, 3 risk, 5 recommendation sentences).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-t-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round1/checks/t-3.AC1.cjs"; echo "exit=$?"</invocation><expect>THESIS THREE CARDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-t-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round1/checks/t-3.AC2.cjs"; echo "exit=$?"</invocation><expect>THESIS CARD WINDOWS: 8 of 8 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-t-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round1/checks/bound.cjs" THESIS drafting.harness.cjs:8 thesisLadder.harness.cjs:10; echo "exit=$?"</invocation><expect>THESIS BOUND: 2 of 2 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-t-3" judgment="true"/>
</proof_of_spec>

AC1 is the face on Valero's served Thesis bundle (chart first, then the three cards in order with leads; no `<details>`; no
accession number in visible text; the check stubs the estate's `PanelHeader`, so the subtitle's own wording is AC4's to read on
the walk). AC2 is each card's window on the same bundle (every sentence and passage, every citation's document in
words, the Recommendation's author line) plus an arm where one passage comes from another filing. AC3 is the bound: the two
re-scoped Thesis harnesses read green with no fewer checks than at the base. A fourth criterion, with its reason: AC4 is
JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded -- three cards under
the chart, and the Recommendation window lets a PM say whose view it is and which document each citation comes from
(FWD-1 ACCEPT; C-ESTATE-FIXTURES; DESIGN.md C3, C11).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~3/DSGN_AMGTV1.TO-AV-t-3.the-thesis-reads-as-three-cards.proof_of_spec.json`.
Report once: what changed and where, how each re-scoped harness check was re-anchored (old anchor -> new), the AC1-AC3 output
lines, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 1 = THE THREAD (PRD v0.2 :159-176), hops 5-6, CTO msg 26416. Base 8fa7abde: AC1 FAIL (0 of 3), AC2
FAIL (0 of 8), AC3 PASS (2 of 2; floor control 9 RED). Scratch GREEN arm: AC1 3 of 3, AC2 8 of 8. Hop 6 cannot pass FWD-1
until AMGT_CORPUS serves the team's recommendation (C-ASKS row 5); this cell renders the served state with its reason (PRD
:171-173), and that route is round 2's first enrichment input.

<status>complete</status>
<round>1</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
