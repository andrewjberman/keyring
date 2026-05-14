# Session — ADVI 5-surface Inflection arc → ADHC_FECACHE_COHERENCE categorical defense

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-14
**Session window:** approximately 12:42Z (Andrew 5-surface trigger) → 18:36Z (categorical SHIPPED) — ~6h wall
**Portal DEV chain:** `1dd406f0` (Issue #2 fee-cascade) → `ec1e4688` (Issue #3 cost_basis) → `d0bbc856` (Phase 2a Conservative) → `dcab7fe6` (NMCOHT foundation) → `95b67df2` (NMCOHT PartnerAnalytics rewire) → `a40d2595` (NMCOHT type drift) → `120df453` (ADHC_FECACHE_COHERENCE.001 categorical)
**Workspace CLOUD:** `2a542e519` (comp-types brief) → `e70fb243f` (Snapshot brief) → `4aa5e2948` (5-surface brief) → `ebce828ac` (FE-cache audit brief) → `b0220e9e9` (categorical v0.1 brief) → `bde4cbd13` (v0.2) → `307b1a3d3` (v0.2.1)
**TOs:** ADVI_INFFIN Issue #2 + #3 (Phase 1.4); ADHC_FECACHE_COHERENCE.001 (CTO-PRD ratified); ADVI_INFLEC.NMCOHT (DS~D-led)

---

## Scope

Five distinct work surfaces shipped this arc:

1. **Issue #2 fee-cascade FE wiring fix** (Andrew 5-surface dispatch surface #2)
2. **Issue #3 cost_basis FE wiring fix** (sibling adapter-omission class)
3. **Issue #5 $202M vs $203M routing correction** (no portal consumer of nmec_nmnc_nna.json)
4. **FE-cache freshness audit brief + Phase 2a Conservative ship** (per-callsite class)
5. **ADHC_FECACHE_COHERENCE design → CTO ratify → categorical implementation** (chain-boundary class)
6. **ADVI_INFLEC.NMCOHT foundation + PartnerAnalytics rewire** (per-HH cohort bucketing per Andrew NO-ROLLING)

All FE work on the Inflection partner surface — cascade triggered by Andrew empirical screenshot pack 12:42-12:51Z + 13:27Z Monthly/Quarterly divergence.

---

## Trigger — Andrew 5-surface screenshot pack

Andrew message 12:42Z: *"I want to bring in a handful of screenshots for your analysis and rectification because I see little errors spread throughout the ADVI page for Inflection that we need to assess and fix. The question of course is if the error is frontend or backend or both, so you need to investigate each and escalate to DS~A if backend is needed."*

5 surface defects:
| # | Surface | Initial diagnosis |
|---|---------|-------------------|
| 1 | AdvisorsTab GRO/RANK columns empty | DS~A (leaderboard emit gap) |
| 2 | AdvisorPublicProfile fee-toggle cascade (Clients=0 / New=0 on Fee-Paying) | DE (suspected DS but empirically FE-adapter) |
| 3 | BookView Asset Mix + Top Holdings + Cost Basis empty | DS~C (gold gap) + DE (FE-side cost_basis adapter omission) |
| 4 | Continuous Segment Analytics "0 New Clients" | DS~C |
| 5 | $202M (header) vs $203M (Segment + Books) AUA divergence | Initially routed FE-cache, corrected to gold-side after DS~A surfaced INF_D_08:259 orphan emit, re-corrected to FE-cache after DE grep confirmed no portal consumer |

5-surface brief authored at `docs/briefs/inf_advi_5_surface_survey_20260514.md` (commit `4aa5e2948`) for COO decomposition into per-lane TOs.

COO decomposed:
- Phase 1.1 → DS~A (Issue #1 + #5 Part B nmec_nmnc_nna investigation)
- Phase 1.2 → DS~C (Issue #3 BookView holdings + Issue #4)
- Phase 1.3 → AE 0.7 (Issue #5 L@E rewrite trace)
- Phase 1.4 → DE 0.4 (Issue #2 fee-cascade)

---

## Issue #2 fee-cascade FE wiring — what shipped

**Commit `1dd406f0`** (portal DEV, 1 file / +10 / -0).

Root cause: Inflection static-S3 adapter at `portal/src/api/endpoints/advisor-intelligence.ts:924-930` dropped `is_fee_paying` per-client during the `.map()` transform from raw `book.json#clients[]` to output `book.clients[]`.

End-to-end empirical chain:
- `s3://opal-data-inf/platinum/advisors/peter_lee/book.json#clients[]` → 199 entries, `is_fee_paying` populated (184 true / 15 false), `relationship_since` populated
- `AdvisorClient.is_fee_paying?: boolean` was already declared at `types.ts:1114` (D_02 emit prep from ADVI_PROFAU.002)
- FE overlay at `feeBucket.ts:170` filters `c.is_fee_paying === want` → undefined !== true → 0 matches → SummaryCard showed `Clients: 0` + `New Clients: 0` on Fee-Paying selection
- Accounts: 514 still rendered correctly because it reads `book.fee_earning_account_count` (a separate field path)

Fix:
1. Added `is_fee_paying?: boolean` to `InflecAdvisorBookRaw.clients[]` type
2. Added `is_fee_paying: c.is_fee_paying` to the `.map()` transform output

`bun tsc --noEmit` clean. Acceptance: post-portal-merge, Peter Lee Fee-Paying → expect 184 Clients (was 0) + 39 New Clients since 2025-01-01 (was 0).

**COO 17:09Z RAVC2 ACCEPTED.**

---

## Issue #3 cost_basis FE wiring — what shipped

**Commit `ec1e4688`** (portal DEV, 1 file / +12 / -2).

Sibling adapter-omission bug class to Issue #2. Inflection static-S3 adapter at `advisor-intelligence.ts:988-996` STUBBED `tax_exposure` to all-zero with a stale `// DS gap pending advisor-level rollup` comment. DS~C INF_D_02 had long since emitted the full block; the adapter just never got updated.

Empirical Peter Lee `book.json#tax_exposure`:
- `cost_basis_by_year` (array of 7 entries; purchase_year, cost_basis, market_value, unrealized_gain)
- `top_gain_positions` (array)
- `realized` / `unrealized` blocks
- `taxable` / `tax_deferred` / `tax_free` + per-bucket pcts
- `capital_gains_ttm`

DS~C Phase 1.2 RAVC2 had ruled-OUT cost_basis as a gold-emit gap (data exists in book.json). FE follow-on uncovered the adapter stub as the root cause.

Fix:
1. Added `tax_exposure?: PlatinumAdvisorSummary['tax_exposure']` to `InflecAdvisorBookRaw` type
2. Replaced zero-stub with `raw.tax_exposure ?? {fallback}` in adapter output

**Banking signal:** Inflection static-S3 adapter `getPlatinumAdvisorSummaryStaticInflection` is a hot zone of stale-stub-by-design landmines. Two sibling adapter-omission bugs in one file in one session. Both typecheck-green because destination types are optional. COO authorized opportunistic stale-stub audit pass through the function (P3; not blocking).

---

## Issue #5 routing correction — what surfaced

**No portal commit** — routing-only call.

Surface: Andrew screenshot footer 12:51Z showed "TOTAL AUA $202M" on page header while Segment Analytics Snapshot Monthly + Books Firm Overview both showed $203M.

Three-act diagnostic walk:

**Act 1 (AE 0.7 17:13Z):** "$202M does NOT exist anywhere in S3" — initial probe scope-narrow. Routing call: FE-cache class; Andrew hard-refresh resolves.

**Act 2 (DS~A 17:15Z):** Full 14-artifact sweep found `s3://opal-data-inf/platinum/firm/nmec_nmnc_nna.json#total.total_aua = $202,602,212.50` ON S3. Root cause: `INF_D_08.nmec_nmnc_nna.py:259` household aggregation misses $581K vs firm canonical $203,183,160.52. **Routing call: DS-side fix-forward, NOT FE-cache.**

**Act 3 (AE 0.7 correction 17:1XZ):** Self-corrected scope-narrow probe; concurred with DS~A.

**Act 4 (DE 0.4 17:13Z grep):** Strict grep `grep -rn "nmec_nmnc_nna" portal/src/` → **ZERO matches**. No portal source file fetches that artifact via any path. `getHeaderMetrics()` reads `header_metrics.json` ($203M canonical), NOT `nmec_nmnc_nna.json`. The `HeaderMetrics` component reads `data.nmnc_ytd` / `data.nmec_ytd` — those are FIELDS on `HeaderSummary` (header_metrics.json), not the artifact name. **Empirical correction: no FE consumer of nmec_nmnc_nna.json.** AE Act 3 correction is structurally true ($202M IS on S3) but routing-irrelevant — no portal consumer exists, so Andrew's $202M screenshot cannot trace through any portal wire path to that artifact.

**COO 17:18Z final routing call:** FE-cache class confirmed (DE 0.4 grep evidence load-bearing). DS~A INF_D_08 fix downgraded P1 → P3 (data-integrity tech debt; not demo-blocker). AE 0.7 banked audit-discipline lesson on scope-narrow probe.

**Meta-rule banked (CTO 17:13Z):** "consumer-path verify before escalating data-side finding to P1." Memory entry candidate `[[feedback-coo-routing-consumer-path-grep-first]]`.

---

## FE-cache freshness audit brief + Phase 2a Conservative

**Trigger:** Issue #5 routing correction surfaced FE-cache as the actual class. Companion brief authored.

### Brief `ebce828ac` — `docs/briefs/fe_cache_freshness_audit_design_20260514.md`

179-LOC brief enumerating 23 `refetchOnMount: false` callsites across 7 files in `portal/src/pages/AdvisorIntelligence/`. Risk-tiered:

| Tier | Count | Class |
|------|-------|-------|
| P1 | 14 | Cross-firm/cross-tenant URL variation; firmOverride in queryKey AND URL; URL-helper changes create poisoning |
| P2 | 4 | Tenant-flag in queryKey suffix bounds blast radius |
| P3 | 5 | Per-entity-id keyed; URL invariant per (firm, entity) tuple |

Today's `cb62f069` fix (from earlier session block) patched 1 of 14 P1 callsites; 13 siblings remained as latent landmines for FIRMSEP.10 Cottonwood onboarding's imminent ROUTER_FIRM_SUFFIX expansion.

Plus v0.6 `comp-validate fe-cache-freshness <queryKey>` tool spec proposal (CTO-banked as v0.6 ADHC_COMPIL_V4 candidate).

### Phase 2a Conservative ship `d0bbc856`

Per COO Q2 endorsement: drop `refetchOnMount: false` on 14 P1 callsites only; keep `staleTime: 5min`; skip AuthContext invalidate (gated on categorical CTO ratification).

14 callsites touched across 6 files (P2/P3 callsites intentionally untouched):
- `_partners/49financial/index.tsx` ×3 (firm-leaderboard, partner-analytics quarterly, cohort-a-summary)
- `_partners/inflection/index.tsx` ×2 (firm-leaderboard, partner-analytics quarterly)
- `_shared/AdvisorBookView.tsx` ×1 (inflec-account-timeseries L4)
- `_shared/tabs/ClientsTab.tsx` ×2 (firm-leaderboard, inflection-client-directory)
- `_shared/tabs/DistributionTab.tsx` ×3 (platinum-cumulative-chart, timeseries-overview, advisor-book-relationship-stacks)
- `_shared/components/PartnerAnalytics.tsx` ×3 (partner-analytics granularity, inflec-timeseries-chart, timeseries-overview)

Net +0 LOC (1-for-1 swap with inline provenance comment). `bun tsc --noEmit` clean.

**Bug class disarmed for Cottonwood ship.**

---

## ADHC_FECACHE_COHERENCE — design → ratify → categorical implementation

### Trigger — Andrew empirical 13:27Z Monthly/Quarterly divergence

Andrew screenshots:
- Monthly view: $203M / May 14 footer
- Quarterly view: $202M / May 13 footer
- Same Distribution panel, same Inflection partner, same browser session

S3 truth at the same minute:
- All 3 partner_analytics_{monthly,quarterly,annual}.json carry IDENTICAL `data_as_of: 2026-05-14` + `total_aua: $203,183,160.52`
- mtimes within 7s at today's 10:22Z chain emit

**Andrew directive verbatim:** *"When we update portal files, we need to update ALL of them. This outcome should never happen. We need to identify where in our process we allow for this dispersion and fix it categorically."*

### Diagnosis

Root cause: `portal/src/main.tsx:33-60` configures `staleTime: Infinity` global + `PersistQueryClientProvider` with 12h localStorage persistence + zero `queryClient.invalidateQueries` calls anywhere in `portal/src/pages/AdvisorIntelligence/`. Quarterly's response was localStorage-persisted from yesterday's session; today's tab hydrated React Query from disk → showed yesterday's $202M. Monthly was a cache miss → fetched fresh today → $203M. Same panel, two chain boundaries' worth of data simultaneously.

### Brief v0.1 → v0.2 → v0.2.1

Per Andrew in-conversation choice: **full design doc + CTO ratification first**; scope **AdvisorIntelligence queries only**.

| Brief | Commit | What |
|-------|--------|------|
| v0.1 | `b0220e9e9` | Initial 304-LOC design DRAFT; 5 implementation choices for CTO; 5 open questions; goals/non-goals; component architecture; test plan; rollback plan; risk register; decision log |
| v0.2 | `bde4cbd13` | §-decisions locked post CTO 17:54Z ratification; data_as_of universality census results (28 canonical / 3 aliases / 7 lacks); Option A multi-key normalization recommended |
| v0.2.1 | `307b1a3d3` | Option A ratified 18:05Z; §"Open follow-ons" (4 DS-side emit-adds); §"Generalized pattern observation" (CTO banking note on same-semantic-different-name pathology hitting 3 times today); code-level cross-ref comment from extractChainTimestamp() to [[feedback-bidirectional-translator-pattern]] |

### CTO ratification chain

CTO `1.0.0_SA_CTO` ratified 17:54Z all 5 implementation choices + all 5 Q answers + R4 atomic-buster-bump:

| # | Choice | Decision |
|---|--------|----------|
| 1 | Interceptor in `apiRequest()` body (vs QueryClient global onSuccess) | RATIFIED |
| 2 | `invalidateQueries` lazy refetch (vs refetchQueries / removeQueries) | RATIFIED |
| 3 | Single cache-buster retry on older `data_as_of` | RATIFIED |
| 4 | Module-singleton + sessionStorage canonical store | RATIFIED |
| 5 | Hardcoded queryKey prefix allowlist (fail-closed) | RATIFIED |
| R4 | `buster: 'v1' → 'v2'` ATOMIC with categorical PR | RATIFIED |

CTO 18:05Z separately ratified Option A multi-key normalization for the `data_as_of` universality gap.

### `data_as_of` universality census (CTO Q1 ask)

Enumerated all 46 `apiRequest<T>` return types in `advisor-intelligence.ts`; grep'd `types.ts` for each:

- **28 types** carry canonical `data_as_of` (load-bearing AdvI surface)
- **3 types** use semantically-equivalent field aliases:
  - `HeaderSummary.as_of_date` ← **the field Andrew literally saw in his $202M screenshot footer**
  - `FeeEfficiencyResponse.as_of_date`
  - `CohortASummaryResponse.snapshot_date`
- **7 types** lack chain-bound freshness marker (3 legitimate skips; 4 DS-side flag follow-ons)

Without Option A multi-key normalization, the categorical fix would have MISSED the precise field Andrew saw broken. Recommended Option A over forcing DS-side rename across 3 gold scripts (~3h DS work + chain re-fire).

### Categorical implementation ship `120df453`

5-file atomic PR; ~270 LOC total (code ~120 LOC + comments + provenance cross-refs):

| File | LOC | Purpose |
|------|-----|---------|
| `portal/src/lib/dataAsOfCanonicalStore.ts` | +75 NEW | Module-singleton + sessionStorage persistence; `get` / `set` / `clear` primitives; lazy-init on first read |
| `portal/src/lib/isAdvisorIntelligenceScope.ts` | +70 NEW | 17-prefix queryKey allowlist (Choice 5; fail-closed); other-page queries unaffected |
| `portal/src/api/endpoints/advisor-intelligence.ts` | +85 MODIFY | `extractChainTimestamp()` multi-key + `observeChainTimestamp()` interceptor + apiRequest wrapper with single-retry budget |
| `portal/src/contexts/AuthContext.tsx` | +3 MODIFY | `clearCanonicalDataAsOf()` paired with `queryClient.clear()` on logout |
| `portal/src/main.tsx` | +7 MODIFY | `export const queryClient` for interceptor access + R4 atomic `buster: 'v1' → 'v2'` |

`bun tsc --noEmit` clean. All 5 CTO choices implemented to spec. ~50min wall (under CTO ~1-1.5h sizing).

**Invariant enforced:** Within a single browser session, if any AdvI fetch returns a response with `data_as_of = D2 > canonical`, every cached AdvI query whose response had `data_as_of < D2` is invalidated before the user observes the new response. The first view to fetch a newer chain run drags every other AdvI view in the session forward.

**Defense-in-depth pair with Phase 2a `d0bbc856`** (URL-decoupling class + chain-emission boundary class together).

---

## ADVI_INFLEC.NMCOHT — per-HH cohort bucketing

### Trigger — Andrew direct

DS~D RAVC1 to DE (mid-session 18:11Z): Andrew direct directive verbatim *"I do NOT WANT ROLLING. We do not use rolling metrics anywhere."* + *"I need to know the first transaction appearance per HH ID because the frontend will bucket those between monthly / quarterly / yearly endpoint views."*

DS~D gold-side ship `2e45c8e25` emits `hh_lifecycle` top-level array on `partner_analytics_{monthly,quarterly,annual}.json` per-HH inception records.

Andrew's "$20M anomaly" was reading the rolling-365d donut (sums Q3'25+Q4'25+Q1'26+Q2'26 partial cohorts ≈ $20M). Under per-quarter cohort bucketing, current quarter 2026-Q2 = $4.2M, matching Andrew "$5M typical" baseline.

### Schema-lock done async

DS~D's brief + 18:30Z RAVC2 had everything needed. No 45min sync slot used. Three open Qs answered:
- Q1 `rep_id`: keep (AdvisorsTab future per-rep cohort views)
- Q2 `inception_source`: keep open string (forward-compat)
- Q3 empty-array fallback: render $0; NO rolling fallback

### Design B confirmed

DS~D 18:30Z reply on timeseries_chart.json question: **Design B confirmed — single source of truth via hh_lifecycle.** FE buckets ALL periods (current + historical) from hh_lifecycle. `timeseries_chart.json#quarters[i].nmnc/nmec` becomes orphan field (still emitted by INF_D_00b but no FE consumer post-rewire). DS~D opportunistic deprecation on next INF_D_00b touch.

INF_D_00b's existing per-period bucketing uses `accounts_dim.first_trade_date` (legacy heuristic); hh_lifecycle uses `accounts_v2.account_start_date` (authoritative). Design B normalizes all FE reads to authoritative.

### NMCOHT foundation `dcab7fe6`

3-file change ~175 LOC:
- `HhLifecycleRow` type added to `_shared/types.ts` (8 fields per DS~D schema)
- `PartnerAnalyticsResponse.hh_lifecycle?: HhLifecycleRow[]` extension
- `_shared/lib/nmncBucketing.ts` NEW (~130 LOC, 4 helpers: `periodRangeFor`, `bucketNmncByPeriod`, `nmecForPeriod`, `currentPeriodKey`)
- Math validated against DS~D probe (Q2'26 → $4.2M matches Andrew baseline)

### NMCOHT PartnerAnalytics rewire `95b67df2`

Per-file rewire ~+69/-20 LOC. Two memos rewired:

1. **`auaDonutSegments` memo**: overrides nmnc/nmec segments with FE-bucketed values for current period; zero'd "existing" residual per Andrew binary invariant (nmnc + nmec = total_aua)
2. **`allSortedAuaPeriods` memo**: replaces per-period NMNC/NMEC with bucketed values for ALL periods (current + historical). REMOVED the rolling-365d last-bar segment-patch logic that was the Andrew load-bearing bug.

Tile rendering at `L1752+` + bar rendering at `L1900+` inherit bucketed values automatically through `aggregatedAuaData → src.NMNC/nmec` reads (no separate tile-site touch needed).

### NMCOHT type drift fix `a40d2595`

DS~D 18:30Z flagged minor type drift in materialized artifact:
- INF_D_08 `nmec_nmnc_nna.json#hh_lifecycle[].household_id` → INT
- INF_D_04 `partner_analytics_*.json#hh_lifecycle[].household_id` → STRING

Empirical: materialized artifact has `"household_id": "101"` (string). FE doesn't compute on household_id (only consumes advisor_key + first_trade_date + aua), so runtime tolerates the drift. Fix: change type to `number | string` to silence TypeScript strict-mode.

### Empirical bucketing verification

After chain materialization (terminal ~18:25Z), empirical S3 fetch + jq:

```
$ jq '[.hh_lifecycle[] | select(.first_trade_date >= "2026-04-01" and .first_trade_date <= "2026-06-30")] | {count: length, nmnc_aua: (map(.aua) | add)}' partner_analytics_quarterly.json
{
  "count": 9,
  "nmnc_aua": 3654733.55
}
$ jq '[.hh_lifecycle[] | select(.first_trade_date >= "2026-01-01" and .first_trade_date <= "2026-12-31")] | {count: length, nmnc_aua: (map(.aua) | add)}' partner_analytics_quarterly.json
{
  "count": 18,
  "nmnc_aua": 9129135.99
}
```

Andrew's "$5M typical / $20M anomaly" framing **empirically confirmed**:
- Per-quarter cohort: $3.6M Q2'26, $5.7M Q3'25 (firm-wide range $3-6M)
- Rolling-365d sum across 4 partial cohorts: $20M (the bug)

### Empirical scope reduction — orphan-component discovery

Brief's projected 5-site consumer fan-out reduced empirically to **1 wired site**:

| Site | Status | Reason |
|------|--------|--------|
| `PartnerAnalytics.tsx` | REWIRED ✓ `95b67df2` | Donut + all-period bars; rolling-365d last-bar segment-patch REMOVED |
| `DistributionTab.tsx` | SKIPPED | NMNC references are color/label only (CATEGORY_ALT mapping, display strings); NOT a data consumer |
| `AdvisorsTab.tsx` | SKIPPED | Only `PALETTE.nmncGreen` color reference; NOT a data consumer |
| `AUACompositionChart.tsx` | ORPHAN — no mount | Grep `<AUACompositionChart` returns ZERO matches |
| `HeaderMetrics.tsx` | ORPHAN — no mount | ClientsTab imports `getHeaderMetrics` fetcher but never renders the component |

**~3-5h sizing → ~70min actual** because of orphan-component analysis catching the scope reduction.

**Out-of-scope flags banked** for future Andrew/COO call:
- `AUACompositionChart.tsx` is fundamentally rolling-12M by design; needs redesign vs remove decision if ever revived
- `HeaderMetrics.tsx` orphan; FE-bucket YTD via DS~D Q5 option (a) if ever revived

---

## Memory entries authored

| Entry | Content |
|-------|---------|
| `feedback_react_query_cache_poisoning_from_deploy_window.md` | Reactive post-mortem of the URL-decoupling class (`cb62f069` anchor) |
| `feedback_query_key_url_decoupling_class.md` | Forward-looking design constraint unifying URL-axis + chain-axis decoupling pathologies; cross-linked to bidirectional-translator-pattern, audits-underspecify, coo-routing-consumer-path-grep-first |

Plus 4 earlier in the session arc (this session block did not author them but referenced):
- `feedback_audit_grep_scope_completeness.md`
- `feedback_audit_grain_consistency.md`
- `feedback_semantic_split_over_audit_collapse.md`
- `feedback_audits_underspecify_by_default.md`

---

## Cross-pod orchestration

**MCP threads spawned this session block:**
- COO: 5 status MCPs + 1 sequencing question (Phase 2a Q1/Q2/Q3) + 1 dispatch ack
- DS~A: 0 (handed off Issue #1 + #5 Part B routing; no direct MCP)
- DS~C: 0 (Phase 1.2 led by COO routing; DE follow-on on Issue #3 cost_basis was FE-adapter not DS gap)
- DS~D: 3 (RAVC1 ACK for NMCOHT schema-lock, design clarification Q on timeseries_chart.json, foundation status)
- CTO: 2 (ratification ask for ADHC_FECACHE_COHERENCE design + Phase 2b courtesy routing of v0.6 tool spec PRD)
- AE 0.7: 0 (Phase 1.3 L@E rewrite trace was AE lane; DE grep evidence corrected their scope-narrow probe)

**Outbound RAVC1 acks for:** Phase 2 consumer-path verify (~5min); NMCOHT schema-lock async; ADHC_FECACHE_COHERENCE.001 TO-001 Path A context-switch.

---

## Session ship summary

**Portal DEV (7 commits):**
1. `1dd406f0` — Issue #2 fee-cascade adapter is_fee_paying pass-through
2. `ec1e4688` — Issue #3 cost_basis tax_exposure pass-through (sibling adapter-omission)
3. `d0bbc856` — Phase 2a Conservative (14 P1 callsite refetchOnMount drops)
4. `dcab7fe6` — NMCOHT foundation (HhLifecycleRow + nmncBucketing helpers)
5. `95b67df2` — NMCOHT PartnerAnalytics rewire (donut + all-period bar bucketing Design B)
6. `a40d2595` — NMCOHT household_id type drift (number | string)
7. `120df453` — ADHC_FECACHE_COHERENCE.001 categorical (5-file atomic; 270 LOC)

**Workspace CLOUD (4 docs commits):**
1. `4aa5e2948` — 5-surface Inflection survey brief
2. `ebce828ac` — FE-cache freshness audit brief (179 LOC; v0.6 ADHC_COMPIL_V4 input)
3. `b0220e9e9` → `bde4cbd13` → `307b1a3d3` — ADHC_FECACHE_COHERENCE v0.1 → v0.2 → v0.2.1
4. `e70fb243f` (earlier session block) — Snapshot Segment Analytics interval gaps brief

**Wall time:** ~6h. Sizing-vs-actual sustained pod 4 5-10× under across multiple ships (Phase 2a ~28min vs ~30min; ADHC_FECACHE_COHERENCE ~50min vs ~1-1.5h; NMCOHT ~70min vs ~3-5h).

---

## Bench-state continuity (end-of-session-block)

**Shipped + closed:**
- ✅ Phase 2a Conservative `d0bbc856`
- ✅ Issue #2 fee-cascade `1dd406f0`
- ✅ Issue #3 cost_basis `ec1e4688`
- ✅ Issue #5 routing correction (COO ratified FE-cache class)
- ✅ NMCOHT foundation + rewire + type drift `dcab7fe6` + `95b67df2` + `a40d2595`
- ✅ ADHC_FECACHE_COHERENCE.001 categorical `120df453`
- ✅ Brief v0.2.1 `307b1a3d3` (canonicalize-ready for CTO `git mv`)

**Awaiting external action:**
- 🟡 CTO `git mv` `docs/briefs/arch_proposal_adhc_fecache_coherence_20260514.md` → `docs/architecture/ADHC_FECACHE_COHERENCE.md` (canonicalize commit)
- 🟡 DT/AE deploy-window coordination on portal/DEV → server promote (bundles `1dd406f0` + `ec1e4688` + `d0bbc856` + NMCOHT chain + `120df453` per COO 17:53Z)
- 🟡 Andrew empirical verify (Peter Lee Q2'26 = $4.2M post-deploy; $202M Monthly/Quarterly divergence not reproducible post-buster-bump)

**Opportunistic / non-blocking:**
- 🟡 Stale-stub audit pass through `getPlatinumAdvisorSummaryStaticInflection` (P3; opportunistic next-touch)
- 🟡 4 DS-side `data_as_of` emit-additions (`AdvisorNnaClientsResponse` / `ConcentrationResponse` / `AdvisorDrilldownSummary` / `InflecTimeseriesChartResponse`) — COO authoring lane
- 🟡 v0.6 `comp-validate fe-cache-freshness <queryKey>` PRD — CTO ratchet queue (weeks-out)
- 🟡 INFGRO.006 MAX-window TWR re-enable (long-standing pending; blocked on DS coverage)

---

## Class-of-bug observations (banked + outbound)

**Three distinct bug-class observations surfaced in one session:**

1. **Adapter-omission class** (Issues #2 + #3) — TS-optional destination field + stale `// DS gap` comment + outdated stub → silent breakage. Two siblings in one file in one session. Hot zone in `getPlatinumAdvisorSummaryStaticInflection`.

2. **queryKey-URL decoupling class** (`cb62f069` + `120df453`) — queryKey doesn't see URL-construction logic OR chain-emission boundary. Two parallel latent-bug surfaces, same root pathology. Memory entry `feedback_query_key_url_decoupling_class.md` captures the unifying forward-looking constraint.

3. **Same-semantic-different-name pathology** (CTO 18:00Z banking note) — hit 3 times today across distinct surfaces:
   - Wire-protocol divergence at L@E (`?firm=` vs `?firmId=`)
   - FE-cache field aliases (`data_as_of` / `as_of_date` / `snapshot_date`)
   - Generalized wire-boundary normalizer pattern
   - CTO routed COO to author `feedback_wire_boundary_normalizer_pattern.md` generalizing the bidirectional-translator-pattern

— 0.4.0_DE_ClientPlatform
