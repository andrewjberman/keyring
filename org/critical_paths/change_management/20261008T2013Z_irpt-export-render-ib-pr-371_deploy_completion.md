# Deploy Completion Record
**Date opened:** 2026-10-08T20:13:00.460923+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T202030Z
**Deploy:** IB-pr-370 E9 release at pin 0a57f3c0e9 (irpt-export-render, five members); rollback source version fHVzTZi4vdHmRqcy0KK1hmrQ_dcT1QkO (idanP8nX...)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~179
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-export-render | tf-lambda | module.irpt_export_render.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | start CodeSha256 idanP8nX/mqaQ+FIGGY6AT4Xe/JxckOM3N0rWwivSh8= (rollback source s3 version fHVzTZi4vdHmRqcy0KK1hmrQ_dcT1QkO); census changed_members=5 at pin 0a57f3c0e9; replay committed 9082fb60e0 (ANALYSIS+PERFORMANCE under irpt-x10-v1, live==built a7a8ae481b97, negative control refused by both, suites 24+9+21); built == packet PbyqmHBQpr4DC76qt0noBfoqKVleydNaJ7s2qsx5mT0= uploaded at version LefrKSE11JIR93JOh.1RP5cSIUrqKfI_ (0e66fa3e31); plan text 20f0b26299 (0 add, 1 change, 0 destroy); safe-apply: Apply complete! Resources: 0 added, 1 changed, 0 destroyed; live CodeSha256 PbyqmHBQpr4DC76qt0noBfoqKVleydNaJ7s2qsx5mT0= == built, re-plan No changes, census changed_members=0; deploy recorded 9abd05a403 | CLOSED 20261008T202030Z |

## Log

- 20261008T201300Z OPENED by 0.9.0_WK_IRPT_BCKEND~179 with 1 leg(s)
- 20261008T202030Z LEG irpt-export-render closed: start CodeSha256 idanP8nX/mqaQ+FIGGY6AT4Xe/JxckOM3N0rWwivSh8= (rollback source s3 version fHVzTZi4vdHmRqcy0KK1hmrQ_dcT1Q
- 20261008T202030Z CLOSED -- all 1 legs proven
