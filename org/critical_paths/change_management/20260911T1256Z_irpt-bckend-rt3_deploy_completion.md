# Deploy Completion Record
**Date opened:** 2026-09-11T12:56:40.307279+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T131235Z
**Deploy:** IRPT_BCKEND IB-rt-3: rebuild the irpt-common layer to carry the ONE opaque-id normalizer (_ids) and re-apply the performance and narrative roots onto the new layer version
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of _ids, the moved call sites and the layer build script | hash on the worker branch | commit 6806f529ac2c63ad8c9bd902127b654cdf758d06 on wk-irpt_bckend-2-1: _ids/{ids.py,raw_keys.json,tests/test_ids.py}, directory_runner.py + holdings_snapshot.py moved onto the normalizer (0 grammar occurrences remain in either), _scope/resolve.py shape check onto _ids.is_issued, build_layer.py carrying _ids; commit-gate rc=0 on every .py; suites green (_ids 29, _scope 50, _authz 27, directory 37, performance 28, narrative 37, ops 34, _gate 20, _keys 45, export 33, gold 42) | CLOSED 20260911T130002Z |
| L2 | s3-prefix | opal-313476888478-lambda-layers irpt-common.zip | the build_layer.py output line with the zip sha256 | build_layer.py rc=0: 'zip irpt-common.zip -- 157 member(s), 631060 bytes, sha256(base64)=ZvfLP5IwnaROdfP0nplUZxzci13k2A8b3Abd/pmJ+2Q='; the three _ids members staged from the COMMITTED blob @6806f529ac (registry @1f54e16dfd); s3api put-object + head-object read back Size=631060 Metadata.content-sha256=ZvfLP5IwnaROdfP0nplUZxzci13k2A8b3Abd/pmJ+2Q= VersionId=bwKPk9Na5PlyzMEaowNIMZ1ik2WCoqLR; python/ids.py and python/raw_keys.json verified BYTE-EQUAL to the committed blobs (14173 and 5990 bytes) | CLOSED 20260911T130002Z |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/performance (publishes irpt-common:3) and narrative | safe-apply Apply complete line with the resource count | safe-apply rc=0 x2: performance 'Apply complete! Resources: 1 added, 1 changed, 1 destroyed.' (publishes irpt-common:5, moves irpt-performance-adapter onto it); narrative 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' (moves irpt-narrative onto :5). The zip published is the UNION build: a strict superset of the live :4 -- 0 members regressed, exactly python/ids.py and python/raw_keys.json added, 0 common members differing -- because a CONCURRENT cell had published :3/:4 while this cell built (row W1-S12) | CLOSED 20260911T131235Z |
| L4 | verify | get-layer-version on irpt-common + both functions' Layers ARN + 0-diff plans | the read output, 2 of 2 functions on the new version | get-layer-version irpt-common:5 CodeSha256=ZUcsQUOsc3lT2cKlnur5rCAZc/a0rCkKvU5pjg11U20= Size=644526 -- EQUALS the built zip's sha256 (content, never filename); get-function-configuration Layers[].Arn = layer:irpt-common:5 for irpt-performance-adapter AND irpt-narrative (2 of 2); terraform plan on both roots: 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260911T131235Z |

## Log

- 20260911T125640Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 4 leg(s)
- 20260911T130002Z LEG L1 closed: commit 6806f529ac2c63ad8c9bd902127b654cdf758d06 on wk-irpt_bckend-2-1: _ids/{ids.py,raw_keys.json,tests/test_ids.py}, di
- 20260911T130002Z LEG L2 closed: build_layer.py rc=0: 'zip irpt-common.zip -- 157 member(s), 631060 bytes, sha256(base64)=ZvfLP5IwnaROdfP0nplUZxzci13k2A8
- 20260911T131235Z LEG L3 closed: safe-apply rc=0 x2: performance 'Apply complete! Resources: 1 added, 1 changed, 1 destroyed.' (publishes irpt-common:5, 
- 20260911T131235Z LEG L4 closed: get-layer-version irpt-common:5 CodeSha256=ZUcsQUOsc3lT2cKlnur5rCAZc/a0rCkKvU5pjg11U20= Size=644526 -- EQUALS the built 
- 20260911T131235Z CLOSED -- all 4 legs proven
