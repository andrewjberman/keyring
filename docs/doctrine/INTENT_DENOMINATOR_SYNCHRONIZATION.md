# DENOMINATOR — the ontology of coverage

> **FILENAME IS LEGACY, DELIBERATELY.** This file is `INTENT_DENOMINATOR_SYNCHRONIZATION.md` because
> **45 files point at that path**. The *title* is the subject; the *path* is an address. Renaming would
> manufacture ~45 dangling citations — the defect this document is about.

**Status:** foundational doctrine. The single authoritative home for denominator work: what a
denominator is, how it goes wrong, how change is classified against it, and what to do at each class.

**Centralized 2026-08-05 by `4.0.0_SA_CRO` on Andrew-direct** — *"expand that to Denominator work as a
whole … an ontological subject that really could use a centralized coherent document"*, and *"would
rather repoint and have centralized doc versus risk drift."* Absorbed: the route-classification model
(formerly `infra/system/ontology/ROUTE_LOGIC_AND_THE_SEMANTIC_BOUNDARY.md`, now a pointer) and the five
orthogonal shapes (from `ARCHETYPAL_LEARNING_LOOP.md` §2, which retains the loop design).

**Instances:** [`docs/references/INTENT_DENOMINATOR_INSTANCES_20260723.md`](../references/INTENT_DENOMINATOR_INSTANCES_20260723.md)
(`D-1`…`D-12`).

---

## §0 The directive, VERBATIM (Andrew, 2026-07-23)

> "the biggest error we uncovered from the analysis of the tool use was the coverage issue, which is
> emblematic of the denominator issue. I think the schema here is being able to concretely generalize
> the 'C(N)' layers, node edge motif system, and how information and activity flows up and down them,
> how change happens, the divergence between intent and configuration, and a foundational element of
> this is being able to synchronize intent with denominator. Our task here is to identify how this
> process can be generalized."

---

# PART I — WHAT A DENOMINATOR IS

## §1 The two quantities

Every assertion the estate makes operates over a set. Two versions of that set exist, and the entire
failure class is the gap between them:

- **INTENT (`I`)** — the set the assertion is SUPPOSED to cover. An **obligation**, sourced from
  **above**: a governing level, a registry, a law, a contract.
- **DENOMINATOR (`D`)** — the set the assertion ACTUALLY covers. A **population**, enumerated from
  **below**: the concrete instances that exist.

An assertion is **SOUND** iff `D ⊇ I`. The **COVERAGE GAP** is `I \ D`.

> **A coverage failure is not a wrong answer; it is a correct answer over an unstated denominator
> smaller than the intent.** That is why it reads green: the arithmetic is right, the scope is
> silently wrong.

## §2 Two quantifiers, two independent failures

`D ⊇ I` is only half of soundness. An assertion carries **two** quantifiers:

```
    an assertion:   ∀ x ∈ D . P(x)          what it is taken to CLAIM:   ∀ x ∈ I . Q(x)
                        │    │                                               │    │
                        │    └── the PREDICATE you evaluated                 │    └── the property
                        └─────── the DOMAIN you enumerated                   └─────── the population
```

| # | Condition | Fails as | Name |
|---|---|---|---|
| 1 | `D ⊇ I` — the domain covers the intended population | **the SENSOR** | CLASS 1, domain under-reach |
| 2 | `P ⊨ Q` — the predicate implies the property that matters | **the ORACLE** | CLASS 2, predicate insensitivity |

> **A perfect `D` does not save a weak `P`.**

**THE SENSOR BOUNDS THE ORACLE SPACE.** An oracle is a function over what the sensor **emits**, so
oracle selection is a choice *within the sensor's emitted vocabulary* — **and if the property you need
is not in that vocabulary, there is no oracle to select.**

> ### Diagnostic order, and it is NOT symmetric:
> ### ask **"does my sensor emit the token this question needs?"** BEFORE **"is my predicate sensitive?"**
> An oracle question asked over a short sensor is unanswerable — **and it will not feel unanswerable.
> It will return a clean verdict.**

**The sensor-side control:** *name a member you KNOW is in `I`. Does `S` emit it?* That is the positive
control, and it is the only check that dissents when two instruments share a sensor.
⚠ **Its failure mode is vacuity:** if you cannot name a member you already know is in `I`, the control
**does not pass — it does not run.** Report UNRUN, never clean.

*(Taxonomy detail — orthogonality, the monotonicity test, the detection asymmetry — is owned by
`infra/system/ontology/DOMAIN_AND_PREDICATE_ERROR_CLASSES.md`, which defers the LAW to this file.)*

## §3 The defect: a denominator that is its own configuration

The pathological case is **INTENT and DENOMINATOR drawn from the SAME artifact.** The instrument checks
a thing against a set the thing itself defines. Then `I ≡ D` by construction, the gap is structurally 0,
and **the instrument cannot fail even when it is wrong.**

**A coverage fraction is evidence only if its denominator is derived from OUTSIDE the instrument's own
configuration.** `9/9` is a true statement about `PUBLISH_MAP`. Where the subjects are enumerable, the
denominator is the **subject registry**, and the check is a **set-difference** against it.

**The fix is always one shape: SEVER intent from denominator.** *(Instances: `D-3`, `D-4`, `D-6`.)*

## §4 The C(N) ladder — the two-directional flow

```
            INTENT flows DOWN                         DENOMINATOR flows UP
        (obligation / what should be)             (population / what is)
   C3  SYSTEM      ──contract obligates──▶     ◀──union-find composes── C3
    │                                                                    ▲
   C2  MOTIF       ──shape obligates────▶      ◀──recurrence composes──  C2
    │                                                                    ▲
   C1  INTERACTION ──edge obligates─────▶      ◀──edges compose────────  C1
    │                                                                    ▲
   C0  FACT        ──type obligates─────▶      ◀──nodes are the atoms──  C0
```

**An assertion at layer N is sound iff the population reaching it from below covers the obligation
reaching it from above.** Recursive — the same instrument applies at C0–C3 and at the D1/D2/D3 rails.

**The dynamic rails give the sets their GRAIN.** *Sets of what?* — unanswerable without a **grain**
(D1), a **path** (D2) and a **contract** (D3). D3 supplies the intent; D1+D2 enumerate the denominator.
**Freshness, provenance and staleness-vs-frozen are coverage gaps** between a D3 obligation and a D1/D2
population.

## §5 Intent-vs-CONFIGURATION is a special case, not a separate axis

DESIRED-vs-APPLIED is **one instance** of intent–denominator divergence where the intent happens to be
a local configuration — more dangerous precisely because a config is BOTH a declaration of intent AND,
if you let it, a definition of the denominator, which collapses it into §3.

> **A configuration is a legitimate INTENT source only when it is governed from above; the moment it
> also supplies the denominator, it is the denominator-is-its-own-configuration defect wearing a
> config's clothes.** DESIRED-vs-APPLIED, completeness, freshness and coverage are not four problems —
> they are one axis measured at four sites.

---

# PART II — CLASSIFYING CHANGE AGAINST A DENOMINATOR (the route model)

*Absorbed 2026-08-05 from `ROUTE_LOGIC_AND_THE_SEMANTIC_BOUNDARY.md` (CTO~Z 2026-07-24, derived from an
Andrew working session; several corrections in it are his).*

## §6 It is a 2×2, not a three-way switch

Every change gets asked **two independent questions** — and Q1 must precede Q2, because *"did anything
move?"* is meaningless about a thing you never looked at.

- **Q1 — Did I look there?** Is it on an axis the enumerator traverses? *(the SENSOR)*
- **Q2 — Did anything move?** Does any predicate react? *(the ORACLE)*

|  | **A predicate reacts** | **No predicate reacts** |
|---|---|---|
| **Traversed** (I looked) | **ROUTE A** — seen and guarded | **ROUTE B** — seen but unguarded |
| **Not traversed** (I did not) | **C-DETECTED** — something moved, cannot localize | **C-SILENT** — total silence |

**C-DETECTED is real and usually omitted from the model.** A coarse predicate — a file hash, a byte
count, an mtime — reacts to *any* change including one you cannot localize. Maximally sensitive,
minimally informative, and **the cheapest available bridge into the inference gate.**

> ### C-SILENT IS THE KILLER. Invisible *and* nothing moved.
> The live case: a section added to the source, never traversed by the enumerator, and no predicate
> sensitive to it. **Thirty consecutive ticks of nothing.** *(`D-12`.)*

**Per change the cells are exclusive; per cycle they are not.** One head-advance produces a *mixed*
delta. **The routes classify ITEMS, not TICKS**, so honest output is a **distribution, never a verdict**:

```
head @1.3 vs pin @1.2 · 6 items -> A · 1 item -> B · 1 unwalked section -> C
```

**A tick that reports a single route has almost certainly collapsed a mixed delta into its most
convenient member.**

## §7 The one hard ordering constraint

> ### RESIDUE MUST BE COMPUTED BEFORE THE DELTA IS TRUSTED.
> Until you know **how much of the surface you examined**, *"here's what changed"* is a statement about
> your traversal, not about the source — and **a clean delta over a 40%-traversed surface reads
> identically to a clean delta over a complete one.**

## §8 The three routes

**ROUTE A — new members on a known axis · MECHANICAL · fully autonomous.** The enumerator already walks
the axis and an existing predicate already discriminates. Extend `D`, reuse `P`, re-run, close in-cycle.
**No human, ever.** *This should be the overwhelming majority of cycles; if it is not, the schema is
under-built and the inference gate is being asked to do routine work.*

**ROUTE B — traversed, but no predicate moves · SEMANTIC, recoverable · semi-autonomous.** Every
predicate in the battery is monotone under the observed change-type, so nothing can redden regardless
of how far the source drifts. **Determinism names the gap precisely** — *"presence-check is monotone
under addition, and the observed edit was additive"* — but cannot choose the replacement.

**ROUTE C — an orthogonal shape · SEMANTIC, committal · determinism HALTS.** The residue detectors fire.
The loop reports the shape, the evidence, and its own inability to proceed, as a **blocking item, never
a note**. **A loop that guesses at an axis it lacks produces exactly the confident-wrong-answer class
this exists to eliminate.**

```
change detected
├── MECHANICAL ──────────► A   (autonomous; no meaning-work whatsoever)
└── SEMANTIC
    ├── recoverable ─────► B   (verifiable; delegable behind a mutant)
    └── committal ───────► C   (unverifiable; needs review; errors latent)
```

## §9 ⚠ "C = A NEW AXIS" UNDERCOUNTS C — the most common misreading

**New-axis is the most legible C. It is NOT the definition.** The five codified orthogonal shapes:

**THE SCHEMA IS TWO-TIERED AND TWO-FIELD.** Andrew-ratified 2026-08-05, closing the two questions
`3.0.0_SA_CVO` and this desk reached **independently, by different routes** — CVO empirically from a
13-instance census, this desk structurally from a Rule 24 audit.

> ## ⚠ THE SHAPE NUMBERS ARE A CITED INTERFACE. NOTHING WAS RENUMBERED.
> `shape #2`, `#3`, `#4`, `#5` are cited from at least six files **including code**
> (`org/modules/graph/boundary_report.py:15`, `L0B_CHANGE_TYPE_VOCABULARY.md`,
> `SENSOR_CONTRACT_PLATFORM_OR_PATTERN.md`, `IMPLEMENTATION_LEVELS_AND_SEQUENCING.md`,
> `GRAPHLEARNS_IMPLEMENTATION_HANDOFF.md`, `ARCHETYPAL_LEARNING_LOOP.md`). **The re-tiering below keeps
> every original number**; `#5` gains sub-members rather than being displaced. *A first draft of this
> edit renumbered and would have silently redirected `shape #4` in live code from VOCABULARY POVERTY to
> SPLIT — caught by checking the citations, not by care.*

**TIER 1 — PRIMITIVES (MECE against each other).**

| # | SHAPE | DETERMINISTIC DETECTOR |
|---|---|---|
| 1 | **NEW AXIS** — a kind of thing the enumerator does not traverse | unwalked structural residue GREW |
| 2 | **GRAIN SHIFT** — same axis, different granularity | member count moves at constant head; child-nodes appear under leaves |
| 4 | **VOCABULARY POVERTY** — a truth has no slot in the type | an observed outcome has no expressible member → coerced to the nearest sayable value |

**TIER 2 — NAMED COMPOSITES.** Recurrent combinations of the primitives, **declared** as composites
rather than pretended to be exclusive. *Naming a composite that occurs often enough to deserve a label
is a feature; leaving its tier undeclared is what breaks MECE.*

| # | SHAPE | DETERMINISTIC DETECTOR |
|---|---|---|
| **5a** | **SPLIT** — 1 concept → 2 | one member's edges **bifurcate** into disjoint clusters |
| **5b** | **MERGE** — 2 concepts → 1 | two members' edges **converge** onto one — ⛔ **NO DETECTOR BUILT** |

> **⚠ `#5` WAS ONE ROW UNTIL 2026-08-05, AND THAT ROW HID A BLIND SPOT.** Its single detector
> (*"edges bifurcate"*) catches **SPLIT only** — so **a MERGE was undetectable under a shape named for
> it**, and the naming asserted a coverage that did not exist (`M13`). Separated because they have
> **opposite detectors**, and two directions cannot share a row without one being invisible.
> **The convergence detector is a NAMED, OWNED, UNBUILT item.** *(A bare `shape #5` citation still
> resolves — to the family; prefer `5a`/`5b` in new writing.)*

**FIELD 2 — CONCEALMENT MECHANISM (`#3` lives here now).**

`#3 SEMANTIC REDIRECT` is **not a peer error**. In every worked instance it is *how* the others stay
invisible. It moves to a second field — and **the second field is not new: it is the §6 2×2, which is
already a concealment classification** (*traversed?* × *does a predicate react?*).

| Concealment | Cell | Why nothing fires |
|---|---|---|
| **not traversed** | C-SILENT / C-DETECTED | the sensor never emitted it |
| **monotone predicate** | ROUTE B | the oracle cannot move under this change-type |
| **semantic redirect** *(`#3`)* | ROUTE B | members, counts and pass-rate all hold; the field's SOURCE moved |
| **coerced to nearest sayable** | ROUTE B | the type had no slot, so a legal-looking value was emitted |

> **CONCEALMENT IS NOT UNIQUE TO `#3` — that is why it is a FIELD, not a row.** `#4` conceals too:
> coercion to the nearest sayable value hides a truth exactly as effectively. **Every error has a
> concealment mechanism, and naming it is what tells you whether your instrument can see it** — which
> is precisely what the 3/2 detectability split measured.
> **A finding is classified as `(what changed) × (why we are blind)`, and the second coordinate is the
> detectability answer.** `#3` citations still resolve — to a field-2 member.
>
> ⚠ **PARTIALLY EXERCISED, STATED AS SUCH.** The mapping is worked for `#1` and `#3`; `#2` and `#4`
> are reasoned, not exercised. **Do not build on the `#2`/`#4` rows until someone walks them.**

> **GRAIN SHIFT (#2) IS A C, NOT A B** — and it is the one most often misfiled. *A guard's coverage goes
> stale the moment the thing it guards gets more granular:* nobody edits the guard, nobody edits the law,
> and the gap opens anyway, **because a new grain is a change to the denominator that no diff shows.**
> The estate's own instance — an invariant written at TOOL grain while declarations grew to SUBCOMMAND
> grain — is a **wrong C**, and it cost more than any single missing predicate has. *(`D-7`.)*

> **SEMANTIC REDIRECT (#3) IS THE TRAP.** Every mechanical signal reads *"nothing changed"* — same
> members, same pass rate, no residue. **If your model says "C means a new axis," you will classify this
> as B, go try to fix the instrument, and fail — because the instrument is fine. The thing it measures
> stopped meaning what its name says.**

> ### THE RULE-24 AUDIT AND WHAT IT CLOSED (2026-08-05, Andrew-direct)
> Audit: `org/tier1_exec/4.0.0_SA_CRO/deliverables/FIVE_SHAPES_TAXONOMY_AUDIT_20260805.md`. The flat
> five failed all four postulates; the two-tier / two-field structure above is the remedy, Andrew-ratified.
>
> | Postulate | Was | Now |
> |---|---|---|
> | **MECE** | `#2`+`#5` both claimed the tool-vs-subcommand instance; `#3`+`#4` both claimed `auth_api_gw`; `#5` hid an undetectable MERGE | **CLOSED** — tiers declared (1/2/4 primitive, 5a/5b composite), `#3` moved to field 2, MERGE separated with its missing detector named |
> | **SAME GRAIN** | five values, five grains | **CLOSED at tier 1** — the three primitives sit on the change-type grain; composites are declared as composites |
> | **INTENT COHERENCE** | the axis mixed change-EVENTS with standing PROPERTIES | **CLOSED** — two fields: field 1 is what changed, field 2 is why we are blind |
> | **STATE COHERENCE** | detectability split 3/2, undeclared | **DECLARED, NOT FIXED** — see below |
>
> ⛔ **STATE COHERENCE REMAINS A REAL SPLIT AND IS DELIBERATELY NOT SMOOTHED.** The residue detector
> reaches `#1`, `#2`, `#5a` and **cannot** reach `#3`, `#4` (and `#5b` has no detector at all). `#3`
> needs provenance the sensor does not emit; `#4` needs the type to report a truth it has no slot for —
> §2's sensor-bounds-oracle law turned on this schema. **A build plan for "the residue detector"
> silently delivers part of this axis and will report itself complete.**
> **CTO ruling 2026-08-05:** *declare the split, do not re-cut* — **re-cutting to make the plan look
> complete would delete the evidence of a real instrument gap.**
>
> **STANDING: classify with the shapes; never compute a coverage claim over them; never read "detector
> exists" as uniform.**

### The formulation that survives all five shapes

> # B changes the INSTRUMENT. C changes the MODEL.

- **B** — the thing being measured is fine; the *measurement* is wrong. **Fix the measurement.**
- **C** — the measurement cannot be fixed, because the *thing being measured* is mis-conceived. **Fix
  the model; the measurement follows.**

## §10 B is DISCOVERY; C is COMMITMENT — and this is why one is verifiable

In **B** there is already a right answer in the world and you are building an instrument to track it.
You are **recovering** a truth, and you can be plainly **wrong** — the world grades you.

In **C** there is no answer waiting to be recovered. *Is this one axis or two? Does it sit at C1 or
between C1 and C2?* **There is no fact of the matter until you decide.** You are not discovering a
grain — you are **legislating** one, and it becomes true by being adopted.

**The discriminator is not "does this start with a discovery?"** (both can) **but what CLOSING it
requires: B closes by finding; C closes by deciding.**

| | **ROUTE B** | **ROUTE C** |
|---|---|---|
| The act | **selection within a bounded space** | **construction of the space** |
| You are given | an axis, enumerable members, a known change-type | nothing to point at |
| The question | *"which property of this known thing do I pin?"* | *"what is the thing, at what grain, sited where, and does it matter?"* |
| Candidate set | small and listable | open |
| Consistency check | against the existing type | none available |
| Oversight | delegable behind a mechanical gate | **needs review; errors are latent** |
| Cost when wrong | the gap stays open behind a guard that looks like coverage | a mis-shaped dimension is **codified into the schema** and everything downstream inherits it |

**B has a gradient:** when the change-type is addition and a version head is sitting right there, the
pin choice is nearly forced. **B's floor approaches A; C's floor is always high.**

## §11 ⚠ B's verifiability is RELATIVE TO ITS SENSOR

In B, once you pick a predicate you can prove you picked correctly: mutate the source with the
change-type, confirm the guard reddens. **The machine grades your design act, same tick.**

> **BUT THE UNQUALIFIED CLAIM IS FALSE, AND IT WAS LOAD-BEARING.** The mutant is injected into, and
> observed through, **THE SAME SENSOR**.
>
> ### A SHORT SENSOR YIELDS A SHORT MUTANT, AND IT PASSES.
> ### The mutant cannot test its own sensor's reach — not by care, not by repetition, not at any rate.

**Exercised, not reasoned:** two independently-built censuses reconciled **member-for-member at 13** —
and both carried the identical `if not f.endswith('.py')` filter, so both were short by the same file.
The remedy in force was *pin the SET, not the COUNT*, precisely to defeat count-level agreement; **the
member-level diff returned "identical, no action."** Only a **different enumeration** dissented.

> **AGREEMENT BETWEEN TWO INSTRUMENTS THAT SHARE A SENSOR IS ONE MEASUREMENT COUNTED TWICE — and it
> reads as corroboration.** The sensor-side check is not a mutant; it is the positive control (§2).

**In C nothing grades the judgment.** You can verify the *machinery* — does the traversal walk it, does
the predicate redden — but that tests the artifact, not the conception. Whether the axis is rightly
grained, sited and named: **no mutant answers that. Only a later failure does.**

## §12 B lands on C three ways — and C returns to A exactly once

1. **B was a misdiagnosis; it was C all along.** You go to pick a pin and discover *why* nothing moved:
   the thing that changed is a new **kind** of thing your axis cannot express. **This surfaces only when
   someone tries to write the fix** — an argument for attempting the remedy early rather than filing B
   and scheduling it.
2. **B correctly diagnosed, but the remedy requires a new axis.** Diagnosis right; remedy routes through
   inference anyway.
3. **Repeated B on one axis is a C-signal by rate.** You are patching predicates while the *dimension*
   is wrong-shaped. No single event escalates; the pattern does. *(The weak, after-the-fact form of §11.)*

**And C returning to A is the entire purpose of the inference gate** — inference names the axis, emits a
traversal and a predicate, and that axis becomes ordinary deterministic surface. Which is why the
inference output contract demands **a mutant proving the new predicate can redden**: without it,
inference resolves C into a **fresh B** — a new guard monotone under the very thing it was built for.
**You would have spent the scarce resource and bought nothing.**

---

# PART III — WHAT TO DO

## §13 The generalized PROCESS — synchronize intent with denominator, at any layer

1. **NAME THE LAYER/RAIL** (C0–C3 structural; D1–D3 dynamic). An assertion that cannot name its layer
   is answering an unknown question.
2. **SOURCE INTENT FROM ABOVE** — a governed obligation one level up, never from the artifact checked.
3. **ENUMERATE DENOMINATOR FROM BELOW, AT RUN TIME** — real instances; never frozen, never curated,
   never the same artifact that supplied the intent.
4. **DECLARE THE GAP** — `I \ D`, printed, every run. **A zero gap is a claim that must be shown, never
   assumed.** An instrument that cannot compute the gap renders UNKNOWN, loudly.
5. **ON CHANGE, RE-DERIVE BOTH** — or it is drift.

## §14 The change-propagation law

A change enters at exactly one layer/rail. **The failure mode is propagation in only ONE direction:**

- **UP but not DOWN** → the population grew, no obligation was updated → the new instance is unchecked.
- **DOWN but not UP** → the obligation grew, the population was not re-enumerated → the new requirement
  is unmet and invisible.

> **Any change re-synchronizes BOTH directions or it is drift.** A change is complete only when its
> layer's denominator and its layer's intent have both been re-derived from it.

## §15 Your probe is an instrument too

> **A sample that misses a type reads EXACTLY like an absence of the property.**

A broad scan returning nothing is not evidence. A **malformed** probe does not fail loudly — it returns
a clean, plausible number that reads as a FINDING against a working tool. **This direction is the
expensive one:** a false finding against a *working* instrument spends the tool's credibility, and a
retraction never fully catches its own claim. *(`D-9`, `D-10`.)*

**Run the positive control on your PROBE, as a separate invocation, before reporting on the instrument.
If your probe cannot find a known-present instance, your probe is broken, not the target.**

**THE FIRING CONDITION — because you cannot control every row:**

> ### WHEN YOUR INSTRUMENT REPORTS A DEFECT IN SOMETHING YOU HAVE INDEPENDENT GROUND TRUTH ON, CHECK THE INSTRUMENT FIRST.

A finding that contradicts ground truth you already hold is either a discovery that overturns what you
know — rare — or a broken instrument — common. **A finding contradicting *any* fact you independently
hold halts the whole census until the instrument is cleared**, because a runner that lied about the row
you know cold lied about the rows you don't. **One trusted row disciplines the entire denominator, and
it costs nothing.** *(`D-11`: it fired on row 1 of 10, before a single false finding shipped.)*

## §16 A sound instrument's TRUE output can still be unfalsifiable

§15 covers a **broken** probe. This is the one it does not cover, and **it survives longest because
nothing about it looks wrong.** A malformed probe eventually returns an *implausible* number, and
implausibility is a trigger. A sound probe returning a true-but-incomplete verdict returns a
**plausible** number, forever.

> ### WHEN YOU ESTABLISH A STRUCTURAL PROPERTY, ASK WHAT INSTRUMENT THAT PROPERTY BLINDS.
> *Additivity* blinds presence-checks. *Supersetness* blinds membership checks. *Idempotence* blinds
> run-count checks. *Monotonicity* blinds threshold checks. **Proving the property and trusting the
> instrument are the two halves nobody puts together.**

**The self-directed form:** not *"is there evidence against my standing verdict?"* — that invites a
search of the world. **"Have I already PRODUCED evidence against my standing verdict and failed to
connect it?"** — a search of your own outputs, bounded and free. *A verdict held for thirty ticks
deserves that search precisely because nothing has gone wrong.*

## §17 Two standing corollaries

**THE FIX FOR A FROZEN COUNT IS NEVER A FRESHER COUNT.** A hand-maintained digit beside a growing
enumeration is a second, unsynchronized copy of the denominator. Delete the digit; the list is the
count. *(This file's own former §8 heading read "the five instances" over six, then seven.)*

**A CORRECT CITATION BOUNDS WHAT YOU VERIFIED, NEVER WHAT IS THERE.** A mechanism confirmed on one of
two layers is not a confirmed mechanism — it is a denominator that happens to contain a true sentence.
Rule 22's `file:line @ commit-ish` can be satisfied exactly and still not be the whole mechanism. *(`D-7`.)*

## §18 What the machinery is FOR

| Instrument | Asks | Locates |
|---|---|---|
| **Residue** | *"is there something here I cannot mechanically account for?"* | the edge of what I traverse |
| **Monotonicity** | *"can my mechanics react to what I can see?"* | the edge of what I can detect |

> **DETERMINISM CAN COMPUTE THE RESIDUE. IT CANNOT INTERPRET IT.** It can always tell you **that** it is
> blind; it can never tell you **what** the blindness is about. **The deterministic machinery exists to
> find its own boundary and stop there loudly, rather than guessing past it.**

---

## Cross-references (cite, do not copy)

| The thing | Its home |
|---|---|
| The instances behind this file | [`../references/INTENT_DENOMINATOR_INSTANCES_20260723.md`](../references/INTENT_DENOMINATOR_INSTANCES_20260723.md) |
| Class 1 / Class 2 taxonomy detail | `infra/system/ontology/DOMAIN_AND_PREDICATE_ERROR_CLASSES.md` |
| The learning-loop design these routes sit inside | `infra/system/ontology/ARCHETYPAL_LEARNING_LOOP.md` |
| How you fail to see the thing | [`CONTROLS_OVER_CARE.md`](CONTROLS_OVER_CARE.md) |
| Where an assertion sits (14 shapes) | [`MECHANISM_LAWS.md`](MECHANISM_LAWS.md) |
| A finding lands as a gate, never a note | [`TRIGGER_LAYER.md`](TRIGGER_LAYER.md) |
| A value must carry its basis | [`A_VALUE_MUST_CARRY_ITS_CLAIM.md`](A_VALUE_MUST_CARRY_ITS_CLAIM.md) |

**This file is the authoritative LAW for denominator work. If any of the above disagrees with it, this
file wins and the other is the drift.**


---

## Grounded evidence in agent memory

> Citations of the form `memory/<slug>` root at the **agent memory DIRECTORY**
> (`~/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace/memory/`), **now under version
> control** (genesis `6843c2f`, 2026-08-05). Those records are the *grounded incidents* — typically
> 40–60 lines each with measured numbers; the law here is their compression. **Doctrine holds the
> law; memory holds the evidence.** Wired 2026-08-05 on Andrew-direct; the two corpora had **zero**
> links between them before that.

- `memory/feedback_sensor_bounds_the_oracle_space_mutant_cannot_test_its_own_sensor` — §2 and §11, the grounded record.
- `memory/feedback_state_the_denominator_or_the_count_is_meaningless` — §13 step 4.
- `memory/feedback_a_predicate_is_not_a_roster` — §3: a tool's universe must be a re-derived predicate, never a hand-drawn allowlist.
- `memory/feedback_wrong_predicate_yields_a_well_formed_answer` — §15, the malformed-probe half.
- `memory/feedback_independent_derivations_not_shared_predicates_and_authored_inputs` — §11.
- `memory/feedback_denominator_framing_wall_vs_ac` — the framing record.
