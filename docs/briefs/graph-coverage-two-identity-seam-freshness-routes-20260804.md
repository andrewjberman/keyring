# BRIEF: the estate graph models served artifacts TWICE, under two identities that do not reference each other

**Author:** `0.7.0_AE_CloudOps~B` · **2026-08-04** · **Status:** FOR CVO ASSESSMENT
**Requested by:** Andrew-direct, ~0620Z, verbatim: ***"write a brief on this matter, relay it to
cvo saying that i want them to assess this"***
**Assessor:** `3.0.0_SA_CVO` · **Posture:** read-only measurement; nothing edited, nothing proposed

---

## 1. WHAT PROMPTED THIS

Andrew asked a direct challenge after I claimed nobody had examined the estate's freshness
surfaces for deprecated-route signal:

> ***"how would those not appear in comp-blast if comp-blast surfaces the entire kuzudb graph layer"***

**He was right and my claim was wrong.** They do appear. But measuring *how* they appear surfaced
something worth an independent look, which is why this brief exists rather than a one-line
retraction.

**Upstream context (both Andrew-direct, same session, recorded at `@2937949e2`):** the MDPF
freshness gate was terminated (gate only; the trigger survives), and an estate-wide freshness
kill is **on the table but withheld** for one stated reason -- *"i bet they are homing signals
for where deprecated routes are."* **If freshness surfaces are to be read as a route map, how the
graph models routes is load-bearing.**

---

## 2. WHAT WAS MEASURED (all controlled; comp-kuzu, canonical auto-refreshing DB)

Graph: **20,495 nodes / 41,010 edges**, two tables only -- `CloudNode`, `CloudEdge`.
Node-type census taken; the two types that matter here:

```
S3Key      232 nodes     gold/ 141 · platinum/ 48 · silver/ 25 · json/ 0
ServedURL   45 nodes     form: endpointurl:/api/general/benchmarks/benchmark_returns.json
```

Both dumps control-verified against the census totals (232 == 232, 45 == 45); a prior extraction
that silently produced 0 rows was caught by that control and discarded.

**Route presence, against the 13 entries in `data/served_freshness_config.yaml`:**

| queried as | result |
|---|---|
| `S3Key` | **1 of 11** terms present -- `aggregate_aua_timeseries` (UNDERSCORE, platinum tier) |
| `ServedURL` | **4 of 5** served terms present -- `aggregate-aua-timeseries`, `benchmark_returns`, `fear-greed-index`, `model_portfolio_benchmarks` |

**Edges out of the producer-side node** (`MATCH (a)-[e]-(b) WHERE a.name CONTAINS 'aggregate_aua_timeseries'`):

```
S3Key          --CONTAINS-->    S3_BUCKET       opal-data-mdpf
S3Key          --OWNED_BY-->    S3_BUCKET       opal-data-mdpf
S3Key          --WRITES_S3-->   PipelineScript  build_aggregate_aua_timeseries
PipelineScript --WRITES_S3-->   S3Key           platinum/mdpf/aggregate_aua_timeseries.json
PipelineScript --RUNS-->        EC2_INSTANCE    mdpf-daily-runner
PipelineScript --CONTAINS-->    Pipeline        mdpf-gold
(+ C2Motif structural edges)
```

**No edge to any `ServedURL` node appears in that traversal. The chain terminates at platinum.**

---

## 3. THE OBSERVATION

The same logical artifact carries **two identities in the graph**:

| side | node type | identity | naming |
|---|---|---|---|
| producer | `S3Key` | `platinum/mdpf/aggregate_aua_timeseries.json` | **underscore**, S3 key, bucket-less |
| served | `ServedURL` | `endpointurl:/api/.../aggregate-aua-timeseries.json` | **hyphen**, API path |

Three consequences follow, and **the third is the reason this is a brief and not a note**:

1. **The producer chain is richly modeled and stops at platinum.** A blast from the producer does
   not reach the served artifact; a blast from the served side does not reach the producer.
2. **`json/` -- the served S3 tier the portal actually reads -- has ZERO of the 232 `S3Key`
   nodes.** The served tier is modeled as API paths, not as storage keys.
3. **The freshness config addresses routes by S3 URI (`s3://bucket/key`), a form matching NEITHER
   node's naming scheme.** So an instrument reading the freshness config and an instrument
   reading the graph are addressing the same artifacts through three different vocabularies:
   S3 URI, bucket-less S3 key, and API endpoint path.

**The underscore/hyphen split is the already-recorded 4-way name-collision hazard, here visible
inside the graph's own model.** A query written for one form silently answers about the other
object, or about nothing.

---

## 4. WHAT I DID **NOT** ESTABLISH -- read these as hard limits on the above

- **I did not verify what `comp-blast` specifically traverses.** The claim that it "surfaces the
  graph" is Andrew's framing and is plausible; I measured the GRAPH, not the TOOL. **Whether
  comp-blast crosses node types, or filters to a subset, is unmeasured.**
- **Absence in one traversal is not absence in the graph.** I ran a single undirected 1-hop match
  from one producer node. **A producer->served path may exist via a hop I did not query.**
- **Single specimen.** The edge analysis covers `aggregate_aua_timeseries` only. Whether the
  disconnect generalises across the other 231 `S3Key` / 44 `ServedURL` nodes is **untested.**
- **I did not test the older per-pipeline `gold_freshness_config.yaml` files or the 119 files
  carrying embedded freshness/staleness logic** -- the surfaces where Andrew's deprecated-route
  signal would more plausibly live.
- `advisor_nna_canonical` was absent from BOTH types. **Unexplained; not chased.**

---

## 5. WHY AN INDEPENDENT ASSESSOR, STATED PLAINLY

**My own measurement error rate on this specific question was high, and the assessor should
weight the findings accordingly.** In the course of this one investigation I produced:

- a `head-object` probe run against **directory prefixes**, which structurally cannot succeed --
  it returned ABSENT for 5 routes that are all live;
- a corrected probe that emitted a **20,669-day** age (epoch-fallback artifact);
- an extraction that silently yielded **0 rows** and would have reported 11 false absences;
- a first graph query keyed on `type` instead of `node_type`, returning empty;
- **the original wrong claim** that these surfaces were unexamined -- which is what Andrew
  challenged.

**Four were caught by controls or implausibility. One was caught by Andrew.** Every number in
section 2 carries a control *because* of that record. **The pattern is consistent and worth the
assessor's attention in its own right: these probes fail toward "nothing here," and "nothing
here" is the reading nobody investigates.** A false ABSENT is more dangerous than a false STALE,
because a false STALE gets checked.

---

## 6. WHAT IS BEING ASKED

Andrew's instruction is **"assess this"** and I am not narrowing it. Scoping is the assessor's.
Offered as candidate questions, not as a mandate:

- Is the producer/served identity split **by design** (two legitimate planes) or **drift** (one
  artifact that lost its link)? Does an edge exist that my single traversal missed?
- Does `comp-blast` actually cross the two node types? If not, what does a blast radius on a
  served artifact omit?
- Is `json/` having **0 of 232** `S3Key` nodes intended coverage or a modelling gap -- given it
  is the tier the portal reads?
- Does the three-vocabulary addressing (S3 URI / bucket-less key / API path) admit a reliable
  join, or is cross-instrument correlation currently unsound?
- Andrew's standing hypothesis: **can the freshness surfaces be read as a deprecated-route map,
  and does the graph help or hinder that read?**

**Nothing in this brief authorizes a change.** It is a measurement and a set of stated limits.

---

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| `comp-kuzu` | `CALL show_tables()` | 2 tables (CloudNode/CloudEdge) | canonical DB, auto-refreshed, header read |
| `comp-kuzu` | node_type census | 30 types; S3Key 232, ServedURL 45 | the denominators for everything above |
| `comp-kuzu` | S3Key + ServedURL dumps | 232 / 45, **both control-matched** | a prior 0-row extraction was caught and discarded |
| `comp-kuzu` | 1-hop edges from the producer node | 10 edges, none to ServedURL | **single specimen -- see section 4** |
| `aws lambda list-functions` | name filter + positive control | 0 checker-named fns of 50 total | control returns `mdpf-daily-trigger` |

**What failed:** see section 5. It is the substance of the brief's own reliability statement,
not an appendix to it.
