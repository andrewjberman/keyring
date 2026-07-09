# Deploy Completion Record
**Date opened:** 2026-07-08T18:56:01.809396+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260708T191931Z
**Deploy:** Collision-fix re-derive (CTO-gated prereq to N>1 C3): rebuild derive image from HEAD (DS~B f875bc854 spec, C3 id -> :25558d98) + re-run derive -> collision-safe C3 node_id live. CVO~B re-cert.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | rebuild derive image from HEAD (f875bc854 spec baked) -> ECR opal-globgrph-derive-runner:latest new digest | CodeBuild SUCCEEDED + ECR :latest NEW digest (Rule 22a live ECR) | CodeBuild c6d83dc7-5523-4497-9ff6-9ffb2d08fd0b SUCCEEDED; zip git-archive HEAD (15 paths, spec baked carries C3 id system:firm-conditional-display:25558d98 verified in zip); ECR :latest NEW digest sha256:c98f48bf760681a5eba88ba26f683429676e6904ec62d1b604c85c61b7f194bf tag 20260708-185712 (Rule 22a live ECR, != prior b76cefe6) | CLOSED 20260708T185845Z |
| R2 | activation | re-derive (ecs run-task globgrph-derive-runner) -> C3 id :25558d98 materialized, full-overwrite replaces old id | task exit=0 + CloudWatch C2C3_MOTIF_INGEST nodes=7 edges_formed=36 edges_unresolved=0 + NESSIE_COMMIT + MARKER_STAMPED | ecs run-task efb3a9f0a3164c0781ff6345e97a43e1 STOPPED exit=0; CloudWatch: C2C3_MOTIF_INGEST nodes=7 (C2Motif=6 C3System=1) edges_formed=36 edges_unresolved=0; NODE_TYPE_LAYER relabel all-mapped (no UNCATEGORIZED); NESSIE_COMMIT ts=1783537150561; MARKER_STAMPED writer=derive_runner hash=f647120374.. nodes_snap=4903851074698690533 | CLOSED 20260708T191120Z |
| R3 | verify | comp-kuzu round-trip: new C3 id live + no orphan of old id | C3System node_id=system:firm-conditional-display:25558d98 present, OLD system:firm-conditional-display ABSENT, 3 C3->C2 + 33 C2->C1 resolve (36 CONTAINS) | comp-kuzu HEAD:current (re-finalized on the re-derive HEAD-advance, marker f647120374/nodes_snap 4903851074698690533): NEW C3 node_id system:firm-conditional-display:25558d98 PRESENT (count=1); OLD bare system:firm-conditional-display ABSENT (count=0, no orphan -- clean full-overwrite REPLACE); C3System_total=1, C2Motif=6, nodes_semctl=7, CONTAINS_semctl=36. CVO~B acceptance bar met. | CLOSED 20260708T191931Z |

## Log

- 20260708T185601Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260708T185845Z LEG R1 closed: CodeBuild c6d83dc7-5523-4497-9ff6-9ffb2d08fd0b SUCCEEDED; zip git-archive HEAD (15 paths, spec baked carries C3 id syste
- 20260708T191120Z LEG R2 closed: ecs run-task efb3a9f0a3164c0781ff6345e97a43e1 STOPPED exit=0; CloudWatch: C2C3_MOTIF_INGEST nodes=7 (C2Motif=6 C3System=
- 20260708T191931Z LEG R3 closed: comp-kuzu HEAD:current (re-finalized on the re-derive HEAD-advance, marker f647120374/nodes_snap 4903851074698690533): N
- 20260708T191931Z CLOSED -- all 3 legs proven
