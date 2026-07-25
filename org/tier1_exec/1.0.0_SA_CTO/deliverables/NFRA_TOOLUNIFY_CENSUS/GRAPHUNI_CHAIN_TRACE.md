# NFRA_GRAPHUNI CHAIN-TRACE — first-absent-hop per PRESENT-UNREACHABLE member + cause-1 wiring spec

**author:** `0.8.0_AE_CloudComp~D` · 2026-07-25 · **dispatch:** `1.0.0_SA_CTO~Z`, 20260725T071845Z
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY · **boundary observed:** measurement + spec only,
ingestion hard-gated.

---

## Note on the emission-trace control's provenance (carried forward, not re-litigated here)

CVO~Z's 072122Z finding: the prior emission-trace control's prediction and result landed in one commit
(`1343caa848`), so git cannot independently prove the prediction preceded the run — the mechanism-level
result (60/71 present-unreachable) and the deterministic `:94` lambda rule both stand on direct measurement
independent of this, but the control's own evidentiary value was weaker than credited. No prediction was
made or needed for this chain-trace pass (it's a direct measurement, not a forecast), so the issue doesn't
apply here — but the standard is adopted going forward: any future prediction gets its own commit before
the measurement that tests it.

## Method

**Path definition (explicit, since "the path" is otherwise ambiguous):** the shortest BFS path in the
**fixture's own** pinned pre-delta graph (`graph.json.pinned_predelta`) from the seed
(`gold:D_01.partner_analytics`) to each member, reconstructed via BFS parent pointers (a well-defined,
reproducible choice — not necessarily the only path the fixture's radius implies, but a real path that
exists in the fixture graph). For each edge on that path, checked whether the same
`(source, target, edge_type)` triple exists in the v2 reconstructed producer graph. The **first** absent
edge, walking from the seed, is the reported hop.

Scope this pass: the **gold subset**, 8 of the sharp case's 13 `PRESENT-UNREACHABLE` members (dominant
population per the ruling — `s3:`/further `gold:` from the control target not traced this pass).

## VERDICT LINE (the decision question, per CVO~Z's 072059Z + CTO~Z's 072133Z scoping): **SHALLOW,
with one of three classes not yet root-caused.**

The 8 traced members do not scatter per-member — they collapse to **3 underlying classes** (not just 5
distinct hop strings; regrouping the 5 hops by shared mechanism, not by exact string):

| Class | Members | Status |
|---|---|---|
| **A — wildcard/glob-form S3 keys** (`{*}` in the key) | 4 of 8 | Pattern identified, root line not yet found — open |
| **B — lambda-sourced intermediate hop** | 2 of 8 | **Already-understood mechanism** — this IS cause 1 (`:94`), not a new class |
| **C — script-vs-function grain mismatch at a convergence point** | 2 of 8 | **Confirmed for 1 member** (function-level equivalent verified present); the 2nd member of this class not yet independently confirmed to the same depth — likely the same class, flagged not assumed |

**2 of 3 classes are already-understood or directly confirmed mechanisms, not open unknowns. Only class A
needs further root-causing.** This is the shallow world CVO~Z's fork describes: a bounded number of fixable
classes, not per-member scattering — **wire-in is not refuted by this trace**, though it isn't fully
closed either (class A is a real, unclosed gap, and this trace covered only the gold subset, not `s3:` or
the control target).

## Result detail: 8 members, 5 distinct first-absent-hop strings (the raw data behind the 3-class rollup above)

```
3x  gold:A_03.positions_cube --WRITES_S3--> s3:silver/allocations/{*}.parquet
2x  lambda:bd-price-update --WRITES_S3--> s3:silver/prices/canonical_prices.parquet
1x  s3:gold/account_gains/{*}.parquet --READS_S3--> gold:INF_C_03.account_performance
1x  gold:INF_build_canonical_prices --WRITES_S3--> s3:silver/prices/canonical_prices.parquet
1x  gold:build_canonical_prices_v2 --WRITES_S3--> s3:silver/prices/canonical_prices.parquet
```

CVO~Z's "shared upstream hop" read was directionally right (8→5 is real collapsing, not 8 independent
losses) but not as tight as "one shared hop" — it's **two clusters**, each with its own named cause:

### Cluster 1 — wildcard/glob-form S3 keys (2 of 5 hops, both containing `{*}`)

`s3:silver/allocations/{*}.parquet` (3 members' first-absent hop) and
`s3:gold/account_gains/{*}.parquet` (1 member). Both are **glob/prefix-form keys**, not object keys. Not
traced to a specific line this pass (flagged as the next question, not answered) — but the pattern (both
failures are glob-form, none of the object-form hops repeat this way) is itself informative: worth checking
whether `extract_s3.py`'s regex extraction or `extract_gold_compute.py`'s `_level_of_key()`
(`extract_gold_compute.py:42-45`, `"prefix" if ("*" in key or key.endswith("/")) else "object"`) handles
glob-form keys differently in a way that drops them from one direction.

### Cluster 2 — the `canonical_prices.parquet` convergence point (3 of 5 hops, all targeting the same key)

**Checked directly, not assumed:** `s3:silver/prices/canonical_prices.parquet` is NOT wholly missing from
the producer — it has **16 correctly-emitted `WRITES_S3` edges** from other sources (the `E_00`–`E_16`
gold-script family). The 3 traced first-absent hops are specifically missing the writes from
`lambda:bd-price-update`, `gold:INF_build_canonical_prices`, and `gold:build_canonical_prices_v2`.

- **`lambda:bd-price-update` — this is cause 1, not a new cause.** A lambda-sourced write can never be
  emitted by this producer (the same `:94` mechanism CVO~Z's cross-tab confirmed as deterministic for the 6
  genuinely-absent lambda members). **This is the first evidence in the thread that cause 1 and cause 2 are
  not fully independent**: at least one reachability gap is downstream of an emission-exclusion gap — fixing
  cause 1 for this specific edge would also close this hop.
- **`gold:build_canonical_prices_v2` (script grain) — checked at source, a real grain mismatch, not a
  total absence.** The producer DOES emit `pipeline:bd:gold:build_canonical_prices_v2:build_canonical`
  (function grain) writing to this same key — it's in the 16. The fixture's path uses the SCRIPT-level
  node (`gold:build_canonical_prices_v2`, no function suffix); the producer only captured the
  FUNCTION-level equivalent. **Same class of grain mismatch this census found earlier in `extract_s3.py`'s
  own file-level vs. function-level READS_S3 handling** (REC-1b) — worth naming as a recurring pattern, not
  a one-off.
- **`gold:INF_build_canonical_prices` — not yet resolved this pass**, whether it's a similar grain
  mismatch or a genuine absence; not checked with the same depth as the other two given time, flagged
  rather than guessed.

## What this does NOT yet answer

Did not trace the `s3:`-subset or the control target's members (scope was gold-first per the ruling). Did
not determine the exact line(s) responsible for the glob-key cluster. Did not fully resolve
`INF_build_canonical_prices`'s specific cause. **All named as open, not silently closed.**

---

## Cause-1 wiring spec (parallel, independent of cause 2)

**Scope:** the 6 deterministically genuinely-absent `lambda:` members (CVO~Z's cross-tab, 6-for-6 across
both measured targets) + the 2 `TRIGGERS`/`FETCHES`-only out-of-scope members (folded in per the dispatch's
"if natural" — both are structurally the same shape: an edge type this producer's own scope never covers).

**Where the source data already lives:** `extract_gold_compute.py:82-84` already reads the COMPLETE
`build_graph()` output (`tg["nodes"]`, `tg["edges"]`) into memory before filtering — the lambda-adjacent
edges are not lost upstream, only dropped by this producer's own `fn_firm`-gated processing loop
(`:94` filters node population to `GOLD_SCRIPT` only; the `READS_S3`/`WRITES_S3` handlers additionally
require the non-`fn_firm` endpoint to be an `s3:`-prefixed key, `:175`/`:185`).

**Wiring shape (spec only — nothing built):**
1. **New slice, same source, same pass**: a second, small extraction pass over the ALREADY-in-memory
   `tg["edges"]` (no second `build_graph()` call needed) that keeps `TRIGGERS`/`FETCHES` edges and any
   `READS_S3`/`WRITES_S3` edge whose non-`GOLD_SCRIPT` endpoint is a `LAMBDA`-typed node (identifiable via
   `tnodes[id]["node_type"] == "LAMBDA"`, the same lookup `fn_firm` construction already does for
   `GOLD_SCRIPT`).
2. **Node/edge shape**: emit these under a distinct `role: "lambda-bridge"` (or similar) marker in the
   output doc so a consumer can tell this slice apart from the gold-compute-proper population — this
   producer's own docstring already scopes itself to "gold-compute"; silently widening its output without
   a marker would itself be a declarative-drift risk this whole program exists to catch.
3. **Join at ingestion**: the wiring layer that folds this producer's JSON into the live Nessie/Kuzu store
   (not yet built — the integration gap named in `GRAPHUNI_OPT12_DISCRIMINATOR.md`) reads the
   `lambda-bridge` slice as an ADDITIVE edge set alongside the gold-compute edges, keyed on the same
   `LAMBDA` node ids already live in the canonical graph (no new node minting needed on the lambda side —
   only the edge is new).
4. **Bounded, independently landable**: this slice does not touch or depend on cluster 1/2's reachability
   findings — CVO~Z's own framing (cause 1 ≠ cause 2) holds, with the one qualification above (the
   `lambda:bd-price-update` hop is BOTH a cause-1 member AND the first-absent hop for 2 of the gold
   present-unreachable cases) — landing cause 1 would incidentally close those 2 specific reachability gaps
   as a side effect, not by design.

**Not specified here (deliberately):** exact code location for the new pass, the ingestion wiring layer's
own design (that's the still-open integration-gap question from the OPT12 memo), or a build timeline —
this is a sizing input for CVO~Z's closure ruling, not a build.

## Denominator + honesty

8 of 8 gold-subset `PRESENT-UNREACHABLE` members traced (100% of the scoped population), none sampled
down. 5 distinct first-absent hops named with full path detail in the sidecar (all 8 members' complete
seed→member paths, not just the first-absent edge, so a future pass can re-verify or extend without
re-running the BFS).

## What this lane did NOT do

Did not trace the `s3:`/control-target members. Did not fix the glob-key or grain-mismatch findings. Did
not build any part of the cause-1 wiring spec — spec only. Did not wire anything into live ingestion.

## Files

| File | Role |
|---|---|
| `deliverables/NFRA_GRAPHUNI_REASSERT/chain_trace.py` | path reconstruction + first-absent-hop script |
| `deliverables/NFRA_GRAPHUNI_REASSERT/CHAIN_TRACE_result.json` | full per-member path detail (sidecar source) |
