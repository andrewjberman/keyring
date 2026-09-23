# ANDREW-DIRECT 2026-09-23 ~18:5xZ -- opal_ai microproduct repo brief (Opal Analyst as a three-slice product)

**Channel:** Andrew-direct at the `4.0.0_SA_CRO~X` terminal (site Z / SITEZ fabric), in-session, ~18:5xZ 2026-09-23
(~2:5x PM Eastern).
**Received by:** `4.0.0_SA_CRO~X`.
**Recorded by:** `4.0.0_SA_CRO~X`, same turn, before any research act.

## Verbatim (typos his, preserved -- THE PHRASING IS THE RULING)

> I need you to look for a brief and prior art as it pertains to making the Opal Analyst a microproduct. We had been
> discussing at one point on this fabric how the GRAPHQL work for opal analyst, OPLGTW, MCPINDEX, and all of this work
> kind of centers around the same one product at differnet layers, which is a modular MCP template setup with proper
> tool call indexing, and an agent that has access and instruction/guardrails around using those tools and
> functionalities. I think there are two layers to this that need to be consiered. First, it is obvious that it needs
> to be a microproduct; it needs its own repo. Second, there are three slices of how this needs to be organized, i.)
> The Opal Implementation: this one comes first, it is the aggregation of all the projects and concepts I listed
> earlier in this message. This is the priority to complete and execute effectively, a teams-based agent that can
> access all the right info and fast/economically/accurately, by tool-calling the firm's MCP. ii.) The Template
> Implementation; after completing a proper V1, even V2 of the Opal Agent, we need to figure out how to modularize it
> for other firms, that means modularizing both the agent and its dynamics/structure, as well as how the MCP is set up
> and the associated patterns for how we build out access to the vendors (look at how Opal handles this for Schwab,
> Black Diamond, and others; official API if we got it, not official API if we don't, with the EC2 cookie crawler and
> lambda REST API, with the self-heal. Also want to template stuff like "The Walk" where we walk an authenticated
> session to do endpoint discovery for a new vendor. iii.) The Client Implementation; this is where we take the
> template and mold it to a Client's specific needs, basing the tool calls around their database and vendors. We need
> a brief that basically ties all this stuff together in a new repo, opal_ai. This repo should be structured in a
> manner that considers the above format in all cases, because all products will follow this journey. We build i.)
> for ourselves first, this is our first internal beta. Then we create ii.) which is our modular form, this should be
> kept very clean and separate in a designated place in the repo, lastly we build the versions for clients which need
> to be held in their own subfolders and directory system. Please do a deep dive on all opal analyst work, all opal mcp
> work, the structures guardrails functions tools, look into our comp-tooling work as this could inform indexing
> functions, look at the MCPINDEX to see current state of that work, compile all of this and write a brief for the
> opal_ai repo.

## What this seat reads as asked (surfaced, NOT adjudicated)

- ONE deliverable: an L1 BRIEF for a new repo `opal_ai`, authored by this seat under `/brief-create`, compiling prior
  art from: Opal Analyst (incl. its GraphQL work), `NFRA_OPLGTW`, `NFRA_MCPINDEX`, the Opal MCP surfaces (structures,
  guardrails, functions, tools), comp-tooling as indexing prior art, and the vendor-access patterns (Schwab, Black
  Diamond, others; official API / unofficial API via EC2 cookie crawler + Lambda REST + self-heal; "The Walk").
- The brief's frame is his: the repo is a microproduct; three slices in order -- (i) Opal implementation (first,
  internal beta, the priority), (ii) template (clean and separate, a designated place), (iii) client implementations
  (their own subfolders).
- ⚠ NOT asked, and not done by this seat: creating the repo, registering a project code, writing an endpoint or PRD,
  decomposing, dispatching, moving any in-flight project (`NFRA_OPLGTW`, `NFRA_MCPINDEX`, Opal Analyst work) into the
  new repo. The brief is CTO intake at L2 (`/endpoint --forward`). Whether any in-flight project is re-homed under it
  is for the CTO and Andrew; this record does not widen or narrow his word.

## Broadcast

Same turn, MCP to CTO + COO + MSTR (site-Z lanes live at the time, plus base serials where live). Message ids are in the
session log.
