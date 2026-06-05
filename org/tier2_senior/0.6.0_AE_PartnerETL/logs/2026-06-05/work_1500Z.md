# 0.6.0_AE_PartnerETL session log — 2026-06-05 work_1500Z (ADHC_GLDINC Phase 0 audit COMPLETE)

**archetype:** DIAGNOSE
**secondary_archetypes:** ANALYZE

## ADHC_GLDINC Phase 0 — bd-gold incrementalization audit (Andrew-direct, I LEAD)
Exploratory analysis-only (no pipeline changes, no ad-hoc runs). Doc: docs/briefs/bd-gold-incrementalization-audit-20260605.md (commit a82c67f39). RAVC2'd COO + CC CTO + 0.4.0.

METHOD: read the 14-phase validated DAG (gold_dispatch.sh) for the backbone; fanned out 3 general-purpose subagents (A+B / C / D groups) to classify all 27 scripts in parallel; synthesized.

ALL 27 CLASSIFIED: 8 CLEAN-APPEND (5 built), 12 INCREMENTAL-WITH-RECONCILE, 7 FULL-RECOMPUTE-INHERENT.

KEY FINDINGS:
- A_03.positions_cube (76GB hog, the reason R3 needs 128GB) is NOT inherent-aggregation — it's expand_pairs_to_daily() materializing the full pair-x-day cross-product (~300M rows) all-at-once. FIFO cumsum is per-(account,asset); build_single_date() already proves a cheap path. Incrementalizing it DROPS the memory floor below r6i.4xlarge (compounds R3) = the single highest-leverage prize.
- Hidden full-scan: load_flows_from_transactions() (C_01/C_02/C_03) reads the ENTIRE silver txn set every run regardless of date args = the low-risk P1 quick win.
- FRI floor (can't delta-reduce, only cheaper reads): firm aggregates/rankings/distributions D_00/D_00b/D_00c/D_01 + C_07 + C_05.
- Per-entity fan-out D_02/D_03/D_04 = dirty-entity-set incremental (rewrite only changed entities, not all ~8000/~5300 files).
- Template: C_06 already implements watermark+per-entity-merge incremental — replicate it.

HONEST READ: tiered hybrid, ~50-70% typical-night compute cut + a memory-floor structural drop, NOT 90%+ elimination. GREENLIGHT YES for build PRD, scoped P1(flow-loader)->P2(A_03 memory floor)->P3(D_02/D_04 fan-out)->P4(cumulative carry).

0.4.0_DS coordination (reconcile-correctness / data-semantics axis) held until 0.4.0 joins post-R2 (per COO); flagged in RAVC2.

## Other threads (holding)
- bd-gold R3: right-size applied (i-01003b03=r6i.4xlarge), validates tonight's nightly. Spot=follow-on design.
- demo-reclone3: ~33h, R8-safe, let-it-run, DS verifies on landing.
- inf-gold: RESOLVED under enforcer-v1.1.1 (threshold 3%->1%); de-prioritized to light <1%-3h backstop.

## Open / next
- Await COO greenlight-routing on the ADHC_GLDINC build PRD (offered to draft the P1 quick-win PRD).
- Tomorrow: validate the right-sized bd-gold nightly -> RAVC2.
- Monitor demo-reclone3 to completion -> R5 leak result -> RAVC2.
