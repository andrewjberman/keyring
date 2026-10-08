# Deploy Completion Record
**Date opened:** 2026-10-08T20:40:35.248547+00:00
**Status:** CLOSED -- STOPPED at step 5; activation and publish NOT performed (issuer107262)
**Deploy:** Fabric overlay worker-only image. BEFORE all seven families pinned digest17ccc9b01855138e2abd0c36938c62a21ffd0730bf7886b9758a5317b4d24d04: derive9, serving4, cse4, comp-learns4, fedobs4, resource-summaries4, worker6. Live service/rule/scheduler references saved consumer-pins-before.json. Pointer SHA2567d8160ec6b8fe37c3ac84c081ac8d4de55e5f42de02b5f2d709efbb8e1c19a14 LastModified2026-10-08T12:55:07Z exact current-before.json. Request b337c560da CTO1d61e96831 COO0b0180e42a. Worker16GiB; measured full RSS6140MiB; 985+240=1225s below3600s. Rollback worker GLOBGRPH_FABRIC_OVERLAY=0, prior digest, or exact saved pointer; no vintage deletes.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| I1 | activation | build one shared image and preserve six nonworker digests | CodeBuild success and exact digest | CodeBuild de95c779-1f3e-4fee-9949-d00e69870cdc SUCCEEDED source5c625a6b9fe80bd2d5635662a7dcda595a6d9a21 includes overlay78e2e7b0b7; digestd3037f32c0143855a283f5e997fa83d8f09fc23755608c190896ab0adfd3f3b1. Six nonworker families already pinned immutable prior digest; exact consumer references saved. | CLOSED 20261008T204542Z |
| W1 | activation | worker definition and its Pipe revision binding only | safe-apply and live digest/pointer references | CANCELLED by issuer107262 after pre-apply refusal; no success claimed | STOPPED |
| V1 | verify | next projection publish and served FabricNode | fabric_node_count positive node_count295xx newer VINTAGE six nonworker digests unchanged | CANCELLED by issuer107262 after pre-apply refusal; no success claimed | STOPPED |

## Log

- 20261008T204035Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20261008T204542Z LEG I1 closed: CodeBuild de95c779-1f3e-4fee-9949-d00e69870cdc SUCCEEDED source5c625a6b9fe80bd2d5635662a7dcda595a6d9a21 includes overlay

- 2026-10-08T20:49Z issuer107256 HOLD step5 pending CTO naming ruling. Nothing landed in the worker/task families, Pipe or projection pointer: safe-apply refused before mutation. Image build DID land and shared latest tag moved; seven task families all reference saved immutable digest. W1/V1 remain OPEN. No family rename.

- 2026-10-08T20:51Z CLOSED -- STOPPED by issuer107262, CTO ruling107259(a). Safe-apply naming gate refused existing family replacement. All seven families/Pipe/pointer unchanged (stop-readback.json). Image built/tag moved but ZERO families reference tags. New GO and fresh ledger required after naming fix. No rename/no bypass.
