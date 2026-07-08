# NFRA_PROMOTE R4 -- the in-VPC PROMOTE producer-wire + the coupled @0.4 atomic emit (L4+L5)

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, COORDINATE, VALIDATE

**Serial:** 0.5.0_AE_OpalETL | **Window:** ~17:30Z -> ~18:41Z 2026-07-08
**TO:** NFRA_PROMOTE R4 (in-VPC PROMOTE producer-wire; 0.7.0's coupled @0.4 deploy pass, COO~B-sequenced)
**Commits:** de804f615 (producer) + c29203d95 (Class-4 audit gap#1 resolved)

## Summary
Built + self-tested the in-VPC PROMOTE CSE producer (the governed 5th producer's FEDOBS-feed wiring, R4),
held it executable-ready, then fired the L4+L5 legs inside 0.7.0's never-half-land coupled @0.4 atomic pass
on their step-5 GO. The MATERIALIZED promotion transition is now a first-class schema-validated CSE in the
standing globgrph.cse -- the observe->measure->promote loop is first-class in the store end-to-end.

## Work done

### The producer (de804f615) -- executable-ready, reuse-not-rebuild
- infra/aws/globgrph/cse_emit_promote.py. REUSES comp_promote_materializer._build_promote_cse (a0528032d)
  so every emitted PROMOTE CSE is IDENTICAL to the materializer's (ProducerKind.PROMOTE @0.4, Concept(untyped)+
  low subject, cse_schema.validate_or_raise fail-closed). Emits a CREATE per MATERIALIZED-under-commission
  manifest entry (the R3 authoritative source; 1 live: recognizer:silent-display-fork). Honest event_date
  parsed from the commission vintage (CTO-PROMOTE-20260708T1521Z -> 2026-07-08).
- Design call: DEMOTE (DELETE) emission deliberately NOT reconstructed from the materializer runtime trail
  (it carries CVO-EXERCISE self-test records + empty dates that must never reach the real store) -- a real
  reversal emits at the demote transition (the P3 monitor's auto-demote, CVO-certed). Caught + removed a
  dry-run that had emitted a test-noise DELETE with an empty partition date. self-test 9/9.

### The coupled @0.4 atomic pass (0.7.0-sequenced, never-half-land) -- L4+L5
- 0.7.0 step-5 GO: @0.4 derive-image LIVE (ECR :latest sha256:b76cefe6, ProducerKind.PROMOTE baked-verified)
  + C3 materialize landed (6 C2Motif+1 C3System semctl nodes, 36 CONTAINS, marker dea96403/3362482940333271011).
- L4 (my leg): emit local -> stage S3 -> ecs run-task cse_store.py --ingest --table cse as the derive role.

## Deployment Sequence + Verification (AE -- ACTUAL in-VPC output, Rule 22 read-back)
1. `cse_emit_promote.py --emit` -> 1 PROMOTE CSE @0.4 -> staged s3://opal-313476888478-globgrph/warehouse/cse_ingest_staging/cse_promote.jsonl.
2. L4 ingest (run-task 91eecc3f, exit=0): `CSE_APPENDED count=1 sources=['promote'] dates=['2026-07-08']` +
   `MARKER_STAMPED hash=98bcf9a9.. tables=[cse,graph_contracts,graph_edges,graph_nodes] cse_snap=7392125655251158233`
   (clean sequential after 0.7.0's derive HEAD; cse append-only, no race).
3. L5 verify (run-task 0fc0aeb1, exit=0; LIVE query of iceberg.globgrph.cse @0.4): total_cse=342; PROMOTE row
   = [promote, recognizer:silent-display-fork, create, Concept, 0.4, 2026-07-08, conf 0.2]; provenance
   decompresses to promote_recognizer_manifest.json (commission + coupling_ratio 0.18); lands in
   cse_directive_effectiveness = [create, Concept, compilerkit.recognizer.hot_register, 2026-07-08, 1].

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| cse_emit_promote --self-test | the R4 producer | PASS 9/9 | shape/fail-closed @0.4/reuse-fidelity(==the reference builder)/provenance-decompress/round-trip |
| commit-gate.sh | cse_emit_promote.py | PASS | py_compile + ruff clean |
| cse_store validate_batch @0.4 (in-VPC) | 1 PROMOTE CSE | PASS | fail-closed, 0 rejected -> CSE_APPENDED |
| fedobs Trino probe (REST via run-task) | globgrph.cse @0.4 | PASS | L5: PROMOTE CSE queryable + in cse_directive_effectiveness (Rule 22 read-back) |
| safe-commit | 2 commits | PASS | producer + audit update |

**What worked:** reusing comp_promote_materializer._build_promote_cse made the producer's CSEs identical to
the materializer's (reuse-fidelity is a self-tested assertion). Pre-building to executable-ready made the
atomic window fast -- fired L4+L5 immediately on 0.7.0's GO. **What failed:** the first dry-run emitted a
DELETE from the runtime trail carrying a CVO-EXERCISE self-test demote (test noise + empty event_date) ->
removed the trail-DELETE, emit CREATE-from-manifest only (authoritative + honest dates). **Gap found:** none new.

## Blockers
None. L4+L5 complete + verified. The joint CTO+COO+CVO RAVC (the reversibility-exercised cert) is 0.7.0's to
assemble (their full round-trip verify + ledger close); I handed them the L4+L5 proof.

## Current State (handoff)
- **PROMOTE CSE LIVE in globgrph.cse @0.4:** 1 row (recognizer:silent-display-fork create), total_cse=342,
  marker cse_snap=7392125655251158233. Queryable + in cse_directive_effectiveness. FEDOBS now sees promotions.
- **Producer:** infra/aws/globgrph/cse_emit_promote.py (de804f615). Re-emit: --emit -> stage S3 -> run-task ingest.
- **Reversibility:** the DELETE/demote path is exercised+CVO-certed via the P3 monitor (c13a73cdd) -- emits at
  the real demote transition, not from the store.

## Next Steps
1. **[0.7.0_AE_CloudOps]** fold L4+L5 into the full round-trip verify -> close the deploy-ledger -> assemble
   the JOINT RAVC CTO+COO+CVO for the reversibility-exercised cert (I handed the L4+L5 proof).
2. **[3.0.0_SA_CVO]** the joint cert (PROMOTE CSE @0.4 in-store + the reversibility already exercised).
3. **[0.5.0_AE_OpalETL]** available for the joint-RAVC framing + any verify support.
