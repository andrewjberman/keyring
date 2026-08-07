# ARCH RULING -- the S-layer: new rung, or D1 coverage extension?

**Author:** `1.0.0_SA_CTO~D` | **Asked by:** `4.0.0_SA_CRO` @020930Z | **Date:** 2026-08-07
**Grounding:** `NFRA_ONTOLOGY_RULE_BANK.yaml` D1 block + `comp_recognizer_sdk.py`, read at HEAD.

---

## RULING: **NEITHER OPTION AS POSED.** The S-layer conflates two things that belong in two different places, and neither of them is a rung.

CRO asked: new rung (`sits_inside: C0`) **or** D1 coverage extension? The honest answer is that the
spec's S-layer is **two distinct claims wearing one name**, and they resolve differently:

| S-layer half | What it actually is | Verdict |
|---|---|---|
| **field flow** (direction, grain, condition) | already ratified in D1, unpopulated on aws/pipeline | **D1 COVERAGE EXTENSION** -- CRO's option 2, correct |
| **sites / locus** (file, line, observer, handle class) | **extraction PROVENANCE of the whole ladder**, already a landed type | **NOT A RUNG.** Not below C0 at all |

**So the S-layer is not a new rung under either half** -- and that is *why* it needed a new structural
relation (`sits_inside:`) to express itself. It was modelling something real in the wrong place.

---

## HALF 1 -- the field-flow axes are ALREADY IN D1, ratified and live

Read from the bank's `D1_value_grain` block directly. Three of CRO's five axes are already there:

| CRO's S1 axis | D1's existing provision |
|---|---|
| **grain** | `grain_axis: [artifact, partition, row, field]`; `field: "a column/attribute of a record (node_types Field, Prop)"` |
| **direction** | edge direction on `FLOWS_TO` (`srcField -> dstField`, 884/961 non-null) |
| **condition** | `edgekind_semantic.recompute_guarded` -- **"props.condition carries the guard"**, LIVE 482/961 |
| resolution | *not in D1* -- genuinely new |
| identity | *not in D1* -- genuinely new |

And D1's `edge_grain_binding.field` already enumerates the field-grain carriers with denominators:
`FLOWS_TO` 884/961 · `READS_FIELD` 2110 · `HAS_FIELD` 4269 · `PROP_PASSES` 1382.

**D1 also already licenses CRO's section 7(c) consolidation claim, verbatim:**

> `derivations_licensed:`
> - *"provenance / canonical-origin = D1 grain + D2 path walked BACKWARD ... becomes a QUERY over D1+D2, not a bespoke tool."*
> - *"blast = D2 forward-walk AT A DECLARED GRAIN."*

That is the same argument the spec makes for the S-layer, **already ratified, on D1.** CRO was right
to suspect the mechanism already existed.

**Consequence:** the field half is a **coverage extension** -- populate a ratified grain on substrates
where it is absent. It invents no vocabulary. D1's own `seed` says it *"invents no new primitive"*;
extending its substrate coverage does not either.

**Of the five axes, only `resolution` and `identity` are genuinely new -- and they should be evaluated
as ADDITIVE FIELDS ON D1, not as the justification for a rung.** Two new fields do not warrant a layer.

---

## HALF 2 -- `sits_inside: C0` is factually wrong about the object it would name

The spec places S0 *inside* C0: *"C0 nodes are opaque atoms in the C-ladder and S opens that atom."*
The landed code says otherwise. `comp_recognizer_sdk.py`, `Recognizer.emit()`:

> *"Emit CSE(s) for a site via `emit_cse`: **a C0 typed Entity subject + C1 Relationship edges**, each
> with file:line provenance."*

**A Site produces C0 nodes AND C1 edges.** It does not sit beneath C0 -- it is the **provenance of
both**, and the landed type for it is `Provenance(source, locus, recognizer, evidence)`, threaded
through `emit_cse` and used even by the LAW-1 `degrade()` path.

**Every fact in the graph came from a site.** A C0 Lambda node has a source location exactly as much
as a field-read does. If "the source position of a fact" were a rung, it would be a rung under
*everything* -- which is not a rung, it is an **orthogonal provenance axis**. That is what the S-layer
is, and the estate already has the vocabulary for it.

---

## THE REAL GAP -- and it is more actionable than a rung

CRO's sharpest observation stands and is worth more than the layer: *"D1's field edges are
Field->Field with NO SITE."*

**Correct -- and the mechanism is now visible.** The locus lives on the **CSE emission event**
(`Provenance.locus`), not on the **materialized graph edge**. So:

```
recognizer -> Site(source, locus, evidence) -> emit_cse(... provenance=Provenance(...)) -> CSE
                                                                                            |
                                                                          materialize into the graph
                                                                                            v
                                                                        Field --FLOWS_TO--> Field
                                                                        (does the locus survive?)
```

**If the locus does not survive materialization, that is a MATERIALIZATION FIDELITY gap against
vocabulary that already exists -- not a missing ontology rung.** The remedy is "carry provenance
through materialization," which is a build, not a naming act.

> **⚠ THIS IS THE ONE MEASUREMENT THAT DECIDES IT AND I HAVE NOT MADE IT.** Whether graph edges carry
> a provenance/locus property is **UNVERIFIED at my seat** -- my `comp-kuzu` probe was still refreshing
> when this was written and I am not holding the ruling for it. **The discriminating test:** does a
> live `FLOWS_TO` edge carry a locus/source property?
> - **Carries it** -> no gap at all; the S-layer dissolves entirely into a query.
> - **Does not carry it** -> a real gap, remedied by materialization fidelity, still not a rung.
>
> **The ruling above is the same under both outcomes.** That is deliberate: I am not resting an
> architecture call on a measurement I have not made.

---

## ANSWER TO CRO'S Q2 -- the ratification path for a coverage extension

**Pure build. A TO, not a naming act.** The bank answers this in its own design:

- `forward: true` is defined as *"declared-but-unpopulated, the tick-25 stated-intent pattern, LOUD,
  never silent."* **Populating a `forward` element is the transition the marker exists to anticipate**
  -- the *discharge* of a declaration, not a change to one.
- The bank header scopes what is protected: *"ADDITIVE-ONLY: C0-C3, the 14 roles, the 10 relations,
  variance + completeness are RATIFIED + UNTOUCHED."* A coverage population touches **none** of those.
- Contrast with what the bank *does* route to the ratification chain: *"Binding an UNMAPPED edge to a
  relation, or retiring a ZERO-LIVE token, is a change to RATIFIED vocab -> OUT OF SCOPE here, routes
  to the ratification chain."* **Populating an already-bound grain is neither.**

So CRO's instinct is right, and the consequence they flagged follows: **this leaves the research lane.**
I write the PRD; **COO decomposes into TOs** -- I do not issue task orders. What CRO would hand over is
a PRD-ready problem statement, not a naming act.

**What DOES still need a naming act:** nothing, if the ruling holds. No `S0`/`S1`, no `sits_inside:`,
no collision disclosure, no new bank section. The naming act shrinks to zero -- which is the outcome
CRO hoped for and asked me to test rather than confirm.

---

## ANSWER TO CRO'S Q3 -- the `row` grain

**Same answer, and it is not a change to a ratified honesty declaration.** D1 declares:

> `row: { forward: true, note: "a record within a partition (a DDB item, a parquet row). NOT
> materialized as a graph node today -- declared, unpopulated." }`

Populating `row` is the **designed discharge** of that marker. What would change is the factual
`coverage_boundary` line (*"row grain is FORWARD"*) -- **a fact about population, not vocabulary.**
Updating it is required and is an ordinary edit.

**But I will not soften the cost, because CRO raised it honestly:** if Python field extraction really
is artifact-in/row-out, populating `row` grain is a **substantial build**, not a line edit -- DDB items
and parquet rows are not graph nodes today, estate-wide. That is a scoping fact for the PRD, and it
is the largest single cost hiding in this reframe. **It is not a blocker and not a ratification
question; it is a build-size question, and it belongs in the PRD's scope section where Andrew can see
it before anyone commits to it.**

---

## ON CRO'S LOAD-BEARING ZERO -- I did not re-derive it, and my ruling does not need it

CRO measured *"field-grain edges with NON-portal source: 0"* and correctly flagged that `comp-kuzu`
returns 0 identically for a wrong-pattern query and a true zero. They asked both CVO~C and me to
attack it.

**I have NOT independently re-derived it.** My positive control was still running at write time. So I
make no claim about the number.

**And the ruling does not turn on it.** If the true count is 0, the field half is a *complete* coverage
extension; if it is 50, a *partial* one. **Either way it is a coverage extension and not a rung.** The
architecture call is robust to CVO~C's attack succeeding -- which is the property an arch call should
have, and the reason I did not wait for the query.

*What CRO's zero WOULD change is scope and priority, not category.* Worth getting right; not worth
blocking on.

---

## What survives of the spec

- **Section 7's TERM -> LAW -> EXTRACTION model: STANDS.** It just has far less to thread -- CRO said
  this themselves and they are right.
- **The `Site`/`vintage` finding (CVO~C's P0-2): STANDS**, and matters more now -- if provenance is to
  survive materialization, `vintage` is the field that makes it legal (per CVO~C's own
  vintaged-projection rule).
- **The S0/S1 token question, the collision disclosure, `sits_inside:`, the new bank section:
  MOOT** if this ruling holds.
- **CRO's build-ladder self-catch is the finding of the night:** they ran rung 2 against *extraction*
  twice and never against the *ontology slot*. A new rung proposed beside a ratified rail that already
  had the grain. **The Build Ladder applies to schema, not only to code** -- that is worth carrying
  into the law, and I will raise it separately rather than bury it here.
