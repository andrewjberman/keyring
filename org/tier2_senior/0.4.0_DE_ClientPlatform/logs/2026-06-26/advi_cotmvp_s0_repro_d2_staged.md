# ADVI_COTMVP pod4-DE: S0 browser-repro grounding + D2 staged + B scoped
**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE
**serial:** 0.4.0_DE_ClientPlatform | **window:** 2026-06-26 ~1820Z -> 1919Z | **project:** ADVI_COTMVP (Andrew-sovereign COT dashboard fix)

## Summary
Spawned onto COO's now-active dispatch ADVI_COTMVP (PRD `docs/architecture/ADVI_COTMVP_PRD.md` @ a50387172, grounded in CVO breaks-audit 0a3092bfa). Own pod4 DE legs: S0 (blocking grounding) + B (/books) + D2 (.quarters guard) + D3 (young-tenant UX). DS owns D1 (gold NMNC) parallel. Drove S0 to a grounded finish, built+verified D2, scoped B. Now event-gated on CTO arch-gates.

## Work done

### S0 -- browser-repro to PIN Symptom-1 (BLOCKING) -- DONE + RAVC'd to CTO (185700Z)
Method: Playwright repro of the COT ADVI page (`/advisor-intelligence`) as internal-admin (= Andrew's view path) on local dev (`bun run dev :5175`), with the REAL served S3 artifacts injected. Local fake dev-token 401s the scoped data proxy (`/api/scoped/.../platinum/firm/*.json?firm=cot`), which blanked ALL firms' panels -- caught this as a LOCAL-AUTH ARTIFACT, not the symptom (Rule-22 trap avoided). Pulled actual `s3://opal-data-cot/platinum/firm/*.json`, served them to the component via a `window.fetch` stub, forced refetch.

GROUNDED FINDING -- Symptom-1 is NOT a hard blank. With real data:
- YEAR  -> ONE bar "2026"   = $401M NMNC  [browser DOM + tso.json aua.annually.data = 1 row]
- QUARTER-> ONE bar "Q2 '26" = $401M NMNC (identical to the cent)  [tso.json aua.quarterly.data = 1 row]
- MONTH -> THREE bars (Apr $0.17M / May $214M / Jun $30.7M NMNC + $371M NMEC) + deltas  [tso.json aua.monthly.data = 3 rows]
Mechanism (grounded, not inferred): COT ~3mo young tenant; non-stacked path `allSortedAuaPeriods = timeseriesData.aua[gran].data` (PartnerAnalytics.tsx:458). 1 annual + 1 quarterly row => lone single bar reads as "not displaying" next to the rich 3-bar Month view. => D3 IS the Symptom-1 fix (per PRD S0 sequence note). Compounded by D1 ($401M stock-as-NMNC, identical Year==Quarter, ~2380x monthly flow).
REFUTED: (a) GEO donut blank -- GEO "Segment Analytics" renders fully (AUM-by-state $401M, Texas 248acct 76.6% + 12 segments); (b) fetch/scope/CF failure -- symptom is granularity-SPECIFIC (Month works), which a fetch failure cannot be; all 3 served artifacts 200+populated. Could-not-verify residual (flagged, not claimed): a real external-COT-JWT deployed-env path.

### D2 -- .quarters schema-guard -- BUILT + VERIFIED, staged uncommitted (arch-gate req 190703Z)
Optional-chained the 3 `.quarters` sites the CVO audit flagged (PartnerAnalytics.tsx:381/405/423):
- :381 `usesStackedBars && inflecTimeseriesChart && inflecTimeseriesChart.quarters.length > 0` -> `usesStackedBars && (inflecTimeseriesChart?.quarters?.length ?? 0) > 0` (+ why-comment)
- :405 / :423 `(inflecTimeseriesChart.quarters as ...)` -> `((inflecTimeseriesChart?.quarters ?? []) as ...)`
Tenant-schema guard so a tenant whose timeseries_chart.json omits `quarters` (COT's divergent BD schema) cannot hit `undefined.length` if stacked-bars ever flips on. Provably NO behavior change (COT: inflecTimeseriesChart=undefined -> `(undefined?...?? 0) > 0`=false == old short-circuit; Inflection: quarters present -> identical). HELD uncommitted: PartnerAnalytics is a SEV1 shared surface -> presenting verified diff for CTO arch-gate, not front-running it.

### B -- /books firm-level (option A) -- SCOPED
BooksTab (in ClientsTab.tsx) is advisor-drill-centric but carries firm-level queries needing NO advisor selection: getPlatinumFirmDashboard / getPlatinumFirmMixSummary / getHeaderMetrics / feeEfficiency; ConsolidatedOverviewPanel consumes firm-mix periods cleanly. COT serves dashboard.json/mix_summary.json/header_metrics.json (S3-verified). Plan: render firm-aggregable panels WITHOUT the leaderboard->advisor->client->account drill; flag any panel hard-requiring the advisor dimension -> defer to option B. Final per-panel verification + spec on CTO panel-scope direction.

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-transform schema-check PartnerAnalytics | baseline (pre-D2) | PASS | "all rendered fields match their response types" |
| comp-transform schema-check PartnerAnalytics | post-D2 | PASS | clean after edit; no prop-contract change |
| comp-grep / comp-glob (portal Books search) | 1 ea | FAIL (0 files) | portal submodule not in comp working-set -> fell back to native Grep (Rule 21 nudge-and-proceed) |
- **What worked:** comp-transform schema-check bracketed the D2 edit (clean before/after) = the cross-tenant guardrail evidence (PRD S4).
- **What failed:** comp-grep/comp-glob scanned 0 files inside the portal submodule -- they don't descend into the nested repo, so portal-internal search needs native Grep.
- **Gap found:** comp-grep/comp-glob coverage gap for the portal submodule (nested-repo working-set). Worth a comp-tools follow-up (portal-aware search) -- repeat overrides for portal search = a real coverage gap per NFRA_COMPRAIL.

Also: `bun run typecheck` (tsc -b --noEmit) exit 0 post-D2; direct S3 pulls of all 3 partner_analytics grans + timeseries_overview to ground the data layer.

## Blockers
None blocking ME (verified). Remaining legs are GENUINE external gates, stated:
- D3 (Symptom-1 fix): gated on CTO S0 ruling (RAVC sent 185700Z).
- D2 land + B build: gated on CTO arch-gates (D2 req 190703Z; B scope in COO status 191143Z).

## Current State
- **S0:** grounded, RAVC'd to 1.0.0_SA_CTO. Conclusion: D3 is the Symptom-1 fix; D1 compounding.
- **D2:** working-tree edit on `portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx` (7+/3-), UNCOMMITTED. Verified (schema-check clean, tsc exit-0). Commit-on-GO via safe-commit.sh under my author line + workspace submodule pointer bump.
- **Repro rig still up:** local dev server (`bun run dev :5175`) running; `portal/public/__mockcot/` holds the injected real COT artifacts (UNTRACKED -- must NOT be committed; clean up at session end). Browser on the COT page w/ fetch stub. Technique banked: `memory/reference_advi_local_browser_repro_inject_served_artifacts.md`.
- **NFRA_TSGRAPH.P2-1:** parked (event-gated on AE P2-2) under this active dispatch.
- Portal main tree on DEV (Rule 19 OK).

## Next Steps
- **[1.0.0_SA_CTO]** rule on S0 (confirm D3 = Symptom-1 fix) + arch-gate D2 (verified diff) + give B panel-scope direction. All three gate my next execution.
- **[0.4.0_DE, me]** on CTO GO: commit D2 + bump submodule pointer -> CVO live-verify; scope+build D3 (young-tenant/single-bar UX); finalize+build B firm-level. comp-transform schema-check on every shared-PartnerAnalytics touch.
- **[0.4.0_DS_ClientPlatform]** D1 gold NMNC stock/flow fix (parallel, DS lane) -- align to 49F exemplar convention.
- **[3.0.0_SA_CVO]** standing live-verify on each landed leg (served-state).
- **[2.0.0_SA_COO]** RAVC tracker -- sequencing per dispatch.
