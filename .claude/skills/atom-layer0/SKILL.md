---
name: atom-layer0
description: Run the atom_layer0 method on a named concept: test whether it is an atomic base within a versioned decomposition grammar, certify bounded frontier closure, compile resolution contracts for every binding above it. Use on `/atom-layer0 <concept>`, "find the true atom of X", "is X the base layer". Findings characterize-not-fix and route to owners.
---

# /atom-layer0 — ad-hoc invocation of the atom_layer0 method

**THE METHOD LIVES IN ITS PACKAGE; THIS SKILL IS THE INVOCATION FRAME.** Never restate the method
from memory — read the canonical entrypoint and follow it:

> `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ATOM_LAYER0/skill/atom-layer0/SKILL.md`

That file (with its `references/workflow.md`, `references/decomposition-grammar.md`,
`references/resolution-contract.md`) is the executable method: S0–S5 in order, template →
validate-after-every-stage → bounded certificate. This shim exists so the method is one `/command`
away and so every ad-hoc run inherits the ESTATE frame the package cannot know:

## Step 0 — Scope the run (before opening the package)

- **Subject:** one named concept per run. If the invoker gave none, ask for it — a run without a
  pinned subject cannot pass S0.
- **Grammar discipline:** the binding decomposition-grammar version must be a target-blind commit
  predating subject selection (package invariant — do not pick a grammar after seeing the subject).
- **Authorization posture:** an ad-hoc run is a legitimate method-application/QA instrument
  (Andrew-direct 2026-08-20 skill commission). It is NOT part of the review-gated full-run sequence
  at `4.0.0_SA_CRO~C` — do not mark sequence items done from an ad-hoc run.

## Step 1 — Execute per the package entrypoint

Follow the package SKILL.md verbatim: copy `templates/atom_layer0_run.template.json` (or compile a
census row via `scripts/validate_run.py --compile-census-row`), run S0–S5 per
`references/workflow.md`, validate after every stage with `scripts/validate_run.py`.
Runtime: python >=3.10, jsonschema>=4, PyYAML>=6 (`PACKAGE_MANIFEST.json#runtime`).

## Step 2 — Land at the ONE HOME (base-CRO adopted, 2026-08-20)

```
workflows/atom_layer0/runs/<subject>/<UTC-stamp>/atom_layer0_run.json   (+ certificates)
```
**A run certificate lives there and NOWHERE ELSE** — a seat-dir copy is a two-homes mint. Then
recompile the ledger so the run is visible: `python workflows/atom_layer0/compile_manifest.py`.

## Step 3 — Route, never repair

- The strongest claim is `ATOMIC_WITHIN(grammar@version × scope)` — never metaphysical
  indivisibility; budget exhaustion / instrument failure → UNKNOWN, never a soft pass.
- Rule 24 binds every enum/array/predicate the run authors or adopts — postulate records + token
  census ride the run artifacts (`rule24/SCHEMA_ENUMERATION_RECORDS.json` is the governance shape).
- **Owner-surface findings ROUTE to their owners** (via COO/base CRO per standing routing); the run
  proposes, it never lands registry/canonical edits. Method status is PROPOSED until Andrew ratifies.

## Cross-references

- Workflow home (the durable design record + run ledger): `workflows/atom_layer0/README.md`
- Registration: `org/projects/ATOM_LAYER0.json` (REGISTERED-PROPOSED 2026-08-20)
- Sibling: `/atom-decomp` — systems/estate decomposition (evidence rectangles over deployed
  reality); use THIS skill for conceptual bases, that one for system truth.
