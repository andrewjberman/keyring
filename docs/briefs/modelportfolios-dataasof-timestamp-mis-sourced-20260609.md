# Bug-note: ModelPortfolios "Portfolio Analytics" timestamp mis-sourced (stuck 06-05 while holdings update daily)

**Author:** 1.0.0_SA_CTO · **Date:** 2026-06-09 · **Route:** COO -> DE (portal, DEV->PROD promote discipline)
**Severity:** customer-facing correctness — a stale-looking "data as of" date on a panel whose numbers are actually fresh. Not a data-loss bug; a trust/label bug.
**Andrew-flagged:** 2026-06-09 ("timestamp still June 5th despite it now being June 9th… the data is updating, just the timestamp is broken").

## Symptom

On the Model Portfolios page, the "Portfolio Analytics" panel (radial/bell-curve = `AccountDistributionChart`) shows a "data as of" date stuck at **June 5** while the **total holdings and the bell-curve distribution change day-to-day**. Reproduces on global + both per-firm (49financial, inflection) views.

## Root cause (two layers)

**Layer 1 — pipeline (separate issue, already routed to AE):** the MDPF `aggregate-aua-timeseries.json` artifacts (the spine rollup) are **frozen at 06-05** — the MDPF daily chain (MDPF_CADENCE) has not advanced since 06-05 (INF spine sentinel not firing for 06-09; 06-08 chain dispatched-but-didn't-advance; BD silver stale at 06-05; `mdpf-daily-freshness-stale` alarm in ALARM). Routed to 0.7.0_AE_CloudOps this cycle.

**Layer 2 — FE label mis-sourced (this bug-note):** `ModelPortfolios.tsx:475-478` sets the panel timestamp `dataAsOf` from the MDPF aggregate artifact's `as_of_last`:
```
const dataAsOf =
  (effectiveFirmId === 'global' ? globalMdpfData?.as_of_last : perFirmMdpfData?.as_of_last) ??
  rawTimeSeriesData?.aggregate?.[…]?.period ?? null
```
But the **holdings + distribution numbers** on the same panel come from **different artifacts produced by different, healthy daily producers**:

| Panel element | Source artifact | Producer | Freshness (verified 2026-06-09) |
|---|---|---|---|
| `dataAsOf` timestamp | `…/mdpf/…/aggregate-aua-timeseries.json` (`as_of_last`) | MDPF daily chain (STALLED) | **06-05** |
| AUA timeseries chart x-axis | same MDPF artifact (`.dates`) | MDPF daily chain (STALLED) | **06-05** (consistent w/ timestamp — also frozen) |
| Total holdings / donut | `…/portfolios/aum-metrics.json` (`last_updated`) | separate daily producer | **06-09 11:30Z** |
| Bell curve (distribution) | `…/portfolios/account-distribution.json` + `…/mdpf/{firm}/account-distribution.json` (`generated_at`) | separate daily producer | **06-09 11:30Z** |

So the 2026-06-08 "MDPF_CADENCE FE-label fix" (which switched `dataAsOf` to `as_of_last` to stop a *different* lie — the SmartX process clock rendering "today" when the spine hadn't re-sampled) tied the panel's single "data as of" label to the **MDPF spine**, which can freeze independently of the fresh snapshot artifacts the panel also renders. When the spine stalled (06-05), the timestamp froze while holdings/distribution kept moving.

**Key nuance for DE:** the AUA *timeseries chart itself* is correctly 06-05 (it shares the frozen MDPF source) — do NOT "fix" it to show fake fresh points. The genuine divergence is **fresh snapshot (holdings/distribution) vs frozen timeseries+timestamp** sharing one label.

## Recommended fix (DE)

Pick one; (A) is the targeted fix, (B) is the robust pattern:

**(A) Per-source timestamps.** The distribution panel stamps `account-distribution.json`'s `generated_at`; the holdings/donut stamp `aum-metrics.json`'s `last_updated`; the AUA timeseries chart keeps the MDPF `as_of_last`. Stop applying one page-level `dataAsOf` (tied to the MDPF spine) across elements fed by fresher artifacts.

**(B) Spine-vs-snapshot divergence guard.** Keep a primary `dataAsOf` but compute `max(spine as_of_last, snapshot generated_at)` is NOT the answer (that would mask the spine staleness). Instead: when the MDPF `as_of_last` lags the fresh snapshot `generated_at` by > 1 trading day, surface an **explicit divergence label** ("Distribution as of 06-09 · model-mix spine as of 06-05") and/or a staleness chip — never a single silently-frozen date over fresh numbers. This also makes a future spine stall self-announcing on the surface instead of looking like fresh data with an old clock.

CTO lean: **(A) for the immediate correctness fix + (B)'s divergence guard as the durable hardening** — both are small, localized to `ModelPortfolios.tsx`.

## Compiler mandate (for the TO)
- `comp-transform schema-check ModelPortfolios` (Phase 1) — confirm the `generated_at` / `last_updated` fields are in the typed contracts for `account-distribution` + `aum-metrics`.
- `comp-cache collisions` if any new query key is introduced (not expected; reuses existing queries).

## Verify
- After fix on DEV: the distribution panel timestamp reflects `account-distribution.generated_at` (today), not the MDPF `as_of_last`. When the MDPF spine resumes (AE), the timeseries-chart date + any spine-labeled element advances; the divergence chip clears.
- This is a portal change → DEV first, then the standard DEV->PROD promote.

## Related
- Pipeline half: MDPF_CADENCE stall (AE_CloudOps, this cycle). When it resolves, the symptom partially clears even without the FE fix — but the FE fragility remains (any future spine stall re-triggers it), so the FE fix is the durable resolution.
- Origin of the current sourcing: the 2026-06-08 MDPF_CADENCE FE-label fix (`ModelPortfolios.tsx:470-474` comment). This bug-note refines that fix; it is not a revert.
