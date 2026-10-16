# Deploy Completion Record
**Date opened:** 2026-10-16T22:39:33.918689+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-f-2204: 49 Financial reporting-gold function irpt-49f-reporting-gold-lambda: ONE new bundle version (build-only hash SCt7IgN3..), plan 0 add 2 change 0 destroy (function code attributes and the role policy: ONE write resource arn:aws:s3:::opal-data-49financial/irpt/49financial/gold/account_transaction/* added last to WriteTheFiveGoldPrefixesOnly), ONE safe-apply, a transaction-only DRY RUN of one day (writes nothing), the CTO's 720 s time trigger, the first one-day WRITE and a bounded 25-day RANGE at the new prefix; bound to the signed packet sha256 b67bd4ad57f2 (COO half signed and countersigned, CTO half @6b6c16b492); rollback: artifact version 00dm6f4.vFnWIiIuxVafNVtxIh0zAEeh and the prior locals.tf through safe-apply; schedule untouched; nothing deleted; the ledger STAYS OPEN for leg L7 (the first scheduled fire, read by the issuer)
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 80.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | source-map entry artifact_sha256 for irpt-49f-reporting-gold-lambda plus this ledger sentinel, committed with explicit paths | commit ids recorded |  | OPEN |
| L2 | s3-prefix | artifact key investor-reporting/irpt-reporting-gold-lambda.zip in opal-313476888478-lambda-artifacts: a NEW VERSION (current 00dm6f4.vFnWIiIuxVafNVtxIh0zAEeh is the rollback target) | new VersionId, landed sha256 equals the built zip equals SCt7IgN3A+SXxfn8cv0QHVnhjVMmHXePihA6MnPm2nQ= |  | OPEN |
| L3 | tf-lambda | ONE safe-apply of infra/aws/terraform/investor-reporting/reporting-gold plan exactly 0 add 2 change 0 destroy: the function by code attributes and aws_iam_role_policy.irpt_reporting_gold (the one new write resource) | plan counts, naming gate, code hash equals the built zip, ten statements byte-identical, write statement seven resources, schedule untouched, post-apply plan No changes |  | OPEN |
| L4 | verify | transaction-only DRY RUN of one day: ok, stages transaction, one day with a positive count, none failed, writes nothing | status 200, 0 objects at the new prefix, within 6553 MB and 720 s |  | OPEN |
| L5 | s3-prefix | the first one-day WRITE (same event without dry_run) at the new prefix account_transaction | one partition, 19 columns, schema hash equal, claims and flow classes valid, same count as the dry run |  | OPEN |
| L6 | s3-prefix | a bounded RANGE of the 25 most recent trading days at the new prefix | days written equal partitions after, the six other tables unchanged |  | OPEN |
| L7 | verify | the first scheduled fire after the apply, read by the issuer (this ledger STAYS OPEN for it) | issuer read |  | OPEN |

## Log

- 20261016T223933Z OPENED by 0.7.0_AE_CloudOps~IB2 with 7 leg(s)
