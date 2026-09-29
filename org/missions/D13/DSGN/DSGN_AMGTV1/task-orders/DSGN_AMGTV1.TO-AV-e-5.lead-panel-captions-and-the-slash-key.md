# DSGN_AMGTV1 task order -- `AV-e-5` -- THE LEAD PANEL'S CAPTIONS IN WORDS, AND NO SLASH IN A TICKER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-e-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~7</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV f1a90a9b -- AC1 3 hits + ResolutionNote not exported, AC2 1 of 3 (FAIL as expected); AC3 3 of 3 (PASS). No scratch green arm was fed this round. Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's (the judgment criterion).
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AV-e-5` (round 2, decomposition v2; serves FWD-2)

The lead panel prints partition names on its face: the footer's "Served by the producer partition TRENDING_PRICE (movement
dimension: MEASURED)", and RankedList's empty states ("No committed ranking for BREAKOUT_CHATTER on this date."). Two
Bloomberg tickers are served with a literal slash ("BP/ LN", "NG/ LN") and print it.

Build:
1. `components/LeadPanel.tsx`: the resolution note says which list is shown in words (e.g. "Showing today's Trending x Price
   list"), never the partition name; export it as the named export `ResolutionNote` (same props as today). The source
   caption (`sourceFooterContent`, `sourceDisclosureText`) and `components/GenerationCaption.tsx` stay free of raw codes.
2. `components/RankedList.tsx`: the empty/absent states name the list in words, never the partition name; a ticker's literal
   "/" never reaches the face -- "BP/ LN" reads "BP LN", on the lead and on the secondary ticker line. The click still sends
   `row.security_key`; row order, the star and every other row are unchanged.

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
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/components/RankedList.tsx
portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~7/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/src/pages/SecurityAnalysis/constants.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-e-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/e-5.AC1.cjs"; echo "exit=$?"</invocation><expect>LEAD CAPTIONS RAW CODE: 0 hit(s) -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-e-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/e-5.AC2.cjs"; echo "exit=$?"</invocation><expect>SLASH KEY: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-e-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/bound.cjs" E5 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>E5 BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-e-5" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on the served payloads and the bound (the page harnesses that load this
surface stay green at their base check counts). AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in
walk screenshots, never self-graded: the lead panel's captions and states read in words and every ticker reads without a slash (FWD-2). A fourth criterion, with its reason: the judgment is the only grade of the look, which no static check can see.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~7/DSGN_AMGTV1.TO-AV-e-5.lead-panel-captions-and-the-slash-key.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 2 = the round-1 analysis's enrichment list @80dc63c5d2 section 5 (CTO msg 26481). Decomposition v2.
Base f1a90a9b: AC1 3 hits + ResolutionNote not exported, AC2 1 of 3 (FAIL as expected); AC3 3 of 3 (PASS).

<status>pending</status>
<round>2</round>
<slot>~7</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
