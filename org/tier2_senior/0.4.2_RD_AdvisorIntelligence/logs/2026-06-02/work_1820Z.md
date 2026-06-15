# /work cycle — 0.4.2_RD_AdvisorIntelligence~B — 2026-06-02 1820Z

## Tick: SENIOR_DISPATCH (COO DRIVE 181807Z) + INFNNA-W2 read-only pre-stage

### COO DRIVE handled
1. **INFOTD bundle STAGED on DEV** — W1 (836c02fd) + W2F (80f285c8) impl-complete; COO committed my TO-statuses under `f5637a0c0` (resolved tilde owned-paths gap). PROMOTE: **Andrew doing the visual smoke himself** → I HOLD the DEV→PROD promote for his GO via CTO. Will not promote in isolation.
2. **INFPRM W1 → new RD ~C lane + AE for W2** — off my plate (Andrew parallel-velocity directive). My P0 brief (c35e3cd40) sizes both for ~C/AE.
3. **My next = INFNNA.P2.W2** (FE repoint + weekly-fallback removal) — GATED on DS INFNNA W1 (canonical GEO emit, DS building now).

### INFNNA-W2 pre-stage (read-only, no writes — gated)
Mapped the exact repoint: **`barData` useMemo, DistributionTab.tsx:1549-1608.**
- Branch 0 (`:1554`, canonical advisor_nna_canonical.json) serves ONLY Level-0 firm + Level-1 ADV-advisor; `!drillChild` guard + null GEO source → GEO-L1(state) + GEO-L2(city) + ADV-L2(client) fall to...
- Branch 1 (`:1582`, computeLegacyBarData) = weekly cumulative_chart pairwise-diff (~65% YTD undercount). **This is what W2 removes for the drill levels.**
- Branch 2 (`:1586`) = canonical per-period (timeseries_overview), Level-0 only.

**W2 plan:** extend Branch 0 to read DS's new `canonicalNna.geo.states.<S>.series` (GEO L1), `.cities.<C>.series.monthly` (GEO L2), `canonicalNna.advisors.<a>.clients.<hh>.series.monthly` (ADV L2); relax `!drillChild` guard; reuse window_bounds filter + `{period,inflows,outflows:-abs,net:nna}` map (`:1564-1575`). Then Branch 1 demotes to pure rollout-lag fallback = **W3 universal fallback-removal**.

**Sent DS 4 shape questions** (gate my consume): (1) canonicalNna.geo top-level key, (2) monthly-only granularity at L2 leaves, (3) window_bounds reuse at leaf series, (4) key casing + 'Other'/'no_city'/'unassigned' catch-all literals. Lets W1+W2 land clean in one pass.

## Standing
- INFOTD: STAGED, holding for Andrew smoke + CTO promote-GO.
- INFPRM: off my plate (~C/AE).
- INFNNA-W2: pre-staged, gated on DS W1 + dispatch.
- Owned-paths: COO committing on my behalf (f5637a0c0); path-class add still pending for self-commit.
Nothing blocked on me.
