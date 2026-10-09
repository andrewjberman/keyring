# DSGN_AMGTV1 task order -- `AV-zzj-1` -- DIRECT ACT: THE FILING PANEL DOES NOT SAY A BREAKDOWN IS ABSENT BESIDE A DRAWN TABLE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzj-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~123</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; two page files, rendered offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 against portal 2d42e9b7 (= origin DEV; the segment files are unchanged since fd345aef) -- r58a.cjs 2 of 4 (arm 1 FAIL: the served "no segment breakdown is shown" reason prints beside a drawn table; arm 3 FAIL: ThesisTab passes no tableServed; CONTROL and PLANTED pass). On a scratch reference edit, 4 of 4, then restored. battery29 ALL PASS at the base.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzj-1` (round 58, decomposition v58; serves FWD-27)

On the Thesis tab, `tabs/ThesisTab.tsx` draws `SegmentTable` (the served `segment_table`; drawn as a table when its `status` is
`"served"`) and then `SegmentBreakdown` (the filing's own segment text). When the filing breakdown has no rows,
`components/SegmentBreakdown.tsx` prints the served `reason` -- for AMD: "No filing analysis is stored for this name yet, so no segment
breakdown is shown. A segment table with figures needs a separate segment data pull." -- directly under a drawn segment table. The sentence
contradicts the table above it. Paths are under `portal/src/pages/SecurityAnalysis/`. Change nothing else.

1. `components/SegmentBreakdown.tsx`: add an optional prop `tableServed?: boolean`. When the breakdown has no rows AND `tableServed` is
   true, keep the section (`data-segment-breakdown`) and its heading, and replace the served reason with ONE short page sentence that does not
   say a breakdown is absent, e.g. "The filing text for these segments is not stored for this name yet." (no "no segment breakdown", no
   restatement of the reason). When `tableServed` is false or absent, print the served reason exactly as today. A breakdown WITH rows is
   unchanged either way.
2. `tabs/ThesisTab.tsx`: pass `tableServed={data.segment_table?.status === 'served'}` to `SegmentBreakdown`.

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY; keep each file's line endings exactly as you find them (read them first, for example
   `python -c "print(open(p,'rb').read().count(b'\r\n'))"`).
5. If a battery29 harness is anchored on markup this cell changes, file a row and stop on that criterion (no harness is in `<paths>`).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/SegmentBreakdown.tsx
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~123/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `components/SegmentTable.tsx` and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round58/checks/r58a.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzj-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round58/checks/r58a.cjs"; echo "exit=$?"</invocation><expect>THE FILING PANEL DOES NOT SAY A BREAKDOWN IS ABSENT BESIDE A DRAWN TABLE: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzj-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~123/DSGN_AMGTV1.TO-AV-zzj-1.filing-panel-beside-table.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY), and only
when every criterion passes. Before you flip, also run `cd portal && node node_modules/typescript/bin/tsc -b --noEmit` (expect no output)
and record it in the instance; a red tsc is not a pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W123-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the exact diff, the output line of every criterion and of tsc, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** `ledger/ROUND_ANALYSIS.round57.md` @fa37dc1b8a, enrichment item 1 (R2; RESAPP round-80 R4). Item 2 (the PROD promote) is
  not a cell. Check prepared @1b26096caa.
- **Andrew-direct ~05:0xZ-05:1xZ** (record `org/tier1_exec/2.0.0_SA_COO~D1/deliverables/ANDREW_DIRECT_20261009_051xZ_SECURITY_ANALYSIS_UI_WALK_SPINE_NEWS_DISCLAIMERS.md`
  @1725deb826) asks for a wider pass on the page (the news spine, the news presentation, the disclaimers). That pass comes from the
  running deep walk as a register + brief for the next rounds, and is not folded into this one-cell order.
- **Base:** portal 2d42e9b7 (origin DEV at the cut).

<status>pending</status>
<round>58</round>
<to_id>DSGN_AMGTV1.TO-AV-zzj-1</to_id>
<slot>~123</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
