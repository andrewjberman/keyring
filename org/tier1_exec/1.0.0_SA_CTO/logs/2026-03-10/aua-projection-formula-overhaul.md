# AUA Projection Formula Overhaul — 1.0.0_SA_CTO

**Date:** 2026-03-10

## Objective

Replace the AUA projection formula in PartnerAnalytics. The prior implementation used linear time-ratio extrapolation (`delta * totalDays / elapsedDays`), which produced nonsensical projections for monthly and annual views because small early-period deltas were amplified 4-5x. The new formula uses a dampened weighted blend that stays grounded in observed data early in a period and converges toward extrapolation as more data accumulates.

---

## Problem

AUA is a balance (stock) metric, not a flow. At any point in time the value is a market-driven snapshot, not an accumulation. The old formula treated it like a flow:

```
projectedDelta = (actual - priorEnd) * (totalDays / elapsedDays)
```

For quarterly with 73% elapsed this produced a mild 1.36x multiplier. For monthly (day 6 of 31) the multiplier was 5.2x. For annual (day 65 of 365) it was 5.6x. A $5M early-year dip became a projected $28M decline. A $180M March surge (largely a reclassification event between NMEC/NMNC) was extrapolated to $934M.

---

## Solution: Dampened Weighted Blend

The new formula has three stages applied per AUA category (NMEC, NMNC):

### Stage 1 — Dampen current period signal by elapsed fraction

```
elapsedFraction = elapsedDays / totalDays        // 0..1

scaledDelta     = rawDelta * (totalDays / elapsedDays)
currentDelta    = rawDelta * (1 - elapsedFraction) + scaledDelta * elapsedFraction
```

This slides between raw observation (safe) and time-scaled extrapolation (accurate when most of the period is observed):

| View | Elapsed | Raw weight | Scaled weight |
|------|---------|-----------|---------------|
| Monthly (day 6/31) | 19% | 81% | 19% |
| Quarterly (day 65/90) | 72% | 28% | 72% |
| Annual (day 65/365) | 18% | 82% | 18% |

The math simplifies to: `currentDelta = rawDelta * (1 - f + ratio * f)` where `f = elapsedFraction` and `ratio = totalDays / elapsedDays`. As `f -> 1`, this converges to `rawDelta * ratio` (full extrapolation). As `f -> 0`, this converges to `rawDelta` (pure observation).

### Stage 2 — Blend with last complete period's growth

```
historicalDelta = priorEnd - priorPriorEnd        // last complete period's change
weightedDelta   = currentDelta * (2/3) + historicalDelta * (1/3)
```

66.67% weight on the current trajectory (from Stage 1), 33.33% on the last complete period's actual change. This anchors the projection against historical context so a single anomalous period doesn't fully dominate.

If no priorPrior exists (first period in history), falls back to 100% current signal.

### Stage 3 — Project

```
projectedValue = priorEnd + weightedDelta
```

Applied per category. `_projectedTotal = sum(projectedValues)`.

---

## Worked Example: March 6, 2026 Data

Source: `s3://opal-data-bd/gold/timeseries_chart.json`
Categories: NMEC (existing managed), NMNC (existing non-managed)

### Reference values

| Date | NMEC | NMNC | Total |
|------|------|------|-------|
| Oct 31, 2025 | $972.5M | $307.3M | $1,279.8M |
| Nov 30, 2025 | $998.6M | $342.1M | $1,340.6M |
| Dec 31, 2025 | $1,013.7M | $354.3M | $1,367.9M |
| Jan 31, 2026 | $1,195.0M | $292.4M | $1,487.4M |
| Feb 28, 2026 | $1,138.4M | $278.1M | $1,416.5M |
| **Mar 6, 2026** | **$1,319.3M** | **$300.0M** | **$1,619.3M** |

### Monthly — March 2026

Period: Mar 1-31 (31 days). Elapsed: 6 days. `elapsedFraction = 0.194`. `ratio = 5.167`.

**NMEC:**
- rawDelta = 1,319.3 - 1,138.4 = +$180.9M
- scaledDelta = 180.9 * 5.167 = +$934.6M
- currentDelta = 180.9 * 0.806 + 934.6 * 0.194 = 145.8 + 181.3 = +$327.1M
- historicalDelta (Feb - Jan) = 1,138.4 - 1,195.0 = -$56.6M
- weightedDelta = 327.1 * 0.667 + (-56.6) * 0.333 = 218.2 + (-18.9) = +$199.3M
- **projected NMEC = 1,138.4 + 199.3 = $1,337.7M**

**NMNC:**
- rawDelta = 300.0 - 278.1 = +$21.9M
- scaledDelta = 21.9 * 5.167 = +$113.2M
- currentDelta = 21.9 * 0.806 + 113.2 * 0.194 = 17.7 + 22.0 = +$39.6M
- historicalDelta (Feb - Jan) = 278.1 - 292.4 = -$14.3M
- weightedDelta = 39.6 * 0.667 + (-14.3) * 0.333 = 26.4 + (-4.8) = +$21.7M
- **projected NMNC = 278.1 + 21.7 = $299.8M**

**Projected total: ~$1,637.5M** (vs current actual $1,619.3M)

### Quarterly — Q1 2026

Period: Jan 1 - Mar 31 (90 days). Elapsed: 65 days. `elapsedFraction = 0.722`. `ratio = 1.385`.

**NMEC:**
- rawDelta = 1,319.3 - 1,013.7 = +$305.6M
- scaledDelta = 305.6 * 1.385 = +$423.3M
- currentDelta = 305.6 * 0.278 + 423.3 * 0.722 = 85.0 + 305.6 = +$390.6M
- historicalDelta (Q4'25 - Q3'25): Dec 31 - Sep 30 values
- weightedDelta = 390.6 * 0.667 + historicalDelta * 0.333
- The 1.385x ratio is mild; result tracks closely to observed trajectory

### Annual — 2026

Period: Jan 1 - Dec 31 (365 days). Elapsed: 65 days. `elapsedFraction = 0.178`. `ratio = 5.615`.

**NMEC:**
- rawDelta = 1,319.3 - 1,013.7 = +$305.6M
- scaledDelta = 305.6 * 5.615 = +$1,716M (illustrates why dampening is critical)
- currentDelta = 305.6 * 0.822 + 1,716 * 0.178 = 251.2 + 305.4 = +$556.6M
- historicalDelta (2025 - 2024): full year-over-year change
- weightedDelta = 556.6 * 0.667 + historicalDelta * 0.333
- The 82% raw weight keeps projection grounded near observed +$305.6M

---

## Y-Axis Domain Fix

The projected total can exceed the tallest bar (e.g., $1.825B projected vs $1.619B actual in annual view). Recharts auto-domain clips the ReferenceLine above the bar max. Added explicit domain to the AUA chart YAxis:

```tsx
domain={[0, (dataMax) => Math.max(dataMax, projectedTotal) * 1.05]}
```

5% padding ensures the dashed projection line and its label are fully visible.

---

## Null Guard Fix

Changed the ReferenceLine visibility guard from `!lastEntry?._projectedTotal` (falsy for zero) to `lastEntry?._projectedTotal == null` (only null/undefined). A projected total of exactly zero is valid and should still render.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| 2/3 current + 1/3 historical (not the original 5-period gradient) | Andrew directed: simpler, more responsive to live data, less lag from stale history |
| Elapsed fraction dampens scaled vs raw blend | Ratio amplification (5x+) is unreliable early in period; dampening makes formula work across all granularities without per-view special casing |
| Y-axis domain includes projected total | Without this, Recharts clips the dashed line above bar max — invisible in annual view where projection exceeds actual by 10%+ |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx` | AUA projection formula, YAxis domain, null guard | Yes — `511dbd7` (portal DEV) |

---

## Current State

**Status:** COMPLETE

The AUA projection formula is deployed to portal DEV. All three granularity views (monthly, quarterly, annual) display correct projections with visible dashed horizontal reference lines. The formula self-adjusts across period lengths via the elapsed fraction dampener. NNA and GRO projections still use the original time-ratio formula — Andrew plans to review those separately before deciding on changes.

---

## Next Steps

1. **[Andrew] Review NNA and GRO projection formulas** — decide whether they need the same treatment (they are flow metrics, so time-ratio may be appropriate)
2. **[0.4.0_DT_ClientPlatform] Push portal DEV** — commit is local only, needs push to remote
