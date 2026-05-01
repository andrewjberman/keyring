# Session Log — ADVI_49FRECN.001B + .001D — Missing Accounts + Phase 0 Consolidation

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-01
**Task Orders:** ADVI_49FRECN.001B (Slice B) + ADVI_49FRECN.001D (Phase 0 Consolidation)
**Status:** COMPLETE

---

## Summary

Executed Phase 0 Slice B and Phase 0 Consolidation (.001D) for the 49Financial reconciliation investigation. Identified root cause of 590 missing accounts (gold-layer scope restriction), confirmed CASE_A, produced Phase 1 TO recommendations, and merged all three slice findings into a final consolidated report.

Key finding: The BD feed is intact — all 6,611 accounts reach silver/allocations. Missing accounts are dropped by the gold pipeline because `C_03.account_performance` only processes accounts with investment positions in the positions cube. The dominant dollar bucket is C1: 60 recently-funded investment accounts (~$55.5M) whose positions elections have not yet been processed by BD.

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| comp-pipescript io | A_00 | OK — 1 read (external/silver), 1 write; no COLUMN GAPS |
| comp-pipescript io | D_00 | OK — 18 reads, 5 writes; no COLUMN GAPS |
| comp-trace | NNA_AUA_BY_ADVISOR | gold/views/nna_aua_by_advisor.parquet — D_00 line 844 |

---

## .001B Deliverables

### AC#1 — 49F-Side Reference Snapshot
Silver/allocations 2026-04-29 confirmed as 49F truth source per Andrew: 6,611 accounts, $1,730.79M. Andrew Q2-Q4 (per-advisor breakdown, AUA basis, non-investment scope) routed to CTO. Investigation proceeded without blocking on Andrew's confirmation.

### AC#2 — Set-Diff Result

| Bucket | Count | AUA |
|--------|-------|-----|
| MISSING_FROM_OPAL | **590** | **$62,413,805** |
| MATCHED | 6,021 | ~$1,597M |
| IN_GOLD_NOT_IN_SILVER | 11 | — |

### AC#3 — Root Cause (4 Buckets)

| Bucket | Count | AUA | Root Cause |
|--------|-------|-----|-----------|
| A: Non-investment types | 44 | -$579K | C_03 exclusion by design |
| B: No transaction history | 11 | $4.2M | Brand-new, onboarding lag |
| C1: Large new investment accounts | 60 | ~$55.5M | Positions cube lag |
| C2/C3: Dormant investment | 475 | ~$3.3M | No active positions |

CASE_A confirmed: $62.4M > $59.6M (3.59% × $1,657.87M). Zero valuation gap on matched accounts.

### AC#4 — Custodian Audit
P0 finding: NONE. All 6,611 silver accounts present in BD feed. Gap is entirely Opal-internal.

### AC#5 — Schwab C_01 Cross-Link
DISJOINT. Phase 6 C_01 = NNA attribution for in-pipeline accounts. 49FRECN = accounts absent from pipeline. Keep parallel.

### AC#6 — 49F-Side Columns Filled
Firm-level columns: 6,611 / $1,730.79M (silver) vs 6,025 / $1,657.87M (portal). Per-advisor pending Andrew Q3.

---

## .001D Deliverables

### AC#1 — Cross-Validation
DS~A's 579 count gap reconciles with DS~B's 590 set-diff: difference = IN_GOLD_NOT_IN_SILVER=11 (590 − 11 = 579). DS~C used DS~B's $62.4M figure (received via MCP). All slices consistent.

### AC#2 — Executive Summary
Inserted at top of `docs/architecture/49F_RECONCILIATION_2026-05-01.md`. Two paragraphs: (1) findings + CASE_A confirmation, (2) top 3 Phase 1 TOs by ROI.

### AC#3 — Unified Reconciliation Matrix
`## Reconciliation Matrix (Unified)` section added with firm-level (fully reconciled), per-account-type (partial fill from bucket data), per-advisor (pending Andrew), per-custodian (P0: none).

### AC#4 — Phase 1 TO Recommendations

| TO | Priority | Effort |
|----|----------|--------|
| ADVI_49FRECN.002 — C1 positions-cube expansion | P0 | 2-3d |
| ADVI_49FRECN.003 — Bucket A scope business rule | P0 | 0.25d |
| ADVI_49FRECN.004 — Dormant account lifecycle | P1 | 2d |
| ADVI_49FRECN.005 — 49F House advisor attribution | P1 | 0.5d |
| ADVI_49FRECN.006 — Custodian field enrichment | P2 | 2d |

### AC#5 — Open Questions
5 items in `## Open Questions` section: Bucket A scope, 3.59% vs 4.2% discrepancy, per-advisor mapping, AUA basis, E_25 dispatch.

---

## Files Modified

| File | Change |
|------|--------|
| docs/architecture/49F_RECONCILIATION_2026-05-01.md | Added executive summary + Slice B content (already in 9088aa2f8) + cross-validation + unified matrix + Phase 1 TOs + open questions |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_49FRECN.001B.ds-b-missing-accounts-and-49f-integration.md | Status: pending -> complete |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_49FRECN.001D.ds-b-consolidation-and-phase1-recommendations.md | Status: pending -> complete |
| org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-01/ADVI_49FRECN_001B_001D_missing_accounts_consolidation.md | This log |

**Note on Slice B commit:** Slice B content was committed in `9088aa2f8` (authored by 1.0.0_SA_CTO) alongside Slices A and C. .001D consolidated sections committed separately in this session with DS~B author.

---

## Next Steps

[CTO] Dispatch Phase 1 TOs per recommendations table. ADVI_49FRECN.002 (P0) and .003 (P0) are unblocked.

[DT/AE] Dispatch E_25.aua_decomposition_audit.py on EC2 (Open Question #5 — required for DS~C live data ACs).

[Andrew] Answers to Open Questions #1-4 needed before ADVI_49FRECN.003 verdict and per-advisor matrix fill.
