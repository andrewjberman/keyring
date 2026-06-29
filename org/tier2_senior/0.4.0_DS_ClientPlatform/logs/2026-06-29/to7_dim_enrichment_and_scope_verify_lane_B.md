# Session Log (delta) — 0.4.0_DS_ClientPlatform~B — scope-verify + TO-7 dim enrichment

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE (scope-verify), VALIDATE
**serial:** 0.4.0_DS_ClientPlatform~B · **date:** 2026-06-29 · **window:** since prior log (schwab_ssot_census_and_g11g13_lane_B.md, 1512Z) -> 1544Z

## Summary

Two new closed items after the census + G11-G13:
1. **CTO scope-verify** (held-away-in-Schwab capture) — commit `5e66272c7`, accepted by CTO (PRD corrected to ~$243M residual).
2. **DATA_SSOTMG TO-7** dim_advisor_role enrichment (Wave-2 parity prereq) — commit `6d48d4782`, TO complete `0e95cf6ca`, RAVC base-DS(co-own)+COO+CC CTO.

## Scope-verify (DIAGNOSE)

CTO asked: does canonical_holdings capture held-away-in-Schwab, or does the cutover drop ~$100M? Grounded (read-only):
- canonical_holdings (5892/$1.591B) is a CLEAN SUBSET of Schwab ACC (6997) — 0 orphans.
- 1105 ACC accounts unpositioned; 88%/$76.5M of held-away-in-Schwab ABSENT from canonical; ACC has NO balance column.
- Mechanism (Rule-22): held-away VALUE in NEITHER RPS positions NOR ACC balances -> BD-only -> RPS-canonical structurally can't source it.
- Corrects my census's optimistic line: BD-dependent residual = $166.3M + $76.5M = ~$243M. Sets CVO Class-D positioned subset = canonical_holdings; held-away = separate parity class. Addendum §5a in the census brief.

## TO-7 dim enrichment (IMPLEMENT)

Folded the full advisor model into canonical dim_advisor_role (schema 1.0 -> 2.0): implementor/consultant/local_ops/additional_advisor + 6 split-% from BD silver/allocations, bridged BD->Schwab via the xref (mirrors build_dim_advisor_fee.py).
- base-DS co-own guards honored: --date/asof idempotent single-partition (latest non-empty <= date, skips frozen 06-26+); write in canonical/schwab/silver; architect/manager/money_manager kept AS-IS; architect_matches_alloc = coherence flag (98%), not overwrite.
- bd-source-flagged: roles_source='bd-allocations-bridge' + roles_source_as_of=2026-06-24.
- Validation: 6753 accts PK-unique, 82% bridged, split-% means sane (impl 57/arch 33/cons 27/lops 5/house 5.5), 81% split-sum~100.
- G11 advisor_attribution re-materialized carrying all 13 BD-bridged fields (Wave-2 parity substrate, AUA $1.591B ties holdings). G12/G13 clean on enriched dim (G13 AUA ties G11).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-pipescript io | build_dim_advisor_role.py | N/A (expected) | NOT-FOUND — canonical not graph-indexed (documented PRD §5); mandate attempted |
| ds-commit-gate | dim + G11 (x2 passes) | PASS | py_compile + AST + ruff clean |
| (read-only boto3) | scope_verify, profile, bridge-coverage | PASS | live-S3 grounding (Rule-21 row data-access, off-rail) |

- **What worked:** the xref bridge (bd_account_id->schwab_padded_id) cleanly carried the BD advisor model into the canonical dim; coherence/split-sum sanity checks caught a cleaning-convention false-divergence (63% -> 98% after normalizing sentinels).
- **What failed:** comp-pipescript io can't cover the canonical tree (known gap).
- **Gap found:** none new; the canonical-graph-coverage gap re-confirmed.

## Blockers

None. (G13 split-weighted multi-role attribution awaits CVO's grounded BD-served leaderboard formula — a coordination item, not a blocker; flagged AC#3.)

## Current State

All 3 dispatched SSOT slices + the CTO scope-verify done + accepted/RAVC'd. Enriched dim + G11-G13 materialized at canonical/schwab/{silver/dim_advisor_role,gold/advisor_attribution,gold/advisor_fee_efficiency,gold/partner_analytics}/[asof|date]=2026-06-24. Commits 31bcb017b (census), 5e66272c7 (scope-verify), d81ea44a0 (G11-G13), 6d48d4782 (TO-7 enrichment). All pushed CLOUD. Registered LIVE, summary IDLE.

## Next Steps

- **[3.0.0_SA_CVO]** ground the BD-served leaderboard split-% attribution formula -> I add split-weighted multi-role attribution to G13 + re-materialize (the Wave-2 advisor parity step).
- **[0.4.0_DS_ClientPlatform]** (base) co-own review of the TO-7 diff (6d48d4782); G11-G13 orchestrator daily-wiring is base-DS lane (D4 cadence open).
- **[2.0.0_SA_COO]** next dispatch (PFMG_TAXSMA S0 resumable, or CVO harness support).
- **[1.0.0_SA_CTO]** Wave-2 parity substrate ready; fee-coverage 8.3% (xref-refresh) + the G13 split-weighting are the remaining advisor-parity items.
