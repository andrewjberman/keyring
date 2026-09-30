# DSGN_AMGTV1 task order -- `AV-e-2` -- THE RECOMMENDATION LEADS WITH THE RESEARCH TEAM'S CASE WHERE IT IS SERVED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-e-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~4</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV f1a90a9b -- AC1 1 of 3, AC2 1 of 3 (FAIL as expected); AC3 2 of 2 (PASS). No scratch green arm was fed this round. Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's (the judgment criterion).
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AV-e-2` (round 2, decomposition v2; serves FWD-1 hop 6, FWD-6)

The Recommendation window (round 1) says honestly that the text is a machine's draft and the research team's own position
is not in the pack. The team's cases are now served on `/thesis` at `model.team_cases` = `{base, upside, downside}`, each
either `{status: "SERVED", table: <the pack's case table AS WRITTEN, e.g. {"EPS": {"2026E": "23.22", ...}, "Multiple": {...},
"Price": {...}, "Return": {...}}>, citation: {report_key, report_id, locator, passage}, currency: <may be null>,
currency_basis: <e.g. "not stated in the pack">, unit_as_written: <may be null>}` or `{status: "ABSENT", reason: <text>}`
(served in code by AMGT_RESAPP vv-2; live after its redeploy vv-4). Ruled by 1.0.0_SA_CTO~Z: where the team wrote a Base,
the page leads with it -- figure, multiple and pack citation, labelled as the team's; the rule's own value is a
"Historical-multiple reference", never "Base case" (the served label already says so). The team's unit is a symbol as
written (C-CASE-UNIT): print it with "as written in the team's pack", never beside the Price card as if in the listing's
currency, never converted; a null currency prints no currency at all.

Build, in `components/ThesisCards.tsx` (the Recommendation window body `ThesisCardDetail` and the card's lead):
1. Ahead of the machine draft, an element carrying `data-team-case="base"` and `data-team-case-state="SERVED"` shows the
   team's Base table as written (every value exactly as served), "as written in the team's pack", the words "research team",
   and the pack citation in words (the report's name from the served citation, e.g. "INTU research pack 4_21_2026", plus
   the passage) -- never the `report_key` path or the `report_id`. Upside and downside may follow the same way.
2. Where the team's Base is ABSENT or `team_cases` is missing from the payload: an element carrying `data-team-case="base"`
   and `data-team-case-state="ABSENT"` holding one plain sentence that names the research team and carries no figure.
3. The machine draft follows unchanged (its sentences, passages, citation lines and the machine-draft author line).
4. `types.ts`: type `model.team_cases` (the shape above) on the Thesis bundle's model block, optional.

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
portal/src/pages/SecurityAnalysis/types.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~4/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx`, `portal/src/pages/SecurityAnalysis/components/CheckFaceBadge.tsx`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-e-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/e-2.AC1.cjs"; echo "exit=$?"</invocation><expect>TEAM CASE LEADS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-e-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/e-2.AC2.cjs"; echo "exit=$?"</invocation><expect>TEAM CASE ABSENT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-e-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/bound.cjs" E2 drafting.harness.cjs:8 thesisLadder.harness.cjs:10; echo "exit=$?"</invocation><expect>E2 BOUND: 2 of 2 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-e-2" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on the served payloads and the bound (the page harnesses that load this
surface stay green at their base check counts). AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in
walk screenshots, never self-graded: on INTU the Recommendation window leads with the team's case, labelled the team's and 'as written in the team's pack', and on Valero it says in one sentence that the team's case is not in the pack (FWD-6; C-CASE-UNIT). A fourth criterion, with its reason: the judgment is the only grade of the look, which no static check can see.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~4/DSGN_AMGTV1.TO-AV-e-2.the-recommendation-leads-with-the-teams-case.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 2 = the round-1 analysis's enrichment list @80dc63c5d2 section 5 (CTO msg 26481). Decomposition v2.
Base f1a90a9b: AC1 1 of 3, AC2 1 of 3 (FAIL as expected); AC3 2 of 2 (PASS).

<status>complete</status>
<round>2</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
