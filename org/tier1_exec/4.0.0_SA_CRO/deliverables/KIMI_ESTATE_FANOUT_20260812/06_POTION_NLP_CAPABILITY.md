# FANOUT 06 — Potion/NLP capability (PARTIAL: embedding/vector-census ADDENDUM received 2026-08-12 ~21:35Z; the agent's main report §1-§6 still owed while its FinBERT sweep completes)

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
missing-trigger orphan) will be relayed on its notification. **Main report §1-§6 appends here on
receipt.**
