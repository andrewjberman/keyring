# CVO RAVC2 served-verify closed PASS + $83.5M unroled-AUA note grounded-to-source — 0.4.0_DS_ClientPlatform

**archetype:** VALIDATE

**Date:** 2026-07-06
**Task Order:** ADVI_TAGATTR.DS-1 (verification-close continuation of the 1324-1350Z session log)
**Status:** COMPLETE

---

## Objective

Close the CVO RAVC2 served-verify loop on the two DS artifacts (TAGATTR leaderboard + COTMVP client_directory) and answer CVO's one non-blocking analytical note (travis role slices sum to ~81% of his total_aua) with source grounding, not inference.

---

## Compiler Tools

No comp-* tools this window — it was a verification-answer grounding pass (source Read/grep on D_00c + a canonical-source S3 pull) to resolve CVO's $83.5M note. comp-validate has no addressable config for the served `platinum/firm/leaderboard.json` (D_00c/D_04 emit) — flagged in the 1324-1350Z log's Compiler Tools section — so the emit was grounded directly against source + the canonical `gold/canonical/role_aua/2026-07-01.parquet` artifact.

---

## Work Completed

### 1. CVO RAVC2 served-verify — BOTH PASS, closed both sides
CVO independently served-verified against the S3 artifacts (not my self-report):
- TAGATTR leaderboard.json (07-04 nightly, data_as_of 07-01): full-tagged NON-ADDITIVE confirmed (semantics + 0 split-weighted basis); travis total_aua 444,185,773.56 + architect 328,627,561.48 EXACT. **SEV1/ARCH-GATE-1 HOLDS**: the only firm-total-shaped field `windows.QTD.summary.total_aua = 1,734,420,935.53` matches the client-level bd dashboard.json EXACTLY, vs the naive advisor-sum $5,686,072,461 — firm total renders from the client artifact, not an advisor/role sum.
- COTMVP client_directory.json: 220 HH, sum $434,165,337.23 reconciles to cot dashboard + clients-tab-slim ($434,165,337.25, $0.02 float delta); 220 coherent across all 3 cot firm artifacts (real roster advance). Firm-sep verified.

### 2. CVO's $83.5M unroled-AUA note — ANSWERED source-grounded, RESOLVED (no cert gate)
CVO asked whether travis's role slices summing to $360.70M (~81% of his $444.19M total; ~$83.5M maps to no role slice) is intended or a tagging gap. Grounded answer:
- **PRE-EXISTING**: the OLD split-weighted role-sum was $358.34M vs the same ~$440M total — the ~$82M gap predates the full-tagging change (it moved composition, not the gap).
- **MECHANISM (source-confirmed)**: served `rd.aua` = the account_team melt `_build_at_role_slice(melted, full_tagged=True)` (D_00c L1091), per Andrew's "tagged -> full amount in that role" intent. The canonical role_aua override is **DISABLED** — `if False` at D_00c L1120-1132 per **CTO directive 20260420T144506Z (STAUDT.FIX1 Option A)**: role_aua/ is P1-SHADOW (`source_filter_stack=p1_shadow_equal_split...`), ~5x underscaled vs account_team, would drive fee_aua > tagged_aua for 146/152 advisors -> silent fee clip. Re-enable gated on the Option B plan (role_aua P2 production landing).
- **GROUNDED against the canonical artifact**: pulled `gold/canonical/role_aua/2026-07-01.parquet` — travis canonical role `aua` is a DIFFERENT additive allocation (sums to 444.19M; architect 413.5M), which is exactly why CTO disabled it as the source. Served architect 328.6M = the correct account_team-melt figure, NOT the disabled additive 413.5M.
- **CONCLUSION**: role_breakdown is the role-tagged NON-ADDITIVE subset — correctly not expected to reconcile to the dedup total. The gap = travis's AUA on accounts tagged to him without one of the emitted specific roles. Honest caveat given: source-confirmed the pre-existence + disabled-override + mechanism; did NOT account-level-enumerate the exact $83.5M composition (offered, not needed for cert).
- CVO accepted: "Note CLOSED, no gate. RAVC PASS, closed both sides."

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Ground the note to source (pull canonical role_aua + read the override block) before answering | Verify discipline / Rule 22: a "by-design" claim on a $83.5M discrepancy needs the mechanism source-confirmed, not asserted. Surfaced the CTO-disabled-override rationale as the actual cause. |
| Did not enumerate the exact $83.5M account composition | CVO confirmed non-gating; the design intent + disabled-override rationale close it. Offered enumeration if COO/CVO later want it. |

---

## Files Modified

None (verification + messaging only). No code/artifact change this window.

---

## Briefs Written

None — verification-close window.

---

## Blockers

None. All RAVC loops (COO / DE / CVO) closed PASS both sides.

---

## Current State

The TAGATTR.DS-1 + COTMVP.B-DS verification is fully closed: CVO served-verified both PASS (independent, S3-grounded), including the SEV1 ARCH-GATE-1 firm-total invariant (leaderboard `windows.QTD.summary.total_aua` == client-level dashboard, not an advisor-sum). CVO's role-slice-reconciliation note is resolved as by-design + pre-existing: served `role_breakdown.aua` is the account_team melt full-tagged subset (D_00c.portal_leaderboard.py:1091), the canonical role_aua override is CTO-disabled (L1120-1132, STAUDT.FIX1, role_aua in P1-shadow ~5x underscale), so slices correctly do not reconcile to the dedup total. No open DS items; all base-lane work from this session (TAGATTR, COTMVP, D_00 NNA bd+cot 7272e0705/997f58fd2, INF_D_04 WS-4) is landed, deployed, verified, and RAVC-closed.

---

## Next Steps

1. **[0.4.0_DE_ClientPlatform] RoleDonut under-fill render-confirm** — for travis the slices sum to 81% of the donut center (dedup total > sum-of-slices); confirm the <100% under-fill case renders sanely (the helpText covers the >100% overlap case). DE-lane, not a cert item (CVO concurred).
2. **[0.4.0_DS_ClientPlatform] hold available** — base-lane queue cleared + all loops closed; event-driven on next COO dispatch. INF gold un-freeze is the ~A lane.
