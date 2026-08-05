# The five orthogonal shapes, audited against the four taxonomy postulates

**Author:** `4.0.0_SA_CRO`, 2026-08-05, Andrew-direct: *"we need to go through those five shapes and
make sure they follow our schema classification ontology, the three postulate concept in claude.md."*
**Postulates:** CLAUDE.md Rule 24 (i) MECE · (ii) SAME GRAIN · (iii) INTENT COHERENCE · (iv) **STATE
COHERENCE**, added by Andrew the same session.

**Subject:** the five orthogonal shapes, now at
`docs/doctrine/INTENT_DENOMINATOR_SYNCHRONIZATION.md` §9 (originally `ARCHETYPAL_LEARNING_LOOP.md` §2,
`1.0.0_SA_CTO~Z`, 2026-07-24).

> **VERDICT: THE SCHEMA FAILS ALL FOUR POSTULATES.** It is a genuinely useful *field guide* and a
> defective *taxonomy* — which is a real distinction, not a softening: a field guide is consulted, a
> taxonomy is computed over, and this one is being computed over (residue detectors, delta routers,
> the inference gate's shape-number output).
> **This is a finding about a schema I do not own. Routed, not fixed.**

---

## The subject, as it stands

| # | SHAPE | DETERMINISTIC DETECTOR |
|---|---|---|
| 1 | **NEW AXIS** — a kind of thing the enumerator does not traverse | unwalked structural residue GREW |
| 2 | **GRAIN SHIFT** — same axis, finer granularity | member count explodes at constant head; child-nodes appear under leaves |
| 3 | **SEMANTIC REDIRECT** — same members, meaning moved | members identical, pass-rate unchanged, the field's SOURCE changed |
| 4 | **VOCABULARY POVERTY** — a truth has no slot in the type | an observed outcome has no expressible member → coerced to the nearest sayable value |
| 5 | **MERGE / SPLIT** — 1 concept → 2 | one member's edges bifurcate into disjoint clusters |

---

## (i) MECE — FAILS, both halves

**MUTUALLY EXCLUSIVE — fails on two pairs:**

- **#2 GRAIN SHIFT vs #5 MERGE/SPLIT.** A split *is* a cardinality change and a grain change at once.
  The estate's own type specimen is ambiguous under its own schema: an invariant written at TOOL grain
  while declarations grew to SUBCOMMAND grain is filed as #2 — but "one concept (tool) turns out to be
  two (tool, subcommand)" is #5's definition verbatim. **The schema cannot classify its own headline
  instance uniquely.**
- **#3 SEMANTIC REDIRECT vs #4 VOCABULARY POVERTY.** The live `auth_api_gw` case is filed as #3: the
  name asserts a security posture, the data became pure topology. But the reason nothing can flag it is
  that the type has **no slot for "topology"** — so the value is coerced into the nearest sayable one.
  That is #4's definition verbatim. **One instance, two shapes, no rule for choosing.**

**COLLECTIVELY EXHAUSTIVE — unproven, and #5 is internally split:**

- **#5 bundles two shapes behind one detector, and the detector only catches one direction.** "One
  member's edges bifurcate into disjoint clusters" detects a **SPLIT**. A **MERGE** (2 concepts → 1)
  presents as edges *converging* — a different signal that nothing in the row looks for. **A merge is
  currently undetectable and is filed under a shape whose name promises it.**
- No completeness argument is offered anywhere for "five." The set is empirical — five shapes observed
  — presented as though closed. Per Rule 24 the burden is on the schema to show exhaustiveness, and it
  does not. *(A candidate sixth, unlisted: **RETIREMENT** — an axis or member class going vestigial, so
  the denominator silently contracts. The reverse of #1 and equally invisible.)*

## (ii) SAME GRAIN — FAILS, and this is the clearest failure

Every value sits at a different grain:

| # | The grain it operates on |
|---|---|
| 1 | the **axis SET** — which dimensions exist |
| 2 | an axis's **GRANULARITY** — how finely one dimension divides |
| 3 | a field's **MEANING** — what the values denote |
| 4 | a type's **RANGE** — what values are expressible at all |
| 5 | a concept's **CARDINALITY** — how many things one member is |

**Five values, five grains, one axis.** This is the exact violation Rule 24 (ii) names — "never a
file-level value beside a cohort-level value" — reproduced at schema-metadata level. It is also *why*
MECE fails: values at different grains cannot be mutually exclusive, because they are not competing
answers to one question. **#1 and #4 can both be true of the same change without contradiction**, which
is definitional of a broken axis.

## (iii) INTENT COHERENCE — FAILS

The axis's implied intent is *"kinds of orthogonal CHANGE the enumerator cannot see."* Four of five
describe a **change event**. **#4 VOCABULARY POVERTY does not describe a change at all** — it describes
a **standing inadequacy of the type**, true on day one, with nothing having happened. Its own detector
is phrased in the present continuous: *"an observed outcome HAS no expressible member."*

> **The axis mixes EVENTS with STANDING PROPERTIES.** That is the same class as mixing content-kind
> with handling-policy: a consumer asking *"what changed?"* and a consumer asking *"what can my type
> not say?"* are served by one enum, and only one of them gets a true answer.

**#3 is a partial instance of the same problem** — "meaning moved" is an event, but the *detection*
depends on a standing property (whether provenance is tracked at all).

## (iv) STATE COHERENCE — FAILS, and this is the finding that pays for the postulate

**State axis: DETECTABILITY — can a mechanical detector reach this shape, and does one remedy move
every value together?**

| # | Detector rests on | Reachable by the residue/monotonicity machinery? |
|---|---|---|
| 1 | structural residue the enumerator already computes | **YES** |
| 2 | member counts at constant head — already held | **YES** |
| 5 | edge clustering over the existing graph — already held | **YES** (split only) |
| 3 | *the field's **SOURCE** changed* — provenance, **not in the member set** | **NO** — needs a signal the sensor does not emit |
| 4 | *an outcome with **no expressible member*** — must observe what the type cannot say | **NO** — structurally self-defeating from inside the type |

> ### THE VALUES DO NOT MOVE TOGETHER, AND THE SPLIT IS 3–2.
> **Build the residue detector — the named, planned, obvious remedy — and you get shapes 1, 2 and 5.
> Shapes 3 and 4 are not late; they are UNREACHABLE by that instrument.** #3 needs provenance the
> sensor does not emit; #4 needs the type to report a truth it has no slot for.

This is §2's own sensor/oracle law turned on the schema: **the property #3 and #4 need is not in the
sensor's emitted vocabulary, so there is no oracle to select.** The schema's own doctrine predicts its
own state incoherence, one document away.

**Why it matters operationally, which is Andrew's stated test:** `ARCHETYPAL_LEARNING_LOOP.md` is
`Status: DESIGN / NOT BUILT`, and its build plan reads as one workstream ("the residue detector, the
monotonicity test, the delta router, the inference gate"). **A plan to build that machinery silently
delivers three fifths of its own axis and will report itself complete.** Nothing in the current schema
says so — the five shapes present as peers with peer detectors. **That is a stability defect on a key
axis, named, exactly as postulate (iv) is for.**

---

## What I recommend — and explicitly do not do here

The schema is `1.0.0_SA_CTO~Z`'s and the loop is `1.0.0_SA_CTO`'s architecture. **I am not
re-authoring another seat's taxonomy on my own reading**, and a re-cut is a Route-C act by this
schema's own definition: constructing the space, unverifiable by mutant, errors latent. It gets review.

**The shape of the remedy, offered not taken** — split the one axis into two, which is what the grain
analysis forces:

- **AXIS 1 — WHAT CHANGED (events, one grain: the change-type).** New axis · grain shift · merge ·
  split · semantic redirect · retirement. MECE-able because every value answers *"what happened to the
  model?"*
- **AXIS 2 — WHY THE INSTRUMENT CANNOT SEE IT (standing properties, one grain: the blindness).**
  Not traversed (sensor gap) · traversed but monotone (oracle gap) · **inexpressible in the type
  (vocabulary gap — today's #4)** · unobservable without provenance (today's #3's real problem).

Two axes, each MECE within itself, each at one grain, each serving one intent — and **crossing them
gives the detectability answer directly**, which is what postulate (iv) was failing to find. A change
is then classified as *(what happened) × (why we are blind)*, and the second coordinate tells you
whether the residue detector reaches it.

**Routing:** `1.0.0_SA_CTO` (loop architecture + gate owner). CC `1.0.0_SA_CTO~Z` (schema author) if
that seat respawns. **Per TRIGGER_LAYER this is filed as an owned blocking item on the loop's build
plan, not as a note** — specifically: *the build plan's completeness claim is unsound until the axis is
re-cut or the 3/2 split is declared in the plan itself.*

**Residual I did not resolve:** whether "five" is exhaustive. I named one candidate sixth
(RETIREMENT) from reasoning, not from an incident. **That is a hypothesis, not a finding**, and it
should not enter the schema on my say-so.
