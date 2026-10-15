# IRPT_DASHBD: CVO adjudication, round 135 (workstream B-49F, ~D2): the report-build contract guard

<sweep_watermark>2026-10-15T19:35Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T19:35Z, on msg 8575 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND133_137_B49F_DRAIN_END_20261015.md` @e7b2e022cc, blob 1b1f31d9cf; one packet covers rounds 133-137, adjudicated as v99-v103, one per round). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order, TO-DB-b-267 (WORLD by its infra path; worker ~217; merged @c756646bd1). No judgment criterion. Re-run here: DB135-1-AC1..AC3, 3 of 3 PASS (rc 0); proof VALID; round-close MAY-CLOSE. The round-131 criteria DB131-1-AC2 and AC3 now FAIL here ('the returns partition 2026-07-10 names no contract'), red by design as the issuer discloses: the round-131 fixture has no manifest.json, which the guard now requires. The struck DB118-3-AC3 still FAILS (rc 1), unmet. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S38",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T19:35:00Z",
  "one_line": "Round 135 B-49F: the report-build handler's contract guard. 3 of 3 PASS re-run. The handler reads each returns partition's manifest.json and chains only within one (contract_version, method_version). A mixed or unnamed contract refuses with zero puts; the 2026-06-22 Commonwealth partition is never listed or opened; a window before the floor reads NOT_SPANNED. All of this is repo code only (v99: no function in AWS). COVERAGE GAP, named by the worker in D2-W217-S2 and confirmed here: the round-131 behavioural probe (the floor, no overwrite, no dry-run put, one Event chain, no other firm, the oldest owed day, each with a failing mutant) now FAILS on its manifest-less fixture. The round-135 checker re-runs only round 131's STATIC clauses, so those behaviours are graded by round 135 and 137's own probes only as far as their scenarios reach. A criterion that is red on purpose is not a grade, and the issuer should re-point or retire DB131-1-AC2/AC3. Rows: D2-W217-S1 (the fixture gained manifests; one GET-count assertion narrowed to data.parquet), D2-W217-S2 (above) and D2-W217-S3 (a model-name trailer) are inert, accepted. D2-S92 (the two-era splice) is answered in code for THIS consumer only, with no disarm row filed; it stays held by v100.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W217-S1",
   "IRPT_DASHBD-D2-W217-S2",
   "IRPT_DASHBD-D2-W217-S3"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): a criterion is re-run, and a criterion red by design is retired or re-pointed, never left as a standing FAIL.",
  "world_is": "The report-build handler refuses a mixed-contract window. Round 131's behavioural criteria are red by design and not replaced one for one. Nothing is deployed.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T19:2xZ: DB135-1-AC1..AC3 PASS rc 0; DB131-1-AC2 and AC3 FAIL rc 1 ('names no contract'); proof-of-spec-check VALID rc 0 on ~217",
    "investigation rows D2-W217-S1..S3, D2-S92",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND133_137_B49F_DRAIN_END_20261015.md blob 1b1f31d9cf (msg 8575)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Three inert worker rows. The red-by-design round-131 criteria and the uncarried S92 disarm are named for the issuer, not repaired here."
 }
]
```
