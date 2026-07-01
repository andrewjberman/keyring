# NFRA_GRAPHUNI P2/D2 -- shared marker-head read-handle BUILT; re-point no-regression FINDING + fork (lane ~D)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Current State
COO~B GO'd GRAPHUNI P2-P3 (the un-cache-ing that structurally kills the stale-cache-phantom class
I caught on Phase-B). Drove it to: the shared read-handle BUILT + committed + GRAPHDEPTH composing,
and the RE-POINT blocked on a grounded architectural finding (fork routed to CTO+CVO~B by COO~B).

**BUILT + LANDED (comp_marker_read.py -- dfad285bf then 42b7f3c48, pushed):** the ONE shared
marker-head read-API (PRD ruling 2). Reuses infra/aws/globgrph _canonical + _provenance (same
_branch_head oracle comp-kuzu uses) + kuzu read-only. Provenance/D4 on every call (status=current,
nodes_snapshot_id=5434137157015633165 == the P1 marker). `_project(scoped)` split:
`as_tracegraph()` = SCOPED trace-graph projection (byte-match target for the re-point) +
`full()` = unscoped unified estate. Grain per node (`grains` SET, many-to-many, LOADED from ~C's
grain_contract, not hardcoded) + CONTAINS `level`. nodes(scope_grain=) membership filter,
drill()/rollup() over the drilldown seams (rollup delegates to comp_coverage_check.rollup_defects
-- ONE existential def). id-canon (pipeline:<firm>:gold:<rest>->gold:<rest>; opal-data-<firm>/<key>
->s3:<key>; lambda arn->lambda:<n>) grounded against BOTH live CloudNode ids + CVO~B's frozen
fixture answer ids.

**~C coordination (clean, shared worktree):** signature ~C-signed-off (4 governor conditions);
~C CO-VERIFIED grain attribution GREEN (live-exercised: 52 node_types match, drill/rollup dirs,
rollup_defects identity). ~C's GRAPHDEPTH P3 comp-depth (3e8d457a9) composes on full(). ~C folded
their drilldown-derive refinement (_DRILL_* from grain_contract.drilldown_seams+strata, not
hardcoded) ON TOP of my push -- no collision (I flagged the shared-file HOLD; sequenced land).

**THE FINDING (re-point HELD): the marker-head compute slice is NOT coverage-equivalent to
build_graph's pre-delta trace graph.** After the scope-filter + a script-grain s3 rollup, only
~11/28 comp-blast targets set-equal to CVO~B's frozen fixture. The misses are COVERAGE LOSS, not
extras: e.g. gold:D_01.partner_analytics script-blast fixture 216 vs marker-head 13. ROOT (grounded,
3 probes -- not inferred): the GRAPHUNI Phase-A/B compute producer is FUNCTION-grain s3 (build_graph
is SCRIPT-grain, 445/903 s3 edge-endpoints) + deferred reads + a DIFFERENT key-form convention (the
fixture itself carries BOTH s3:.../* and s3:.../{*} per-key -- a glob-norm made it WORSE, reverted).
So the cross-script s3 data-flow bridges build_graph had are missing/mismatched -- NOT canonicalizable
at the read-handle (the edges aren't in the population). Scoped projection 2040n/2353e vs pre-delta
2152n/2772e quantifies the gap.

**FORK (surfaced BEFORE grinding -- COO~B ACCEPTED "textbook ground-then-escalate"; routing to CTO
+CVO~B for a converged ruling, re-point HELD until the joint verdict):**
(a) re-populate the unified compute slice at build_graph fidelity (script-grain s3 + full reads +
    key-form parity) -- a derive/producer change; true unification.
(b) re-run build_graph pinned to the marker HEAD -- kills the divergent-vintage phantom (the ACTUAL
    D2/D3 goal) at low risk, but not literally "read the Kuzu projection". [my lean; COO~B concurs it's strong]
(c) re-baseline the fixture vs the unified graph -- abandons the no-regression guarantee [not recommended].

## Compiler Tools
| tool | use | result |
|---|---|---|
| comp-which / comp-grep | route rebuild + locate cache-read sites (on-rails) | PASS -- surface centralized (cli.py::_get_graph covers blast/trace/xref; platinum_cli.py; comp-kuzu=marker path) |
| comp-kuzu | live CloudNode id-forms + provenance for the id-canon + smoke | PASS -- pipeline:/opal-data-/arn forms confirmed; HEAD current snap 5434137157015633165 |
| marker_head_read (smoke + no-regression probes vs fixture) | build-verify the handle + measure the re-point gap | PASS(build) / FINDING(re-point): scoped 2040n/2353e, 11/28 blast set-equal, 216->13 coverage loss grounded |
| ds-commit-gate | pre-commit (comp_marker_read.py) | PASS |

**What worked:** grounding the id-canon against BOTH live ids + the frozen fixture (no guess);
catching the coverage gap via the fixture BEFORE wiring the re-point (the fixture did its job).
**What failed:** the glob-norm hypothesis (fixture key-forms are heterogeneous) -- reverted, not shipped.
**Gap found:** THE finding -- the GRAPHUNI population's compute slice under-covers build_graph's
cross-script data-flow; the re-point can't byte-match until that's resolved (fork).

## RESOLUTION (JOINT VERDICT -> (b) LANDED, CLOSE-READY)
COO~B relayed the converged CTO+CVO~B verdict = **(b)-GO** (head-pinned build_graph; (a) literal-Kuzu
DEFERRED as the coverage-equivalence workstream; (c) rejected). "Do NOT regress coverage to satisfy the
letter" (CTO). Shipped (b):
- **4 structure tools head-pinned** -- cli.py::_get_graph (blast/trace/xref, e0d839996) + graph_cache
  DEFAULT (platinum, 70ff64a56): serve the cache ONLY if drift-free (current source), else rebuild.
- **Producer head-pinned** -- extract_gold_compute (57518fc3a): rebuild-if-stale before read (the ACTUAL
  1347 phantom source, folded into the close per COO~B ITEM-2 "don't over-claim").
- **D4 one-head assertion** -- test PASSING (gc drift->miss; _get_graph rebuilds on source-drift, serves
  current sha). Exec-land routed to CVO~B (tests/ = ANY_EXEC, AE-blocked).
- **CVO~B (b) cert GREEN (150e0b8b4)** -- blast 28/28, trace 6/6, platinum 8/8 byte-equal; xref delta
  DECISIVELY confirmed source-drift (re-pointed == fresh build_graph, both != 20h-stale fixture). Zero
  re-point regression. Coverage PRESERVED (blast 216/148, not the 13-node Nessie regression).
GRAPHUNI closes VINTAGE-unified (phantom class killed) on the D4-test-land + COO~B 2-step. NOT graph-unified
-- (a) is the tracked follow-on (CVO~B pins the coverage-equivalence measurement).

## Blockers
None assumption-blocked. Residual = exec steps: D4-test SoD-land (CVO~B) + COO~B 2-step close. (a) +
GRANTS_S3 + NFRA_INFRPT retire-tail = the COO~B-sequenced post-close queue.

## Next Steps
1. **[1.0.0_SA_CTO / 3.0.0_SA_CVO~B]** the converged ruling (a/b/c) -- COO~B relays ONE decision.
2. **[0.8.0_AE_CloudComp~D] (me)** on the verdict: (b) wire cli.py to a head-pinned build_graph +
   per-tool CVO no-regression + P3 retire + D4; OR (a) re-populate the compute slice at build_graph
   fidelity (derive change) then re-point.
3. **[0.8.0_AE_CloudComp~C]** GRAPHDEPTH P3 continues on full() (independent of the fork).
4. **[0.8.0_AE_CloudComp~D]** queued for COO~B sequencing: GRANTS_S3 (CTO arch-Q) + NFRA_INFRPT sec-8 retire-tail.
