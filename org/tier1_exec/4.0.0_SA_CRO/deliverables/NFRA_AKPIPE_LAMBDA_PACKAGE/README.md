# NFRA_AKPIPE — production Lambda package (PROPOSAL, for CloudOps/AE + CTO)

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Recon ID:** RCN-0003 — registered in RECON_REGISTER.md
**Spec:** [`../../briefs/NFRA_AKPIPE_BUILD_SPEC_20260723.md`](../../briefs/NFRA_AKPIPE_BUILD_SPEC_20260723.md)

> **THIS IS A PROPOSAL PACKAGE, NOT A DEPLOY.** It sits in the CRO deliverables tree because
> `infra/aws/**` is an **AE lane** and every apply is **CTO-gated**. The CRO authored and
> validated the logic; it does not place or apply infrastructure. The Terraform is deliberately
> named `main.tf.proposal` so no `terraform` run can pick it up from this path.

## Contents

| File | What it is |
|---|---|
| `lambda_function.py` | The daily handler: harvest → dedup → full-text → score → DDB+S3 → whole-corpus recompute → watermark. Compiles clean, ruff clean. |
| `main.tf.proposal` | Lambda + DDB + S3 + EventBridge + scoped IAM. **Rename to `main.tf` only after relocation.** |
| `build_profile.py` | Builds the **pinned idf** profile artifact. Exercised on the real 182-row substrate. |

## Handoff steps (AE, then CTO)

1. **AE relocates** to `infra/aws/lambda/akpipe/`, renames `main.tf.proposal` → `main.tf`.
2. **AE registers** the Lambda in `infra/aws/lambda/ci/lambda-source-map.json` (Deployment Rule 4).
3. **AE builds layers** (Rule 3 — deps in layers, never `pip install -t .`): `model2vec`, `numpy`,
   `pymupdf`, and **potion-base-8M baked in at `/opt/potion-base-8M`**. The model must ship in the
   layer — a runtime HuggingFace download would be **undeclared egress** outside the arxiv-scoped grant.
4. **Build + upload the pinned profile** to `s3://<bucket>/_profile/akpipe-profile-v3.json`
   (see the gap below first — the reference corpus needs fixing).
5. **CTO gates the apply** via `.tools/safe-apply.sh` — never bare `terraform apply`.
6. **Open a deploy-completion ledger entry** at deploy-start, close it at completion (NEVER-rule 5).

## IAM — this is a NEW-RESOURCE case (CLAUDE.md Rule 22a)

**`comp-iam` FAILS GREEN here.** It models `(action)`, never `(action, resource)` — a role holding
`s3:GetObject` on any bucket reports GRANTED for a call to this new one. Verify on the live primitive,
**one `--resource-arns` per call**, **positive control as a separate invocation**:

```
aws iam simulate-principal-policy --policy-source-arn <role> \
  --action-names dynamodb:PutItem --resource-arns <exact table arn>
aws iam simulate-principal-policy --policy-source-arn <role> \
  --action-names s3:PutObject --resource-arns <exact bucket arn>/*
```

## Egress boundary

The Lambda's **only** external destinations are `export.arxiv.org` and `arxiv.org`. That is the
concrete extent of the standing grant (Andrew-direct 2026-07-23, amended 2026-07-23 to permit
local dev runs; production stays cloud-Lambda-only). Nothing else — including model downloads.

## What is PROVEN vs what is NOT

**Proven, by exercise on real data (182 papers, 3 age bands, local dev runs):**
- Harvest, scope filter, full-text fetch (`/html` render with PDF fallback), contact-ID
  (emails on 8/12 full-text papers; 588 authors captured), substrate write.
- Scoring core: 6/6 acceptance checks pass offline — positive control, degeneracy, ablation,
  determinism, recompute monotonicity, and the composition-sanity regression.
- **Recency exercised**: the highest-relevance paper in the corpus (0.894) correctly ranks *below*
  a fresher 0.808 paper because it is ~14 days old. The relevance/recency tradeoff behaves.
- **Length bias** reduced from `corr=+0.60` to `+0.26`.
- Retry/backoff honoring `429/503 Retry-After` (added after I tripped arxiv's rate limit).

**NOT proven — declared, not hidden:**

1. **⚠ THE PINNED-IDF REFERENCE CORPUS IS WRONG AS BUILT — fix before deploy.**
   `build_profile.py` computes idf from **title + abstract**, but production scores **full text**.
   Measured consequence: 54/85 phrases have `df=0` in the 182-abstract reference — including
   *every* retrieval phrase (`retrieval augmented generation`, `dense retrieval`, `semantic search`,
   `reranking`, `vector database`). Those phrases demonstrably DO occur in full text (they drove the
   top full-text results). Zero-df ⇒ maximum idf ⇒ a single body occurrence would score enormously.
   **Idf must be built from the SAME text basis used at scoring time (full text), over a corpus far
   larger than 182.** The mechanism is right; the input is not. This is the top build item.
2. **Ranking quality is only partially proven.** Topical discrimination looks right on inspection and
   the off-target tail scores exactly 0.0 — but there is still no blinded relevance judgement. The
   honest bar (CONTENT_MODULE_DESIGN §7, CVO) is a **decoy null**: structurally-matched off-topic
   papers, pre-registered pass bar, blinded. Not yet run.
3. **`BM25_SAT_C = 6.0` is PROVISIONAL** — deliberately *not* tuned to the sample (that would be the
   Goodhart failure the estate keeps naming). Calibrate against the decoy null.
4. **Potion stays demoted.** Measured CV 0.088–0.165 vs BM25's 0.695–1.985 — near-constant *within*
   CS papers. It guards against non-CS noise, it does not rank. One weak counter-signal is on the
   record (2 papers promoted into a top-5 on n=12) — that is **recorded to re-measure on a larger
   slice, not acted on**.
5. **The handler has never run in AWS.** It compiles and its scoring path is exercised locally, but
   DDB conditional-put, the whole-corpus recompute pagination, and the watermark have not been
   exercised against live AWS. **Deployed ≠ working** — first invocation must be verified against the
   served artifacts, not a green apply.

## Design contracts worth not breaking

- **Lossless**: dedup key `(arxiv_id, version)`; a new version is a NEW row; `attribute_not_exists`
  conditional put; S3 versioned with **no expiry**; the watermark advances **only** on a fully
  successful window.
- **Daily recompute**: `derived_state_rank = recency_decay × nlp_score` is re-derived for the whole
  corpus each run (age moved for everything) and stamped with `rank_asof_date`. Components stay
  stored so any reader can **independently recompute and check** the stored rank.
- **RRF orders, it never multiplies.** RRF has ~3% dynamic range vs recency's 16× — multiplying by it
  let noise outrank a perfect match (the v1 defect, regression-tested at spec §7.6).
- **Normalization is load-bearing.** `closed-loop` must match `closed loop`, `knowledge graphs` must
  match `knowledge graph` — a hyphen and a plural silently zeroed a bullseye paper (CLARK).
