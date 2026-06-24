# Session Log -- 0.4.0_DS_ClientPlatform~B -- reverse-ETL data-calibration chunks 2-4 (allocations / txn-NNA / T2-residual)

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, TRACE, SCRIBE

## Summary

2nd DS lane (~B), spawned for the DATA_PLATFORM reverse-ETL parallelization (the BD/Orion/Eclipse supplant proof-of-method). Took chunks 2-4 of the 49F/Schwab data-calibration (base-DS leads method + chunk-1 lot-diff). All three chunks delivered as data-calibrated tier rows, grounded against LIVE artifacts + source-confirmed mechanisms (Rule-22), committed + pushed + RAVC'd to base-DS (integrator) + COO + CTO (cc CVO/0.6.0). chunk-2 already CVO-PASS (independently reproduced to the number) + CTO-accepted; chunk-3 CTO-accepted; chunk-4 just landed. Net result CLOSES the supplant headline hypothesis: for the Schwab-custodied 49F book, BD's served value is mostly T0/T1 + T2-HOST with a near-empty genuine-T2-COMPUTE residual -> strongly feasibility-positive.

## Briefs Written

| Brief | Path | Commit | Audience |
|-------|------|--------|----------|
| chunk-2 ALLOCATIONS tier | docs/briefs/DATA_PLATFORM_reverse_etl_chunk2_allocations.md | 19648fd8c | base-DS (fold) / COO / CTO / CVO / 0.6.0 |
| chunk-3 TXN/NNA tier | docs/briefs/DATA_PLATFORM_reverse_etl_chunk3_txn_nna.md | 235736f3f | base-DS (fold) / COO / CTO / CVO |
| chunk-4 T2-RESIDUAL tier | docs/briefs/DATA_PLATFORM_reverse_etl_chunk4_t2_residual.md | 9ef997a95 | base-DS (fold) / COO / CTO / CVO |

## Threads (chronological)

1. **Startup + orient.** /watcher (registered ~B, armed persistent Monitor b9xgfo2ps). MSTR orient (chunks 2-4, CTO-arch-gate-sequenced-but-COO-parallelized) + COO GO + base-DS handoff all consistent -> ACK'd all three, coordinated boundary (base keeps chunk-1; I take 2-4). Method/map/gradient = base-DS v0.1 brief.
2. **chunk-2 ALLOCATIONS.** REFRAMING (load-bearing): BD silver/allocations is NOT asset-allocation -- it's the BD account/relationship/advisor/fee DIMENSION (92 cols, 1/account). Tier SPLIT: VALUE cols (account_market_value et al.) = T1 (reproduces from Schwab RPS -- live 2026-06-18 per-account diff: +0.29% aggregate on 5,427 matched accts, 99.3% within 1% cash-adjusted; BD overage = broader universe 979 accts/$244M + cash + join-grain artifacts, NOT computation; corroborates 2026-03 ACAT). DIMENSION cols (86 of 92) = T2-HOST (firm-owned advisor/relationship/fee ref data BD merely HOSTS -- supplant = migrate the SoR, NO algorithm to reverse-engineer). Introduced the T2-HOST vs T2-COMPUTE distinction (ADOPTED into the gradient by base-DS + CTO). CVO independently reproduced Row-A to the number = PASS.
3. **chunk-3 TXN/NNA.** Both rows T1. 3A txn-feed: Schwab TRN = custodian source-of-truth; BD silver/transactions repackages + deterministic taxonomy + the SAME T2-HOST dimension overlay (cross-ref 2C). 3B NNA-classification: deterministic rule-set (convert_schwab_trn_to_nna_silver classify()) reproduces NNA from Schwab TRN, validated 85-90% monthly vs Schwab's OWN published 49F NNA; BD external_flow (Contribution/Withdrawal) confirms BD does the same; cross-validated 2 ways (our gold C_01 gains-method + the txn-classification). HONEST Rule-22 residual: a fresh same-period BD-vs-Schwab reconciliation is NOT cleanly achievable from current silver (BD trailing-window vs Schwab single-day partitions + market_value-vs-gross-cash semantics for in-kind TOA + broader universe -- naive diffs gave artifact 25%/495%); tiered on deterministic-mechanism + documented-validation, confidence-tagged. -> CTO adopted the SNAPSHOT-vs-FLOW verifiability distinction.
4. **chunk-4 T2-RESIDUAL.** Closes the set. Row 4A PERFORMANCE = standard-method COMPUTE (Dietz-family growth/NNA attribution, CTO case-(a) replicable), already SELF-OWNED + Schwab-sourced -- C_00.canonical_performance reads ONLY account_gains (B_03 <- holdings/lots/txns <- Schwab-direct), NO BD-perf ingest; portal serves OUR C_03; so NOT a BD-IP supplant blocker (parity-vs-BD-published = INFERRED residual). Row 4B GROUPING = T2-HOST + T1: C_02 deterministic groupby on EXPLICIT firm-assigned relationship_id, NO clustering heuristic (grep-confirmed) -- not T2-COMPUTE. => genuine T2-COMPUTE residual NEARLY EMPTY for the 49F/Schwab book.

## Compiler Tools

Window = reverse-ETL data-calibration (live-artifact diffs + source-confirmed mechanism reads; no gold run, no deploy). Rail: comp-which routed every grounding question; comp-pipescript io for the producer<->served maps; native source Reads for the mechanism; live boto3 data-access for the diffs (off-rail per Rule-21 row data-access).

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-which | allocations producer routing | PASS | -> comp-pipescript io (correct route) |
| comp-pipescript io | B_00, A_03, C_01, C_02, C_03, C_00, B_03 | PASS | producer/consumer maps; surfaced A_03 read+write of silver/allocations + confirmed C_00 reads NO BD-perf (only account_gains) |
| comp-to | chunk2/chunk3/chunk4 TO_ID set per chunk | PASS | race-free per-session TO attribution |
| boto3 live data-access | silver/allocations, schwab/silver/rps, schwab/silver/trn, schwab_bd_account_mapping, silver/transactions | PASS | the per-account MV diff + NNA classify + schema grounding (Rule-21 row data-access, off-rail) |
| safe-commit.sh | 3 brief commits + this log | PASS | author ~B, pathspec-scoped, surface-check clean |
| grep C_02 (rail-checked) | groupby/cluster/household | PASS | confirmed deterministic relationship_id groupby, no clustering heuristic (marker logged) |

**What worked:** ground-against-LIVE-then-source-confirm-mechanism (chunk-2's +0.29%/99.3% per-account diff = the gold-standard reproduce-to-the-number; chunk-4's "C_00 reads no BD-perf" = the supplant-decisive structural read). The T2-HOST/T2-COMPUTE refinement + the snapshot-vs-flow verifiability distinction both emerged from the calibration and were adopted into the method by CTO+base-DS. **What failed:** none (zero false-claims). **Gap/finding:** a fresh same-period flow-entity (NNA) reconciliation is NOT cleanly achievable from current silver artifacts (window + amount-semantic mismatches) -- a real verifiability-asymmetry finding (flagged honestly, not papered over), now a tracked hardening follow.

## Files Modified

See commit messages: 19648fd8c (chunk-2), 235736f3f (chunk-3), 9ef997a95 (chunk-4). Three new docs/briefs/* tier-row briefs; no code/infra touched (analysis-only).

## MCP Traffic

~16 broker messages this window. Significant: MSTR orient (chunks 2-4) + COO GO + base-DS handoff (ACK'd all); per-chunk RAVC2 to base-DS+COO+CTO (cc CVO/0.6.0) x3; base-DS validated+folded chunk-2 + chunk-3 (chunk-4 pending); CTO arch-accepted chunk-2 (adopted T2-HOST/T2-COMPUTE) + chunk-3 (adopted snapshot-vs-flow); CVO independently reproduced chunk-2 Row-A to the number = PASS.

## Current State

- **reverse-ETL chunks 2-4: ALL COMPLETE + RAVC'd.** Tier rows delivered to base-DS for fold into the unified data-calibrated tier table (the proof-of-method deliverable, base-DS Part-4). chunk-2 = CVO-PASS + CTO-accepted + base-DS-folded; chunk-3 = CTO-accepted + base-DS-folded; chunk-4 = landed (9ef997a95), base-DS + CVO verification pending.
- **Calibrated tiers (49F/Schwab anchor):** positions = T0 (base-DS, Schwab-RPS-direct); lots = chunk-1 (base-DS, in progress); allocations-value = T1, allocations-dimension = T2-HOST; txn-feed = T1, NNA = T1; performance = standard-method self-owned compute (not BD-IP); grouping = T2-HOST+T1. **Genuine T2-COMPUTE residual NEARLY EMPTY** for the Schwab book.
- **Confidence convention (CTO-adopted):** 2-axis -- (DIFFABLE vs INFERRED) x (SNAPSHOT-cleanly-reproducible vs FLOW-mechanism-confirmed). 49F = DIFFABLE; cot/inf = INFERRED (bounded, no custodian-raw to diff).
- **Method refinements I contributed (adopted):** T2-HOST vs T2-COMPUTE; snapshot-vs-flow verifiability; both flagged by CTO for the PRD/arch-gate.

## Next Steps

- **[0.4.0_DS_ClientPlatform]** (base, integrator) fold chunk-4 tier rows into the unified table; continue chunk-1 (lot-diff = the passthrough-vs-reconstruct test). On its call for my next unit.
- **[3.0.0_SA_CVO]** independently verify chunk-3 + chunk-4 as they land (chunk-2 already PASS).
- **[1.0.0_SA_CTO]** carry T2-HOST/T2-COMPUTE + snapshot-vs-flow into the DC-REV PRD gradient.
- **[0.4.0_DS_ClientPlatform~B]** (me) available -- candidate next units: the fresh-diff hardening follow (assemble BD full-month window + normalize amount semantics + matched-accts for a clean NNA reconciliation); the cot/inf INFERRED projection (apply the 49F-calibrated gradient, flag INFERRED); or a new dispatch.

## Addendum — chunk-4 residuals #1 + #3 CLOSED no-crawl (commit c0c67e5c8)

After chunks 2-4 closed, base-DS directed the two no-crawl residuals I'd surfaced; both grounded + RAVC'd (brief: docs/briefs/DATA_PLATFORM_reverse_etl_chunk4_residuals_perf_parity_and_consumer_census.md):
- **#1 PERF-PARITY -> RESOLVED feasibility-positive.** BD delivers ZERO computed performance — DataMining = exactly 5 raw prefixes (assets/txns/realized/unrealized/allocations); no perf file OR column; estate holds 0 perf-keys (scanned opal-data-bd 8,065 + opal-data-cot 447 objs). So the parity-diff is un-runnable no-crawl (no BD-perf artifact exists) — which RESOLVES the 4A INFERRED: supply-side (BD delivers none) confirms chunk-4's demand-side (C_00 ingests none). Full close would need a BD-platform crawl/statement-pull = Andrew-gated; NOT needed for feasibility.
- **#3 CONSUMER CENSUS -> NOTHING consumes a BD-computed analytic directly.** Full advi-bd thread traced (pipescript, 19 threads): BD inputs all RAW (custodian feeds + fee config); all analytics computed in OUR gold C-chain (A_00..D_04); all frontend served via OUR Lambdas (bd-gold-layer-pipeline/bd-portal-publisher/bd-client-detail-api -> gold/* + platinum/firm/*); even pricing self-owned (yfinance + our canonical_prices). Hardens chunk-4 "no BD ingest" TRANSITIVELY. The one BD-compute residual = lots passthrough-vs-reconstruct = base-DS chunk-1 (cross-ref, not re-done).

NET: BD/49F supplant surface = raw-data-delivery (Schwab-direct held) + firm-config-host (T2-HOST migrate-SoR). Decision-grade reinforced. Compiler tools this delta: comp-which (route), pipescript advi-bd (the census), boto3 estate scan (perf-artifact existence). cot/inf projection HELD per Andrew risk-gate.

## Blockers

None. All chunks (2-4) + both no-crawl residuals (#1/#3) delivered + RAVC'd. Remaining legs event-gated on base-DS (chunk-1 lots + unified proof-of-method close) / CVO (independent verify) / CTO (PRD/D5 fold) / Andrew (cot/inf risk-gate). ~B idle/available, not blocked.
