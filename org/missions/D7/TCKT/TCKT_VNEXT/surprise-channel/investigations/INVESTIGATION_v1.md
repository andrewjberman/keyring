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
  },
  {
    "id": "TCKT_VNEXT-D2-S2",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "2.0.0_SA_COO~V2",
    "surfaced_at": "2026-10-07T19:05:00Z",
    "one_line": "Disarm record for rows D2-W1-S4 and D2-W1-S1 at the round-1 drain: every ticket_center suite run by the issuer this round ran with invalid AWS keys so no SES send can succeed; the invented advisory_fee default 1.0 was set to None at da43155418.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~V2 (the procedure); the standing fix for S4 (stub SES in the pre-existing ticket_center tests) is carried to the CTO in the round-1 slug",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "AWS_ACCESS_KEY_ID=AKIAINVALIDTCKT AWS_SECRET_ACCESS_KEY=invalid python -m pytest infra/aws/lambda/ticket_center/tests -q at CLOUD da43155418: 89 passed, 43 subtests passed",
        "infra/aws/lambda/ticket_center/lambda_function.py at da43155418: advisory_fee definition default None, comment cites D2-W1-S1",
        "docs/briefs/d7-ticket-center-request-types-analysis-request-first-brief-20261007.md:28 says 'the default fee' and names no value; comp-find for a default fee constant: 2 hits / 61,952 files, neither a fee"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A test run sends no mail, and the service states no fee value nobody ruled.",
    "world_is": "The pre-existing tests still construct a real SES client; only the run procedure keeps them from sending. The fee default is None until someone names the default.",
    "notes": "Which value 'the default fee' is stays open (Alyssa or Andrew); FWD-1's run leaves the fee blank."
  },
  {
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "2.0.0_SA_COO~V2",
    "surfaced_at": "2026-10-07T19:45:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "TCKT_VNEXT-D2-S3",
    "one_line": "The Analysis Request form's firm answer is free text and is sent to the upload door as selectedTenant; it should be a choice from the caller's allowed firms (the door refuses any other firm anyway).",
    "disarm_owner": "2.0.0_SA_COO~V2 (enrichment round: carried to the CTO in the round-1 slug as a TV-p cell)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1.0.0_SA_CTO~DELL2 msg 1013 (review of portal f7fa7fb1 against DEV 3b8c292f): PASS for DEV, with this item to file as a row",
        "portal f7fa7fb1 src/pages/TicketCenter/analysisRequest.ts: firm is a text answer"
      ]
    },
    "spec_asserts": "The person filing picks a firm they may file for.",
    "world_is": "They type a firm id; a wrong one is refused only at the door.",
    "notes": "Not blocking FWD-1."
  },
  {
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "2.0.0_SA_COO~V2",
    "surfaced_at": "2026-10-07T19:45:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "TCKT_VNEXT-D2-S4",
    "one_line": "The report opens through IRPT's OWNED read (getOwnedAnalysisRequest), so only the person who requested the report can open it from the ticket; a different person opening the ticket is refused.",
    "disarm_owner": "2.0.0_SA_COO~V2 (names it in TV-r-1 and in FWD-1's organic arm: Alyssa both requests and opens; a second-reader path is IRPT_YCDGEN's)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1.0.0_SA_CTO~DELL2 msg 1013 (review of portal f7fa7fb1 against DEV 3b8c292f): PASS for DEV, with this item to file as a row",
        "X-2 answer msg 929: a firm advisor or ops user is admitted only for inputs they uploaded themselves (prospect.py:51-59); OPAL_GLOBAL admitted for any creator's input"
      ]
    },
    "spec_asserts": "Anyone opening the ticket later can open its report (FWD-1 hop 5, read with FWD-6's 'anyone opening the ticket later').",
    "world_is": "Only the requester of the report can open it; fine for FWD-1 where one person files, works and opens.",
    "notes": "Carried to the slug; not a round-1 blocker."
  },
  {
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "2.0.0_SA_COO~V2",
    "surfaced_at": "2026-10-07T19:45:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "TCKT_VNEXT-D2-S5",
    "one_line": "The one-account-per-file check (C-ANALYSIS-REQUEST) is in neither round-1 cell; it belongs to the enrichment round (PRD section 3 item 2, FWD-3), and round 1's real run uses a one-account file.",
    "disarm_owner": "2.0.0_SA_COO~V2 (carried to the CTO in the round-1 slug as the FWD-3 cell)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1.0.0_SA_CTO~DELL2 msg 1013 (review of portal f7fa7fb1 against DEV 3b8c292f): PASS for DEV, with this item to file as a row",
        "org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP.md: round 1 is the FWD-1 thread; the enrichment backlog including the one-account check is not in this round"
      ]
    },
    "spec_asserts": "A multi-account file is turned back before anyone at Opal sees it (FWD-3).",
    "world_is": "Round 1 does not check it; the door does not either (PRD R8).",
    "notes": "By design for round 1."
  },
  {
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "2.0.0_SA_COO~V2",
    "surfaced_at": "2026-10-08T22:30:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "TCKT_VNEXT-D2-S6",
    "one_line": "FWD-6 says the draft appears on the SAME ticket and the ticket shows who sent the final commentary and when; workstream F10 (CTO scope msg 1789: svc-commentary CREATE-only) puts the draft on a NEW analysis_request ticket and builds no sent-by/sent-at field.",
    "disarm_owner": "2.0.0_SA_COO~V2 (carried to the CTO in the F10 slug: an append-to-existing-ticket route needs the report to know its ticket, contract O2)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md:57 (FWD-6 text)",
        "1.0.0_SA_CTO~DELL2 msg 1789 (scope: CREATE-only on analysis_request, the two fields, the 08-12 read)",
        "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/FWD10_H6_H5_TICKET_WRITE_CONTRACT.md section 6 O2"
      ]
    },
    "spec_asserts": "The draft lands on the same ticket as the request, and the ticket records who sent the final commentary and when (FWD-6).",
    "world_is": "After F10 the draft lands on a new ticket created by svc-commentary; report_ref lives on the ticket only, so the service cannot find the request's own ticket; no sent-by/sent-at field is built.",
    "notes": "Not built in F10 by scope; FWD-6 grades PARTIAL until a later cell closes both clauses."
  },
  {
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_TCKT_VNEXT~3",
    "surfaced_at": "2026-10-08T23:10:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "TCKT_VNEXT-D2-W3-S1",
    "one_line": "The order words the svc-commentary principal as sub == svc-commentary; the handler resolves every service subject from the authorizer context key email, so the new class matches email == svc-commentary AND userType == service.",
    "disarm_owner": "2.0.0_SA_COO~V2 (F10-d-1 / F10-r-1: the svc-commentary token the authorizer mints must carry the subject in the context field the handler reads as email, as svc-ticket-form and svc-analyst-intake do)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ticket_center/lambda_function.py principal_class: email = actor.get('email'); if email == SVC_TICKET_FORM ... (the existing two service subjects, same key)",
        "infra/aws/lambda/ticket_center/tests/test_authz_matrix.py SVC_FORM / SVC_INTAKE contexts carry the subject in email",
        "org/missions/D7/TCKT/TCKT_VNEXT/task-orders/TCKT_VNEXT.TO-F10-l1.svc-commentary-draft-write.md WORKER FACE item 1 (sub wording)"
      ]
    },
    "spec_asserts": "principal_class resolves sub == svc-commentary AND userType == service to the new class (TO-F10-l1 item 1).",
    "world_is": "The handler has no sub key; the authorizer context field that holds a service subject is email. The class was built on that existing key. Also: AMENDMENT 1 (coordinator message) moved svc-commentary's firm check to env COMMENTARY_ALLOWED_FIRMS; built as a module constant, the order file text itself left unedited because the order's write grant is status flip only.",
    "notes": "If the authorizer mints svc-commentary with the subject only in sub, the class is UNRESOLVABLE and every create is a 403 - the O1 token-mint question in the contract."
  },
  {
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "2.0.0_SA_COO~V2",
    "surfaced_at": "2026-10-08T22:52:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "TCKT_VNEXT-D2-S7",
    "one_line": "infra/aws/terraform/ticket-center/build-and-upload.sh has no BUILD_ONLY mode: BUILD_ONLY=1 still uploaded the F10 package (OuTw3w...) over ticket-center/opal-ticket-api.zip at 22:50:01Z while opal-ticket-api ran y0UF...; the issuer restored the 10-07 version (y0UF..., new version ZBF40mIM...) at ~22:51Z.",
    "disarm_owner": "2.0.0_SA_COO~V2 (disarmed same turn by the restore; the script fix is the script owner's, carried in the F10 slug)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api list-object-versions ticket-center/opal-ticket-api.zip: ICKV1ztn... 2026-10-08T22:50:01Z latest, lx44Hu0g... 2026-10-07T19:16:29Z",
        "copy-object of lx44Hu0g... -> ZBF40mIM..., head-object content-sha256 y0UFtRIfZxu3x6BCFSGLjXsNgScCl/GPuWNHbmZV7BI= = live CodeSha256",
        "grep BUILD_ONLY infra/aws/terraform/ticket-center/build-and-upload.sh: 0 hits",
        "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/TV_D1_DEPLOY_PACKET_20261007.md section 1 cites BUILD_ONLY=1 as a build-only run (it was not)"
      ]
    },
    "spec_asserts": "A build-only read of the package hash writes nothing to the artifact bucket; the artifact key holds what is deployed until the applier's upload.",
    "world_is": "The script always uploads; any later terraform plan on ticket-center would have seen a code change nobody applied.",
    "notes": "Window ~1 min; the Lambda never moved (CodeSha256 y0UF... read before and after). The F10 apply order builds and uploads in its own leg."
  },
  {
      "project": "TCKT_VNEXT",
      "fabric": "dell2",
      "surfaced_by": "0.9.0_WK_TCKT_VNEXT~3",
      "surfaced_at": "2026-10-08T23:25:00Z",
      "class": "BLOCKING",
      "hazard_standing": "INERT",
      "disposition": "UNDER_INVESTIGATION",
      "id": "TCKT_VNEXT-D2-W3-S2",
      "one_line": "Adding the PACKAGE action to MATRIX, as the order says, fails the pre-existing test_authz_matrix.py layer-coverage test (9 != 8 actions); that file is outside the order's <paths>, so F10-l3-AC3 cannot pass.",
      "grounding": {
          "status": "GROUNDED",
          "evidence": [
              "infra/aws/lambda/ticket_center/tests/test_authz_matrix.py:289-292 @c3721347e2: authorized = set(re.findall(r'authorize[(]\"([A-Z-]+)\"', src)); assertEqual(authorized, set(mod.MATRIX)); assertEqual(len(authorized), 8, 'a new one must land in MATRIX AND here')",
              "pytest -q infra/aws/lambda/ticket_center/tests with PACKAGE in MATRIX and authorize(\"PACKAGE\", ...) in package_ticket: 1 failed (test_layer_coverage_every_route_behind_the_matrix_and_actions_match: 9 != 8), 117 passed, 43 subtests passed; baseline before the change 108 passed 0 failed",
              "no spelling satisfies both the order and that test: the set-equality needs the authorize literal, the len==8 needs it absent from a 9-key MATRIX"
          ]
      },
      "spec_asserts": "WORKER FACE item 1: add a PACKAGE action to MATRIX; F10-l3-AC3: the whole ticket_center/tests directory passes at no fewer than the pre-cut count and 0 failed; <paths> excludes test_authz_matrix.py.",
      "world_is": "test_authz_matrix.py pins the route table at exactly 8 actions (and ROUTES at 8 routes) and fails at 9. The worker kept the order's design (PACKAGE in MATRIX as an empty row, authorize call in the route) and did not edit or weaken that test. The fix is a one-line count change plus the package route in ROUTES, in a file the issuer or a later order must grant.",
      "notes": "Every other test passes: 117 passed, the 10 new ones included."
  }
,
  {
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_TCKT_VNEXT~3",
    "surfaced_at": "2026-10-08T23:50:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "TCKT_VNEXT-D2-W3-S3",
    "one_line": "Resolves TCKT_VNEXT-D2-W3-S2: AMENDMENT 1 (commit 6751522799) granted test_authz_matrix.py; the package route is in ROUTES, the pinned action count is 9, and f10-regress now passes. Also: the order file in this worktree was found holding a truncated uncommitted copy and was restored byte-for-byte from 6751522799 before the status flip.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_CHECKS/f10_checks.py f10-regress: F10-REGRESS-OK passed=118 failed=0",
        "infra/aws/lambda/ticket_center/tests/test_authz_matrix.py: ROUTES gains POST /api/scoped/tickets/TCK-20260820-aaaa1111/package; assertEqual(len(authorized), 9, ...); no other line changed",
        "git diff of the order file in the worktree before restore: 71 lines vs 131 at 6751522799 (cell text and acceptance block missing, uncommitted)"
      ]
    },
    "spec_asserts": "AMENDMENT 1: two changes only to test_authz_matrix.py (ROUTES entry, count 8 to 9); F10-l3-AC3 passes at no fewer than the pre-cut count with 0 failed.",
    "world_is": "Both changes landed as specified; 118 passed 0 failed (pre-cut 108 plus the 10 new tests). The worktree copy of the order file was a damaged uncommitted version; it was rewritten from the issuer's commit, not edited by hand.",
    "notes": "Resolves D2-W3-S2; that row is not rewritten."
  }
]
```

## TCKT_VNEXT-D2-S8 -- the mint pair orders a stored-token read-back and grants no reader, so the applier can create the secret but not read it: leg M steps 3-7 are not executable by this seat

```json
{
  "id": "TCKT_VNEXT-D2-S8",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL2",
  "surfaced_at": "2026-10-09T01:15Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "The svc-commentary mint pair orders leg M step 3 to read the STORED token back out of opal/ticketing/svc-commentary and decode its claims, and in the same document grants no reader at all ('No reader is granted in this pair') -- so the applier can CreateSecret but is refused GetSecretValue on the secret it just created, and steps 3 through 7 (the claim read-back and all four arms, which need the token) cannot be executed by this seat; the secret IS created and verified by metadata, and NO rollback trigger has fired.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "MEASURED 2026-10-09 01:13:37Z: create-secret SUCCEEDED -- ARN arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/ticketing/svc-commentary-pXsmuU, VersionId 2950da39-7bc4-4803-b98e-fba53b7d92cb = AWSCURRENT, description byte-equal to the pair's section 3 text with minted 2026-10-09 and rotate by 2026-12-24 filled in",
      "MEASURED same minute: get-secret-value on that secret -> AccessDeniedException, 'User: arn:aws:iam::313476888478:user/cloudops-dell2-agent-user is not authorized to perform: secretsmanager:GetSecretValue on resource: opal/ticketing/svc-commentary'",
      "POSITIVE CONTROL, same identity, same minute: get-secret-value on opal/auth/jwt-private-key ANSWERED (that is the read this leg legitimately makes, reported under msg 1233 rule 2). So the identity holds the ACTION on at least one resource and the refusal is RESOURCE-SCOPED, not an absent action -- AWS's 'no identity-based policy allows' wording would otherwise read as the broader claim",
      "step 1 before-read PASSED first: describe-secret opal/ticketing/svc-commentary -> ResourceNotFoundException, so the secret this seat created is the only one and nothing was overwritten",
      "the pair's own section 3 Reader clause: 'only ~T2's commentary Lambda role, named at H6's deploy. No reader is granted in this pair.' -- the document that orders the read-back is the document that grants no reader",
      "steps 4-7 (positive arm plus the three negative arms) all send the TOKEN over HTTPS, and the only copy of the token is inside the secret, so they inherit the same refusal; they were NOT attempted",
      "NO ROLLBACK TRIGGER FIRED. The pair's triggers are a claim MISMATCH at step 3, a step-5 call returning firm data, a step-6 201, or a CTO/Andrew word. Step 3 did not mismatch -- it was not executable. UNVERIFIABLE is not FAILED, and the secret was therefore left in place rather than deleted"
    ]
  },
  "spec_asserts": "NEVER_WIDEN_PAIR_SVC_COMMENTARY_MINT.md section 4 step 3: 'Read back: decode the stored token WITHOUT verifying; the claim set must equal section 2 exactly (no firmId, no role), and exp - iat <= 90d.'",
  "world_is": "Step 2 is done and step 3 is not executable by the seat the order names. The claim set WAS built to section 2 exactly in the minting process (sub, userType service, tier service, name, iss opal-portal-auth, aud opal-portal-api, iat, exp = iat + 90 days, with firmId/role/advisorId/allowedPages/allowedTabs/firmRole absent), and exp reads 2027-01-07T01:13:37Z which is iat + 90 days -- but THAT IS THE PRODUCER'S OWN ACCOUNT OF WHAT IT SIGNED, not the independent read of stored bytes the step asks for, and this row does not dress it up as one. The remedy is a laptop act either way, because the Dells cannot write IAM: add one secretsmanager:GetSecretValue statement for cloudops-dell2-agent-user on this exact ARN so this seat can finish steps 3-7, or have a laptop seat run step 3 and the four arms and return the result as a file (the standing rule of msg 215 shape). Re-running the mint is NOT the remedy: the secret exists, and a second create would mint a second token. Current risk is low and stated rather than assumed: no reader is granted to anyone yet, so nothing can consume the token, and the pair's own position is that the real control is leg D's code clamp plus the CREATE-only matrix, both of which are deployed and verified."
}
```

## TCKT_VNEXT-D2-S9 -- the svc-commentary read grant reaches dell1 as well as dell2 (shared Dell platform-key policy); the pair names dell2 only

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-09T02:13:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "TCKT_VNEXT-D2-S9",
  "one_line": "The svc-commentary read grant reaches dell1 as well as dell2: the laptop put the one ARN in the SHARED Dell platform-key policy, while the signed pair (COO AMENDMENT 1 @b70dd6fbad, CTO 1.2) names dell2's allow-list only.",
  "disarm_owner": "1.0.0_SA_CTO~DELL2 (rule: accept the parity with svc-analyst-intake on both Dells, or narrow to dell2; carried in the F10 slug)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "0.0.0_AB_MSTR~DELL2 msg 2170 relaying laptop 2.0.0_SA_COO~C msg 107630: cloudops-dell2-agent-user AND cloudops-dell1-agent-user each allowed GetSecretValue on opal/ticketing/svc-commentary-pXsmuU (policy default v3)",
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_DEPLOY/NEVER_WIDEN_PAIR_SVC_COMMENTARY_MINT.md COO-half AMENDMENT 1: 'add the ONE ARN ... to dell2's existing secretsmanager:GetSecretValue allow-list'"
    ]
  },
  "spec_asserts": "One reader is added: cloudops-dell2-agent-user.",
  "world_is": "Two readers were added, dell2 and dell1, through the shared Dell platform-key policy. That matches how svc-analyst-intake is held, but it is one identity wider than the pair says.",
  "notes": "No dell1 seat holds TCKT_VNEXT work. A read by dell1 would be a credential first-read, which the standing rule requires it to report."
}
```

## TCKT_VNEXT-D2-S10 -- leg M step 4 is unsatisfiable without an attachment the pair never supplies, and step 6's expected 400 comes from the attachment check rather than the firm clamp (a status-only false pass)

```json
{
  "id": "TCKT_VNEXT-D2-S10",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL2",
  "surfaced_at": "2026-10-09T02:15Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "Leg M's positive arm cannot succeed as written and its second negative arm cannot exercise what it is for: analysis_request requires an attachment {upload_id, input_id} with input_id matching ^portfolio_[0-9a-f]{64}$ and NO svc-commentary exemption, while the mint pair's step 4 supplies no attachment -- and because _validate_attachment (line 1063) runs BEFORE _create_firm_allowed (line 1072), the off-list-firm arm returns the expected 400 for the WRONG reason, so a status-only reading of it is a false pass.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "MEASURED 2026-10-09 ~02:1xZ through https://opalinvest.dev with the real svc-commentary token: step 4 POST /api/scoped/tickets, ticket_type analysis_request, answers.firm cottonwood, report_type Overview, report_request_id test-f10-20261009-one, draft_commentary {text,model,generated_at,status=DRAFT} -> HTTP 400 {\"error\": \"attachment is required: {upload_id, input_id}\"}. No ticket was created, so created_by could not be read",
      "infra/aws/lambda/ticket_center/lambda_function.py:643-657 _validate_attachment: the attachment is unconditionally required for a type that declares one; the only svc-commentary exemption in the type definition is on the QUESTION 'household' (line 89 optional_for: [SVC_COMMENTARY]), and there is no equivalent on the attachment",
      "ORDERING, line-cited: _validate_attachment is called at :1063 and _create_firm_allowed at :1072. So an svc-commentary create for an off-list firm WITHOUT an attachment refuses at :1063 and NEVER REACHES the firm clamp at :1072",
      "MEASURED consequence: step 6 (firm=demo, off COMMENTARY_ALLOWED_FIRMS) returned HTTP 400 -- the status the arm expects -- with body {\"error\": \"attachment is required: {upload_id, input_id}\"}, identical to step 4's. The firm clamp was never exercised. A tester comparing only the status code would record a PASS for an arm that tested nothing, which is the ABSENT != EXERCISED-AGAINST shape",
      "THE TWO ARMS THAT DID RUN CLEANLY, both meaningful: step 5 arm 1a GET /api/scoped/investor-reporting/directory/search?selected_tenant=cottonwood -> HTTP 200 but ok:false, state UNAVAILABLE, 0 rows (no firm data); step 5 arm 1b GET /api/scoped/advisor-intelligence/artifacts/architect_leaderboard.json -> HTTP 403 'Missing firm identity', which is a direct live confirmation of the pair's central claim that the token carries NO firm reach; step 7 GET /api/scoped/tickets -> HTTP 403 {\"error\": \"forbidden: LIST is not permitted to principal class 'svc-commentary'\", \"action\": \"LIST\", \"principal_class\": \"svc-commentary\"}",
      "step 3 PASSED independently on the STORED bytes before any arm ran: 8 claims, names exactly section 2's set, fixed values matching, the six forbidden claims absent, exp - iat = 7776000 s = exactly 90.00 days; secret VersionId 2950da39-7bc4-4803-b98e-fba53b7d92cb",
      "the attachment's input_id pattern ^portfolio_[0-9a-f]{64}$ is the analysis-input-upload flow's own output shape (release 3 recorded input_id portfolio_7112270b57ed..), so satisfying step 4 requires a COMPLETED analysis upload first -- a dependency the mint pair does not name"
    ]
  },
  "spec_asserts": "NEVER_WIDEN_PAIR_SVC_COMMENTARY_MINT.md section 4 step 4: 'The token through the CloudFront API path does POST /api/scoped/tickets with an analysis_request for cottonwood, a draft_commentary (status DRAFT, text [TEST TCKT_VNEXT F10] draft) and a report_request_id test-f10-<run>. Expect 201; created_by == svc-commentary.' Step 6: 'the same token creates an analysis_request for demo (off the list). Expect 400.'",
  "world_is": "Step 4 as written is not satisfiable: the body it specifies is complete except for an attachment the ticket type requires unconditionally, and the required input_id is a portfolio_<64 hex> id that only a completed analysis-input-upload produces. So leg M's positive arm has an unnamed dependency on that upload flow. Step 6's expected 400 IS returned, but by the attachment check rather than the firm clamp, so the arm does not currently test the thing it exists to test; its status assertion is satisfiable without the clamp working at all. Steps 3, 5 and 7 are genuinely satisfied and are recorded as PASS. Nothing is asked of this seat beyond the record and the ask: the remedy is the issuer's -- either supply a real {upload_id, input_id} for step 4 (which makes step 6 reach the clamp too), or re-cut step 6 to assert the firm-refusal REASON rather than the status alone. No ticket was created, so there is no test ticket to close under step 8 and none is claimed."
}
```

## TCKT_VNEXT-D2-S11 -- L9 TO-APPLY-F10 AC2 MET

```json
{
  "id": "TCKT_VNEXT-D2-S11",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T03:47:27Z",
  "one_line": "L9 TO-APPLY-F10 AC2 MET. Leg D read live by this seat: opal-ticket-api CodeSha256 RFRuryx.., LastModified 2026-10-09T01:01:08Z, Successful, COMMENTARY_ALLOWED_FIRMS '49financial,cottonwood,inflection', POST /api/scoped/tickets/{ticketId}/package live with CUSTOM auth (117 routes, every page read). Leg M: step 4 201 created_by svc-commentary; step 6 400 whose message names the firm, so the clamp at :1072 was reached (D2-S10's false-pass shape is closed by AMENDMENT 2); steps 3, 5a, 5b, 7 as the pair predicts.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier2_senior/0.7.0_AE_CloudOps~DELL2/deliverables/tckt_f10/F10-M_arms_result.json @5c513af524",
      "org/critical_paths/change_management/20261009T0056Z_tckt-vnext-f10-d1-mint-20261009_deploy_completion.md (CLOSED 4/4)",
      "aws lambda get-function-configuration / apigatewayv2 get-routes, this seat ~03:3xZ",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_F10_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-APPLY-F10 AC2: steps 5 and 6 (deployed bytes and env), and leg M's positive arm plus its negative arms.",
  "world_is": "Met as written. Weighed: (a) the positive arm used a synthetic attachment, so it proves the write path and claims, not real report ids (H6 / TV-r-1 carry that); (b) test ticket TCK-20261009-a1052909 stays open on Andrew's word (35fabf20c8); (c) the dell1 reach is D2-S9, the CTO's. None changes the grade."
}
```

## TCKT_VNEXT-D2-W6-S1 -- Neither candidate one-firm token meets the CTO's bar: both authorizer-resolve to allowedFirmIds=opal-capital, so a ticket CREATE for 49financial is refused 400 and 27 of 117 portal routes reach more than one firm

```json
{
  "id": "TCKT_VNEXT-D2-W6-S1",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~6",
  "surfaced_at": "2026-10-09T04:05Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "Neither candidate one-firm token meets the CTO's bar: both authorizer-resolve to allowedFirmIds=opal-capital, so a ticket CREATE for 49financial is refused 400 and 27 of 117 portal routes reach more than one firm",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.json: rows=117, per token ONE_FIRM=36 NO_FIRM=51 MORE_THAN_ONE=27 UNRESOLVED=3 (sa_checks.py sa-census: SA-CENSUS-OK)",
      "infra/aws/users/lambda/portal-authorizer/index.mjs:293-322 computeAllowedFirms: ALL only for userType Dev or tier internal; otherwise the own firmId",
      "infra/aws/lambda/ticket_center/lambda_function.py:310-315 _firm_allowed and :1072-1073 the CREATE refusal",
      "infra/aws/lambda/investor-reporting/_authz/served.py:1124-1137 selected_tenant admitted for any internal caller; the allowedFirmIds clamp only when x-user-type is service"
    ]
  },
  "spec_asserts": "CTO msg 2342 requires the synthetic test-filer row clamped to ONE firm (49financial) on every /api/scoped route it can reach, and the FWD-1 design has this filer, as INTERNAL (firmId opal-capital), file an Analysis Request for 49financial.",
  "world_is": "Both T_ADVISOR_OPAL and T_SERVICE_TIER_OPAL get allowedFirmIds=opal-capital (only userType Dev or tier internal yields ALL), which (a) fails _firm_allowed for answers.firm=49financial so CREATE returns 400, and (b) leaves 6 ticket routes (list, metrics, get, claim, complete, report) with no firm check and 21 investor-reporting routes admitting any of 3 client firms via selected_tenant (the allowedFirmIds clamp there is service-only). Census: 117 routes, MORE_THAN_ONE=27, UNRESOLVED=3 per token.",
  "notes": "The smallest clamps (a FILER_ALLOWED_FIRMS env map in the COMMENTARY_ALLOWED_FIRMS pattern, in _firm_allowed and at served.py:1134) are written in SA_ROUTE_CENSUS.md section 2. Neither is built here; this order is read-only."
}
```

## TCKT_VNEXT-D2-W6-S2 -- The data-refresh routes (including trigger and rollback) admit a caller whose userType is absent, so a one-firm test filer token reaches platform-wide data operations that have no firm axis

```json
{
  "id": "TCKT_VNEXT-D2-W6-S2",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~6",
  "surfaced_at": "2026-10-09T04:05Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "The data-refresh routes (including trigger and rollback) admit a caller whose userType is absent, so a one-firm test filer token reaches platform-wide data operations that have no firm axis",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/data_refresh/lambda_function.py:160-167: 'Allow Dev users or users without userType restriction' returns True when user_type is empty",
      "infra/aws/lambda/data_refresh/lambda_function.py:1830-1865 routes: POST /data-refresh/trigger, POST /data-refresh/rollback, POST /data-refresh/upload-urls",
      "infra/aws/users/lambda/portal-authorizer/index.mjs:406 userType: decoded.userType || 'null' (no claim becomes the string null)"
    ]
  },
  "spec_asserts": "The CTO's bar is about FIRM reach, and the census treats a route that reads no firm as NO_FIRM; nothing in the order suggests a no-userType token can run platform operations.",
  "world_is": "opal-data-refresh-api validate_user_type admits userType 'Dev' OR empty and maps the authorizer's 'null' string to empty, so any token without a userType passes the gate on all 9 data-refresh and security-scanner routes (trigger, rollback, upload-urls included). The same census shows the trade-desk dashboard/workflow routes, portal-content GET and the market data proxy read no identity or firm either. These 51 NO_FIRM rows satisfy a firm bar and are still reachable by the filer. Whether production users carry a userType is data, not in source.",
  "notes": "Not a defect of this order. Raised because a token mint that clears the firm bar would still hold these routes; a mint with userType set to a non-Dev value would be refused here (:168-170).",
  "disarm_owner": "1.0.0_SA_CTO"
}
```

## TCKT_VNEXT-D2-W6-S3 -- The portal route denominator cannot be completed from source: a console-only default route and live-only routes exist, and the IRPT route contract's own denominator is stale

```json
{
  "id": "TCKT_VNEXT-D2-W6-S3",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~6",
  "surfaced_at": "2026-10-09T04:05Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "The portal route denominator cannot be completed from source: a console-only default route and live-only routes exist, and the IRPT route contract's own denominator is stale",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/shared-infra/apigateway-portal/routes.tf:1-2 and main.tf:53-57: $default route and stage console-only",
      "infra/aws/terraform/partners-api/api-gateway.tf:12-13: /api/shared/ routes manually created and never in Terraform",
      "docs/contracts/investor-reporting/v1/routes.json lines 271-279 _denominator vs a count of its routes array: DECLARED 21, ROUTED_ELSEWHERE 2"
    ]
  },
  "spec_asserts": "The order says to enumerate every route on the portal API across all Terraform roots under infra/ and that comp-routes is not complete.",
  "world_is": "Source yields 116 routes plus the console-only $default (khcd4f1, no authorization setting in source, integration s7ntfz4 opal-portal-data-proxy). partners-api/api-gateway.tf:12-13 says the /api/shared/advisor-intelligence/* routes were manually created and never in Terraform, so any still live are invisible to source. docs/contracts/investor-reporting/v1/routes.json _denominator says declared=19 while the file holds 21 DECLARED plus 2 ROUTED_ELSEWHERE (23 rows).",
  "notes": "A live apigatewayv2 get-routes read would close the console-only part; it was barred by this order (no AWS call). The census JSON records the gap in denominator.not_in_source."
}
```

## TCKT_VNEXT-D2-S12 -- disposition of ARMED row D2-W6-S2: measured real (45 profiles), fix ruled fail-closed, routed cross-box; stays ARMED until live

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-09T04:08:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "TCKT_VNEXT-D2-S12",
  "one_line": "Disposition record for ARMED row TCKT_VNEXT-D2-W6-S2 (data-refresh admits callers with no userType): measured REAL by 1.0.0_SA_CTO~DELL2 (45 opal-users-v2 PROFILE rows lack userType: 43 user, 2 admin); fix ruled fail-closed (admit only Dev or opal-capital internal); routed cross-box via 0.0.0_AB_MSTR~DELL2 (~02:1xZ... 04:0xZ msg); W6-S2 stays ARMED until the fix is live.",
  "disarm_owner": "the data_refresh Lambda's owning project (routed by 1.0.0_SA_CTO~DELL2 through 0.0.0_AB_MSTR~DELL2); TCKT_VNEXT builds nothing on it",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "1.0.0_SA_CTO~DELL2 msg 2361 (Re 2358): read-only census 45 PROFILE rows without userType; authorizer passes userType 'null'",
      "infra/aws/lambda/data_refresh/lambda_function.py:165-167 'if not user_type or user_type == Dev: return True' (read by the issuer at 41b7e28bdf)"
    ]
  },
  "spec_asserts": "Only Dev or Opal-internal callers may trigger or roll back a data refresh.",
  "world_is": "Any authenticated portal user whose profile lacks userType (45 rows today) is admitted to the data-refresh routes, trigger and rollback included.",
  "notes": "Disposition only; W6-S2 itself is append-only and not rewritten."
}
```

## TCKT_VNEXT-D2-W7-S1 -- The existing ticket_center tests reach the live users table when a box holds AWS credentials; closed in the test setups by an empty users stand-in

```json
{
  "id": "TCKT_VNEXT-D2-W7-S1",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~7",
  "surfaced_at": "2026-10-09T04:30:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "The existing ticket_center tests reach the live opal-users-v2 table whenever a box holds AWS credentials: _directory_snapshot ran un-faked on every claim, and the new profile-scope lookup would have run on every internal call",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ticket_center/tests/test_authz_matrix.py (at 050b5f0f0f): mod._ddb is the real boto3 dynamodb ServiceResource and no setUp replaces it; boto3.Session().get_credentials() on this box resolves from the shared-credentials-file",
      "measured by the worker: pytest of infra/aws/lambda/ticket_center/tests took 15.78s with credentials resolvable and 0.84s with AWS_SHARED_CREDENTIALS_FILE and AWS_CONFIG_FILE pointed at a missing file (both 118 passed at that point)",
      "after the fix: the same directory, credentials blanked, 131 passed in 1.47s; the empty-users stand-in is EmptyUsersDdb in test_authz_matrix.py, installed by test_authz_matrix, test_analysis_request fresh(), test_we_dl_notice and test_client_notify setUp"
    ]
  },
  "spec_asserts": "The order says NO AWS call, and that an existing test whose fake has no users table and now hits the lookup gets an empty users table in that test's setup.",
  "world_is": "The suite already issued read-only Query/GetItem calls to the live opal-users-v2 on every claim (the pre-existing directory enrichment), silently, because the soft-fail swallows the result; the worker's first full run after adding the scope lookup and one probe call did the same (read-only, no write, nothing applied). The suite never failed on it, so the order's 'now hits the lookup' premise was already true at base for the claim path. Now closed in four test files (test_commentary_write and test_package_route ride test_analysis_request's fresh()); test_directory_resolution.py and the new test file install their own users doubles.",
  "notes": "Read-only calls only, from the worker's first test run and one probe, before the stand-in landed. No IAM or data effect. A box without credentials never saw this."
}
```

## TCKT_VNEXT-D2-S13 -- L9 workstream SA: SA-c1-AC2 MET, TO-APPLY-SA1 AC2 MET

```json
{
  "id": "TCKT_VNEXT-D2-S13",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T05:21:38Z",
  "one_line": "L9 workstream SA: SA-c1-AC2 MET -- the census N=117 (116 declared routes over 8 roots + the console-only $default) equals the live route count this seat read over every page at ~03:3xZ; each verdict cites its line, and the 3 it cannot resolve from source are named UNRESOLVED, not forced. TO-APPLY-SA1 AC2 MET -- live package = uploaded zip, the deployed lambda_function.py = the pin's bytes (21fe06e0), env 8 keys unchanged, unauthenticated POST 401, ItemCount 13, replan 0-diff; the plan's s3_object_version move is this module's pinned-artifact mechanics (same as F10's accepted plan).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.SA.md @8c48e44f64",
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.json",
      "org/tier2_senior/0.7.0_AE_CloudOps~DELL2/deliverables/tckt_sa1/SA1_after_reads.json",
      "this seat's live reads ~05:2xZ: opal-ticket-api CodeSha256 ywAvsfx/j3RT... (= the uploaded package), LastModified 2026-10-09T04:57:46Z, Successful, 8 env keys; git show 6e19a53535:infra/aws/lambda/ticket_center/lambda_function.py sha256 21fe06e0d46bbfe5... (= the deployed member)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_SA_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "SA-c1-AC2 and TO-APPLY-SA1 AC2 (the two judgment criteria of workstream SA).",
  "world_is": "Both met as written; notes in the grade file."
}
```

## TCKT_VNEXT-D2-S14 -- W6-S3 disposition: live route list (117) = census (117), diff empty

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-09T05:31:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "TCKT_VNEXT-D2-S14",
  "one_line": "Disposition of TCKT_VNEXT-D2-W6-S3 per CTO msg 2568 (the census denominator is the LIVE route list): apigatewayv2 get-routes on the portal API 7k3ed8px20 (CLI auto-paginated) returns 117 routes; normalized against the census's 117 rows, live-not-in-census = 0 and census-not-live = 0, so the console $default and every manual route are already counted.",
  "disarm_owner": "1.0.0_SA_CTO~DELL2 (ruled the denominator); nothing left open on W6-S3's census-coverage question",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws apigatewayv2 get-routes --api-id 7k3ed8px20 at ~05:3xZ: 117 Items, 117 distinct RouteKeys after normalizing path parameters to {}",
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.json: 117 rows, 117 distinct",
      "1.0.0_SA_CTO~DELL2 msg 2568 (W6-S3 ruling)"
    ]
  },
  "spec_asserts": "The census denominator is the live route list, with the source diff named.",
  "world_is": "Live 117 = census 117; the source diff is empty.",
  "notes": "The IRPT routes.json _denominator mismatch (19 vs 21) inside the source remains a documentation defect in that file, not a census gap."
}
```

### TCKT_VNEXT-D2-S2 -- TO-APPLY-SA1 is STALE THREE WAYS; running it as written would REVERT two later releases of opal-ticket-api

- **owner:** `0.7.0_AE_CloudOps~DELL2`
- **disarm_owner:** `2.0.0_SA_COO~V2` (the issuer; it chooses re-pin or withdraw -- this seat cannot)
- **state:** BLOCKING-CANDIDATE. Nothing degrades while it waits, because the correct act is to NOT
  deploy. The hazard is that the order still reads `pending` and its branch A looks runnable.
- **spec_asserts:** TO-APPLY-SA1 deploys `opal-ticket-api` at `box/dell2 6e19a53535` with
  `lambda_function.py` sha256 `21fe06e0...`; STOP 1 is that
  `git diff --name-only 6e19a53535 HEAD -- infra/aws/lambda/ticket_center infra/aws/terraform/ticket-center`
  is EMPTY, and the BEFORE read expects live `CodeSha256` `RFRuryx...`.
- **world_is:** three independent staleness facts, each measured:
  1. **STOP 1 is NOT empty: 6 files differ**, and one of them is `lambda_function.py` itself -- the
     very file whose hash the order pins. (Control: the same diff over `org/tier2_senior` returns
     241 files, so the command works and an empty result would have meant something.)
  2. **SA1's pin is OLDER than the pin already released.** `merge-base --is-ancestor 6e19a53535
     86454002bf` returns rc 0 and the reverse does not, so SA1's pin PRECEDES TO-APPLY-V12's, which
     was applied and graded MET by its issuer. The per-file hashes line the three up in order:
     SA1 `21fe06e0`, V12 `04f5727b`, HEAD `670686262068`. Deploying SA1 would put the OLDEST of the
     three onto the function.
  3. **The BEFORE expectation is already false.** Live `opal-ticket-api` reads
     `HK82TEd0SQWeGqWEEG7HV10QK8agPizblDoXkvITRJA=`, which is neither SA1's expected `RFRuryx...`
     nor V12's `IMJsVN6U`. So the function has moved at least once since V12 as well.
- **why this is the dangerous shape rather than a nuisance:** every one of SA1's own guards would
  have caught it -- STOP 1, the BEFORE read, and the zip hash check. The order is well built. The
  hazard is that a seat under time pressure reads "branch B" as a formality and re-pins forward to
  make the diff empty, which is precisely how the oldest artifact wins. Branch B here means STOP,
  not "adjust the pin until it passes".
- **cross-project note worth the issuer's attention:** `opal-ticket-api` is now targeted by TWO
  projects -- TCKT_VNEXT (this order, D7) and IRPT_ANLREQ (V12 applied, and R13 re-issued to an
  MSTR-seated CloudOps lane under ruling @5ff94852a6 item 2, D9). One function, two projects, two
  appliers. Nothing in either order's bounds mentions the other, so neither would see the clash.
- **acts NOT taken:** no ledger opened, no build, no upload, no plan, no apply. Nothing of SA1 ran.

- **RESOLVED 2026-10-09 ~12:5xZ, and the cause was narrower than this row first implied.** Issuer
  `2.0.0_SA_COO~V2` (msg 3281) confirmed the STOP was right and ruled the order WORLD-DONE: SA1 had
  ALREADY been applied by `0.7.0_AE_CloudOps~DELL2` at 04:57:46Z, ledger
  `tckt-vnext-sa1-clamp-20261009` CLOSED 05:01:11Z, branch A, deployed file `21fe06e0...` -- and was
  simply never flipped out of `pending`. So the three staleness facts are exactly what an
  already-executed order looks like once HEAD moves on, not a defect in the order. STOP 1 held when
  it mattered: its own after-reads record `changed_paths_pin_to_head=0` beside a
  `positive_control_org_paths=142`, so the zero was a real absence at the time.
  **What this row got right and is worth keeping:** the hazard of a world-done-but-unflipped order is
  RE-EXECUTION, and the tempting fix -- re-pin forward until the diff is empty -- is precisely how the
  oldest artifact wins. That is NEVER-2's rule in the general case: world-done closes SUPERSEDED,
  never re-executes. Disposition: the order is flipped `complete -- SUPERSEDED`, its proof instance
  is VALID rc=0, and cell SA-k-1 lives on in TO-APPLY-V12 and R13b. The two-project overlap on
  `opal-ticket-api` is acknowledged by the issuer, which owns both lines, so it is not an open call.

## TCKT_VNEXT-D2-S15 -- seat-arm pair v2.1: hop (b) ticket CREATE cannot pass for any firm (token reach and row scope are disjoint)

```json
{
  "id": "TCKT_VNEXT-D2-S15",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-09T15:42:00Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "Pair v2.1's synthetic filer cannot file the FWD-1 ticket: CREATE requires the firm in BOTH the token's authorizer-derived allowedFirmIds and the PROFILE row's scope list, and v2.1 makes them disjoint (token tier advisor -> 'opal-capital'; row [49financial]), so 49financial fails the first check and opal-capital the second. Found by the executor before hop (b) ran; confirmed from the code.",
  "disarm_owner": "2.0.0_SA_COO~V2 (pair v2.2 to the CTO; asked 15:41Z)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ticket_center/lambda_function.py:339-344 _create_firm_allowed: return _firm_allowed(actor, firm) and _in_profile_scope(actor, firm)",
      "infra/aws/lambda/ticket_center/lambda_function.py:331-336 _firm_allowed: firm must be in the token's allowedFirmIds csv unless 'ALL'",
      "infra/aws/lambda/ticket_center/lambda_function.py:391-393 _in_profile_scope: firm must be in the PROFILE list when one exists",
      "R1_RUN/TV_R1_SEAT_ARM_PLAN_AND_PAIR.md v2.1: token tier advisor, role user (authorizer allowedFirmIds = opal-capital, census); row allowedFirmIds [49financial]",
      "0.7.0_AE_CloudOps~TV2 msg 3584 (inferred from deployed bytes, being measured)"
    ]
  },
  "spec_asserts": "Pair v2 / v2.1 section 2.3(b): the filer creates an analysis_request ticket for 49financial, and the clamp narrows it to that one firm.",
  "world_is": "With a non-ALL token, the clamp can only narrow the token's own reach, which is opal-capital alone; it cannot admit 49financial. The test filer can reach no client firm on CREATE, so v2.1 proves one-firm safety but cannot complete FWD-1.",
  "disposition": "UNDER_INVESTIGATION"
}
```

## TCKT_VNEXT-D2-S16 -- W6-S2's fix is live, and it is why the pair's data-refresh arm cannot be met (v2.1 measured 200; v2.2 no better)

```json
{
  "id": "TCKT_VNEXT-D2-S16",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~TV2",
  "surfaced_at": "2026-10-09T15:52:00Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "W6-S2's routed fix is LIVE, and it is why the seat-arm pair's data-refresh expectation cannot be met: validate_user_type now admits 'Dev' OR an Opal-internal principal, and _is_opal_internal is true on tier=='internal' OR firmId=='opal-capital'. The filer must carry firmId opal-capital for the ticket service to class it INTERNAL, so it is admitted as Opal-internal and userType is never consulted. This was the measured STOP of SA-r-1 under v2.1, and v2.2 (internal tier) does not close it either.",
  "disarm_owner": "1.0.0_SA_CTO~DELL2 with 2.0.0_SA_COO~V2 -- the pair's 'one data-refresh route: refused' arm needs re-ruling or qualifying; this seat builds nothing on it",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "MEASURED LIVE: GET https://d2n2nzpeqf34ge.cloudfront.net/api/scoped/data-refresh/history -> HTTP 200 for a token with userType 'test-filer', tier advisor, role user, firmId opal-capital (SA-r-1 run SA-r-1-2026-10-09T15:40:57Z, trace R1_RUN/sa_r1_trace.json one_firm_proof.data_refresh)",
      "THE ADMIT PROVES THE NEW GATE IS DEPLOYED: the pre-fix gate was 'if not user_type or user_type == Dev: return True' (cited in row D2-S12), which REFUSES a non-empty non-Dev userType. A non-empty 'test-filer' was admitted, so the live bytes are the post-fix gate, not the pre-fix one -- W6-S2's empty-userType hole is closed and the admit came through the INTERNAL limb",
      "infra/aws/lambda/data_refresh/lambda_function.py validate_user_type: 'Admit a caller that is Dev OR Opal-internal; refuse everything else'",
      "infra/aws/lambda/data_refresh/lambda_function.py _is_opal_internal: returns True if tier == OPAL_INTERNAL_TIER, or if firmId == OPAL_INTERNAL_FIRM_ID ('opal-capital')",
      "opal-data-refresh-api CodeSha256 qHMjXkK1/1NhmBmkK/6Q+q+WdXMRoTOprNfTixBIxaM=, LastModified 2026-10-09T07:59:39Z (get-function-configuration)",
      "ticket_center/lambda_function.py principal_class: INTERNAL is keyed on firmId == 'opal-capital', so the filer cannot drop that claim and still reach CLAIM/REPORT",
      "parents: row TCKT_VNEXT-D2-W6-S2 (the reach) and TCKT_VNEXT-D2-S12 (its fix ruled fail-closed, 'admit only Dev or opal-capital internal')"
    ]
  },
  "spec_asserts": "Pair v2.1 (CTO W6-S2 ruling msg 2568): giving the test filer a non-empty, non-Dev userType ('test-filer') makes data_refresh refuse it, because the gate admitted only an empty userType or 'Dev'. Pair v2.2 step 3 keeps the same arm: 'one data-refresh route: refused'.",
  "world_is": "The gate that premise describes is no longer the deployed one. W6-S2's ruled fix replaced it with 'Dev OR Opal-internal', and Opal-internality is satisfied by firmId 'opal-capital' alone -- the exact claim the ticket plane requires of the filer. So userType is not a lever on this route for ANY token the pair can mint: v2.1 is admitted (measured 200) and v2.2's internal tier satisfies the first limb directly. The arm is unmeetable until the data-refresh side changes, not until the pair changes.",
  "disposition": "UNDER_INVESTIGATION"
}
```

## TCKT_VNEXT-D2-S17 -- data_refresh admits any Opal-internal caller whatever its userType (routed to the data_refresh owner, CTO msg 3619)

```json
{
  "id": "TCKT_VNEXT-D2-S17",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-09T16:04:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "data_refresh's validate_user_type admits a caller as Opal-internal on firmId opal-capital OR tier internal and then admits it whatever its userType, so a synthetic or test userType (here 'test-filer') gains the same data-refresh write-path reach as Opal staff. The W6-S2 premise that a non-empty, non-Dev userType is refused there does not hold in the deployed code.",
  "disarm_owner": "2.0.0_SA_COO~O (NFRA_OPLGTW, owner of the data_refresh admission: TO-OG-da-1)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/data_refresh/lambda_function.py:142-163 is_opal_internal: tier == 'internal' -> True; firmId == 'opal-capital' -> True",
      "infra/aws/lambda/data_refresh/lambda_function.py validate_user_type: userType 'Dev' admits; otherwise is_opal_internal(context) admits, userType not consulted",
      "last change: d9539cc0b7 (NFRA_OPLGTW.TO-OG-da-1 Phase A); live per lambda-source-map: opal-data-refresh-api last_deployed_at 2026-10-09T07:59:39Z",
      "0.7.0_AE_CloudOps~TV2 msg 3607 and row TCKT_VNEXT-D2-S16 (the seat-arm STOP arm that this defeats)",
      "CTO msg 3619 (v2.2 half AMENDMENT 1 @133952758b): the arm is dropped for the run; the admission finding goes to the data_refresh owner as a row"
    ]
  },
  "spec_asserts": "CTO ruling msg 2568 (TCKT_VNEXT W6-S2): a non-empty, non-Dev userType (e.g. 'test-filer') is refused by data_refresh.",
  "world_is": "Any principal with firmId opal-capital or tier internal is admitted to data_refresh regardless of userType. TCKT_VNEXT's seat-arm run neither probes nor calls data_refresh, and proves 0 calls from the logs (SA-r-1b AMENDMENT 2). Whether a test userType should be refused there is the owner's call.",
  "disposition": "UNDER_INVESTIGATION"
}
```

## TCKT_VNEXT-D2-S18 -- irpt-status 500s on 7 live routes after its 15:43:11Z redeploy (TypeError in build_retained_repositories); 6 of the 27 ungradeable and FWD-1's hop (e) blocked

```json
{
  "id": "TCKT_VNEXT-D2-S18",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~TV2",
  "surfaced_at": "2026-10-09T16:32:00Z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "one_line": "irpt-status answers HTTP 500 on 7 live routes after its 2026-10-09T15:43:11Z redeploy: TypeError build_retained_repositories() got an unexpected keyword argument 'additional_policy_revisions'. 6 of the 27 clamped routes therefore cannot be graded for the firm clamp at HEAD, and FWD-1 cannot complete because hop (e) polls one of them. Measured before and after: the same routes answered 200 with sane refusal envelopes at 15:40Z.",
  "disarm_owner": "the IRPT_BCKEND release line that deployed irpt-status at 15:43:11Z, routed via 2.0.0_SA_COO~V2 to the owning COO/CTO; TCKT_VNEXT builds nothing on it and this seat changes no code",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "MEASURED LIVE 16:19Z through CloudFront (run SA-r-1b-2026-10-09T16:19:13Z): HTTP 500 on GET /api/scoped/investor-reporting/status, /status/{jobId}, /analysis/requests, /analysis/requests/{requestId}, /analysis/requests/{requestId}/pdf, /analysis/{jobId}/sections, and the live-only /analysis/requests/{requestId}/original -- for the own firm AND both off-list firms, so the clamp is not reached",
      "THE HOST'S OWN LOG: /aws/lambda/irpt-status, 47 matching events over 16:18-16:26Z: '[ERROR] TypeError: build_retained_repositories() got an unexpected keyword argument additional_policy_revisions', Traceback /var/task/read_memo.py line 93 in scoped then /var/task/served...",
      "DEPLOYED STATE: irpt-status CodeSha256 VC/r14kaXm6FqaZOOFm3fT+8qngsyGI5Yr7U+DgYx64=, LastModified 2026-10-09T15:43:11Z (get-function-configuration)",
      "BEFORE/AFTER BRACKET: at 15:40Z (run SA-r-1-2026-10-09T15:40:57Z, trace committed @e652ac4d3e) the same routes answered 200 with refusal envelopes -- own firm NOT_FOUND / INVALID_INPUT, cottonwood FIRM_BINDING. The 15:43:11Z deploy sits inside the window between the two measurements",
      "WHY reread_27.py STILL READS CLAMPED: it hashes the deployed served.py member (87d9ecc4) and those clamp bytes ARE present. A member-hash check cannot see a runtime TypeError raised on the way to that code, so 'CLAMPED' and '500' are both true at once -- the member hash is not a liveness oracle"
    ]
  },
  "spec_asserts": "The 27 formerly-MORE_THAN_ONE routes are clamped and answer: each serves its one firm and refuses an off-list firm (reread_27.py READ27 27/27 rc 0, measured 16:18Z). Pair v2.2 step 4 grades every firm-scoped route on that answer, and FWD-1's hop (e) polls GET /analysis/requests/{requestId} to READY.",
  "world_is": "7 irpt-status routes raise before any firm logic runs and return 500 to every caller, so 6 of the 27 are ungradeable at HEAD and hop (e) cannot reach READY. The clamp itself is not implicated -- it was measured working on these same routes 39 minutes earlier; what changed is a deploy that landed a call site without the signature it calls. This is the half-landed-deploy shape, found from outside by a seat that deployed nothing.",
  "disposition": "UNDER_INVESTIGATION"
}
```

## TCKT_VNEXT-D2-S19 -- SA-r-1b run 2 ran before its ledger entry was opened (NEVER-2); the self-start clause in the issuer's AMENDMENT 3 invited it

```json
{
  "id": "TCKT_VNEXT-D2-S19",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-09T17:02:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "SA-r-1b run 2 (a live write: a users-table row and a test ticket) self-started under AMENDMENT 3's 'no new GO needed' clause and opened its NEVER-2 ledger only after the act (entry labelled RETROSPECTIVE). The issuer's own clause removed the GO checkpoint that would have put the ledger first.",
  "disarm_owner": "2.0.0_SA_COO~V2 (AMENDMENT 4 @ae01a5d96b gates run 3 on an explicit GO with the ledger opened first; CTO msg 3751)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "commit 943caa24dd: deploy-ledger(open) tckt-vnext-sa-r1b-run2-RETROSPECTIVE-20261009, after the run 2 act",
      "0.7.0_AE_CloudOps~TV2 msg 3739: 'run 2 ran with no ledger entry (retrospective one filed, labelled)'",
      "TO-RUN-SA-r-1b AMENDMENT 3 @a10101dc7a: 'Run 2 ... with NO new GO needed'",
      "CTO msg 3751: breach of NEVER-2 (ledger at start); file the row; run 3 gated on an explicit GO with its ledger opened first"
    ]
  },
  "spec_asserts": "CLAUDE.md NEVER-2: a deploy or live-write act opens its ledger entry in org/critical_paths/change_management/ at START and closes it at completion.",
  "world_is": "Run 2 wrote and removed the row and created and completed a ticket before any ledger entry existed. The retrospective entry records the act, and cleanup was verified (row absent, ticket completed). No residue, but the at-start control did not hold for one run.",
  "disposition": "UNDER_INVESTIGATION"
}
```

## TCKT_VNEXT-D2-S20 -- the pair's 'remove the row' rollback WIDENS the token rather than narrowing it; only the 2h exp actually bounds it

```json
{
  "id": "TCKT_VNEXT-D2-S20",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~TV2",
  "surfaced_at": "2026-10-09T17:44:00Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "The pair's stated rollback -- 'remove the row' -- does not narrow the token, it WIDENS it. The row is what narrows an internal caller; with the row gone, _internal_allowed_firms returns None, which the boundary reads as NO RESTRICTION, so for the remainder of its 2h life the still-valid token may select ANY registry tenant on the IRPT plane and CREATE a ticket for ANY firm. The run's own reach was NARROWER than its post-rollback reach.",
  "disarm_owner": "1.0.0_SA_CTO~DELL2 with 2.0.0_SA_COO~V2 -- the never-widen pair's rollback clause is theirs. INERT in fact for runs 1-4 because the token lived only in the executor's process memory, was never printed, stored or committed, and that process has exited; but the clause is wrong as written for any future run.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/_authz/served.py (deployed member 87d9ecc4, resolved by content from pin 74a62fb46c) _internal_allowed_firms: 'Returns None = UNCHANGED (no row, no attribute, or an empty list)'",
      "same file, Entry.handle: `listed = self._internal_allowed_firms(...)` then `if listed is not None and selected not in listed: return refuse(..., FIRM_BINDING)`. listed None therefore refuses NOTHING, and an internal caller may name any tenant bucket_for() maps",
      "infra/aws/lambda/ticket_center/lambda_function.py _profile_scope: no PROFILE row returns (None, None); _in_profile_scope returns `scope is None or str(firm) in scope`, i.e. TRUE for every firm once the row is gone; _firm_allowed is already TRUE for every firm because a tier-internal token's authorizer allowedFirmIds is ALL. So _create_firm_allowed admits ANY firm after cleanup",
      "the token is unaffected by the row's deletion: the authorizer verifies the JWT signature and claims, and v2.2's exp is iat+2h (run 4: iat 17:19:43Z, exp 19:19:43Z), so roughly 100 minutes of wider reach followed each run's cleanup",
      "pair v2.1/v2.2 blast radius, 'Rollback': 'remove the row; the 2h exp bounds the token; complete the ticket' -- the first clause is presented as the narrowing act"
    ]
  },
  "spec_asserts": "Pair v2.1 and v2.2 both state the rollback as: remove the row, the 2h exp bounds the token, complete the ticket. Removing the row is offered first and reads as the act that takes the reach away; the row LIST [49financial] is described as 'the only client reach'.",
  "world_is": "The row is the NARROWING, not the grant. Deleting it deletes the narrowing and leaves the grant (the token's tier-internal claim) standing until exp, so the post-rollback token is strictly WIDER than the token the run exercised. The only real bound is exp, which the pair also names -- so the rollback is sound ONLY because of its second clause, and the first clause works against it. A rollback that widens the subject it is rolling back should be stated as such, or the row should be left in place until exp and removed after.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S21",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-11T02:37:48Z",
  "one_line": "L9 round 1 FWD-1 seat-arm run: SA-r-1b AC2 NOT MET. Hops (e) and (g) never read a request: 61 of 61 analysis-request-read calls in 17:21:15-17:32:15Z were refused INVALID_REQUEST_ID on the live irpt-status log (60 polls plus hop (g)'s second read); the HTTP 200s were refusal envelopes. The runner polled the idempotency token it sent (sar1b-<24 hex>), and the read plane accepts REQ-<24 hex> only. Hop (f) stored that token as the ticket's report_ref, so the report cannot open from the ticket. irpt-export-render ran 0 times in the window.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.SA_RUN.md @5617aaa82d",
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R1_RUN/sa_r1b_trace.json sha256 0532f0aa...0c16 (this seat's hash)",
      "this seat's filter-log-events on /aws/lambda/irpt-status, 2026-10-09T17:21:15Z-17:32:15Z: 65 invocations, 61 irpt_error operation analysis-request-read public_reason_code INVALID_INPUT, each with RequestReadRefused INVALID_REQUEST_ID, first 17:21:39, last 17:31:59",
      "same read on /aws/lambda/irpt-ycharts-generate: 5 invocations, 1 refusal (analysis-requests MISSING_REQUEST_FIELD 17:21:23); on /aws/lambda/irpt-export-render: 0 invocations",
      "infra/aws/lambda/investor-reporting/ops/owned_requests.py:18 REQUEST_ID = REQ-[0-9a-f]{24}; :86-88 raises INVALID_REQUEST_ID (tree HEAD f7268537db, not diffed against deployed bytes)",
      "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/sa_r1/sa_r1b_run.py:559-569 (rid falls back to rid_sent)",
      "infra/aws/lambda/ticket_center/lambda_function.py:1363-1369 (report request_id: non-empty string, at most 200 characters, no shape check)",
      "this seat's query of irpt-requests: AccessDenied kms:Decrypt for cloudops-dell2-agent-user on key 7f4d3042",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_SA_R1B_L9_GRADE_20261010.md"
    ]
  },
  "spec_asserts": "SA-r-1b AC2: the one-firm proof with zero cottonwood admits, and every hop recorded with its artifact. FWD-1 ACCEPT (PRD :30-31): the report is made from that file without anyone re-typing the holdings, and the finished report opens from the ticket.",
  "world_is": "The run submitted an analysis (hop (d) not refused) and never read it: every read named an id the read plane refuses. No report generation is shown, and the ticket's report_ref names an id that cannot be opened. The packet's cause (state polled instead of stage) is not the cause; a runner that reads stage fails the same way. The census half (82 armed, 0 off-list admits) is the producer's record, not re-run by this seat.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S22",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-11T03:31:12Z",
  "one_line": "Disposition record for ARMED row TCKT_VNEXT-D2-W6-S2 (data-refresh admitted a caller with no userType): DISARMED by the CTO's round-2 analysis. Row D2-S16 measured the routed fix live (the gate admits Dev or an Opal-internal principal, so a one-firm token is refused). The residue (S17: an Opal-internal principal is admitted whatever its userType) stays with the data-refresh owner and leaves this project's list.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_2_20261011.md @bbba700c22 section 2",
      "investigation rows TCKT_VNEXT-D2-W6-S2, D2-S12, D2-S16, D2-S17",
      "1.0.0_SA_CTO~DELL2 msg 3619 (S17 routed to the data-refresh owner)"
    ]
  },
  "spec_asserts": "Only Dev or Opal-internal callers may trigger or roll back a data refresh; a one-firm test filer token does not reach those routes.",
  "world_is": "As ruled by the CTO on row D2-S16's measurement, not re-measured by this seat: a one-firm token is refused. The bound round 2 carries: no internal-tier test token is minted outside a signed pair that names data-refresh in its blast radius, with a zero-call read after.",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Disposition only; W6-S2 itself is append-only and not rewritten. Round 2's re-run pair (cell R2-tr-1) carries the bound."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S23",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-11T03:31:12Z",
  "one_line": "round-close-check --project TCKT_VNEXT --round 1 printed verdict=MAY-CLOSE with judgment=1 graded=1 while a second judgment grade of the round, SA-r-1b AC2 NOT MET (row D2-S21), was on file. The run order TO-RUN-SA-r-1b lives in the applier seat's flat task_orders folder, outside the 4 orders the check counted.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "this seat's run 2026-10-11T03:12Z: 'ROUND-CLOSE project=TCKT_VNEXT device=dell2 reviewer=present orders=4 judgment=1 graded=1 ungraded=0 self_graded=0 verdict=MAY-CLOSE'",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_SA_R1B_L9_GRADE_20261010.md @771737f0a6",
      "org/tier2_senior/0.7.0_AE_CloudOps~TV2/task_orders/TCKT_VNEXT.TO-RUN-SA-r-1b.fwd1-seat-arm-journey-v22-tv2.md (the order whose AC2 was graded)",
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_2_20261011.md @bbba700c22 section 2"
    ]
  },
  "spec_asserts": "The check counts every graded judgment criterion of the round, and does not print MAY-CLOSE while one of them is NOT MET.",
  "world_is": "It printed judgment=1 graded=1 and MAY-CLOSE with a second grade on file that reads NOT MET. Which limb missed it (the order's folder, or a NOT MET verdict counted as graded) was not isolated by this seat. The round did not close on it; the slug reported FWD-1 NOT REALIZED.",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Tool gap, owner of .tools/round-close-check.py. Filed at the CTO's ask."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W8-S1",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~8",
  "surfaced_at": "2026-10-11T03:40:00Z",
  "one_line": "R2-rn-1: the request-list history item carries no ticket id and no input_id, so the order's 'match on the ticket id or input_id' cannot be done; the runner matches on a before/after difference of REQ ids instead.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json (properties list)",
      "docs/contracts/investor-reporting/v1/OwnedAnalysisRequestHistory.schema.json",
      "infra/aws/lambda/investor-reporting/ops/owned_requests.py:229-231 _public, :313-363 history (tree HEAD of this worktree, not diffed against deployed bytes)",
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/fwd1_runner/fwd1_run.py hop_d_analysis; test_fwd1_runner.py test_falls_back_to_request_list_when_answer_has_no_id, test_ambiguous_request_list_is_a_named_failure"
    ]
  },
  "spec_asserts": "TO TCKT_VNEXT.TO-R2-rn1 rule 2: when the submission answer has no id, pick the ONE row of GET .../analysis/requests that belongs to this submission, matching on a field that ties it to this run (the journey ticket id or the uploaded input_id, whichever the schema carries).",
  "world_is": "OwnedAnalysisRequestHistory.schema.json items are OwnedAnalysisRequest, whose only properties are identity{tenant_firm_id, request_id, revision, immutable, ingestion_gate_revision, destination_policy_revision}, accepted_at, and (single read only) comparisons, composition, persist_inputs; the history omits composition (_public returns {identity, accepted_at}). Neither ticket_id nor input_id is on a history item. fwd1_run.py hop_d_analysis therefore reads the list just BEFORE the submission and just after it and takes the ONE REQ id present only in the second (0 or >1 is REQUEST_ID_UNRESOLVED). This ties by novelty, not by an identifier of this run: a concurrent submission by the same firm in the window makes it ambiguous (a named failure, never a wrong id).",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W8-S2",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~8",
  "surfaced_at": "2026-10-11T03:40:00Z",
  "one_line": "R2-rn-1: the single-request read the runner polls (analysis-request-read) is OwnedAnalysisRequest, which has no `stage` property, so hop (e) as ordered cannot observe a stage on the served read; the runner names STAGE_ABSENT after one poll.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "docs/contracts/investor-reporting/v1/responses/analysis-request-read.response.schema.json (grep -c \"stage\" = 0)",
      "docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json (grep -c \"stage\" = 0)",
      "docs/contracts/investor-reporting/v1/AnalysisRequest.schema.json properties.stage enum",
      "infra/aws/lambda/investor-reporting/ops/owned_requests.py:233-255 read, :229-231 _public",
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/fwd1_runner/test_fwd1_runner.py test_missing_stage_is_a_named_failure_not_a_pass"
    ]
  },
  "spec_asserts": "TO TCKT_VNEXT.TO-R2-rn1 rule 3: poll GET .../analysis/requests/<REQ id> and read the contract field `stage` (AnalysisRequest.schema.json: RECEIVED, PARSED, NEEDS_CORRECTION, READY, SUBMITTING, GENERATED, RELEASED, FAILED); poll while in flight, GENERATED or RELEASED ends the hop OK.",
  "world_is": "responses/analysis-request-read.response.schema.json refs OwnedAnalysisRequest.schema.json (data), and neither file contains the string \"stage\" (grep -c = 0 on both); owned_requests.py read() returns {identity, accepted_at} plus optional comparisons/composition only. `stage` lives on AnalysisRequest.schema.json, which the owned read route does not serve. So a live poll can read no stage; a 200 with no stage is recorded by fwd1_run.py as the named failure STAGE_ABSENT after ONE poll (not polled 40 times, not read as a pass). The runner's tests pass against canned bodies that carry `stage`; whether the deployed irpt-status adds `stage` to the read is NOT measured here (no AWS or network call was made).",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S24",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-11T03:51:15Z",
  "one_line": "The portal's ticket link does not open a report. openReport reads analysis-request-read for the ticket's report_ref.request_id, and that route answers {identity, accepted_at} as soon as the request is ACCEPTED with a retained composition. None of its refusal codes means not-yet-generated, so a 200 there does not show that a report was made.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/pages/TicketCenter/analysisRequest.ts:178-183 openReport -> deps.ir.getOwnedAnalysisRequest(requestId, ticket.answers?.firm)",
      "portal/src/api/endpoints/investor-reporting.ts:214 analysis-request-read = GET {IR_ROUTE_BASE}/analysis/requests/{requestId}; :1068 getOwnedAnalysisRequest",
      "infra/aws/lambda/investor-reporting/ops/owned_requests.py:230-241 read() returns _public(record) = identity + accepted_at; :163-190 _validate, :192-196 _materialize, :215-227 _final",
      "the same file's RequestReadRefused codes (26 raise sites read by this seat): identity, composition, authorization, retention and history bindings; no code names report generation",
      "docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json: required identity, accepted_at; no stage",
      "1.0.0_SA_CTO~DELL2 msg 4015 (hop (e) oracle = the route the ticket's own link opens)",
      "tree read at box/dell2 HEAD; not the deployed bytes"
    ]
  },
  "spec_asserts": "FWD-1 ACCEPT (PRD :30-31): the report is made from the filed file, and the finished report opens from the ticket.",
  "world_is": "From the ticket the page opens the accepted request record. Whether a report was generated is answered by other routes (analysis-request-pdf, the analysis-report read) that the ticket link does not call. A journey run graded on the ticket link alone would pass with no report made.",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Read from the tree, not exercised. Bears on cell R2-tr-1's oracle and on whether round 2 needs a page cell; with the CTO."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W11-S1",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~11",
  "surfaced_at": "2026-10-11T04:06:53Z",
  "one_line": "The analysis-report read has no typed 'not generated yet' result; the ticket's waiting state is mapped from IrRequestError (reason code NOT_READY or NOT_FOUND, or transport 404), which the tree does not prove the deployed sections route emits for an ungenerated report.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory.tsx:59-64 readOwnedSections -> api.getOwnedAnalysisReport (called at :334); on ANY throw the page sets reportError and says 'Report sections are not available' -- it does not distinguish not-ready",
      "portal/src/api/endpoints/investor-reporting.ts:1091-1098 getOwnedAnalysisReport; :970-1041 send() raises IrRequestError(publicReasonCode) for a refused envelope or IrRequestError(httpStatus) for a transport failure; no dedicated not-ready class",
      "portal/src/pages/InvestorReporting/render/Page.tsx:108 CONTRACT_NAMED_REASON_CODES names NOT_READY and NOT_FOUND",
      "portal/src/pages/TicketCenter/analysisRequest.ts isReportNotReady (this worker's commit e4b9f8966c on wk-TCKT_VNEXT-11-portal); tests use IrRequestError built with those codes; tree read and unit-tested, not exercised against the deployed route (LOCAL: no AWS or live API call)"
    ]
  },
  "spec_asserts": "Cell R2-pg-1 item 2: a report not yet generated is a stated waiting state, read from how the chosen read reports 'no report yet'.",
  "world_is": "The chosen read reports it only as a generic IrRequestError. The worker treated public reason code NOT_READY / NOT_FOUND or http 404 as the waiting state and every other failure as an error. If the deployed analysis/{jobId}/sections route answers an ungenerated report with another code or status (for example 409), the ticket shows an error banner instead of the waiting message. Also: OpenedReport in AnalysisRequestParts.tsx (outside this order's paths) is now unused; the panel is OpenedReportPanel in TicketCenter.tsx.",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Also: bunx is absent on this box; tsc was run as 'bun x tsc -b'."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S25",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~TV2",
  "surfaced_at": "2026-10-11T04:27:59Z",
  "one_line": "opal-ticket-api's lambda-source-map entry is internally inconsistent and stale: its artifact_sha256 is the 2026-10-09 SA1 build while its last_deployed_commit and last_deployed_at still name the 2026-10-07 deploy, so the one field a reader would reach for as a rollback hash names neither the build that was live before this apply nor the commit beside it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ci/lambda-source-map.json at box/dell2 HEAD, functions['opal-ticket-api']: artifact_sha256 ywAvsfx/j3RTZOoOvN+znGsRhslUT+92XNgHhcglNQA=, last_deployed_commit da431554186bd74759f3d85bc4423f42a6c4a8f9, last_deployed_at 2026-10-07T19:37:43Z, recorded_by record-terraform-deploy.sh (235 functions in the map as the printed denominator)",
      "the same three values read identically in the uncommitted working copy, so this is not an artifact of the 4 uncommitted lines in that file -- those move the artifact_sha256 of two OTHER functions and contain 0 ticket lines",
      "ywAvsfx... is the SA1 build, named as that deploy's uploaded content-sha256 in org/critical_paths/change_management/20261009T0450Z_tckt-vnext-sa1-clamp-20261009_deploy_completion.md leg S1, dated 2026-10-09T045422Z -- two days after the last_deployed_at beside it",
      "aws lambda get-function-configuration --function-name opal-ticket-api read CodeSha256 HK82TEd0SQWeGqWEEG7HV10QK8agPizblDoXkvITRJA= with LastModified 2026-10-09T11:43:28Z at this order's BEFORE read, and the artifact bucket holds that build as object version TNDfJSNhCarmtqRmFU.jsPUaiO7BLSsK uploaded 2026-10-09T11:40:43Z -- a deploy the map records in no field",
      "live CodeSha256 after this order's own apply is W03VREoMEmxNaRoADDDWrXE3IycD9c5vodB+rHBAtg0= (object version RI4EX8i.EL18LgmpA54Fixk.hmjLsH4h), which the map also does not carry; this seat cannot write it, because infra/aws/lambda/ci/ is outside the <paths> of TCKT_VNEXT.TO-APPLY-R2-rr2 and owned-paths refuses it"
    ]
  },
  "spec_asserts": "The deployment rules' Rule 4 (canonical home /cloud-ops): every Lambda has an entry in infra/aws/lambda/ci/lambda-source-map.json, and this entry declares itself recorded_by record-terraform-deploy.sh -- a writer that runs per deploy and whose fields are therefore read as naming the last deploy.",
  "world_is": "For opal-ticket-api the writer's fields have drifted apart and then stopped. artifact_sha256 advanced to the SA1 build on 2026-10-09 while last_deployed_commit and last_deployed_at did not, so within ONE entry the hash and the commit beside it describe different deploys; and neither records the 2026-10-09T11:40Z build that was actually live when this order began, nor this order's own. Rule 4 already states the map does not compare deployed bytes to built-from bytes and that code currency is the assignee's read, which is why this is INERT and why this order measured the live package by content instead. The sharper point is narrower than staleness: a reader doing a rollback could take artifact_sha256 as the previous build's hash. Here that would have been wrong -- the real prior build was HK82TEd0..., and ywAvsfx... is a build two deploys back. The correct rollback source for this apply was established from S3 object versioning and git, not from this file.",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Off-task for TO-APPLY-R2-rr2 and filed as one row rather than halting, per CLAUDE.md section 2. No act is proposed here and nothing in this order depended on the map: pipeline, tf_resource and artifact key were read from it and are correct; only the deploy-recording fields are at issue. Owner for the carrier itself is unnamed in this row because record-terraform-deploy.sh is shared infrastructure and /cloud-ops already records it as having known writer failures (the CHANGELOG.json writer plus the owned-paths hook on the Andrew identity); whether that is the cause here was NOT measured."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W11-S2",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~11",
  "surfaced_at": "2026-10-11T04:25:50Z",
  "one_line": "Follow-up to TCKT_VNEXT-D2-W11-S1: the code a not-generated report answers is NOT_FOUND, raised at owned_report.py:119 as AnalysisUnavailable for a job that is not READY.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ops/owned_report.py:119 (read at this worktree's HEAD): `raise AnalysisUnavailable(\"ANALYSIS_REPORT_NOT_READY\")`, guarded at :118 by `if state[\"state\"] != \"READY\":`",
      "infra/aws/lambda/investor-reporting/ops/entry.py:254 maps \"AnalysisUnavailable\" to \"NOT_FOUND\" (read at this worktree's HEAD)",
      "portal/src/pages/TicketCenter/analysisRequest.ts isReportNotReady already treats publicReasonCode NOT_FOUND (and NOT_READY, and http 404) as the waiting state, so the shipped mapping covers this code; tree read only, not exercised against the deployed route (LOCAL)."
    ]
  },
  "spec_asserts": "TCKT_VNEXT-D2-W11-S1 asked which code the analysis-report read answers for a report not yet generated.",
  "world_is": "Per the CTO's read and the worker's re-read of owned_report.py:119 and entry.py:254, a job that is not READY raises AnalysisUnavailable, which the boundary answers NOT_FOUND. S1's code question is answered by this line. S1 is not edited (rows are append-only).",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Appended in binary mode with CRLF line endings, after S1."
}
```

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~8",
  "surfaced_at": "2026-10-11T04:30:40Z",
  "id": "TCKT_VNEXT-D2-W8-S3",
  "one_line": "R2-rn-1 AMENDMENT 1 A3: the Write tool refused fwd1_runner/REPORT_READ_REFUSALS.md ('subagents should return findings as text, not write report files'), so the refusal table is not a file; it is in the worker report.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "TO TCKT_VNEXT.TO-R2-rn1 AMENDMENT 1 A3 orders the file at org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/fwd1_runner/REPORT_READ_REFUSALS.md, inside the worker's <paths>",
      "the Write tool call for that path returned a tool error, the file does not exist in the worktree; this seat did not route around the refusal by another writer",
      "NOT_READY_CODES in fwd1_run.py carries the classification as a comment and the final worker report carries the full table (32 rows)"
    ]
  },
  "spec_asserts": "A3: write fwd1_runner/REPORT_READ_REFUSALS.md, one row per refusal the finished-report read can raise, with the denominator, marked PROPOSED.",
  "world_is": "The deliverable file is absent. The table exists only as text in the final worker report. 32 rows: 31 per-request raise sites read in ops/entry.py (1), ops/owned_report.py (11 + 1 re-raise), ops/owned_requests.py (11), _scope/owner_reads.py (3), ycharts/generate/durable_job.py (2), _authz/served.py _owner_read_request (3). Not read: the raise sites inside reports/repository.py and reports/retention.py reached through artifacts.head, retention.require_live, reports.index.get and reports.get (reach the caller by class only).",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~8",
  "surfaced_at": "2026-10-11T04:30:40Z",
  "id": "TCKT_VNEXT-D2-W8-S4",
  "one_line": "R2-rn-1 A2/A3: on the finished-report read the public code NOT_FOUND cannot tell a report not yet generated from one that failed, expired or never will be; polling it to the bound records NOT_READY for all of them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ops/owned_report.py:118-119 raises AnalysisUnavailable('ANALYSIS_REPORT_NOT_READY') for ANY state other than READY (CTO lead msg 4041 confirmed by reading)",
      "infra/aws/lambda/investor-reporting/ops/entry.py:254-255 maps AnalysisUnavailable, RetentionExpired and LeaseRefused each to NOT_FOUND; _authz/errors.py:136 maps KeyError to NOT_FOUND",
      "infra/aws/lambda/investor-reporting/ycharts/generate/durable_job.py:16 STATES lists the non-READY states; read from the tree, not exercised and not the deployed bytes",
      "no-such-request is told apart: ops/entry.py:226-228 and _scope/owner_reads.py:28-33 stop an absent or foreign record before the report read, answered NOT_AUTHORIZED at _authz/served.py:985"
    ]
  },
  "spec_asserts": "A2: NOT_READY_CODES names the refusal codes that mean 'not generated yet'; the bound reached is the named result NOT_READY.",
  "world_is": "NOT_FOUND is in NOT_READY_CODES because it is the only code the not-READY branch can answer. A generation that FAILED answers the same code and is polled 40 times 30 s apart (20 minutes) before NOT_READY is recorded. The status-job operation on the same entry is the read that carries a job's state; the order does not call it.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~8",
  "surfaced_at": "2026-10-11T04:30:40Z",
  "id": "TCKT_VNEXT-D2-W8-S5",
  "one_line": "R2-rn-1: round 1 observed an INVALID_REQUEST_ID reason in a refusal envelope, but the HEAD boundary can only emit members of a closed public set and answers a malformed id as INVALID_INPUT, so the tree and the observation disagree on the code vocabulary NOT_READY_CODES depends on.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ops/owned_requests.py:88 raises RequestReadRefused('INVALID_REQUEST_ID'), the internal string",
      "infra/aws/lambda/investor-reporting/_authz/served.py:874-887 public_reason_for returns a code only if it is in BOUNDARY_REASONS (errors.PUBLIC_REASONS plus CONTRACT_VERSION, UNPROJECTED_GRANT, SELECTION_UNSUPPORTED), else UNEXPECTED; INVALID_REQUEST_ID is in neither (grep of served.py and errors.py finds it in neither file)",
      "TO TCKT_VNEXT.TO-R2-rn1 WHY and rule 4 cite INVALID_REQUEST_ID as the round-1 refusal reason; the runner's existing refusal test uses that string",
      "tree at box/dell2 HEAD only; the deployed bytes and any layer in front of the lambda were not read (no AWS or network call)"
    ]
  },
  "spec_asserts": "A3: NOT_READY_CODES is set from the handler's refusal codes as the tree has them.",
  "world_is": "Either the deployed lambda differs from HEAD, or a layer in front of it produced INVALID_REQUEST_ID, or the order's citation paraphrases. If the deployed boundary exposes internal strings, the not-ready answer would read ANALYSIS_REPORT_NOT_READY, which is not in NOT_READY_CODES, and hop (e) would end terminal on the first poll. NOT_READY_CODES is PROPOSED from the tree; the issuer's run pair is what settles it.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S26",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-11T04:50:50Z",
  "one_line": "L9 round 2 R2-rr-2: TO-APPLY-R2-rr2 AC2 MET. The live opal-ticket-api package, downloaded by this seat, hashes to the live CodeSha256 and holds one member byte-equal to lambda_function.py at pin a366ce52ec (negative control: the pin's parent does not match). The code delta from the previously deployed file (eb80f55340, 67068626) is 4 added lines, the report request-id shape check. Runtime, handler, memory and timeout equal the Terraform file; 8 environment keys. The check's two live arms are not exercised (cell R2-tr-1).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R2_RR2.md @16fcc87ae6 (msg 4098)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_R2_RR2_L9_GRADE_20261011.md",
      "this seat's download of the live package (get-function Code.Location): zip base64 sha256 W03VREoM..., 1 member, sha256 ca3be343..., equal to git show a366ce52ec:infra/aws/lambda/ticket_center/lambda_function.py",
      "git diff eb80f55340 a366ce52ec on the handler: 4 insertions, 0 deletions; git show eb80f55340:<file> sha256 67068626...",
      "get-function-configuration opal-ticket-api: python3.11, lambda_function.lambda_handler, 256 MB, 30 s, 8 env keys, LastModified 2026-10-11T04:19:14Z; infra/aws/terraform/ticket-center :243-246",
      "org/critical_paths/change_management/20261011T0403Z_tckt-vnext-r2-rr2-report-id-shape-20261011_deploy_completion.md (CLOSED)"
    ]
  },
  "spec_asserts": "TO-APPLY-R2-rr2 AC2 (judgment): the deployed bytes are the pinned file, and nothing else moved.",
  "world_is": "Holds on this seat's content comparison. The shape check is APPLIED and not exercised live; FWD-1 still needs a run that reads a server-minted request id.",
  "disposition": "UNDER_INVESTIGATION"
}
```
