# ADVI_HDRSPL.002 + .003 — ADVI header restructure + Segment Analytics local toggles (bundled)

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-04-13 (ET)
**Commit:** portal DEV `4cb34a2`
**Status:** code landed; `/frontend-dev` pass outstanding pending submodule bump.

## Summary

Bundled Waves 2 + 3 into a single commit per CTO's `<cross_domain_coordination><none/></cross_domain_coordination>` and Andrew's GO message allowing DE discretion. Splitting would have left Segment Analytics without Window/Interval controls between commits.

### Wave 2 — page header restructure

- `AdvisorIntelligence.tsx`: firm picker moved out of the `PartnerAnalytics` panel header to the page top-right (above the tab strip), rendered via `<PageSurfaceControl variant="solid-indigo" as="dropdown" />` (Wave 1 primitive). Internal users only, unchanged gate.
- `AdvisorIntelligence.tsx`: `granularity` + `timeWindow` state removed from page root. Each panel now owns its own.
- Page-root `useQuery` for `getPlatinumPartnerAnalytics` reduced to a minimal fixed-quarterly fetch used only by the Data Source footer timestamp. Otherwise each panel fetches independently.
- `PartnerAnalytics.tsx`: added local `useState` for `granularity` + `timeWindow`, added own `useQuery` for `getPlatinumPartnerAnalytics`. Dropped `data`/`isLoading`/`granularity`/`onGranularityChange`/`timeWindow`/`onTimeWindowChange`/`selectedFirmId`/`onPartnerChange` props. Dropped in-panel firm picker block.

### Wave 3 — Segment Analytics local toggles

- `DistributionTab.tsx`: added local `useState` for `granularity` + `timeWindow`; own `useQuery` for `getPlatinumPartnerAnalytics` on panel-local key `['partner-analytics', granularity, firmOverride]`. React Query de-dupes with PartnerAnalytics' fetch when both happen to be at `quarterly`; diverging states trigger separate cache entries.
- Panel header toggle strip restructured to exact PRD order **Mode → Interval → Window → View** (with Cohort preceding as an orthogonal segmentation axis; PRD lists only the 4 named toggles — Cohort kept separately, positioned before Mode).
- Dropped `analyticsData`/`analyticsLoading`/`granularity`/`timeWindow` from `DistributionTabProps`.

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| 1 | Grep `timeWindow`, `granularity`, `selectedFirmId` across `portal/src/pages/AdvisorIntelligence/` | Confirmed page-root ownership at `AdvisorIntelligence.tsx:144,156` (matches CTO PRD evidence). |
| 1 | Read `PartnerAnalytics.tsx` + `DistributionTab.tsx` — inspected every prop usage | Verified lifting each into panel-local state does not cascade beyond the scoped changes. |
| 2 | `tsc --noEmit` | clean |
| 2 | `eslint` on 3 changed files | 0 errors, 10 pre-existing warnings (all `react-hooks/set-state-in-effect`, unrelated to this change; same count as before) |
| 3 | `/frontend-dev` closed-loop pass | **outstanding** — requires dev-server + submodule bump |

## Acceptance criteria — HDRSPL.002

| # | Criterion | Status |
|---|-----------|--------|
| 1 | Firm picker outside every `<Panel>` | page header flex row, outside Panel |
| 2 | Top-right, above tab strip, silver bg | `flex items-start justify-between` with picker in the pt-2 shrink-0 slot |
| 3 | Uses `<PageSurfaceControl variant="solid-indigo" as="dropdown" />` | yes (default variant is solid-indigo) |
| 4 | `timeWindow` + `granularity` local to PartnerAnalytics | moved |
| 5 | Firm change still propagates to both panels + all tabs | `selectedFirmId` still owned at page root; prop drilling preserved |
| 6 | No TS/ESLint errors | 0/0 |
| 7 | Compiler log entries | appended below |

## Acceptance criteria — HDRSPL.003

| # | Criterion | Status |
|---|-----------|--------|
| 1 | Panel header order Mode → Interval → Window → View | implemented with Cohort as a preceding axis (PRD does not list Cohort among the 4 named toggles) |
| 2 | `timeWindow` + `granularity` local to DistributionTab | new useState |
| 3 | Assets Overview window flip does NOT change Segment Analytics data | each panel fetches its own React Query key — independence by construction |
| 4 | Segment Analytics window flip does NOT change Assets Overview | same |
| 5 | Firm picker change propagates to both panels | `firmOverride` flows down unchanged |
| 6 | Segment Analytics fetches with its own (window, interval, firm) triple | own useQuery |
| 7 | No TS/ESLint errors | 0/0 |
| 8 | `/frontend-dev` visual test | outstanding |

## Outstanding

- `/frontend-dev` pass against the live DEV portal after the parent-repo submodule pointer is bumped to include `4cb34a2`. Items to verify:
  - Firm picker position (top-right, above tabs, on silver bg)
  - WCAG AA numeric contrast ratio for PageSurfaceControl (Wave 1 gate)
  - Panel independence: flipping Assets Overview Window 1Y→3Y does not change Segment Analytics chart; and vice versa
  - Toggle order in Segment Analytics header: Cohort, Mode, Interval, Window, View (left→right)
  - Firm change propagates to all tabs + both panels
- If Andrew wants Cohort inside the named strip, trivial move; current placement was my read of the PRD.
