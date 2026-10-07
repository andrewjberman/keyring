# TCKT_VNEXT decomposition -- ROUND 1, the FWD-1 thread (2026-10-07, issuer 2.0.0_SA_COO~V2, dell2)

PRD `org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md` v0.2 @99eb4053c2, ADMITTED (`prd-signoff.py status`, 17:3xZ: ratified-text
SIGNED current @de16a955c3, brief SIGNED auto). Notifier msg 911. Placement DELL2 (PRD line 16; surprise row TCKT_VNEXT-D2-S1 carries
the carriers that still say laptop).

**The rectangle is the PRD section 2 thread, over its six hops.** Round 1 builds the journey (file -> hold -> work -> generate ->
return -> trace) on DEV, internal users only. FWD-4 (self-claim) is hop 3 of the thread and rides it. The enrichment backlog
(PRD section 3: C-FENCE, the one-account check, queue, commentary, second type, advisor filing) is NOT in this round.

| cell | builds (PRD hop / contract) | outcome | status | placement | risk | worker_class | depends on (observed completion) |
|---|---|---|---|---|---|---|---|
| `TV-l-1` | Ticket service: request types as definitions (C-TYPE), the `analysis_request` type with its questions and the upload handle (C-ANALYSIS-REQUEST, hop 1-2), the requester clause of `_sod_block` removed (C-SELF-CLAIM, hop 3), a report-reference write on the ticket (C-HANDOFF, hop 5) | FWD-1, FWD-4 | NOT-EVALUATED | dell2 worker | WORLD (path floor: a Lambda handler; nothing applied by the worker) | worker | -- |
| `TV-p-1` | Portal Ticket Center: choose Analysis Request, answer its questions, attach the file through the Analysis upload door, file only on NORMALIZED and show the findings otherwise (hop 1); from a held ticket, request the report through `POST .../analysis` with the ticket's `input_id` and write the reference back (hop 4-5); open the report from the ticket (hop 5) | FWD-1 | NOT-EVALUATED | dell2 worker (portal worktree) | LOCAL (DEV only; product file, lands by the portal review route) | worker | -- (builds against the API contract below, not against TV-l-1's output) |
| `TV-d-1` | Deploy: TV-l-1's code and the one new route line, through `safe-apply`, ledger entry opened and closed | FWD-1, FWD-4 | NOT-EVALUATED | ISSUER (a served apply; no worker holds an apply) | WORLD | -- | TV-l-1 drained and merged |
| `TV-r-1` | The one real run (hop 6): an Opal sign-in in Alyssa's role files one request (one household, one account, Overview, default fee) with a real holdings file on DEV, claims it, generates, opens the report from the ticket; the trace record shows ticket id, upload handle, report reference, timestamps | FWD-1, FWD-4 | NOT-EVALUATED | ISSUER | WORLD (a claim to Andrew) | -- | TV-d-1 applied; TV-p-1 on portal DEV; X-1 landed (X-2 answered) |

Status vocabulary: NOT-EVALUATED / BUILT / SERVED / REALIZED.

## The API contract both worker cells build against (fixed here so the cells need no edge)

- **Type definitions.** `TYPE_DEFINITIONS` in the service: key -> {label, questions [{name, kind, required}], attachment (none |
  `analysis_upload`), route key}. `VALID_TYPES` is derived from its keys. The four existing types keep their exact current behaviour
  (no questions, no attachment). `analysis_request`: label "Analysis Request"; questions `advisor` (text, req), `firm` (firm id,
  req), `household` (text, req), `report_type` (one of Overview / Comparison / Multi-Comp, req), `comparison_model` (text, required
  only when report_type is not Overview), `advisory_fee` (number, default stated by the definition), `needed_by` (date), 
  `add_commentary` (boolean, default false); attachment `analysis_upload`.
- **Create.** `POST /api/scoped/tickets` (the internal CREATE route, unchanged authorization) admits, for `analysis_request` only,
  `answers` (object, validated against the definition: unknown key -> 400, missing required -> 400) and `attachment`
  `{upload_id, input_id}` with `input_id` matching `^portfolio_[0-9a-f]{64}$` (400 otherwise; 400 if absent for this type). Stored on
  the item as `answers` and `attachment`; never bytes. `requester_firm` is the answers' `firm`, server-checked by the existing
  `_firm_allowed`.
- **Report reference.** `POST /api/scoped/tickets/{ticketId}/report` body `{request_id, revision?}`: INTERNAL only; only the
  ticket's current assignee; ticket must be `in_progress` and carry an `attachment`; writes `report_ref {request_id, revision,
  recorded_by, recorded_at}` and one `report_recorded` event. Any other body field -> 400. **Per X-2 (msg 929, IRPT_YCDGEN):**
  `POST .../analysis` returns no `report_id`; it returns `NOT_READY`/`QUEUED` with `data.identity.request_id` (+ `revision`), sent
  with `selected_tenant` = the owner firm. The report is read at `GET .../analysis/requests/{requestId}` (and `/pdf`) once `READY`.
- **Self-claim.** `_sod_block` drops the requester clause for every type; the complete-by-non-holder clause stays.

## Write sets (disjoint across slots)

- `TV-l-1` (slot ~1): `infra/aws/lambda/ticket_center/lambda_function.py`; `infra/aws/lambda/ticket_center/tests/test_analysis_request.py`
  (new); `infra/aws/lambda/ticket_center/tests/test_authz_matrix.py` (only where it asserts the requester clause).
- `TV-p-1` (slot ~2): `portal/src/pages/TicketCenter/` (all files), `portal/src/api/endpoints/tickets.ts`, a new test under
  `portal/src/pages/TicketCenter/__tests__/`. READ only: `portal/src/api/endpoints/investor-reporting.ts` and
  `portal/src/pages/InvestorReporting/contracts/wire/*` (the upload door and the submission request are IRPT's).
- **Hookups at the merge (the issuer's, belong to no cell):** `infra/aws/terraform/ticket-center/main.tf` -- one `ticket_routes` line
  `report = "POST /api/scoped/tickets/{ticketId}/report"` and one `ROUTING_MATRIX` entry `analysis_request` (primary
  alyssa@ + manav@, as service_request). CloudFront `/api/scoped/tickets/*` already covers the path (`comp-routes behaviors` #12);
  the existing `lambda:InvokeFunction` permission's `source_arn` is `/*/*`, so no permission is written (a Dell writes none).

## External requests at L5 (not cells; the round's real run waits on both, the builds do not)

- **X-1 -> IRPT_BCKEND's COO.** C-ONE-DOOR's owned dependency (PRD v0.2): the door refuses an `opal-capital` owner
  (`intake/uploads.py:193`) and an actor whose home firm differs from the owner's (`:227-234`). Ruled change: admit an internal
  principal whose `allowedFirmIds` names the owner firm, record both the acting principal and the owner firm, refuse everyone else as
  now. Requested, never written from this project.
- **X-2 -> IRPT_YCDGEN's COO.** C-HANDOFF: confirm `POST .../analysis` with an `input_id` it did not upload from its own page, by an
  internal principal on behalf of the owner firm, is supported, and name the field the report reference returns in.
  **ANSWERED 17:40Z (msg 929, 2.0.0_SA_COO~G2, from code):** supported as-is for an OPAL_GLOBAL principal with `selected_tenant` = the
  owner firm, provided the input was uploaded for that firm (so it rests on X-1); reference `data.identity.request_id`. Not yet
  exercised live (IRPT_YCDGEN F1 is pending Andrew's run). Folded into the contract above before issuance.

**Chains.** A = TV-l-1 (slot ~1) -> TV-d-1 (issuer). B = TV-p-1 (slot ~2). TV-r-1 joins A and B with X-1, X-2. Fan-out 2 of 2 worker
chains, cap 8.

## Rule 24 record

- **MECE over a declared domain.** Domain: the six hops of PRD section 2 plus the contracts they name. By subtraction: hop 1 = TV-p-1
  (form, door call) + TV-l-1 (create admits the type); hop 2 = TV-l-1 (item holds answers + handle); hop 3 = TV-l-1 (self-claim);
  hop 4 = TV-p-1 (the request to `POST .../analysis`) + X-2; hop 5 = TV-l-1 (reference write) + TV-p-1 (write-back, open) ; hop 6 =
  TV-r-1. The door's on-behalf admission = X-1. Remainder: none. Section 3 is the enrichment list, outside this round by construction.
- **Same grain.** One cell per write set; served acts (TV-d-1, TV-r-1) are the issuer's; foreign-owned changes are requests.
- **Intent coherence.** l = the service holds and records; p = the person files and opens; d = the code reaches DEV's served API;
  r = the journey is exercised once.
- **State coherence -- what no cell moves.** No cell writes IRPT's door, store, IAM or generation path; no cell creates a bucket
  (C-ONE-DOOR); no cell adds an alert or notification (C-MORATORIUM; the existing create email is unchanged); no cell writes a
  Lambda permission or bucket policy; nothing reaches PROD; the client submit path and its authorization are unchanged.

## Battery (thread round)

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- thread round; no schedule, hold or gate is created or consumed by the cells.
- `comp-iam`: DECLARED-NOT-APPLICABLE -- the thread touches no IAM: the portal calls IRPT with the user's own session; the new route
  rides the existing integration and the existing `/*/*` invoke permission (main.tf `aws_lambda_permission.tickets_apigw`). X-1 is
  an authorization change inside IRPT's code, run by its own battery.
- `comp-adversary`: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches C-FENCE (FWD-2).
- `comp-routes behaviors` (COO minimum): RUN 17:4xZ -- 30 behaviors parsed, `/api/scoped/tickets/*` (#12) and
  `/api/scoped/investor-reporting/*` (#28) both present; DESIRED plane only (parsed Terraform).
- `comp-blast` (COO minimum): TOOL-FAILED on dell2 -- `cloudops-dell2-agent-user` lacks `secretsmanager:GetSecretValue` on
  `opal/mcp/graph-read-token`; no fallback. Blindness stated: the served graph's dependents of `opal-ticket-api` are unread from
  this seat; the write sets above are drawn from source reads only.
- Drain checks (on no face): `commit-gate.sh` on the touched `.py`; the ticket-center unittest suite once after slot ~1 merges;
  the portal's `tsc -b` and test run once after slot ~2 merges.
