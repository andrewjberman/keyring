# CRO Session — NFRA_AKPIPE: arxiv daily-harvest pipeline, spec to validated build package

**archetype:** MIXED
**secondary_archetypes:** EXPLORE (arxiv surface teardown), IMPLEMENT (scorer/harvest/Lambda package), VALIDATE (acceptance battery + defect hunts), COORDINATE (egress amendment record + broadcast)

**Agent:** `4.0.0_SA_CRO` (Chief Research Officer) · **Window:** 2026-07-23 18:21Z → 2026-07-24 14:35Z
**Commits:** 5 (`0be8ae60c` → `aba30634f`), all pushed to CLOUD · **MCP:** ~14 messages; significant below.

---

## What this session delivered

A new project taken from a cold ask to a validated, buildable package in one window: **NFRA_AKPIPE**,
a daily arxiv harvest + contact-ID + ontology-relevance ranking pipeline. The through-line is that
**every material claim was exercised rather than asserted, and running the thing found four real
defects — three of them mine** — including two silent-wrong-answer classes that would have shipped
looking like clean runs.

### 1. Teardown + spec + project registration (`0be8ae60c`)
RCN-0003. Andrew supplied 3 HARs (2 md5-identical — one capture duplicated) plus a sample paper.
**Marked capture gap, in-band:** the HARs retained **zero HTML response bodies** (only PDF bytes), so
they ground the *surface topology* — `/list/cs/new`, `/abs`, `/html` LaTeX render, `/src` tarball,
`/search` — but **not** the page field-schema. No DOM parse was specified off an endpoint name; the
harvest backbone was routed to the official **OAI-PMH / Atom API** instead, which is the correct
mechanism regardless. Sample paper = *SWE-Explore* (`cs.SE`), adopted as the scoring **positive control**.

**The load-bearing design call:** the ranking CONVERGES with `infra/system/ontology/CONTENT_MODULE_DESIGN.md`
(RRF over BM25/Potion, materialized substrate, deterministic-pinned, ablate-don't-fuse, decoy-null
threshold). NFRA_AKPIPE is that content module's **external/arxiv instance**, not a parallel NLP stack —
"four names, one fact", held at CTO for ratification.

### 2. Scoring core, and the v1 defect it caught in my own spec (`a58862437`)
Built the scorer and ran the §7 battery offline (`HF_HUB_OFFLINE=1`; potion-base-8M from local cache —
**scoring performs zero egress**). It immediately falsified the spec I had landed hours earlier:
v1 defined `nlp_score` as the **RRF fusion** and multiplied it by recency. **Measured:** RRF's dynamic
range between a perfect match and pure noise is **1.03x**, while recency decays **2x per 45 days /
16x over 180**. Falsification test: **word salad published today outranked the high-relevance exemplar
at 3 days old.** RRF is a *rank* fuser with no magnitude by construction — it can order, it must never
be a multiplicand. Fixed to an absolute saturating magnitude; regression-pinned as check [7.6].
Normalization kept **absolute, not min-max/z-score**, because a corpus-relative score would silently
change a stored paper's value as new papers arrive — breaking losslessness *and* independent recomputability.

### 3. First real harvest + five measured fixes + a silent false negative (`76b8f0839`)
Andrew asked for a live run. I surfaced the fork rather than quietly acting: I cannot `terraform apply`
(CTO's gate, and my charter bars CRO applies), and a local pull would violate the **cloud-Lambda-only**
shape *he* set. He amended for DEV runs; recorded verbatim + broadcast same turn.

First harvest: **120 papers, full-text on top 12** (10 `/html`, 2 PDF fallback), **588 authors**, emails
on **9/12**. Then four defects measured on the real data:
| Defect | Measured | Fix |
|---|---|---|
| Scope leak | **48%** (57/120) primary-category off-target (`cs.CV`, `quant-ph`, `physics.flu-dyn`) — `cat:` matches cross-listings | filter on `primary_category`, denominator printed |
| Potion not earning its axis | CV **0.165** vs BM25 **0.845** — near-constant *within* CS | demoted to stored component + floor guard; recovery bar measured each run |
| Length bias | `corr(chars, bm25) = +0.60` | phrase-BM25 + length norm |
| Generic profile | "graph"/"code"/"agent" matched nearly every CS paper | **85-phrase** profile; corpus idf weights specificity |

**Then the worse one, found by reading output rather than stats:** after the phrase profile landed,
47/63 scored exactly 0 — including **CLARK: "Closed-loop Learning for Adaptive Reasoning over Knowledge
Graphs"**, a bullseye for the brief, at **0.000**. Cause verified at the data: **hyphenation**
("closed-loop" ≠ phrase "closed loop") and **plurals** (`\bknowledge graph\b` fails on "knowledge graphs").
CLARK hit both. Impact 7/63 hyphenated + 9/63 plural. Fixed via `normalize()` + plural-tolerant patterns:
**CLARK 0.000 → 0.633 (rank 3)**; positive control 14 → 18 phrase hits. *A silent false negative on
perfect content is the worst failure this pipeline can have — invisible in aggregate, reads as a clean run.*

### 4. Banded harvest — recency finally exercised (`6927bd1b3`)
Paginated pulls tripped arxiv's **429**; I stopped hitting them and added retry/backoff honoring
`Retry-After` (a real robustness gap the Lambda would have hit). Replaced pagination with **age bands**
via `submittedDate` ranges, one request per band: **182 papers across ~0.9d / ~14d / ~30d**.
**Recency now demonstrably trades against relevance** — ReProAgent scores the corpus-highest relevance
(0.894, 22 phrase hits) yet ranks **4th** at ~14 days old, below a fresher 0.808 paper. Length bias
**+0.60 → +0.262**. Also caught a defect I introduced: my own E702 fix outdented `dedup.append(r)`
outside its `if` guard, silently disabling dedup while the printed count still looked plausible.

### 5. Production Lambda package (`aba30634f`)
Authored into **my own deliverables tree, deliberately** — `infra/aws/**` is an AE lane and applies are
CTO-gated, so the CRO writes and validates the logic but does not place or apply infrastructure. TF is
named `main.tf.proposal` so no terraform run can pick it up from that path.
Handler (harvest → dedup → full-text → score → DDB+S3 → whole-corpus recompute → watermark; lossless
throughout, FAIL-LOUD run identities), Terraform (Lambda 2048/900 deliberately sized, DDB PK/SK + GSI +
PITR, S3 versioned no-expiry AES256, EventBridge daily, IAM scoped to the one bucket + one table, Rule-22a
warning inline), and `build_profile.py` for the **pinned-idf** artifact.

**Exercising the builder found the next defect, declared as the top build item:** it computes idf from
**title+abstract** while production scores **full text** — 54/85 phrases show `df=0`, including *every*
retrieval phrase, which demonstrably do occur in bodies. Zero df ⇒ max idf ⇒ one body hit scores
enormously. Mechanism right, input wrong.

---

## Compiler Tools

| Tool | Where | Result | Note |
|---|---|---|---|
| `ruff` (via commit-gate) | every `.py` commit (4 files) | PASS after 3 fixes | caught E402 (`__future__` before docstring) + 2x E702; the E702 fix is what introduced the dedup outdent |
| `py_compile` (via commit-gate) | `lambda_function.py` | PASS | handler compiles; has NOT run in AWS |
| safe-commit surface-check | all 5 commits | PASS | "no critical surface" each; workspace-side is advisory per Rule 20 |
| risk-reflex (`comp-pulse diff`) | all 5 commits | 1 HOLD, 4 CLEAN | HOLD on `REGISTRY.md` cited LD-0326:56, a GCONTR *row-move* claim — unrelated to my new-row append; read and proceeded |
| raw `grep` on `.owned-paths.yaml` (rail-checked) | write-boundary checks | PASS | established `infra/aws/**` is an AE lane → package stays in CRO tree; and that the `org/projects` grant had already landed |

**What worked:** the acceptance battery is the whole story — it falsified my own spec within minutes of
the scorer existing, and the `[7.6]` regression now pins that defect permanently. Running `build_profile.py`
against real data (rather than shipping it) surfaced the idf axis mismatch.
**What failed:** arxiv 429 rate-limit on paginated pulls (my request pattern, not their fault) — replaced
with banded single requests; and `Read` on the sample PDF failed (`pdftoppm` absent), worked around with `pymupdf`.
**Gap found:** `comp_similar.py`'s BM25 is a **pairwise resource-vs-resource** index, not query-vs-document,
so it is not directly reusable for paper ranking — the *method* is converged with CONTENT_MODULE_DESIGN,
the *implementation* is not, and aligning it is a build item for the `.tools/content/` partition.

---

## MCP — significant only

- **Andrew-direct (recorded verbatim + broadcast same turn, twice):** the 5 founding decisions establishing
  NFRA_AKPIPE incl. the **standing arxiv-scoped, cloud-Lambda-only daily-egress grant**; then the
  **amendment** permitting DEV/local runs (production shape unchanged).
- **CTO:** banked the grant at his gate with the scope explicit; later **banked the amendment as superseding
  his own stricter record**, and confirmed gate expectations (TF-only, 22a battery, convergence ratification).
- **MSTR:** initially held my registration as grant-blocked; I surfaced HEAD ground-truth
  (`.owned-paths.yaml` line 556 grant already landed 07-22) and **MSTR verified and corrected itself**,
  clearing the commit under a pre-commit branch-check safe-path during the live git-integrity fire.
- **CVO + CTO:** notified that my scope narrowed to NFRA_AKPIPE only — the backtest tandem hold on
  "CRO's delta" is **released from my side**; do not wait on me.
- **Scope narrowing (Andrew-direct):** *"you should only be focused on ARKIV pipeline work and validation"*;
  plus *"we don't care about that honestly, not worth our time"* de-prioritizing the MDPF_3FIRMS record gap
  and RCN-0001 D2. Both dropped, not routed.

---

## Blockers

**None.** The package sits at CTO's gate by design, and MDPF owns his night — that is awaited-not-blocked,
and I explicitly advised against putting new-resource infra on him mid-flip. No agent owes me anything.

---

## Current State (handoff surface)

**Project:** `org/projects/NFRA_AKPIPE.json` (active, phase = spec-landed pre-build) + REGISTRY row.
**Register:** RCN-0003 in `org/tier1_exec/4.0.0_SA_CRO/RECON_REGISTER.md`.
**Spec:** `briefs/NFRA_AKPIPE_BUILD_SPEC_20260723.md` (at **v1.1** — carries the RRF-composition correction
and the §6.5 validation-status table).
**Code (`scripts/`):** `akpipe_scorer.py` (profile **v3**, 85 phrases, PhraseIndex + normalize + acceptance
battery), `akpipe_harvest.py` (banded + paginated harvest, retry/backoff, full-text, contact-ID),
`akpipe_rescore.py` (zero-egress re-score of a stored substrate — both the profile-iteration path and the
production daily-recompute in miniature).
**Package (`deliverables/NFRA_AKPIPE_LAMBDA_PACKAGE/`):** `lambda_function.py`, `main.tf.proposal`,
`build_profile.py`, `README.md` (the handoff + the declared-gaps section).
**Data (scratchpad, EPHEMERAL — reapable by `/kill storage`):** `akpipe_papers.jsonl` (182 rows, 3 age
bands), `akpipe_papers_v2.jsonl`, `akpipe-profile-v3.json`, `paper_2606.07297v1.txt`.

**PROVEN:** harvest, scope filter, full-text (`/html`+PDF fallback), contact-ID, substrate write; scoring
6/6 acceptance checks offline; recency limb exercised on real age variance; length bias +0.60 → +0.26;
retry/backoff.
**NOT PROVEN (declared, in the README + spec):** (1) **pinned-idf reference corpus is wrong as built** —
must be rebuilt on FULL TEXT over a much larger corpus; (2) no **blinded decoy-null** relevance judgement —
inspection is not evidence; (3) `BM25_SAT_C=6.0` provisional, calibrate against that null, deliberately not
tuned to the sample; (4) Potion demoted on measured CV, with one weak counter-signal (2 promotions into a
top-5 at n=12) **recorded to re-measure, not acted on**; (5) **the handler has never run in AWS** — DDB
conditional-put, recompute pagination and the watermark are unexercised; **deployed != working**.

---

## Next Steps

- **[4.0.0_SA_CRO]** Rebuild the pinned-idf reference on **full text** over a larger corpus (needs a few
  more polite banded harvests); then stand up the **blinded decoy-null** and calibrate `BM25_SAT_C` against it.
- **[1.0.0_SA_CTO]** When MDPF clears: gate the package — Rule-22a battery on the new bucket/table ARNs
  (`comp-iam` FAILS GREEN on new resources), source-map registration, layer-packaged deps with potion baked
  at `/opt` (a runtime HF download would be undeclared egress), deploy-completion ledger. Plus the held
  **four-names-one-fact** convergence ratification with `CONTENT_MODULE_DESIGN`.
- **[2.0.0_SA_COO]** Staffing when CTO releases it: a cloud-ops lane (Lambda/DDB/S3/EventBridge TF+IAM) and
  a content/NLP lane (`.tools/content/` partition).
- **[0.0.0_AB_MSTR]** Remaining config sweep for this serial: the `ajb.ps1` CRO role-map entry (cosmetic,
  deferred) + folding the arxiv standing-egress into the shared egress index.
