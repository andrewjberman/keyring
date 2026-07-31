# estate-contracts — WS-E1 D3 contract instances

**Owner:** `0.7.0_AE_CloudOps~D` · **Arch-gate:** `1.0.0_SA_CTO` (shape approved 20260731T074941Z,
re-gated against the ratified grammar 20260731T075420Z).

## WHAT THIS IS

Instances of the **ratified `contract_record`** (`org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml`
v1.8, `:349-357`). Per that spec: *"CORE fixes the vocabulary; ESTATE WS-E1 declares INSTANCES
against it and **ADDS NO TERMS**."*

**Subject identity is the KEY, not a field.** The record is *carried by* the subject, so each entry
is keyed by subject and its value is a `contract_record` with **only ratified fields**:
`required: [intent_source, obligation, lifecycle_class, revalidate_by, scope]` ·
`optional: [successor, expiry_condition, cadence, vintage_probe]`.

## ⛔ PROHIBITION 1 — NO CACHED VOCABULARY. EVER. AND HERE IS WHY.

**`lifecycle_class` values are RESOLVED from the rule bank at read time. No cache of resolved
vocabulary may outlive a single read. If resolution cannot reach the rule bank, IT FAILS LOUD — it
never serves a stale copy.**

**THE REASON, stated because a prohibition without its reason gets optimised away by the next
reader:** caching the resolved vocabulary recreates a **frozen enumeration inside a consumer** — the
exact defect of the telemetry appender's `VERDICT_EXIT_TOOLS`, which drifted from the surface it
mirrored and produced **434 miscounted verdicts** and an order-of-magnitude error in the program's
measurement of itself. A cache is that defect returning **with a performance justification instead
of a design one**, and it will be proposed by someone helpful who has never read M3.

## ⛔ PROHIBITION 2 — `lifecycle_class` IS PRODUCER-ASSERTED, NEVER OBSERVER-INFERRED

Rule bank `:364`: *"ANY implementation inferring `lifecycle_class` from KEY NAMES, DIRECTORY
POSITION, or OBSERVED ABSENCE has rebuilt the comp-legacywriter name-pattern stopgap with more
syntax. Transience cannot be derived; it must be DECLARED."*

**Every `lifecycle_class` in this registry is `UNDECLARED`, and that is deliberate.** Recording
`UNDECLARED` **is not inferring a lifecycle — it is declining to.** It asserts nothing about an
artifact's life shape; it records that **no producer has asserted one.** It is the one enum value an
observer may write, precisely because it is the *absence* of the judgement an observer cannot make.
**`UNDECLARED` AUTHORIZES NOTHING.**

Observations about these subjects live in `../../../tier2_senior/0.7.0_AE_CloudOps/deliverables/WS_E1_SPECIMEN_OBSERVATIONS.md`
and are **never promoted into assertions.** That separation is load-bearing.

## ⛔ PROHIBITION 3 — `intent_source` MUST BE A GOVERNANCE LEVEL *ABOVE* THE ARTIFACT

Rule bank `:354`: *"An `intent_source` naming the artifact itself IS the
denominator-is-its-own-configuration defect and is **REJECTED AT DECLARATION**."*

**Where no governance level above an artifact can be cited, the declaration is REJECTED and counted
as a rate. We do NOT go looking for a plausible parent to satisfy the field** — a manufactured
parent is the defect wearing a passing grade.

## Resolution records are OBSERVATIONS WITH A VINTAGE, not a mirror

Each entry records **what its `lifecycle_class` resolved to and when**. A dated resolution record
says *"on date D this resolved to X"* and can only ever be true. A valid-values list claims to be
current and goes wrong. A **non-additive** rule-bank change therefore surfaces as a **mismatch
against the historical record** rather than silently re-mapping every contract's meaning.

## This registry fires nothing

No alarm, no monitor, no checker, no notification. It renders records. Single-writer violations are
**type errors at declaration time**, detectable by reading the registry alone — no scan, no
schedule.
