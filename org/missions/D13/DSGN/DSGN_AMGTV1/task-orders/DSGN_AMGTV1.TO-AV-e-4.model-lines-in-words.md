# DSGN_AMGTV1 task order -- `AV-e-4` -- MODEL LINES NAMED IN WORDS, EACH MISSING LINE SAYS WHY, AND THE TEAM'S BASE LEADS THE CASES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-e-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~4</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV f1a90a9b -- AC1 64 hits, AC2 1 of 3 (FAIL as expected); AC3 2 of 2 (PASS). No scratch green arm was fed this round. Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's (the judgment criterion).
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AV-e-4` (round 2, decomposition v2; serves FWD-9, FWD-6)

The Model tab prints vendor mnemonics as line names (PX_LAST, SALES_REV_TURN, IS_OPER_INC ...) and each refused line as
machine text ("REFUSED -- REVENUE_PER_SH: unit/sign convention is 'NOT-YET-BUILT', not MEASURED"). On Valero: 37 lines
(`data-model-row`), 18 refused (`data-model-refused`). Andrew: "If that's just a back-end data issue, so be it. But if
that's a lack of front-end adapter ... handle in this project."

Build, in `tabs/ModelTab.tsx` and `modelSheet.ts`:
1. Every line is named in words (from the figure's served `basis.definition` or a label map in these files); the mnemonic may
   sit in a data attribute, never in visible text. No line is dropped (still 37 / 18 on Valero).
2. Every refused line carries `data-model-line-reason="DATA_MISSING"` (the served data is not there) or `"NOT_SHOWN_YET"`
   (the data is served but the page cannot yet show it, e.g. its unit convention is not built) and ONE plain sentence of at
   least five words saying which, with no mnemonic and no "NOT-YET-BUILT".
3. The team's Base leads the cases where served (1.0.0_SA_CTO~Z's Base-case anchor ruling): an element carrying
   `data-model-team-case="base"` BEFORE the rule's cases (`data-model-case`), showing the team's `model.team_cases.base`
   table as written with "as written in the team's pack" and labelled the research team's; the rule's case keeps its served
   label ("Historical-multiple reference"). Read the team-case types AV-e-2 added to `types.ts` (this order runs after it in
   your queue; your worktree carries AV-e-2 once you merge its branch -- see below).

**Your worktree first:** this order follows AV-e-2 in your queue. Before you edit, bring your worktree to AV-e-2's work: `git -C <your worktree> merge --no-edit CLOUD` (the outer repository, which carries AV-e-2 once the issuer drains it) and `git -C <your worktree>/portal merge --no-edit DEV` (the portal DEV carrying AV-e-2). Both are merges, never a rebase. If either stops on a conflict, abort it and file a BLOCKING row.

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
portal/src/pages/SecurityAnalysis/modelSheet.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~4/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts` (AV-e-2's team-case types), `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-e-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/raw.cjs" model; echo "exit=$?"</invocation><expect>MODEL RAW CODE: 0 hit(s) -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-e-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/e-4.AC2.cjs"; echo "exit=$?"</invocation><expect>MODEL LINES AND CASES: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-e-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/bound.cjs" E4 modelPattern.harness.cjs:12 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>E4 BOUND: 2 of 2 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-e-4" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on the served payloads and the bound (the page harnesses that load this
surface stay green at their base check counts). AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in
walk screenshots, never self-graded: the Model sheet reads in plain line names, each missing line says in one sentence whether the data is missing or the page cannot yet show it, and the team's Base leads the cases where served (FWD-9). A fourth criterion, with its reason: the judgment is the only grade of the look, which no static check can see.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~4/DSGN_AMGTV1.TO-AV-e-4.model-lines-in-words.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 2 = the round-1 analysis's enrichment list @80dc63c5d2 section 5 (CTO msg 26481). Decomposition v2.
Base f1a90a9b: AC1 64 hits, AC2 1 of 3 (FAIL as expected); AC3 2 of 2 (PASS).

<status>pending</status>
<round>2</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
