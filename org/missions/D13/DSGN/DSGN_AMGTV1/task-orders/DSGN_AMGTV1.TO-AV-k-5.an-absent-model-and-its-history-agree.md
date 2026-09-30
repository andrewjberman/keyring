# DSGN_AMGTV1 task order -- `AV-k-5` -- AN ABSENT MODEL AND ITS HISTORY AGREE ON ONE FACE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-k-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~54</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check reads fixtures the issuer captured (read-only invokes, round 13).
comp-adversary: RUN by the issuer at the cut on portal DEV 118cd005 -- modelhistory.cjs 2 of 3 (FAIL as expected: with the latest model ABSENT the compare block beside "No model in the research pack for this name yet" is headed "What moved between two versions"; arms 2 and 3 are controls and pass at base by design); green arm (scratch r14-green-e @2a9ef6a4, an issuer-spawned helper; ModelTab.tsx only, +13/-2) 3 of 3; bytes 3/3; portal tsc -b rc=0; all 16 page harnesses green. Blind spots: the compare block's heading only (the "Versions of this model" list above it is not graded); one name (BA) and the page's default pair (oldest to newest); static markup (model-empty.png is the render run's); "history" is a word pattern.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-k-5` (round 14, decomposition v14; serves FWD-15 and FWD-19)

The CTO's ruling 6 (round-13 analysis): an ABSENT model and its version history must not contradict on one face. Today the Model
tab reads "No model in the research pack for this name yet. No figure, case or estimate is shown in its place." (the empty state,
keyed on the LATEST block) beside "What moved between two versions ... 212 figures added ..." (the compare, keyed on HISTORY). Both
are true; a PM reads a contradiction. Build, in `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx` (the `ModelVersions` block):
1. **When the latest model is ABSENT** (the served `model_status` is not SERVED) and version history is served, the compare block is
   headed as HISTORY -- e.g. "Earlier versions of the pack held these figures" -- with one lead sentence saying the latest pack holds
   no model and these figures are from versions it held before. It is NOT hidden: the history is information a PM may want. The
   figures and counts are unchanged (served, printed as served).
2. **When the latest model is SERVED**, the compare block keeps its current heading and figures.
3. **When the latest is ABSENT and no history is served**, only the empty sentence shows (no compare block, no "figures added").
The frame may ride a `data-` attribute (e.g. `data-model-compare-frame="history|current"`).

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing. **Design law (portal
`DESIGN.md`):** a code, field name or path may sit in a data attribute or in code, never in visible text.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact, keep its
claim, never drop it; only a harness named in `<paths>` may be edited. Measured on the green arm, no harness needs a change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~54/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md` and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-k-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/modelhistory.cjs"; echo "exit=$?"</invocation><expect>AN ABSENT MODEL AND ITS HISTORY AGREE ON ONE FACE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-k-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bound.cjs" K5 modelPattern.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>K5 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-k-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-k-5" judgment="true"/>
</proof_of_spec>

AC1 renders the Model tab on BA's served bundle three ways: latest ABSENT with history served (the empty sentence beside a compare
block headed as history), latest SERVED (the current heading and the same figures), and latest ABSENT with no history (no compare
block). AC2 is the bound on every harness that loads the Model tab; AC3 no control byte. AC4 is JUDGMENT, graded by
`3.0.0_SA_CVO~Z` at L9 on the issuer's render-run PNG `model-empty.png`, never self-graded: nothing contradictory on the face
(ruling 6). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~54/DSGN_AMGTV1.TO-AV-k-5.an-absent-model-and-its-history-agree.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where (the visible wording of the new heading and sentence), the output line of every criterion, the
portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 14 = the round-13 analysis @1e7d4bac11 s.4 item 5 with ruling 6. The check grades statically on
`compare.BA_US_Equity.oldest-latest.json` (the page's default pair: 212 added, 7 changed), not the named compare capture (a different
pair, 0 changes). Base 118cd005: modelhistory.cjs 2 of 3; green r14-green-e @2a9ef6a4 3 of 3.

<status>pending</status>
<round>14</round>
<slot>~54</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
