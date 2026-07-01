# 0.4.0_DS_ClientPlatform -- ADVI_TAGATTR.DS-1 (role_breakdown FULL-TAGGED) + advisor-attribution rollup investigation

**archetype:** IMPLEMENT (secondary: DIAGNOSE, COORDINATE)
**window:** 2026-07-01 ~1325Z -> 1356Z
**serial:** 0.4.0_DS_ClientPlatform | **branch:** CLOUD | **project:** ADVI_TAGATTR
**driver:** GO from 0.4.0_DE (TO 0517a8397) + CTO arch-gate addendum (via MSTR/COO) + Andrew-direct investigative ask.

## HEADLINE
ADVI_TAGATTR.DS-1 leg-1 LANDED + deployed + verified: advisor role_breakdown AUA/NNA/inflows/outflows
are now FULL TAGGED (non-additive), not split-weighted. Both CTO arch-gates honored (non-additive
labeling done + effective at the served layer; fee-basis leg correctly escalated to CTO). Artifact
validation gated on the scheduled nightly (no ad-hoc gold run -- NEVER rule). Separately answered
Andrew's rollup question with a source-grounded finding.

## What landed (leg-1)
- **AUA:** D_00c `_build_at_role_slice(full_tagged=True)` sums full total_aua (deduped per advisor+account,
  mirrors L865) instead of `_weighted_aua`. Top-level per-role only; fee sub-buckets untouched.
- **NNA/inflows/outflows:** per-role pair weight 1.0 (was equal-split `_split_weight`); fee/no-fee
  partition exhaustive+disjoint so role.nna == fp.nna+nf.nna preserved, both full-tagged.
- **ARCH-GATE 1 labeling:** per-role `aua_basis` + top-level `role_breakdown_semantics` =
  `advisor_tagged_full_nonadditive`. Found + fixed the D_04 `_LEADERBOARD_ROLE_FIELDS` whitelist +
  fresh top-level dict which would have STRIPPED both labels before the served artifact.
- **GROUNDING correction to the TO hypothesis:** the canonical role_aua path (aua_tagged_total) is
  disabled (`if False`, P1-shadow INTERIM-REVERT 2026-04-20, ~5x underscale) -> NOT used; recomputed
  from the account_team melt (same trusted source as total_aua). Reported to DE (AC4).
- advisor total_aua (dedup ~439.97M) UNCHANGED (served value sourced from D_02 book.json via D_04).

Commits: D_00c `0ab172d3f`, D_04 `fc8c18361`, data_contract.xml `60dfec6ae`. Both scripts MATCH on
s3://opal-data-bd/code/gold/ (comp-pipescript deployed). Offline full-tag math unit-tested (travis
architect $300M / implementor $200M; legacy split undercount reproduced; invariants hold).

## ARCH-GATE 2 (fee-basis) -> ESCALATED to CTO
Fee-blast: per-role fee_paying.aua is post-hoc scaled to the C_08 canonical billing total (D_00c
L602-624); implied_revenue is sourced from C_08 advisor_fee_detail; D_00c CONSUMES C_08 (not upstream);
E_23 no consumers; C_08 fee_efficiency scorecard independent. Full-tagging the fee-basis rebases it
across the C_08 lane -> STOP + CTO ADR (A: full-tag non-additive w/ fee-owner coord, vs B: keep
C_08-reconciled). Leg-1 fee buckets unchanged; no_fee.aua shifts only as the full-tagged residual.

## Andrew-direct investigation: are we assigning AUA to non-explicitly-tagged advisors? -> YES (report-only)
Two relationship-rollup/inference mechanisms in C_07.advisor_attribution.py:
- **Layer-2 (blank -> relationship modal REAL architect, C_07:300-304):** applied EVERYWHERE incl. the
  no-infer canonical path (D_00c/D_00f). A blank-architect account inherits a real sibling architect
  from the same relationship -> AUA credited to an advisor not explicitly tagged on that account.
- **Layer-3 (House/blank -> inferred individual, `resolve_architect` C_07:232-262):** T1 modal real
  architect (also overrides House); T2 impl-pairing GUESS. The $357.6M-House-leak class.
- **Consumer split:** only 4 files read `architect_no_infer` (D_00c, D_00f, the lib, C_07). ALL ~14
  other consumers read the Layer-3 inferred `architect`, incl. the AUA-served surfaces:
  D_02.advisor_client_detail (overlays resolved_architect D_02:3153-3166, book total_aua D_02:1235-1260)
  -> D_04 sources the SERVED leaderboard total_aua from it (D_04:2311-2313); D_01 ADV view (D_01:355).
- Net: post-TAGATTR the same served entry mixes bases (role_breakdown=no_infer/House-excluded;
  total_aua=Layer-3-inferred/House-rolled-up). Pre-existing. NO changes made (Andrew: report-only).
  Banked: memory/reference_bd_architect_inference_no_infer_split.md.

## RAVC
RAVC2 to DE (leg-1 evidence, validated by DE); CTO ADR ask (fee leg); CC COO (ACK closed) + CVO
(served-verify consult accepted, co-gated on nightly with the 49F FE fix). Loops OPEN: leg-1 artifact
validation (comp-validate Phase-3 post-nightly) + leg-2 CTO ruling.

## Compiler Tools
| Tool | Result |
|---|---|
| comp-pipescript io D_00c / D_04 | READS/WRITES + consumers; confirmed D_04 trims employee_leaderboard -> served leaderboard.json |
| comp-blast D_00c / C_08 / E_23 | fee-surface enumeration: C_08 independent scorecard, E_23 no consumers, D_00c consumes C_08 |
| comp-pipescript deployed D_00c / D_04 | MATCH x2 (S3 == committed) |
| comp-which (x2) | routed field-passthrough + rollup questions to comp-pipescript io / comp-platinum |
| ds-commit-gate.sh D_00c / D_04 | clean x2 (py_compile + AST + ruff) |
Source-mechanism tracing (C_07 resolvers, lib/advisor_nna_attribution, D_02/D_01 AUA paths) via
native Read/Grep -- rule 22 mandates reading source to ground a MECHANISM/why claim (Explore banned).
