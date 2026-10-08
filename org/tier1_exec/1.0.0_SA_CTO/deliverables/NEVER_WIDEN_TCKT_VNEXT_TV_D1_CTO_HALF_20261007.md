# Never-widen CTO half -- TCKT_VNEXT TV-d-1: the ticket service's round-1 code and one new route

Signer `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~19:1xZ. **Packet:**
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/TV_D1_DEPLOY_PACKET_20261007.md` @41443247bb (COO half SIGNED).

## A correction to the packet's scope, read by this seat

The packet's title says "DEV's served API". It is not DEV's alone:
- `infra/aws/terraform/ticket-center/main.tf:31` tags the stack `Environment = "Production"`;
- `:38` attaches the route to `portal_api_id = "7k3ed8px20"` ("opal-portal-data-proxy-api (shared; routes are pure-add)");
- there is one function, `opal-ticket-api`.

**This release changes the ONE live Ticket Center service behind every portal, PROD included.** The packet's behavioural reading still
holds:
- the new type is on the INTERNAL create route only;
- the client SUBMIT path is unchanged;
- CLAIM and COMPLETE stay internal-only.

So the half is signed, with that scope named.

## SIGNED, for exactly this act

1. **Code:** `opal-ticket-api` at CLOUD `da43155418`, package sha256 `y0UFtRIfZxu3x6BCFSGLjXsNgScCl/GPuWNHbmZV7BI=`.
2. **Environment:** its `ROUTING_MATRIX` value gains `analysis_request`.
3. **Route:** one new route, `POST /api/scoped/tickets/{ticketId}/report` (custom authorizer, the existing integration).
4. **Plan:** it must re-plan at apply to 1 / 1 / 0, with only these. Anything else is outside this half.
5. **Rollback:** re-apply the `481dde1dbf` build (`/38K...`) and remove the route line. Table items written meanwhile stay readable by
   the old code.

**The one widening** is the requester-claim removal: an internal person may claim and complete a ticket they filed. It is Andrew's
2026-09-30 ruling for all tickets (PRD C-SELF-CLAIM). Clients still cannot claim, because the route matrix is unchanged.

## Conditions

1. **The ledger names the PROD scope:** "the live Ticket Center for every portal", not DEV.
2. **After-reads, beyond the packet's:**
   - (a) the PROD portal's ticket list returns its existing tickets unchanged in count;
   - (b) a client principal's claim is still refused;
   - (c) an existing type's create still stores exactly the fields it stored before.
3. **Notifications:** `ROUTING_MATRIX` makes Manav and Alyssa the primaries for `analysis_request`, so a seat's test ticket emails them
   through the existing SES path. Test tickets carry a test marker in the title, and the ledger names who was notified. No new
   notification path is built (moratorium).

-- 1.0.0_SA_CTO~DELL2
