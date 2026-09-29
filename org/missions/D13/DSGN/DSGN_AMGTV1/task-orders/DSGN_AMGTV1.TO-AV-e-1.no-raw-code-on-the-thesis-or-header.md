# DSGN_AMGTV1 task order -- `AV-e-1` -- NO RAW CODE ON THE THESIS PANEL OR THE HEADER, AND ONE BAND

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-e-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~5</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV f1a90a9b -- AC1 5 hits, AC2 1 hit (FAIL as expected); AC3 4 of 4 (PASS). No scratch green arm was fed this round. Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's (the judgment criterion).
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AV-e-1` (round 2, decomposition v2; serves FWD-11)

The Thesis tab and the security header still print system text a PM cannot read. On Valero's served bundle the Thesis
face reads (among others) the held-uncited line "Claims held uncited: not carried on this drafted document
(held_uncited_basis ABSENT_ON_OBJECT) -- no count is shown, because none was measured", the chart card's absent reason
("... INTERFACE F-1 carries its segments as cited prose ... held_uncited 0 vs points 0 ..."), and the header's description
source line "from bloomberg CIE_DES". The Thesis panel's header is also a second dark band (the header above it is the
page's one band).

Build:
1. `ThesisTab.tsx` / `ThesisDriverChart.tsx`: the chart card's absent reason and the held-uncited footer line say the same
   facts as plain sentences (e.g. "The driver's series is not in the model data yet." / "The drafted document does not say
   how many claims were held back uncited."), and the Thesis panel's header is not a dark band (a white panel header with
   navy ink, built from the estate's pieces in these files). `heldUncitedLine` and `thesisSubtitle` keep their names and
   signatures; their words may change.
2. `HeaderBrief.tsx`: the description's source line names its source in words (e.g. "Company description from Bloomberg"),
   never the field code.
3. `drafting.harness.cjs` recomputes the held-uncited line and `thesisLadder.harness.cjs` walks the Thesis face: bring them to
   the new words, claims kept.

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
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/components/ThesisDriverChart.tsx
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/thesisLadder.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~5/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx`, `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-e-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/raw.cjs" thesis; echo "exit=$?"</invocation><expect>THESIS RAW CODE: 0 hit(s) -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-e-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/raw.cjs" header; echo "exit=$?"</invocation><expect>HEADER RAW CODE: 0 hit(s) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-e-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/bound.cjs" E1 drafting.harness.cjs:8 thesisLadder.harness.cjs:10 tabs.harness.cjs:20 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>E1 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-e-1" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on the served payloads and the bound (the page harnesses that load this
surface stay green at their base check counts). AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in
walk screenshots, never self-graded: the Thesis panel and the header read as plain sentences with one dark band on the page (DESIGN.md C3; FWD-11). A fourth criterion, with its reason: the judgment is the only grade of the look, which no static check can see.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~5/DSGN_AMGTV1.TO-AV-e-1.no-raw-code-on-the-thesis-or-header.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 2 = the round-1 analysis's enrichment list @80dc63c5d2 section 5 (CTO msg 26481). Decomposition v2.
Base f1a90a9b: AC1 5 hits, AC2 1 hit (FAIL as expected); AC3 4 of 4 (PASS).

<status>pending</status>
<round>2</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
