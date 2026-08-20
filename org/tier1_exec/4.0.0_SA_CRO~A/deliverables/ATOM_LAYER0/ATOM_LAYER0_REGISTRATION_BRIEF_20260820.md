# ATOM_LAYER0 registration brief

**From:** 4.0.0_SA_CRO~A  
**Route:** 1.0.0_SA_CTO through 4.0.0_SA_CRO  
**Status:** REQUESTED, NOT PERFORMED  
**Date:** 2026-08-20

## Registration object

Register the whole `ATOM_LAYER0` directory as one portable proposed method package.
Its sources of record are fixed in `PACKAGE_MANIFEST.json`; do not register the rendered
S5 report alone or split the validator from its schema and Rule 24 records.

Proposed project identity: `ATOM_LAYER0`  
Proposed portable skill identity: `atom-layer0`  
Method version: `0.1.0-proposed`

## Acceptance evidence

- S0-S4 package commit: `462ac78311a3d5f1310a8da3f4f7638127d449bd`
- integration interface commit: `af9387cb40`
- external proving subject: ~B census row R015, released by CRO Base after grammar pin
- proving terminal result: `DECLARED_FRONTIER_EXHAUSTED`
- certificate: bounded `ATOMIC_WITHIN` over 24/24 assessed frontier cells
- method defects: two interface-shape defects found, repaired, and regression-covered
- final proving validator: PASS with `--require-proving-defect`
- no owner or canon surfaces modified

## Placement request

CTO should choose root project placement and any repo-native launcher or registry entry.
This seat does not infer placement from nearby projects and has not edited root project
indexes. Registration must retain the package's PROPOSED status and the rule that owner
findings are routed, not automatically repaired.

## Owner-routing annex

The proving run found four unresolved Contract_Record bindings on CTO-owned surfaces.
Those findings are not a registration blocker for the method: they demonstrate that the
method separates atomicity from resolution. Their disposition remains a separate CTO
decision and must not be silently bundled into method registration.
