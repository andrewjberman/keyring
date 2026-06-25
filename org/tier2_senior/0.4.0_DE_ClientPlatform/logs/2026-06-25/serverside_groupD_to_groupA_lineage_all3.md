# Server-side Group-D -> Group-A lineage manifest (all 3 partners)

**archetype:** TRACE
**Serial:** 0.4.0_DE_ClientPlatform | **Date:** 2026-06-25 | **Window:** 1542Z -> 1610Z

## Summary
Andrew-direct: authored the server-side companion to FE1 -- backtracking each Group-D served artifact UP through
C -> B -> A -> raw, per partner, successively (49F -> COT -> INF). Layered: script-spine + field-detail on the 3
headline numbers + rebuild-relevance tags. FE1 format approved by Andrew first.

## Current State
- **Deliverable:** `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/DATA_ANALYTICS.A1_serverside_groupD_to_groupA_lineage_manifest.md` @ 49f27df7f (v1.0, all 3 partners). Desktop copies dropped at each version (49F v0.1, +COT v0.2, +INF v1.0) for Andrew review; he approved 49F then COT, then GO'd INF.
- **PART 1 49F (BD):** full D->A spine (8 D-publishers transitive to A->Schwab-silver), §2 per-script `<-` edges, §3 field-detail on total_aua (<-C_02/03 ending_mv <-B_00/02 market_value <-A_03 positions_cube <-silver allocations+prices) / nna (<-C_01 <-B_03 account_gains <-silver/transactions TRN) / tax_liability (<-C_05 <-B_02 custodian-lots ULN/RLD + B_01 FIFO). §4 = the value-parity census substrate for CTO's G2 excise gate (tags B_01-FIFO/B_00-reconcile excise targets, N1-fee retain, N2-household deferred). Finding: B_02 ALREADY reads schwab/silver/{rld,uln,ult} direct -- the custodian-direct lot path exists; rebuild retires B_01-FIFO + B_00-reconcile around it.
- **PART 2 COT (BD-native):** scripts are structural CLONES of 49F (D_04 sole publisher, same schwab/silver path NAMES) BUT bronze/silver is BD-DataMining-native (BD session export populates those paths), NOT Schwab-direct -> grounds CTO G3 "BD-native not Schwab-native" sequencing gate. Essential D_00/D_00b/D_01/D_04; agnostic D_00c/D_02/D_03+cohort_a/cash_coverage; NO D_00f (gap-4a); +A_05 assets_dim; +E-tier (E_00..E_24) diagnostics OFF the served path.
- **PART 3 INF (Orion):** same A/B/C canonical tier (INF_A/B/C_*) but ~20-publisher FAN-OUT D-tier (no single D_04); several publishers (INF_D_04, INF_D_08) reach bronze/orion-api DIRECTLY (flatter); leaves = Orion+Eclipse, NOT Schwab/BD -> SEPARATE TRACK (not the Schwab-raw rebuild target). INF_D_00e = the gap-4b header_metrics_fresh origin. Insights-panel lineage (INF_D_05/06/07a <- gold/cache anchors + silver/accounts_dim).
- **Pairs with FE1:** FE1 (panel->D) + this (D->A) = the complete panel->platinum->D->C->B->A->raw vertical.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-pipescript io` | 49F D/C/B/A scripts (~25); COT D_04/B_02/A_03/A_05/D_00-01; INF D_04/D_00/D_05/06/07a/08 | PASS (mostly) | the load-bearing tool -- per-script READS `<-` edge map built the whole D->A DAG |
| `pipescript advi-bd/advi-cot/advi-inf` | partner backends | PASS | (from FE1 session) confirmed the publisher set + served paths per partner |

**What worked:** `comp-pipescript io` `<-` edges are exactly the backtrack primitive -- deterministic upstream-resolution per script, no tree-grep. Built all 3 partner DAGs from it. **What failed:** `comp-pipescript io` returned EMPTY reads for 3 INF scripts (INF_B_02, INF_A_03, INF_09) -- index doesn't carry their (pattern/dynamic) read map; position inferred from siblings + flagged in §3.4. **Gap found:** comp-pipescript io INF-tree coverage gap (3 scripts) -- sibling to the comp-platinum-reverse BD-only-index gap noted in FE1. Worth a comp-tool coverage follow.

## Blockers
None. Deliverable complete (all 3 partners, Andrew-reviewed per-partner). Feeds the canonize-gold rebuild + CTO's G2 value-parity census.

## Next Steps
- **[Andrew]** review v1.0 (INF part); the D->A map is the value-parity census substrate for the rebuild.
- **[1.0.0_SA_CTO / 3.0.0_SA_CVO]** §4 (49F) tags the B_01-FIFO/B_00-reconcile-derived served fields = the G2 excise-parity target list.
- **[0.4.0_DS_ClientPlatform]** this complements your A1 D-tier field-requirements -- the consumer(FE1)+lineage(this) bracket the gold internals your silver-dim rebuild reshapes.
- **[0.4.0_DE]** available; rebuild build-TO FE-lead on contract-lock.
