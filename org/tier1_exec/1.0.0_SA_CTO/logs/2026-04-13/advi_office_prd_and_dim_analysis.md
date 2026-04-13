# CTO Session - ADVI_OFFICE PRD + Office Dim Analysis

**Agent:** 1.0.0_SA_CTO
**Date:** 2026-04-13
**Project:** ADVI_OFFICE

---

## Objective

Register the ADVI_OFFICE project, write the PRD for adding OFC as a third cohort
dimension on Segment Analytics (Distribution tab), and run a preliminary dim logic
analysis to establish how relationships map to offices under competing resolution rules.

---

## Work Completed

### 1. Compiler Tool Pass (PRD Research)

Ran before writing any PRD section:

- `comp-blast D_01.partner_analytics` — no tracked downstream consumers; D_04 pass-through
  is hardcoded. Changes to D_01 are isolated to `partner_analytics_{gran}.json`.
- `comp-blast DistributionTab` — 8 downstream nodes (4 endpoints x opal-partners-data).
  OFC is additive; no breakage risk.
- `comp-pipescript io D_01` — reads `account_team`, canonical NNA, acct_dim. Writes
  `gold/artifacts/partner_analytics/header_metrics_{gran}.json`.
- `comp-pipescript io D_00b` — reads `account_team`, `client_performance`,
  `accounts_dimension`. Writes `gold/artifacts/timeseries_chart.json` → D_04.
  Already has `_build_advisor_view()`. `_build_office_view()` is a direct parallel.
- `comp-pipescript io D_04` — pure pass-through for both artifacts. No D_04 changes needed.
- Manual read of `DistributionTab.tsx` L314: `CohortOption = 'geo' | 'adv'`, confirmed
  all branching patterns that need an `=== 'ofc'` arm.
- Manual read of `types.ts` L449: `PartnerAnalyticsBaseView`, `NnaPeriodView`,
  `CumulativeChartViewMode` — all must gain `'ofc'`.

### 2. Office Mapping Cache Review

Reviewed:
- `data/black_diamond/config/office_mapping/advisor_registry_lusha_office_bridge_clean.csv`
  — 178 advisors, 10 resolved offices, 13 unresolved names (all non-architect), 0 unresolved
  architects.
- `data/black_diamond/config/office_mapping/README.md` — dim logic specification.
- `data/black_diamond/config/office_mapping/relationship_role_office_assignments_long_clean.csv`
  — 8,857 rows, 2,743 unique relationships, 5 roles, max 1 advisor per relationship+role.

Confirmed offices: Arkansas, Atlanta, Austin, Charlotte, Dallas, Houston, Jacksonville,
Kansas City, Los Angeles, Minnesota.

### 3. PRD Written and Registered

- `docs/architecture/ADVI_OFFICE_PRD.md` (v1 + v2 with decisions)
- `org/projects/ADVI_OFFICE.json`
- `org/projects/REGISTRY.md` updated (ADVI_OFFICE added to Active table)
- `org/tier1_exec/1.0.0_SA_CTO/prompt.md` dashboard updated

Commits: `f3bf44ee` (v1 registration), `fda948b4` (v2 decisions resolved).

### 4. Preliminary Dim Analysis (Python, local parquet + CSV data)

Ran three passes against `relationship_role_office_assignments_long_clean.csv`:

**Pass 1 — Full resolution breakdown (architect-dominant):**

| Resolution Step | Count | % |
|---|---|---|
| Lead pair match (arch == impl) | 993 | 36.2% |
| Architect only, no implementor | 478 | 17.4% |
| Architect wins, impl disagrees | 763 | 27.8% |
| Implementor only, no architect | 407 | 14.8% |
| Consultant fallback | 52 | 1.9% |
| Local ops fallback | 16 | 0.6% |
| Other (unresolved) | 34 | 1.2% |

**Pass 2 — Implementor as tiebreaker (Andrew requested for comparison):**

Flipping the 763 Tier-2b disagreements to implementor meaningfully rehabilitates Houston
(16 → 239), Charlotte (14 → 149), Kansas City (35 → 123) — because Austin/Dallas architects
have large implementor populations in those cities.

**Pass 3 — Yang confirmation: architect-dominant is correct.**

Andrew confirmed that Yang's logic (and the original task order) specifies architect as the
authoritative dim. Implementor is only used when no architect is present at all. The
tiebreaker question was explored but resolved in favor of architect primacy.

### 5. Final Dim Rule (Locked)

```
1. If architect_office == implementor_office (both present, agree): use that office
2. If architect_office present, implementor absent or disagrees:    use architect_office
3. If architect absent, implementor_office present:                 use implementor_office
4. If both absent: consultant -> local_ops -> additional_advisor -> Other
5. All unresolved accounts fold into "Other" bucket (not excluded; canonical AUA preserved)
```

### 6. Final Office Distribution (architect-dominant)

| Office | Relationships | % |
|---|---|---|
| Austin | 1,419 | 51.7% |
| Dallas | 566 | 20.6% |
| Los Angeles | 208 | 7.6% |
| Arkansas | 182 | 6.6% |
| Jacksonville | 139 | 5.1% |
| Atlanta | 130 | 4.7% |
| Kansas City | 35 | 1.3% |
| Houston | 16 | 0.6% |
| Charlotte | 14 | 0.5% |
| Minnesota | 0 | 0.0% |
| Other | 34 | 1.2% |
| **Total** | **2,743** | |

Notable: Minnesota shows 0 relationships — Lincoln Rock is in the bridge CSV but has no
active relationships in relationship_team. Needs confirmation (new hire / inactive).

Houston and Charlotte being small (16 and 14) is correct under architect-dominant logic.
Those offices are primarily implementor-staffed under Austin/Dallas architects. Their AUA
rolls up to the architect's office, which is the intended behavior per Yang's framework.

---

## Decisions Made

| Decision | Resolution |
|---|---|
| Unresolved advisors | Fold into "Other" bucket — canonical AUA preserved exactly |
| Continuous AUA OFC | In V1 scope — D_00b emits `ofc` timeseries |
| ADV toggle | Stays — OFC added as third button; ADV removal is a future project |
| Tiebreaker on arch/impl disagree | **Architect wins** (Yang-consistent, original task order) |
| Implementor role | Only used when no architect present |
| Other/unresolved bucket | Named "Other" (not "Unassigned"); same gray as Top-9+Other |

---

## PRD Wave Structure (Final)

| Wave | Agent | Work |
|---|---|---|
| W1 | `0.4.0_DS_ClientPlatform` | D_01 OFC AUA snapshot + NNA view; D_00b OFC timeseries |
| W2 | `0.4.0_DE_ClientPlatform` | DistributionTab OFC toggle, donut, L1 advisor drill, Continuous |
| W3 | `0.6.0_AE_PartnerETL` | Upload dim CSV to S3; D_00b → D_01 → D_04 gold run; PROD |
| W4 | `0.4.0_DT_ClientPlatform` | Portal DEV → PROD deploy |

Sequencing note from `ADVI_OFFICE.json` (updated by COO): DS W6-003 (ADVI_REBORN) must
ship before DS starts ADVI_OFFICE W1.

---

## Compiler Tools

| Tool | Command | Result |
|---|---|---|
| `comp-blast` | `comp-blast D_01.partner_analytics` | PASS. No tracked downstream; changes isolated to artifact. |
| `comp-blast` | `comp-blast DistributionTab` | PASS. 8 downstream nodes; OFC additive, no breakage. |
| `comp-pipescript io` | `comp-pipescript io D_01` | PASS. account_team + canonical NNA in read set. |
| `comp-pipescript io` | `comp-pipescript io D_00b` | PASS. account_team + client_perf in read set; _build_advisor_view pattern confirmed. |
| `comp-pipescript io` | `comp-pipescript io D_04` | PASS. Pure pass-through for both artifacts. |

---

## Open Items

- **Minnesota (Lincoln Rock)**: 0 relationships in BD data. Confirm active or inactive
  before DS builds the dim — if active, verify he appears in account_team.
- **PRD dim rule**: now explicitly architect-dominant. DS must implement accordingly and
  NOT use the implementor-tiebreaker path that was explored during analysis.
- **ADVI_OFFICE.json blocking note** confirms DS W6-003 must ship first.
