# DSGN_AMGTV1 task order -- `AV-w-6` -- THE HISTORY VIEW READS WITH TEN OR MORE NAMES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-w-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~14</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV a93071b8 -- history.cjs 0 of 5 (FAIL as expected; a scratch green arm reached 4 of 5, arm 1 reading the real constants file); bound 4 of 4 (PASS). Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-w-6` (round 4, decomposition v4; serves FWD-3 (first cut))

FWD-3: "A PM can read how names moved over time without untangling a knot of lines" -- ACCEPT: "With ten or more names, the
dates do not overlap, each line is labelled by company name, there is one legend, and the PM can pick out one name and follow
it." The CTO's fork ruling F1: the lead panel's chart is the highlight chart with legend toggles (the pattern of
`portal/src/pages/FactorTilts/components/ModelTiltTimeSeriesView.tsx`, read-only -- port the pattern, do not import or edit it).

Today (`components/RankedChart.tsx`): the lead panel requests the head 5 names (`constants.ts` `RANK_SERIES_TOP_N = 5`); the
X axis forces every date (`interval={0}`, angled); there are two legends (recharts `<Legend>` and the point-count list
below the chart); 5 strokes repeat by index, so 12 names share colours; nothing can be picked.

Build:
1. `constants.ts`: `RANK_SERIES_TOP_N = 12` (the head of the producer's already-ordered list; which and in what order is
   unchanged). Nothing else in `constants.ts` changes.
2. `RankedChart.tsx`, in the drawn-chart branch only (the NO_PAYLOAD / INCOMPLETE / COMPLETE_EMPTY branches unchanged):
   - Dates do not overlap: the X axis lets recharts thin its ticks (`interval="preserveStartEnd"` or another non-zero
     policy) with a `minTickGap` (a number > 0).
   - ONE legend: remove recharts `<Legend>`; the point-count list below the chart becomes the one legend -- the `<ul>`
     carries `data-rank-legend`, and each entry is a `<button type="button">` carrying `data-series-ticker="<ticker>"` and
     `aria-pressed`, showing the colour swatch, the label and the point count (and the unresolved count, as today).
   - Each line labelled: every `<Line>` gets `name` = the series' served company name when the series carries one (a
     `name` field; not served today -- declare it optional on `TickerRankSeries` in `types.ts` only if you must, as
     `name?: string | null`), else the ticker exactly as written ("BP/ LN" whole). The legend entry shows the same label.
     Never look a name up or join one from another payload.
   - Pick one and follow it: an optional prop `focusTicker?: string` seeds the picked name (default none). Clicking a
     legend button picks that name (clicking it again clears); the picked line draws at full strength (`strokeOpacity`
     1, and may be thicker) and every other line is muted (`strokeOpacity` < 1); with no pick every line is full strength.
   - Distinct colours: 12 series draw with 12 distinct strokes (a fixed palette of at least 12 opaque colours indexed by
     position, readable on the band this chart sits on; no translucent white, C5.8).
The pivot, ranks, the completeness banners and the generations line are unchanged.

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
(old anchor -> new) in the instance.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` under `portal/` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/RankedChart.tsx
portal/src/pages/SecurityAnalysis/constants.ts
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~14/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/` (never edit them; the fixtures are the served payloads the checks render).
Also read-only: `portal/src/pages/FactorTilts/components/ModelTiltTimeSeriesView.tsx` (the pattern F1 names).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-w-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/checks/history.cjs"; echo "exit=$?"</invocation><expect>HISTORY VIEW: 5 of 5 arms (series 12) -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-w-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/checks/bound.cjs" W6 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 tabs.harness.cjs:20 chart.harness.mjs; echo "exit=$?"</invocation><expect>W6 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-w-6" judgment="true"/>
</proof_of_spec>

AC1 is the built behaviour on a served 12-name series (recharts props read through a stub; pixels are the walk's); AC2 the bound. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded: walked with ten or more names, the history view has one legend, dates that do not overlap, and one name a PM can pick and follow (FWD-3).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~14/DSGN_AMGTV1.TO-AV-w-6.the-history-view-with-ten-names.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 4 = the round-3 analysis's enrichment list @46d28c6c4c section 4 (CTO msg 26587). Decomposition v4.
Base a93071b8: history.cjs 0 of 5 (FAIL as expected; a scratch green arm reached 4 of 5, arm 1 reading the real constants file); bound 4 of 4 (PASS).

<status>complete</status>
<round>4</round>
<slot>~14</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
