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
