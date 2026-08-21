# NFRA_EPISTEMY C7-CLOSURE S0 ground read

Seat: `4.0.0_SA_CRO~B`  
Pinned input vintage: `b30b05d00675f0b3758d1ed8ccbedf0004b901f5`  
Status: Phase 1 complete before compiler/D3 authorship

## Boundary read

Component 7 is the production-influence closure compiler and its process-generated
D3 population. Component 3 identity/support closure is excluded. PRD section 2.9
harm surfaces remain OPEN and are not implemented. No graph engine, AWS surface,
gate, monitor, or enforcement surface is changed.

The governing law is cited, not restated as a new source of record:
`docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md:9-18 @
b30b05d00675f0b3758d1ed8ccbedf0004b901f5`. The shared
`Observation_Record` is cited at PRD section 2.1 and consumed through the landed
C1 implementation, not copied into this component.

## Declared input-source population

| Source | Pinned blob | Declared grain | Measured denominator | Treatment |
|---|---|---|---:|---|
| Pass 3 code-grain census | `18d49c1611b3b75c27302a22017d36a90c171346` | one surface x concept binding | 10 rows (9 unresolved, 1 resolved) | Every row becomes one `CODE_BINDING` seed, per the C7 task order's explicit ruling that these rows are influence-edge census. |
| Trigger census compiler | `cc196e33c83432e31b2ab9e1b917cc42fc80c889` | one enumerated trigger and its target list | builder declares 154 triggers | `build_map` and `diff_maps` are the declared generation/drift process (`trigger-census.py:395-490`). |
| Trigger map | `7c254d168a0fbaedc89dcda9d053769b07b39fdc` | one trigger x target edge | 154 declared triggers; 153 keyed rows; 162 materialized target edges | The 162 edges enter. The declared-minus-keyed delta of 1 becomes an explicit UNKNOWN member; it is never silently dropped. |
| Census substrate | `ea27e693716e449935e20ad682a383d87ae69f9b` | one inventory descriptor | 2 descriptors (`aws.iam`, `aws.lambda`) | Descriptor rows enter as inventory-frontier seeds. With no live inventory result in the pinned input bundle, they terminate `NOT_REACHED`, not absent. |
| Estate census drift instrument | `1f646d7c26d95dff3af19b5eee74e81385709ff7` | census x desired/applied set difference | one declared instrument, two planes | Cited as a precursor/control. C7 does not execute AWS and does not duplicate its set-diff (`opal_estate_infrastructure.py:749-801`). |
| C1 envelope implementation + schema | `4aa72ab99cea52b8a1c46091aa08c73c9d73b859` + `4673036e8d12a1a73d6e5c9abd214ee7d30b513e` | one instrument invocation | one landed implementation/schema | C1 landed at `6f944857c42fb9013a3fe04542a487339a24f55f`; C7 emits envelopes using `build_record` and validates with `validate_record` (`observation_envelope.py:29-118`). |

Expected process-generated D3 row denominator from these pinned inputs is 175:
10 Pass 3 bindings + 162 trigger-target edges + 2 descriptor frontiers + 1
UNKNOWN trigger-map residue.

## S0 finding carried, not chased

`trigger-map.json` declares 142 EventBridge Rules plus 12 Scheduler schedules =
154 triggers, while the keyed `triggers` object contains 153 members. The builder
uses a dict keyed only by `trigger_name` (`trigger-census.py:395-419`), so a name
collision or stale denominator can erase a row. C7 cannot distinguish which from
the committed map alone. It therefore carries exactly one UNKNOWN population
member and routes the source-instrument finding; it does not edit the owner
instrument.

## Status-shape decision

The C1 envelope is landed, so C7 emits `Observation_Record` envelopes rather than
inventing an interim envelope. C7's internal closure-state axis remains explicit:
`REACHED`, `NOT_REACHED`, `UNKNOWN`, and `FAILED`. The accompanying Rule-24
pre-record defines their non-overlapping evaluation order and the process-origin
predicate before any compiler or D3 population is authored.

