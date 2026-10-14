# Andrew-direct 2026-10-14 ~11:5xZ (laptop, 1.0.0_SA_CTO terminal) -- an "opal-data-harvest" tool set for the asset managers, through the gateway MCP

## VERBATIM

> "Ok it's time to drive, make sure that MCPINDEX has work associated with the asset manager test. we need an 'opal-data-harvest' tool
> set that hits the various items there on a company search and can pull full analysis from the various buckets. I recommend issuing
> a message over to sitez and have their CRO assess the silver and gold layers in opal-data-harvest and come up with a series of
> tools for searching individual securities across the various vectors, which I think should include not only the published/platinum
> material on the portal, but also individual columns/features in those gold and silver layers."

Read with his word of ~11:4xZ, from the same session's record `ANDREW_DIRECT_20261014_114xZ_EIGHT_OPEN_CALLS_ANSWERED.md` (call 7):

> "The true test for her [lauren@opalinvest.com] is actually going to be setting up her access from the Claude GUI App to the
> opalgateway mcp with the relevant skills/mcp. The frontend is just a visual/exploratory layer, but I think the operational
> day-to-day work layer will be this MCP."

## What this sets

1. **The asset-manager test is an MCP test.** Lauren, in the Claude desktop app, connected to the opalgateway MCP with the relevant
   skills, searches a company and gets its full analysis. The MC Portal page is the visual layer. NFRA_MCPINDEX's FWD-21 (harvest) is
   graded on that MCP use, not on the portal.
2. **The tool set, named `opal-data-harvest`, served through the gateway MCP:**
   - a COMPANY search: one security, by ticker, name, CUSIP or ISIN, across every vector the harvest holds;
   - returning the FULL analysis, pulled from the various buckets;
   - three layers covered:
     - the published and platinum material the portal shows;
     - the individual columns and features in the GOLD layer;
     - the individual columns and features in the SILVER layer.
3. **Who does what:**
   - **Site Z's CRO (`4.0.0_SA_CRO~Z`) assesses first.** It reads the silver and gold layers of `opal-data-harvest`, plus the
     platinum and published material, and proposes the series of tools: which searches, over which vectors, keyed how, returning
     which columns. The proposal reaches site Z's CTO as the L1 input.
   - **NFRA_MCPINDEX carries the build** (site Z's `1.0.0_SA_CTO~Z`, COO `~MI`), with the gateway grant on NFRA_OPLGTW. The
     project's next round analysis cuts it.
4. **Bounds already ruled, still standing:**
   - Opal users only, managed by gateway entitlements; non-Opal principals stay refused (dell1 call `ce58`, Andrew ~20:0xZ
     10-13);
   - dell1's servable-prefix list v4 (`7e0da2dfee`) is the starting map of what may be served;
   - no new vendor call is made by a search; it reads what the harvest already holds.

## The CRO's assessment, when delivered, names

- **Per layer:** the datasets, their keys (how a security is identified), the columns and features worth exposing, freshness, and row
  counts.
- **The proposed tools:** for each, name, input, output columns and the layer it reads.
- **One worked example:** one real company, end to end, across all three layers.
- What it could not read, and why.
