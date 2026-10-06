# DSGN_AMGTV1 task order -- `AV-zv-1` -- A DRIVER-CHART POINT OPENS ITS SERVED PASSAGE; THE SEGMENT BREAKDOWN IS ON THE PAGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zv-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~105</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; portal page files graded offline on fixtures the issuer captured from the deployed API.
comp-adversary: RUN by the issuer at the cut on portal DEV b0051830 -- r44.cjs 1 of 5 (arm 1 FAIL: BA's 2023 point prints "The filing passage for this point is not shown on this page."; arms 2-3 FAIL: no SegmentBreakdown component; arm 4 FAIL: ThesisTab does not mount it; PLANTED passes). 5 of 5 on scratch reference edits via CHECK_SRC_OVERRIDE.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zv-1` (round 44, decomposition v44)

The deployed producer serves two things the Security Analysis page does not draw.

**(a) FWD-18: a driver-chart point opens its served passage** (`src/pages/SecurityAnalysis/components/ThesisDriverChart.tsx`).
- Each served `thesis_driver_chart.points[]` entry carries:
  - `passage_id`;
  - `passage_text` (the filing passage);
  - `passage_cite: {accession, location}`, e.g. `location`: "ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS / TABLE 2023".
- Today the component resolves the id only against `drafted_sections`, so a click on any BA point shows "The filing passage for this
  point is not shown on this page."
- Change the opened passage to read, in this order:
  1. the point's served `passage_text`, followed by its `passage_cite.location` in words, as a cite line in the same opened block;
  2. else the `drafted_sections` record, as today;
  3. else the existing sentence.
- Keep the "no passage carried" line for a point with no `passage_id`.
- Keep the link, the toggle and the chart.

**(b) FWD-1: the served segment breakdown on the page** (a NEW `src/pages/SecurityAnalysis/components/SegmentBreakdown.tsx`,
mounted in `tabs/ThesisTab.tsx`).
- The `/thesis` bundle serves `segment_breakdown: {rows: [{segment, text, cite}], reason, source: {form, filing_date, ...}}`. BA has
  11 rows; MSFT has `rows: []` with a plain `reason`.
- Export `SegmentBreakdown: FC<{ breakdown?: <that block> | null }>`:
  - **No block:** render nothing (null).
  - **Rows present:**
    - the root carries `data-segment-breakdown` and `data-segment-state="SERVED"`;
    - one element per row carrying `data-segment-row`, with the `segment` (bold, navy) and its `text` at rest;
    - the row's `cite` VERBATIM inside a CLOSED `<details data-segment-cite>` with summary "Source". The served cite names a
      passage id, which may not sit on the visible face (FWD-11 v0.8: a closed provenance block is not the face);
    - one source line in words: "From the 10-K filed January 30th, 2026." (use `longDate` from `../dateWords`).
  - **No rows:** the root carries `data-segment-state="REASON"` and the served `reason` as the shared `PanelEmpty` message.
- The look is the page's light card family: hairline border, navy ink, Lato. Give it a small header, "Business segments -- from the
  filing".
- **Mount:** in `ThesisTab.tsx`, directly under the driver chart's block and above `<ThesisCards ...>`, render
  `<SegmentBreakdown breakdown={data.segment_breakdown} />`.
- **Types:** declare `segment_breakdown` on the thesis bundle type, and the point's optional `passage_text` / `passage_cite`, in
  `types.ts`.

**AMENDMENT 1 (issuer, 2026-10-06 ~06:3xZ): the drafting harness stubs the new import.**
`src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs` stubs each ThesisTab import by name (ThesisDriverChart at ~:98) and throws
`Cannot find module '../components/SegmentBreakdown'`. Add ONE stub beside the others:
`name === '../components/SegmentBreakdown'` returning `{ SegmentBreakdown: () => null }`. Change nothing else in that file.

**AMENDMENT 2 (issuer, 2026-10-06 ~06:3xZ): the segment card is NOT part of the drafted thesis.**
`ThesisTab.tsx` renders its body in two branches on `served` (`drafting_status === 'SERVED'`). A name with no drafted thesis (MSFT:
`ABSENT`) never reaches the branch that holds `<SegmentBreakdown ...>`, so its served segment reason never shows (issuer walk on the
candidate, read-20261006T061411Z). Move the ONE mount out of the `served` branch:
`{!isLoading && !isError && data && <SegmentBreakdown breakdown={data.segment_breakdown} />}`. Place it directly ABOVE the
`{!isLoading && !isError && data && served && (` branch, so it shows for a drafted and an undrafted name alike. Remove the old mount.
AC1's arm 4 now refuses a mount under the `served` branch.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the paths below change. Presentation only: no served value is changed, computed or rewritten.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool for existing files; Write for the one new component; keep line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/ThesisDriverChart.tsx
portal/src/pages/SecurityAnalysis/components/SegmentBreakdown.tsx
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~105/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zv-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round44/checks/r44/r44.cjs"; echo "exit=$?"</invocation><expect>A DRIVER-CHART POINT OPENS ITS SERVED PASSAGE; THE SEGMENT BREAKDOWN IS ON THE PAGE: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zv-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~105/DSGN_AMGTV1.TO-AV-zv-1.driver-passage-and-segments.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W105-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **AMENDMENT 2 (~06:3xZ):** the walk on candidate fdf63a4b read MSFT with no segment card. The mount sat under ThesisTab's
  `served` branch, which was the issuer's own spec gap. r44 arm 4 is tightened: 4 of 5 on fdf63a4b, 5 of 5 with the mount moved
  (scratch reference). The order is re-opened.
- **AMENDMENT 1 (~06:3xZ):** on ~105's AC2 red (row Z-W105-S1, BLOCKING, ARMED, disarm_owner this seat), granted
  drafting.harness.cjs for the one-line stub of the new ThesisTab import. The row disarms when AC2 reads ALL PASS. No gate limb graded
  this modification (to-pipeline-gate fires on new orders only).
- **Source:** AMGT_RESAPP `ROUND_ANALYSIS.round73.md` @cf0d03deb2 item 1 (msg 29921); rows Z-W251-S1 and Z-W251-S2.
- **Base:** the round-43 candidate (portal c123c5a0 = DEV bacc2a22 + round 43), so rounds 43 and 44 go to Andrew as ONE DEV push, per the
  analysis.
- **Issued by hand, no loop.**

<status>complete</status>
<round>44</round>
<slot>~105</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
