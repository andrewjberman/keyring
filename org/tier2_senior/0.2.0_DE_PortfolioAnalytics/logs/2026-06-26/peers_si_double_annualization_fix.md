# 0.2.0_DE_PortfolioAnalytics — /Peers SI double-annualization fix (deployed PROD v2.1.127)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE, DEPLOY
**window:** 2026-06-26 ~1800Z -> ~1825Z (session start since last log `session_close_1455-1650Z.md`)

## Summary

Came up live, self-healed reachability (re-registered + persistent inbox Monitor armed), and
drove an Andrew-direct bug end-to-end: `/Peers` Since-Inception (SI) quartile charts rendered
~half the true values due to FRONTEND double-annualization in `PeersTab.tsx`. Fixed it (identity
pass-through, mirroring the proven `BenchmarkHeatmap.tsx:309` precedent), verified independently,
committed, shipped DEV->PROD (v2.1.127), grounded the deploy against the CI artifact + served
data (not self-reports), and closed the COO RAVC GREEN.

## Work done

1. **Reachability** — `get_agent_status` showed NOT REGISTERED (window-exit drop). Re-registered
   (PID 15700), armed persistent inbox Monitor (task `btvy814mh`). No stale crons.
2. **Inbox dispatch** — Pulled an Andrew-direct referral from `0.2.0_DS_PortfolioAnalytics`
   (root-caused) + a duplicate DRIVE dispatch from `2.0.0_SA_COO`. I was already in-flight before
   the COO dispatch (came live + pulled DS referral first).
3. **Root cause confirmed** — `PeersTab.tsx` re-annualized SI returns that arrive ALREADY
   annualized from `yang-generate-peer-performance`. The actual-days exponent (365/779 ~= 0.47)
   nearly halved an already-annual figure. Verified INDEPENDENTLY: pulled served
   `s3://opal-data-portal-v2/json/peers/peer_performance.json` myself — INT SI model=13.8746 sits
   sanely next to 1Y=14.4275 (cumulative over ~26mo would be ~30%+), so SI is already annual.
   Ties DS's 30/30 source<->served audit.
4. **Fix** — Removed `annualizeSinceInceptionReturn` + `transformPeerData` + `INCEPTION_DATE`
   from `PeersTab.tsx`; `transformedData = data` (render served directly). Footnote
   "** SI annualized (not cumulative)" kept (stays true). Mirrors `BenchmarkHeatmap.tsx:309`
   identity pass-through (the sibling that fixed this same bug; PeersTab was the lone holdout).
5. **Verified pre-deploy** — `tsc --noEmit` rc=0; `comp-transform schema-check PeersTab` =
   benign types-resolution WARN only (interfaces inline), no MISSING; `grep` confirmed 0 dangling
   refs to the removed fns.
6. **Shipped** — commit `016dd9cc` on DEV (VALGATE passed) -> DEV CI `28256241405` SUCCESS ->
   handed PROD promote to `0.2.0_DT_PortfolioAnalytics` (their lane; `/prod-deploy` halts non-DT).
   DT promoted: merge `95703cc8`, tag `portal-v2.1.127`, "Deploy to Production" CI `28256867173`.
7. **Verified post-deploy (artifact, not self-report)** — `gh run view 28256867173` in portal
   repo: Build Production Assets=success, Deploy to S3+CloudFront=success, Tag Deployment=success.
   Tag `portal-v2.1.127` = `95703cc8` = `origin/PROD` HEAD; contains `016dd9cc`; `git grep` on
   origin/PROD HEAD = 0 matches for the removed fns. Served data intact.
8. **RAVC** — Closed COO GREEN; DT + DS loops closed.

## Files Modified

see commit message: `016dd9cc` (portal repo). Single file: `portal/src/pages/ModelPortfolios/tabs/PeersTab.tsx` (+12 / -65).

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-transform schema-check PeersTab` | prop/schema drift on the edited component | WARN (types-resolution only — interfaces inline; no MISSING) |
| `comp-routes trace` / `behaviors` | find portal serving path + PROD CF domain | PASS (S3-opalinvest-portal SPA; domain ddekdm5vg1xns.cloudfront.net; /Peers auth-gated) |

What worked: schema-check + comp-routes gave the rail-correct way to find the serving path and
confirm no prop drift without a raw `aws cloudfront` call (HUD gated my raw attempt — complied).
What failed: none. Gap found: none — the rail routed cleanly.

## Blockers

None. Two residuals are environment limits OUTSIDE my reach (not verification gaps), routed to
Andrew by COO: (1) live-DOM pixel eyeball of /Peers SI bars — page is auth-gated, no portal
/login creds; (2) direct live-bundle fetch — sandbox egress blocked (HTTP 000). The build+deploy-
success chain + source-confirm + served-data tie binds rendered SI = full values without them.

## Current State

- **DEPLOYED + CLOSED GREEN.** `/Peers` SI fix live on PROD `portal-v2.1.127` (commit `95703cc8`,
  contains `016dd9cc`). CI `28256867173` all jobs success. SI now renders full un-halved values:
  INT ~13.87%, LTC/LTA ~18.5/18.4%, UST ~4.67% (was ~6.3/8.3/8.2/2.2).
- `PeersTab.tsx` no longer annualizes; renders served `peer_performance.json` directly (data
  layer unchanged — DS confirmed 30/30 tie, no producer change).
- Workspace submodule pointer bumped to `cdf8adf3b` on CLOUD (by DT).
- This is DISTINCT from the prior-session /Peers missing-models fix (yang-v2.4.14, 5 models).

## Next Steps

- [Andrew] 10-second pixel glance of live /Peers SI column (full-height bars) — routed via COO,
  the only residual; functional correctness already grounded.
- [0.2.0_DE_PortfolioAnalytics] None owed. Pod 0.2 idle/available, event-driven (COO-confirmed
  idle-correct). Inbox Monitor `btvy814mh` armed.
