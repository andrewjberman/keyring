# Andrew-direct 2026-10-19 ~17:0xZ -- pause new work; merge everything forward; everything on PROD

**Received at:** `1.0.0_SA_CTO~DELL2` terminal. **VERBATIM (two messages):**

> "What is going on with the merges on this device? Also what do you mean syncing the test portal "back" to match the live
> one? Why would we be pulling anything backwards? What needs to be happening here is that we're pushing forwards. I need
> the most current builds and all the work from this device to be on PROD so I can actually test and see where we are at."

> "There seems to be some kind of mess of merges happening here and we need to clean that out and fast forward everything so
> the most updated stuff is all committed and pushed. Let's put a pause on new work until we are adequately merged forward
> and everything is on PROD so we can actually test and establish where we are across these various workstreams. I need to
> establish cleanly where we are at when it comes to the Investor Reporting Suites as well as the Ticket Flow Analysis
> Request sequence, because we really need these handled this week and It is impossible for me to adequately test and come
> to conclusions if we do not clearly have everything pushed and recognized."

## The order, as this seat applies it on dell2

1. **PAUSE:** no new cell, order or round is cut on any dell2 project until this record's DONE line is appended. Work
   already running finishes, and its result is merged forward.
2. **MERGE FORWARD (workspace):** every worker branch and worktree on this box is drained into `box/dell2` through
   `safe-merge`, or, when its content is superseded, retired after an `archive/` tag. `box/dell2` is then pushed and
   integrated into CLOUD. MSTR prints the census before and after: worktrees, unmerged branches, and the ahead and behind
   counts against origin.
3. **EVERYTHING ON PROD (portal):** measured at ~16:5xZ.
   - Every dell2 change merged to DEV is on PROD, portal-v2.1.242, 9107d48a. PROD-to-DEV now differs only in 5 dell1
     files and the 3-file Trade Request reveal that PROD has.
   - ONE dell2 portal change never reached DEV or PROD: `cand/dell2/anlreq-filing-hint-keep-equal-pair` (f78ea50e,
     AR-y-354, 10-15). `~Y2` ships it or retires it.
   - The "fold" is DEV taking PROD's newer commits forward. It moves nothing on PROD; it only keeps DEV from falling
     behind, so the next release is clean.
4. **EVERYTHING ON PROD (servers):** already-built fixes ship forward. That is r34l, the report-server update carrying
   the 425-cards fix (AR-y-404, AR-y-406, AR-y-408). Nothing new is cut.
5. **Then a clean statement of where things stand** for the Investor Reporting suite and the Ticket Center analysis
   request flow, measured on PROD, for Andrew to test against.
