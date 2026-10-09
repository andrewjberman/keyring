# NFRA_OPSWKF decomposition -- ROUND 1 (the FWD-1 thread), 2026-10-09, issuer 2.0.0_SA_COO~O2, dell2

PRD `org/missions/D9/NFRA/NFRA_OPSWKF/prd/NFRA_OPSWKF_PRD.md` v0.2 @d66acfc2d8 (`1.0.0_SA_CTO~DELL2`, msg 2517). Status at
drafting: the ratified-text half is STALE (CVO re-sign owed), so nothing is issued until `prd-signoff.py status` reads
ADMITTED. This file is DRAFT until then.

**Rectangle = the SURFACE MANIFEST's FWD-1 rows S1-S6.** S7 (the SharePoint workbook leg) is enrichment, not round 1.

## Hop walk (FWD-1, every hop real)

H1 the filer opens the trade form in the Ticket Center -> H2 one `trade_request` ticket is created with typed answers ->
H3 the same submit carries the securities to the engine with `ticket_id`; the engine takes the filer from the TOKEN, checks
the ticket, stores one submission, writes `linked_submission_id` and an event on the ticket -> H4 the operations lead
approves or rejects in the engine; each transition appears on the ticket -> H5 Execute on a ticket-originated submission is
refused and recorded; he phones the custodian himself and completes the ticket.

## Field contract (binds every cell; cells run in parallel on it)

- Ticket answers (`trade_request`): `fund` text required; `weights_as_of` date required; `trade_comments` text optional;
  `attestations_confirmed` boolean required. The securities list is NOT a ticket answer (the 200-character text cap,
  `lambda_function.py` ANSWER_TEXT_MAX_CHARS, and no list kind exists); it travels in the engine submission only.
- Engine submission gains: `origin` = `"ticket"` and `ticket_id` (`^TCK-\d{8}-[0-9a-f]{8}$`) when filed from a ticket;
  absent otherwise (every legacy body is byte-for-byte unchanged in behaviour).
- Ticket event rows written by the engine use the ticket service's own `_event_row` shape (`lambda_function.py`), actor
  = the engine principal plus the acting human's email; kinds `trade_linked`, `trade_approved`, `trade_rejected`,
  `trade_execute_refused`. Status: APPROVED -> `in_progress`; REJECTED -> `completed`; the operations lead completes an
  approved ticket himself through the existing complete action.

| cell | builds | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|
| `OW-l-1` | S1: the `trade_request` entry in `TYPE_DEFINITIONS` gets the four questions above; nothing else in `lambda_function.py` changes; new test file proves a valid create, each required answer refused when missing, and the four untyped types unchanged | FWD-1 | NOT-EVALUATED | dell2 worker | WORLD (path floor: a Lambda handler; the worker applies nothing) | worker-light | -- |
| `OW-e-1` | S4 (C-INITIATOR): `submission_handler.py` takes the initiator from the authorizer context (`requestContext.authorizer.lambda.email`, the workflow handler's existing read); no context -> 403; a body `initiator_email` that disagrees -> 403; tests | FWD-1 | NOT-EVALUATED | dell2 worker | WORLD (path floor) | worker | -- |
| `OW-e-2` | S3 (the bridge): `submission_handler.py` accepts optional `ticket_id`; reads the ticket (`opal-tickets`); refuses unless type `trade_request`, `created_by` == the token email, no `linked_submission_id`, `answers.fund` == body `fund`; stores `origin`/`ticket_id`; then a CONDITIONAL update writes `linked_submission_id` + a `trade_linked` event (condition: attribute absent); tests with a stubbed table | FWD-1 | NOT-EVALUATED | dell2 worker | WORLD (path floor) | worker | OW-e-1 drained (same file) |
| `OW-e-3` | S5 + S6: `workflow_handler.py` -- (a) after an APPROVE/REJECT on a submission carrying `ticket_id`, append the event and move the ticket status per the field contract; (b) `handle_execute` on `origin == "ticket"` returns 409 BEFORE any status write, S3 put or `send_brokerage_email`, and appends `trade_execute_refused`; tests prove the email function is never called | FWD-1 | NOT-EVALUATED | dell2 worker | WORLD (path floor) | worker | -- |
| `OW-i-1` | `infra/aws/terraform/trade-pipeline/iam.tf`: `dynamodb:GetItem` + `dynamodb:UpdateItem` on `table/opal-tickets` for the role the submission and workflow Lambdas run as; `lambdas.tf`: `TICKETS_TABLE = "opal-tickets"` on those two functions; `terraform validate` | FWD-1 | NOT-EVALUATED | dell2 worker | WORLD (path floor: Terraform; the worker applies nothing) | worker-light | -- |
| `OW-p-1` | S2: `portal/src/pages/TicketCenter/TradeRequestParts.tsx` (new): fund, weights date, securities grid, attestations, comments; ONE submit = ticket create with answers, then `POST /api/general/trades/submit` with `ticket_id` + securities; reuses the TradeSubmission page's types and API client read-only; plus ONE `trade_request` branch in `TicketCenter.tsx` beside `:219-229` mounting it, nothing else in that file (X1, granted by `~V2` msg 2522); typecheck + lint clean | FWD-1 | NOT-EVALUATED | dell2 worker (portal worktree) | LOCAL (DEV; CTO review route: product file) | worker | -- |
| `OW-d-1` | Deploy: an apply order to `0.7.0_AE_CloudOps~DELL2` -- the ticket Lambda artifact built from the merged HEAD (it carries TCKT_VNEXT's code too), the two trade Lambdas, and the `trade-pipeline` Terraform. Ledger opened and closed. After-reads: deployed bytes against the build; a legacy submit body (no `ticket_id`) still accepted with the token identity | FWD-1 | NOT-EVALUATED | ISSUER cuts the apply order; the applier applies | WORLD | -- | OW-l-1, OW-e-2, OW-e-3, OW-i-1 drained |
| `OW-r-1` | The real run on DEV: a seat files one trade request through the form; the ticket shows `linked_submission_id`; an approve shows on the ticket; Execute is refused and the refusal is on the ticket; no email left SES for it | FWD-1 | NOT-EVALUATED | ISSUER | WORLD | -- | OW-d-1 closed; OW-p-1 on DEV |

Status vocabulary: NOT-EVALUATED / BUILT / SERVED / REALIZED. FWD-1's organic arm is the operations lead's first real
request; it is recorded, never waited on.

## WORKSTREAM K -- FWD-7, the operations lead's starter kit (PRD v0.3 @1698a6a69d, C-OPS-KIT, S8; parallel to the thread)

A disjoint surface: one new folder `tools/ops_kit/`, which touches no ticket, engine or portal file. Runtime is the Python
standard library (build ladder rung 3): `python serve.py` serves one static page and one JSON route on localhost. There is
no install step and no AWS SDK.

| cell | builds | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|
| `OW-k-1` | `tools/ops_kit/`: `serve.py` (stdlib HTTP server, localhost only); `adapter.py` (THE one data entry, `get_panel(name)`; mode `fixture` today, a stub `mcpindex` mode reading `OPAL_MCP_URL`/token from env, never AWS); `fixtures/trade_rec.json`, `fixtures/billing.json`; `static/index.html` + `app.js` + `theme.css` with the trade-rec and billing panels and a visible "source: fixture" stamp per panel; `README.md` (one command; "ask your Claude to change anything"; "more data = ask Opal"); a `CLAUDE.md` for his Claude (where layout lives, never touch `adapter.py`'s contract). Criteria: `python tools/ops_kit/serve.py --selftest` exits 0 and prints both panels' row counts with `source=fixture`; a scan of the folder for `boto3|aws_access_key|aws_secret` prints 0 hits; `theme.css`'s canvas/panel/ink tokens equal the portal colour-law values the worker cites by path | FWD-7 | NOT-EVALUATED | dell2 worker | LOCAL | worker | -- |
| `OW-k-r-1` | The real run: the kit unzipped into an empty folder starts with one command and shows both panels; a fresh Claude session given only the kit changes one panel's layout, and `git diff` on Opal's tree shows nothing outside the copy; the zip lands in his SharePoint (location read at the run) | FWD-7 | NOT-EVALUATED | ISSUER | LOCAL (+ one SharePoint upload) | -- | OW-k-1 drained |

Live data in the kit (FWD-7's "live data" clause) waits on X2; the fixture stamp says so on every panel until then.

## External requests (not cells)

- **X2, trade-rec and billing readers in NFRA_MCPINDEX** (site Z, `2.0.0_SA_COO~MI`), in the shape `OW-k-1`'s fixtures
  publish. This is a cross-fabric ask, routed by `1.0.0_SA_CTO~DELL2` (MSTR to MSTR). The kit switches `adapter.py` to
  `mcpindex` mode when the readers are served; nothing else changes.
- **X1, the form's mount** in `portal/src/pages/TicketCenter/TicketCenter.tsx`: GRANTED by `2.0.0_SA_COO~V2` (msg 2522,
  the C-SHARED-SURFACE owner) -- ONE `trade_request` branch beside `:219-229`, nothing else; folded into OW-p-1. Owed back
  to `~V2`: the portal DEV hash once OW-p-1 lands (its AR-v-11 cuts from DEV after it).

## Write set

- `OW-l-1`: `infra/aws/lambda/ticket_center/lambda_function.py` (the `trade_request` entry ONLY);
  `infra/aws/lambda/ticket_center/tests/test_trade_request_type.py` (new).
- `OW-e-1`, `OW-e-2`: `infra/aws/lambda/trade-pipeline/trade-submission-handler/src/submission_handler.py`;
  `.../trade-submission-handler/tests/test_initiator_from_token.py` (new, e-1); `.../tests/test_ticket_bridge.py` (new, e-2).
- `OW-e-3`: `infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/workflow_handler.py`;
  `.../trade-workflow-handler/tests/test_ticket_writeback_and_fence.py` (new).
- `OW-i-1`: `infra/aws/terraform/trade-pipeline/iam.tf`, `infra/aws/terraform/trade-pipeline/lambdas.tf`.
- `OW-k-1`: `tools/ops_kit/**` (new folder, nothing outside it).
- `OW-p-1`: `portal/src/pages/TicketCenter/TradeRequestParts.tsx` (new); `portal/src/pages/TicketCenter/TicketCenter.tsx` (the one X1 branch).

**Chains.** A = OW-l-1; B = OW-e-1 -> OW-e-2; C = OW-e-3; D = OW-i-1; E = OW-p-1; all join at OW-d-1 -> OW-r-1.
K = OW-k-1 -> OW-k-r-1. Fan-out 6 of 6 chains, cap 8.

## Rule 24 record

- **MECE over a declared domain.** Domain: the manifest's FWD-1 rows S1-S6. By subtraction: S1 = l-1; S2 = p-1 (+ X1);
  S3 = e-2; S4 = e-1; S5 = e-3(a); S6 = e-3(b); i-1 is the grant S3 and S5 need; d-1 serves them; r-1 exercises them.
  Remainder: (1) FWD-1's ACCEPT says "an advisor files"; the Ticket Center is internal-only today
  (`portal/src/App.tsx:500-506`, `firmAccess.ts:104-113`) and the client `/submit` takes no answers. DONE WHEN reads "a
  seat files", so round 1 is whole; advisor reach goes to the round-1 analysis as an enrichment item. (2) The
  TCKT_VNEXT firm-scope work (SA-k-1) is that project's.
- **Same grain.** One worker cell per write set; served acts are the issuer's and the applier's.
- **Intent coherence.** l = the type takes a shape; e = the engine trusts the token and binds one ticket; i = the grant;
  p = one form; d = served; r = exercised once.
- **State coherence: what no cell moves.** The TradeSubmission page and its legacy submit bodies (except that the
  initiator now comes from the token); every `BROKERAGE_EMAILS` value; the Execute path for non-ticket submissions;
  the other ticket types, the client submit path, TCKT_VNEXT's routes; no notification, alert or monitor is added.

## Battery

- `comp-iam`: APPLICABLE to OW-i-1 (a new grant on an existing table to an existing role); run at the cut.
- `comp-schedule`: DECLARED-NOT-APPLICABLE -- no schedule, hold or gate is created or consumed.
- `comp-adversary`: APPLICABLE at the drain on OW-e-1/e-2/e-3 (an identity change and a fence).
- Drain checks (on no face): `commit-gate.sh` on every touched `.py`; the whole ticket-center suite and both trade
  handler suites once after the merge; portal typecheck on DEV.
