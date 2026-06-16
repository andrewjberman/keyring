# Deploy Completion Record
**Date opened:** 2026-06-16T18:35:53.129000+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260616T183815Z
**Deploy:** YANG_SITTW.TO-1 MDPF 1c/SMA collapse -- re-emit served aggregate-aua-timeseries (never-widen co-signed CTO+COO)
**Authored by:** 0.4.0_DS_ClientPlatform
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit 935d3ba79 (build_aggregate_aua_timeseries.py 1c/SMA collapse) already on origin/CLOUD via shared push | hash on origin/CLOUD | 935d3ba79 on origin/CLOUD (ancestor of b2cd5138d; git diff origin/CLOUD HEAD on file = empty; fold fn present in origin version) | CLOSED 20260616T183814Z |
| L2 | s3-prefix | opal-data-mdpf code/scripts/backfill -- runner code copy (DURABILITY: next nightly Stage-4 must run new code, not revert) | aws s3 cp ETag | s3://opal-data-mdpf/code/scripts/backfill/build_aggregate_aua_timeseries.py ETag 818d30493b7e03acdfabde48f7367e1b LastModified 2026-06-16T18:36:24Z; deployed runner code _fold_sma_into_nonmodel present (durable -- next nightly Stage-4 runs new code) | CLOSED 20260616T183814Z |
| L3 | activation | re-emit served json/mdpf/{global,49financial,inflection}/aggregate-aua-timeseries.json + platinum mirrors via producer --upload | producer --upload OK lines | producer --upload OK: 7 puts (platinum+json x global/49financial/inflection + non-sliced global) all rc=0, no AccessDenied; deployed mtime 2026-06-16T18:37:13Z | CLOSED 20260616T183814Z |
| L4 | verify | Phase-3 served-verify: $0 TOTAL + combined-Non-Model-band movement on DEPLOYED artifact, sma_aua gone, mtime>commit (CTO+COO never-widen binding AC) | deployed-vs-before diff | Phase-3 served-verify on DEPLOYED artifact: TOTAL/model/combined-Non-Model-band = $0.0000 movement all 413 dates x 3 slices (global/49f/inflection) vs pre-deploy before; sma_aua absent; by_model identical; dates identical; mtime 18:37:13Z > commit 18:26Z. CTO+COO never-widen binding AC SATISFIED on deployed result | CLOSED 20260616T183814Z |

## Log

- 20260616T183553Z OPENED by 0.4.0_DS_ClientPlatform with 4 leg(s)
- 20260616T183814Z LEG L1 closed: 935d3ba79 on origin/CLOUD (ancestor of b2cd5138d; git diff origin/CLOUD HEAD on file = empty; fold fn present in origin 
- 20260616T183814Z LEG L2 closed: s3://opal-data-mdpf/code/scripts/backfill/build_aggregate_aua_timeseries.py ETag 818d30493b7e03acdfabde48f7367e1b LastMo
- 20260616T183814Z LEG L3 closed: producer --upload OK: 7 puts (platinum+json x global/49financial/inflection + non-sliced global) all rc=0, no AccessDeni
- 20260616T183814Z LEG L4 closed: Phase-3 served-verify on DEPLOYED artifact: TOTAL/model/combined-Non-Model-band = $0.0000 movement all 413 dates x 3 sli
- 20260616T183815Z CLOSED -- all 4 legs proven
