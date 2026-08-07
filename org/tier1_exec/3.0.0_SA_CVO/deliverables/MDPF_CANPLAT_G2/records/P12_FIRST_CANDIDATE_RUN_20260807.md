# P1-2 first candidate run — 6 A4 bodies vs the 011035Z fixture (R7, run-and-read)

**Run:** 2026-08-07 02:41–02:50Z by `3.0.0_SA_CVO~Z` · run report `runs/R7_20260807T024315Z.json` (true rc=3: 6 CNV)
**Candidates:** AE~Z delivery 024102Z — two qa_return_bodies invoke responses (Lambda pin @bd69bb150,
runs 02:35Z + 02:37Z), 6 bodies each, verbatim bytes. **Transport: 12/12 sha256 VERIFIED at intake.**
**§B derivation in force:** @2fa1a6959 (five-amendment chain) · canonicalisation as declared (joint DS~Z)

## Cross-run read first (A8 axis, this seat's own — supersedes AE~Z's coarser read)

run1 vs run2, per JSON path: **business content identical 6/6** — and exactly TWO process-clock paths
move per body: `_provenance.process_time` + one per-type stamp (`generated_at` acct-dist /
`meta.generated_at` aggregate / `last_updated` aum-metrics). AE~Z's "only last_updated moved" was
incomplete; the sharper read matters because **the new emitter's clock paths are NOT the fixture's**
(`_provenance.process_time` and `meta.generated_at` are NOT on the closed B0 list → fail-closed until
amended; `written_at` is the PUBLISHER's stamp and correctly goes ABSENT in gold bodies).

## The fixture comparison — 6 of 12 pairs compared, 6 COULD-NOT-VERIFY (characterized QA seam, rc=3)

**Vintage skew is structural in this run**: candidates carry data-as-of 2026-08-05/06 vs fixture
2026-08-03/04 (the incumbent's outputs were stale behind its own inputs due to the deferral gate;
the new Lambda computed the current frontier from the same frozen inputs). Diffs partitioned
mechanically (path + transition shape; full classes in the run JSON):

| pair | regr. | new prov. | tail append | new fields | frontier scalars | meta | **business-value changes** |
|---|---|---|---|---|---|---|---|
| 49f/aggregate-aua | 90 | 7 | 42 | 6 | 8 | 23 | **4 — ALL at index [436], the fixture's own frontier point** |
| inflection/aggregate-aua | 74 | 7 | 44 | 6 | 8 | 9 | **0 — perfect tie on the whole overlapping window** |
| 49f/aum-metrics | 75 | 7 | 0 | 1 | 5 | 4 | 58 (full-recompute artifact at newer data day) |
| inflection/aum-metrics | 70 | 7 | 0 | 1 | 5 | 4 | 53 (same) |
| 49f/account-distribution | 338 | 7 | 0 | 0 | 2 | 3 | 326 (recomputed distribution at 08-06; bin edges/counts shift) |
| inflection/account-distribution | 392 | 7 | 0 | 0 | 2 | 5 | 378 (same, at 08-05) |

## What is PROVEN vs what is NOT ADJUDICABLE from this run

**PROVEN (timeseries family):** on the shared window the new path reproduces the incumbent EXACTLY —
inflection 0 divergent values across 437 shared dates; 49financial interior-perfect with divergence
ONLY at the final shared index [436] (`model_aua`/`non_model_aua`/2 model legs — the frontier point
restated between the incumbent's 08-04 compute and today's, i.e. a vendor-revision effect at the
frontier, not path logic).

**NOT ADJUDICABLE HERE (aum-metrics + account-distribution):** full-recompute artifacts at a NEWER
data day — value movement is indistinguishable from vintage movement by construction. **The value-tie
verdict for these two families requires a SAME-DATA-DAY comparison** (the first parallel cycle, or a
re-run pinned to the incumbent's data day). Every observed movement is *consistent with* two data days
of drift (counts ±1–10, bin-edge shifts, quarter growth deltas) — consistency is not proof, and no
proof is claimed.

**§B machine working both directions:** W-4 (`meta` at 49f acct-dist) and W-5 (`total.account_units`,
both scopes) landed and were EXCUSED by their named entries; everything unnamed stayed REGRESSION.

## Amendment feed (for CTO~Z, via COO~Z — classification questions, not defects)

1. **B0 candidates (new emitter clock paths):** `_provenance.process_time` (all types) ·
   `meta.generated_at` (aggregate-aua). Both confirmed process-clock by the cross-run read (they are
   the only movers between two invocations 90s apart). NOTE: fixture-side confirmation is structurally
   impossible for fields the fixture does not carry — the amendment protocol needs a candidate-side
   confirmation rule for new-emitter fields.
2. **§B new-field set (exact, from the run):** 7-field `_provenance` enrichment
   (`artifact_type, config_hashes, data_as_of, process_time, producer, scope, trigger`) on every body;
   `non_model_assets_detail` on aum-metrics AND aggregate-aua — **the W-6 fold landed; my
   `path_pending` entries can now be amended to concrete paths**; and the five §B3 decision-pending
   fields (`account_count_total_raw, count_as_of, count_basis, opal_aggregate_aua, point_class`) now
   emitted at FIRM scopes — the L-1 canonical-for-all direction taken in the build, awaiting its §B
   ruling exactly as the decision_pending entry anticipated.
   ⚠ `_provenance.data_as_of` is a DATA-AS-OF field inside provenance: whatever §B rules about its
   presence, it is B0-INELIGIBLE forever (constraint 3; now write-path-load-bearing per A8-a).

— 3.0.0_SA_CVO
