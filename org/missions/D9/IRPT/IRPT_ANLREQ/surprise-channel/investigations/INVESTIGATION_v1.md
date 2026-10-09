# IRPT_ANLREQ -- surprise channel, INVESTIGATION v1

Rows are `IRPT_ANLREQ-W<n>-S<k>` (worker) per `org/surprise_channel/schemas/investigation_item.schema.json`.

```json
[
  {
    "id": "IRPT_ANLREQ-D2-W1-S1",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~1",
    "surfaced_at": "2026-10-09T05:00:00Z",
    "one_line": "AR-y-11: the JSON contract for the analysis request body (AnalysisSubmissionRequest.schema.json, additionalProperties false) lacks ticket_id and lives outside the order's paths.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-AR-y-11: if a JSON contract for this request body exists that the served path validates against, add ticket_id there too; if it lives outside <paths>, stop and file a row.",
    "world_is": "docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json declares the browser body with additionalProperties false and no ticket_id; it is outside the order's paths, so it was NOT edited. submission.validate_public_request does not load it, and now admits ticket_id. ops/owned_requests.py _frozen_composition (line 128) returns the retained browser body (which now includes ticket_id) on the history read, and test_owned_requests.py:254 says a field that contract does not declare is refused; whether the served read path validates the returned composition against this schema was not traced. A ticketed request may therefore be refused on that read until the schema gains an optional ticket_id with pattern ^TCK-\\d{8}-[0-9a-f]{8}$ (and the paired maintained_sources.py:492 pin is updated).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json line 8 additionalProperties false; properties list request_id..prepared_for, input_id only",
        "infra/aws/lambda/investor-reporting/ops/owned_requests.py:128-141 and _scope/maintained_sources.py:492 (read in worktree wk-irpt-anlreq-1)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_ANLREQ-D2-W1-S2",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~1",
    "surfaced_at": "2026-10-09T05:30:00Z",
    "one_line": "AR-y-11 AMENDMENT 1 disposes S1 (schema now admits ticket_id, commit 5be2acd7cc); the packaged pin of that schema in lambda-source-map.json is now stale and sits outside the order's paths.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-AR-y-11 AMENDMENT 1 item 1: if a packaged hash or pin of this schema exists, report it, and file a row if moving it is outside <paths>.",
    "world_is": "Disposition of IRPT_ANLREQ-D2-W1-S1: repaired by AMENDMENT 1, schema edited at 5be2acd7cc. infra/aws/lambda/ci/lambda-source-map.json line 4258-4261 packages docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json as contracts/AnalysisSubmissionRequest.schema.json with pin 3f29017cfcd28c6be36841c61f1b9b313c1f8d29 and sha256 ed84ac362c9071319d27e2581ad06ec4d3122c956d5f546266cb3a722cde69bd; the file now hashes a6f224cd834e3dd85ff20a59213c5c41e6a0fa63465287fd6df669d30ea598ef, so the built artifact carries the old schema until that pin is moved by a seat whose grant covers the source map. Not edited.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/lambda-source-map.json:4257-4261 at worktree HEAD 5be2acd7cc",
        "sha256sum of the schema at HEAD versus git show 3f29017cfc:<schema> (ed84ac36...)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  }
]
```
