# Session Log -- ADVI_REBORN W5 + Classification Fix + B_01b
**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-08
**Projects:** ADVI_REBORN, ADVI_GLDOPS

---

## Summary

Three-part session: (1) completed all REBORN W5 DS task orders, (2) diagnosed and fixed the Assets Overview vs Books tab alternatives classification divergence (31 bad DynamoDB entries), (3) wrote B_01b.classify_new_securities.py to automate classification in the gold pipeline.

---

## Commits

| Commit | Description |
|--------|-------------|
| 2c17b18d | fix(D_00): NNA timeseries outputs cumulative sums, not daily values |
| 72201784 | feat(D_02): pre-compute per-entity AUA timeseries to eliminate Lambda hot-path |
| 65f24ae7 | feat(C_08): add advisor_effective_bps alongside gross fee_bps_weighted |
| 946f0e0e | log(DS): REBORN W5 session -- all 3 TOs complete + deploy brief |
| 5f5b35b (portal DEV) | fix(portal): FeeEfficiencyPanel shows advisor effective rate |
| e71fe8fe | feat(gold): B_01b auto-classify new securities after holdings_lots |

---

## Part 1: REBORN W5 Task Orders (all complete)

### W5-001: NNA Cumulative Fix (2c17b18d)
D_00's NNA view and _nna_drill_data() outputted daily flow values. Frontend diffs adjacent period endpoints to compute period flows -- only works with cumulative data. Added cumsum on daily_inflow/daily_outflow for firm NNA and per-category cumsum for geo/adv drill views. header_metrics (Snapshot) unaffected -- uses cum_inflows from C_05.

### W5-003: Books Tab Performance (72201784)
Investigation found getClientsTab() is NOT the bottleneck -- it serves a pre-computed JSON (~60-80KB). The real bottleneck is handle_books_timeseries() reading full client_performance.parquet (50-350MB) to serve one entity. Fix: D_02 now pre-computes ~600 relationship + ~3500 account AUA timeseries JSONs. Lambda tries pre-computed JSON first, parquet fallback until next gold re-run.

### W5-004: Fee Display Clarification (65f24ae7 + portal 5f5b35b)
Confirmed fee_bps_weighted = gross client fee (split cancels in back-derivation). Added advisor_effective_bps = implied_annual_fee / total_aua * 10000 (advisor's weighted avg take rate across their book, reflecting varying splits). Andrew confirmed this is the right metric. Portal FeeEfficiencyPanel updated to display advisor_effective_bps (~37bps) instead of gross (~100bps).

---

## Part 2: Classification Divergence Fix

### Problem
Assets Overview tab showed ~$8M alternatives (0.5%) while Books tab showed ~$67M (4.1%). All structured products (Shield, Buffer, Annuity) were bucketed as equity or fixed_income in Assets Overview.

### Root Cause
31 entries in bd-securities DynamoDB had wrong asset_class values. These were NAME:: synthetic entries (no real ticker) created by classify_bd_securities.py using OpenAI. The LLM misclassified structured products.

Assets Overview (C_06) reads positions_cube which has NO ticker column. Classifier falls to Layer 2 (name-alias -> DynamoDB) and hits the bad entries. Books tab (D_03) reads holdings_lots which HAS tickers -- those resolve to different, correctly-classified DynamoDB entries via Layer 1.

### Fix
Corrected all 31 DynamoDB entries directly:
- 28 structured products (Shield/Buffer/Annuity/Futures ETF) from equity/fixed_income -> alternatives
- 3 additional (TrueShares Bear Hedge, TrueShares Structured Outcome x2) from equity/fixed_income -> alternatives

No code changes to ETFClassifier -- the DynamoDB-first design is correct. The data was wrong, not the code.

### Audit
Ran a full audit of all 5,203 bd-securities entries against regex patterns. Remaining flagged items (JPMorgan Hedged Equity, Pacer Cash Cows, etc.) are correctly classified -- the broad regex caught keywords in their names but they are equity funds.

---

## Part 3: B_01b Auto-Classification (e71fe8fe)

### Problem
classify_bd_securities.py was never wired into any automated flow. New securities from BD ingestion would land in positions_cube/holdings_lots unclassified, falling through to regex or defaulting to equity.

### Solution
Wrote B_01b.classify_new_securities.py -- runs after B_01 (holdings_lots), before B_02 (canonical_lots). Watermark-based incremental scan: only processes holdings_lots partitions newer than last run. Classifies net-new securities via OpenAI -> DynamoDB.

Wired into gold_dispatch.sh:
- CHAIN_FOUNDATION: ... B_01 B_01b
- CHAIN_CANONICAL: B_00 B_01b B_02 B_03 ...
- GROUP_B: B_00 B_01 B_01b B_02 B_03

### AE Coordination
Messaged 0.6.0_AE_PartnerETL. They confirmed:
- Hook point: after B_01, before C_00 (correct)
- OpenAI API key: in Secrets Manager (openai-api-key), IAM policy update needed (they'll handle)
- They'll deploy B_01b + updated gold_dispatch.sh to EC2 runner

---

## Reconciliation

| Task Order | Status Change |
|------------|---------------|
| ADVI_REBORN.W1-002 | staged -> complete |
| ADVI_REBORN.W3-002 | staged -> complete |
| ADVI_REBORN.W3-004 | staged -> complete |
| ADVI_REBORN.W5-001 | pending -> complete |
| ADVI_REBORN.W5-003 | pending -> complete |
| ADVI_REBORN.W5-004 | pending -> complete |

No pending DS task orders remain.

---

## Files Modified

| File | Change |
|------|--------|
| D_00.portal_aggregates.py | NNA cumsum for firm + per-category drill views |
| D_02.advisor_client_detail.py | New: build_relationship_timeseries(), build_account_timeseries() |
| lib/s3_layout.py | New: client_aua_timeseries_key(), account_aua_timeseries_key() |
| opal-partners-data/lambda_function.py | handle_books_timeseries: pre-computed JSON fast path |
| C_08.advisor_fee_efficiency.py | advisor_effective_bps, effective_split_pct, total_aua agg |
| E_24.rebuild_fee_scorecard.py | Graceful fallback for new fields |
| FeeEfficiencyPanel.tsx (portal) | Display advisor_effective_bps instead of fee_bps_weighted |
| types.ts (portal) | Added advisor_effective_bps, effective_split_pct fields |
| B_01b.classify_new_securities.py | NEW: auto-classify new securities after B_01 |
| gold_dispatch.sh | Wired B_01b into chains and groups |

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| DevOps deploy | docs/briefs/devops-brief-reborn-w5-deploy.md | DT + AE |

---

## Next Steps

- [AE] IAM policy update for openai-api-key on bd-exporter-ec2-role
- [AE] Deploy B_01b + gold_dispatch.sh to EC2 runner
- [AE] Run full gold pipeline to regenerate all artifacts with corrected classifications
- [DT] Deploy opal-partners-data Lambda (entity timeseries fast path)
- [DT] CloudFront invalidation after gold re-run
- [Andrew] Verify Assets Overview alternatives % matches Books tab after gold re-run
