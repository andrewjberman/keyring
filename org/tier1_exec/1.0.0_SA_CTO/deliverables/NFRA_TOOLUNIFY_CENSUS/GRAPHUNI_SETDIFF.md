# NFRA_GRAPHUNI SET-DIFF — enumerated missing members, partitioned by edge class, function-grain control

**author:** `0.8.0_AE_CloudComp~D` · 2026-07-25 · **dispatch:** `1.0.0_SA_CTO~Z`, 20260725T065418Z
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY · **boundary observed:** measurement only, no
ingestion wiring, no live/S3 writes.

---

## CORRECTION FIRST — the OPT1_RUN.md sharp-case number was measuring the wrong node

Building the set-diff harness surfaced a real methodology bug in the prior deliverable's reconstruction
script (`opt1_setcompare.py`, v1). **`TraceGraph.find_node()` is a substring match, and `cli.py:568`'s
`cmd_blast` uses only `matches[0]`** (the FIRST match, not a union — a detail CVO~Z's own seed-count
analysis didn't need to resolve, since it only checked match COUNT, not which specific node index 0 lands
on). `matches[0]` is decided by **node insertion order into `TraceGraph.nodes` (a dict)**. The original
`build_graph` (`extract_s3.py:347-377`) always inserts a script's own node before its function children, so
`matches[0]` for a script-level query reliably resolves to the script node. **v1's reconstruction built
nodes lazily off EDGE iteration order** (whichever node an edge happened to reference first), which
scrambled that guarantee — verified directly: `find_node('gold:D_01.partner_analytics')[0]` in v1 resolved
to `gold:D_01.partner_analytics:get_periods`, a FUNCTION node, not the script node. **v1's "5 of 216"
sharp-case number was the radius of the wrong node, not a measurement of the intended target.**

**Fixed in v2** (`opt1_setcompare_v2.py`): nodes are pre-populated from the producer's own `nodes` list (in
its own order — confirmed source-side that the producer preserves script-before-function ordering,
inherited transitively from `build_graph`'s own insertion sequence) before any edge is processed.
**Verified the fix holds**: `find_node('gold:D_01.partner_analytics')[0].id == 'gold:D_01.partner_analytics'`
asserted true before trusting anything downstream of it.

**The aggregate verdict is UNCHANGED: still SET-IDENTITY REFUTED, 11/28.** The bug was concentrated in this
one sharp case (and whatever few other sample targets share the same collision shape), not the whole
sample — the overall match count held. **What changes is the sharp case's own number, corrected below, and
it changes the qualitative picture substantially for the better.**

---

## Corrected sharp case: 19 missing (not ~211), 3 extra, out of 216 expected — 91% already covered

```
SET-DIFF script case: 19 missing / 216 expected; 3 extra
SET-DIFF function control: 0 missing / 39 expected; 0 extra
```

The function-grain control is **zero missing, zero extra, exact** — the fourth independent confirmation
this session (live marker-head, v1 reconstruction, and now v2 twice: the aggregate 28-target pass and this
specific control) that function grain is clean. Per CVO~Z's own framing: this rules the METHOD trustworthy
(a suspect method would show gaps here too) and isolates the deficit to script grain specifically.

## Edge-class partition of the 19 script-grain missing members

```
READS_S3,WRITES_S3         6
READS_S3,TRIGGERS,WRITES_S3  4
CALLS,WRITES_S3            4
TRIGGERS                   2
READS_S3                   2
FETCHES,READS_S3           1
```
(Full per-member list with its edge-class set in the sidecar, `GRAPHUNI_SETDIFF.sidecar.json`.)

**This directly discriminates the fork CTO~Z named, and the answer is split, not single-cause:**

- **`TRIGGERS` and `FETCHES` appear on 7 of the 19 missing members** (6 with TRIGGERS, 1 with FETCHES,
  some overlapping with READS_S3/WRITES_S3). **These edge types are structurally outside this producer's
  scope** — `extract_gold_compute.py`'s own `coverage.slices_scanned` states its scope exactly:
  `"gold-compute (CALLS + READS_S3/WRITES_S3 + compute CONTAINS)"`. `TRIGGERS` comes from
  `extract_eventbridge_edges`/`extract_lambda_routes` (EventBridge/Lambda-invoke passes); `FETCHES` from
  the platinum/routing layer. **A gold-compute producer was never going to emit these — this portion of
  the gap is out-of-scope by design, not a defect in what this producer covers.**
- **The remaining members are reached purely via `READS_S3`/`WRITES_S3`/`CALLS`** (2 pure-`READS_S3`, the
  6 `READS_S3,WRITES_S3` combined, the 4 `CALLS,WRITES_S3` combined) — edges this producer DOES emit and
  is scoped to cover. **This is the genuine, in-scope residual**: roughly 12 of 19 members (the ones whose
  edge-class set contains no `TRIGGERS`/`FETCHES`) are missing via edges the producer is supposed to
  provide, and does not, for these specific reachability chains.

**Reading the combined-class entries correctly:** an edge-class SET on a missing member (e.g.
`READS_S3,WRITES_S3`) means that node is connected into the radius by more than one edge in the fixture's
own multi-hop BFS (it may be reachable via a `WRITES_S3` edge from one predecessor AND a `READS_S3` edge
from a different predecessor) — not that a single edge carries two types. So `READS_S3,WRITES_S3:6` does
not mean 6 uses of one combined edge; it means for 6 members, BOTH a `READS_S3`-typed and a
`WRITES_S3`-typed edge exist somewhere on their path/predecessor set in the fixture graph. The
still-real, still-relevant finding stands regardless of this nuance: **`READS_S3` participates in 13 of 19
missing members' connecting-edge sets (68%), `WRITES_S3` in 14 of 19 (74%)** — both are heavily
represented, consistent with (though not exclusively proving) this session's earlier finding that the
producer under-covers `READS_S3` reachability specifically; `WRITES_S3`'s comparable representation here
is a new data point this pass adds, worth carrying forward rather than assuming `READS_S3` is the sole
axis.

## The v1 bug's blast radius (so to speak) — 6 of 28 sample targets affected, all similarly

Diffed v1 vs v2 across the full 28-target sample (sidecar `GRAPHUNI_SETDIFF.sidecar.json`,
`v1_vs_v2_changed_targets`). **6 targets changed materially, all script-level** (the exact class the node-
order bug hits): `gold:D_01.partner_analytics`, `gold:D_04.client_portal_summary`,
`gold:INF_D_04.client_portal_summary`, `gold:D_00.portal_aggregates`, `gold:D_02.advisor_client_detail`,
`gold:B_02.canonical_lots`. Every one of them jumped from a single-digit `new_n` (3–6, reading as
near-total misses) to 92–98% of its `old_n` (e.g. 200/216, 114/130) once the node-order fix landed. **None
of the 6 became an exact MATCH** — all still carry a small, real residual, consistent with the sharp case's
19-missing/216 finding — so the aggregate 11/28 verdict is genuinely unchanged. But the *qualitative*
picture across the whole script-level slice of the sample is the same correction as the sharp case: a
handful of near-total-miss-looking numbers were mostly measurement artifact, not mostly real coverage
failure.

## What this changes about the picture

1. **The gap is much smaller than v1 suggested — 91% coverage on the sharp case, not ~2%.** REFUTED is
   still the correct verdict (member-level set-identity requires 100%, and 19 real gaps is not zero), but
   the earlier framing ("still-under-covering graph," "216 vs 5") materially overstated the size of the
   deficit due to the node-order bug.
2. **Roughly a third of the residual (7/19) is out-of-scope for this producer by design** (TRIGGERS/FETCHES
   come from different extraction passes entirely) — not something "wiring in this producer's output"
   could ever close, regardless of any future fix to it.
3. **The remaining ~12/19 in-scope gap** is consistent with, and now more precisely bounded than, the
   `READS_S3`-population concern already raised in `GRAPHUNI_OPT12_DISCRIMINATOR.md` — but this pass adds
   `WRITES_S3` as comparably implicated, which that earlier memo did not have grounds to claim.

## Denominator + honesty

28/28 blast targets re-run in the aggregate v2 pass (superseding v1's per-target numbers where they differ
— full v1-vs-v2 diff in the sidecar). Set-diff + edge-class partition run on exactly the 2 targets the
dispatch named (script sharp case + function control) — not sampled further, not silently narrowed. Edge
classes are read from the FIXTURE's own pinned pre-delta graph
(`graph.json.pinned_predelta`, loaded via `TraceGraph.load()`, the same file the original fixture capture
ran against) — not guessed, not inferred from the reconstruction's own (incomplete) edge set.

## What this lane did NOT do

Did not wire anything into live ingestion. Did not re-run comp-trace/comp-xref set-diffs (scope was the
blast sharp case + control, per the dispatch). Did not attempt to close the in-scope ~12-member gap or
determine whether it's a further extractor limitation vs. a genuinely absent source relationship — that is
follow-on work, not this dispatch's ask. Did not re-verify whether the v1 bug affected any of the OTHER 27
sample targets' individual numbers beyond confirming the aggregate 11/28 held — the full per-target v1-vs-v2
diff is in the sidecar for anyone who wants to check a specific target.

## Files

| File | Role |
|---|---|
| `deliverables/NFRA_GRAPHUNI_REASSERT/opt1_setcompare_v2.py` | corrected reconstruction + set-diff + edge-class script |
| `deliverables/NFRA_GRAPHUNI_REASSERT/OPT1_SETCOMPARE_v2_result.json` | corrected 28-target per-target result |
| `deliverables/NFRA_GRAPHUNI_REASSERT/SETDIFF_20260725_result.json` | the set-diff + edge-class result (this memo's sidecar source) |
