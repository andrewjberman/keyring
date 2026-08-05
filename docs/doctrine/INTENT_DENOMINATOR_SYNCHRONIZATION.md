# Intent–Denominator Synchronization — the generalized schema behind every coverage failure

**Status:** foundational doctrine (binds future behaviour; design spine of NFRA_ONTOLOGY2 +
NFRA_ARCHTOOL). **Authored:** 2026-07-23, `1.0.0_SA_CTO~Z`.
**Instances:** [`docs/references/INTENT_DENOMINATOR_INSTANCES_20260723.md`](../references/INTENT_DENOMINATOR_INSTANCES_20260723.md)
(`D-1`…`D-12`). Split 2026-08-05 on Andrew-direct: governance carries principle, the record carries
what happened.

## §0 The directive, VERBATIM (Andrew, 2026-07-23)

> "the biggest error we uncovered from the analysis of the tool use was the coverage issue, which is
> emblematic of the denominator issue. I think the schema here is being able to concretely generalize
> the 'C(N)' layers, node edge motif system, and how information and activity flows up and down them,
> how change happens, the divergence between intent and configuration, and a foundational element of
> this is being able to synchronize intent with denominator. Our task here is to identify how this
> process can be generalized."

## §1 The two quantities, defined once

Every assertion the estate makes — a tool answer, a gate verdict, a freshness check, a completeness
claim, a review sign-off — operates over a set. Two versions of that set exist, and the entire failure
class is the gap between them:

- **INTENT** — the set the assertion is SUPPOSED to cover. An **obligation**, sourced from **above**:
  a governing level, a registry, a law, a contract.
- **DENOMINATOR** — the set the assertion ACTUALLY covers. A **population**, enumerated from
  **below**: the concrete instances that exist.

An assertion is **SOUND** iff `DENOMINATOR ⊇ INTENT`. The **COVERAGE GAP** is `INTENT \ DENOMINATOR`.

> **A coverage failure is not a wrong answer; it is a correct answer over an unstated denominator
> smaller than the intent.** That is why it reads green: the arithmetic is right, the scope is
> silently wrong.

## §2 The defect: a denominator that is its own configuration

The pathological case is **INTENT and DENOMINATOR drawn from the SAME artifact.** The instrument
checks a thing against a set the thing itself defines. Then `INTENT ≡ DENOMINATOR` by construction,
the gap is structurally 0, and **the instrument cannot fail even when it is wrong.**

**The fix is always one shape: SEVER intent from denominator.** Source intent from a governance level
ABOVE the artifact being checked; enumerate the denominator from the layer BELOW at run time; and
DECLARE the residual gap. *(Instances: `D-3`, `D-4`, `D-6`.)*

## §3 The C(N) ladder — the two-directional flow this law rides on

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

- **UPWARD = COMPOSITION = where the DENOMINATOR comes from.** Enumerate what exists bottom-up.
- **DOWNWARD = OBLIGATION = where INTENT comes from.** A C3 contract obligates its C2 motifs; a
  motif's shape obligates its C1 edges; a type obligates its C0 facts.

**An assertion at layer N is sound iff the population reaching it from below covers the obligation
reaching it from above.** Recursive: the same instrument applies unchanged at C0–C3 and at the D1/D2/D3
dynamic rails.

## §4 The dynamic rails give intent and denominator their GRAIN

Sets *of what?* Unanswerable without a **grain**, a **path**, and a **contract** — ONTOLOGY2's D1/D2/D3:

- **D3 (contract) SUPPLIES THE INTENT** — the cadence/completeness/canonical-source obligation.
- **D2 (path) + D1 (grain) ENUMERATE THE DENOMINATOR** — walking the flow at the right grain.
- **Freshness, provenance, staleness-vs-frozen are coverage gaps** between a D3 obligation and a
  D1/D2 population. *"Freshness is downstream of flow"* is exactly this.

## §5 How CHANGE happens — the change-propagation law

A change enters at exactly one layer/rail. **The failure mode is a change that propagates in only ONE
direction:**

- **UP but not DOWN** → the population grew, no obligation was updated → the new instance is unchecked
  (silent extra).
- **DOWN but not UP** → the obligation grew, the population was not re-enumerated → the new requirement
  is unmet and invisible (silent gap).

> **Any change re-synchronizes BOTH directions or it is drift. A change is complete only when its
> layer's denominator and its layer's intent have both been re-derived from it.**

**And the deniable form: a new GRAIN is a change to the denominator that no diff shows.** A guard's
coverage goes stale the moment the thing it guards gets more granular — nobody edits the guard, nobody
edits the law, and the gap opens anyway. **Re-derive a registration invariant against the surface's
CURRENT grain, not the grain it was written for.** *(Instance: `D-7`.)*

## §6 Intent-vs-CONFIGURATION is the special case, not a separate axis

DESIRED-vs-APPLIED is **one instance** of intent–denominator divergence where the intent happens to be
a local configuration. It is more dangerous precisely because a config is BOTH a declaration of intent
AND, if you let it, a definition of the denominator — which collapses them into the §2 tautology.

> **A configuration is a legitimate INTENT source only when it is governed from above; the moment it
> also supplies the denominator, it is the denominator-is-its-own-configuration defect wearing a
> config's clothes.** DESIRED-vs-APPLIED, completeness, freshness and coverage are not four problems —
> they are one axis measured at four sites.

## §6b YOUR PROBE IS AN INSTRUMENT TOO

> **A sample that misses a type reads EXACTLY like an absence of the property.**

A broad scan returning nothing is not evidence — a true absence and a sample that missed the relevant
subset produce **byte-identical silence**. And a **malformed** probe does not fail loudly: it returns a
clean, plausible number — a 0, an empty set, a byte-identical diff — that reads as a FINDING against a
working tool. *(Instances: `D-9` scope, `D-10` shape.)*

**This direction is the expensive one:** a false finding against a *working* instrument spends the
author's time and the tool's credibility, and **a retraction never fully catches its own claim.**

**THE RULE, and it is the existing law pointed one step back at the apparatus doing the pointing:**
run **Rule 22a's positive control on your PROBE** — as a separate invocation — before you report on the
instrument. **If your probe cannot find a known-present instance, your probe is broken, not the target.**

**THE FIRING CONDITION — because you cannot control every row:**

> **WHEN YOUR INSTRUMENT REPORTS A DEFECT IN SOMETHING YOU HAVE INDEPENDENT GROUND TRUTH ON, CHECK THE
> INSTRUMENT FIRST.**

A finding that contradicts ground truth you already hold is either a discovery that overturns what you
know — rare — or a broken instrument — common. **A finding that contradicts *any* fact you
independently hold halts the whole census until the instrument is cleared**, because a runner that lied
about the row you know cold lied about the rows you don't. **One trusted row disciplines the entire
denominator, and it costs nothing — you already hold the answer.** *(Instance: `D-11`.)*

## §6c A SOUND instrument's TRUE output can still be an unfalsifiable verdict

> **BOUNDARY:** the taxonomy — CLASS 1 (domain under-reach, `D ⊉ I`) vs CLASS 2 (predicate
> insensitivity, `P ⊭ Q`), their orthogonality, the monotonicity test, the detection asymmetry — lives
> in `infra/system/ontology/DOMAIN_AND_PREDICATE_ERROR_CLASSES.md`. **This file remains the
> authoritative LAW; that file owns the taxonomy and cites this one. If they disagree, this file wins.**

§6b covers a **broken** probe. This is the one it does not cover, and **it survives longest precisely
because nothing about it looks wrong.** A malformed probe eventually returns an *implausible* number,
and implausibility is a trigger. A sound probe returning a true-but-incomplete verdict returns a
**plausible** number, forever. There is no anomaly to notice; it is caught only by an inference nobody
is scheduled to make. *(Instance: `D-12` — a correct 100% held for ~30 ticks.)*

**THE OPERATIONAL RULE, cheap because it runs on evidence you already have:**

> **WHEN YOU ESTABLISH A STRUCTURAL PROPERTY, ASK WHAT INSTRUMENT THAT PROPERTY BLINDS.**
> *Additivity* blinds presence-checks. *Supersetness* blinds membership checks. *Idempotence* blinds
> run-count checks. *Monotonicity* blinds threshold checks. **Proving the property and trusting the
> instrument are the two halves nobody puts together.**

**The sharper self-directed form:** not *"is there evidence against my standing verdict?"* — that
invites a search of the world. **"Have I already PRODUCED evidence against my standing verdict and
failed to connect it?"** — a search of your own outputs, bounded and free. *A verdict held for thirty
ticks deserves that search precisely because nothing has gone wrong.*

## §7 The generalized PROCESS — Andrew's ask, answered

**To synchronize intent with denominator, at any layer, for any assertion:**

1. **NAME THE LAYER/RAIL** (C0–C3 structural; D1–D3 dynamic). An assertion that cannot name its layer
   is answering an unknown question.
2. **SOURCE INTENT FROM ABOVE** — a governed obligation one level up, never from the artifact checked.
3. **ENUMERATE DENOMINATOR FROM BELOW, AT RUN TIME** — real instances; never frozen, never curated,
   never the same artifact that supplied the intent.
4. **DECLARE THE GAP** — `INTENT \ DENOMINATOR`, printed, every run. **A zero gap is a claim that must
   be shown, never assumed.** An instrument that cannot compute the gap renders UNKNOWN, loudly.
5. **ON CHANGE, RE-DERIVE BOTH** — or it is drift.

**Layer-agnostic by construction** — the same five steps define a coverage declaration, a completeness
gate, a freshness check, a registration invariant, a review sign-off, and a synthesized tool's
self-test. NFRA_ARCHTOOL's stability grader is this process pointed at itself: a pattern is stable
enough to build a tool from **only when its intent source is governed (law, not habit) and its
denominator is enumerable (bounded, not open)**.

## §8 Two standing corollaries from the instance record

**THE FIX FOR A FROZEN COUNT IS NEVER A FRESHER COUNT.** A hand-maintained digit beside a growing
enumeration is a second, unsynchronized copy of the denominator. Delete the digit; the list is the
count. *(This file's own §8 heading committed it: it read "the five instances" over six, then seven.)*

**A CORRECT CITATION BOUNDS WHAT YOU VERIFIED, NEVER WHAT IS THERE.** A mechanism confirmed on one of
two layers is not a confirmed mechanism — it is a denominator that happens to contain a true sentence.
Rule 22's `file:line @ commit-ish` can be satisfied exactly and still not be the whole mechanism.
*(Instance: `D-7`, caught only because acceptance was written as BEHAVIOR rather than registry-presence.)*

---

**Related:** [`CONTROLS_OVER_CARE.md`](CONTROLS_OVER_CARE.md) · [`TRIGGER_LAYER.md`](TRIGGER_LAYER.md)
(a finding lands as a gate; this says what the gate must check) · `NFRA_ONTOLOGY2_PRD.md` ·
`NFRA_ARCHTOOL_PRD.md` · `NFRA_PSTMRT_PRD.md` (first enforcement site) ·
`docs/references/MDPF_POSTMORTEM_20260722.md` (the incident that started it).

*Split 2026-08-05 by `4.0.0_SA_CRO` (380 → this + `D-1`…`D-12`). **Nothing cut — the evidence moved
and is linked.***
