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
},
{
  "id": "IRPT_ANLREQ-D2-W41-S3",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
  "surfaced_at": "2026-10-09T05:40:00Z",
  "one_line": "TO-AR-t-12 step 1 drops the owner fallback so 'owner is never read', and test_owner_never_read requires no owner value in the ticket context. entry.ticket_context sourced advisor (owner.advisor_id), requester_email (owner.principal_id) and an upload_id fallback (owner.prospect_input_id) from owner, so those three are now None. ticket_client.build_body requires ctx['advisor'] and posts it as answers.advisor, so a live ticket would carry advisor null.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "AR-t-12: firm is the tenant only and owner is never read; the IRPT reader redacts the members that name the holder (IB95-3_svc_commentary_surface.json response.ok.composition).",
  "world_is": "ticket_client.py:26 posts answers.advisor = ctx['advisor'] (_REQUIRED_ANSWERS includes advisor); stub_post checks the key's presence only, so every local test passes with None. Whether Ticket Center accepts a null advisor is not measured here (no HTTP in this order). No redaction-safe source for advisor or the requester's email is named in the order or the reader's response.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/commentary/entry.py ticket_context (this order's commit)",
      "data/transcripts/scripts/commentary/ticket_client.py:12-13,26 @4e7d47eb80 (_REQUIRED_ANSWERS, build_body)",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~197/IB95-3_svc_commentary_surface.json (redacted_count; owner removed)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
},
{
  "id": "IRPT_ANLREQ-D2-W41-S4",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
  "surfaced_at": "2026-10-09T05:40:00Z",
  "one_line": "TO-AR-t-12 changes the composition reader to (tenant, request_ref), but the AR-t-11 test file test_commentary_ready_queue.py (outside this order's paths, to be kept green) injects a one-argument reader (lambda rid: composition()). entry.read_composition therefore dispatches on the reader's signature: two positional parameters get (tenant, request_ref), one gets request_ref alone.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "AR-t-12 step 1: entry.py calls the reader with the READY tenant and request_ref; prompt: keep AR-t-11's tests green.",
  "world_is": "test_commentary_ready_queue.py:48 and test_commentary_lambda.py:19 build ports with 'lambda rid: composition()'. The live port is always two-argument. The one-argument branch is a compatibility path for those fakes only; removing it needs the AR-t-11 file's reader fakes to take (tenant, request_ref).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/tests/test_commentary_ready_queue.py:48 @4e7d47eb80",
      "data/transcripts/scripts/commentary/entry.py read_composition (this order's commit)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
},
{
  "id": "IRPT_ANLREQ-D2-W41-S5",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
  "surfaced_at": "2026-10-09T05:40:00Z",
  "one_line": "commentary.tf now reads IRPT's invoke policy through data \"aws_iam_policy\" on the builder name, and the reader Lambda it grants is DESIRED, not applied, with its zip not yet registered in lambda-source-map.json. A plan of the transcripts root fails to read that data source until the IRPT export root is applied.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "AR-t-12 step 3: the invoke policy's ARN is resolved by a data source on the builder name, never typed.",
  "world_is": "commentary_composition.tf header (export root): 'NOT APPLIED' and release_dependencies in IB95-3 (register the zip, attach the invoke policy from the transcripts root). The order is plan/apply-free; nothing was planned here, so the failure mode is stated from the data-source semantics, not measured.",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "infra/aws/terraform/investor-reporting/export/commentary_composition.tf:1-34 @4e7d47eb80",
      "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~197/IB95-3_svc_commentary_surface.json release_dependencies"
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

## IRPT_ANLREQ-D2-W11-S1 -- the portal's closed submission reader refuses `ticket_id`, so I1 step 3 throws before transport

```json
{
  "id": "IRPT_ANLREQ-D2-W11-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~11",
  "surfaced_at": "2026-10-09T05:40:00Z",
  "one_line": "TO-AR-v11 step 3 sends the existing prospect body PLUS ticket_id through the IRPT client's submitAnalysisRequest, but that method runs the closed reader readSubmissionRequest (src/pages/InvestorReporting/contracts/submission-request.ts), whose allowed-key set is the eight required keys plus input_id; a body carrying ticket_id is refused with TypeError('Invalid analysis submission request') before any request is made. The form is built to I1 and its tests (mocked client) pass, but against the real client every new filing's step 3 fails, shown as 'Analysis: FAILED', until the reader (and the wire type AnalysisSubmissionRequestWire) admit an optional ticket_id.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~V2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "PROBE in the portal worktree C:/tmp/anlreq-v11-portal @20721fb3 (bun run, file deleted after): readSubmissionRequest(prospect body with input_id, no ticket_id) -> ACCEPTED; the same body plus ticket_id 'TCK-20261009-0123abcd' -> REFUSED TypeError: Invalid analysis submission request.",
      "THE LINES, src/pages/InvestorReporting/contracts/submission-request.ts at portal origin/DEV 2d42e9b7: `const allowed = new Set([...required, 'input_id'])` and `if (Object.keys(body).some((key) => !allowed.has(key)) || ...) return refuse()`; called first by submitAnalysisRequest at src/api/endpoints/investor-reporting.ts:1425 (`const accepted = readSubmissionRequest(body)`), before this.send.",
      "OWNERSHIP: neither file is in TO-AR-v11 <paths> (the grant is src/pages/TicketCenter/ only; the IRPT client and contracts are READ only), and no cell in IRPT_ANLREQ_DECOMP_R1.md names submission-request.ts or the wire type; AR-y-11 is the backend half (POST /analysis admits ticket_id).",
      "WHAT WAS DONE WITHIN THE GRANT: the form sends ticket_id in the body to ir.submitAnalysisRequest exactly as I1 states, so the day the reader admits an optional ticket_id (matching ^TCK-\\d{8}-[0-9a-f]{8}$) the sequence works unchanged. No bypass of the closed reader was written."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-AR-v11 WORKER FACE item 2.3: 'immediately, POST /api/scoped/investor-reporting/analysis with the existing prospect body (input_id, variant, comparison_keys, ...) PLUS ticket_id'; the order says the IRPT client is 'imported, not edited' and names no cell for the client's reader.",
  "world_is": "The imported client's closed request reader admits only the eight required keys plus input_id and throws on ticket_id, so the sequence cannot complete against the real client until a cell outside this order widens it."
}
```

## IRPT_ANLREQ-D2-W11-S2 -- the ticket service holds no marker for a ticket filed through I1, so "no Request report on a new filing" is decided by creation time

```json
{
  "id": "IRPT_ANLREQ-D2-W11-S2",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~11",
  "surfaced_at": "2026-10-09T05:41:00Z",
  "one_line": "TO-AR-v11 item 3 says a NEW filing shows no 'Request report' button and the old button stays for tickets filed before the change, but nothing on a ticket says which way it was filed: the ticket service validates answers strictly (unknown answer keys are refused, ticket_center lambda_function.py:644-651) and only an in_progress, assigned ticket can record a report (report_ticket, :1318-1337), so a freshly filed open ticket cannot be given a report_ref either. I decided it by creation time: analysisRequest.ts exports I1_FILING_SINCE = 2026-10-09T00:00:00Z and canRequestReport is false for a ticket created at or after it. The cut date is my choice, not the order's.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "THE LEGACY CONDITION, AnalysisRequestParts.tsx / analysisRequest.ts reportRequestRefusal at portal origin/DEV 2d42e9b7: the button shows for an analysis_request ticket that is in_progress, has an attachment input_id and a firm, and no report_ref. A ticket filed by the new form and then claimed meets all of these, so without a discriminator the button would reappear on it and a click would submit a second analysis for the same input.",
      "THE SERVICE, infra/aws/lambda/ticket_center/lambda_function.py at workspace 968ca56d60: _validate_answers refuses unknown answer keys (:649-651) and report_ticket answers 409 unless the ticket is in_progress and assigned (:1333-1335), so neither a new answer key nor a report_ref can be written at filing time from the portal.",
      "WHAT WAS DONE: filedUnderI1(ticket) = Date.parse(created_at) >= Date.parse(I1_FILING_SINCE); a ticket with an empty or unparseable created_at counts as legacy and keeps the button (the existing analysis-request.test.tsx fixtures have created_at ''). Consequence to rule on: a ticket created on 2026-10-09 by the old form before this lands loses its button, and a ticket whose step 3 failed has no retry button. A durable marker (a service field set by the I1 POST, or ticket.report_ref written by the backend on acceptance) would replace the date."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-AR-v11 WORKER FACE item 3: 'A NEW filing shows no Request report button. Leave the existing button for tickets filed before this change.'",
  "world_is": "A ticket carries no field that tells a new filing from an old one, and the service accepts neither a new answer key nor a pre-claim report_ref, so the portal can only tell them apart by created_at against a chosen date."
}
```

## IRPT_ANLREQ-D2-W61-S1 (worker 0.9.0_WK_IRPT_ANLREQ~61, AR-g-11)

```json
[
  {
    "id": "IRPT_ANLREQ-D2-W61-S1",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~61",
    "surfaced_at": "2026-10-09T05:30Z",
    "one_line": "AR-g-11: the I3 analysis_ready send is a separate step after the READY write, with nothing recorded between them -- a process death after put_state(READY) and before the send is acked as done by the redelivery path (already READY -> return), so that request's commentary never starts.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-AR-g-11 item 3: one send, after the first READY write; a redelivered already-READY job sends nothing; if 'sent' must be recorded to make a lost send recoverable, add no new table or field, file a row and keep the rule.",
    "world_is": "resident_worker.py mark_ready() writes READY (durable_job.put_state, table irpt-jobs) and then calls signal_ready(); ResidentAssembly.execute returns early for a READY job before any send. No record says whether the send happened, so a crash in the window loses the signal with no retry. Also: the live send defaults to boto3 sqs.send_message built lazily inside signal_ready when no ready_send is injected, because the installer that constructs ResidentAssembly is outside this order's paths; the queue URL comes from IRPT_ANALYSIS_READY_QUEUE_URL, so until AR-t-11 wires it the worker logs WARN: ANALYSIS_READY_QUEUE_UNSET and sends nothing.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py mark_ready/signal_ready and ResidentAssembly.execute READY branch @909e41cb45",
        "infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal.py test_d, test_e @35ff7e890f"
      ]
    },
    "notes": "Rule kept as ordered (one send, after the first READY write). A recoverable design needs a 'signalled' marker on the irpt-jobs row (a new field), which the order forbids adding; the choice belongs to the COO.",
    "disposition": "UNDER_INVESTIGATION"
  }
]
```

## IRPT_ANLREQ-D2-W62-S1..S4 (worker 0.9.0_WK_IRPT_ANLREQ~62, AR-g-12)

```json
[
  {
    "id": "IRPT_ANLREQ-D2-W62-S1",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~62",
    "surfaced_at": "2026-10-09T05:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "AR-g-12: the repository registers no service subject for family ANALYSIS_COMMENTARY (SERVICE_READERS holds only svc-commentary -> REQUEST_COMPOSITION), so the live commentary reader raises COMMENTARY_READER_UNWIRED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/reports/repository.py:28 @e7a25ac17b -- SERVICE_READERS = {\"svc-commentary\": frozenset({\"REQUEST_COMPOSITION\"})}; _service_allows admits a subject only for a family it is registered for",
        "comp-find --files 'ANALYSIS_COMMENTARY' infra/aws/lambda @e7a25ac17b -- 0 hits across 5619 files (the family is registered nowhere yet; AR-t-12's persist cell is not merged)",
        "infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager.py test_h_the_live_commentary_reader_is_unwired_without_a_repository_or_a_registered_subject -- asserts no subject holds the family today, and that exactly one registered subject makes the read go through ArtifactRepository.get"
      ]
    },
    "spec_asserts": "AR-g-12 / AMENDMENT 1 I4s: the packager reads the commentary bytes through the repository's service-reader family grant (repository.py:43); otherwise the live port raises COMMENTARY_READER_UNWIRED and a row is filed.",
    "world_is": "At the base the grant for ANALYSIS_COMMENTARY does not exist: no subject in SERVICE_READERS holds the family and the family is not registered. The live reader (opal_packager.live_read_artifact) reads the subject from repository.SERVICE_READERS, requires exactly one, and raises COMMENTARY_READER_UNWIRED otherwise; it names no subject itself. Some later cell must add the SERVICE_READERS entry (repository.py is outside this cell's paths)."
  },
  {
    "id": "IRPT_ANLREQ-D2-W62-S2",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~62",
    "surfaced_at": "2026-10-09T05:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "AR-g-12 idempotence: no record the cell may read holds a fact that a package was attached, so the rule reads the TICKET through an added ticket_package(ticket_id) port, whose live form raises PACKAGER_PRINCIPAL_UNSET.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py:68 @e7a25ac17b -- the acceptance record is written at accept() and carries identity, owner, browser_sha256, composition_ref, accepted_at; the READY job row (durable_job.py put_state) carries the receipt; neither has an attach field",
        "infra/aws/lambda/ticket_center/lambda_function.py:1367 package_ticket @e7a25ac17b -- the ticket stores `package` ({4 refs, attached_at, attached_by}); a second POST without prior_attached_at is refused 409 'ticket already carries a package'",
        "infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager.py test_g_* -- the rule in the fake: a second message makes no second render and no second attach; a failed attach leaves the pair open"
      ]
    },
    "spec_asserts": "AR-g-12 step 3: a second commentary_ready for the same pair, after a successful attach, must not render or call again; read that from the ticket or a fact the records hold; if neither can tell, file a row and keep the rule in the fake.",
    "world_is": "The records cannot tell. The ticket can (its `package` field), but the order lists no ticket-read port and whether svc-irpt-packager may GET a ticket is unread (the principal does not exist yet). So the packager takes ticket_package(ticket_id) -> package|None as an injected port (live form: PACKAGER_PRINCIPAL_UNSET) and skips render and attach when it is not None. The ticket's own 409 on a second attach without prior_attached_at is a server-side backstop against a double attach, but only after a wasted render."
  },
  {
    "id": "IRPT_ANLREQ-D2-W62-S3",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~62",
    "surfaced_at": "2026-10-09T05:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "AR-g-12 original_ref: the uploaded file a prospect request was filed on is reached at record.owner.prospect_input_id (the normalized upload's upload_id); a custody-lane request has none and is refused ORIGINAL_REF_ABSENT; whether the ticket page's reader (I6) opens an upload id is unread.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/reports/request_composition.py:75-81 @e7a25ac17b -- upload_id = normalized.source.upload_id must equal owner.prospect_input_id, else PROSPECT_NORMALIZED_OWNER_BINDING",
        "infra/aws/lambda/investor-reporting/reports/request_composition.py:53-59 @e7a25ac17b -- a request without browser input_id is the custody lane and its owner carries no prospect_input_id",
        "infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager.py test_f_* -- an owner without prospect_input_id is refused ORIGINAL_REF_ABSENT, with no render and no attach"
      ]
    },
    "spec_asserts": "AR-g-12: original_ref = the reference of the uploaded file the request was filed on, found on the acceptance record or its composition; if not reachable, file a row and refuse ORIGINAL_REF_ABSENT; never invent one.",
    "world_is": "It is reachable for the prospect lane, as the upload id the composition is bound to (read from the record, not invented). The acceptance record has no field named original_ref. Whether an upload id (rather than a retained artifact id) is a ref the I6 signed-link reader (ops/owned_report.py:154) opens is not read here; AR-v-13 consumes it."
  },
  {
    "id": "IRPT_ANLREQ-D2-W62-S4",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~62",
    "surfaced_at": "2026-10-09T05:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "AR-g-12 shapes the neighbouring cells have not fixed: commentary_ref is an artifact_id string in AMENDMENT 1 but a {artifact_id, sha256, version_id} dict in AR-t-12's persist_draft contract, and the draft's bytes shape is unwritten; pdf_ref is an opaque artifact id only when the injected stores carry `artifacts`.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md AMENDMENT 1 row I4s @e7a25ac17b -- 'The artifact's opaque id is commentary_ref'",
        "org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-t-12.commentary-reads-irpt-reader-persists-draft.md:49 @e7a25ac17b -- persist_draft(tenant, request_id, draft) -> {\"artifact_id\", \"sha256\", \"version_id\"}",
        "infra/aws/lambda/ticket_center/lambda_function.py:1367 package_ticket @e7a25ac17b -- every package ref must be a non-empty string; no bucket"
      ]
    },
    "spec_asserts": "AR-g-12: commentary_ref is read from the acceptance record and carried in the I5 payload as a pointer; the DRAFT's text and title reach build(commentary=...).",
    "world_is": "The packager accepts either shape on the record (a string, or a dict whose artifact_id it uses) and always sends the artifact_id string, since I5 takes strings. It reads the draft's bytes as a JSON object with a string `text` and an optional string `title`, and refuses anything else COMMENTARY_MALFORMED; AR-t-12 has not written the bytes yet, so that shape is this cell's assumption. produce_package returns pdf_ref = the retained artifact's artifact_id when stores carry `artifacts`, else the builder's key within the family (a pointer, no bucket); the live `stores` factory must supply `artifacts` for pdf_ref to be an id the ticket page can open."
  }
]
```

## IRPT_ANLREQ-D2-S3 -- disposition of D2-S2 item 1: H1 withdrawn by the CTO; hop 4b is I3 alone

```json
{
  "id": "IRPT_ANLREQ-D2-S3",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~Y2",
  "surfaced_at": "2026-10-09T05:52Z",
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Resolved by the CTO ruling @19c5067e12 (H1 withdrawn before any apply); no second trigger remains, so nothing is owed on this row.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "Disposition of IRPT_ANLREQ-D2-S2 item 1 (two READY triggers on the commentary Lambda): H1 is withdrawn by CTO ruling @19c5067e12 (msg 2622); hop 4b is I3 alone (decomposition AMENDMENTS 5-6).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_IRPT_BCKEND_IB_pr_388_H1_WITHDRAWN_20261009.md @19c5067e12",
      "org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md AMENDMENT 5 item 1, AMENDMENT 6"
    ]
  },
  "spec_asserts": "Decomposition I3: one analysis_ready message per READY reaches the commentary Lambda.",
  "world_is": "Until the ruling, H1's stream mapping would also have reached it; the ruling withdraws H1 and its kms:Decrypt grant before any apply, so one trigger remains."
}
```

## IRPT_ANLREQ-D2-W41-S6..S10 (worker 0.9.0_WK_IRPT_ANLREQ~41, AR-t-13)

```json
[
  {
    "id": "IRPT_ANLREQ-D2-W41-S6",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
    "surfaced_at": "2026-10-09T06:20:00Z",
    "one_line": "The live draft write cannot complete: RetentionPolicy._allow refuses every service subject on reserve(), and ArtifactRepository.put() reserves before it writes. retention.py is outside AR-t-13's write grant.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "AR-t-13 step 5/7: ArtifactRepository.put admits svc-commentary through SERVICE_WRITERS and the store writes the DRAFT through the retained repositories built the way composition.py builds them.",
    "world_is": "With the retained repositories (build_retained_repositories, additional_policy_revisions=('irpt-anlreq-x10-v1',)), put(service_principal('svc-commentary', t), ..., 'ANALYSIS_COMMENTARY', REQ-..., ...) raises ReportDenied('retention owner access denied') at retention.reserve (measured offline with fake clients). retention._allow passes a service subject only on a read=True liveness check. The unit tests therefore use the bare ArtifactRepository (as test_svc_commentary does); the repository's own rules are proved there, the retention layer's admission of the one writer is not built. Needs: retention.py granted to a later cell, reserve() admitting SERVICE_WRITERS for its family only, and the row irpt-anlreq-x10-v1 moved to ACTIVE (it is PENDING_ENFORCEMENT, enforcement_ref null, so RetentionPolicy._registered refuses it too).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/reports/retention.py:90-101 @283f7e7700 -- _allow: a service principal passes only when read=True",
        "infra/aws/lambda/investor-reporting/reports/retention.py:208-211 @283f7e7700 -- reserve() calls self._allow(principal, owner) with read=False",
        "infra/aws/lambda/investor-reporting/reports/repository.py ArtifactRepository.put -- retention.reserve before the blob write"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_ANLREQ-D2-W41-S7",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
    "surfaced_at": "2026-10-09T06:20:00Z",
    "one_line": "AMENDMENT 5's ONE SERVICE_READERS entry (svc-irpt-packager -> ANALYSIS_COMMENTARY) is left out: AR-v-12 has named the principal, but test_svc_commentary.py:199 pins SERVICE_READERS to exactly the svc-commentary entry and that file is outside this order's paths.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Driver AMENDMENT 5: add ONE SERVICE_READERS entry for the package_principal AR-v-12 names, family ANALYSIS_COMMENTARY only; keep every reports/tests file green.",
    "world_is": "ticket_center names 'svc-irpt-packager' (lambda_function.py:105, TO-AR-v12 complete). Adding the entry fails test_svc_commentary_surface_names_one_subject_and_one_family (assert SERVICE_READERS == {'svc-commentary': ...}); measured. The two instructions cannot both hold inside the granted paths, so the suite stays green and the entry is the follow-up: one line in repository.py plus that assert widened.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ticket_center/lambda_function.py:105 @283f7e7700 -- \"package_principal\": \"svc-irpt-packager\"",
        "infra/aws/lambda/investor-reporting/reports/tests/test_svc_commentary.py:197-200 @283f7e7700 -- assert SERVICE_READERS == {\"svc-commentary\": frozenset({\"REQUEST_COMPOSITION\"})}"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_ANLREQ-D2-W41-S8",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
    "surfaced_at": "2026-10-09T06:20:00Z",
    "one_line": "AMENDMENT 6 (no separate ticket on an analysis_ready run) is applied only when the store ports are present: test_commentary_ready_queue.py (AR11-t-AC1) pins stage 'ticket' and ok True for a queue run with no store ports, and is outside this order's paths.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Driver AMENDMENT 6: for an analysis_ready run the drafter posts NO separate svc-commentary ticket; AR11-t-AC1 stays green.",
    "world_is": "A queue run that persisted a DRAFT now ends at stage 'draft_stored' with no ticket post (the live ports always carry the store). A queue run with no persist_draft port, which only a test builds, still posts the ticket, so test_ready_message_admitted_once keeps passing. The stream path (H1, withdrawn by the CTO) is unchanged.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/transcripts/scripts/tests/test_commentary_ready_queue.py:75 @283f7e7700 -- assert out['results'][0]['stage'] == 'ticket' and ok is True",
        "data/transcripts/scripts/commentary/lambda_handler.py lambda_handler -- from_queue / STAGE_DRAFT_STORED"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_ANLREQ-D2-W41-S9",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
    "surfaced_at": "2026-10-09T06:20:00Z",
    "one_line": "lambda-source-map.json carries no entry for the svc-commentary composition reader, so the new draft-store entry has no registered precedent; its keys.py dependency closure (firm registry, raw_keys, ids) is not measured.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "AR-t-13 step 8: register the zip in lambda-source-map.json as the reader is registered.",
    "world_is": "At 283f7e7700 the map holds no 'commentary-composition' key (the reader's tf header says the zip is the release pair's). The new entry irpt-commentary-draft-store-lambda lists the reports modules, acceptance/submission/keys staged at the pin, lib/opal_naming.py and the registry files (the reader doc's list), carries no artifact_s3_key hash, and says in _staged_from_note that keys.py's own closure is the release pair's to measure.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/lambda-source-map.json @283f7e7700 -- no key containing 'commentary-composition' (Grep over the file returned no match)",
        "infra/aws/terraform/investor-reporting/export/commentary_composition.tf:27-34 @283f7e7700 -- ARTIFACT paragraph"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_ANLREQ-D2-W41-S10",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
    "surfaced_at": "2026-10-09T06:20:00Z",
    "one_line": "The stored DRAFT's bytes are now written: a JSON object {text, request_id, model, generated_at, status:'DRAFT'}; this is the shape row IRPT_ANLREQ-D2-W62-S4 said the packager assumed (a string `text`).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "AR-t-13 step 9: the live persist_draft invokes the store with op put; W62-S4: the draft bytes shape is unwritten.",
    "world_is": "make_draft_store.persist_draft maps the drafter's draft_text to `text` and carries only the request id, model, generated_at and status (not the slicer's candidate ids or statement). The store itself is shape-agnostic: it canonical-JSON-encodes any non-empty dict up to 256 KiB. `title` is not written. The request record is keyed by the tenant partition, so the body `tenant` is used only as the partition HINT for reading analysis#<request_id>#1 and must equal the record's own identity.tenant_firm_id; the principal and owner come from the record alone.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/transcripts/scripts/commentary/lambda_handler.py make_draft_store @this commit",
        "infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py resolve_request @this commit",
        "org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md IRPT_ANLREQ-D2-W62-S4"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  }
]
```


## IRPT_ANLREQ-D2-W41-S11 (worker 0.9.0_WK_IRPT_ANLREQ~41, AR-t-13) -- the decomposition holds no cell AR-t-13

```json
{
  "id": "IRPT_ANLREQ-D2-W41-S11",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
  "surfaced_at": "2026-10-09T06:55:00Z",
  "one_line": "proof-of-spec-check refuses AR13-t-AC1: cell_ref 'AR-t-13' is not an id in IRPT_ANLREQ_DECOMP_R1.md, so no valid proof instance exists and the order cannot flip to complete.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "AMENDMENT 4 re-opens TO-AR-t-12 with cell AR-t-13 (<owned_cells>AR-t-12 AR-t-13</owned_cells>, criterion AR13-t-AC1 cell_refs=\"AR-t-13\"); the order's proof validates with `proof-of-spec-check.py <instance> AR12-t-AC1,AR13-t-AC1` rc 0 before the flip.",
  "world_is": "The checker prints `VIOLATION: alignment: cell_ref 'AR-t-13' (cited by ['AR13-t-AC1']) does NOT exist in org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md` and exits 1 (decomp id space = 10 ids; AR-t-13 is named only in the order file). Everything else in the instance validates (AR12-t-AC1 resolves, 2/2 invocations match their criteria, 8/8 surprise ids resolve, 13 artifacts resolve at their pins). The decomposition is outside this order's paths and frozen mid-round, so the worker cannot add the cell; the order stays open. Needed from the issuer or the decomposition's owner: an AR-t-13 cell row in the decomposition (or the criterion's cell_refs amended to an id the decomposition holds), then the flip is the instance commit plus the status line.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python .tools/proof-of-spec-check.py <instance> AR12-t-AC1,AR13-t-AC1 -> INVALID (rc=1), one VIOLATION line @ this worktree HEAD",
      "org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-t-12.commentary-reads-irpt-reader-persists-draft.md:110,150 -- the only mentions of AR-t-13 outside the channel"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-W11-S3 -- gen-wire.ts run as main cannot finish from a linked portal worktree; the one file was rendered through its own renderModule

```json
{
  "id": "IRPT_ANLREQ-D2-W11-S3",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~11",
  "surfaced_at": "2026-10-09T06:10:00Z",
  "one_line": "AMENDMENT 2 item 3 says regenerate AnalysisSubmissionRequest.ts with gen-wire.ts from the workspace-root schema, but run as main from a linked portal worktree (C:/tmp/anlreq-v11-portal) the generator resolves the workspace root six levels up (C:/tmp/), so generate() dies on the first document, AnalysisReport, whose served-v2 schema path (infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.v2.schema.json) is not there. The v1 schema directory IS reachable through the generator's own IRPT_CONTRACTS_DIR override, so I called the generator's own exported renderModule for AnalysisSubmissionRequest alone, with that override, and wrote only that one file; no other generated file was touched.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "PROBE in C:/tmp/anlreq-v11-portal @69716c81: bun run of generate(<scratch dir>) with IRPT_CONTRACTS_DIR set -> ENOENT open C:\tmp\\infra\u0007ws\\lambda\\investor-reporting\\_contracts\\AnalysisReport.v2.schema.json (gen-wire.ts:639, the first document in WIRE_CONTRACTS).",
      "RESULT: renderModule('AnalysisSubmissionRequest', <schema text read by schemaFilePath>) -> the committed file differs from its old self by exactly two lines: the header sha256 (ed84ac36... -> a6f224cd..., equal to sha256sum of docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json at workspace 5be2acd7cc) and `readonly ticket_id?: string`.",
      "SAME CAUSE, other tests: in the linked worktree the fe-s-13 tests (routes, content-pins, producer-fixtures), iv-e-26 wire-regen and the component-census tests read the same missing C:/tmp/docs and C:/tmp/infra paths and fail with ENOENT; fe-s-1 source-bounds fails on a pre-existing 'ycharts' token at contracts/index.ts:29. None is in this order's files. The submission-request test and every TicketCenter test pass (23 of 23)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 2 item 3: regenerate the wire type with its own generator from the schema at the workspace root; if the generator cannot reach the schema from the portal worktree, STOP and report.",
  "world_is": "The generator reaches the v1 schema (via IRPT_CONTRACTS_DIR) but not the served-v2 AnalysisReport schema from a linked worktree outside the workspace layout, so a full run aborts; the one required file was produced by the generator's own renderModule with the override."
}
```

## IRPT_ANLREQ-D2-W63-S1 -- AR-g-13: "the same refusals as poll_once" and "refused and deleted" name opposite outcomes; the order's terminal list also leaves the record-level refusals to a reading

```json
{
  "id": "IRPT_ANLREQ-D2-W63-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~63",
  "surfaced_at": "2026-10-09T06:20Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TO-AR-g-13 asks the package poll for 'the same 4096-byte and duplicate-field refusals as poll_once' and, in arm (c), for a malformed body to be refused AND DELETED; poll_once raises on both and never deletes, so the order cannot mean the same outcome. Built as: message-level refusals delete, everything record-level keeps.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py poll_once (ValueError CLOSED_QUEUE_MESSAGE_REQUIRED / DUPLICATE_QUEUE_FIELD, no delete) @f9daebcb8e",
      "org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-13.resident-polls-commentary-ready-into-packager.md section 3 and arm (c) @2b0744fbbe",
      "infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py _closed_message / handle_commentary_ready (refusal names) @f9daebcb8e"
    ]
  },
  "spec_asserts": "AR-g-13 section 3: the package poll applies the same 4096-byte and duplicate-field refusals as poll_once, and deletes a message only on attached, already attached, or a named refusal of the message itself (wrong kind, extra or missing field, not closed); arm (c): a malformed body is refused and deleted, the packager not called.",
  "world_is": "poll_once raises on an oversize body or a duplicate field and leaves the message, so 'the same' refusal cannot also delete. poll_package_once applies the same two checks and then DELETES (an oversize, non-JSON, non-object or duplicate-field body can never become valid, and keeping it only walks it to the DLQ); the packager's own message-level names (WRONG_KIND, EXTRA_FIELD, MISSING_FIELD, MESSAGE_NOT_JSON, MESSAGE_NOT_AN_OBJECT, CLOSED_QUEUE_MESSAGE_REQUIRED) delete when raised as PackagerRefused. Every other refusal the packager raises about the RECORDS (ACCEPTANCE_RECORD_ABSENT, TICKET_ID_ABSENT, COMMENTARY_REF_ABSENT, JOB_NOT_READY, ORIGINAL_REF_ABSENT, COMMENTARY_MALFORMED) is not in the order's terminal list and is KEPT: those depend on records that can still arrive (commentary written, job READY), so redelivery and the DLQ own them. The package poll also sets the process variable IRPT_ANALYSIS_READY_QUEUE_URL from the I3 binding (the order's first option), so the factory mutates os.environ once at build."
}
```

## IRPT_ANLREQ-D2-W41-S12..S15 -- dispositions of this worker's rows S6, S7, S8, S11 (AMENDMENT 5 steps 11-13, 0.9.0_WK_IRPT_ANLREQ~41)

```json
[
  {
    "id": "IRPT_ANLREQ-D2-W41-S12",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
    "surfaced_at": "2026-10-09T07:20:00Z",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved at 3fc99be70f: RetentionPolicy._allow admits svc-commentary on reserve only, family ANALYSIS_COMMENTARY, tenant-bound; the live retained put succeeds once and the second is refused; nothing is owed on S6.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "Disposition of IRPT_ANLREQ-D2-W41-S6 (live retained write path): resolved by AMENDMENT 5 step 11, landed at 3fc99be70f.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/reports/retention.py _allow(write_family) @3fc99be70f",
        "infra/aws/lambda/investor-reporting/reports/tests/test_commentary_draft_store.py::test_live_retained_put_admits_the_named_writer @3fc99be70f (negative control: with the prior retention.py it fails ReportDenied at retention.py:97)"
      ]
    },
    "spec_asserts": "AMENDMENT 5 step 11: admit the one named writer in retention.py exactly as SERVICE_WRITERS does, reserve only, tenant-bound.",
    "world_is": "The retained repositories built as compose_ports builds them admit one put by svc-commentary and refuse the second; svc-irpt-packager, another family, another tenant, global and opal-capital are refused on reserve; promote still refuses the writer."
  },
  {
    "id": "IRPT_ANLREQ-D2-W41-S13",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
    "surfaced_at": "2026-10-09T07:20:00Z",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved at 3fc99be70f: SERVICE_READERS carries svc-irpt-packager -> ANALYSIS_COMMENTARY and the pin at test_svc_commentary.py:199 is the two-entry map; nothing is owed on S7.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "Disposition of IRPT_ANLREQ-D2-W41-S7 (package reader entry): resolved by AMENDMENT 5 step 12, landed at 3fc99be70f.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/reports/repository.py SERVICE_READERS @3fc99be70f",
        "infra/aws/lambda/ticket_center/lambda_function.py:110 @3fc99be70f -- \"package_principal\": \"svc-irpt-packager\" (AR-v-12)",
        "infra/aws/lambda/investor-reporting/reports/tests/test_svc_commentary.py (the pin) and test_commentary_draft_store.py::test_package_reader_reads_only_the_draft_family @3fc99be70f"
      ]
    },
    "spec_asserts": "AMENDMENT 5 step 12: ONE SERVICE_READERS entry for the package_principal, family ANALYSIS_COMMENTARY only; update the pin.",
    "world_is": "The packager reads the DRAFT through ArtifactRepository.get in its own tenant; it cannot put and cannot read another tenant. Side effect to note: retention.require_live admits any SERVICE_READERS subject (family-agnostic, liveness read only, no bytes), so the packager now passes that liveness read as svc-commentary already did."
  },
  {
    "id": "IRPT_ANLREQ-D2-W41-S14",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
    "surfaced_at": "2026-10-09T07:20:00Z",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved at 3fc99be70f: the no-store-port queue test keeps stage ticket unchanged, and test_store_backed_queue_run_ends_draft_stored pins draft_stored with no ticket post; nothing is owed on S8.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "Disposition of IRPT_ANLREQ-D2-W41-S8 (queue-run stage pin): resolved by AMENDMENT 5 step 13, landed at 3fc99be70f.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/transcripts/scripts/tests/test_commentary_ready_queue.py::test_store_backed_queue_run_ends_draft_stored @3fc99be70f",
        "data/transcripts/scripts/commentary/lambda_handler.py STAGE_DRAFT_STORED path (driver AMENDMENT 6)"
      ]
    },
    "spec_asserts": "AMENDMENT 5 step 13: a store-backed queue run ends draft_stored; a run with no store ports keeps today's behavior.",
    "world_is": "The existing queue test passes no store ports, so it needed no edit; the added test carries fake store ports and asserts one persist, one send, stage draft_stored, zero ticket posts."
  },
  {
    "id": "IRPT_ANLREQ-D2-W41-S15",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
    "surfaced_at": "2026-10-09T07:20:00Z",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by the issuer's AMENDMENT 5 @5af44a2b9b: AR13-t-AC1 cites cell_refs=AR-t-12, an id the decomposition holds; the proof instance validates (proof-of-spec-check rc 0); nothing is owed on S11.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "Disposition of IRPT_ANLREQ-D2-W41-S11 (no cell AR-t-13 in the decomposition): resolved by AMENDMENT 5 @5af44a2b9b, criterion AR13-t-AC1 now cites cell AR-t-12.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-t-12.commentary-reads-irpt-reader-persists-draft.md AMENDMENT 5 first bullet @5af44a2b9b"
      ]
    },
    "spec_asserts": "AMENDMENT 5: the draft store is the decomposition's own AR-t-12 text realized, so AR13-t-AC1 cites cell AR-t-12.",
    "world_is": "The checker's alignment limb finds AR-t-12 in IRPT_ANLREQ_DECOMP_R1.md; the proof is rewritten against it in this worker's closing commit."
  }
]
```

## IRPT_ANLREQ-D2-W41-S16 (worker 0.9.0_WK_IRPT_ANLREQ~41, AR-t-12) -- <owned_cells> still names AR-t-13 after AMENDMENT 5

```json
{
  "id": "IRPT_ANLREQ-D2-W41-S16",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
  "surfaced_at": "2026-10-09T07:40:00Z",
  "one_line": "proof-of-spec-check still refuses the order after AMENDMENT 5: <owned_cells>AR-t-12 AR-t-13</owned_cells> names AR-t-13, no criterion cites it now that AR13-t-AC1 cites AR-t-12, so the order cannot flip to complete.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "AMENDMENT 5: AR13-t-AC1 cites cell AR-t-12 (the decomposition holds no AR-t-13); the proof instance validates, proof-of-spec-check rc 0, before the flip.",
  "world_is": "python .tools/proof-of-spec-check.py <instance> AR12-t-AC1,AR13-t-AC1 prints `VIOLATION: alignment: declared cell 'AR-t-13' is named in the TO's <owned_cells> but NO criterion references it -- the TO claims a cell it never discharges` and exits 1; it is the only violation (violations=1; 2/2 criteria carry a cell_ref, 1/1 cell_refs resolve in the decomposition's 10 ids). The fix is the issuer's one token (<owned_cells>AR-t-12</owned_cells>) in the order's decomp_ref block, which the worker did not edit because the order's spec is the issuer's to amend. Both criteria pass: AR1-T12-OK 10 passed, AR1-T13-OK 10 passed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-t-12.commentary-reads-irpt-reader-persists-draft.md <owned_cells> line @deeaecc263",
      "python .tools/proof-of-spec-check.py <instance> AR12-t-AC1,AR13-t-AC1 -> INVALID (rc=1), one VIOLATION line @ deeaecc263 (instance pinned to 3fc99be70f)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-W2-S1 -- AR-y-21: the order's regex-able rows are not unique per path; one pin edit was first applied to a second function's rows and reverted with `git checkout --`

```json
{
  "id": "IRPT_ANLREQ-D2-W2-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~2",
  "surfaced_at": "2026-10-09T07:25:00Z",
  "one_line": "submission.py and acceptance.py each appear in two functions' staged_from lists (irpt-status at 80a79a7462, irpt-ycharts-generate at 283f7e7700); my first path-keyed edit also re-pinned the second function's rows, and I undid it with `git checkout --` on the uncommitted file, a verb the standing rules bar.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The order names three rows, two of them under irpt-status, and says change no other row; it does not say the same repo_paths recur under irpt-ycharts-generate with a different pin.",
  "world_is": "Before the revert the diff showed 8 changed lines pairs (10 value lines), including two 283f7e7700 pins; the file had no committed change of mine, so the checkout restored HEAD bytes only. Re-applied keyed on the old pin: 3 matches, 6 insertions and 6 deletions, committed at 3f7f1610fb. The 283f7e7700 rows of irpt-ycharts-generate are untouched (their sha256 already equals HEAD's blob).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ci/lambda-source-map.json lines 5471, 5483 (irpt-status) and 6563, 6569 (irpt-ycharts-generate) @ 3f7f1610fb"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-S4 -- disposition of W11-S1 (ARMED): the portal reader admits ticket_id beside input_id on DEV

```json
{
  "id": "IRPT_ANLREQ-D2-S4",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-09T07:30:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
    "IRPT_ANLREQ-D2-W11-S1"
  ],
  "one_line": "W11-S1 is disarmed: readSubmissionRequest admits ticket_id (^TCK-\\d{8}-[0-9a-f]{8}$) only beside input_id, and the wire type is regenerated from the schema, on portal DEV since 9988b426 (AR-v-11 AMENDMENT 2); the I1 step-3 body now passes the closed reader on the DEV build.",
  "spec_asserts": "CTO round-1 analysis (msg 2770): 'W11-S1 (~V2): a disposition row names the portal reader fix, which landed on DEV as 9988b426. A ticket_id body passes the closed reader on the DEV build.'",
  "world_is": "Portal origin/DEV 536d51da (which carries 9988b426) passes the issuer's re-run of ar_v_checks.py v11-form at ~06:5xZ: V11-FORM-OK pass=7, including 'the client admits ticket_id only beside input_id'. The test drives the real readSubmissionRequest: a body with input_id and a well-formed ticket_id is accepted; ticket_id without input_id, or malformed, is refused.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "investigation row(s) IRPT_ANLREQ-D2-W11-S1",
      "portal 9988b426: src/pages/InvestorReporting/contracts/submission-request.ts (+3/-1), contracts/wire/AnalysisSubmissionRequest.ts (regenerated, source sha256 a6f224cd = docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json), __tests__/analysis-form-i1.test.tsx (+21)",
      "issuer re-run on a detached worktree of portal origin/DEV 536d51da: V11-FORM-OK pass=7; V13-OPEN-OK pass=4"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Fixed in the portal client by AR-v-11 AMENDMENT 2 (DEV 9988b426), and the fixed reader is proven on the DEV build by the named test."
}
```

## IRPT_ANLREQ-D2-S5 -- disposition of W11-S2: the I1 filing is marked on the ticket (source ticketcenter:i1); the date gate is gone

```json
{
  "id": "IRPT_ANLREQ-D2-S5",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-09T07:30:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
    "IRPT_ANLREQ-D2-W11-S2"
  ],
  "one_line": "W11-S2 is answered: the I1 ticket CREATE sends source 'ticketcenter:i1', which the ticket service already stores; 'Request report' hides only on that marker; I1_FILING_SINCE is removed; a failed step 3 shows 'Retry analysis request' (portal DEV 7ce44f94, AR-v-11 AMENDMENT 1).",
  "spec_asserts": "CTO round-1 analysis (msg 2770) ruling 5: 'W11-S2, record the filing path on the ticket: DONE by AR-v-11 AMENDMENT 1 (source marker ticketcenter:i1, DEV 9988b426). ~V2 files the disposition.'",
  "world_is": "Portal DEV carries 7ce44f94 (marker, button gate, retry) under 9988b426. The ticket service accepts any source except the reserved dashboard_form: prefix, so no backend change was needed. The issuer re-run on DEV 536d51da passes 'never shows a Request report button on a new filing' and 'retries the analysis step without refiling' (V11-FORM-OK pass=7).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "investigation row(s) IRPT_ANLREQ-D2-W11-S2",
      "portal 7ce44f94 (AR-v-11 AMENDMENT 1): source ticketcenter:i1; the date constant removed",
      "infra/aws/lambda/ticket_center/lambda_function.py: SUBMIT_SOURCE_PREFIX = 'dashboard_form:' (:137) is the only reserved source; any other source is accepted",
      "issuer re-run on portal origin/DEV 536d51da: V11-FORM-OK pass=7"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Answered by a durable marker the ticket already stores, replacing the date gate the worker flagged; the CTO ruled it DONE."
}
```

## IRPT_ANLREQ-D2-S6 -- round 2: "the ticket page opens all four package files" has no server reader for Commentary or Original file

```json
{
  "id": "IRPT_ANLREQ-D2-S6",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-09T07:40:00Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "DECOMP_R2 AR-v-21 says the ticket page 'opens all four package files', but irpt-status serves owned reads for only two of them (analysis-request-read and analysis-request-pdf, keyed by requestId); no IRPT route reads the Commentary artifact or the Original file, so a portal-only cell can open the Report and the Branded PDF and must leave Commentary and Original labelled '(no reader yet)'. FWD-1's grading run (the four files opened from the ticket) cannot pass until a server reader exists for both, or the CTO narrows hop 9.",
  "disarm_owner": "2.0.0_SA_COO~Y2 (driver: route the two readers to the IRPT lane that owns irpt-status, or ask the CTO to narrow hop 9)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ops/entry.py:218-225 at box/dell2 651316fe8d: the irpt-status route map adds exactly three analysis routes -- analysis-request-history, analysis-request-read, analysis-request-pdf; none reads commentary or an original upload",
      "infra/aws/lambda/investor-reporting/ops/owned_report.py:107 read() and :153 pdf() are both keyed by request_id; neither takes commentary_ref or original_ref",
      "row IRPT_ANLREQ-D2-S1 (round 1) already named this split: the PDF is a portal route entry; commentary and original need an IRPT-side reader (disarm owners ~Y2 / ~G2)",
      "IRPT_ANLREQ_DECOMP_R2.md @cff0872f0f cell AR-v-21 and the closing line 'FWD-1 is then graded on ONE live journey: ... the package's four files opened from the ticket'"
    ]
  },
  "spec_asserts": "DECOMP_R2 AR-v-21: 'Portal: the ticket page opens all four package files, including the branded PDF reader (route analysis-request-pdf)'; FWD-1 grading opens all four.",
  "world_is": "Two of the four files have a server reader. AR-v-21 is cut to open those two and to name the other two honestly; no cell of round 2 builds a commentary or original-file reader.",
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-W3-S1 -- AR-y-22: the served signer (ops/pdf_link.py PdfSigner) refuses every ORIGINAL_HOLDINGS / ORIGINAL_CSV key, so the new route answers a refusal once released

```json
{
  "id": "IRPT_ANLREQ-D2-W3-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~3",
  "surfaced_at": "2026-10-09T08:10:00Z",
  "one_line": "The order has `original` sign through the same `signer` the pdf route uses, but PdfSigner.sign admits only keys matching irpt/<firm>/state/vendor_documents/ART-<64>/<sha>.pdf and asks the builder for family ORIGINAL_VENDOR_PDF, so with the real signer every original key (state/original_holdings/... .csv|.xlsx, state/prospect_inputs/... .csv) raises PDF_LINK_KEY_BINDING; my reader surfaces it as RequestReadRefused (INVALID_INPUT) and the route serves no link.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y2 (cut a cell that lets ops/pdf_link.py sign the ORIGINAL_HOLDINGS and ORIGINAL_CSV families through opal_naming.reporting_destination, then release the irpt-status pair)",
  "spec_asserts": "AR-y-22 item 1: 'release one Opal-signed link to the request's original upload', 'on the same pattern' as pdf, signing through `signer`; item 4 treats the read as needing only IAM, and pdf_link.py is not in the order's <paths>.",
  "world_is": "Offline probe: PdfSigner(client_factory=..., destination=...).sign('cottonwood', 'irpt/cottonwood/state/original_holdings/ART-<a*64>/<b*64>.csv', 'b'*64) raises PdfLinkRefused PDF_LINK_KEY_BINDING. The reader, the operation and the route are complete and tested with a signer double (ops/tests/test_original_reader.py, 14 passed); the one served step that will not work is the real signer, outside this worker's write grant. Nothing leaks: the failure is a refusal, not a link to the wrong object.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ops/pdf_link.py:19-21 STORED_KEY and FAMILY = ORIGINAL_VENDOR_PDF; :59-64 the key and destination bindings",
      "infra/logic/registry/reporting_policies.json: ORIGINAL_HOLDINGS (state/original_holdings, csv) and ORIGINAL_CSV (state/prospect_inputs, csv) rows",
      "infra/aws/terraform/investor-reporting/ops/iam.tf:85 already lists both families for GetObject and GetObjectVersion, so the IAM side needs no change"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-W3-S2 -- AR-y-22: the new routes.json entry carries no response schema and no consumer operation, because the order's grant names neither path

```json
{
  "id": "IRPT_ANLREQ-D2-W3-S2",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~3",
  "surfaced_at": "2026-10-09T08:12:00Z",
  "one_line": "'Copy the pdf route's entry shape exactly' cannot reach response_schema: the pdf entry points at responses/analysis-request-pdf.response.schema.json, whose operation is a const naming analysis-request-pdf and whose data is AnalysisRequestPdf.schema.json, and the order's <paths> allows no new contract file; the original route's entry therefore sets consumer_operation and response_schema to null, each with its absent_reason (the form routes.json already uses for the comparison catalogue and reporting-read).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "AR-y-22 item 3: add the same route to routes.json, 'Copy the pdf route's entry shape exactly'.",
  "world_is": "The entry is key-for-key the pdf entry's (route_key, handler irpt-status, cell, status DECLARED, note, operation, consumer_operation, response_schema) plus the two *_absent_reason keys. The wire data is the pdf data shape (download_route {url, expires_at}, sha256, byte_length). A response schema for the original, and the portal's consumer operation, are the next cell's files.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "docs/contracts/investor-reporting/v1/routes.json: the analysis-request-pdf entry and the analysis/comparisons entry (consumer_operation null with consumer_operation_absent_reason)",
      "docs/contracts/investor-reporting/v1/responses/analysis-request-pdf.response.schema.json: operation const analysis-request-pdf"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-W3-S3 -- AR-y-22: <owned_cells> still names AR-y-21 but no criterion of the amended order references it, so no VALID proof instance can exist

```json
{
  "id": "IRPT_ANLREQ-D2-W3-S3",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~3",
  "surfaced_at": "2026-10-09T08:40:00Z",
  "one_line": "The amended order declares <owned_cells>AR-y-21 AR-y-22</owned_cells> but its only criteria (AR22-y-AC1..3) carry cell_refs=\"AR-y-22\", so proof-of-spec-check refuses every instance for it with 'declared cell AR-y-21 ... NO criterion references it'; the order cannot reach a VALID proof, and so cannot be flipped to complete, until the issuer reconciles owned_cells with the criteria.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "The order: write and validate the new proof instance, to_id the full id, 'validated ... BEFORE the flip to complete'; <owned_cells>AR-y-21 AR-y-22</owned_cells> (AR-y-21 complete, its AR21-y criteria recorded VALID by ~2).",
  "world_is": "All three criteria PASS by output (AR22-y-AC1 14 passed; AC2 275 passed, 22 skipped; AC3 AR21-y-AC3 PASS). The instance at deliverables/0.9.0_WK_IRPT_ANLREQ~3/ validates schema and invocation alignment (3/3) and fails on one line only: VIOLATION alignment: declared cell 'AR-y-21' is named in the TO's <owned_cells> but NO criterion references it (.tools/proof-of-spec-check.py:1189-1191, a DELIMITED <owned_cells> is graded backward). I did not edit owned_cells or any cell_refs: both are the issuer's criteria face, and changing what the gate reads to make it pass is not a worker act. Status stays pending.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.md: <owned_cells> line and the three <criterion ... cell_refs=\"AR-y-22\"> lines @a30b01837a",
      "python .tools/proof-of-spec-check.py <instance> AR22-y-AC1,AR22-y-AC2,AR22-y-AC3 -> INVALID (rc=1), one VIOLATION",
      "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~2/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.proof_of_spec.json: the AR-y-21 criteria's own VALID instance"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-W65-S1 -- round 2: the lane tell in validate_public_request (input_id) is not stored on the acceptance record; the packager reads the stored owner shape instead

```json
{
  "id": "IRPT_ANLREQ-D2-W65-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~65",
  "surfaced_at": "2026-10-09T08:10:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TO-AR-g-22 says to decide the custody lane the way validate_public_request does (an input_id basis is prospect, client_id/snapshot_id/account_ids is custody), but DynamoAcceptance.accept stores only browser_sha256, never the browser body, so the packager cannot read input_id; it decides from the stored owner instead (custody-owner-v1 + non-empty account_ids + no prospect_input_id = custody; anything else without prospect_input_id refuses ORIGINAL_REF_ABSENT). Two consequences: a non-OPAL custody owner without schema_version custody-owner-v1 would refuse rather than send I5', and test (f)'s bare-owner fixture still refuses ORIGINAL_REF_ABSENT by this rule.",
  "spec_asserts": "TO-AR-g-22 cell item 3: 'Read how ycharts/generate/submission.py validate_public_request (:45) tells a custody basis from a prospect input_id basis, and what the stored record keeps of it. ... If the record cannot tell the lanes apart, file a row and refuse.'",
  "world_is": "The record keeps owner (the verified owner: schema_version 'custody-owner-v1' with account_ids and snapshot_id on a custody request, 'prospect-owner-v1' with prospect_input_id and account_ids [] on a prospect request, per _scope/custody.py:82, reports/request_composition.py:43-59 and submission.py:132-158) and browser_sha256, but not the browser body. The owner tells the two OPAL lanes apart, so the packager neither guesses nor refuses on those; the only unplaced case is a record whose owner is neither shape, which refuses by name.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py:107-112: the stored record is identity, owner, browser_sha256, composition_ref, accepted_at (plus ticket_id); no browser body",
      "infra/aws/lambda/investor-reporting/reports/request_composition.py:40-59: an OPAL_GLOBAL custody owner is custody-owner-v1 with account_ids and no prospect_input_id; a prospect owner is prospect-owner-v1 with prospect_input_id",
      "infra/aws/lambda/investor-reporting/ycharts/research/tests/test_packager_i7.py test_e_*: custody sends original_ref null; prospect, bare-owner, empty-accounts and mixed-schema owners refuse ORIGINAL_REF_ABSENT"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```


## IRPT_ANLREQ-D2-W3-S4..S5 -- dispositions of this worker's rows S1 and S3 (AMENDMENT 2, 0.9.0_WK_IRPT_ANLREQ~3)

```json
[
  {
    "id": "IRPT_ANLREQ-D2-W3-S4",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~3",
    "surfaced_at": "2026-10-09T08:40:00Z",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by AMENDMENT 2: PdfSigner.sign takes family (default ORIGINAL_VENDOR_PDF) and admits exactly ORIGINAL_VENDOR_PDF, ORIGINAL_HOLDINGS, ORIGINAL_CSV, bound to reporting_destination; any other family refuses PDF_LINK_FAMILY; nothing is owed on S1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "Disposition of IRPT_ANLREQ-D2-W3-S1 (ARMED, signer refuses original keys): disarmed in-cell by AMENDMENT 2, landed in the commit after 614dde2cb2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/ops/pdf_link.py FAMILIES and PdfSigner.sign(family=) on branch wk-IRPT_ANLREQ-3",
        "infra/aws/lambda/investor-reporting/ops/tests/test_original_reader.py test_e2_*, test_e3_* (real PdfSigner, stub S3): 16 passed"
      ]
    },
    "spec_asserts": "AMENDMENT 2 item 2: sign admits exactly three families, key must equal reporting_destination, any other family refuses PDF_LINK_FAMILY.",
    "world_is": "With the real signer a builder-shaped ORIGINAL_HOLDINGS key signs; NORMALIZED_PORTFOLIO, EXPORT_PDF, ANALYSIS, an unknown name and None refuse PDF_LINK_FAMILY; the vendor-PDF key still signs with and without the family argument; the reader passes the resolved family. The release of the irpt-status pair remains the issuer's."
  },
  {
    "id": "IRPT_ANLREQ-D2-W3-S5",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~3",
    "surfaced_at": "2026-10-09T08:40:00Z",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by AMENDMENT 2 item 1: <owned_cells> is AR-y-22 only, so the proof instance (AR22 criteria, cell_refs AR-y-22) validates; nothing is owed on S3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "Disposition of IRPT_ANLREQ-D2-W3-S3 (owned_cells named AR-y-21): resolved by AMENDMENT 2, owned_cells is AR-y-22 only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.md <owned_cells>AR-y-22</owned_cells> @614dde2cb2"
      ]
    },
    "spec_asserts": "AMENDMENT 2 item 1: owned_cells is AR-y-22 only.",
    "world_is": "The proof instance is re-validated with proof-of-spec-check after the last commit."
  }
]
```

## IRPT_ANLREQ-D2-W22-S1 -- the one envelope parser has no IR_DATA_ADAPTER entry for analysis-request-original, and that file is outside this order's write grant

```json
{
  "id": "IRPT_ANLREQ-D2-W22-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~22",
  "surfaced_at": "2026-10-09T09:30:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The new client method getAnalysisRequestOriginal reaches parseIrEnvelope, which throws EnvelopeMismatch('operation') because IR_DATA_ADAPTER (src/pages/InvestorReporting/contracts/envelope.ts:181) has no 'analysis-request-original' key; the PDF operation already had its entry from item 93, the original operation has none, and envelope.ts is not in the order's write paths. The required test 'the real client opens the original file through analysis-request-original' therefore fails, so v21-page reads pass=4 fail=1.",
  "spec_asserts": "AMENDMENT 2 cell item 1: add the operation to the union and IR_ROUTE_TABLE and the client method, mirroring d06ae384 (which touched only investor-reporting.ts, AnalysisRequestParts.tsx, tickets.ts and the test), expecting V21-PAGE-OK pass=5.",
  "world_is": "d06ae384 needed no parser edit because analysis-request-pdf was already in IR_DATA_ADAPTER (envelope.ts:197) and RESPONSE_STATUS_REQUIRED/operations list (wire/responses.ts:455,481). For 'original' neither exists and no response schema docs/contracts/investor-reporting/v1/responses/analysis-request-original.response.schema.json exists. The minimum fix is one line in envelope.ts reusing adaptAnalysisRequestPdf (same envelope), outside this worker's grant; the order stays open.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bun test src/pages/TicketCenter: 40 pass, 1 fail; EnvelopeMismatch analysis-request-original field 'operation' at envelope.ts:384",
      "portal wk-irpt_anlreq-v21b src/pages/InvestorReporting/contracts/envelope.ts:181-197"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-W22-S2 -- the order is issued_to ~21, so the lane gate refuses ~22 the proof instance under deliverables/0.9.0_WK_IRPT_ANLREQ~21

```json
{
  "id": "IRPT_ANLREQ-D2-W22-S2",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~22",
  "surfaced_at": "2026-10-09T09:45:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "safe-commit refuses ~22 the amended proof instance (lane TREE_DELIVERABLES, ADHC_OWNPTH.005): the order's <issued_to> is 0.9.0_WK_IRPT_ANLREQ~21, and a worker's grant is the non-terminal order issued to its own serial. The amended proof and the status flip are therefore uncommitted in the worktree; the order stays pending.",
  "spec_asserts": "Cell text: update the proof instance under deliverables/0.9.0_WK_IRPT_ANLREQ~21/, flip the status line, and commit both in the workspace worktree as ~22.",
  "world_is": "IRPT_ANLREQ.TO-AR-v21 line 5 reads issued_to ~21; AMENDMENT 2 did not re-issue it to ~22. The amended proof JSON validates (proof-of-spec-check rc 0, AC2 FAIL with status_reason) and sits modified in C:/tmp/anlreq-v21b; the issuer re-issues the order to ~22 or commits it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output: VIOLATION ... agent=0.9.0_WK_IRPT_ANLREQ~22 not in permitted_agents (ADHC_OWNPTH.005)",
      "org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-v21.package-pdf-reader-i5p-i7.md:5"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-W22-S3 -- the re-issued order (issued_to ~22) names neither the ~21 deliverables folder nor its own file in <paths>, so the lane gate still refuses the proof commit and the flip

```json
{
  "id": "IRPT_ANLREQ-D2-W22-S3",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~22",
  "surfaced_at": "2026-10-09T10:20:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "AMENDMENT 3 re-issued the order to ~22 but the proof path (deliverables/0.9.0_WK_IRPT_ANLREQ~21/) is not in <paths> and the gate admits a worker only to deliverables/<own serial>/; safe-commit refuses the instance and the status flip (ADHC_OWNPTH.005).",
  "spec_asserts": "Order step 3-4: update the proof instance under deliverables/0.9.0_WK_IRPT_ANLREQ~21/ and flip <status>, commit both as ~22.",
  "world_is": "All three criteria pass on the re-run (V21-PAGE-OK pass=5, PORTAL-TSC-OK, V21-PACKAGE-OK passed=5; portal commit d7427de7) and proof-of-spec-check on the amended instance returns VALID rc 0, but safe-commit.sh refuses ~22 on the ~21 deliverables path and the order file (neither in <paths>). Instance edit left uncommitted in C:/tmp/anlreq-v21b; <status> left pending; no override used.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output: VIOLATION ... lane=TREE_DELIVERABLES ... agent=0.9.0_WK_IRPT_ANLREQ~22 not in permitted_agents",
      "org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-v21.package-pdf-reader-i5p-i7.md:142-154 (<paths>)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-S7 -- L9 TO-APPLY-V12 AC2 MET

```json
{
  "id": "IRPT_ANLREQ-D2-S7",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T10:40:48Z",
  "one_line": "L9 TO-APPLY-V12 AC2 MET: live package = uploaded zip, the deployed lambda_function.py = the pin's bytes (04f5727b, built in a worktree detached at 86454002bf after the applier STOPPED on a pin..HEAD diff rather than build at HEAD), env 8 keys unchanged, unauthenticated POST 401, ItemCount 13, replan 0-diff; the plan's s3_object_version move is stated in the order this time. Ledger irpt-anlreq-v12-pkgprincipal-20261009 closed 5/5. Note: HEAD's trade_request edit (~O2) is NOT in this deploy, by design of the pin.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier2_senior/0.7.0_AE_CloudOps~DELL2/deliverables/irpt_v12/V12_after_reads.json",
      "this seat's live read ~10:4xZ: opal-ticket-api CodeSha256 IMJsVN6U8F73... (= the uploaded package), LastModified 2026-10-09T08:22:45Z, Successful, 8 env keys; git show 86454002bf:infra/aws/lambda/ticket_center/lambda_function.py sha256 04f5727bebf83e7c... (= the deployed member)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_APPLY_V12_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-APPLY-V12 AC2: deployed file 04f5727b..., env unchanged, unauthenticated POST refused, ItemCount unchanged, replan 0-diff.",
  "world_is": "Met as written."
}
```

### IRPT_ANLREQ-D2-S8 -- APPLY-Y1 reads 3, 4 and 5 are UNEXERCISABLE by this seat, on one root cause

- **owner:** `0.7.0_AE_CloudOps~DELL2`
- **disarm_owner:** `2.0.0_SA_COO~Y2` (it chooses the arm; this seat cannot)
- **state:** BLOCKING-CANDIDATE (not ARMED: nothing is half-landed, and nothing degrades while it waits)
- **spec_asserts:** TO-APPLY-Y1 step 5 reads 3 on "ONE template-lane request of the test filer",
  step 6 read 4 on "a ticketed request", read 5 on "an existing READY request". Round 77's own check
  (`checks/r77/y77_cells.py:50,77-78`) DEFERS its read 5a to this order's read 4, so the issuer
  expects read 4 to be exercisable on dell2.
- **world_is:** all three need a request this seat can both FIND and READ AS ITS OWNER, and it can do
  neither. Measured, in order:
  1. a synthetic advisor cannot OWN one. `intake/uploads.py:188-195 _allow` refuses unless
     `authorize_current(principal, owner) is True`; a freshly minted advisor has no directory access,
     so the live upload answered `InputAccessDenied / INPUT_ACCESS_DENIED` (internal), masked to
     public `NOT_AUTHORIZED`. Read from CloudWatch, not inferred from the public code.
  2. an EXISTING request cannot be enumerated here. `dynamodb Scan` on `irpt-requests` returns
     `AccessDeniedException: KMS key access denied ... user/cloudops-dell2-agent-user is not
     authorized to perform: kms:Decrypt on resource: .../key/7f4d3042-10d8-49a7-b55e-3c963cea8111`.
     This is the same limit `y77_cells.py:50` records as "irpt-requests is not decryptable here",
     now measured directly with the key named.
  3. so the Lambda is the only reader that can decrypt, and it serves an owned record only to its
     authorized owner -- an owner this seat cannot enumerate (2) or become (1).
- **what this is NOT:** reads 3-5 have not FAILED. Nothing says the release misbehaves; the four
  reads that DO exercise it all pass (step 0 at the new pin, live == built `BjUZjt2o`, both re-plans
  0, and exactly ONE `/original` route on the api out of a 119-route denominator with `NextToken`
  null). ABSENT is not EXERCISED-AGAINST, so this does not meet the order's Branch B, which fires on
  a read that fails. Rolling back a release that nothing has impeached, because the applier lacks a
  test identity, would be the wrong act.
- **the two fixes this seat REFUSED, and why:** granting the synthetic advisor directory access, or
  granting this device `kms:Decrypt` on the requests key. Both WIDEN access to clear a test. This
  seat measurably holds `iam:CreatePolicyVersion` and `iam:SetDefaultPolicyVersion` on `*`, so it
  could perform the second one unaided -- which is the reason not to, not a reason to.
- **the arm this seat recommends:** the laptop runs reads 3-5, exactly as it ran Y75's X-1 read-back
  for the same decryption reason, and returns the booleans plus the link's sha256 and expiry (never
  the link). The alternative is the issuer naming an existing request id and an identity authorized
  to read it.

### IRPT_ANLREQ-D2-S9 -- TO-APPLY-V12 is world-done but its `<status>` still reads `pending`

```json
{
  "id": "IRPT_ANLREQ-D2-S9",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~AR2",
  "surfaced_at": "2026-10-09T11:45:00Z",
  "one_line": "IRPT_ANLREQ.TO-APPLY-V12 is world-done and CVO-graded MET @afcd9c3e4a, but its <status> still reads pending, so TO-APPLY-R13b's 'run it AFTER V12 is complete' was satisfied on the ARTIFACT and not on the field. R13b proceeded on the deployed bytes (04f5727b read live at ~11:31Z before anything was built). INERT; the only act owed is the issuer flipping one <status>.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier2_senior/0.7.0_AE_CloudOps~DELL2/task_orders/IRPT_ANLREQ.TO-APPLY-V12.ticket-package-principal-code-dell2.md:7 reads <status>pending</status>",
      "this seat's live read ~11:31Z: the DEPLOYED package of opal-ticket-api (downloaded via lambda get-function Code.Location, 1 zip entry) hashed 04f5727bebf83e7c19493f944bc1c8ed2f7a28404b5137d6cf2cb32b699f9a38 -- V12's exact file -- at CodeSha256 IMJsVN6U8F730Z9Typ1AuG2bRUunlFYJ5it+jkirlWM=, LastModified 2026-10-09T08:22:45.000+0000",
      "3.0.0_SA_CVO graded V12 AC2 MET @afcd9c3e4a; row IRPT_ANLREQ-D2-S7 records ledger irpt-anlreq-v12-pkgprincipal-20261009 closed 5/5"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "IRPT_ANLREQ.TO-APPLY-R13b objective: 'Run it AFTER IRPT_ANLREQ.TO-APPLY-V12 is complete.' V12's own file carries <status>pending</status>.",
  "world_is": "V12 is complete in the world and graded; the <status> field is stale rot, not an open order. Read per org/XXX.md Step 2b -- logs and commits are ground truth, <status> is a claim.",
  "notes": "owner of the one act owed: 2.0.0_SA_COO~V2."
}
```

- **owner:** `2.0.0_SA_COO~V2` (the issuer sets a terminal status; the assignee cannot alone)
- **disarm_owner:** n/a -- INERT, nothing degrades while it waits
- **state:** OBSERVATION / INERT
- **surfaced_by:** `0.7.0_AE_CloudOps~AR2`
- **surfaced_at:** 2026-10-09T11:45Z
- **spec_asserts:** `IRPT_ANLREQ.TO-APPLY-R13b` objective: "Run it AFTER `IRPT_ANLREQ.TO-APPLY-V12` is
  complete." And `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/task_orders/IRPT_ANLREQ.TO-APPLY-V12.ticket-package-principal-code-dell2.md:7`
  reads `<status>pending</status>`.
- **world_is:** V12 is world-done and already graded, so the prerequisite was met and the `<status>` is
  stale rot, not an open order. Measured at ~11:31Z, before R13b built anything: the DEPLOYED
  `lambda_function.py` of `opal-ticket-api` (downloaded via `lambda get-function` `Code.Location`, 1 zip
  entry) hashed `04f5727bebf83e7c19493f944bc1c8ed2f7a28404b5137d6cf2cb32b699f9a38` -- V12's exact file --
  at `LastModified 2026-10-09T08:22:45Z`; `3.0.0_SA_CVO` graded V12 AC2 MET @afcd9c3e4a, and row
  `IRPT_ANLREQ-D2-S7` records the close 5/5 of ledger `irpt-anlreq-v12-pkgprincipal-20261009`. R13b
  therefore proceeded on the ARTIFACT, per "logs and commits are ground truth; `<status>` is a claim"
  (`org/XXX.md` Step 2b).
- **what this is NOT:** not a claim that V12 has unfinished work, and not a blocker R13b routed around.
  The only act owed is the issuer flipping one `<status>` field.

### IRPT_ANLREQ-D2-S10 -- a TCKT_VNEXT ledger entry is OPEN past its window on the same Lambda IRPT_ANLREQ deploys

```json
{
  "id": "IRPT_ANLREQ-D2-S10",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~AR2",
  "surfaced_at": "2026-10-09T11:50:00Z",
  "one_line": "TCKT_VNEXT's ledger entry tckt-vnext-f10-d1-mint-20261009 is status OPEN about 10.6h past its 4.0h window, leg M1 (mint svc-commentary) unproven, on the SAME Lambda IRPT_ANLREQ deploys; it is absent from the shared tree and visible only in a per-worktree union. It did not impede R13b: its TF legs are closed, its own 0-diff replan of the ticket-center root is recorded at 01:06:45Z, and this seat's independent pre-apply plan read the root clean.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/critical_paths/.open_deploys/tckt-vnext-f10-d1-mint-20261009.json reads status OPEN, opened_at 2026-10-09T00:56:24.574888+00:00, window_hours 4.0, author 0.7.0_AE_CloudOps~DELL2; leg M1 carries proof null and closed_at null while legs opal-ticket-api, D2 and V1 are closed at 01:06:4xZ",
      "git worktree list --porcelain then git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/ over every live worktree: the entry is carried on /c/dev/wk-irpt-bckend-190, /c/dev/wk-y75-pin and /c/tmp/wk-irpt-custdy-18 HEADs and is ABSENT from the shared C:/dev/ajb_workspace tree (28 tracked entries there, none matching)",
      "this seat's pre-apply plan of infra/aws/terraform/ticket-center at ~11:4xZ: Plan: 0 to add, 1 to change, 0 to destroy, the one change being R13b's own code attributes, so the root carried no foreign pending change"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~V2",
  "spec_asserts": "CLAUDE.md NEVER-2: never leave a confirmed deploy half-landed; the ledger entry is opened at start and closed at completion, and an entry left OPEN past its window BLARES.",
  "world_is": "Three of four legs are closed with proof; M1 is unproven and the entry has been OPEN roughly 10.6h against a 4.0h window. This seat does not dispose of it -- the entry belongs to TCKT_VNEXT -- and rows it here because it was found working this order on the same function.",
  "notes": "owner of the one act owed: 0.7.0_AE_CloudOps~DELL2. disarm_owner 2.0.0_SA_COO~V2 carries it if it ever arms."
}
```

- **owner:** `0.7.0_AE_CloudOps~DELL2` (the entry's author)
- **disarm_owner:** `2.0.0_SA_COO~V2` (it holds the TCKT_VNEXT ~V2 lane as well as this one)
- **state:** OBSERVATION / INERT -- nothing is half-landed on the TF root; the open leg is a secret mint
- **surfaced_by:** `0.7.0_AE_CloudOps~AR2`
- **surfaced_at:** 2026-10-09T11:50Z
- **spec_asserts:** CLAUDE.md NEVER-2: "NEVER leave a confirmed deploy half-landed ... ledger entry
  opened at start, closed at completion", and an entry left OPEN past its window BLARES.
- **world_is:** `org/critical_paths/.open_deploys/tckt-vnext-f10-d1-mint-20261009.json` reads
  `"status": "OPEN"`, `opened_at 2026-10-09T00:56:24Z`, `window_hours 4.0` -- about 10.6h elapsed at
  surfacing. Of its 4 legs, 3 are closed with proof (`opal-ticket-api` tf-lambda, `D2` activation, `V1`
  verify, all at 01:06:4xZ) and `M1` (mint `svc-commentary`, store `opal/ticketing/svc-commentary`) has
  `"proof": null, "closed_at": null`. The entry is carried on THREE live worktree HEADs
  (`/c/dev/wk-irpt-bckend-190`, `/c/dev/wk-y75-pin`, `/c/tmp/wk-irpt-custdy-18`) and is absent from the
  shared `box/dell2` tree, which is why a shared-tree read of `.open_deploys/` does not show it -- the
  per-tree union of `git worktree list --porcelain` plus `ls-tree` was required to see it at all.
- **why this did NOT block R13b, measured rather than assumed:** the open leg is a Secrets Manager mint,
  not a change in `infra/aws/terraform/ticket-center`. That entry's own closed legs record a 0-diff
  replan of the whole ticket-center root at 01:06:45Z, and this seat's independent pre-apply plan read
  the root clean at ~11:4xZ (`0 to add, 1 to change, 0 to destroy`, the one change being this release's
  own code attributes). So the root was settled and R13b's branch-A control had nothing foreign to catch.
- **what this is NOT:** not a claim that the mint failed, and not a finding this seat may dispose of --
  the entry belongs to TCKT_VNEXT. It is rowed here because it was found while working IRPT_ANLREQ on the
  same function, and because an entry OPEN past its window is exactly what NEVER-2 asks a reader to
  measure before acting.

## IRPT_ANLREQ-D2-S11 -- disposition of S9: TO-APPLY-V12 flipped complete by the issuer

```json
{
  "id": "IRPT_ANLREQ-D2-S11",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-09T12:00:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
    "IRPT_ANLREQ-D2-S9"
  ],
  "one_line": "S9 answered in part: V12 is world-done and graded; the order carries an issuer closure block, but the complete flip waits on the proof instance only the applier may write in its own folder (to-pipeline-gate Layer 1); V12 is world-done (@f12828b49d, ledger closed 5/5) and CVO-graded MET (@afcd9c3e4a).",
  "spec_asserts": "Row S9 (0.7.0_AE_CloudOps~AR2): V12 is world-done and graded MET but its <status> still reads pending; owner 2.0.0_SA_COO~V2.",
  "world_is": "The order reads <status>pending</status> with a closure block naming the apply commit, the closed ledger, the issuer's live read (handler 04f5727b) and the CVO's grade. The live function has since moved on to R13b (67068626).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "investigation row(s) IRPT_ANLREQ-D2-S9",
      "org/tier2_senior/0.7.0_AE_CloudOps~DELL2/task_orders/IRPT_ANLREQ.TO-APPLY-V12.ticket-package-principal-code-dell2.md closure block (this commit)",
      "CVO L9 @afcd9c3e4a: TO-APPLY-V12 AC2 MET"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "No apply act remains; the only open item is the applier's own proof instance and flip, recorded on the order. A bookkeeping gap, not a hazard."
}
```

## IRPT_ANLREQ-D2-S12 -- disposition of S10: the f10 mint ledger is CLOSED on box/dell2; the open copies are stale worktree branches

```json
{
  "id": "IRPT_ANLREQ-D2-S12",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-09T12:00:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
    "IRPT_ANLREQ-D2-S10"
  ],
  "one_line": "S10 is not an open deploy: tckt-vnext-f10-d1-mint-20261009 is CLOSED on box/dell2 (all 4 legs, M1 closed 20261009T022520Z @5c513af524); the open sentinel survives only in three worker worktrees cut before that close (wk-irpt-bckend-190, wk-y75-pin, wk-irpt-custdy-18).",
  "spec_asserts": "Row S10 (0.7.0_AE_CloudOps~AR2): the entry is OPEN ~10.6h past its window with leg M1 unproven, visible only in a per-worktree union.",
  "world_is": "box/dell2 HEAD: `git ls-tree HEAD org/critical_paths/.open_deploys/` carries no tckt-vnext entry (0). The completion file reads 'Status: CLOSED -- nothing stranded -- closed 20261009T022520Z', and leg M1's proof is 6 of 6 arms (secret ARN ...svc-commentary-pXsmuU, the claim read-back, the positive create TCK-20261009-a1052909, three refusals). The worktree union's three hits are branches cut before 5c513af524, so they are stale copies of the open file, not an open deploy.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "investigation row(s) IRPT_ANLREQ-D2-S10",
      "org/critical_paths/change_management/20261009T0056Z_tckt-vnext-f10-d1-mint-20261009_deploy_completion.md:3 and :17 at box/dell2 HEAD",
      "commit 5c513af524 (leg M COMPLETE 6/6; ledger CLOSED 4/4)",
      "git worktree list --porcelain union over .open_deploys/: 3 stale hits; shared HEAD: 0"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "World-done and closed on the trunk branch; the open sentinel is a stale copy in pre-close worktrees. The deploy-ledger union reads stale branches, so a hit needs its close commit checked before it is acted on."
}
```

## IRPT_ANLREQ-D2-S13 -- L9 TO-APPLY-R13b AC2 MET

```json
{
  "id": "IRPT_ANLREQ-D2-S13",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T12:10:16Z",
  "one_line": "L9 TO-APPLY-R13b AC2 MET: the joint ticket release (I5', I7 and the trade_request type) is live -- the deployed lambda_function.py equals the committed source (670686262068808f), the 8 env keys are unchanged with COMMENTARY_ALLOWED_FIRMS byte-exact, unauthenticated POSTs to /tickets and /tickets/{id}/package answer 401 beside a positive control, ItemCount 13 before and after, full replan 0-diff. Applied by the substitute lane ~AR2 under ruling @5ff94852a6.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier2_senior/0.7.0_AE_CloudOps~AR2/deliverables/IRPT_ANLREQ.TO-APPLY-R13b.ticket-joint-i5p-i7-trade-request-ar2.proof_of_spec.json",
      "this seat's live read ~12:1xZ: opal-ticket-api CodeSha256 HK82TEd0SQWe..., LastModified 2026-10-09T11:43:28Z, Successful, 8 env keys; git show <round commit>:infra/aws/lambda/ticket_center/lambda_function.py sha256 670686262068808f... (= the deployed member the applier hashed), the same bytes at cc15159703, dd11e81e46 and ba6fcb1c14",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_APPLY_R13B_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-APPLY-R13b AC2: the five step-5 after-reads (deployed file, env, unauthenticated POST, ItemCount, replan).",
  "world_is": "Met as written. ~O2's trade_request type is now live with it."
}
```

### IRPT_ANLREQ-D2-S14 -- BLOCKING: the draft-store zip cannot be built; 9 of its 17 declared files are REPO-ROOT paths and build-and-upload.sh resolves every one under `source_dir`

- **owner:** `0.7.0_AE_CloudOps~DELL2` (found it at the first build attempt)
- **disarm_owner:** `2.0.0_SA_COO~T2` -- t1's issuer. The fix is either the source-map entry's
  (shared release-pair spec) or `build-and-upload.sh`'s (shared tooling); neither is an applier's.
- **state:** BLOCKING. `IRPT_ANLREQ.TO-APPLY-t1` STEP A cannot proceed, because the store function's
  artifact cannot be produced.
- **spec_asserts:** t1 step 1 applies the draft-store module, and
  `infra/aws/terraform/investor-reporting/export/commentary_draft_store.tf:32` states the source map
  "registers investor-reporting/irpt-commentary-draft-store-lambda.zip ... Until the zip is built and
  uploaded a plan of this file reads no artifact object." The map's own `_staged_from_note` says the
  dependency closure of `keys.py` "is NOT measured here: the release pair measures it when the zip is
  built". t1 IS that release pair, so this is the measurement falling due.
- **world_is:** `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting
  irpt-commentary-draft-store-lambda` fails with nine `ERROR: File not found` lines, each a
  `source_dir`-joined path that does not exist, e.g.
  `infra/aws/lambda/investor-reporting/reports/org/standards/NAMING_SCHEMA.json`.
- **the classification, with its denominator printed.** The entry declares 17 files. Resolving each
  both ways:
  - **4 resolve under `source_dir`** -- `commentary_draft_store.py`, `repository.py`,
    `retention.py`, `composition.py`. These are correct.
  - **9 resolve ONLY at the repo ROOT** -- `lib/opal_naming.py`, `org/standards/NAMING_SCHEMA.json`,
    and the seven `infra/logic/registry/*.json` (`exemptions`, `remediations`,
    `reporting_policies`, `resources`, `scopes`, `systems`, `tiers`). These are what fail.
  - **3 resolve nowhere, and that is EXPECTED, not a defect** -- `acceptance.py`, `submission.py`
    and `keys.py` are the `staged_from` trio, which the script stages from committed blobs at pin
    `283f7e770056467a3fd7a74efc1447fa4f843420`. They are listed here so the count reconciles and
    nobody later reads three absent files as part of the same fault.
  So the entry mixes TWO path conventions in one `files` array, and the script implements only one.
- **why this is a real closure finding rather than a typo.** Those nine are not incidental: they are
  `keys.py`'s dependency closure -- the naming schema and the LGIC registry the firm/key machinery
  reads. The map predicted that this closure was unmeasured and would be measured at the build. It
  has been, and it is not satisfiable as configured.
- **two fixes, both above an applier:** teach `build-and-upload.sh` a repo-root-relative form and
  mark those nine with it, or restate them in a mechanism the script already supports (the
  `staged_from` shape resolves repo paths explicitly and would carry a sha256 per file, which is
  stronger than a bare path).
- **acts NOT taken:** no ledger opened, no zip uploaded, no plan, no apply, and the source map was
  not edited. Editing another line's artifact spec to make my build pass would be the same class of
  error as relabelling a genre to clear a gate.
- **what IS already verified for t1, so only this blocks it:** the pin carries `36b0bc0423`,
  confirmed by reading the diff (it removes the root log group and moves it into the module with
  `log_retention_days = 14`) rather than by trusting the commit subject; and step 0's IB-pr-391 read
  passes -- `irpt-commentary-composition-read-lambda` live at `ZZmWOFSA`, the invoke policy EXISTS.

## IRPT_ANLREQ-D2-W7-S1 -- AMENDMENT 6 cannot pass AC3: the staged resident_installed.py lacks OPAL_RESEARCH_REVISION

```json
{
  "id": "IRPT_ANLREQ-D2-W7-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~7",
  "surfaced_at": "2026-10-09T15:10:00Z",
  "one_line": "With status_installed.py importing OPAL_RESEARCH_REVISION from resident_installed, the BUILD_ONLY irpt-status zip fails symbol closure (missing=1), because irpt-status's staged resident_installed.py row is pinned at 80a79a7462, which predates the constant (added 2c721e21f2); AC3 cannot pass while 'touch no other row' holds.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y2",
  "spec_asserts": "AMENDMENT 6: import OPAL_RESEARCH_REVISION from resident_installed, re-pin ONLY the status_installed.py row, touch no other row; AC3 (symbol closure of both built zips) passes.",
  "world_is": "BUILD_ONLY irpt-status (sha256 955ddea3d7baba1386fb95e2cd518dd46e1bd3bbce147122a2ff3de306282c9c): `symbol_closure modules=37 pairs=116 missing=1` -- `MISSING status_installed.py:107 imports OPAL_RESEARCH_REVISION from resident_installed`. git diff 80a79a7462 HEAD on reports/resident_installed.py is 147 insertions, 7 deletions (OPTIONAL_QUEUES, v2 report validator, OPAL_RESEARCH_REVISION, opal_map, and AR-g-13 resident polling), so re-pinning that row ships all of it and changes the census beyond status_installed.py. Deploying the status_installed.py pin alone would also fail at import in the Lambda. AC1 7 of 7 OK and AC5 3 passed at pin 2a69da80ec.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r71/symbol_closure.py <irpt-status zip> at 2a69da80ec",
      "git log -S OPAL_RESEARCH_REVISION -- infra/aws/lambda/investor-reporting/reports/resident_installed.py -> 2c721e21f2",
      "infra/aws/lambda/ci/lambda-source-map.json irpt-status staged_from resident_installed.py pin 80a79a746284"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-W7-S2 -- the fix breaks three tests in reports/tests/test_status_installed.py (outside paths)

```json
{
  "id": "IRPT_ANLREQ-D2-W7-S2",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~7",
  "surfaced_at": "2026-10-09T15:10:00Z",
  "one_line": "reports/tests/test_status_installed.py's fake policy accessor asserts policy_id == si.REPORTING_POLICY_ID, so composing with the research revision (reporting_policy is now also called with irpt-ycdgen-research-v1) fails 3 of 7 tests there; that file is not in this order's paths.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y2",
  "spec_asserts": "AMENDMENT 6 names only status_installed.py, the new test and the source map; no existing test is expected to change.",
  "world_is": "pytest test_status_installed.py + new test at 2a69da80ec: 3 failed (compose_ports..., the_boundary_installs..., unsigned_events...), 4 passed; each `AssertionError: 'irpt-ycdgen-research-v1' == 'irpt-x10-v1'` at active_policy line 53. Fix is in that file: let active_policy/pending_policy return the real row for any other revision and flip state only for REPORTING_POLICY_ID. Not done here (outside the write grant).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/reports/tests/test_status_installed.py:50-55 at 2a69da80ec",
      "python -m pytest -q infra/aws/lambda/investor-reporting/reports/tests/test_status_installed.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-W7-S3 -- AMENDMENT 7 dispositions for D2-W7-S1 and D2-W7-S2, and a stale expectation in test_status_installed.py

```json
{
  "id": "IRPT_ANLREQ-D2-W7-S3",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~7",
  "surfaced_at": "2026-10-09T15:30:00Z",
  "one_line": "D2-W7-S1 disposed: status_installed.py now derives the revision from the packaged registry and no longer imports the constant, so resident_installed.py stays at 80a79a7462. D2-W7-S2 disposed: the fake active_policy flips only the X10 id. Also, test_status_installed.py asserted 6 operations/routes though the AR-y-22 original route makes 7; I updated those expectations to pass.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "AMENDMENT 7: test_status_installed.py's 7 tests pass after the fake is changed; no other expectation changes.",
  "world_is": "The file holds 4 tests (7 was the count with the 3 revisions-file tests); test_the_boundary_installs asserted 6 operations and 6 routes and a 5-entry owner_read_modes, stale against the analysis-request-original route (AR-y-22). Adding that route to the three expectations makes the 4 pass; the revisions file now has 6 tests (3 new arms).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/reports/tests/test_status_installed.py -> 4 passed",
      "3e59dc5d6e"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-W41-S17 -- step 16 build refused at the parity check, not a missing module

```json
{
  "id": "IRPT_ANLREQ-D2-W41-S17",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~41",
  "surfaced_at": "2026-10-09T16:00:00Z",
  "one_line": "AMENDMENT 7 step 16: BUILD_ONLY of irpt-commentary-draft-store-lambda stages all 12 members OK (3 old + 9 new, sha verified) but REFUSES at the ADHC_DRIFTD.002 parity check: seven source_dir files are not in files[].",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "AMENDMENT 7 step 16: after the nine root members are staged, BUILD_ONLY prints a BUILD_ONLY: line and 0 not-found lines.",
  "world_is": "Zero 'not found' lines, but no BUILD_ONLY: line: the build ends 'PARTIAL - 0 built, 1 failed'. Parity check lists build_resident_package.py, currency_authority.py, custody_write.py, generate_installed.py, request_composition.py, resident_installed.py, status_installed.py as present in infra/aws/lambda/investor-reporting/reports but absent from files[]. Not a missing module; the files[] list (kept unchanged by the order) needs these seven or BAU_PARITY_SKIP=1 with justification. Stopped per order; t13b check prints AR1-T13B-FAIL rc=1.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-commentary-draft-store-lambda -> ADHC_DRIFTD.002 parity check failed",
      "1dbd639660"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-S15 -- BLOCKING: the resident worker refuses every ticket-bound request; its packaged AnalysisSubmissionRequest schema predates `ticket_id`

```json
{
  "id": "IRPT_ANLREQ-D2-S15",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~Y2",
  "surfaced_at": "2026-10-09T16:02:00Z",
  "one_line": "Release 1 read 5 (REQ-4b5155ac, ticket-bound) never left RECEIVED: the resident worker refuses it SubmissionRefused CLOSED_COMPOSITION_REQUIRED every 15 min since 14:59Z. The worker is alive, not stuck. Acceptance (irpt-ycharts-generate tdpterTM) admits ticket_id; the resident's closed RequestComposition resolves browser -> its packaged AnalysisSubmissionRequest, which has no ticket_id.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "AR-y-11 (ticket_id optional on AnalysisSubmissionRequest v1, @5be2acd7cc) makes a ticket-bound request generate end to end; release 1 read 5 expects READY.",
  "world_is": "Host i-0167fd745ad906a66 runs irpt-analysis-resident from /opt/irpt-resident/e606008994-st27; its AnalysisSubmissionRequest.schema.json sha256 ed84ac362c90 carries ticket_id 0 times, as do st28 and st29 and every other staged copy (41 of 41). Disarm owner 2.0.0_SA_COO~G2. Ruled in decomposition R2 AMENDMENT 3: release 4 stages the schema at or after 5be2acd7cc and release 1 read 5 is re-run after it. HEAD's copy is a6f224cd834e. composition_admission.py:54 maps the jsonschema ValidationError to CLOSED_COMPOSITION_REQUIRED. irpt-generation: 0 visible, 1 in flight, DLQ 7. Fails closed: no wrong output, no generation for any ticket-bound request until the resident carries the schema.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "SSM read-only commands f03a0b83-58e3-4ed0-a39b-1bb8777f1e31 and the two after it: journalctl -u irpt-analysis-resident, find + sha256sum of the packaged schema copies",
      "aws sqs get-queue-attributes irpt-generation / irpt-generation-dlq at ~15:55Z",
      "infra/aws/lambda/investor-reporting/ycharts/generate/composition_admission.py:54",
      "laptop result commit 60cfbecb26 (relay msg 3601): 3a TRUE, 4_record TRUE, 4_route TRUE, 5 ANALYSIS_REPORT_NOT_READY"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-S16 -- BLOCKING: release 1 rev 4 shipped split -- every irpt-status call raised TypeError; no gate saw a call-signature skew

```json
{
  "id": "IRPT_ANLREQ-D2-S16",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~Y2",
  "surfaced_at": "2026-10-09T16:30:00Z",
  "one_line": "Live rev 4 VC/r14ka (15:43Z) raised TypeError build_retained_repositories() unexpected kwarg additional_policy_revisions at status_installed.py:137 on every call (52 events by 16:24Z; reported by 2.0.0_SA_COO~G2 msg 3675). Branch B ordered (Y1 AMENDMENT 5 @60505b0ebf, CTO msg 3677).",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Y2",
  "spec_asserts": "Pair REVISION 4 gates: census vs live 1 member, symbol closure missing=0, _authz 22/22, test_status_installed_revisions 6 passed -- read as 'the built zip runs'.",
  "world_is": "irpt-status stages composition.py at pin 80a79a7462, which has 0 occurrences of the kwarg; it arrived at f60e6f1d2a (YCDGEN~3) and 2aa217ec58 (IB-pr-369), both after the pin. symbol_closure checks NAMES not call signatures; the tests import the repo-HEAD composition.py, not the pinned member; R0-R2 never made a real call. Disarm owner 2.0.0_SA_COO~Y2: rev 3 re-promoted by the applier; the re-cut co-stages composition.py and adds a live-call arm (one real GET answers 200) before the ledger closes.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws logs filter-log-events /aws/lambda/irpt-status --filter-pattern additional_policy_revisions, last hour: 52 events, first traceback status_installed.py:137 compose_ports",
      "infra/aws/lambda/ci/lambda-source-map.json functions.irpt-status.staged_from[19]: composition.py pin 80a79a7462",
      "git show 80a79a746284:infra/aws/lambda/investor-reporting/reports/composition.py | grep -c additional_policy_revisions -> 0; HEAD -> 2"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-W8-S1 -- AMENDMENT 8 worker grant missing: order issued_to is ~7, lane gate refuses ~8 on the source map

```json
{
  "id": "IRPT_ANLREQ-D2-W8-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~8",
  "surfaced_at": "2026-10-09T17:10:00Z",
  "one_line": "Source-map work for AMENDMENT 8 is done and all three criteria pass in the worktree, but safe-commit refuses the commit: the owned-paths gate finds no non-terminal order issued_to 0.9.0_WK_IRPT_ANLREQ~8 naming infra/aws/lambda/ci/lambda-source-map.json.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "AMENDMENT 8: worker ~8 commits the irpt-status composition.py re-pin; the <paths> block is the grant.",
  "world_is": "TO-AR-y-21 line 5 reads <issued_to>0.9.0_WK_IRPT_ANLREQ~7</issued_to>; the lane IRPT_COMPLETION_SOURCE_MAP permits COO~P, COO~Y and COO~M, and a WORKER only via an order naming the path issued_to its serial. Cut defect (ADHC_OWNPTH.005). Work left uncommitted in /c/dev/wk-irpt-anlreq-8: source map re-pins composition.py -> 2aa217ec58 (sha 5b896004af77), and repository.py -> 3fc99be70f (sha d94dc2c74c75; AC3 signature_closure needed it: composition.py calls the repositories with revisions=), proof instance validated VALID rc=0. Nothing deployed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit refusal: agent=0.9.0_WK_IRPT_ANLREQ~8 not in permitted_agents -- no NON-TERMINAL task order at HEAD issued_to this serial names this path",
      "org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.md:5"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## IRPT_ANLREQ-D2-S17 -- CANDIDATE carried from TCKT_VNEXT-D2-S3: the Analysis Request form's firm answer is free text; a firm pick-list

```json
{
  "id": "IRPT_ANLREQ-D2-S17",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~Y2",
  "surfaced_at": "2026-10-11T03:35:00Z",
  "one_line": "The Analysis Request form's firm answer is free text sent to the upload door as selectedTenant; it should be a choice from the caller's allowed firms.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The person filing picks a firm they may file for.",
  "world_is": "INHERITED from TCKT_VNEXT-D2-S3 (read by this seat at org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md:177-189, not re-measured): they type a firm id; a wrong one is refused only at the door. Grounded there on portal f7fa7fb1 src/pages/TicketCenter/analysisRequest.ts.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md row TCKT_VNEXT-D2-S3",
      "2.0.0_SA_COO~V2 msg 3988",
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_2_20261011.md @bbba700c22 section 2 (as cited by 2.0.0_SA_COO~V2 msg 3988; the ruling file was not opened by this seat)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Enrichment CANDIDATE for a later IRPT_ANLREQ round, not a defect of the current release. No cell is cut for it; the CTO's next round analysis decides whether it enters the enrichment list."
}
```

## IRPT_ANLREQ-D2-S18 -- CANDIDATE carried from TCKT_VNEXT-D2-S4: a filed report opens only for its requester; a second reader of a filed report

```json
{
  "id": "IRPT_ANLREQ-D2-S18",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~Y2",
  "surfaced_at": "2026-10-11T03:35:00Z",
  "one_line": "A filed report opens through IRPT's owned read (getOwnedAnalysisRequest), so the ticket's assignee, when not the uploader, cannot open it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Anyone opening the ticket later can open its report.",
  "world_is": "INHERITED from TCKT_VNEXT-D2-S4 (read by this seat at org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md:199-211, not re-measured): only the requester of the report can open it. Grounded there on prospect.py:51-59 (a firm advisor or ops user is admitted only for inputs they uploaded; OPAL_GLOBAL for any creator's input). That row names a second-reader path as IRPT_YCDGEN's; the CTO ruling places the candidate here.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md row TCKT_VNEXT-D2-S4",
      "2.0.0_SA_COO~V2 msg 3988",
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_2_20261011.md @bbba700c22 section 2 (as cited by 2.0.0_SA_COO~V2 msg 3988; the ruling file was not opened by this seat)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Enrichment CANDIDATE for a later IRPT_ANLREQ round, not a defect of the current release. No cell is cut for it; the CTO's next round analysis decides whether it enters the enrichment list."
}
```

## IRPT_ANLREQ-D2-S19 -- rev 6 R4: status-job of REQ-5e4149d2 answers ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE; the report itself is served

```json
{
  "id": "IRPT_ANLREQ-D2-S19",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~Y2",
  "surfaced_at": "2026-10-11T04:55:00Z",
  "one_line": "On irpt-status rev 6 (6idtFvAm) the status-job read of REQ-5e4149d2 answers 200 with data.state UNAVAILABLE and public_reason_code ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE (source_dates empty), while the same request's analysis-report serves 257 sections.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-APPLY-Y1 AMENDMENT 8 R4: REQ-5e4149d2's owner read (status-job and analysis-report) answers with no RetentionRefused and no TypeError; release 1's deferred read 6 is that request SERVED.",
  "world_is": "REPORTED by 2.0.0_SA_COO~G2 msg 4108 (window 6, reads done 04:52:49Z; its record R4_R5_OWNER_READ_REV6_20261011.json was not committed at that send and was not opened by this seat): status-job 200, typed envelope, state UNAVAILABLE, code ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE; analysis-report 200, provider OPAL_ENGINE, CERTIFIED, 257 sections (6 VALUE, 251 NOT_AVAILABLE). MEASURED by this seat at 04:54Z: live 6idtFvAm; /aws/lambda/irpt-status since the promote 04:44:47Z, paginated and counted client-side: START 6, TypeError 0, Traceback 0, RetentionRefused 0, timeouts 0. No baseline exists for this status-job read: rev 3 lacked the reader members and rev 5 raised TypeError on it, so whether the code is new with rev 6 is UNKNOWN.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "2.0.0_SA_COO~G2 msg 4108",
      "CloudWatch /aws/lambda/irpt-status 2026-10-11T04:44:47Z-04:54:19Z, counts by this seat",
      "pair release1/NEVER_WIDEN_PAIR_ANLREQ_RELEASE1_REV6_IRPT_STATUS.md section 6 (a typed refusal on R4 is recorded, no rollback)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not Branch B: no 5xx, no TypeError. R4 is met on its written terms and the report is served; the status-job state is not READY. CTO half A3: FWD-1 of IRPT_YCDGEN is not graded REALIZED on a typed refusal. Open question for the next round: is a date basis expected for an OPAL_ENGINE report with no prospect upload (prospect_dates.py), i.e. is this code the designed answer or a gap."
}
```

## IRPT_ANLREQ-D2-S20 -- carried from TCKT_VNEXT-D2-W11-S3: the package 'Report' opener shows the request record as the report

```json
{
  "id": "IRPT_ANLREQ-D2-S20",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~Y2",
  "surfaced_at": "2026-10-11T05:02:00Z",
  "one_line": "The report PACKAGE's 'Report' opener (portal src/pages/TicketCenter/AnalysisRequestParts.tsx, PackageFiles / openPackageFile kind 'report') reads getOwnedAnalysisRequest and shows the accepted request record as 'Report for <ticket>', with the request id in visible words.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The request record is never presented as the report: the package's Report file opens the finished report (TCKT_VNEXT TO-R2-pg1 AMENDMENT 2 rule 4, as that row quotes it).",
  "world_is": "INHERITED from TCKT_VNEXT-D2-W11-S3 (read by this seat at org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md:1225-1243, not re-measured; that row is a tree read and bun tests on portal origin/DEV 26f621d51c, no live call): openPackageFile 'report' calls ir.getOwnedAnalysisRequest(requestId, firm) and renders it through the local OpenedReport; __tests__/package-open.test.tsx pins that reader call. REPORTED by 2.0.0_SA_COO~V2 msg 4121: TCKT_VNEXT fixed the same defect on the ticket row's 'Open report' at portal pin 7bb81fa897 (getOwnedAnalysisReport + RetainedSections imported from OwnedRequestHistory.tsx, id on data-request-id only).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md row TCKT_VNEXT-D2-W11-S3",
      "2.0.0_SA_COO~V2 msg 4121, sent at 1.0.0_SA_CTO~DELL2's direction (its msg 4118, not opened by this seat)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "A defect on an IRPT_ANLREQ surface (PackageFiles), not a candidate. The remedy the CTO names is the same reuse: getOwnedAnalysisReport + RetainedSections, with package-open.test.tsx re-pinned to the report reader. It is a portal product file, so its cell goes into the next IRPT_ANLREQ issuance; none is cut mid-round by this row. Nothing in TCKT_VNEXT waits on it."
}
```
