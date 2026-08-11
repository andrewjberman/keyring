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

## 5a. WHERE "28 VERTICALS" COMES FROM (Andrew's challenge -- grounded answer)

**It is DECLARED (legislated), not discovered -- BY THE ONTOLOGY'S OWN DESIGN, and Andrew's "hand-drawn"
instinct is correct AND intended.** `NFRA_ONTOLOGY_C2C3_CANONICAL.yaml` c3_ii_semantic_verticals.invariant,
verbatim: *"DECLARED, never discovered -- membership changes only by naming act + CVO-verified row
adjudication. Emergence proposes; legislation admits. The symmetric complement of C3.i."*

**But it is NOT ungrounded -- it is a COMPLETE partition of the DISCOVERED ground set.** Measured:
- C3.ii declared verticals = 29, their chain_counts **sum to 138**.
- C3.i discovered structures = 14, their chain_counts **sum to 138**.
- Design: "14 structures over 138 chains." So BOTH partition the SAME 138 chains -- C3.i by union-find
  (discovered), C3.ii by naming act (declared). The **138 chains are the measured atoms**; the verticals
  are legislated groupings over them. Every discovered chain is assigned to exactly one named vertical.

**Provenance chain:** the 29 were declared in a CVO/Andrew-direct adjudication pass **2026-07-30**
(`estate-coverage-manifest.yaml adjudications_20260730`), each carrying chains; 3 (etf-reports,
ceo-digest, ticketing) ADMITTED by naming act with family=UNASSIGNED. Then mdpf+model-portfolios MERGED
2026-08-07 (Andrew) -> ratified roster = **28**.

⛔ **THE DRIFT THIS EXPOSES (real finding): the ratified 28 has NOT propagated to the structural
instruments.** The canonical yaml still declares **29**; `comp-estate --matrix` still shows **29** (mdpf +
model-portfolios separate). So "how many verticals" answers 29 (yaml/matrix) or 28 (ratified lifecycle
sitting) depending on which instrument you read -- a coverage-denominator ambiguity. **The coverage
denominator must pin to the RATIFIED 28; the stale 29 in the yaml + matrix is owed a reconcile (the merge
propagated).** Same dead-in-ruling/live-in-record class as the A.2 finding. Routed.

**Standing consequence for coverage:** because C3.ii is declared, the roster is only as complete as the
legislation. The design's own check ("emergence PROPOSES; legislation ADMITS") means the declared roster
should be periodically reconciled against emergence over the 138 chains -- are there candidate clusters
legislation has not admitted, or residue verticals still un-placed (7 today on UNASSIGNED-RESIDUE)?
Coverage = the ratified partition IS complete over today's 138 chains, checked at the matrix; it is not a
discovered number and must not be quoted as one.

## 5b. CORRECTION (Andrew's 2nd challenge) -- NEITHER number is deterministically discovered. Both are LEGISLATED.

**My s.5a answer took the yaml's self-description at face value ("C3.i discovered, both sum to 138"). Going
to the CONSTRUCTION (go-and-see) corrects it -- and vindicates Andrew's suspicion on BOTH numbers.**

**Q1 -- how did C3.i "get down to 14" if it's deterministic?** It did NOT come from the deterministic
construction. Measured (design s.13, line 622, Andrew's own ruling): the MATERIALIZED graph count is
**`C3System = 4`**; the yaml's `c3_deterministic_structures = 14` is a SEPARATE hand-authored list --
his ruling calls all these counts *"VOCABULARY, not a POPULATION."* The cited emergence script
(`NFRA_MOTIF_P2_c3_emergence.py`) composes **C2 frontend motifs** into systems named `firm-conditional-
display` / `cluster-X` -- NOT the estate-wide `sys-bd-medallion` / `sys-yang-analytics-engine` names the
yaml lists. **So the 14 is a legislated vocabulary; the deterministic materialization is 4. The yaml's
"DISCOVERED via union-find" provenance line overstates it.** I repeated that overstatement in s.5a.

**Q2 -- when/how was 28/29 chosen, from what bank?** The bank is the **NAMED_THREAD_CATALOG**
(`d33fe4aab`, 2026-06-15, author 3.0.0_SA_CVO). Its commit message is the answer, verbatim: *"Pivots the
**134-thread inventory** into **15 NAMED THREADS at product/surface granularity** (advi / model-portfolios
/ news / market / pm-optimizer / partners / trade-submission / graph-platform / causality / mdpf /
fred-macro / security-scanner / insurance / portal-infra / ops)"* -- an **"Andrew-direct reframe."** So:
- The **bank = a 134-thread estate census** (a measured resource inventory -- the closest thing to discovered).
- **CVO aggregated 134 -> 15 named threads** on 2026-06-15; Andrew directed the REFRAME (product-surface
  granularity, standalone named-thread project), CVO did the grouping/naming.
- It **grew 15 -> 29** through adjudication passes (07-30 admitting ceo-digest / ticketing / etf-reports
  by naming act); Andrew **ratified verticals one-by-one** in the Aug lifecycle sitting; merged **-> 28**
  (08-07). **Andrew never picked "28" off a list** -- he directed the reframe + ratified members; the
  roster SIZE is CVO's aggregation of the census, adjudicated with him.

**The honest denominator, restated:** ~134-138 census threads/chains are the measured atoms; the 14
structures and 28 verticals are BOTH legislated groupings/namings over them (CVO-aggregated,
Andrew-directed/ratified). Coverage rigor therefore = reconcile the 28 against the ACTUAL census (are all
census threads covered? is the census itself current?), NOT quote 14/28 as discovered. My s.5a
"both partitions sum to 138, C3.i discovered" was the vocabulary-as-population error his s.13 ruling names.

## 6. COVERAGE CLASSES (the 28, from the deterministic backbone)
FULL-battery 18 · RESIDUE-degraded 7 (F1 heat-only: canonical-schwab, ceo-digest, etf-reports, news,
ops-internal, ticketing, trade-submission) · TERMINAL 2 (causality RETIRED, insurance DORMANT) ·
NO-baseline 2 (security-scanner, ticketing UNDECLARED -> State proposes an initial, no shift-from).
State baseline coverage: 26 of 28 ratified. ⚠ ROSTER DRIFT: comp-estate --matrix still lists mdpf +
model-portfolios separately (29); the ratified roster MERGED them (28, Andrew 2026-08-07) -- flagged.
