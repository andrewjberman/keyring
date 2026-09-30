# DSGN_AMGTV1 task order -- `AV-l-4` -- THE RENDER CHECK COUNTS A STRIP INSIDE A BAND AS THAT BAND, AND STILL FAILS A SEPARATE DARK CONTAINER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-l-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~51</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the instrument reads local builds and static pages only.
comp-adversary: RUN by the issuer at the cut on portal DEV ba62e945 -- strip.cjs 1 of 3 (FAIL as expected: DEV's list reads darkContainers 2 = band 1 + strip 1, the Lead Panel's own header bar; the issuer's inband page reads the same; the negative arm -- a separate strip and a second band each FAIL -- passes at base by design); green arm (scratch r13-green-c @19420ece, an issuer-spawned helper; ui-contract-check.mjs +8/-1, ui-measure.mjs +22/-2) 3 of 3, and round 12's control carried as round13/checks/rendercontrol.cjs still 3 of 3 (the pre-redesign page still FAILS darkContainers in thesis, exec, model and posture); ui-measure self-test OK. Blind spot: a full run takes several minutes; the classifier reads computed colours.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-l-4` (round 13, decomposition v13; serves FWD-20, FWD-12)

The CTO's ruling 4 (round-12 analysis): "The `list` title strip is the instrument's error, not the page's (the CVO: not a C3
rejection). `darkContainers` counts a strip INSIDE a band as that band. The AC plants a second, separate dark band, which must still
FAIL." Round 12's instrument (`portal/scripts/ui-contract-check.mjs` + `ui-measure.mjs`, `--dist`, `<out>/grades.json`) reads
darkContainers = top-level band containers + top-level strip containers in `main`, PASS iff 1; on DEV's list it reads band 1 + strip 1,
where the strip is the Lead Panel's own navy header bar on its band. Build, in `portal/scripts/` only:
1. A strip that sits INSIDE a band -- a DOM descendant of the band element, or its box within the band's box -- counts as that band
   (not a second container). Its value still names the strip it folded in (e.g. `{total: 1, band: 1, strip: 0, foldedStrips: 1}`).
2. A strip OUTSIDE any band, or a second separate band, still counts, so such a page still FAILS. Nothing else in the grading moves.

**Rules:** no page file changes -- this cell is the instrument. Do not edit the issuer's checks or static pages; if one is wrong for the
classifier, file a surprise row with the exact change and keep working.

**This slot's next orders, `AV-l-5` (the no-permission lever) and then `AV-l-6` (the FWD-14..19 clauses), follow on the same
worktree after you finish.**

## 2. BOUNDS

1. No server (no vite, no dev server, no port: portal law, dev builds use 5174 only and 5174 is another seat's), no fetch, no network,
   no install, no push, no deploy. REFUSE, do not rescue.
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

Read-only: the whole repository; in particular the issuer's checks and pages under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/` (never edit them) and the builds the issuer staged:
`C:/tmp/dsgn-r13-dist/dev` (DEV ba62e945) and `C:/tmp/dsgn-r13-dist/pre` (8fa7abde).

## 4. PROOF OF SPEC (literal; timeout 1200)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-l-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/strip.cjs"; echo "exit=$?"</invocation><expect>A STRIP IN ITS BAND IS THE BAND: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-l-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/rendercontrol.cjs"; echo "exit=$?"</invocation><expect>THE RENDER CHECK CAN FAIL: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-l-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node portal/scripts/ui-measure.mjs --self-test --fixture portal/src/pages/SecurityAnalysis/__harness__/tests/uiMeasureFixture.html; echo "exit=$?"</invocation><expect>SELF-TEST OK -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-l-4" judgment="true"/>
</proof_of_spec>

AC1 runs the instrument on the DEV build (six states) and on the issuer's inband, outstrip and planted pages: every DEV state reads
darkContainers PASS, the inband page PASS with its strip named, the separate strip and the second band each FAIL. AC2 is round 12's
control carried forward (the pre-redesign page still FAILS darkContainers in thesis, exec, model and posture; every style clause can
fail on a planted page and pass on a clean one; a blank page is never a pass). AC3 keeps the classifier self-test OK. AC4 is JUDGMENT,
graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's render run, never self-graded: the list reads as one dark container to a person and to
the instrument alike (FWD-12, FWD-20).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~51/DSGN_AMGTV1.TO-AV-l-4.a-strip-in-its-band-is-the-band.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the DEV list's darkContainers value, the portal and outer commit
hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 13 = the round-12 analysis s.4 item 4 with ruling 4 (the fixture refresh the CTO also named here rides AV-l-1,
which owns the fixture file). Chain C on slot ~51: l-4 -> l-5 -> l-6. Base ba62e945: strip.cjs 1 of 3; green r13-green-c @19420ece 3 of
3; rendercontrol 3/3.

<status>pending</status>
<round>13</round>
<slot>~51</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
