# WS-E — Cottonwood BD Model-Portfolio Discovery (lane ~A)

**archetype:** EXPLORE
**secondary_archetypes:** TRACE, VALIDATE, SCRIBE

**Agent:** 0.6.2_AE_PartnerETL~A · **Window:** 2026-07-21 ~17:44Z -> ~18:56Z · **Session:** WS-E discovery (spawned this session)

## Summary

Spawned for WS-E of OPAL_CONSOLIDATION: find WHERE Cottonwood marks Model Portfolios in Black Diamond, characterize the shape + value/count, design the opal-data-assets daily fold-in. DISCOVERY-ONLY, cot READ-ONLY + LOCAL (Andrew grant @b5af1e929). Delivered a grounded answer, resolved 3 CTO disposition items, and taxonomy-aligned the fold-in design — all read-only, zero writes to BD/cot, zero cross-firm.

**Core finding:** the models are NOT in DataMining. They live in the **Black Diamond Rebalancer** app (`rebalancer.bdreporting.com` > StrategiesAndModels). DataMining only projects a sparse (currently snapshot-frozen) assignment dimension. Cottonwood has **60 models**; scope = strict "Opal" in name (Andrew-ruled) -> **17 in / 43 out**, 296 assigned accounts across the 17.

## Work done

1. **Discovery path (EXPLORE/TRACE):** DataMining catalog sweep (querytypes 1..25, roster) -> confirmed the model marker is `accountRebalStrategyID/Name` (Rebalancer "Account Strategy"), sparse (2/642 on the last non-frozen date 06-09). Read landed cot silver/allocations + holdings -> confirmed the DataMining dim under-populates and current feed is 0-row (known cot snapshot as-of latent bug, `cot_bronze_ingest.py:92-93` — NOT closed). Pivoted per Andrew's steer ("find the endpoint") to live read-only discovery of the BD Rebalancer app JS/config/module-map -> located `rebalancer.bdreporting.com`, `RebalancerModels/RebalancerStrategies` modules, API base `apiBase=rebalancer.bdreporting.com/request/api`.
2. **HAR-driven resolution (VALIDATE):** Andrew provided a live-UI HAR. Parsed it -> exact endpoints + shapes without any POST of mine: `POST /api/models/strategies/search` (roster, totalResultCount=60), `GET /api/models/{id}` (composition). **Join key proven by exact GUID match:** DataMining `accountRebalStrategyID` === Rebalancer `model.id` (439fc4b6=Opal Satellite 80, c973839d=Opal Long Term Conservatiove). **Blend shape:** recursive hierarchy `model -> children[] (weighted sub-models, relativeAllocation) -> components[] (securities: metadata.symbol + absoluteAllocation + AssetId)`; blend split = `children[].relativeAllocation` (sum 1.0). Live blend example: Opal Conservative Growth 0.4565 / Opal Intermediate-Term 0.4565 / Opal Ultra Short-Term Income 0.087.
3. **Andrew MDPF count-vs-$ requirement:** satisfiable directly — blended acct = +1 count per underlying primary Opal model, $ = account_value x child.relativeAllocation.
4. **CTO 3 disposition items resolved (no new egress):** (2) strict Opal filter -> 17 in / 43 out, "Opal Satellite NN" vs "Core|Satellite NN" are DISTINCT families cleanly split by the name filter (no Andrew round-trip); (1) Rebalancer AUTHORITATIVE for assignment (296 accts) vs DataMining 2 (under-reports) -> Rebalancer primary, freeze-fix = reconciliation cross-check only; explicit per-account list needs one more Rebalancer endpoint (PRD: fresh HAR or scoped live read); (3) Strategy-vs-Model union confirmed.
5. **Taxonomy alignment (SCRIBE):** grounded the estate layout + read `OPAL_CONSOLIDATION_TAXONOMY_STANDARD.md` §A/§D. Corrected the prefix: cot models land at `blackdiamond/cottonwood/{layer}/{type}/{date}` (cot is a SCOPE under the `blackdiamond` source, NOT a top-level `cot/` — grounded: 6 live sources, blackdiamond scopes = {49f, cottonwood}). Aligned §7 to bronze-raw-json / silver-fact-parquet / gold-dim / meta-manifest + mirror the `opal-assets-bd49f-*` trigger + firm-sep by scope + absence-twin deferred (alert enforcement paused).
6. Corrected a stale figure: fresh cot AUA ~$437.1M/845 accts (holdings 07-17), vs my initial $372.9M/642 (06-09 backfill).

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| safe-commit (surface-check) | PASS | 4 commits, each "OK: touch no critical surface" (doc-only) |
| safe-commit (risk-reflex / comp-pulse) | CLEAN | each: DENOMINATOR 1 file vs 1239 danger nodes, REFLEX CLEAN |
| commit-gate | PASS | markdown-only commits (no .py) |

**What worked:** the estate grounding via boto3 ListObjectsV2 (source/scope map) + the taxonomy doc gave a precise, firm-clean prefix ruling. **What failed:** n/a. **Gap:** no comp-tool covers a VENDOR-API surface (BD Rebalancer) — it's off the estate graph; discovery ran via native Read/Glob/Grep + boto3 data-plane reads + GET-only bundle fetches (all off-rail-legal: data-plane + non-estate). The HUD nudged once (S3-key search) on a JS-bundle probe — not applicable, proceeded.

## Files Modified

See commit messages: `8db94105b`, `4adbdb831`, `c10dbd81d`, `772ac6934` — all one file: `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/COT_MODEL_PORTFOLIO_DISCOVERY_WSE_20260721.md` (the deliverable, built incrementally: discovery -> Andrew ruling -> CTO items -> taxonomy alignment). Pushed to CLOUD.

## MCP traffic

~10 messages. Significant: received MSTR + CTO WS-E GO briefs (ACKed both); received + ACKed COO egress-boundary reinforcement (confirmed cot read-only + LOCAL); reported findings -> CTO (CC MSTR); CTO ACCEPTED discovery + §8 + §7; MSTR ACK (stand-by, likely fold-in builder). No dispatches issued (worker lane).

## Blockers

None self-owned. The one remaining live need (explicit per-account -> model assignment endpoint) is NOT a blocker — CTO carries it as a PRD decision (fresh HAR from Andrew OR a scoped live read on a fresh per-use word). My per-use egress grant is SPENT.

## Current State (handoff)

- **Deliverable** `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/COT_MODEL_PORTFOLIO_DISCOVERY_WSE_20260721.md` @772ac6934 (CLOUD) is complete + taxonomy-aligned = the basis for CTO's WS-E production PRD.
- **Model store:** BD Rebalancer, `rebalancer.bdreporting.com`. Auth = mint bearer at `GET rebalancer.bdreporting.com/auth/token` (cot OIDC cookie `blackdiamond/cot/session`). Endpoints (read): `POST /api/models/strategies/search`, `GET /api/models/{id}`, `POST api.bdreporting.com/ModelMarketplace/subscriptions/summary`.
- **Join key:** DataMining `accountRebalStrategyID` === Rebalancer `model.id`.
- **Fold-in target prefix:** `s3://opal-data-assets/blackdiamond/cottonwood/{bronze|silver|gold|meta}/{type}/{date}` (firm-clean; NOT a top-level cot/). silver = fact_model_definition / fact_model_blend / fact_model_assignment; gold = dim_model_portfolio -> MDPF DDB.
- **Scratchpad artifacts** (session-local, NOT committed): `…/scratchpad/cot_discovery/` (querytype catalog, HAR extracts, model roster, model-detail JSON, api-surface maps). Token never persisted.
- **Status:** WS-E discovery + design CLOSED on my side. IDLE/available, standing by reachable (persistent Monitor `blcpcdveq` live).

## Next Steps

- **[1.0.0_SA_CTO]** author the WS-E production PRD from this deliverable; decide the assignment-source endpoint (fresh HAR vs scoped live read); gate the cloud-side build. I hold the deepest context — likely the fold-in builder.
- **[0.6.2_AE_PartnerETL~A / self]** stand by reachable for the WS-E PRD/build or COO context-reallocation. No further cot BD calls without a fresh Andrew per-use word (grant spent). If Andrew provides an account-assignment HAR, parse it to nail the per-account->model endpoint.
