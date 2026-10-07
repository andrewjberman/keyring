# TCKT_VNEXT -- surprise channel, INVESTIGATION v1 (round 1, dell2 fabric)

**Opened by:** `2.0.0_SA_COO~V2` ahead of the L5 cut (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`).
Lane `ANY`.
**Id grammar:** a worker's row is `TCKT_VNEXT-D2-W<n>-S<k>`; a seat's row is `TCKT_VNEXT-D2-S<k>` (dell2 coordinate); the CVO's adjudication rows
live in `../adjudications/` as `TCKT_VNEXT-C-S<k>`.
**Append-only during the round.** Never edit an existing row.

```json
[
  {
    "id": "TCKT_VNEXT-D2-S1",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "2.0.0_SA_COO~V2",
    "surfaced_at": "2026-10-07T17:20:00Z",
    "one_line": "Three carriers still place TCKT_VNEXT on the laptop although Andrew moved D7 to dell2 at ~15:1xZ: project.json and the PRD header carry fabric laptop, and SEQUENCE.yaml lists OPAL_TICKET_VNEXT PARKED with fabric laptop under its old code.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~DELL2 (writes project.json, the PRD and SEQUENCE.yaml; un-parking is its act on Andrew's word); this seat only surfaces",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/project.json: \"fabric\": \"laptop\" beside \"placement\": \"DELL2\"",
        "org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md:7 (v0.1 @a6978b2ac2): \"fabric\": \"laptop\"; line 16 says Placement DELL2",
        "org/missions/SEQUENCE.yaml:291-293 (last touched 29853d7edf, 2026-10-07 14:13Z): OPAL_TICKET_VNEXT fabric laptop, parked on Andrew's card-4 yes",
        "DIRECTIVES.yaml D7 placement: DELL2, MOVED 2026-10-07 by Andrew-direct ~15:1xZ (record org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261007_151xZ_TICKET_CENTER_D7_FORWARD_ON_DELL2_ANALYSIS_REQUEST_FIRST_ATTACHMENTS.md)",
        "python .tools/sequence-check.py --project OPAL_TICKET_VNEXT (17:3xZ dell2): listed under PARKED (21)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The project's carriers name the fabric Andrew placed it on (dell2), and a project moved forward by his word is not PARKED in the sequence.",
    "world_is": "project.json, the PRD header and SEQUENCE.yaml say laptop; SEQUENCE also says PARKED, under the pre-rename code.",
    "notes": "The park (14:13Z) predates his move-forward word (15:1xZ). Not edited here: all three carriers are the CTO's. L5 reads the PRD's placement line (DELL2) and proceeds; a fabric-keyed tool may refuse dell2 seats until the carriers agree."
  },
  {
    "id": "TCKT_VNEXT-D2-W2-S1",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_TCKT_VNEXT~2",
    "surfaced_at": "2026-10-07T18:10:00Z",
    "one_line": "TO-TV-p1's worker face says the submit response carries data.identity.request_id; the investor-reporting client's submitAnalysisRequest returns the adapted AnalysisSubmissionView (requestId, requestRevision as a string), so the page reads those and sends revision as a number when it parses as one.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/api/endpoints/investor-reporting.ts:1325-1335 (portal worktree branch wk-tckt_vnext-1-2-portal, base DEV 339851c7): submitAnalysisRequest returns adaptAnalysisSubmission output",
        "portal src/pages/InvestorReporting/contracts/adapt.ts:1379-1399: AnalysisSubmissionView {requestId, requestRevision: String(wire.identity.revision)}",
        "portal src/pages/TicketCenter/analysisRequest.ts requestReport(): reads issued.requestId / issued.requestRevision; the ticket service's report-route revision type (number or string) is not stated in the order"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The submit response carries data.identity.request_id (+ revision), which the page passes to the report-reference route.",
    "world_is": "The client the page imports hands back the adapted view, not the wire envelope; the same two values are read from it. The revision is IRPT's integer, stringified by the adapter; the page converts it back to a number for the report route when it parses."
  }
]
```
