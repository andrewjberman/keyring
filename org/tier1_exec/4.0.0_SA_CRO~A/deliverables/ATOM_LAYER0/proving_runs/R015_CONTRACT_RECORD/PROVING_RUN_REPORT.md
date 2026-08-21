# ATOM_LAYER0 S5 proving run: R015 Contract_Record

**Seat:** 4.0.0_SA_CRO~A  
**Status:** PROPOSED; acceptance bar satisfied, owner findings not repaired here  
**Subject selector:** 4.0.0_SA_CRO~B via CRO Base  
**Subject release:** census commit `3265c08100`, row R015  
**Evidence vintage:** `602b73a1f99d889dabbc884525b10dd8e7bf2e56`  
**Target-blind grammar:** `decomposition_grammar@1.0.0` at `462ac78311a3d5f1310a8da3f4f7638127d449bd`, committed before disclosure

## Result

The 24-cell declared frontier closed. Five raw hypotheses were rejected by the
same-grain, independence, reconstruction, consequence, and non-triviality tests.
Grammar adequacy was separately demonstrated against all six prescribed historical
decompositions before the certificate was revalidated.
The bounded result is:

`ATOMIC_WITHIN(decomposition_grammar@1.0.0 x repo-only Contract_Record authorities/schema/consumers at 602b73a1f99d889dabbc884525b10dd8e7bf2e56)`

This is not a global indivisibility claim. It separates concept composition from binding
resolution: Contract_Record can be atomic within the declared grammar while four of its
five enumerated bindings are unresolved.

## Method defects found and repaired

The pre-repair adapter claimed direct census-row ingestion but attempted JSON decoding
on the whole YAML document and expected local alias fields absent from ~B's Rule-24 row.
The exact command failed as `INSTRUMENT_UNKNOWN`.

The repair adds JSON/YAML loading, exact `rows[]` selection, external schema validation,
enclosing-document vintage carry, and unchanged preservation of the selected source row.
The earlier normalized JSON shape remains an explicit compatibility alternative. The
pre-repair failure and both defect records are preserved beside the run.

The pre-repair certificate predicate also trusted whatever productions the grammar
happened to expose. A schema-valid retrodiction battery now exercises six real
decompositions, and the validator refuses frontier exhaustion unless the battery is
present and every specimen is expressible.

## Grammar-v1 retrodiction battery

| Specimen | Expressible? | Operator and reconstruction rule |
|---|---:|---|
| Territory -> Substrate x Deploy_State | yes | CONJUNCTIVE; constrained Cartesian coordinate over the two independent axes |
| six-tag epistemic legend -> five axes | yes | CONJUNCTIVE; product of Authority, Realization, Basis, Resolution, and Genesis coordinates |
| mutation_purpose -> five-axis act tuple | yes | CONJUNCTIVE; five-axis Cartesian tuple, with Gate_Profile derived by constraint join |
| trust-base membership -> proof role x empirical status | yes | CONJUNCTIVE; independent two-axis coordinate jointly scopes reliance |
| census verdict taxonomy -> three axes | yes | CONJUNCTIVE; constrained product with null/empty limbs for NOT_ASSESSED |
| Lifecycle contest -> Class + Stage | yes | DISJUNCTIVE; exhaustive partition of the ambiguous semantic-sense set while retaining distinct governed grains |

Result: 6/6 expressible; no grammar-v2 operator is required by this battery.

## Concept findings routed, not fixed

- Registry `Contract_Record` copies the member list despite the registry header's
  cite-never-copy rule and omits optional `describes` relative to the rule bank.
- `LAYER_FIELD_ANATOMY.md` repeats the same optional-field omission.
- `estate-contracts/README.md` omits `describes`, retains retired `scope` where the
  authority uses `locality`, and cites a stale rule-bank version/line range.
- `comp_legacywriter.py` dynamically checks its universal-required mirror and its C9l
  control passes, but runtime still re-declares the pair instead of compiling it.
- The two-file, 14-record instance population resolves at the pinned vintage; the live
  self-test printed its denominator and passed all 22 controls.

All findings route to candidate owner `1.0.0_SA_CTO`. No registry, rule-bank,
documentation, code-owner, cloud, or deployed surface was changed.

## Verification

- exact R015 source-row preservation: PASS
- adapter and adequacy self-test: PASS 10/10
- grammar-v1 retrodiction battery: PASS 6/6
- proving validation with `--require-proving-defect`: PASS
- comp_legacywriter live-fixture self-test: PASS 22/22
- package manifest exact-set check: see package handoff

The structured source of record is `atom_layer0_run.json`; this report does not replace
its frontier, contracts, Rule 24 records, or residue.
