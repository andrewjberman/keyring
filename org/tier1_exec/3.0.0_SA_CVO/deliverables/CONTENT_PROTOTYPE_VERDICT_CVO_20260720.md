# CVO provisional verdict: content-relatedness prototype (doc-similarity scan, real workspace corpus)

**Author:** 3.0.0_SA_CVO~Z · **Date:** 2026-07-20 · **For:** CTO~Z (engine owner) + MSTR + COO~Z
**Engine:** content_relate_prototype.py @f8ed1cefa · **Harness:** content_negcontrol_harness.py @ef477bbfa ·
**Runner:** content_prototype_run.py. **Corpus:** 25 real workspace docs, 5 distinct subsystems (auth /
ontology / comms / pipeline / terraform), filetype mix ts:4 md:9 py:7 yaml:1 sh:1 tf:3. Per-doc text bounded
to 1500 chars (semantic PPMI-SVD is O(vocab^3) x 26 pooled-null runs -- a PROTOTYPE-SPEED choice, flagged).
**Nature:** Andrew-reset doc-similarity scan on available documents (NOT a proxy). PROVISIONAL, solo blinded pass.

## Headline
The **apparatus is validated end-to-end on real content** (engine -> harness -> blinded rating works, and my
blind pass correctly separated a random decoy from coherent clusters). But this corpus is too thin + too
folder-aligned for a POWERED go/no-go, and the **semantic axis is DEGENERATE here (not merely redundant)**.
Recommend a richer corpus + a semantic-axis calibration check before a definitive verdict. No DROP (asymmetric
rule); no premature SHIP.

## Blinded pass (I rated coherence 1-5 from member content BEFORE revealing the key)
| token | members (basenames) | my blind rating | revealed arm |
|---|---|---|---|
| C000 | README, AGENT_COMMS_ARCHITECTURE, 03_comp_tools, TERRAFORM_PROTOCOL, canon-patterns | **2** (mixed subsystems, no single topic) | **decoy** (random) |
| C001 | PORTAL_AUTHHARD_PRD, breached-passwords, throttle, password, auth | **5** (all portal-auth) | **baseline** (folder-colocation) |
| C002 | 00_synthesis, 01_substrate, 03_comp_tools, README, canon-patterns | **5** (all ontology/system) | **real** (engine cluster) |

The blind held: I rated the random decoy low (2) on content alone, not knowing it was the decoy.

## Per-axis result

### bm25 -- apparatus + baseline VALIDATED; run UNDERPOWERED + FOLDER-CONFOUNDED
- null_threshold 58.95; 13 pairs gated; **1 cross-filetype cluster** = the 5 ontology/system docs
  (md+yaml), blind-rated **5/5 coherent** -- a genuine cross-filetype topical motif. The engine found a REAL,
  meaningful cluster on real content. **real(5) - decoy(2) = +3, clears my pre-registered +2 bar.**
- TWO limits that block a powered verdict:
  1. **UNDERPOWERED:** only N=1 cross-filetype cluster on 25 docs. My locked bar = N<8 real clusters is
     "insufficient to accept," never a pass. One coherent cluster is a promising signal, not a verdict.
  2. **FOLDER CONFOUND (#4) is live:** the folder-colocation baseline (C001, the auth folder) blind-rated
     **5/5** -- as coherent as the real cluster (real - baseline = 0, misses my +1 bar). Root cause: my corpus
     labels folders = subsystems, so any within-subsystem cluster is folder-colocated BY CONSTRUCTION; the free
     `contains` edge already delivers the coherence, so bm25-relatedness cannot be shown to ADD signal here.

### semantic -- DEGENERATE on this corpus (a calibration finding, stronger than "redundant")
- null_threshold **0.9964**; **0 pairs gated**; `semantic_only_RECOVERED = 0`.
- What that number MEANS: the pooled token-SHUFFLE decoy docs reach ~0.9964 cosine, and NO real pair exceeds
  it. So at SVD dim=8 on this constrained-vocab technical corpus, **shuffled-noise docs embed as similarly as
  real docs** -- the axis has no discriminating power (likely stopword/high-frequency-token-dominated
  embeddings: `def/self/return/import/the` swamp topical content into a near-collinear 8-dim space).
- Per the ASYMMETRIC rule (CTO~Z): no recovery on constrained vocab -> **INCONCLUSIVE, do NOT drop**. But this
  is not a clean "semantic lives in bm25's space" redundancy -- it is a DEGENERACY (semantic gated nothing at
  all), which would recur on business prose too if uncalibrated. **Flagging to CTO~Z as an axis-calibration
  item, not a drop.**

## Which asymmetric branch fired
Semantic no-recovery -> **INCONCLUSIVE (do NOT drop)**. bm25 baseline validated, with the underpowered +
folder-confound caveats. Definitive semantic ship/drop rides a calibrated axis on synonym-rich business prose.

## Recommendations (to CTO~Z)
1. **Richer corpus for a powered verdict:** more docs (target >=8 cross-filetype clusters), and crucially
   **topics that CROSS folders** (so the folder-colocation baseline is a real control, not tautologically
   coherent). Consider dropping per-doc truncation (or raising it) once the semantic axis is calibrated.
2. **Calibrate the semantic axis BEFORE re-testing recovery:** the 0.9964 null-saturation says dim=8 +
   no stopword handling is degenerate on technical prose. Try higher SVD_DIM, IDF/stopword weighting on the
   co-occurrence, or a min-df floor -- verify a token-shuffle decoy scores CLEARLY below real pairs on a
   sanity corpus before trusting any semantic recovery/redundancy read.
3. **Apparatus is ready:** engine+harness+blinded-control plumbing is proven end-to-end on real content;
   re-running is cheap once the corpus + axis calibration land.

## Grounding / honesty
- Corpus = repo's own files (no client-document text; storage-care N/A). Run reproducible: fixed corpus list,
  pinned engine seeds, harness rng seed 2026. Key at content_prototype_key.json (revealed post-rating).
- Solo blinded pass = PROVISIONAL (I authored the corpus + ran the harness). Per CTO~Z, Andrew is pulled in as
  a 2nd blinded co-rater only if the semantic ship/drop call is CLOSE -- it is NOT close (semantic degenerate,
  0 pairs), so no Andrew escalation is warranted; the actionable next step is calibration + a richer corpus,
  not a second rater on a degenerate axis.
