# /work cycle — ADVI_INFDEMO.001 IWM demo-prep (2026-05-28 ~1352-1418Z)

Agent: 0.4.2_RD_AdvisorIntelligence. TO: ADVI_INFDEMO.001 (CTO 47de0e461; COO 1352Z bundle = same scope, dedup'd to one). PRD: docs/architecture/ADVI_INFDEMO.md. Demo: IWM, today early-afternoon.

## Shipped (portal DEV, pushed origin/DEV; ws submodule bumped 646e386f0)
- **F1** (f61cb40b): ModelPortfolios.tsx:172 default benchmark `index`->`etf`.
- **F2** (f61cb40b): ETF/Index toggle hidden behind `SHOW_BENCHMARK_TOGGLE=false` (reversible; Returns toggle + benchmarkType logic intact).
- **F3** (f61cb40b): getPlatinumAdvisorSummaryStaticInflection maps `headline.historical_quarters`->`mix_periods` (FirmMixPeriodPoint[]); `raw.mix_periods ?? mapped` precedence; per-class zero-default (known limitation). NOTE: data is at `headline.historical_quarters` (nested, post-3-envelope-merge), not top-level `raw.historical_quarters` as PRD literal wrote — used type-safe accessor. CVO verified PASS (428454ac1).
- **F3b** (4bdb844e): graceful-hide chips when active_since/role absent. SUPERSEDED-IN-PRINCIPLE — see below.

Verified by me: bun run build PASS (every step), comp-transform schema-check ConsolidatedOverviewPanel clean, VALGATE D-1 PASS/WARN (pre-existing nested-schema-drift WARN). CVO F3 + F5 PASS. RAVC2 sent COO + CC CTO (140531Z).

## Open gates (legitimate gated-standby)
- **.001 visual-confirm**: no browser-automation tool in this agent env — cannot screenshot the auth-gated SPA. Routed to Andrew (live :5173) / CVO. TO held in_progress.
- **F3b wire-vs-hide**: DS empirical (1415Z) — Peter Lee book.json DOES emit active_since="2023-10-02" + role via role_breakdown.advisor. So my hide was on a false-absence premise; correct branch is AC3b.2 WIRE. Traced gaps: ROLE_KEYS (L129) omits "advisor" key; primaryRole reads leaderboard rawEntry not book.json advisorSummary.role_breakdown; active_since via getPlatinumAdvisorDrilldownSummary needs mapping confirm. SCOPE-FLAGGED to CTO (141755Z) w/ plan + recommend WIRE; awaiting GO. Graceful-hide stays as safe fallback.
- **F4 Cost Basis by-Year suppress**: posture churned COO 1413Z (suppress) -> 1415Z (don't, race DS fix, keep visible) -> 1418Z (HIDDEN is safe default, unhide only if DS fix verifies $166M). Current: `SHOW_COST_BASIS_BY_YEAR=false` (HIDDEN), commit e6e105df local DEV, build PASS, NOT pushed (held for Andrew nod per CTO+COO). Staged for one-line flip either direction per COO decision tree. AUA-by-Tax-Status bar + Unrealized/Realized cards always visible.

## Discipline notes
- Held origin push for F4 (client-facing UI suppression) per CTO caution — CTO+COO both confirmed correct.
- Flagged F3b scope change rather than silently expanding (CTO "flag if bigger than it looks").
- No browser tool: stated visual-confirm gap explicitly rather than claiming a visual pass.
