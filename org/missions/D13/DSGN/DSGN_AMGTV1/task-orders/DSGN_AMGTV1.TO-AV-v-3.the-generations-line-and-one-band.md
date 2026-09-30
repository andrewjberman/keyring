# DSGN_AMGTV1 task order -- `AV-v-3` -- THE LEAD CHART'S GENERATIONS LINE IN WORDS, AND ONE DARK BAND ON THE LOAD VIEW

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-v-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~19</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 09bd04b1 -- gens.cjs 0 of 3 (FAIL as expected: "Generations across 30 date(s): 25 ABSENT, 5 SERVED; latest 2026-09-25 generation 20260926T110728Z-df5d006844da"; PanelFooter x1); green arm 3 of 3; bound 4 of 4 (PASS). Blind spot: the band count is read from the component tree (no PanelFooter), not from pixels -- the issuer's walk runs the walker's design:bands check.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-v-3` (round 5, decomposition v5; serves FWD-11)

This is your slot's SECOND order. The first, AV-v-2 (the chart's palette, right-edge room and the walker's pick step), is already
committed on your branches by this slot; build on top of it and do not change what it built.

Two things on the lead panel:
1. `components/RankedChart.tsx` `GenerationsLine` prints under the chart title: "Generations across 30 date(s): 25 ABSENT, 5
   SERVED; latest 2026-09-25 generation 20260926T110728Z-df5d006844da" -- pointer-status words and a generation id on the face
   (it renders in the drawn chart and in the INCOMPLETE / COMPLETE_EMPTY branches). Build: ONE plain sentence saying how many
   dates the window has, how many carry a published ranking, and the latest such date (e.g. "Of the 30 dates in the window, 5
   have a published ranking; the latest is 2026-09-25."; a window with none says so in words). No ABSENT / SERVED / EMPTY /
   PENDING word and no generation id in visible text; the element keeps `data-generation-caption` (the id may ride it or
   another attribute). Counts are the producer's own pointer statuses, counted as today -- nothing else is derived.
2. The load view shows TWO full-width `#0A1733` bands (DESIGN.md C3 allows one): measured on the round-4 walk (shot 004), the
   Lead Panel's header rows and its footer rows are both rgb(10,23,51) while its body is rgb(25,38,67) -- the second band is the
   `PanelFooter` in `components/LeadPanel.tsx`. Build: the source caption (`SourceCaption`: the "Source: ..." line, the
   disclosure line and the collapsed "Details" block, `data-source-caption="generation" | "disclosure" | "detail"`) and the
   `ResolutionNote` move INTO the panel body (`PanelContent`, below the list / chart), in the body's own band ink; no
   `PanelFooter` on the Lead Panel. Every caption line and attribute is kept.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state
naming, in plain words, what is missing and which team fills it -- never a project code, serial or storage path.
C-ESTATE-FIXTURES -- windows are the estate's HeroDialog + DialogStamp, panels and states are the estate's; nothing forked.
**Design law (portal `DESIGN.md`):** white panels with navy ink (C3); ONE dark band per page; no translucent white (C5.8); no
shadow (C11). A code, field name or path may sit in a data attribute or in code, never in visible text -- and text inside a
collapsed `<details>` is still visible text.

**If a bound harness check is anchored on the raw text this cell removes,** re-anchor that ONE check onto the same fact as the
page now states it (the words, or a data attribute), keep its claim, never drop it; the harness keeps at least its base
check count (the floor in the bound criterion). Only a harness named in `<paths>` may be edited. Record each re-anchor
(old anchor -> new) in the instance. (`tabs.harness.cjs` and `errorEmpty.harness.cjs` stub `PanelFooter` and read the "Source:"
text through it; if they go red on the footer's removal, re-anchor them onto the caption's `data-source-caption` element.)

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` under `portal/` change; every other page, component, tab and harness is unchanged. In
   `RankedChart.tsx` change only `GenerationsLine` (the palette and margin are the previous order's).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/RankedChart.tsx
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/shell.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~19/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx`,
`portal/src/ui/components/panels/`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-v-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/gens.cjs"; echo "exit=$?"</invocation><expect>GENERATIONS LINE AND ONE BAND: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-v-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/bound.cjs" V3 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 shell.harness.cjs:10 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>V3 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-v-3" judgment="true"/>
</proof_of_spec>

AC1 is the built behaviour on the served 12-name series and the served ranking; AC2 the bound. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded: the lead panel reads its ranking's history in one plain sentence and the load view carries one dark band (FWD-11).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~19/DSGN_AMGTV1.TO-AV-v-3.the-generations-line-and-one-band.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 5 = the round-4 analysis's enrichment list @177c576c80 section 4 item 3. Decomposition v5. Slot ~19's
second order (after AV-v-2; one file, `RankedChart.tsx`). Base 09bd04b1: gens.cjs 0 of 3; green arm (scratch GenerationsLine
sentence + LeadPanel caption moved into PanelContent) 3 of 3; V3 bound 4 of 4. Band evidence MEASURED from walk C shot 004 pixels
(header y150-190 and footer y800-875 rgb(10,23,51); body y215-300 rgb(25,38,67)).

<status>complete</status>
<round>5</round>
<slot>~19</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
