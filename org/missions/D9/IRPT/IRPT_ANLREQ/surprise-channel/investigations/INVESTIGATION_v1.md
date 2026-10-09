# IRPT_ANLREQ -- surprise channel, INVESTIGATION v1 (round 1, dell2 fabric)

**Opened by:** `0.9.0_WK_IRPT_ANLREQ~41` on its first row (the channel file mints on its first row, per the row gate).
**Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py` validates every NEW row (schema
`org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`.
**Id grammar:** a worker's row is `IRPT_ANLREQ-D2-W<n>-S<k>`. **Append-only during the round.** Never edit an existing row.
**Denominator at this write:** 2 rows (this file's first two).


## IRPT_ANLREQ-D2-W41-S1 -- the transcripts-pull zip does not carry keys.py or the firm registry, so the commentary Lambda refuses every analysis_ready message once applied

```json
[
{
  "id": "IRPT_ANLREQ-D2-W41-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
  "surfaced_at": "2026-10-09T05:10:00Z",
  "one_line": "TO-AR-t-11 says to import infra/aws/lambda/investor-reporting/_keys/keys.py by path, or file the row. lambda_handler now imports it by path (env IRPT_KEYS_DIR, else a bounded walk up for infra/aws/lambda/investor-reporting/_keys/keys.py), but the commentary Lambda's package (infra/aws/lambda/transcripts-pull/build.sh) carries neither keys.py nor data/firm_registry.json, so in the deployed zip admit_ready_message raises KEYS_MODULE_UNAVAILABLE and refuses EVERY message to the DLQ (fail closed). The repo tests pass because the repo tree holds both.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~T2",
  "spec_asserts": "AR-t-11 step 2: 'If keys.py cannot be imported in the commentary package, vendor nothing: import it by path the way the IRPT code does, or file the row.' Interface I3: one READY yields exactly one commentary run.",
  "world_is": "build.sh copies only handler.py, mail_handler.py, data/transcripts/scripts, data/transcripts/assets, lib/opal_naming.py, org/standards/NAMING_SCHEMA.json and infra/logic/registry/*.json (build.sh:14-20). keys.py is not in that list and keys._find_registry() (keys.py:125) needs data/firm_registry.json or env IRPT_FIRM_REGISTRY, also not packaged. build.sh is outside this order's paths, so the packaging was not changed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/transcripts-pull/build.sh:13-20 @c2f8d004d0 (the full list of copies)",
      "infra/aws/lambda/investor-reporting/_keys/keys.py:125-155 @c2f8d004d0 (_find_registry: env override, upward walk for data/firm_registry.json, copy beside the module)",
      "data/transcripts/scripts/commentary/lambda_handler.py _load_keys / admit_ready_message (this order's commit): KEYS_MODULE_UNAVAILABLE refusal path"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
},
{
  "id": "IRPT_ANLREQ-D2-W41-S2",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
  "surfaced_at": "2026-10-09T05:10:00Z",
  "one_line": "TO-AR-t-11 asks for the resident role's SendMessage on the analysis_ready queue as a queue-policy statement whose principal is read from IRPT remote state. The only citable resident principal is the ycharts root's runner_role_arn output (the role the always-on resident host runs under); commentary.tf reads it from that root's remote state. The resident's own identity-side SendMessage grant on the new queue is not in this order's paths and is not declared anywhere yet.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "AR-t-11 step 1: producer access is a queue-policy statement whose principal is read from the IRPT remote state; if the resident role is not in any remote state you can cite, leave the queue policy out and file the row.",
  "world_is": "The ycharts root exports runner_role_arn (infra/aws/terraform/investor-reporting/ycharts/iam.tf:183, backend key investor-reporting/ycharts/tfstate at main.tf:34); that root's role 'runner' carries the resident policy (resident.tf:61 aws_iam_role_policy.runner_resident) and the host is described as the always-on single resident consumer (instance.tf:159). So the queue policy is emitted, with the principal read from that remote state. That the resident process sends as this role is INFERRED from those lines; the role's identity policy has no statement for the new queue (that grant is the resident-side cell's).",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "infra/aws/terraform/investor-reporting/ycharts/iam.tf:183-186 @c2f8d004d0 (output runner_role_arn)",
      "infra/aws/terraform/investor-reporting/ycharts/resident.tf:61-64 @c2f8d004d0 (runner_resident policy on role runner)",
      "infra/aws/terraform/transcripts/commentary.tf data.terraform_remote_state.irpt_ycharts and aws_sqs_queue_policy.commentary_ready (this order's commit)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
]
```


## IRPT_ANLREQ-D2-S1 -- hop 9 (I6): only the Report opens; PDF reader not in the portal client, commentary and original have none

```json
{
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-09T05:25:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "IRPT_ANLREQ-D2-S1",
  "one_line": "Hop 9 (I6) is only partly openable: of the package's four files only the Report has a portal reader (getOwnedAnalysisRequest); the Branded PDF reader exists server-side (ops/owned_report.py:153 pdf(), route analysis-request-pdf) but is absent from the portal client's IR_ROUTE_TABLE, and Commentary and Original file have no reader at all -- the ticket page shows those three as '(no reader yet)'.",
  "disarm_owner": "2.0.0_SA_COO~V2 (portal client: add the existing PDF route; carried to the round-1 analysis) with 2.0.0_SA_COO~Y2 / ~G2 (a reader for the commentary and the original file, IRPT side)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "worker 0.9.0_WK_IRPT_ANLREQ~13 report on IRPT_ANLREQ.TO-AR-v13 (portal c34ff9c0): 'analysis-request-pdf is not in the client's IR_ROUTE_TABLE'; adapt.ts says no page calls it yet",
      "infra/aws/lambda/investor-reporting/ops/owned_report.py:153 def pdf(...) returns download_route.url (signed)",
      "decompositions/IRPT_ANLREQ_DECOMP_R1.md I6: 'each ref opens through IRPT's signed-link reader under the VIEWER's own scope'"
    ]
  },
  "spec_asserts": "FWD-1 hop 9: an Opal person opens the report, the branded PDF with commentary, and the original Excel from the ticket page (I6).",
  "world_is": "Only the report opens; PDF, commentary and original are listed as text with '(no reader yet)'.",
  "notes": "AR-v-13 was barred from adding an endpoint by its order; the PDF needs only a client route entry for an existing server route."
}
```

```json
{
  "id": "IRPT_ANLREQ-D2-S2",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~T2",
  "surfaced_at": "2026-10-09T05:25:00Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "Two READY triggers now target the commentary Lambda: AR-t-11's I3 analysis_ready queue (merged 30bed477ad) and ~P2's H1 DynamoDB stream mapping (IB-pr-388, drained 4e7d47eb80); H1 also grants the commentary role kms:Decrypt on the irpt key, which CTO ruling msg 2341 forbids.",
  "disarm_owner": "2.0.0_SA_COO~Y2 (driver: rule ONE trigger for hop 4b), then 2.0.0_SA_COO~P2 or 2.0.0_SA_COO~T2 removes the other before any apply",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "IRPT_ANLREQ_DECOMP_R1.md interface I3: ONE closed message queue_message('analysis_ready', {tenant, request_id}), hop 4b cell AR-t-11",
      "~P2 msg 2562: infra/aws/terraform/investor-reporting/core/ready_trigger.tf -- event-source mapping from the irpt-requests NEW_IMAGE stream to the commentary Lambda + inline policy with the 4 stream actions and kms:Decrypt on the irpt key",
      "CTO msg 2341: the Lambda's role gets no GetItem, kms:Decrypt or GetObjectVersion on request_compositions",
      "data/transcripts/scripts/commentary/lambda_handler.py at 30bed477ad admits both shapes (stream records; SQS via admit_ready_message)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-1 hop 4b: one READY yields exactly one commentary run, through I3; the commentary role holds no direct IRPT data or key grant.",
  "world_is": "Both triggers are DESIRED Terraform; applied together they would run the drafter twice per READY and re-open the irpt kms:Decrypt the ruling removed.",
  "notes": "Nothing applied. Asked of ~Y2 at 05:27Z, REC (a) I3 only."
}
```

## IRPT_ANLREQ-D2-W1-S1 -- AR-y-11: the JSON contract for the analysis request body (AnalysisSubmissionRequest.schema.json, additionalProperties false) lacks ticket_id and lives

```json
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
}
```

## IRPT_ANLREQ-D2-W1-S2 -- AR-y-11 AMENDMENT 1 disposes S1 (schema now admits ticket_id, commit 5be2acd7cc); the packaged pin of that schema in lambda-source-map.json is now sta

```json
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
```
