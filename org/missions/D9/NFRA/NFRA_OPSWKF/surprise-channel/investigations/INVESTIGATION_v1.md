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

## NFRA_OPSWKF-D2-S4 -- the dell2 cloudops principal cannot run after-read (c)'s prescribed instrument: iam:SimulatePrincipalPolicy and dynamodb:GetResourcePolicy are both denied

```json
{
  "id": "NFRA_OPSWKF-D2-S4",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~OW2",
  "surfaced_at": "2026-10-09T10:20:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "OW-d-1's after-read (c) names simulate-principal-policy, including the CTO half's negative arm; cloudops-dell2-agent-user holds neither iam:SimulatePrincipalPolicy nor dynamodb:GetResourcePolicy, so (c) was satisfied by evaluating the applied policy document over a complete printed denominator instead, and ONE arm (a table resource-based policy) could not be closed from this device at all.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::313476888478:role/trade-submission-lambda-role (10:05Z), NINE separate invocations -- 6 arms plus 3 controls, one --resource-arns each as the IAM trap requires -- every one returned: 'AccessDenied ... User: arn:aws:iam::313476888478:user/cloudops-dell2-agent-user is not authorized to perform: iam:SimulatePrincipalPolicy on resource: arn:aws:iam::313476888478:role/trade-submission-lambda-role'",
      "aws dynamodb get-resource-policy --resource-arn arn:aws:dynamodb:us-east-1:313476888478:table/opal-tickets (10:08Z): 'AccessDeniedException ... not authorized to perform: dynamodb:GetResourcePolicy'",
      "aws iam list-role-policies trade-submission-lambda-role (10:07Z): exactly 2 inline policies, opal-users-v2-access and trade-submission-policy; list-attached-role-policies: 0 attached managed policies; get-role: PermissionsBoundary = null",
      "aws iam get-role-policy for BOTH inline policies (10:07Z): the union of statements naming table/opal-tickets is exactly TicketBridgeOpalTicketsRead (dynamodb:GetItem) and TicketBridgeOpalTicketsWrite (dynamodb:UpdateItem under ForAllValues:StringEquals dynamodb:Attributes in [ticket_id, linked_submission_id, events, status]); the DynamoDBAccess statement carrying PutItem/DeleteItem/Scan names only opal-trade-submissions, trade-users and trade-security-identifiers plus indexes; opal-users-v2-access names only opal-users-v2; no wildcard resource and no Deny anywhere",
      "aws dynamodb describe-table opal-tickets (10:04Z): ACTIVE, arn:aws:dynamodb:us-east-1:313476888478:table/opal-tickets, HASH key ticket_id -- the existence read the cloud-ops false-allow rule requires beside any simulation of a named ARN"
    ]
  },
  "spec_asserts": "NFRA_OPSWKF.TO-APPLY-D1 step 5(c): run simulate-principal-policy on trade-submission-lambda-role for GetItem ALLOWED, UpdateItem with dynamodb:Attributes = [ticket_id, linked_submission_id, events] ALLOWED, UpdateItem with dynamodb:Attributes = [ticket_id, answers] DENIED (the CTO half's negative arm), and DeleteItem, PutItem and Scan DENIED.",
  "world_is": "The instrument is unavailable to the only principal this device has, so NO simulate result exists for this deploy and none is claimed. That every one of the nine calls -- the positive arms, the negative arms AND the three controls against a table the role IS granted -- failed with the identical message is itself the evidence that this is the instrument and not the world; an instrument that denies its controls is not reporting on its subject. The substitute was an evaluation of the APPLIED document over a denominator that was enumerated and printed (2 of 2 inline, 0 of 0 managed, boundary null), which yields the same six verdicts by construction: GetItem allowed, conditioned UpdateItem allowed, UpdateItem naming `answers` denied because the only UpdateItem grant for that table is the conditioned one and `answers` is outside its set, and DeleteItem/PutItem/Scan denied because no statement anywhere names that table with those actions. It is weaker than the prescribed arm in one specific way, which is NOT papered over: a document read inspects the rule, it does not evaluate it, and because dynamodb:GetResourcePolicy is also denied a table resource-based policy that could widen the role beyond the identity-policy union cannot be ruled out from dell2.",
  "notes": "Sibling of NFRA_OPSWKF-D2-S3, which is the same class on a different action (ses:DescribeConfigurationSet) and whose grant the issuer has already routed to the laptop fabric via 0.0.0_AB_MSTR~DELL2. The three gaps together say something the individual rows do not: the dell2 CloudOps principal was provisioned for APPLY but not for the READS that grade an apply. Recommend the grant that closes D2-S3 also carry iam:SimulatePrincipalPolicy and dynamodb:GetResourcePolicy, so the next trade-pipeline deploy from this device can run after-read (c) as written. OUT-OF-LANE for this seat (the principal is NFRA_CTLPLN's identity stack, and this lane is seated for NFRA_OPSWKF only); routed, not chased. The deploy itself is COMPLETE and its ledger CLOSED -- this row does not hold anything, and it is filed so the issuer grades OW-d1-AC2 knowing exactly which instrument produced each verdict."
}
```

## NFRA_OPSWKF-D2-S5 -- Row D2-S3 RESOLVED by NFRA_CTLPLN AMENDMENT 29 (live read); row D2-S2's pyarrow path does not reach any NFRA_OPSWKF flow

```json
{
  "id": "NFRA_OPSWKF-D2-S5",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~O2",
  "surfaced_at": "2026-10-09T13:13:52Z",
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Nothing remains to investigate: D2-S3's grant is applied and read live (NFRA_CTLPLN AMENDMENT 29), and D2-S2's path cannot be reached from any NFRA_OPSWKF flow; S2 itself stays open for its own owner.",
  "one_line": "Resolves row NFRA_OPSWKF-D2-S3: NFRA_CTLPLN.TO-APPLY-29 applied 12:21:00Z, and COO~C's live read for cloudops-dell2-agent-user shows ses:DescribeConfigurationSet allowed and ses:DeleteConfigurationSet refused. D2-S2 (pyarrow absent from trade-workflow-handler) stays an OBSERVATION: its only import is in Execute's success path, wrapped non-critical, and the C-NO-SEND fence returns 409 for every ticket-origin Execute before it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "0.0.0_AB_MSTR~DELL2 msgs 3329 and 3333, relaying laptop 2.0.0_SA_COO~C msg 107967: TO-APPLY-29 applied 12:21:00Z, 0/2/0, ledger closed; live read 13:0xZ: DescribeConfigurationSet allowed, DeleteConfigurationSet refused",
      "infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/workflow_handler.py:527-533 @HEAD: the lazy 'from parquet_exporter import export_single_submission' sits inside try/except 'Failed to export to Parquet (non-critical)', after the EXECUTED write and the brokerage send",
      "the same file: handle_execute's first statement returns 409 for origin == 'ticket' (OW-e-3, live since 10:02:52Z, deployed bytes 49a9607ece5d verified by the issuer)"
    ]
  },
  "spec_asserts": "A dell2 CloudOps lane can run safe-apply's untargeted tagauthz plan; NFRA_OPSWKF's flows do not depend on a module the deployed function cannot import.",
  "world_is": "Both now hold. The first holds since 12:21Z. The second held throughout: the pyarrow gap is reachable only from a non-ticket Execute, where it degrades to a logged non-critical failure. That gap belongs to the trade pipeline (TRSB_LEDGER, inactive) and goes to the round-1 analysis as an enrichment candidate; it is not a round-1 defect.",
  "notes": "Resolving row written by the issuer; append-only, S2 and S3 left as written."
}
```

## NFRA_OPSWKF-D2-S6 -- a tier-only check refuses 7 of the 9 trade users: Opal staff mostly carry tier advisor with firmId opal-capital

```json
{
  "id": "NFRA_OPSWKF-D2-S6",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~O2",
  "surfaced_at": "2026-10-11T18:28:50Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "FWD-8 as written (refuse every caller whose tier is not internal) would refuse 7 of the 9 people in trade-users: their portal rows carry tier advisor with firmId opal-capital. Only 2 of 9 carry tier internal. The fix as ordered (OW-s-2, built on its branch, not merged, not released) locks most Opal staff out of the blotter.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~O2",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws dynamodb scan trade-users (cloudops-dell2-agent-user, 2026-10-11 ~18:3xZ): Count 9, ScannedCount 9, no LastEvaluatedKey; all 9 emails at opalinvest.com",
      "aws dynamodb scan opal-users-v2 (same time): 87 items, no LastEvaluatedKey; joined to the 9 on email: 5 = tier advisor, userType absent, firmId opal-capital; 2 = tier advisor, userType Dev, firmId opal-capital; 2 = tier internal, userType Dev, firmId opal-capital. All portal users by tier: advisor 52, internal 6, absent 29",
      "infra/aws/users/lambda/portal-authorizer/index.mjs:388 and :400 @HEAD: the context's tier is the token's claim, unchanged; :201 firmId defaults to the string null",
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_XB_74E2_TRADE_DASHBOARD_API_SERVES_ANY_PORTAL_LOGIN_20261011.md:27 @HEAD: the ruled helper is tier == 'internal' (or firmId == 'opal-capital'); the PRD v0.5 ENDPOINT and the relay carry only the tier clause",
      "infra/aws/lambda/data_refresh/lambda_function.py:142-165 @HEAD: the estate's existing is_opal_internal admits tier internal OR the internal firm id by exact match"
    ]
  },
  "spec_asserts": "PRD v0.5 FWD-8 DONE WHEN: each of the eight routes refuses a verified caller whose tier is not internal and still serves one whose tier is; ACCEPT: an Opal staff member sees the blotter as before.",
  "world_is": "The two clauses disagree for 7 of 9 trade users. Opal staff are identified in the portal's user table by firmId opal-capital far more often than by tier internal (6 portal users in all carry that tier). A tier-only check meets DONE WHEN and breaks ACCEPT. The join is on the user table's stored tier; the tier a live token carries was not read (a token is minted at login from that row; a stale session could differ).",
  "notes": "Disarm: the issuer does not cut the release pair (OW-s-d-1) and does not merge wk-NFRA_OPSWKF-8 until 1.0.0_SA_CTO~DELL2 rules what 'internal' is for FWD-8; the ENDPOINT's wording is the CTO's. The issuer's recommendation: tier internal OR firmId exactly opal-capital, as the owner's ruling line 27 and data_refresh already have it, with the probe gaining an arm for an advisor-tier opal-capital caller (served) and an advisor-tier caller of another firm (refused). Found while building the pair's caller census, not by the order's checks: both of the order's checks pass on the branch."
}
```

## NFRA_OPSWKF-D2-S7 -- data-refresh admits a test-filer whose firmId is opal-capital: the release pair's expected refusal was the issuer's error

```json
{
  "id": "NFRA_OPSWKF-D2-S7",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "surfaced_by": "2.0.0_SA_COO~O2",
  "surfaced_at": "2026-10-11T19:46:33Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "The FWD-8 release pair expected data-refresh to REFUSE a userType test-filer caller; the deployed service ADMITTED synthetic caller IN-F (firmId opal-capital, tier advisor, userType test-filer) on GET /api/scoped/data-refresh/history. The code at HEAD says it should: data_refresh admits Dev OR any Opal-internal principal, and firmId opal-capital is Opal-internal. The expectation was the issuer's error, copied from an older pair without re-reading.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/critical_paths/change_management/20261011T1909Z_opswkf-fwd8-trade-dashboard-api-20261011_deploy_completion.md leg L6 (0.7.0_AE_CloudOps~DELL2, closed 19:44:10Z): 7(f) IN-F on GET /api/scoped/data-refresh/history?limit=1 answered HTTP 200 from the API (apigw-requestid present, application/json, top-level key executions); field names only were recorded",
      "infra/aws/lambda/data_refresh/lambda_function.py:209-216 @HEAD: userType Dev admits; otherwise is_opal_internal(context) admits; :142-165: is_opal_internal is tier internal OR firmId exactly opal-capital. userType test-filer is neither refused nor read past that point",
      "org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R1_RUN/TV_R1_SEAT_ARM_PLAN_AND_PAIR.md:110-116: the premise this pair copied (data_refresh lambda_function.py:165-167 admits only an empty userType or Dev) describes bytes that the file at HEAD no longer carries",
      "the same ledger leg L2: both tokens carry ONE absolute exp, 2026-10-11T19:56:21Z, held in the executor's memory only"
    ]
  },
  "spec_asserts": "Release pair OW_S_D1_RELEASE_PAIR_20261011.md section 4 and CTO half condition (the data-refresh read by IN-F): expect refused; an admit is a STOP and cleanup.",
  "world_is": "Admitted, by the function's own rule. This is not a defect of the FWD-8 release (trade-dashboard-api does not serve the route; R0, R1, R3, R4 and the bytes all read as expected) and not a new opening in data-refresh: an opal-capital principal is who that service is for. What it does change: (1) a synthetic test identity given firmId opal-capital is NOT kept out of data-refresh by a userType, so any pair that mints one must count the data-refresh routes in its blast radius; this run's IN-F had that reach from mint (19:2xZ) to exp 19:56:21Z and used it once, a GET with limit=1; (2) TCKT_VNEXT's synthetic filer carries firmId opal-capital and the same userType, and its pair rests on the same premise. NOT read by this seat: whether the data-refresh write routes (trigger, rollback, upload) pass through the same validate_user_type; the deployed bytes of data-refresh.",
  "notes": "Ruled by the issuer for its own decomposition (msg to 0.7.0_AE_CloudOps~DELL2 answering 5693): K1 stays in place, the applier records the deploy and runs the cleanup as written, no further call with either token. Routed in the round's slug to 1.0.0_SA_CTO~DELL2, whose half carried the expectation and who holds TCKT_VNEXT's halves; nothing is asked of TCKT_VNEXT's seats by this row."
}
```
