# CVO design review: content-class ontology module + s.7 prototype

**Author:** 3.0.0_SA_CVO · **Date:** 2026-07-20 · **Route:** CVO -> CTO (CC MSTR, for Andrew)
**Nature:** DESIGN REVIEW, pre-build. NOT a gate, NOT a build-go. Independent analysis; Andrew decides build.
**Artifacts reviewed (@ current HEAD, fresh):** `infra/system/ontology/CONTENT_MODULE_DESIGN.md` (@ea6c177cd,
s.7 prototype @ff7f0b29e) primary; `README.md`, `ESTATE_AXIS_AND_SEAM_GRAIN_DESIGN.md`,
`C2C3_NAMING_AND_DOMAINS.md` for context. Grounded against `org/modules/graph/debtscan/comp_similar.py`
(the tool the design claims to generalize).

---

## Verdict

**The ARCHITECTURE is sound.** The `code|content` soft-core-plus-modules split, the C3-protection invariant,
content-has-no-flow-so-compute-from-relatedness, and cross-filetype-span as a structural bridge are all
well-reasoned and internally consistent.

**The load-bearing WEAKNESS is the s.7 acceptance methodology (#3) -- as written it cannot fail on trash.**
That is the one thing to fix before build, and it is fixable. Everything else is a framing correction or a
prototype-scope fix. Below: the two corrections that change what the prototype must be, then the 6 points
(with #3/#2 hardened as asked), then the concrete negative-control protocol.

---

## Two corrections that change the prototype BEFORE the 6 points

**C-1. "Deterministic" is being conflated with "no model / no inference" -- they are different guarantees.**
`CONTENT_MODULE_DESIGN.md:11` says RRF-of-axes is "still deterministic, no LLM, no inference." But **Potion is
a model** -- a static-embedding forward pass is inference; it is *cheap and reproducible*, not *absent*. An LLM
at temperature 0 is also deterministic. So "deterministic" and "no LLM" are orthogonal axes, and the property
the ontology actually needs is **REPRODUCIBILITY / auditability** (same corpus + same pinned axis versions ->
same edges, every run, no hidden per-run variance), NOT "no learned parameters." This matters operationally:
the moment Potion's embedding table version bumps, "relatedness" shifts -- so the guarantee is only real if the
**axis versions are PINNED and stamped into every output** (BM25 params, Potion model hash, heat snapshot
timestamp). This is the same vintage-honesty discipline as the comp-iam census. Recommend restating the
guarantee as "deterministic + version-pinned + reproducible," and dropping "no inference" (it is false for
Potion and invites a false sense of purity).

**C-2. The prototype tests a DIFFERENT axis set than the design proposes -- an axis-mismatch.**
Design axis set (s.2): `RRF(BM25, Potion, heat)`. Prototype (s.7 Part A steps 3-5): `RRF(BM25, heat)` --
**Potion is dropped, heat (the weakest/most-suspect axis, see #5) is kept.** So the prototype validates
`BM25+heat` and the design would ship `BM25+Potion+heat`. A trash verdict could be caused by heat-noise that
Potion would have masked; a pass could be BM25 alone carrying it. **You cannot conclude about the design's axis
set from the prototype's axis set** (this is the "a rigorous instrument on the wrong axis survives review"
failure -- enumerate what the number is OF). Fix: the prototype must run **per-axis ablations** --
`BM25-only`, `BM25+heat`, `BM25+Potion` (once buildable) -- and report which axis actually adds discrimination,
not a single fused number. The prototype's job is to find the axis set, so it must vary the axis set.

**Bonus grounding correction (affects the reuse claim, not the design):** the design says content relatedness
is "a direct generalization of `comp-similar` (which already fuses BM25 x heat in its supersede/cluster modes)"
(s.2). It does not. In `comp_similar.py`: `cluster_scan` (`:179`) is **BM25-only** ("no heat"); heat is used
ONLY as a categorical **divergence** anchor in `supersede_scan` (`:130`, one-HOT/one-COLD = supersession), and
`:88-90` treats WARM as "not a divergence anchor" -- heat is a 3-state gate, not a continuous fused axis. And
**RRF does not exist anywhere in the estate** (grep: zero hits). So RRF and the heat-as-continuous-relatedness
axis are **net-new**, not a generalization of a proven fusion. This is fine -- but scope it as new code to be
validated, not as reuse of a trusted mechanism.

---

## The 6 points

### #1 DETERMINISM -- does an axis smuggle in a drifting model?
**Assessment: PASS in principle, with C-1's pin.** BM25 (fixed scoring over a fixed corpus), heat (recency
given a snapshot), and RRF (a fixed rank-fusion formula) are all deterministic. Potion is deterministic
*per pinned model version* but IS a model. **No axis introduces per-run randomness** (I checked comp_similar
for `random`/`seed`/`shuffle` -- none). The only drift vector is **unpinned axis versions** (Potion table
bump, corpus re-extraction changing tokenization, an un-snapshotted heat read). Fix = C-1's version-pin +
output stamp. With that, the no-inference-drift guarantee holds; without it, it is aspirational.

### #2 THE THRESHOLD -- set defensibly, not fit-to-sample (anti-Goodhart)
**This is solvable, and the negative control (#3) is what makes it solvable.** The design correctly names the
relatedness/cluster threshold as "the one non-tuned knob" and the code analog `recurrence>=2`. But note the
inherited risk: `comp_similar.py:70` already carries `SIM_TWIN=0.60` labelled "conservative v1; CTO may retune
at the gate" -- a hand-picked, retunable number. Inheriting that as the content threshold imports the exact
fit-to-sample hazard. **Defensible threshold-setting (recommended, in priority order):**
1. **Anchor to the null distribution, not to a target output.** Compute the similarity distribution of RANDOM
   file pairs (the #3 decoys). Set the promotion threshold at a pre-registered high quantile of THAT null
   (e.g. the 99th percentile of random-pair RRF). A promoted edge is then *definitionally* "more related than
   chance produces" -- a semantic property (like "recurs >= 2 = appears more than once"), not a tuned fit.
2. **Report threshold SENSITIVITY.** Show the high-signal verdict across a threshold sweep. A conclusion that
   holds only at one hand-picked value is fit-to-sample; one stable across a band is robust.
3. **Set on one slice, validate discrimination on a DIFFERENT slice.** A threshold that only works on the
   slice it was fit to is fit-to-sample by definition.
**Do NOT** pick the threshold that "makes the sample clusters look best" -- that is Goodhart, and it is
undetectable without a held-out/null baseline. Tie the knob to the null, and it cannot be tuned to itself.

### #3 THE "HIGH-SIGNAL OR TRASH?" TEST -- the one to harden (an acceptance that cannot fail on trash is not one)
**FINDING: the s.7 acceptance #1 as written cannot fail on trash.** It says "the cross-filetype clusters are
assessed HIGH-SIGNAL ... CVO/Andrew read a sample. If trash -> iterate." Two independent defects make this an
instrument that cannot fail:
- **No negative control + no blinding.** A human reading a set of documents is a pattern-completion engine --
  we can construct a plausible topic for ALMOST ANY grouping (apophenia). Reading real clusters and asking
  "do these look meaningful?" will return "yes" for random clusters too, because the reader supplies the
  coherence. Without a random baseline and a blind, "looks meaningful" measures the READER, not the CLUSTERS.
- **The reviewer knows they are real.** Confirmation bias: a reviewer who knows a cluster came from "the
  relatedness engine" grades it up.
**The fix is a blinded discrimination test (protocol in the final section).** Convert "do these look
meaningful?" (unfalsifiable) into "can a blinded reader tell REAL clusters from structurally-matched RANDOM
ones, above chance?" (falsifiable, has a null). If reals and decoys score the same, the axis set has no signal
-- regardless of how good the reals looked alone. This is the acceptance that CAN fail, and it is the one that
must gate the build.

### #4 CROSS-FILETYPE MOTIF -- sound unit, or does ">=2 filetypes" hide tuning?
**The >=2 threshold itself is NOT tuned -- it is the minimal definition of "cross" (like recurrence>=2), so it
is defensible.** But there is a hidden-confound risk the design does not address: **cross-filetype clusters may
look meaningful because same-topic files are co-located in the same folder/site and named similarly -- i.e. the
signal is the FREE `contains` structural edge, not the expensive RRF relatedness mesh.** If so, the RRF mesh
adds nothing over folder co-location. **Second negative control required:** compare RRF-formed cross-filetype
clusters against clusters formed by folder-co-location alone (random pairing within a folder, filtered to
>=2 filetypes). If folder-colocation clusters score as "meaningful" as RRF clusters, RRF is not earning its
cost -- ship `contains` and skip the mesh. This isolates whether relatedness adds signal beyond structure.

### #5 AXES + co-change deferral -- is BM25+Potion+heat enough; is heat real or noise?
- **BM25 + Potion = a defensible first signal** (lexical + semantic overlap are genuine relatedness).
- **Heat-as-relatedness is the suspect axis.** comp-similar uses heat for DIVERGENCE (supersession), never as
  positive relatedness. Co-*recency* (same last-modified window) is a weak, high-false-positive proxy for
  relation: quarter-end touches everything; a bulk migration re-timestamps everything; it conflates temporal
  coincidence with topical relation. **Do not assume heat helps -- ablation-test it** (RRF with vs without
  heat, against the #3 discrimination metric). Keep it only if it measurably raises real-vs-decoy separation;
  otherwise it is noise diluting BM25+Potion.
- **Co-change deferral is defensible.** Per-user co-modification is the STRONG relatedness signal, and it is
  deferred for a real gap (M365 exposes no version/author API; needs Graph `driveItem/versions`). Dropping it
  does NOT gut the first signal IF BM25+Potion carry it -- which is exactly what the prototype must MEASURE,
  not assume. Honest framing: BM25+Potion (strong) + heat (suspect, ablate) now; co-change (the real prize)
  when the API is wired.

### #6 PARTITION + class-routing -- is "cross-class isolation kills theft entirely" real?
**PARTIALLY real, and the framing over-reaches on the failure modes the design itself names.** For a query
that classifies cleanly to one class, disjoint partitions genuinely cannot compete -> that theft is gone, by
construction. TRUE. But:
- **The theft is not eliminated; it is TRANSFORMED into a routing-classification error, which is worse because
  it is silent.** Intra-pool rank-1 theft is visible and theft-checkable. A misroute sends the query to the
  WRONG PARTITION and returns wrong-class results with full confidence, the other class omitted entirely.
- **The two failure modes the design flags are the whole risk.** (a) *Ambiguous query* -> "default to code or
  ask." **Silently defaulting to code is a silent-omission failure** -- a content-intended query returns code
  results and the user never learns the content partition existed. (b) *Cross-class query* (e.g. "the pipeline
  that ingests the SharePoint fee docs" -- spans code:pipeline AND content:SharePoint) -> the classifier must
  pick one and HIDES the other. The partition amplifies this into total omission of one class.
- **The classifier is a NEW instrument and needs its own can-it-fail test.** A vocabulary/keyword front-step is
  itself the brittle pattern-match the estate distrusts; a synonym outside the keyword list misroutes silently.
**Recommendations:** (1) never SILENTLY default -- a low-confidence classification must signal "ambiguous:
searched CODE; a CONTENT partition also exists" or run BOTH and label results by class; (2) for genuinely
cross-class queries, run both partitions and merge with class labels (the theft-check runs within each);
(3) measure classifier accuracy on a labeled query set -- the classifier gets the same discrimination
discipline as #3. The partition is a real routing-hygiene win; the "eliminates theft entirely" claim should be
narrowed to "eliminates intra-pool cross-class theft for cleanly-classified queries, and moves the residual
risk to classification, which must itself be measured."

---

## The concrete deliverable: a blinded negative-control acceptance protocol (hardening #3)

Replace s.7 acceptance #1 with this. It is the instrument that CAN fail.

1. **Build the real set.** Run the engine over the bounded slice; take the top-N cross-filetype clusters (real).
2. **Build structurally-matched decoys.** For each real cluster, generate a decoy with the SAME size and the
   SAME filetype-span (>=2 types), but members drawn at random from the slice (matched on the structural
   properties so a reviewer cannot distinguish by shape -- only by topical coherence). Also build a
   **folder-colocation baseline** (random within-folder pairs, >=2 filetypes) for the #4 confound.
3. **Pre-register the pass bar BEFORE looking** (anti-Goodhart): e.g. "reals' median coherence rating is >= 2
   points above decoys' on a 1-5 scale, AND decoy false-positive rate (decoys rated 'coherent topic') is
   <= X%." Register the numbers first; do not adjust them after seeing results.
4. **Blind + shuffle.** Interleave real + decoy + folder-baseline clusters, strip provenance, present in random
   order. Reviewer (CVO and Andrew independently) rates each cluster's topical coherence WITHOUT knowing which
   is which.
5. **Score discrimination.** ACCEPT only if reals score significantly above decoys AND above the folder
   baseline (the latter proves RRF beats free structure, #4). Report the confusion explicitly: decoy
   false-positive rate and real false-negative rate. **If a blinded reader cannot separate real from random
   above the pre-registered bar, the axis set/threshold has no signal -- FAIL, no matter how good the reals
   looked in isolation.**
6. **Keep SIGNAL and WIRING as two independent verdicts.** s.7 bundles acceptance #1 (signal) and #2 (the tool
   lands + class-routes). These are orthogonal: a pipeline that runs end-to-end and produces trash clusters is
   a WIRING pass + a SIGNAL fail. Do not let "it runs" leak into "the clusters are meaningful." Report two
   verdicts.

This protocol also FEEDS #2: the decoy random-pair similarity distribution IS the null the threshold anchors to
(the 99th percentile of decoy similarity = the defensible, non-tuned promotion threshold). One negative control
resolves both the acceptance and the threshold.

---

## Bottom line

- **Architecture: sound, build-worthy.** No structural objection to the code|content module split.
- **Before build, three things:** (C-2) make the prototype ablate axes (BM25-only / +heat / +Potion), not test
  one fused BM25+heat number; (#3) replace the "read a sample, looks meaningful?" acceptance with the blinded
  negative-control protocol above; (#2) anchor the threshold to the decoy null, not a hand-picked value.
- **Two smaller corrections:** (C-1) restate the guarantee as deterministic+version-pinned+reproducible (drop
  "no inference"; Potion is a model) and stamp axis versions into outputs; (#6) narrow the "kills theft
  entirely" claim and never silently default an ambiguous query -- measure the classifier.
- **One thing to watch:** heat may be noise as a relatedness axis (it is a divergence signal in the tool it is
  borrowed from) -- ablate it, keep only if it earns discrimination.

None of these block the architecture; they harden the go/no-go so it can actually say NO. The prototype's whole
value is the ability to fail on trash -- so the acceptance must be built to fail on trash, and as written it
cannot.

## CVO grounding / residual unknowns
- Grounded on source @ current HEAD: `comp_similar.py:70` (SIM_TWIN=0.60 "conservative v1; CTO may retune"),
  `:71` (SIM_FLOOR=0.15), `:88-90` (heat WARM = not-a-divergence-anchor -> heat is categorical), `:130`
  (supersede uses heat as divergence), `:179` (cluster_scan BM25-only); RRF absent estate-wide (grep 0 hits).
- Not verified (out of design-review scope): Potion's actual determinism/version-stability in practice (no
  implementation exists yet); the M365 Graph `driveItem/versions` feasibility for co-change; live classifier
  accuracy (no classifier built yet). These are build-time verification items, flagged for when they exist.
- This is a DESIGN review on documents + the one live tool cited. Signal/threshold claims become verifiable
  only when the prototype produces real output; CVO re-grounds the negative-control results on that output.
