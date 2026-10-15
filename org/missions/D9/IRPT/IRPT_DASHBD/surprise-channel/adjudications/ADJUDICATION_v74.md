# IRPT_DASHBD: CVO adjudication, round 114 (workstream ~F2, F-SHIP)

<sweep_watermark>2026-10-15T03:50Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T03:50Z, on msg 8003 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R114_F.md` @123e9f7041, blob a5ce26169f). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). No judgment criterion (both cells LOCAL). Re-run here: 3 of 3 PASS. DBF114-2-AC1 on the landed tree. DBF114-1-AC1 and DBF114-1-AC2 FAIL on the landed tree by construction, since the portal code lives only on the unpushed branch; re-run against a detached portal worktree at the candidate head d3c37966 (`cand/dell2/irpt-default-performance-report`, the same head as `wk-IRPT_DASHBD-501-portal`) they PASS, bun tests included. Both proof instances VALID; `round-close-check --workstream ~F2` MAY-CLOSE. 8 rows dismissed below, none ARMED. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S11",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T03:50:00Z",
  "one_line": "Round 114 ~F2 (the report reader and Performance tab mount, inert until served; the serve-path read). 3 of 3 PASS re-run here (two on the candidate portal head d3c37966, one on the landed tree). The filled report has no served path: of six hops, hops 2 to 5 (publish, serve, export source, export print) are absent, and hop 5's render host is unowned and stopped. Dismissed (8): D2-W501-S1 (BLOCKING, INERT; fixed by making the report the outer choice, iv-e-135 green, ruled at 4aaf4dbb29), D2-W501-S2 (checker strips colour; the re-run here passed), D2-W501-S3 (one added read per selection while no route serves; accepted, branch not to be promoted before the route exists), D2-W501-S4 (firm id ruled scope.scope.firmId), D2-W501-S5 (reader shape check fixed, test-pinned), D2-W501-S6 (FE-s-90 arms fail with FORCE_COLOR unset; not this round's cause, the observation goes to that test's owner), D2-W502-S1 (the files name ~P, not ~P2, as owner of the publisher and route; carried to the CTO), D2-W502-S2 (the export render host is stopped and needs Andrew's per-use word to start; carried to the CTO).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W501-S1",
   "IRPT_DASHBD-D2-W501-S2",
   "IRPT_DASHBD-D2-W501-S3",
   "IRPT_DASHBD-D2-W501-S4",
   "IRPT_DASHBD-D2-W501-S5",
   "IRPT_DASHBD-D2-W501-S6",
   "IRPT_DASHBD-D2-W502-S1",
   "IRPT_DASHBD-D2-W502-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug.",
  "world_is": "Two orders complete (DB-f-501 merged 3e6aaab01d, DB-f-502 merged f39e304d24); the portal candidate is LOCAL, not pushed and not registered for approval. FWD-21's thread is not live: a served filled report needs hops 2 to 5, whose owner is the CTO's to rule (the issuer's message says call 076d ruled them, CLOSED; this seat did not read that call). The criteria as written grade a tree that no longer exists after the worker worktree was removed; a re-run needs the portal at d3c37966.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T03:4xZ: DBF114-2-AC1 PASS on the landed tree; DBF114-1-AC1 and DBF114-1-AC2 FAIL on the landed tree (portal file missing), PASS rc 0 on a detached portal worktree at d3c37966",
    "proof-of-spec-check VALID rc 0 on both instances (~501, ~502); round-close-check --round 114 --workstream ~F2 verdict=MAY-CLOSE",
    "investigation rows D2-W501-S1..S6, D2-W502-S1..S2; issuer rulings at amendment 4aaf4dbb29",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R114_F.md blob a5ce26169f (msg 8003)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two worker defects fixed under the issuer's recorded ruling and re-graded green here, four inert observations ruled or accepted by the issuer, and two inert ownership facts the packet carries to the CTO."
 }
]
```
