# NFRA_GRAPHUNI option-1-vs-2 discriminator — can the compute producer emit function/script-grain
# READS_S3, or is that data only available in build_graph's AST pass?

**author:** `0.8.0_AE_CloudComp~D` · 2026-07-25 · **dispatch:** `1.0.0_SA_CTO~Z`, 20260725T063020Z
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY
**scope discipline:** source question only, per dispatch — no build, no producer change, no re-point
executed. Every load-bearing claim below is a file:line citation, not a paraphrase.

---

## Answer, up front: (a)-with-caveats — but the caveat reframes the question

**The capability is not missing. It already exists, and it has already been exercised.** The GRAPHUNI
Phase-A/B compute producer (`infra/aws/globgrph/extract_gold_compute.py`) does not need a NEW ability to
emit function/script-grain `READS_S3` edges — it already runs `build_graph()` internally and already reads
`READS_S3` edges straight out of its output. A prior run's committed output,
`org/projects/NFRA_GRAPHUNI/NFRA_GRAPHUNI.P1-D.gold_compute_producer.json`, contains **192 `READS_S3`
edges at exactly the grain needed** — but **that file is never read back in by anything.** `grep -rln
"gold_compute_producer" --include="*.py" .` returns zero hits: no ingestion/fold step exists that loads
this JSON into the live Nessie/Kuzu store `comp_marker_read.py` queries. So CVO~Z's live count of 0
`READS_S3` (s3->function) is real and correctly measured — but its cause is an **integration gap** (a
computed artifact nothing consumes), not a **capability gap** (the producer cannot derive the edges). This
is the same shape as this project's own §0.2 through-line finding, independently rediscovered here.

---

## 1. WHERE build_graph's AST pass derives READS_S3 (the extractor, the evidence per edge)

`org/modules/graph/trace_graph.py:402-441` (`build_graph`) calls `extract_s3_edges` from
`org/modules/graph/extract_s3.py:329` as "Pass 2 (priority)".

**`extract_s3.py:448-455`** is the READS_S3 emission site:
```python
# File-level S3 reads (gold scripts reading from other scripts' output)
for s3_key in _extract_s3_reads(content, constants):
    s3_node_id = f"s3:{s3_key}"
    graph.add_node(Node(id=s3_node_id, node_type="S3_ARTIFACT", label=s3_key))
    graph.add_edge(Edge(source=s3_node_id, target=script_node_id, edge_type="READS_S3"))
```
`script_node_id` (defined at `extract_s3.py:347`, `f"gold:{py_file.stem}"`) is the **FILE-level** node —
**build_graph's own READS_S3 edges are already SCRIPT-grain, not function-grain, by construction.** There is
no per-function READS_S3 pass at all — contrast `WRITES_S3`, which has two dedicated function-level passes
(`_extract_functions_with_s3()` at `extract_s3.py:223`, `_extract_builder_to_save_mapping()` at
`extract_s3.py:178`, both keyed to `func_node_id`/`builder_node_id`, `extract_s3.py:399-445`).

**Evidence per edge:** `_extract_s3_reads()` (`extract_s3.py:296-322`) is a **regex/pattern scan over the
file's ENTIRE text content** (not an AST slice per function) — three regex families
(`_S3_GET_OBJECT`, `_S3_HELPER_READ`, `_S3_READ_PARQUET`) plus a constant-resolution pass
(`_S3_GET_CONST`), each matched against the whole `content` string (`extract_s3.py:301-320`). It structurally
cannot attribute a read to its enclosing function, because it never looks at function boundaries — it is a
whole-file scan by design, unlike the write-side passes which do walk per-function.

**So build_graph's own READS_S3 grain is SCRIPT, not function** — the pre-delta fixture's 306 "script-side
READS needed" (CVO~Z's phrasing) is exactly this file-grain edge, not some finer grain build_graph also
carries. This resolves a possible ambiguity in the question as posed: there is no function-grain READS_S3
in build_graph to begin with; the discriminator is whether the COMPUTE PRODUCER can reach build_graph's
actual (script-grain) READS_S3 edges, not whether it can go finer than build_graph does.

## 2. Does the compute producer already consume this — YES, at source, already exercised

`infra/aws/globgrph/extract_gold_compute.py:63`:
```python
from org.modules.graph.trace_graph import TraceGraph, build_graph, check_node_freshness
```
`extract_gold_compute.py:82-84` (`build()`):
```python
_ensure_fresh_tracegraph()   # HEAD-PIN (b): never fold a stale/divergent-vintage TraceGraph
with open(TRACEGRAPH, "r", encoding="utf-8") as fh:
    tg = json.load(fh)
```
(`_ensure_fresh_tracegraph`, `extract_gold_compute.py:53-63`, itself calls `build_graph` when the cached
`.comp-graph/graph.json` is stale.) The producer's INPUT is build_graph's own output — the exact same AST
pass CTO~Z's question contrasts it with. It is not a separate, independent, more-limited reader.

`extract_gold_compute.py:182-195` is the READS_S3 handling:
```python
elif et == "READS_S3":
    fn = t if t in fn_firm else (s if s in fn_firm else None)
    key = (s if isinstance(s, str) and s.startswith("s3:") else t)
    if fn is None or not (isinstance(key, str) and key.startswith("s3:")):
        continue
    kk = key[3:]
    # Phase-A: defer reads of a read-only INPUT (no gold writer = non-gold tier) to Phase-B.
    if phase_a and not ((firmq.get(kk) or {}).get("writer_firms")):
        deferred_phase_b.append("READS_S3 %s -> %s (read-only input, Phase-B)" % (fn, kk))
        continue
    sk = s3key_id(kk, owner_for_read(kk, fn_firm[fn]), "READS_S3 by %s" % fn)
    if sk:
        edges.append({"source": _pipeline_id(fn, fn_firm[fn]), "target": sk,
                      "edge_type": "READS_S3", "level": _level_of_key(kk)})
```
`fn_firm` (`extract_gold_compute.py:92-98`) is populated from **every** `GOLD_SCRIPT`-typed node in the
TraceGraph regardless of whether it carries a `function_name` — i.e. it includes the SCRIPT-level nodes
build_graph's `READS_S3` edges actually target (`t` above resolves to the script node id, e.g.
`gold:A_00.accounts_dimension`, matching `fn_firm`'s keys directly, per `extract_s3.py:347`'s naming
convention). **So the producer's READS_S3 handling already operates at the same grain build_graph emits —
no rollup, no adapter, no new logic is needed to pick these edges up.**

**Proof this already ran and produced real output, not a hypothetical:**
`org/projects/NFRA_GRAPHUNI/NFRA_GRAPHUNI.P1-D.gold_compute_producer.json` (a prior, committed run of this
exact producer) contains:
```
edge_type counts: CALLS=1635, CONTAINS=1344, WRITES_S3=270, READS_S3=192
```
Sample READS_S3 entries (verbatim from the file):
```json
{"source": "pipeline:bd:gold:A_00.accounts_dimension",
 "target": "opal-data-bd/gold/dimensions/accounts_dimension_latest.parquet",
 "edge_type": "READS_S3", "level": "object"}
{"source": "pipeline:bd:gold:A_01.advisor_assignments",
 "target": "opal-data-bd/gold/_state/advisor_assignments/daily_state.parquet",
 "edge_type": "READS_S3", "level": "object"}
```
`gold:A_00.accounts_dimension` and `gold:A_01.advisor_assignments` are **exactly two of the nodes** this
session's fresh re-measurement (`REASSERT_20260725_result.json`) found MISSING from
`gold:D_01.partner_analytics`'s live blast radius. **The edges needed to close that gap were already
computed, on 2026-07-2x [see file's own coverage block for exact provenance -- no `generated_at` timestamp
was stamped in this copy, `extract_gold_compute.py:199`'s comment says it stamps "at emit time"; not
independently dated further here, flagged rather than guessed], and are sitting in a tracked JSON file
right now.**

## 3. The caveat — why the live measurement still reads 0

`grep -rln "gold_compute_producer" --include="*.py" .` (this workspace, this session) returns **zero
matches.** No script reads `NFRA_GRAPHUNI.P1-D.gold_compute_producer.json` back in. There is no fold/ingest
step wiring this producer's output into the Nessie/Kuzu store that `comp_marker_read.py` queries at the
marker head. **The 192 edges are real, correctly derived, and orphaned** — a control that ran and produced
correct output that nothing downstream consumes, the same class this whole project's §0.2 through-line
names, found here independently.

**Second caveat, smaller: Phase-A scope is not yet complete even if ingestion is fixed.**
`extract_gold_compute.py:76-80`'s own comment: Phase-A **deliberately defers** `READS_S3` edges whose
target key has no `writer_firms` in `NFRA_GRAPHUNI.P1.d_s3key_firm_qualified.json` (read-only,
non-gold-tier inputs) to Phase-B. The producer's own `coverage.phase_b_deferred_count` in the committed
JSON is **112**. `192 + 112 = 304`, within rounding of CVO~Z's "306 script-side READS needed" (the small gap
is very likely the two `S3KEY_FIRM_UNRESOLVED` cases the same coverage block names explicitly —
`gold/timeseries/client_performance.parquet` read by `build_mdpf_wsc_inflection_feeder` and
`build_mdpf_inflection_history_from_spine` — not silently unaccounted). **So: wiring the existing 192-edge
output into the live graph would close most, not all, of the gap; the remaining ~112 are a real, separate,
already-named Phase-B scope item, not a new discovery.**

## 4. Direct answer to the option-1-vs-2 framing

Neither original option is quite what the evidence supports:
- **NOT option 2 as originally framed** ("structurally tied to the full AST traversal, un-reproducible by
  the marker-head path") — FALSE. The marker-head compute path already runs the full AST traversal itself
  (`extract_gold_compute.py:63,82-84` call `build_graph` directly) and already has code to consume its
  READS_S3 edges at the correct grain.
- **NOT quite option 1 as originally framed** either, if "re-populate marker-head at build_graph fidelity"
  implies new derivation work — the derivation already happened and is sitting on disk, unconsumed.
- **The actual gap is narrower and cheaper than either option: wire the existing, already-computed
  `NFRA_GRAPHUNI.P1-D.gold_compute_producer.json` (or a fresh re-run of the same producer, since this copy's
  vintage is unstamped) into the live Nessie/Kuzu ingestion path, then separately decide Phase-B's disposition
  for the remaining ~112 read-only-input edges.** This is a costed, concrete next step, not a design fork
  between two expensive alternatives.

## What this lane did NOT do

Did not run `extract_gold_compute.py`, did not modify it or `comp_marker_read.py`, did not touch the
ingestion path (none was found to touch), did not fold the 192-edge JSON into anything live. Did not
independently re-date the committed `gold_compute_producer.json`'s vintage beyond what its own coverage
block states (flagged as unstamped in §2, not guessed). Did not verify the 2 `S3KEY_FIRM_UNRESOLVED` cases
beyond quoting the producer's own coverage block. Source-only, per the dispatch's explicit scope.
