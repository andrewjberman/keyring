# CVO Audit + /seams verdict — ADVI / bd NNA estate — 2026-06-17 ~18:04Z

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, TRACE

Andrew-directed audit (plan APPROVED): the larger NNA risk is canonical-source consistency — the same
advisor's NNA must be identical across every route, no alternative methodologies by component path.
Swept every bd NNA surface + supplying gold script; ran `/seams` on the connecting scripts to root-cause
the central divergence against ground truth. Full remediation plan: `~/.claude/plans/now-would-be-a-velvety-anchor.md`.
Andrew product decisions this session: **per-advisor NNA scope = ALL roles** (non-additive; firm stays
additive); **MAX window = 2021-Q1** end-to-end.

## Method
Ground-truth only — no Explore/Task agents (org/XXX.md ban; fabrication is fatal for an audit), no heavy
local compute (full_scan/windowed OOMs the box — Andrew-confirmed). Empirical reconciliation + a /seams
3-axis pass via small served-JSON reads + deployed-source reads vs deployed `gold_dispatch.sh`, served
`platinum/firm/*`, the live graph.

## SEAM: bd NNA attribution — C_01 → {D_00f, D_00c} → FE   (scale: MACRO, decomposed)

### Axis verdicts
| Seam | MECHANICAL | DECLARATIVE | SEMANTIC |
|---|---|---|---|
| C_01 → D_00f (architect) | PASS — reads `gold/canonical/nna/`, uses C_01-stamped `architect` (D_00f:190), no C_07 re-resolution | **FAIL** — "filtered to architect" hides that the source (acct_dim SCD) parks 34.5% of firm NNA in `Unassigned`/`49F House`, listed as advisors | **FAIL** — attribution source-inconsistent with D_00c; 34.5% unattributed |
| C_07 → D_00c (all-roles tagged) | PASS — `account_team` melt + per-day gate + role redistribution | PASS | caveat — Layer-3 architect is **inferred** (modal-implementor ≥60%); validate the inference |
| C_01 → {D_00f, D_00c} (atomic source) | PASS | PASS | PASS — same atomic account×date NNA |
| served → {DistributionTab, AdvisorPublicProfile} | PASS | PASS | **FAIL** — Distribution=architect $4.14M vs profile card=all-roles $6.95M, SILENT (no lens label) |

### Knowledge-parity delta (BELIEVED vs TRUE)
- BELIEVED (my first hypothesis): the D_00f-vs-D_00c architect divergence is a per-day tagging gate +
  role-overlap redistribution. **FALSIFIED by /seams.**
- TRUE: **dual attribution source.** D_00f attributes from C_01's `acct_dim` SCD (`architect` stamped at
  write, "latest snapshot; PIT history out of scope") which leaves unresolved accounts as `Unassigned` /
  `49F House`. D_00c attributes from C_07's `account_team`, whose **Layer-3 architect-implied** pass resolves
  those placeholders to real architects. Evidence: leaderboard (D_00c) has **0 placeholder entries**;
  canonical (D_00f) parks **$35.3M of $102.35M firm QTD (34.5%)** — `Unassigned` $27,856,941.62 (the #1
  "advisor") + `49F House` $7,462,529.56. The per-day gate is a secondary modifier, not the cause.

## Empirical evidence (served, 06-17 / data_as_of 06-15)
- Firm QTD NNA $102,353,326.43 (canonical, additive to $0.03 across all windows).
- Travis Penfield QTD: canonical architect $4,139,233.58 | leaderboard role_breakdown.architect
  $6,172,316.75 (+$2.03M / +49%, same concept two scripts) | leaderboard all-roles total $6,952,133.44.
  1Y: $11.74M vs $24.23M (+106%). Leaderboard Σ(entries) QTD $308.9M ≈ 3× firm (non-additive by construction).
- Routing: DistributionTab/Continuous-ADV-NNA + AdvisorPublicProfile Lifetime-chart/Exec-flows read
  `getAdvisorNnaCanonical` (architect); AdvisorPublicProfile SummaryCard `periodNna = entry.nna` + AdvisorsTab
  read the leaderboard (all-roles). `ADVI_INFMVP.F5` repointed card inflows/outflows to canonical but left
  `periodNna` on the leaderboard → on the same card nna ≠ inflows−outflows.

## Clean bill of health
Single canonical SOURCE (C_01 ← load_flows; all D_* read it); firm-additive arithmetic exact ($0.03); legacy
NNA scripts dead (0 dispatch); upstream load_flows L4 deploy-clean (this AM); stale served artifacts
(`employee_leaderboard.json` aliased to fresh `leaderboard.json`; `nna_by_*.json` 0 FE refs) dead-served, not read.

## Findings (must remediate — full text + remediation in the plan)
- **F-0 [P1]** Attribution-coverage gap — 34.5% ($35.3M QTD) unattributed in the canonical/architect surfaces.
- **F-1 [P1]** Cross-route + cross-script per-advisor NNA divergence; root cause = dual attribution source
  (F-1a), scope mismatch resolved to all-roles (F-1b), within-card nna≠inflows−outflows (F-1c).
- **F-2 [P2]** MAX-window mismatch → 2021-Q1 everywhere.
- **F-3 [P2]** FE client-side NNA re-derivation (Inflection synthetic ratio; deriveNoFeeFromTagged route split).
- **F-4 [P2/P3]** Headline cum-diff methodology + `dashboard.json` NNA-omission/zeroing fallback.
- **F-5 [P3]** D_02 C_03 cum-diff fallback.

## Verdict
Estate **SOUND on the SOURCE** (single canonical C_01, exact firm arithmetic) but **BROKEN@DECLARATIVE +
@SEMANTIC on advisor-level attribution** (dual source, 34.5% placeholder parking, silent cross-route lens
split). Remediation = unify on one C_07-resolved attribution + one tenure rule + all-roles per-advisor +
MAX 2021-Q1, gate-enforced via the NFRA_GCONTR NNA value-limb.

## Residual / unknowns
- **Open decision (Andrew/CTO):** adopt C_07's *inferred* architect resolution (resolves the 34.5%) vs keep
  genuinely-unknown accounts `Unassigned` (conservative). F-0's remediation shape turns on it.
- Per-day-gate vs snapshot tenure rule: to be decided once + applied to both surfaces (F-1a).
- Exact $-decomposition of Travis's $2.03M architect gap into resolved-account contributions: not itemized
  (the 0-placeholder + $35.3M-parked aggregate evidence is sufficient for the mechanism).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| Grep/Read (deployed gold_dispatch.sh + C_01/C_07/D_00/D_00b/D_00c/D_00f/D_01/D_02 + FE) | estate map + attribution-source trace + FE routing | producers/consumers mapped; dual attribution source found |
| pipescript advi-bd + comp-blast advisor_nna_canonical | NNA lineage + consumers (blast = lower-bound, FE dynamic reads uncounted) | C_01→D_*; graph can't see FE consumers (dynamic) |
| aws s3 + python (boto3, in-memory served-JSON reads — LIGHT) | empirical reconciliation (firm + Travis per window across artifacts) | the $4.14M/$6.95M/$6.17M divergence + $35.3M placeholder parking |
| /seams (3-axis, this skill) | root-cause the divergence vs ground truth | falsified per-day-gate hypothesis; confirmed dual attribution source |

**What worked:** /seams forced the ground-truth read that falsified my per-day-gate hypothesis and surfaced
the bigger 34.5%-placeholder finding — the exercise-or-evidence discipline caught a wrong mechanism before
it shipped in the plan. **Gap found:** the bd NNA advisor-attribution seam had no prior knowledge-parity
record; durable entry now at `org/seams/advi-bd-nna-attribution.md`.

— 3.0.0_SA_CVO
