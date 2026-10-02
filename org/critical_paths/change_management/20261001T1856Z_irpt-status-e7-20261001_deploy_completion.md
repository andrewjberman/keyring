# Deploy Completion Record
**Date opened:** 2026-10-01T18:56:46.248951+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T112211Z
**Deploy:** irpt-status whole bundle at CLOUD b1db201025 for E7 (CTO rulings batch 98, 100): the owned request read serves the chosen comparisons' names; never-widen packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | re-pin the irpt-status source-map row to the pin, build-and-upload, read the uploaded object back by version | artifact sha256 and S3 version; downloaded by version, hash equal; census against the live function | built at b1db201025 (build_irpt-status.txt); s3 opal-313476888478-lambda-artifacts/investor-reporting/irpt-status.zip version gqIQUc_Z0srcda_A1CGybmGZSXzTowjW downloaded BY VERSION 2026-10-02 ~02:3xZ: sha256 iYgp83014ZjXiXxdgcBnvme/QooX4aIlUh8C5C7LTVI= equal, 327801 bytes, 45 members, owned_requests.py and durable_job.py byte-equal to git show b1db201025; census vs live 2V7xV1..: 43 identical, 2 changed, 0 added, 0 removed (E7_STATUS/census_irpt-status.json) | CLOSED 20261002T024516Z |
| D1 | verify | ONE targeted safe-apply of module.irpt_status.aws_lambda_function.this after both halves | apply output; CodeSha256 equals the built hash; a re-plan of the same target reads no changes | SUPERSEDED by irpt-status-e7b-20261002 (CTO batches 142, 146, 148): E7's artifact gqIQUc_Z was never applied; E7b's bundle Jg3uJ0x7 (X/JLmPJZ) applied 2026-10-02T11:13:50Z carries E7's _chosen_comparisons byte-identical behind include=comparisons, so row S261's parser gate no longer applies; nothing of E7 was served | CLOSED 20261002T112211Z |
| V1 | verify | served read-back: the request read of REQ-a1d9abc0 as the service principal names both comparisons; the Overview REQ-a69e5751 reads []; status and sections routes unchanged | the route outputs, read for values before commit | SUPERSEDED by irpt-status-e7b-20261002 (CTO batches 142, 146, 148): E7's artifact gqIQUc_Z was never applied; E7b's bundle Jg3uJ0x7 (X/JLmPJZ) applied 2026-10-02T11:13:50Z carries E7's _chosen_comparisons byte-identical behind include=comparisons, so row S261's parser gate no longer applies; nothing of E7 was served | CLOSED 20261002T112211Z |

## Log

- 20261001T185646Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261002T024516Z LEG U1 closed: built at b1db201025 (build_irpt-status.txt); s3 opal-313476888478-lambda-artifacts/investor-reporting/irpt-status.zip ve
- 20261002T024516Z HELD-SOVEREIGN-GATED gate=external/row IRPT_BCKEND-S261: the deployed page parser (portal owned-requests.ts readOwn
- 20261002T112211Z HOLD RELEASED -> OPEN
- 20261002T112211Z LEG D1 closed: SUPERSEDED by irpt-status-e7b-20261002 (CTO batches 142, 146, 148): E7's artifact gqIQUc_Z was never applied; E7b's bund
- 20261002T112211Z LEG V1 closed: SUPERSEDED by irpt-status-e7b-20261002 (CTO batches 142, 146, 148): E7's artifact gqIQUc_Z was never applied; E7b's bund
- 20261002T112211Z CLOSED -- all 3 legs proven
