# DSGN_AMGTV1 task order -- `AV-f-3` -- THE LEAD PANEL HEADER LOOKS LIKE THE REST OF THE PORTAL

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-f-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~56</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV a41cf763 -- panelhead.cjs 2 of 3 (FAIL as expected: visible title "Lead Panel", no card-face header, Starred a hand-built button; arm 2 the negative and arm 3 the hex/shade mutants PASS by design); green arm (scratch r15-green-b @69653d85) 3 of 3, tsc -b rc=0. Blind spots: the search input is not counted as a hand-built control (the estate has no input control to require); rgb()/hsl() numbers are not linted.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-f-3` (round 15, decomposition v15; serves FWD-23)

The CTO's round-14 analysis s.3 row 3, the panel half (PRD v0.6 FWD-23). This order follows AV-f-2 on the same worktree AND starts
from a worktree that has merged CLOUD/DEV after chain ~57 (AV-f-6, the shared `GraphicCard`) drained -- the issuer merges it into your
branches before you start; keep AV-f-1/AV-f-2's work whole. Build in `portal/src/pages/SecurityAnalysis/components/`:
1. **`LeadPanel.tsx`:** the panel header renders through the shared `GraphicCard` card face (`@/ui/components/graphic/GraphicCard`);
   its visible title is a person's title (e.g. "What is moving"), never the internal name "Lead Panel" (no "Lead Panel" / "lead-panel"
   anywhere in visible text); the Starred filter is the shared `Segmented` control, not a hand-built button; 0 hand-built `<button>`
   in the header actions.
2. **`LeadPanel.tsx`, `PriceBars.tsx`, `ChatterBubbles.tsx`:** 0 hard-coded hex colour literals and 0 raw Tailwind palette shades;
   colours from `lib/chartColors.ts`.
3. **ISSUER AMENDMENT 1 (row DSGN_AMGTV1-Z-W56-S2; ruling R5 "no other views for chatter"):** in `LeadPanel.tsx`, "Starred only"
   on the Chatter subject filters the BUBBLES (it never renders `StarredList` or any list), and the chatter face never renders the
   ranking `SourceCaption` (its footer is the bubbles' own source line). The price face's Starred filter stays as AV-f-1 built it.
4. **ISSUER AMENDMENT 2 (CONTRACT amendment 2 @5ca1a00f56, CTO msg 27571):** the live route returns ALL covered names (95; most with
   an empty `by_month`). `ChatterBubbles.tsx` sizes bubbles only for names with a count in the cursor's month and prints the
   denominator beside the chart: "<k> of <n> covered names have collected articles this period" (k = names with a count in the
   month, n = all served rows). A missing `by_publisher` key means "none collected" -- never a printed zero. `bubbles.cjs` (AC2)
   now grades the denominator line on a fixture of 22 rows (10 with an empty `by_month`, zero publishers dropped).

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Granted harness change (exact, tested on the green arm):** `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/fixtures/r15b.grant.leadPanelPattern.harness.cjs.diff` -- its
`starred_toggle` check reads the Starred `Segmented`. Apply with `git -C portal apply` (re-fit the hunk to AV-f-1's re-anchored file
if it does not apply clean; the claim stays the same). No other harness may change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. A harness listed in `<paths>` changes ONLY by its granted diff (re-anchor, never a deleted
   check).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte;
   AC3 scans for it).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/components/PriceBars.tsx
portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~56/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-f-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/panelhead.cjs"; echo "exit=$?"</invocation><expect>THE LEAD PANEL HEADER LOOKS LIKE THE PORTAL: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-f-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bubbles.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/pricebars.cjs"; echo "exit=$?"</invocation><expect>CHATTER IS BUBBLES BY MONTH: 3 of 3 arms, then PRICE IS RANKED BARS, ONE FORM: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-f-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" F3 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>F3 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-f-3" judgment="true"/>
</proof_of_spec>

AC1 renders LeadPanel: no internal name in visible text, the header through the card face, Starred a Segmented, 0 hand-built header
buttons, 0 hex and 0 raw shades in the three files; arms 2-3 the negative and the planted mutants. AC2 keeps the bars and bubbles green.
AC3 the harness bound. (Run the round-14 bytes.cjs too and report its line.) AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the
close-render PNG beside /philosophy: the panel and the selected-name header read as one card family with the portal.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~56/DSGN_AMGTV1.TO-AV-f-3.lead-panel-header-looks-like-the-portal.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** AMENDED before hand-over (items 3-4, rows Z-W56-S2 and CONTRACT amendment 2; bubbles.cjs arm 1 + mutant 'nodenom' amended by the issuer; graded by to-pipeline-gate on modification: GATE (viii) placeholders only).  analysis s.3 row 3, panel half. Third on chain ~56, AND after chain ~57 drains (it imports AV-f-6's GraphicCard): the issuer hands it to slot ~56 only after merging ~57 into CLOUD/DEV and into the ~56 branches. Base: panelhead 2 of 3; green 3 of 3.

<status>complete</status>
<round>15</round>
<slot>~56</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
