# Deploy Completion Record
**Date opened:** 2026-10-11T05:10:32.398752+00:00
**Status:** OPEN
**Deploy:** MDPF_HEALGAP R3 act 1 (HG-t-9 v2): cot-satellites-registry-producer code + inline policy in place, then the 13:15Z stamp-gated rule (3 resources) via safe-apply. CTO half SIGNED @698312232c (msg 3504). Rollback: restore artifact version mgzFeamx2_MIO_R.lBF6IYGUNM5aXcir (CodeSha256 eFToEJ0F..., 2026-09-14T19:50:02Z) and terraform apply of the same targets from 5828c0da8b~1 (removes rule, target, permission and the ListStampPrefix statement)
**Authored by:** 2.0.0_SA_COO~G1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | rollback targets read live: Lambda CodeSha256, artifact VersionId, role policy statements, rules on the function | values printed from get-function-configuration, head-object, get-role-policy, list-rule-names-by-target |  | OPEN |
| L2 | activation | build and upload cot-satellites-registry-producer.zip to the lambda-artifacts bucket from the merged tree (BUILD_ONLY read first) | BUILD_ONLY sha256 printed; head-object on the uploaded key shows content-sha256 equal to it and a new VersionId |  | OPEN |
| L3 | activation | Terraform cot-pipeline safe-apply -target of module.cot_satellites_registry_producer, the s3 inline policy, module.stamp_gated_rule_name, rule, target, permission | plan reads code hash + one inline policy changed in place and 3 added, nothing else; apply result |  | OPEN |
| L4 | verify | acceptance 1-3 read back: live CodeSha256 = build sha256; two rules, new one cron(15 13 * * ? *) ENABLED input require_stamp true; policy Sid list with one ListStampPrefix and no meta GetObject | values printed from live reads |  | OPEN |
| L5 | verify | first 13:15Z fire after the apply: registry.json as_of today with LastModified >= 13:15Z OR the log line STAMP-ABSENT | CloudWatch log excerpt and head-object |  | OPEN |

## Log

- 20261011T051032Z OPENED by 2.0.0_SA_COO~G1 with 5 leg(s)
