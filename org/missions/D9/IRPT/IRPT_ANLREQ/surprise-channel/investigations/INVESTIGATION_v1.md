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
