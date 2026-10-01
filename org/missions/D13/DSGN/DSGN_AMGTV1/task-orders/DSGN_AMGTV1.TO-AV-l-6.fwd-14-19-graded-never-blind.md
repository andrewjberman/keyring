# DSGN_AMGTV1 task order -- `AV-l-6` -- THE RENDER CHECK GRADES FWD-14..FWD-19, EACH CLAUSE WITH ITS VALUE, AND NEVER PASSES A CLAUSE IT COULD NOT SEE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-l-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~51</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the instrument reads local builds and static pages only.
comp-adversary: RUN by the issuer at the cut on portal DEV ba62e945 -- fwd1419.cjs 1 of 3 (FAIL as expected: no FWD-14..19 clause exists in grades.json; arm 3 passes vacuously at base); green arm (scratch r13-green-c @9ce993d3 over AV-l-5, an issuer-spawned helper; ui-contract-check.mjs +172/-4, ui-measure.mjs +226) 3 of 3 -- on DEV fwd14..fwd18 PASS (each with a positive count) and fwd19 FAIL (the Peers panel has no designed empty state -- the page's defect, graded honestly); on the pre-redesign build fwd14, fwd15 and fwd17 FAIL; the blank page NOT_EXERCISED; sweep, strip and rendercontrol still 3/3; self-test OK. Blind spot: each clause measures what its DONE WHEN names from the DOM of a fixture-fed build; the live page is the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-l-6` (round 13, decomposition v13; serves FWD-14, 15, 16, 17, 18, 19)

The CTO's item 6 (round-12 analysis): "The FWD-14..19 grading pass on the refreshed instrument. It prints each clause's value per
state, and a NOT_EXERCISED clause is never a PASS." The outcomes' DONE WHEN texts are in
`org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md` lines 149-195. This order follows AV-l-5 on the same worktree (keep its
sweep folding whole). Build, in `portal/scripts/` only, the clauses in grades.json at these states, each `{grade: PASS | FAIL |
NOT_EXERCISED | N/A, value}` measured from the DOM:
- `thesis`: `fwd14_passagesFolded` -- in the Thesis windows each sentence shows its PASS face and passage count; opening it reveals the
  passage and accession line from the DOM; passages carried in a native `title=` tooltip read ZERO in the same capture as the positive
  control (the tab present, a non-zero count of nodes scanned).
- `model`: `fwd15_modelTable` -- the fiscal table is a white panel with tabular numerals; a REFUSED row renders one status icon and one
  navy sentence spanning the row; ABSENT rows fold into one footnote.
- `peers`: `fwd16_absentColumns` -- the table renders the PRESENT columns only; an "Absent columns (N)" disclosure lists each with its
  reason; the basis chip carries its test statement one hover away.
- `posture`: `fwd17_verdictComparable` -- the verdict card shows the comparable beside the verdict; each numbered reason's cites are
  folded; an UNRESOLVED cite renders a warning ICON beside navy text, 0 amber text.
- all six states: `fwd18_controls` -- in list, Movement and Subject are segmented controls whose active state is weight and rule; the
  generation and resolution lines sit in the "Source:" footer; purpleFills 0 in list, 1 (Refresh) in the Security states.
- run level: `run.fwd19_designedStates` -- the four designed states, per panel, across the run and its `--states-sweep`.
A PASS value carries a positive count (nodes / elements / cells / columns / panels / affordances / count > 0); a page with no
application DOM grades each clause NOT_EXERCISED; `result` counts every graded cell. A clause the page does not meet reads FAIL -- that
is honesty, not a defect of this cell.

**Rules:** no page file changes. Do not edit the issuer's checks or static pages; file a surprise row if one is wrong, and keep working.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`. Never edit a script while a check that runs it
   is still running.

## 3. SURFACES

<paths>
portal/scripts/ui-contract-check.mjs
portal/scripts/ui-measure.mjs
portal/scripts/ui-smoke.mjs
portal/scripts/ui-dist.mjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~51/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the PRD's FWD-14..19 (lines 149-195), the page's source under
`portal/src/pages/SecurityAnalysis/`, the issuer's checks and pages under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/`, and `C:/tmp/dsgn-r13-dist/{dev,pre}`.

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-l-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/fwd1419.cjs"; echo "exit=$?"</invocation><expect>FWD-14..19 GRADED, NEVER BLIND: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-l-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/sweep.cjs"; echo "exit=$?"</invocation><expect>THE FOUR DESIGNED STATES, ONE GRADED RUN: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-l-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node portal/scripts/ui-measure.mjs --self-test --fixture portal/src/pages/SecurityAnalysis/__harness__/tests/uiMeasureFixture.html; echo "exit=$?"</invocation><expect>SELF-TEST OK -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-l-6" judgment="true"/>
</proof_of_spec>

AC1 runs `--states-sweep` on the DEV build and on the blank page: every FWD-14..19 clause graded at its state with a value; the blank
page NOT_EXERCISED on each and exiting non-zero; every PASS carrying a positive count; `result` counting every cell. AC2 keeps AV-l-5's
sweep green; AC3 the classifier self-test. Also report `strip.cjs` and `rendercontrol.cjs` (both must still read 3 of 3). AC4 is
JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's render run, never self-graded: each clause's value matches what a person reads
on the PNGs (FWD-14..19 are graded by this instrument from round 13).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~51/DSGN_AMGTV1.TO-AV-l-6.fwd-14-19-graded-never-blind.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion (and strip, rendercontrol), the DEV run's grade + value summary
for each fwd clause, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 13 = the round-12 analysis s.4 item 6. After AV-l-5 on slot ~51. Base ba62e945: fwd1419.cjs 1 of 3; green
r13-green-c @9ce993d3 3 of 3. fwd19 FAILS on DEV (Peers lacks a designed empty state) -- a round-14 page input, graded honestly here.

<status>complete</status>
<round>13</round>
<slot>~51</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
