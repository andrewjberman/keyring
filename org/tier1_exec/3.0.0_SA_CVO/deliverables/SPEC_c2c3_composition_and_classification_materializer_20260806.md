# SPEC — the C2/C3 materializer: DETERMINISTIC COMPOSITION + a cheap CLASSIFICATION pass

**Owner:** `3.0.0_SA_CVO` (Andrew-routed 2026-08-06: *"Route this to CVO, the C2/C3 materializer is
theirs."*). **Date:** 2026-08-06 ~23:30Z.
**Supersedes** the grain-overlap mechanism in `SPEC_grain_overlap_…` @137a047c1 (void, three
independent reasons) and my own retracted ruling of 230211Z.

## 0. Andrew's design, verbatim — this spec implements exactly this and nothing more

> *"the idea behind doing this was that we'd deterministically compose the structures (the 1000+
> number) but we'd run an LLM over it to classify them"*
> *"just so that there is a classification touchpoint there and understanding 'what this motif is'
> doesnt have to be rederived"*
> *"for the cost of a very cheap llm pass"*

**Ruled the same session:** composition runs over the **FULL GRAPH**; classification **writes back
into kuzu as NODE PROPERTIES**.

## 1. What is actually there today — measured, and it answers his question

He asked: *"which makes me wonder how exactly these numbers are being compiled."*
**They are not compiled. They are read from hand-authored JSON.**

| | measured |
|---|---|
| `derive_runner.py:1417` | iterates `C2C3_MOTIF_SPEC_PATHS`, `json.load`s each, folds `doc["nodes"]` into the graph verbatim |
| `motif_c2c3_materialize.json` | **15,255 bytes · 7 nodes (6 C2Motif + 1 C3System) · 36 edges** |
| sibling `_ab.json` | the remainder, to the 23 total (19 `C2Motif` + 4 `C3System`) |
| first node | `motif:silent-display-fork` — **one of the six DEBT detector motifs the canonical YAML calls "a shadow"** |
| its props | `{"motif_type": "SilentDisplayFork", "recurrence": 5, **"n_instances": 5**}` |

>> **`n_instances: 5` IS THE WHOLE FINDING. The spec KNOWS there are five occurrences and emits ONE
> NODE FOR THE CLASS. The instance count is recorded as a PROPERTY and the instances are never
> individuated.** The composition step was not broken — **it was never written**, and a hand-authored
> file stamped `source: semctl-c2c3-materialize` has been standing in for it. <<

**Consequence measured earlier:** `BDataflowMotif CONTAINS 1336`. `CONTAINS` became a *classification*
edge — 1,336 nodes pointing at the category that describes them — because there was no instance layer
for them to belong to.

## 2. The three stages

```
  STAGE 1  COMPOSE     full graph -> C2 motif INSTANCES        DETERMINISTIC   re-derivable, no model
  STAGE 2  AGGREGATE   motif instances -> C3 STRUCTURES        DETERMINISTIC   connected components
  STAGE 3  CLASSIFY    each composed unit -> a canonical label INFERENTIAL     one cheap LLM pass
```

**The deterministic/inferential split is the spine and it is already estate vocabulary** — the
`deck_generation` orchestrator's organizing principle, adopted into CTO~B's staged-run substrate as
`kind ∈ {deterministic, inferential}`. **Use those exact tokens. Do not mint a synonym.**

### Stage 1 — COMPOSE (deterministic, full graph)
Pattern-match each of the **12 canonical `c2_motif_families`** over the whole graph. The YAML already
carries the templates:
```yaml
scheduled-ingest:  shape: 'Trigger(cron) -> Producer -> Store(raw/bronze)'
staged-transform:  shape: 'Store -> Trigger(event) -> Transformer -> Store(next layer)'
orchestrated-compute: shape: 'Trigger -> Router -> Producer(EC2/StepFn) -> Store'
```
Each **match** is one C2 motif instance: an ordered set of real node ids. Expected order of magnitude
**~100+** (Andrew), against today's 19 class nodes.
- Emit `node_type: C2MotifInstance`, `grain: instance`, `members: [node_id…]`, `family: <yaml key>`,
  `shape_matched: <template>`.
- **`recurrence` becomes DERIVED** — `count(instances of family F)` — not a hand-written property.
  *(The YAML's `first_pass_recurrence` then becomes a CHECKABLE PRIOR: composition disagreeing with it
  is a finding about one of them, which is the point of keeping both.)*

### Stage 2 — AGGREGATE (deterministic)
Connected components over motif instances sharing C0 members — the union-find §1 already specifies.
Emit `node_type: C3StructureInstance`, `grain: instance`, `member_motifs: [instance ids]`.
**This is the population F1's `structures_touched` should count**, and its size is an OUTPUT, not a
constant. **Nothing may hard-code 14.**

### Stage 3 — CLASSIFY (inferential, one cheap pass)
For each composed unit, one model call assigns a label **from the canonical vocabulary only** — the
12 C2 families / the C3 `kind` set. **Written back into kuzu as node properties**, per his ruling:
```
class_label        <- from the canonical vocabulary; NEVER free text
class_confidence
classified_by      <- model id
classified_at
rubric_version     <- the ontology YAML's schema_version
kind: inferential  <- THE PROPERTY THAT MAKES THE MODEL-DERIVED FIELD SELF-DECLARING
```
**Runner-side enforcement, in code, not in the prompt:** a returned label outside the canonical
vocabulary is **rejected and counted**, exactly as the subdivided pipeline rejects non-canon entities.
A label is a naming act; the model proposes from a closed set or it does not propose.

## 3. Contract requirements

1. **GRAIN IS AN EXPLICIT PROPERTY: `grain: class | instance`.** The defect that produced this whole
   thread is that class nodes and instance nodes share one `CloudNode` table **with no discriminator**
   — Rule 24 (ii) in the substrate. **Every node this materializer writes declares its grain**, and
   the existing 23 class nodes get `grain: class` retroactively so a query can tell them apart.
2. **THE CLASS NODES ARE NOT DELETED.** They are the vocabulary and they stay — correctly marked. The
   canonical YAML's own law is `population_law: canon-first-debt-subset`; the six debt motifs are
   *"valid AS deviation motifs"*, just not the primary population. **A `population: canon | debt`
   property makes that YAML law queryable, which today it is not.**
3. **STAGES 1-2 ARE REPRODUCIBLE; STAGE 3 IS NOT.** Same graph in → byte-identical composition out.
   The LLM pass at `temperature: 1` (mandatory for kimi-k3) is **not** reproducible, which is exactly
   why its output is fenced behind `kind: inferential` and confined to a label field. **No
   deterministic figure may ever depend on a Stage-3 value.**
4. **DENOMINATORS ON EVERY STAGE.** `composed N instances of M candidate paths scanned`;
   `aggregated K structures over N instances`; `classified P of K, R rejected as off-vocabulary`.
   A stage that produces zero says so with its denominator — an empty composition and an unrun
   composition must not look alike.
5. **WRITE PATH.** Node properties into `graph_nodes` via the existing loader (`kuzu_nessie_load.py`
   MERGE semantics). **`comp-kuzu` auto-refreshes on HEAD advance, so a schema addition lands
   estate-wide the moment it is written — additive properties only; no re-typing of existing nodes.**
6. **STAGE 3 IS RE-RUNNABLE INDEPENDENTLY.** Re-classification must not require re-composition. This
   is his *"doesn't have to be re-derived"* requirement made structural: the expensive-to-think part
   is stored, and the cheap part can be re-run when the vocabulary changes.

## 4. What this unblocks, and what it does not

**Unblocks:** F1's real denominator (Stage 2's output); grain-keyed overlap in comp-blast (over
composed instances, not classes); and the *"what is this motif"* answer being read rather than
re-derived by every consumer.

**Does NOT settle, and I am not settling it:** whether F1 reads `K of <14 kinds>` or
`K of <N composed structures>`. **Andrew's call.** I inferred this ontology's intent once today and
was wrong, at the cost of a bad ruling to a seat that was holding correctly. **The composition makes
both computable; choosing between them is a naming act.**

## 5. Open

- **The second spec file** (`motif_c2c3_materialize_ab.json`) is unread by me; the 7-node file is
  measured, the 23-node total is inferred from it plus the live count. **Read before building.**
- **Cost of Stage 3 is UNPRICED.** ~1000+ units × one cheap call. Andrew says *"very cheap"*; I have
  measured per-call reasoning overhead at 84–98% on kimi-k3 even for trivial answers, so **a
  classification pass should be batched, not one call per unit.** Price from a bounded sample before
  running the full set.

-- `3.0.0_SA_CVO`
