# DSGN_AMGTV1 task order -- `AV-r-2` -- THE TEAM-CASE ABSENCE NAMES THE GAP THE PAGE CAN SEE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-r-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~10</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 670f29e4 -- AC1 1 of 3, AC2 1 of 3 (FAIL as expected); AC3 3 of 3 (PASS). No scratch green arm was fed this round. Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's (the judgment criterion).
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AV-r-2` (round 3, decomposition v3; serves FWD-6, FWD-1 hop 6)

Round 2 renders the research team's case where served (`model.team_cases`), and otherwise one sentence: "The research team's
Base case is not in this pack yet." The CVO found that sentence FALSE on INTU's live walk (the pack has the case; the API had
not served the field yet). Ruled (the CVO's decision 1, round-2 analysis): the sentence names the gap the page can SEE. `vv-4`
now serves `team_cases` for 84 of 95 names.

Build, in the Recommendation window (`ThesisCardDetail` in `components/ThesisCards.tsx`, element `data-team-case="base"`) and the
Model tab's team Base (`tabs/ModelTab.tsx`, element `data-model-team-case="base"`) -- the team-case element ONLY, nothing else
in ModelTab (the Model header is AV-r-5's, after you, in your queue):
1. The payload carries NO `team_cases` field -> "The research team's Base case is not served on this page yet." Never "not in
   the pack".
2. The field is served and its base reads ABSENT -> the sentence says the case is not in the (research team's) pack, and the
   element carries the dossier's own served `reason` -- in its text or, since that reason is machine text, in a
   `data-team-case-reason` attribute on the element.
3. The base is SERVED -> the table as written, exactly as round 2 renders it (unchanged).

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
portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~10/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts` (the team-case types), `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-r-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/checks/team.cjs" window; echo "exit=$?"</invocation><expect>TEAM CASE GAP (window): 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-r-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/checks/team.cjs" model; echo "exit=$?"</invocation><expect>TEAM CASE GAP (model): 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-r-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/checks/bound.cjs" R2 drafting.harness.cjs:8 thesisLadder.harness.cjs:10 modelPattern.harness.cjs:12; echo "exit=$?"</invocation><expect>R2 BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-r-2" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on the served payloads and the bound (the page harnesses that load this
surface stay green at their base check counts). AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in
walk screenshots, never self-graded: on the walk INTU's Recommendation window and Model tab lead with the team's own case, and Valero's say in one true sentence that the team's pack does not include one (FWD-6). A fourth criterion, with its reason: the judgment is the only grade of the look, which no static check can see.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~10/DSGN_AMGTV1.TO-AV-r-2.the-team-case-gap-in-words.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 3 = the round-2 analysis's enrichment list @172d3d9600 section 4 (CTO msg 26551) + ruling @06d51bce50. Decomposition v3.
Base 670f29e4: AC1 1 of 3, AC2 1 of 3 (FAIL as expected); AC3 3 of 3 (PASS).

<status>pending</status>
<round>3</round>
<slot>~10</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
