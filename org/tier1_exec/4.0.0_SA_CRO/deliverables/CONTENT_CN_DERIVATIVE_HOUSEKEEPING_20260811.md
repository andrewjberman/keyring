# THE FILESYSTEM-BASED C(N) DERIVATIVE (CONTENT MODULE) -- HOUSEKEEPING AUDIT BEFORE RUNNING

**Author:** `4.0.0_SA_CRO~B` · Andrew-direct 2026-08-11: document space has no data flow, the logic
differs; the filesystem-based C(N) derivative exists for this reason -- *"revisit that and make sure its
clean and clear prior to running, just for housekeeping sake."*
**The artifact:** `infra/system/ontology/CONTENT_MODULE_DESIGN.md` (Andrew thread 2026-07-20,
CVO-reviewed + corrections folded @42fd458dc). **Routes to:** CVO (ontology home owner) for the
reconciliation edits; run stays gated on this housekeeping completing.

## 1. VERIFIED CLEAN (holds as-is)
- **The core distinction is exactly Andrew's point, already law in the doc:** *"Code reads C1 edges from
  flow structure. Content has no flow -> it computes edges from relatedness."* Content C1 = filesystem
  structural skeleton (`contains` folder-nesting + `owns` Entra ID, deterministic-given) + a computed
  mesh -- and **deliberately NO ground-truth C1 file** ("docs.jsonl is the content estate's C0; it has
  no C1 file, by design").
- **The full C(N) ladder is defined:** C0 = materialized text substrate (docs.jsonl, enumerated incl.
  null-text media for the denominator) · C1 = skeleton + computed mesh · C2 = CROSS-FILETYPE
  high-similarity cluster (anti-trivial by construction) · C3 = connected cluster set named by folder/site.
- **CVO-hardened acceptance already in-doc:** blinded negative-control (a reader must beat chance vs
  structurally-matched decoys -- the can't-fail-on-trash fix), decoy-null threshold (never hand-picked),
  ablate-don't-fuse, heat-is-divergence-not-relatedness, "deterministic+PINNED+reproducible, not
  'no-inference'" honesty.
- **NO PARTIAL RESIDUE (measured today):** `.tools/content/` does not exist; no docs.jsonl substrate
  anywhere; nothing half-built. The design never started -- housekeeping is reconciliation, not cleanup.
- Materialized-substrate-not-live-crawl + **mtime freshness (never T-1)** + the partitioned-tooling
  contamination refusal (Andrew: "majorly important") all remain correct.

## 2. HOUSEKEEPING ITEMS (the post-07-20 rulings to fold BEFORE running)
1. **Declare the cascade mapping PER-SUBSTRATE, honestly.** ms's split differs from code by construction:
   DETERMINISTIC = filesystem skeleton + metadata (mtime/author/co-change from the lakehouse);
   INFERENTIAL = the computed relatedness mesh + clusters (a pinned model IS inference-reproducible --
   the doc's own C-1 correction says so); USER = folder/site naming. **Content's deterministic share is
   structurally smaller than code's -- DECLARE the per-substrate split rather than force-fitting the mesh
   into "deterministic" to hold 90%** (CVO's ceilings-are-honesty-floors constraint, applied here).
2. **Anchor-catalog integration:** ms anchors = `MS_FOLDER` / site / drive (node-keyed) -- consistent
   with the doc's own folder/site-named C3, but must be stated in catalog terms so the four-substrate
   cover is uniform.
3. **Axis reconciliation (Rule 24):** the doc's `class: code|content` vs the new substrate axis
   {aws|portal|codebase|ms} -- one relation, stated once: class is DERIVED from substrate (ms -> content;
   the rest -> code), never a second independent axis that can disagree.
4. **Vintage re-verification (pre-run checklist):** (a) `ms_heat_snap`/`ms_cloud_extract` still flowing
   (the "already in the lakehouse" claim is 07-20-vintage; producer exists at
   `infra/aws/globgrph/ms_cloud_extract.py` -- liveness unverified today); (b) MS node counts current;
   (c) comp-similar BM25 still the reuse target.
5. **Semantic-axis implementation re-affirmed deliberately:** the doc prefers PPMI-SVD (corpus-fit) over
   pretrained Potion; since 07-20 Potion matured into the vendored one-home module
   (`org/modules/graph/potion/`, byte-verified). Choose again ON THE RECOVERY BAR (the doc's own rule),
   not by drift -- either is defensible; silence is not.
6. **Status header repointed** at the substrate/cascade rulings so a fresh reader lands in the current
   frame (the doc predates them by 3 weeks).

## 3. SEQUENCE
Housekeeping edits (CVO, ontology home) -> pre-run checklist verified -> THEN the ms motif run becomes
eligible (its own park lifted by Andrew's "cool with that" for the DESIGN; the RUN still follows the
cleaned design + the step-0/step-2 cover sequence). Nothing runs before the reconciliation lands.
