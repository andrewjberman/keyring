# DSGN_AMGTV1 task order -- `AV-r-5` -- THE MODEL HEADER WHITE, NO UNSERVED DOLLAR, AND THE CHART CAPTION IN WORDS (BATCH, LAST)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-r-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~10</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 670f29e4 -- AC1 1 estate band header, AC2 2 of 3 (FAIL as expected); AC3 3 of 3 (PASS). No scratch green arm was fed this round. Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's (the judgment criterion).
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AV-r-5` (round 3, decomposition v3; serves FWD-11, FWD-4)

Three remaining items, one batch cell that runs after AV-r-2 in your queue (it re-touches ModelTab.tsx):
1. The Model panel header is a second dark band: make it white with navy ink, carrying `data-model-panel-header` (the Thesis
   tab's `ThesisPanelHeader` is the pattern; no estate `PanelHeader`). Change nothing else in ModelTab (AV-r-2's team-case
   element stays as you left it).
2. `formatStatValue` in `components/StatTile.tsx` still prints "$<amount>" when called with no currency argument (the legacy
   path); make that path read "<amount> currency not stated", like a null currency. A served code still prints first
   ("EUR 382.86"); non-money formats are unchanged. Served prose that carries "$" (a drafted sentence) is never rewritten.
3. The Thesis chart's caption, when a chart is served, names its line in words, not its mnemonic (`components/ThesisDriverChart.tsx`;
   the mnemonic may ride a data attribute). No served fixture carries a chart, so the walk grades this item.

**Your worktree first:** this order follows AV-r-2 in your queue. Before you edit, bring your worktree to AV-r-2's work: `git -C <your worktree> merge --no-edit CLOUD` (the outer repository, which carries AV-r-2 once the issuer drains it) and `git -C <your worktree>/portal merge --no-edit DEV` (the portal DEV carrying AV-r-2). Both are merges, never a rebase. If either stops on a conflict, abort it and file a BLOCKING row.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state
naming, in plain words, what is missing and which team fills it -- never a project code, serial or storage path.
C-ESTATE-FIXTURES -- windows are the estate's HeroDialog + DialogStamp, panels and states are the estate's; nothing forked.
**Design law (portal `DESIGN.md`):** white panels with navy ink (C3); ONE dark band per page; no translucent white (C5.8); no
shadow (C11). A code or path may sit in a data attribute or in code, never in visible text.

**If a bound harness check is anchored on the raw text this cell removes,** re-anchor that ONE check onto the same fact as the
page now states it (the words, or a data attribute), keep its claim, never drop it; the harness keeps at least its base
check count (the floor in the bound criterion). Record each re-anchor (old anchor -> new) in the instance.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` under `portal/` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/components/StatTile.tsx
portal/src/pages/SecurityAnalysis/components/ThesisDriverChart.tsx
portal/src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~10/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx` (ThesisPanelHeader), `portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-r-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/checks/band.cjs" model; echo "exit=$?"</invocation><expect>MODEL PANEL HEADER: estate band headers=0, white header=yes -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-r-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/checks/money.cjs"; echo "exit=$?"</invocation><expect>NO UNSERVED DOLLAR: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-r-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/checks/bound.cjs" R5 modelPattern.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>R5 BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-r-5" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on the served payloads and the bound (the page harnesses that load this
surface stay green at their base check counts). AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in
walk screenshots, never self-graded: the Model tab adds no second band, no money reads in a form the page was not served, and a served chart's caption reads in words (FWD-11, FWD-4). A fourth criterion, with its reason: the judgment is the only grade of the look, which no static check can see.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~10/DSGN_AMGTV1.TO-AV-r-5.the-last-band-money-and-caption.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 3 = the round-2 analysis's enrichment list @172d3d9600 section 4 (CTO msg 26551) + ruling @06d51bce50. Decomposition v3.
Base 670f29e4: AC1 1 estate band header, AC2 2 of 3 (FAIL as expected); AC3 3 of 3 (PASS).

<status>complete</status>
<round>3</round>
<slot>~10</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
