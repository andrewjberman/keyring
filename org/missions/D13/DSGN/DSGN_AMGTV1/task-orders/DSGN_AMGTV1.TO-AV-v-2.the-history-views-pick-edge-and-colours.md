# DSGN_AMGTV1 task order -- `AV-v-2` -- THE HISTORY VIEW'S PICK, RIGHT EDGE AND COLOURS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-v-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~19</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 09bd04b1 -- pick.cjs 1 of 3 (FAIL as expected: min CIE76 dE 18.1 #f59e0b/#fb923c; 8 px right of the last tick); pickstep.cjs 1 of 3 (FAIL as expected: no legend button is pressed); green arms 3 of 3 and 3 of 3; bound 3 of 3 (PASS). Blind spot: recharts is a prop-recording stub (no pixels); the walker step is read statically -- the issuer's round-5 walk is its live run.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-v-2` (round 5, decomposition v5; serves FWD-3)

FWD-3: "A PM can read how names moved over time without untangling a knot of lines" -- ACCEPT: "With ten or more names, the
dates do not overlap, each line is labelled by company name, there is one legend, and the PM can pick out one name and follow
it." Round 4 built the one legend, the thinned dates and the pick (`components/RankedChart.tsx`). The CVO's round-4 grade left
three defects:
1. Two strokes nearly match: `SERIES_STROKES` index 1 `#f59e0b` and index 9 `#fb923c` sit at CIE76 dE 18.1 (VLO US / WALMEX* MM
   on the walk). Build: a palette of 12 opaque `#RRGGBB` strokes, still indexed by series position, whose MINIMUM pairwise CIE76
   difference over all 66 pairs is at least 25, each readable on the band this chart sits on (no translucent colour, C5.8).
2. The rightmost date tick is clipped at the chart's right edge (the angled label runs past it). Build: at least 24 px of room
   right of the last tick -- the `LineChart` `margin.right` plus the `XAxis` `padding.right` (a number or `{ right: n }`).
3. No walk ever pressed a legend button, so the pick is ungraded on pixels. Build, in `.claude/skills/ui-walk/walk.mjs`
   (`walkSecurityAnalysis`): on each lead-panel Chart view, after its existing `checks(page, ...)` step, press the FIRST
   `[data-series-ticker]` legend button (when one exists), let the page settle, and run a second step labelled
   `lead-<movement>-<subject>-Chart-picked` through the same `checks(page, label)` call (so the round-4 sign-in guard and the
   screenshot run on it). Add one line to `.claude/skills/ui-walk/SKILL.md` saying the walk presses one legend button per chart.
The pick itself (round 4) stays: a picked line full strength, the others muted; with no pick every line full strength.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state
naming, in plain words, what is missing and which team fills it -- never a project code, serial or storage path.
C-ESTATE-FIXTURES -- windows are the estate's HeroDialog + DialogStamp, panels and states are the estate's; nothing forked.
**Design law (portal `DESIGN.md`):** white panels with navy ink (C3); ONE dark band per page; no translucent white (C5.8); no
shadow (C11). A code, field name or path may sit in a data attribute or in code, never in visible text -- and text inside a
collapsed `<details>` is still visible text. **The charts keep their colour (C6).**

**If a bound harness check is anchored on the raw text this cell removes,** re-anchor that ONE check onto the same fact as the
page now states it (the words, or a data attribute), keep its claim, never drop it; the harness keeps at least its base
check count (the floor in the bound criterion). Only a harness named in `<paths>` may be edited. Record each re-anchor
(old anchor -> new) in the instance.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue. Never run the walker signed in, never
   touch the walker account (`ui_walker_account.py`); the walker change is proven statically and by the issuer's walk.
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged. Change ONLY the palette, the
   chart margin / X-axis padding and nothing else in `RankedChart.tsx` -- the generations line in that file is the NEXT order's.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/RankedChart.tsx
portal/src/pages/SecurityAnalysis/__harness__/chart.harness.mjs
.claude/skills/ui-walk/walk.mjs
.claude/skills/ui-walk/SKILL.md
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~19/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md`, `.claude/skills/ui-walk/signin_detect.mjs`, and the issuer's
checks and fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-v-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/pick.cjs"; echo "exit=$?"</invocation><expect>HISTORY PICK, EDGE AND COLOURS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-v-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/pickstep.cjs"; echo "exit=$?"</invocation><expect>WALK PICKS A NAME: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-v-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/bound.cjs" V2 chart.harness.mjs leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>V2 BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-v-2" judgment="true"/>
</proof_of_spec>

AC1 is the built behaviour on the served 12-name payload; AC2 the walker's new step; AC3 the bound. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots (the new "-Chart-picked" shots), never self-graded: with ten or more names every line has its own colour, the last date is whole, and one picked name can be followed (FWD-3).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~19/DSGN_AMGTV1.TO-AV-v-2.the-history-views-pick-edge-and-colours.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 5 = the round-4 analysis's enrichment list @177c576c80 section 4 item 2 (CTO msg 26684). Decomposition v5.
Slot ~19 queue: AV-v-2 then AV-v-3 (both write `RankedChart.tsx`). Base 09bd04b1: pick.cjs 1 of 3 (min dE 18.1; room 8 px);
pickstep.cjs 1 of 3; green arms 3 of 3 (scratch palette #0ea5e9 #ea580c #a3e635 #c026d3 #fed7aa #059669 #2563eb #f472b6 #eab308
#99f6e4 #ddd6fe #f43f5e, min dE 40.2, margin.right 28; scratch walk.mjs with the picked step) and 3 of 3; V2 bound 3 of 3. The
analysis names "45 pairs" (the walk's 10 names); the check grades all 66 pairs of the 12 strokes (stricter, covers any 10).

<status>pending</status>
<round>5</round>
<slot>~19</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
