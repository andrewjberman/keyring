# NFRA_GRAPHUNI.P1-B — INFRA + CROSS-STRATUM stitcher populator spec (STAGED)

**Author:** 0.8.0_AE_CloudComp~B (GRAPHDEPTH fleet — INFRA + CROSS-STRATUM populator)
**Date:** 2026-06-30  **Status:** STAGED (P1 GO 230512Z; fire-on-Phase-A-land). READ-ONLY so far — ZERO graph mutation pending ~D/~A node landing + ~D node-id convention.
**Pairs with:** P0-B denominator (dd50fa7f6) — this is the populate spec the denominator enumerated. ~D compute (P1) + ~A storage (P0-A) land the target nodes first; ~B is the fusion layer.

---

## 0. Fire-conditions (the sequencing gate — verified before each mutation)
1. comp-kuzu provenance `current` (pin == marker HEAD) — checked immediately pre-mutation. [Baseline: current, marker 7647070038814948852 @ 22:27Z, my on-demand derive.]
2. The stitcher's TARGET nodes exist (else dangling). Checked per-stitcher:
   - S1/S2 target ~D's PipelineScript / handler nodes (`MATCH node_type IN [PipelineScript,...]` > 0).
   - S3 targets ~A's S3Key nodes (bucket-qualified, ~C canonical id 02286234a).
3. ~D's PipelineScript node-id convention settled (OPEN — Q to ~D 231551Z) so RUNS edges target byte-exact (the glob=prefix-class dangling hazard ~D hit with ~A).
4. N-party /seams co-sign per spanned strata + ~C, via the canonical `rollup_defects()` one-head (~C's `multiparty_rollup()` harness, staged 95eac5d04).

## 1. The 4 stitcher families (spanned strata per P0-B §3)
| # | edge | edge_type (grain_contract) | targets (owner) | /seams sign-off | Phase |
|---|---|---|---|---|---|
| S1 | EC2_INSTANCE -RUNS-> PipelineScript | RUNS, levels=[ec2,lambda,stepfn] | ~D PipelineScript | {~B,~D,~C} | A (gold runners) / B (silver+ingestion runners) |
| S2 | LAMBDA -CONTAINS-> handler | CONTAINS, level=object | ~D handler/object | {~B,~D,~C} | A/B |
| S3 | LAMBDA -READS_S3/WRITES_S3-> S3Key (327; 87 lambda-only + 13 shared) | READS_S3/WRITES_S3, levels=[object,prefix] | ~A S3Key | {~B,~A,~C}; 13-shared {~B,~D,~A,~C} | A (coupled to ~A) |
| R1 | EC2/LAMBDA READS S3_BUCKET (coarse) <= fn READS_S3 S3Key (fine) | existential rollup_via [RUNS,CONTAINS,OWNED_BY] | derived | {~B,~D,~A,~C} | A (post S1+S3) |

## 2. S1 EC2-RUNS->PipelineScript binding (GROUNDED from EC2_MANIFEST.json — the keystone, ~B domain)
Each EC2 runner -> the script-source it runs -> the PipelineScript node(s) the RUNS edge targets. **GOLD runners fire in Phase A (~D's gold PipelineScript first); silver/ingestion runners' RUNS edges wait on Phase-B compute enrich.**

| EC2 runner (instance) | runs (source) | pipeline/tier | RUNS fires |
|---|---|---|---|
| inf-gold-layer-runner (i-0ed5afded2ebd4ed4) | data/inf/scripts/gold/*.py (orion-gold-dispatch.sh) | inf/gold | Phase A |
| inf-gold-qa-runner (i-04373615f03fbf9a9) | data/inf/scripts/gold/*.py (OUTPUT_PREFIX=qa/) | inf/gold-QA | Phase A |
| bd-gold-layer-runner (i-01003b035d2988dfb) | data/black_diamond/scripts gold (EVENTBRIDGE-only prod) | bd/gold | Phase A |
| bd-gold-qa-runner (i-0090b823a4a0997e3) | data/black_diamond/scripts gold (manual QA) | bd/gold-QA | Phase A |
| bd-gold-detail-generator (ephemeral) | infra/aws/ec2/bd-gold-detail-generator (user-data baked) | bd/gold-detail | Phase A |
| mdpf-daily-runner (i-02448edb624a7a7cf) | mdpf 4-stage chain (s3://opal-data-mdpf/code/, mdpf-daily-dispatch.sh) | mdpf/gold | Phase A |
| canonical-schwab-runner (i-0ed92ce2e72f505dc) | build_canonical_daily.py (17 silver + G1-G14 gold) | bd/schwab canonical | Phase A (gold part) |
| bd-allocations (i-0800437d1dbb0b5cc) | opal-bd-allocation-download SSM (s3://opal-data-bd/scripts/src/) + bd_price_update.py | bd/silver (alloc+price) | Phase B |
| bd-transactions (i-00c7568bc510f7423) | opal-bd-transaction-download SSM | bd/silver (txn) | Phase B |
| bd-fees (i-0868fc7e7ebec26f2) | download-daily-fees.ts -> convert_fees_to_silver.py | bd/silver (fees) | Phase B |
| bd-assets (i-0e6f6dc014fdcf1cd) | download-daily-asset-dim.ts (Step Functions) | bd/silver (assets) | Phase B |
| inf-bronze-runner (i-083ad9ae297f88e9f) | inf 9-dim bronze pulls (s3://opal-data-inf/code/bronze-runner/) | inf/bronze | Phase B |
| inf-exporter (i-081ae6aafb394fb1a) | Orion Playwright export | inf/ingestion | Phase B |
| bd-49f-auto-login (i-0fa1846f04ed7e337) | bd_49f_auto_login.js (BD 49F CV-login) | bd/ingestion (auth) | Phase B |
| canonical-schwab-si2 / "quartz-si2-spike" (i-0f3d57a97f14727af) | SchwabAutoDownload + SchwabS3Sync (C:\\SchwabData\\sync-to-s3.ps1) | schwab/ingestion (SI2 raw) | Phase B (ingestion-tier) |
| historical-prices-fetcher (i-00abf626b065373bc, x8 inst) | yfinance fetch (historical-prices-scheduler Lambda) | prices/ingestion | Phase B |
| etfs-reports-reporter (i-070477bf35fc54409) | render_month_end.py (data/etfs/scripts/presentation) | etfs/reporting | Phase B |
| smartx-exporter (i-06ebcb27395eb3f49) | run-all-portfolios.sh | smartx/export | Phase B |
| orion-crawl-harness (i-010f195f1798b40ad) | infra/aws/ec2/crawl-harness (Orion recon) | orion/ingestion | Phase B |
| astn-wsjft-scraper (i-0c8b110af37486ecc) | tools/astn_wsjft (run.py, analyze.py, fetch_ft.js) | astn/ingestion | Phase B |
| seeking-alpha-scraper (i-06376c11d8b3c3443, x2) | infra/aws/ec2/seeking_alpha_scraper | seeking-alpha/ingestion | Phase B |
| **m365-mcp-gateway (i-07dccb1615503ac99)** | app/server.py (MS MCP gateway) | — | **RUNS-EXCLUDE (service host, no pipeline script)** |
| **cot-exporter** | NOT IN EC2_MANIFEST.json (finding F5) | cot/export | binding TBD (see F5) |

## 3. S2 / S3 derivation (refs P0-B)
- **S2 LAMBDA-CONTAINS->handler:** each Lambda (174) -> its handler function (object grain). Source: Lambda function config `Handler` field (lambda-source-map / get-function-configuration). Targets ~D's handler/object nodes.
- **S3 LAMBDA-READS_S3/WRITES_S3->S3Key:** the 327 lambda-endpoint IO edges (from the TraceGraph LAMBDA-READS_S3/WRITES_S3->S3_ARTIFACT at key-grain — `derive_stitch.py` L135-145 already computes this). 87 lambda-only + 13 shared keys (~D 215302Z list). Targets ~A's bucket-qualified S3Key nodes; my edge target-id == ~A node-id (both-sign convergence). NOTE: `derive_stitch.py` (P2-STITCH) ALREADY emits LAMBDA-READS/WRITES->S3_DATA_KEY + STORED_IN(->bucket) — the GRAPHUNI head-pinned populate re-homes this to the grain_contract READS_S3/WRITES_S3 + OWNED_BY (~A) form. Reuse the TraceGraph derivation, not a new IO scan.

## 4. Findings (this spec adds 2 to P0-B's F1-F4)
- **F5 — cot-exporter not in EC2_MANIFEST.json (manifest gap, Rule 8):** an EC2 in the graph (31) but unregistered in the manifest. Route to 0.7.0 (manifest owner). Its RUNS->cot-pipeline-script binding must be grounded from elsewhere (the cot pipeline run config) for S1 completeness — flagged, not blocked.
- **F6 — quartz-si2-spike reclassified (corrects P0-B F4):** it is the `canonical-schwab-si2` box, a REAL SI2 Schwab raw-INGESTION runner (Win UI-automation), NOT a spike/experimental exclusion. ~D-confirmed it has zero GOLD-pipeline binding (correct — ingestion-tier PS, not gold Python), so Phase-A RUNS-exclusion CONFIRMED but a Phase-B RUNS-TARGET (ingestion-tier). Only `m365-mcp-gateway` is a permanent (service-host) exclusion.

## 5. Open dependencies (fire-blockers, not defects)
1. ~D PipelineScript node-id convention (Q 231551Z) — RUNS target format.
2. ~D PipelineScript nodes landed (gold first) — S1/S2 targets.
3. ~A S3Key nodes landed (bucket-qualified) — S3 targets.
4. The shared graphuni populate->Nessie commit entrypoint (Q to ~D) — so ~B commits via the same path, no 409 race.
5. ~C's `multiparty_rollup()` / `rollup_defects()` one-head — R1 + the N-party /seams sign-off (staged 95eac5d04).

---
*Staged 0.8.0_AE_CloudComp~B per P1 GO (COO~B 230512Z). The S1 binding is grounded (EC2_MANIFEST.json); S2/S3/R1 ref P0-B + the existing P2-STITCH TraceGraph derivation. Fires per-stitcher as ~D/~A land their nodes + ~D's node-id convention settles; each fire is provenance-gated + N-party /seams co-signed. RAVC2 COO~B as stitchers go GREEN-IN-SCOPE.*
