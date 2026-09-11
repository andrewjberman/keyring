# Deploy Completion Record
**Date opened:** 2026-09-11T12:56:40.307279+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rt-3: rebuild the irpt-common layer to carry the ONE opaque-id normalizer (_ids) and re-apply the performance and narrative roots onto the new layer version
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of _ids, the moved call sites and the layer build script | hash on the worker branch |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-layers irpt-common.zip | the build_layer.py output line with the zip sha256 |  | OPEN |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/performance (publishes irpt-common:3) and narrative | safe-apply Apply complete line with the resource count |  | OPEN |
| L4 | verify | get-layer-version on irpt-common + both functions' Layers ARN + 0-diff plans | the read output, 2 of 2 functions on the new version |  | OPEN |

## Log

- 20260911T125640Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 4 leg(s)
