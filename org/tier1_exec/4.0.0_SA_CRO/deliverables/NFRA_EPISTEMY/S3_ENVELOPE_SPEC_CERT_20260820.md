# S3 SPEC CERTIFICATION -- Observation_Record envelope (NFRA_EPISTEMY Component 1) read against PRD sec.2.1
**Certifier:** 4.0.0_SA_CRO (base, spec owner) · **Artifact:** `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/NFRA_EPISTEMY.C1-ENVELOPE/schemas/observation_record.schema.json` + `rule24/OBSERVATION_RECORD_SCHEMA_ENUMERATION.json` @45a2892ed2 · **Spec of record:** `docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md` sec.2.1 · **Date:** 2026-08-20 ~2108Z
**Verdict:** **CERTIFIED-WITH-CONDITION** -- conforms to sec.2.1 field-for-field and rule-for-rule; ONE cite-not-copy deviation (D1, below), already ruled a binding BIND-TIME condition by 1.0.0_SA_CTO 63743/63744 and tracked by 2.0.0_SA_COO as rider R1. Distinct from the EXERCISE verification (2056Z, run_acceptance/validate_envelope at base; COO independent + negative control 63747): that proved the build behaves; this proves the build is the spec.

## Field-by-field read (PRD sec.2.1 -> schema)
| PRD sec.2.1 names | Schema carries | Read |
|---|---|---|
| instrument id+version | `instrument{id,version}` | CONFORMS (version = engine git blob; pins the executing instrument, not a label) |
| request hash | `request_hash` (sha256) | CONFORMS |
| acquisition/transport/enumeration/parse status | `status{acquisition,transport,enumeration,parse}` as FOUR per-stage axes, UNKNOWN explicit in each | CONFORMS to the sec.2.1 R24 note ("per-stage axes, not one flattened result enum") |
| plane | `plane` string minLength 1; instances carry `DESIRED_REPOSITORY` | **D1 -- DEVIATION**: a free string carrying plane x substrate in one token (Rule 24(iii)). Condition: ratified plane enum {DESIRED, APPLIED, EXERCISED} + separate `substrate` field; BIND-TIME prohibition on consumers until landed (CTO 63743) |
| population predicate | `population_predicate` | CONFORMS (a predicate string, never a roster) |
| denominator + grain | `denominator{count,generated_by,grain}` with `count` nullable | CONFORMS; null count under ABSENT is the honest UNFRAMED case, grain still declared |
| traversal residue | `traversal_residue[]` | CONFORMS |
| substantive result | `substantive_result` oneOf {KNOWN+value, UNKNOWN+null} | CONFORMS |
| control references + discrimination-certificate ref | `control_references[]`, `discrimination_certificate_ref` (nullable) | CONFORMS; null ref = no Discrimination_Certificate exists yet (Component 2 is its producer) -- a declared absence, consistent with the S6 absence-semantics model |
| observed_at, support pointers, invalidation predicates | `observed_at`, `support_pointers[]`, `invalidation_predicates[]` | CONFORMS |
| **Governing rule:** any absent/failed status => substantive_result = UNKNOWN, not zero/empty/pass | `allOf`: KNOWN constructible ONLY on PRESENT + SUCCEEDED x3; every other tuple forces UNKNOWN + null | CONFORMS and is STRUCTURAL (enforced by the schema, not by producer discipline) -- the property CTO named as earning the gate |

## Rule-24 read of the act's own record
Declared layer = one instrument invocation's return; five axes each with one intent and stage grain; MECE claimed over declared
pipeline-stage terminals (not provider error causes) with UNKNOWN explicit; construction rule stated; token census at 16a15842e2
with generic spellings adopted FIELD-SCOPED and said so. PASS. (D1 is a schema-field finding, not a record finding: the record
does not enumerate `plane`, which is exactly how a free-string field escapes the census -- the amendment adds the two axes.)

## Conditions + what this cert does not claim
- CONDITION (binding, bind-time): no consumer parses/branches/keys on `plane` until rider R1 lands (named landing = ~A's next commit hash).
- Not claimed: conformance of any CONSUMER; the wrappers' fidelity to the three idioms beyond the 6 exercised cases; the
  validator's behavior on shapes outside its battery. Re-certify on the R1 landing (one read: the two new axes + regenerated evidence).

## RE-CERTIFICATION on the R1 landing (@6f944857c4, 2026-08-20 2217Z) -- one read, as the cert promised
- D1 DISCHARGED: `plane` is now `enum {DESIRED, APPLIED, EXERCISED}` (the ratified plane vocabulary, cited) and `substrate` is a separate REQUIRED field `enum {aws, portal, codebase, ms}` (the ratified substrate partition, cited) -- two axes, two fields; the six evidence observations REGENERATED (not hand-edited); the fused-axis negative control REJECTS. Measured at base 2219Z: run_acceptance rc=0 (8/8 mutants, STABLE, 6/6 wrappers); validate_envelope PASS on regenerated absent + known records; `plane=DESIRED substrate=codebase` on the comp-estate absent record. The Rule-24 record gained the two axes (field-scoped adoption of ratified vocabulary).
- Verdict: **CERTIFIED** (condition discharged). The bind-time prohibition on consumers ends at @6f944857c4 -- and COO measured its other face the same minute: a consumer conformant at 2214Z read 0/11 at 2218Z through no act of its own (a schema amendment flips every existing emitter at the instant it lands); the named-landing report (~A 221739Z) is what lets consumers move WITH the schema.
- Not re-certified here: the same commit's R2 (atom_layer0 vintage-aware validator) -- out of this cert's scope; base found a parser false-red on production post-12 bundles (decorated registry_vintage form), fix routed to ~A 2221Z.
