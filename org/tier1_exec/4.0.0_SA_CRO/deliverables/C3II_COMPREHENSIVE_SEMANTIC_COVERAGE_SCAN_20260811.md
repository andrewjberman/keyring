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

## 7. V2 HARDENING EXECUTED (Andrew GO ~1953Z: "get back to the Semantic Scan and Vertical work")
**Tool:** `scripts/c3ii_semantic_scan_v2.py` · **Artifact:** `C3II_SEMANTIC_SCAN_V2_OUTPUT_20260811.json`.
All three s.4 hardening items landed:
1. **NULL-ANCHORED GATE (adopted from `content_relate_prototype` iter-2/3):** pooled decoy null,
   M=25 seeded frequency-weighted random-token queries (length-matched), family-wise threshold =
   quantile(1 - 0.05/N) -- expected false admits per vertical stays 0.05 regardless of corpus size.
2. **QUERY ENRICHMENT:** + resolver served-artifact leaves (baked prose STRIPPED -- the B9 defect
   class must not enter a query) + producer names; opal-mcp aliases m365-mcp; model-portfolios pulls
   the mdpf rows (roster drift declared, not silently absorbed).
3. **CORPUS EXTENDED + PLANE-LABELED:** 5,865 docs = docs 1,009 / projects 307 / logs 4,549 --
   planes reported separately (a log hit and a PRD hit mean different things).

**RESULT -- 28/28 verticals COVERED through the family-wise gate on the BM25 axis**, and the admit
COUNT is a real coverage spectrum: advi-inf 224 · model-portfolios 206 · portal-infra 134 ·
advi-bd 127 ... down to ceo-digest 3 · ticketing 3 · etf-reports 3 · canonical-schwab 2 (the thin
tail = exactly the RESIDUE/naming-act verticals, independently confirming s.6's coverage classes).

**THE POTION AXIS IS RETIRED AT GATE SEVERITY FOR QUERY-SHAPED RETRIEVAL -- measured, both directions:**
- Zero admits on all 28 verticals at fw AND at p999 AND at p99: real max cosine (0.66-0.87) sits
  BELOW the decoy null's p99 (0.78-0.87) -- a random-token query cosines HIGHER than the real
  enriched query (the 64-dim mean-pool maps generic corpus soup near every doc; centroid effect).
- **POSITIVE CONTROL (isolated invocation): the gate itself FIRES** -- a verbatim-doc query
  self-cosines 1.0 vs fw 0.9306, admitted rank 0, 15 total admits (self + true neighbors). So the
  instrument discriminates; the zero is a TRUE NEGATIVE about short topical queries on this
  embedder, not a dead gate. This is the anatomy axis-8 regime (bm25 decisively better on
  code-adjacent prose), now measured on OUR corpus with OUR null.
- Consequence: **the canonical per-vertical verdict rides BM25 (null-gated); Potion stays in the
  artifact as top-display ablation only.** Ablate-don't-fuse did its job -- a fused score would have
  buried this axis-level finding.

## 8. WIRED INTO THE CALLS -- pre-registered rubric (BEFORE the validation fire; CVO rider)
The friction call gains a `VERTICAL DOCUMENTATION CONTEXT` block: top null-gated admitted docs per
plane (BM25 axis) from the scan artifact, with the law stated in-prompt: docs give IDENTITY context;
friction characterization cites F-figures ONLY. New output field `doc_context_used`.
**RUBRIC, registered before reading any response:**
- R1 SCHEMA: JSON parses; all fields incl. `doc_context_used` present.
- R2 NO-LEAK: friction_character/direction/summary cite only F-figures; no doc path used as
  friction evidence.
- R3 GROUNDED: `doc_context_used` is a SUBSET of the provided paths (no invented paths).
- R4 BLIND SPOTS: F3 still named blind (the only UNMEASURED axis in the battery).
PASS = all four. A response failing R2 or R3 fails the wiring, not the vertical.

## 9. WIRING VALIDATED LIVE -- two fires, rubric 4/4 on the second; one harness defect caught + named
**Tool:** `scripts/kimi_call1_friction_v2.py` (extends the established call-1 canonical form with the
null-gated doc-context block; scan artifact -> model-portfolios entry, 11 paths across 3 planes).

**FIRE 1 (R1 FAIL, defect MINE not the model's):** response omitted `doc_context_used` -- because my
schema-extension replace MISSED and its guard `'"doc_context_used"' not in out` read the LAW-BULLET
mention as the-field-landed, skipping the fallback; the whole-prompt assert then passed off the same
prose mention. **The guard and the assert shared a derivation, so they could not cross-check -- the
checks-that-pass-on-the-confirming-limb class, live in my own harness the same day I merged binding
M.** The model saw a schema without the field and correctly followed the schema. Fix: replace on the
exact schema anchor (asserted present), then assert the field in the SCHEMA REGION
(`prompt[find("Return ONLY JSON"):]`), not the whole prompt.

**FIRE 2 (rubric 4/4 PASS):** R1 all fields incl. `doc_context_used` -- PASS. R2 friction evidence
cites F1/F2/F4 only, zero doc paths as friction evidence -- PASS. R3 `doc_context_used` = 5 paths,
ALL a subset of the provided 11 (mdpf-revamp brief, MDPF_GLOBAL, MDPF_REVAMP, yang lineage map, the
CTO wp7 seam log) -- PASS, and the field makes context-use FALSIFIABLE (fire 1 could not be scored
on R3 at all). R4 F3 named blind with the correct silent-toward-calm framing, plus an unprompted
honest F1-scope caveat -- PASS.

**Banked observations (canonical-form notes, not defects):**
1. **Character enum ambiguity, measured at temperature=1:** fire 1 read HEATING/DIVERGING, fire 2
   CONSOLIDATING/DIVERGING off the identical battery -- both defensible because the vertical is hot
   AND consolidating and the enum permits ONE value. Fire 2's resolution (consolidation subsignal
   carries CHARACTER, volume ratio carries DIRECTION) is the sharper convention -- candidate: state
   that precedence rule in the prompt rather than widening the enum.
2. **Budget calibration:** the doc-context block roughly doubled reasoning tokens (3,665 -> 5,825;
   total 8,985 of 16,000) -- headroom fine, worth tracking as context blocks grow.
3. **Retrieval quality at top-11:** genuinely-mdpf docs dominate; the looser admits (DRFR_PTMCH,
   MKOV_TRSRCE, ADVI_FIRMSEP) are shared-serving-spine neighbors -- consistent with the vertical
   spanning the shared platform, and the model did not leak them into friction evidence (R2).

## 10. CALL #2 (STATE) WIRING -- rubric pre-registered BEFORE the fire
Same context block; ADDED STATE-LAYER LAW in-prompt: a doc's own lifecycle language (revamp plan,
deprecation note, old status line) is NEVER shift evidence -- docs age; the ratified value + friction
figures are the only live inputs. RUBRIC (registered before reading any response):
R1 SCHEMA (all fields incl. doc_context_used) · R2 SHIFT-EVIDENCE = friction figures only (no doc
cited as evidence OF a shift) · R3 GROUNDED (doc_context_used subset of provided paths) ·
R4 SOVEREIGNTY (proposal framing intact; no asserted lifecycle fact) · R5 F3-dark named in
confidence_reason. PASS = all five.

**CALL #2 FIRE RESULT -- 5/5 PASS (scored against s.10's pre-registered rubric):**
R1 all fields incl. doc_context_used -- PASS-WITH-NOTE (response arrived ```json-fenced despite
"Return ONLY JSON"; parseable after strip; canonical form gains a "no code fences" line). R2 shift
evidence cites F2/F1/F4 only -- PASS, and **the load-bearing result: the REVAMP docs sat in context
and were NOT read as transition evidence** (the state-layer law held against exactly the trap it was
written for). R3 doc_context_used = 4 paths, subset of 11 -- PASS. R4 sovereignty framing intact
(NONE-shift / PERMANENT proposed, nothing asserted) -- PASS. R5 F3-dark named, "UNMEASURED, not
calm, caps the read" -- PASS. Fast + cheap: 21.8s, 548 reasoning tokens (the state call stays light
even with context).

**CHAIN STATE: friction (4/4) -> state (5/5), both wired with the null-gated doc context, both
live-validated on the mdpf specimen. The scan -> calls wiring Andrew ordered is COMPLETE for the
established call pair.** Next on this thread (queued): fold the doc-context block + "no code fences"
line into the estate_report_runner call builders when the new friction/state calls land in the
deployed runner (CVO operational loop, build routes via COO), and the per-vertical daily refresh
rides the existing 9a-ET schedule.

## 11. CANONICAL FORM CLOSED OUT (2026-08-12, under the standing-egress ruling)
Two banked items from s.9 folded into BOTH call builders, then EXERCISED (a claim that a prompt
rule works is behavioral -- a read of the prompt cannot establish it):
1. **PRECEDENCE RULE (friction):** CHARACTER is carried by the consolidation/spread evidence (where
   the work is GOING); DIRECTION by the instrument's own ratio bands; HEATING only when intensity
   rises with NO consolidation/spread signal to place it. Written because two fires on an IDENTICAL
   battery returned HEATING and CONSOLIDATING -- both defensible, the enum permitting one.
2. **NO CODE FENCES** on both schema blocks (the state call had returned ```json-fenced).
**Verification:** both folds asserted present in the SCHEMA REGION of the wired prompts (never the
whole prompt -- that whole-prompt assert is the confirming-limb defect s.9 records). **LIVE FIRE
against a pre-registered expectation (character=CONSOLIDATING, direction=DIVERGING, unfenced):
ALL THREE MET**, and the response cites the rule by name ("per the precedence rule does not soften
the volume divergence"), so the ambiguity is resolved BY THE RULE rather than by luck of sampling.
Blind-spot handling stayed correct (F3 named, absence-not-calm). Canonical forms are now stable for
the runner fold-in at CVO/COO.
