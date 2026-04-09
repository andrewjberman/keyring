# ADVI_49PUSH Phase 2: Cross-Surface Consistency Matrix

**Author:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-04-08
**Task Order:** ADVI_49PUSH.004 (Requirement 5)
**Status:** Framework complete -- Books columns filled; PartnerAnalytics/Distribution/Advisors columns pending .002/.003 deliverables

---

## Purpose

This matrix documents every metric that appears on more than one Advisor Intelligence surface, traces each instance to its gold source, and flags divergences where the same logical metric is computed from different scripts or aggregation paths.

The "numbers must tie" principle: if Advisor X's NNA appears on the Advisors tab leaderboard, the Distribution tab donut, the Books L2 summary, and the PartnerAnalytics ADV view, all four must ultimately derive from the same gold-layer aggregation.

---

## Gold Source Inventory (Scripts That Produce Shared Metrics)

| Script | Key Outputs | Metrics Produced |
|--------|------------|-----------------|
| D_00 | `employee_leaderboard.json`, `clients_tab.json`, `header_metrics.json`, `timeseries_chart.json` | Firm AUA, firm NNA, advisor NNA/AUA/growth, client count, advisor rolling flows |
| D_01 | `partner_analytics/header_metrics_{gran}.json` | Firm AUA by cohort, NNA by geo/advisor/segment, distribution histograms |
| D_02 | `advisors/{id}/book.json`, `clients/{id}/detail.json` | Per-advisor AUA/NNA/client count, per-client AUA, fee summaries |
| C_08 | `advisor_fee_efficiency.json`, `advisor_fee_detail/{date}.parquet` | Per-advisor NNA, commission, AUA, fee yield (windowed) |
| C_07 | `account_team.parquet` | Advisor-to-account resolution (used by D_00, D_02, C_08) |

**Critical dependency:** D_00, D_01, D_02, and C_08 all read `account_team.parquet` from C_07 for advisor name resolution. This is the shared lookup that should ensure name consistency, but each script aggregates independently.

---

## Cross-Surface Consistency Matrix

### Legend

- **Source:** The gold script + field that produces this metric on this surface
- **Aggregation:** How the metric is computed (direct sum, weighted avg, etc.)
- **SAME:** Gold source matches across surfaces
- **DIVERGENT:** Different gold source or aggregation path -- requires resolution
- **PENDING .002/.003:** Cells that need input from PartnerAnalytics/Distribution/Advisors tab audits

---

### Metric: Firm Total AUA

| Surface | Current Gold Source | Aggregation Path | Divergent? |
|---------|-------------------|-----------------|-----------|
| PartnerAnalytics header | D_01: `header_metrics_{gran}.json` -> `views.nna.metrics.aua` | PENDING .002 | PENDING |
| Distribution tab | D_01 (shared with header) | PENDING .002 | PENDING |
| Advisors tab (leaderboard sum) | D_00: `employee_leaderboard.json` -> sum of `entries[].managed_aua` | Sum of split-weighted managed_aua per advisor | PENDING .003 |
| Books N1 headline | D_00: `clients_tab.json` -> `headline.total_aua` | Direct from accounts_dimension aua_current sum | **REFERENCE** |

**Analysis:** D_00's `clients_tab.json` sums AUA from `accounts_dimension` (A_00) -- this is the direct, unweighted, un-split total. D_00's `employee_leaderboard.json` sums managed_aua (split-weighted) per advisor. These are intentionally different: total AUA vs sum of advisor-managed AUA. The leaderboard sum will be LESS than total AUA if any accounts lack advisor assignments (split < 100%).

D_01's header_metrics computes AUA from `client_performance.parquet` (C_02) -- needs .002 verification.

**Resolution:** D_04 should use `clients_tab.json` `headline.total_aua` (D_00) as the canonical firm AUA for all platinum surfaces. If D_01 uses a different source, D_04 must override with the canonical value.

---

### Metric: Firm NNA YTD

| Surface | Current Gold Source | Aggregation Path | Divergent? |
|---------|-------------------|-----------------|-----------|
| PartnerAnalytics header | D_01: `header_metrics_{gran}.json` -> `views.nna.metrics.nna_ytd` | PENDING .002 | PENDING |
| Distribution tab | D_01 (shared with header) | PENDING .002 | PENDING |
| Advisors tab (leaderboard sum) | D_00: `employee_leaderboard.json` -> sum of `entries[].nna` (ytd window) | Sum of C_08's split-weighted nna_txn per advisor | PENDING .003 |
| Books N1 (not directly shown) | Not rendered at N1 -- only per-advisor NNA in fee scatter | N/A | N/A |

**Analysis:** D_00's employee leaderboard NNA now comes from C_08 advisor_fee_detail (transaction-classified nna_txn, split-weighted). D_01's NNA source needs .002 verification. D_01 reads canonical NNA directly; D_00 reads C_08's advisor-attributed output. These may diverge due to split weighting and advisor assignment gaps.

**Resolution:** For firm-level NNA YTD, use D_00's `clients_tab.json` or D_01's `header_metrics` (both read canonical NNA from C_01). The leaderboard sum of advisor NNA is intentionally different (split-weighted, excludes unassigned accounts).

---

### Metric: Advisor {id} AUA

| Surface | Current Gold Source | Aggregation Path | Divergent? |
|---------|-------------------|-----------------|-----------|
| PartnerAnalytics ADV donut | D_01: `header_metrics_{gran}.json` -> `views.adv.donut.segments[].value` | PENDING .002 | PENDING |
| Advisors tab leaderboard | D_00: `employee_leaderboard.json` -> `windows.{w}.entries[].managed_aua` | Split-weighted: `aua_current * split_pct / 100`, aggregated from C_08 advisor_fee_detail latest day | PENDING .003 |
| Books L2 summary | D_02: `advisors/{id}/book.json` -> `summary.total_aua` | Sum of all account aua_current for accounts where this advisor has ANY role | **REFERENCE** |
| Books N1 fee scatter | C_08: `advisor_fee_efficiency.json` -> `advisors[].aua` | Split-weighted managed_aua from latest fee_detail snapshot | SAME as leaderboard |

**DIVERGENCE IDENTIFIED:**

1. **D_02 advisor AUA** = total AUA of all accounts where this advisor has a role. NOT split-weighted. If an advisor is architect on a $10M account with 60% split, D_02 shows $10M.
2. **D_00/C_08 advisor AUA** = managed_aua = `aua_current * split_pct / 100`. For the same account, shows $6M.

This is a **semantic divergence, not a bug**. D_02 shows "book size" (total AUA of accounts this advisor touches). D_00/C_08 shows "managed share" (AUA weighted by split).

**Resolution:** Both are valid views. D_04 platinum should:
- `platinum/advisors/{id}/summary.json` -> `book.total_aua`: D_02's total (book size) for the advisor detail page
- `platinum/firm/dashboard.json` -> `employee_leaderboard[].managed_aua`: C_08's split-weighted (for fair comparison across advisors)
- `platinum/firm/dashboard.json` -> `fee_efficiency[].aua`: C_08's managed_aua (matches scatter dot size)

Document this distinction in the platinum schema spec.

---

### Metric: Advisor {id} NNA YTD

| Surface | Current Gold Source | Aggregation Path | Divergent? |
|---------|-------------------|-----------------|-----------|
| PartnerAnalytics ADV donut | D_01: PENDING .002 | PENDING | PENDING |
| Advisors tab leaderboard | D_00: `employee_leaderboard.json` -> `windows.ytd.entries[].nna` | Split-weighted nna_txn from C_08 advisor_fee_detail | PENDING .003 |
| Books L2 summary | D_02: `advisors/{id}/book.json` -> `nna.ytd` | Likely from canonical NNA, NOT split-weighted | **CHECK** |
| Books N1 fee scatter | C_08: `advisor_fee_efficiency.json` -> `windows.ytd.advisors[].nna` | Split-weighted nna_txn | SAME as leaderboard |

**DIVERGENCE RISK:**

D_02's advisor NNA may use a different calculation than C_08's split-weighted nna_txn. D_02 reads NNA directly for relationship aggregation; C_08 applies split weighting.

**Resolution:** D_04 should use C_08's windowed NNA (split-weighted, transaction-classified) as the canonical advisor NNA for all platinum surfaces where advisors are compared. D_02's relationship-aggregated NNA is valid for the advisor's book detail view (L2) but should not be compared against leaderboard rankings.

---

### Metric: Advisor {id} Growth %

| Surface | Current Gold Source | Aggregation Path | Divergent? |
|---------|-------------------|-----------------|-----------|
| Advisors tab leaderboard | D_00: `employee_leaderboard.json` -> `entries[].growth_pct` | Computed from AUA change: `(current - prior) / prior * 100` | PENDING .003 |
| Books N1 fee scatter | C_08: `advisor_fee_efficiency.json` -> NOT directly in output | Not in C_08 output -- scatter uses nna/commission/pctile, not growth% | N/A |

**Analysis:** Growth % only appears on the Advisors tab leaderboard (as gradient bar cards). The fee efficiency scatter does NOT render growth %. The scatter color represents efficiency_pctile (commission/nna ratio), not growth.

**Resolution:** Single source (D_00). No cross-surface divergence for this metric.

---

### Metric: Client {rel_id} AUA

| Surface | Current Gold Source | Aggregation Path | Divergent? |
|---------|-------------------|-----------------|-----------|
| Books L2 client list | D_02: `advisors/{id}/book.json` -> `clients[].aua` | Per-client total AUA from accounts_dimension | **REFERENCE** |
| Books L3 headline | D_02: `clients/{id}/detail.json` -> `headline.total_aua` | Same source as L2 | SAME |
| Books N1 clients tab | D_00: `clients_tab.json` -> `clients[].total_aua` | From accounts_dimension aggregated to relationship | SAME |

**Analysis:** All client AUA values trace to `accounts_dimension_latest.parquet` (A_00/B_01), summed by relationship_id. D_00 and D_02 both read this artifact. No divergence.

**Resolution:** Single canonical source. No action needed.

---

### Metric: Firm Client Count

| Surface | Current Gold Source | Aggregation Path | Divergent? |
|---------|-------------------|-----------------|-----------|
| PartnerAnalytics header | D_01: PENDING .002 | PENDING | PENDING |
| Books N1 headline | D_00: `clients_tab.json` -> `headline.client_count` | Count of unique relationship_ids with AUA > 0 | **REFERENCE** |
| Advisors tab (sum of per-advisor) | D_00: `employee_leaderboard.json` -> sum of `entries[].client_count` | Sum of per-advisor client counts | **DIVERGENT** |

**DIVERGENCE IDENTIFIED:**

Sum of per-advisor client counts will EXCEED firm client count if any client has multiple advisors (e.g., architect + implementor on same account, different advisors). Each advisor counts the client, but the firm counts the client once.

**Resolution:** This is expected behavior. The firm client count (D_00 `clients_tab.json`) is authoritative. Per-advisor client counts include shared clients. D_04 platinum should use:
- `platinum/firm/dashboard.json` -> `headline.client_count`: from `clients_tab.json` (unique relationships)
- `platinum/firm/dashboard.json` -> `employee_leaderboard[].client_count`: per-advisor count (may include overlaps)

---

### Metric: Advisor Client Count

| Surface | Current Gold Source | Aggregation Path | Divergent? |
|---------|-------------------|-----------------|-----------|
| Advisors tab leaderboard | D_00: `employee_leaderboard.json` -> `entries[].client_count` | Count of unique relationship_ids where advisor has role | PENDING .003 |
| Books L2 summary | D_02: `advisors/{id}/book.json` -> `summary.client_count` | Count of unique relationship_ids in book | **CHECK** |

**Analysis:** Both D_00 and D_02 count unique relationship_ids for the advisor. D_00 uses C_07's account_team -> relationship mapping. D_02 uses the same lookup. Should be identical.

**Resolution:** Verify in .003 audit. If both trace to C_07 account_team, they are identical.

---

## Divergence Summary

| # | Metric | Surfaces | Divergence Type | Resolution |
|---|--------|----------|----------------|------------|
| 1 | Advisor AUA | Leaderboard vs Books L2 | Semantic: managed_aua (split-weighted) vs total_aua (un-split) | Both valid. Document distinction in platinum schema. Use split-weighted for cross-advisor comparison, total for book detail. |
| 2 | Advisor NNA YTD | Leaderboard vs Books L2 | Likely: split-weighted (C_08) vs relationship-aggregated (D_02) | Use C_08 split-weighted for rankings. D_02 for book detail. |
| 3 | Firm Client Count | N1 headline vs leaderboard sum | Expected: unique count vs per-advisor sum (overcounts shared clients) | Not a bug. Both are correct at their level. |

---

## Pending Cells (Awaiting .002 and .003 Deliverables)

The following matrix cells require input from the PartnerAnalytics/Distribution audit (.002) and Advisors tab audit (.003):

| Metric | Missing Surface | Needed From |
|--------|----------------|------------|
| Firm Total AUA | PartnerAnalytics header, Distribution tab | .002: What does D_01 `header_metrics` use as AUA source? |
| Firm NNA YTD | PartnerAnalytics header, Distribution tab | .002: Does D_01 NNA match D_00/C_08 NNA? |
| Advisor AUA | PartnerAnalytics ADV donut | .002: Does D_01 ADV view use managed_aua or total_aua? |
| Advisor NNA YTD | PartnerAnalytics ADV donut | .002: How does D_01 compute per-advisor NNA? |
| Advisor Growth % | Advisors tab leaderboard | .003: Verify computation formula |
| Advisor Client Count | Advisors tab leaderboard | .003: Verify uses C_07 lookup |
| Firm Client Count | PartnerAnalytics header | .002: Does D_01 report client count? |

---

## Platinum Canonical Source Assignments

For each metric, the canonical platinum source that ALL surfaces should read:

| Metric | Canonical Gold Source | Canonical Platinum Path | Rationale |
|--------|---------------------|------------------------|-----------|
| Firm Total AUA | D_00 `clients_tab.json` -> `headline.total_aua` | `platinum/firm/dashboard.json` -> `headline.total_aua` | Direct sum from accounts_dimension, no split weighting |
| Firm NNA YTD | D_00 `clients_tab.json` or D_01 canonical NNA | `platinum/firm/dashboard.json` -> `headline.nna_ytd` | Transaction-classified NNA from C_01 canonical |
| Advisor Managed AUA | C_08 `advisor_fee_efficiency.json` -> `.aua` | `platinum/firm/dashboard.json` -> `employee_leaderboard[].managed_aua` | Split-weighted, used for cross-advisor comparison |
| Advisor Book AUA | D_02 `book.json` -> `summary.total_aua` | `platinum/advisors/{id}/summary.json` -> `book.total_aua` | Full book size, for advisor detail view |
| Advisor NNA (windowed) | C_08 `advisor_fee_efficiency.json` -> `windows.{w}.advisors[].nna` | `platinum/firm/dashboard.json` -> `fee_efficiency.windows.{w}[].nna` | Split-weighted nna_txn, transaction-classified |
| Client AUA | D_02 `detail.json` -> `headline.total_aua` | `platinum/clients/{rel_id}/summary.json` -> `detail.total_aua` | From accounts_dimension, no ambiguity |
| Client Count (firm) | D_00 `clients_tab.json` -> `headline.client_count` | `platinum/firm/dashboard.json` -> `headline.client_count` | Unique relationship count |
| Fee Efficiency (per advisor) | C_08 -> all fields | `platinum/firm/dashboard.json` -> `fee_efficiency` | C_08 is sole producer, no divergence risk |
| Fee Role Breakdown (per advisor) | D_02 -> `fee_summary` | `platinum/advisors/{id}/summary.json` -> `fee_summary` | D_02 reads A_02 + C_08 detail |
| Fee Summary (per client) | D_02 -> `fee_summary` | `platinum/clients/{rel_id}/summary.json` -> `fee_summary` | D_02 reads A_02 |

---

## Key Principle: Why Divergences Exist

The divergences identified above are NOT bugs. They reflect a legitimate architectural choice:

- **Split-weighted metrics** (C_08, D_00 leaderboard): Used when comparing advisors fairly. An advisor managing 60% of a $10M account gets credit for $6M, not $10M.
- **Total/book metrics** (D_02): Used when showing the advisor their own book. The advisor sees ALL the AUA they touch, regardless of split.

The platinum layer resolves this by:
1. Using split-weighted metrics for ALL cross-advisor comparisons (leaderboard, scatter, rankings)
2. Using total metrics for individual advisor/client detail pages
3. NEVER mixing the two in the same view

This is the "numbers tie" guarantee: within any single view, all numbers are internally consistent because they come from the same platinum file, which enforces one aggregation path.
