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
> individuated.** <<

### ⛔ CORRECTION 2026-08-06 ~2350Z — I WAS WRONG THAT "THE COMPOSITION WAS NEVER WRITTEN"

**That claim rested on the 7-node debt file alone. Reading the sibling `_ab.json` falsifies it — and
the correction makes this build SMALLER.** Measured:

| | `motif_c2c3_materialize_ab.json` |
|---|---|
| size | **1,141,941 bytes · 16 nodes · 5,088 edges** |
| `producer` | `NFRA_ONTOLOGY.AB-MAT-S1 (0.4.0_DS_ClientPlatform~B) — canonical A+B materialize` |
| `grounding.recurrence` | **"MEASURED live per detector (not echoed from spec)"** |
| `grounding.nodes_snapshot_id` | `8277340521493435453` — pinned |
| every C2 node carries | `detector: "(S3_BUCKET)-CONTAINS->(S3Key)-OWNED_BY->(S3_BUCKET)"` — **a real graph pattern** |
| `counts.c2_to_c1_edges` | **5,079**, e.g. `motif:a-store CONTAINS arn:aws:s3:::opal-data-bd {layer: C2->C1}` — **real estate node ids** |
| `c3_model` | `OVERLAPPING-DOMAIN-COVER` (CTO-ruled) — anchor-defined membership, HUB types excluded |

**THE DETECTORS ARE REAL, WERE EVALUATED LIVE AGAINST A PINNED SNAPSHOT, AND THE MEMBERSHIPS ARE REAL
NODE IDS.** My "hand-authored JSON stamped with a producer name that makes it look derived" is **FALSE
for `_ab.json`** — the file states outright that recurrence is measured and not echoed from spec.
*(It may still hold for the 7-node debt file, `tier: gate-ready` — a different artifact, not
re-derived here.)*

### The defect, restated precisely — narrower than I claimed

>> **THE COMPOSITION PRODUCES INSTANCE MEMBERSHIP BUT NOT INSTANCE IDENTITY.** One node is emitted per
> DETECTOR, and every match is attached as a `CONTAINS` edge from that class node. You can ask *"which
> S3 buckets participate in a-store"*; you **cannot** ask *"how many a-store instances exist, and
> which nodes constitute instance #7."* <<

Two derived counters prove the instance concept already exists and is merely unaddressable:
`a-store` **recurrence 232** (pattern matches) vs **n_instances 236** (distinct constituents);
`a-grant` 1553 vs 817; `b-dataflow` 956 vs 1336. **Both computed, neither individuated.**

**CONSEQUENCE: Stage 1 is not authored from scratch.** The detectors exist and run. **The change is
the OUTPUT SHAPE — emit one node per MATCH, not one per DETECTOR** — plus the grain property. §2's
Stage 1 should be read as *"re-shape the existing composition,"* not *"write it."*

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
  `shape_matched: <template>`, **`substrate_side: [...]`**.
- **`recurrence` becomes DERIVED** — `count(instances of family F)` — not a hand-written property.
  *(The YAML's `first_pass_recurrence` then becomes a CHECKABLE PRIOR: composition disagreeing with it
  is a finding about one of them, which is the point of keeping both.)*

#### `substrate_side` is DERIVED PER INSTANCE, and it is multi-valued
`SYSTEM_DEFINITIONS.yaml` v1.8 (`@dcdedf6fe`): a rollup over the substrate axis —
**BACKEND** (`layer` ∈ {aws, pipeline}) · **FRONTEND** (`layer` = portal) · **KNOWLEDGE** (`layer` = ms).

```
substrate_side(instance) = sorted(set( side_of(m.layer) for m in members ))
```
**Derived from the members, never declared, never inherited from the family.** Two instances of one
family can sit on different sides, and a family-level side would erase that.

>> **AN INSTANCE WITH MORE THAN ONE SIDE IS A SERVE-SEAM CROSSING, AND THAT IS A FINDING, NOT A
> BOOKKEEPING DETAIL.** Measured at class grain today, exactly ONE motif crosses — `AServeMotif`
> (CloudFront → ServedURL/Endpoint/DataFetch). **At instance grain the crossings become individually
> addressable**, which is what F1 is for: `[BACKEND, FRONTEND]` instances ARE the c3.i↔c3.ii bridge
> the friction battery is meant to watch. **Emit the multi-side set even when it is a singleton** —
> a one-element list and an absent field must not look alike. <<

*(`semctl` never appears here: it is not a substrate, so it contributes no side. Per SYSTEM_DEFINITIONS
the C2/C3 nodes take their side FROM THEIR MEMBERS, which is exactly the derivation above. A member
whose `layer` is absent or unknown lands in a counted `side_unresolved` residue — it is not silently
assigned.)*

### Stage 2 — AGGREGATE (deterministic)

⛔ **NOT connected-components. That approach is KNOWN-FAILED and I specified it in error.** The
generator's own commit (`fbfa06590a`) records: *"C3 emergence: connected-components OVER-MERGES to 1
supersystem — SURFACED to COO… spec 3-5 = overlapping domain cover, a partition cannot represent it."*
**A partition cannot represent overlap, and this estate's systems overlap.**

**The ruled model is `OVERLAPPING-DOMAIN-COVER`** (CTO-ruled 144621Z, MSTR doctrine-blessed):
a motif is a MEMBER of a system **iff it contains that system's ANCHOR constituent-type**;
membership is many-to-many, so a motif may belong to several systems.
**HUB types are NEVER anchors** — `HUB_TYPES = {LAMBDA, EC2_INSTANCE, actor}` (`:314`), because
compute transformers touch everything and would merge every system into one. That exclusion is the
whole reason the model works, and it is a filter on ANCHORING, never on detection.

Emit `node_type: C3StructureInstance`, `grain: instance`, `member_motifs: [instance ids]`,
**`substrate_side`** — rolled up the same way, from its member motifs' sides.
**This is the population F1's `structures_touched` counts**, and its size is an OUTPUT.
**Nothing may hard-code 14.**

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
4. **DENOMINATORS ON EVERY STAGE, AND EVERY ONE IS SIDE-SCOPED.**
   `composed N instances of M candidate paths scanned`; `aggregated K structures over N instances`;
   `classified P of K, R rejected as off-vocabulary`. A stage that produces zero says so with its
   denominator — an empty composition and an unrun composition must not look alike.
   **PLUS the coverage triple, per side, on every emission:**
   `covered X nodes of Y in detector scope, of Z on this substrate_side`.
   >> **A SINGLE ESTATE-WIDE COVERAGE FIGURE IS PROHIBITED.** Measured 2026-08-06: BACKEND
   > **2,693/3,396 = 79.3%**, FRONTEND **1,495/11,338 = 13.2%**. **Their average, 38.4%, describes
   > NEITHER population** — it is the number I reported before the split existed, and it made a
   > 96.6%-covered pipeline and a 0%-covered ms look like one moderately-covered estate. This is
   > `substrate_side`'s load-bearing clause in `SYSTEM_DEFINITIONS` and it binds here first. <<
4a. **THE THIRD FIGURE IS NOT OPTIONAL.** `Y` (nodes in detector scope) and `Z` (nodes on the side)
   are different denominators, and reporting only `X/Y` makes a complete-looking instance layer over
   a partial substrate. **Individuating today's matches yields 100% of what the detectors reach and
   ~13% of the frontend** — without `Z` that reads as done.
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

**SETTLED — Andrew-direct 2026-08-06 ~2340Z, VERBATIM:**

> *"F1 will be over the deterministic structural baseline, not the named baseline. The semantic naming
> is just metadata on various C(N) grain elements, not a denominator. Our whole focus here is C2 and
> C3.i. Do not worry about C3.ii just yet, that will come after we've handled these items listed
> here."*

**F1's denominator is `|composed C3.i structures|` — Stage 2's OUTPUT.** Not 14, not any count from
the YAML.

>> **THE PRINCIPLE, AND IT IS LARGER THAN F1: SEMANTIC NAMING IS METADATA ON A GRAIN ELEMENT. IT IS
> NEVER A DENOMINATOR.** A name is an attribute of a thing that was composed; it is not the set of
> things. **Every count in this pipeline comes from a deterministic composition; every name comes from
> Stage 3 and can never enter an arithmetic.** That is the same law as §3's "no deterministic figure
> may depend on a Stage-3 value," stated one level up — and it retires the entire 4-vs-14-vs-12-vs-19
> question, which was four ways of counting a vocabulary and calling it a population. <<

**SCOPE, same ruling: C2 and C3.i ONLY. C3.ii is DEFERRED** until the items in this spec are handled.
The vertical join / per-vertical scoping is C3.ii work and is therefore **not on this critical path**.
*(Relayed verbatim to `1.0.0_SA_CTO~B`, who is mid-build on the vertical-join walk-up on my earlier
recommendation. **Relayed, NOT converted into a hold on them** — his word binds the addressed seat and
adjudicating its breadth is not mine.)*

## 5. Open

- **The second spec file** (`motif_c2c3_materialize_ab.json`) is unread by me; the 7-node file is
  measured, the 23-node total is inferred from it plus the live count. **Read before building.**
- **Cost of Stage 3 is UNPRICED.** ~1000+ units × one cheap call. Andrew says *"very cheap"*; I have
  measured per-call reasoning overhead at 84–98% on kimi-k3 even for trivial answers, so **a
  classification pass should be batched, not one call per unit.** Price from a bounded sample before
  running the full set.

-- `3.0.0_SA_CVO`
