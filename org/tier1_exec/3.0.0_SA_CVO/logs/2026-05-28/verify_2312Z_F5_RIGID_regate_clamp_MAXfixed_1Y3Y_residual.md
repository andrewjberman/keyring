# CVO F5 RIGID re-gate #2 — emit-clamp re-serve (d679d8a60, artifact 23:07:11Z)

**archetype:** VALIDATE
**Trigger:** DS-CP emit-clamp re-serve (in-progress bucket period_end -> data_as_of). Empirical re-gate vs re-served artifact.

## VERDICT: MAX FIXED ✓ — but STILL BLOCKED at 1Y/3Y (continuous hero vs Lifetime headline)

### FIXED by the clamp (credit DS-CP) — MAX overlap, all advisors
Current-quarter bucket now period_end=2026-05-27 (was 2026-06-30); included by every window filter. Re-verified empirically on the re-served artifact:
- Peter/Joe/Patrick MAX: ExecSummary windows[MAX] == quarterly == monthly == weekly series-filtered == $108,959,119.23 / $10,332,532.49 / $14,984,690.98. EXACT, all granularities.
- No-regression CLEAN: QTD/YTD/q1 anchors unchanged; fee-split invariant 0 failures; all 3 series tie to MAX exact.

### STILL BLOCKED — 1Y / 3Y cross-panel headline inequality
The two panels display a DIFFERENT NNA for the same advisor + same "1Y" (and 3Y) window, because they source the headline scalar differently:
- **Continuous chart HERO** (`DistributionTab.tsx:1651-1659` heroMetrics.totalNet = `sum over barData`; default granularity `quarterly` line 826): sums the WINDOWED BARS -> granularity-dependent.
- **Lifetime panel HEADLINE** (`AdvisorAnalytics.tsx:377-382` canonicalWindowTotals = `entry.windows[W]`): reads the PRECOMPUTED window total -> granularity-independent, exact-boundary.

Empirical (Peter, re-served artifact):
| window | Continuous hero (sum bars, quarterly) | Lifetime headline (windows[W]) | gap |
|---|---|---|---|
| 1Y | $12,587,630.25 | $13,796,544.32 | $1,208,914.07 |
| 3Y | $24,464,137.77 | $22,366,386.69 | $2,097,751.08 |
| MAX | $108,959,119.23 | $108,959,119.23 | 0 (fixed) |

(Granularity-dependence of the hero: Peter 1Y quarterly $12.59M / monthly $13.52M / weekly $13.80M — only weekly ~ the precomputed exact. The hero changes with the granularity toggle; the Lifetime headline does not.)

### Root cause
The clamp fixed the END boundary (current incomplete period). The remaining divergence is the trailing-window START boundary: 1Y starts 2025-05-27 (mid-Q2'25), 3Y starts 2023-05-28 (mid-Q2'23) — mid-quarter. Summing whole coarse buckets that straddle that start boundary cannot reproduce the exact-boundary precomputed windows[W]. The continuous hero sums the bars; the Lifetime headline + Exec Summary read windows[W]. Same-label, different-number -> violates the F5 mandate ("NNA cannot vary between the Segment Analytics panel and the Lifetime Activity panel for the same window").

### Fix (single-source the hero scalar — same principle as the Exec Summary repoint that worked)
Continuous chart heroMetrics.totalNet should read `windows[W].nna` (precomputed — the same source Lifetime headline + Exec Summary already use), NOT sum the windowed bars. The bars remain the trend SHAPE; the hero number becomes the canonical window total. Then continuous hero == Lifetime headline == Exec Summary == windows[W], every window, every granularity. (Note: the leftmost bar at a mid-period window start is honestly a partial period; the hero-from-windows[W] is the authoritative total regardless.)

### Posture
MAX clean; QTD/YTD clean (Exec Summary, precomputed); continuous==Lifetime BAR agreement holds (same granularity). Residual is the continuous-hero-source at 1Y/3Y — one FE line-class change, FE-only (no emit/data change; substrate + clamp are correct). Re-gate again on re-ship.

— 3.0.0_SA_CVO
