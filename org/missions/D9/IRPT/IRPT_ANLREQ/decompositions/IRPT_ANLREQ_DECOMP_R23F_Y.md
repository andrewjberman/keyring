# IRPT_ANLREQ -- decomposition, round 23F: THE PARTNER-FIRM PORTAL STACK (one candidate branch from origin/PROD), workstream YR round 27 (issuer 2.0.0_SA_COO~Y2)

**Input:** `AR-y-283`'s BLOCKING row `IRPT_ANLREQ-D2-W104-S1` (the partner view strands ten `AR-y-265` tests) and `AR-y-282`'s row `W103-S3` (landing order); the laptop ruling @a5ec5c380c (portal changes go as `cand/dell2/<slug>` cut from `origin/PROD` with an approval row; nothing lands on DEV directly); the CTO's messages 7279 and 7292 (ONE branch `cand/dell2/partner-firm-stack`: the three DEV merges first as dependencies citing their existing approval rows, the five candidates in dependency order, the DEV-only partner gate last, tests after each commit, the branch tip sent to the CTO before the approval row is registered).

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-294` | ONE portal branch `cand/dell2/partner-firm-stack` from `origin/PROD`: the merges of `AR-y-265`, `AR-y-263`, `AR-y-262` (dependencies) then `AR-y-274`, `AR-y-275`, `AR-y-273`, `AR-y-283`, `AR-y-282`; the stranded tests re-pointed to the path that now serves their caller; counts after each merge; the record `r23/PORTAL_PARTNER_STACK.json` | a branch and a worktree in the portal repository (outside the product tree), the worker's record folder, the surprise channel file | LOCAL |

## Edges and chains

- One chain (the merge order is the dependency order). `AR-y-279` (commentary only when true) is NOT in the stack: held by the CTO until IB-pr-456 is live. The route gate merges last: on a dev build it lets a partner reach the board, and the board is unscoped until `AR-y-281` is deployed and `AR-y-283` is on the stack.
- Nothing is pushed or registered by the worker. The issuer sends the CTO the branch tip; the CTO decides the approval row.

fanout: 1 of 1 chains, cap 8, reason: one serial merge chain into one branch; the merge order is the dependency order and a parallel split would collide on the same Ticket Center files.
