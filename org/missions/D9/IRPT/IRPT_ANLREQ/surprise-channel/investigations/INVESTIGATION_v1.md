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


