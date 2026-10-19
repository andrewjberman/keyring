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

```json
{
  "id": "TCKT_VNEXT-D2-W11-S3",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~11",
  "surfaced_at": "2026-10-11T04:51:54Z",
  "one_line": "On origin/DEV 26f621d51c the report PACKAGE's 'Open Report' button (AnalysisRequestParts.tsx PackageFiles/openPackageFile) reads getOwnedAnalysisRequest and shows the request projection as 'Report for <ticket>' with the request id in visible words; the ticket's own 'Open report' (this cell) reads the finished report. Both are called the report; the order said keep DEV's opener untouched, so it is kept.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal origin/DEV 26f621d51c src/pages/TicketCenter/AnalysisRequestParts.tsx: openPackageFile kind 'report' calls ir.getOwnedAnalysisRequest(requestId, firm) and hands the result to showReport; PackageFiles renders it with the local OpenedReport (rows Request, Revision, Firm, request id in a visible dd)",
      "origin/DEV __tests__/package-open.test.tsx pins the 'owned' reader call for the package Report file (calls toEqual [['owned', ['REQ-13','fir_test']], ...]) and package-r2.test.tsx uses openPackageFile; those tests pass unchanged on the merge 7bb81fa8 (pg-suite 31 pass 0 fail)",
      "tree read and bun tests only; no live call (LOCAL)"
    ]
  },
  "spec_asserts": "TO-R2-pg1 AMENDMENT 2 C3/C4: one 'Open report' behaviour (this cell's), DEV's package file openers untouched beside it, and DEV's use of OpenedReport kept; rule 4: the request record is never presented as the report.",
  "world_is": "After the merge two surfaces on one ticket carry the word report: (a) the ticket row's 'Open report' button, which opens the finished report through getOwnedAnalysisReport and RetainedSections, and (b) DEV's package block 'Open Report' button, which still opens the request projection through the local OpenedReport, with the request id in visible words (the UIC-23 rule B2 states). The worker kept (b) exactly as DEV has it, per C3 and C4, and did not judge it a stop condition because the order names this case; the issuer decides whether the package Report opener should read getOwnedAnalysisReport as well (a change to DEV's file and to package-open.test.tsx, outside this order's grant to alter).",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Appended in binary mode with CRLF line endings after S2. INERT: no new behaviour; it is DEV's pre-existing opener."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W8-S6",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~8",
  "surfaced_at": "2026-10-11T05:16:32Z",
  "one_line": "R2-rn-1 AMENDMENT 2: the runner still writes its trace to round 1's two files (TRACE = 2.0.0_SA_COO~V2/R1_RUN/sa_r1b_trace.json and MY_TRACE = 0.7.0_AE_CloudOps~TV2/deliverables/sa_r1/sa_r1b_trace.json) and no D-item or argument names a trace path, so a round-2 run appends its record into round 1's trace files.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~V2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "fwd1_runner/fwd1_run.py constants TRACE and MY_TRACE (module top) are unchanged from the copy of sa_r1b_run.py:133-134",
      "save() slots a run whose run_id differs from the file's into the next free run_N key, so it appends and does not overwrite; the round-1 record stays but the file now holds a round-2 section",
      "D7 replaces the header fields only; D1-D8 and the argument list name no trace path; tree read and fake-layer tests only, nothing was run against AWS"
    ]
  },
  "spec_asserts": "AMENDMENT 2 D7: the trace header names this run (run label, pair, executor); the order expects a round-2 run's trace to be distinguishable from round 1's.",
  "world_is": "The header now names the run, but the file it lands in is still round 1's R1_RUN trace plus a copy under the TV2 deliverables folder (outside any round-2 grant). Not widened by the worker: no trace-path argument was added because the order's argument list does not name one. The issuer decides before the run pair executes: add a --trace-dir style argument in a further amendment, or accept the append into run_N and read the trace by run_label.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W8-S7",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~8",
  "surfaced_at": "2026-10-11T05:16:32Z",
  "one_line": "R2-rn-1 AMENDMENT 2 D4: the zero-call read counts streams from filter_log_events' `searchedLogStreams`, which AWS documents as deprecated (to my recollection, returned empty since May 2023), and its positive control assumes opal-ticket-api logs the filer's email; either makes the read VOID live where the fake layer proves it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "D4 text: the read is VOID when the count of log streams searched is 0; the existing code counts len(r.get('searchedLogStreams', [])) per page (fwd1_run.py _scan_group)",
      "the deprecation of searchedLogStreams is recalled from the CloudWatch Logs API reference, not read in this session (no network call allowed)",
      "whether opal-ticket-api writes the filer's email into its log lines was not read; the pattern is the filer email in double quotes, the same filter as the data-refresh read"
    ]
  },
  "spec_asserts": "D4: ZERO_CALLS_PROVEN is reachable when streams searched > 0 and the control over /aws/lambda/opal-ticket-api finds the filer at least once.",
  "world_is": "If the live field is empty, streams searched is always 0 and the result is always ZERO_CALL_VOID, which fails SAFE (never a false zero) but means the proof cannot be produced; the fake tests cannot tell. The same holds if the ticket API does not log the email. INERT because the failure direction is VOID. For the issuer's run pair: read the control block and searched_log_streams in the trace; a VOID with control found 0 or streams 0 is this row, not a data-refresh call.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W8-S8",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~8",
  "surfaced_at": "2026-10-11T05:32:28Z",
  "one_line": "R2-rn-1 AMENDMENT 3 E1: the order says --trace-out is created if absent and holds one run, but not what happens when the path already holds a trace; I made main() refuse (rc 2, nothing done) a path that exists and is non-empty.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "fwd1_run.py main(): the trace-out guard at the top of main(); test_trace_out_is_required_and_is_the_only_file_written asserts the refusal leaves the file's bytes unchanged and makes no AWS or HTTP call"
    ]
  },
  "spec_asserts": "E1: the runner writes its trace to THAT file only, creating it if absent, as one JSON object for this run, with no run_N appending into an older file.",
  "world_is": "The order is silent on an existing file. Overwriting would destroy an older run's record and appending is forbidden, so the runner refuses before any write. INERT: a reused path stops the run before the row is written; the issuer picks a fresh path per run. If the issuer wants overwrite-in-place instead, it is a one-line change in main().",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W8-S9",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~8",
  "surfaced_at": "2026-10-11T05:32:28Z",
  "one_line": "R2-rn-1 AMENDMENT 3 E2: the new denominator calls logs:DescribeLogStreams on two log groups; whether the run's AWS identity may call it was not read (no AWS call allowed), and a denied call makes the zero-call verdict UNREAD, not PROVEN.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "fwd1_run.py _streams_active_in_window calls logs.describe_log_streams(orderBy=LastEventTime, descending=True) on /aws/lambda/opal-data-refresh-api and /aws/lambda/opal-ticket-api, every page",
      "the earlier read already needed logs:FilterLogEvents; whether the same identity holds logs:DescribeLogStreams was not read"
    ]
  },
  "spec_asserts": "E2: the denominator is the count of log streams whose last event time is at or after iat, from describe_log_streams, every page read.",
  "world_is": "If the identity lacks logs:DescribeLogStreams the call raises, data_refresh_zero_calls records verdict UNREAD (never a zero) and the issuer's run pair sees UNREAD in the trace. The fake tests cannot show the live permission. INERT because the failure direction is UNREAD.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S27",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-11T05:42:31Z",
  "one_line": "On the deployed opal-ticket-api configuration a new ticket notifies no one: TICKET_DL_MAP parses to an object with 0 keys, so there is no row for any firm and no default, and every create takes the unconfigured branch.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "this seat's get-function-configuration on opal-ticket-api, 2026-10-11 ~05:4xZ: Environment.Variables.TICKET_DL_MAP parsed as JSON has 0 keys ('49financial' ABSENT, '*' ABSENT); no address was printed because none exists",
      "infra/aws/lambda/ticket_center/lambda_function.py:819-829 (the distribution-list send and its resolver; tree read at box/dell2 HEAD, the build deployed by TO-APPLY-R2-rr2)",
      "1.0.0_SA_CTO~DELL2 msg 4201 (the CTO's read: every create logs WE_DL_UNCONFIGURED; carried to Andrew by the CTO)"
    ]
  },
  "spec_asserts": "Staff learn of a filed ticket by the distribution-list notice.",
  "world_is": "No list is configured, so no notice is sent on a create. Not exercised by this seat: the WE_DL_* line a live create logs is recorded by the R2-tr-1 run.",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed at the CTO's ask. Who is on the list is Andrew's to say; the CTO carries it. Not a gate on R2-tr-1."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S28",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~TV2",
  "surfaced_at": "2026-10-11T06:02:00Z",
  "one_line": "R2-tr-1's AC1 instrument, reread_27.py, decides opal-ticket-api by membership in a HAND-MAINTAINED set of two deployed-member hashes, so the signed R2-rr-2 deploy -- a third hash -- makes it print NOT-RELEASED and drop that host's 6 routes: READ27 reads 21/27 and the run STOPS at branch D, while the clamp it is meant to detect is provably still there.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R1_RUN/reread_27.py:35-38 TICKET_OK = {04f5727beb... '# V12 (contains SA-k-1)', 670686262068808f... '# R13 (V12 + AR-v-21 + OW-l-1)'}; :57 ok = (h in TICKET_OK) if fn == 'opal-ticket-api'; :62 prints 'CLAMPED' if ok else 'NOT-RELEASED'; :66 exit 0 only when done == total",
      "the live deployed member is ca3be34307f70079e48c4a26d1f711e47318285f2cf2722fdf0cfdcbd637eade -- the R2-rr-2 build, landed by this seat 2026-10-11T04:19:14Z under both signed halves (ledger 20261011T0403Z_tckt-vnext-r2-rr2-report-id-shape-20261011, closed @5660c698f1) -- and it is NOT a member of that two-element set",
      "the run's own output, printed before any write: 7 hosts read CLAMPED, opal-ticket-api reads 'opal-ticket-api 6 2026-10-11T04:19:14 ca3be343 NOT-RELEASED', and the total is 'READ27 21/27'. 27 minus that host's 6 routes is exactly 21, so the whole shortfall is this one host",
      "THE CLAMP IS INTACT, measured not argued: git diff --numstat between the R13 pin 5a36586b5f and the deployed build's pin a366ce52ec on infra/aws/lambda/ticket_center/lambda_function.py reads 4 added / 0 REMOVED, so every byte of R13 -- and of the SA-k-1 clamp inside it -- is still in the deployed file. Control on that zero: the same instrument reports non-zero removals for this exact file in 18 of its last 40 history rows",
      "the whole behavioural delta is the 4 inserted lines: one compiled REPORT_REQUEST_ID pattern and a three-line fullmatch refusal returning 400 INVALID_REPORT_REQUEST_ID",
      "the live package pulled from the function's own Code.Location hashes its member to ca3be343... and still carries allowedFirmIds 12 times, plus INVALID_REPORT_REQUEST_ID once"
    ]
  },
  "spec_asserts": "TCKT_VNEXT.TO-RUN-R2-tr1 @ec3d0fd6c1 proof_of_spec AC1: reread_27.py expect READ27 27/27; and the pair's step 1 and the GO's step 2 both make that read a precheck whose failure is a STOP before the identity row is written. The script's own docstring describes the opal-ticket-api limb as checking the live file 'against the V12 pin's bytes ... or, after R13, against R13's', which states the allow-list is extended by hand per signed build.",
  "world_is": "The instrument is an ALLOW-LIST over deployed bytes, so it reads NOT-RELEASED for any build it has not been told about -- including a build landed correctly under a signed never-widen pair by the immediately preceding cell of the same round. R2-rr-2 (the report-id shape check) and R2-tr-1 (the thread re-run that exercises it) were cut into the same round, and the first one's success is what makes the second one's AC1 fail. The failure mode is the one that matters here: the script cannot distinguish 'the clamp was removed' from 'the file changed for an unrelated, signed reason', and both render as the same NOT-RELEASED line and the same non-zero exit. Read as a clamp regression it would be alarming; it is not one. Nothing about the live clamp changed, and nothing in the world is unsafe, which is why this row is INERT -- it is BLOCKING only in the sense that AC1 cannot be met as written and so the FWD-1 thread re-run did not run.",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "This seat did NOT edit the script to clear its own criterion. reread_27.py sits under deliverables/2.0.0_SA_COO~V2/R1_RUN/, outside this order's <paths>, and widening an acceptance instrument so that it admits the build under test would be the wrong act whoever owned the file. The call belongs to 2.0.0_SA_COO~V2 and 1.0.0_SA_CTO~DELL2: either TICKET_OK gains the R2-rr-2 hash ca3be343... as a signed release build input, or AC1 is restated against something that is not a hand-maintained hash set. Branch D was taken as the pair defines it -- nothing of the journey ran, no row written, no token minted, no mail path entered, nothing retained under any tenant -- and the ledger closed with 4 of 4 legs dispositioned. A second run needs a new GO. Related: [[TCKT_VNEXT-D2-S25]] is the same shape one layer down -- a per-deploy record that a signed build silently ages out of."
}
```

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~TV2",
  "surfaced_at": "2026-10-11T07:12:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "TCKT_VNEXT-D2-S29",
  "one_line": "The pair's zero-call step cannot be satisfied as written: its POSITIVE CONTROL looks for the filer's address in /aws/lambda/opal-ticket-api and finds 0 matches even though the filer created two tickets through that function in the window, so the runner correctly returned ZERO_CALL_VOID (CONTROL_FOUND_NO_FILER) and no zero-call claim is available.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "trace data_refresh_zero_calls: target /aws/lambda/opal-data-refresh-api over 2026-10-11T06:20:46Z..07:05:46Z -> streams_in_group 442, streams_active_in_window 0, matches 0; control /aws/lambda/opal-ticket-api -> streams_in_group 167, streams_active_in_window 1, matches 0, found 0; verdict ZERO_CALL_VOID, void_reason CONTROL_FOUND_NO_FILER",
      "the filter is filterPattern=\"tckt-fwd1-testfiler-20261009@opal.invalid\" over all pages, with active defined as last event >= iat (the trace records the query verbatim)",
      "the filer DID exercise opal-ticket-api in that window: hop (b) created TCK-20261011-b13495db at http 201, the census create arm created TCK-20261011-19bf345c at http 201, and both were completed at http 200 through that same function",
      "R2_TR1_THREAD_RERUN_PAIR.md @9e9e6e62f3 section 3 step 9: 'Only streams > 0, control >= 1 and matches == 0 is ZERO-CALLS-PROVEN'",
      "my own WE_ filter over the SAME log group and the SAME window returned 3 events naming this run's ticket ids, so the group is readable and does hold this run's traffic -- what it does not hold is the filer's address in a form the control's filter matches"
    ]
  },
  "spec_asserts": "The pair's step 9 treats a 0 in the data-refresh group as meaningful ONLY when the same filter finds the filer in the ticket-api group, precisely so that an instrument blind to the filer cannot be read as proof of no calls.",
  "world_is": "The control is blind here, so the guard fired as designed and the claim is withheld. The cause is not the window and not pagination: the group was read, the window did hold this run's traffic, and a different filter over the same group and window returned events. The deployed ticket handler evidently does not write the filer's email address into its log lines in a form this filter matches -- the WE_ lines it does write carry the ticket id, the firm, a message_id and a from= sender, and no requester address. So the control's premise, that the filer's address appears in ticket-api logs whenever the filer acts, does not hold against the current handler. Until the control keys on something the handler actually logs, step 9 is unsatisfiable on every run, not just this one, and ABSENT in the target group stays uninformative.",
  "notes": "No act proposed and nothing widened: the pair forbids probing the data-refresh routes and I did not. This is the ABSENT != EXERCISED-AGAINST distinction with a working guard, so it is INERT -- the run reported VOID rather than a false negative. The remedy is the issuer's and the CTO's: key the control on a token the handler logs (the ticket id is present in all three WE_ lines), or name a different control surface. Related: [[TCKT_VNEXT-D2-S30]] is the same handler's logging gap seen from the mail side."
}
```

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~TV2",
  "surfaced_at": "2026-10-11T07:12:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "TCKT_VNEXT-D2-S30",
  "one_line": "CTO condition 3 is written against a log line that carries no recipient: WE_CLIENT_SENT logs kind, ticket, firm, message_id and the SENDER's from= address only, so a send to the filer and a send to anyone else are indistinguishable from it -- and the CREATE ack leg logged no WE_CLIENT_* line at all, where AMENDMENT 2 anticipated two.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "the one line, local-part masked by me: 'WE_CLIENT_SENT kind=pickup ticket=TCK-20261011-b13495db firm=49financial message_id=010001a129a094e8-... from=<local>@opalinvest.dev' -- the only address present is from=, the sender, on Opal's own domain; there is no to= or recipient= field",
      "filter WE_ over /aws/lambda/opal-ticket-api across iat..exp returned exactly 3 events: WE_DL_UNCONFIGURED x2 (one per created ticket) and WE_CLIENT_SENT x1 (kind=pickup). WE_DL_SENT count is 0",
      "NEVER_WIDEN_R2_TR1_THREAD_RERUN_CTO_HALF.md condition 3: 'A WE_CLIENT_* line naming the filer's .invalid address, sent or failed, is expected. A WE_CLIENT_SENT to any other address is a STOP before hop (d)'; AMENDMENT 2 moves the read after the run and makes a wrong one a BLOCKING row",
      "AMENDMENT 2 also states 'Two such bounces per run are accepted here', i.e. the CREATE ack leg and the CLAIM pickup leg; only the pickup leg logged a line",
      "the intended recipient, established from the data the code path uses rather than from the log: the journey ticket's requester.email domain is opal.invalid (the filer's own), requester.firm is 49financial, created_by is the filer; the CTO half's own code read places notify_client_isolated's single recipient at the requester (lines 1004-1035)"
    ]
  },
  "spec_asserts": "CTO condition 3 makes a WE_CLIENT_SENT to an address other than the filer's .invalid address a STOP, and AMENDMENT 2 makes it a BLOCKING row read after the run -- a test that presumes the line names the recipient.",
  "world_is": "The line does not name the recipient, so condition 3 is UNVERIFIABLE FROM ITS OWN INSTRUMENT. I reported it neither violated nor confirmed: no BLOCKING row was filed, because nothing evidences a foreign recipient, and no clean bill was given, because nothing evidences the filer either. The domain that IS on the line, opalinvest.dev, is Opal's own and is the sender -- read carelessly as a recipient it would look exactly like the violation the condition is hunting, which is the sharp edge here. The recipient was instead inferred from the ticket's requester.email domain plus the CTO's own code read, which is code-plus-data and not a measured delivery; by the fabric's own delivery rule, SENT is not READ and an agent-side ack is the only sound oracle, and there is none for mail. Separately, the ack leg firing no line at all means a silent no-op and a successful send are also indistinguishable on this surface.",
  "notes": "Vacuous-versus-measured matters here and is stated per limb: AMENDMENT 1's empty-map limb is satisfied BY MEASUREMENT (map read empty before the write, then WE_DL_UNCONFIGURED x2 and WE_DL_SENT 0 live, exactly as predicted from the tree), while condition 3's recipient limb is not measurable from this line at all. Remedy is the owner's: log the recipient (or its domain) on the WE_CLIENT_* lines, or restate condition 3 against the ticket's requester field, which IS readable. Related: [[TCKT_VNEXT-D2-S29]]."
}
```

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~TV2",
  "surfaced_at": "2026-10-11T07:12:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "id": "TCKT_VNEXT-D2-S31",
  "one_line": "The pair's four signed branches are not MECE over what the run can do: this run's outcome -- hop (d) refused, so hops (e), (f), (g) UNREACHABLE and both report-route arms unrun -- is named by none of A, B, C or D, because C is written as hop (e) ending NOT-READY or on a terminal refusal and hop (e) never started.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "trace named_failures: [{hop d_analysis, status 200, reason INVALID_INPUT, note 'submission refused (any HTTP status); (e)-(g) depend on it'}, then e_ready, f_report and g_open each status null, reason UNREACHABLE, note 'depends on (d), which produced no service request id'}]",
      "trace report_route_arms is the empty object: neither the malformed-id arm nor the issued-id arm ran",
      "R2_TR1_THREAD_RERUN_PAIR.md @9e9e6e62f3 section 5: A is every hop met with hop (g) returning the report; B is a 400 from the report route on the ISSUED id; C is 'hop (e) ends NOT-READY or on a terminal refusal'; D is 'any STOP in steps 0-3: nothing of the journey runs'",
      "none of the four fits: A is false; B cannot arise because the report route was never called with an issued id; C's subject is hop (e), which never started; D is false because the prechecks passed (STOP=None), the census passed with 82 armed and 0 off-list admits, and hops (a) through (d) all ran",
      "the first attempt of this same order WAS a clean D (the AC1 precheck stop, row TCKT_VNEXT-D2-S28), so D's own boundary is exercised and distinct"
    ]
  },
  "spec_asserts": "The pair presents A, B, C and D as the signed branch set for the run's outcome, and the GO's step 6 requires the executor to report 'the branch (A, B, C or D)' -- a closed four-way choice over the run's possible endings.",
  "world_is": "A fifth ending exists and occurred: the journey ran past the census and stopped at hop (d), the submission, with a 200 carrying INVALID_INPUT and no issued request id. I reported it as C, because C is the branch whose CONSEQUENCES fit exactly -- it is a RESULT, the code is recorded, there is no re-run and no widening of the read, FWD-1 stays not realized and the code names the next cell -- and I said in the report that the branch set does not name this case rather than quietly widening C's text or inventing an E. Worth separating clearly: this is NOT branch B, so the R2-rr-2 rollback is NOT triggered and the report-id shape check is not implicated; it was never reached in either direction. The practical risk of the gap is that a hop-(d) refusal and a hop-(e) not-ready both land on C and would be told apart only by whoever reads the trace.",
  "notes": "Taxonomy law (CLAUDE.md rule 24(i), MECE over a declared domain) read against the declared domain of branch outcomes, with the uncovered member found by subtraction from the printed hop list rather than by a forward guess. No act proposed; the branch set is the pair's, and re-cutting it belongs to 2.0.0_SA_COO~V2 with 1.0.0_SA_CTO~DELL2. The substantive question for the next cell is upstream of the taxonomy: why POST /api/scoped/investor-reporting/analysis answers 200 INVALID_INPUT for this submission."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W8-S10",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~8",
  "surfaced_at": "2026-10-11T07:54:46Z",
  "one_line": "R2-rn-1 AMENDMENT 5 G4 is silent on a filter read that raises after a stream was active; the runner records ZERO_CALL_VOID with void_reason FILTER_NOT_READABLE.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "fwd1_run.py data_refresh_zero_calls: the filter_log_events read for the filer address sits in a try block; the except branch sets verdict ZERO_CALL_VOID and void_reason FILTER_NOT_READABLE",
      "test_zero_call_read_needs_its_positive_control asserts it with a filter answer that raises"
    ]
  },
  "spec_asserts": "G4: ZERO_CALL_VOID when the group cannot be described or holds 0 streams; zero active streams is ZERO_CALLS_PROVEN; otherwise the filter is read and matches > 0 is NON-ZERO, matches == 0 goes to the ticket-id control.",
  "world_is": "The rule names no verdict for an active stream whose filter read raises (throttle, denied). A raised read is not a zero, so the runner records a void with its own reason rather than a proof or a crash. INERT: it adds a fourth void reason to the three the order names; the issuer may rename or re-rule it.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S32",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~TV2",
  "surfaced_at": "2026-10-11T08:54:30Z",
  "one_line": "Branch E's instruction cannot be satisfied as written: hop (d) served NOT_READY, but /aws/lambda/irpt-ycharts-generate logs NO reason for that call -- the token NOT_READY appears nowhere in the group's 41 events for the window, and the only two reason-bearing events are census arms that both precede the journey ticket's creation.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "run 3 trace hop d_analysis: POST /api/scoped/investor-reporting/analysis, status 200, request_id null, refused_reason NOT_READY, result BRANCH_E_SUBMISSION_REFUSED, idempotency_token r2tr1run3-a5e6c43e3bbe069d00ef4894",
      "full read of /aws/lambda/irpt-ycharts-generate over the token window 2026-10-11T08:12:32Z..08:42:32Z: 41 events; a token census over all 41 returns INIT_START, LATEST, UNEXPECTED, NOT_AUTHORIZED, REPORT, MISSING_REQUEST_FIELD, INVALID_INPUT and nothing else -- the token NOT_READY does not occur",
      "exactly TWO events carry a public_reason_code, and both are census arms: 08:12:47.288Z operation analysis-input-upload code NOT_AUTHORIZED (corr-81d4c714ebf8), and 08:14:05.686Z operation analysis-requests code INVALID_INPUT with internal MISSING_REQUEST_FIELD (corr-193f487e4169)",
      "the journey ticket TCK-20261011-61631267 has created_at 2026-10-11T08:14:27.233Z, and hop (d) necessarily follows hops (b) and (c) -- so BOTH reason-bearing events precede hop (d), whichever invocation served it; the conclusion does not depend on identifying that invocation, which matters because the trace records no correlation id for hop (d)",
      "for completeness, the only invocation in the group after the ticket's creation is START 08:14:32.028Z / END 08:14:37.587Z, 5558 ms, the longest in the window, and it logged neither an irpt_error nor an irpt_internal line"
    ]
  },
  "spec_asserts": "TO-RUN-R2-tr1 AMENDMENT 2 @f0d4c2db95 defines branch E as a RESULT whose handling is to 'record the served code, read the service's own refusal reason from /aws/lambda/irpt-ycharts-generate for that minute (tokens only), no retry, no second submission'; CTO half AMENDMENT 3 part 1 restates it as 'the refusal's reason token is read from the service log and stated'.",
  "world_is": "The served code is recorded (NOT_READY, HTTP 200, a public-code shape) and the no-retry rule was honoured, but the second half of the instruction has nothing to read. For the refusals the service DOES log, the pattern is an irpt_error event carrying operation and public_reason_code, as both census arms show; hop (d) produced no such event. So on this surface a refusal that logs its reason and one that does not are indistinguishable, and the served code is the only available account of why the submission was refused. This is the third instrument in this pair whose evidence the condition written against it cannot produce -- after the zero-call control and the WE_CLIENT_SENT recipient -- and unlike those two it was not foreseeable from the tree, because the service's own refusal path was assumed to log uniformly. Worth separating: NOT_READY is a DIFFERENT refusal from run 2's INVALID_INPUT, so the per-run idempotency token the amendment shipped did work and the CHANGED_INPUTS_SAME_REQUEST_ID collision is gone; what replaced it is unexplained from the log.",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No retry, no second submission, no widening -- the pair forbids all three and none was done. No act proposed and none available to this seat: reading why the submission is NOT_READY needs either the handler's source for that path or a reason on the log line, and neither is in this order's <paths>. There is no fourth run under this half (CTO AMENDMENT 3 part 1: 'If run 3 stops short of hop (g), the next act is the round's slug, not another GO'), so this row is input to the round's slug rather than to another attempt. Companions, both of which CLOSE on run 3: [[TCKT_VNEXT-D2-S29]] -- the zero-call read now reads ZERO_CALLS_PROVEN (NO_INVOCATION_IN_WINDOW) with the CTO's two conditions printed; [[TCKT_VNEXT-D2-S30]] -- condition 3 met on the agreed basis of the code read plus per-ticket WE_CLIENT_* counts, with no recipient inferred. [[TCKT_VNEXT-D2-S31]] closed when branch E was added."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S33",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-11T09:15:51Z",
  "one_line": "L9 round 2 R2-tr-1: TO-RUN-R2-tr1 AC2 NOT MET. No run read a finished report and no ticket holds an issued id: in run 3 hops (e), (f) and (g) are UNREACHABLE with request_id None. This seat's read of the generate function's log agrees that run 3's submission was not refused by the service (12 invocations, 2 refusals, neither NOT_READY; the last invocation ran 5.6 s with none), but acceptance is not measured: no line names the token or a request id and the answer's body was not kept. Three rounds have now stopped at hop (d), each time on the runner.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R2_TR1.md @4387ede65a (msg 4548)",
      "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r2_tr1/r2_tr1_run3_trace.json @4e2e35ac32",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_R2_TR1_L9_GRADE_20261011.md",
      "this seat's filter-log-events on /aws/lambda/irpt-ycharts-generate, 2026-10-11T08:12:32Z to 08:52:32Z (run 3's token window): 12 invocations, 2 refusals logged (analysis-input-upload NOT_AUTHORIZED at 08:12:47, analysis-requests MISSING_REQUEST_FIELD at 08:14:05), neither carrying NOT_READY; the last invocation (08:14:32, 5.6 s) logs no refusal; 0 lines name the run's token and 0 name a REQ- id. /aws/lambda/irpt-export-render in the same window: 15 invocations, all at 08:13, before the submission"
    ]
  },
  "spec_asserts": "TO-RUN-R2-tr1 AC2 (judgment): FWD-1's ACCEPT, the report is made from the filed file and the finished report opens from the same ticket, shown by hops (e) and (g) reading the finished report for the id the service issued and the ticket holds; one firm only; the row removed after exp.",
  "world_is": "FWD-1 is not realized. The one-firm, row-removal and zero-call limbs are the applier's measurements and were not re-run by this seat.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S34",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~TV2",
  "surfaced_at": "2026-10-11T09:28:00Z",
  "one_line": "R2-pk-2's STOP 3 cannot be satisfied because the route's ONE caller is not deployed at all: no live Lambda carries opal_packager.py, so there is no function to name, no CodeSha256 to record and no attach call site to compare -- both halves are written as though a deployed caller exists and only its BYTES were unmeasured.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "DOMAIN FALSIFIED FIRST: one unscoped comp-find over the corpus returned 98 hits across 88800 files scanned; the SURFACED band (first-party source, 22 hits) places every code reference to opal_packager under infra/aws/lambda/investor-reporting/ -- exactly two files, reports/resident_installed.py (imports at :295, wires 'attach': opal_packager.live_attach at :303, handle_commentary_ready at :306) and ycharts/generate/resident_worker.py:864 (a comment). The rest of the band is org/ logs and check scripts, not lambda source",
      "SWEPT BY CONTENT: all 17 investor-reporting functions the source map declares (printed denominator), each one's live package downloaded from its own Code.Location and its member list read -- 0 carry opal_packager.py, 17 do not, 0 unreadable",
      "POSITIVE CONTROL on that member test, run separately: served.py IS found in irpt-status (49 members) and generate_installed.py IS found in irpt-ycharts-generate (104 members), so a miss is a miss and not a broken test",
      "the served AWS graph, 235 LAMBDA nodes scanned, vintage 2026-10-11 08:36:08 UTC, holds no function whose name or properties mention a packager; the only commentary functions are irpt-commentary-composition-read-lambda and irpt-commentary-draft-store-lambda, both downloaded and neither carrying the member",
      "the source map holds ZERO entries naming opal_packager or ycharts/research across 235 entries -- on its own not an absence proof, since Rule 4 records the map as covering 192 of about 198 live functions, which is why the content sweep was run",
      "COHERENT, not mysterious: opal_packager.py was added 2026-10-09T01:25:59Z (7e66decdff, IRPT_ANLREQ TO-AR-g-12) and last changed 2026-10-11T02:59:05Z, while irpt-ycharts-generate's live build dates from 2026-10-09T09:32:22Z and does not contain it -- that build does not bundle research/. The deploy that would carry it is IRPT_ANLREQ's, whose ledger entry irpt-anlreq-t1-commentary-store-and-lambda-20261009 is still OPEN with legs B, SIM and INVOKE stranded, and whose leg B is the commentary.tf apply -- which is why no aws_lambda_function.commentary is live"
    ]
  },
  "spec_asserts": "TO-APPLY-R2-pk2 @dbb7aa26cf step 3 and the packet's step 1b: 'name the Lambda function that runs opal_packager.py, record its live CodeSha256, download its live package, and show that its attach call to /package discards the answer as the tree's does'. The packet's blast-radius table names the gap it meant to close -- 'Not measured: that the deployed packager is the tree's bytes' -- and CTO condition 3 requires the read to 'state the function it read and its CodeSha256'.",
  "world_is": "There is no deployed packager, so the gap is one category wider than either half described. The packet's unmeasured quantity was 'are the deployed caller's bytes the tree's bytes'; the measured answer is 'there is no deployed caller'. Both halves are consistent and careful about the caller COUNT in the tree -- 1 caller, 0 portal callers, read by the worker and re-read by the CTO at opal_packager.py:176-184 -- and that count is about the TREE. Nothing in either half asserts the caller is live, and nothing checks it; the gate was written to compare a live caller against the tree, and the case where none exists falls outside its two branches (reads ticket -> STOP; discards it -> proceed). It is arguable that an absent caller makes this apply SAFER, since no live consumer can break on the narrowed answers. That is not this seat's call: the CTO made step 1b a pre-plan gate with a named STOP, and deciding that an absent caller satisfies a gate written for a present one is an adjudication, not a reading. Second-order, for whoever does decide: the packager's own deploy is still ahead of it, so whether the FUTURE deployed packager reads ticket from the 200 or the changed-under-write 409 is a question about a build neither half examined, and it would be answerable at that deploy rather than this one.",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Nothing was planned, built, uploaded or applied: the STOP precedes step 5's build and step 6's plan, and the artifact object plus the live function both still stand where TO-APPLY-R2-rr2 left them (version RI4EX8i.EL18LgmpA54Fixk.hmjLsH4h, CodeSha256 W03VREoM..., deployed file ca3be343...). STOPS 1 and 2 passed and AC1 reads PK-200-OK 2 of 2 with PK-CODES-OK 5 of 5, so the order is ready to run the moment the gate is resolved. ONE consequence for the issuer's precheck list ([[TCKT_VNEXT-D2-S28]]): the live ticket build is UNCHANGED, so reread_27.py already admits it and cf10e19e... must NOT be added until the apply actually lands -- adding it now would make the list admit a build that is not running. The remedy is the issuer's and the CTO's: either the gate is restated to cover the no-live-caller case, or this apply waits on IRPT_ANLREQ's stranded commentary deploy so that step 1b has something to read. ID NOTE: this row was first appended as S33 and immediately re-identified to TCKT_VNEXT-D2-S34 by its own author, because 3.0.0_SA_CVO appended a different S33 between my next-free-id read and my append -- the append-only channel has no id reservation, so a concurrent writer can take the id a reader just computed. Only my own trailing block was rewritten; the CVO's S33 is untouched."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S35",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-11T10:04:42Z",
  "one_line": "L9 round 2: TO-APPLY-R2-pk2 AC2 MET. The live opal-ticket-api package hashes to the function's CodeSha256 and its one member is byte-equal to the handler at be67d1fd38; CloudTrail shows one code update and no configuration update. 'The one caller was read first' is met in a narrower sense: no deployed caller exists, and this seat read the caller's source, whose attach branches on the status alone. The live arms are unexercised.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R2_PK2.md @5047fa86e6 (msg 4656)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_R2_PK2_L9_GRADE_20261011.md",
      "this seat's live reads 2026-10-11T10:04:42Z: opal-ticket-api CodeSha256 t1EoiJRZ...lej4=, LastModified 2026-10-11T09:47:09Z, Successful; the downloaded package hashes to that CodeSha256 and holds 1 member, lambda_function.py, byte-equal to infra/aws/lambda/ticket_center/lambda_function.py at be67d1fd38 (sha256 cf10e19e423b...) and not equal to it at a366ce52ec (the negative control)",
      "this seat's CloudTrail lookup by the function's name since 2026-10-11T04:00Z: 2 UpdateFunctionCode events (04:19:14Z and 09:47:09Z, both by cloudops-dell2-agent-user) and 0 configuration updates",
      "this seat's read of infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py:268-276: the attach port branches on the status alone (409, then any non-2xx) and reads no member of the 200 body; git diff --numstat a366ce52ec be67d1fd38 on the handler: 16 added, 7 removed"
    ]
  },
  "spec_asserts": "TO-APPLY-R2-pk2 AC2 (JUDGMENT, graded by the CVO at L9): the deployed bytes are the pinned file, the one caller was read first, and nothing else moved.",
  "world_is": "All three limbs hold on this seat's reads, the second as a source read because nothing deployed calls the route. Not re-run by this seat: the 17-function sweep, the resident's build-input read.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S36",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~TV2",
  "surfaced_at": "2026-10-11T10:22:41Z",
  "one_line": "TO-RECORD-R3-sm1's objective and bounds both say 'no AWS write', but the recorder it orders me to run carries an `aws sns publish` to opal-infrastructure-alerts on its half-landed branch -- so a RECORD order's no-AWS-write bound is not a property of the recorder, only of the branch it happens to take.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ci/record-terraform-deploy.sh:871 `aws sns publish --region \"${REGION:-us-east-1}\" --topic-arn arn:aws:sns:us-east-1:313476888478:opal-infrastructure-alerts ...` -- one hit across one file scanned, inside the else branch of the comp-lambdamap reconcile-deployed call at :862-866",
      "the branch is the C1 persistent-half-landed path: it fires when a just-deployed function's live CodeSha256 does not match its S3 artifact after a 45 s settle retry, and it is best-effort (`>/dev/null 2>&1 || echo` keeps the recorder going if the publish fails)",
      "TCKT_VNEXT.TO-RECORD-R3-sm1 @11c612ede3 objective: 'A git record only: no AWS write, no apply, no build, no upload'; its bounds repeat 'No AWS write'",
      "IT DID NOT FIRE on this run, and that is measured rather than assumed: the reconcile printed 'reconcile-deployed: 1 reconciled, 0 first-recorded, 0 HELD, 0 left unrecorded, 0 already-in-parity' then '[RECONCILED] opal-ticket-api: ywAvsfx/j3RTZOoO.. -> t1EoiJRZWXBsSc0H..' and 'reconcile: OK (deployed set in parity)' -- the OK branch, not the ALERT branch",
      "why it could not have fired here: the R2-pk-2 apply fully landed and I verified it three ways before this order -- live CodeSha256 t1EoiJRZ... equals the uploaded object's content-sha256, and the deployed package re-downloaded from Code.Location hashes its single member to the pinned cf10e19e..."
    ]
  },
  "spec_asserts": "The order states a flat bound, 'no AWS write', for an act whose whole mechanism is a third-party script the order itself names and tells the executor to run unmodified ('If it refuses, quote the refusal and STOP: do not hand-edit the map').",
  "world_is": "The bound holds for the path this run took and does not hold for the script. A RECORD order that runs this recorder can publish to SNS whenever the reconcile finds a persistently half-landed function -- which is exactly the state a record act is most likely to meet, since it runs right after an apply. So the bound is satisfied here by the deploy having fully landed, not by anything the order or the executor controls. Two things follow, both narrow. First, an executor who reads 'no AWS write' as a guarantee would be surprised by a publish; I read the code before running it because step 1 told me to, which is the only reason this was visible in advance rather than after the fact. Second, the publish is a notification, and the estate carries a standing moratorium on building alert/SNS/notification paths without Andrew's explicit word -- this is a PRE-EXISTING path in shared CI tooling and nothing here builds or extends one, so the moratorium is not breached; it is named because a future reader comparing the two sentences would otherwise have to work out which applies.",
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Reported in the order's own designated place as well: step 1 asks the executor to state what the recorder writes and commits from the CODE and to say where the code disagrees with the order, with the code winning. This row is the durable carrier, because the divergence outlives this order and the next RECORD order will inherit it. No act proposed and nothing hand-edited: the recorder ran unmodified and its commit 6a5bee406c touched exactly the three paths its own pathspec permits (the map, the CHANGELOG, the reconcile audit log). The remedy, if any, is the issuer's and the CTO's: either the bound is restated as 'no AWS write on the success path, one best-effort SNS publish if the reconcile finds a half-landed function', or the recorder's alert limb is made conditional on a flag. Separately noted, not mine to file: the recorder's own [one-writer] WARN says infra/aws/lambda/ci/source-map-reconcile-audit.jsonl is the laptop's unsuffixed file being written from dell2, and labels itself 'WARN until C-QUEUE' -- an owned, known condition."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S37",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-11T10:28:33Z",
  "one_line": "L9 round 1: TO-RUN-SA-r-1 AC2 NOT MET. The one-firm proof holds on what was exercised (21 of 21 arms with a cottonwood leg read FIRM_BINDING, 0 admits; 5 of 6 ticket routes not exercised), but 0 of 7 hops ran: the run stopped before the hops on a data-refresh route that admitted the token. The stop was the right act. Graded on the applier's trace of 2026-10-09, which cannot be re-read live.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "msg 4720 (round-close-check --round 1 reads two judgment criteria UNGRADED by id)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_R1_SA_R1_L9_GRADE_20261011.md",
      "this seat's count 2026-10-11T10:28:33Z over org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/sa_r1/sa_r1_trace.json (run SA-r-1-2026-10-09T15:40:57Z, the applier's file, claim measured): 27 arms, 22 exercised; 21 carry a cottonwood leg and 21 of 21 read FIRM_BINDING, 0 admitted; the 22nd is the ticket list, which carries no cottonwood leg and shows a filter (8 tickets, one requester firm); 5 ticket routes not exercised, each with its stated reason; the ticket-create arm refused 400 on a missing attachment before the firm check; 0 of 7 hops carry a status; named failure STOP_BEFORE_HOPS on a data-refresh admit (200)"
    ]
  },
  "spec_asserts": "TO-RUN-SA-r-1 AC2 (JUDGMENT, graded by the CVO at L9): the trace -- the one-firm proof with zero cottonwood admits, and every hop recorded with its artifact.",
  "world_is": "The first limb holds on the exercised arms; the second does not: no hop ran. The trace is the applier's own record.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S38",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-11T10:28:33Z",
  "one_line": "L9 round 1: TO-RUN-SA-r-1b AC2 NOT MET. This row restates, under the order's id, the grade this seat gave on 2026-10-10 in row TCKT_VNEXT-D2-S21 (61 of 61 reads returned INVALID_REQUEST_ID; the runner polled its own idempotency token, so no run read a finished report). The grade does not change.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "msg 4720 (round-close-check --round 1 reads two judgment criteria UNGRADED by id)",
      "investigation row TCKT_VNEXT-D2-S21",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_SA_R1B_L9_GRADE_20261010.md"
    ]
  },
  "spec_asserts": "TO-RUN-SA-r-1b AC2 (JUDGMENT, graded by the CVO at L9).",
  "world_is": "Graded NOT MET on 2026-10-10. Row D2-S21 named the criterion as 'SA-r-1b AC2', without the order's id, and the round-close check could not match it.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W8-S11",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~8",
  "surfaced_at": "2026-10-11T12:30:00Z",
  "one_line": "R3-rn-1: the order's constant ROW_LIFETIME_SECONDS = 7200 collides with an existing test that bars the literal 7200 from the runner's code; coded as 2 * 60 * 60 (value 7200).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/fwd1_runner/test_fwd1_runner.py test_token_exp_is_the_argument_and_capped asserts '7200' not in _code_only(run.__file__) (no two-hour TOKEN anywhere in the code)",
      "fwd1_run.py: ROW_LIFETIME_SECONDS = 2 * 60 * 60; the new test asserts run.ROW_LIFETIME_SECONDS == 7200"
    ]
  },
  "spec_asserts": "TO-R3-rn1 item 1: ROW_LIFETIME_SECONDS = 7200 (a module constant), and no earlier test is weakened.",
  "world_is": "A literal 7200 in the runner's code fails the older test, whose intent is that the token never lives two hours (the ROW does, the token does not). The value is 7200; only the spelling differs. The older test was not edited.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W8-S12",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~8",
  "surfaced_at": "2026-10-11T12:30:00Z",
  "one_line": "R3-rn-1: the order names the trace field `cleanup: \"PENDING_ROW_DELETE\"`, but trace[\"cleanup\"] is already an object that holds the cleanup record; the state is coded as trace[\"cleanup\"][\"state\"].",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "fwd1_run.py build_trace: \"cleanup\": {\"row_removed_read_back_absent\": False, \"tickets_completed\": {}}; the existing tests read trace[\"cleanup\"][\"row_deleted_at_unix\"] and the other keys",
      "fwd1_run.py leave_row_in_place and finish_cleanup write state PENDING_ROW_DELETE then DONE, with row_left_in_place, row_delete_not_before (ISO and unix), known_limit, row_deleted_at, row_removed_read_back_absent and finished_by, all inside trace[\"cleanup\"]; job_last_read is top level"
    ]
  },
  "spec_asserts": "TO-R3-rn1 items 1 and 2: the trace carries cleanup: \"PENDING_ROW_DELETE\" and later cleanup: \"DONE\".",
  "world_is": "A string cannot replace the object without breaking the earlier tests and losing the ticket and wait record. A reader of the trace looks for cleanup.state, not a string at cleanup.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W8-S13",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~8",
  "surfaced_at": "2026-10-11T12:30:00Z",
  "one_line": "R3-rn-1: 'accepted' is coded as 'hop (d) was not refused', so two hop (d) outcomes with no usable REQ id (SUBMISSION_ANSWER_UNREADABLE and REQUEST_ID_UNRESOLVED) also leave the row in place.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "fwd1_run.py hop_d_analysis: submitted_at_unix is set whenever submission_refusal() returns None; the runner's own test names the first case 'accepted without a REQ id'",
      "test_accepted_submission_leaves_the_row_and_exits_3 covers an answer with state QUEUED and an identity that carries no request_id"
    ]
  },
  "spec_asserts": "TO-R3-rn1 item 1: the row is left in place when hop (d) is classified ACCEPTED by the existing state-and-identity rule.",
  "world_is": "The existing rule classifies a refusal by state and HTTP status; an answer that is not a refusal and carries no usable id is not classified as accepted or refused by it, yet the service may have queued a job whose start re-reads the row. Leaving the row costs two hours of a synthetic row; deleting it could kill a job. Chosen: leave it.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S39",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-11T12:05:17Z",
  "one_line": "L9 round 3: TO-RUN-R3-tr1 AC2 NOT MET. Run 4 is the first past the submission (accepted, queued, the service's own request id), but no read returned a finished report (40 polls, each NOT_FOUND) and the two ticket hops did not run. The job's fate is unknown; the generation dead-letter queue still reads 8, so it was not dead-lettered by the grade. irpt-status changed build 8 minutes into the polling; both builds answered the same.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R3_TR1.md @92c34457f2 (msg 4877)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_R3_TR1_L9_GRADE_20261011.md",
      "this seat's read 2026-10-11T12:05:17Z of org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r3_tr1/r3_tr1_run4_trace.json (the applier's file, claim measured): hops a, b, c answered 200, 201, 200; hop d answered 200, QUEUED, with a request id of the service's own form; hop e made 40 polls, last code NOT_FOUND, outcome NOT_READY, last poll 2026-10-11T11:38:55Z; hops f and g carry status 0, UNREACHABLE, report_opened false; report_route_arms is empty; result is null. This seat's live read at the grade: the generation dead-letter queue holds 8 messages, as it did before the run. irpt-status changed build at 11:26:53Z (this seat's reads of 10:53Z and 11:5xZ), inside the polling window"
    ]
  },
  "spec_asserts": "TO-RUN-R3-tr1 AC2 (JUDGMENT, graded by the CVO at L9 on the trace): FWD-1's ACCEPT -- the report is made from the filed file, and the finished report opens from the same ticket, shown by hop (e) and hop (g) reading the finished report for the id the service issued and the ticket holds; one firm only.",
  "world_is": "No finished report was read and no report opened from the ticket. Not re-read by this seat: the route census, the zero-call proof. The order is still pending on its row-delete step.",
  "disposition": "UNDER_INVESTIGATION"
}
```


```json
{
  "id": "TCKT_VNEXT-D2-S40",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-11T12:54:55Z",
  "one_line": "The report read does NOT refuse an internal reader who does not own the request, so 'a foreign id opens nothing' does not hold for the readers of a ticket whose creator recorded the id (cell R3-rf-1).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/ops/owned_requests.py:175-184: the record's owner firm must equal the data firm, then authorize_current(principal, owner) must be True",
      "infra/aws/lambda/investor-reporting/_scope/interactive_access.py:115-116: for principal_class OPAL_GLOBAL authorize_current returns True for any owner; lines 117-119 hold an ordinary viewer to its own firm and its own principal_id",
      "infra/aws/lambda/investor-reporting/_scope/tests/test_interactive_access.py:22-31 and 47-52: the tests assert both halves",
      "infra/aws/lambda/ticket_center/lambda_function.py:164: the REPORT matrix row admits INTERNAL only, so every creator the new branch admits is an internal caller",
      "scope: those files in the working tree at box/dell2 73eb85c914; code read only, nothing exercised; whether a profile's allowedFirmIds narrows the data firm on this read was not read"
    ]
  },
  "spec_asserts": "CTO msg 4945, for the deploy pair of cell R3-rf-1: state what stops a ticket pointing at another person's request -- the report read is refused by IRPT unless the reader owns the request, so a foreign id opens nothing; if it does not hold for an internal reader, that is a finding before the apply.",
  "world_is": "It holds for an ordinary (firm) viewer and does not hold for an internal Opal viewer, who may by design open another creator's request. So a creator-recorded foreign id gives an internal reader nothing that reader could not already open; what it can do is make a ticket show a report that is not that ticket's. Nothing binds the recorded id to the ticket: the ticket service does not check that the request's stored ticket_id equals this ticket.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S41",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-11T14:33:12Z",
  "one_line": "The issuer lists fourteen BLOCKING or ARMED rows still reading UNDER_INVESTIGATION. Read against this channel's own files: five of them already carry this seat's disposition (D2-W3-S2, D2-S8, D2-S10, D2-W6-S1, D2-W6-S2); nine did not, and are adjudicated now. Beyond the fourteen, 40 INERT rows of rounds 1 to 3 have never been compiled by this seat: in this project the issuer wrote its own slug files and this seat was asked for grades only. That compile is owed and waits on the two pending orders.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R4_RUN/STALE_ROW_DISPOSITIONS_FOR_CVO_20261011.md @5719b01097 (msg 5123)",
      "this seat's subtraction over the channel: 49 rows undispositioned before this compile, by id against every adjudication and remediation file"
    ]
  },
  "spec_asserts": "Spine L8/L10 (CLAUDE.md rule 27): the CVO compiles the channel and its one send is the slug; a COO's drain-end packet is a different artifact sharing the label.",
  "world_is": "Nine rows are dispositioned on the issuer's quoted slug lines; this seat re-measured three of them (D2-S18, D2-S28, D2-S34) on its own earlier reads and none of the other six.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S42",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-11T17:53:41Z",
  "one_line": "L9 round 4: TO-RUN-R4-tr1 AC2 NOT MET. Run 5 filed a ticket by the one-step sequence, was accepted, and the creator recorded the issued id on the ticket, each read live for the first time; but no read returned a finished report (40 polls, each NOT_FOUND) and nothing opened from the ticket. It is the wall run 4 met. The generation dead-letter queue still reads 8, so the job was not dead-lettered 43 minutes on. The host-side read of why is another seat's and is not in.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R4_TR1.md @04a542b518 (msg 5497)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_R4_TR1_L9_GRADE_20261011.md",
      "this seat's read 2026-10-11T17:53:41Z of org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r4_tr1/r4_tr1_run5_trace.json (the applier's file): mode ONE_STEP, 1 submission call; upload 200; ticket 201 with source ticketcenter:i1; the claim hop NOT RUN; the submission 200 with the service's own request id and the ticket's id; the finished-report read 40 polls, last code NOT_FOUND, outcome NOT_READY, last poll 2026-10-11T17:29:36Z; the open hop UNREACHABLE, report_opened false; result null. This seat's live read at 17:52Z: the generation dead-letter queue holds 8 messages, the count before the run"
    ]
  },
  "spec_asserts": "TO-RUN-R4-tr1 AC2 (JUDGMENT, graded by the CVO at L9): FWD-1's ACCEPT -- the report is made from the filed file, and the finished report opens from the same ticket, shown by the finished report read for the id the service issued and the ticket holds; one firm only.",
  "world_is": "No finished report was read and none opened from the ticket. The form's own code was not executed; the producer was the vendor path. The order is pending on its row-delete step.",
  "disposition": "UNDER_INVESTIGATION"
}
```


### TCKT_VNEXT-D2-S43 -- terraform's RENDERED plan prints an empty env string as `null`, in BOTH directions

**owner:** `0.7.0_AE_CloudOps~TV2` (filer) | **disarm_owner:** n/a -- not armed; this is an instrument trap, not a hazard
**class:** INSTRUMENT | **found:** 2026-10-11, cells R4-pk-2 and R4-pk-3, both applies of `opal-ticket-api`

**spec_asserts:** a reader of `terraform plan`'s rendered diff can tell what an env value will be after the apply, and can
tell an ABSENT key from a key that is PRESENT AND EMPTY. Cell R4-pk-2's branches turned on exactly that distinction: branch A
was "present-and-empty, the door admits nobody", and a key AWS had DROPPED would have been a different world.

**world_is:** the rendered diff prints the empty string as `null`, in both directions, and twice in one day:
- R4-pk-2 ADDED `PACKAGE_ALLOWED_FIRMS = ""`. The rendered plan read `+ "PACKAGE_ALLOWED_FIRMS" = null`.
- R4-pk-3 CHANGED that same key from `""` to three firms. The rendered plan read
  `~ "PACKAGE_ALLOWED_FIRMS" = null -> "49financial,cottonwood,inflection"`, calling the BEFORE value `null`.

In R4-pk-3 the before value was independently known to be the empty string from two other instruments: the saved planfile
read as JSON (`terraform show -json <planfile>`, which gives `before` as `''`), and a live
`get-function-configuration` read taken minutes earlier showing the key PRESENT at length 0 with sha256 prefix
`e3b0c44298fc1c14`, the hash of the empty string. So the rendered `null` is a rendering of `""`, not a reading of the world.

**why it matters:** `null` and `""` are NOT the same thing to this consumer. AWS DROPS an env key whose value is null and
KEEPS one whose value is empty, and the handler treats unset and empty alike only because someone wrote it that way -- which
is a property of the handler, not of Terraform. A seat that verifies "the key is present and empty" by reading the rendered
diff cannot distinguish the two states it is being asked to tell apart, and the failure is SILENT: the rendered output is
well-formed and looks like an answer.

**the sound instrument:** read the SAVED planfile as JSON (`terraform show -json <planfile>`) and compare `before` against
`after` field by field; confirm after the apply with a live `get-function-configuration`, recording each value as a LENGTH
and a sha256 rather than printing it. Both applies did this and both landed correctly; the row exists so the next seat does
not have to rediscover it, and so that "the rendered plan said so" is never offered as the evidence.

**not established:** whether this is specific to the `aws_lambda_function` environment block, to this provider version, or
general to every map-typed attribute. One object, two sightings, same attribute -- the domain of the claim is
`environment.variables` on this resource type and nothing wider is asserted here.

```json
{
  "id": "TCKT_VNEXT-D2-S43",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-11T20:10:59Z",
  "one_line": "Row TCKT_VNEXT-D2-W6-S2 (data-refresh admits a caller with no userType; ARMED since round 1) is DISARMED and closed by CTO ruling msg 5737 on a read of the deployed bytes.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r5_dr1/DATA_REFRESH_DEPLOYED_VS_BUILD_INPUT_20261011.md and members.json beside it (0.7.0_AE_CloudOps~TV2, order TCKT_VNEXT.TO-READ-R5-dr1, report msg 5712): MEMBERS 2 EQUAL 2 DIFFERENT 0 NOT_IN_SOURCE_DIR 0; deployed == recorded commit d9539cc0b7 == HEAD; the download's sha256 equals the live CodeSha256",
      "the same file, from the deployed lambda_function.py (is_opal_internal line 142, validate_user_type line 168): userType Dev admitted by exact match; a caller with no userType refused unless Opal-internal; tier internal admitted whatever its userType",
      "1.0.0_SA_CTO~DELL2 msg 5737: 'Row TCKT_VNEXT-D2-W6-S2: DISARMED and closed ... That is the estate's rule, exercised live today by NFRA_OPSWKF's release. Record the applier's file in the row.'",
      "not re-read by this seat: the deployed package (the applier's read); the NFRA_OPSWKF exercise (the CTO's statement)"
    ]
  },
  "spec_asserts": "Row D2-W6-S2: a caller whose userType is absent is admitted on the data-refresh routes.",
  "world_is": "The deployed function refuses a caller with no userType unless that caller is Opal-internal, and it is byte-equal to its build input. An Opal-internal caller with any userType is admitted; the CTO rules that is the estate's rule and not a defect of this function (rows D2-S16 and D2-S17 describe it).",
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "CTO ruling msg 5737: the deployed data-refresh function equals its build input and refuses a caller with no userType unless Opal-internal; that is the estate's rule. This row records the closure of row TCKT_VNEXT-D2-W6-S2 and carries no hazard of its own."
}
```

### TCKT_VNEXT-D2-S44 -- the closure record of row D2-W6-S2, renumbered by citation: the JSON row above by 2.0.0_SA_COO~V2 took the id D2-S43, which the applier's row already held

```json
{
  "id": "TCKT_VNEXT-D2-S44",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-11T20:18:57Z",
  "one_line": "Two rows in this channel carry the id TCKT_VNEXT-D2-S43: the applier's heading-and-prose row on terraform's rendered null, and this seat's JSON row recording the closure of row D2-W6-S2 (commit 11e26d72b5). Cite the closure record as THIS row, D2-S44.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "this file: the heading '### TCKT_VNEXT-D2-S43 -- terraform's RENDERED plan prints an empty env string as null' (0.7.0_AE_CloudOps~TV2, filed during R4-pk-3) and, directly after its prose, the JSON block whose id is TCKT_VNEXT-D2-S43 and whose surfaced_by is 2.0.0_SA_COO~V2",
      "this seat's id scan read JSON id lines only (max 42, so it minted 43) and did not read headings; the applier's row has no JSON id line",
      "surprise-row-gate refused a renumbering of the committed row ('The channel is append-only: retire it with a new row that cites it'), so this row is the retirement"
    ]
  },
  "spec_asserts": "A row id names one row.",
  "world_is": "D2-S43 names two. The applier's row keeps the id. The closure of row D2-W6-S2 (DISARMED and closed by CTO ruling msg 5737 on the applier's read of the deployed data-refresh bytes: MEMBERS 2 EQUAL 2; a caller with no userType refused unless Opal-internal) is to be cited as D2-S44; its evidence is in the JSON block above with this seat's name.",
  "disposition": "UNDER_INVESTIGATION"
}
```


### TCKT_VNEXT-D2-S45 -- the clamp precheck's 27 is a CLOSED historical set, so it can never take in a new scoped route

**owner:** `0.7.0_AE_CloudOps~TV2` (filer) | **disarm_owner:** n/a -- not a hazard; the routes ARE clamped (see world_is)
**class:** INSTRUMENT / DENOMINATOR | **found:** 2026-10-11, cell R5-ml-2, step 8 of TO-APPLY-R5-ml2
**read the same hour by:** `1.0.0_SA_CTO~DELL2` -- its half asked for exactly this row ("an unclamped scoped route is not
left to a later round")

**spec_asserts:** `clamp_precheck.py` reading `READ27 27/27` after an apply that adds two scoped ticket routes tells a reader
that the firm clamp covers the routes now live. The task order's step 8 anticipated the two readings it could give: the census
"does not take in the two new routes", or "the total changes".

**world_is:** NEITHER, exactly. The total did **not** change -- it reads `READ27 27/27` with `opal-ticket-api 7113a749
CLAMPED` -- and the two new route names appear **nowhere** in its output or its JSON table (0 mentions of `commentary`;
`commentary-draft` and `commentary-sent` both absent from the table). The reason is in the precheck's own first line: it reads
*"which of the **27 formerly-MORE_THAN_ONE** routes run the firm clamp LIVE"*. Its denominator is a **frozen historical set**
named in round 3, not a live census of scoped routes. So:

- `27/27` is TRUE of its declared domain and says **nothing at all** about a route created after that set was fixed;
- the total was never going to move, so "the total changes" could not have happened either;
- the tell is the one rule 24(i) names: a denominator whose scope **in TIME** is narrower than the sentence beside it. "27 of
  27 clamped" reads like coverage of the live surface; it is coverage of a 2026-10-xx snapshot.

**the substantive question, answered directly from the DEPLOYED bytes rather than left to the instrument:** both new routes DO
run a firm check. Read from the package downloaded from the function's own `Code.Location` after the apply (handler sha256
`7113a749...`):

- `commentary_draft_ticket`, deployed line 1532: at line 1552,
  `if cur is None or (cur.get("requester") or {}).get("firm") not in COMMENTARY_ALLOWED_FIRMS: return _deny("COMMENTARY_DRAFT", pc)`
  -- one folded check, so a missing ticket and an off-list firm return the **same** deny. That is AMENDMENT 1's first
  requirement, confirmed in the deployed bytes and not merely in the diff.
- `commentary_sent_ticket`, deployed line 1575: `_resolve_scope(actor, pc)` at 1583 and
  `_in_profile_scope(actor, (cur.get("requester") or {}).get("firm"))` at 1587, answering 404 out of scope -- the report
  route's own check.

So there is **no unclamped scoped route**. What there is, is an acceptance instrument that cannot see two live routes and
whose PASS line invites the opposite conclusion.

**why it matters:** AC1 was the only mechanical criterion on this apply. A reader taking `READ27 27/27` as "the clamp covers
the ticket routes" would be wrong by two routes, and would be wrong the same way after the next route is added. The failure is
silent and reads identically to full coverage.

**what would fix it (not done here -- not this seat's and not in this order's bounds):** the precheck's domain becomes the
live scoped-route set rather than the 27, with its total printed as `<clamped>/<routes found live>` so adding a route moves
the denominator. Until then the criterion's expectation is the issuer's to amend, which the order says plainly.

**not established:** whether any OTHER scoped route created since the 27 was fixed is outside the clamp. I measured the two
routes this apply added and did not sweep the rest of the API's 121 routes; that sweep is a different read with a different
denominator.

### TCKT_VNEXT-D2-W24-S1 -- the precheck's table is a list, so the handler rows go to a sibling file

```json
{
  "id": "TCKT_VNEXT-D2-W24-S1",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~24",
  "surfaced_at": "2026-10-11T22:10:03Z",
  "one_line": "TO-R5-pc2 asks for a NEW top-level key ticket_handlers in the precheck's JSON table, but that table is a JSON list with no top-level key, and existing tests read it as a list; the handler rows are written to a sibling file instead.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~13/clamp_precheck/clamp_precheck.py main(): Path(a.out).write_text(json.dumps(table, indent=1)) where table is the list build_table returns",
      "test_clamp_precheck.py test_irpt_host_on_a_release_build_is_clamped and test_unreadable_host_is_named_and_the_total_is_not_full iterate json.loads(out) as a list of rows (t['function']); the order says no existing test changes and the existing rows stay byte-identical",
      "also: the shared test helper ticket_source() gained a lambda_handler router (additive, no existing test body changed) because a deployed member with no lambda_handler now exits non-zero (TICKET_HANDLERS UNREADABLE) rather than passing as 0 handlers"
    ]
  },
  "spec_asserts": "The precheck's JSON table has top-level keys, and a new key ticket_handlers can be added beside the existing ones without changing the existing rows.",
  "world_is": "The --out table is a bare list of host rows. Wrapping it in an object would change every existing row's container and break the tests that read it as a list. The handler rows are written to <out stem>_ticket_handlers.json as {ticket_handlers, dispatched, classed}; the --out file is byte-identical to before for the same inputs (asserted by test_the_read27_line_and_its_table_rows_are_unchanged).",
  "disposition": "UNDER_INVESTIGATION"
}
```

### TCKT_VNEXT-D2-S46 -- any holder of lambda:InvokeFunction on a function behind the portal authorizer can be any caller to it

```json
{
  "id": "TCKT_VNEXT-D2-S46",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-11T22:43:51Z",
  "one_line": "Any holder of lambda:InvokeFunction on a function behind the portal authorizer can be any caller to it: a direct invoke goes around the authorizer and the function believes the event's own caller context.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO~DELL2 (its own word, msg 6001: 'one row in this project's channel, owner me')",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ticket_center/lambda_function.py:300-309 (_actor): the caller's email, userType, firmId and allowedFirmIds are taken from event.requestContext.authorizer.lambda and from nowhere else; nothing in the handler checks that the event came through API Gateway",
      "aws lambda get-policy on opal-ticket-api (this seat, 2026-10-11 22:4xZ): the RESOURCE policy has one statement, the API Gateway service with the portal API's source ARN; it does not bound identity-based grants",
      "iam simulate-principal-policy for arn:aws:iam::313476888478:user/cloudops-dell2-agent-user on that function's ARN (this seat, same minute): lambda:InvokeFunction allowed, lambda:GetFunction allowed",
      "1.0.0_SA_CTO~DELL2 msg 5396: an administrator identity reads every secret and the laptop's agent sessions run as it; by the same reasoning it may invoke any function. NOT read by this seat: which other identities hold lambda:InvokeFunction on this or any other function behind the authorizer",
      "scope: ONE function read (opal-ticket-api) and ONE identity simulated; the sentence about 'a function behind the portal authorizer' in general is the CTO's and is inferred for every other function"
    ]
  },
  "spec_asserts": "The portal authorizer is the only identity source of the ticket service (the handler's own docstring at line 301).",
  "world_is": "It is the only identity source the handler READS, and a direct invoke supplies it. An agent identity on this box can therefore call the ticket service as any internal person, any client or any service subject, read and write, with no token. The round-6 direct-invoke act (TO-RUN-R6-fn1) uses exactly this, for five GETs under a signed pair. No grant is added by this project; whether the invoke permission should be narrower is the owner's.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-S47",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-11T23:10:27Z",
  "one_line": "L9 round 6: TO-RUN-R6-fn1 AC2 MET for the ticket. By five direct invocations of the deployed ticket function, a client of another firm is refused the ticket, the list and a missing id, and an internal caller is served as the control. The refusal is by class: the ticket's own firm's client is refused the same way. FWD-2 is not yet realized, because its sentence also names the file and the file's second arm is owed. Not shown live: the firm fence between internal callers.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R6_FN1.md @31091d1eeb (msg 6047)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_R6_FN1_L9_GRADE_20261011.md",
      "this seat's reads 2026-10-11T23:10:27Z: the applier's result file org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r6_fn1/RESULT.json, 5 arms, each with no function error: four answered 403 with the principal class client-human and naming no ticket, one answered 200 with 27 key names and a status only; and the ticket function's live code hash, which begins as the packet states it did at the act. No invocation was made by this seat"
    ]
  },
  "spec_asserts": "TO-RUN-R6-fn1 AC2 (JUDGMENT, graded by the CVO at L9): FWD-2's ACCEPT for the TICKET, 'a person at another firm cannot open the request', shown by arms A2, A3 and A5 refused with A4 served as the control.",
  "world_is": "No invocation was made by this seat. The file is served by another service and was not touched. Rows D2-S20 and D2-S46 stand.",
  "disposition": "UNDER_INVESTIGATION"
}
```

### TCKT_VNEXT-D2-S48 -- the investor-reporting internal firm reader leaves a caller with no users row unrestricted, as the ticket service did

```json
{
  "id": "TCKT_VNEXT-D2-S48",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-11T23:39:35Z",
  "one_line": "The investor-reporting service's INTERNAL firm reader has the same no-row case the ticket service is about to close: an internal caller with no users row is left unrestricted, by the code's own stated rule.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/_authz/served.py:1138-1166 (_internal_allowed_firms), printed by this seat 2026-10-11 ~23:5xZ: 'Returns None = UNCHANGED (no row, no attribute, or an empty list)'; `if row is None or \"allowedFirmIds\" not in row: return None`",
      "the same file, lines 1100-1136 (_service_allowed_firms), read by worker 0.9.0_WK_TCKT_VNEXT~26 and NOT printed by this seat: no row, no attribute and an empty list each return an empty list (no firm)",
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~26/EMPTY_FIRM_LIST_READ.json @1a47d695fb (claim: inferred; the portal authorizer was not found in the checkout and three of its cells are NOT_READ)",
      "scope: code read at HEAD on box/dell2; nothing invoked; the deployed bytes of the investor-reporting functions were not compared with this file"
    ]
  },
  "spec_asserts": "TCKT_VNEXT PRD v0.4 ADDENDUM 3 (C-FENCE): an internal caller the users table does not know is refused; 'the service does not grant its widest reading to a caller it cannot find'. The addendum rules on the ticket service only.",
  "world_is": "The ticket service is being changed to refuse that caller (TO-R7-nr1). The investor-reporting internal reader, which applies when a firm other than the caller's own is selected, returns unchanged for no row, and its docstring states that as the rule (IB-pr-387, CTO msgs 2367 and 2569). After the ticket release the two services answer the same caller differently. Whether the investor-reporting reader should follow is not this project's to rule: it is IRPT's contract and the CTO's. Nothing is changed here.",
  "disposition": "UNDER_INVESTIGATION"
}
```


### TCKT_VNEXT-D2-S49 -- "refused today" by the firm-scope lookup is NOT a row count, and a live row proves it

**owner:** `0.7.0_AE_CloudOps~TV2` (filer) | **disarm_owner:** n/a -- not a hazard: the affected caller is refused either
way. The hazard would be a release built on the count alone.
**class:** DENOMINATOR / MECE | **found:** 2026-10-11, cell R7-ct-1, step 2 of TO-READ-R7-ct1
**for:** the pair of the release that refuses an internal caller with no PROFILE row

**spec_asserts:** the order and the PRD's ADDENDUM 3 describe who the firm-scope lookup refuses TODAY as a ROW COUNT:
"More than one such item is a refusal today; none will be a refusal after the release." On that model, reading
`with_more_than_one_row = 0` says nobody is refused today, and the release's only new refusal is the no-row case.

**world_is:** the count is indeed 0, and that is not the whole set. `_profile_scope`
(`infra/aws/lambda/ticket_center/lambda_function.py`, read at HEAD) has THREE refusal paths, only one of which is a count:

1. line 375 -- more than one PROFILE row: `403 firm scope lookup failed`. **Measured: 0 callers.**
2. line 381 -- the lookup raised: `403 firm scope lookup failed`. Not reachable by a read of rows.
3. **line 391 -- `allowedFirmIds` is present and is NOT a list: `403 firm scope malformed`.** The guard is
   `if isinstance(val, list)`, and `_ddb` is `boto3.resource` (line 71), so a DynamoDB `S` arrives as a Python `str`,
   fails that test, and falls through to the refusal. **Measured: ONE live row**, digest `35cb8f292b44`, `firmId
   opal-capital`, `status active`, carrying `allowedFirmIds` as a STRING of length 10 which is not the literal `ALL`.
   (A string `ALL` would fail the same way -- the code's own docstring says the literal belongs INSIDE a list, where it
   "is just an id that matches nothing".)

So the set of internal callers the lookup refuses today is `{count > 1} UNION {non-list value}`, and the second member
is non-empty while the first is empty. A reader who checks only the count concludes "nobody is refused today" and is
wrong by one.

**a second path on the SAME row, which makes the first possibly unreachable:** that row also carries `userType
"service"` with a local-part that is NOT one of the three service subjects the handler knows
(`svc-ticket-form`, `svc-analyst-intake`, `svc-commentary`). If the authorizer mints `userType "service"` for it,
`principal_class` returns UNRESOLVABLE at line 324 -- "an unknown service subject is nobody" -- and every action denies
BEFORE the scope lookup is reached, so the malformed value never fires. **Which path fires depends on the userType the
authorizer mints, which is NOT visible to a read of these two tables.** Either way the caller is refused; the point of
this row is that neither path is a row count.

**why it matters:** the release's pair is being built on a count. The count is a sound answer to "who has no row" and
not to "who does the lookup refuse". If the pair's record says "0 refused today" on the strength of
`with_more_than_one_row = 0`, it will be contradicted the first time this row is exercised, and the contradiction will
look like a regression introduced by the release when it predates it.

**what would close it (not mine, and not in this order's bounds):** the release's pair states its "refused today"
population as the UNION of the three paths, with the non-list case measured; and someone who owns that identity decides
whether the attribute should be a list, be absent, or whether the row should exist at all.

**not established:** whether any row in a firm OTHER than `opal-capital` carries a non-list `allowedFirmIds`. My
population was the internal one this order defines -- 30 addresses -- so the 33 PROFILE rows of other firms were not
examined for this attribute's type. A sweep of all 56 PROFILE rows is a different read with a different denominator.

### TCKT_VNEXT-D2-S50 -- a DISABLED users row still admits its address: the no-row rule reads existence, not status

```json
{
  "id": "TCKT_VNEXT-D2-S50",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-12T00:08:14Z",
  "one_line": "The no-row refusal reads whether a users row EXISTS, not its status: a DISABLED row still admits a caller presenting its address by direct invoke.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO~DELL2 (its own word, msg 6180: 'File it as one row of this project, owner me, beside D2-S46. This release does not fix it.')",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ticket_center/lambda_function.py at 09488abbb1, _profile_scope: the lookup keeps items whose SK is PROFILE and reads allowedFirmIds; no line reads the row's status",
      "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r7_ct1/INTERNAL_CALLERS_AND_PROFILE_ROWS_20261011.json @8d900213a1: 23 internal addresses with one row, 21 active and 2 disabled; both disabled rows have no firm list (this seat's read of the file)",
      "PRD v0.4 ADDENDUM 3 line 239 says 'every active internal user'; its CONTRACT sentence (line 235) says 'holds no PROFILE row'. The CTO's msg 6180 names the first as its own error",
      "scope: code and one count file read; NOT read: whether the portal authorizer refuses a disabled user at sign-in (it is not in this checkout), so the admission is shown only for a caller that goes around the authorizer (row TCKT_VNEXT-D2-S46)"
    ]
  },
  "spec_asserts": "PRD v0.4 ADDENDUM 3: an internal caller the users table does not know is refused; its count speaks of ACTIVE internal users.",
  "world_is": "After the round-7 release a caller presenting a disabled user's address by direct invoke is admitted with no firm fence, exactly as before it. The round-7 proof's twin arm N3 uses one such row deliberately (a non-human Dev identity). The release does not fix this and does not claim to.",
  "disposition": "UNDER_INVESTIGATION"
}
```


### TCKT_VNEXT-D2-S51 -- an UNQUOTED hyphenated CloudWatch filter-pattern returns 0 silently, and 0 reads as "it never logged"

**owner:** `0.7.0_AE_CloudOps~TV2` (filer) | **disarm_owner:** n/a -- an instrument trap, not a hazard
**class:** INSTRUMENT / RETRIEVAL | **found:** 2026-10-12, cell R7-nr-3, step 10 of TO-APPLY-R7-nr2

**spec_asserts:** `aws logs filter-log-events --filter-pattern FIRM-SCOPE-NO-ROW` counts the lines carrying that token, so a
result of 0 means the function did not log it. The order's step 10 asks for exactly that count, expecting 2.

**world_is:** the UNQUOTED pattern returns **0 events** while the SAME window holds **2** such lines. CloudWatch Logs filter
syntax treats a bare hyphen as part of its own grammar, so the term must be double-quoted:

| pattern, same log group and same window | events |
|---|---|
| `FIRM-SCOPE-NO-ROW` (unquoted) | **0** |
| `"FIRM-SCOPE-NO-ROW"` (quoted) | **2** |
| no filter at all, counted client-side | 16 scanned, **2** carrying the token |

The zero is well-formed, returns rc 0, and is indistinguishable at a glance from "the code path never ran" -- which, on this
order, would have meant "the release does not log its refusal", i.e. a finding against a release that was in fact working.

**how it was caught:** the order's own step-10 wording invites a bare count, and I ran one. The thing that exposed it was a
CONTROL I ran beside the zero -- the same pattern minus the specific suffix (`FIRM-SCOPE`), which ALSO returned 0. Two zeros
where at least one had to be non-zero is a contradiction, and a contradiction is checkable where a single zero is not. An
unfiltered read then printed 16 events as the denominator and found the 2 lines client-side.

(A second, unrelated zero preceded it and was mine, not the tool's: a hand-typed `--start-time` of `1791778800000`, which is
04:20Z, about four hours in the FUTURE of the act. It also returned a clean 0. Deriving the window from `date -u +%s` fixed
it. Two different causes, one indistinguishable symptom.)

**the sound instrument:** quote every hyphenated term in a filter pattern, AND print a denominator -- either an unfiltered
count over the same window filtered client-side, or a control pattern that must match something. CLAUDE.md already says a
failed retrieval returns a VALUE and to put the control on the retrieval; this is that rule's CloudWatch instance, and the
specific syntax is what the rule does not name.

**not established:** which other characters CloudWatch's filter grammar swallows unquoted. I measured the hyphen on one log
group with one pattern. Colons, slashes and dots are plausible and untested, so no claim is made about them.

### TCKT_VNEXT-D2-S52 -- the portal authorizer's source at HEAD is ahead of the build input recorded as deployed (a render-token path)

```json
{
  "id": "TCKT_VNEXT-D2-S52",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-12T01:04:41Z",
  "one_line": "The portal authorizer's source at HEAD is 188 lines ahead of the build input recorded as deployed: a render-token path is in the tree and, by the source map, not in the live function.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r8_ds1/DISABLED_USERS_READ_20261012.json @e377de62b6 (0.7.0_AE_CloudOps~TV2, claim measured): opal-portal-authorizer live CodeSha256 equals the source map's artifact hash; the map's last_deployed_commit is 26ffa22b79 (2026-09-09); `infra/aws/users/lambda/portal-authorizer/index.mjs` is 450 lines at HEAD and 262 at that commit",
      "the same file: the added code is a render-token path (getRenderPublicKeyPem, isRenderAudienceToken, hasForbiddenRenderClaims, assertBoundedRenderExpiry, authorizeRenderToken); the function's LastModified (2026-10-03) is later than the map's last_deployed_at, which the applier reads as consistent with a configuration-only update and did not establish",
      "NOT read by anyone in this project: the deployed bytes (no download, by the order); whether the artifact was built from 26ffa22b79's source; whether the render-token path is deliberately unreleased or is deployed by a path the source map does not record",
      "this seat's own part: the round-8 order pointed the applier at the HEAD file as 'the authorizer's source'; the applier re-measured against the recorded build input and found the difference"
    ]
  },
  "spec_asserts": "The round-8 order's pointer: the authorizer's source is `infra/aws/users/lambda/portal-authorizer/index.mjs` (as `infra/aws/terraform/portal-auth/lambdas.tf:61-63` names it).",
  "world_is": "That file at HEAD is not the build input the source map records as live. The round-8 answer (neither authorizer reads a users row's status) was measured on both and holds on both, so this project's finding is not affected. The gap itself belongs to whoever owns the render-token work (the comment in the file cites IRPT_BCKEND.TO-IB-rtr-2): either a release is owed or the map is behind. Nothing is changed here.",
  "disposition": "UNDER_INVESTIGATION"
}
```

### TCKT_VNEXT-D2-S53 -- an ACTIVE users row on an outside company's domain carries the internal firm id with no firm list

```json
{
  "id": "TCKT_VNEXT-D2-S53",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-12T01:33:52Z",
  "one_line": "An ACTIVE users row on an outside company's domain carries the internal firm id with no firm list: it signs in and reads every firm, in every service that classes by firm id.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO~DELL2 (its own word, msg 6259: 'File it as its own row of this project, ARMED, owner me'). Whether the row should be internal is Andrew's; the CTO tells him and the manager carries it to the laptop.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r9_ct1/ACTIVE_INTERNAL_ROWS_BY_DOMAIN_20261012.json @e7bb608065 (0.7.0_AE_CloudOps~TV2, claim measured; its check re-run by this seat: CT-COUNT-OK active_internal=21 opal=20 non_opal=1): a re-scan of opal-users-v2, 86 items, 56 PROFILE, 21 active with firm opal-capital; one of them, digest 1af514167abb, is on a domain that is neither of Opal's two nor a reserved test domain; userType null; firm list ABSENT; updatedAt 2026-10-01; no event on any of 27 tickets",
      "infra/aws/lambda/ticket_center/lambda_function.py principal_class (lines 312-330): a caller whose firmId is opal-capital and who is not a service subject is INTERNAL; _profile_scope: an absent firm list is no scope, which reads every firm",
      "infra/aws/opalinvest_dev/lambda/auth-handler/src/auth.ts:106: sign-in admits a row whose status is exactly active (the applier's print); this row's status is active",
      "NOT read by anyone: who created the row and when; whether the person has signed in; what any service other than the ticket service does with it (the sentence about every service that classes by firm id is the CTO's and is inferred beyond the ticket service). By the CTO's word no seat on dell2 changes, disables or probes the row, and no context is constructed for its address"
    ]
  },
  "spec_asserts": "PRD v0.4 C-FENCE and its addenda treat a caller with firm id opal-capital as Opal-internal staff; the CTO's round-8 ruling says an absent firm list means every firm because those rows 'are Opal staff'.",
  "world_is": "20 of the 21 active internal rows are on Opal's own or a reserved domain. One is on an outside company's domain and has the same standing as staff. It may be a contractor seated on purpose; that is not known. The round-9 status release does not move it (active: admitted before and after) and no arm of its proof uses it. A disabled row on a near-identical domain (digest 04fc361f3802) was the round-8 finding and is a different row.",
  "disposition": "UNDER_INVESTIGATION"
}
```


### TCKT_VNEXT-D2-S54 -- an arm row this release's proof depends on was touched 40 minutes before the apply, by nobody the project names

**owner:** `0.7.0_AE_CloudOps~TV2` (filer) | **disarm_owner:** n/a -- the condition it guards was MET; this records that the
guard earned its place, and that a signed sentence about the row is now stale
**class:** PROVENANCE | **found:** 2026-10-12, cell R9-st-3, step 2 of TO-APPLY-R9-st2

**spec_asserts:** the CTO half of R9-st-2 says of the disabled tooling row the S1/S3 arms use (digest `e95c05c7ae90`): *"The
tooling row was last touched hours before round 7 by nobody this project can name; it is re-read, not assumed."* Condition 2
makes that re-read a STOP if the row no longer reads as stated.

**world_is:** the condition is MET -- exactly one PROFILE row, status still `disabled` -- so there was no STOP and the release
proceeded correctly. But the row's `updatedAt` has moved AGAIN, and much more recently than the half says:

| when I read it | `updatedAt` on digest `e95c05c7ae90` |
|---|---|
| R8-ds-1, about 00:0xZ | `2026-10-11T22:41:40.809Z` |
| R9-st-2 step 2, 01:4xZ | **`2026-10-12T01:03:31.142Z`** |

So it was written at **01:03:31Z**, between my own two reads and about **40 minutes before this apply** -- not "hours before
round 7". Its status and `userType` are unchanged across both reads; only the timestamp moved, so whatever touched it did not
change the thing the arm depends on.

**why it matters:** this release's S1 and S3 arms rest on that row reading `disabled` at the moment they run. Something outside
this project is writing to it during the round, and the row carries no attribute that says who or what -- no `disabledAt`, no
audit field (my round-8 read: zero of 56 PROFILE rows carry one). Had the writer flipped `status` instead of touching only the
timestamp, S1 would have refused before the apply and the order's own STOP would have fired -- which is precisely what condition
2 is for, and it is the reason to keep it rather than treat the row as settled. A proof whose fixture moves under it is sound
only for the instant it was taken.

**what I did NOT conclude:** that the write was unauthorised, or that it relates to this project. I measured two timestamps and
the fields that did not change. Who wrote it is not recoverable from the table, and `updatedAt` records a touch of any kind --
including one that set a field to the value it already had.

**the record this corrects:** the CTO half's sentence, not its condition. The condition held and did its job. Recorded so that
the next pair citing that row does not inherit "last touched hours before round 7" as a current fact.

**not established:** what wrote it, whether the other disabled row (`04fc361f3802`, `updatedAt` 2026-07-14) has moved since, or
whether any other row the project's proofs depend on is being written during a round. A sweep of `updatedAt` across the rows
used as fixtures is a different read with a different denominator.

```json
{
 "id": "TCKT_VNEXT-D2-S54",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "1.0.0_SA_CTO~DELL2",
 "surfaced_at": "2026-10-12T21:06:00Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "Row TCKT_VNEXT-D2-S46 is DISARMED by its owner on Andrew's word: the dell agents' lambda:InvokeFunction is NOT narrowed ('Dell boxes should not be curtailed'), so the direct-invoke property is a standing, accepted fact, not a hazard awaiting a fix.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "Andrew-direct ~20:5xZ 2026-10-12, verbatim 'Dell boxes should not be curtailed', record org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261012_205xZ_SITEZ_PORTFOLIO_SEVEN_PROJECT_RULINGS.md @cdb5ff66b1 (site Z's branch; CLOUD at the next integrate)",
   "relay 1.0.0_SA_CTO~Z msg 33515 via 0.0.0_AB_MSTR~DELL2 msg 6554: NFRA_IAMROLES202609 will NOT take D2-S46; round-8 Addendum 1 (the narrowing) is withdrawn",
   "row TCKT_VNEXT-D2-S46 (disarm owner 1.0.0_SA_CTO~DELL2, msg 6001)"
  ]
 },
 "spec_asserts": "Row D2-S46: whether the invoke permission should be narrower is the owner's; the row stayed ARMED until NFRA_IAMROLES202609 narrowed it.",
 "world_is": "The narrowing will not happen, by Andrew's word. A dell agent identity can still invoke a function behind the portal authorizer as any caller. Acts that use this are run as signed read-only pairs (TO-RUN-R6-fn1; IRPT_ANLREQ TO-READS-Y8), as before; no new gate is added. The property stays named so no proof reads a direct-invoke answer as an authorizer answer.",
 "disposition": "UNDER_INVESTIGATION",
 "notes": "Disarms D2-S46 on its owner's read of Andrew's word; nothing measured live by this row."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W41-S1",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~41",
  "surfaced_at": "2026-10-14T19:35:44Z",
  "one_line": "TO-R18-L1 asked that no existing assertion about another type or action change, but three existing assertions treat meeting_request as an untyped type, so each was edited to match the new definition (old and new text in R18_L1_RECORD.json).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ticket_center/tests/test_analysis_request.py@023b5ce5b0 (test_four_existing_types_unchanged loop and test_requester_claims_and_completes_own_ticket types list both include meeting_request, creating it with no answers)",
      "infra/aws/lambda/ticket_center/tests/test_trade_request_type.py@023b5ce5b0 (test_other_untyped_types_unchanged asserts meeting_request questions == [])",
      "infra/aws/lambda/ticket_center/tests/test_authz_matrix.py@023b5ce5b0 (test_layer_coverage asserts 11 actions and a ROUTES list with no meeting route)"
    ]
  },
  "spec_asserts": "TO-R18-L1 step 1: the four existing types keep their exact rows. Step 5: edit an existing test only where a fixture needs the new action or definition; no existing assertion about another type or another action may change.",
  "world_is": "Three existing assertions encode meeting_request as an untyped type with no questions and no answers. The new definition makes them false. Edited: the untyped loop in test_four_existing_types_unchanged and the untyped loop in test_other_untyped_types_unchanged drop meeting_request; the self-claim types loop keeps meeting_request and supplies its required answers; test_layer_coverage goes from 11 to 12 actions with one ROUTES entry. Every edited assertion is about meeting_request, the type this order changes; no assertion about another type or action changed.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W41-S2",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~41",
  "surfaced_at": "2026-10-14T19:35:44Z",
  "one_line": "The order's refusal order (non-coordinator 403 before not-found 404) conflicts with its own AC3J requirement that a refusal reveal nothing about tickets outside the caller's scope; the handler applies scope and existence first, then the coordinator test.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ticket_center/lambda_function.py@023b5ce5b0 (_new_item copies ROUTING_MATRIX into the item's routing.primary, so the coordinator is readable only after the ticket is read)",
      "infra/aws/lambda/ticket_center/lambda_function.py@023b5ce5b0 (get_ticket answers 404 for a ticket outside the caller's profile scope, the refusal this order names as the one to match)"
    ]
  },
  "spec_asserts": "TO-R18-L1 step 2 lists the rules in order: not INTERNAL 403; caller not in routing.primary 403 naming no one; ticket not found or outside scope 404. AC3J: a refusal reveals nothing about tickets outside the caller's scope.",
  "world_is": "routing.primary sits on the ticket, so the coordinator test cannot run before the ticket is read. A literal 403-first order would answer 403 for an existing out-of-scope ticket and 404 for a missing one, which reveals existence across scope. Implemented: read; missing or out of firm scope gives the get_ticket 404; then the coordinator test gives 403; then type 409, completed 409, body 400, time 400, one conditional write.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W41-S3",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~41",
  "surfaced_at": "2026-10-14T19:35:44Z",
  "one_line": "The order asks that no notify_* run on any path, but CREATE of every ticket type already calls notify_dl_isolated (the W-E first-line DL send), so a meeting filing sends it; the outcome route sends nothing.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ticket_center/lambda_function.py@023b5ce5b0 (create_ticket calls notify_dl_isolated(item) unconditionally before the 201)",
      "infra/aws/lambda/ticket_center/tests/test_meeting_request.py (test_create_keeps_the_existing_dl_first_line_and_sends_no_client_notice pins the create-time call; the outcome tests assert the spy list is empty)"
    ]
  },
  "spec_asserts": "TO-R18-L1 step 4: no notify_* function is called on any path (a spy). AC3J: no mail or notice is sent.",
  "world_is": "The 'any path' reading would forbid the existing CREATE-time DL line that W-E attaches to every ticket create. Implemented: confirm, propose and every refusal of the outcome route call no notifier; the filing keeps the existing DL line, which the spy test pins. Whether a filing keeps that line is the issuer's call.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W41-S4",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~41",
  "surfaced_at": "2026-10-14T19:35:44Z",
  "one_line": "The before-arm expected every case of the new file to fail on the base handler; 31 of 33 failed and two controls passed: test_other_untyped_types_keep_their_shape (unchanged service_request behaviour) and test_create_keeps_the_existing_dl_first_line_and_sends_no_client_notice (the existing CREATE-time DL line).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "run of the new test file against the base lambda_function.py at 023b5ce5b0 (git archive HEAD into .scratch/base_arm): 31 failed, 2 passed (the passing cases are test_other_untyped_types_keep_their_shape and test_create_keeps_the_existing_dl_first_line_and_sends_no_client_notice)"
    ]
  },
  "spec_asserts": "TO-R18-L1 step 6: the before-arm, the new tests run on the base, every case FAILS.",
  "world_is": "Two controls pass on the base by construction: one on an unchanged type and one on the existing CREATE-time DL line. They cannot fail there. They were kept as regression guards, not rewritten to fail. Recorded as the before-arm result.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W41-S5",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~41",
  "surfaced_at": "2026-10-14T19:35:44Z",
  "one_line": "Decomposition row R18-mt-1 says the outcome route refuses a non-assignee, but the wire contract and the order gate it on routing.primary (the coordinator); the handler follows the order and the wire contract.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R18.md@023b5ce5b0 (row R18-mt-1 reads 'refused for a non-assignee')",
      "org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R18.md@023b5ce5b0 (WIRE CONTRACT item 1: caller is an INTERNAL human whose email is in routing.primary)"
    ]
  },
  "spec_asserts": "TO-R18-L1 step 2 and the WIRE CONTRACT item 1: the caller must be an INTERNAL human whose email is in the ticket's routing.primary (the coordinator); anyone else 403.",
  "world_is": "The decomposition row's 'non-assignee' wording differs from the contract. claim_ticket sets the assignee to whoever claims, so the assignee is not the coordinator unless that person claims. Implemented the routing.primary rule as the order and the wire contract state.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W41-S6",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~41",
  "surfaced_at": "2026-10-14T19:37:23Z",
  "one_line": "Running tests/test_authz_matrix.py by path reaches the real SES notifier: my by-path run printed one WE_CLIENT_SENT kind=pickup line with a real SES message_id from tickets@opalinvest.dev, a live send the worker bound forbids.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~V2 (issuer of TCKT_VNEXT round 18; owns test_authz_matrix.py). Until disarmed, no run of that file by path (python <file>) -- pytest only, where conftest.py's guard applies.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ticket_center/lambda_function.py@023b5ce5b0 line 1121 (notify_client calls _ses_client().send_raw_email(Source=EMAIL_FROM, ...) with no guard of its own)",
      "infra/aws/lambda/ticket_center/tests/test_authz_matrix.py@023b5ce5b0 lines 342-343 (__main__ runs unittest.main with no notifier stub; MatrixTests claim tickets, which reaches notify_client_isolated)",
      "infra/aws/lambda/ticket_center/tests/conftest.py@023b5ce5b0 (the SES guard is an autouse pytest fixture; it does not apply to a by-path run)",
      "worker run at 2026-10-14T19:3xZ: python infra/aws/lambda/ticket_center/tests/test_authz_matrix.py printed WE_CLIENT_SENT kind=pickup ticket=TCK-20261014-8279bd23 with a real SES message_id; the pytest runs of the same folder printed no such line"
    ]
  },
  "spec_asserts": "Worker face, TO-R18-L1: no live call of any kind -- no AWS, no network, no mail, no deploy, no apply; tests/conftest.py refuses a real call.",
  "world_is": "The file's own __main__ run is not guarded, because the conftest guard exists only under pytest. Its claim tests reach the unstubbed notifier, which sends through SES from the pinned sender. The hazard is in the base file too; the R18-L1 edit changed only an action count and one ROUTES entry. Not re-run after the send was seen; the ticket and recipient owner must check whether the message was delivered.",
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W41-S7",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~41",
  "surfaced_at": "2026-10-14T19:57:22Z",
  "one_line": "A firm id with a dot is a valid trade_request firm answer but is refused as a plain id for the trade form attachment, so such a ticket can exist with no attachment route.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ticket_center/lambda_function.py@ef5871585d (_FIRM_ID_RE admits dots and the firm kind is validated with it; _validate_answers accepts the firm answer)",
      "infra/aws/lambda/ticket_center/lambda_function.py, worktree wk-TCKT_VNEXT-41 at filing (uncommitted L2 edit): _PLAIN_FIRM_RE = letters, digits, dash, underscore, applied before a firm is formatted into a bucket or key; _validate_trade_form refuses a dotted firm 400)",
      "org/missions/D7/TCKT/TCKT_VNEXT/task-orders/TCKT_VNEXT.TO-R18-L2.trade-request-form-upload-and-open-routes.md@7a663e8c28 (step 2: the firm value is checked to be a plain id of letters, digits, dash and underscore before it is formatted in)"
    ]
  },
  "spec_asserts": "TO-R18-L2 step 2 requires the firm to be a plain id (letters, digits, dash, underscore) before it is formatted into the key template, and step 2 requires CREATE to store the reference for a valid trade_request.",
  "world_is": "The firm kind admits a dotted id as a valid answer, so a trade_request with a dotted firm passes the answers check but its attachment is refused 400 (the firm is not a plain id). The contract does not say which of the two wins for a dotted id; the implementation refuses the attachment. No firm id in the present estate has a dot (the ids seen are plain).",
  "disposition": "UNDER_INVESTIGATION"
}
```

### TCKT_VNEXT-D2-W42-S1 -- the candidate is cut from DEV, while CONTRIBUTING-BOXES says cut from PROD and re-cut before registration

```json
{
  "id": "TCKT_VNEXT-D2-W42-S1",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~42",
  "surfaced_at": "2026-10-14T19:45:44Z",
  "one_line": "The order cuts the candidate from origin/DEV 9e637fe51e, but portal/CONTRIBUTING-BOXES.md says to cut from the last PROD release and to re-cut a DEV-cut branch onto PROD before it is registered.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~V2 (registers cand/dell2/tckt-meeting-request with open-calls.py; re-cuts it onto origin/PROD first, per CONTRIBUTING-BOXES step 2)",
  "spec_asserts": "WORKER FACE step 1: base_tip is the portal worktree HEAD at origin/DEV 9e637fe51ebfa6322910cc032945a1e755e9ea13, and the candidate branch is cut from it.",
  "world_is": "CONTRIBUTING-BOXES.md at 9e637fe51e says a feature branch is cut from the last PROD release, never from DEV. Live reads at 2026-10-14T19:45Z: origin/PROD = 5ab67a651a626e7224de0a2cf03a2223f99dc15e and origin/DEV = 9de7c7e3227c321d45c2b6d3d3ccf72590b20710. An earlier read in this session gave origin/PROD = fa10e75861, so PROD moved in between. The base 9e637fe51e is an ancestor of origin/DEV (5 commits behind) and not of origin/PROD. The candidate 9e07fa320c is committed on the order's base and was NOT re-cut. The branch is LOCAL and unpushed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/CONTRIBUTING-BOXES.md@9e637fe51ebfa6322910cc032945a1e755e9ea13 lines 15-21 (Build steps 1 and 2)",
      "git -C portal ls-remote origin refs/heads/PROD -> 5ab67a651a626e7224de0a2cf03a2223f99dc15e (measured 2026-10-14T19:45Z)",
      "git -C portal ls-remote origin refs/heads/DEV -> 9de7c7e3227c321d45c2b6d3d3ccf72590b20710 (measured 2026-10-14T19:45Z)",
      "portal commit 9e07fa320cf55945e3ab1d391ce7716e7daac9d4 on wk-TCKT_VNEXT-42-portal, parent 9e637fe51ebfa6322910cc032945a1e755e9ea13"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The order fixes the base, so this row does not re-cut it. Registration is the issuer's act."
}
```

### TCKT_VNEXT-D2-W42-S2 -- the order's line numbers for TicketCenter.tsx point at other code

```json
{
  "id": "TCKT_VNEXT-D2-W42-S2",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~42",
  "surfaced_at": "2026-10-14T19:45:44Z",
  "one_line": "The order's line ranges for src/pages/TicketCenter/TicketCenter.tsx do not hold the code it names: the showCreate panel is at 668-735, not 458-521; handleCreate at 484-506, not 383; the board rows at 803-853, not 589-637.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "WORKER FACE step 2 (read first): the showCreate panel about lines 458-521, handleCreate about 383 and the board rows about 589-637 of TicketCenter.tsx.",
  "world_is": "At base 9e637fe51e the file has 891 lines. The create panel is at 668-735, handleCreate at 484-506, and the board rows at 803-853. The cited ranges hold other code. The cell's content was found by reading the file, not by the numbers, and no edit depended on them.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/pages/TicketCenter/TicketCenter.tsx@9e637fe51ebfa6322910cc032945a1e755e9ea13 (891 lines; showCreate panel at 668-735; handleCreate at 484-506; board rows at 803-853)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Stale citation only. Nothing measured live by this row."
}
```

### TCKT_VNEXT-D2-W42-S3 -- the trade branch of the create panel cannot be reached through the page's type list

```json
{
  "id": "TCKT_VNEXT-D2-W42-S3",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~42",
  "surfaced_at": "2026-10-14T19:45:44Z",
  "one_line": "The create panel's type list filters trade_request out (Andrew-direct 2026-10-13), so the order's per-branch test of the trade branch cannot be run through the mounted page.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "WORKER FACE step 3: the trade, analysis, service and other branches of the create panel render as before, a test per branch.",
  "world_is": "TicketCenter.tsx at 9e637fe51e lines 681-685 build the type select from TICKET_TYPE_LABELS with the trade_request entry filtered out, so no UI path selects trade. The candidate's test covers the trade branch only at the decision level (drawsOwnForm('trade_request') is true). The analysis, service and other branches are mounted and tested.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/pages/TicketCenter/TicketCenter.tsx@9e637fe51ebfa6322910cc032945a1e755e9ea13 lines 681-685 (the filter and the Andrew-direct comment)",
      "portal/src/pages/TicketCenter/__tests__/meeting-request.test.tsx (candidate 9e07fa320c): test 'the trade branch is decided the same way, and trade is still not offered in the type list'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The trade branch's render is unchanged in code. It is not mounted by any test."
}
```

### TCKT_VNEXT-D2-W42-S4 -- the scope rule and the cell's hiding rule force the trade-named gating lines to change

```json
{
  "id": "TCKT_VNEXT-D2-W42-S4",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~42",
  "surfaced_at": "2026-10-14T19:45:44Z",
  "one_line": "The cell hides the generic title, details and Create controls for meeting_request, and AC3 bans added TicketCenter.tsx lines that name trade_request. The three trade-named gating conditions at base lines 687, 725 and 726 were therefore replaced through drawsOwnForm() in MeetingRequestParts.tsx.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~V2 (orders TO-R18-P2 after P1 and decides the merge of TicketCenter.tsx lines 687, 725, 726 and the import line)",
  "spec_asserts": "WORKER FACE step 2: touch no other branch of TicketCenter.tsx, and TradeRequestParts.tsx and the trade branch are TO-R18-P2's. AC3: no added TicketCenter.tsx line mentions trade_request, TradeRequestForm or analysis_request.",
  "world_is": "The three conditions read newType !== 'trade_request' at base. The candidate writes !drawsOwnForm(newType), which is true for trade_request and meeting_request, so the trade gating behaviour is unchanged. The trade branch of the ternary is not edited. The meeting branch is inserted before the analysis branch line. TO-R18-P2 edits the same file and may conflict on these three lines and on the import line.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/pages/TicketCenter/TicketCenter.tsx@9e637fe51ebfa6322910cc032945a1e755e9ea13 lines 687, 725, 726 (the three trade-named gating conditions)",
      "portal commit 9e07fa320cf55945e3ab1d391ce7716e7daac9d4, file TicketCenter.tsx: 20 added lines, none naming trade_request, TradeRequestForm or analysis_request (scope_check_mt3.py: SCOPE-OK)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Behaviour preserved, text changed. The P2 merge is the place it can bite."
}
```

### TCKT_VNEXT-D2-W42-S5 -- the trade members went on a sibling type, not on TicketAttachment

```json
{
  "id": "TCKT_VNEXT-D2-W42-S5",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~42",
  "surfaced_at": "2026-10-14T20:04:07Z",
  "one_line": "The order says TicketAttachment gains the trade form's member set, but the analysis code reads its upload_id and input_id as required strings, so the trade members went on a sibling type joined by a union.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "WORKER FACE step 2: src/api/endpoints/tickets.ts, TicketAttachment gains the trade form's member set (key, filename, content_type, size).",
  "world_is": "TicketAttachment at portal commit 9e07fa320c has upload_id: string and input_id: string as required members, and analysisRequest.ts reads ticket.attachment?.input_id as a string (lines 305, 431, 479, 527). Adding the trade members to that interface makes the analysis shape claim members it never has. The candidate (b032bcf793) adds TradeFormAttachment, with key, filename, content_type and size, and declares upload_id and input_id as absent (undefined) on it. Ticket.attachment and CreateTicketInput.attachment take the union, and the analysis reads still type-check.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/api/endpoints/tickets.ts@9e07fa320cf55945e3ab1d391ce7716e7daac9d4 (TicketAttachment: upload_id and input_id required)",
      "portal/src/pages/TicketCenter/analysisRequest.ts@9e07fa320cf55945e3ab1d391ce7716e7daac9d4 lines 305, 431, 479, 527 (ticket.attachment?.input_id read as a string)",
      "portal commit b032bcf79311528ecf7999d5d55f4b84e9059c00 (TradeFormAttachment sibling; typecheck rc=0)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The order's sentence is read as the member set, not as a widening of the analysis interface. The CVO may rule the shape differently."
}
```

```json
{
 "id": "TCKT_VNEXT-D2-W43-S1",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_TCKT_VNEXT~43",
 "surfaced_at": "2026-10-14T19:27:46Z",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "disarm_owner": "2.0.0_SA_COO~V2",
 "one_line": "TO-R18-TR1 cannot name one bucket: doctrine tier state (R21) homes the ticket attachment per firm, so the three served firms resolve to three buckets and the ticket Lambda's single TICKET_ATTACH_BUCKET cannot serve the address. The order's BLOCKING branch applies; no address, key template or checker is written.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D7/TCKT/TCKT_VNEXT/task-orders/TCKT_VNEXT.TO-R18-TR1.ticket-attachment-address-from-the-naming-builder.md:33-44 (cell R18-tf-1: per-firm bucket is a BLOCKING stop; the Lambda uses ONE bucket)",
   "infra/logic/02_DOCTRINE.md:588-597 (R21: per-request intake, keyed by request, is state, never inside a tier plane; state lives in the bucket whose tenancy it belongs to)",
   "infra/logic/02_DOCTRINE.md:360-365 (R4: opal-data-assets is for client/partner custodial information) and :439-441 (R9: bronze is raw, untouched vendor bytes) -- bronze is not the class of a per-request ticket upload",
   "infra/logic/registry/tiers.json homes.FIRM.state = {home: scope, rule: R21} -- scope bucket per firm",
   "lib/opal_naming.py address() in worktree HEAD ba9347065b, run by this worker on 2026-10-14 after 19:27Z: state 49financial -> s3://opal-data-49financial/portal/49financial/state/ticket-attachments/trade-form ; state inflection -> s3://opal-data-inflection/portal/inflection/state/ticket-attachments/trade-form ; state cottonwood -> s3://opal-data-cottonwood/portal/cottonwood/state/ticket-attachments/trade-form",
   "same probe at tier bronze -> s3://opal-data-assets/portal/<firm>/bronze/ticket-attachments/trade-form for all three firms (one bucket, reached by choosing bronze; rejected as the convenience choice the cell forbids)"
  ]
 },
 "spec_asserts": "TO-R18-TR1 step 1: decide the tier by the doctrine, not by convenience; the ticket Lambda uses ONE bucket for every firm, so the tier must resolve to the same bucket for all three served firms; if the doctrine tier resolves to a bucket per firm, STOP, file a BLOCKING row naming the tier, the three buckets and the rule, and do nothing else.",
 "world_is": "The doctrine tier for a non-holdings ticket attachment is state (R21, per-request intake keyed by request; the attachment is keyed by the ticket). state homes per firm (tiers.json FIRM.state, scope). The three buckets are opal-data-49financial, opal-data-inflection and opal-data-cottonwood. Under the order's own branch no address, key_template, ATTACH_ADDRESS.json, address_check.py or mutant_check.py is written, and TO-R18-TR2 and TO-R18-TR3 cannot take a single TICKET_ATTACH_BUCKET from this order as written.",
 "disposition": "UNDER_INVESTIGATION",
 "notes": "ARMED because TO-R18-TR3 writes the Lambda environment from the file this order would produce; left alone, TR3 either carries a hand-typed bucket or a wrong single bucket. Disarm owner is the issuer, who must re-cut the attachment design (one bucket by a new registry decision, or a per-firm env) or confirm the tier. Nothing created in AWS; no registry row added (the builder did not refuse; the blocker is the tier, not a missing row). Not a decision on which tier is right; the rule text is quoted at the cited lines for the CTO or CVO to read."
}
```

```json
{
 "id": "TCKT_VNEXT-D2-W43-S2",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_TCKT_VNEXT~43",
 "surfaced_at": "2026-10-14T19:57:06Z",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "disarm_owner": "2.0.0_SA_COO~V2",
 "one_line": "TO-R18-TR3 cannot be committed as written: the naming gate refuses the attachment key template because the table segment ticket-attachments is not snake_case (NAMING_SCHEMA key.table_case), though address() printed it without refusal; the issuer must decide the table name in TO-R18-TR1.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "python .tools/naming-gate.py (safe-commit of the TR3 source staged on top of a8a40f308b, ENFORCE): NAMING REFUSE infra/aws/terraform/ticket-center/main.tf:321 portal/{firm}/state/ticket-attachments/trade-form/ -> portal/{firm}/state/ticket_attachments/trade-form/ (NEW and OUT-OF-PATTERN as S3Key); commit aborted, log at .scratch/tr3_commit.log in the worktree",
   "org/standards/NAMING_SCHEMA.json key.table_case (line 49 of the file, @worktree HEAD 2e0b4b59f8 and later): snake_case; kebab-case binds only NEW served platinum leaves (.json)",
   "lib/opal_naming.py address(portal, 49financial, state, ticket-attachments, trade-form) returned s3://opal-data-49financial/portal/49financial/state/ticket-attachments/trade-form with no refusal (TO-R18-TR1 ATTACH_ADDRESS.json, commit 2e0b4b59f8)",
   "same gate run also REFUSES: line 223 IAM policy name opal-ticket-attachments-trade-form (owed suffix -policy), lines 232-234 the three firm ARN literals (hand-kept carriers outside the lookup() context)"
  ]
 },
 "spec_asserts": "TO-R18-TR1 step 4 and TO-R18-TR3 steps 2 and 3: the key template is builder output copied as a literal (rule 30, every S3 address is lib/opal_naming.py address() output), and the permission names one ARN per firm from that record.",
 "world_is": "The builder printed a table segment (ticket-attachments) that NAMING_SCHEMA key.table_case does not admit (snake_case), and it did not refuse it. The commit-time naming gate grades the key canonically and refuses the template and the three ARNs built on it. TR3 source cannot land as the cell is written. Its fix is a table-name decision (re-run address() with a snake_case table, which changes ATTACH_ADDRESS.json and every template), owned by the issuer, not a hand-typed workaround.",
 "disposition": "UNDER_INVESTIGATION",
 "notes": "Filed by the worker on TO-R18-TR3 (AMENDMENT 1 record). The order is left pending and its source is NOT committed: the working-tree edits to infra/aws/terraform/ticket-center/main.tf, the TR3 checkers, R18_TR3_RECORD.json and the instance are uncommitted in the worktree. No bypass of the naming gate was attempted. The TR2 meeting change and the TR1 record are unaffected."
}
```
```json
{
 "id": "TCKT_VNEXT-D2-W48-S1",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_TCKT_VNEXT~48",
 "surfaced_at": "2026-10-16T01:39:13Z",
 "one_line": "TO-R19-TR cannot start: infra/aws/terraform/ticket-center/main.tf is tracked at HEAD but excluded from this worktree by sparse-checkout (index skip-worktree flag S, not on disk).",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "spec_asserts": "TO-R19-TR (WORKER FACE, BOUNDS and the paths block): the worktree C:/dev/wk-tckt-vnext-48 carries org/ and .tools/ and the grant path infra/aws/terraform/ticket-center/main.tf, which the cell edits in place and the checkers read.",
 "world_is": "The path is tracked at HEAD b84a2ca293 (blob 17298d3fb7d9d45a10873e6fdd2d90592ed5affa, 28387 bytes) but the worktree sparse-checkout cone omits infra/aws, so the file is not on disk and its index entry carries the skip-worktree flag. The worktree therefore cannot carry the granted path. The worker did not widen the sparse-checkout, reconstruct the file or write the checkers, and stopped per the order. The sibling worktree C:/dev/wk-tckt-vnext-47 materialises the same path, so the gap is per-worktree provisioning.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "git -C C:/dev/wk-tckt-vnext-48 ls-files -v infra/aws/terraform/ticket-center/main.tf prints 'S infra/aws/terraform/ticket-center/main.tf'; ls -la infra/aws returns No such file or directory (read at HEAD b84a2ca293, 2026-10-16T01:39Z)",
   "git -C C:/dev/wk-tckt-vnext-48 config --get core.sparseCheckout = true; git sparse-checkout list = .tools, infra/logic/registry, lib, org/devices, org/missions/D7/TCKT/TCKT_VNEXT (no infra/aws entry)",
   "git cat-file -s HEAD:infra/aws/terraform/ticket-center/main.tf = 28387 bytes: the file is tracked at HEAD b84a2ca293, so the absence is a worktree materialisation gap, not a missing file",
   "positive control: git -C C:/dev/wk-tckt-vnext-47 ls-files infra/aws/terraform/ticket-center/main.tf lists the path (sibling worktree, read only, not edited)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "notes": "Filed by 0.9.0_WK_TCKT_VNEXT~48 on TCKT_VNEXT.TO-R19-TR. BLOCKING: the order stays pending; no source edit, no deliverable instance, no checker scripts, no R19_TR_RECORD.json, status not flipped. The issuer or the provisioner decides whether the worktree sparse set is widened; the worker does not widen it. Hazard INERT: nothing is planned, applied or deployed by this stop."
}
```
```json
{
 "id": "TCKT_VNEXT-D2-W46-S1",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_TCKT_VNEXT~46",
 "surfaced_at": "2026-10-16T01:42:24Z",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "one_line": "TO-R19-L2 cannot start: the worktree carries org/ and .tools/ but not infra/aws, because its sparse-checkout cone omits infra/. The order's source and tests (infra/aws/lambda/ticket_center/) are absent on disk, so no cell is built and no acceptance criterion runs.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "C:/dev/wk-tckt-vnext-46 @HEAD b84a2ca293: git config core.sparseCheckout = true; git sparse-checkout list = .tools, infra/logic/registry, lib, org/devices, org/missions/D7/TCKT/TCKT_VNEXT, org/modules/graph, org/ref, org/standards (infra/aws is not in the cone)",
   "C:/dev/wk-tckt-vnext-46 @HEAD b84a2ca293: ls infra shows README.md, launch_agents_powershell.ps1, logic/ only; ls infra/aws -> No such file or directory",
   "git ls-tree HEAD -- infra/aws/lambda/ticket_center @b84a2ca293 lists lambda_function.py and tests/ (conftest.py, test_list_scoped_firm.py and others): the path exists in the commit and is excluded from the checkout; git ls-files -- infra/aws = 9277 entries; git ls-files -v -- infra: 9503 skip-worktree (S) and 34 index (H)"
  ]
 },
 "spec_asserts": "TO.TO-R19-L2 WORKER FACE and <paths>: the worktree carries infra/aws/lambda/ticket_center/lambda_function.py and infra/aws/lambda/ticket_center/tests/ as the write grant, and the cell is built and tested there (TREE-OK check: org/ and .tools/ present).",
 "world_is": "The worktree carries org/ and .tools/ but not infra/aws. The granted source and tests are not materialised in the worktree, so the cell cannot be built, the new test file cannot be written in place, and mutant_check.py has no lambda_function.py to copy. Per the order's BLOCKING rule the tree was not rebuilt, extracted or reconstructed and the sparse cone was not widened. No source or test was changed. R19L2-AC1 and R19L2-AC2 are recorded FAIL (not run); R19L2-AC3J is a judgment row.",
 "disposition": "UNDER_INVESTIGATION",
 "notes": "The order stays pending and is not flipped. Disarm is not needed (INERT). The fix is the issuer's or integrator's: widen this worktree's sparse cone to infra/aws/lambda/ticket_center, or re-provision the worktree from a checkout that carries it. Filed by the worker under the BLOCKING stop rule of its WORKER FACE."
}
```
```json
{
 "id": "TCKT_VNEXT-D2-W46-S2",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_TCKT_VNEXT~46",
 "surfaced_at": "2026-10-16T02:16:30Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "The whole-folder pytest run of infra/aws/lambda/ticket_center/tests/ cannot collect 8 modules: test_package_route.py reads org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json at import, and that file is tracked at HEAD but outside this worktree's sparse cone (org/missions/D9 is not in it).",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "C:/dev/wk-tckt-vnext-46 @HEAD 8957fed16b: git ls-tree HEAD -- org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json lists the file (1 entry); the file is absent from the worktree (test -f returns no)",
   "C:/dev/wk-tckt-vnext-46 @HEAD 8957fed16b: infra/aws/lambda/ticket_center/tests/test_package_route.py lines 37-41 open the I7 sample at import and raise FileNotFoundError; test_no_row_refuses.py, test_package_409_codes.py, test_package_env_firms.py, test_package_i5p_i7.py, test_package_principal.py, test_package_request_id.py, test_status_active.py load that module through _load",
   "run: timeout 120 python -m pytest C:/dev/wk-tckt-vnext-46/infra/aws/lambda/ticket_center/tests/ -q -p no:cacheprovider --color=no --continue-on-collection-errors -> 312 passed, 8 errors, 42 subtests passed, rc=1"
  ]
 },
 "spec_asserts": "TO-R19-L2 step 6 and R19L2-AC1: run the whole infra/aws/lambda/ticket_center/tests/ folder once and record the counts in the record (a drain check).",
 "world_is": "The whole-folder run measures 312 passed and 8 collection errors. The 8 modules named in the evidence are not measured in this worktree, because their import fails before any test runs. None of the 8 modules, and not test_package_route.py, is edited by this order; the cause is the sparse cone, not the change.",
 "disposition": "UNDER_INVESTIGATION",
 "notes": "Not a blocker for AC1 (the new file passes 7 of 7; the order's check is the new file plus the folder count). The fix belongs to the integrator or issuer: widen this worktree's sparse cone to org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/ or have the drain run the folder where that file is materialised. The worker did not widen the cone, did not extract the file, and did not edit the 8 modules."
}
```
```json
{
 "id": "TCKT_VNEXT-D2-W46-S3",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_TCKT_VNEXT~46",
 "surfaced_at": "2026-10-16T02:16:30Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "The before-arm of the new test file (its 7 cases run against the HEAD copy of lambda_function.py) gives 6 failed and 1 passed, not 7 failed: test_an_internal_caller_is_unchanged_by_the_set passes on the base because it is the INTERNAL non-regression guard.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "scratch arm: git show HEAD:infra/aws/lambda/ticket_center/lambda_function.py written to C:/dev/wk-tckt-vnext-46/.scratch/base_arm/ticket_center/ with a copy of tests/; timeout 120 python -m pytest C:/dev/wk-tckt-vnext-46/.scratch/base_arm/ticket_center/tests/test_analyst_intake_scoped.py -q -p no:cacheprovider --color=no -rA -> 6 failed, 1 passed in 0.87s, rc=1",
   "PASSED test_an_internal_caller_is_unchanged_by_the_set; FAILED test_intake_lists_only_the_tickets_of_the_configured_firms, test_an_unset_or_empty_configuration_lists_nothing_with_status_200, test_all_is_never_a_wildcard_for_the_intake_list, test_a_ticket_with_no_requester_firm_is_dropped, test_status_assignee_and_ticket_type_filters_still_work_inside_the_set, test_the_response_carries_cutoff_et_and_a_count_equal_to_the_list_length"
  ]
 },
 "spec_asserts": "TO-R19-L2 step 6 record: the before-arm (the new tests on the base: every case FAILS).",
 "world_is": "On the base, 6 of 7 cases FAIL and the INTERNAL-unchanged case PASSES. That case asserts that an INTERNAL caller still sees all 8 tickets, which holds before and after the change. It is kept as the non-regression guard step 4 names and is not re-pinned.",
 "disposition": "UNDER_INVESTIGATION",
 "notes": "The mutant arm is consistent with this: the firm filter removed gives 6 failed and 1 passed (MUTANT-FIRES). Nothing in the product changed for this row; the expectation in the order's before-arm sentence is what differs from the world."
}
```
```json
{
 "id": "TCKT_VNEXT-D2-W45-S1",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_TCKT_VNEXT~45",
 "surfaced_at": "2026-10-16T01:45:08Z",
 "one_line": "TO-R19-L1 names infra/aws/lambda/ticket_center/ (lambda_function.py and tests/) in its paths and cell, but this worktree is a sparse checkout whose cone excludes infra/aws: the files exist at HEAD b84a2ca293 and are not on disk, so the cell cannot be built or its criteria run here.",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "C:/dev/wk-tckt-vnext-45: git config core.sparseCheckout = true; git sparse-checkout list = .tools, infra/logic/registry, lib, org/devices, org/missions/D7/TCKT/TCKT_VNEXT, org/modules/graph, org/ref, org/standards (no infra/aws) @ HEAD b84a2ca293",
   "git ls-files -v infra/aws | grep -c ^S = 9277 and git ls-files infra/aws = 9277: every infra/aws index entry carries skip-worktree; ls infra/aws = No such file or directory",
   "git cat-file -e HEAD:infra/aws/lambda/ticket_center/lambda_function.py rc=0 (present in the commit); git show HEAD:infra/aws/lambda/ticket_center/lambda_function.py defines _client_recipients at line 1182, _recipient_digest 1195, notify_client 1204, notify_client_isolated 1225, and the body requester_email at 1373",
   "positive control: git cat-file -e HEAD:org/missions/D7/TCKT/TCKT_VNEXT/task-orders/TCKT_VNEXT.TO-R19-L1.client-notice-recipient-derived-from-the-firms-contacts.md rc=0, and that order file is on disk in this worktree",
   "python -m pytest C:/dev/wk-tckt-vnext-45/infra/aws/lambda/ticket_center/tests/test_notice_recipient_firm.py -q -p no:cacheprovider rc=4 'file or directory not found'; python C:/dev/wk-tckt-vnext-45/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~45/mutant_check.py rc=2 'No such file or directory'"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "The worktree carries every path the task order names in its <paths> grant (infra/aws/lambda/ticket_center/lambda_function.py and infra/aws/lambda/ticket_center/tests/), so the cell can be built in it and its acceptance criteria run in it.",
 "world_is": "The worktree materialises only the sparse cone listed in the evidence; infra/aws is excluded by skip-worktree on all 9277 entries, so the named paths exist in HEAD and not on disk. The worker did not change the sparse-checkout, copy files from another checkout or reconstruct the tree; no product path was edited.",
 "notes": "Provisioning owner: the issuer 2.0.0_SA_COO~V2 (the worktree is issuer-provisioned). Not checked: whether sibling worktrees -46, -47 and -48 share the cone (no census run). The order stays pending; the proof instance records AC1 and AC2 as FAIL and AC3J as UNVERIFIABLE-BY-INSTRUMENT."
}
```
```json
{
 "id": "TCKT_VNEXT-D2-W45-S2",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_TCKT_VNEXT~45",
 "surfaced_at": "2026-10-16T02:26:23Z",
 "one_line": "The drain-check run of infra/aws/lambda/ticket_center/tests/ cannot collect 8 test modules in this worktree: they read org/missions/D9 deliverables, which the sparse cone does not materialise. The same 8 fail at the base commit and after the build.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "timeout 120 python -m pytest C:/dev/wk-tckt-vnext-45/infra/aws/lambda/ticket_center/tests/ -q -p no:cacheprovider --color=no : 8 errors during collection (test_no_row_refuses, test_package_409_codes, test_package_env_firms, test_package_i5p_i7, test_package_principal, test_package_request_id, test_package_route, test_status_active), each FileNotFoundError on org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json; the run is interrupted (rc=2) without --continue-on-collection-errors",
   "same folder with --continue-on-collection-errors at base b569143371: 305 passed, 8 errors (rc=1); at 8398ba291b and f388d5ea4a: 321 passed, 8 errors (rc=1); the 16 new cases account for the difference",
   "git sparse-checkout list at HEAD f388d5ea4a: .tools, infra/aws/lambda/ticket_center, infra/logic/registry, lib, org/devices, org/missions/D7/TCKT/TCKT_VNEXT, org/modules/graph, org/ref, org/standards (no org/missions/D9)"
  ]
 },
 "spec_asserts": "TO-R19-L1 ACCEPTANCE R19L1-AC1: run the whole infra/aws/lambda/ticket_center/tests/ folder once and record the counts in the record (a drain check the issuer re-runs).",
 "world_is": "The folder cannot be collected in full in this worktree: 8 modules name files under org/missions/D9, which the sparse cone excludes, so collection fails before any test runs. The failure is pre-existing and is not caused by the build. The counts recorded under the continue-on-collection-errors flag are 305 passed at base and 321 passed after the build, with the same 8 errors.",
 "disposition": "UNDER_INVESTIGATION",
 "notes": "Filed by 0.9.0_WK_TCKT_VNEXT~45 on TO-R19-L1. Not fixed: the sparse cone and the D9 files belong to the issuer. The drain re-run should use a worktree whose cone includes org/missions/D9, or accept the 8 collection errors as known."
}
```
```json
{
 "id": "TCKT_VNEXT-D2-W45-S3",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_TCKT_VNEXT~45",
 "surfaced_at": "2026-10-16T02:26:23Z",
 "one_line": "The cell's rule (a blank stored requester goes to the firm's first contact) contradicts one existing assertion in test_client_mail_digest.py, which asserts that a blank requester refuses. The worker kept the assertion by giving that single test an empty map.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "base b569143371 infra/aws/lambda/ticket_center/tests/test_client_mail_digest.py lines 67-76: test_send_failed_digest_is_none_when_the_recipient_did_not_resolve sets requester email to empty and asserts WE_CLIENT_NOT_SINGULAR in the output",
   "TO-R19-L1 step 2 (cell text): else return [contacts[0]] and log WE_CLIENT_RECIPIENT_IGNORED; a blank stored address is not a contact, so it takes this branch",
   "at 8398ba291b the same test sets os.environ CLIENT_NOTICE_CONTACT_MAP to {} before the send; its assertions are byte-identical to base (one line added)"
  ]
 },
 "spec_asserts": "TO-R19-L1 step 5: an existing test is edited ONLY where a fixture assumed the requester's own address receives the notice with no map set; no existing assertion about another behaviour may change.",
 "world_is": "A blank stored requester is refused at base but, under the cell's rule, sends to the firm's first contact whenever a contact is configured. The existing test asserts the base refusal. To keep that assertion unchanged the worker configured zero contacts for that one test. The blank-to-first-contact behaviour is now a named case in test_notice_recipient_firm.py.",
 "disposition": "UNDER_INVESTIGATION",
 "notes": "Raised for the CTO or CVO at L9: confirm that a blank stored requester should reach the firm's first contact (the rule as written) and not be refused. The worker did not change the rule. The fixture edit is recorded in R19_L1_RECORD.json."
}
```
```json
{
 "id": "TCKT_VNEXT-D2-W45-S4",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_TCKT_VNEXT~45",
 "surfaced_at": "2026-10-16T02:26:23Z",
 "one_line": "The cell's before-arm premise (every new case FAILS on the base) does not hold: three cases pin behaviour the base already has, so they pass on the base lambda by construction.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "pytest -v on the final test file against the base lambda (git show b569143371:infra/aws/lambda/ticket_center/lambda_function.py in .scratch/r19l1_before): 9 of 16 test cases FAILED; 10 further subtests failed inside tests that report PASSED; 19 failed, 7 passed, 9 subtests passed",
   "passing on base at test level: test_the_stored_requester_that_is_a_contact_gets_the_notice, test_the_single_recipient_guard_still_refuses_two_addresses, test_no_log_line_the_notice_path_writes_contains_a_full_address",
   "base _client_recipients (lambda_function.py line 1182 at b569143371) returns [requester email] when non-blank: a stored contact is already sent to; base logs digests only"
  ]
 },
 "spec_asserts": "TO-R19-L1 RECORD FACE: the before-arm (the new tests on the base) -- every case FAILS.",
 "world_is": "Three cases assert behaviour the base already has: a stored requester that is a contact is notified, the single-recipient guard refuses two addresses, and no notice-path log line carries a full address. They pass on the base, and they stay in the file as regression pins. The other cases fail on the base as the cell intends.",
 "disposition": "UNDER_INVESTIGATION",
 "notes": "Recorded in R19_L1_RECORD.json as the before-arm result. The mutant check (AC2) is separate: it fires on the mutant copy. The order's criteria are unaffected by this premise."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W47-S1",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~47",
  "surfaced_at": "2026-10-16T01:40:53Z",
  "one_line": "The worktree C:/dev/wk-tckt-vnext-47 is a sparse checkout that omits infra/aws, so the TO-R19-L3 paths infra/aws/lambda/ticket_center/lambda_function.py and tests/ are absent from the working tree although HEAD carries them.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git -C C:/dev/wk-tckt-vnext-47 config --get core.sparseCheckout = true; git sparse-checkout list = .tools, infra/logic/registry, lib, org/devices, org/missions/D7/TCKT/TCKT_VNEXT, org/modules/graph, org/ref, org/standards (rc=0)",
      "git ls-files -v infra/aws: 9277 entries flagged S (skip-worktree); ls infra in the worktree shows README.md, launch_agents_powershell.ps1, logic/ only",
      "git ls-tree HEAD infra/aws/lambda/ticket_center/ at worktree HEAD b84a2ca293: lambda_function.py (blob b51d9ab912) and tests/ (tree e5e5594bea) present",
      "Read, Glob and Grep on C:/dev/wk-tckt-vnext-47/infra/aws/lambda/ticket_center return does-not-exist; TO-R19-L3 <paths> names these two entries for the cell"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The worker worktree carries the paths the task order names (infra/aws/lambda/ticket_center/lambda_function.py and its tests/ folder), so the cell can be built and tested in it.",
  "world_is": "The worktree is a sparse checkout that excludes infra/aws and org/surprise_channel; the named paths exist at HEAD but are not materialised. Per the worker rules this is a BLOCKING stop: the worker does not rebuild, extract or change the sparse-checkout. The surprise-row schema org/surprise_channel/schemas/investigation_item.schema.json is also absent from the worktree.",
  "notes": "Stop taken at the first act. No source edit, no test, no deploy, no apply, no live call. TO-R19-L3 status stays pending. The issuer may re-provision the worktree or amend the grant; the worker does not decide which."
}
```

```json
{
  "id": "TCKT_VNEXT-D2-W47-S2",
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~47",
  "surfaced_at": "2026-10-16T02:27:24Z",
  "one_line": "The whole-folder drain check cannot collect 8 of the 30 test modules in this sparse worktree: test_package_route.py reads org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json at import, the file is tracked at HEAD but outside the sparse-checkout list, so collection raises FileNotFoundError.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git config --get core.sparseCheckout = true; git sparse-checkout list (rc=0) has no org/missions/D9 entry",
      "git ls-files -- org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json lists the file at HEAD (839 bytes); it is absent from C:/dev/wk-tckt-vnext-47",
      "python -m pytest C:/dev/wk-tckt-vnext-47/infra/aws/lambda/ticket_center/tests/ -q -p no:cacheprovider (no -k): 8 errors during collection, FileNotFoundError at test_package_route.py:37 (_i7_canonical); line 37 is not edited by this order (git diff of test_package_route.py touches line 85 only)",
      "scratch copy under .scratch/cur-root (the working-tree infra folder plus the same fixture restored byte-for-byte from HEAD): 403 passed, 42 subtests passed, 0 failed"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The drain check named by TO-R19-L3 (the whole infra/aws/lambda/ticket_center/tests folder run in the worker worktree, zero failures after the re-pins) collects and runs every test module in the worktree.",
  "world_is": "In this sparse worktree org/missions/D9 is outside the sparse-checkout, so the one fixture read at import is absent and 8 modules (test_no_row_refuses, test_package_409_codes, test_package_env_firms, test_package_i5p_i7, test_package_principal, test_package_request_id, test_package_route, test_status_active) error at collection. The worker did not change the sparse checkout or the grant. The folder count in the record comes from the scratch copy with the fixture restored from HEAD; the product tree was not changed for it.",
  "notes": "Filed for the issuer. AC1 and AC2 are measured as the order states. The fix (a sparse-checkout entry for that fixture, or a grant for it) is the issuer's decision; the worker does not decide which."
}
```
```json
{
 "id": "TCKT_VNEXT-D2-W46-S4",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "0.9.0_WK_TCKT_VNEXT~46",
 "surfaced_at": "2026-10-16T03:06:13Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "The whole-folder run of infra/aws/lambda/ticket_center/tests/ after AMENDMENT 1 reads 374 passed, 7 failed, 8 errors. The 8 errors are the known sparse-cone collection errors; the 7 failures are all in test_cross_firm_global_register.py, which reads infra/aws/lambda/investor-reporting/_scope/interactive_access.py at test time. That file is tracked at HEAD and absent from this sparse worktree.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "C:/dev/wk-tckt-vnext-46 @535b02a627: timeout 120 python -m pytest C:/dev/wk-tckt-vnext-46/infra/aws/lambda/ticket_center/tests/ -q -p no:cacheprovider --color=no --continue-on-collection-errors -> 7 failed, 374 passed, 8 errors, 59 subtests passed, rc=1 (output .scratch/folder_run.txt); 15 FAILED/ERROR lines, all test_cross_firm_global_register.py (7) or a collection error (8)",
   "git ls-files -- infra/aws/lambda/investor-reporting/_scope/interactive_access.py lists the file at 535b02a627; test -e on the worktree path returns ABSENT (the sparse cone excludes infra/aws); the tracebacks end in FileNotFoundError on that worktree path",
   "git diff HEAD -- infra/ touches only infra/aws/lambda/ticket_center/tests/test_analyst_intake_scoped.py; test_cross_firm_global_register.py is unmodified, so the failure is the sparse checkout, not the change"
  ]
 },
 "spec_asserts": "TO-R19-L2 step 7 (AMENDMENT 1) and R19L2-AC1: after the stub fix, the whole ticket_center tests folder runs once as a drain check, and the only failures are the known sparse-cone collection errors.",
 "world_is": "The folder run shows 7 failures in test_cross_firm_global_register.py beyond the 8 known collection errors. The module collects; its tests read the investor-reporting fixture named at its line 17, which is outside the sparse cone. Both the 8 errors and the 7 failures are sparse-cone effects; neither comes from this order's edit.",
 "disposition": "UNDER_INVESTIGATION",
 "notes": "Filed by 0.9.0_WK_TCKT_VNEXT~46 under the order's counts rule. OBSERVATION, not BLOCKING: no file in the grant is touched by the failure, and the order's own criteria (the new file: 7 of 7; the mutant: fires) do not run that module. The fix (a sparse entry for the investor-reporting fixture, or a drain run where it is materialised) is the issuer's or integrator's decision. Hazard INERT: nothing is deployed, applied or called."
}
``````json
{
 "id": "TCKT_VNEXT-D2-S55",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "0.7.0_AE_CloudOps~TV2",
 "surfaced_at": "2026-10-16T04:25:00Z",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "disarm_owner": "2.0.0_SA_COO~V2 (amends the check or rules on the row; any write to that row needs a pair of its own, CTO half included)",
 "one_line": "TO-R19-MIG is applied exactly per the pair (19 of 19 written, 19 of 19 read back unchanged but for the marker) and r19_mig_check.py still prints MIG-BAD: it counts the one active string-valued allowedFirmIds service row (opaque key c56e4e2e507b) as locked out, and the pair says that row is not selected and not changed. The check can never pass while the pair holds.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R19_CHECKS/r19_mig_check.py (04:2xZ, after the 19 writes) -> MIG-BAD 1 active internal row(s) have neither a non-empty list nor the marker, rc=1",
   "read-only ConsistentRead scan of the 23 internal PROFILE rows (types only, no value printed): exactly one active row lacks a marker and a non-empty L list: key sha256-12 c56e4e2e507b, userType service, allowedFirmIds type S",
   "r19_mig_check.py:64 tests r[allowedFirmIds].get('L') only, so a string value reads as an empty list; R19_MIG_PAIR.md sections 2, 3 and 4 item 4 list this row as not selected and not changed",
   "infra/aws/lambda/ticket_center/lambda_function.py:426-429: a non-list allowedFirmIds returns 403 'firm scope malformed', with or without the marker, so after the release this service row is refused whatever the migration does"
  ]
 },
 "spec_asserts": "R19_MIG_PAIR.md section 6 and the order's R19MIG-AC1: the issuer's check prints MIG-OK once the 19 selected rows carry the marker, and section 2 says the string-valued service row is left unchanged.",
 "world_is": "Both cannot hold. With the 19 markers written and the service row untouched, the check prints MIG-BAD for that one row, so the ledger leg M4 and the order's close stay open. Nothing was rolled back: the 19 writes match the pair and the offender row was never touched.",
 "disposition": "UNDER_INVESTIGATION",
 "notes": "Decision for the issuer, one of: (a) amend the check to exclude the string-valued service row and re-run it (the release will still refuse that row with 403 malformed, which matters only if that service identity calls the ticket service); (b) a separate pair to rewrite that row's allowedFirmIds as a list or add the marker after removing the string (CTO half needed); (c) rule the row out of scope in the release pair. The applier decides none of them. Key is the first 12 hex of sha256(PK): 7 of the 23 internal PKs embed an address, so no raw key is recorded."
}
```
```json
{
 "id": "TCKT_VNEXT-D2-S56",
 "project": "TCKT_VNEXT",
 "fabric": "dell2",
 "surfaced_by": "0.7.0_AE_CloudOps~TV2",
 "surfaced_at": "2026-10-16T18:45:00Z",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "disarm_owner": "2.0.0_SA_COO~V2 (rules the method; lifting the hide is a portal change on Andrew's word through the CTO, not this seat's)",
 "one_line": "TO-R18-RUN STEP 3 cannot be run as the pair writes it: the Ticket Center's New Ticket type select does not offer Trade Request on portal DEV (the hide of 4d601023 is still in the committed code), so no browser click can choose it, and the pair forbids any call replacing a click.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "git show origin/DEV:src/pages/TicketCenter/TicketCenter.tsx (origin/DEV fcbf2bcecb, tree clean): line 730 `Object.entries(TICKET_TYPE_LABELS).filter(([v]) => v !== 'trade_request').map(...)` fills the New Ticket select; lines 728-729 carry the comment 'Andrew-direct 2026-10-13 ~18:5xZ: Trade Request is not offered until it has a working channel (NFRA_OPSWKF); the form and its labels stay'",
   "git log -S: the filter was added by 4d601023 (2026-10-13 14:56 -0400, 1.0.0_SA_CTO~DELL2, 'hide(TicketCenter): Trade Request is not offered in the new-ticket type list until it has a working channel')",
   "git show --stat c05e3dda and 12c164a0 (the two candidates, both ancestors of origin/DEV): each edits TicketCenter.tsx (6 and 23 lines) and neither removes the filter; line 742 mounts TradeRequestForm only when newType === 'trade_request', which the select can no longer produce",
   "nothing was minted, written or opened by this seat: no ledger, no identity row, no token, no dev server"
  ]
 },
 "spec_asserts": "R18_RUN_PAIR.md section 3 step 3 and the order's STEP 3: in a browser on portal DEV, signed in as the filer, choose New Ticket, Trade Request, the firm cottonwood, choose the placeholder PDF, submit; the page makes the three calls and no call replaces a click.",
 "world_is": "On the DEV checkout the select offers every ticket type except Trade Request, so the Trade Request form cannot be reached by a click; FWD-11 (the meeting request and the coordinator's confirm) is reachable and unaffected.",
 "disposition": "UNDER_INVESTIGATION",
 "notes": "Options for the issuer and CTO, none taken by the applier: (a) lift the hide on DEV (a portal candidate and an Andrew word, since the hide was Andrew-direct) and re-measure the start gate; (b) amend the pair to run FWD-11 alone now and FWD-10 after (a); (c) run FWD-10 from a scratch copy of the DEV checkout with the one filter line removed (a modified build, not DEV; the CTO's call). The order says do not retry with a changed method, so I hold at the start gate."
}
```

## TCKT_VNEXT-D2-S57 -- A meeting ticket's outcome line is drawn only while the ticket is not completed, so once a meeting_request completes the Ticket Center shows no confirmed or rescheduled outcome anywhere (FWD-11 ACCEPT: the filer reads the outcome on the ticket).

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-16T21:15:00Z",
  "class": "OBSERVATION",
  "id": "TCKT_VNEXT-D2-S57",
  "disposition": "UNDER_INVESTIGATION",
  "hazard_standing": "INERT",
  "one_line": "A meeting ticket's outcome line is drawn only while the ticket is not completed, so once a meeting_request completes the Ticket Center shows no confirmed or rescheduled outcome anywhere (FWD-11 ACCEPT: the filer reads the outcome on the ticket).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal origin/DEV src/pages/TicketCenter/TicketCenter.tsx lines 909-915: {t.ticket_type === 'meeting_request' && t.status !== 'completed' && (<tr>...<MeetingOutcomeLine ticket={t} />...)}: the only mount of MeetingOutcomeLine on the board",
      "portal origin/DEV src/pages/TicketCenter/MeetingRequestParts.tsx lines 219-222: MeetingOutcomeLine reads ticket.meeting and draws outcomeLineWords(ticket.meeting)",
      "the CVO's ADJUDICATION_v8 (3.0.0_SA_CVO~DELL2, 21:05Z), section FWD-11: 'The filer sees the outcome on the same ticket: NOT EXERCISED'; the source note that MeetingOutcomeLine shows only while status !== 'completed'",
      "TCK-20261016-9d7654eb: the part-1 meeting ticket was confirmed 19:24Z and COMPLETED 20:2xZ by the issuer's part 1b (to exercise the pickup notice), which is the state in which no outcome line is drawn"
    ]
  },
  "spec_asserts": "TCKT_VNEXT PRD v0.6 FWD-11 ACCEPT: the filer reads confirmed or rescheduled on the ticket.",
  "world_is": "The board's meeting block is mounted only for tickets whose status is not completed. A meeting_request that a coordinator confirmed and staff then completed shows its outcome on neither the open/in-progress tabs (it has left them) nor the Completed tab (the block is not mounted there). The data is stored (ticket.meeting.status, .time, .by); only the page omits it. Not yet decided whether completing a meeting ticket is the normal end of its life or whether the outcome must stay readable after it; that is the CTO's reading of FWD-11 for the round-N analysis."
}
```

## TCKT_VNEXT-D2-W49-S1 -- The whole-folder drain run of infra/aws/lambda/ticket_center/tests/ cannot be clean in this worktree: 8 modules fail collection and 11 tests fail, all reading paths this worktree does not carry, and the same counts occur on the unchanged base.

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~49",
  "surfaced_at": "2026-10-16T21:58:12Z",
  "class": "OBSERVATION",
  "id": "TCKT_VNEXT-D2-W49-S1",
  "disposition": "UNDER_INVESTIGATION",
  "hazard_standing": "INERT",
  "one_line": "The whole-folder drain run of infra/aws/lambda/ticket_center/tests/ cannot be clean in this worktree: 8 modules fail collection and 11 tests fail, all reading paths this worktree does not carry, and the same counts occur on the unchanged base.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-tckt-vnext-49 @430b378b8f (base HEAD, before the lambda edit): timeout 120 python -m pytest C:/dev/wk-tckt-vnext-49/infra/aws/lambda/ticket_center/tests/ -q -p no:cacheprovider --color=no --continue-on-collection-errors -> 13 failed, 380 passed, 8 errors, rc=1; the 2 new same-member cases are among the 13, so the pre-existing count is 11 failed and 8 errors",
      "after the uncommitted edit, same command -> 11 failed, 382 passed, 8 errors, rc=1: the failures are test_cross_firm_global_register.py (7) and test_cross_firm_global_sites_widened.py (4); no failure names attachment_open_ticket",
      "collection errors (8): test_no_row_refuses, test_package_409_codes, test_package_env_firms, test_package_i5p_i7, test_package_principal, test_package_request_id, test_package_route, test_status_active end in FileNotFoundError; test_package_route reads org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json, which is absent from this worktree",
      "test_cross_firm_global_sites_widened fails with 'scan finds 0 site(s), the record table says 2 -- re-classify this file in org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~229/OPAL_GLOBAL_SITES_CLASSIFIED' for infra/aws/lambda/investor-reporting/_authz/enforce.py; that record and the scanned file are outside this order's grant"
    ]
  },
  "spec_asserts": "TO-R20-LM step 4 (drain check): the whole ticket_center tests folder is run once and its counts are recorded in the record; the issuer re-runs it. The order states no expected folder outcome.",
  "world_is": "In this worktree the folder run is not a clean drain. Eight modules cannot be collected and eleven tests fail, all in modules that read D9 IRPT deliverables or the investor-reporting classification record, neither of which this worktree carries. The same eleven failures and eight errors occur on the base before the edit, so none is caused by this order. Counts are recorded in R20_LM_RECORD.json."
}
```

## TCKT_VNEXT-D2-W49-S2 -- The step-2 presign-from-requester-firm with the step-1 equality test removed does not fire on a ticket whose key sits under the answers firm, so the first same-member case carries a second sub-ticket whose key sits under the requester firm.

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~49",
  "surfaced_at": "2026-10-16T21:58:12Z",
  "class": "OBSERVATION",
  "id": "TCKT_VNEXT-D2-W49-S2",
  "disposition": "UNDER_INVESTIGATION",
  "hazard_standing": "INERT",
  "one_line": "The step-2 presign-from-requester-firm with the step-1 equality test removed does not fire on a ticket whose key sits under the answers firm, so the first same-member case carries a second sub-ticket whose key sits under the requester firm.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-tckt-vnext-49 @430b378b8f: attachment_open_ticket key-prefix check 'if not att[key].startswith(key_tpl.format(firm=firm)): return 404 carries no attachment' (lambda_function.py base line 2126); a base ticket with requester inflection, answers cottonwood and a cottonwood key returns 200 (the before-arm: the first case FAILS on base as the order expects)",
      "with the presign member set to req_firm and the equality refusal removed (mutant copy in .scratch/mutant_R20LM), a ticket whose key sits under the answers prefix is refused by the key-prefix check: the sub-ticket-a case passes on the mutant",
      "mutant_check.py run after the sub-ticket-b case was added: CONTROL rc=0 (5 passed); MUTANT rc=1 '1 failed, 4 passed'; pytest -rf names test_open_refuses_a_ticket_whose_requester_firm_differs_from_answers_firm; MUTANT-FIRES"
    ]
  },
  "spec_asserts": "TO-R20-LM step 2 and AC2: the presign member is built from req_firm, and removing the step-1 equality refusal is a mutant the new test file catches (MUTANT-FIRES).",
  "world_is": "With the presign built from req_firm, removing the equality refusal alone leaves the answers-prefix key refused by the existing key-prefix check with the same 404, so no test on that key fails on the mutant. The mutant fires only on a ticket whose key sits under the requester firm's prefix; the base answers-prefix case is what makes the before-arm fail. Both are kept: the first same-member case (one named test) carries sub-ticket a (answers-prefix key) and sub-ticket b (requester-prefix key). The mutant fires on sub-ticket b. The order's two expectations are met only with that second sub-ticket."
}
```

## TCKT_VNEXT-D2-S58 -- A LIVE seat with an armed inbox watcher did not receive a GO message for about 55 minutes: the broker offered it and recorded OFFER-EXHAUSTED with no READ, the seat's watcher re-armed three times reporting no new messages, and only a keystroke nudge into its terminal made it read the message.

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-17T08:02:02Z",
  "class": "OBSERVATION",
  "id": "TCKT_VNEXT-D2-S58",
  "disposition": "UNDER_INVESTIGATION",
  "hazard_standing": "INERT",
  "one_line": "A LIVE seat with an armed inbox watcher did not receive a GO message for about 55 minutes: the broker offered it and recorded OFFER-EXHAUSTED with no READ, the seat's watcher re-armed three times reporting no new messages, and only a keystroke nudge into its terminal made it read the message.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "get_delivery_state(0.7.0_AE_CloudOps~TV2, since 2026-10-17T07:00Z) read at ~07:28Z: msg 10369 (2.0.0_SA_COO~V2 to TV2, 'TO-R20-RV: GO written'), sent 2026-10-17T07:05:11Z, SENT@07:08:13Z, state OFFER-EXHAUSTED, READ coverage 0/1; get_agent_status read at the same time: LIVE, last seen 6s ago, and its inbox listing carried 20261017T070511Z_2.0.0_SA_COO_V2_TCKT_VNEXT_TO-R20-RV__GO_written__AMENDM.md unread",
      "unstick peek of TV2's tab at 07:58:27Z (PNG unstick_peek_0.7.0_AE_CloudOps~TV2_20261017T075827Z.png, read by this seat): the transcript shows the seat re-arming its inbox watcher three times, each followed by 'No new messages. I'm idle.', and an empty composer",
      "after one nudge typed into the composer at 07:59Z (the order id and message id only), the peek at 08:00:20Z shows the seat's own words: 'I see the message was actually sent at 07:08Z but my watcher missed it, so my earlier no new messages reports were a false inference rather than confirmed fact', and it then measured the pair blobs and read the GO draft"
    ]
  },
  "spec_asserts": "CLAUDE.md rule 22a (DELIVERY): SENT != EMITTED != READ, only an agent-side ACK is a sound oracle, and an orphaned watcher reads REACHABLE because the agent is deaf; the watcher skill: the inbox monitor emits one [INBOX] event per message.",
  "world_is": "The seat was reachable on every liveness signal (LIVE, heartbeat seconds old, a watcher monitor running) and unreachable for the one thing that mattered: its watcher emitted no [INBOX] event for message 10369, and the seat concluded 'no new messages' from the silence. The cost was about 55 minutes on a due-in-seven-days run, recovered by a keystroke nudge. Cause not measured: this seat did not read the watcher script's run or the seat's monitor output. Not claimed: that other seats are affected."
}
```

## TCKT_VNEXT-D2-S59 -- The meeting outcome line is drawn on the Ticket Center board in navy ink on the board's dark navy row, a contrast of 1.25 to 1, so a filer cannot read it in the rendered page after the confirm or after completion; the outcome words are in the DOM and the build tests pass, so only the rendered read shows it. It blocks FWD-11 from REALIZED and rides in the approved PROD re-cut.

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-17T08:30:46Z",
  "class": "OBSERVATION",
  "id": "TCKT_VNEXT-D2-S59",
  "disposition": "UNDER_INVESTIGATION",
  "hazard_standing": "INERT",
  "one_line": "The meeting outcome line is drawn on the Ticket Center board in navy ink on the board's dark navy row, a contrast of 1.25 to 1, so a filer cannot read it in the rendered page after the confirm or after completion; the outcome words are in the DOM and the build tests pass, so only the rendered read shows it. It blocks FWD-11 from REALIZED and rides in the approved PROD re-cut.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "the six R20-RV shots at org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_run/ (TCK-20261017-da2a1987, origin http://localhost:5174 serving DEV 38d4f9473284), each READ by this seat as an image: in filer_waiting, filer_confirmed, filer_completed and bystander_no_control the second row of the ticket reads in dark blue on the dark navy board row; in coordinator_controls the white controls panel is readable but the outcome line above it is not",
      "contrast measured from the pixels of the saved PNGs (python PIL, the outcome line's rows, left 620 px): background rgb(25,38,67), strongest text pixel rgb(22-23,51,114), WCAG contrast ratio 1.25:1 on filer_waiting, filer_confirmed and filer_completed (readable text needs 4.5:1)",
      "portal/src/pages/TicketCenter/MeetingRequestParts.tsx line 29 'const INK = text-[hsl(var(--palette-navy))]' (the ink the file's own comment says belongs on a white panel) and line 222 MeetingOutcomeLine returns <p className={text-xs font-medium ${INK}}>; the board row it mounts in (TicketCenter.tsx, the meeting row after AnalysisDraftAndPackage) has no white panel, and its neighbours use text-white/50 and text-white/70"
    ]
  },
  "spec_asserts": "The CTO's rounds 18-19 ruling 4 and the PRD FWD-11: the filer reads the meeting outcome on the ticket in every status that carries one; R20PT-AC4J as graded: the outcome line shows (graded on the diff, the tests and the DOM text, not rendered).",
  "world_is": "The outcome line is present in the DOM and absent to the eye: navy ink on a dark navy row at 1.25:1. The ten tests render to static markup and assert the words, never a colour, so they pass; the first look at the rendered page (R20-RV, the filer's shots) is the first thing that could show it. The same code is in the approved PROD re-cut (row 8b35, 4e1e35bf) that the dell2 PROD set carries, so PROD would ship the line unreadable. Remedy not yet applied: one class on MeetingOutcomeLine (a light ink for the board row, as its neighbours use) and a test that the line carries no navy ink outside a white panel."
}
```

## TCKT_VNEXT-D2-S60 -- The second GO message in one morning that 0.7.0_AE_CloudOps~TV2's armed inbox watcher did not deliver: the broker records OFFER-EXHAUSTED with 0 of 1 read, the seat sits idle at an empty input, and a keystroke nudge makes it read the message through check-inbox; the seat itself says the watcher missed it.

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-17T10:00:50Z",
  "class": "OBSERVATION",
  "id": "TCKT_VNEXT-D2-S60",
  "disposition": "UNDER_INVESTIGATION",
  "hazard_standing": "INERT",
  "one_line": "The second GO message in one morning that 0.7.0_AE_CloudOps~TV2's armed inbox watcher did not deliver: the broker records OFFER-EXHAUSTED with 0 of 1 read, the seat sits idle at an empty input, and a keystroke nudge makes it read the message through check-inbox; the seat itself says the watcher missed it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "get_delivery_state(0.7.0_AE_CloudOps~TV2, since 2026-10-17T09:40Z) read at ~09:58Z: msg 10486 (2.0.0_SA_COO~V2 to TV2, 'TO-R20-PROD: GO written'), sent 09:46:55Z, SENT@09:49:58Z, OFFER-EXHAUSTED, READ coverage 0/1; TV2 had opened no ledger and written no r20_prod artifact in 11 minutes",
      "unstick peek of TV2's tab at 09:58:30Z (PNG unstick_peek_0.7.0_AE_CloudOps~TV2_20261017T095830Z.png, read by this seat): its last words 'Nothing else is waiting ... I re-armed the inbox watcher and read the inbox directly' (done 5:33 AM ET = 09:33Z), an empty composer, and its watcher re-armed",
      "after one nudge typed at 09:59Z (order id and message id only), the peek at 09:59:45Z (PNG ..._20261017T095945Z.png) shows the seat's words 'The watcher missed this one too - only check-inbox caught the 09:49Z message', and it began measuring the blobs",
      "the first instance is row TCKT_VNEXT-D2-S58 (msg 10369, 07:05Z, missed for ~55 min); a third GO that day (msg 10445, TO-R20-RV2, 09:02Z) was read 'at once' by the seat's own check-inbox, because the GO text told it to run check-inbox first"
    ]
  },
  "spec_asserts": "CLAUDE.md rule 22a (DELIVERY): SENT != EMITTED != READ and only an agent-side ACK is a sound oracle; the watcher skill: the inbox monitor emits one [INBOX] event per message and re-arms at its 30-minute expiry.",
  "world_is": "Two of three GOs sent to this seat today reached it only by a reader pulling the inbox, not by its watcher (the third because the GO itself told the seat to run check-inbox). The seat's liveness reads fine each time; its silence is the only symptom. This seat's practice is now to put 'run check-inbox first' in every GO to TV2 and to read get_delivery_state ten minutes after a send. Cause not measured; not claimed: that other seats are affected, or that the watcher script itself is at fault rather than this seat's monitor lifecycle (idle between re-arms)."
}
```

## TCKT_VNEXT-D2-S61 -- The third GO message in three days that 0.7.0_AE_CloudOps~TV2's armed inbox watcher did not deliver (msg 10800, TO-R20-PROD2): OFFER-EXHAUSTED with 0 of 1 read after 12 minutes, the seat idle at an empty input; a keystroke nudge made it read the GO through check-inbox, and the seat says the watcher never surfaced it.

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~V2",
  "surfaced_at": "2026-10-19T17:05:00Z",
  "class": "OBSERVATION",
  "id": "TCKT_VNEXT-D2-S61",
  "disposition": "UNDER_INVESTIGATION",
  "hazard_standing": "INERT",
  "one_line": "The third GO message in three days that 0.7.0_AE_CloudOps~TV2's armed inbox watcher did not deliver (msg 10800, TO-R20-PROD2): OFFER-EXHAUSTED with 0 of 1 read after 12 minutes, the seat idle at an empty input; a keystroke nudge made it read the GO through check-inbox, and the seat says the watcher never surfaced it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "get_delivery_state(0.7.0_AE_CloudOps~TV2) read at ~16:59Z: msg 10800 (2.0.0_SA_COO~V2 to TV2, 'GO: TO-R20-PROD2 ... run check-inbox first'), sent 16:47:38Z, SENT@16:50:44Z, OFFER-EXHAUSTED, READ coverage 49 of 50 (this one unread); TV2 had opened no ledger and written no r20_prod2 artifact in 12 minutes (ls of deliverables/r20_prod2: absent)",
      "unstick peek of TV2's tab at 17:00:10Z (PNG unstick_peek_0.7.0_AE_CloudOps~TV2_20261019T170010Z.png, read by this seat): its last words 'Re-armed the inbox watcher and read the inbox directly. It is empty. I'm idle.' (done 12:46 PM local, before the GO was sent), an empty composer, one monitor running",
      "one nudge typed at ~17:01Z (the message id, the commit and the order file; no new instruction); the peek at 17:04:18Z (PNG ..._20261019T170418Z.png) shows the seat's words 'The GO is there (10800, sent 16:47Z, never surfaced by the watcher). Acking it, then the order file and pair amendments 8 and 9', and it began reading the order",
      "earlier instances: rows TCKT_VNEXT-D2-S58 (msg 10369) and TCKT_VNEXT-D2-S60 (msg 10486), both 2026-10-17; this is the third of the GOs this seat has been sent since then that the watcher missed (the 2026-10-17 GO 10445 was read at once because the seat ran check-inbox on its own)"
    ]
  },
  "spec_asserts": "CLAUDE.md rule 22a (DELIVERY): SENT != EMITTED != READ and only an agent-side ACK is a sound oracle; the watcher skill: the inbox monitor emits one [INBOX] event per message and re-arms at its 30-minute expiry. The GO text told the seat to run check-inbox first, which only helps once the seat has been told a GO exists.",
  "world_is": "A GO sent to an IDLE TV2 seat does not reach it unless something wakes it: the watcher event did not fire for the message, and the 'run check-inbox first' line in the GO is read only after the seat has read the GO. This seat's practice is to read get_delivery_state about ten minutes after each GO sent to TV2 and to peek and nudge when it reads OFFER-EXHAUSTED. Cost this time: about 12 minutes of the run's start. Cause not measured; not claimed: that the watcher script is at fault rather than the seat's monitor lifecycle, or that other seats are affected."
}
```

## TCKT_VNEXT-D2-S62 -- The CloudOps applier identity cannot delete the Trade Request test object on PROD: s3:DeleteObject on opal-data-cottonwood is an EXPLICIT DENY in cloudops-dell-agent-deploy-policy, so TO-R20-PROD3 left one 31-byte synthetic object under the trade-form prefix.

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~TV2",
  "surfaced_at": "2026-10-19T20:50:00Z",
  "class": "OBSERVATION",
  "id": "TCKT_VNEXT-D2-S62",
  "disposition": "UNDER_INVESTIGATION",
  "hazard_standing": "INERT",
  "one_line": "The CloudOps applier identity cannot delete the Trade Request test object on PROD: s3:DeleteObject on opal-data-cottonwood is an EXPLICIT DENY in cloudops-dell-agent-deploy-policy, so TO-R20-PROD3 left one 31-byte synthetic object under the trade-form prefix.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "TO-R20-PROD3 attempt 1, 20:37Z: upload door 200, PUT 200, ticket 201 (TCK-20261019-2d6d1a25); head-object read at 20:49Z of s3://opal-data-cottonwood/portal/cottonwood/state/ticket_attachments/trade-form/8b46f05593e643f0bb229023841d2a4a/tckt-r20-trade-synthetic.csv: ContentLength 31, text/csv, LastModified 2026-10-19T20:37:24Z, VersionId U2wA9rMN_iqdUnci740XcsAfyvgsTK3h (bucket versioning Enabled)",
      "20:45:22Z delete-object by that exact key answered AccessDenied: 'User arn:aws:iam::313476888478:user/cloudops-dell2-agent-user is not authorized to perform s3:DeleteObject on resource ... with an explicit deny in an identity-based policy: arn:aws:iam::313476888478:policy/cloudops-dell-agent-deploy-policy' (deliverables/r20_trade_prod/attempt1/attempt1_run_events.txt)",
      "the same run deleted its opal-tickets item by key (ConsistentRead ABSENT) and, at 20:49:11Z by the CLI after the script crashed on the denial, its opal-users-v2 row (ConsistentRead ABSENT)"
    ]
  },
  "spec_asserts": "TO-R20-PROD3 and the CTO's msg 10936 bound the run to delete the ONE uploaded object by exact key with aws s3api delete-object; the order named the S3 role scope as unread. The object is invented numbers only (symbol,qty,px and one row SYN1,100,12.34).",
  "world_is": "The applier cannot do the order's S3 delete: an explicit deny, which a policy edit or another identity would be needed to get around. This seat did not try either. One synthetic 31-byte object stays under the firm's trade-form prefix until a seat that may delete does it (the key and version id are above); the ticket and the filer row are gone. Not claimed: that the deny is a mistake (it may be deliberate), or that any other prefix or bucket is affected."
}
```

## TCKT_VNEXT-D2-S63 -- TO-R20-PROD3 rerun (attempt 2) also stopped at the open read: the Open route answered 200 and the browser's own read of the object went through, but this seat's script took no url from the response body, so the SHA-256 comparison was never obtained in either attempt.

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~TV2",
  "surfaced_at": "2026-10-19T21:30:00Z",
  "class": "OBSERVATION",
  "id": "TCKT_VNEXT-D2-S63",
  "disposition": "UNDER_INVESTIGATION",
  "hazard_standing": "INERT",
  "one_line": "TO-R20-PROD3 rerun (attempt 2) also stopped at the open read: the Open route answered 200 and the browser's own read of the object went through, but this seat's script took no url from the response body, so the SHA-256 comparison was never obtained in either attempt.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "attempt 2, 21:24Z: ticket TCK-20261019-b931d737 filed (door 200, PUT 200, ticket 201); R20_TRADE_TRACE.json statuses show 'GET open route' 200 and a GET to s3 opal-data-cottonwood on the exact key (request census, path only); the script then printed 'STOP: the open route returned no url (status None)' at 21:24:48Z: it read no 'url' member from the 200 body (the body's shape was not logged, so the shape is not known to this seat)",
      "ticket and filer row deleted by key 21:26:56Z, ConsistentRead ABSENT; residue objects: attempt 1 version U2wA9rMN_iqdUnci740XcsAfyvgsTK3h, attempt 2 key .../trade-form/b35a21075c634b588e83a529a8a724c5/tckt-r20-trade-synthetic.csv version 0pTf.3QXwPeHDLNgFTEKCnP32IE4IWuu (head-object 21:28Z, 31 bytes each)",
      "attempt 1 (row TCKT_VNEXT-D2-S62): the same step stopped on a hung route.fetch; the open route's own presigned GET for the key was visible in that error log"
    ]
  },
  "spec_asserts": "TO-R20-PROD3 step (c): the bytes are fetched through the Open control and the SHA-256 read back equals the SHA-256 uploaded. The order allowed one rerun (AMENDMENT 2); it is used.",
  "world_is": "Two stops on the one step that is this seat's own instrument; the door, the PUT, the ticket, the delete of ticket and row all behave. The read-back equality is UNPROVEN, not failed. The result file was not written, so R20PROD3-AC1 would read RUN-BAD. A third attempt needs a new GO, and the first act of it should log the key set (not values) of the open route's body. Not claimed: that the bytes differ, or that the open route is wrong."
}
```

## TCKT_VNEXT-D2-W53-S1 -- The package route's test harness cannot load in this worktree: test_package_route.py reads org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json at import, and that file is absent here, so the issuer's Lambda check R20LM7-AC1 cannot run and the ticket_center folder fails collection.

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~53",
  "surfaced_at": "2026-10-19T23:03:34Z",
  "class": "BLOCKING",
  "id": "TCKT_VNEXT-D2-W53-S1",
  "disposition": "UNDER_INVESTIGATION",
  "hazard_standing": "INERT",
  "one_line": "The package route's test harness cannot load in this worktree: test_package_route.py reads org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json at import, and that file is absent here, so the issuer's Lambda check R20LM7-AC1 cannot run and the ticket_center folder fails collection.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-tckt-vnext-53 @d2f482c9678 (branch wk-TCKT_VNEXT-53): git config core.sparseCheckout = true, cone mode; git ls-files -v marks org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json with the S (skip-worktree) flag; ls org/missions/D9 -> No such file or directory; the file is tracked (git ls-files lists it, 1 entry)",
      "timeout 120 python -m pytest C:/dev/wk-tckt-vnext-53/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_CHECKS/test_r20_package_commentary_null.py -q -p no:cacheprovider --color=no -> rc 2, collection error: FileNotFoundError on C:\\dev\\wk-tckt-vnext-53\\org\\missions\\D9\\IRPT\\IRPT_ANLREQ\\deliverables\\2.0.0_SA_COO~G2\\I7_SAMPLE.json, raised at test_package_route.py line 41 (_i7_canonical at line 37)",
      "timeout 120 python -m pytest infra/aws/lambda/ticket_center/tests -q -p no:cacheprovider --color=no -> rc 2, Interrupted: 8 errors during collection (test_no_row_refuses, test_package_409_codes, test_package_env_firms, test_package_i5p_i7, test_package_principal, test_package_request_id, test_package_route, test_status_active), all the same FileNotFoundError",
      "sibling row TCKT_VNEXT-D2-W49-S1 (worker 49, worktree 430b378b8f) records the same eight collection errors for the same missing path"
    ]
  },
  "spec_asserts": "TO-R20-LM7 ACCEPTANCE R20LM7-AC1: the issuer's Lambda check file runs from C:/dev/wk-tckt-vnext-53 and passes 5 of 5; the drain check runs the whole infra/aws/lambda/ticket_center/tests/ folder once. The worker's grant is exactly the <paths> the order names, and a path the worker needs that it lacks is a BLOCKING row on that criterion, never an override.",
  "world_is": "The worktree carries the order's named paths (the Lambda source, the portal files, the D7 task order and the issuer check file) but not the D9 fixture the harness reads at import, because the sparse checkout omits it. The worker did not copy the fixture into the worktree and did not change the sparse-checkout settings: both are outside the grant. AC1 and the drain check are therefore NOT RUN to a verdict; the Lambda change is committed on the branch, unverified by the check. Not claimed: that the Lambda change is wrong."
}
```

## TCKT_VNEXT-D2-W53-S2 -- The order names the surprise schema at org/surprise_channel/schemas/investigation_item.schema.json, but org/surprise_channel is outside this worktree's sparse checkout, so the schema was read from the HEAD blob with git show.

```json
{
  "project": "TCKT_VNEXT",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_TCKT_VNEXT~53",
  "surfaced_at": "2026-10-19T23:03:34Z",
  "class": "OBSERVATION",
  "id": "TCKT_VNEXT-D2-W53-S2",
  "disposition": "UNDER_INVESTIGATION",
  "hazard_standing": "INERT",
  "one_line": "The order names the surprise schema at org/surprise_channel/schemas/investigation_item.schema.json, but org/surprise_channel is outside this worktree's sparse checkout, so the schema was read from the HEAD blob with git show.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-tckt-vnext-53 @d2f482c9678: cat org/surprise_channel/schemas/investigation_item.schema.json -> No such file or directory; git config core.sparseCheckout = true (cone)",
      "git show HEAD:org/surprise_channel/schemas/investigation_item.schema.json returned 10462 bytes, rc 0; the required fields and the class enum (OBSERVATION, BLOCKING) were read from that blob"
    ]
  },
  "spec_asserts": "Surprise section of the task order: a row is appended to the investigation file, per org/surprise_channel/schemas/investigation_item.schema.json, and the schema is the reference for its fields.",
  "world_is": "The schema path the order names is absent from this worktree, the same sparse-checkout cause as TCKT_VNEXT-D2-W53-S1. The worker read the schema from the committed blob and wrote the row to it. Not claimed: that the schema at the base checkout differs from the blob."
}
```
