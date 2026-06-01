# BMKAUD — Peers UST 1M "no display" — FE-symptom-location diagnosis (RD leg)

- **Author:** 0.4.2_RD_AdvisorIntelligence~B
- **Date:** 2026-06-01
- **Trigger:** COO [DRIVE] 20260601T144035Z — BMKAUD WS-2 classified Andrew's "Peers UST shows no 1M" symptom to the RD lane. DS~B proved the served UST-1M value is faithful to the source xlsx (data faithful), so the gap is FE-side. Task: DIAGNOSE only; HOLD the fix (audit mid-flight; Andrew has a pending 1M/1Q window-definition ruling).
- **Verdict:** Confirmed FE-side display bug. Falsy-zero guard suppresses a present, faithful value. **Fix HELD per COO.**

## Symptom
On the Model Portfolios → Peers tab, with UST selected, the **1M** quartile chart renders **"No data available"** even though UST's 1M model return exists in the data.

## Root cause (precise)
`portal/src/pages/ModelPortfolios/tabs/PeersTab.tsx:143` — the `QuartileChart` render guard:

```tsx
if (!data || !data.percentiles.p95) {
  return ( ... "No data available" ... )
}
```

This is a **truthy** test on `percentiles.p95`. The served JSON for UST 1M (verified against `s3://opal-data-portal-v2/json/peers/peer_performance.json`, 2026-06-01) is:

```json
"UST": { "periods": { "1M": {
  "percentiles": { "p5": 0.3126, "p25": 0.2926, "p50": 0.2664, "p75": 0.0919, "p95": 0.0 },
  "model": 0.3017, "benchmark": 0.1639
}}}
```

`p95` is exactly **`0.0`**. In JS, `!0.0 === true`, so the guard short-circuits to "No data available" — suppressing the present and faithful `model: 0.3017` and `benchmark: 0.1639`. It is a **falsy-zero conflation**: a legitimate `0.0` bottom-of-range percentile is treated as "missing data."

### Why the symptom is UST-specific
UST is the only model whose **1M `p95` is exactly 0.0**. Compare ST 1M (`p95: 0.7018`), which renders fine. The 1M peer universe's lowest-percentile (p95) for the ultra-short-term sleeve happens to be 0.00%, uniquely tripping the truthy guard for UST.

(Periods array = `["1M","QTD","1Q","YTD","1Y","Since Inception"]`; UST has all six period keys — so the 1M column IS attempted; the guard is what kills it. Not a missing-column or missing-field issue.)

## Secondary site (same bug class)
`PeersTab.tsx:415` — the global Y-scale inclusion loop:
```tsx
if (periodData && periodData.percentiles.p95) { ... include in globalMin/globalMax ... }
```
Same truthy gate on `p95`. A period with `p95 === 0.0` is excluded from the shared Y-axis scale. (Moot for UST-1M while line 143 hides the chart entirely, but it's the same latent falsy-zero bug and would matter if the chart rendered.)

Note: the `|| 0` fallbacks in the segment/scale math (e.g. `percentiles.p95 || 0`) are acceptable for plotting (0 is a valid coordinate), so they are NOT the display-killer. The display-killer is specifically the truthy **guard** at line 143.

## Proposed fix (HELD — do not implement until COO GO post-audit-consolidation)
Change the guard from a truthy test to an explicit presence test, e.g.:
```tsx
if (!data || data.percentiles.p95 == null) { ... "No data available" ... }
```
(`== null` catches both `null` and `undefined`, admits a real `0.0`.) Apply the same change at line 415. A more robust variant would gate on "all percentiles null" rather than p95 alone, since p95 being the sole presence-sentinel is itself fragile.

**Why held:** BMKAUD is mid-flight and Andrew has a pending 1M/1Q window-definition ruling that may change which periods/values surface on this tab. The falsy-zero guard is a pure FE bug independent of that ruling, but the actual edit should land in the audit's consolidated FE pass so it composes with any window-definition change (and any data-writer requantine outcome). One-line change when GO'd.

## Scope confirmation
- Read-only diagnosis. No code changed, no commits. Portal main tree confirmed on DEV (Rule 19) for inspection.
- Data faithfulness (DS~B) corroborated: `model: 0.3017` is present in the served artifact; the gap is purely the FE render guard.
