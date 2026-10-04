# DSGN_AMGTV1 task order -- `AV-zn-1` -- THE RENDER INSTRUMENT GRADES THE REDESIGN: THE LIGHT-FAMILY BAND CLAUSE, THE PRICE FACE AT REST, THE WINDOWED CHATTER FIXTURE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zn-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~97</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the instrument serves a vite build from disk through Playwright routing with fixtures (no server, no network).
comp-adversary: RUN by the issuer at the cut on portal 35a723bf -- instrument35.cjs 0 of 4 in 948 s (arm 1: no state grades a re-anchored band clause, faces.chatter 0 visible on the monthly fixture; arm 2: 8fa7abde grades no re-anchored clause FAIL; arm 3: no plant is told apart; arm 4: 12 stale darkContainers/bandIsIdentityHeader FAILs). At the round-35 cut it read 4 of 4 on a scratch reference re-anchor (INSTRUMENT_DIR).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zn-1` (round 36, decomposition v36; serves FWD-20; touches no product file)

`portal/scripts/ui-contract-check.mjs` is FWD-20's render instrument. It drives six Security Analysis states through `ui-measure.mjs`
and grades them into `grades.json`. Its last run on the redesign read 62 PASS and 14 FAIL, and every FAIL was the instrument's own
stale anchor, not the page:

1. **The band clause.**
   - `darkContainers` expects exactly one dark band, and `bandIsIdentityHeader` expects a navy identity band. Both FAIL on all six
     states (12 FAILs), because the light-family redesign removed the navy band.
   - PRD FWD-20 (v0.9): the band clause is `bandContainersTopLevel <= 1 and lightOnDark == 0`. That is, at most one top-level dark
     band, and no light panel, strip, card or light ink inside a dark container.
   - Grade those two values instead. Add a `lightOnDark` count to `ui-measure.mjs`: light fills or light text whose nearest painted
     ancestor is dark.
   - Retire the two stale clauses. No clause named `darkContainers` or `bandIsIdentityHeader` may grade FAIL on the redesign.
2. **The price face.** `run.faces.price` FAILs "19 [data-price-bar] visible for 32 served". The page shows the top ten per side at
   rest (`components/PriceBars.tsx` `REST_PER_SIDE = 10`). The expected count is the page's own rule, min(10, gainers) +
   min(10, losers) over the served `return_30d_pct`, not every served row.
3. **The chatter face.** `run.faces.chatter` FAILs "0 visible for 18 served". The fixture serves the round-16 MONTHLY
   collected-chatter shape, but the face has been windowed since round 31 (RESAPP FWD-36: `window_days`, `articles_total`).
   - Replace the fixture's collected-chatter entry with the served windowed shape. Copy the payload of
     `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round31/fixtures/windows.chatter.30.json`, a read-only capture
     of the deployed route.
   - The expected count is rows with `articles_total > 0` (`components/ChatterBubbles.tsx` `buildCollage`).

The instrument must still be able to FAIL. The check builds the real pre-redesign page (portal 8fa7abde), which must FAIL the band
clause. It also plants pages with two dark bands and with a white card on a band, beside a clean one-band control.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue. (A local `vite build` and the instrument's
   own Playwright run from disk are the check's, not yours to change.)
2. Only the files in `<paths>` change. No product file (`src/pages/SecurityAnalysis/**` other than the one fixture) changes.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file. Keep each
   file's existing line endings. The fixture JSON may be rewritten whole with the Write tool.

## 3. SURFACES

<paths>
portal/scripts/ui-contract-check.mjs
portal/scripts/ui-measure.mjs
portal/src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~97/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 2400)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zn-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; R35_SCRATCH="C:/tmp/r36-scratch-wk97" DIST_8FA7ABDE="C:/tmp/r35-scratch-c/dist-8fa7abde" node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round35/checks/instrument/instrument35.cjs"; echo "exit=$?"</invocation><expect>THE INSTRUMENT GRADES THE REDESIGN AND CAN FAIL: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zn-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 takes about 13 minutes: it builds your tree once (about 20 s), then runs the instrument several times. Use `R35_ARMS="1,4"`
while you iterate; the proof is the full run above. The pre-redesign build at `C:/tmp/r35-scratch-c/dist-8fa7abde` is the issuer's.
Read it, never rebuild or edit it.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~97/DSGN_AMGTV1.TO-AV-zn-1.instrument-reanchor-light-family.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W97-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the result tally the instrument printed on your tree, the
portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** ROUND34_CLOSE.md section 1 (the six-state run at PROD dbd29c6320, 62/14) and ROUND35_CLOSE.md section 4 item 1.
- **Check provenance:** instrument35.cjs, authored at the round-35 cut and committed @9e5820652c. At 055ba370 it read 0 of 4 (776 s)
  and 4 of 4 on a scratch reference re-anchor (`INSTRUMENT_DIR=C:/tmp/r35-scratch-c/ref/portal/scripts`); on that reference
  8fa7abde reads `lightOnDark=7` on five states.
- **Not this cell:** the list-state font sizes and radii the re-anchored instrument sees (AV-zn-2). The person's read of the six PNGs
  (FWD-20's person arm) is the issuer's at the close.

<status>complete</status>
<round>36</round>
<slot>~97</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
