# DSGN_AMGTV1 task order -- `AV-zn-2` -- REPAIRS: THE LIST READS AT 11PX; THE TOOLTIP NAMES ITS HEADLINE; NO ZERO MOVE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zn-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~98</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically from fixtures captured on the deployed route.
comp-adversary: RUN by the issuer at the cut on portal 35a723bf -- repairs36.cjs 2 of 5 (arm 1 FAIL: Chatter 30/90/365D carry 39/47/51 label sizes 8-10.5px and one 5px radius; arm 2 FAIL: BA 09-28/09-29/09-08 print the coverage event's headline under "Strongest headline" while the day read is pending; arm 3 FAIL: 3 rows print "-0.00%"/"+0.00%"; KEEP 6/6 and PLANTED 9/9 pass). It reads 5 of 5 with a scratch reference fix loaded through CHECK_SRC_OVERRIDE.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zn-2` (round 36, decomposition v36; a batched repair cell; serves FWD-20, FWD-5 and FWD-27)

Three faults in `portal/src/pages/SecurityAnalysis/components/`. The check names every offender at base.

1. **The chatter collage's labels read below 11px, and the legend swatch has a 5px radius (FWD-20: no size below 11; radii within
   {2, 3, 4, pill}).** In `ChatterBubbles.tsx`:
   - `:264-266` labels beside a bubble step `fs` 10, 9, 8;
   - `:269` shortened labels use `fs` 9 and 8;
   - `:359` labels inside a bubble step down to `fs >= 8`;
   - `:401` the last-resort label is `const fs = 8`;
   - `:653` the legend swatch has `borderRadius: 5`.
   Requirements:
   - No label renders below 11px at 30, 90 or 365 days.
   - The swatch radius is one of 2, 3 or 4px.
   - Keep round 34's rules: no label box meets another label or another bubble, no leader line crosses another label, every label
     stays inside the viewBox, a label that cannot be placed may drop, every bubble keeps its hover, the layout stays deterministic,
     and a shortened label's `<g>` carries a `<title>` with the full served name.
   **Warning, measured at the cut:** raising the floor to 11 on its own breaks the round-29 collage check (7 of 95 bubbles end up
   with no label on the month view), and labels34 runs it as a KEEP. The scratch reference fix needed four more changes, which you
   may use or replace:
   - fill density 0.5 -> 0.42;
   - a retry that caps the length of labels beside a bubble when any bubble is left unlabelled;
   - a fix to the three-character shortening, which printed "NU..." for "NU Holdings Ltd";
   - a finer search grid for the last-resort position.
2. **The timeline tooltip names a headline that is not the day's strongest (FWD-5).** In `TimelinePanel.tsx` (`:362-368`):
   `const strongest = body?.articles?.[0]?.headline ?? covering?.lead_headline ?? null`. Until the day route answers, the tooltip
   prints the covering coverage event's lead headline under "Strongest headline".
   - While the day read is pending, print no headline under "Strongest headline"; "Strongest headline: loading" is fine.
   - If the coverage event's headline is shown, show it under its own label, for example "Coverage event:".
   - Once the day read answers, "Strongest headline" carries the day route's first article headline, as now.
3. **What changed prints a zero move with a sign (FWD-27).** In `model/WhatChangedPanel.tsx`, a percent move that rounds to zero
   at its printed precision prints "-0.00%" or "+0.00%" (BA capital expenditure 2027 -3,979.67 -> -3,979.78; free cash flow
   2027/2028).
   - Such a move prints "0.00%" with no sign, or "<0.01%" with its sign.
   - No cell prints "-0.00%", "+0.00%", "-0.0%" or "+0.0%".
   - The round-35 rules stay: every line named, "unchanged at this precision" on equal prints.

**Contracts:**
- C-PRESENTATION-ONLY: served values are formatted, never changed.
- No hard-coded colour outside `lib/chartColors.ts` tokens and the panel ink tokens the files already use.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file. Keep each
   file's existing line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
portal/src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~98/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zn-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round36/checks/repairs/repairs36.cjs"; echo "exit=$?"</invocation><expect>THE LIST READS AT 11PX, THE TOOLTIP NAMES ITS HEADLINE, NO ZERO MOVE: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zn-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

The KEEP arm inside repairs36.cjs runs round 35's changed35, cloud35 and payload35, round 34's labels34 and repairs34, and round 29's
timeline/chart.cjs. Each must exit 0. battery29 includes the CI's ESLint step.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~98/DSGN_AMGTV1.TO-AV-zn-2.repairs-list-type-tooltip-zero-move.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W98-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Sources:** ROUND35_CLOSE.md section 4 items 2-4; the round-35 close walk's fwd5-timeline-hover FAIL; the reference re-anchor's
  list-state reading (sizes 8/9/10, radii 5px).
- **Census only, not cut:** RankedChart.tsx `:237/:250/:256` `fontSize: 10` ticks (not mounted on the list state); shared
  `PanelContent.tsx` `rounded-b-lg` (8px, a shared component, the estate's).
- **Sequencing (CTO msg 29279):** AMGT_CORPUS's round-36 candidate is on ModelTab.tsx and modelSheet.ts; this cell touches neither.
- **Not graded here** (the issuer's close walk): how the collage reads at 11px; the tooltip while loading in a browser.

<status>pending</status>
<round>36</round>
<slot>~98</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
