---
name: atom-layer0
description: Test whether a concept is an atomic conceptual base within a versioned decomposition grammar and scope, then define exact resolution contracts for prose and code that bind to it. Use for first-principles ontology work; do not use to claim metaphysical indivisibility or to repair discovered owner-surface defects.
---

# atom-layer0

Produce a structured, bounded atomicity assessment and the resolution contract for every
layer that binds to the candidate base.

## Invariants

- The strongest claim is `ATOMIC_WITHIN(decomposition_grammar@version x scope)`.
- A failed search is not a universal proof. Only declared frontier exhaustion certifies.
- Normalize candidate sub-concepts to one grain before union or counting.
- Use a target-blind grammar commit that predates subject selection; one layer declares
  one binding grammar version and rivals run only as challenges.
- Use a differently-derived splitter as a challenge control.
- Budget exhaustion, instrument failure, and an unavailable splitter route to UNKNOWN.
- Rule 24 applies to every authored or adopted enum, array, and predicate.
- Code cites canonical vocabulary; code never maintains a second member list.
- Findings are characterize-not-fix and remain PROPOSED until ratified.

## Run

1. Copy `templates/atom_layer0_run.template.json` to the run location.
2. Read [workflow.md](references/workflow.md) and complete S0-S5 in order.
3. During S1-S2 read
   [decomposition-grammar.md](references/decomposition-grammar.md).
4. During S4 read [resolution-contract.md](references/resolution-contract.md).
5. Validate after every stage:

   `python scripts/validate_run.py <run.json>`

   For the package proving run, add `--require-proving-defect`.

## Outputs

The JSON run bundle is the source of record. A rendered summary may cite it but must not
replace its populations, candidates, frontier, Rule 24 records, contracts, or residue.

Stop loudly when a required surface is unreachable. Always print `STAGE_NOT_ASSESSED`
residue, including an empty list.
