# DSGN_AMGTV1 task order -- `AV-y-1` -- THE FIGURE TOOLTIP STAYS INSIDE ITS POP-UP AND SHOWS NO RAW CODE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-y-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~68</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV da0b3bd7 -- tipface.cjs 2 of 3 (FAIL as expected: CODE, ROWLABEL, CARRIER on both figures; arms 2-3 PASS by design). Blind spot: a static render has no layout, so the clip is graded only by the issuer's live walk of the Financials and Market Features pop-ups.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-y-1` (round 21, decomposition v21; serves FWD-13, FWD-1)

DIRECT ACT. The CTO's ruling msg 27914, on the walk 20261001T151253Z shot 009: in the header cards' Financials pop-up, the
figure tooltip (`FigureTooltip` in `portal/src/pages/SecurityAnalysis/components/StatTile.tsx`, `absolute left-0 top-full`) runs past the pop-up's bottom edge, and
its face reads "Enterprise value (CURR_ENTP_VAL)" with a "mnemonic" row. Two changes:
(1) THE CLIP: the tooltip stays inside its pop-up -- open it upward (`bottom-full`) or cap it to the container where it would cross the
pop-up's edge; the header cards on the band and the Model tab keep a readable tooltip.
(2) THE FACE: the tooltip's visible text shows the plain label ("Enterprise value"), the definition and the full-precision value -- never
the Bloomberg code. FWD-13 still holds: the mnemonic stays CARRIED in the markup as `data-mnemonic="<MNEMONIC>"` on the tooltip
element, not in its text. Apply the face rule in `FigureTooltip` and `figureTooltipRows` (and the same header in `StatTile`). Do not edit
`portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx` (AMGT_CORPUS's through the freeze); it inherits the face through `FigureTooltip`. Presentation only. Do not run
the walker.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Harness changes:** none. No harness may change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. A harness listed in `<paths>` changes ONLY by its granted diff (re-anchor, never a deleted
   check).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte;
   AC3 scans for it).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/StatTile.tsx
portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~68/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-y-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round21/checks/tipface.cjs"; echo "exit=$?"</invocation><expect>THE FIGURE TOOLTIP SHOWS NO RAW CODE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-y-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round20/checks/namecard.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/cardface.cjs"; echo "exit=$?"</invocation><expect>THE IDENTITY CARD SHOWS THE SERVED COMPANY NAME: 3 of 3 arms, then THE HEADER CARDS ARE THE PHILOSOPHY CARD FACE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-y-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; cd portal &amp;&amp; node node_modules/typescript/bin/tsc -b --noEmit &amp;&amp; cd .. &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" ALL leadPanelPattern.harness.cjs errorEmpty.harness.cjs tabs.harness.cjs shell.harness.cjs drafting.harness.cjs execFallback.harness.cjs execPattern.harness.cjs execText.harness.cjs peersCarry.harness.cjs peersPattern.harness.cjs peersReadFailed.harness.cjs modelPattern.harness.cjs posturePattern.harness.cjs thesisLadder.harness.cjs; echo "exit=$?"</invocation><expect>tsc rc 0 (no output), then ALL BOUND: 14 of 14 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 renders FigureTooltip on two figures (CURR_ENTP_VAL, EQY_BETA) through figureTooltipRows: the label, definition and full
value on the face, no capitals_underscore code and no "mnemonic" row, the mnemonic in data-mnemonic; arm 2 the pinned base; arm 3 planted
faces. AC2 keeps round 20's name and the card face. AC3 the TYPECHECK and all 14 harnesses (the Model tab inherits the face). The CTO's
acceptance read is the issuer's live walk: the Financials pop-up tooltip unclipped, no CURR_* code on its face.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~68/DSGN_AMGTV1.TO-AV-y-1.the-figure-tooltip-stays-in-its-popup-and-shows-no-raw-code.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (StatTile.tsx + HeaderCards.tsx if the flip needs it, LOCAL). CTO ruling 27914; walk clean by 21:30Z or drop. Base tipface 2 of 3 on DEV da0b3bd7.

<status>complete</status>
<round>21</round>
<slot>~68</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
