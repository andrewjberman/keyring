# COMPREHENSIVE C3.ii VERTICAL COVERAGE SCAN -- SEMANTIC (Potion/model2vec + BM25), not grep

**Author:** `4.0.0_SA_CRO~B` · Andrew-direct: coverage across all 28 C3.ii verticals, via the
model2vec/Potion/BM25 machinery over all PRDs/docs (*"it came out very rich"*), **not grep** (*"grepping
is a nightmare for something like this, i wouldnt grep"*). Tool: `scripts/c3ii_semantic_scan.py`.

## 1. METHOD (reuses the estate's own machinery -- BUILD LADDER rung 2)
- **Embedder:** `org/modules/graph/potion/potion_embed.PotionEmbedder` -- the vendored model2vec static
  embedder (data-not-code safetensors, byte-verified `cos=1.0` vs `model2vec.StaticModel.encode`), dim 64.
- **Two axes, ablated not fused** (per `CONTENT_MODULE_DESIGN` / `content_relate_prototype`): Potion
  cosine (semantic) + BM25 (lexical), reported side by side. NEVER one fused number (RRF collapses to a
  corpus-invariant distribution that cannot discriminate -- the doctrine's own iter-1 finding).
- **Corpus:** 1,310 docs = `docs/**/*.md` (PRDs + architecture + briefs + doctrine) + `org/projects/*.json`.
- **Per-vertical query:** name + its C3.i structure meanings (DERIVED from the canonical yaml, not
  hand-typed keywords -- the grep brittleness Andrew rejected).

## 2. RESULT -- covers all 28, and it IS rich where the vertical is well-represented
- **Every vertical scanned; none dropped** (denominator discipline). Qualitatively strong, both axes
  agreeing (high confidence): **advi-inf** -> ADVI_APISCP / ADVI_INFLEC / ADVI_INFSHIP_A2 / ADVI_APISCP_PRD;
  **causality** -> causality-teardown; **advi-bd** -> the ADVI project cluster. The signal is real.

## 3. HONEST QUALITY READ (applying the estate's OWN instrument doctrine to this scan)
1. **Cross-vertical cosine magnitude is NOT a coverage metric.** The max-cosine ranking puts RESIDUE
   verticals (canonical-schwab 0.678, ticketing 0.651) ABOVE real full-battery ones (smartx 0.538,
   advi-cot 0.567) -- a query-length / embedder artifact, not real coverage. Do not read it as "more
   covered."
2. **Raw absolute scores need the NULL-ANCHORED gate.** Per `content_relate_prototype` (the estate's own
   design): a pooled Monte-Carlo decoy null -> a stable 99th-pct absolute-score cutoff separates
   RELEVANT from NOISE. Without it, a 0.53 top-hit cannot be called coverage-or-not. **The gate exists in
   the repo; this first pass does not yet apply it.**
3. **The 64-dim static embedder DRIFTS on some verticals** (smartx, graph-platform pull broadly-related
   but not sharply-identifying docs). BM25 complements exactly there (sharper on exact terms) -- which is
   why the ablation is kept, not fused.
4. **Query quality is the other lever:** a richer per-vertical query (its served artifacts + lifecycle-row
   description, not just name + structure-meaning) sharpens retrieval measurably.

## 4. HARDENING PATH (to rigorous coverage)
- Apply the **null-anchored decoy gate** (content_relate_prototype) -> per-vertical relevant/noise verdict.
- **Enrich the per-vertical query** from its served artifacts + lifecycle description.
- **Extend the corpus** to logs (`org/tier*/**/logs/`) -- Andrew's "logs" plane, deliberately not in the
  first pass (docs/PRDs/projects first; logs are ~10^4 files and want their own pass).

## 5. DOWNSTREAM -- this feeds the friction/state calls
The per-vertical top-relevant docs ARE the "comprehensive scan" that grounds the calls: each vertical's
friction/state call can be given its top-K semantically-relevant PRDs/docs as context, so the model
reasons over the vertical's real documentation, not just its git deltas. Coverage (this scan) is the
precondition Andrew named; the calls consume it.

## 6. COVERAGE CLASSES (the 28, from the deterministic backbone)
FULL-battery 18 · RESIDUE-degraded 7 (F1 heat-only: canonical-schwab, ceo-digest, etf-reports, news,
ops-internal, ticketing, trade-submission) · TERMINAL 2 (causality RETIRED, insurance DORMANT) ·
NO-baseline 2 (security-scanner, ticketing UNDECLARED -> State proposes an initial, no shift-from).
State baseline coverage: 26 of 28 ratified. ⚠ ROSTER DRIFT: comp-estate --matrix still lists mdpf +
model-portfolios separately (29); the ratified roster MERGED them (28, Andrew 2026-08-07) -- flagged.
