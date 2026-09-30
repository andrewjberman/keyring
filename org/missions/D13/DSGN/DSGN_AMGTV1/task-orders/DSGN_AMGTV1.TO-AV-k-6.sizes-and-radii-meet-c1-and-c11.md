# DSGN_AMGTV1 task order -- `AV-k-6` -- SIZES AND RADII MEET C1 AND C11

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-k-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~55</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the render run serves a page build from disk with fixtured API reads.
comp-adversary: RUN by the issuer at the cut on portal DEV 118cd005 -- styles.cjs 1 of 3 (FAIL as expected: sizes FAIL {"smallest":10} and radii FAIL in all five Security states; the header timeline's Y-axis ticks render at 10px and its three legend swatches at a 1px radius; arm 3 is the control -- the base build reads FAIL -- and passes at base by design); green arm (scratch r14-green-f @88205f47, an issuer-spawned helper; TimelinePanel.tsx + ThesisCards.tsx, +5/-5) 3 of 3 (12 of 12 sizes/radii cells PASS; ticks at 11px, swatches and the MACHINE chip at 2px, Exec's status dots unchanged); bytes 3/3; portal tsc -b rc=0; all 16 page harnesses green. Measured correction to the analysis: the radii clause rejects only 1px; a pill is accepted, so Exec's confirmed dots (status dots, legal under C11) are not touched. Blind spots: radii reads the top-left corner only; the chip selector is structural; BA's fixtures only; the clause accepts a pill on any element (it cannot see C11's "dots and avatars only") -- an instrument finding, not this cell's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-k-6` (round 14, decomposition v14; serves FWD-20)

The CTO's ruling 8 (round-13 analysis): `sizes` and `radii` are graded against DESIGN.md C1 (the type scale's floor) and C11 (the radius
set) as round-14 styling -- they became visible when round 13's refreshed fixtures first drew the header timeline. Build, under
`portal/src/pages/SecurityAnalysis/components/`:
1. **`TimelinePanel.tsx`:** the Y-axis tick labels at the scale's floor (11px, not 10px); the three legend swatches at a radius C11 allows
   (2px, not 1px). The axis keeps its labels (do not delete them).
2. **`ThesisCards.tsx`:** the MACHINE chip takes a chip radius (2px, per C11: the pill is for status dots and avatars only).
Nothing else changes; Exec's confirmed dots are status dots and keep their pill.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing. **Design law:** portal
`DESIGN.md` C1 and C11.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact, keep its
claim, never drop it; only a harness named in `<paths>` may be edited. Measured on the green arm, no harness needs a change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~55/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md` (C1, C11), `portal/scripts/ui-measure.mjs` (the `sizes` and `radii`
clauses) and the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1200)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-k-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/styles.cjs"; echo "exit=$?"</invocation><expect>SIZES AND RADII MEET C1 AND C11: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-k-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bound.cjs" K6 thesisLadder.harness.cjs:10 timelineFourStates.harness.cjs drafting.harness.cjs:8 shell.harness.cjs:10 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>K6 BOUND: 5 of 5 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-k-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-k-6" judgment="true"/>
</proof_of_spec>

AC1 builds the page from your worktree's `portal/` (vite, into a temp dir), runs the graded render with `--states-sweep` (`sizes` and
`radii` PASS in all six states), checks that nothing was deleted to pass (the axis ticks, the swatches, the MACHINE chip and Exec's dots
still render, at C1/C11 shapes), and runs the negative (the base build reads sizes and radii FAIL). AC1 takes about 10 minutes. AC2 is
the bound on every harness that loads those components; AC3 no control byte. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the
issuer's render-run PNGs, never self-graded: the chart's labels still read, nothing styled off the contract (FWD-20).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~55/DSGN_AMGTV1.TO-AV-k-6.sizes-and-radii-meet-c1-and-c11.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the sizes/radii values per state, the output line of every criterion, the portal and outer commit
hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 14 = the round-13 analysis @1e7d4bac11 s.4 item 6 with ruling 8. Its own chain ~55 (TimelinePanel and ThesisCards
are written by no other round-14 cell). The analysis named "12 dots" among the causes; the helper measured the clause and C11: status dots
may be pills, so ExecManagementTab.tsx is not in this cell. Base 118cd005: styles.cjs 1 of 3 (608 s); green r14-green-f @88205f47 3 of 3
(630 s).

<status>pending</status>
<round>14</round>
<slot>~55</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
