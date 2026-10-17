# Deploy Completion Record
**Date opened:** 2026-10-16T21:24:12.145404+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T215724Z
**Deploy:** IRPT_DASHBD TO-DB-b-312: 49 Financial reporting-publish function irpt-49f-reporting-publish-lambda: ONE new bundle version (build-only hash s/OKOv98j..), plan 0 add 2 change 0 destroy (function code attributes and the role policy two statements: READ and LIST of the filled-report gold prefix), ONE safe-apply, the switch-OFF probe (exact no-op), ONE dry-run shard, the after-read; bound to the signed packet sha256 e6af7a92148d (COO half @a30664edac, CTO half @6aaa28e481); the filled-report switch stays OFF; rollback: prior artifact version 41lfCmfJWyvHbzqC3VtGeHVm6VJ4gRZb and the prior locals.tf through safe-apply; nothing deleted; no schedule change
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | source-map entry artifact_sha256 for irpt-49f-reporting-publish-lambda plus this ledger sentinel, committed with explicit paths | commit ids recorded | 025d4088c15e contains the packet pin 4aca09a82d and IB2's upload commit 0450aadea4 | CLOSED 20261016T215724Z |
| L2 | s3-prefix | artifact key investor-reporting/irpt-reporting-publish-lambda.zip in opal-313476888478-lambda-artifacts: a NEW VERSION (current 41lfCmfJWyvHbzqC3VtGeHVm6VJ4gRZb is the rollback target) | new VersionId, landed sha256 equals the built zip equals s/OKOv98j53aFJCLrBpYP8xh3oUcuWagn0vSHVBjhIM= | build-only sha256 s/OKOv98j53aFJCLrBpYP8xh3oUcuWagn0vSHVBjhIM= equals the packet; import smoke rc 0 (17 members incl handler.py and publisher.py); real upload landed NEW VersionId oXM0wQg8revg3asMHOhpbz1gPDnXaatK (before 41lfCmfJWyvHbzqC3VtGeHVm6VJ4gRZb kept as rollback); landed bytes sha256 equal the built zip b3f38a3a | CLOSED 20261016T213101Z |
| L3 | tf-lambda | ONE safe-apply of infra/aws/terraform/investor-reporting/reporting-publish plan exactly 0 add 2 change 0 destroy: the function by code attributes and aws_iam_role_policy.irpt_reporting_publish (two statements) | plan counts, naming gate, code hash equals the built zip, six of eight statements byte-identical, schedules ENABLED untouched, post-apply plan No changes | plan 0 add 2 change 0 destroy (aws_iam_role_policy.irpt_reporting_publish: List and Read statements gain the one filled-report prefix; the function: last_modified, s3_object_version 41lfCmfJ..->oXM0wQg8.., source_code_hash SX0xYFZs..->s/OKOv98j..); naming gate PASS 8 graded; ONE safe-apply 21:38:00Z-21:39:57Z Apply complete 0/2/0; function CodeSha256 s/OKOv98j53aFJCLrBpYP8xh3oUcuWagn0vSHVBjhIM= memory 1024 timeout 300 no reserved concurrency one layer no env; exactly the two named statements differ and six are byte-identical; both schedules ENABLED untouched; post-apply plan No changes | CLOSED 20261016T214118Z |
| L4 | verify | the switch-OFF probe {filled_report true}: the answer is exactly enabled false, clients 0, written 0, not_available [], refused [] | exact answer, within 819 MB and 240 s | ONE probe {filled_report true} at 21:41:19Z: status 200, no function error, answer exactly enabled false clients 0 written 0 not_available [] refused []; Max Memory Used 59 MB, duration 1.86 ms | CLOSED 20261016T214140Z |
| L5 | verify | ONE dry-run shard {dry_run true, shard 0, shards 7}: ok, about 990 accounts, 0 refused | ok true, refused_count 0, within 819 MB and 240 s, platinum counts unchanged | ONE dry-run shard {dry_run true, shard 0, shards 7} at 21:41:40Z: status 200, no function error, ok true, accounts 971, refused_count 0; Max Memory Used 649 MB, duration 52300 ms (limits 819 MB and 240 s); platinum counts unchanged (18257 objects, 227049 versions) | CLOSED 20261016T214505Z |
| L6 | verify | the after-read and the receipt | after, platinum_after and the record written, three criteria run | receipt PUB49F_HOP2_READER_RECORD.json; p179 DBC179-1-AC1, -2-AC1, -3-AC1 PASS | CLOSED 20261016T215724Z |

## Log

- 20261016T212412Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
- 20261016T213101Z LEG L2 closed: build-only sha256 s/OKOv98j53aFJCLrBpYP8xh3oUcuWagn0vSHVBjhIM= equals the packet; import smoke rc 0 (17 members incl han
- 20261016T214118Z LEG L3 closed: plan 0 add 2 change 0 destroy (aws_iam_role_policy.irpt_reporting_publish: List and Read statements gain the one filled-
- 20261016T214140Z LEG L4 closed: ONE probe {filled_report true} at 21:41:19Z: status 200, no function error, answer exactly enabled false clients 0 writt
- 20261016T214505Z LEG L5 closed: ONE dry-run shard {dry_run true, shard 0, shards 7} at 21:41:40Z: status 200, no function error, ok true, accounts 971, 
- 20261016T215159Z LEG L1 closed: source-map commit 0450aadea4 (artifact_sha256 only: s/OKOv98j.. replaces SX0xYFZs..); records and scripts committed with
- 20261016T215159Z LEG L6 closed: after-read: function s/OKOv98j.. memory 1024 timeout 300 no reserved concurrency; two of eight statements differ, six by
- 20261016T215724Z LEG L1 closed: 025d4088c15e contains the packet pin 4aca09a82d and IB2's upload commit 0450aadea4
- 20261016T215724Z LEG L6 closed: receipt PUB49F_HOP2_READER_RECORD.json; p179 DBC179-1-AC1, -2-AC1, -3-AC1 PASS
- 20261016T215724Z CLOSED -- all 6 legs proven
