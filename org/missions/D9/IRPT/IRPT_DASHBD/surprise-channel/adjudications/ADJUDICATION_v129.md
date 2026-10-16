# IRPT_DASHBD: CVO adjudication, round 125 (workstream F-SHIP, ~F2): the transactions table view model, not mounted

<sweep_watermark>2026-10-16T05:52Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T05:52Z, on msg 9105 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R125_F.md`, no commit named in the message; resolved by git log -1 on the path to 0e52d651a0, blob ae50debf8d). Not B-IN's or B-49F's round 125. One LOCAL order, TO-DB-f-1101 (worker ~1101; record merged 85d5f4516c, in HEAD). No judgment criterion. Both criteria target the CANDIDATE portal tree: DBF125-1-AC1 and AC2 FAIL on the landed tree (no portal files there) and PASS at candidate head ee30038f (scratch root, removed after). The candidate is not in origin/DEV or origin/PROD. round-close --round 125 --workstream ~F2 MAY-CLOSE. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S67",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T05:52:00Z",
  "one_line": "Round 125 F-SHIP (~F2): a pure view model for the transactions table (filter, search, sort, CSV export with formula guard, windowing); nulls stay null, never zero. UNMAPPED AND UNRATIFIED WORDS, probed at the candidate head: the module names no word and passes txn_type through as written. A row whose type is UNMAPPED appears in the type filter as 'UNMAPPED' and can be filtered on (distinctTypes gave Dividend, Fee, UNMAPPED), so it is shown, not folded into another class at this layer. There is no 'pending ratification' marker, and none is needed now: the CTO RATIFIED the words in its round-124 analysis (160 codes at tran_srcde, 16 UNMAPPED; flow class ruled per code, W1001-S2), and ruled that UNMAPPED lines show as 'Other' with their count, never hidden. That rule belongs to the table component, not this module, so it is not built yet. One note for the component: 'Other' sits beside the ratified word 'Other income', and a reader can confuse the two; a label that says the code is not classified would keep them apart. EMPTY VS ZERO (as v123): the module has no served/absent state. viewRows([]) returns [] and exportCsv([]) returns the header line alone, so 'no transactions file served' and 'no transactions in the window' look identical here. When the table is mounted, the reader must carry served versus absent with a reason, or an absent file renders as a real empty table. Today nothing is mounted and nothing is served. Dismissed (3): D2-W1101-S1 (sparse worktree, row schema read at HEAD), D2-W1101-S2 (the holdings sort lives in components, idea copied), D2-W1101-S3 (a pre-existing lint error outside the cell).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W1101-S1",
   "IRPT_DASHBD-D2-W1101-S2",
   "IRPT_DASHBD-D2-W1101-S3"
  ],
  "spec_asserts": "Spine L9/L10: criteria re-run on the tree they target. CTO round-124 analysis: UNMAPPED lines shown as 'Other' with their count, never hidden. An empty series is not a measured zero (v123).",
  "world_is": "Two new portal files on an unpushed candidate (ee30038f), unmounted; no transactions file served; words ratified; the transaction contract not cut.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T05:4xZ: DBF125-1-AC1, AC2 FAIL on the landed tree; PASS with <root>/portal at ee30038f8456 (scratch worktree, removed); round-close-check --round 125 --workstream ~F2 MAY-CLOSE",
    "bun probe at ee30038f: viewRows([]) -> []; exportCsv([]) -> header line only; distinctTypes of rows typed Dividend/UNMAPPED/Fee -> [Dividend, Fee, UNMAPPED]; filterByType(UNMAPPED) -> 1",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_124_20261016.md line 32 (RATIFIED) and line 35 (UNMAPPED shown as 'Other' with its count)",
    "git -C portal merge-base --is-ancestor ee30038f origin/DEV and origin/PROD: not an ancestor of either",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R125_F.md @0e52d651a0 blob ae50debf8d (msg 9105)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Three INERT worker rows. The empty-vs-absent requirement and the 'Other' label note are for the mount cell, carried to the CTO in the slug."
 }
]
```
