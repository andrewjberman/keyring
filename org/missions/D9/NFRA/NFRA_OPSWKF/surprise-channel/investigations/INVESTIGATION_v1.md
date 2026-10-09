# NFRA_OPSWKF -- surprise channel, INVESTIGATION v1 (round 1, dell2 fabric)

**Opened by:** `2.0.0_SA_COO~O2` at the L6 cut (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py` validates every NEW row (schema
`org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`.
**Id grammar:** a worker's row is `NFRA_OPSWKF-D2-W<n>-S<k>`; a seat's row is `NFRA_OPSWKF-D2-S<k>` (dell2 coordinate); the CVO's
adjudication rows live in `../adjudications/` as `NFRA_OPSWKF-C-S<k>`.
**Append-only during the round.** Never edit an existing row.

## NFRA_OPSWKF-D2-S1 -- Three trade-workflow tests ERROR under pytest at base: a script-run file whose fixture only its own __main__ supplies

```json
{
  "id": "NFRA_OPSWKF-D2-S1",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~O2",
  "surfaced_at": "2026-10-09T05:32:45Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "pytest over infra/aws/lambda/trade-pipeline/trade-workflow-handler/tests reports 18 passed, 3 errors at base: test_actor_identity.py takes a monkeypatched_no_submission argument that only its own __main__ runner supplies, so pytest finds no fixture",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/trade-pipeline/trade-workflow-handler/tests/test_actor_identity.py:67,75,82 (last touched 7d02fb663d): def test_...(monkeypatched_no_submission); :108 the __main__ runner passes a _Ctx() for that name",
      "python -m pytest -q infra/aws/lambda/trade-pipeline/trade-workflow-handler/tests (box/dell2 @e8b80719f1 base, 05:3xZ): 18 passed, 3 errors, E fixture 'monkeypatched_no_submission' not found",
      "python infra/aws/lambda/trade-pipeline/trade-workflow-handler/tests/test_actor_identity.py: 6 passed, 0 failed, rc=0 (the positive control: the tests themselves hold)"
    ]
  },
  "spec_asserts": "A drain-time regression run of the trade handler test directories (round 1's OW-e-AC2) reads green at base.",
  "world_is": "It reads 3 errors at base from a test-harness mismatch, not a behaviour fault. The round's check (R1_CHECKS/ow_checks.py trade-regress) deselects the three under pytest and runs the file as its script instead; a conftest fixture would retire the mismatch and is a one-file repair for a later round's batch cell.",
  "notes": "Not this round's to fix: no round-1 cell owns test_actor_identity.py."
}
```

## NFRA_OPSWKF-D2-W1-S1 -- trade_request create hits answers['firm'] KeyError

```json
{
  "id": "NFRA_OPSWKF-D2-W1-S1",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_NFRA_OPSWKF~1",
  "surfaced_at": "2026-10-09T06:00:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "A create of a trade_request with the four ruled answers raises KeyError 'firm' (500) in create_ticket: the typed-type branch reads answers['firm'] unconditionally, so OW-l-1's cell cannot satisfy test_trade_request_valid_create without a second edit the order forbids.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/ticket_center/lambda_function.py:1120-1125 (wk-NFRA_OPSWKF-1 @17633ea3e5 + the four questions): `if body.get(\"requester_firm\") and ... != answers[\"firm\"]` then `req_firm = answers[\"firm\"]` run for every type with questions or an attachment",
      "python -m pytest -q infra/aws/lambda/ticket_center/tests/test_trade_request_type.py: 1 failed, 3 passed; KeyError: 'firm' at lambda_function.py:1125 in test_trade_request_valid_create"
    ]
  },
  "spec_asserts": "Giving TYPE_DEFINITIONS['trade_request'] the four questions is the whole change, and an internal human's create with all four answers returns 201 with the answers stored.",
  "world_is": "The create path assumes every typed ticket carries answers.firm (the analysis_request shape); a typed trade_request without a firm answer reaches answers['firm'] and raises KeyError. Needs a TCKT_VNEXT-owned edit to fall back to the principal's firm (the untyped branch's req_firm rule) when the type has no firm question; the order grants no such edit, so the valid-create test is left failing.",
  "notes": "Not worked around: lambda_function.py is changed in exactly the one entry."
}
```

## NFRA_OPSWKF-D2-W5-S1 -- The ticket create body names the type field ticket_type, not type

```json
{
  "id": "NFRA_OPSWKF-D2-W5-S1",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_NFRA_OPSWKF~5",
  "surfaced_at": "2026-10-09T06:20:12Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "The worker face says ticket create takes `type: \"trade_request\"`; the shared tickets client and the ticket service read `ticket_type`.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/api/endpoints/tickets.ts:111-112 @2d42e9b7: export interface CreateTicketInput { ticket_type: TicketType ...",
      "infra/aws/lambda/ticket_center/lambda_function.py:1052,1092 @1addff06a5: ttype = body.get(\"ticket_type\")",
      "bun test portal/src/pages/TicketCenter/__tests__/trade-request.test.tsx: createTicket called with ticket_type trade_request, 3 pass"
    ]
  },
  "spec_asserts": "OW-p-1 call 1: ticket create with `type: \"trade_request\"`.",
  "world_is": "The tickets client's CreateTicketInput field is `ticket_type` (portal tickets.ts:111-112, POST /api/scoped/tickets) and the Lambda reads body.get(\"ticket_type\") (lambda_function.py:1052,1092). TradeRequestParts.tsx sends `ticket_type: \"trade_request\"`; a body keyed `type` would be refused 400 (ticket_type must be one of VALID_TYPES) or default to service_request.",
  "notes": "Not a deviation from intent: the face's `type` is shorthand for the ticket type. Also: CreateTicketInput.answers is typed AnalysisRequestAnswers, so the component casts the trade_request answers; widening that type is TicketCenter-side (tickets.ts is outside this order's paths)."
}
```

## NFRA_OPSWKF-D2-W5-S2 -- AnalysisRequestParts does not default its firm answer from the signed-in user

```json
{
  "id": "NFRA_OPSWKF-D2-W5-S2",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_NFRA_OPSWKF~5",
  "surfaced_at": "2026-10-09T06:20:12Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "AMENDMENT 1 says to fill the firm the way AnalysisRequestParts.tsx fills its firm answer; that file leaves firm blank (placeholder 'Firm id (required)').",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/pages/TicketCenter/AnalysisRequestParts.tsx:28-31,64-65 @2d42e9b7: firm: '' ; placeholder=\"Firm id (required)\"",
      "portal/src/contexts/AuthContext.context.ts:31-32 @2d42e9b7: Claims.firmId: string | null",
      "portal/src/pages/TicketCenter/TradeRequestParts.tsx: userFirm = useContext(AuthContext)?.claims?.firmId ?? ''"
    ]
  },
  "spec_asserts": "AMENDMENT 1: the form's firm field defaults to the signed-in user's firm, filled the way AnalysisRequestParts.tsx fills its firm answer.",
  "world_is": "AnalysisRequestParts.tsx:62-65 renders firm as an empty required input (EMPTY_ANALYSIS_FORM.firm = ''); no user default exists to copy. TradeRequestForm defaults firm from the auth context claims.firmId (useContext(AuthContext)?.claims?.firmId, '' when no provider), and the field stays editable.",
  "notes": "An internal Opal user's claims.firmId is 'opal-capital', which the ticket service may refuse for a partner-firm trade; the field is editable so the filer can type the firm."
}
```

## NFRA_OPSWKF-D2-S2 -- trade-workflow-handler's parquet export imports pyarrow, and no attached layer looks big enough to hold it

```json
{
  "id": "NFRA_OPSWKF-D2-S2",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~OW2",
  "surfaced_at": "2026-10-09T09:34:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "The OW-d-1 build of trade-workflow-handler raises an UNENFORCED import-closure advisory for openpyxl and pyarrow; the live function carries exactly ONE layer, openpyxl-layer:3 at 817,805 bytes, which is far too small to contain pyarrow, so the lazily-imported parquet export path looks like a dormant ImportError. PRE-EXISTING and untouched by this act.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bash infra/aws/lambda/ci/build-and-upload.sh trade-pipeline trade-workflow-handler (BUILD_ONLY, 09:30Z): 'ADVISORY (not enforced -- no BUILD_MANIFEST.json ...) ? openpyxl (imported by: excel_generator.py) ? pyarrow (imported by: parquet_exporter.py)'",
      "infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/parquet_exporter.py:16-17 @71a1877db0: 'import pyarrow as pa' / 'import pyarrow.parquet as pq', both TOP-LEVEL in the module",
      "infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/workflow_handler.py:529 @71a1877db0: 'from parquet_exporter import export_single_submission' -- the import is LAZY, inside the handler path, so the module loads only when that path runs",
      "aws lambda get-function-configuration --function-name trade-workflow-handler --query 'Layers[].Arn' (09:31Z): exactly one entry, arn:aws:lambda:us-east-1:313476888478:layer:openpyxl-layer:3",
      "aws lambda get-layer-version --layer-name openpyxl-layer --version-number 3 (09:33Z): CodeSize 817805, Description 'openpyxl for yang-generate-cma xlsx parsing', created 2026-03-11"
    ]
  },
  "spec_asserts": "The packaged trade-workflow-handler's top-level imports are satisfied at runtime by the package, the stdlib, the runtime or an attached layer -- the condition the import-closure gate grades, and which it declares UNENFORCED for this function because there is no BUILD_MANIFEST.json declaring layer_dependencies.",
  "world_is": "parquet_exporter.py imports pyarrow at module top level. The deployed function's only layer is openpyxl-layer:3, whose description names openpyxl alone and whose CodeSize is 817,805 bytes. That pyarrow is therefore ABSENT is INFERRED from the layer's size and description, NOT measured: no layer content listing was taken, and the python3.11 runtime does not ship pyarrow. If the inference holds, workflow_handler.py:529 raises ImportError whenever the single-submission parquet export path runs, and the failure is invisible until that path is exercised because the import is lazy. What would settle it, and what this row does NOT claim to have run: download openpyxl-layer:3 and list its top-level modules, or invoke the export path once and read the result.",
  "notes": "OFF-TASK for OW-d-1 and deliberately not investigated further. This act changes the two handlers' code, one env key and one inline policy; it changes NO layer, NO packaged file list and nothing in parquet_exporter.py, whose bytes are identical pin..HEAD. The condition predates the act: the same file set and the same single layer were deployed on 2026-09-25 (CodeSha256 ChlY4kHsBjueRP2tGawZgXRZ0Qpzx4P48vTdPyRlFYY=). So this is not a regression from OW-d-1 and is not a reason to hold it. OWNER: the trade-pipeline owner via 2.0.0_SA_COO~O2; this lane is seated for NFRA_OPSWKF only and is not chasing it. A sibling row, NFRA_OPSWKF-D2-S1, already records a separate pre-existing test-harness defect in this same function's tests."
}
```

## NFRA_OPSWKF-D2-S3 -- the dell2 cloudops principal cannot plan the trade-pipeline tree, so safe-apply's tagauthz gate cannot evaluate and OW-d-1 cannot be applied from this device

```json
{
  "id": "NFRA_OPSWKF-D2-S3",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~OW2",
  "surfaced_at": "2026-10-09T09:45:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "cloudops-dell2-agent-user holds no ses:DescribeConfigurationSet, so `terraform plan` of infra/aws/terraform/trade-pipeline exits 1 on refreshing aws_ses_configuration_set.trade_pipeline; safe-apply's comp-tagauthz limb runs its OWN untargeted plan of the tree and therefore fails closed (exit 4), and a -target or saved-planfile apply does not help because that limb accepts neither.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "terraform plan -chdir=infra/aws/terraform/trade-pipeline (09:40Z) rc=1: 'Error: reading SES Configuration Set (trade-pipeline-notifications): ... StatusCode: 403 ... AccessDenied: User: arn:aws:iam::313476888478:user/cloudops-dell2-agent-user is not authorized to perform: ses:DescribeConfigurationSet because no identity-based policy allows the ses:DescribeConfigurationSet action', with aws_ses_configuration_set.trade_pipeline, ses.tf line 19",
      "the SAME plan nonetheless rendered 'Plan: 0 to add, 3 to change, 0 to destroy' over exactly the three OW-d-1 resources, so the failure is a refresh-permission fault and NOT a branch-B plan shape",
      "terraform plan with -target on the three resources (09:41Z) rc=0, no error, 'Plan: 0 to add, 3 to change, 0 to destroy' -- the targeted plan is clean",
      ".tools/safe-apply.sh -chdir=infra/aws/terraform/trade-pipeline apply <saved targeted planfile> (09:43Z) exit 4: 'could not produce a plan JSON to run the tag-authz gate ... a gate that cannot evaluate must not pass. Refusing to apply. (Fail closed.)' with the same 403 echoed as the cause",
      ".tools/safe-apply.sh:424-427 -- the tagauthz limb runs `\"$TERRAFORM\" -chdir=\"$CHDIR_TREE\" plan -input=false -lock=false -out=\"$TAG_TMP.bin\"` with NO -target and NO reuse of the caller's planfile; :342 records that reusing the saved planfile is DEFERRED",
      "aws sts get-caller-identity (09:44Z): arn:aws:iam::313476888478:user/cloudops-dell2-agent-user",
      "aws iam list-attached-user-policies / list-user-policies / list-groups-for-user (09:44Z): 2 attached user policies (cloudops-dell2-agent-bus-policy, cloudops-dell2-agent-ssm-policy), 0 inline, group cloudops-dell-agents-group with 9 attached policies",
      "aws iam get-policy-version cloudops-dell-agent-plan-reads-policy v2 (09:45Z): 2 statements, Sids ReadSsmParametersPlanReads and ReadUiWalkerPassword, actions ssm:GetParameter/ssm:GetParameters ONLY -- no ses action of any kind",
      "Grep 'ses:|SES' over infra/aws/terraform/nfra-ctlpln-identity/iam.tf: 3 hits, all PROSE comments about secret classes; zero ses: actions granted"
    ]
  },
  "spec_asserts": "NFRA_OPSWKF.TO-APPLY-D1 step 4: plan, then `.tools/safe-apply.sh`, with the dell2 applier running the apply on the device that owns the work (CLAUDE.md rule 26, and the CTO applier-substitution ruling @5ff94852a6 naming this lane).",
  "world_is": "The apply cannot be run from dell2 at all, for any plan shape, until cloudops-dell2-agent-user gains ses:DescribeConfigurationSet. The permission set is defined in infra/aws/terraform/nfra-ctlpln-identity/ (iam.tf, main.tf), whose natural home is cloudops-dell-agent-plan-reads-policy -- the policy whose stated purpose IS the reads terraform needs at plan time, and which today carries only two ssm:GetParameter statements. INFERRED, not measured: that this ONE grant is sufficient. The failing plan surfaced exactly one error and still rendered a summary, which is evidence the rest of the refresh walked, but aws_ses_configuration_set_event_destination and anything else downstream of the failed resource may have been skipped rather than read, so a second SES read may surface once the first is granted. What would settle it: grant it, then re-plan and read the rc.",
  "notes": "OUT-OF-LANE for this seat, which is seated for NFRA_OPSWKF only; the principal belongs to NFRA_CTLPLN's identity stack. This lane did NOT and will not grant itself the permission, and did NOT reach for TAGAUTHZ_OVERRIDE: safe-apply says in terms that the override 'is not the remedy for this error' and 'Do not bypass a gate to work around your own toolchain', and self-granting a bypass to land one's own deploy is the shape the no-manufactured-friction law exists to prevent. The gate behaved correctly. State of the world after the refusal, measured not claimed: both functions still CodeSha256 AaR7TiZ0qAGfzozoKmd+JFgvdBvQEcymjP/T+Yfzp50= and ChlY4kHsBjueRP2tGawZgXRZ0Qpzx4P48vTdPyRlFYY= at LastModified 2026-09-25T17:19:52Z, env still the 3 prior keys with NO TICKETS_TABLE, and trade-submission-policy still 5 statements with ZERO occurrences of 'opal-tickets' in the live document. The two new artifact object versions sit in S3 unreferenced; both functions still pin their prior s3_object_version, so nothing is half-landed and the rollback pins in the ledger remain valid. OWNER: 2.0.0_SA_COO~O2 to route to the NFRA_CTLPLN identity owner."
}
```
