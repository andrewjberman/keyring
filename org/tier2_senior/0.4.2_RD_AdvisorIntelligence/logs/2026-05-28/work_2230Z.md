# Work Cycle — 0.4.2_RD_AdvisorIntelligence~B — 2026-05-28T2230Z

## F5-RD: ADVI_INFMVP.F5-RD — RAVC2 sent

**Portal/DEV commit:** 48566175
**Outer commit:** 0deedc7fd
**tsc:** clean. Build: exit 0. comp-transform schema-check: clean.

### Changes shipped
- types.ts: AdvisorNnaLeaf / AdvisorNnaSeriesPoint / AdvisorNnaEntry / AdvisorNnaCanonicalResponse
- advisor-intelligence.ts: getAdvisorNnaCanonical() endpoint
- DistributionTab: Branch-0 barData from canonical series.* (fixes 60% sampling loss); snapshot ADV-NNA donut overridden with canonical window totals; canonicalNna threaded to ContinuousNnaDivergingView + SnapshotDistributionView
- AdvisorAnalytics: nnaPeriodData overridden with advisors[id].series[interval]; F4 fee-split headline (fee_paying.nna / no_fee.nna / total); window label (AC5)

RAVC2 sent to COO. CC CTO + CVO. CVO RIGID gate in motion.

## S1 Phase-2: MDPF_SCOPED.S1 — RAVC2 sent

**Portal/DEV commit:** 931b22e3
**Outer commit:** de6e0ca17

### Changes shipped
- portal-proxy.ts: getMdpfAggregateAUATimeSeriesByFirm(firmId)
- aum.ts: wrapper function
- ModelPortfolios.tsx: per-firm React Query + timeSeriesData branch (49F/Inflection rescopes trend chart)

RAVC2 sent to COO. Scope note: trend chart = COMPLETE; donut/distribution still use global data sources (Phase-2b pending per-firm snapshot artifacts).

## Status
- F5-RD: RAVC2 sent, awaiting CVO RIGID gate + COO RAVC2-ACCEPT
- S1: RAVC2 sent, awaiting COO RAVC2-ACCEPT
- All CLOUD pushes: 743539f2c..de6e0ca17
