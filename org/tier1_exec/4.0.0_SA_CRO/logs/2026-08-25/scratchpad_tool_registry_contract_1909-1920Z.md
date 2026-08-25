# 4.0.0_SA_CRO — scratchpad tool registry contract, 2026-08-25 19:09–19:20Z

**archetype:** ARCHITECT  
**secondary_archetypes:** BUILD, VALIDATE

Andrew's exact instruction for this continuation was: *"explain the nested registries and why internal has dependencies but external does not, which kind of makes sense but let's make sure this is rigidly organized and the fields on the various items are relevant. look at how we store the comp-tools and the comp-registry check manifest check coverage check etc. see how all that stuff works and identify what in there is useful for the purposes herein"*.

## Result

The `/tooling` registry and dependency architecture in
`C:/Users/AndrewBerman/Downloads/scratchpad_tmp` is now executable policy rather than narrative.
Commit `0a2a02222af206b695ae7c63056498174e9c375f` establishes:

- one population authority per `(scope, population_grain)`;
- different-grain parent/child registry links with exact backlinks;
- registry membership separated from per-item manifests;
- candidates excluded from admitted-member, invocation, release, dependency, and coverage denominators;
- one-reference manifest ownership and first-level package parity;
- typed dependency consumers with consumer backlinks;
- package-local external dependencies until two admitted families justify shared promotion;
- hash-bound generated registry projections and a unified discovery index;
- atomic, parsed, exact-round-trip replacement of generated outputs.

Internal dependencies exist because the active compiler executes on Python and the repository uses
Git. External lenses have no dependency registry because they remain a planned family with zero
admitted executable lens packages and zero factual supply-chain dependencies. Inventing an empty or
speculative external registry would turn planning guesses into false current-state records.

## Legacy comp-tool findings retained

Useful mechanics adopted: one-home checks, inventory completeness, non-redundancy, projection
currency, source hashes, canonical invocation, effect/state declarations, explicit denominator,
controls, and positive/negative tests.

Mechanics rejected: five overlapping hand-authored populations with drifting counts, same-grain
duplication, narrative incident history in operational manifests, independent router vocabulary,
graph-specific seam fields as universal tool fields, and misleading command names such as the old
`comp-registry` wrapper that actually synchronizes project records.

## Validation

- Authored denominator: 35 files.
- Compile and generated-output check: PASS.
- Input digest: `82991bdf61e83f7e2ff1fa912684d9752d478a20ec3d135ea91169112add2745`.
- Tests: 15/15 PASS, including six registry/dependency/projection negative controls.
- Generated views: three per-registry projections plus one unified tooling index.
- New repository Markdown: zero; source bytecode: zero.
- Clean detached worktree repeated compile/check/tests with the identical digest; worktree removed.

## Compiler Tools

The legacy comp-tools were exercised during the audit through explicit interpreter/path invocation.
`comp-coverage-check` passed 99 homed tools and 12 gates; `comp-manifest-check selfcheck` passed its
three negative controls; `comp-routable-check` passed 77 registered targets with one router-index
warning. They work for Codex when invoked explicitly from PowerShell. Bare `comp-*` resolution in
PowerShell is not reliable and command resolution alone is not proof of execution.
