# Content-relatedness prototype: PRE-REGISTERED acceptance + negative-control harness (CVO~Z-owned)

**Author:** 3.0.0_SA_CVO~Z · **Date:** 2026-07-20 · **Status:** PRE-REGISTRATION -- committed BEFORE the
engine produces any clusters (that ordering is the whole point; a bar set after seeing results is not
pre-registration). **Build GO:** Andrew-confirmed via CTO~Z (1.0.0_SA_CTO~Z), all 3 ~Z live. **Division:**
CTO~Z builds the relatedness engine; CVO~Z (this doc) owns the acceptance that can fail + the threshold null.
**Origin:** the fix from CVO review @42fd458dc (s.7 acceptance could not fail on trash). COO~Z coordinates.

> **The one rule this doc enforces:** the pass bar below is LOCKED as of this commit. It may be changed only
> BEFORE the engine's first real output exists, and only by an explicit committed edit citing why. It may NOT
> be adjusted after seeing results -- that is the Goodhart failure this whole harness is built to prevent.

## CHANGELOG (pre-result edits only -- each must cite why + confirm no real output yet)

- **C-01 (2026-07-20, still PRE any real engine output):** the threshold NULL is on **absolute per-axis
  scores, pooled**, NOT on RRF. WHY: CTO~Z, building the engine, found (and I independently confirmed) that
  RRF fuses ranks (`1/(k+rank)`) and so is corpus-invariant -- a random-pair RRF null cannot discriminate.
  This is a CORRECTNESS fix to the null MECHANISM (s.4), surfaced before any real result; it makes the gate
  *able* to discriminate (a strengthening). The human-coherence ACCEPTANCE BAR (s.3) is UNCHANGED and stays
  locked -- only the separately-computed statistical threshold null moved.

## 1. Interface schema (CVO<-CTO, to agree before both sides build)

**What the harness NEEDS from the engine (CTO~Z emits):**
```
{
  "run_meta": {
    "slice": "<sharepoint site/library id>",
    "axis_versions": {"bm25_params": "<hash>", "heat_snapshot_utc": "<ts>", "potion_model": "<hash|null>"},
    "rrf_weights": {...}, "promotion_threshold": <float>
  },
  "corpus": [                      # THE FULL slice, not just clustered items -- I need all of it for decoys
    {"item_id": "...", "filetype": "docx|xlsx|pptx|script", "folder_path": "...", "text_sha": "..."}
  ],
  "pairs": [                       # ALL scored pairs (or a random sample of NON-cluster pairs too) -- the NULL
    {"a": "id", "b": "id", "rrf": <float>,
     "ablation": {"bm25_only": <float>, "bm25_heat": <float>, "bm25_potion": <float|null>}}
  ],
  "clusters": [                    # the candidate cross-filetype motifs
    {"cluster_id": "...", "members": ["id", ...], "intra_sim": <float>, "filetypes": ["docx","xlsx"]}
  ]
}
```
The two non-obvious asks: (a) I need the **FULL corpus** (all items, not just clustered) to build
structurally-matched decoys + the folder-colocation baseline; (b) I need **non-cluster pair scores** (or a
random pair sample) so the null distribution is real, not just the within-cluster tail.

**What the harness EMITS:** the decoy sets + the blinded rating sheet + (post-rating) the discrimination
verdict + the threshold recommendation. Schema in s.4.

## 2. The three arms (what a rater sees, blinded + shuffled, provenance stripped)

| Arm | How built | Tests |
|---|---|---|
| **REAL** | the engine's candidate cross-filetype clusters | the hypothesis |
| **DECOY (random)** | for each real cluster, a cluster of the SAME size + SAME filetype-span (>=2 types), members drawn at RANDOM from the corpus | "can a reader tell real from random?" -- the core negative control |
| **BASELINE (folder-colocation)** | random members drawn from within ONE folder/site, same size + >=2 filetypes | "does RRF beat the FREE `contains` structural edge?" (review #4 confound) |

Decoys are matched on structure (size, filetype-span) so the ONLY thing distinguishing a real cluster is
topical coherence -- a rater cannot cheat off shape. Every arm carries an internal provenance key the rater
never sees; the rater sees only a shuffled list of clusters + a coherence question.

## 3. PRE-REGISTERED pass bar (LOCKED as of this commit)

- **Rating instrument:** each cluster rated on topical coherence, 1-5 (1 = unrelated grab-bag; 3 = loosely
  related; 5 = one tight coherent topic/project). Rater sees member filenames + a short text snippet per
  member; NOT the arm label.
- **Raters:** CVO~Z + Andrew, INDEPENDENTLY, both blinded. Report inter-rater agreement (Spearman); a low
  agreement is itself a finding (the signal is not legible).
- **Sample:** target N>=15 per arm. If the engine yields <15 real clusters, match decoys/baseline 1:1 to the
  reals and REPORT the reduced power explicitly (never silently). N<8 real clusters = UNDERPOWERED, verdict is
  "insufficient to accept", not a pass.
- **ACCEPT requires ALL of:**
  1. real median coherence >= decoy median + **2.0** (a clear 2-point separation on the 5-point scale);
  2. real median coherence >= folder-baseline median + **1.0** (RRF must beat free structure by a real margin);
  3. decoy false-positive rate (decoys rated >=4) <= **20%**;
  4. rank separation: >= **70%** of real clusters rated strictly above the decoy median (a per-cluster check,
     not just medians -- guards against a few great clusters carrying a trashy tail).
- **FAIL / iterate** if any of 1-4 misses. A miss means the axis set or threshold is wrong -- iterate BEFORE
  productionizing, exactly as s.7 intends. **A blinded reader who cannot separate real from random is the
  instrument reporting NO SIGNAL, regardless of how good the reals looked alone.**
- Verdicts are computed and reported PER ABLATION (bm25_only / bm25_heat / bm25_potion) -- which axis actually
  earns the discrimination is the review-#5 question (heat may be noise; keep it only if it lifts separation).

## 4. The threshold (#2, anti-Goodhart) -- anchored to THIS run's null, not hand-picked

The promotion threshold is NOT a tuned constant. It is the **(1-alpha) quantile of the NULL** = the
**ABSOLUTE per-axis score** distribution of RANDOM (non-cluster) corpus pairs (from `pairs`, s.1), computed
**per ablation** (bm25_only / bm25_heat / bm25_potion). PRE-REGISTERED: **alpha = 0.01 -> the 99th percentile**
of the random-pair absolute-score distribution is the promotion cutoff. Report SENSITIVITY at 95th / 99th /
99.5th; the verdict must survive the band, not sit on one knob. This ties the threshold to "more related than
chance produces" -- a semantic property, like code's `recurrence>=2` -- so it cannot be tuned to flatter the
sample. **The random-pair null feeds BOTH the acceptance (s.3) and the threshold (here) -- one negative
control, two uses.**

> **NOT RRF (correction, see CHANGELOG C-01).** The gate is on ABSOLUTE per-axis scores, never RRF. RRF fuses
> RANKS (`score = 1/(k+rank)`), which is magnitude-discarding and corpus-invariant -- a random decoy's top
> pair gets the same RRF as a real cluster's top pair, so an RRF null CANNOT discriminate. RRF is retained
> only to RANK gated pairs, never to GATE them. The null is POOLED (the full background, or >=25 seeded
> permutation draws) -- a single small draw's 99th pct is too noisy to gate on.

Output verdict schema:
```
{"per_ablation": {"bm25_only": {"real_median":_, "decoy_median":_, "baseline_median":_,
   "decoy_fp_rate":_, "pct_real_above_decoy_median":_, "verdict": "PASS|FAIL|UNDERPOWERED"}, ...},
 "threshold_reco": {"null_p99": _, "sensitivity": {"p95":_, "p99":_, "p995":_}},
 "inter_rater_spearman": _, "n_per_arm": _, "notes": "..."}
```

## 5. Ownership + honesty
- CVO~Z owns: decoy/baseline generation, blinding+shuffle, the pre-registered bar (this doc), the null/threshold
  computation, the discrimination verdict. The engine (CTO~Z) does NOT own its own acceptance -- separation
  preserved (builder != acceptance owner).
- The blinded RATING step needs human readers (CVO~Z + Andrew); the harness produces the sheet + scores it. The
  harness's own logic (decoy match, shuffle, scoring) will carry an offline synthetic self-test (a known-signal
  fixture must PASS and a known-noise fixture must FAIL -- the harness itself must be an instrument that can fail).
- Residual: exact N depends on the engine's yield on the chosen slice (unknown until it runs); the bar adapts
  only via the pre-registered UNDERPOWERED path, never by moving the thresholds post-hoc.
