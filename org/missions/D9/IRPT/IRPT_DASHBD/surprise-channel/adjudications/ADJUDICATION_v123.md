# IRPT_DASHBD: CVO adjudication, round 121 (workstream F-SHIP, ~F2): the class-series reader, not mounted

<sweep_watermark>2026-10-16T03:22Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T03:22Z, on msg 8983 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R121_F.md` @5ebb62fbff, blob 561d584ee9). Not B-IN's or B-49F's round 121. One LOCAL order, TO-DB-f-801 (worker ~801; record merged 6efa66552c, in HEAD). No judgment criterion. Both criteria target the CANDIDATE portal tree (the checker runs bun test in `<root>/portal` and diffs against the class candidate head): DBF121-1-AC1 and AC2 FAIL on the landed tree (no reader file there; the diff is DEV's) and PASS at the candidate head 6e0e4ab9 (scratch root, removed after). 2 of 2 PASS on the target tree; round-close MAY-CLOSE. The candidate is not in origin/DEV or origin/PROD (git -C portal merge-base). No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S61",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T03:22:00Z",
  "one_line": "Round 121 F-SHIP (~F2): the class-series reader, two new portal files on an unpushed candidate. WHAT IT DOES AGAINST THE LIVE SERIES TODAY: nothing reaches a page. Nothing imports readClassSeries (census of the candidate's src: only the reader and its test name it), it is not mounted, and it requests nothing by itself. If it were called, the route has no class_series member: comp-find 'class_series' over 108,066 files finds no serving-route code, only producer samples, records and messages, so a call would come back as an envelope refusal or a failed fetch and the reader returns {kind: 'absent', reason}. It does not error and does not render. The live route was not called (it needs a signed-in session); this part is INFERRED from the code census. EMPTY-AS-REAL RISK, MEASURED: classSeriesToRows accepts a well-formed document with zero dates or zero classes (date [] or class_names [], with empty per-class objects) and returns kind 'served' with rows [] (probed at the candidate head). So once the reader is mounted, a page could show an empty class section as if it were real data, unless the mount treats served-with-no-rows as absent. Today that cannot happen (not mounted, nothing served). The mount cell needs a criterion that a served document with no class rows reads as absent with a reason, never as an empty table. Dismissed (3): D2-W801-S1 (a pre-existing lint error outside the grant), D2-W801-S2 (sparse-cone suite failures identical before and after), D2-W801-S3 (a committer identity set in the command environment only).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W801-S1",
   "IRPT_DASHBD-D2-W801-S2",
   "IRPT_DASHBD-D2-W801-S3"
  ],
  "spec_asserts": "Spine L9/L10: every terminal round is graded by the CVO before close; a criterion is re-run on the tree it targets. A value must carry its claim: an empty series is not a measured zero.",
  "world_is": "The reader exists only on unpushed candidate 6e0e4ab9, unmounted and unused. It refuses malformed documents whole, but it accepts an empty well-formed one as served with no rows. No class object is served, and the series contract at HEAD is 0.2.0 with no class_object section.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T03:1xZ: DBF121-1-AC1, AC2 FAIL on the landed tree (dd4897fd22); PASS with <root>/portal at 6e0e4ab9756f (scratch worktree, removed); round-close --round 121 MAY-CLOSE",
    "bun probe at 6e0e4ab9: classSeriesToRows({...header, date: [], class_names: [], coverage: [], market_value_eod: {}, class_return_daily: {}}) -> rows []; with two dates and no classes -> rows []",
    "comp-find 'class_series' --files: DENOMINATOR 42 hits across 108066 files scanned; no route or handler member",
    "git -C portal merge-base --is-ancestor 6e0e4ab9 origin/DEV and origin/PROD: not an ancestor of either",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R121_F.md blob 561d584ee9 (msg 8983)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Three INERT worker rows. The empty-as-real finding is not dispositioned here: it is a criterion the mount cell owes, carried to the CTO in the slug."
 }
]
```
