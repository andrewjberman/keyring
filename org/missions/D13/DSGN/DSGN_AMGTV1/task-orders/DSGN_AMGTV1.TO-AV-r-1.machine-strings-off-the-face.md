# DSGN_AMGTV1 task order -- `AV-r-1` -- EVERY MACHINE STRING THE CVO NAMED OFF THE FACE, AND THE POSTURE HEADER WHITE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-r-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~9</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 670f29e4 -- AC1 14 hits, AC2 1 estate band header (FAIL as expected); AC3 6 of 6 (PASS). No scratch green arm was fed this round. Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's (the judgment criterion).
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AV-r-1` (round 3, decomposition v3; serves FWD-11, FWD-2, FWD-10)

The CVO's round-2 judgment found machine text still on the face after round 2 (ADJUDICATION_v3): "(S13)" (the header feed's
social line), "crosswalk/v1" (the identity line on the Thesis, Model, Exec and Posture tabs), "generation: none -- no committed
pointer for this date" (the header's axis footnote), the lead panel's source line ("Source: generation 20260926T110728Z-... |
state COMPLETE | ... coverage vintage bloomberg-dapi-boxside-pull:... (blp_client 127.0.0.1:8194, live)"), "WMB_US_Equity" and
"claude-opus-5" (the Posture comparable and snapshot lines), and "BLOOMBERG SESSION: NOT REPORTED" (the header badge). The
Posture panel header is also a second dark band.

Build:
1. Each of those strings reads in words a PM can use, or sits behind a details affordance the PM opens on purpose (a collapsed
   `<details>`), never on the face: e.g. the lead source line becomes "Ranked 2026-09-25 from Bloomberg prices (32 names)" with
   the generation id and client in a details block; the identity line drops "crosswalk/v1"; the session badge says nothing
   when the session is not reported (its state stays in `data-bloomberg-session`); the Posture comparable reads its company
   name or "a comparable the research team has not identified"; the snapshot line names the machine in words ("drafted by a
   machine on 2026-09-16"). A code, id, path or model name may ride a data attribute.
2. The Posture panel header is white with navy ink, carrying `data-posture-panel-header` (the Thesis tab's `ThesisPanelHeader`
   is the pattern; it uses no estate `PanelHeader`).
3. If a bound harness check is anchored on a string this cell removes, re-anchor that one check (see below).
The inverted census (`round3/checks/census.cjs`, the CVO's instrument) prints every non-prose token left; read it before you
report, and name in your report any token you left on purpose and why.

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
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/components/IdentityLine.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/postureCites.ts
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/shell.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/posturePattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~9/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx` (ThesisPanelHeader, the white-header pattern), `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-r-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/checks/named.cjs"; echo "exit=$?"</invocation><expect>NAMED MACHINE STRINGS: 0 hit(s) over 4 surfaces -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-r-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/checks/band.cjs" posture; echo "exit=$?"</invocation><expect>POSTURE PANEL HEADER: estate band headers=0, white header=yes -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-r-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/checks/bound.cjs" R1 tabs.harness.cjs:20 shell.harness.cjs:10 errorEmpty.harness.cjs:12 leadPanelPattern.harness.cjs:15 posture.harness.cjs:32 posturePattern.harness.cjs:13; echo "exit=$?"</invocation><expect>R1 BOUND: 6 of 6 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-r-1" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on the served payloads and the bound (the page harnesses that load this
surface stay green at their base check counts). AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in
walk screenshots, never self-graded: on the walk the header, lead panel, Thesis identity line and Posture tab carry no machine text on the face and the Posture tab adds no second band; the inverted census's remaining tokens are judged one by one (FWD-11, FWD-2, FWD-10). A fourth criterion, with its reason: the judgment is the only grade of the look, which no static check can see.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~9/DSGN_AMGTV1.TO-AV-r-1.machine-strings-off-the-face.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 3 = the round-2 analysis's enrichment list @172d3d9600 section 4 (CTO msg 26551) + ruling @06d51bce50. Decomposition v3.
Base 670f29e4: AC1 14 hits, AC2 1 estate band header (FAIL as expected); AC3 6 of 6 (PASS).

<status>complete</status>
<round>3</round>
<slot>~9</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
