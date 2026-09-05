# Deploy Completion Record
**Date opened:** 2026-09-03T18:49:23.655427+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260903T190944Z
**Deploy:** NFRA_CLDGRPH CG-s-2/3 worker revision 3 remediation
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | opal-globgrph-derive-runner revision-3 image | CodeBuild SUCCEEDED and exact ECR digest/source commit recorded | CodeBuild globgrph-derive-build:efc258e6-713c-47ae-ba79-fa2e691e0d0e SUCCEEDED; source HEAD 649164d75bc96b7c9f3001a9342108a5852ad0a2 containing C2 a38c0437eb; ECR opal-globgrph-derive-runner:latest digest sha256:68bd8b932689a331928c1c3a6cc00fe124d24e04e7a9b64ba008f1a2d3de10e8, image size 131519853 bytes. | CLOSED 20260903T185212Z |
| L2 | activation | globgrph-projection-worker task definition revision 3 and Pipe retarget | targeted safe-apply result and applied task/Pipe ARNs | Targeted safe-apply of aws_ecs_task_definition.projection_worker, aws_iam_role_policy.projection_pipe, and aws_pipes_pipe.projection_worker completed: 1 added, 2 changed, 1 destroyed (revision replacement). Applied ECS arn arn:aws:ecs:us-east-1:313476888478:task-definition/globgrph-projection-worker:3 ACTIVE; Pipe RUNNING targets :3; applied Pipe IAM RunTask resource is :3. | CLOSED 20260903T185651Z |
| L3 | verify | Terraform scope and applied identity | one unscoped re-plan names exact four foreign addresses and no C2 address; applied task override remains 3600 seconds | Post-apply unscoped plan names exactly aws_glue_partition.tool_activity[rolling_log], [rolling_log_summary], [routing], and aws_sns_topic_subscription.critical_surface_alerts_email; no C2 address. Fresh comp-iam census 2026-09-03T18:55:16Z: 221 roles; projection worker 2 inline/4 statements/0 attached; applied Pipe IAM targets task definition :3. Applied task env retains PROJECTION_DEADLINE_SECONDS=3600 and KUZU_REBUILD_DEADLINE_S=3600. | CLOSED 20260903T185651Z |
| L4 | verify | authentic strictly-forward publisher advance | real stamp task id plus verify-before-PUT logs and before/after pointer vintages | Authentic PutBucketTagging event 675113f0-3085-4734-b459-43654615c6ce at 2026-09-03T18:59:54Z flowed through incremental Lambda request ce77d595-65da-5b36-a749-b686a038ff26, marker vintage 2026-09-03T19:02:18.412096+00:00, Pipe execution 358ac19b-d1f7-4d0c-9c92-489e358e3e1c, and rev-3 ECS task f8b288ad95ec42dab2d17ef5a33cbd29 exit 0. Worker logged POINTER_VERIFY_OK then POINTER_PUT_OK. Pointer advanced strictly from 2026-09-03T17:01:08.128628+00:00 to 2026-09-03T19:02:18.412096+00:00. | CLOSED 20260903T190943Z |
| L5 | verify | same-vintage conditional-create controls on running image | byte-identical no-op and non-identical refusal with real objects preserved | Same-vintage byte-identical task 842093d9e6874ebca80f4ad8b495be1a on rev 3 exited 0, logged POINTER_VERIFY_OK and POINTER_NOOP, and left pointer ETag 7b16c2239928aaa255808d6080ff19b2 / LastModified 19:02:50Z unchanged. Non-identical running-image seam task fd3d9ea9afdc46749ab7b84fcf77d16f used IfNoneMatch=* against the existing manifest, logged IMMUTABLE_REFUSED plus EXPECTED_COLLISION_REFUSAL, exited 0, and left manifest ETag d66b9b358248d49352149a264e2ae610 / LastModified 19:02:49Z and pointer unchanged. | CLOSED 20260903T190943Z |
| L6 | verify | compacted incremental integrity publication | real incremental task id; direct counts, exact sizes and SHA-256 match; pointer advanced | Real incremental task f8b288ad95ec42dab2d17ef5a33cbd29 compacted 83615744 to 34824192 bytes, reclaiming 48791552, then published exact two-object prefix projection/2026-09-03T19:02:18.412096+00:00/: manifest 1540 bytes and kuzu_nessie_db 34824192 bytes. Streamed SHA256 values match declarations: artifact 29a3ded43743baa46a3ed8c399dc1d672eb385ab286c1cf2cca5d8c35f551116, manifest/pointer 751b870534c474298e0e968390f143e325b4741a4a4fc471c3bf341cd39c0b58. POINTER_VERIFY_OK proves direct Kuzu counts nodes=27225, edges=58606 before pointer advance. | CLOSED 20260903T190943Z |
| L7 | verify | measured rebuild deadline callers | inherited 3600-second default and explicit deployed 3600-second override both observed | Inheriting local invocation with KUZU_REBUILD_DEADLINE_S unset exited 0 and reported KUZU_REBUILD_DEADLINE_S=3600 source=measured-default. Deployed-image explicit caller task bd842c7582a840f0aa0fe10541149784 on task definition rev 3 exited 0 and logged KUZU_REBUILD_DEADLINE_S=3600 source=environment. Applied task definition retains KUZU_REBUILD_DEADLINE_S=3600 and PROJECTION_DEADLINE_SECONDS=3600. | CLOSED 20260903T190943Z |

## Log

- 20260903T184923Z OPENED by 0.7.0_AE_CloudOps~S with 7 leg(s)
- 20260903T185212Z LEG L1 closed: CodeBuild globgrph-derive-build:efc258e6-713c-47ae-ba79-fa2e691e0d0e SUCCEEDED; source HEAD 649164d75bc96b7c9f3001a93421
- 20260903T185651Z LEG L2 closed: Targeted safe-apply of aws_ecs_task_definition.projection_worker, aws_iam_role_policy.projection_pipe, and aws_pipes_pip
- 20260903T185651Z LEG L3 closed: Post-apply unscoped plan names exactly aws_glue_partition.tool_activity[rolling_log], [rolling_log_summary], [routing], 
- 20260903T190943Z LEG L4 closed: Authentic PutBucketTagging event 675113f0-3085-4734-b459-43654615c6ce at 2026-09-03T18:59:54Z flowed through incremental
- 20260903T190943Z LEG L5 closed: Same-vintage byte-identical task 842093d9e6874ebca80f4ad8b495be1a on rev 3 exited 0, logged POINTER_VERIFY_OK and POINTE
- 20260903T190943Z LEG L6 closed: Real incremental task f8b288ad95ec42dab2d17ef5a33cbd29 compacted 83615744 to 34824192 bytes, reclaiming 48791552, then p
- 20260903T190943Z LEG L7 closed: Inheriting local invocation with KUZU_REBUILD_DEADLINE_S unset exited 0 and reported KUZU_REBUILD_DEADLINE_S=3600 source
- 20260903T190944Z CLOSED -- all 7 legs proven
