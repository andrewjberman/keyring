# A Value Must Carry Its Claim

**Status:** doctrine. Binding on design, gate conditions, and acceptance criteria.
**Authored:** 2026-07-24, `1.0.0_SA_CTO`.
**Instances:** [`docs/references/A_VALUE_MUST_CARRY_ITS_CLAIM_INSTANCES_20260724.md`](../references/A_VALUE_MUST_CARRY_ITS_CLAIM_INSTANCES_20260724.md)
(`V-1`…`V-5`). Split 2026-08-05 on Andrew-direct.

---

## The principle

> **A value must carry the claim it is making, in a field a consumer can reject on — never in a
> heuristic, a convention, or a reader's memory of how it was produced.**

Two claims travel with every served value, and both get dropped:

| The claim | The question it answers | When it is dropped |
|---|---|---|
| **PROVENANCE** — *how do we know this?* | measured / inferred / held / absent | a value and a guess share one type |
| **BASIS** — *what quantity is this?* | which firms, which axis, which source | the same field name spans two quantities |

**When either is dropped, the artifact asserts more than it knows — and nothing downstream can tell.**

---

## 1 — Model the third state; do not widen the predicate

**Binary models collapse "we do not know" into either "fine" or "broken." Both are lies.**

> **The instinct to widen a predicate until the awkward cases pass is always wrong. It retires the
> control. The awkward cases are awkward because the model is missing a state.**

**Test:** if a consumer asks *"did we measure this or infer it?"* and the artifact cannot answer, the
state is missing. Add it. *(Instances: `V-1` — UNKNOWN≠COMPLETE, HELD≠CERTIFIED, UNREADABLE≠UNCLOSED,
INFERRED-PRESENT≠MEASURED.)*

## 2 — Carry the basis

**The same field name across two bases is a defect even when both values are correct.**

Do not resolve it by forcing one name — that hides a real semantic difference behind a shared label.
**One ACCESS PATH plus an explicit `basis` sibling**: the consumer reads one field and learns from the
basis what it holds, so it can never render an enterprise total where a custody total belongs.
*(Instances: `V-2` — including a −9.97% divergence between two served AUA figures from the same nightly
run, with no instrument reporting it.)*

**And doctrine is not only a catalogue of defects — copy the shape that works:** an artifact carrying
its own fold-marker, per-model breakdown, source key, and an in-band statement of the never-sum law is
correct *precisely because it carries its own basis*, and needs no archaeology. *(`V-3`.)*

## 3 — A control that can be satisfied by breaking what it guards

> **The most dangerous control is one whose easiest passing route re-commits the defect.**

**Write the forbidden shortcut into the control. It costs one sentence.** And prefer **differential**
invariants to absolute ones: *"`sum(rows)/denominator` is IDENTICAL pre/post (90.03% → 90.03%)"* fails
if anything re-bases, and does not require a number that was never true. *(Instances: `V-4` — including
one authored and ratified by two Tier-1 seats, caught by the implementer refusing the shortcut.)*

## 4 — Only the loud ones scar

A silently-eaten tool call, an unstaged artifact nobody depended on that day, a stub that passed a
freshness check — these leave **no trace**.

> **Historical incidence is UNKNOWABLE. Never quote an observed count as a rate. `1 of 25` is a floor
> with an unknown ceiling.** *(`V-5`: six things believed, none of which had happened.)*

---

## What this obligates

1. **Emitting a value?** Emit its `basis` and its provenance beside it, in a field rejectable
   **without heuristics** — never a value that could be mistaken for the trustworthy one.
2. **Writing a gate condition?** Ask *"what is the easiest way to make this pass?"* If the answer
   re-commits the defect, the condition is wrong. **Name the forbidden route inside the criterion.**
3. **Modelling a state?** If *"we do not know"* has nowhere to go, the model is incomplete. **Add the
   state; do not widen the predicate.**
4. **Two producers of one quantity?** Decide the basis **once and carry it** — a shared resolver
   returning `(value, basis)`. **Re-derivation at each consumer *is* the defect generator.**
5. **A control inherits the scope it was written in; a change does not.** Enumerate the scopes a change
   can reach and carry a control per scope. An un-exercised scope is named **UNCOVERED**, never
   silently passed.

---

**Related:** [`CONTROLS_OVER_CARE.md`](CONTROLS_OVER_CARE.md) ·
[`INTENT_DENOMINATOR_SYNCHRONIZATION.md`](INTENT_DENOMINATOR_SYNCHRONIZATION.md) (basis and provenance
are the intent side of an assertion) · `docs/architecture/MDPF_REVAMP_GLOBAL_COUNT_CLOSEOUT.md`.

*Split 2026-08-05 by `4.0.0_SA_CRO` (150 → this + `V-1`…`V-5`). **Nothing cut — the evidence moved.***
