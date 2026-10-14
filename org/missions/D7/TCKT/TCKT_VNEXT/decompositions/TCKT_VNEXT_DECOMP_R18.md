# TCKT_VNEXT decomposition -- ROUND 18, 2026-10-14, issuer 2.0.0_SA_COO~V2, dell2 (DRAFT: nothing cut)

**Authority:** PRD v0.5 ADDENDUM 5 @1bf1db1b0f (`org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md`, FWD-10 and FWD-11, due 2026-10-24 on dell2),
Andrew-direct ~17:3xZ and ~18:3xZ 2026-10-14; the CTO's re-seat msg 7806. Round 17 cut nothing (CTO analysis @0a18c286a5), so this is the
first cut of the two outcomes. **Nothing is cut yet:** the ratified-text half reads STALE (`prd-signoff.py status TCKT_VNEXT`, owed by
`3.0.0_SA_CVO~DELL2`), and `.tools/to-pipeline-gate.py` LIMB 6 refuses a newly added order against an unsigned half.

## Measured shape (read at HEAD, box/dell2)

- `infra/aws/lambda/ticket_center/lambda_function.py:88-97`: `trade_request` is a definition (firm, fund, weights_as_of, trade_comments,
  attestations_confirmed; attachment None); `meeting_request` exists with NO questions and NO attachment. Attachment kinds: only
  `analysis_upload` (`_validate_attachment`, :753-758, "unreachable until a second attachment kind is defined").
- `infra/aws/terraform/ticket-center/main.tf:363-390`: `ROUTING_MATRIX` is config. `meeting_request.primary` is manav and alyssa today.
  The main.tf names no S3 bucket: the ticket service has no byte store.
- Routes: `claim`, `complete`, `report`, `package` (`lambda_function.py:1894`). There is no meeting-outcome route.
- Portal `portal/src/pages/TicketCenter/TradeRequestParts.tsx` is NFRA_OPSWKF's engine-submit form (project on HOLD; its 409 defect uncut).

## Cells

| cell | builds | outcome | status | risk | depends on |
|---|---|---|---|---|---|
| `R18-mt-1` | `meeting_request` definition gains its questions per C-MEETING-REQUEST (firm via C-FIRM-CHOICE, who, purpose, up to three proposed times) and the coordinator outcome: a route that records confirm or propose-another on the ticket (status, time, by, at, one event row), refused for a non-assignee and for another ticket type; unit tests | FWD-11 | held (v0.5 half) | LOCAL, SERVED at deploy | none |
| `R18-mt-2` | `main.tf`: `meeting_request.primary` = the coordinator (users-table PROFILE confirmed by the CTO), the new route and its permissions; plan only, no apply | FWD-11 | held | LOCAL, SERVED at apply | mt-1 (the route's path and body) |
| `R18-mt-3` | Portal Ticket Center: the filer's Meeting Request form, the coordinator's confirm/propose controls on the ticket page, the filer reading the outcome; DEV candidate | FWD-11 | held | SERVED (client-facing class: Andrew approves) | mt-1 (the wire shape, stated in the order) |
| `R18-mt-4` | The release pair for `opal-ticket-api` and the `terraform` apply (applier seat, `safe-apply`) | FWD-11 | held | WORLD | mt-1, mt-2 |
| `R18-mt-5` | ONE live run on DEV: a synthetic staff user files, the coordinator identity confirms one time, the filer reads it on the same ticket | FWD-11 EXERCISED | held | WORLD | mt-3, mt-4 |
| `R18-tf-0` | RULED (b) by `1.0.0_SA_CTO~DELL2` msg 7818, PRD v0.6 @c578883de8 (C-ATTACH): the trade form lives at a `lib/opal_naming.address()` address under the ticket's FIRM; presigned upload and open after C-FENCE; never the Analysis door; `TradeRequestParts.tsx` released to this project, upload only, engine submit unwired | FWD-10 | done | -- | -- |
| `R18-tf-1` | The registry row and the address: the `infra/logic/registry/` row a builder refusal asks for, and the printed `address()` output for the ticket-attachment key (rule 30); no hand-typed address | FWD-10 | held (v0.6 half) | LOCAL | tf-0 |
| `R18-tf-2` | `trade_request` definition per C-TRADE-REQUEST: questions firm (C-FIRM-CHOICE, the explicit `allowedFirmIds` check) and the form upload; checks a file is present, kind PDF/XLSX/CSV, size cap; the presigned upload route and the presigned open route, each after C-FENCE; no engine call; unit tests | FWD-10 | held | LOCAL, SERVED at deploy | tf-1 (the address) |
| `R18-tf-3` | `main.tf`: the ticket Lambda's permission on that prefix, plan only. The BUCKET POLICY is a laptop role request (C-DEPLOY): a pre-arranged input with an owner, sent the moment tf-1 prints the address | FWD-10 | held | LOCAL, SERVED at apply | tf-1; the laptop's policy (named input, owner laptop `0.0.0_AB_MSTR`) |
| `R18-tf-4` | Portal: the Trade Request upload form (firm chosen, file chosen, placeholder form named as such), the file opened from the ticket page, `TradeRequestParts.tsx` reworked upload-only with the engine submit unwired; DEV candidate | FWD-10 | held | SERVED (client-facing class: Andrew approves) | tf-2 (the wire shape, stated in the order) |
| `R18-tf-5` | The release pair for `opal-ticket-api` and the apply (applier seat, `safe-apply`), beside `R18-mt-4` as ONE release if both are ready | FWD-10 | held | WORLD | tf-2, tf-3, the laptop's policy |
| `R18-tf-6` | ONE live run on DEV: a synthetic staff user chooses Trade Request and a firm, uploads the placeholder form, submits; the OPEN ticket's form is opened from the ticket page | FWD-10 EXERCISED | held | WORLD | tf-4, tf-5 |

**Chains (M = 2):** {mt-1, mt-2, mt-4, mt-5 with mt-3 beside mt-1} and {tf-1, tf-2, tf-3, tf-5, tf-6 with tf-4 beside tf-2}. tf-0 is
ruled. First issuance when the v0.6 half signs: `2 of 2 chains`, cap 8. The first six cuts are mt-1, mt-3, tf-1, then tf-2 and tf-4
(their wire shapes fixed in the order text) and mt-2; tf-3 and the release cells follow their inputs. The two lambda cells (mt-1 and
tf-2) edit one file, `lambda_function.py`: they take ONE worker chain or two disjoint functions under one merge order, never two
parallel workers on the file; the issuance states which.

## WIRE CONTRACT (fixed by the issuer at the cut; every order cites it; a change is an AMENDMENT to each order it touches)

PRD v0.6 C-MEETING-REQUEST, C-TRADE-REQUEST, C-ATTACH, C-FIRM-CHOICE, C-FENCE. Three new routes, all on the existing API, authorizer and
CloudFront behavior `/api/scoped/tickets/*`:

1. `POST /api/scoped/tickets/{ticketId}/meeting` (route name `meeting`). Body: `{"action":"confirm","time":"<one of the ticket's
   answers.proposed_time_1..3>"}` or `{"action":"propose","times":["<text>", ...]}` (1 to 3 non-empty strings, each at most 200 characters).
   Caller: an INTERNAL human whose email is in the ticket's `routing.primary` (the coordinator); anyone else 403. Ticket: type
   `meeting_request`, status not `completed`, else 409. Effect: sets `meeting = {"status": "confirmed"|"rescheduled", "time": <string or
   null>, "proposed_times": [<strings>], "by": <email>, "at": <iso>}` with a condition that the status is not `completed`, appends ONE
   event row (`meeting_confirmed` or `meeting_proposed`), changes nothing else (the ticket stays open; `complete` is the existing route).
   200 returns `{"ticket_id": ..., "meeting": {...}}`. A confirm whose `time` is not one of the three answers: 400. `get_one` and `list`
   return the `meeting` member whole.
2. `POST /api/scoped/tickets/attachment-upload` (route name `attachment_upload`). Body: `{"firm":"<firm id>","filename":"<name>",
   "content_type":"<mime>","size":<int bytes>}`. Caller: an INTERNAL human; `firm` must pass `_create_firm_allowed(pc, actor, firm)`
   exactly as CREATE does (the allowed list AND the caller's own PROFILE scope; C-FIRM-CHOICE: the same server check, the choice never
   the body's say-so). `content_type` one of `application/pdf`, `text/csv`,
   `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`; `size` an integer from 1 to 10485760; the filename's extension
   (`.pdf`, `.csv`, `.xlsx`) must agree with the type. 200 returns `{"upload_url":"<presigned PUT, 300 s>","attachment":{"key":
   "<prefix><32 hex>/<safe filename>","filename":..., "content_type":..., "size":...}}`, where `<prefix>` is `KEY_TEMPLATE.format(firm=<firm>)`.
   The presign is for exactly that key and content type. The bucket is env `TICKET_ATTACH_BUCKET` and the key template is env
   `TICKET_ATTACH_KEY_TEMPLATE` (it contains `{firm}` exactly once and ends with `/`; its value is the builder output of
   `TO-R18-TR1`, for example `portal/{firm}/bronze/ticket-attachments/trade-form/`); either unset or malformed: 503 and nothing
   presigned. Bytes never pass through the Lambda.
3. `GET /api/scoped/tickets/{ticketId}/attachment` (route name `attachment_open`). Caller and fence exactly as `get_ticket` (C-FENCE);
   the ticket must carry an `attachment` whose `key` starts with `KEY_TEMPLATE.format(firm=<the ticket's answers.firm>)`, else 404. 200 returns
   `{"url":"<presigned GET, 300 s, Content-Disposition attachment with the filename>","filename":..., "expires_in":300}`.

`trade_request` CREATE (existing `POST /api/scoped/tickets`, internal human): `answers.firm` (required, in `allowedFirmIds`) and
`attachment` = `{"key","filename","content_type","size"}` exactly the member set the upload route returned; the key must start with
`KEY_TEMPLATE.format(firm=<answers.firm>)` and every other member is re-checked (type list, size cap, extension). The old trade questions (`fund`,
`weights_as_of`, `trade_comments`, `attestations_confirmed`) stay in the definition as NOT required, so a held engine-path ticket
still reads. No call to the trade engine. `meeting_request` CREATE: `answers` = firm (required, `allowedFirmIds`), `who` (text,
required), `purpose` (text, required), `proposed_time_1` (text, required), `proposed_time_2` and `proposed_time_3` (text, optional).
`ROUTING_MATRIX.meeting_request.primary` = `["jeanette@opalinvest.com"]`.

## Rule 24 record

- **MECE over FWD-11's DONE WHEN.** Domain: the sentence (files, lands in the coordinator's queue, confirms or proposes, the filer sees
  it). By subtraction: files = mt-1 definition and mt-3 form; queue = mt-2 routing; confirms/proposes = mt-1 route and mt-3 controls;
  the filer sees it = mt-1 stored outcome and mt-3 view; DEV run = mt-5. Nothing uncovered.
- **Same grain:** one cell per surface (lambda, terraform, portal, release, run). **State coherence:** a confirmed outcome does not
  complete the ticket; the coordinator's completing it is the existing `complete` route, unchanged.
- **Names this draft does not choose:** the route's path, the field names of the stored outcome and any new address are rule-30 output,
  printed at the cut; none is typed here.

## Battery

comp-schedule: DECLARED-NOT-APPLICABLE (no schedule). comp-iam: for mt-2 a permission is added to the ticket Lambda role; the run
and the gap read ride that cell. comp-adversary: the check of mt-5 is a live re-read of the ticket by an identity that did not
write it. Every check is dry-run at the base when the order is cut, not before.
