# Session Log -- Platinum Layer Architecture Design
**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-08
**Project:** ADVI_GLDOPS

---

## Summary

Andrew requested a visual mapping of the gold runner pipeline (script -> file -> downstream)
and portal data serving architecture (S3 -> CloudFront -> Lambda -> browser). This led to
a design discussion that produced four deliverables:

1. A complete script-to-file flow reference for the gold pipeline
2. A complete auth and data serving flow reference for the portal
3. A concrete D_04 spec for the Books tab platinum publisher
4. A broader platinum layer architecture strategy for the full portal migration

The core insight: the portal has no clean boundary between analytical computation and
presentation. Gold-layer scripts write to scattered paths, the portal reads from all of
them, and two Group C scripts (C_06, C_08) leak portal-facing JSON directly into gold/.
The platinum layer (`platinum/` S3 prefix) establishes this boundary. Group D scripts
become publishers that read gold/ and write platinum/. The portal reads only platinum/.

---

## Design Decisions (Andrew-directed)

1. **Portal reads only Group D outputs.** C_06 and C_08 currently write portal-facing JSON
   to gold/. This is a leak. D_04 will read those files and republish to platinum/.

2. **gold/ = analytical, platinum/ = portal-serving.** All non-portal outputs (parquets,
   intermediate views, full timeseries) stay in gold/. Only pre-computed, lightweight
   JSONs optimized for display go in platinum/.

3. **D_04 covers all drill levels uniformly.** Not just client-level slicing -- firm,
   advisor, client, and account all get the same treatment for consistency.

4. **No client timeseries in portal.** The client drill in Books tab is purely snapshot
   (tax lots, capital gains, mix pie, top holdings). Full timeseries stays in gold/
   for future use but is not served to the portal.

5. **90-day decomposition is pre-computed.** The portal currently pulls the full AUA
   timeseries just to sum 90 days of market_growth/nna/synthetic_correction. D_04
   pre-computes these three numbers into the client summary.

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| D_04 Books Tab Spec | `docs/briefs/data-scientist-D_04-client-portal-summary-spec.md` | DS (self), DE, DT, AE |
| Platinum Architecture Strategy | `docs/briefs/data-scientist-platinum-layer-architecture-strategy.md` | Full Pod 4, AE |

---

## Reference Documents (complete chain)

| # | Document | Path | Purpose |
|---|----------|------|---------|
| 1 | Gold Script-to-File Flow | `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-08/gold_pipeline_script_file_flow.md` | Every script, its I/O, S3 keys, dependency DAG |
| 2 | Portal Auth & Serving Flow | `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-08/portal_auth_and_data_serving_flow.md` | Two serving paths, auth chain, route-to-file map |
| 3 | D_04 Books Tab Spec | `docs/briefs/data-scientist-D_04-client-portal-summary-spec.md` | Phase 1 deliverable: schemas, fetch maps, open questions |
| 4 | Platinum Architecture Strategy | `docs/briefs/data-scientist-platinum-layer-architecture-strategy.md` | Big picture: phases, audit methodology, folder structure, roles |

---

## Files Modified

| File | Change |
|------|--------|
| `docs/briefs/data-scientist-D_04-client-portal-summary-spec.md` | New: D_04 spec |
| `docs/briefs/data-scientist-platinum-layer-architecture-strategy.md` | New: architecture strategy |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-08/gold_pipeline_script_file_flow.md` | New: script-to-file reference |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-08/portal_auth_and_data_serving_flow.md` | New: auth and serving reference |

---

## Next Steps

- [Andrew] Review D_04 spec, resolve open questions (N1 payload split, L4 pre-computation, advisor client list size)
- [Andrew] Approve platinum/ prefix and folder structure
- [DS] Write D_04 script after approval
- [DE] Begin tab-by-tab audit of remaining Advisor Intelligence tabs (Asset Overview, NNA/Flows, Partner Analytics, Fee Efficiency, Leaderboard)
- [DT] Plan infrastructure changes: shared-advisor-router rewrite, opal-partners-data Lambda updates
- [AE] Confirm gold runner can accommodate D_04 at end of downstream chain
