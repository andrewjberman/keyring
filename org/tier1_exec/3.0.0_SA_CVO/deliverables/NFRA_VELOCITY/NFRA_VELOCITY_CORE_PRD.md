# NFRA_VELOCITY_CORE — PRD: the type system, the loop, and the tools (~Z site fabric)

**Program:** NFRA_VELOCITY (see `NFRA_VELOCITY_PROGRAM.md` — thesis, seam, metrics, constraints live
there and are cited, not copied). **Author:** `3.0.0_SA_CVO`, Andrew-direct commission + plan-review
approval 2026-07-29. **Canonical home:** `docs/architecture/NFRA_VELOCITY_CORE_PRD.md` (landed by
base CTO from this staged copy).
**Owner:** `1.0.0_SA_CTO~Z` (design + gate) · **Build:** `0.8.0_AE` base + ~A..~E lanes, `~C` on
rule-bank content · **Verify:** `3.0.0_SA_CVO~Z` · **Inter-fabric comms:** `0.0.0_AB_MSTR~Z`.
**Constitution:** `docs/doctrine/INTENT_DENOMINATOR_SYNCHRONIZATION.md`.
**Substrate (ratified, untouched):** `org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml` (C0–C3, 14
roles, 10 relations, variance + completeness) · `infra/system/ontology/` (ARCHETYPAL_LEARNING_LOOP,
ROUTE_LOGIC_AND_THE_SEMANTIC_BOUNDARY, DOMAIN_AND_PREDICATE_ERROR_CLASSES,
IMPLEMENTATION_LEVELS_AND_SEQUENCING) · `infra/system/sdk/` (GENESIS).

## §0 Scope in one sentence

Build the vocabulary in which the estate's dominant failure class becomes machine-statable, the loop
that patrols it autonomously, and the tool layer derived from graded patterns — so that CORE hands
ESTATE a type system, and ESTATE hands CORE a live world to type.

**Absorbs (all closed as superseded, open work re-homed here):** NFRA_ONTOLOGY2 (P1–P4 → WS-C1/C2),
NFRA_TOOLARCH (→ WS-C3/C4), NFRA_TOOLSEM (→ WS-C6), COMPLEARNS/GRAPHLEARNS L0–L3 (→ WS-C5),
NFRA_LIVELEARN (acceptance bar → WS-C5), NFRA_TOOLUNIFY remainder (→ WS-C7), MSBEFF R1/R3/R5/R7
(→ WS-C7/C4/C6).

**Supersession note (explicit, so no future reader re-derives it):** ONTOLOGY2's charter clause
*"not a new graph — these rails must be derivable from the existing graph + declared contracts"* is
superseded by Andrew's plan-review approval: **declaring the contracts IS the work** (ESTATE WS-E1);
the rails and the contract registry co-evolve through the specimen round-trip.

---

## WS-C1 — The rails: D1 / D2 / D3 + LIFECYCLE (the constitutional build)

Author D1 (value/grain), D2 (path/flow + cadence), D3 (contract/obligation) as **additive**
rule-bank sections — the ratified C0–C3 vocabulary, 14 roles, 10 relations, variance + completeness
axes untouched — **plus the lifecycle/supersession vocabulary inside D3**: every contracted
resource/process carries `(intent_source, obligation, successor?, expiry_condition?)`.

Each rail ships with: its vocabulary · the graph evidence that populates it · its honest coverage
boundary · the derivations it licenses. The licensed derivations are definitional, never primitives:

| Derived property | Defined as |
|---|---|
| freshness | D2 path + D3 cadence + upstream vintages + trading calendar (kills config-is-its-own-denominator by construction) |
| provenance / canonical-origin | D1 grain + D2 path walked backward (this IS comp-dataflow / MSBEFF R2 — a query over D2, not a bespoke tool) |
| staleness-vs-frozen | vintage advancing along the path vs the value not moving |
| blast | D2 forward walk at a declared grain |
| **debt** (new) | **D3 lifecycle walk: `expired_obligation ∪ superseded_with_live_successor`** |

Then the DEBTLOOPS shapes are typed violations by definition: LEGACY-WRITER (writer with expired
obligation or live successor, still writing) · CLOBBER (two writers at one `(key, grain)`, no
adjudicating contract) · TRIGGER-MISSEQUENCE (an edge firing against the D2 topological+temporal
order) · ZOMBIE/ORPHAN (a C-SILENT resident: no enumerator traverses it, no predicate reacts).

**VOCABULARY REQUIREMENT (~C item 3, evidence-grounded 2026-07-29): the lifecycle enum MUST carry
an explicit `TRANSIENT` value** — written → consumed → deleted; **absent-at-rest is its healthy
state.** A live trigger marker is indistinguishable from a dead key under ANY existence check
(`gold/trigger-pending.json` et al. landed in a kill list's top tier on "no object found" — and a
transient key independently reads absent AND dormant AND reader-less, so WS-E3's ≥2-CONFIRMED bar
does not save it: two confirmed signals, both wrong, on a live pipeline trigger). Transience cannot
be derived; it must be declared. The comp-legacywriter TRANSIENT-MARKER guard (@d51f6b38a0) is the
name-pattern stopgap this type replaces — a pattern-match on key names is not a type system.

*Acceptance:* rule-bank `meta.version` head advances carrying the D-rail sections **including
lifecycle `TRANSIENT`**; every derived property defined as a derivation; ratification chain for
vocabulary; CVO~Z verify.

## WS-C2 — Expressiveness validation against the three corpora (before the types freeze)

Every item in (a) MSBEFF's 718 findings, (b) the 210-incident INCIDENT_TAXONOMY, (c) the DEBTLOOPS
memo shapes + the nine same-day false-negative specimens must be **expressible** in
`(rail, grain, plane, scope)` + lifecycle — typed, or an honest UNKNOWN naming the missing
vocabulary. This is TOOLSEM §2d's law pointed at ourselves: *an outcome the type system cannot hold
is coerced to the nearest lie* — shape the type system against the full failure record while it is
cheap to change.

**Also discharges MSTR's V1** (the taxonomy handoff's load-bearing verification): re-bucketing the
210 incidents onto these independently derived axes IS the re-bucket control; publish whether the
55% four-mechanism concentration survives the re-bucketing.

*Acceptance:* a typed corpus table with a stated residual (unexpressible items → WS-C1 round 2 or
declared out-of-scope with reason); the concentration-survival verdict published.

## WS-C3 — Archetype census + pattern inventory (debt patterns first-class)

TOOLARCH Q1/Q2 on the rails: per-plane motif frequency with printed denominators, starting from
CVO~Z tick-29's honest uncovered-edge gap (11 live edge types on no axis; 9 declared-but-zero-live);
then the pattern inventory — pattern → archetype → instantiating tools → gaps — seeded from the ~96
registered tools + 718 findings + 187 rail-override intents + **the debt shapes as named
first-class patterns** (LEGACY-WRITER, CLOBBER, ZOMBIE-PROCESS, TRIGGER-MISSEQUENCE,
ORPHAN-ARTIFACT). Expect the inventory far smaller than the tool count — the compression ratio IS a
finding.

*Acceptance:* census + inventory + compression ratio + the ranked tool-gap list (the generative
"what tool is missing" answer the estate cannot currently produce).

## WS-C4 — Stability grader + tool synthesis pipeline

TOOLARCH §3/P3/P4. Grade every pattern before choosing its extraction mechanism — brittleness is a
property of the TARGET, not of regex:

| Axis | Question |
|---|---|
| GOVERNANCE | law, convention, or accident? (declared in a standard/gate vs merely observed) |
| CHURN | how often has the shape changed? (git history of declaration + instances) |
| POPULATION | enumerable? bounded by a registry? |
| VIOLATION | do live exceptions exist today? |
| BLAST | what breaks silently if the shape drifts? |

STABLE-BY-LAW (governed + low churn + bounded + zero live violations) → a pattern extractor is
legitimate **and must cite the law it depends on** (a law change fails the tool loudly). Anything
less → structural extraction (AST/graph/live-primitive), or the tool is not built. **A pattern
extractor whose governing law is not cited is unregistrable.**

Synthesis emits, per graded pattern: the tool · its R1/R3 coverage + vintage declarations · its
registration entry · its mutants. **No exception carved for generated tools** — the same
registration invariant and mutant requirements as hand-built.

*Acceptance:* grader validated against known-stable (the S3 key grammar) and known-unstable (vendor
filenames) — both must grade correctly or the grader is wrong; ≥1 tool synthesized end-to-end
through registration + mutants.

## WS-C5 — The learning loop: L2 aggregate + L3 inference gate (the engine)

Per `IMPLEMENTATION_LEVELS_AND_SEQUENCING.md` (L0a DONE · L0b v1.0 LIVE · L1a 4-of-N · L1b
delivered — the ≥3-sensors-mixed-shapes prerequisite for L2 is MET):

1. **Build L2 — the fleet aggregate:** collect boundary reports, rank, declare applicability
   denominators; *"where is our model short?"* becomes one answerable question. Its five banked
   design inputs are in the levels doc.
2. **Formalize L3 — the inference gate as a BLOCKING site** with the output contract enforced: every
   inference event terminates in (a traversal that walks the new axis + a predicate that MOVES under
   the change-type + a version pin + a mutant proving the predicate can redden) — or the loop dies
   at that axis (the persistence rule). Route C escalates as a blocking item, never a note; the loop
   never guesses past its own boundary.
3. **Generalize version-head pinning** beyond the rule bank: any governed source (a registry, the
   estate-contract set, the tool index) can be a pinned head — which is what lets ESTATE's surfaces
   join the loop.

*Acceptance:* L2 renders the fleet aggregate with denominators; one full C-route cycle exercised
end-to-end (residue → inference → new determinism → head advance → autonomous re-cover);
LIVELEARN's bar folded (fresh-when-consumed; the loop provably closes over ≥2 cycles).

## WS-C6 — Typed routing: the comp-which successor

TOOLSEM P1–P3 on the now-typed surfaces:

1. **Query→denominator parser**, validated on the corpora with declared misclassification; an
   UNKNOWN-layer query is loud, never force-typed.
2. **Type-matched router**: the tool whose declared coverage space contains the query's required
   denominator wins — never a similarity argmax. **Honest empty** when nothing covers; a near-tie
   renders as stated no-confident-route.
3. **Law-sufficiency as a first-class routing input**: for a query class the law governs (the
   Rule-22a/comp-iam case), the routed answer surfaces the mandated call or says what it is not — a
   tool right about a narrower question than the one asked is the hardest failure to see.
4. **`machine_surface:` declarations consumed before parsing** (§2e); routing binds to *verified*
   coverage declarations, never assumed capability (§2b corollary).
5. **Gap-as-demand:** a query no tool covers feeds WS-C3's inventory as a measured demand signal
   (successor to hand-reading the rail-override log).

*Acceptance:* held-out corpus routing beats keyword-argmax; an uncovered query routes to the
sanctioned fallback WITH the gap stated; zero silent argmax on the replacement path; the memorized
head protected (no router hop where memory already routes correctly).

## WS-C7 — The recall standard (boundary reports become law)

The DEBTLOOPS brief's structural observation is the crux: *"Every tool reports what it FOUND; none
reports what it COULD NOT HAVE FOUND."* Generalize L0a's boundary report into the registration
invariant: **every tool/detector declares its address space, its traversal residue, and its
method's failure direction** (mention under-reports · traversal exact · declared over-reports) —
the recall denominator as a required output. Fold TOOLUNIFY's pinned remainder: the per-row
verification-provenance register and the **negative-declaration axis** (what a tool cannot see
WITHIN its declared surface).

**Framing (~C item 1):** boundary reports ARE measurement-time controls — the estate's empty
quadrant (commit-time gating is dense and works; measurement-time gating is near-zero, and every
control that failed on 2026-07-29 was measurement-time). This workstream aims at the gap, not the
strength.

**Two design inputs from the registration chain's own measured cost (~C scope note):**
(a) **a pre-flight "everything registration will require" check** — the chain is already six gates
deep and each reveals itself only after the previous passes (five serial discoveries ≈ 40 min on
one tool); serial discovery COMPOUNDS for synthesized tools, which is WS-C4's whole output, so the
pre-flight is a WS-C4 dependency, not a nicety. (b) **shell-reachability joins the chain** — the
current gates prove the ROUTER can name a tool, never that a shell can RUN it (comp-legacywriter
landed unreachable; only exercising the forwarder caught it — the A.3 exercise-don't-resolve lesson
as a registration gate).

**Named limit (feeds WS-C8/C9):** a boundary report declares what the TOOL cannot see; it does NOT
declare whether a CONTROL shared the target's transport path — a distinct property with no home in
this contract (see the M15 candidate in WS-C8).

*Acceptance:* the registration invariant extended (a tool cannot register without the declaration —
comp-manifest-check enforced, announce-then-enforce ramp); N of M existing tools migrated with the
count printed (the count is the gate's, never prose's); the nine-specimen fixture suite green —
each specimen re-derives as a Class 1 or Class 2 failure the contract surfaces; the pre-flight
check exists and the registration chain includes an exercised shell-reachability gate.

## WS-C8 — The doctrine collapse (executing the PREVENTION ruling)

Andrew ruled the fenced question: the corpus is for **PREVENTION**. Author (here at ~Z, which owns
the taxonomy): `docs/doctrine/MECHANISM_LAWS.md` — the 14 mechanism-laws, each as {law ≤2 lines ·
the exposing question · the gate-or-test that absorbs it · instance rows}; the 210-row instance
table as the evidence appendix; INTENT_DENOMINATOR_SYNCHRONIZATION promoted to corpus head;
CONTROLS_OVER_CARE's §III family collapsed into the M-classes. **Nothing deleted** — instances
become rows; dated material moves to `docs/references/`; nothing Andrew called good is cut without
his word.

**Landing is main-CTO-gated** (law surfaces: the doctrine files, CLAUDE.md Rule-22 re-point,
doctrine/README fix) — a designed seam crossing, protocol 3.

**First candidate M-law beyond the taxonomy's 14 (~C item 2, specimen-grounded 2026-07-29 — the
CRLF incident, where a MECHANISM control and a PER-BUCKET control both passed while the result was
100% wrong, 81/81 false absence):**

> **M15 (candidate) — DIVERGENT-TRANSPORT CONTROL: a control that does not travel the same
> argument/transport path as the target validates the AUTHOR, not the instrument.**
> Exposing question: *did my control's input arrive by the same path as the target's?*
> Counter-instrument: the argv-echo oracle (echo the argument back through the same transport —
> already banked in CLAUDE.md's MSYS section, generalized past MSYS by this law).

Adjacent to but distinct from "a hand-chosen control measures the author": the control can be
correctly GENERATED from live data and still enter by a different path (typed in a shell vs read
from a `\r\n` file). Enters the schema through the WS-C9 gate under the full output contract.

*Acceptance:* doctrine byte-count falls; every M-law carries a named gate/test or an explicit "no
gate possible + why"; the collapse's own diff shows zero lost instances; the M15 candidate
adjudicated (admitted with detector + mutant, or rejected with the reason on record).

## WS-C9 — The living error-classification schema (Andrew-direct at plan review)

> "when errors inevitably still come up, there needs to be a classification schema for errors, so we
> can continue to drive the evolution of the tool based on error archetype weight and dynamics as
> the loop/fabric proceed indefinitely. … it is essential to keep the loop alive and the velocity
> accelerating."

Errors still occur after everything above lands — and each must land as a **classified instance in
a standing schema**, never a fresh discovery (the corpus's instance-#29-reads-as-new defect,
closed). Build the classification vocabulary as a governed, **versioned head**: seeded from
AXES.md's 9 axes + the 14 M-mechanisms, re-expressed in rail vocabulary per WS-C2's mapping;
**open-set with unknowns reported, never dropped** — a closed error schema would be the
frozen-enumeration defect applied to the error schema itself. A genuinely new mechanism class is a
**Route-C event**: it enters through the WS-C5 inference gate under the full output contract (the
class gets a detector, a predicate that moves, a pin, a mutant), and the schema head advances. The
ESTATE half (intake at occurrence + the archetype weight/dynamics report) is WS-E7.

*Acceptance:* the schema is a versioned artifact with a head; classifying a new incident is a
≤5-minute act with a defined intake form; one new-class event exercised through the gate
end-to-end; the schema's own coverage boundary printed.

**FLAGGED PENDING ANDREW (~C item 7):** the full schema build stays P5 per Andrew's placement —
but the archetype-weight ranking is what steers WS-C3/C4's queue, and installed at P5 it ranks
nothing (a steering signal installed after the voyage is a log, not a rudder). Proposal: a
**minimal hand-classified intake form at P1** (M-code + one line, no automation) so the queue is
weight-ranked from the start; the schema build itself stays P5. Requires Andrew's word because he
placed C9/E7 "at the very end."

---

## Phases

**P1** = C1 + C2 (the vocabulary, validated against the full failure record) →
**P2** = C3 + C7 (census + the recall standard) →
**P3** = C5 (the loop closes) →
**P4** = C4 + C6 (synthesis + routing) →
**P5** = C9 (the living schema — last, on top of everything, so the loop never closes dead).
C8 runs parallel from P1 (its content already exists).

## Governance

~Z designs + gates; 0.8.0_AE builds (~C on rule-bank content); CVO~Z verifies once across the
family; ratified-vocabulary changes route to the ratification chain; **comp-tool STANDARD changes
route to main CTO before landing** (standing carve); law-surface landings via main CTO (seam
protocol 3). Cross-fabric coordination per the program doc §4 — MSTR~Z ↔ MSTR(base), COORD-ONLY,
each relaying to its own CTO. Not an LLM-semantics project (deterministic structure first; any LLM
label orthogonal and one-way). Program-level constraints (moratorium, LD-0175, TRIGGER_LAYER, firm
separation, gate ramps) bind per program doc §6.
