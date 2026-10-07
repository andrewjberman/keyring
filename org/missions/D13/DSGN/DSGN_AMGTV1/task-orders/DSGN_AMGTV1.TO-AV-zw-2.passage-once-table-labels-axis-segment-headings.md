# DSGN_AMGTV1 task order -- `AV-zw-2` -- THE PASSAGE ONCE PER PRESS, THE SERVED TABLE DRAWN WITH ITS COLUMN LABELS, READABLE AXIS TICKS, ONE HEADING PER SEGMENT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zw-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~107</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; page code and its checks only.
comp-iam: DECLARED-NOT-APPLICABLE -- no store, role or route changes; the page reads the same /thesis body it reads today.
comp-adversary: RUN by the issuer at the cut on portal DEV 34803ef6 -- r77_ba5.py AC1, AC2 and AC3 each read SERVED: NO with their controls passing (one press opens three blocks where points share an id; no table and no axis formatter; no segment heading). The check, its harness and its fixture were written and dry-run by 2.0.0_SA_COO~Z at portal DEV 13509c52 with the same three base FAILs.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; a captured fixture only.
</preflight>

**Your worktree:** `C:/tmp/wk-dsgn-amgtv1-107`. Its `portal/` is a nested checkout at portal DEV 34803ef6 on its own branch. Work and
commit only there. Start every shell call with `cd /c/tmp/wk-dsgn-amgtv1-107`: a call that starts elsewhere resolves
`git rev-parse --show-toplevel` to the base checkout.

## 1. THE CELL -- `AV-zw-2` (round 45, decomposition v45)

CTO ruling 6 (round-76 analysis @c8bbeeac10) and the walk's rows Z-W266-S2 and Z-W266-S3. All five repairs are on the security
page, in `portal/src/pages/SecurityAnalysis/components/`. The served data does not change.

1. **The passage renders ONCE per press** (`ThesisDriverChart.tsx`). Today the open state is the pressed point's passage id.
   Where several points cite one passage (ASML NA: three points, one id), one press opens a block under every point. Key the
   open state on the POINT, so one press opens one block under the pressed point, a press on another point moves it, and a
   second press on the open point closes it.
2. **A served table passage is drawn as a table** (`ThesisDriverChart.tsx`, with a new `PassageTable.tsx` beside it). A point may
   carry `passage_table: {columns: [...], rows: [{label, values: [...]}], heading, note}`. Draw it as a table: one column
   header per served column label, each row's label in the row, the figures in the order served, the `heading` above it and
   the `note` (when not null) below it in words. Compute, join or re-order nothing. A row may carry more or fewer figures than
   there are columns; draw what is served. When a point carries no `passage_table`, keep today's text block. Show
   `passage_table_reason` in words when it is served. The cite line stays.
3. **The y-axis ticks are readable** (`ThesisDriverChart.tsx`). Give the chart's `YAxis` a `tickFormatter`: a large figure reads
   short (393,421,721 as about "393.4M"), a small figure is exact (528 reads "528"), and the axis is wide enough that no tick
   is clipped.
4. **One heading per segment** (`SegmentBreakdown.tsx`). The served rows each carry `segment`. Today the label is printed on
   every row and the rows interleave (BA: 11 rows under 3 labels). Group the rows by `segment`, in the order each segment is
   first served. Print the segment's name ONCE as that group's heading and its rows beneath it. The rows keep their text, their
   closed Source disclosure and their served order inside a group. A row's `segment_reason`, when served, is shown once
   under its heading.

5. **A refused chart reads its reason** (`ThesisDriverChart.tsx`). A producer cell in another lane refuses a share-count figure as a driver
   chart; the route will then serve the chart `status: "ABSENT"` with `plain_reason`, a sentence written for a reader. When
   an ABSENT chart carries `plain_reason`, show that sentence in place of the default message. The existing `reason` field
   is system text and stays in the data attribute, never in visible text. An ABSENT chart with no `plain_reason` keeps
   today's message. A refused segment breakdown needs no page change: it serves no rows and its `reason`, which the page
   already shows.

**The contract the check reads.** Keep these attributes:
- the pressed element carries `data-driver-chart-passage-link` and its `onClick`, and `aria-expanded`;
- each OPEN passage block carries `data-driver-chart-passage-source`;
- the table is `<table data-driver-chart-passage-table>` with a `<th>` per column label;
- each segment heading carries `data-segment-heading`, and each row keeps `data-segment-row`;
- the open state stays in React state (`useState` or `useReducer`).

**The existing harnesses** under `portal/src/pages/SecurityAnalysis/__harness__/` assert on today's markup. Run the ones that
name `data-driver-chart` or `data-segment` (`node <file>`), and re-anchor only the assertions your change moves. Say which.

**A render for the review.** Write `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~107/RENDER_ZW2.md`: for BA (a table passage, three ids) and ASML NA (one shared id), the page's
rendered text of the driver chart after one press and of the segment breakdown, from the fixture
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_groupB_fixture.json` (the deployed /thesis bytes of four names).

## 2. BOUNDS

1. Write only the paths below. No server, no fetch, no network, no install, no push, no deploy, no store write. REFUSE, do not rescue.
2. Do not edit `App.tsx`, `SecurityAnalysis.tsx`, the Thesis tab's layout or any other component. A sibling cell is writing
   `SecurityAnalysis.tsx`, `components/SecurityOverlay.tsx` and `hooks/useLeadPanelApi.ts`.
3. Presentation only: no number is computed, joined, rounded in the table or rewritten. The axis formatter is the one place a
   figure is shortened, and only on the axis.
4. Colours and type come from the design system's tokens already used in these two files. No new colour.
5. Plain words on the page; no internal names (identity, security key, crosswalk, dossier, model block, input ledger, passage id).
6. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/ThesisDriverChart.tsx
portal/src/pages/SecurityAnalysis/components/PassageTable.tsx
portal/src/pages/SecurityAnalysis/components/SegmentBreakdown.tsx
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~107/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zw-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba5.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>one press opens ONE passage where three points share an id, a press on another point moves it, a second press closes it, and the three-id control opens one; C1-C5 PASS; R77 BA5 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zw-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba5.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>BA's served table is drawn with its six column labels, both row labels and every figure; the no-table control draws none; the y axis formats a nine-digit figure in 7 characters or fewer and keeps 528 exact; an ABSENT chart shows its served plain reason; C1-C10 PASS; R77 BA5 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zw-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba5.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>BA's 11 rows sit under 3 headings in first-served order, each name alone once; the one-label and no-row controls hold; C1-C6 PASS; R77 BA5 AC3 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-zw-2" judgment="true"/>
</proof_of_spec>

AC4 is the CTO's judgment on the render (a portal candidate is reviewed from a render), not a fourth mechanical check.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~107/DSGN_AMGTV1.TO-AV-zw-2.passage-once-table-labels-axis-segment-headings.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W107-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ) and
`disarm_owner` `2.0.0_SA_COO~D`.
Report once: the exact diff, the output lines of every criterion, the portal and outer commit hashes, the existing harnesses you
ran and which assertions you re-anchored, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** AMGT_RESAPP `ROUND_ANALYSIS.round76.md` @c8bbeeac10 ruling 6 and ADDENDUM 1 item 4 @a7b2c3e0ba (CTO msg 30491); rows
  AMGT_RESAPP-Z-W266-S2 and Z-W266-S3. Re-pointed by `2.0.0_SA_COO~Z` (msg 30485): its draft order, check, harness and fixture at
  `deliverables/2.0.0_SA_COO~Z/round77/handoff_dsgn/` and `round77/checks/r77_ba5*` @7daf7c5677. The act text is that draft's, unchanged
  except for the lane, the slot and the paths.
- **Battery:** this order holds three mechanical criteria; battery29 runs on the combined candidate at the drain (issuer).
- **Disjoint from `AV-zw-1`:** that cell owns `SecurityAnalysis.tsx`, `SecurityOverlay.tsx`, `hooks/useLeadPanelApi.ts` and its new files.
  Both orders name `__harness__/`; zw-1 touches `posture.harness.cjs` only, zw-2 the harnesses naming `data-driver-chart` or
  `data-segment`.
- **Issued by hand, no loop.**

<status>pending</status>
<round>45</round>
<slot>~107</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
