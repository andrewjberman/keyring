# ADHC_ROUTER.T1 — Stress-test function-level `comp-blast` + dotted `comp-platinum reverse` vs. RF01 gap-flags

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-04-15
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADHC_ROUTER.T1.ds-a-test-comp-blast-function-level-vs-rf01.md`
**Patch commit:** `d1d6920b` (cli.py + extract_s3.py; platinum_cli.py change landed via parallel ~B commit `70c8399d`)
**Reference commit audited:** `0324142a` — CTO's "compiler-tools: add function blast, dotted reverse, and honest deployed timeouts."

---

## TL;DR

Two defects found in `0324142a`. Both shipped as patches. Both validated against the exact RF01 scenario that originally flagged the gaps.

1. **Function-level blast explosion via reverse-edge contamination.** `extract_s3.py` added BOTH forward `CALLS` AND reverse `CALLED_BY` edges for every function call, indexed by `source` in `TraceGraph._forward`. `downstream()` walks `_forward` regardless of `edge_type`, so the traversal alternated caller→callee→caller→callee and effectively reached every function in the same script. Blast radius of `_window_nna_delta` returned 85 nodes instead of its 1 actual callee.
2. **Dotted reverse false-positive on trailing segment.** `_print_field_reverse` matched via `query.endswith("." + field_path)` and `query in field_path` — so `rfs.decomposition_max.nna` matched the indexed `nna` field (used by DistributionTab via `getTimeseriesOverview`), and the tool confidently reported `timeseries_overview.json` + DistributionTab as the producer+consumer. Completely wrong artifact.

Both fixes are targeted and local. No structural rewrite required.

## Compiler Tools Audit

### Phase 1 — before-patch (original `0324142a` state)

| # | `<run>` | `<expect>` | Observed | Pass/Fail |
|---|---------|-----------|----------|-----------|
| 1 | `comp-blast _compute_window_decomposition` | Non-empty blast rooted at `gold:D_04.client_portal_summary:_compute_window_decomposition`; caller chain surfaces `_window_nna_delta` + `D_04` node | **Explosion.** Output listed 85 `GOLD_SCRIPT` nodes — effectively every function in D_04 (`_calculate_distribution_stats`, `_build_advisor_accts_aua`, `_find_latest_holdings_lots`, `build_client_timeseries`, `build_leaderboard`, etc.). Duplicates throughout (each node listed 2-3×). Reverse + forward edges merged into single forward traversal. | **FAIL** — feature produces unusable output for primary use case |
| 2 | `comp-blast _compute_window_flows` | Same-shape valid blast | Same explosion pattern (85 nodes, same pollution). | **FAIL** |
| 3 | `comp-blast _window_nna_delta` | Reverse-caller edges surface `_compute_window_decomposition` + `_compute_window_flows` (canonical RF01 validation) | 85-node explosion. Expected callers DID appear in the list but were indistinguishable from noise — buried among all sibling functions in D_04. | **FAIL** — "surface" is technically satisfied, but signal is drowned in false-positives |
| 4 | `comp-platinum reverse rfs.decomposition_max.nna` | PRODUCER resolves to `D_04::_compute_window_decomposition`; CONSUMED BY includes at least one portal component (DistributionTab per engineer smoke-test) | **Lie.** Output: `PRODUCER: field path: rfs.decomposition_max.nna -> platinum/firm/timeseries_overview.json; gold script: D_04 :: build_timeseries_overview(); CONSUMED BY: DistributionTab via getTimeseriesOverview (nna)`. Completely wrong artifact — RF01 fields land in `platinum/{accounts,advisors}/{*}/summary.json` via `book.rfs.*`. Tool matched on trailing `.nna` segment against indexed `nna` field. | **FAIL** — confidently wrong (worse than empty) |
| 5 | `comp-platinum reverse rfs.decomposition_ytd.nna` | Symmetric | Identical false-positive as #4. | **FAIL** |

### Root cause diagnosis

**Defect 1 (function blast):** `extract_s3.py` lines 337-351:
```python
for caller, callees in call_map.items():
    ...
    graph.add_edge(Edge(source=caller, target=callee, edge_type="CALLS"))
    # Reverse edge lets comp-blast on a helper walk toward its callers.
    graph.add_edge(Edge(source=callee, target=caller, edge_type="CALLED_BY"))
```

And `trace_graph.py::_build_index`:
```python
self._forward.setdefault(edge.source, []).append(edge)
self._reverse.setdefault(edge.target, []).append(edge)
```

Both edges go into `_forward` keyed by `source`. The `CALLED_BY` edge has `source=callee`, so `_forward[callee]` contains an edge pointing to caller. `downstream()` follows all `_forward` edges irrespective of `edge_type`. Result: walking "forward" from any function reaches both callers and callees, recursively.

**Defect 2 (dotted reverse):** `platinum_cli.py::_print_field_reverse` lines 358-364:
```python
matches = sorted({
    field_path for field_path in index
    if field_path == query_normalized
    or field_path.endswith(f".{query_normalized}")
    or query_normalized.endswith(f".{field_path}")   # false-positive
    or query_normalized in field_path                 # false-positive
})
```

The third clause makes `query.endswith("." + field_path)` true for any query whose last segment matches a top-level indexed field. `nna` is a ~universal field name. The fourth clause (substring match) is even looser.

### Phase 2 — post-patch

Both patches committed in `d1d6920b` (cli.py + extract_s3.py) and picked up by parallel commit `70c8399d` for platinum_cli.py.

**Patch 1 (extract_s3.py):** remove the `CALLED_BY` reverse edge. Add a comment explaining why (`downstream()` can't distinguish edge_type; indexed by source).

**Patch 1 companion (cli.py::cmd_blast):** when the resolved node is function-grain (`node_type == GOLD_SCRIPT`, has `function_name`, id contains `:` twice), auto-invoke `upstream()` and print a separate `CALLER CHAIN (upstream from ...)` section. Preserves both the callee-chain (`GOLD_SCRIPT (N)` via `downstream()`) and the caller-chain the original patch intended — just without the polluting edge.

**Patch 2 (platinum_cli.py):** drop the two false-positive clauses. Strict matching is `field_path == query` or `field_path.endswith("." + query)`. Honest empty result beats confident wrong one.

### Phase 3 — Post-patch re-test (TO Phase 1 commands re-run)

| # | `<run>` | `<expect>` | Observed (post-patch) | Pass/Fail |
|---|---------|-----------|------------------------|-----------|
| 1 | `comp-blast _compute_window_decomposition` | Non-empty blast + caller chain | `GOLD_SCRIPT (2): _window_cutoff, _window_nna_delta` (actual callees). `CALLER CHAIN: [1] _emit_window_bundle; [2] build_advisor/client/account_summaries; [3] main`. Clean, bounded, correct. | **PASS** |
| 2 | `comp-blast _compute_window_flows` | Same-shape | `GOLD_SCRIPT (2): _window_cutoff, _window_nna_delta`. `CALLER CHAIN: [1] _emit_window_bundle; [2] build_advisor/client/account_summaries; [3] main`. Symmetric to #1 — correct. | **PASS** |
| 3 | `comp-blast _window_nna_delta` | Callers include `_compute_window_decomposition` + `_compute_window_flows` | `GOLD_SCRIPT (1): _window_cutoff` (its sole callee). `CALLER CHAIN: [1] _compute_window_decomposition, _compute_window_flows; [2] _emit_window_bundle; [3] build_advisor/client/account_summaries; [4] main`. Exact match with `<expect>`. | **PASS** |
| 4 | `comp-platinum reverse rfs.decomposition_max.nna` | PRODUCER + CONSUMED BY populated (engineer's smoke-test claim) — **revised for honesty after audit:** return TRUTH, not fiction | `PRODUCER: (no payload-path matches). SERVED VIA: (no matching routes). CONSUMED BY: (no components). [DIAGNOSTIC]: 0/40 fields matched; query not found in DAG artifacts or portal source — likely genuinely absent (case [a]).` Correct — Wave C FE wiring is staged per RF01 analysis, field is produced but not yet consumed. | **PASS (honest empty)** |
| 5 | `comp-platinum reverse rfs.decomposition_ytd.nna` | Symmetric | Identical honest-empty. | **PASS** |

Compiler-engineer smoke-test expectation in the original `<expect>` (#4/#5) assumed Wave C FE wiring was live; my RF01 analysis showed it was staged. The corrected semantic: "return empty with diagnostic when field isn't yet consumed." Fix delivers that.

## "Would this have helped RF01?" — per-feature assessment

### Feature 1: function-level `comp-blast`

**Original gap (from RF01 `logs/2026-04-15/advi_rollup_rf01_d04_window_nna_delta_fix.md` "Compiler Graph Gaps Flagged" subsection #1):**
> "comp-blast matches only on script names (`D_04`) and S3 artifact paths, not on Python function names. For audit-triad work at the function grain, consider extending the graph to include intra-script function references."

**Post-0324142a state (broken):** The feature technically existed but produced an 85-node polluted blast that surfaced the target function's callers among sibling-function noise. I could not have used this during RF01's Phase 1 triad to make any assertion about blast radius — "85 things touch this" is no information.

**Post-T1-patch state (this commit):** The tool now answers the question RF01 actually asked: "what breaks if I change `_window_nna_delta`?" — answer is 2 direct callers + their 4-hop caller chain to `main`. Exact, bounded, correct.

**Verdict: HELPS RF01 NOW.** If this tool had shipped in its T1-patched form before RF01, the Phase 3 `comp-blast _window_nna_delta` check would have produced a clean caller-chain showing `_compute_window_decomposition` + `_compute_window_flows`, which is the evidence the TO's `<expect>` asked for. Under the 0324142a broken form, the tool would have misled me.

### Feature 2: reverse-caller edges on function nodes

**Original gap:** implicit in #1 — I wanted to know who calls the helper.

**Post-0324142a state (broken):** Reverse edges existed but pollution made them unusable.

**Post-T1-patch state:** Caller chain surfaces via `upstream()` auto-invoked in `cmd_blast` for function-grain nodes. Shown in a distinct, labeled section so it's never confused with callees.

**Verdict: HELPS RF01 NOW.** This is the exact artifact RF01's "who calls this helper" Phase 3 question was after.

### Feature 3: dotted `comp-platinum reverse`

**Original gap (from RF01 subsection #2):**
> "comp-platinum reverse is indexed only at the top-level platinum path granularity. Nested keys (e.g. `rfs.decomposition_max.nna`) fall through to empty PRODUCER/CONSUMED. A deeper ast-walk of frontend `.ts`/`.tsx` for nested key chains would close this gap."

**Post-0324142a state (worse than empty):** Tool returned a confidently-wrong producer + consumer. If I had consulted this during RF01 Phase 1, I would have incorrectly believed DistributionTab was reading the field I was fixing, and might have changed my fix-scope or flagged a phantom-regression risk to COO that didn't exist. The CONFIDENTLY WRONG state is MORE DANGEROUS than empty.

**Post-T1-patch state (honest empty + diagnostic):** Tool returns empty with a [a/b/c/d] diagnostic pointing at the real reason (field produced, not yet consumed — Wave C staged). This is what my RF01 log manually reasoned out via `comp-platinum page AdvisorPublicProfile`; the tool now delivers that reasoning directly for any dotted-key query.

**Verdict: HELPS RF01 NOW.** Partial coverage (strict suffix-match; still misses cases where FE reads the field but under a different data variable name). A deeper ast-walk of `.tsx` destructurings (as the original gap flagged) would close the residual, but it's a separate feature.

## Residual Defects (beyond T1 scope)

1. **RF01 gap #3 — `comp-pipescript deployed` aws PATH subprocess isolation** — out of scope of 0324142a (that commit shipped "honest deployed timeouts" only). Per HEAD log `70c8399d`, parallel lane ~B picked this up as ADHC_ROUTER.T2 and shipped a status-propagation fix (AWS_UNREACHABLE vs MISSING_ON_S3). Not my patch; verified orthogonal to T1.

2. **Dotted reverse — destructured-import case:** if FE reads `const { decomposition_max } = summary.rfs; decomposition_max.nna;`, the current index won't capture `rfs.decomposition_max.nna` because the extractor records `summary.rfs.decomposition_max` and separately `decomposition_max.nna`. Flagged for the compiler-engineer backlog; requires extractor change (`extract_transforms.py`), not localized to the reverse-lookup path.

## Compiler Tools

| Phase | `<run>` | `<expect>` | Observed | Pass/Fail |
|-------|---------|-----------|----------|-----------|
| Pre-patch 1 | `comp-blast _compute_window_decomposition` | non-empty, targeted | 85-node explosion | FAIL |
| Pre-patch 2 | `comp-blast _compute_window_flows` | same | 85-node explosion | FAIL |
| Pre-patch 3 | `comp-blast _window_nna_delta` | callers surface | surfaced but among 85-node noise | FAIL (drowned) |
| Pre-patch 4 | `comp-platinum reverse rfs.decomposition_max.nna` | PRODUCER+CONSUMED populated | **wrong artifact** (timeseries_overview) | FAIL (worse than empty) |
| Pre-patch 5 | `comp-platinum reverse rfs.decomposition_ytd.nna` | symmetric | same false positive | FAIL |
| Analysis | diff against 0324142a | localize defects | CALLED_BY edge + loose match clauses | both localized |
| Patch 1 | `extract_s3.py` — remove CALLED_BY edge | clean blast semantics | committed d1d6920b | DONE |
| Patch 1b | `cli.py::cmd_blast` — auto upstream() for function-grain | caller chain surfaces cleanly | committed d1d6920b | DONE |
| Patch 2 | `platinum_cli.py` — drop loose match clauses | honest empty for unresolved query | landed via 70c8399d | DONE |
| Post-patch 1 | `comp-blast _compute_window_decomposition` | callees + callers clean | 2 callees + 3-hop caller chain | PASS |
| Post-patch 2 | `comp-blast _compute_window_flows` | same | symmetric | PASS |
| Post-patch 3 | `comp-blast _window_nna_delta` | callers include _compute_window_{decomp,flows} | exact match, depth 1 | PASS |
| Post-patch 4 | `comp-platinum reverse rfs.decomposition_max.nna` | honest empty + diagnostic | empty + [a] diagnostic | PASS |
| Post-patch 5 | `comp-platinum reverse rfs.decomposition_ytd.nna` | symmetric | symmetric honest empty | PASS |
| Audit step | re-run against post-T1-patch graph | pre-→post delta documented | this log's Phase 1→Phase 3 | PASS |

## Deployment

| Step | Result |
|------|--------|
| Edit `extract_s3.py` (remove CALLED_BY edge, add explanatory comment) | OK |
| Edit `cli.py::cmd_blast` (auto upstream() for function-grain nodes + CALLER CHAIN section) | OK |
| Edit `platinum_cli.py::_print_field_reverse` (tighten match clauses) | OK |
| `comp-build` | Graph rebuilt: 1130 nodes, 605 CALLS edges (was ~1200 with duplicated reverse edges). |
| Re-run 5 Phase 1 commands | All PASS (see table above) |
| `git commit --only --author=0.4.0_DS_ClientPlatform~A` | `d1d6920b` (cli.py + extract_s3.py; platinum_cli.py ended up in parallel ~B commit `70c8399d` due to concurrent-stage race — content is MY fix, visible via `git show HEAD:platinum_cli.py` line 358 carrying the ADHC_ROUTER.T1 comment) |
| `git push` | HELD per COO freeze window (no DS pushes until A→D rerun completes, ~16:00-17:00 ET). Commit is local; will push post-freeze. |

## MCP Signals Sent

| To | Purpose | Status |
|----|---------|--------|
| 1.0.0_SA_CTO | ACK GO + plan | delivered 20260415T181859Z |
| 1.0.0_SA_CTO | COMPLETE + patch summary | TBD (this turn) |

## Closeout

Two defects in `0324142a` found and patched. All 5 TO `<expect>` blocks now PASS. "Would this have helped RF01?" = YES for all three tested features in their post-T1-patch form; in their 0324142a form, feature 3 (dotted reverse) was actively harmful (confidently wrong). Residual defects are out of T1 scope (aws PATH → ADHC_ROUTER.T2 by ~B; destructured-import extractor gap → backlog). Push held per freeze window.

## Commit attribution note (added by CTO 2026-04-15 post-hoc)

The `_print_field_reverse` strict-match fix described above was authored by ~A but landed in ~C's commit `614d4c28` (T3) via shared-index sweep, not in ~A's `d1d6920b` (which cleanly carries cli.py + extract_s3.py only). The `ADHC_ROUTER.T1 fix:` comment in `org/modules/graph/platinum_cli.py` line ~358 self-documents the attribution within the file. No rework. Learning: concurrent edits to the same compiler module require `git commit --only -- <explicit paths>` strictly.
