# ANDREW-DIRECT 2026-10-06 ~18:3xZ -- AMGT_HARVST: SA already paid; FT later; proceed on bbg/barrons/wsj; remove the worktrees

**Seat:** `2.0.0_SA_COO~H` terminal (site Z). **Prompted by:** `/open-calls` at this lane (3 cards: SA account, FT hold, 8 worktrees).

## Verbatim

> "Seeking alpha is already paid. We may need to re-login on the browser, this sounds like some kind of caching issue. moving
> on to call 2, we can do FT any time, but because its been so diffcult, my inclination is proceed where we are getting results
> (bloomberg barrons and wsj) and we deal with FT later. SA should be solvable though we already pay for that. Movig on to call
> 3, yeah get rid of those worktrees."

## Disposition

1. **Call 1 (SA account): answered -- the subscription is paid; no billing act.** The issuer measured the 402 after the word:
   the rejected body (`.runtime/opal-data-harvest-sa/rejected_bodies/20261006T011002Z-sa-7876682ed5.402-1.body`, 351 B) is
   Bright Data's residential proxy refusing the site ("not available for immediate residential (no KYC) access mode ... fill in
   the KYC form"), not Seeking Alpha. SA egress is the residential proxy by contract (`lib/opal_data_harvest/contracts.json`
   sa `egress`; `org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py` header item 3: native egress was PerimeterX-blocked
   after ~10 calls). The saved session is also aged (`saved_session_file` 2026-09-15, `signed_in: false`). SA stays stopped
   until its account check answers 200 (CTO ruling @69ce080222, unchanged).
2. **Call 2 (FT): FT deferred.** The ft hold stands as "deal with FT later". Collection proceeds on bbg, barrons and wsj.
3. **Call 3 (worktrees): done.** Removed `wk-coo-h-r47-{land,store,widen}` and `wk-hvst-r46-94`, `-r47-95`, `-r48-96`,
   `-r48-97`, `-r49-98`; deleted 9 merged branches (each `merge-base --is-ancestor <b> CLOUD` true before deletion). Three
   residue folders held only a `portal/node_modules` junction into the shared tree; the junctions were unlinked without being
   followed (shared `portal/node_modules` intact, 258 entries).

## Acts that follow

- `2.0.0_SA_COO~H` resumes bbg, barrons and wsj, each from its own round-46 checkpoint with `--clear-stop <pub>` on a new
  invocation (CTO ruling @69ce080222: a leg resumes with Andrew present to hand-solve its challenge in the visible browser).
- Round 50 is triggered by that resume (CTO round-49 analysis @f3b9c1d972).
