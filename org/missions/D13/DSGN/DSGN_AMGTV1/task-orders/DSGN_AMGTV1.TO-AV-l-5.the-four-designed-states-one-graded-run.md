# DSGN_AMGTV1 task order -- `AV-l-5` -- THE FOUR DESIGNED STATES ARE CAPTURED IN THE SAME GRADED RUN, NO-PERMISSION BY ITS LEVER AND LABELLED FOR WHAT IT IS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-l-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~51</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the instrument reads local builds and static pages only.
comp-adversary: RUN by the issuer at the cut on portal DEV ba62e945 -- sweep.cjs 2 of 3 (FAIL as expected on arm 1: `--states-sweep` is a separate mode that prints its own RESULT, so grades.json's fourStates stays FAIL with no-permission 0; arms 2 and 3 -- labelling and the blank-page negative -- are controls); green arm (scratch r13-green-c @cc2705d1 over AV-l-4, an issuer-spawned helper; ui-contract-check.mjs +196/-102) 3 of 3 -- DEV fourStates PASS (loading 8, error 11, empty 6, no-permission 1, standalone, PNG 7371 bytes); strip 3/3 and rendercontrol 3/3 still. Note from the arm: the standalone no-permission render must count only on a running application page (a blank host must not pass).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-l-5` (round 13, decomposition v13; serves FWD-19, FWD-20)

The CTO's ruling 5 (round-12 analysis): "FWD-19's no-permission state needs its lever: the `--states-sweep` path renders
`PanelNoPermission`, so the `fourStates` clause can pass." Today `--states-sweep` (AMGT-rl-9, in `portal/scripts/ui-contract-check.mjs`)
is a separate mode: it renders the four designed panel states -- empty / loading / error by fixture levers, no-permission STANDALONE
(the real `PanelNoPermission` export rendered off-route and injected into a loaded page: it has no live consumer, per
PanelStates.tsx's own docstring) -- prints its own matrix and RESULT, and writes no grades.json; a plain run grades `fourStates` FAIL
(no-permission 0). This order follows AV-l-4 on the same worktree. Build, in `portal/scripts/` only:
1. ONE invocation `node portal/scripts/ui-contract-check.mjs --dist <dir> --out <dir> --states-sweep` grades the six states (as a plain
   run does) AND folds the sweep's captures into grades.json `run.fourStates`: PASS only when each of loading / error / empty /
   no-permission is captured at least once across the run and the sweep; counts per kind.
2. The no-permission capture is labelled STANDALONE in `run.fourStates` (not claimed reachable from a route) and its PNG is written; it
   counts only when its host page is the running application (a blank host page must not pass).
3. The run's exit and RESULT come from grades.json; a blank page never reads fourStates PASS and exits non-zero.

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

Read-only: the whole repository; in particular `portal/src/ui/components/states/PanelStates.tsx`, the issuer's checks and pages under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/`, and `C:/tmp/dsgn-r13-dist/{dev,pre}`.

## 4. PROOF OF SPEC (literal; timeout 1500)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-l-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/sweep.cjs"; echo "exit=$?"</invocation><expect>THE FOUR DESIGNED STATES, ONE GRADED RUN: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-l-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/strip.cjs"; echo "exit=$?"</invocation><expect>A STRIP IN ITS BAND IS THE BAND: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-l-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/rendercontrol.cjs"; echo "exit=$?"</invocation><expect>THE RENDER CHECK CAN FAIL: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-l-5" judgment="true"/>
</proof_of_spec>

AC1 runs `--states-sweep` on the DEV build and on the blank page: fourStates PASS with each kind counted, no-permission labelled
standalone with its PNG, the six states still graded in the same file; the blank page never passes. AC2 and AC3 keep AV-l-4's rule and
round 12's control green. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the sweep's PNGs, never self-graded: each designed state
looks designed, and the standalone capture is honestly labelled (FWD-19, FWD-20).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~51/DSGN_AMGTV1.TO-AV-l-5.the-four-designed-states-one-graded-run.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the DEV run's fourStates value and out folder, the portal and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 13 = the round-12 analysis s.4 item 5 with ruling 5. After AV-l-4 on slot ~51. Base ba62e945: sweep.cjs 2 of 3;
green r13-green-c @cc2705d1 3 of 3. Behaviour change recorded: `--states-sweep` no longer prints its own RESULT (a `SWEEP:` line
instead; the run's RESULT is grades.json's).

<status>complete</status>
<round>13</round>
<slot>~51</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
