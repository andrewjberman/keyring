# Deploy Completion Record
**Date opened:** 2026-10-08T22:06:21.925105+00:00
**Status:** OPEN
**Deploy:** IB-pr-374 Performance client statement writer release at pin 9238309eca (irpt-export-render, five members, function only, no route); rollback source version LefrKSE11JIR93JOh.1RP5cSIUrqKfI_ (PbyqmHBQ...)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~182
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-export-render | tf-lambda | module.irpt_export_render.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | start CodeSha256 PbyqmHBQpr4DC76qt0noBfoqKVleydNaJ7s2qsx5mT0= (rollback source s3 version LefrKSE11JIR93JOh.1RP5cSIUrqKfI_); census changed_members=5 at pin 9238309eca; replay committed a5eeec04a4 (ANALYSIS+PERFORMANCE under irpt-x10-v1, live==built a7a8ae481b97 and 04afa6c7a36a, negative control refused by both, suites 24+9+21); built == packet rNjtTwcmhpNdHUV7VcO1cRPcC1wHaANm1oIP+Xvf6Ek= uploaded at version WiLXOyzMQ8_U42fSAeTIOwyMyw9.A9X3 (0c4a8bf984); plan text 168a193c96 (0 add, 1 change, 0 destroy); safe-apply: Apply complete! Resources: 0 added, 1 changed, 0 destroyed; live CodeSha256 rNjtTwcmhpNdHUV7VcO1cRPcC1wHaANm1oIP+Xvf6Ek= == built, re-plan No changes, census changed_members=0; deploy recorded 3dfc5387bb; function only, route and api root not touched | CLOSED 20261008T221333Z |

## Log

- 20261008T220621Z OPENED by 0.9.0_WK_IRPT_BCKEND~182 with 1 leg(s)
- 20261008T221333Z LEG irpt-export-render closed: start CodeSha256 PbyqmHBQpr4DC76qt0noBfoqKVleydNaJ7s2qsx5mT0= (rollback source s3 version LefrKSE11JIR93JOh.1RP5cSIUrqKf
