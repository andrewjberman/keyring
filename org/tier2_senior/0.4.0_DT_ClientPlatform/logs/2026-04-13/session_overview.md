# 0.4.0_DT Session Overview — 2026-04-13

**Agent:** 0.4.0_DT_ClientPlatform
**Coordinating agents:** 0.4.0_DS_ClientPlatform, 0.4.0_DE_ClientPlatform, 0.5.0_AE_OpalETL, 0.6.0_AE_PartnerETL

## Topline

- Diagnosed + fixed **BenchmarkHeatmap SI double-annualization** end-to-end with DS (Lambda) and AE 0.5.0 (deploy). UI now shows correctly-annualized SI.
- Found + fixed **DistributionTab Snapshot hang** — panel-wide `isLoading` gate tied to the cumulative chart fetch was blocking Snapshot view unnecessarily.
- Shipped + reverted a **scoped-Lambda PII gate** for `partner_analytics` and `cumulative_chart`. Coordinated with AE 0.6.0 on the router v10/v11 + opal-partners-data rewrite. Andrew called it net-negative (over-hashing in Snapshot, nothing in Continuous, added latency); fully rolled back.
- Shipped an **ADV cohort drill gate** (both views) as the tactical replacement pending DS's gold-emit v3 redesign.
- **Manual-invoked yang Lambda** to regenerate `benchmark_returns.json` with cumulative SI values (S3 was stale; scheduled refresh hadn't run since yang-v2.3.7 deploy). Confirmed UST SI=9.52, LTC SI=33.32 matching AE brief.

**7 portal DEV commits** today under `0.4.0_DT_ClientPlatform` author.

## Portal DEV commit stack (chronological)

| SHA | Scope |
|---|---|
| `dbee109` | (superseded) BenchmarkHeatmap annualizeSI → pass-through. Correct at time of commit (Andrew originally wanted cumulative display) |
| `094c265` | BenchmarkHeatmap restore single-annualize. Andrew pivoted to annualized display mid-session; frontend single-annualizes on Lambda's cumulative output |
| `bdfb235` | DistributionTab Snapshot no longer blocked by cumulative chart fetch (`isLoading` gate moved into Continuous branch only) |
| `d957ab6` | (reverted) partner-analytics routed through scoped Lambda for PII filtering |
| `4c3ce93` | (reverted) cumulative-chart routed through scoped Lambda for PII filtering |
| `64bc570` | Revert of both PII rewires after Andrew's net-negative call |
| `7368940` | ADV cohort drill gated to architect-level only in Snapshot + Continuous (tactical PII mitigation pending DS gold-emit pass) |

## Thread 1 — SI double-annualization

**Symptom (Andrew):** UST SI +2.34%, LTC SI +7.59% on Benchmark Comparison heatmap, mathematically impossible vs 1Y returns. Onset ~10 AM ET 2026-04-06.

**Investigation (my half):** DS had already proven S3 Lambda output had been annualized-once since 2026-01-22 (commit feca94a1). The remaining mystery was why the display went double-annualized on 4/6 and not sooner. I traced:
- Bundle hash history: UNRECOVERABLE (opalinvest-portal bucket has versioning DISABLED — recommend enabling for future forensics)
- CloudFront invalidations: 4/6 was unexceptional (3 invalidations 13:02–14:33 UTC), 4/5 had 4, 4/2 had 9
- Portal deploy timeline: auto-deploy CI landed 2026-03-23 but `deploy-manual.sh` already did CF invalidation; 25 tagged deploys carrying the annualizeSI code between Feb 25 and 4/6
- 4/6 yang commit 629a2fef's CacheControl flip: did NOT touch benchmarks Lambdas (only macro-timeseries, volatility, peer-performance, positioning, trigger)

Server-side evidence **cannot** explain a sudden 4/6 onset. Conclusion: stale-bundle theory unsupported. Residual hypotheses (browser-side service worker, different code path) left open. Andrew accepted the mystery and shipped anyway.

**Fix path:**
- DS: Lambda emits cumulative (commit `bc6f4ccb` CLOUD, AE 0.5.0 deploy `yang-v2.3.7`)
- DT: frontend annualizes once for display (commit `094c265`)
- ReturnVolatilityScatter untouched (already correct)

**Direction pivot flagged:** Initially briefed as "cumulative display, pass-through frontend" (`dbee109`). Andrew's mid-session redirect to annualized display flipped my approach (`094c265`). Sent DS a correction before his S3-acceptance spot-check fired against wrong expected UI values.

**Manual yang Lambda refresh:** Scheduled PKL refresh hadn't run since yang-v2.3.7 deploy (generated_at stuck at 2026-04-12T01:34 UTC with stale 4.79 UST SI). Identified `LATEST.json` shape mismatch against handler's `get_latest_data_pkl_key` (reads `files.data_pkl` but file has `data_pkl` at top level). Worked around by invoking with explicit Step-Functions-shaped payload `{"manifest":{"bucket":"opal-data-portal-v2"},"processed":{"data_pkl_key":"benchmarks/data_20260412_v1.pkl"}}`. Both `yang-model-portfolio-benchmarks` and `yang-generate-benchmark-returns` re-emitted. S3 now shows UST SI=9.52, LTC SI=33.32 (cumulative). The shape mismatch is a latent bug worth an AE/DS fix pass.

## Thread 2 — DistributionTab Snapshot hang

**Symptom (via DE):** Snapshot view spins indefinitely; Continuous renders fine.

**Root cause:** Panel-wide `if (isLoading) return <LoadingInline/>` at `DistributionTab.tsx:713` where `isLoading` tracks the `platinum-cumulative-chart` query. That query feeds only Continuous, but the early-return gate blocked both views. Slow cumulative fetch → Snapshot spins despite its own `analyticsData` being ready.

**Fix (`bdfb235`):** Removed the panel-wide gate. Snapshot branch already had its own `analyticsLoading` check at the render site. Moved the spinner into the Continuous branch only.

**Not a HDRSPL.002+.003 regression** — the gate pre-dates that work. HDRSPL made it more visible by adding Snapshot-specific `analyticsLoading` handling that exposed the panel-wide gate as redundant/harmful.

## Thread 3 — Partner-analytics PII leak (coordinated with AE 0.6.0)

**DE's brief:** Chase (`chase.bertrand@49financial.com`, role=user) could drill into Travis Penfield's architect segment on Segment Analytics and see cleartext client relationship names ("Smith Family Trust") in DevTools. DE tried a frontend gate first (`5a79b64`), Andrew correctly redirected (DevTools = raw payload visible regardless), DE reverted.

**My trace (sent to DE):**
- `auth-validator-edge` is viewer-request only — can't rewrite response bodies
- Firm-level `platinum/firm/*` path matches no per-user scoping regex; `shared-advisor-router` passes it straight to S3 with an explicit comment "numerical data only, no PII" (wrong for `partner_analytics`)
- Precedent already existed in router at lines 111-125: `platinum/advisors/{id}/summary.json` and `platinum/clients/{id}/summary.json` are blocked 401 S3-direct and forced through `opal-partners-data` Lambda for pseudonymization (M1 mitigation from P4 audit)

**Recommended (Option 1B):** extend existing M1 pattern — router blocks `partner_analytics_*.json` S3-direct, `opal-partners-data` reads artifact and filters `clients[].label` by `X-User-Role` + `X-Advisor-Id` headers.

**AE 0.6.0_PartnerETL** accepted, shipped:
- P0: partners-api-v1.15.7 + portal-auth-v1.12.0
- P0v2 (Andrew feedback on over-hashing): partners-api-v1.15.8 + portal-auth-v1.12.1 (router v11 extended the block to `cumulative_chart.json`; pseudonymizer rewritten with per-view structural filter)

**My rewires:** `d957ab6` + `4c3ce93` through `GET /api/scoped/advisor-intelligence/partner-analytics?firmId=&granularity=` and `/cumulative-chart?firmId=`.

**Outcome: reverted.** Andrew tested and it was net-negative:
- Snapshot: everything hashed including segment-level labels (states, cities, architect names) and own-book exemption still broken for both Travis and Chase
- Continuous: nothing hashed (propagation gap? filter structural hole?)
- Latency increase from Lambda round-trip

Revert: portal `64bc570` + AE `portal-auth-v1.12.2` (router v12, both blocks removed; line-129 comment updated).

**Residual (harmless):** opal-partners-data scoped routes `partner-analytics` and `cumulative-chart` and their API GW entries are still live but unused by portal. AE will clean up alongside DS's v3 gold-emit pass.

## Thread 4 — ADV drill gate (tactical PII mitigation)

Per Andrew post-revert: ADV cohort shows architect level only in both views, no drill into clients. GEO stays as-is (cities are public). DS will follow up with the v3 design that strips `clients[]` and `adv_drill[*].categories` at gold-emit time so artifacts carry no PII regardless of access path.

**Fix (`7368940`):**
- Snapshot `handleSegmentClick` (line 2608): ADV architect click falls through to segment-highlight toggle, no longer promotes `advDrillLevel` to 'client'
- Continuous `handleDrillChange` (line 648): ADV cohort is no-op; GEO state→city unchanged
- State vars (`selectedArchitectKey`, `advDrillLevel`) and reset effects left in place — child components have unreachable 'client' branches, kept cheap so v3 restore is clean

## Coordination artifacts

- 18+ MCP messages exchanged across DS, DE, AE 0.5.0, AE 0.6.0, and this log
- Inbox watcher relaunched after every notification; earlier session had a wrong-path launch that missed the DE PII brief by ~5 min (fixed mid-session)
- Direction pivot on SI (cumulative → annualized) propagated to DS same-turn to prevent acceptance-value drift

## Open loops at session end

- **Portal DEV→PROD merge** ready: 4 commits stacked (`bdfb235`, `094c265`, `64bc570`, `7368940`). SI gate cleared via manual yang refresh. Andrew's promotion call.
- **yang LATEST.json shape mismatch** — latent bug in `get_latest_data_pkl_key`; scheduled refresh will fail silently until fixed (AE 0.5.0 or DS lane).
- **PII v3 design** — DS owns gold-emit strip of `clients[]` + `adv_drill[*].categories`. AE 0.6.0 flagged for followup cleanup of unused scoped-Lambda routes.
- **Original SI-flip 4/6 onset mystery** — unresolved server-side; Andrew's working theory is the ADVI CloudFront edits inadvertently flushed a cache. Not pursued further.
- `comp-pii sweep` on `platinum/firm/*` — recommended to DE and AE, not yet greenlit.
- Bucket versioning on `opalinvest-portal` — recommended for future forensics.

— 0.4.0_DT_ClientPlatform
