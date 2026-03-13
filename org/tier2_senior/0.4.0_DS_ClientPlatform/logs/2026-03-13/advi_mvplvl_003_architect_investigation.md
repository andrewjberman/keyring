# ADVI_MVPLVL 3a: Portfolio Group + Architect Data Quality Investigation — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-13
**Task Order:** `ADVI_MVPLVL.003.p3-architect-investigation`
**Data Sources:** `s3://opal-data-bd/gold/accounts_dimension_latest.parquet`, `s3://opal-data-bd/gold/views/nna_aua_by_advisor.parquet`

---

## Requirement 1: Portfolio Group Field Analysis

**Source:** `gold/accounts_dimension_latest.parquet` (9,781 accounts, 9,407 open)

| Metric | Value |
|--------|-------|
| Null/blank rate | 0.0% (every account has a portfolio_group) |
| Distinct values | 176 |

### Value Categories

| Category | Count | Examples |
|----------|-------|---------|
| **Institutional/Support** | 6 | `No Advisor` (2,548 accts), `49F Schwab AUM` (969), `Dallas Support` (304), `49 Private Wealth` (41), `49 Solutions` (24), `Centralized Client Ops` (7) |
| **"Local Ops" tagged** | 9 | `Lane Curry - Local Ops` (336), `Sam Owens - Local Ops` (305), `Alex Bright - Local Ops` (305), `Joseph Bolling - Local Ops` (242), etc. |
| **Person names** | 161 | The vast majority are individual person names — the same names that appear in the `architect` field |

### Qualitative Assessment

`portfolio_group` is **not** a team, office, or organizational unit. It is a **second person-name field** that largely mirrors `architect` but with inconsistent formatting, duplicates (e.g., `Joseph Bolling` and `Joseph Bolling - Local Ops` coexist), and operational tags. It appears to be a free-text assignment field in Black Diamond that was never normalized.

The 9 "Local Ops" entries suggest operations staff who handle account servicing, not architects managing client relationships. 3 of these names (`Erick Webb`, `Lane Curry`, `Sam Owens`) also appear as architects — indicating the same person has accounts under both their plain name and their "Local Ops" tag.

---

## Requirement 2: Architect AUA Distribution

**Source:** `gold/views/nna_aua_by_advisor.parquet` (latest date: 2026-03-11, 53 architects)

### Top 20 Architects by AUA

| Rank | Architect | Total AUA | Relationships | NNA (Cumulative) |
|------|-----------|-----------|---------------|-----------------|
| 1 | 49F House | $703,387,999 | 1,477 | $641,072,612 |
| 2 | Travis Penfield | $243,909,648 | 68 | $119,591,906 |
| 3 | Kyle Sims | $94,096,023 | 113 | $63,698,589 |
| 4 | David Farrell | $78,298,695 | 65 | $29,335,954 |
| 5 | Greg Rosner | $60,077,784 | 105 | $42,611,073 |
| 6 | Dean Dillenberg | $55,903,850 | 107 | $33,461,304 |
| 7 | Hunter Lloyd | $49,280,753 | 50 | $37,934,379 |
| 8 | Chase Bertrand | $42,988,315 | 99 | $38,131,667 |
| 9 | Matt Foxhall | $41,907,101 | 64 | $26,376,777 |
| 10 | Tim Rodgers | $40,264,106 | 123 | $28,027,362 |
| 11 | Ted Grant | $35,419,250 | 75 | $31,101,969 |
| 12 | Patrick Mundlin | $29,666,553 | 60 | $20,755,351 |
| 13 | Josh Henson | $26,406,212 | 92 | $16,238,629 |
| 14 | Sydney Cobb | $24,585,283 | 1 | $2,195,813 |
| 15 | Brandon Lanz | $23,189,714 | 40 | $16,721,786 |
| 16 | Zach Hawkins | $16,700,150 | 34 | $11,101,608 |
| 17 | Lincoln Rock | $11,890,574 | 32 | $6,688,519 |
| 18 | Boston Prachyl | $9,542,000 | 30 | $6,745,856 |
| 19 | Grant Boren | $8,768,362 | 23 | $5,207,579 |
| 20 | Liv Shin | $8,354,791 | 33 | $6,373,028 |

### Threshold Analysis

| Threshold | Architects | % of 53 |
|-----------|-----------|---------|
| >= $25M AUA | 13 | 24.5% |
| >= $10M AUA | 17 | 32.1% |
| >= $5M AUA | 21 | 39.6% |
| >= $1M AUA | 30 | 56.6% |

### Concentration

| Metric | Value |
|--------|-------|
| Top 10 share of total AUA | 85.9% |
| Top 20 share of total AUA | 97.8% |
| 49F House alone | 42.9% of total AUA ($703M / $1.64B) |

The long tail (architects 21-53) controls only 2.2% of AUA. Most are sub-$1M accounts — likely operational assignments, not client-facing architect relationships.

### Notable Anomaly: Sydney Cobb

Rank 14 by AUA ($24.6M) but only 1 relationship. This appears to be a single large institutional or family account assigned to an individual. It passes the AUA threshold but fails any relationship-count filter, suggesting it's not a traditional "architect book" pattern.

---

## Requirement 3: Portfolio Group -> Architect Alignment

### Many-to-Many Relationship

| Metric | Value |
|--------|-------|
| Distinct (architect, portfolio_group) pairs | 855 |
| Portfolio groups mapping to >1 architect | 147 / 176 (83.5%) |
| Architects mapping to >1 portfolio_group | 45 / 58 (77.6%) |

**The relationship is heavily many-to-many.** A single architect's accounts are spread across 7-46 different portfolio_groups (median ~20). A single portfolio_group is shared across multiple architects. This makes portfolio_group unusable as a hierarchical parent of architect.

### Name Overlap

29 of 58 architects have a portfolio_group that contains their own name as the top assignment. But the concentration is low — even the best cases only have 25-35% of their accounts under their own-name portfolio_group. The remaining 65-75% of their accounts are scattered across other person-name portfolio_groups.

This pattern is consistent with **portfolio_group being the operations support person** assigned to each account, not the architect. When an architect onboards a client, support staff from the "Local Ops" team is assigned, and the portfolio_group reflects whichever support person handled the account — not which architect owns the relationship.

### Conclusion

`portfolio_group` is not a team, office, or organizational unit. It is an **operations-level assignment field** — essentially "which support person services this account." It is not suitable as a group-by dimension for the Advisors Tab.

---

## Requirement 4: Recommendation

### 4A. Group-by Dimension: Do Not Use portfolio_group

`portfolio_group` fails as a hierarchical grouping dimension because:
1. It is person-name free-text, not an organizational unit
2. It has 176 distinct values — higher cardinality than `architect` (53)
3. It is many-to-many with architect (83.5% of PGs map to multiple architects)
4. No normalization is possible without a hand-curated mapping from 49 Financial

**Alternative grouping dimensions available in accounts_dimension:**

| Field | Suitability | Notes |
|-------|-------------|-------|
| `portfolio_group` | NO | Person names, many-to-many with architect, not an org unit |
| `local_relationship` | UNKNOWN | Not investigated — may have same quality issues |
| `manager` | UNKNOWN | Not investigated |
| `investment_strategy_name` | POSSIBLE | Strategy-level grouping (UST, ST, INT, LTC, LTA, etc.) — already used in ModelPortfolios. This is an asset-level grouping, not a people-level grouping. |

**Recommendation:** For MVP, abandon the Portfolio Group -> Architect -> Implementor hierarchy. Use a flat architect list with a true-architect filter (below) to reduce from 53 to ~19 meaningful entries. If Andrew/CTO confirms that 49 Financial has an internal team structure (e.g., regional offices, pods), a hand-curated mapping table can be loaded later as a dimension — but the gold layer does not currently contain this information.

### 4B. True Architect Filter: `is_true_architect`

**Proposed filter (dual-threshold):**

```
is_true_architect = (total_aua >= $5M) AND (num_relationships >= 5) AND (architect != '49F House')
```

| Filter Criterion | Purpose |
|-----------------|---------|
| `total_aua >= $5M` | Eliminates negligible-AUA operational assignments (33 architects fail this) |
| `num_relationships >= 5` | Eliminates single-account anomalies like Sydney Cobb ($24.6M, 1 relationship) |
| `architect != '49F House'` | Removes the institutional catch-all bucket |

**Result:** 19 true architects out of 53, controlling $884.5M AUA (53.9% of total, or **96.7% of total excluding 49F House**).

The 19 passing architects:

| Architect | AUA | Relationships |
|-----------|-----|---------------|
| Travis Penfield | $243.9M | 68 |
| Kyle Sims | $94.1M | 113 |
| David Farrell | $78.3M | 65 |
| Greg Rosner | $60.1M | 105 |
| Dean Dillenberg | $55.9M | 107 |
| Hunter Lloyd | $49.3M | 50 |
| Chase Bertrand | $43.0M | 99 |
| Matt Foxhall | $41.9M | 64 |
| Tim Rodgers | $40.3M | 123 |
| Ted Grant | $35.4M | 75 |
| Patrick Mundlin | $29.7M | 60 |
| Josh Henson | $26.4M | 92 |
| Brandon Lanz | $23.2M | 40 |
| Zach Hawkins | $16.7M | 34 |
| Lincoln Rock | $11.9M | 32 |
| Boston Prachyl | $9.5M | 30 |
| Grant Boren | $8.8M | 23 |
| Liv Shin | $8.4M | 33 |
| Michael Ihlenfeldt | $7.8M | 24 |

The remaining 33 entries (plus 49F House and Unassigned) would be suppressed from the Advisors Tab leaderboard, Top 3 highlights, and rolling flows — not deleted, just filtered from display.

### 4C. Implementation Path

This filter can be applied in two places:

1. **Script 09 / gold layer** (preferred): Add the filter when building the NNA GEO/ADV donut segments and the advisor_rolling_flows output. This reduces JSON payload size and ensures consistency across all consumers.

2. **Frontend** (fallback): Filter on `total_aua` and `client_count` in the leaderboard and rolling flows components. Quick to ship but duplicates business logic.

The filter thresholds ($5M AUA, 5 relationships) should be configurable constants in whatever layer implements them, not hardcoded in multiple locations.

### 4D. 49F House Treatment

`49F House` is the largest single entry at $703M AUA / 1,477 relationships. It is an institutional catch-all — accounts not assigned to a specific architect. Options:

1. **Suppress entirely** from Advisors Tab (current default for institutional)
2. **Show as a separate "Unassigned" summary** at the top of the Advisors Tab, distinct from the architect leaderboard
3. **Include as a pseudo-architect** in the leaderboard (distorts rankings due to scale)

Recommendation: Option 2 — surface it as an "Unassigned Book" summary panel so the $703M is not invisible, but keep it out of architect rankings.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| portfolio_group is unusable as a hierarchy | 176 values, many-to-many with architect (83.5%), person names not org units |
| Flat architect list with filter for MVP | No clean grouping dimension exists in gold layer; filter reduces noise |
| AUA >= $5M + rels >= 5 as true-architect filter | Captures 19 architects controlling 96.7% of non-institutional AUA |

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

All 4 requirements answered. No code changes made (research-only per task order constraints).

---

## Next Steps

1. **[1.0.0_SA_CTO] Review recommendation** — confirm flat-list approach for MVP; decide if a hand-curated team mapping is worth pursuing with 49 Financial
2. **[0.4.0_DE_ClientPlatform] Incorporate filter into Advisors Tab task orders** — true-architect filter at $5M AUA + 5 relationships for leaderboard, Top 3, and rolling flows
3. **[0.4.0_DS_ClientPlatform] If CTO approves backend filter** — implement `is_true_architect` in `08_build_nna_aua_by_advisor.py` or in `advisor_rolling_flows` publisher
