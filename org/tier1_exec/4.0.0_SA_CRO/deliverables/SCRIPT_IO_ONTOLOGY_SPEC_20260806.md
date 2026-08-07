# SCRIPT I/O ONTOLOGY — the S-layer (S0 sites · S1 bindings)

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Status:** DRAFT SPEC — for `3.0.0_SA_CVO~C` review. Nothing here is ratified; nothing here is built.
**Date:** 2026-08-06
**Revision:** **REV 2, 2026-08-07** — §2, §6 and §10.5 corrected against a surface REV 1 missed. See
§0.1. REV 1 (@72279a7c2) is superseded on those three sections only; §3–§5 and §7–§9 are unchanged.
**Commissioned:** Andrew-direct 2026-08-06, this session (see §0 for the verbatim scope and its
mid-course correction).
**Reviewer:** `3.0.0_SA_CVO~C` (Andrew-named).
**Subordination clause:** this document is DERIVED. Its authorities are
`infra/system/ontology/SYSTEM_DEFINITIONS.yaml` (v1.8) and
`org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml`. Where this document and either authority
disagree, **the authority wins and this file is wrong.**

---

## 0. What was asked, and the correction that shaped it

Andrew, opening the engagement (paraphrase of scope, not of ruling): build toward *project
coherence* — a structured way to attack very large projects so that agents stop mis-assessing
grains, missing detail, and duplicating each other. The existing C0–C4 / D1–D3 /
territory–substrate ontology covers resource nodes, data flow and location. One layer is missing
and is to be designed: **"script io", tracking line-level inputs and outputs for field-level
dependencies and flow**, initially for Python and React/JS.

Mid-engagement correction, VERBATIM:

> *"Yeah we probably need to enhance this somehwat with more classifications than simply input and
> output. need to figure out how to reconcile this layer with D1 and C1."*

**That correction is the spine of this spec and it is load-bearing.** A layer whose defining
distinction is input-versus-output cannot express three things that occur constantly in real
scripts — a site that reads and writes the same target, a purely internal derivation that crosses
no boundary, and a control call that carries no payload at all. Under TAXONOMY LAW (CLAUDE.md
Rule 24) an input/output split is **not MECE**: those cases are either forced into the wrong bucket
or silently dropped. §3 replaces the binary with a layer definition, and moves direction to being
*one axis among five*.

**Sequence Andrew set:** this spec → CVO~C review → then the project-coherence work, of which
`ATOM_DECOMP` is the base. **This document is step one only.** It specifies; it builds nothing.

---

## 0.1 REV 2 — what REV 1 got wrong, and how

REV 1 §11 admitted: *"the denominator of tools I did not examine is not zero and I have not bounded
it."* **I bounded it. It was not empty, and what it contained changes three sections.**

`infra/system/sdk/gensdk/recognizer_sdk/` is a **wired FrontEnd SDK with capability tiers** —
`python_ast.py` (LEXICAL_AST), `python_resolved.py` (RESOLVED_SEMANTIC, real since 2026-07-18,
whole-project import resolution), `raw_text.py`, and `tree_sitter_stub.py` (RESOLVED_SEMANTIC for
TS/JS, an **honest declared gap**, `RESOLVED_TIER_AVAILABLE = False`). Wired into `genesis_cli.py`,
`gensdk/loop/local_loop.py`, `infra/aws/globgrph/cse_emit_promote.py`, `scaffold.py`.
`python_ast.py`'s own docstring: *"Proven shape: the Opal code recognizers use exactly this."*

**Three corrections, and the third is the one that matters:**

1. **§2 undercounted.** Seven surfaces listed; the SDK is an eighth and it is *not* another private
   pass — it is the generalized abstraction the others are ad-hoc instances of.
2. **§6 was the wrong shape** — it specified *building* language adapters where an abstraction
   already exists. **A build-ladder rung was skipped.** Corrected in place.
3. **§10.5's acceptance test may be unpassable today.** Cross-language field join requires the
   TS/JS RESOLVED_SEMANTIC tier, which is a deliberate declared gap pending P6. **I wrote an
   acceptance test the estate cannot currently pass and did not know it.**

**And a denominator error against myself.** I first measured *"75 first-party `.py` performing an AST
parse."* That 75 **included vendored Lambda-layer dependencies** — numpy, pydantic, tqdm, rich,
pyarrow, pygments. **True first-party count: 56.** A number published with the wrong noun on it is
the `denominator_grain` defect the ratified vocabulary exists to name, committed inside a spec that
cites that vocabulary.

> **The method note worth keeping: §11's admitted gap is what produced the finding.** Writing *"I
> have not bounded this"* is what made it obvious the next morning that it should be bounded. An
> unmarked gap would have read as coverage and this would have surfaced during implementation
> instead — after the wrong architecture had been built.

---

## 1. The one-sentence claim

> **A C1 edge asserts that two nodes interact. Nothing in the estate records WHERE INSIDE THE NODE
> that is true.** The S-layer is the missing witness: it makes every C1 edge and every D1 grain
> claim traceable to the exact site that justifies it, and makes an *absent* edge distinguishable
> from an *unlooked-for* one.

Everything below is in service of that sentence.

---

## 2. Ground state — what already exists (BUILD LADDER rung 2, measured)

CLAUDE.md's BUILD LADDER requires establishing that the estate does not already have this before
specifying a line of new code. **It substantially does, in pieces.** The honest framing of this
work is therefore **CONSOLIDATION, not greenfield** — which lowers its risk and raises its
coordination cost, and both facts belong in front of the reviewer.

Measured this session (denominators printed; retrieval controls run):

| Surface | What it already does | Grain reached | Line numbers? |
|---|---|---|---|
| `org/modules/graph/script_io_ast.py` (271 ln) | deterministic AST I/O for **any** first-party Python file; recognizer map, UNRESOLVED never dropped, denominator emitted | artifact / partition (S3 URI) | **YES** (`"line": lineno`) |
| `extract_pipeline.py::_extract_script_io` | parses `s3_layout` imports of curated gold scripts → `ScriptIO{reads,writes,read_keys,write_keys}` | artifact / partition | no |
| `comp_dataflow.py` | value-origin trace + canonical-source assertion | value/expression | **YES** |
| `comp_constants_cli.py` | constant sites with env-backing | expression | **YES** |
| `comp_honesty.py` | residual/bucket/equality-guard defect shapes | expression | **YES** |
| `comp_legacywriter.py::removal_behaviour_for` | behaviour of a read **at a line** (guarded/dead/live) | statement | **YES** |
| `tsgraph_spike/extractor.ts` + `cluster_extract.py` | ts-morph portal semantic graph; Page→PanelCluster→Drilldown | component / field | (TS AST — positions available) |
| **`infra/system/sdk/gensdk/recognizer_sdk/`** *(REV 2 — missed in REV 1)* | **the generalized FrontEnd abstraction** the rows above are ad-hoc instances of: capability tiers, `artifact_class`, `lifecycle`; Python LEXICAL_AST **and** RESOLVED_SEMANTIC both real; TS/JS resolved = declared honest gap | per tier | via front-end |

Live graph population supporting the field grain (rule bank `D1.grain_node_denominators` +
`edge_grain_binding`): `Field` **4969**, `Prop` **359**, `HAS_FIELD` **4269**, `READS_FIELD`
**2110**, `PROP_PASSES` **1382**, `RENDERS` **2447**, `FLOWS_TO` **961** of which **884** carry a
non-null `dstField`.

**Count of `lineno` uses across `org/modules/graph/*.py`: 137.**

### 2.1 The finding that justifies the layer

Seven-plus tools independently parse the same first-party source, each with its **own** AST pass and
its **own** private notion of what counts as a read. **None of them shares a record.** No two can be
joined, none is registered in `SYSTEM_DEFINITIONS.yaml`, and none is addressable from a C-ladder or
D-rail query.

> **REV 2 CORRECTION — the sharper and less flattering version of this finding.** *"No shared
> abstraction exists"* would be FALSE: `recognizer_sdk` is one, and it is wired. What is true is
> narrower and more interesting — **an extraction abstraction exists and an ONTOLOGY does not, so
> its output is not addressable from the C-ladder or the D-rails.** The seven private passes are
> evidence that a *wired abstraction does not get adopted by tools that do not know it is there*.
> That is a discoverability finding as much as an ontology one, and it argues for registering the
> vocabulary precisely so the SDK becomes reachable from the ladder every agent already reasons in.

> **The estate has line-level knowledge and no line-level ONTOLOGY.** That is the gap — not the
> parsing. Any spec that proposes to "build script I/O extraction" has misread the ground state and
> will produce an eighth private pass.

### 2.2 What is genuinely absent

- **Field/column grain inside Python.** `script_io_ast.py` resolves *which S3 object* a script
  touches, never *which columns*. `comp-pipescript io` reports "column gaps" **only** for the
  curated DAG — measured at **262 scripts = 52.6%** of `data/*/scripts` `.py` and **7.7%** of
  first-party repo `.py` (per `script_io_ast.py`'s own header, P8 cold descent @a2be6600c). Six
  script trees resolve to no graph at all.
- **A join between the Python side and the React side.** Both compute field-ish facts; they share
  no schema, so a field cannot be followed across the serve boundary.
- **Any registered vocabulary** for a sub-node fact.

---

## 3. The layer

### 3.1 Naming — and why the numbering must mean what C's numbering means

Andrew's sketch was *"S0 line-level inputs, S1 line-level outputs."* **This spec proposes a
different split, for the reason in §0.** Direction is a property, not a stratum. Splitting the
layer by direction makes the layer itself non-MECE.

> **S0 = SITES — the intra-node FACTS.**
> **S1 = BINDINGS — the intra-node INTERACTIONS.**

This is deliberately the **same relationship C0 and C1 have** (`C0` FACTS / `C1` INTERACTIONS,
`SYSTEM_DEFINITIONS.yaml:81-90`). An agent who has learned the C-ladder already knows what S0 and
S1 are. Under Rule 24 SAME GRAIN, both S0 and S1 sit at one grain — inside one node — and the
direction/resolution/condition distinctions become axes carried **on** S1 rather than partitions
**of** S.

### 3.2 Where it sits — inside C0, not below it

The C-ladder is `C4 → C3 → C2 → C1 → C0`, and **C0 nodes are opaque atoms within it.** The S-layer
opens that atom. It is therefore **not** a sixth rung and must never be written `C-1`:

```
   C1  INTERACTIONS   ── edges BETWEEN nodes ─────────────────┐
        ▲                                                     │ aggregation
   C0  FACTS          ── the node, as an atom ────────────────┤ (never a relation)
   ┌────┴─────────────────────────────────────────────────┐   │
   │  INSIDE one C0 node:                                  │   │
   │     S1  BINDINGS   site → target, typed on 5 axes  ───┼───┘
   │          ▲                                            │
   │     S0  SITES      (file, line, col, symbol)          │
   └───────────────────────────────────────────────────────┘
```

The rule bank already legislates the connecting law and the S-layer inherits it unchanged:
**"never spans ladder levels (cross-level connection is aggregation, not relation)"**
(`relations`, rule-bank `:147`). **A set of S1 bindings AGGREGATES UP to one C1 edge.** Many sites,
one edge. That is the whole C1 reconciliation, and it required no new primitive.

### 3.3 S0 — a site

The addressable atom. One S0 record per call/expression site that participates in any binding:

| field | meaning |
|---|---|
| `node_id` | the owning C0 node (LAMBDA, PipelineScript, ReactComponent …) |
| `file` | repo-relative path |
| `line`, `end_line`, `col` | position; `end_line` because a call may span lines |
| `symbol` | enclosing function/component |
| `vintage` | the commit-ish the parse was taken at — **REQUIRED** |

> **`file:line` WITHOUT A VINTAGE IS NOT A CITATION** (CLAUDE.md Rule 22) — it resolves at every
> vintage, to different code. An S0 record without `vintage` is malformed, not merely incomplete.
> This is the single most likely field to be dropped as "obvious" and it is the one that makes the
> layer sound.

---

## 4. The five axes on an S1 binding

Andrew asked for more classifications than input/output. These are **five orthogonal axes**, not one
richer enum — Rule 24 INTENT COHERENCE forbids one axis serving two intents, and direction,
confidence, and reachability are three different intents. Collapsing them is precisely the RCG
charter-v1 defect the taxonomy law cites as its type specimen.

Each axis below states its **intent** in one line. If a proposed value does not answer that
question, it belongs on a different axis.

### Axis 1 — DIRECTION · *what does this site do to the value?*

**This is the axis that carries Andrew's correction.** Its values bind up to the ratified C1
relations, using the rule bank's own `binds_up:` adapter pattern — so the S-layer speaks existing
vocabulary rather than a parallel one.

| value | meaning | `binds_up` (C1) |
|---|---|---|
| `ingress` | value enters the node from outside | `consumes` |
| `egress` | value leaves the node to outside | `produces` |
| `derive` | value computed from other in-node values; **crosses no boundary** | `derives-from` |
| `roundtrip` | same target both read and written at one site or one loop | `consumes` + `produces` |
| `control` | invokes/triggers another node, **carries no payload** | `triggers` |
| `guard` | site gates whether another site executes | `guards` |

Two of these are the direct answer to "more than input and output":

- **`derive`** is what makes *field-level dependency* expressible at all. An input/output binary has
  no bucket for `df["c"] = df["a"] / df["b"]` — the single most common field-dependency fact in the
  estate. It is neither an input nor an output; it is the edge between two fields inside one node.
- **`roundtrip`** already exists as an unnamed special case: `ScriptIO.rolling_window_candidates`
  (`extract_pipeline.py:51-53`) strips keys appearing in both `reads` and `writes` **to avoid false
  circular-dependency edges**, and surfaces them as warnings. That is a real ontological category
  currently living as a warning list in one dataclass. Naming it promotes a workaround into a fact.

`control` and `guard` are included because a site that fires another node, or gates one, is a
line-level fact about flow that an I/O framing drops entirely.

### Axis 2 — GRAIN · *at what resolution is the value named here?*

**Reuses `D1.grain_axis` verbatim: `[artifact, partition, row, field]`. The S-layer invents no
grain vocabulary.** This is the D1 reconciliation and it is a strict reuse, not a parallel scale.

The S-layer's contribution is that **a site is where grain is actually OBSERVABLE.** A C1 edge
carries one grain; the sites underneath it may carry finer ones. Therefore:

> **S1 sites may be FINER-grained than the C1 edge they aggregate into, and the difference is
> itself the finding.**

D1's own `coverage_boundary` records the live symptom this addresses: *"77/961 FLOWS_TO carry no
dstField — coarser-than-field flow; grain read as artifact."* Today those 77 are indistinguishable
between "genuinely artifact-grain" and "field grain that the extractor lost." **With sites, that
question has an answer**; without them, D1's grain axis is asserted with no witness. Note `row`
remains `forward: true` in D1 and stays forward here — the S-layer must not silently populate a
grain D1 declares unpopulated.

### Axis 3 — RESOLUTION · *how well is the target actually known?*

The anti-fabrication axis. `script_io_ast.py` already implements this in embryo and its test battery
is built around it (`test_rebound_constant_is_NOT_folded` — "THE ANTI-FABRICATION CONTROL").
Promoting it to a named axis makes the discipline general.

| value | meaning |
|---|---|
| `literal` | fully static in-place |
| `folded` | resolved through a single-binding module constant |
| `partial` | some segments dynamic — e.g. `s3://bucket/{?}` |
| `unresolved` | call site recognized, target not statically derivable |
| `opaque` | call not in the recognizer set at all |

> **`unresolved` and `opaque` must be EMITTED, never dropped.** This axis exists because
> **SILENCE IS THE DEFECT** (CLAUDE.md Rule 22a — the comp-iam lesson): an under-reporting I/O
> instrument does not fail loudly, it returns a clean zero that reads as "no I/O here." The
> distinction between `unresolved` (we looked, we could not resolve) and absence (we never looked)
> is the entire difference between an honest layer and a fabricated one.
>
> **Corollary, and it must be a hard rule: RESOLUTION IS NEVER COLLAPSED INTO DIRECTION.** A
> consumer asking "what does this script read" must not receive `unresolved` sites silently folded
> into `ingress`, nor silently omitted. Both failures are the same failure.

### Axis 4 — CONDITION · *under what circumstances does this site execute?*

| value | meaning |
|---|---|
| `unconditional` | executes on every run of the enclosing symbol |
| `guarded` | inside a conditional; the predicate is recorded |
| `iterated` | inside a loop — implies multiplicity, relevant to grain |
| `handled` | inside `try`/`except` or an error path |
| `unreachable` | statically dead |

Precedent exists on both sides: `comp_legacywriter.removal_behaviour_for(tree, lineno, src_lines)`
already computes exactly this for a read at a line, and D1's ratified `EdgeKind` carries
`recompute_guarded` with `props.condition` (**LIVE: 482/961**). This axis is what lets a future
consumer tell a real dependency from one behind `if DRY_RUN:` — a distinction an input/output
binary cannot make, and one that matters enormously to any decommission decision.

### Axis 5 — IDENTITY · *what is the value called on each side?*

`local_symbol` → `remote_name` (column, key segment, prop name), plus a `renamed: bool`.

This mirrors ratified `EdgeKind(passthrough|rename|recompute_guarded)` on `FLOWS_TO`
(**LIVE: 337 / 142 / 482**, and the rename count cross-checks the flag). At field grain this axis is
what turns *presence* into *flow*: without it you know a component touches a field; with it you can
follow that field across a rename.

### 4.1 Axis independence is a claim, and it must be tested

Five axes are proposed as orthogonal. **That is a falsifiable claim, not a design assertion.**
CVO~C should treat it as the primary review target: if any two axes are found to co-vary such that
one is derivable from the other, they are one axis wearing two names and the schema is wrong before
it is built. §9 states the specific pair I most suspect.

---

## 5. Reconciliation — the part Andrew asked for, stated as rules

**R1 — S1 aggregates up to C1; it never competes with it.**
A C1 edge is *entailed by* ≥1 S1 binding whose `direction.binds_up` matches the relation. The
existing law is unchanged: cross-level connection is **aggregation, not relation**.

**R2 — the edge's grain is the COARSEST grain among its sites.**
Deriving an artifact-grain edge from field-grain sites is correct and lossless — the sites keep the
detail. Deriving a *field*-grain edge from artifact-grain sites would be fabrication.

**R3 — S1 is the WITNESS for a D1 claim; D1 remains the AUTHORITY on grain vocabulary.**
The S-layer may not add, rename or reorder `D1.grain_axis` values. If the S-layer finds it needs a
grain D1 does not have, that is a **ratification-chain change to D1**, routed, never a local
addition. (This is the identical boundary the rule bank draws around UNMAPPED edge types: *"Binding
an UNMAPPED edge to a relation … is a change to RATIFIED vocab → OUT OF SCOPE here, routes to the
ratification chain."*)

**R4 — an S1 binding whose C1 edge does not exist is a FINDING, in both directions.**
Sites with no edge = extraction the graph missed. Edges with no sites = an edge the graph asserts
and no line justifies. **The second direction is the more valuable one and the estate currently
cannot ask it.**

**R5 — the S-layer asserts nothing about deployment.**
Sites are parsed from source. Source is the DESIRED plane (`SYSTEM_DEFINITIONS.yaml` `plane`:
DESIRED vs APPLIED). **An S-layer claim is never evidence that a line runs in production** — that
remains a live-state read. This must be stated in the layer's own definition or it will be misread
exactly as `comp-iam`'s DESIRED-only view has been.

---

## 6. Extraction — RECOGNIZERS ON THE EXISTING FRONT-END SDK *(REV 2: rewritten)*

> **REV 1 SAID "BUILD LANGUAGE ADAPTERS." THAT WAS A SKIPPED BUILD-LADDER RUNG.**
> `infra/system/sdk/gensdk/recognizer_sdk/` already provides the `FrontEnd` abstraction, the
> capability tiers, the `artifact_class`/`lifecycle` model, and a `genesis validate` step that WARNS
> when a recognizer requires a tier no front-end can honestly reach. **S-layer extraction is a set
> of RECOGNIZERS on that SDK. It is not a new adapter layer.**

The two languages produce **the same S0/S1 schema**; only the recognizers differ. This mirrors the
rule bank's existing `relations.binds_up` adapter shape, where concrete per-plane edge types bind up
to abstract vocabulary — and the SDK already implements exactly that shape one level down.

**The tier model is load-bearing and REV 1 had no equivalent of it:**

| tier | meaning | S-layer consequence |
|---|---|---|
| `LEXICAL_AST` | single file, coarse, **no cross-file resolution** | Axis 3 can reach `literal`, `partial`, `unresolved`, `opaque` — **never `folded` across files** |
| `RESOLVED_SEMANTIC` | whole-project resolution | Axis 3 can reach `folded` |

> **THE CONSTRAINT REV 1 STATED NOWHERE, and it is a candidate axis collision:**
> `FrontEndCapability` is a property of the **EXTRACTOR**; Axis 3 `resolution` is a property of the
> **SITE**. They are not the same axis — but they are **not independent**: a site cannot be reported
> `folded` if the tier serving it cannot resolve across files. **Axis 3's achievable values are
> BOUNDED BY the front-end tier.** Whether that is a missing constraint on a sound axis, or evidence
> that Axis 3 is partly an extractor property wearing a site property's clothes, is a live review
> question (§4.1, §9) and is **deliberately not resolved here by the person who authored the axis.**

> **If the two sides are allowed to emit different schemas, the layer has failed at birth** — the
> single most valuable query it enables (follow a field across the serve boundary) is exactly the
> one that a schema split makes impossible.

### 6.1 Python — `ast` (stdlib)

Reuse, do not rebuild: `script_io_ast.py`'s recognizer architecture, its constant-folding rules
(including the rebound-constant refusal), its UNRESOLVED-never-dropped discipline, and its printed
denominator. **Net-new is the field grain**: dataframe column subscripts and assignments, the
`derive` direction, and the CONDITION axis (liftable from `comp_legacywriter`).

### 6.2 React / TypeScript — ts-morph

Reuse the P1 extractor in `org/modules/graph/tsgraph_spike/` (`extractor.ts`, `extractor_full.ts`),
which already emits a HEAD-current portal semantic graph on the CloudNode/CloudEdge schema with
portal node counts equal to the live canonical Nessie graph, and whose additive cluster pass already
achieves **119/119 page coverage with 0 silent Unknown**.

**Do not parse TypeScript from Python.** The toolchain exists, is proven, and the AST positions
needed for S0 are already available in it.

> **REV 2 — the TS/JS tier ceiling, stated so nothing downstream promises past it.** The SDK's
> TS/JS `RESOLVED_SEMANTIC` front-end is `tree_sitter_stub.py`: it **declares** the tier and yields
> **no trees**, so a recognizer requiring resolved semantics is never dispatched against it, and
> `genesis validate` **WARNS** rather than under-reporting silently. Real resolution is a **P6**
> follow-on. **The React side of the S-layer is therefore LEXICAL-tier until P6 lands**, and that
> ceiling must be carried in the layer's own `coverage_boundary` — not discovered by a consumer.
> *The stub's discipline is the same one Axis 3 encodes: make the gap visible, never silently
> under-report. It is a good pattern to inherit rather than re-derive.*

### 6.3 The asymmetry, stated because it will otherwise be discovered late

Python I/O is mostly **boundary-crossing** (S3, DDB); React "I/O" is mostly **prop and render flow**
— `PROP_PASSES` 1382 and `RENDERS` 2447 versus `WRITES` 562 / `READS` 712. So the `derive` direction
will dominate the React side and `ingress`/`egress` the Python side. **This is expected and is not a
defect**, but it means any single coverage percentage across both is the
`substrate_side` averaging error already ratified in `SYSTEM_DEFINITIONS.yaml` v1.8: BACKEND 79.3%
vs FRONTEND 13.2%, whose average (38.4%) *describes neither*. **Every S-layer denominator is
reported per `substrate_side`.**

---

## 7. Where this threads into the ratified system

Three surfaces, in dependency order. **All three are drafts for the ratification chain — this
document lands none of them.**

**(a) `infra/system/ontology/SYSTEM_DEFINITIONS.yaml`** — new terms `S0`, `S1`, `site`, `binding`,
in the file's exact form `{definition, authority, sits_at, status}`, `status: reserved_ratified`
only upon a naming act. Draft:

```yaml
  S0:
    definition: SITES -- the intra-node facts; an addressable (file, line, col, symbol) position
      inside ONE C0 node, carried with the vintage it was parsed at. Not a ladder rung: C0 nodes are
      opaque atoms in the C-ladder and S opens that atom.
    authority: org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml#script_io_layer.S0_sites
    sits_at: inside C0; below C1 by aggregation, never by relation
    status: reserved_ratified
  S1:
    definition: BINDINGS -- the intra-node interactions; a typed site->target binding carrying five
      orthogonal axes (direction, grain, resolution, condition, identity). A SET of S1 bindings
      AGGREGATES UP to one C1 edge; S1 is the WITNESS for a D1 grain claim and never its authority.
      Source-parsed, therefore DESIRED-plane only -- never evidence that a line runs.
    authority: org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml#script_io_layer.S1_bindings
    sits_at: inside C0; aggregates to C1; witnesses D1
    status: reserved_ratified
```

**(b) `org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml`** — a `script_io_layer:` section carrying the
five axes with `binds_up` adapters, per-language recognizer sets, `graph_evidence` with **printed
denominators**, `derivations_licensed`, and an honest `coverage_boundary`. It follows the
`dynamic_rails` shape (`sits_between`/`names`/`seed`/…/`coverage_boundary`) with one deliberate
difference: **`sits_inside: C0` rather than `sits_between: [Cx, Cy]`**, because it is not a rail
between rungs. Unpopulated elements carry `forward: true`, LOUD, per the section's own rule.

**(c) Consumers** — `comp-estate --definitions` serves (a) automatically. `comp-pipescript io`
becomes an S-layer *query* rather than a private parse. The `derivations_licensed` framing of D1/D2
applies: **provenance, blast radius and column-gap all become queries over S+D1+D2 rather than
bespoke tools** — which is the same consolidation argument D1 makes for itself.

---

## 8. Constraints this spec is bound by

**8.1 THE HELD-OUT FENCE — and it directly touches Andrew's sequencing.**
`NFRA_ONTOLOGY_RULE_BANK.yaml#dynamic_rails.held_out_fence` is binding on **every rail author**
(Andrew-direct 2026-07-29 ~2325Z): ***ADVI_PERFORMANCE and MDPF_GLOBAL are the held-out test set and
must not shape these rails.*** No surface of either may be used as a vocabulary example.

> ⚠ **THE CONFLICT, SURFACED RATHER THAN RESOLVED — it is Andrew's fence and only he can move it.**
> `ATOM_DECOMP`'s entire case study is `case_study/ADVI_REFACTOR/**` — i.e. **ADVI_PERFORMANCE**.
> The sequence Andrew set (this spec → CVO~C → project coherence on the atom_decomp base) therefore
> runs the S-layer straight at the held-out set at step three.
>
> Why this is not pedantry: the fence's own text says a breach **has no failure channel** — *"a
> breached held-out set looks EXACTLY like a well-fitting rail … the gap reads structurally zero and
> the fit reads excellent. THERE IS NO DOWNSTREAM SIGNAL THAT FIRES."* If the S-layer is shaped
> using ADVI, nothing will ever report that its validation was circular.
>
> **This spec is written entirely from non-held-out surfaces** — `script_io_ast.py`,
> `extract_pipeline.py`, `comp_dataflow`, `comp_legacywriter`, `tsgraph_spike`, and the live graph
> census. **I have not read the ADVI case-study contents for design input.** Three readings are
> open to Andrew: (i) the fence binds the D-rails only and S is outside it; (ii) S is a rail sibling
> and inherits it, so atom_decomp must validate on a different system; (iii) the fence is
> discharged. **I am not choosing among these** — a fence author's scope is his, per the
> no-inferred-gates and surface-don't-adjudicate rules.

**8.2 No gate is proposed.** Per Andrew-direct 2026-08-06, this spec implements no approval step,
hold, or co-sign. CVO~C review is **Andrew's own instruction**, not a gate I invented.

**8.3 Nothing is built.** Per Andrew's sequence, spec first. No code, no schema landed, no
ratification attempted, no cron, no monitor.

**8.4 Placement.** `projects/ATOM_DECOMP/**` is lane **`TIER0_MSTR`** (`.owned-paths.yaml:956-958`)
— **not a CRO write lane.** This spec is authored in the CRO home instead of overriding. If Andrew
wants it to live in `projects/`, MSTR places it. *(A ruling is not a grant — this agent's own
charter records three instances of exactly that confusion, all caught by the gate.)*

---

## 9. Open questions — the review targets for CVO~C

Ranked by how much damage a wrong answer does. **1 and 2 are structural: wrong answers there make
everything downstream wrong.**

1. **Is `derive` one direction or two?** An in-node field dependency (`c = a / b`) and an in-node
   *pass-through* (`c = a`) may be different facts. D1's ratified `EdgeKind` already splits
   `passthrough` from `recompute_guarded` — arguably `derive` should inherit that split rather than
   re-invent it, in which case Axis 1 and Axis 5 partly overlap. **This is the axis-independence
   failure I most suspect (§4.1).**
2. **Does `roundtrip` survive contact with real code, or does it decompose?** It may be an honest
   primitive, or it may be an `ingress` and an `egress` that a coarse extractor could not separate —
   in which case naming it *ratifies an extraction limit as an ontological category*. The
   `rolling_window_candidates` precedent argues it is real; that is evidence, not proof.
3. **Does `guard` belong on the DIRECTION axis at all?** It may be a CONDITION-axis property of the
   *guarded* site rather than a direction of the *guarding* one. Both readings are defensible and
   they are not equivalent.
4. **Should S0 sites be materialized as graph nodes, or computed at view time?**
   `view_time_compiled` is the ratified serving law for C3-and-below. Site counts will exceed
   current node counts by roughly an order of magnitude; materializing may violate the law's spirit
   while computing may be too slow to be reached for.
5. **What is the honest denominator for S-layer coverage?** Candidates: first-party `.py` + `.tsx`
   files / call sites / lines. `denominator_grain` is ratified vocabulary precisely because
   *"a denominator without its noun is half a number"* — and the estate has a measured instance of
   one count reported three ways, all true, none interchangeable.
6. **Is `S` the right letter?** It collides with nothing today, but `S0`/`S1` in
   `NFRA_HEATMAP` context already means something else (`.owned-paths.yaml:745` — "DS placed S0
   (heat_map.py) + O1"). A collision in an ontology's own token space is cheap to fix now and
   expensive later.

---

## 10. Acceptance — how to tell if this layer is real

Falsification tests, not a green checklist. Each names the failure it is designed to catch.

1. **Round-trip:** every C1 edge over a covered node resolves to ≥1 S1 binding, **and every
   unresolved one is enumerated.** *Catches: silent under-extraction.*
2. **Negative control:** a file with genuinely no I/O returns `sites: 0` with its denominator
   printed, **distinguishable from a parse failure.** *Catches: the clean-zero defect the whole
   `script_io_ast` posture exists to prevent.*
3. **Mutation:** rename a column in a source file; the S1 `identity` axis must change and the
   dependent edge must move. A passing assertion never mutated has never been tested.
4. **Anti-fabrication:** a rebound constant must NOT fold (the existing battery already asserts
   this — inherit it, do not re-derive it).
5. **Cross-language join:** one field followed from a Python producer through to a React consumer.
   **If this cannot be demonstrated, §6's shared-schema requirement was not actually met**, whatever
   the schemas look like on paper.
   > ⛔ **REV 2 — THIS TEST IS NOT PASSABLE AT THE RESOLVED TIER TODAY, AND REV 1 DID NOT KNOW IT.**
   > The TS/JS `RESOLVED_SEMANTIC` front-end is a deliberate declared gap (`tree_sitter_stub.py`,
   > `RESOLVED_TIER_AVAILABLE = False`); real tree-sitter/ts-morph resolution is a flagged **P6**
   > follow-on. A LEXICAL_AST-tier join may be demonstrable and is **not the same claim**.
   > **Therefore: either scope this test to the lexical tier and say so, or mark the layer's
   > cross-language promise as gated on P6 — and DO NOT let the S-layer promise, anywhere, a
   > resolved-tier cross-language trace the estate cannot currently perform.** Writing an
   > unpassable acceptance test is a cheap error; shipping a promise behind it is not.
6. **Known-negative:** a case that **did** come out differently. Ratified vocabulary requires it
   whenever a declaration claims basis `exercised` — *"exercising proves a tool RUNS and only a
   known_negative proves it DISCRIMINATES."*

---

## 11. What this document does not claim

- **Not ratified.** No naming act has occurred. `S0`/`S1` are proposed tokens.
- **Not measured against ADVI or MDPF_GLOBAL** — deliberately (§8.1).
- **Not costed.** No estimate of extraction runtime or storage is offered; §9.4 is open.
- **Not a build plan.** Owner, lane, and sequencing are for CTO/COO — **research proposes, it does
  not staff** (CRO charter §3).
- **The ground-state census in §2 is a census of what I FOUND.** *(REV 2: the residue REV 1 left
  unbounded HAS now been bounded on one axis — **56 first-party `.py` perform a Python AST parse**,
  corrected down from a first measurement of 75 that wrongly included vendored Lambda-layer deps.
  That sweep is what surfaced `recognizer_sdk`. **The bound is one-axis only:** it finds Python
  `ast` users. It does **not** cover TS/JS parsers, regex-based extractors, or anything reading
  source without the stdlib `ast` module — so §2 is still not a closed census, only a less open
  one.)* *An unmarked gap reads as coverage.*
