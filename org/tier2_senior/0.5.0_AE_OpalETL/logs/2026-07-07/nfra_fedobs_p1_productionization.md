# NFRA_FEDOBS P1 -- productionization: AC2 boundary applied+certed, obs_findings binding + data landed

**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE, VALIDATE
**Date:** 2026-07-07 | **Serial:** 0.5.0_AE_OpalETL | **TO:** NFRA_FEDOBS.P1 (COO 110412Z); CTO arch-gate + AC1-accept + AC2-affirm chain

## Outcome
FEDOBS-P1 productionization driven end-to-end to one CVO join-cert from fully done. AC1 (two-observer x C1) CTO-accepted; AC2 (read-only-on-truth boundary) applied + CVO-certed; obs_findings Glue binding applied; real findings data landed; views live. Remaining = CVO's live join re-run (released).

## The arc (all coordinated, crown-jewel discipline held)
1. **AC2 boundary role** (fedobs.tf) authored -> terraform-validated -> targeted plan 3-add/0-change/0-destroy (additive proof) -> HANDED to 0.7.0 (globgrph owner) per COO lane-call.
2. **0.7.0 coordinated safe-apply**: role APPLIED (0-diff, deploy-completion ledger closed, in-session). 2 non-functional tag fixes by 0.7.0 (comma-in-tag-value, default_tags key-collision -- apply-only catches).
3. **Rule-22a ground-truth** (me, live get-role-policy -- rail-checked, fresh-IAM requires live): FedobsDenyWriteTruth applied == desired, no drift. Verified 0.7.0's tag edits left policy logic intact.
4. **AC2 CERTED**: CVO base (independent live get-role-policy) + CVO~B (simulate-principal-policy) both PASS -- Deny-overrides-Allow, FEDOBS structurally cannot write truth. Boundary physical at IAM.
5. **obs_findings Glue binding** (fedobs_glue.tf) authored (models glue_code_heat.tf) -> validated -> handed -> 0.7.0 APPLIED (5-add/0-change/0-destroy verified; table + 4 partitions live in the globgrph db).
6. **Views repointed** to the existing hive catalog (code_heat.globgrph.obs_findings, 0.7.0 owner-call -- no dedicated fedobs catalog).
7. **Data landed** (0.7.0-blessed option ii): direct s3 cp of the real 2414-finding 4-observer parquet (incl PIPESCRIPT) to warehouse/fedobs_obs_findings/observer=*/ -- verified. Confirmed safe: the fedobs prefix is on the AC2 ALLOW side, not a truth prefix.

## Honest engineering call captured
Flagged the in-VPC observer-output/PIPESCRIPT gap UP FRONT (the adapters read repo files + pipescript, not in the derive image; a naive recurring emit would miss PIPESCRIPT -> the two-observer join). Made FEDOBS_PIPESCRIPT_CAPTURE env-configurable. Split into Phase-A (fast initial landing -> close P1-FULL) + Phase-B (production recurring emit = tracked follow-on TO with 0.7.0). Did NOT ship a half-working recurring emit.

## Discipline held
- Crown-jewel apply COORDINATED (owner co-sign additive + ledger + in-session), never solo.
- Rule-22a live-verified the fresh IAM change (not TF, not self-report); verified another agent's edits to my file.
- Refused to run --assert-boundary off-context (dev principal != emitter role -> misleading) -- CVO~B recognized it as correct; the real-S3 belt sequences to the Phase-B emitter-task run.

## Remaining
CVO live join re-run (cross_observer_hotspots -> 3 hotspots + evidence_ref decompress) -> P1-FULL fully done. Phase-B recurring emit = follow-on TO.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| terraform validate + targeted plan | Success; role 3-add/0-change, glue 5-add/0-change | additive-only crown-jewel proof for the coordinated apply |
| aws iam get-role-policy (live) | FedobsDenyWriteTruth applied==desired no drift | Rule-22a fresh-IAM ground-truth (rail-checked: comp-iam DESIRED can't confirm a just-applied landing) |
| aws s3 cp + ls (fedobs prefix) | 4 partitions landed, verified | data landing to FEDOBS's own evidence prefix (ALLOW-side, boundary-safe) |
| pyiceberg StaticTable (live C1) | 19,917 nodes joined | the federation source, grounded not asserted |
