# DSGN_AMGTV1 task order -- `AV-l-2` -- EVERY FISCAL FIGURE ON THE MODEL TAB CARRIES ITS UNIT, TABULAR NUMERALS AND A TOOLTIP WITH ITS MNEMONIC AND FULL VALUE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-l-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~50</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV ba62e945 -- fiscal.cjs 0 of 3 (FAIL as expected: 40+ BA fiscal cells without a tooltip; 32 of 35 rows without their unit, e.g. "EPS 7.92 14.03 ..."; a planted served case reason shows "(derived before C-MODEL-WINDOW-AND-ROWS (5))"); green arm (scratch r13-green-b @49771e9c, an issuer-spawned helper; ModelTab.tsx only, +63/-8) 3 of 3 -- 322 served cells, 35 rows; round-12 figures.cjs 3/3; ALL 16 of 16 harnesses green with no harness edit; bytes 3/3; portal tsc -b rc=0. Blind spots: static markup (hover and a tooltip overflowing the rightmost column are the walk's); arm 2 strips tooltip markup with a simple pattern that works on the stubbed DataTooltip.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-l-2` (round 13, decomposition v13; serves FWD-13, FWD-15)

The CTO's ruling 2 (round-12 analysis): "FWD-13 binds the Model tab's fiscal cells: each fiscal figure carries its unit and tabular
numerals, and a tooltip with its mnemonic and full-precision value, exactly as the header does." Round 12 (AV-m-3) gave the header
cards and What-moved lines that tooltip: `FigureTooltip` / `figureTooltipRows` in `components/StatTile.tsx` render an element with
`role="tooltip"`, `data-figure-tooltip="<MNEMONIC>"` and the served value verbatim in `data-full-value`, holding the estate
`DataTooltip`. Each served fiscal figure of the /thesis bundle's `fiscal_year_figures` carries `unit` (MILLIONS, PERCENT, PER SHARE
..., RATIO ..., PRICE ..., MILLIONS (share count), UNRESOLVED ...) and a `currency` (sometimes empty). Build, in
`portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx`:
1. **Each served fiscal cell** (`ModelCell`, `[data-model-cell]` in a `[data-model-row]`) keeps its tabular numerals and its
   `data-model-cell` / `data-model-year` attributes, and gains the header's tooltip: `FigureTooltip` naming the row's mnemonic, with
   `data-full-value` = String(served value) verbatim, shown on hover.
2. **Each served row says its unit in words**, from the served `unit` (and the served `currency` where every figure of the row
   carries the same one): e.g. "EPS (USD per share)", "Revenue (USD millions)", "Operating margin (%)", "P/E (multiple)", "Diluted
   shares (millions of shares)"; a row whose figures carry no currency says so ("millions, currency not stated"); an UNRESOLVED unit
   reads "unit not resolved". A refused row is unchanged.
3. **No contract-code token in visible text:** Opal's rule-case lines print a served reason; a reason such as "no cases on the landed
   block (derived before C-MODEL-WINDOW-AND-ROWS (5))" shows no "C-MODEL..." token -- the visible sentence drops the parenthetical
   code; the served reason stays whole in `data-model-case-reason`.
4. Nothing else moves: the served values, the rows and their order, the refusal sentences, the header and What-moved (round 12).

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: the unit is the served
unit in words; nothing is converted or computed. **Design law (portal `DESIGN.md`):** a code, field name or path may sit in a data
attribute or in a tooltip FWD-13 names, never in visible text.

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
portal/src/pages/SecurityAnalysis/components/StatTile.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~50/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md`, `portal/src/components/DataTooltip.tsx`, and the issuer's checks and
fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-l-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/fiscal.cjs"; echo "exit=$?"</invocation><expect>FISCAL FIGURES CARRY UNIT AND TOOLTIP: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-l-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/bound.cjs" Q2 modelPattern.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>Q2 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-l-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-l-2" judgment="true"/>
</proof_of_spec>

AC1 is BA's built Model tab on the SERVED /thesis (342 fiscal figures): each served cell tabular with a tooltip naming its mnemonic
and the served value verbatim; each served row saying its unit; 0 raw floats; a labelled planted case reason showing no contract
code. AC2 is the bound on every harness that loads the Model tab; AC3 no control byte. Also keep round 12's figures check green:
`node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/figures.cjs"` must still read 3 of 3 (report
its line). AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk (BA's Model tab), never self-graded: a PM
reads each fiscal figure's unit and can open any cell to its mnemonic and full value (FWD-13, FWD-15). Portal typecheck, if you run
one: `node_modules/.bin/tsc -b --noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~50/DSGN_AMGTV1.TO-AV-l-2.fiscal-figures-carry-unit-and-tooltip.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion (and figures.cjs), the portal and outer commit hashes, and any
row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 13 = the round-12 analysis s.4 item 2 with ruling 2, plus ruling 3's "derived before C-MODEL-WINDOW-AND-ROWS
(5)" token (on the Model tab, so this cell owns it). Base ba62e945: fiscal.cjs 0 of 3; green r13-green-b @49771e9c 3 of 3. StatTile.tsx
granted for the tooltip import; the green arm needed ModelTab.tsx only.

<status>pending</status>
<round>13</round>
<slot>~50</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
