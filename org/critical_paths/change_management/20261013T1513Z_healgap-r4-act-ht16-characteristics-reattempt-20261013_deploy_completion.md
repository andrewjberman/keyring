# Deploy Completion Record
**Date opened:** 2026-10-13T15:13:03.591377+00:00
**Status:** OPEN
**Deploy:** MDPF_HEALGAP round 4 HG-t-16: characteristics producer re-attempt (rule cron(55 * * * ? *), one ListBucket on two exact keys, handler branch) -- package at scratch pin 102b2b29d3, CTO half ADDENDUM 1
**Authored by:** 2.0.0_SA_COO~G1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 48.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | rollback targets read live: function CodeSha256, the artifact object version, the role policy statements, the rules that target the function | values printed from get-function, head-object, get-role-policy, list-rule-names-by-target |  | OPEN |
| L2 | activation | the package built at pin 102b2b29d3 (three vendored members at the live bytes, handler == 8cc7e0458e) uploaded to the artifact key | head-object LastModified/VersionId/ContentLength and the zip sha256 2103fa23c1319fad; member sha256 table: three same as live, handler equals the merged blob |  | OPEN |
| L3 | activation | terraform apply via safe-apply, targeted at the rule, target, permission, role policy and function: 3 added and 2 changed in place, nothing else | the targeted plan counts printed before apply; the apply result |  | OPEN |
| L4 | verify | read back: the new rule cron(55 * * * ? *) ENABLED with input require_partition, the permission, the role policy statement, and CodeSha256 equals the uploaded zip's | describe-rule, list-targets-by-rule, get-role-policy, get-function printed |  | OPEN |
| L5 | verify | the QA negative arm on the apply day: one invoke of {require_partition: true} logs PARTITION-ABSENT (or HOLDINGS-NOT-FINAL / SKIP-COMPLETE / the producer branch) and the read states which branch ran; characteristics.json LastModified unchanged on a skip | the invoke's log lines and head-object LastModified before and after |  | OPEN |
| L6 | verify | the organic arm: the first day PARTITION-ABSENT is followed by the T-1 partition's arrival, the next :55 serves the day; a day written at 13:26Z draws HOLDINGS-NOT-FINAL then SKIP-COMPLETE | the re-attempt log lines and characteristics.json LastModified |  | OPEN |

## Log

- 20261013T151303Z OPENED by 2.0.0_SA_COO~G1 with 6 leg(s)
