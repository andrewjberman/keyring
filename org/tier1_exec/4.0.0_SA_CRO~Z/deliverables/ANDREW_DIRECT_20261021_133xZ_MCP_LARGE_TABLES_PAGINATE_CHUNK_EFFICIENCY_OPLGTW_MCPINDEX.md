# ANDREW-DIRECT 2026-10-21 ~13:3xZ -- MCP: what it indexes and surfaces; paginate or chunk the large tables so queries do not overload the server

Channel: typed by Andrew at the `4.0.0_SA_CRO~Z` terminal (Claude Code session, site Z), ~13:3xZ (9:3x AM ET).

## VERBATIM

> I need you to analyze current state of the MCP, particularly what it is indexing and what it surfaces. The issue i am seeing
> is that some of the tables inherently are very large. We need to figure out how to paginate these or otherwise chunk them so
> that it doesnt overload the server when people are querying. We need to increase efficiency. Please analyze and identify how
> this works currently. It should be folded in to jobs for the OPLGTW and MCPINDEX COOs

## Recorded as said, not adjudicated here

- **The ask (this seat):** analyze what the MCP indexes and what it surfaces, and how large tables are read and returned today.
- **The problem named:** some tables are inherently very large, and querying them can overload the server.
- **The direction named:** paginate or otherwise chunk, to increase efficiency.
- **Placement named:** fold the work into the jobs of NFRA_OPLGTW's COO (`2.0.0_SA_COO~O`) and NFRA_MCPINDEX's COO
  (`2.0.0_SA_COO~MI`). This seat analyzes; the CTO folds.
