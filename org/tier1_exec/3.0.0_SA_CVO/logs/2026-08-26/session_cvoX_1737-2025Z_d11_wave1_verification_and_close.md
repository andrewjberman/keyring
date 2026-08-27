# 3.0.0_SA_CVO~X — session 1737–2025Z: D11 wave-1 proof-of-spec verification, decomp cert, wave close

**archetype:** VALIDATE

## What this session was

Seated Andrew-direct (~17:3xZ, verbatim @9473b5121d): proof-of-spec verifier for the ~X cohort's
Tier-2 deliverables, singular focus D11. The session ran the full arc: startup → rubric staging →
ATOM_DECOMP certification (sealed mutant found) → four TO verifications (all PASS, all accepted) →
SC-m-5 measured discharge → the wave-1 close record @303f8160b5.

## Deliverables, all committed under this author line

| record | commit |
|---|---|
| Andrew-direct seating record | 9473b5121d |
| Verification rubric (14 amendments through the session) | 59e9e49508 … 2e53c35e97 (final @bf4c0dc1f7 lineage) |
| Decomp cert ATTEMPT 1 PASS + rectangle.final.certified.json | 5b390a5662 |
| Verdicts: CCX / CCY / COX / DTX-phaseA | d9f1385596 / 00348b4524 / c97a0f30cc / 26b4d6cea3 |
| Wave-1 close record (phase-B verdict + SC-m-5 discharge) | 303f8160b5 |

Push states: all landed LOCAL at write time except where re-measured (CCX artifacts confirmed on
origin with fired positive control); rides integration.

## The certification (headline of the session)

Sealed mutant found: SC-f-4.executor_class, planted 0.7.0_AE_CloudOps~X, true 0.8.0_AE_CloudComp~Y.
Three independent discriminators with counterfactuals; seal matched on all five fields two-sided —
COO~X's sealed dry sha256 reproduced from MY independent regeneration under their named
normalization (503da693…), so neither seat copied the other's bytes. Consumable minted via
DRY-DERIVES-CERTIFIED (plant excluded by construction).

## Verification results

4/4 TOs PASS at my seat, none cited from lanes: gate VALID by stdout token (the rc does not
discriminate — lane-found, confirmed harmless to my verdicts), v1 schema 0 errors on all 8 cards +
the 39-part manifest (L0), 56/56 + 14/14 rows complete, 0 absent rows, as_of on-pin 8/8, zero
evidence back-dating, alignment ENFORCE at full denominators. Phase B residue-2 boundary re-derived
with a different instrument to the identical 22-part set. SC-m-5 discharged at measured zero on
three instruments — after discarding my own first sweep whose positive control failed.

## Verifier errors, own record (all caught before they fed a verdict)

Digest mislabel (CRLF-as-LF) in my own cert, fixed pre-commit · false arm-missing off a regex
phrasing mismatch (COX AC4) · wrong-key part_id probe · "UNOPENED" literal miss · a dead-control
zero on the first SC-m-5 sweep, discarded. Pattern banked in the rubric: probes screen, artifacts
decide; a zero over a non-firing control is discarded unread.

## Compiler Tools

| tool | use | result |
|---|---|---|
| proof-of-spec-check.py | 5 gate runs (4 TOs + re-checks) | VALID all; verdict read from stdout token, never rc (rc measured non-discriminating by DTX) |
| comp-* rail | not otherwise invoked — this seat's session was artifact verification over named files (Read/git/jsonschema were the fitting instruments); comp-find/comp-keys trap findings from lanes were banked into the rubric rather than re-run | n/a |
| aws dynamodb list-tables | 1 run, bounding DTX's known_unsearched gap | 36 tables, 0 graph-named |
| git (log/show/diff/merge-base, fetch) | vintage pins, delta scopes, push-state re-measures, SC-m-5 sweeps | all with positive controls where a verdict rested on them |
| jsonschema Draft 2020-12 | card schema v1, L0 manifest, 11 artifact validations | exercised with negative controls |

## Open at session end

Event-driven standing posture. Waiting on: whatever D11 wave-2 / v2-schema work the issuers route;
any Andrew-direct. No cell, verdict, or ask is open at this seat. Watcher Monitor b4f9nh7q8 live.

— 3.0.0_SA_CVO
