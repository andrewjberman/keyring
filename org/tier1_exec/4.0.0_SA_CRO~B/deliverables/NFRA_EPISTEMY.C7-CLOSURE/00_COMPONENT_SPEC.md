# NFRA_EPISTEMY C7 production-influence closure and D3 population

Status: locally complete; proposed for `4.0.0_SA_CRO` registry execution and
`1.0.0_SA_CTO` architecture gate.

Source of record: `docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md`
sections 0, 2.1, and Component 7 at
`b30b05d00675f0b3758d1ed8ccbedf0004b901f5`. This package cites the shared
`Observation_Record` and calls the landed C1 implementation; it does not own or
copy the envelope fields.

The compiler reads only pinned Git objects. Three declared adapters generate the
influence-seed population: Pass 3 code bindings, trigger-map target edges, and
census-substrate inventory descriptors. Generic breadth-first closure returns a
path witness for every reached production terminal. Known seeds with no terminal
path are `NOT_REACHED`; incomplete source population is `UNKNOWN`; malformed
source members are `FAILED`. No terminal is represented by silent absence.

The compiler produced 175 D3 rows: 172 `REACHED`, 2 `NOT_REACHED`, 1 `UNKNOWN`,
and 0 `FAILED` in the production instance. The `FAILED` terminal was exercised by
a scratch mutant. The single `UNKNOWN` is the measured difference between the
trigger map's declared 154 triggers and its 153 keyed trigger records.

Run the acceptance without writing:

```text
python org/tier1_exec/4.0.0_SA_CRO~B/deliverables/NFRA_EPISTEMY.C7-CLOSURE/scripts/run_acceptance.py
```

Regenerate only after the scratch controls pass:

```text
python org/tier1_exec/4.0.0_SA_CRO~B/deliverables/NFRA_EPISTEMY.C7-CLOSURE/scripts/run_acceptance.py --write
```

The `--write` path always runs the scratch hand-authored-row, unreachable-edge,
and malformed-edge mutants first. It then runs the production compile twice and
requires byte identity before writing the population, the C1 envelope, and the
acceptance record.
