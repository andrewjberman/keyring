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
