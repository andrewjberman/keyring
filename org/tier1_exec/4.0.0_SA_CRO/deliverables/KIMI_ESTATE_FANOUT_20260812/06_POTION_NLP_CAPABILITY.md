# FANOUT 06 — Potion/NLP capability (COMPLETE: main report received ~21:50Z on re-emit request + addendum ~21:35Z; FinBERT-subagent delta may still follow)

**Agent scope:** what NLP/semantic classification capability exists — DEPLOYED vs BUILT vs DESIGNED.
**Evidence class: agent-derived. This file carries the addendum verbatim; the main report appends on
receipt. The addendum's headline (Potion-axis retirement) is ALREADY twice-derived: fanout 07's agent
re-derived it independently from the commit record, and the underlying scan is a CRO~B first-party
deliverable — three agreeing derivations total.**

---

## ADDENDUM — embedding/vector census results (corrections and additions to the agent's main report)

**1. The estate USED to have a vector database — decommissioned 2025-12-26.**
`infra\aws\bedrock\BEDROCK_KB_RECREATION_GUIDE.md:1-25`: system `opal-market-update-analysis`,
**DECOMMISSIONED (2025-12-26), reason "Cost optimization ($216/month while unused)"**. Deleted:
OpenSearch Serverless collection `opal-analysis-vectors` (VECTORSEARCH, us-east-2), Bedrock Knowledge
Base ID `YXHLKMXOKT`, role `BedrockKBRole`. Embedding model **Titan Embeddings G1-Text v2, 1024-dim**
(`scripts/recreate-bedrock-kb-infrastructure.sh:153`). What remains is a recreation runbook + shell
scripts (8 files, not Terraform, not applyable). **Prior art: standing vector-search infrastructure
was torn down as unused cost** — consistent with the 2026-07-30 live census
(`AWS_ESTATE_CENSUS_20260730/SLR_REVIEW.md:11-12`, 0 domains / 0 collections, SLRs marked DELETE).

**2. Two dead callers left behind by that teardown** (DEAD, not dormant):
- `tools\market_update\components\news_recap\generate\rag_retriever.py:22` imports
  `corpus.vector_index` — **the package was swept 2026-08-04 (@201610e2e8, 371-file archive batch)
  and the caller was not removed**; any import raises ModuleNotFoundError. Both its backends (FAISS
  index, Bedrock KB) are gone. `faiss-cpu>=1.7.4` survives orphaned in root `requirements.txt:20`;
  **zero `import faiss` anywhere in the repo**.
- `tools\news_scanner\scripts\utilities\query_keyword_clouds.py:36-70` — an OpenSearch client against
  index `trending_vectors`, referencing a `create_opensearch_cluster.py` that exists nowhere.

**3. The deployed news-pipeline similarity path (sharper detail).**
`news_semantic_clustering/lambda_function.py:379-470` caches 384-dim MiniLM vectors as DynamoDB
attribute `embedding_384` (write-back :518) — **the estate's de-facto vector store, but a CACHE, not
a searchable index**; clustering is HDBSCAN (:145), relevance is cosine-to-centroid
(`scoring_utils.py:81-116`), vectors int8-quantized to base64 for JSON (:237-282). Downstream,
`semantic-news-layer3-curation/lambda_function.py:398-406` computes a **hand-rolled pure-Python dot
product** over normalized centroids (no numpy); `news_layer3_curation` injects the similarity list
into a GPT prompt (:1235, :1409, :1514). All three Lambdas live (verified via
get-function-configuration per the agent).

**4. Negative-space confirmations, with denominators.** 400 `.tf` files scanned: `aws_opensearch*` 0
· `aws_kendra*` 0 · `aws_elasticsearch*` 0 · bedrock-KB 0; the only live Bedrock IAM grant is
`stability.stable-image-*` (image gen, `shared-infra/opal-portal-lambda-role.tf:107-122`).
`TruncatedSVD` 0/26,109 files (the PPMI-SVD prototype hand-rolls `np.linalg.svd`). `qdrant` 0. All
371 `knn` hits are `pickNna`/Net-New-Assets TSX; all 51 `chroma` hits are CSS vocabulary; `pinecone`
(12) and `weaviate` (4) are 100% prose — never imported. Tool-rail purity: **0 of 92** `.tools/*.py`
import numpy; in `org/modules/graph/`, exactly **1 of 247** does — `potion_embed.py`.

**5. Two name-collision traps for later censuses:** `org/modules/graph/nerves_lexical.py` is regex
entity-linking, not lexical ranking; `org/modules/graph/vectorize-audit/` has nothing to do with
vectors (audit-chain vocabulary). `NFRA_MOTIF_P2_c3_emergence.py:13-14` matched only because it
*asserts the absence* of embeddings ("NEVER embedding-similarity... every edge is a node_id
set-intersection").

**6. Supply-chain delta:** the AKPIPE Lambda proposal specifies **potion-8M** from a Lambda layer
(`/opt/potion-base-8M`), the vendored one-home module ships **potion-2M** (hash-pinned), and a
HF-cache path exists via model2vec in `akpipe_scorer.py:167` — **three distinct Potion supply chains
on paper.**

**7. Independent re-derivation of the Potion-axis retirement** from the commit record
(@013b204312): **retired at gate severity 2026-08-11 — real cosine below the decoy null's p99 on all
28 verticals, positive control admitting at rank 0 — while BM25 carried 28/28.** Two independent
derivations agree (three counting the CRO~B first-party scan).

**Agent's closing note:** the FinBERT/news-NLP subagent still running; anything beyond the live-AWS
reads already established (function configs, rule states, the handler-contract mismatch, the
missing-trigger orphan) will be relayed on its notification. **Main report appended below.**

---

# MAIN REPORT (verbatim, re-emitted ~21:50Z) — NLP / SEMANTIC-CLASSIFICATION CAPABILITY, GROUND TRUTH

**Workspace HEAD:** 4b76525ba3 (CLOUD, dirty tree). Live-AWS reads run 2026-08-12, account 313476888478, us-east-1.

## 0. BOTTOM LINE — the three buckets

DEPLOYED: FinBERT sentiment (opal-news-ai-sentiment, container Lambda) + batch driver (finbert-batch-processor, 14 ENABLED cron fires/day) [live get-function-configuration + live list-rules]. OpenAI text-embedding-3-small + HDBSCAN + GPT-labelling inside news-trending-analysis [live, 2 ENABLED fires/day]. Kimi K3 prose-proposal loop on estate-report-runner EC2, schedule estate-report-0900et ENABLED [live EC2 + scheduler].
DEPLOYED-BUT-DORMANT: news-semantic-clustering (sentence-transformers all-MiniLM-L6-v2) — function exists, ZERO EventBridge rules target it [live function + full 139-rule materialised sweep].
BUILT (local only): POTION static embedder, vendored + hash-pinned, wired LIVE into comp-which routing on this machine [exercised: loads, dim=64]. The C3.ii semantic vertical scan (Potion + BM25, ablated, decoy-null gated) — already RUN over 5,865 docs [committed artifact + script].
BUILT-NOT-DEPLOYED: NFRA_AKPIPE arxiv Lambda (BM25 + potion-8M), self-labelled "PROPOSAL, NOT A DEPLOY" [absent from the 197 live functions]. 5-lexicon SentimentAnalyzer (Loughran-McDonald/VADER/NRC/Harvard-GI/FinSenticNet, ~12.9 MB dictionaries) [no TF, no source-map, no EC2 entry].
DESIGNED ONLY: the materialized content substrate (docs.jsonl), the .tools/content/ partition, llm_class producer, RRF-over-axes fusion [measured zeros below].

**No vector database, no managed search, no hosted model endpoint in this account.** Live, rc=0, positively controlled: opensearch list-domain-names returns empty; kendra list-indices empty; sagemaker list-endpoints empty; bedrock list-custom-models empty.

## 1. POTION — what it is, exactly where it runs

A vendored static-embedding table, not a service: minishlab/potion-base-2M (model2vec distillation of baai/bge-base-en-v1.5), pinned to HF revision 389b9f64be5aa4ae7a6bc6fe95ef20ce485ae5da (org/modules/graph/potion/MANIFEST.json). Runtime dim 64. Two git-tracked files: model/model.safetensors (7,559,256 B) + model/tokenizer.json (683,666 B), each SHA256-pinned. Engine org/modules/graph/potion/potion_embed.py — data-not-code (:9-15): runtime loads table+tokenizer, ZERO model2vec import at inference; mean-pool + L2-normalize (:69-75); hash mismatch fail-closed (:57-64); load_embedder() returns None on failure with an ALARM to stderr (:93-96).

EXERCISED: embedder loads, dim=64; cos("what lambdas read from the opal-data-bd bucket", "which functions consume that s3 data") = 0.5409 vs cos(..., "portfolio tax lot harvesting") = 0.0903. It discriminates.

THREE call sites, all LOCAL: (1) comp-which routing — LIVE on this machine (.tools/comp-which:1887 build_provider inside _shape_b_relevance_route; "NFRA_COMPROUTE Charter-1 LIVE FLIP (CTO-authorized 20260707T080634Z, CVO~B E1 PASS)" :1878; two-pass route, lexical Shape-B pin then semantic; caveat: the semantic path EXECUTES, but whether it CHANGED the answer for a given query was not proven — the Shape-B pin can preserve the lexical top-1 by design). (2) the C3.ii scan (section 3). (3) akpipe_scorer.py:167-172 — loads Potion via model2vec from HF cache, NOT the vendored hash-pinned module: same model, different supply chain, no hash pin (two-homes divergence).

POTION HAS ZERO PRESENCE IN AWS: comp-find -i potion infra gives 13 hits across 7,737 files, ALL DOC band (CONTENT_MODULE_DESIGN.md prose). model2vec/safetensors/tokenizers in zero requirements/Dockerfile/toml — no packaging path by which Potion currently reaches AWS.

## 2. CONTENT_MODULE_DESIGN.md — the design and its status

STATUS verbatim (:4-11): "DESIGN, in progress — HOUSEKEEPING-RECONCILED 2026-08-11 (CVO, ontology home) ... Nothing built yet; the CORE audited clean, zero partial residue."

Key elements: RRF-over-axes as the flow-substitute (C1 edges computed from relatedness by version-pinned functions, :66-69; axis table :82-87 marks BM25 YES via comp-similar, heat YES, Semantic buildable, co-change partial). Deterministic-pinned WITH the CVO C-1 correction on record (:57-58): "Potion IS a static-embedding MODEL = inference, but deterministic-given-a-pinned-model; the honest guarantee is deterministic + PINNED + reproducible." Ablate-don't-fuse (C-2 :58). Decoy-null threshold (:55-56): anchor to the 99th pct of random-pair RRF, explicitly not comp_similar.py:70's SIM_TWIN=0.60. Blinded negative control (:157-166) — structurally-matched random decoy clusters, pre-registered pass bar ("a reader supplies coherence [apophenia], so it measures the READER"). Section 8 recovery bar (:182-187): a semantic axis earns its place ONLY by recovering items BM25 structurally misses, measured on the bm25-ABSENT set. SLM/LLM rerank DEFERRED by Andrew (:190-191). Section 9 materialized substrate (:203-236): periodic Lambda/EC2 ingest under a scoped MS service principal writes content/substrate/{site}/{drive}/docs.jsonl; the engine consumes THAT, never live-crawls.

Status of each piece, measured: the doc DESIGNED (mtime 2026-08-11, actively reconciled). Reference implementation BUILT — infra/system/ontology/content_relate_prototype.py (17,061 B, tracked; self-describes "validated reference implementation (self_test PASS, deterministic) ... NOT YET a registered .tools/content/ comp-tool"). .tools/content/ DOES NOT EXIST. docs.jsonl DOES NOT EXIST (comp-find --name: 0 hits / 26,108 files). RRF ABANDONED IN PRACTICE — prototype :26-28 iter-1 finding: "the null-anchored gate is on ABSOLUTE per-axis scores, NOT RRF ranks — RRF fuses ranks into a corpus-INVARIANT 1/(60+rank) distribution, so decoy-RRF == real-RRF and cannot discriminate"; RRF census 425 hits/26,113 files, DEF band 3 (1 numpy false positive) — exactly ONE implementation estate-wide (akpipe_scorer.py:187), labelled "ORDERING diagnostic ONLY". Co-change axis BLOCKED (:33-44): ms_heat_snap frozen since 2026-07-17; the doc's own rule: revive or declare HONEST-BOUNDARY-UNAVAILABLE.

## 3. THE MOST IMPORTANT FINDING: the C3.ii scan already ran, and Potion scored ZERO

BUILT and EXECUTED — the closest existing thing to the estate-wide inferential scan. Script c3ii_semantic_scan_v2.py (tracked @013b204312); artifact C3II_SEMANTIC_SCAN_V2_OUTPUT_20260811.json (435,993 B); report C3II_COMPREHENSIVE_SEMANTIC_COVERAGE_SCAN_20260811.md. Implements the CONTENT_MODULE_DESIGN pattern exactly: Potion cosine AND BM25 ablated never fused (:16-17), pooled Monte-Carlo decoy null, family-wise threshold quantile(1-0.05/N) (:171-177). Corpus 5,865 docs plane-labelled (docs 1,009 / projects 307 / logs 4,549); 28 ratified verticals; queries derived.

THE MEASURED RESULT (re-derived from the artifact by this agent): VERDICTS over 28 verticals: all COVERED. total potion admits = 0, bm25 admits = 1824; potion_only = 0, bm25_only = 1824. Potion admitted ZERO documents across all 28 verticals at fw, p999, AND p99. Per-vertical example (news): decoy-null p99 = 0.8486, real max cosine = 0.7942 — a random-token query cosines HIGHER than the real enriched query. Mechanism + control on the record (:139-150): the 64-dim mean-pool maps generic corpus prose near every document (centroid effect); the isolated positive control (verbatim-doc query) self-cosines 1.0 against fw 0.9306 and admits at rank 0 with 15 total admits — the gate discriminates; the zero is a TRUE NEGATIVE about short topical queries on this embedder. Verdict on the record: "THE POTION AXIS IS RETIRED AT GATE SEVERITY FOR QUERY-SHAPED RETRIEVAL." The canonical per-vertical verdict rides BM25. Downstream, kimi_call1_friction_v2.py:36 consumes admitted.bm25 only, retrieval note :45: "semantic axis retired at gate severity (measured; positive-controlled)."

THIS IS THE SINGLE MOST CONSEQUENTIAL FACT against "C3.ii becomes entirely inferential, driven by potion/NLP": on this estate's own corpus, with its own null gate, Potion has already measured at zero recovery for query-shaped retrieval — and the ablation is what made that visible. (Cascade budget re-derivation already flagged in the ruling record itself.)

## 4. PRODUCTION NLP TODAY — the news pipeline

Denominators: 197 Lambdas materialised (auto-paginated, NOT --query length); 13 matched the NLP pattern; 139 EventBridge rules materialised; 31 NLP-relevant; 16 Scheduler schedules.

FinBERT: opal-news-ai-sentiment live (PackageType=Image, 3008 MB, LastModified 2026-02-21); source layer2_finbert_scoring/lambda_function.py:52-53 ProsusAI/finbert; 3-class to signed scalar [-1,+1]; DDB attrs sentiment_finbert/_label/_confidence. Driver finbert-batch-processor live (py3.11, 256 MB, 900s); rules finbert-scoring-post-ingestion cron(10 2,4,12,14,16,17,18,20,21,22,23 * * ? *) + -45min cron(55 0,13,20 * * ? *) = 14 fires/day, both ENABLED live-verified. Code managed OUTSIDE TF (finbert-batch.tf:34-37 ignore_changes) — repo file is not evidence of running bytes.

Live embedding path is OPENAI, not local ML: news-trending-analysis (py3.12, 10240 MB, LastModified 2026-06-11) calls embeddings.create(model="text-embedding-3-small", dimensions=256) at lambda_function.py:968-969, then HDBSCAN, then GPT cluster-labelling (:884,:891,:907); requirements = openai, numpy, hdbscan — no torch, no transformers. Rule ENABLED, 2 fires/day.

DEPLOYED BUT ORPHANED: news-semantic-clustering (Image, 3008 MB, LastModified 2026-02-21) imports sentence_transformers (:32), model all-MiniLM-L6-v2 (:397). NO EventBridge rule targets it (full 139-rule sweep); eventbridge.tf:14 records the two clustering rules DELETED. Its Dockerfile is unbuildable as committed (COPYs an absent text_cleaner.py) — INFERRED the live image predates that.

BUILT-NOT-DEPLOYED: sentiment_analyzer.py 5-lexicon engine (LM 7 financial dimensions :63-70, VADER, NRC, Harvard-GI, FinSenticNet), 6-axis output schema v5.0; ~12.9 MB dictionaries present. Zero source-map/TF/EC2 entries.

Heavy-ML discriminator: torch/transformers/sentence-transformers appear in exactly 2 real dependency files, both backing container images, both last deployed 2026-04-28 per source map, NEITHER built by CI (lambda-deploy.yml handles zips only; no ECR/docker path). No Lambda layer carries torch or transformers.

Two seams, both INFERRED, both need a live DDB/ECR read: (a) the mapped layer2 handler ignores event and table-scans (:247) while the batch driver invokes per-text with a text payload — incompatible contracts, so the ECR image cannot hold the mapped source; (b) news_layer3_curation :1812 projects sentiment_score but every writer writes sentiment_finbert — that branch likely yields 0.0 silently.

## 5. EMBEDDING / VECTOR / SIMILARITY INVENTORY

Potion 64-dim (org/modules/graph/potion/) BUILT local, live in comp-which. OpenAI text-embedding-3-small 256-dim DEPLOYED 2 fires/day. MiniLM-L6-v2 DEPLOYED no trigger. BM25: 768 hits/26,113 files, DEF band 13 — content_relate_prototype.py:63; debtscan/dup_scan.py:84 (class BM25, the base engine); state_scan.py:232 (what /comp-state runs on); dup_scan_proto.py:42; akpipe_scorer.py:52,53,59,183; NFRA_AKPIPE_LAMBDA_PACKAGE/lambda_function.py:59,145; c3ii_semantic_scan.py:85; c3ii_semantic_scan_v2.py:142. comp-similar = BM25 over resource summaries, no embeddings. PPMI-SVD semantic axis BUILT prototype-only (SVD_DIM=8). RRF: ONE implementation, demoted to ordering-diagnostic. Vector DB / Kendra / SageMaker / Bedrock custom: NONE (live, rc=0, positively controlled). NFRA_AKPIPE_LAMBDA_PACKAGE: "THIS IS A PROPOSAL, NOT A DEPLOY" verbatim :3; live-confirmed absent among 197. Local laptop: model2vec 0.8.2, safetensors 0.7.0, tokenizers 0.22.2, numpy 2.4.2, torch 2.10.0+cpu, transformers 5.3.0, sentence_transformers 5.2.3, sklearn 1.8.0, hdbscan — the full ML stack exists on the dev machine and nowhere in AWS.

## 6. comp-read / comp-find / comp-which — semantic?

comp-find: NO — deterministic 7-band grade ladder (:61-78, :221-231); ":16-18 NO SLM. NO LEARNED RERANK ... a non-deterministic rail cannot be a control"; explicitly refuses corp_write's CatBoost/qwen3 reranker (:24-26). comp-read: NO — BM25-lite salience over one file (:289); ":38-40 Andrew-direct 2026-08-06: NO MODEL. NO EMBEDDINGS. NO NETWORK. NO CACHE ... 'We dont need an slm for this, it is important that it functions in milliseconds'". comp-which: YES — the ONLY semantically-ranked comp-tool: Potion cosine primary relevance into a folded posterior, lexical exact-NAME boost, Shape-B lexical top-1 preserve pin (:1878-1904); structural gates remain hard backstops; fail-safe degrades to lexical. Design: docs/architecture/NFRA_COMPROUTE_POTION_DESIGN.md sections 2-5. comp-similar: NO (BM25).

## 7. COMPUTE SUBSTRATE for an estate-wide inferential scan

Container-batch substrate DEPLOYED: ECS cluster opal-globgrph, 7 ACTIVE task-definition families (derive-runner, cse-producer, resource-summaries-producer, comp-learns-producer, fedobs-producer, nessie, trino); globgrph-cse-producer-nightly ENABLED; ms_cloud_extract.py already ships inside the derive image (Dockerfile:80, imported derive_runner.py:42). Transient EC2 LLM runner DEPLOYED: estate-report-runner i-0512bd3cbaf602b7f t3.medium stopped, launched 13:00Z today; schedule ENABLED; ALLOWLIST permits description/enrichment/classification(+reason) ONLY — deterministic fields compiled, cannot be proposed against. (Manifest's pinned id i-04981b6aec3bed86b returns EMPTY — the documented id-churn class; resolved by Name tag.) Lambda viable-but-constrained: two 3008 MB container Lambdas carry ML runtimes with HF caches at /tmp (lambdas.tf:167-170); no CI builds them, publishing manual. LLM inference channel is EXTERNAL API (Kimi K3 moonshot.ai, key astn/kimi/api-key; news embeddings OpenAI). Nothing self-hosted. Scale reference: the 5,865-doc x 28-vertical x 25-decoy scan ran on the laptop. MS estate 5,886 nodes / 28.5% not structurally derivable — a CRO deliverable claim this agent did NOT independently re-derive.

## 8. COULD NOT DETERMINE

Whether the deployed finbert-lambda:latest image matches its mapped repo source (handler-contract mismatch says it cannot; image opaque without an ECR pull — Rule-22a CODE layer, unresolved). A source-map/live discrepancy left unasserted: source map claims last_deployed 2026-04-28 for opal-news-ai-sentiment while live LastModified is 2026-02-21 (an ECR :latest push does not update LastModified without UpdateFunctionCode — both readings can be true of different things). Whether the 14 daily finbert-batch fires SUCCEED (needs CloudWatch; ENABLED is not evidence the job works). Whether sentiment_score exists as a live DDB attribute. Whether comp-which's semantic ranking CHANGES outcomes in practice (path proven to execute; effect needs the shadow eval, comp_route_eval.py).

Two observations surfaced-not-chased: (1) c3ii_semantic_scan_v2.py:34 + kimi_call1_friction_v2.py:26 hardcode the C:\Users\AndrewBerman workspace root — device-specific logic in a device-agnostic repo. (2) akpipe_scorer.py:167 loads Potion by a second unpinned supply chain — one logical model, two independently-editable load paths.
