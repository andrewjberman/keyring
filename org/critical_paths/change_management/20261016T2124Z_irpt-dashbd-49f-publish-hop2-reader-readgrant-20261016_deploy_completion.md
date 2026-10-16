# Deploy Completion Record
**Date opened:** 2026-10-16T21:24:12.145404+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-312: 49 Financial reporting-publish function irpt-49f-reporting-publish-lambda: ONE new bundle version (build-only hash s/OKOv98j..), plan 0 add 2 change 0 destroy (function code attributes and the role policy two statements: READ and LIST of the filled-report gold prefix), ONE safe-apply, the switch-OFF probe (exact no-op), ONE dry-run shard, the after-read; bound to the signed packet sha256 e6af7a92148d (COO half @a30664edac, CTO half @6aaa28e481); the filled-report switch stays OFF; rollback: prior artifact version 41lfCmfJWyvHbzqC3VtGeHVm6VJ4gRZb and the prior locals.tf through safe-apply; nothing deleted; no schedule change
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | source-map entry artifact_sha256 for irpt-49f-reporting-publish-lambda plus this ledger sentinel, committed with explicit paths | commit ids recorded |  | OPEN |
| L2 | s3-prefix | artifact key investor-reporting/irpt-reporting-publish-lambda.zip in opal-313476888478-lambda-artifacts: a NEW VERSION (current 41lfCmfJWyvHbzqC3VtGeHVm6VJ4gRZb is the rollback target) | new VersionId, landed sha256 equals the built zip equals s/OKOv98j53aFJCLrBpYP8xh3oUcuWagn0vSHVBjhIM= |  | OPEN |
| L3 | tf-lambda | ONE safe-apply of infra/aws/terraform/investor-reporting/reporting-publish plan exactly 0 add 2 change 0 destroy: the function by code attributes and aws_iam_role_policy.irpt_reporting_publish (two statements) | plan counts, naming gate, code hash equals the built zip, six of eight statements byte-identical, schedules ENABLED untouched, post-apply plan No changes |  | OPEN |
| L4 | verify | the switch-OFF probe {filled_report true}: the answer is exactly enabled false, clients 0, written 0, not_available [], refused [] | exact answer, within 819 MB and 240 s |  | OPEN |
| L5 | verify | ONE dry-run shard {dry_run true, shard 0, shards 7}: ok, about 990 accounts, 0 refused | ok true, refused_count 0, within 819 MB and 240 s, platinum counts unchanged |  | OPEN |
| L6 | verify | the after-read and the receipt | after, platinum_after and the record written, three criteria run |  | OPEN |

## Log

- 20261016T212412Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
