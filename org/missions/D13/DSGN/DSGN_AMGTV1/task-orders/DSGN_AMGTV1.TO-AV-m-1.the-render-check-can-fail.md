# DSGN_AMGTV1 task order -- `AV-m-1` -- THE CONTRACT'S RENDER CHECK GRADES EVERY CLAUSE, CAN FAIL EACH ONE, AND NEVER READS A BLIND PAGE AS A PASS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-m-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~45</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the instrument reads local builds and fixtures only.
comp-adversary: RUN by the issuer at the cut on portal DEV 846ecc6c -- rendercontrol.cjs 0 of 3 (FAIL as expected: the instrument has no --dist and writes no grades.json); the existing ui-measure self-test reads SELF-TEST OK at base. Green arm: scratch r12-green-a @75baeecc (issuer-spawned helpers, 395+/36- over DEV in the four granted files) reads rendercontrol 3 of 3 over the issuer's fixed clean page (its button had computed Arial; fixed before issuance) in ~6 minutes; SELF-TEST OK. On that arm the DEV run itself exits non-zero -- list's darkContainers reads 2 (the Lead Panel band plus one navy strip) and fourStates FAILS (no no-permission state in a plain run) -- which the check expects: FWD-20 is not yet green on DEV, and the instrument must say so. Measured on that arm: the pre-redesign build (portal 8fa7abde) PASSES the band, fonts, weights, sizes, radii, shadows, lowContrast and purple clauses in all six states; its navy title strips (the instrument's stripContainers: 1 each in thesis, exec, model, posture) are what DEV no longer has. Blind spots: the fixture router serves the page's API reads, so a panel the fixtures do not feed renders its error state; the four designed states are counted, not forced (FWD-19's levers are a later round's).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-m-1` (round 12, decomposition v12; serves FWD-20, with FWD-12 folded in)

FWD-20 (PRD v0.5 @bf3a6f5614, as amended by `1.0.0_SA_CTO~Z` for this cut): `portal/scripts/ui-smoke.mjs` -- driven by
`ui-contract-check.mjs` and `ui-measure.mjs`, the estate's render instrument since AMGT_RESAPP rounds 37-38 -- writes, for each of
the six states (list, thesis, exec, peers, model, posture), a PNG at 1440 and a DOM JSON reading one band, fonts {Lato}, weights
{400,700}, no size below 11, radii {2,3,4,pill}, no shadow outside the focus ring, lowContrastChars 0, purpleFills per FWD-18 (0
in list, 1 = Refresh in the Security states), the four designed states present, and the drafting / tabs / posture harnesses green;
and it CAN FAIL: it FAILS a planted page on each clause beside a clean control, and FAILS the real pre-redesign page on the band
clause. FWD-12: in the Security states the ONE dark band is the identity header and the tab panels are white hairline panels. The
instrument already measures most of this (read all three scripts first). Extend it, in `portal/scripts/` only:
1. **`--dist <built dir>`** on ui-contract-check.mjs, ui-smoke.mjs and ui-measure.mjs (a small shared helper module is fine, e.g.
   `scripts/ui-dist.mjs`): serve a vite build from disk through Playwright routing -- no server, no port -- with the auth stub
   and the fixture router still answering the API; a route with no file falls back to index.html. Absent `--dist`, routing is
   unchanged.
2. **`<out>/grades.json`**, beside the PNGs and per-state JSON and the printed table (keep them):
   `{ "states": { "<state>": { "<clause>": { "grade": "PASS"|"FAIL"|"NOT_EXERCISED"|"N/A", "value": ... } } },
      "run": { "fourStates": { "grade": ..., "counts": {...} }, "harnesses": { "grade": ..., "drafting": {"grade":..,"tally":..},
               "tabs": {...}, "posture": {...} } },
      "result": { "PASS": n, "FAIL": n, "NOT_EXERCISED": n } }`
   with ten per-state clauses: `darkContainers`, `bandIsIdentityHeader`, `tabPanelsWhite`, `fonts`, `weights`, `sizes`, `radii`,
   `shadows`, `lowContrastChars`, `purpleFills`. Exit 0 only when every graded cell is PASS.
3. **`darkContainers`** = top-level band containers + top-level strip containers inside the graded scope (main); PASS iff == 1.
   Keep bandContainersTopLevel and stripContainers as informational values. **`bandIsIdentityHeader`**: in the five Security
   states the one band is the identity header (in list, the Lead Panel). **`tabPanelsWhite`**: the tab panel is white with a
   hairline border (N/A in list).
4. **NOT_EXERCISED:** a state with no application DOM (e.g. redirected to sign-in, body text under ~500 characters, 0 nodes scanned)
   grades every clause NOT_EXERCISED -- never PASS -- and the run exits non-zero. Print nodes scanned per state (the positive
   control).
5. **fourStates:** count `data-panel-state` = loading / error / empty / no-permission per state and across the run; PASS only when
   each of the four is captured at least once (it will FAIL on today's page -- that is FWD-19's, not this cell's).
6. **Harnesses:** run drafting.harness.cjs, tabs.harness.cjs and posture.harness.cjs (portal/src/pages/SecurityAnalysis/__harness__/)
   exactly the way the estate runner does -- read `runHarness` in the issuer's `round12/checks/_load.cjs` (cwd, env, invocation) --
   and grade each from its CHECKS-OK tally. (On DEV they read drafting 8/8, tabs 20/20, posture 32/32 that way; a different
   invocation crashes posture on its module paths.)
7. `--states list` on a static page (the issuer's planted/clean/blank pages) must not hang waiting for application elements.
Inputs the issuer staged for the check: `C:/tmp/dsgn-r12-dist/pre` (vite build of 8fa7abde, the pre-redesign page) and
`C:/tmp/dsgn-r12-dist/dev` (vite build of DEV 846ecc6c), plus `round12/checks/dists/{planted,clean,blank}/index.html`.

**Rules:** no page file changes -- this cell is the instrument. Do not edit the issuer's check or its planted/clean/blank pages; if
one is wrong for the classifier, file a surprise row with the exact change and keep working.

## 2. BOUNDS

1. No server (no `vite`, no dev server, no port: portal law, dev builds use 5174 only and 5174 is another seat's), no fetch, no
   network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (they turn a backslash sequence into a
   control byte).

## 3. SURFACES

<paths>
portal/scripts/ui-contract-check.mjs
portal/scripts/ui-measure.mjs
portal/scripts/ui-smoke.mjs
portal/scripts/ui-dist.mjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~45/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md`, `portal/src/ui/components/states/PanelStates.tsx`, the page's
`__harness__/` and the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/` (never edit
them).

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-m-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/rendercontrol.cjs"; echo "exit=$?"</invocation><expect>THE RENDER CHECK CAN FAIL: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-m-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node portal/scripts/ui-measure.mjs --self-test --fixture portal/src/pages/SecurityAnalysis/__harness__/tests/uiMeasureFixture.html; echo "exit=$?"</invocation><expect>SELF-TEST OK -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-m-1" judgment="true"/>
</proof_of_spec>

AC1 runs the instrument five times from disk -- the pre-redesign build, the DEV build, and the planted, clean and blank pages -- and
reads each `grades.json`: the pre-redesign page FAILS darkContainers in thesis, exec, model and posture while DEV passes it and
bandIsIdentityHeader in all five Security states, every state grading all ten clauses; the planted page FAILS each of the eight
style clauses and the clean page PASSES them; the blank page grades every clause NOT_EXERCISED and exits non-zero; on DEV the three
harnesses read green. AC2 keeps the instrument's own classifier self-test OK. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9,
never self-graded: the six PNGs of the DEV run are read by a person, and a rejection cites its DESIGN.md clause (FWD-20: "A JSON
PASS WITHOUT THE PNG READ BY A PERSON IS CARE, NOT A CONTROL"). Leave the DEV run's output folder path in your report.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~45/DSGN_AMGTV1.TO-AV-m-1.the-render-check-can-fail.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the DEV run's per-clause grade table and output folder, the
portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 12 = the round-11 analysis s.4 items 1 and 6 with ruling 5; FWD-12 folded in (the existing instrument read
bands == 1, fonts {Lato}, purple 0/1 on every state of 5174 @4e4307be at the cut, so an FWD-12 build cell's check could not FAIL at
base; the FWD-12 clauses ride this instrument). FWD-20's negative-control clause measured unmeetable as first written (the
pre-redesign page passes 10 clauses); ENDPOINT amended by `1.0.0_SA_CTO~Z` to this cut's form, PRD v0.5 @bf3a6f5614 (msg 27097).
`portal/scripts/` is outside PRD PATHS' owned list, but FWD-20 names `portal/scripts/ui-smoke.mjs` as its instrument.

<status>complete</status>
<round>12</round>
<slot>~45</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
