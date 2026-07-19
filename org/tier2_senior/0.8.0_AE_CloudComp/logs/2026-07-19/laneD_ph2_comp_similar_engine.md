# 0.8.0_AE_CloudComp~D -- NFRA_COMPSIMILAR PH2: comp-similar engine + --supersede built
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

Window: after PH2-C2 close (this session) -> PH2 engine build. Trigger: COO PROCEED-ALL-NFRA GO
@180112Z (Andrew-direct via CTO ~17:5xZ VERBATIM "proceed all NFRA work... we are not waiting, move
it along"). Scope expanded from PH2-C2-only to the NFRA queue; PH2 engine-supersede cleared to build
toward CTO's arch-gate. variance _position_key fix stays PARKED (COO, do-not-start-unless-sequenced).

## What I built -- comp_similar.py (@b63b18853, 538 lines) + .tools/comp-similar wrapper
A new engine module at the debtscan home (ZERO edits to summary_corpus.py -- ~C owns that file's
_position_key lane; edit-surface declared + COO/~C seam-cleared). comp_similar.py IMPORTS
summary_corpus's public API read-only (build_corpus / SimilarityIndex / coverage / _HELD_RX) +
dup_scan suppressors (_firm_of / _service_suffix_of / _strip_env). Modes:
- `comp-similar <a> <b>`  pairwise BM25 summary-sim + HYPOTHESIS framing (never a bare "duplicate").
- `comp-similar <a>`      one-vs-corpus summary-similar neighbors.
- `comp-similar supersede [--heat-json F | --live-heat]`  the headline joint scan.
- `comp-similar cluster [--type T]`  functional-overlap census.
- `--json`, `--self-test`.

**--supersede algorithm:** SUMMARY-similar (functional twin, >=0.60) x heat-DIVERGENT (one COLD one
HOT) x NOT a designed parallel (firm-cross/env/service suppressed) x NOT held. Emits the COLD member
as the decommission CANDIDATE + the HOT member as its replacement; ranked summary_sim x confidence.
Heat CONFIDENCE-GRADED per CTO §9-5: both-axes-cold=HIGH, one-axis-cold=MEDIUM (surfaced, never
silently dropped). Heat sources = comp-heat (data-cold) + comp-debris (invoke-cold), normalized to
{name: {data, invoke}}; UNKNOWN is a BAND (a blind row is never cold -- C3).

**DELIBERATE PRD-4.3 departure (flagged to CTO for ruling):** PRD said "name-cluster FIRST." I built
SUMMARY-similarity-first candidate generation -- because the headline superseded twin (monolith
cutover opal-data-{firm} -> opal-data-assets) is a NAME-DIFFERENT replacement that name-clustering
would MISS. Summary-BM25 over ~1.8k nodes is cheap (df-cut); the expensive LIVE HEAT read is what I
gate to summary-similar candidates -- same cost-gate intent, correct signal.

## Compiler Tools
| Tool | Why | Result |
|---|---|---|
| comp-which | route "describe an ARN with motif enrichment" (PH2-C2 leg) | -> comp-describe |
| comp-manifest-check | registration invariant (before + after registering) | baseline PASS -> BLOCKED (UNPLACED) -> coverage-map home added -> now blocks only on tools_index/entries (COO SoD) |
| comp_similar --self-test | the 5 PRD controls, offline discriminating | PASS 7/7 (C1..C5 + designed-parallel-supp + confidence-grade) |
| comp-similar (live) | exercise on the real 1790-node corpus | cluster -> real functional twins; --heat-json supersede -> HIGH candidate surfaces; no-heat -> honest C1 degrade to pool |
| comp-debris / comp-heat | ground the heat sources | comp-debris --json live >2min (slow, lambda-default); comp-heat freshness = REPO-path-scoped, not per-S3-bucket -- the open heat-plumbing item |
| commit-gate.sh | Rule 14 on comp_similar.py + wrapper | .py PASS; .py+.sh BLOCKED on registration (SoD boundary -- expected) |

**What worked:** the pure/heat-injectable design made the algorithm fully offline-testable (the C4
mutant IS the injected-heat path); reusing summary_corpus + dup_scan meant ZERO new similarity/
suppressor code and ZERO collision with ~C. **What failed:** first self-test fixture was a
small-corpus BM25 df-cut artifact (4 identical docs > 25% df) -- fixed with filler; the C-supp test
initially mis-expected a firm->consolidated pair as suppressible (it is a real supersession) -- fixed
to a firm<->firm pair. **Gaps surfaced (to CTO):** (1) live heat is impractical inline (comp-debris
slow + lambda-default; comp-heat repo-scoped) -> v1 decouples via --heat-json; heat cadence is the
open §6-5 call. (2) the monolith dogfood pair is PH3-gated: opal-data-assets is UNKNOWN-thin in
derive-at-scan (sim 0.164, no modeled edges) -> C3 correctly excludes it -> "surface once both carry
summaries" (PRD), needs PH3 authored summaries. Instrument correct; corpus coverage is the gap.

## Blockers
Two NAMED external gates, both submitted this turn (not stalls):
- CTO arch-gate (@184502Z): rule the PRD-4.3 departure + confirm gate-scoping (READ/scan, no
  store-writer, no plan-gate/22a per §9-2) + the open heat-plumbing call.
- COO registration SoD (@184511Z): land the graph-call-manifest tools_index + entries + comp-which
  row -- the registration invariant HARD-BLOCKS the .tools/comp-similar wrapper commit without it
  (my comp-tools.yaml + coverage-map half is staged; a .py-only commit passed, which is how the
  engine landed).

## Current State
- **comp_similar.py ENGINE: LANDED @b63b18853** (self-test 7/7, live-exercised). Pushed.
- **.tools/comp-similar wrapper + comp-tools.yaml + coverage-map: STAGED** -- ride COO's routing row
  (coordinated commit; wrapper blocked by the registration gate until comp-similar is in tools_index).
- Monitor bs1gsnh6o LIVE. Session PID 25024.

## Next Steps
1. **[1.0.0_SA_CTO]** arch-gate: rule the PRD-4.3 departure + gate-scoping confirm + the heat-plumbing call.
2. **[2.0.0_SA_COO]** land the graph-call-manifest routing row (tools_index + entries + comp-which);
   then I commit the wrapper + comp-tools.yaml + coverage-map (or COO bundles). Ping CVO on land.
3. **[0.8.0_AE_CloudComp~D, event-driven]** on COO routing row -> commit wrapper + registries,
   comp-manifest-check PASS, ping COO+CVO. On CTO ruling -> apply any retune (thresholds / heat
   cadence). On ~C _position_key land -> pull + re-run comp-describe/--build to confirm re-verdict.
4. PH3 (authored summaries, ~549 targets) = separate TO behind PH1+PH2 (CTO §9-4), not this leg.
