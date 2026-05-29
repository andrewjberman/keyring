# /work cycle — 0.4.0_DE_ClientPlatform — 2026-05-29 ~2005Z

Session reopened on MDPF_SCOPED (Andrew empirical smoke). Two substantive items this cycle.

## 1. MDPF D1 — firm-scoped Daily-AUA data-query trace (COO [DRIVE GO])

**Mandate:** own the data-query/binding layer of defect #1 (firm-scoped 49F/Inflection Daily-AUA returns NO data in portal). Confirm the query reads the right per-firm S3 key + shape matches `MdpfPerFirmTimeSeries`.

**Finding: data-query layer is CORRECT end-to-end. NO query-key/shape/route/data gap. The empty-state was PRE-PUBLISH TIMING.**

End-to-end trace:
- `perFirmMdpfData` useQuery (ModelPortfolios.tsx L179-184) → `getMdpfAggregateAUATimeSeriesByFirm(firmId)`, firmId ∈ {`49financial`,`inflection`} (L89-90)
- → `apiRequest('/api/general/mdpf/{firmId}/aggregate-aua-timeseries.json')` (portal-proxy.ts L496-499)
- CF rewrite (`lambda-edge/public-data-router/index.mjs`): `/api/general/*` → `/json/*` → resolved S3 key = `json/mdpf/{firmId}/aggregate-aua-timeseries.json`
- **NOTE:** portal-proxy doc-comment ("→ platinum/mdpf/...") is MISLEADING. Live serving prefix is `json/`, not `platinum/`. Publish step copies platinum→json + renames `aggregate_aua_timeseries.json` (underscore) → `aggregate-aua-timeseries.json` (hyphen). Both handled correctly.

Verified from S3 (both serving artifacts present + fresh, generated `2026-05-29T19:38:07Z`):
- `json/mdpf/49financial/aggregate-aua-timeseries.json` (91.7KB; partner_custody_total $776M; 7 models; n_dates=402)
- `json/mdpf/inflection/aggregate-aua-timeseries.json` (70.3KB; $148M; 7 models; n_dates=402; 2024-11-01→2026-05-29)
- Shape = full `MdpfPerFirmTimeSeries`; TS types (portal-proxy.ts L407-442) match artifact + component transform (ModelPortfolios.tsx L336-354) exactly. No slimming.
- Live CF unauth 401 uniform across firm AND global paths (auth-validator-edge at viewer-request) — no firm-vs-global routing difference; CLI cannot auth.

**Disposition:** NOT a DS~B fix (data correct + complete) and NOT a DE query-key fix (query correct). Handed RD~B (0.4.2_RD~B) the confirmed query + resolved key + shape evidence to bind D1 (Daily AUA chart) + D3 (Portfolio Analytics panel). RAVC2 to COO. Final return-data gate = RD~B authenticated visual smoke (render lane).

## 2. ADVI_DEMOV1.010 — demo tenant data-source label (carry-open, D1-first done)

Andrew UAT F3: demo Data Source panel showed "Black Diamond Connected: Source: SS&C Black Diamond Wealth Solutions." (49F-template leak) → now "Database Connected: Lone Pine Analytics" (demo pseudonym identity).

- 3 files: `demo/{index.tsx,constants.ts,layout.ts}` — span text, BD_SOURCE_ATTRIBUTION + tooltips, primaryCustodian (dormant field), comment rationale.
- AC1 satisfied (renders "Database Connected: Lone Pine Analytics"); AC2 satisfied (demo/* grep-clean of "Black Diamond"); `tsc -b --noEmit` exit 0.
- Shipped portal/DEV **81fc3b38**, pushed origin/DEV (VALGATE D-1 PASS). RD~B's concurrent ModelPortfolios.tsx + modelPortfolioColors.ts WIP left untouched (--only scoping).
- AC4 authenticated visual smoke deferred to DT PROD-promotion / Andrew (CLI cannot auth demo tenant; playwright MCP unavailable this session). Cognito→DynamoDB fold-in skipped per TO scope L33 (routed to CTO v0.4.2).
- COO RAVC2-ACCEPTED (clean closeout; AC4 visual rides DT/Andrew glance).

## 3. MDPF D3 unblock — answered RD~B's 2 shape Q-MCPs (COO critical-path)

D1 resolved (pre-publish) + D2 (naming) landed by RD~B; D3 (Portfolio Analytics panel + AUA-by-Model radial re-scope on selectedPartner) was the last MDPF defect, blocked on my shape-confirm.

Answered from live json/mdpf/{firm}/ artifacts:
- **by_model is data-driven 7-per-firm, DIFFERENT per firm:** Inflection = 5 base models + 2 BLENDS ('50/50 INT/LTC','50/50 ST/INT'), all cohort_class='model'. 49F = 5 base 'model' + 2 'sma' (Dividend SMA, Opal Equity Growth SMA). Told RD~B: render donut data-driven from actual by_model (NOT hardcode-5, NOT cohort_class filter for a 5-selector) + Non-Model from non_model_aua.
- **No canonical collisions** (verified vs CANONICAL_MODEL_NAME L125-147: 'Long Term'≠'Ultra-Long Term'; blends/SMAs pass through verbatim). 7 distinct names per firm.
- **Quarterly AUMGrowthMetrics:** confirmed RD~B derives per-firm quarter-end from daily partner_custody_total (authoritative; no per-firm quarterly object).
- **Distribution bell-curve = GLOBAL-ONLY** (verified: no per-firm distribution artifact; json/portfolios/account-distribution.json single global file, getAccountDistribution takes no firmId). Flagged COO: scope-call A (FE graceful-degradation now) vs B (DS~B per-firm distribution slice).

COO disposition: PATH A AFFIRMED (RD~B builds — re-scope left partition fully + explicit-labeled aggregate bell-curve on right; closes the radial defect Andrew named). PATH B (per-firm bell-curve) surfaced to Andrew (his "everything should change" call); DS~B held-ready. Pre-scoped the Path-B DE endpoint (getAccountDistributionByFirm → /api/general/portfolios/{firmId}/account-distribution.json, existing CF rewrite, no infra) for fast handoff if greenlit.

## 4. portal-proxy doc-comment fix (COO-flagged follow-on)

Fixed the misleading "→ platinum/mdpf/..." doc-comments on the MDPF aggregate + per-firm endpoints (portal-proxy.ts) — live serving is json/ via the CF /api/general/*→/json/* rewrite; platinum/ is the build-tier source. Comment-only, no behavior change. Shipped portal/DEV **03dddcae**, pushed origin/DEV (VALGATE PASS).

## Cycle outcome
MDPF: D1 accepted, D2 landed, D3 unblocked (Path A building), DEMOV1.010 shipped+accepted, doc-drift fixed. Idle pending RD~B Path-A completion + Andrew Path-B call. Older non-MDPF queue held per COO steer until MDPF fully closes.
