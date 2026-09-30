# DSGN_AMGTV1 task order -- `AV-k-7` -- FWD-17'S COUNT IS PERSON-READABLE (THE OPENED-FOLD PNG)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-k-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~53</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the instrument serves a page build from disk with fixtured API reads.
comp-adversary: RUN by the issuer at the cut on portal DEV 118cd005 -- foldopen.cjs 1 of 3 (FAIL as expected: no posture-cites-open.png and no visible count; the blank page leaves the instrument silent; arm 2 is the control and passes at base by design); green arm (scratch r14-green-g @bce8e785, an issuer-spawned helper; ui-contract-check.mjs + ui-measure.mjs, +99/-5) 3 of 3 (the opened shot 1440x2691, 20 visible cites == citesFolded 20, 8 visible UNRESOLVED == unresolvedCites 8; blank NOT_EXERCISED; planted FAIL 2 vs 3); ui-measure self-test OK; rendercontrol.cjs 3 of 3; portal tsc -b rc=0. Arm 2 was amended by the issuer at the cut to compare the at-rest run's SHAPE with the base close run, not its values (the round's other cells move values by design). Blind spots: a cite covered by an overlapping element or drawn in its background colour counts as visible (DOM, not pixels); the posture state and the base fixtures only; arms 2 and 3 read C:/tmp/dsgn-r13-close-render and C:/tmp/dsgn-r13-dist/final (the issuer holds both through round 14).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-k-7` (round 14, decomposition v14; serves FWD-17 and FWD-20) -- INSTRUMENT ONLY

The CTO's ruling 8 (round-13 analysis): fwd17's render run adds an OPENED-fold PNG, so its cite count is person-readable. Today
`fwd17_verdictComparable` on posture reads citesFolded 20 / unresolvedCites 8, but those cites sit inside folds the at-rest `posture.png`
never opens. Build, in `portal/scripts/ui-contract-check.mjs` and `portal/scripts/ui-measure.mjs`:
1. After grading posture, the render run writes `<out>/posture-cites-open.png` with every cite fold opened, and a sidecar
   `<out>/posture-cites-open.json` = { grade: PASS|FAIL|NOT_EXERCISED, png, pngBytes, visibleCites, visibleUnresolved, fwd17: {
   citesFolded, unresolvedCites } } -- the cites VISIBLE in that shot, read from the DOM around the capture.
2. The sidecar grades PASS only when the visible counts equal fwd17's counts and both are positive; FAIL when they differ; NOT_EXERCISED
   when nothing was seen (a blank page). The instrument is never silent on a blind read.
3. The at-rest run is unchanged: `posture.png` keeps its folds closed, fwd17 is still graded in grades.json, and grades.json gains no new
   cell (the count lives in the sidecar).

**The rules every cell keeps (PRD CONTRACTS, binding):** the instrument changes no page file; the page derives nothing.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`.

## 3. SURFACES

<paths>
portal/scripts/ui-contract-check.mjs
portal/scripts/ui-measure.mjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~53/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/scripts/ui-smoke.mjs`, `portal/scripts/ui-dist.mjs`, and the issuer's checks under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-k-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/foldopen.cjs"; echo "exit=$?"</invocation><expect>FWD-17'S COUNT IS PERSON-READABLE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-k-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/rendercontrol.cjs"; echo "exit=$?"</invocation><expect>THE RENDER CHECK CAN FAIL: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-k-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node portal/scripts/ui-measure.mjs --self-test --fixture portal/src/pages/SecurityAnalysis/__harness__/tests/uiMeasureFixture.html; echo "exit=$?"</invocation><expect>SELF-TEST OK -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-k-7" judgment="true"/>
</proof_of_spec>

AC1 runs the instrument on the base page build three ways: the full graded run (the opened PNG written, its visible counts equal
grades.json's fwd17 counts, both positive), the at-rest run unchanged in kind (posture.png folds closed, fwd17 PASS, the same graded
cells), and the negatives (a blank page NOT_EXERCISED; a planted page where one cite hides once opened grades FAIL). AC1 takes about
11 minutes. AC2 keeps the render check able to fail; AC3 the instrument's self-test. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9
on the issuer's render run's `posture-cites-open.png`, never self-graded: the cites a person counts on the PNG equal grades.json's.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~53/DSGN_AMGTV1.TO-AV-k-7.fwd17-count-is-person-readable.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the sidecar's values on the base page, the output line of every criterion, the portal and outer
commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 14 = the round-13 analysis @1e7d4bac11 s.4 item 7 with ruling 8. Leads chain ~53 (k-7 -> k-3: both write
ui-contract-check.mjs); AV-k-2 (chain ~52) writes the standalone no-permission block of the same file -- region-disjoint, merge-tree
0 conflicts, the issuer merges at the drain. Base 118cd005: foldopen.cjs 1 of 3; green r14-green-g @bce8e785 3 of 3 (re-run after the
issuer's arm-2 amendment: see the decomposition).

<status>complete</status>
<round>14</round>
<slot>~53</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
