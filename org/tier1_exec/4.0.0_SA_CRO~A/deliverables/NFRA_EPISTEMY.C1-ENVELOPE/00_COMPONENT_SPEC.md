# NFRA_EPISTEMY C1 typed observation envelope

Status: proposed for 4.0.0_SA_CRO registry execution and 1.0.0_SA_CTO architecture gate.

Source of record: `docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md` section 2.1 at `bf88ff55c6`. This package implements and cites that shared object; it does not independently own its field set.

The schema and constructor enforce one boundary: only an acquisition pipeline with `PRESENT / SUCCEEDED / SUCCEEDED / SUCCEEDED` may carry a `KNOWN` substantive result. Every other terminal tuple carries `UNKNOWN` and a null value. Denominators state their grain and generating process. CTO condition 63744 is discharged by keeping the ratified verification `plane` (`DESIRED`, `APPLIED`, `EXERCISED`) separate from physical `substrate` (`aws`, `portal`, `codebase`, `ms`).

Run:

```text
python org/tier1_exec/4.0.0_SA_CRO~A/deliverables/NFRA_EPISTEMY.C1-ENVELOPE/scripts/validate_envelope.py --self-test
python org/tier1_exec/4.0.0_SA_CRO~A/deliverables/NFRA_EPISTEMY.C1-ENVELOPE/scripts/run_acceptance.py
```

The acceptance run exercises the PRD section 5c eight-mutant battery twice and six wrapper cases: one successful and one genuinely absent acquisition for each of `comp-find`, `comp-estate`, and `census_substrate`. The absent cases must be valid envelopes whose substantive result is `UNKNOWN`, never zero, empty, or pass.
