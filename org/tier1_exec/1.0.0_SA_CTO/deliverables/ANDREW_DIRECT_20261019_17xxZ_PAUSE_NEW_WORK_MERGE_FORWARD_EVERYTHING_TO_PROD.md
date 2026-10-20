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

## DONE (2026-10-19 ~21:4xZ, 1.0.0_SA_CTO~DELL2)

Each item is measured; the source of each read is named.
1. **Merge forward:** worker branches on dell2 went from 92 unmerged to 2 (MSTR census, `~Y2` msg 10975).
   - `scratch/r34k-pin` is KEPT: it is r34l's rollback source.
   - `wk-IRPT_ANLREQ-102` is archived (tag `archive/wk-IRPT_ANLREQ-102` @65a62a9aa8). Its worktree holds 6 uncommitted files, so it
     is removed only on Andrew's word (open-calls row a392).
   - box/dell2 is pushed by MSTR's box-sync; at this line origin reads dead0ecd84, 20 commits behind this tree's HEAD (ls-remote read).
2. **Portal on PROD:**
   - The backoff (AR-y-410) is LIVE as portal-v2.1.244, facddeb6, since 20:15:44Z. Read here: origin/PROD is facddeb6; the site's
     Last-Modified is 20:15:38Z.
   - AR-y-354 is RETIRED (tag `archive/cand/dell2/anlreq-filing-hint-keep-equal-pair` @f78ea50e); v0.24 removes the field it hinted.
   - DEV contains PROD: the fold, row 7797, was approved, and `merge-base --is-ancestor origin/PROD origin/DEV` reads yes.
3. **Servers on PROD:** r34l is LIVE since 21:39Z. Root `0485393f3a-r34l`; V1 shows 4 changed members; every V2S line is OK
   (`org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_r34l/A_AFTER_R34L.txt`). Ledger CLOSED 21:43Z.
4. **Where things stand:**
   - Ticket Center Analysis Request:
     `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/TICKET_CENTER_ANALYSIS_REQUEST_STATE_ON_PROD_20261019.md`.
   - The Investor Reporting Performance tab:
     `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_STATE_ON_PROD_20261019.md`.
   - Trade and Meeting Request: `~V2`'s page.
   - Run 4, the clean unseeded staff filing on PROD after both ships, was GO'd to IB2 at 21:44Z. Its receipt is the measured proof.

**The PAUSE is lifted.** Work resumes in Andrew's relayed order (~18:4xZ):
1. the Ticket Center (Analysis Request first: the v0.24 issuance by `~Y2`, O1+O2 first; then Trade and Meeting);
2. the Performance tab;
3. Cottonwood (the CTO's call, below).

**What is released now:**
- `~P2`'s two CTO-approved Cottonwood cells (ruling `RULING_481D_COTTONWOOD_CELLS_WAIT_FOR_PAUSE_DONE_20261019.md`);
- `~D2`'s all-days rewrite-and-republish pair (packet sha256 c0906587), ruled by this seat in the tick that follows.

-- 1.0.0_SA_CTO~DELL2

**CORRECTION (2026-10-19 ~23:4xZ, 1.0.0_SA_CTO~DELL2):** DONE item 2 says AR-y-354 was retired because "v0.24 removes the field it hinted".
That is wrong. Read from f78ea50e itself: AR-y-354 is the C-FILING-HINT Keep path. Keep re-posts the equal pair, so an unknown symbol files
UNRESOLVED and reaches C-SWAP. It is restored into the v0.24 round and ships with or after the door's AR-g-68. The DONE line otherwise
stands: AR-y-354 was never on PROD, and the pause's PROD terms were met by the backoff and r34l.

