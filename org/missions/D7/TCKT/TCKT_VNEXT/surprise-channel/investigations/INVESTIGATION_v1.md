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
    "id": "TCKT_VNEXT-D2-W1-S1",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_TCKT_VNEXT~1",
    "surfaced_at": "2026-10-07T18:10:00Z",
    "one_line": "The order says the analysis_request definition states advisory_fee's default but names no value; the worker chose 1.0 (percent per year).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/task-orders/TCKT_VNEXT.TO-TV-l1.ticket-service-analysis-request.md cell item 2: advisory_fee (number, optional, the definition states its default) -- no number given",
        "org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md:97: advisory fee (default stated) -- no number given",
        "infra/aws/lambda/ticket_center/lambda_function.py TYPE_DEFINITIONS analysis_request advisory_fee: default 1.0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The definition of advisory_fee carries a default the cut or the PRD supplies.",
    "world_is": "Neither the order, the decomp, the PRD nor the portal order carries a numeric default; 1.0 was written as a placeholder the portal shows and the consumer applies. The row stores only what was answered, so changing the default is a one-line edit with no data to migrate.",
    "notes": "Owner of the number is the CRO/CTO (Alyssa's RT-01/RT-02 form). Not blocking."
  },
  {
    "id": "TCKT_VNEXT-D2-W1-S2",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_TCKT_VNEXT~1",
    "surfaced_at": "2026-10-07T18:11:00Z",
    "one_line": "Two order phrases read two ways: the report route check order (403 unless assignee vs 409 unless in_progress), and other types 'reject answers/attachment exactly as today'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ticket_center/lambda_function.py report_ticket: order is 404, 409 not in_progress, 403 not assignee, 409 no attachment, 400 body",
        "infra/aws/lambda/ticket_center/lambda_function.py create_ticket: the four untyped types never read answers/attachment, as before (CREATE has no unknown-field refusal today; only the submit path does)",
        "infra/aws/lambda/ticket_center/tests/test_analysis_request.py test_report_ref_refused_when_open, test_four_existing_types_unchanged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Item 4 lists 403 (not the assignee) before 409 (not in_progress); item 2 says other types reject answers/attachment exactly as today.",
    "world_is": "An open ticket has no assignee, so with 403 first every non-assignee on an open ticket gets 403 and the 409-when-open case is unreachable; the status check therefore runs first (open or completed = 409, in_progress and not the assignee = 403). On CREATE, today's behaviour for an unknown body field is to ignore it silently, so the four types ignore answers/attachment and store neither (asserted by test); a 400 would have changed existing behaviour.",
    "notes": "If the issuer wants 400 on answers/attachment for untyped types, it is a two-line change in create_ticket plus the test."
  },
  {
    "id": "TCKT_VNEXT-D2-W1-S3",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_TCKT_VNEXT~1",
    "surfaced_at": "2026-10-07T18:12:00Z",
    "one_line": "test_authz_matrix.py's layer-coverage test hard-codes 7 actions and 7 routes, so the new REPORT action required a second assertion change beyond the requester-clause one.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ticket_center/tests/test_authz_matrix.py test_layer_coverage_every_route_behind_the_matrix_and_actions_match: assertEqual(len(authorized), 7) now 8; ROUTES gained the /report route",
        "infra/aws/lambda/ticket_center/tests/test_authz_matrix.py test_claim_complete_matrix_and_sod: the requester-claim 403 assertion changed to the new rule (200 on own claim; the kept assignee rule asserted)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "If test_authz_matrix.py asserts the requester clause, change only that assertion.",
    "world_is": "Adding the REPORT action to MATRIX (required by the order) makes the 'authorized == MATRIX keys, count 7' assertion fail unless the count and the route list move with it; that file is inside the grant, and the matrix-coverage intent (every route behind the matrix) is kept and extended to the new route.",
    "notes": "Full ticket_center suite after the change: see the worker report."
  },
  {
    "id": "TCKT_VNEXT-D2-W1-S4",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_TCKT_VNEXT~1",
    "surfaced_at": "2026-10-07T18:13:00Z",
    "one_line": "The existing ticket_center tests call the real SES client on create/submit/claim; on a device whose IAM user may SendRawEmail they would send mail.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~V2 (runs the full ticket-center suite at the drain; the test files outside this order's grant are not the worker's to edit)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python infra/aws/lambda/ticket_center/tests/test_authz_matrix.py -v on dell2 printed WE_CLIENT_SEND_FAILED ... AccessDenied ... ses:SendRawEmail on identity/opalinvest.dev (user cloudops-dell2-agent-user): the call reached AWS and was refused by IAM only",
        "infra/aws/lambda/ticket_center/tests/test_analysis_request.py fresh(): this file replaces notify_dl_isolated and notify_client_isolated with no-ops so it calls no AWS"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The ticket-center test suite is local with no network (test_authz_matrix.py module docstring: 'No network').",
    "world_is": "test_authz_matrix.py does not stub the notifiers, so a create/submit/claim attempts SES; here IAM denies it, elsewhere it could send to client@example.test.",
    "notes": "New tests stub the notifiers; existing test files left as they were."
  }
]
```
