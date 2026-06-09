# 0.4.0_DE_ClientPlatform — Session Log 2026-06-09 (~2130Z continuation)

**archetype:** IMPLEMENT + VERIFY

**Portal DEV commits this session:**
- `c6f12701` — fix(MDPF_CADENCE): per-source timestamps + divergence guard for Portfolio Analytics panel

**Portal PROD promotes this session:**
- v2.1.119 (DT): `00f70f2d` ADVI_PRTORG.04 Cottonwood module (from prior session)
- v2.1.120 (DT): `c6f12701` MDPF per-source timestamps + divergence guard

---

## Context

Continuation of the 2026-06-09 session. Prior session (log: advi_prtorg_04_cottonwood_frontend_module.md)
had completed ADVI_PRTORG.04 scaffold + DEV layout smoke. This session picks up from context compaction
with Monitor b7ktcxf6k dead (exit-143). Re-armed sequentially: b2tou1xiz → bd25ts9w1 → bhhhasgtf.

---

## Work Completed

### 1. Monitor re-arm

Multiple exit-143 SIGTERM events across session (LD-0146 expected, lossless). Final live Monitor:
`bhhhasgtf`. Followed /watcher protocol each time: no orphan check needed (persistent Monitor model),
re-arm via Monitor tool, pull inbox to catch any missed deliveries.

### 2. ADVI_PRTORG.04 post-promote (v2.1.119)

DT promote signal received (20260609T214705Z). portal v2.1.119 LIVE with `00f70f2d`.

**AC1-4 PROD smoke — partial results:**

| Test | Result | Notes |
|------|--------|-------|
| AC3: COT JWT → /api/general/* → 200 | PASS | aum-metrics.json 200 |
| BD regression: bd JWT → bd endpoints → 200 | PASS | partner_analytics_quarterly.json?firm=bd = 200, body has firm_id=49financial |
| AC2: non-COT JWT → cottonwood endpoint | **404** (not 403) | Routing confirmed reaching opal-data-cot (PRTORG.03 live), but cottonwood platinum/ not published; Lambda@Edge JWT-firm cross-check NOT confirmed |
| AC1 / AC4 | BLOCKED | COT JWT unavailable; ownership_map.json not in opal-data-cot; cottonwood platinum data not produced |

**AC2 Security Finding (routed to AE_CloudOps~B):** Lambda@Edge appears to route on `?firm=` query
param without validating JWT firmId matches. A bd JWT requesting `?firm=cottonwood` returns 404
(S3 key not found), not 403 (auth rejection). Currently safe (no platinum data = nothing to leak).
Must be resolved before AC7 (platinum data published). COO accepted finding + routed AE_CloudOps~B.

**Action 2 — c6f12701 push:** Pushed `c6f12701` to origin/DEV per COO dispatch. VALGATE D-1 PASS.

### 3. ModelPortfolios MDPF timestamp fix (new DRIVE, ~2134Z)

**Trigger:** COO [DRIVE] — Andrew-flagged bug: "timestamp still June 5th despite it now being June 9th".
CTO brief: `docs/briefs/modelportfolios-dataasof-timestamp-mis-sourced-20260609.md` (887dd07ba).

**Root cause (CTO-diagnosed):** `ModelPortfolios.tsx:475-478` sourced the Portfolio Analytics panel
footer timestamp from MDPF `as_of_last` (frozen 06-05). Holdings (aum-metrics.json `last_updated`)
and bell curve (account-distribution.json `generated_at`) come from fresh daily producers (06-09
11:30Z). The 2026-06-08 fix correctly switched AWAY from SmartX process clock, but tied the whole
panel to the MDPF spine — which can stall independently.

**Fix (ModelPortfolios.tsx):**

Part A — `distributionAsOf` (after `activeDistribution` definition, ~line 873):
```ts
const distributionAsOf: string | null = activeDistribution?.generated_at ?? null
```
Uses `activeDistribution` (already handles isPerFirm logic: per-firm or global distribution).

Part B — Divergence guard:
```ts
const spineIsStale = (() => {
  if (!dataAsOf || !distributionAsOf) return false
  const spineDay = dataAsOf.split('T')[0]
  const distDay = distributionAsOf.split('T')[0]
  return new Date(distDay).getTime() - new Date(spineDay).getTime() > 3 * 86_400_000
})()
```
3-day calendar grace covers normal weekends. Current 4-day lag (06-05 → 06-09) fires correctly.

Portfolio Analytics PanelFooter (line ~1379):
```tsx
<PanelFooter
  timestamp={distributionAsOf}
  content={modelSourceAttribution}
  leftContent={spineIsStale ? (
    <span>Spine as of {dataAsOf?.split('T')[0]}</span>
  ) : undefined}
/>
```

AUA timeseries chart footer (~line 1827) — UNCHANGED (correctly frozen to MDPF spine).

**Compiler gates:**
- `comp-transform schema-check ModelPortfolios` — WARN "no types.ts" (structural, same as PRTORG.04).
  Manual verification via aum.ts: `AccountDistribution.generated_at: string` (line 150) +
  `last_updated?: string` (line 117). Both fields in typed contracts.
- `typecheck` — EXIT 0

**Commit:** `c6f12701` on portal DEV.

### 4. v2.1.120 PROD verification

After DT promote (20260609T215644Z), verified on PROD at opalinvest.dev/portfolios:
- `"Spine as of 2026-06-05"` — divergence guard visible in footer leftContent ✓
- `"June 9th, 2026, 7:30a ET | Source: SMArtX..."` — Portfolio Analytics footer shows fresh
  account-distribution.generated_at (was June 5th before fix) ✓
- `"June 5th, 2026, 5:00p ET | Source: SMArtX..."` — AUA timeseries footer correctly frozen ✓

Note: error boundary on initial navigation was stale chunk hash (v2.1.119 session trying to
lazy-load ModelPortfolios-Bztw_QE4.js after v2.1.120 replaced it). Standard post-deploy SPA
behavior. Resolved by hard page.goto to get fresh index.html.

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| comp-transform | schema-check ModelPortfolios | WARN no types.ts — manual field verification PASS |
| typecheck | bun run typecheck | EXIT 0 |
| comp-transform | schema-check AdvisorIntelligence (prior session) | Component not found — manual verification PASS |
| comp-cache | collisions | 5 pre-existing shared-by-design; 0 new |

---

## Open Items

| Item | Gate | Owner |
|------|------|-------|
| AC1/AC4 Cottonwood PROD smoke | COT JWT + ownership_map.json + platinum data | AE_PartnerETL |
| AC2 JWT-firm isolation fix | Security audit + Lambda@Edge firmId cross-check | AE_CloudOps~B |
| MDPF_CADENCE stall (spine 06-05) | INF_D_08 fix | AE_CloudOps |

---

## Session Deliverables

| Artifact | Status |
|----------|--------|
| portal v2.1.119 — ADVI_PRTORG.04 Cottonwood module | LIVE, BD regression PASS |
| portal v2.1.120 — MDPF per-source timestamps + divergence guard | LIVE, PROD verified |
| AC2 JWT-firm isolation finding | Routed AE_CloudOps~B |
| c6f12701 push to origin/DEV | Done |

## Posture

IDLE. Awaiting AC1/AC4 re-run signal (AE_PartnerETL gate). Monitor bhhhasgtf live.
