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

## CTO ruling on the SA route (1.0.0_SA_CTO~Z msg 30219, 2026-10-06 18:52Z)

> "Ruling: (a). SA stays stopped until Andrew completes Bright Data KYC; I am surfacing it to him now. No (b): native egress
> was PerimeterX-blocked after about 10 calls on 09-10, and a repeat risks getting the paid SA account flagged, a cost no proxy
> fix undoes. bbg, barrons and wsj continue as resumed; FT stays deferred on Andrew's word."

SA resumes (r47_sa checkpoint, root `.runtime/opal-data-harvest-sa`, `--clear-stop sa`) only after Andrew's KYC and an account
check that answers 200.

## ANDREW-DIRECT ~19:2xZ -- SA runs on the tab pattern, no Bright Data (supersedes the route-(a) ruling above)

> "SA shouldnt need Bright Data, we should be able to run th same pattern on SA as we use with all the others which is logging
> in via google credentials, then in the browser window using the same session to pull the relevant rest api endpoints"

Route: SA moves to `transport: tab` like wsj, barrons and bbg -- its own persistent Chrome profile
(`browser-profiles/sa`), Google sign-in in that profile, and the SA REST endpoints called in-tab (`TabSession.get`, which
already carries the per-page Referer). No residential proxy and no KYC act. The 09-10 PerimeterX block was a curl session
off a datacenter IP replaying harvested cookies; an in-tab fetch runs inside the browser that executes PerimeterX itself.
First act: an in-tab probe of the account and listing endpoints after Andrew's Google sign-in in the sa profile; the build
(contracts.json `sa.transport`, `TAB_ORIGINS["sa"]`, the sa sign-in route) is cut after the probe reads 200.
