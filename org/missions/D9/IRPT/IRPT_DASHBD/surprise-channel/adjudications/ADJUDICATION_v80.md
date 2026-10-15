# IRPT_DASHBD: CVO adjudication, round 115 (workstream ~F2, F-SHIP)

<sweep_watermark>2026-10-15T04:47Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T04:47Z, on msg 8047 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R115_F.md` @665b278c9c, blob ad8af87450; drain @06100e8539). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). No judgment criterion (one LOCAL cell). Re-run here: all three DBF115-1 criteria FAIL on the landed tree by construction (the portal code is only on the unpushed branch, as in round 114, v74). On a detached portal worktree at the worker's own head 476f8388 all three PASS, bun tests included. At the candidate head 506a2302 (`cand/dell2/irpt-default-performance-report`, also now the head of `wk-IRPT_DASHBD-503-portal`) AC1 and AC2 PASS and **AC3 FAILS**: `files changed outside the grant: ['src/pages/InvestorReporting/index.tsx']`, the issuer's own two-line hookup commit on top of the worker's branch. The proof instance VALID; `round-close-check --round 115 --workstream ~F2` MAY-CLOSE. 4 rows dismissed below, 1 ARMED among them. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S17",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T04:47:00Z",
  "one_line": "Round 115 ~F2 (the export mount of the filled report, inert until served). DBF115-1-AC1..AC3 PASS re-run here at the worker's head 476f8388; at the candidate head 506a2302 AC3 FAILS on the grant clause because the issuer's hookup (index.tsx, +2 lines) sits on the branch the candidate ref names, so the candidate as it would be registered does not pass its own criterion as written. That is an issuer act outside the cell, not a worker defect; it needs an amendment of AC3's grant or a note that AC3 grades 476f8388. Dismissed (4): D2-W503-S1 (ARMED, owner ~F2; the export gate opens on the reader's served answer, not on an availability a filled report lacks; the issuer's ruling holds in code: reportRead.ts line 107 returns served only when isFilledReport passes, else absent REPORT_UNREADABLE, and ExportButton.tsx lines 161 and 236 open the gate only on that served answer; its second ground, the route's scope check, is design, not code, since the route (IB-pr-554) is cut but not built; accepted as inert until a route serves), D2-W503-S2 (the entry admits client as a print key), D2-W503-S3 (FILLED_REPORT sits in a doc comment in submit.ts, which the checker requires), D2-W503-S4 (a client print with no served report shows the missing-payload panel, not a worded refusal; later polish).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W503-S1",
   "IRPT_DASHBD-D2-W503-S2",
   "IRPT_DASHBD-D2-W503-S3",
   "IRPT_DASHBD-D2-W503-S4"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug; a worker's write surface is exactly its order's paths.",
  "world_is": "One order complete (DB-f-503, drained 06100e8539); the portal candidate is LOCAL, 25 commits over origin/PROD, not pushed, not registered. FWD-21's thread is not live: no route serves a report and the render host (hop 5) is not live. The issuer reports a leftover plain directory C:/dev/wk-irpt-dashbd-503 (not a worktree), left for Andrew's word on recursive deletion.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T04:4xZ: DBF115-1-AC1/AC2/AC3 FAIL on the landed tree (portal files missing); PASS rc 0 on a detached portal worktree at 476f8388; at 506a2302 AC1/AC2 PASS, AC3 FAIL rc 1 (index.tsx outside the grant)",
    "portal 506a2302 author 2.0.0_SA_COO~F2, 1 file, src/pages/InvestorReporting/index.tsx +2",
    "portal 476f8388 src/pages/InvestorReporting/dashboard/report/reportRead.ts line 107; export/ExportButton.tsx lines 161, 236",
    "proof-of-spec-check VALID rc 0 on ~503; round-close-check --round 115 --workstream ~F2 verdict=MAY-CLOSE",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R115_F.md blob ad8af87450 (msg 8047)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An ARMED gate row whose issuer ruling holds in the code it cites (its route-scope ground is design, inert until a route serves), and three inert observations. The AC3 grant failure at the candidate head is the issuer's to amend, named above for the CTO, not repaired here."
 }
]
```
