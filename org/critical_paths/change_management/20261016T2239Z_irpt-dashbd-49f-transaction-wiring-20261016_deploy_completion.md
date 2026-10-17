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
| L1 | git | source-map entry artifact_sha256 for irpt-49f-reporting-gold-lambda plus this ledger sentinel, committed with explicit paths | commit ids recorded | source-map commit 4b2fcc823f (artifact_sha256 only: SCt7IgN3.. replaces JNTOivgN..); script and state committed with it | CLOSED 20261016T225715Z |
| L2 | s3-prefix | artifact key investor-reporting/irpt-reporting-gold-lambda.zip in opal-313476888478-lambda-artifacts: a NEW VERSION (current 00dm6f4.vFnWIiIuxVafNVtxIh0zAEeh is the rollback target) | new VersionId, landed sha256 equals the built zip equals SCt7IgN3A+SXxfn8cv0QHVnhjVMmHXePihA6MnPm2nQ= | build-only sha256 SCt7IgN3A+SXxfn8cv0QHVnhjVMmHXePihA6MnPm2nQ= equals the packet; import smoke rc 0 and AT49_IMPORT_ERROR None (24 members incl handler.py, account_transaction.py and transaction_words.json); real upload landed NEW VersionId NeB6JJ_0Qy72SG3LgV7nWjOs0keBl0oy (before 00dm6f4.vFnWIiIuxVafNVtxIh0zAEeh kept as rollback); landed bytes sha256 equal the built zip 482b7b22 | CLOSED 20261016T225715Z |
| L3 | tf-lambda | ONE safe-apply of infra/aws/terraform/investor-reporting/reporting-gold plan exactly 0 add 2 change 0 destroy: the function by code attributes and aws_iam_role_policy.irpt_reporting_gold (the one new write resource) | plan counts, naming gate, code hash equals the built zip, ten statements byte-identical, write statement seven resources, schedule untouched, post-apply plan No changes | plan 0 add 2 change 0 destroy (aws_iam_role_policy.irpt_reporting_gold gains the one write resource account_transaction in WriteTheFiveGoldPrefixesOnly, as a set per the amendment; the function: last_modified, s3_object_version 00dm6f4..->NeB6JJ_.., source_code_hash JNTOivgN..->SCt7IgN3..); naming gate not yet run; ONE safe-apply 22:53:49Z-22:55:48Z Apply complete 0/2/0; function CodeSha256 SCt7IgN3.. memory 8192 timeout 900 no reserved concurrency one layer no env; only the write statement differs, seven resources; schedule ENABLED untouched; post-apply plan No changes | CLOSED 20261016T225716Z |
| L4 | verify | transaction-only DRY RUN of one day: ok, stages transaction, one day with a positive count, none failed, writes nothing | status 200, 0 objects at the new prefix, within 6553 MB and 720 s | dry run (RE-STAGED code JgSV12Tz..) 2026-10-17T01:26:47Z: status 200, stages transaction, 2026-10-15 rows 5135, none failed, duration 849 ms, Max Memory 255 MB, 0 objects at the new prefix after; time trigger sum 299063 ms not over 720000, no rollback; plan 0/1/0 on the function only, apply 01:25Z, replan No changes | CLOSED 20261017T014249Z |
| L5 | s3-prefix | the first one-day WRITE (same event without dry_run) at the new prefix account_transaction | one partition, 19 columns, schema hash equal, claims and flow classes valid, same count as the dry run | first one-day write 01:27:50Z: status 200, 5135 rows (equal to the dry run), partition date=2026-10-15 only, 19 columns, schema hash ac652e2f.. equal, claims and flow classes valid | CLOSED 20261017T014249Z |
| L6 | s3-prefix | a bounded RANGE of the 25 most recent trading days at the new prefix | days written equal partitions after, the six other tables unchanged | range 2026-09-11 to 2026-10-15 at 01:28:13Z: status 200, 25 days written, 25 partitions after, none failed, 20108 ms, Max Memory 379 MB, the six other tables unchanged; CTO condition 4 returns-stage no-write dry run read: 200, stages returns/class/lots, 480146 ms, 4384 MB | CLOSED 20261017T014249Z |
| L7 | verify | the first scheduled fire after the apply, read by the issuer (this ledger STAYS OPEN for it) | issuer read |  | OPEN |

## Log

- 20261016T223933Z OPENED by 0.7.0_AE_CloudOps~IB2 with 7 leg(s)
- 20261016T225715Z LEG L1 closed: source-map commit 4b2fcc823f (artifact_sha256 only: SCt7IgN3.. replaces JNTOivgN..); script and state committed with it
- 20261016T225715Z LEG L2 closed: build-only sha256 SCt7IgN3A+SXxfn8cv0QHVnhjVMmHXePihA6MnPm2nQ= equals the packet; import smoke rc 0 and AT49_IMPORT_ERRO
- 20261016T225716Z LEG L3 closed: plan 0 add 2 change 0 destroy (aws_iam_role_policy.irpt_reporting_gold gains the one write resource account_transaction 
- 20261017T014249Z LEG L4 closed: dry run (RE-STAGED code JgSV12Tz..) 2026-10-17T01:26:47Z: status 200, stages transaction, 2026-10-15 rows 5135, none fai
- 20261017T014249Z LEG L5 closed: first one-day write 01:27:50Z: status 200, 5135 rows (equal to the dry run), partition date=2026-10-15 only, 19 columns,
- 20261017T014249Z LEG L6 closed: range 2026-09-11 to 2026-10-15 at 01:28:13Z: status 200, 25 days written, 25 partitions after, none failed, 20108 ms, Ma
