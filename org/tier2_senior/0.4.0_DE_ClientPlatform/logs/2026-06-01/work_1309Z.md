# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 1309Z

**archetype:** TRACE
**secondary_archetypes:** VALIDATE, COORDINATE

## Dispatch
COO [DRIVE] redirect (Andrew-direct, MDPF_SCOPED P1 FIRST priority): DE leg = **backend-fit mapping** of the pod-4 shared FE↔BE linkage matrix for the Model Portfolios page across GLOBAL / 49 (49financial) / INFLECTION (inflection). RAVC2 in ~75 min. RD~B owns FE rows, AE owns schedule/interval, DS~B standby for data-shape gaps.

## Work done (~25 min, under SLA)
FE→BE→S3 trace of all 8 Model Portfolios panels:
- Inventoried queries from `ModelPortfolios.tsx` (queryKeys, firm-gating).
- Resolved each through `aum.ts` → `portal-proxy.ts` to serving path + S3 key.
- **Verified all serving artifacts PRESENT in S3** (live `aws s3 ls`, not assumed) for all 3 segments.
- **Shape-parity check** via downloaded artifacts: 49 & inflection aggregate-aua schema-identical (both 402 dates, identical top-level + by_model entry fields); per-firm account-distribution = superset of global.

## Result
- **Growth-tab panels (#1-5) FIT all 3 segments** — real backend per segment, no empty-firm-view. D1 reopen defect does NOT recur on current artifacts.
- **Shape-parity PASS.** by_model key-set divergence (49: 5 base + 2 sma; INF: 5 base + 2 blends) is data-driven content, not a shape break.
- **1 FLAG (classification, not data gap):** Performance + Peers tabs (#6-8) NOT firm-gated (gated only by activeTab) → show global/model-level for all 3 segments. Model-level data is firm-invariant by design; page doesn't signal it. Call needed (accept / label / hide) — DE no fix pending until adjudicated.
- **AE note:** 2 possible orphan S3 artifacts (json/mdpf/aggregate-aua-timeseries.json + json/mdpf/global/...) not referenced by current ModelPortfolios.tsx.

## Commits
- CLOUD `31f3b09ed` — docs/briefs/mdpf-fe-be-linkage-matrix-be-columns-20260601.md (BE columns, 8 panels x3 segments)

## Comms
- RAVC2-Request → COO (2.0.0_SA_COO, 130916Z) with full fit result + classification call.
- SYNC-REPLY → RD~B (0.4.2_RD~B, 130904Z): BE cols keyed by queryKey for clean join + the Performance/Peers flag. Awaiting RD~B FE row set to reconcile merged matrix.

## Next
- [COO + RD~B] Awaiting Performance/Peers firm-invariance classification call.
- [RD~B] Awaiting FE row set → reconcile into merged linkage matrix.
- Standing on /work cron (next tick ~20m); pick up classification/re-scope immediately.
