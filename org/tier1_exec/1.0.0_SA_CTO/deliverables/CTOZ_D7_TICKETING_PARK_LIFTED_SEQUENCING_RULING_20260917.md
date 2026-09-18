# D7 OPAL TICKETING -- PARK LIFTED. This seat's SEQUENCING RULING.

**Author:** `1.0.0_SA_CTO~Z`. **Trigger:** `0.0.0_AB_MSTR~Z` msg 23589, relaying the laptop `1.0.0_SA_CTO`: Andrew-direct at
that terminal lifted D7 Opal Ticketing's park, **client view first**, named D7 a SITE-Z directive, and left the SEQUENCING to
this lane. His words are not quoted here because this seat did not hear them; they are relayed, and the relay is the record.

## 1. STATE AT THE LIFT, MEASURED (not read off the register's prose)

| what | measured |
|---|---|
| register row | `org/projects/OPAL_TICKET_VNEXT.json`: `dep_stage REGISTERED`, `status active`, `coo_lane` null, `fabric` null |
| directive row | D7 live, device SITEZ, `open_tos 0`, one member project `OPAL_TICKET_VNEXT` |
| stage gate, from its own `blocking` field | Rule 27 stage 2 (purpose-level PRD) SATISFIED @`c2837692bc` (`docs/architecture/D7_TICKET_VNEXT_PRD.md`); **stage 3, the COO decomposition, OUTSTANDING. No task order may precede it.** |
| specs on disk | `D7_TICKET_VNEXT_PRD.md`, `D7_TICKETING_INTAKE_PRD.md`, `D7_TICKET_CENTER_IA_VARIANT_SPEC.md` |
| the system that already exists | live DynamoDB `opal-tickets` (12 items, key `ticket_id`, GSI `status-index`); `infra/aws/lambda/ticket_center/` with four test suites; `infra/aws/terraform/ticket-center/`; `integrations/ticketing/intake/`; portal `src/pages/TicketCenter/`. **86 tracked files carry the token.** Zero Lambda function names contain "ticket", so the ticket center's own deploy target needs naming before any deploy claim |
| tree home | NONE. This is a LEGACY FLAT project, so first pickup is also its L3 landing into `org/missions/D7/...` under the tree grammar |
| COO capacity | 1 live COO lane on this box, `2.0.0_SA_COO~Z`, holding AMGT_RESAPP round 13. No cap ruled for this box |

## 2. THE RULING

1. **D7 STARTS NOW, at this seat's own limbs, and those consume no COO slot.** In order: the source-architecture read its own
   phase field names (begun above and continued next), then the **L3 tree landing**, then the **L4 PRD**.
2. **CLIENT VIEW FIRST is the L4's scope boundary**, read narrowly: the client-facing ticket view is the first cut. The agent
   and internal views, the attachment and transcript store, and the notification semantics are named as later cuts in the PRD
   rather than built into the first one. The bucket shape is not changed, per the register row's own standing instruction.
3. **NO COO LANE IS ASKED FOR UNTIL AMGT_RESAPP ROUND 13 DRAINS.** `2.0.0_SA_COO~Z` holds AMGT_RESAPP as its one project, and
   one project per Tier-2 seat instance binds at the seat. So D7's L5 decomposition and L6 issuance wait on that drain, or on
   a SECOND COO lane, which is a seating act plus a capacity question.
4. **The capacity question is Andrew's, and it is a card, not an assumption:** running D7's decomposition beside AMGT round 13
   needs a second live COO lane on this box. This seat does not seat it and does not ask for it while the round is draining.
   If he wants D7 decomposed in parallel, that word seats the lane.
5. **The `/self-drive AMGT_RESAPP` loop's scope is NOT widened.** D7 is driven at this seat's limbs, outside the loop, and the
   loop keeps reporting AMGT_RESAPP only. Nothing about round 13 changes.

## 3. WHAT THIS RULING DOES NOT DO

It does not cut a task order, does not touch the existing ticket center's live surfaces, does not rule the attachment store
or the notification design, and does not read Andrew's words wider than the relay carries them. The intake identity and the
Graph discovery legs named in the directive's `stance` stay where they are: at Andrew.
