# C2 S0 ground read

Source of record: `docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md` section 2.2.
This package cites that shared object and proposes an implementation; it does not become a
second source of record.

## Seven reused registry terms

The exact seven are named by `RESPONSE_II_MUTATION_BUNDLE_AND_ADOPTIONS_20260820.md`
section 1.3. The schema reuses them by term:

| Ratified term | Certificate field | Registry home |
|---|---|---|
| Failure_Direction | `failure_directions` | `SYSTEM_DEFINITIONS.yaml#Failure_Direction` |
| Known_Negative | `known_negative` | `SYSTEM_DEFINITIONS.yaml#Known_Negative` |
| Denominator_Grain | `denominator_grain` | `SYSTEM_DEFINITIONS.yaml#Denominator_Grain` |
| Traversal_Residue | `traversal_residue` | `SYSTEM_DEFINITIONS.yaml#Traversal_Residue` |
| searched population | `searched_population` | `SYSTEM_DEFINITIONS.yaml#Address_Space` and the searched-population discipline cited by Response II |
| vintage | `vintage` | `SYSTEM_DEFINITIONS.yaml#View_Time_Compiled` version-coordinate discipline |
| positive controls | `isolated_positive_control` | `CONTROLS_OVER_CARE.md` and CLAUDE Rule 22a/22b |

The new schema candidates are `shared_failure_domain`, `independence_crossings`, and
`invalidation_predicates`. The first two implement one shared-failure-domain / independence-cut
concept. Base is the registry executor and CTO is the architecture gate.

## Pre-act token census

Invocation:

`python .tools/comp-find '\b(shared_failure_domain|independence_crossings|invalidation_predicates)\b' infra/system/ontology/SYSTEM_DEFINITIONS.yaml org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml org/modules/graph/NFRA_ONTOLOGY_C2C3_CANONICAL.yaml --limit 100`

Measured result: 0 hits across 3 files scanned. This is a scoped zero over definitions,
rule-bank, and canonical surfaces, not an estate-wide absence claim.

## Current control practice on the three C1 instruments

- `comp-find`: graded denominator and word-boundary search exist; C2 adds a one-file isolated
  sentinel population and a deterministically generated absent token.
- `comp-estate`: `--list --head 2` preserves the denominator footer; C2 contrasts it with a
  deterministically generated nonexistent vertical, which returns rc=2 and a C1 UNKNOWN record.
- `census_substrate`: its descriptor path already accepts an injected runner; C2 runs a one-item
  isolated `aws.lambda` payload and a generated malformed JSON payload through the real parser.

Every acquisition emits a C1 Observation_Record. No shared engine is edited.
