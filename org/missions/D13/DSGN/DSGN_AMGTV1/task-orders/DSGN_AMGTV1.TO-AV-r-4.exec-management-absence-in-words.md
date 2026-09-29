# DSGN_AMGTV1 task order -- `AV-r-4` -- EXEC MANAGEMENT'S ABSENCE READS AS A SENTENCE SAYING WHERE THE LIST WAS LOOKED FOR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-r-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~12</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 670f29e4 -- AC1 2 of 3 (FAIL as expected); AC2 2 of 2 (PASS). No scratch green arm was fed this round. Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's (the judgment criterion).
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AV-r-4` (round 3, decomposition v3; serves FWD-7)

On INTU (management ABSENT, absent_because ZERO_OFFICERS) the Exec Management tab reads "Exec Management: ABSENT
(ZERO_OFFICERS). no declared shape read this section (4 usable line(s), 0 candidate(s)): neither a narrative entry per officer
nor a Name/Age/Position ..." plus field names (roster_status, roster_reason, source_item, source_accession) and "crosswalk/v1".

Build, in `tabs/ExecManagementTab.tsx`: the absence reads as one or two plain sentences naming the officers and where the list
was looked for (e.g. "No officer list is in this name's pack yet: the company's 10-K had no officer section this page could
read, and no other source was used."), with no code, field name or status word on the face; the served state stays in
`data-exec-status` / `data-exec-absent-because`, and any detail a PM may want sits behind a collapsed details affordance.
The identity line's "crosswalk/v1" is AV-r-1's (IdentityLine.tsx), not yours; the exec check excludes nothing, so if that
string is the only hit left, say so in your report rather than editing IdentityLine.

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
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/execPattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~12/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/src/pages/SecurityAnalysis/components/IdentityLine.tsx`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-r-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/checks/exec.cjs"; echo "exit=$?"</invocation><expect>EXEC ABSENCE IN WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-r-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/checks/bound.cjs" R4 execPattern.harness.cjs:9 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>R4 BOUND: 2 of 2 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-r-4" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on the served payloads and the bound (the page harnesses that load this
surface stay green at their base check counts). AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in
walk screenshots, never self-graded: the Exec Management tab reads its absence in words and says where the list came from (FWD-7).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~12/DSGN_AMGTV1.TO-AV-r-4.exec-management-absence-in-words.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 3 = the round-2 analysis's enrichment list @172d3d9600 section 4 (CTO msg 26551) + ruling @06d51bce50. Decomposition v3.
Base 670f29e4: AC1 2 of 3 (FAIL as expected); AC2 2 of 2 (PASS).

<status>pending</status>
<round>3</round>
<slot>~12</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
