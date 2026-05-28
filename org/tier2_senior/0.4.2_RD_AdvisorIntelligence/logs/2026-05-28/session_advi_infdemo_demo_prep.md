# Session log — 0.4.2_RD_AdvisorIntelligence — ADVI_INFDEMO demo-prep (2026-05-28)

**Agent:** 0.4.2_RD_AdvisorIntelligence (Tier-2 RD, AdvisorIntelligence frontend lane)
**Arc:** Session-start startup + TO-reconciliation → IWM (Inflection Wealth Management) demo-prep frontend batch (Andrew-direct, demo TODAY). Portal DEV only (Rule 19).
**Lane COO:** 2.0.0_SA_COO. **Lane CTO:** 1.0.0_SA_CTO. **Data SME:** 0.4.0_DS_ClientPlatform.

## 1. Startup
- /watcher self-heal: registered LIVE, launched tracked inbox-watcher. /work cron armed (20m). Watcher needed several mid-session kill+relaunch cycles (recurring exit-143 / AUTO-RESPAWN-INTERRUPT-LOST) — handled each per /watcher Step 4.
- **TO-status reconciliation** (commit `77cb902db`, CLOUD): 4 stale TO headers flipped to committed/accepted ground-truth (entity-truth sweep) — RD2/RD3 active→complete (shipped weeks ago), INFLV2.010 open→complete (FULL PASS 2026-05-01), INFGRD.004 open→cancelled (Andrew ON HOLD, superseded by ORIAPI). No code change; just header drift.

## 2. ADVI_INFDEMO batches (portal DEV; all build + comp-transform schema-check clean)
All commits below are on **origin/DEV** (HEAD `c50a58b9`; pushed — see §4).

### .001 (CTO 47de0e461) — `f61cb40b`, `4bdb844e`, `d158fe85`
- **F1** ModelPortfolios default benchmark `index`→`etf`.
- **F2** ETF/Index toggle hidden behind `SHOW_BENCHMARK_TOGGLE=false` (reversible; Returns toggle + logic intact).
- **F3** Inflection Books-tab lookback AUA: map `headline.historical_quarters`→`mix_periods`. NOTE: data is nested in `headline` post-3-envelope-merge, not top-level `raw` as PRD literal wrote — used the type-safe accessor. CVO-verified PASS (`428454ac1`).
- **F3b** active-since/role header chips. Andrew ruling: IWM has no explicit roles (taxonomy is 49F-specific) → role chip graceful-HIDDEN; active_since WIRED (`advisorSummary?.active_since ?? drilldownSummary`, 49F-safe — shows "Oct 02, 2023"). LinkedIn-derived roles deferred.

### F4 — `d057f2b7`/`0172b01e`/`e6e105df` (final: hidden)
- Cost Basis by-Year table suppressed via `SHOW_COST_BASIS_BY_YEAR=false`. CVO `a8be3399e`: $166M reconciliation PASSED but per-year breakdown has attribution artifacts → keep suppressed for demo. Posture churned (suppress→race→hidden-default) across COO 1413/1415/1418/1440Z; final = hidden.

### Donut + Top Holdings fix — `b0089ab0` (Andrew-direct)
- Root cause: `getPlatinumAdvisorSummaryStaticInflection` fetched only `book.json` (no `composition`); asset-mix + holdings live in a SEPARATE INF_D_03 `composition.json`. Fix: fetch composition.json in parallel (Promise.allSettled, graceful) + use it as composition source. Mirrors the L3 client pattern. Inflection-scoped. DS-confirmed data was correct.

### .002 (CTO efdcd80b3) — `b5487690`
- **F6** Unrealized→blue / Realized→orange recolor + titles moved outside the card (CLIENT LIST header style). SHARED component (advisor/client/account/49F).
- **F8** Advisor Split default 100% (IWM single-advisor) + SPLIT(BPS) col full bps; real split wins.
- **F9** "Advisor Revenue (Estimated)" = split × windowed firm revenue, tracks Window toggle.

### F7 — `ecfb18b7` (folded into .002 per CTO pre-auth + DS confirm + Andrew direct)
- L3 client tax-status bar empty: `getPlatinumClientDetailStatic` `detail.tax` mapped only realized/unrealized. Added taxable/tax_deferred/tax_free + pcts from `detail.json summary.tax` (+ extended raw type). Verify against fresh in-scope hh (peter_lee 108/1352).

### F11/.003 (CTO 190ab0e43) — VERIFIED-READY, no FE change (`98bbe3ac0` TO flip)
- Fee-sliced flows: traced `getFirmLeaderboard` (raw JSON.parse passthrough, identical to 49F) → applyFeeBucket (preserves fee_breakdown) → SummaryCard slice (optional-chained, no Inflection gating). Path already threads fee_breakdown; nothing to add. IWM activation = DS F11 emit into `platinum/firm/leaderboard.json`. CTO + COO accepted.

### F12 — `c9fab075` → `7a0e3980` (Total Fee relabel)
- "Total Fee (TTM)" → "Total Fee (since Jul 2025)" + tooltip. DS-confirmed Orion fee data starts 7/1/2025 (cumulative-since, not TTM). Aligned to CTO F12 spec.

### GRO Growth-card redesign (Andrew/Yang) — `eaaef5ad`→`c7105d63`→`f0fe6841`→`b40e643c`→`c50a58b9`
- Growth card now: total growth DOLLAR `+$20.4M (+11.0%)`; beneath, Market/NNA contribution mix (absolute-value share, 0-100%, robust across mixed-sign periods) — labels purple/gold, values white, `|` divider; subtext "since {current period}".
- Then "(MKT)" abbreviation across all Assets Overview Market labels (legend/tooltip/summary card/footnote → "Market (MKT)"; Total legend + footnote formula → "MKT + NNA"; Growth mix line → bare "MKT" parallel to bare "NNA").

## 3. Judgment calls / lessons
- **Recurring root-cause this session: Inflection data is split across SEPARATE per-artifact S3 files** (book.json vs composition.json vs detail.json#summary.tax vs leaderboard.json#fee_breakdown). Empty panels = check which artifact the adapter reads vs where the data actually lives. Drove the donut fix, F3, and F7.
- No browser-automation tool in this agent env — stated the visual-confirm gap explicitly rather than claiming a visual pass; routed visual-confirm to Andrew (:5173 HMR) / CVO. Did code-scans where possible (e.g., confirmed no client_count "184+69=199" summing presentation exists per CTO's F11 display heads-up — labels are account-grain, clean partition).
- COO standing rule (1615Z): trivial same-lane demo cosmetics can go DIRECT (no formal TO) when label/style-only + DS-verified data claim + folds into the held bundle; route non-trivial/data-changing/cross-lane through COO/CTO.
- F11 finding discipline: verified the passthrough before coding — the CTO's "if it drops it, add a passthrough" condition was false; reported no-change rather than adding a no-op.

## 4. Current state
- **All work on origin/DEV** (HEAD `c50a58b9`, 0 ahead). I had HELD the push per the demo-gate posture; origin/DEV now matches HEAD — pushed by a concurrent agent or Andrew (DEV is a dev branch, not PROD; Rule 19 intact). Flagging COO to confirm the parent-repo submodule pointer is bumped to `c50a58b9`.
- HMR-live on Andrew's localhost:5173 throughout — Andrew live-confirmed + iterated the GRO card in real time.
- Open: Andrew's final visual-confirm on the full bundle; DS F11 emit (post-demo) auto-activates the fee-sliced flows.
- F4 stays suppressed (final demo posture).
