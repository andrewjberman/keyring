# 0.4.0_DE_ClientPlatform — Session Log 2026-06-09 (~2030Z)

**archetype:** IMPLEMENT

**Portal DEV commits:** `00f70f2d` (ADVI_PRTORG.04 cottonwood module)
**Workspace CLOUD commit:** (this log)

---

## Context

COO [DRIVE] dispatch received on session start: ADVI_PRTORG.04 — Cottonwood frontend module.
§5-A RESOLVED YES (Andrew 2026-06-09): Cottonwood gets an ADVI page structured in-pattern.
Gate: PRTORG.03 (AE serving route, opal-data-cot FIRM_CONFIG) must land + RAVC2 before
real Cottonwood JWT smoke is reachable.

## Work Completed

**Startup:** /watcher self-healed (fresh session, not registered → re-registered PID 27832,
Monitor armed b7ktcxf6k). LD-0157 confirmed: ZERO crons armed (event-driven). org/XXX.md
steps A-E complete. Inbox delivered COO DRIVE during startup.

**Compiler mandates (pre-code):**
- `comp-transform schema-check AdvisorIntelligence` → "Component not found" (tool expects
  component name, not page path; schema confirmed manually via direct-read of TenantLayoutConfig.ts
  + 49financial/inflection layout files). No MISSING fields for cottonwood — all fields in
  TenantLayoutConfig are optional or carry defaults; COTTONWOOD_LAYOUT populates every field
  explicitly per §3.3 zero-fall-through rule.
- `comp-cache collisions` → 5 existing shared-by-design keys (firm-leaderboard, partner-analytics,
  timeseries-overview, advisor-nna-canonical, advisor-book-view). All pre-existing intentional cache
  sharing across shared tabs. NO new collisions from cottonwood — cottonwood reuses the same
  `firmOverride`-keyed queries that all partners use via `_shared` tabs.

**Files created — `portal/src/pages/AdvisorIntelligence/_partners/cottonwood/`:**

| File | Change | Committed |
|------|--------|-----------|
| `constants.ts` | BD attribution constants (BD_SOURCE_ATTRIBUTION, BD_TOOLTIP_ATTRIBUTION, FIRM_DISPLAY_NAME, SMALL_ACCOUNT_THRESHOLD_USD) | Yes - portal DEV `00f70f2d` |
| `roles.ts` | CottonwoodRole type + COTTONWOOD_ROLE_KEYS/ROLES placeholder (v1 architect key; composition.enabled=false suppresses use) | Yes - portal DEV `00f70f2d` |
| `layout.ts` | COTTONWOOD_LAYOUT — full TenantLayoutConfig, OUTCOME-B reductions applied | Yes - portal DEV `00f70f2d` |
| `index.tsx` | CottonwoodAdvisorIntelligence component — Distribution-centric, PartnerAnalytics header + DistributionTab only (no TabNavigation, single surface) | Yes - portal DEV `00f70f2d` |

**Files modified:**

| File | Change | Committed |
|------|--------|-----------|
| `AdvisorIntelligence/index.tsx` | Import CottonwoodAdvisorIntelligence; add cottonwood to ALL_PARTNER_FIRMS + PARTNER_VIEWS | Yes - portal DEV `00f70f2d` |
| `_shared/hooks/useTenantLayout.ts` | Import COTTONWOOD_LAYOUT; add `cottonwood: COTTONWOOD_LAYOUT` to LAYOUTS registry | Yes - portal DEV `00f70f2d` |
| `portal/src/lib/firmAccess.ts` | Add `/advisor-intelligence` to cottonwood's FIRM_ALLOWED_PATHS set; cites §5-A + PRTORG.03 gate | Yes - portal DEV `00f70f2d` |

**OUTCOME-B layout reductions (§6.1, ADVI_PRTORG.md 2026-06-09):**
- `tabs.advisors.enabled: false` — no segmentable advisor dimension v1 (2-founder joint-coverage rep codes, 96% AUA)
- `tabs.books.enabled: false` — advisor drill has no targets without advisor dimension
- `tabs.distribution.cohorts: { geo: 'enabled', adv: 'disabled', ofc: 'disabled' }` — geo available, adv/ofc not applicable
- `tabs.partnerAnalytics.defaultViewMode: 'geo', allowedViewModes: ['aua','nna','geo']` — no adv view mode
- `roles.composition.enabled: false` — no role decomposition
- `routes.defaultTab: 'distribution', routes.tabs: [distribution only]`
- Every disabled field cites the ruling (§5-A + §6.1 OUTCOME-B 2026-06-09) per §3.3 standard

**Typecheck:** `bun run typecheck` EXIT 0 (portal DEV, post-commit).

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| comp-transform | `schema-check AdvisorIntelligence` | "Component not found" — confirmed manually via TenantLayoutConfig.ts + exemplar layout reads; no MISSING fields |
| comp-cache | `collisions` | 5 pre-existing shared-by-design collisions; 0 new from cottonwood |
| typecheck | `bun run typecheck` | EXIT 0 |

## Gate Status

**PRTORG.04 scaffold: COMPLETE (typecheck EXIT 0, firmAccess cottonwood includes /advisor-intelligence).**
**Final smoke (real Cottonwood JWT): GATED on PRTORG.03 (AE serving route) RAVC2.**
DT needs to push portal DEV `00f70f2d` to PROD (stacks behind prior DEV commits).

## Next Steps

- [AE/COO] PRTORG.03: serving route (FIRM_CONFIG cottonwood→opal-data-cot + sentinel flip + CF origin + OAI + rebuild + smoke) must land + RAVC2 before COT ADVI is reachable
- [DT] Push portal DEV `00f70f2d` → PROD once PRTORG.03 lands
- [DE/COO] Post-.03 RAVC2: real Cottonwood JWT smoke → verify ADVI page renders Distribution tab + PartnerAnalytics header
- [Future] When COT advisor dimension materializes: flip layout flags (advisors.enabled=true, books.enabled=true, composition.enabled=true, adv cohort enabled) — zero structural change needed per OUTCOME-B design intent

## Posture

WORKING: PRTORG.04 scaffold complete, awaiting PRTORG.03 (AE). Will monitor inbox for .03 RAVC2 signal.
