# DSGN_AMGTV1 task order -- `AV-g-3` -- THE RENDER INSTRUMENT SEES THE PRICE AND CHATTER FACES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-g-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~61</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV 209678ff -- instrument.cjs (FAIL as expected: no chatter fixture, no price-face capture, fwd18 grades the removed Movement control, the band looks for "Lead Panel", fwd19 misses list/loading); green arm (scratch r16-green-g, an issuer-spawned helper) in progress at the cut -- the issuer hands this order only after it reads 3 of 3. Blind spots: only the Universe (list) state is run; renderCheck.tsx's "Lead Panel" substring is not graded.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-g-3` (round 16, decomposition v16; serves FWD-20, FWD-21, FWD-22)

The CTO's round-15 analysis s.4 row 3 and ruling 2 (the render instrument must see the demo faces before any face is graded again).
THE CONTRACT (quoted from `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/instrument.cjs`): the instrument is `portal/scripts/ui-contract-check.mjs` (+ `scripts/ui-measure.mjs`)
and its fixture set `portal/src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json`. Run as `ui-contract-check.mjs --dist <build> --out <dir> --states
list --states-sweep`:
- the fixtures serve `/api/scoped/amgt/lead-panel/timeseries/collected/chatter` with EXACTLY the payload of
  `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/fixtures/r16g.collected.chatter.json` (AMGT_RESAPP's live shape: 95 covered names, 73 with an empty by_month, by_publisher only
  publishers with >= 1 article), and the trending price ranking the Price face reads;
- the sweep writes `<out>/list-price.png` + `.json` (the Price segment clicked; `expectLine` for `[data-price-bar]`) and
  `<out>/list-chatter.png` + `.json` (the Chatter face; `expectLine` for `[data-bubble]`, and the denominator line
  "<k> of 95 covered names" via `[data-chatter-denominator]`);
- grades.json `states.list.fwd18_controls` PASS with the Movement clause retired (ruling R6) and `states.list.bandIsIdentityHeader`
  PASS, the band anchored to the new header card (`[data-panel-header]`);
- `run.fwd19_designedStates.value.missing` names no `list/` entry (list's loading = the chatter read held).
If the chatter face needs `data-chatter-denominator` on its denominator line, add that attribute in `portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx`
(attribute only). **Walker rule (CTO msg 27641):** do NOT run `.claude/skills/ui-walk/walk.mjs` or `ui_walker_account.py arm|disarm|secret` -- the one walker account is shared across two devices; no criterion here needs a walk.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Harness changes:** `errorEmpty`, `leadPanelPattern` and `tabs` may change ONLY to re-anchor a claim the new fixtures move (the same fact,
never a deleted check); AC3's bound grades them.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. A harness listed in `<paths>` changes ONLY by its granted diff (re-anchor, never a deleted
   check).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte;
   AC3 scans for it).

## 3. SURFACES

<paths>
portal/scripts/ui-contract-check.mjs
portal/scripts/ui-measure.mjs
portal/src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json
portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx
portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~61/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-g-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/instrument.cjs"; echo "exit=$?"</invocation><expect>THE RENDER SEES THE DEMO FACES: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-g-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bubbles.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/pricebars.cjs"; echo "exit=$?"</invocation><expect>CHATTER IS BUBBLES BY MONTH: 3 of 3 arms, then PRICE IS RANKED BARS, ONE FORM: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-g-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" G3 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>G3 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 vite-builds your portal, runs YOUR instrument on it (--states list --states-sweep) and requires every clause above; arm 2 the base
instrument on the same build fails; arm 3 five planted defects in the build (a 7px font, a purple-filled Subject segment, a renamed
data-panel-header, a renamed data-price-bar, changed denominator words) are each caught by your instrument. About 5 minutes. AC2 keeps the
bars and bubbles green. AC3 the harness bound. The PNGs it writes are the L9 inputs for the next close.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~61/DSGN_AMGTV1.TO-AV-g-3.the-render-sees-the-demo-faces.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** AMENDED before hand-over: instrument.cjs arm 3 tightened by its helper (missing face captures no longer count as catches); re-run base 1 of 3 (279 s), green r16-green-g @3c64bf13 3 of 3 (297 s: 32 bars, 18 bubbles, '18 of 95 covered names', 5 of 5 planted caught). GATE viii only.  analysis s.4 row 3 (ruling 2). Chain ~61 alone. Helper G's green arm was in progress at the cut; the issuer reads it 3 of 3 before the hand-over (or amends the contract with the gate limb named).

<status>pending</status>
<round>16</round>
<slot>~61</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
