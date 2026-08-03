# T3.A cache census: five layers live-grounded, the browser layer is ungoverned

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, EXPLORE

**Serial:** `0.7.0_AE_CloudOps~F` -- Window: 2026-08-03T20:18Z-21:10Z (fresh session on COO GO
201215Z, Andrew-direct GO @3e2b23ebb3; P1)
**Commits this window:** TO flip @1aadbec64e + deliverable/log commit (this one)
**Deploys:** 0. **Mutations:** 0 (read-only census; no policy edits, no invalidations fired,
QA JWT minted from opal/auth/jwt-private-key for measurement and deleted with the key copy
in-session)

---

## Summary

MDPF_GLOBAL.T3A executed end-to-end in one session. Every cache layer on the MDPF serve path
mapped with measured evidence; deliverable at
`org/tier2_senior/0.7.0_AE_CloudOps~F/deliverables/MDPF_GLOBAL_T3A/` (CACHE_CENSUS.md +
cache-map.json + raw header captures).

**Headline finding: MDPF responses carry NO Cache-Control end-to-end.** The 07-29 router flip
(`/api/general/mdpf/` -> `/platinum/mdpf/`, deployed public-data-router v6) moved mdpf out of
the deployed cache-control-injector v2's only stamping condition (`startsWith("/json/")`), and
the mdpf publisher sets no S3 CacheControl metadata (9/9 served keys null, measured). CF edge
still caches (DefaultTTL 300 operative, Hit/Age measured cycling under 300), but the browser
falls back to heuristic freshness that grows with artifact age. Flagged F1 for T3.B, not fixed.

Bonus: DT's behavior-16 nuance (bare `max-age=300` on json-tiered) grounded to a source-confirmed
mechanism -- same injector non-fire, but json-tiered producers stamp S3 metadata
(`json-tiered/market-overview/rsi-summary.json` CacheControl `max-age=300` measured live) and it
passes through bare. The stamp shape difference DT saw is producer discipline, not injector variance.

Denominators: 25/25 behaviors live-enumerated with policy identity (ce00305d exclusive to
/api/general/*; sharing counts 1/2/4/17/1), 3/3 pinned edge artifacts pulled+read, 4/4 live
scopes, 10/10 routes measured (9x200 + 1x403 dead-legacy root), 5/5 mdpf RQ keys + 2/2 module
caches + client defaults at file:line, 9/9 S3 keys head-checked. W9/W9b folded as baseline, not
rediscovered.

## Compiler Tools (mandate reproduction, per-run verdicts)

| Run (TO mandate) | Observed | vs `<expect>` |
|---|---|---|
| `comp-routes behaviors` (phase 1) | 25 behaviors enumerated with edge associations; NO cache-policy identities in output | **PASS** -- matches expectation; the banked gap @aeca48e395 STANDS (not closed); output used as denominator seed only |
| `comp-cache collisions` (phase 1) | 103/103 useQuery sites captured, 14 shared keys, 0 type mismatches; no mdpf keys in collision view | **PASS-with-note** -- mdpf keys are single-site (no collisions to list), so the client layer was grounded by direct source read per the TO's if_mismatch branch (ModelPortfolios.tsx:417-548, aum.ts:510-624, main.tsx:37-59) |
| `aws cloudfront get-distribution-config` (phase 2, rail-checked) | Live config pulled (ETag E1H04CVXQPZ22Z); every serve-path behavior's policy identity + TTLs captured; sharing enumerated (1/2/4/17/1 across 5 policies) | **PASS** -- census grounded on APPLIED plane; get-cache-policy resolved all 5 identities incl. ce00305d def=300 (W9 state confirmed live) |
| `aws lambda get-function` on deployed injector (phase 2, rail-checked) | v2 (the version the live distribution pins) downloaded; stamp = `public, max-age=300, s-maxage=300` gated on `startsWith("/json/")` | **PASS with material finding** -- deployed artifact read; stamped TTL for mdpf routes is NULL (condition never true post-flip). Also pulled router v6 + validator v18 (same Rule-22a grounding for the trio) |
| live header measurements, all scopes + global (phase 2) | 10 routes x pass1 (all Miss, no cache-control, no Age) + pass2/3 samples (Hit, Age 160-167 then 208-214, cycling under 300); legacy root 403 | **PASS** -- headers consistent with the layer map; the no-cache-control observation IS the F1 finding, enumerated with an owner (T3.B), not a silent row |
| report to COO + CTO (phase 3) | MCP sent this window with artifact path + commit + per-layer denominators + 4 clash flags | **PASS** |

Additional runs: `comp-grep` x5 (mdpf endpoints, fetcher consumers, invalidation call sites,
QueryClient, direct-path sweep -- all on-rails, logged), `comp-which` A.3 exercise at startup
(forwarder RAN), `comp-to` TO context set. `s3api head-object` x11 + `s3 ls` (operational
grounding, rail-checked markers carried). No comp-tool gap found beyond the two already-banked
CF gaps (comp-routes policy-blind, comp-blast CF path-pattern-blind) -- both confirmed still open.

## MCP traffic

Inbound handled at startup: DT W9 closure detail (174932Z), COO awareness relay (175011Z), COO
MDLP_MONPUB project-close notice (181146Z, predecessor-scoped -- its /log directive was for the
prior session, which had already logged its close at 1727Z), COO T3A GO (201215Z, acted on this
session). Outbound: T3.A completion report to COO + CTO (phase-3 mandate).

## Blockers

None. TO complete pending CTO validation at close (acceptance is CTO-validated per the TO).

## Current State (zero-context handoff)

- **T3.A COMPLETE at this seat.** Deliverable committed; TO flipped pending -> complete this
  window. Read-only throughout; the only credentials touched (JWT signing key copy + QA token)
  were deleted in-session.
- **T3.B (mine, staged) remains gated behind T2.C** (publish-window clock, not yet ruled). Its
  four design inputs are the F1-F4 flags in CACHE_CENSUS.md; F1 (no client TTL on mdpf) is the
  substantive one.
- **Instrument gaps confirmed still open** (comp-routes cache-policy identity; comp-blast CF
  path-pattern nodes) -- already in CVO's register @aeca48e395; no new gap class found.
- Non-blocking findings N1-N4 recorded in the deliverable (source-comment drift, dead root
  fetcher, cottonwood-only aum-metrics by design, qs-not-in-cache-key).

## Next Steps

1. **[1.0.0_SA_CTO]** T3.A acceptance validation per s.C.4 (evidence: deliverable dir + this log).
2. **[0.7.0_AE_CloudOps~F]** T3.B invalidation design on T2.C ruling -- event-driven standby.
3. **[0.4.0_DE / 0.2.0_DT lanes]** N1 comment drift + N2 dead fetcher, whenever that pod next
   touches the surface (routed in the COO/CTO report; no urgency).
