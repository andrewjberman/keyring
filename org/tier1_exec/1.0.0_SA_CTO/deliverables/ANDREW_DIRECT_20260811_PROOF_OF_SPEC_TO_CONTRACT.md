# ANDREW-DIRECT — build TOs carry machine-readable PROOF-OF-SPEC deliverables

**Channel:** Andrew-direct at the 1.0.0_SA_CTO terminal, 2026-08-11 ~0815Z.
**Recorded by:** 1.0.0_SA_CTO same turn. **Broadcast:** COO + CVO + MSTR.

## VERBATIM

> "Make sure that the instructions are rigidly explicit and have machine-code json deliverable
> expectations that the tier 2 senior worker agents have to fill out to prove that they did it
> to spec"

## THE MECHANISM (built + exercised this window, not just specified)

1. **`org/standards/PROOF_OF_SPEC.schema.json`** — the canonical deliverable contract (draft-07).
   Every build TO's completion artifact is an INSTANCE of it: one acceptance row PER criterion of
   the governing spec's battery (criterion quoted VERBATIM — the assignee proves against the SPEC,
   not a paraphrase), each row carrying the exact re-runnable invocation + verbatim output
   evidence + its denominator; artifacts with deployed-state declared (an atomic commit is not an
   atomic deploy); mandatory mutant + determinism controls (a control that did not fire INVALIDATES
   the deliverable by its own field); declared exclusions (an unmarked gap reads as coverage);
   surprise-channel entries; compiler-tools table. NO BARE VALUES — a PASS with empty evidence
   invalidates the whole instance.
2. **`.tools/proof-of-spec-check.py`** — the mechanical gate. Exit 0 VALID / 1 INVALID with every
   violation printed. Layered: jsonschema structure + the conditional rules the schema cannot
   express (FAIL-requires-reason; thin-evidence-PASS; dead-control). Degrades LOUDLY if jsonschema
   is absent. **Exercised at authoring: positive control VALID rc=0; a 4-defect mutant instance
   caught 4/4 rc=1.**
3. **The TO law**: COO's build TOs EMBED the criterion_ids (lifted from the specs' acceptance
   batteries) and state the deliverable expectation explicitly: "completion = a schema-valid
   PROOF_OF_SPEC instance passing proof-of-spec-check, committed beside the work." CVO's
   cert-of-built CONSUMES the instances (re-running invocations from the rows is the adversarial
   re-derivation, made mechanical). A TO without a valid instance is NOT complete — this extends
   the existing TO_COMPILER_GATE standard, same home.
