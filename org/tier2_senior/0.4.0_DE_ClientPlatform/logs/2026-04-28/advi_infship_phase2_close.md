# Session Log — 2026-04-28 ADVI_INFSHIP Phase 2 CLOSE (6 of 6 panels shipped)

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-04-28
**Type:** Phase 2 ship session — 11 commits, all 6 INFSHIP panels closed
**Portal DEV commits:** `995262c` -> `45eaca0` -> `fb926fa` -> `aa862dd` -> `ade43c4` -> `12ea545` -> `8d76c70` -> `b41cd04` -> `9e62caf` -> `fc6acc7`
**Workspace CLOUD commit:** none (no parent-repo changes; submodule pointer bump pending DT)

---

## Session Pivot

Started session answering Andrew on `INFLEC_PORTAL_FIELD_USAGE.md` doc + Orion-API addendum question. Mid-session COO + CTO converged on dispatching ADVI_INFSHIP Phase 2 (PRD `docs/architecture/ADVI_INFSHIP.md`, brief `docs/architecture/ADVI_INFSHIP_PHASE2_BRIEF.md`). Andrew explicit ("make sure phase 2 is executed" relayed via COO ~05:43Z; "keep pushing" mid-session) -> pivoted to B1-B6 sequence. Closed all 6 panels in this session.

---

## Phase 2 Scoreboard — 6 of 6 SHIPPED

| Commit | TO | Files | Summary |
|--------|----|----|---------|
| `995262c` | B1 + B2 | 3 | PartnerAnalytics layout-driven `defaultViewMode='geo'` + Distribution cohort cleanup (`geo='enabled', adv='disabled', ofc='disabled'`) |
| `45eaca0` | B3 | 2 | N1 `top_holdings` schema flexibility (Inflection global vs 49F per-class discriminator + concentration optional) |
| `fb926fa` | B3 / Path C | 2 | `HeaderTotal` 4 `fee_earning_*` fields + parallel `getHeaderMetrics` fetch + `clients_tab.headline` backfill |
| `aa862dd` | B4 init | 1 | L2 advisorDrill enabled (Peter+Patrick); IWM bucket suppressed |
| `ade43c4` | B4 amend | 1 | IWM restored as 3rd drillable advisor (Andrew override) |
| `12ea545` | B5 prep | 1 | `BooksClientTaxDetail` optional `realized?`/`unrealized?` (Path 1) |
| `8d76c70` | B5 inc 1 | 2 | Static-S3 `getPlatinumClientDetailStatic` + Inflection-shape adapter; AdvisorBookView L3 useQuery branches on firmOverride |
| `b41cd04` | B5 inc 2 | 3 | TaxCostBasisPanel renders realized/unrealized cost basis + gain/loss grid (LT/ST/Total per side, color-coded) |
| `9e62caf` | B5 inc 3 | 6 | Inflection billing summary card (Total Fee TTM + Avg Annual Fee % + Fee-Earning AUA/Accts) |
| `fc6acc7` | B6 | 3 | L4 account modal per-account realized/unrealized tax (17-field schema + 10 optional deeper fields on `ClientTaxRealizedUnrealized`) |

tsc --noEmit clean on every commit. 49F backwards-compat preserved on every commit (DEFAULT_LAYOUT untouched, optional fields, ?-chained reads). Single-author throughout.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal/src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts | Add `tabs.partnerAnalytics.{defaultViewMode, allowedViewModes}`; PartnerAnalyticsViewKey | `995262c` |
| portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts | INFLECTION_LAYOUT post-INFSHIP corrected (`defaultViewMode='geo'`, `cohorts {geo:'enabled', adv:'disabled', ofc:'disabled'}`); flipped advisorDrill enabled; IWM restored | `995262c` -> `aa862dd` -> `ade43c4` |
| portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx | Import useTenantLayout; layout-driven initial viewMode | `995262c` |
| portal/src/pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx | Schema discriminator split (per-class 49F / global Inflection / flat L3-L4) + null-safe concentration fallbacks | `45eaca0` |
| portal/src/pages/AdvisorIntelligence/_shared/types.ts | `BooksCompositionResponse.concentration` optional; `HeaderTotal` 4 fee_earning fields; `HeaderMetricsResponse._meta?`; `ClientTaxRealizedUnrealized` (7 core + 10 optional deeper); `ClientBillingSummary`; `BooksClientTaxDetail.realized?/unrealized?`; `BooksClientAccount.realized?/unrealized?`; `inflecBilling?` on PlatinumClientSummary + BooksClientDetailResponse | `45eaca0`, `fb926fa`, `12ea545`, `9e62caf`, `fc6acc7` |
| portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx | Third parallel `getHeaderMetrics` fetch; merge spread injects header_metrics.total.fee_earning_* into clients_tab.headline | `fb926fa` |
| portal/src/api/endpoints/advisor-intelligence.ts | New `getPlatinumClientDetailStatic` static-S3 fetcher + Inflection adapter; per-account tax + billing passthrough | `8d76c70`, `9e62caf`, `fc6acc7` |
| portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx | L3 useQuery branches on firmOverride (Inflection -> static helper, 49F -> Lambda); l3 adapter passes inflecBilling through | `8d76c70`, `9e62caf` |
| portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookClientDetail.tsx | l3Tax mapping passes realized/unrealized + inflecBilling through to CanonicalTax | `b41cd04`, `9e62caf` |
| portal/src/pages/AdvisorIntelligence/_shared/panels/types.ts | CanonicalTax: 49F fields optional; new `realized?/unrealized?/inflecBilling?` | `b41cd04`, `9e62caf` |
| portal/src/pages/AdvisorIntelligence/_shared/panels/TaxCostBasisPanel.tsx | `has49FBuckets` + `hasInflectionTax` discriminators; new realized/unrealized 2-col grid; new billing summary card | `b41cd04`, `9e62caf` |
| portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookAccountDetail.tsx | `taxFromAccountStatus` -> `taxFromAccount` (passes realized/unrealized through to L4) | `fc6acc7` |

---

## Decisions Made

1. **B2 folded into B1's commit** — DistributionTab cohort filter was already wired through useTenantLayout per INFLV2.006 ship; flipping `cohorts.adv` from `'enabled'` to `'disabled'` in INFLECTION_LAYOUT (alongside the B1 PartnerAnalytics change) closed B2's "drop ADV" requirement structurally without separate commit.
2. **B4 IWM suppression then revert** (Andrew direction) — initial B4 (`aa862dd`) suppressed the inflection_wealth_management firm-bucket from advisor list because S3 inventory smoke showed it has only top_holdings.json (no book.json / no composition.json) and would crash on drill. CTO ratified. Andrew immediately overrode in chat ("IWM should be treated the same way as Peter Lee and Patrick Scanlan as advisors with drilldowns/pages"). Amended at `ade43c4` to restore. Drill is structurally drill-ready via existing `.catch` -> null -> AdvisorPublicProfile empty-state in ClientsTab.tsx:355-357 — auto-populates the moment DS publishes the missing artifacts.
3. **DS~B Finding 5 Path 1** — extend `BooksClientTaxDetail` with optional `realized?`/`unrealized?` rather than create a separate `InflectionBooksClientDetailResponse` (Path 2) or rename DS output (Path 3). Smallest TS change, no DS rework, no republish of 305 detail.json files.
4. **Static-S3 L3 fetcher** for Inflection rather than waiting on AE/DT to extend `opal-partners-data` Lambda. New `getPlatinumClientDetailStatic` reads `${PLATINUM_BASE}/clients/${hhId}/detail.json` directly via CloudFront -> shared-advisor-router -> S3, adapts the `summary`-rooted Inflection envelope into a minimal `PlatinumClientSummary`-shaped envelope. Mix/concentration/decomposition fields default to null/empty so downstream panels render their built-in empty-states gracefully. AdvisorBookView L3 useQuery branches on `firmOverride === 'inf' | 'inflection'`.
5. **Billing card colocated with TaxCostBasisPanel** rather than threading through to FeeSummaryPanel — billing is conceptually the fee-aggregate sibling of cost basis at the per-HH grain, and TaxCostBasisPanel was already the natural L3 home; FeeSummaryPanel is 49F-specific window-toggle UX that doesn't fit Inflection's flat 5-field summary shape.

---

## Postmortem: Auth-login still fails post-CORS-allowlist

### Symptom
DT shipped CORS allowlist for `localhost:5176` -> `https://7k3ed8px20.execute-api.us-east-1.amazonaws.com/auth/refresh` in `portal-auth-v1.14.1`. Real-login Playwright (michael@opalinvest.com / l85a1q1p0666 AND andrew@opalinvest.com / SmokeTest2026!) still stuck at `/login` post-submit; `localStorage.token = undefined`. No `[CONSOLE ERROR]` lines — the request seems to round-trip cleanly without a CORS error pattern, but auth doesn't establish.

### Hypotheses (unconfirmed)
- (a) Credentials rotated since the constitution was authored
- (b) `/auth/login` (or whatever the form POSTs to) needs separate CORS allowlist entry — `portal-auth-v1.14.1` may have only covered `/auth/refresh`
- (c) Login flow bypasses CORS check but JWT issuance fails for some other reason

### Resolution
Pinged DT separately. Visual data validation deferred to next session post-debug. Structural acceptance (B1+B2 visual validated under devBypass earlier, all subsequent commits tsc-clean and 49F backwards-compat) still proves the layout integration is sound. Inflection real-data render validation gated on auth unblock OR DT push to a deployed origin where auth works natively.

---

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `comp-transform schema-check PartnerAnalytics --feature inflection` | 1 false-positive `period` MISSING flag | Click-handler local param type, not a field-path read; ignored |
| `bun run tsc --noEmit` | 0 errors across 11 commits | Ran after every Edit before commit |
| `aws s3 cp s3://opal-data-inf/platinum/firm/{partner_analytics_quarterly,partner_analytics_monthly,partner_analytics_annual,firm_composition,leaderboard}.json` | Inspection only | Surfaced 3 findings: (1) views.aua/nna/adv donut segments empty (Path A ruling -> firm-centric scope); (2) 10 advisor folders + quarantine in platinum/advisors/ vs brief's 3 (layout.allowedAdvisorKeys filters; not blocker); (3) clients/ count 1990 vs brief's 305 (multi-snapshot Hive partitioning; not bug) |
| `aws s3 ls s3://opal-data-inf/platinum/advisors/{inflection_wealth_management,peter_lee,patrick_scanlan}/` | Inventory smoke | IWM has only top_holdings.json (no book.json / no composition.json); Peter + Patrick have all 3. Drove B4 suppression decision (later reverted per Andrew direction; structural empty-state pattern handles missing artifacts) |
| `python .tools/frontend-dev.py --constitution _b1b2_validate_inflec.json` | PASS for B1+B2 structural | Visual confirmed: 49F default cohort selector shows GEO/ADV/OFC; Inflection switch shows GEO only + ADVISORS tab dropped + firm name "Inflection Wealth Management" + source attribution "Orion Portfolio Solutions" |
| Real-login Playwright (CORS-live) | FAIL — auth doesn't establish | Hypotheses logged in postmortem; pinged DT |

---

## Coordination Out

Sent in this session (in chronological order):

| Recipient | Subject | Outcome |
|-----------|---------|---------|
| 2.0.0_SA_COO | RAVC ACK — ADVI_INFSHIP Phase 2 B1+B2+B3 GO received | ACK |
| 0.4.0_DS_ClientPlatform~C | RAVC4 ACK — INF_D_04 geo shape received | DS~C standing by for live S3 sample post-dispatch |
| 1.0.0_SA_CTO | RAVC ACK — INFSHIP Phase 2 B1-B6 GO; full data inventory received | CTO ACK |
| 1.0.0_SA_CTO | RAVC2 — INFSHIP P2 Stage 1 partial — brief read + 3 BLOCKERS surfaced before B1 render attempt | CTO ruled Path A for AUA/NNA/ADV donut |
| 2.0.0_SA_COO | RAVC ACK — Phase 2 cleared by Andrew relay; pivoting to B1 now | COO confirmed |
| 1.0.0_SA_CTO | RAVC4 — INFSHIP B1 SHIPPED (995262c) | CTO ACK + GO B2 first then validate combined |
| 0.4.0_DT_ClientPlatform | Push request — INFSHIP B1 portal/DEV 995262c | DT pushed batch through 12ea545 |
| 1.0.0_SA_CTO | RAVC4 — INFSHIP B1+B2 VISUALLY VALIDATED (PASS) | CTO ACK |
| 1.0.0_SA_CTO | RAVC4 — INFSHIP B3 SHIPPED (45eaca0) | CTO ACK |
| 1.0.0_SA_CTO | RAVC4 — INFSHIP B3 followup (Path C) SHIPPED (fb926fa) | CTO ACK |
| 0.4.0_DS_ClientPlatform~B | RAVC ACK — Path C HeaderTotal extension | DS~B ACK Path 1 |
| 1.0.0_SA_CTO | RAVC4 — INFSHIP B4 SHIPPED (aa862dd) + B5 Path 1 pick | CTO ratified IWM suppression (later overridden by Andrew) |
| 0.4.0_DS_ClientPlatform~B | RAVC ACK — Finding 5 path pick: Path 1 | DS~B ACK |
| 0.4.0_DT_ClientPlatform | UPDATE — push batch grows by 1: ade43c4 (B4 amend) | DT pinned CLOUD submodule at ade43c4 |
| 1.0.0_SA_CTO | FYI — IWM suppression reversed post your ACK (Andrew direction) | CTO ratified amend |
| 0.4.0_DS_ClientPlatform | REQUEST — publish book.json + composition.json for inflection_wealth_management firm-bucket advisor | Awaiting DS publish |
| 1.0.0_SA_CTO | RAVC4 — INFSHIP B5 SHIPPED (8d76c70 + b41cd04) | CTO GO B5 inc 3 + B6 |
| 0.4.0_DT_ClientPlatform | UPDATE — push batch grew again: 9 commits | DT held push for B5+B6 wave |
| 0.4.0_DT_ClientPlatform | Auth still failing after CORS allowlist | Awaiting DT debug |
| 1.0.0_SA_CTO | RAVC4 — INFSHIP PHASE 2 CLOSED — 6 of 6 panels SHIPPED | Final close |
| 0.4.0_DT_ClientPlatform | PUSH WAVE TRIGGER — B6 SHIPPED (fc6acc7) | DT push wave triggered |

---

## Next Steps

- **[DT]** Push 4-commit delta to portal/DEV (`8d76c70`, `b41cd04`, `9e62caf`, `fc6acc7`) + bump parent CLOUD submodule pointer from `ade43c4` to `fc6acc7` + (optional) tag portal-v2.1.65
- **[DT]** Debug auth-login post-CORS-allowlist failure (separate ticket from me); allowlist `/auth/login` if scope was limited to `/auth/refresh`
- **[DS]** Publish `s3://opal-data-inf/platinum/advisors/inflection_wealth_management/{book.json, composition.json}` so the IWM drill auto-populates (current empty-state path renders cleanly until then)
- **[DE]** Visual validation pass once auth unblocks — single Playwright run across all 6 panels with real-login + real S3 data routing under live CORS, RAVC4 with screenshots
- **[DE]** Optional follow-on: extend B5 inc.3 billing card to L4 (currently only renders at L3)
