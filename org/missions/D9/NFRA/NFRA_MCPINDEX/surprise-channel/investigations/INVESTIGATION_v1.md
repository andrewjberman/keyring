# NFRA_MCPINDEX -- surprise channel, INVESTIGATION v1

**Opened by:** `0.9.0_WK_NFRA_MCPINDEX~1` at L7, cell `MX-c-1`, 2026-09-21. **Home:** the project tree's channel.
Lane `ANY`; the gate `.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder
== project). **Append-only.** Worker rows carry their slot's coordinate, `NFRA_MCPINDEX-W<n>-S<k>`; a seat's row
carries none.

**Denominator at this write: 2 rows** -- `NFRA_MCPINDEX-W1-S1`, `NFRA_MCPINDEX-W1-S2`, both `0.9.0_WK_NFRA_MCPINDEX~1` at L7.

```json
[
  {
    "id": "NFRA_MCPINDEX-W1-S1",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-21T05:07:26Z",
    "one_line": "MXC1-AC4 requires running the named writer once and observing the SERVED file (infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml) change, plus a reversible edit to an emitter input under workflows/atom_decomposition/runs/; this cell's <paths> grant names only emit_catalog_v02.py (docstring lines 1-10) and this investigation file.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO: org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-c-1.catalog-writer.md <paths> block (2 entries only): 'workflows/atom_decomposition/emit_catalog_v02.py' and 'org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md'.",
        "CRITERION: same TO, MXC1-AC4 verbatim -- '(difference) the named writer is run once at the cell's HEAD with one reversible change to an emitter input, the served file changes by exactly that row, and the same run with the input unchanged leaves the served file's SHA-256 unchanged (the run and its revert both in the cell's command log)'.",
        "WRITE TARGET: emit_catalog_v02.py:42-43 -- OUT_DIR/OUT resolve to infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml (the 'served file'), confirmed by MXC1-AC3's module-import read (probes/mx_c_1.py AC3, 2026-09-21T05:07:04Z): resolved target == live path.",
        "INPUT SOURCE: lift_catalog_v02.py :308-313 -- resolve_substrates() reads rectangle.final.certified.json under workflows/atom_decomposition/runs/<unit>/<stamp>/, the only 'emitter input' a reversible edit could target without editing emit_catalog_v02.py's own non-docstring code.",
        "BOUND: worker face BOUNDS (top-level, and this TO's own Bounds section) verbatim -- 'A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.' Bound 9 (decomp s.8) -- 'A criterion that cannot be satisfied as written is REFUSED and reported with its measurement, never repaired, widened or met by another route.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order's ACCEPTANCE section demands MXC1-AC4 be satisfied by actually running the writer once and observing the live served catalog file change by exactly one planted row, with the run and its revert logged; the same order's <paths> block is the worker's whole write grant.",
    "world_is": "The <paths> block names only the emitter's own docstring lines and this investigation file. Exercising MXC1-AC4 as written needs write access to infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml (the served file itself) and to a workflows/atom_decomposition/runs/ certified-run JSON (the only lever for a 'reversible change to an emitter input' that does not edit the emitter's own logic, itself out of grant beyond the docstring). Neither path is granted. The worker recorded MXC1-AC4 REFUSED (probe VERDICT: FAIL-MXC1-AC4) rather than writing outside the grant or redirecting the writer's output to a substitute path (which would not exercise the NAMED writer against the NAMED live path C1/AC3 require).",
    "notes": "BLOCKING on MXC1-AC4 only; AC1, AC2, AC3, AC5, AC6 are unaffected and PASS by their own probes. INERT: no live state changed and nothing is armed by the refusal -- the writer's exercise remains undone, not miswired. disarm/owner: whoever re-cuts or re-grants this cell (issuer 2.0.0_SA_COO~M) decides whether to widen the <paths> grant to cover the served file + a runs/ input for a future pass at AC4, or to accept the REFUSED disposition as this round's answer."
  },
  {
    "id": "NFRA_MCPINDEX-W1-S2",
    "project": "NFRA_MCPINDEX",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_MCPINDEX~1",
    "surfaced_at": "2026-09-21T05:30:00Z",
    "one_line": "This TO's <proof_of_spec> section names firm `NFRA` for the proof-of-spec instance, but PROOF_OF_SPEC.schema.json's `firm` field is a closed enum {49F, INF, COT, MDPF, FABRIC} with no NFRA member; setting it would fail jsonschema structural validation, so the field was left absent (schema-optional) instead.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO: org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-c-1.catalog-writer.md:114 -- '(phase `INVESTIGATION`, firm `NFRA`, spec_ref.group `OTHER`, ...)'.",
        "SCHEMA: org/standards/PROOF_OF_SPEC.schema.json, `firm` property -- 'enum: [\"49F\",\"INF\",\"COT\",\"MDPF\",\"FABRIC\"]'; NFRA is not a member.",
        "INSTRUMENT: py -3.12 -c \"import jsonschema; print(jsonschema.__version__)\" -> 4.26.0 installed in this worktree's environment, and .tools/proof-of-spec-check.py:2316-2323 runs jsonschema.Draft7Validator(schema).iter_errors(inst) when the package is present -- an enum violation would be a structural FAIL, not a warning."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order's own <proof_of_spec> instructions name the literal field value firm `NFRA` for this instance.",
    "world_is": "The ratified schema's `firm` enum has no NFRA member (its 5 members are client-firm codes plus FABRIC for no-client-firm fabric-infrastructure work); NFRA is this project's macro code, not a schema-recognized firm token. Setting `firm: \"NFRA\"` would make the instance schema-INVALID under jsonschema, which is installed and active in proof-of-spec-check.py. The worker omitted the field (OPTIONAL per schema) rather than write a value the checker's own structural pass would reject; the field's absence resolves per the schema's own documented fallback to UNPARSED-by-derivation (to_id's leading token 'NFRA_MCPINDEX' is also not an enum member).",
    "notes": "OBSERVATION, INERT: no criterion in this cell reads the `firm` field, and omitting it does not fail proof-of-spec-check.py (the field is optional at the schema level). Whether NFRA-macro projects need a `firm` enum member (or whether FABRIC is the intended value for D9/NFRA work) is a schema-owner call, outside this cell's <paths>."
  }
]
```
