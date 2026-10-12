# Andrew-direct 2026-10-12 ~20:5xZ at the 1.0.0_SA_CTO~Z terminal -- the site Z portfolio: seven project rulings

**Context.** This seat put a portfolio review of site Z's 7 active projects to Andrew, with a recommendation per project. He
answered each one in order. His words, VERBATIM:

> "I will address the rec/status/etc of each project listed starting with IAMROLES with a comment: 1.) Dell boxes should not
> be curtailed. Is there further work slated on this project? I think this one can be wound down/closed. 2.) I think we are
> probably good here for now, but I wouldnt close this project (OPLGTW) until I have seen a full breakdown of the
> vendors/channels available via the gateway, what tools/indexes exist for each, and current state of entitlements. The
> easiest way to manage this would be via the MCPORTAL, and this is what I think should be the first distinct outcome of the
> MCPORTAL project. 3.) I will handle this with Alyssa tomorrow. 4.) Give me URL for this I will check it right now. 5.) I need
> /open-calls as it pertains to this project. 6.) Why do we need Dell2 for this as opposed to building locally here? 7.) This
> project should be marked "HOLD" or "SUSPENDED". If there is no enumerated array for project status, then either will do,
> if there is a designated status then whatever is closest to those should be employed, as this is a project to address
> downstream of where we are at now."

The order was the review's: 1 IAMROLES, 2 OPLGTW, 3 OPALAI, 4 MCPORTAL, 5 COMM_ASSIST, 6 MCPINDEX, 7 MCPMSP.

## How each is carried (verbatim scope; nothing widened)

| # | project | carried as |
|---|---|---|
| 1 | NFRA_IAMROLES202609 | **No act narrows the dell agents.** Round-8 Addendum 1 (R10-E1a/b, the dell agent users' `lambda:InvokeFunction`) is WITHDRAWN. **No round 10.** The one non-terminal order, IAM-z-2, is a passive read: is the already-applied delete's real bd run healthy? Its next qualifying run is ~2026-10-13 04:00Z. The project closes at that round's L10. dell2's row D2-S46 is told by relay that no narrowing comes |
| 2 | NFRA_OPLGTW | Stays OPEN. Its close waits on Andrew seeing the full gateway breakdown on MCPORTAL (item 4 of this table's next row) |
| 2/4 | NFRA_MCPORTAL | PRD v0.7 addendum. The **first distinct outcome** is the gateway breakdown: (a) every vendor or channel, (b) the tools and indexes on each, (c) the current state of entitlements. It is cut ahead of every other open order |
| 3 | NFRA_OPALAI | Andrew handles it with Alyssa on 2026-10-13. His words are relayed to `2.0.0_SA_COO~AI` |
| 4 | NFRA_MCPORTAL | URL given: `https://mcp.opalinvest.dev/control-plane` (and `/open-calls`) |
| 5 | COMM_ASSIST | `/open-calls` run for the project at this seat |
| 6 | NFRA_MCPINDEX | Answered: why the producers sit on dell2. No change until Andrew rules |
| 7 | NFRA_MCPMSP | `status` carries NO enum (`org/standards/PROJECT_TREE.contract.json` value_enums.status `no_enum`). `dep_stage`'s enum (`REGISTERED`, `PRD`, `DECOMP`, `EXECUTING`, `ROUND_CLOSE`, `CLOSED`) holds no hold value. So **`status: "hold"`**, with `dep_stage` left at `ROUND_CLOSE` |

-- recorded by 1.0.0_SA_CTO~Z
