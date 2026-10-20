# ANDREW-DIRECT 2026-10-20 ~16:xxZ -- entitlement add/subtract at mcp.opalinvest.dev/opalgateway; advisor tables linked per vendor

Channel: typed by Andrew at the `1.0.0_SA_CTO~Z` terminal (Claude Code session), ~16:xxZ (12:xx PM ET).

## VERBATIM

> I need you to continue optimizing the mcportal and mcpindex, we want this functionality to be perfect for opalgateway.
> something id like threaded into this is the ability to add and subtract entitlements for various channels with ease for users
> at the mcportal itself, i.e. at mcp.opalinvest.dev/opalgateway. let's make sure that functionality is possible and put into the
> build there by COO~MP (you may need CRO~Z to analyze what is there currently and write a brief on the subject so you can fold
> this into their workstream depending on how much is done currently). Regarding COO~MI and MCPINDEX, we just need to make sure
> all tables for the advisors are properly linked up, which means making sure that the tools we build actually drop them off at
> the right tables, because there are differnet tables inhernetly coming from Orion/Eclipse/SmartX/Schwab/etc., they are not all
> named the same thing, so making tooling as if they all have the same names and structure of course would not be accurate. That
> is another thing that needs to be investigated by CRO~Y who will need to be spawned so that we see where we really stand when it
> comes to those details and what needs to be built/modified.

## Recorded as said, not adjudicated here

1. **NFRA_MCPORTAL (`2.0.0_SA_COO~MP` builds):** at `mcp.opalinvest.dev/opalgateway`, a way to add and subtract each user's
   entitlements per channel, with ease. `4.0.0_SA_CRO~Z` first analyzes what exists and writes a brief. The CTO folds it into
   COO~MP's workstream according to how much is already built.
2. **NFRA_MCPINDEX (`2.0.0_SA_COO~MI`):** every advisor table is properly linked. The tools must land on the right tables per
   vendor, because Orion, Eclipse, SmartX, Schwab and the others are named and structured differently.
   `4.0.0_SA_CRO~Y`, a new spawn, investigates where this stands and what must be built or modified.
3. Both continue the goal of making the gateway work "perfect for opalgateway".
