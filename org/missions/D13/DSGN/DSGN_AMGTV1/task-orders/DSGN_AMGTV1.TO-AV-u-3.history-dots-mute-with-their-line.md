# DSGN_AMGTV1 task order -- `AV-u-3` -- THE HISTORY VIEW: AN UNPICKED LINE'S DOTS MUTE WITH IT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-u-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~24</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 4f927ad0 -- dots.cjs 2 of 3 (FAIL as expected: with VLO picked, 11 strokes muted and 0 dots muted; the no-pick control and the label path pass); green arm 3 of 3; bound 3 of 3 (PASS). Blind spot: recharts is a prop-recording stub (no pixels).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-u-3` (round 6, decomposition v6; serves FWD-3)

`components/RankedChart.tsx`: with one name picked, the picked line draws full and every other line's STROKE is muted
(`strokeOpacity` MUTED_STROKE_OPACITY) -- but each line's `dot` is `{ r: 3 }` at full strength, so on the round-5 walk the
unpicked series still read as columns of bright dots. Build: an unpicked line's dots mute WITH its line (its `dot` object carries
`fillOpacity` and `strokeOpacity` equal to the line's muted opacity); the picked line's dots stay full; with no pick every dot is
full strength. No dot is removed (`dot` never becomes `false`); radius, colours, palette and everything else are unchanged.

The line label already reads the served company `name` when a series carries one, else the ticker as written (`seriesLabel`);
keep that exactly. The served rank series carries no name today (AMGT_RESAPP xx-2 serves it and is not yet deployed), so the check
proves the label path on a labelled issuer variant only.

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
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/RankedChart.tsx
portal/src/pages/SecurityAnalysis/__harness__/chart.harness.mjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~24/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-u-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/checks/dots.cjs"; echo "exit=$?"</invocation><expect>HISTORY DOTS AND NAMES: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-u-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/checks/bound.cjs" U3 chart.harness.mjs leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>U3 BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-u-3" judgment="true"/>
</proof_of_spec>

AC1 is the built behaviour on the served 12-name payload (and the named issuer variant for the label path); AC2 the bound. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk "-Chart-picked" shots, never self-graded: with one name picked, the rest fade -- lines and dots -- and the picked name can be followed; a line is labelled by company name only where the name is served (FWD-3).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~24/DSGN_AMGTV1.TO-AV-u-3.history-dots-mute-with-their-line.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 6 = round-5 analysis s.4 item 3, ruling 6. The label half needs no page change (seriesLabel already reads series.name); it is realised when AMGT_RESAPP deploys xx-2 (merged @209a6cce2f, not deployed at the cut). Base 4f927ad0: dots 2 of 3; green (dot opacities) 3 of 3; U3 bound 3 of 3.

<status>complete</status>
<round>6</round>
<slot>~24</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
