# IRPT_ANLREQ -- round 1 remediations

<sweep_watermark>2026-10-09T07:06Z</sweep_watermark>

Graduated at round 1's L8 (ADJUDICATION_v1.md), round label v2: 13 rows, OPEN. Two ARMED (D2-W41-S1, D2-W11-S1), each disarmed by its lane.

```json
[
  {
    "id": "IRPT_ANLREQ-D2-W41-S1",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "TO-AR-t-11 says to import infra/aws/lambda/investor-reporting/_keys/keys.py by path, or file the row. lambda_handler now imports it by path (env IRPT_KEYS_DIR, else a bounded walk up for infra/aws/lambda/investor-reporting/_keys/keys.py), but the commentary Lambda's package (infra/aws/lambda/transcripts-pull/build.sh) carries neither keys.py nor data/firm_registry.json, so in the deployed zip admit_ready_message raises KEYS_MODULE_UNAVAILABLE and refuses EVERY message to the DLQ (fail closed). The repo tests pass because the repo tree holds both.",
    "evidence": [
      "investigation row IRPT_ANLREQ-D2-W41-S1",
      "infra/aws/lambda/transcripts-pull/build.sh:13-20 @c2f8d004d0 (the full list of copies)"
    ],
    "remedy": "~T2's commentary apply pair packages keys.py and the firm registry in the zip and proves the import from the built bytes (with a negative control) before apply.",
    "owner": "2.0.0_SA_COO~T2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T2",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~T2",
      "at": null
    }
  },
  {
    "id": "IRPT_ANLREQ-D2-W11-S1",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "TO-AR-v11 step 3 sends the existing prospect body PLUS ticket_id through the IRPT client's submitAnalysisRequest, but that method runs the closed reader readSubmissionRequest (src/pages/InvestorReporting/contracts/submission-request.ts), whose allowed-key set is the eight required keys plus input_id; a body carrying ticket_id is refused with TypeError('Invalid analysis submission request') before any request is made. The form is built to I1 and its tests (mocked client) pass, but against the real client every new filing's step 3 fails, shown as 'Analysis: FAILED', until the reader (and the wire type AnalysisSubmissionRequestWire) admit an optional ticket_id.",
    "evidence": [
      "investigation row IRPT_ANLREQ-D2-W11-S1",
      "PROBE in the portal worktree C:/tmp/anlreq-v11-portal @20721fb3 (bun run, file deleted after): readSubmissionRequest(prospect body with input_id, no ticket_id) -> ACCEPTED; the same body plus ticket_id 'TCK-20261009-0123abcd' -> REFUSED TypeError: Invalid analysis submission request."
    ],
    "remedy": "~V2 files the disposition row naming the portal reader fix (AR-v-11 AMENDMENTS 1+2 drain, portal DEV) and proves a ticket_id body passes the closed reader on the DEV build.",
    "owner": "2.0.0_SA_COO~V2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~V2",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~V2",
      "at": null
    }
  },
  {
    "id": "IRPT_ANLREQ-D2-W41-S2",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-AR-t-11 asks for the resident role's SendMessage on the analysis_ready queue as a queue-policy statement whose principal is read from IRPT remote state. The only citable resident principal is the ycharts root's runner_role_arn output (the role the always-on resident host runs under); commentary.tf reads it from that root's remote state. The resident's own identity-side SendMessage grant on the new queue is not in this order's paths and is not declared anywhere yet.",
    "evidence": [
      "investigation row IRPT_ANLREQ-D2-W41-S2",
      "infra/aws/terraform/investor-reporting/ycharts/iam.tf:183-186 @c2f8d004d0 (output runner_role_arn)"
    ],
    "remedy": "The resident principal in the analysis_ready queue policy is cited from the ycharts root's runner_role_arn output; ~G2's resident release confirms it is the role that sends.",
    "owner": "2.0.0_SA_COO~G2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G2",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "IRPT_ANLREQ-D2-W41-S5",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "commentary.tf now reads IRPT's invoke policy through data \"aws_iam_policy\" on the builder name, and the reader Lambda it grants is DESIRED, not applied, with its zip not yet registered in lambda-source-map.json. A plan of the transcripts root fails to read that data source until the IRPT export root is applied.",
    "evidence": [
      "investigation row IRPT_ANLREQ-D2-W41-S5",
      "infra/aws/terraform/investor-reporting/export/commentary_composition.tf:1-34 @4e7d47eb80"
    ],
    "remedy": "Order the releases so the reader Lambda (IRPT, DESIRED) is applied and its zip registered before the transcripts root is planned; the commentary pair states that precondition.",
    "owner": "2.0.0_SA_COO~T2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T2",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "IRPT_ANLREQ-D2-W41-S9",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "lambda-source-map.json carries no entry for the svc-commentary composition reader, so the new draft-store entry has no registered precedent; its keys.py dependency closure (firm registry, raw_keys, ids) is not measured.",
    "evidence": [
      "investigation row IRPT_ANLREQ-D2-W41-S9",
      "infra/aws/lambda/ci/lambda-source-map.json @283f7e7700 -- no key containing 'commentary-composition' (Grep over the file returned no match)"
    ],
    "remedy": "Register the draft-store entry in lambda-source-map.json and measure its keys.py dependency closure from the built zip.",
    "owner": "2.0.0_SA_COO~T2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T2",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "IRPT_ANLREQ-D2-W1-S2",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AR-y-11 AMENDMENT 1 disposes S1 (schema now admits ticket_id, commit 5be2acd7cc); the packaged pin of that schema in lambda-source-map.json is now stale and sits outside the order's paths.",
    "evidence": [
      "investigation row IRPT_ANLREQ-D2-W1-S2",
      "infra/aws/lambda/ci/lambda-source-map.json:4257-4261 at worktree HEAD 5be2acd7cc"
    ],
    "remedy": "Re-pin the packaged AnalysisSubmissionRequest schema in lambda-source-map.json in ~Y2's irpt-status release.",
    "owner": "2.0.0_SA_COO~Y2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y2",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "IRPT_ANLREQ-D2-S1",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Hop 9 (I6) is only partly openable: of the package's four files only the Report has a portal reader (getOwnedAnalysisRequest); the Branded PDF reader exists server-side (ops/owned_report.py:153 pdf(), route analysis-request-pdf) but is absent from the portal client's IR_ROUTE_TABLE, and Commentary and Original file have no reader at all -- the ticket page shows those three as '(no reader yet)'.",
    "evidence": [
      "investigation row IRPT_ANLREQ-D2-S1",
      "worker 0.9.0_WK_IRPT_ANLREQ~13 report on IRPT_ANLREQ.TO-AR-v13 (portal c34ff9c0): 'analysis-request-pdf is not in the client's IR_ROUTE_TABLE'; adapt.ts says no page calls it yet"
    ],
    "remedy": "A portal reader for the branded PDF (route analysis-request-pdf), so hop 9 opens all four package files from the ticket.",
    "owner": "2.0.0_SA_COO~V2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~V2",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "IRPT_ANLREQ-D2-W11-S2",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-AR-v11 item 3 says a NEW filing shows no 'Request report' button and the old button stays for tickets filed before the change, but nothing on a ticket says which way it was filed: the ticket service validates answers strictly (unknown answer keys are refused, ticket_center lambda_function.py:644-651) and only an in_progress, assigned ticket can record a report (report_ticket, :1318-1337), so a freshly filed open ticket cannot be given a report_ref either. I decided it by creation time: analysisRequest.ts exports I1_FILING_SINCE = 2026-10-09T00:00:00Z and canRequestReport is false for a ticket created at or after it. The cut date is my choice, not the order's.",
    "evidence": [
      "investigation row IRPT_ANLREQ-D2-W11-S2",
      "THE LEGACY CONDITION, AnalysisRequestParts.tsx / analysisRequest.ts reportRequestRefusal at portal origin/DEV 2d42e9b7: the button shows for an analysis_request ticket that is in_progress, has an attachment input_id and a firm, and no report_ref. A ticket filed by the new form and then claimed meets all of these, so without a discriminator the button would reappear on it and a click would submit a second analysis for the same input."
    ],
    "remedy": "Record on the ticket which path filed it (form sequence or legacy), so the 'Request report' button rule can be applied per ticket.",
    "owner": "2.0.0_SA_COO~V2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~V2",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "IRPT_ANLREQ-D2-W61-S1",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AR-g-11: the I3 analysis_ready send is a separate step after the READY write, with nothing recorded between them -- a process death after put_state(READY) and before the send is acked as done by the redelivery path (already READY -> return), so that request's commentary never starts.",
    "evidence": [
      "investigation row IRPT_ANLREQ-D2-W61-S1",
      "infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py mark_ready/signal_ready and ResidentAssembly.execute READY branch @909e41cb45"
    ],
    "remedy": "Make the READY write and the I3 send recoverable together (an outbox record, or redelivery that re-sends when no send is recorded), so a crash between them cannot strand a request (FWD-4).",
    "owner": "2.0.0_SA_COO~G2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G2",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "IRPT_ANLREQ-D2-W62-S1",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AR-g-12: the repository registers no service subject for family ANALYSIS_COMMENTARY (SERVICE_READERS holds only svc-commentary -> REQUEST_COMPOSITION), so the live commentary reader raises COMMENTARY_READER_UNWIRED.",
    "evidence": [
      "investigation row IRPT_ANLREQ-D2-W62-S1",
      "infra/aws/lambda/investor-reporting/reports/repository.py:28 @e7a25ac17b -- SERVICE_READERS = {\"svc-commentary\": frozenset({\"REQUEST_COMPOSITION\"})}; _service_allows admits a subject only for a family it is registered for"
    ],
    "remedy": "Wire the commentary reader's service subject for ANALYSIS_COMMENTARY in the resident release (the reader entry landed @3fc99be70f) and read one draft live.",
    "owner": "2.0.0_SA_COO~G2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G2",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "IRPT_ANLREQ-D2-W62-S2",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AR-g-12 idempotence: no record the cell may read holds a fact that a package was attached, so the rule reads the TICKET through an added ticket_package(ticket_id) port, whose live form raises PACKAGER_PRINCIPAL_UNSET.",
    "evidence": [
      "investigation row IRPT_ANLREQ-D2-W62-S2",
      "infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py:68 @e7a25ac17b -- the acceptance record is written at accept() and carries identity, owner, browser_sha256, composition_ref, accepted_at; the READY job row (durable_job.py put_state) carries the receipt; neither has an attach field"
    ],
    "remedy": "The packager mint (a later pair) sets package_principal live; until then the idempotence port refuses PACKAGER_PRINCIPAL_UNSET by design.",
    "owner": "2.0.0_SA_COO~G2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G2",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "IRPT_ANLREQ-D2-W62-S3",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AR-g-12 original_ref: the uploaded file a prospect request was filed on is reached at record.owner.prospect_input_id (the normalized upload's upload_id); a custody-lane request has none and is refused ORIGINAL_REF_ABSENT; whether the ticket page's reader (I6) opens an upload id is unread.",
    "evidence": [
      "investigation row IRPT_ANLREQ-D2-W62-S3",
      "infra/aws/lambda/investor-reporting/reports/request_composition.py:75-81 @e7a25ac17b -- upload_id = normalized.source.upload_id must equal owner.prospect_input_id, else PROSPECT_NORMALIZED_OWNER_BINDING"
    ],
    "remedy": "Rule the custody-lane request's original_ref (no prospect upload): refused, or a named substitute shown on the ticket in a sentence.",
    "owner": "2.0.0_SA_COO~Y2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y2",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "IRPT_ANLREQ-D2-W62-S4",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AR-g-12 shapes the neighbouring cells have not fixed: commentary_ref is an artifact_id string in AMENDMENT 1 but a {artifact_id, sha256, version_id} dict in AR-t-12's persist_draft contract, and the draft's bytes shape is unwritten; pdf_ref is an opaque artifact id only when the injected stores carry `artifacts`.",
    "evidence": [
      "investigation row IRPT_ANLREQ-D2-W62-S4",
      "org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md AMENDMENT 1 row I4s @e7a25ac17b -- 'The artifact's opaque id is commentary_ref'"
    ],
    "remedy": "Fix one shape for commentary_ref (string vs {artifact_id, sha256, version_id}) and pdf_ref across AR-g-12 and AR-t-12, with a contract test on both sides.",
    "owner": "2.0.0_SA_COO~Y2",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y2",
      "round": "v2"
    },
    "closed": false
  }
]
```
