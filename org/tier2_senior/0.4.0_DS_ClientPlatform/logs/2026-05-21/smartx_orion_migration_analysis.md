# Session Log — SmartX → Orion Account-Admin Migration Analysis

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-05-21
**Type:** Ad-hoc analytical request from Andrew (not a task order)

---

## Request

Andrew: design the SmartX → Orion account-admin migration. SmartX charges 4 bps/yr;
Orion charges $37 flat/account/yr; breakeven $92,500/account. SmartX mandates a
$900M AUM minimum. Two parts:
- **Part 1** — which households/accounts migrate, with a CSV + a rich proposal.
- **Part 2** — a routing model for where to send *new* accounts by size/growth,
  with its own proposal.

Iterated extensively on universe definition, ending on the Schwab-custodied basis.

## Briefs / Deliverables Written

| Deliverable | Path | Audience |
|-------------|------|----------|
| Part 1 migration plan | docs/proposals/smartx-orion-migration/Part1_Migration_Plan.md | Andrew / exec |
| Part 1 account-level CSV | docs/proposals/smartx-orion-migration/Part1_migration_accounts.csv | Andrew / ops |
| Part 1 household-level CSV | docs/proposals/smartx-orion-migration/Part1_migration_relationships.csv | Andrew / ops |
| Part 2 routing model | docs/proposals/smartx-orion-migration/Part2_Routing_Model.md | Andrew / exec |
| Part 2 reference implementation | docs/proposals/smartx-orion-migration/routing_model.py | Andrew / DS |
| Folder README | docs/proposals/smartx-orion-migration/README.md | Andrew |

## Files Modified

| File | Change |
|------|--------|
| docs/proposals/smartx-orion-migration/Part1_Migration_Plan.md | Created, then fully revised onto the Schwab-custodied basis (139 households / 607 accounts / $777.4M collective / $275.6K savings) |
| docs/proposals/smartx-orion-migration/Part1_migration_accounts.csv | Regenerated — 607 accounts in the 139 migrating households, with custodian flag |
| docs/proposals/smartx-orion-migration/Part1_migration_relationships.csv | Regenerated — 139 households with Schwab / non-Schwab / collective splits |
| docs/proposals/smartx-orion-migration/Part2_Routing_Model.md | Created; cross-ref fix (G3→O3) after Part 1 revision |
| docs/proposals/smartx-orion-migration/routing_model.py | Created — parameterized routing-decision prototype |
| docs/proposals/smartx-orion-migration/README.md | Created, then revised to the Schwab basis |

## Current State

**Data basis (resolved).** Started from Black Diamond
`s3://opal-data-bd/silver/allocations/2026-05-19.parquet` ($1,803,455,648,
6,723 accounts). The earlier $1.65B-vs-$1.80B gap is closed: applying
`custody_crosswalk_published.json`, the BD total splits Schwab $1,646,651,097 /
ByAll Accounts $130.1M / Fidelity IWS $12.8M / DST $1.2M / unmapped $12.7M.
**The Schwab-custodied subset ($1,646,651,097) is the migration basis** — it is
the "~$1.65B" figure. Cross-referenced to the Schwab custodial extracts
`s3://opal-data-bd/schwab/silver/{acc,rps}` (2026-05-15): 6,750 of 6,925 Schwab
accounts carry `manager = "SmartX Advisory Solutions"` (97.7% of the cohort by
AUA, $1,555,812,263) — SmartX is effectively the whole Schwab book.

**Part 1 — migration set (final).** Households are the unit; the $900M floor is
measured on SmartX/Schwab AUM, so eligible households are ranked by Schwab AUA
and selected until cumulative Schwab AUA hits the $746.65M movable budget. When
a household migrates, all its accounts move (non-Schwab accounts ride along).

- 139 households / 607 accounts (540 Schwab + 67 non-Schwab) / $777,401,224 collective AUM
- SmartX/Schwab AUM moved $745,129,704 → SmartX retained $901,521,392 (floor satisfied)
- Annual savings $275,593 (before $658,660 / after $383,068)

**Part 2 — routing model.** Static breakeven $92,500; dynamic breakeven adds a
migration-cost-aware growth buffer (formula CA(V) in routing_model.py); a
portfolio floor-governor keeps SmartX ≥ $900M target by conscripting the
smallest accounts. Key finding: for any realistic migration cost the SmartX-cheaper
zone collapses to terminal-small accounts only — new accounts default to Orion.

**Mandate-cost finding.** 93.8% of the Schwab book by AUA is in above-breakeven
households; the $900M minimum conscripts ~$799M of Orion-economic AUA at a
recurring ~$230K+/yr avoidable cost. Renegotiating the minimum is the largest
lever — each $100M of reduction is worth ~$30K+/yr.

## Open Items (Phase 0, before execution)

1. Obtain a SmartX platform AUM statement — confirm SmartX ≈ the Schwab cohort;
   decide whether the precise universe is $1.647B (all Schwab) or $1.556B
   (SmartX-managed only).
2. Build the Schwab-`acc` ↔ Black-Diamond account-ID bridge (no join key today:
   Schwab `account_id` `0010020692` vs BD `z08…`; Schwab `account_number` blank).
3. Confirm the SmartX mandate mechanics (measurement frequency, cure period).
4. Measure the per-account migration cost in a Phase-1 pilot.

## Next Steps

| Recipient | Item |
|-----------|------|
| Andrew | Review the two proposals; decide on Phase 0 (SmartX statement, ID bridge) and whether to pursue the $900M-minimum renegotiation in parallel (Part 1 R4). |
| DS (self) | On request: regenerate to the $1.556B SmartX-managed universe once the Schwab↔BD ID bridge exists; pilot-wave runbook support. |

## Compiler Tools

N/A — ad-hoc analytical task. No gold/silver/bronze scripts, Lambda code, or
portal components were created or modified; the deliverables are markdown
proposals, CSVs, and a standalone reference Python prototype that is not wired
into any pipeline. The comp-* tool suite (pipescript io/deployed/postdeps,
transform schema-check, validate) has no applicable surface here. Data was read
directly from S3 (`opal-data-bd` BD silver + Schwab silver) with pandas.
