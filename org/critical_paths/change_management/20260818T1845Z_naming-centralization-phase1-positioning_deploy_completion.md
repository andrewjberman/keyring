# DEPLOY COMPLETION LEDGER -- naming-centralization-phase1-positioning

**Opened:** 2026-08-18T18:45Z by 1.0.0_SA_CTO~X (Andrew-direct "Execute" on the 4-step naming
centralization; this is step 1 + the packaged-shadow decommission)
**Status:** CLOSED 2026-08-18T19:55Z -- all legs verified across THREE applies (v1.5.5 registry-first
names + shadow decommission; v1.5.6 BENCHMARK_ETFS names through the registry, closing the AGG/BIL
prediction gap the L7 verify caught; v1.5.7 vendored-module refresh after single-homing
etf_classifications_dynamodb.py at _shared). Final L7: served positioning_data.json == the full
5-change prediction EXACTLY (AGG/BIL/DIVZ/ICSH/IDVZ), 32/32 tickers, membership identical, non-name
payload byte-identical. Each apply: plan-scoped, 0-diff re-planned, deployed bytes re-hashed. No
stranded leg.

## Scope

One Lambda: `yang-generate-positioning` (yang-pipeline, TF module `generate_positioning`).
Changes: (a) display names resolve registry-first via `resolve_display_name` (etf-classifications
DynamoDB, same shared role/grant the attribution Lambda already exercises); inline
`ETF_NAME_OVERRIDES` (29 entries) DELETED; (b) the packaged-but-UNIMPORTED, 492-diff-line-stale
`etf_classification.py` shadow copy DELETED from the package (source-map files list updated).
Predicted served delta (computed pre-deploy against the live registry): exactly 5 name changes
(AGG/BIL/ICSH cosmetic-canonical; DIVZ/IDVZ to the Opal-branded names the portal already displays);
0 registry misses across 32 served tickers.

## Legs

- [ ] L1 commit source (yang lane)
- [ ] L2 build-and-upload yang-pipeline yang-generate-positioning
- [ ] L3 plan: exactly generate_positioning in-place
- [ ] L4 safe-apply
- [ ] L5 0-diff re-plan
- [ ] L6 record-terraform-deploy + tag yang-pipeline-v1.5.5
- [ ] L7 regenerate positioning_data.json via last production SFN input; verify served names ==
      the 5-change prediction exactly, all other payload identical

**Rollback:** prior artifact version retained in the versioned artifact bucket; re-apply.

**Closed:** (pending)
