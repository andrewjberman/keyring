# Session S: NFRA_CLDGRPH round-3 worker revision 3

**Seat:** `0.7.0_AE_CloudOps~S`  
**Order:** `NFRA_CLDGRPH.TO-CG-C-2`  
**Owned cells:** `CG-s-2`, `CG-s-3`  
**Window:** 2026-09-03 18:40-19:15Z

## Outcome

Revision-3 source commit `a38c0437eb1c6207040c99361f302d7676085321` replaced the cross-mode publication band with exact set/byte/hash/direct-count integrity, retained compaction and conditional/forward-only publication, re-derived the engine default deadline to 3600 seconds from the 835-second accepted maximum, and stamped task revision 3. Focused tests passed 12/12; the combined suite passed 19/19; Terraform validation and commit gates passed.

CodeBuild `globgrph-derive-build:efc258e6-713c-47ae-ba79-fa2e691e0d0e` succeeded from HEAD `649164d75bc96b7c9f3001a9342108a5852ad0a2`, containing the C2 commit. ECR `latest` resolved to `sha256:68bd8b932689a331928c1c3a6cc00fe124d24e04e7a9b64ba008f1a2d3de10e8`. A scoped safe-apply registered `globgrph-projection-worker:3` and retargeted the RUNNING Pipe. The unscoped post-apply plan named only the three known Glue partitions and the known SNS email subscription; no C2 address remained. Fresh IAM census counted 221 roles.

## Authentic run

At 18:59:49-53Z the seat re-PUT the bucket's existing six-tag set unchanged. CloudTrail event `675113f0-3085-4734-b459-43654615c6ce` entered the real incremental chain. Lambda request `ce77d595-65da-5b36-a749-b686a038ff26` wrote one node and stamped marker `2026-09-03T19:02:18.412096+00:00`. Pipe execution `358ac19b-d1f7-4d0c-9c92-489e358e3e1c` launched task `f8b288ad95ec42dab2d17ef5a33cbd29` on revision 3/digest `68bd...`.

The task exited 0. It incrementally refreshed 3 node upserts/1 delete and no edge delta, yielding 27,225 nodes and 58,606 edges. It compacted 83,615,744 bytes to 34,824,192, read the published DB back, matched direct counts and manifest declarations, logged `POINTER_VERIFY_OK`, then `POINTER_PUT_OK`. The pointer advanced from vintage `2026-09-03T17:01:08.128628+00:00` to `2026-09-03T19:02:18.412096+00:00`. C1 peer `~T` was immediately sent both vintages and the task id.

The prefix contained exactly two objects. Manifest: 1,540 bytes, SHA-256 `751b870534c474298e0e968390f143e325b4741a4a4fc471c3bf341cd39c0b58`. Database: 34,824,192 bytes, SHA-256 `29a3ded43743baa46a3ed8c399dc1d672eb385ab286c1cf2cca5d8c35f551116`. Both independent streamed hashes matched declarations.

## Controls

- Same-vintage identity task `842093d9e6874ebca80f4ad8b495be1a` exited 0 with `POINTER_VERIFY_OK` then `POINTER_NOOP`; pointer ETag and LastModified did not change.
- Non-identical task `fd3d9ea9afdc46749ab7b84fcf77d16f` invoked the deployed conditional-create helper against the real existing manifest with a two-byte different candidate. `If-None-Match: *` prevented overwrite; it logged `IMMUTABLE_REFUSED`, caught the expected `PublicationRefused`, and exited 0. Manifest and pointer ETags/LastModified did not change.
- Local caller with `KUZU_REBUILD_DEADLINE_S` absent reported `3600 source=measured-default` and exited 0.
- Deployed task `bd842c7582a840f0aa0fe10541149784` inherited the task definition's explicit env and reported `3600 source=environment`; it exited 0.

The seven-leg deployment ledger `cldgrph-cgc2-worker-revision3` closed 7/7 through `.tools/deploy_ledger.py`, rendered `CLOSED -- nothing stranded`, and removed its sentinel. No serving/gateway/client/deriver surface, marker, peer-owned contract file, or foreign Terraform address was changed. No push occurred.

