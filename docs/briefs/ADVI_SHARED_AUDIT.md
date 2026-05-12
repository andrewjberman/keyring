# ADVI_SHARED Phase 0 — Multi-Tenant Audit Matrix

| Field | Value |
|---|---|
| Project | `ADVI_SHARED` |
| TO | `ADVI_SHARED.000` (`org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/`) |
| Author | `0.4.0_DE_ClientPlatform` |
| Date | 2026-05-12 |
| PRD | `docs/architecture/ADVI_SHARED.md` v0.1 (CTO 1.0.0_SA_CTO, commit `54c1ea270`) |
| Brief feeder | `org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/briefs/ADVI_SHARED_brief_to_cto.md` (commit `cd0847d1d`) |
| Cache state | `comp-build` PASS — 1590/1663 file-backed nodes indexed |
| Cache collisions | `comp-cache collisions` — 4 matched PRD §5.2 exactly |
| Schema-check leaf components | FAIL — `comp-transform schema-check InflectionAdvisorIntelligence` and `FortyNineFinancialAdvisorIntelligence` both returned "Component not found." Per TO `if_mismatch`: documented in §H, manual Grep used. |

This audit is **read-only on `portal/src/**`**. It enumerates every site Phase 1 will touch, classified by treatment category. Phase 1 TOs (SHARED.001 — type extension; SHARED.002 — PartnerAnalytics; SHARED.003 — BookView + ClientsTab; SHARED.004 — co-location; SHARED.005 — component extraction; SHARED.006 — firmId canonicalization; SHARED.007 — residual mop-up; SHARED.008 — DEV smoke gate) reference this document as their authoritative inventory.

---

## §A. firmId-conditional branch inventory

Empirical grep on `firmId === '...' | firmOverride === '...' | isInflectionFirm | isInflec\b` across `portal/src/pages/AdvisorIntelligence/**`. Internal-tier gates (`firmId === 'opal-capital'`) are documented in §A.5 as out-of-ADVI_SHARED-scope.

Treatment categories:
- **REPLACE-WITH-CONFIG** — branch is per-firm divergence; should route through `useTenantLayout(firmId).<field>`.
- **KEEP-AT-DISPATCHER** — branch is a partner-routing decision belonging to `_partners/*/index.tsx` or `useTenantLayout` itself; stays inline by design.
- **DELETE-POST-CANONICALIZATION** — branch is a defensive `'inf' || 'inflection'` disambiguation that disappears once SHARED.006 collapses L3 to canonical L1.
- **OTHER** — justify per entry.

### §A.1 `_shared/components/PartnerAnalytics.tsx` (15 sites — worst offender)

| Line | Current behavior | Proposed `TenantLayoutConfig` field | Treatment | Target TO |
|---|---|---|---|---|
| 124 | `const isInflectionFirm = firmOverride === 'inf' \|\| firmOverride === 'inflection'` — declares local alias used by all 14 sites below | — (alias declaration; deleted when downstream sites migrate) | DELETE-POST-CANONICALIZATION (becomes single `firmId === 'inflection'` literal after SHARED.006, then disappears entirely after sites L129-L1856 migrate) | SHARED.002 + SHARED.006 |
| 129 | `if (!isInflectionFirm \|\| !data) return null` — gates an Inflection-only timeseries-chart memo | `layout.features.auaDonut.source === 'partner_analytics_views'` (positive: when source is partner-analytics views, build the inflection-style memo) | REPLACE-WITH-CONFIG | SHARED.002 |
| 134 | `useMemo` dep on `isInflectionFirm` | derived from `layout.features.auaDonut.source` — closure dep updates | REPLACE-WITH-CONFIG | SHARED.002 |
| 173 | `enabled: isInflectionFirm` — gates a `useQuery` for `inflecTimeseriesChart` | `enabled: layout.features.auaDonut.source === 'partner_analytics_views'` | REPLACE-WITH-CONFIG | SHARED.002 |
| 275 | `if (isInflectionFirm && inflecTimeseriesChart && ...)` — Inflection-specific data-merge branch | `if (layout.features.auaDonut.source === 'partner_analytics_views' && inflecTimeseriesChart && ...)` | REPLACE-WITH-CONFIG | SHARED.002 |
| 335 | `if (!isInflectionFirm \|\| raw.length === 0) return raw` — Inflection-specific data shape pass-through | `if (layout.features.auaDonut.source !== 'partner_analytics_views' \|\| raw.length === 0) return raw` | REPLACE-WITH-CONFIG | SHARED.002 |
| 342 | `useMemo` dep on `isInflectionFirm` | derived from `layout.features.auaDonut.source` | REPLACE-WITH-CONFIG | SHARED.002 |
| 383 | `const pts = isInflectionFirm ? ... : ...` — timeseries pts source branch | derived from `layout.features.auaDonut.source` | REPLACE-WITH-CONFIG | SHARED.002 |
| 401 | `useMemo` dep on `isInflectionFirm` | derived from `layout.features.auaDonut.source` | REPLACE-WITH-CONFIG | SHARED.002 |
| 599 | `const barCategories = (isInflectionFirm && inflecTimeseriesChart?.categories?.length && auaGranularity !== 'monthly') ? ...` — chooses Inflection categorical vs 49F derived | `layout.features.barChart.stacked` controls; categories are derived per-firm from data shape (already partial config — extend to fully cover) | REPLACE-WITH-CONFIG | SHARED.002 |
| 943 | `{timeseriesLoading \|\| (isInflectionFirm && inflecTimeseriesChartLoading) ? ...` — combines two loading states for Inflection | `(isInflectionFirm && inflecTimeseriesChartLoading)` → `(layout.features.auaDonut.source === 'partner_analytics_views' && inflecTimeseriesChartLoading)`; useQuery `enabled` already gates the fetch, so the loading flag is consistent | REPLACE-WITH-CONFIG | SHARED.002 |
| 1494 | `.filter(cls => cls !== 'cash' \|\| isInflectionFirm)` — asset-class cash inclusion in donut | `layout.assetClasses.includesCash` — INF=true, 49F=false | REPLACE-WITH-CONFIG | SHARED.002 |
| 1641 | `.filter(cls => cls !== 'cash' \|\| isInflectionFirm)` — asset-class cash inclusion (2nd site) | `layout.assetClasses.includesCash` | REPLACE-WITH-CONFIG | SHARED.002 |
| 1856 | `(['cash', 'fixed_income', 'equity', 'alternatives'] as const).filter(cls => cls !== 'cash' \|\| isInflectionFirm).map((cls) => ...)` — 3rd cash-inclusion site; ALSO hardcodes the asset-class ordering as a literal `['cash', 'fixed_income', 'equity', 'alternatives']` | `layout.assetClasses.ordered` + `layout.assetClasses.includesCash` — both fields needed; ordering is the new field | REPLACE-WITH-CONFIG | SHARED.002 |

**§A.1 notes:** The 3 `cls !== 'cash' || isInflectionFirm` sites (L1494/L1641/L1856) plus the hardcoded `['cash', 'fixed_income', 'equity', 'alternatives']` literal at L1856 are the canonical asset-class-taxonomy case the PRD calls out (§2.3 row 1). SHARED.001 must add `layout.assetClasses` BEFORE SHARED.002 can complete. **Andrew Q2 (asset class taxonomy authority) directly affects this section.**

### §A.2 `_shared/AdvisorBookView.tsx` (6 sites)

| Line | Current behavior | Proposed `TenantLayoutConfig` field | Treatment | Target TO |
|---|---|---|---|---|
| 105 | `if (firmOverride === 'inf' \|\| firmOverride === 'inflection') warnOnInflectionAdvisorDrift(r)` — Inflection-only schema-drift sentinel hook | `if (firmId === 'inflection') warnOnInflectionAdvisorDrift(r)` post-canonicalization; sentinel hook itself is firm-specific defensive infra and stays | DELETE-POST-CANONICALIZATION (the `'inf' \|\|` disjunction goes; the conditional stays) | SHARED.006 |
| 121 | `const isInflectionFirm = firmOverride === 'inf' \|\| firmOverride === 'inflection'` — alias declaration | — (alias deleted when downstream sites migrate) | DELETE-POST-CANONICALIZATION | SHARED.003 + SHARED.006 |
| 123 | `queryKey: ['advisor-book-client', advisorId, selectedClientKey, firmOverride, isInflectionFirm ? 'static' : 'lambda']` — query-key suffix branches on data path | `queryKey: [..., layout.dataSources.staticPaths.clientDetailHandler ?? 'lambda']` | REPLACE-WITH-CONFIG | SHARED.003 |
| 124 | `queryFn: () => isInflectionFirm ? getPlatinumClientDetailStatic(...) : getPlatinumClientSummary(...)` — fetch fn selection | `queryFn: () => layout.dataSources.staticPaths.clientDetailHandler === 'static' ? getPlatinumClientDetailStatic(...) : getPlatinumClientSummary(...)` | REPLACE-WITH-CONFIG | SHARED.003 |
| 151 | `enabled: isInflectionFirm && !!selectedAccountId && !!selectedClientKey` — enables Inflection-only L4 account timeseries query | `enabled: layout.dataSources.staticPaths.accountTimeseriesHandler === 'static' && !!selectedAccountId && !!selectedClientKey` | REPLACE-WITH-CONFIG | SHARED.003 |
| 403 | `timeseriesData={isInflectionFirm ? inflecAccountTimeseries : (accountRfsById[...]?.timeseries?.map(...) ?? accountSummary?.timeseries?.map(...))}` — JSX prop selects static vs lambda timeseries shape | `timeseriesData={layout.dataSources.staticPaths.accountTimeseriesHandler === 'static' ? inflecAccountTimeseries : ...}` | REPLACE-WITH-CONFIG | SHARED.003 |

**§A.2 notes:** All 5 functional sites (L105 is borderline — defensive sentinel hook for an empirically observed schema-drift; not pure render branch) collapse onto `layout.dataSources.staticPaths.{clientDetailHandler, accountTimeseriesHandler}`. SHARED.001 must add these PRD §3.2 fields. Acceptable migration sequence: SHARED.001 (type) → SHARED.003 (consume via BookView+ClientsTab in parallel since they share the pattern).

### §A.3 `_shared/tabs/ClientsTab.tsx` (6 sites)

| Line | Current behavior | Proposed `TenantLayoutConfig` field | Treatment | Target TO |
|---|---|---|---|---|
| 331 | `const isInflec = firmOverride === 'inf' \|\| firmOverride === 'inflection'` — local-scope alias inside `firmComposition` useMemo (introduced by ADVI BooksTab N1→useQuery migration `6f81d13a`, 2026-05-12) | — (alias deleted; downstream L332 migrates to config) | DELETE-POST-CANONICALIZATION | SHARED.003 + SHARED.006 |
| 332 | `return normalizeMixTo4Class(mix.composition, { includeCash: isInflec })` — composition normalization opts | `return normalizeMixTo4Class(mix.composition, { includeCash: layout.assetClasses.includesCash })` | REPLACE-WITH-CONFIG | SHARED.003 |
| 411 | `const isInflectionFirm = firmOverride === 'inf' \|\| firmOverride === 'inflection'` — alias declaration (separate scope from L331) | — (alias deleted when downstream sites migrate) | DELETE-POST-CANONICALIZATION | SHARED.003 + SHARED.006 |
| 413 | `queryKey: ['advisor-book-client', selectedAdvisorId, selectedClientKey, firmOverride, isInflectionFirm ? 'static' : 'lambda']` — same pattern as BookView L123 | `queryKey: [..., layout.dataSources.staticPaths.clientDetailHandler ?? 'lambda']` | REPLACE-WITH-CONFIG | SHARED.003 |
| 414 | `queryFn: () => isInflectionFirm ? getPlatinumClientDetailStatic(...) : getPlatinumClientSummary(...)` — same pattern as BookView L124 | `queryFn: () => layout.dataSources.staticPaths.clientDetailHandler === 'static' ? ... : ...` | REPLACE-WITH-CONFIG | SHARED.003 |
| 480 | `enabled: isInflectionFirm && !!selectedAccountId && !!selectedClientKey` — same as BookView L151 | `enabled: layout.dataSources.staticPaths.accountTimeseriesHandler === 'static' && ...` | REPLACE-WITH-CONFIG | SHARED.003 |
| 617 | `timeseriesData={isInflectionFirm ? inflecAccountTimeseries : accountSummary?.timeseries?.map(...)}` — same JSX pattern as BookView L403 | `timeseriesData={layout.dataSources.staticPaths.accountTimeseriesHandler === 'static' ? ... : ...}` | REPLACE-WITH-CONFIG | SHARED.003 |

**§A.3 notes:** ClientsTab N1 was migrated useEffect→useQuery in `6f81d13a` (2026-05-12). The L331-332 alias inside the new `firmComposition` useMemo is a regression risk to flag — the BooksTab migration carried the inline pattern forward as a local-scope alias rather than introducing the `layout` reference. SHARED.003 closes this loop cleanly; until then, the local alias is acceptable (no behavior delta from pre-migration).

### §A.4 `_shared/AdvisorPublicProfile.tsx` (1 site)

| Line | Current behavior | Proposed `TenantLayoutConfig` field | Treatment | Target TO |
|---|---|---|---|---|
| 57 | `function firmIdFromOverride(firmOverride): if (firmOverride === 'inf' \|\| firmOverride === 'inflection') return 'inflection'` — L3→L1 namespace normalization helper | — (function DELETED once L3 namespace canonicalizes to L1; callers pass `firmId` directly to `useTenantLayout`) | DELETE-POST-CANONICALIZATION | SHARED.006 |

**§A.4 notes:** `firmIdFromOverride()` is the explicit symptom of PRD §2.2's "defensive disambiguation everywhere" — the helper exists because `useTenantLayout(firmId)` expects L1 but call sites have L3. Post-SHARED.006 the helper disappears entirely.

### §A.5 `_shared/types/TenantLayoutConfig.ts` — informational

| Line | Reference | Treatment |
|---|---|---|
| 5 | Doc comment: `Replaces scattered firmId === 'inflection' checks. New partners add one entry to the partner config map; component code reads layout flags via the hook.` | KEEP — describes design intent. Update comment to cite ADVI_SHARED PRD §3.1 + §3.2 instead of the older ADVI_INFLV2.md reference at L9 after SHARED.001 lands. |
| 9 | Doc comment: `See ADVI_INFLV2.md §5 (architectural pattern) for rationale.` | KEEP-AND-UPDATE — point to ADVI_SHARED PRD §3.2 after SHARED.001. |

### §A.6 Dispatcher allowlist — `pages/AdvisorIntelligence/index.tsx`

| Line | Current behavior | Proposed change | Treatment | Target TO |
|---|---|---|---|---|
| 13-16 | `ALL_PARTNER_FIRMS = [{ id: 'bd', name: '49 Financial' }, { id: 'inflection', ... }]` — partner enumeration array (L2 namespace) | `[{ id: '49financial', name: '49 Financial' }, { id: 'inflection', ... }]` — converge L2 to L1 canonical | KEEP-AT-DISPATCHER (the array IS the dispatcher's source of truth; rename keys only) | SHARED.006 |
| 18-21 | `PARTNER_VIEWS: Record<string, ComponentType<PartnerViewProps>> = { bd: FortyNineFinancialView, inflection: InflectionAdvisorIntelligence }` — map keyed by L2 namespace | `{ '49financial': FortyNineFinancialView, inflection: ... }` — converge to L1 | KEEP-AT-DISPATCHER (this IS the partner dispatcher) | SHARED.006 |
| 29 | `const [selectedFirmId, setSelectedFirmId] = useState<string>('bd')` — default firm fallback literal | `useState<string>('49financial')` | KEEP-AT-DISPATCHER | SHARED.006 |
| 31 | `const firmId = internal ? selectedFirmId : (claims?.firmId ?? 'bd')` — fallback firm literal | `... ?? '49financial')` | KEEP-AT-DISPATCHER | SHARED.006 |
| 32 | `const PartnerView = PARTNER_VIEWS[firmId] ?? DEFAULT_PARTNER_VIEW` — dispatcher lookup itself | unchanged (lookup is correct) | KEEP-AT-DISPATCHER | — |

**§A.6 notes:** The dispatcher is the one place where firmId conditionalization is correct by design (it's the routing primitive). The four `'bd'` literals are L2-namespace artifacts the PRD §3.1 rename targets. **SHARED.006 must update L13/L18/L29/L31 atomically** (changing only one causes a fall-through to `DEFAULT_PARTNER_VIEW`).

### §A.7 Internal-tier gates (out of ADVI_SHARED scope — informational)

Inline `firmId === 'opal-capital'` literals exist for **internal-user (Opal staff) tier gating**, NOT per-firm divergence. Listed here for completeness so SHARED.006's rename pass doesn't touch them by accident.

| File | Lines | Purpose | Treatment |
|---|---|---|---|
| `contexts/AuthContext.tsx` | 34, 550, 573, 584, 604, 610, 615, 620 | `internal = claims?.firmId === 'opal-capital'` and `isInternal()` / `canSeePII()` / `canSeeCrossFirm()` helpers | KEEP-AS-IS — auth-tier gate, not multi-tenant divergence |
| `lib/firmAccess.ts` | 4 | Doc comment: "Internal users (firmId === 'opal-capital')" | KEEP-AS-IS (comment) |
| `lib/permissionGroups.ts` | 51 | Doc comment: "plus firmId === 'opal-capital' (Opal internal users are implicitly admin)" | KEEP-AS-IS (comment) |
| `pages/TradeSubmission/TradeSubmission.tsx` | 28 | `const isInternal = claims?.firmId === 'opal-capital'` — internal-tier gate | KEEP-AS-IS — out of ADVI_SHARED scope (TradeSubmission is a separate page) |

**§A.7 notes:** `'opal-capital'` is the JWT-claim sentinel for internal users. It's a fixed L1 identity, not a multi-tenant config dimension. PRD §3.1 doesn't propose renaming it. The custom-ESLint allowlist (§3.6) should include `firmId === 'opal-capital'` as an exempted comparison.

### §A.8 Aggregate count

| Source | Count |
|---|---|
| §A.1 PartnerAnalytics | 15 sites |
| §A.2 AdvisorBookView | 6 sites |
| §A.3 ClientsTab | 6 sites (1 of which introduced by the 2026-05-12 BooksTab migration) |
| §A.4 AdvisorPublicProfile | 1 site (helper function) |
| §A.5 TenantLayoutConfig | 0 functional + 2 doc-comment refs |
| §A.6 Dispatcher | 4 literal sites (L13/L18/L29/L31) |
| §A.7 Internal-tier (out of scope) | 8 functional + 3 doc-comment refs in 4 files |
| **ADVI_SHARED scope total** | **28 functional sites + 4 dispatcher literals = 32** |

PRD §2.1 predicted "3 files × ~22 inline branches"; empirical count is 27 inline branches across the 3 files (PartnerAnalytics 15 + AdvisorBookView 6 + ClientsTab 6), plus 1 in AdvisorPublicProfile (`firmIdFromOverride`) that PRD §2.1 didn't enumerate. Plus 4 dispatcher literals. **Net: 32 sites in ADVI_SHARED scope** (PRD slightly undercounted by including ClientsTab+BookView at 5 each rather than 6).

ProtectedRoute references mentioned in PRD §5.2: **not yet audited in §A — see §G.4** (firmId namespace literal census will cover all routing-tier literals).

---

## §B. Per-firm component override inventory

Empirical file listing of `_partners/{firm}/**` (10 files total across 2 firms):

| Partner component | `_shared/*` counterpart | Classification | Config-extractable? | Treatment | Target TO |
|---|---|---|---|---|---|
| `_partners/49financial/index.tsx` (1-360 lines, est. — only first 100 read this pass) | Conceptually parallel to `_partners/inflection/index.tsx` — both are page dispatchers wiring `_shared/*` tabs + panels for their firm | REPLACEMENT of nothing; AUGMENTATION of `_shared/*` (imports DistributionTab/AdvisorsTab/BooksTab/PartnerAnalytics/AdvisorPublicProfile and wires them with `BD_SOURCE_ATTRIBUTION` + `BD_TOOLTIP_ATTRIBUTION` + `FORTY_NINE_FINANCIAL_ROLES`) | PARTIALLY — the wiring is structurally identical to inflection/index.tsx; differences are constants (source attribution, role meta) + tab list (admin gates Books, non-admin gets Profile) + dropdown wiring. All differences map to `TenantLayoutConfig` per PRD §3.2. | KEEP-AS-DISPATCHER (per PRD §3.5 scaffolding emits this template). After SHARED.001 type extension + SHARED.002/.003 panel migrations, the file shrinks to ~50 LOC (mostly tab dispatch + layout wiring; all firm-specific values come from `useTenantLayout(firmId)`). | SHARED.005 (component extraction may pull the duplicated dispatcher into a shared `<TenantAdvisorIntelligence />` wrapper); SHARED.007 (residual mop-up) |
| `_partners/inflection/index.tsx` (289 lines, read in full) | Same as above — parallel of 49F dispatcher | Same classification | Same — values map to PRD §3.2 fields | Same: KEEP-AS-DISPATCHER; shrinks post-SHARED.001+.002+.003. **Note**: inflection/index.tsx is already further along the convergence path — uses `layout.tabs.advisors.enabled`, `layout.tabs.books.enabled`, `layout.panels.advisorPublicProfile.enabled` (lines 132-145) for tab visibility filtering. 49F-index.tsx hasn't adopted this yet (still hardcodes the tab list per PRD §2.1 "half-migrated" finding). | SHARED.002 / SHARED.005 (49F migration to layout-driven tabs to match Inflection's pattern) |
| `_partners/49financial/constants.ts` | None (constants file) | Per-firm constants module | YES — every constant either maps to `TenantLayoutConfig` field (FIRM_ID → `layout.firmId`; FIRM_DISPLAY_NAME → `layout.displayName`; PRIMARY_CUSTODIAN → `layout.primaryCustodian`; BD_SOURCE_ATTRIBUTION → `layout.sourceAttribution`; BD_TOOLTIP_ATTRIBUTION → `layout.tooltipAttribution`; SMALL_ACCOUNT_THRESHOLD_USD → `layout.features.smallAccountThreshold.usd`) OR is per-firm sentinel (FIRM_EMAIL_DOMAINS stays at firmAccess.ts layer) | Full migration to layout per PRD §3.2 Identity + Numeric defaults blocks; file becomes a thin re-export of `INFLECTION_LAYOUT.firmId` + similar for backward-compat OR deletes entirely | SHARED.001 (type) + SHARED.006 (canonicalization) — exact migration order TBD by COO sizing |
| `_partners/49financial/roles.ts` | `_shared/types` AdvisorRole | Role taxonomy override (5 roles: architect / implementor / consultant / local_ops / additional_advisor) | YES — fully extractable to `layout.roles.keys` + `layout.roles.meta` per PRD §3.2 Role taxonomy block | DELETE — content moves to `inflection/layout.ts` style (`FORTY_NINE_FINANCIAL_LAYOUT.roles = { keys: [...], meta: {...}, composition: { enabled: true } }`) | SHARED.001 + SHARED.006 |
| `_partners/inflection/constants.ts` | None | Same as 49F constants — FIRM_ID/FIRM_DISPLAY_NAME/PRIMARY_CUSTODIAN/INFLECTION_SOURCE_ATTRIBUTION/INFLECTION_TOOLTIP_ATTRIBUTION | YES — same field map as §B 49F constants row | Same migration as 49F constants | SHARED.001 + SHARED.006 |
| `_partners/inflection/roles.ts` | `_shared/types` AdvisorRole | Role taxonomy override (2 roles: rep / firm) | YES — same as 49F roles | Same migration as 49F roles | SHARED.001 + SHARED.006 |
| `_partners/inflection/layout.ts` | `_shared/hooks/useTenantLayout.ts` consumes this | Layout config (partial — current `TenantLayoutConfig`) | N/A — this IS the layout config that the migration pattern formalizes | EXPAND in place (additive — current fields preserved; new fields per PRD §3.2 added) | SHARED.001 (extend type) + SHARED.002/.003/.007 (populate values as fields migrate) |
| `_partners/inflection/InflectionInsightsPanel.tsx` (read first 60 lines; est. 500-1000 total) | Conceptually parallel to `_shared/tabs/FeeEfficiencyPanel.tsx` — both are N1 revenue-ops scatter panels | REPLACEMENT (Inflection-only; not used by 49F. 49F renders FeeEfficiencyPanel via `CanonicalBookView`'s `revenueOpsSlot`-default; Inflection passes this component as `revenueOpsSlot` prop instead per `inflection/index.tsx:250` + `INFLECTION_LAYOUT.tabs.books.revenueOpsPanel='inflection_insights'`) | NO — genuinely component-distinct. Inflection has Activity Scan + Cash Drag + Firm Concentrations data sources that don't exist for 49F. The render shape is also different (treemap + bar chart hybrid vs 49F's scatter). | KEEP-AS-PARTNER-OVERRIDE. Substitution mechanism already exists via `revenueOpsPanel: 'inflection_insights' \| 'standard' \| 'suppressed'` (PRD §3.2 books panel registry). No migration needed beyond the existing pattern. **Lint sub-concern**: file is in PRD §2.4 worst-offenders list (Category A — exports both component + helpers). Resolution via SHARED.004 (co-location refactor). | SHARED.004 (Cat A lint resolution); SHARED.005 (Cat B if any inner components exist — TBD) |
| `_partners/inflection/overrides/FidelityCustodianBar.tsx` (45 lines, read in full) | None (new Inflection-only Data Source panel decoration; renders below the "Orion Connected" line in the Data Source panel at `inflection/index.tsx:279`) | REPLACEMENT (Inflection-only decoration; 49F has no parallel — 49F's Data Source panel shows only the BD_SOURCE_ATTRIBUTION line) | YES (in a partial sense) — the COMPONENT is firm-specific (Fidelity 99.4% / Other 0.6% hardcoded), but the PATTERN ("render an overlay component in the Data Source panel") is extractable to `layout.panels.dataSourcePanel.overlay?: ComponentType<{}> \| null`. PRD §3.2 panel registry currently covers `revenueOpsPanel` + 3 proposed (taxCostBasisPanel / feeEfficiencyPanel / concentrationPanel) but does NOT propose `dataSourcePanel.overlay` — **§3.2 supplement candidate**. | Hybrid: COMPONENT stays as `_partners/inflection/overrides/`; REGISTRATION moves to `layout.panels.dataSourcePanel.overlay = FidelityCustodianBar`. 49F's layout has `overlay: null` (no override) → DataSourcePanel renders the standard layout. | SHARED.001 (type extension + PRD §3.2 supplement) + SHARED.007 (residual mop-up registers the overlay) |
| `_partners/inflection/overrides/index.ts` (re-export only, est. 1-5 lines) | None | Re-export barrel | N/A | KEEP-AS-IS (folder structure stays; barrel re-exports any future overrides) | — |

### §B.1 Cross-firm pattern observation

The `_partners/49financial/` directory has **3 files** (index.tsx + constants.ts + roles.ts) — no `layout.ts` (49F falls through to `DEFAULT_LAYOUT`). The `_partners/inflection/` directory has **7 files** (the 3 49F has + layout.ts + InflectionInsightsPanel.tsx + overrides/FidelityCustodianBar.tsx + overrides/index.ts).

**Inflection is ahead of 49F on the migration path** — Inflection has a `layout.ts` extracted; 49F doesn't. SHARED.001 should add `_partners/49financial/layout.ts` even if it's just `export const FORTY_NINE_FINANCIAL_LAYOUT: TenantLayoutConfig = DEFAULT_LAYOUT` initially, so the scaffolding tool (PRD §3.5) has a single canonical template for new partners.

### §B.2 PRD §3.2 supplement candidate

**`layout.panels.dataSourcePanel.overlay?: ComponentType<{}> \| null`** — required by §B's FidelityCustodianBar finding. Not in PRD §3.2 as written. Per Requirement 3 (no silent renames; surface gaps to CTO), this gets logged in the "PRD §3.2 supplement" section at the bottom of this doc.

---

## §C. Per-firm constants inventory

### §C.1 `_partners/49financial/constants.ts` (12 LOC)

| Constant | Type / value | Move target (PRD §3.2) | Notes |
|---|---|---|---|
| `DEFAULT_FIRM_ID` | `'bd' as const` | DEAD CODE — **SHARED.007 delete**. Grep confirms zero importers outside the declaring file. The dispatcher hardcodes `'bd'` at `_pages/AdvisorIntelligence/index.tsx:29,31` instead of reading from here. | Pre-canonicalization the value is `'bd'` (L3 namespace); post-SHARED.006 the entire constant goes away (canonical firm-id is in `layout.firmId`). |
| `AVAILABLE_FIRMS` | `[{ id: 'bd', name: '49 Financial' }] as const` | DEAD CODE — **SHARED.007 delete**. Grep confirms zero importers. The dispatcher has its own `ALL_PARTNER_FIRMS` at `_pages/AdvisorIntelligence/index.tsx:13-16`. | Pre-existed before partner-dispatcher consolidation; never cleaned up. |
| `BD_SOURCE_ATTRIBUTION` | `'Source: SS&C Black Diamond Wealth Solutions.'` | `layout.sourceAttribution` (PRD §3.2 Identity block) | Move into `_partners/49financial/layout.ts` (created in SHARED.001 per §B.1 finding) as `FORTY_NINE_FINANCIAL_LAYOUT.sourceAttribution`. |
| `BD_TOOLTIP_ATTRIBUTION` | `{ stateNna: '...', cityAua: '...' } as const` | `layout.tooltipAttribution: Record<string, string>` (PRD §3.2 Identity block) | Same move. |
| `SMALL_ACCOUNT_THRESHOLD_USD` | `40_000` | `layout.features.smallAccountThreshold.usd` (PRD §3.2 Feature flags block) | INF emits `null` (not surfaced); 49F emits `40_000`. Field type `number \| null` already specified in PRD §3.2. |

**Missing fields (relative to Inflection's parity):** 49F's `constants.ts` does NOT declare `FIRM_ID`, `FIRM_DISPLAY_NAME`, or `PRIMARY_CUSTODIAN`. Inflection does (all 3 declared at L1-3). Per §B.1 finding, this asymmetry should resolve by SHARED.001 + SHARED.006 producing a uniform `layout.ts` shape with full Identity block populated for every firm. Scaffolding tool (PRD §3.5) emits the canonical 3 + others.

### §C.2 `_partners/inflection/constants.ts` (18 LOC)

| Constant | Type / value | Move target (PRD §3.2) | Notes |
|---|---|---|---|
| `FIRM_ID` | `'inf' as const` | `layout.firmId: CanonicalFirmId` (PRD §3.2 Identity) | Pre-canonicalization the value is `'inf'` (L3); post-SHARED.006 renames to `'inflection'` (L1 canonical). |
| `FIRM_DISPLAY_NAME` | `'Inflection Wealth Management' as const` | `layout.displayName` | Move into `inflection/layout.ts`. |
| `PRIMARY_CUSTODIAN` | `'Fidelity' as const` | `layout.primaryCustodian` | Imported by `FidelityCustodianBar.tsx:1` — keep that import path resolving post-migration via re-export or direct `layout.primaryCustodian` reference. |
| `DEFAULT_FIRM_ID` | `FIRM_ID` (alias) | DEAD CODE — **SHARED.007 delete** (same as §C.1) | Same as 49F's dead constant; never imported. |
| `AVAILABLE_FIRMS` | `[{ id: FIRM_ID, name: FIRM_DISPLAY_NAME }] as const` | DEAD CODE — **SHARED.007 delete** | Same as 49F. |
| `INFLECTION_SOURCE_ATTRIBUTION` | `'Source: Orion Portfolio Solutions.'` | `layout.sourceAttribution` | Move into `inflection/layout.ts`. |
| `INFLECTION_TOOLTIP_ATTRIBUTION` | `{ stateNna: '...', cityAua: '...' } as const` | `layout.tooltipAttribution` | Same move. |
| `SMALL_ACCOUNT_THRESHOLD_USD` | `number \| null = null` | `layout.features.smallAccountThreshold.usd` | INF=null (PRD §3.2 specifies `null` semantics: "not surfaced"). |

**Module comment hints at TODOs:** `// W5.1: populate source attribution once Inflection data pipeline is live` (L9) and `// W5.1: determine threshold with Andrew once Inflection fee schedule is confirmed` (L17). Both were resolved post-comment (Orion source attribution + null threshold respectively are the empirically-settled values). Comments are stale and should be removed in SHARED.007 mop-up.

### §C.3 `_partners/49financial/roles.ts` (16 LOC)

| Constant | Type / value | Move target (PRD §3.2) | Notes |
|---|---|---|---|
| `FortyNineFinancialRole` type | `'architect' \| 'implementor' \| 'consultant' \| 'local_ops' \| 'additional_advisor'` | DELETE — collapses into `layout.roles.keys` (string-literal array) | TS-level type loss is acceptable; the runtime keys array gives equivalent narrowing via `as const`. |
| `FORTY_NINE_FINANCIAL_ROLE_KEYS` | `readonly FortyNineFinancialRole[]` (5 keys) | `layout.roles.keys: readonly string[]` (PRD §3.2 Role taxonomy) | Move into `_partners/49financial/layout.ts` as `FORTY_NINE_FINANCIAL_LAYOUT.roles.keys`. |
| `FORTY_NINE_FINANCIAL_ROLES` | `Record<FortyNineFinancialRole, AdvisorRoleMeta>` (5 entries) | `layout.roles.meta: Record<string, AdvisorRoleMeta>` (PRD §3.2 Role taxonomy) | Same move. Each entry has `{key, label, color, order}`; values resolved from `@/lib/chartColors` (`ADVISOR_ROLE_LABELS` + `ADVISOR_ROLE_COLORS`) which stay in `_shared` (firm-agnostic palette source). |

### §C.4 `_partners/inflection/roles.ts` (13 LOC)

| Constant | Type / value | Move target (PRD §3.2) | Notes |
|---|---|---|---|
| `InflectionRole` type | `'rep' \| 'firm'` | DELETE — collapses into `layout.roles.keys` | Same TS-level loss as 49F roles. |
| `INFLECTION_ROLE_KEYS` | `readonly InflectionRole[]` (2 keys: `['rep', 'firm']`) | `layout.roles.keys` | Move into `inflection/layout.ts`. |
| `INFLECTION_ROLES` | `Record<InflectionRole, AdvisorRoleMeta>` (2 entries) | `layout.roles.meta` | INF role meta uses hardcoded hex colors (`#6366f1`, `#8b5cf6`) instead of the shared palette — possibly intentional (rep/firm aren't in `ADVISOR_ROLE_COLORS`). Worth confirming with RD whether INF roles should be added to the global palette or stay locally-colored. |

### §C.5 `_partners/inflection/layout.ts` (57 LOC)

The current INFLECTION_LAYOUT object is already a `TenantLayoutConfig`. Migration semantics: **EXPAND in place** (additive) as SHARED.001 extends the type with new fields. Existing keys preserved.

Per the §C.3 + §C.4 inventory above, post-SHARED.001 the layout grows to include `roles: { keys, meta, composition }` + Identity (`firmId`, `displayName`, `primaryCustodian`, `sourceAttribution`, `tooltipAttribution`) + `features.smallAccountThreshold.usd: null` etc. The current 57-LOC file roughly doubles in size; still under 150 LOC, comfortable as one config object.

### §C.6 `_partners/inflection/overrides/index.ts` (re-export barrel)

Read but not enumerated — barrel re-export of `FidelityCustodianBar`. Stays as-is structurally. If additional overrides land (per PRD §3.5 scaffolding), they're added to this barrel. No migration target.

### §C.7 Aggregate count

| Source | Constants | Move targets |
|---|---|---|
| 49F constants.ts | 5 | 2 DELETE (dead code) + 3 → `layout` Identity/Numeric blocks |
| INF constants.ts | 8 | 2 DELETE (dead code) + 6 → `layout` Identity/Source/Numeric blocks |
| 49F roles.ts | 3 (1 type + 2 const) | 1 type DELETE + 2 → `layout.roles` |
| INF roles.ts | 3 (1 type + 2 const) | 1 type DELETE + 2 → `layout.roles` |
| INF layout.ts | (already layout) | EXPAND in place |
| **Total** | **19 constants / types** | **6 dead-code deletes + 13 layout migrations** |

### §C.8 Sentinel-keep

Zero. Every constant migrates or deletes. No partner-level "infra-implementation detail" constants surfaced that must stay outside `layout`. (If SHARED.005 component extraction creates new partner-local constants for InflectionInsightsPanel's internal helpers — e.g., `RYG_COLOR_TABLE`, `PERCENTILE_THRESHOLDS` — those would be sentinel-keeps. None exist today.)

---

## §D. Cache-key collision resolution

`comp-cache collisions` output (captured 2026-05-12 21:50Z, identical to PRD §5.2):

### §D.1 `['advisor-book-view', 'advisorId', 'firmOverride']`

| Call site | firmOverride literal at call time |
|---|---|
| `_shared/AdvisorBookView.tsx:102` | Propagated from parent; can be `'bd'` (L3 49F) or `'inf'` (L3 INF) or `'inflection'` (L2 INF) depending on caller |
| `_shared/AdvisorPublicProfile.tsx:1734` | Same — propagated, mixed L2/L3 |

**Recommendation:** Canonicalize-upstream. SHARED.006 collapses L3 to L1 so all callers pass `'49financial'` or `'inflection'` (single literal per firm). Collision resolves once both call sites receive the same canonical literal.

### §D.2 `['advisor-intelligence', 'timeseries-overview', 'firmOverride']`

| Call site | firmOverride literal at call time |
|---|---|
| `_shared/components/PartnerAnalytics.tsx:225` | Mixed (PartnerAnalytics receives `firmOverride` prop from partner index) |
| `_shared/tabs/DistributionTab.tsx:805` | Same |

**Recommendation:** Canonicalize-upstream (SHARED.006).

### §D.3 `['firm-leaderboard', 'firmOverride']`

| Call site | firmOverride literal at call time |
|---|---|
| `_partners/49financial/index.tsx:90` | `'bd'` (L3 self) |
| `_shared/tabs/AdvisorsTab.tsx:217` | Propagated from partner index — `'bd'` or `'inflection'` |
| `_shared/tabs/ClientsTab.tsx:145` | Same as above |

**Recommendation:** Canonicalize-upstream (SHARED.006). 49F-index L90 specifically passes `'bd'` literal; rename to `'49financial'` per PRD §3.1.

### §D.4 `['partner-analytics', 'granularity', 'firmOverride']`

| Call site | firmOverride literal at call time |
|---|---|
| `_shared/components/PartnerAnalytics.tsx:116` | Propagated |
| `_shared/tabs/DistributionTab.tsx:744` | Propagated |

**Recommendation:** Canonicalize-upstream (SHARED.006).

### §D.5 Decision summary

All 4 collisions resolve via SHARED.006 firmId canonicalization. **No need for namespace-split (`cacheKeyNamespace` field in TenantLayoutConfig).** The PRD §3.2 supplement does NOT need this field added.

---

## §E. `TenantLayoutConfig` field-gap analysis

Type-extension shopping list for SHARED.001. Format: per proposed field, document current location of the data, default semantics, 49F/INF empirical values, and any semantic-divergence subtleties.

Current `TenantLayoutConfig` ([source](../../portal/src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts)) has 5 nested keys:
- `tabs.{partnerAnalytics, distribution, books, advisors}`
- `panels.{advisorList, advisorPublicProfile, roleComposition?}`

PRD §3.2 proposes the full extended schema. §E enumerates the **delta** (what needs to be added).

### §E.1 Identity block (NEW)

| Proposed field | Type | Current location | 49F value | INF value | Semantic-divergence notes |
|---|---|---|---|---|---|
| `firmId` | `CanonicalFirmId` (= `'49financial' \| 'inflection' \| 'cottonwood' \| 'opal-capital'`) | 49F: dispatcher hardcode `'bd'` (post-SHARED.006: `'49financial'`); INF: `_partners/inflection/constants.ts:1` `FIRM_ID = 'inf'` (post-SHARED.006: `'inflection'`) | `'49financial'` | `'inflection'` | Post-SHARED.006 canonicalization |
| `displayName` | `string` | 49F: hardcoded `'49 Financial'` at dispatcher L14; INF: `_partners/inflection/constants.ts:2` `FIRM_DISPLAY_NAME` | `'49 Financial'` | `'Inflection Wealth Management'` | — |
| `primaryCustodian` | `string` | 49F: not declared (gap); INF: `_partners/inflection/constants.ts:3` `PRIMARY_CUSTODIAN = 'Fidelity'` | needs population — `'SS&C Black Diamond'` likely | `'Fidelity'` | Currently used by `FidelityCustodianBar.tsx:1` (Inflection-only). After SHARED.001 + §B's `panels.dataSourcePanel.overlay`, the field becomes generally consumable. |
| `sourceAttribution` | `string` | 49F: `_partners/49financial/constants.ts:5` `BD_SOURCE_ATTRIBUTION`; INF: `_partners/inflection/constants.ts:10` `INFLECTION_SOURCE_ATTRIBUTION` | `'Source: SS&C Black Diamond Wealth Solutions.'` | `'Source: Orion Portfolio Solutions.'` | — |
| `tooltipAttribution` | `Record<string, string>` | 49F: `_partners/49financial/constants.ts:7` `BD_TOOLTIP_ATTRIBUTION`; INF: `_partners/inflection/constants.ts:12` `INFLECTION_TOOLTIP_ATTRIBUTION` | `{stateNna:'...', cityAua:'...'}` (BD-keyed strings) | same shape, Orion-keyed strings | Record keys (`stateNna`, `cityAua`) are firm-agnostic; values are firm-specific. Schema is fixed; consumers should reach for specific keys. |

### §E.2 dataSources block (NEW)

| Proposed field | Type | Current location | 49F value | INF value | Semantic-divergence notes |
|---|---|---|---|---|---|
| `dataSources.lambdaScopeKey` | `string` | `api/endpoints/advisor-intelligence.ts:76` `LAMBDA_FIRM_ID = { bd: '49financial', inf: 'inflection' }` (L3→L1 mapping) | `'49financial'` | `'inflection'` | Post-SHARED.006 this is identical to `firmId`. Reserved field for future divergence where the Lambda scope key differs from the canonical firmId. |
| `dataSources.staticPaths.clientDetailHandler` | `'static' \| 'lambda' \| undefined` | Inline `isInflectionFirm ? 'static' : 'lambda'` at `AdvisorBookView.tsx:123-124` + `ClientsTab.tsx:413-414` (cross-ref §A.2 / §A.3) | `'lambda'` (or undefined — Lambda is the default) | `'static'` | Field controls whether L3 client-detail data comes from `getPlatinumClientDetailStatic` (Inflection's pre-baked artifact) or `getPlatinumClientSummary` (BD's Lambda computation). |
| `dataSources.staticPaths.accountTimeseriesHandler` | `'static' \| 'lambda' \| undefined` | Inline `isInflectionFirm` at `AdvisorBookView.tsx:151,403` + `ClientsTab.tsx:480,617` (cross-ref §A.2 / §A.3) | `'lambda'` | `'static'` | Same pattern as `clientDetailHandler` for L4 account-timeseries data. Inflection uses INF_D_09 separate artifact; 49F uses inline `accountSummary.timeseries`. |

### §E.3 tabs block (EXTENDED — add 3 panel-substitution slots)

| Proposed field | Type | Current state |
|---|---|---|
| `tabs.books.taxCostBasisPanel` | `'standard' \| 'simplified' \| 'suppressed'` | NOT currently in `TenantLayoutConfig`. No inline branch for TaxCostBasisPanel substitution in current code — pure PRD §3.2 design proposal anticipating future Inflection or Cottonwood divergence. Default `'standard'`. |
| `tabs.books.feeEfficiencyPanel` | `'standard' \| 'suppressed'` | Same: pure PRD §3.2 proposal. Inflection currently uses `revenueOpsPanel: 'inflection_insights'` which already swaps the panel; this field is for the `'standard'`-with-suppression variant. |
| `tabs.books.concentrationPanel` | `'standard' \| 'firm_only' \| 'suppressed'` | Same: pure PRD §3.2 proposal. |

**§E.3 note:** all 3 fields are forward-looking. No 49F/INF behavior changes today. Optional fields with `'standard'` default. SHARED.001 adds the types; SHARED.002 wires consumers when needed.

### §E.4 panels block (EXTEND with §B supplement)

| Proposed field | Type | Current location | Notes |
|---|---|---|---|
| `panels.dataSourcePanel.overlay` | `ComponentType<{}> \| null` (or `string` panel-key with a registry) | `_partners/inflection/index.tsx:279` hardcodes `<FidelityCustodianBar />` inside the Data Source panel. Cross-ref §B's `_partners/inflection/overrides/FidelityCustodianBar.tsx`. | **PRD §3.2 supplement candidate** — surfaced by this audit. CTO ratification needed before SHARED.001 implements. |

### §E.5 assetClasses block (NEW)

| Proposed field | Type | Current location | 49F value | INF value | Semantic-divergence notes |
|---|---|---|---|---|---|
| `assetClasses.ordered` | `readonly string[]` | Inline `['cash', 'fixed_income', 'equity', 'alternatives'] as const` literal at `PartnerAnalytics.tsx:1856` (§A.1) | `['fixed_income', 'equity', 'alternatives']` (cash excluded) | `['cash', 'fixed_income', 'equity', 'alternatives']` (cash included) | Ordering also matters for chart segment stacking — same order both firms, just cash-prepended for INF. |
| `assetClasses.includesCash` | `boolean` | Inline `.filter(cls => cls !== 'cash' \|\| isInflectionFirm)` at `PartnerAnalytics.tsx:1494, 1641, 1856` + `ClientsTab.tsx:332` (§A.1 + §A.3) | `false` | `true` | Could be derived from `.ordered.includes('cash')` but explicit boolean is faster to read. Recommend: keep both fields; `.includesCash` is convenience, `.ordered` is authoritative. |
| `assetClasses.colorPalette` | `Record<string, string>` | `@/lib/chartColors` global palette (`MIX_PIE`, `mixPieColor`); no per-firm overrides today | Inherit global | Inherit global | Field exists for future firm-color customization; both firms default to the shared palette. |
| `assetClasses.groupings` | `Record<string, string[]> \| undefined` | Not currently used | undefined | undefined | Pure PRD §3.2 forward-looking. Optional. |

### §E.6 roles block (NEW)

| Proposed field | Type | Current location | 49F value | INF value | Semantic-divergence notes |
|---|---|---|---|---|---|
| `roles.keys` | `readonly string[]` | 49F: `_partners/49financial/roles.ts:6` `FORTY_NINE_FINANCIAL_ROLE_KEYS`; INF: `_partners/inflection/roles.ts:7` `INFLECTION_ROLE_KEYS` | `['architect','implementor','consultant','additional_advisor','local_ops']` | `['rep', 'firm']` | — |
| `roles.meta` | `Record<string, AdvisorRoleMeta>` | 49F: `roles.ts:10` `FORTY_NINE_FINANCIAL_ROLES`; INF: `roles.ts:9` `INFLECTION_ROLES` | 5 entries (delegated colors via `ADVISOR_ROLE_COLORS`) | 2 entries (hardcoded hex colors) | **Subtle divergence**: INF roles use local hex colors (`#6366f1`, `#8b5cf6`) instead of the global `ADVISOR_ROLE_COLORS` palette. RD 0.4.2 may want to add `rep`/`firm` to the global palette during SHARED.001 + SHARED.004 co-location work for consistency. Non-blocking. |
| `roles.composition.enabled` | `boolean` | Currently in `panels.roleComposition.enabled` (the existing field) | `true` (default) | `false` (INF overrides via `panels.roleComposition.enabled = false`) | **Semantic move**: PRD §3.2 places this under `roles.composition` rather than `panels.roleComposition`. Decision point for SHARED.001: keep `panels.roleComposition` for backward-compat OR refactor to `roles.composition`. Recommendation: refactor — `roles.composition` is the more cohesive location semantically. Touches `AdvisorPublicProfile.tsx` consumer (1 LOC). |

### §E.7 features block (NEW)

| Proposed field | Type | Current location | 49F value | INF value | Semantic-divergence notes |
|---|---|---|---|---|---|
| `features.gro.enabled` | `boolean` | No explicit gate today | `true` | `true` | Both firms support GRO mode. Field exists for future suppression. |
| `features.gro.maxWindowCap.months` | `number \| null \| undefined` | RD 0.4.2 commit `939138a7` removed the Max-window cap for INF (NNA/GRO modes). The cap-removal is inline in the consuming component. | TBD — currently unbounded | `null` (no cap per RD `939138a7`) | Was previously capped; recent INF-specific behavior removed cap. SHARED.001 captures the policy in the layout config. |
| `features.nna.groDecompositionEnabled` | `boolean` | ADVI_INFGRO project gate (separate active project) | TBD | TBD | Forward-looking. Active project ADVI_INFGRO Stage 1 (dispatch_held) decides the values. SHARED.001 adds the field; ADVI_INFGRO writes them. |
| `features.auaDonut.source` | `'gold_aua' \| 'partner_analytics_views'` | Inline `isInflectionFirm` branches at `PartnerAnalytics.tsx:129, 173, 275, 335, 383, 599, 943` (§A.1 — 8 sites) | `'gold_aua'` | `'partner_analytics_views'` | INF reads its donut from `partner_analytics.json#views.aua.current.donut.segments`; 49F reads from gold AUA totals. |
| `features.barChart.stacked` | `boolean` | Inline `isInflectionFirm` at `PartnerAnalytics.tsx:599` (§A.1) | `false` (single-series bars) | `true` (stacked NMNC+NMEC per quarter) | — |
| `features.smallAccountThreshold.usd` | `number \| null` | 49F: `_partners/49financial/constants.ts:12` `SMALL_ACCOUNT_THRESHOLD_USD = 40_000`; INF: `_partners/inflection/constants.ts:18` `SMALL_ACCOUNT_THRESHOLD_USD: number \| null = null` | `40_000` | `null` (not surfaced) | `null` semantic = the field renders em-dash in the UI per existing post-`5a31973b` convention. |

### §E.8 routes block (NEW — forward-looking)

| Proposed field | Type | Current location | Status |
|---|---|---|---|
| `routes.tabs` | `readonly { id: TabType; label: string; surface: 'admin' \| 'non_admin' \| 'both' }[]` | Currently constructed inline in `_partners/{firm}/index.tsx` (49F L242-249 + INF L132-145) | Pure PRD §3.2 proposal. Inflection already iterates a layout-driven tab array (`inflection/index.tsx:133-141`); 49F still hardcodes. SHARED.002 + SHARED.005 may unify into shared `routes.tabs`. |
| `routes.defaultTab` | `TabType` | Currently inline in `_partners/{firm}/index.tsx` (INF L145 `tabs[0]?.id ?? 'books'`) | Same forward-looking field. |
| `routes.customRoutes` | `Record<string, string> \| undefined` | Not currently used | Future per-firm deep-link path support. Optional. |

### §E.9 Aggregate SHARED.001 type-extension shopping list

| Block | New top-level fields | New nested fields | Touch effort |
|---|---|---|---|
| Identity | 5 (`firmId, displayName, primaryCustodian, sourceAttribution, tooltipAttribution`) | — | Trivial — pure type additions; default values come from per-firm `layout.ts` |
| dataSources | 1 (`dataSources`) | 3 (`lambdaScopeKey, staticPaths.{clientDetailHandler, accountTimeseriesHandler}`) | Trivial |
| tabs (extend) | — | 3 (`books.{taxCostBasisPanel, feeEfficiencyPanel, concentrationPanel}`) | Trivial — optional fields |
| panels (extend, §B supplement) | — | 1 (`dataSourcePanel.overlay`) | Trivial |
| assetClasses | 1 (`assetClasses`) | 4 (`ordered, includesCash, colorPalette, groupings`) | Trivial |
| roles | 1 (`roles`) | 3 (`keys, meta, composition.enabled`) | Trivial type; `roles.composition.enabled` semantic-moves from `panels.roleComposition.enabled` (1 file touch in consumer code) |
| features | 1 (`features`) | 6 (`gro.{enabled, maxWindowCap.months}, nna.groDecompositionEnabled, auaDonut.source, barChart.stacked, smallAccountThreshold.usd`) | Trivial |
| routes | 1 (`routes`) | 3 (`tabs, defaultTab, customRoutes?`) | Trivial — forward-looking |
| **Total** | **10 new top-level blocks** | **~23 new nested fields** | **SHARED.001 sized at ~150-200 LOC type addition** |

Plus per-firm `layout.ts` population:
- `_partners/49financial/layout.ts` — NEW FILE per §B.1, populating `FORTY_NINE_FINANCIAL_LAYOUT: TenantLayoutConfig` with all new field values (Identity from constants.ts, roles from roles.ts, dataSources from inline branches, etc.)
- `_partners/inflection/layout.ts` — EXPAND existing 57-LOC file to ~150-180 LOC

### §E.10 Default semantics policy (new-firm scaffolding implication)

Per PRD §3.5 scaffolding tool, every new field needs a sensible `DEFAULT_LAYOUT` value:

| Block | DEFAULT_LAYOUT value rationale |
|---|---|
| Identity | All required; scaffolding template prompts user |
| dataSources.staticPaths | `clientDetailHandler: undefined`, `accountTimeseriesHandler: undefined` (Lambda is the default code path) |
| tabs.books (substitution slots) | `'standard'` for each |
| assetClasses | `ordered: ['fixed_income', 'equity', 'alternatives']` (49F-style), `includesCash: false` |
| roles | scaffolding template prompts user (no sensible global default) |
| features.gro.enabled | `true` (default-allow) |
| features.gro.maxWindowCap.months | `null` (no cap by default) |
| features.nna.groDecompositionEnabled | `false` (opt-in) |
| features.auaDonut.source | `'gold_aua'` |
| features.barChart.stacked | `false` |
| features.smallAccountThreshold.usd | `null` (not surfaced) |
| routes.defaultTab | `'distribution'` (matches 49F-pattern) |

These become the `DEFAULT_LAYOUT` updates SHARED.001 ships alongside the type extension.

### §E.11 PRD §3.2 supplement (consolidated)

Per Requirement 3, ADD to the PRD §3.2 supplement section at the bottom of this audit:

1. **`panels.dataSourcePanel.overlay?: ComponentType<{}> \| null`** — surfaced by §B FidelityCustodianBar finding.

No other supplement gaps. All other inline branches map cleanly to existing §3.2 proposed fields.

---

## §F. Lint warning enumeration

Fresh `bun run lint` 2026-05-12 ~23:30Z (post-`ff54d611` hotfix tree).
**Total: 101 warnings, 0 errors** in 21 files.

### §F.0 PRD §2.4 framing vs empirical reality — significant divergence

PRD §2.4 framed the 102 warnings as: Category A `react-refresh/only-export-components` ~75, Category B `react-hooks/static-components` ~12, Other ~15.

Empirical rule distribution today:

| Rule | Count | PRD Category | Notes |
|---|---:|---|---|
| `unused-imports/no-unused-vars` | 23 | OTHER | Mechanical cleanup (mostly `eslint --fix`-able; some require import-order intent) |
| `@typescript-eslint/no-explicit-any` | 21 | OTHER | Type-tightening — concentrated in `InflectionInsightsPanel.tsx` (12!) + `api/endpoints/portfolio.ts` (7) + scattered |
| `react-hooks/set-state-in-effect` | 17 | OTHER | Modern ESLint rule (useEffect → setState pattern); L2 fetch in `ClientsTab.tsx` is one source post-N1-migration |
| `react-refresh/only-export-components` | 16 | **Category A** | Worse offenders below |
| `react-hooks/exhaustive-deps` | 11 | OTHER | useEffect dep-array completeness |
| `react-hooks/static-components` | 9 | **Category B** | Inner components declared in render (cross-ref PRD §3.4 two-tier rule) |
| `react-hooks/preserve-manual-memoization` | 5 | OTHER | useMemo preservation hints |
| `react-hooks/refs` | 1 | OTHER | Single ref-usage warning |

**Category remap:**
- Cat A (react-refresh): 16 (PRD predicted ~75 — **PRD overcounted by 4-5x**)
- Cat B (static-components): 9 (PRD predicted ~12 — close)
- Cat OTHER: 76 (PRD predicted ~15 — **PRD undercounted by 5x**)

The PRD's framing of Cat A as dominant is INCORRECT against today's empirical state. Cat OTHER is now dominant (~75%). Likely explanation: the post-RD-marathon DEV head (`939138a7`) introduced material `@typescript-eslint/no-explicit-any` + `react-hooks/exhaustive-deps` + `unused-imports/no-unused-vars` warnings that PRD §2.4 didn't anticipate.

**This is a Requirement 5 surfaceable observation** but not a blocker for Phase 0 audit ship. SHARED.004 (co-location) scope shrinks (16 Cat A files; was estimated against 75); SHARED.005 (component extraction) stays similar (9 Cat B). New scope needed for OTHER bucket — recommendation: SHARED.007 (residual mop-up) expand OR new SHARED.009/.010 sub-TOs for `no-explicit-any` (typing work) + `set-state-in-effect` (effect→useQuery migration; partial parallel to today's BooksTab work). **Logging in PRD §3.2 supplement.**

### §F.1 Per-file warning table

Sorted by warning count descending. ADVI_SHARED-scope files in **bold**; out-of-scope files (Attribution, market-performance, etc.) listed for completeness.

| File | Total | Cat A | Cat B | Cat OTHER | Treatment | Target TO |
|---|---:|---:|---:|---:|---|---|
| **`_partners/inflection/InflectionInsightsPanel.tsx`** | 20 | 1 | 3 | 16 | Cat A: file structure split per §3.3 co-location. Cat B: extract 3 inner components per §3.4 Tier 1. Cat OTHER: 12 `no-explicit-any` (RD 0.4.2 type-tightening; treat sentinel-keep if `any` is genuinely necessary on API response shapes) + 4 dep-array fixes. | SHARED.004 + SHARED.005 + SHARED.007 (subdivide) |
| **`_shared/tabs/DistributionTab.tsx`** | 15 | 1 | — | 14 | Heavy Cat OTHER load: 9 `set-state-in-effect` (effect→useQuery candidates), 2 `exhaustive-deps`, 2 `preserved`-memo, 2 `unused-imports`. | SHARED.004 (Cat A split) + SHARED.007 (Cat OTHER mop-up). **Note**: DistributionTab is also the `set-state-in-effect` worst-offender file — same pattern this morning's BooksTab N1→useQuery migration fixed. Candidate for a DistributionTab parallel migration as part of SHARED.007 or a separate ADVI_DISTRIB-grade TO. |
| `Attribution/constants/holdings-shared.tsx` | 14 | 13 | — | 1 | Out of ADVI_SHARED scope (Attribution page). Documented for cross-pod awareness — PRD §2.4 cited this as Cat A worst-offender, and that's still empirically true. Recommend a cross-pod follow-on TO via the relevant pod (Attribution lives in 0.2.x territory I think). | OUT-OF-SCOPE |
| **`_shared/tabs/FeeSummaryPanel.tsx`** | 9 | — | 7 | 2 | Heavy Cat B — 7 inner-`SortIcon` component declarations in render (lines 263, 460-462 cross-bound). Per §3.4 Tier 2 rule, `SortIcon` is small enough to refactor as a function returning JSX (no new React identity per render). | SHARED.005 |
| **`_shared/AdvisorPublicProfile.tsx`** | 8 | — | 1 | 7 | 1 Cat B (inner component at L1672 per PRD §3.4 audit list) + 7 Cat OTHER (5 `unused-imports`, 1 `exhaustive-deps`, 1 `preserved`-memo). | SHARED.005 + SHARED.007 |
| `api/endpoints/portfolio.ts` | 7 | — | — | 7 | 7 `no-explicit-any` in portfolio-shape responses. Out of ADVI_SHARED scope (Portfolios page); but type cleanup is portal-wide concern. | OUT-OF-SCOPE |
| **`_shared/tabs/ClientsTab.tsx`** | 5 | — | — | 5 | All Cat OTHER (5 `unused-imports`). My 2026-05-12 BooksTab migration introduced 4 new type imports (`AdvisorRole`, `FeeEfficiencyResponse`, `HeaderMetricsResponse`, `PlatinumFirmMixSummary`); some of the legacy imports may now be unused. Run `eslint --fix` to verify. | SHARED.007 (or `eslint --fix` pre-commit) |
| **`_shared/tabs/AdvisorsTab.tsx`** | 5 | — | 3 | 2 | 3 Cat B inner-component declarations + 2 Cat OTHER. Per PRD §3.4 audit list (lines 246/265/293/1112 — though PRD said 4, lint shows 3; 1 may have been resolved). | SHARED.005 + SHARED.007 |
| **`_shared/AdvisorBookView.tsx`** | 4 | — | — | 4 | 2 `no-explicit-any` + 2 `unused-imports`. | SHARED.007 (type cleanup + import sweep) |
| **`_shared/tabs/FeeEfficiencyPanel.tsx`** | 2 | 1 | — | 1 | 1 Cat A (file exports both components + B8_ROLE_KEYS/B8_ROLE_LABELS constants — split per §3.3) + 1 `unused-imports`. | SHARED.004 + SHARED.007 |
| **`_shared/panels/ClientsTable.tsx`** | 2 | — | 2 | — | 2 Cat B inner components at PRD §3.4 lines 125 + 138. | SHARED.005 |
| **`contexts/AuthContext.tsx`** | 2 | — | — | 2 | 2 `exhaustive-deps` warnings. AuthContext owns auth lifecycle — careful refactor (don't introduce new deps that re-fire critical effects). | SHARED.007 (low priority; AuthContext stability is more important than warning-elimination) |
| **`_shared/panels/useSyncedHeight.tsx`** | 1 | 1 | — | — | Cat A — file exports both hook + helper. Split per §3.3. | SHARED.004 |
| **`_shared/panels/ClientListPanel.tsx`** | 1 | — | 1 | — | 1 Cat B. | SHARED.005 |
| **`_shared/components/AUATrendChart.tsx`** | 1 | — | 1 | — | 1 Cat B. | SHARED.005 |
| **`_shared/ClientDetail/panels/MixTimeseriesPanel.tsx`** | 1 | — | 1 | — | 1 Cat B. | SHARED.005 |
| **`_shared/ClientDetail/panels/ConcentrationPanel.tsx`** | 1 | — | 1 | — | 1 Cat B. | SHARED.005 |
| **`_shared/ClientDetail/ClientDetailPage.tsx`** | 1 | — | 1 | — | 1 Cat B. | SHARED.005 |
| `context/TimeMachineContext.tsx` | 1 | 1 | — | — | Cat A — split Provider + useContext per PRD §3.3 + DT brief callout. | SHARED.004 (cross-pod scope; TimeMachineContext is portal-wide; can ride ADVI_SHARED.004 as the canonical example) |
| `components/PerformanceHeatMap.tsx` | 1 | — | — | 1 | Out of scope. | OUT-OF-SCOPE |
| `components/market-performance/RSIBars.tsx` | 1 | — | — | 1 | Out of scope. | OUT-OF-SCOPE |

### §F.2 ADVI_SHARED-scope subtotal

| Bucket | ADVI_SHARED-scope warnings |
|---:|---:|
| Cat A in scope | 4 (InflectionInsightsPanel + FeeEfficiencyPanel + useSyncedHeight + 1 misc) |
| Cat B in scope | 18 |
| Cat OTHER in scope | 53 |
| **Total in-scope** | **75 of 101** |

26 of 101 warnings are out of ADVI_SHARED scope (Attribution/portfolio/market-performance).

### §F.3 SHARED.004 / SHARED.005 sizing implications

| TO | Pre-empirical scope (PRD estimate) | Empirical scope (this audit) | Sizing delta |
|---|---|---|---|
| SHARED.004 (Cat A co-location) | ~75 file-splits | 4 in-scope splits (16 total but 12 are Attribution which is out-of-scope) | **3-5x smaller than PRD expected** |
| SHARED.005 (Cat B extraction) | ~12 component lifts | 18 in-scope lifts | **1.5x larger** |
| SHARED.007 (residual mop-up) | ~15 misc | 53 in-scope OTHER warnings | **3-4x larger than PRD expected** — needs subdivision |

### §F.4 PRD §3.2 supplement candidates (consolidated for §F)

1. **SHARED.007 subdivision** — 53 Cat OTHER warnings won't fit cleanly into one "mop-up" TO. Recommended subdivision:
   - SHARED.007a: `unused-imports` sweep across in-scope files (mechanical, eslint --fix-able; ~12 warnings in scope)
   - SHARED.007b: `no-explicit-any` type tightening (RD 0.4.2 — focus InflectionInsightsPanel; ~14 in scope)
   - SHARED.007c: `set-state-in-effect` migration (DistributionTab N1 effect→useQuery; partial parallel to today's BooksTab N1 work; ~9 in scope — sizable, may warrant its own TO)
   - SHARED.007d: `exhaustive-deps` + `preserve-manual-memoization` cleanup (~7 in scope)
2. **Out-of-scope coordination** — `Attribution/constants/holdings-shared.tsx` (13 Cat A) is portal-wide enough to deserve flagging to the Attribution pod owner. Not ADVI_SHARED scope but worth a "cross-pod awareness" line item for COO.

---

## §G. firmId namespace literal census (4-layer)

SHARED.006 will consume this section as its complete scope inventory. Every literal site is enumerated so renames are mechanical (no rediscovery work).

### §G.1 L1 — `firmAccess.ts` canonical namespace

File: `src/lib/firmAccess.ts`. **L1 stays as-is** per PRD §3.1 (other layers converge onto L1). Listed here for reference.

| Line | Literal | Context | Rename action |
|---|---|---|---|
| 18 | `INTERNAL_FIRM_ID = 'opal-capital'` | Internal-user sentinel | KEEP — canonical L1 value, never renamed |
| 21 | `'49financial':` | FIRM_ALLOWED_PATHS map key | KEEP — canonical |
| 31 | `'inflection':` | FIRM_ALLOWED_PATHS map key | KEEP — canonical |
| 41 | `'cottonwood':` | FIRM_ALLOWED_PATHS map key | KEEP — canonical |
| 75 | `'49financial':` | FIRM_EMAIL_DOMAINS map key | KEEP — canonical |
| 76 | `'inflection':` | FIRM_EMAIL_DOMAINS map key | KEEP — canonical |
| 77 | `'cottonwood':` | FIRM_EMAIL_DOMAINS map key | KEEP — canonical |

**Net L1: 0 renames.** All values already in canonical form.

### §G.2 L2 — Portal dispatcher (`AdvisorIntelligence/index.tsx`)

Cross-reference §A.6. Already enumerated:

| Line | Literal | Context | Rename action |
|---|---|---|---|
| 14 | `id: 'bd'` | ALL_PARTNER_FIRMS array entry | RENAME → `id: '49financial'` |
| 19 | `bd: FortyNineFinancialView` | PARTNER_VIEWS map key | RENAME → `'49financial': FortyNineFinancialView` |
| 29 | `useState<string>('bd')` | selectedFirmId fallback | RENAME → `useState<string>('49financial')` |
| 31 | `claims?.firmId ?? 'bd')` | claim-fallback firm | RENAME → `?? '49financial')` |

**Net L2: 4 renames** in 1 file. Atomic — all four happen in one SHARED.006 commit.

### §G.3 L3 — Partner-internal FIRM_ID constants

Cross-reference §C.1 / §C.2. Already enumerated:

| File | Line | Literal | Rename action |
|---|---|---|---|
| `_partners/49financial/constants.ts` | 1 | `DEFAULT_FIRM_ID = 'bd' as const` | DELETE (dead code per §C.1) |
| `_partners/49financial/constants.ts` | 3 | `id: 'bd', name: '49 Financial'` | DELETE (dead code per §C.1) |
| `_partners/inflection/constants.ts` | 1 | `FIRM_ID = 'inf' as const` | RENAME → `FIRM_ID = 'inflection'`, then migrate to `layout.firmId` (then delete constant per §C.2) |
| `_partners/inflection/constants.ts` | 5 | `DEFAULT_FIRM_ID = FIRM_ID` | DELETE (dead code per §C.2) |
| `_partners/inflection/constants.ts` | 7 | `id: FIRM_ID, name: FIRM_DISPLAY_NAME` | DELETE (dead code per §C.2) |

**Net L3: 1 rename + 4 deletes.** 49F has no live FIRM_ID constant to rename (only dead code).

### §G.4 L4 — Lambda routing (`api/endpoints/advisor-intelligence.ts`)

| Line | Literal | Context | Rename action |
|---|---|---|---|
| 76 | `LAMBDA_FIRM_ID: Record<string, string> = { bd: '49financial', inf: 'inflection' }` | The L3→L1 mapping table itself | DELETE — post-SHARED.006 the L3 keys ARE the canonical L1 keys, so the table becomes an identity map. PRD §3.1 explicitly: "DELETED — identity map; consumers use canonical firmId directly." |

**Downstream lookup sites** (all become identity / direct passthrough after L4 table deletes):

| Line | Pattern | Treatment |
|---|---|---|
| 287, 302, 322, 341 | `const firmId = LAMBDA_FIRM_ID[firmOverride] ?? firmOverride` | DELETE the indirection; replace with `const firmId = firmOverride` (or just inline the value). |
| 352, 362, 376, 382, 392 | `LAMBDA_FIRM_ID[firmOverride] ?? firmOverride` in template-string composition | Same: replace with `firmOverride` directly. |
| 419 | `firmId: LAMBDA_FIRM_ID[firmId] ?? firmId` in URLSearchParams | Same: replace with `firmId` directly. |
| 446 | `const resolvedFirmId = LAMBDA_FIRM_ID[firmId] ?? firmId` | DELETE the alias; use `firmId` directly. |

**Net L4: 1 table delete + 11 callsite simplifications.** Mechanical replace pass.

### §G.5 ProtectedRoute / route-tier references

Per PRD §5.2 mention. Searched for `'opal-capital'` and partner-firm literals across `src/**`:

| File | Lines | Context | Treatment |
|---|---|---|---|
| `contexts/AuthContext.tsx` | 34, 550, 573, 584, 604, 610, 615, 620 | 8 inline `firmId === 'opal-capital'` for internal-tier gates (cross-ref §A.7) | KEEP (internal-tier gate, out of ADVI_SHARED scope) |
| `pages/TradeSubmission/TradeSubmission.tsx` | 28 | 1 inline `firmId === 'opal-capital'` | KEEP (out of scope — TradeSubmission is a separate page outside ADVI) |
| `components/ui/__tests__/PageSurfaceControl.demo.tsx` | (test stub) | Likely `'bd'` / `'inflection'` as demo data | KEEP-OR-DELETE (test-file allowlist per PRD §3.6 ESLint rule; safe to leave as-is) |

**ProtectedRoute reference per PRD §5.2:** searched for `ProtectedRoute` import + usage. Result: not found as a literal route-component name in this audit's grep results. May be at the App.tsx level (out of `pages/AdvisorIntelligence/` scope) or may be a PRD §5.2 reference to the `isPathAllowedForFirm()` route-access function pattern instead. Recommend CTO clarify in PRD §3.2 supplement — non-blocking.

### §G.6 Aggregate SHARED.006 scope

| Layer | Action | Site count |
|---|---|---|
| L1 firmAccess.ts | KEEP-AS-IS (canonical) | 0 renames |
| L2 dispatcher | RENAME `'bd'` → `'49financial'` | 4 sites in 1 file |
| L3 partner constants | DELETE dead constants + RENAME live FIRM_ID via migration to `layout.firmId` | 1 rename + 4 deletes |
| L4 LAMBDA_FIRM_ID | DELETE map + simplify 11 callsites | 1 delete + 11 simplifications |
| Test files + out-of-scope | KEEP | n/a |
| **Total SHARED.006 surface** | | **~21 mechanical edits in 4 files** |

SHARED.006 is structurally small (4 files) but has cross-file invariants (L2 + L3 + L4 must rename atomically; otherwise dispatcher lookup falls through). Recommend a single-PR SHARED.006 commit that touches all 4 files plus a CI grep gate.

---

## §H. Cross-project overlap risks

Active TOs from ADVI_INFTGT + ADVI_INFGRO with portal/src/pages/AdvisorIntelligence/** touch scope.

### §H.1 ADVI_INFGRO (Stage 1 — dispatch_held)

DE-side TOs (live + portal-touching):

| TO | Status | Files Touched | Overlap with ADVI_SHARED |
|---|---|---|---|
| `ADVI_INFGRO.005.de-portal-gro-side-by-side` | pending + dispatch_held (gated on DS~A `TO-INFGRO.004` MCP signal + Andrew Q decisions) | `_shared/tabs/AdvisorsTab.tsx` (extend with GRO decomposition); `_shared/types.ts` (`PlatinumLeaderboardResponse` field extension for `advisor_return_pct_twr`, `advisor_nna_$`, `advisor_epsilon_$`) | **OVERLAP** — AdvisorsTab is in §A.1 (lint Cat A worst-offender per PRD §2.4 + DT brief), expected to be touched by SHARED.004 (co-location refactor) and possibly SHARED.005 (component extraction). The type extension on `PlatinumLeaderboardResponse` is orthogonal to ADVI_SHARED's `TenantLayoutConfig` extension. |
| `ADVI_INFGRO.006.de-max-window-twr-reenable` | pending + dispatch_held (gated on TO-INFGRO.005 + coverage proof) | `_shared/tabs/DistributionTab.tsx` (re-enable MAX-window TWR mode) | **OVERLAP** — affects the `features.gro.maxWindowCap.months` field proposed in §E.7. ADVI_INFGRO ships the policy value (`null` for INF); ADVI_SHARED ships the field. **Sequencing dependency**: ADVI_SHARED.001 (type extension) must land BEFORE ADVI_INFGRO.006 can wire `features.gro.maxWindowCap.months` instead of an inline hardcode. |

DS-side TOs (no portal overlap):

| TO | Status | Files Touched | Overlap |
|---|---|---|---|
| `ADVI_INFGRO.001.ds-perf-canonical-silver` | staged | `data/orion/scripts/silver/*` | NONE |
| `ADVI_INFGRO.002.ds-puller-persist-summaries-block` | staged | DS data layer | NONE |
| `ADVI_INFGRO.003.ds-client-perf-three-field-decomposition` | staged | DS data layer | NONE |
| `ADVI_INFGRO.004.ds-leaderboard-gro-rollup` | staged | Gold scripts (extends `INF_D_00c.portal_leaderboard.py`) | NONE — DS-side, no portal touch |
| `ADVI_INFGRO.TO-000(.b).ds-cashflow-taxonomy-yaml-...` | staged | Cashflow taxonomy infra | NONE |

### §H.2 ADVI_INFTGT (P0 closed; P1/P2 HOLD)

Per project state (from my session-start log + COO context), ADVI_INFTGT P0 wave is closed. P1/P2 are on HOLD pending RD scope reconciliation. Active DS-side TOs:

| TO | Status | Files Touched | Overlap |
|---|---|---|---|
| `ADVI_INFTGT.TO-1.ds-period-start-aua-fix` | (DS lane) | Gold scripts | NONE — DS layer |
| `ADVI_INFTGT.TO-1b.ds-snapshot-pair-existence-check` | (DS lane) | Gold scripts | NONE |
| `ADVI_INFTGT.TO-2.ds-avg-fee-bps-unit-fix` | (DS lane) | Gold scripts | NONE |
| `ADVI_INFTGT.TO-2b.ds-timeseries-canonical-realign` | (DS lane) | Gold scripts | NONE |
| `ADVI_INFTGT.TO-4b.ds-geo-untagged-bucket` | (DS lane) | Gold scripts | NONE |
| `ADVI_INFTGT.TO-7.ds-concentration-risk-wire-up` | (DS lane) | Gold scripts | NONE |
| `ADVI_INFTGT.TO-8.dsc-activity-scan-cash-drag-compute-fix` | (DS lane) | Gold scripts | NONE |

RD-side ADVI_INFTGT TOs (TO-3, TO-4, TO-10) — all complete per `<status>` grep (2026-05-12). No active portal overlap.

**Net ADVI_INFTGT overlap: ZERO.** P1/P2 HOLD'd, no active portal touch.

### §H.3 Aggregate cross-project overlap

| Project | Overlap with ADVI_SHARED scope | Sequencing recommendation |
|---|---|---|
| **ADVI_INFGRO** | 2 active DE TOs (`.005` + `.006`) both touch portal `_shared/tabs/*` | **SEQUENCE**: SHARED.001 (type extension) lands first → unblocks `.006` to use `features.gro.maxWindowCap.months` without inline hardcode. SHARED.004 (co-location) on AdvisorsTab can serialize after `.005` lands OR run in parallel via cross-domain-coordination block. Andrew Q5 ruling on parallel-vs-serialize. |
| **ADVI_INFTGT** | None — DS lane work + RD TOs complete | No coordination needed |
| **ADVI_INFLEC** (chain marathon complete 2026-05-12) | None active — chain shipped | No coordination needed |
| **ADVI_FIRMSEP** (Phase 1+2 complete 2026-05-07/11) | Data-side primitives; portal-side sibling | No active overlap (separate layer) |

### §H.4 Schema-check leaf-component failure (compiler tool gap)

`comp-transform schema-check InflectionAdvisorIntelligence` and `comp-transform schema-check FortyNineFinancialAdvisorIntelligence` both returned **"Component not found"** on 2026-05-12. The graph indexes components by some-other-naming-convention; the leaf names in `_partners/{firm}/index.tsx` (`InflectionAdvisorIntelligence`, default export from 49F's `index.tsx` as `AdvisorIntelligence as FortyNineFinancialView`) don't resolve.

**Impact**: low — schema validation falls back to manual Grep + TSC. Audit completion not blocked.
**Workaround**: filename-derived entity names. Empirically `comp-transform schema-check ClientsTab` resolves; `BooksTab` does not (the exported name vs the filename); `InflectionInsightsPanel` likely resolves.
**Recommended action**: file under ADHC_COMPIL_V4 indexer brief (CTO drafted) for resolution — schema-check should accept either filename-stem OR primary-exported-component-name to be useful for audit work.

### §H.5 Mid-audit hotfix (informational, not overlap-blocking)

During this audit I shipped a localhost-only regression hotfix `ff54d611` (revert of Step 6 AuthContext.prefetchQuery upgrade from `6f81d13a`'s BooksTab migration). PROD `portal-v2.1.82` unaffected. The hotfix is on portal DEV `ff54d611` + parent CLOUD `c741c0e81`. This is mentioned here so anyone reading the audit notices the `AuthContext.tsx` is in its pre-prefetchQuery-upgrade state — relevant to anyone authoring SHARED.001 who might be tempted to re-introduce the upgrade. **Don't re-do Step 6 until the COO-filed follow-on TO `prefetchquery-saturation-root-cause` (commit `576056e67`) resolves the root cause.**

**Working hypothesis (DT 0.4 raised to COO 23:30Z):** The prefetchQuery saturation may be caused by the same firmOverride-namespace divergence that produces the 4 cache-key collisions in §D — prefetch fires with one firmOverride literal (`'bd'` for internal users via `prefetchAdvisorIntelligence`), component mounts with a different literal (`'inf'` or `'inflection'` post partner-switch), React Query's dedupe fails because keys don't match, second fetch happens, both compete on the same connection pool. **If DT's hypothesis is correct, SHARED.006 firmOverride canonicalization is the structural fix** — Step 6 prefetchQuery upgrade can be safely re-introduced AFTER SHARED.006 ships. COO concurred 23:30Z.

---

## PRD §3.2 supplement (consolidated from §B, §E, §F findings)

Per Requirement 3, fields surfaced by the audit that aren't in PRD §3.2 as authored. CTO ratification needed before SHARED.001 implementation.

### Supplement field 1 — `panels.dataSourcePanel.overlay`

| Property | Value |
|---|---|
| Proposed field | `layout.panels.dataSourcePanel.overlay` |
| Type | `ComponentType<{}> \| null` (or `string` panel-key with a registry) |
| Default | `null` |
| Source | §B (FidelityCustodianBar partner-only Data Source panel decoration) |
| Rationale | The pattern "render an overlay component in the Data Source panel" needs a config slot. PRD §3.2 panel registry covers `revenueOpsPanel` + 3 proposed (`taxCostBasisPanel`, `feeEfficiencyPanel`, `concentrationPanel`) but not `dataSourcePanel`. INF needs this slot to register `FidelityCustodianBar`; 49F defaults to `null` (no overlay). |
| Consumer migration | `_partners/inflection/index.tsx:279` removes the hardcoded `<FidelityCustodianBar />` and the shared `DataSourcePanel` renders `layout.panels.dataSourcePanel.overlay` if non-null. |

### Supplement note 1 — SHARED.007 subdivision

Per §F.3 sizing: 53 Cat OTHER warnings need finer task-order decomposition than PRD §4.2 "SHARED.007 residual mop-up." Recommended subdivision (TBD with COO):

- **SHARED.007a** — `unused-imports` sweep (mechanical eslint --fix; ~12 in-scope warnings)
- **SHARED.007b** — `@typescript-eslint/no-explicit-any` type tightening (RD 0.4.2 focus on `InflectionInsightsPanel.tsx`; ~14 in-scope)
- **SHARED.007c** — `react-hooks/set-state-in-effect` migration (DistributionTab N1 effect→useQuery; ~9 in scope; this morning's BooksTab N1 migration is the canonical template)
- **SHARED.007d** — `react-hooks/exhaustive-deps` + `preserve-manual-memoization` cleanup (~7 in scope)

### Supplement note 2 — PRD §2.4 lint category framing was off (§F.0)

PRD §2.4 framed: Cat A ~75, Cat B ~12, Other ~15. Empirical state today: Cat A 16, Cat B 9, Other 76. The PRD's "Cat A dominant" framing is incorrect — Cat OTHER dominates by 5x. Adjust SHARED.004 sizing downward (now 4 in-scope splits, not 75) and SHARED.007 sizing upward (subdivide per Supplement note 1).

### Supplement note 3 — Cross-pod coordination flag

`Attribution/constants/holdings-shared.tsx` (13 Cat A) is portal-wide architectural debt that SHARED.004's conventions (PRD §3.3 co-location) would also fix if Attribution adopts them. Suggest a cross-pod awareness ping from COO to the Attribution pod owner so ADVI_SHARED's lint regression gate (§3.6) doesn't trip a Pod-2 review when Attribution gets touched.

### Supplement note 4 — `roles.composition` semantic move (§E.6)

PRD §3.2 places `roles.composition.enabled` under the `roles` block; today's code has `panels.roleComposition.enabled`. SHARED.001 must decide: refactor to `roles.composition` (recommended for semantic cohesion; 1 file touch in `AdvisorPublicProfile.tsx` consumer) OR keep `panels.roleComposition` for backward-compat. Audit recommendation: refactor.

### Supplement note 5 — comp-transform indexer gap (§H.4)

`comp-transform schema-check` resolves filename-stem (`ClientsTab`) but not exported-component-name (`BooksTab`). Workaround: filename. File under ADHC_COMPIL_V4 indexer brief for resolution. Non-blocking for this audit; affects future schema-validation work.

---

## Audit metadata

| Item | Value |
|---|---|
| Sections complete | §A (32 sites) + §B (10 partner files) + §C (19 constants/types) + §D (4 collisions) + §E (~23 new fields) + §F (101 warnings in 21 files) + §G (~21 mechanical SHARED.006 edits in 4 files) + §H (cross-project overlap + tooling gaps + hotfix note) |
| Total document length | (run `wc -l` per Phase 2 mandate to verify ≥ 300 lines) |
| Mid-checkpoint heartbeat | Fired 2026-05-12 22:05Z to COO after §A + §B + §D complete. COO ACK 23:15Z (§3.2 supplement accepted, comp-transform indexer flag accepted, §B Inflection-ahead-of-49F finding noted for SHARED.001 scoping). |
| Compiler tools log | Session log at `org/tier2_senior/0.4.0_DE_ClientPlatform/logs/2026-05-12/session_advi_shared_000_phase0_audit.md` |
| Audit revision | r1 — full §A through §H + PRD §3.2 supplement consolidated |
| PRD §3.2 supplement candidates | 1 new field (`panels.dataSourcePanel.overlay`) + 5 notes (SHARED.007 subdivision, lint-category-framing correction, cross-pod coordination, `roles.composition` semantic move, comp-transform indexer gap) |
| Out-of-scope sites noted | 8 internal-tier gates (`firmId === 'opal-capital'`) + 4 lint-warning files (Attribution, portfolio.ts, market-performance) |
