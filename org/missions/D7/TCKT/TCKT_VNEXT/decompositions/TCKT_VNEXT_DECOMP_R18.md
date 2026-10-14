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
| `R18-mt-1` | `meeting_request` definition gains its questions (who, purpose, proposed times) and the coordinator outcome: a route that records confirm or propose-another on the ticket (status, time, by, at, one event row), refused for a non-assignee and for another ticket type; unit tests | FWD-11 | held (v0.5 half) | LOCAL, SERVED at deploy | none |
| `R18-mt-2` | `main.tf`: `meeting_request.primary` = the coordinator (users-table PROFILE confirmed by the CTO), the new route and its permissions; plan only, no apply | FWD-11 | held | LOCAL, SERVED at apply | mt-1 (the route's path and body) |
| `R18-mt-3` | Portal Ticket Center: the filer's Meeting Request form, the coordinator's confirm/propose controls on the ticket page, the filer reading the outcome; DEV candidate | FWD-11 | held | SERVED (client-facing class: Andrew approves) | mt-1 (the wire shape, stated in the order) |
| `R18-mt-4` | The release pair for `opal-ticket-api` and the `terraform` apply (applier seat, `safe-apply`) | FWD-11 | held | WORLD | mt-1, mt-2 |
| `R18-mt-5` | ONE live run on DEV: a synthetic staff user files, the coordinator identity confirms one time, the filer reads it on the same ticket | FWD-11 EXERCISED | held | WORLD | mt-3, mt-4 |
| `R18-tf-0` | **The byte store of the trade form.** Not decidable here: (a) the IRPT upload door takes a second kind, or (b) a new ticket-attachment address from `lib/opal_naming` plus open-from-ticket routes. Asked of `1.0.0_SA_CTO~DELL2` (the v0.5 re-sign carries it) | FWD-10 | **blocked on the CTO** | -- | -- |
| `R18-tf-1..5` | a `trade_form` attachment kind and its checks; the portal upload form (no engine submit) and the release of `TradeRequestParts.tsx` from NFRA_OPSWKF; the open-from-ticket route; the release pair; ONE live run on DEV | FWD-10 | held on tf-0, cut after it | LOCAL to WORLD | tf-0, then a chain |

**Chains (M = 2):** {mt-1, mt-2, mt-4, mt-5 with mt-3 beside mt-1} and {tf-0, tf-1..5}. First issuance fan-out when the half signs:
the FWD-11 chain only, `2 of 2 chains` if tf-0 is ruled by then, otherwise `1 of 2`, cap 8; mt-1 and mt-3 run side by side
once the wire shape is fixed in the order text.

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
