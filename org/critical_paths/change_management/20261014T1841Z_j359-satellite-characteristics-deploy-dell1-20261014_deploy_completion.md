# Deploy Completion Record
**Date opened:** 2026-10-14T18:41:32.335916+00:00
**Status:** OPEN
**Deploy:** J359 (ADHOC.j359-satellite-characteristics-deploy, WORLD): the cot-satellites-characteristics-producer function rebuilt at a pin carrying efb3f6550f (the four scalars by the Models' method over the model sleeves; returns over the holdings that have each window) and uploaded to the artifact key s3://opal-313476888478-lambda-artifacts/cot-pipeline/cot-satellites-characteristics-producer.zip (prior VersionId 1Dw2S3IjFNtmZwZpbAE0p_3o_IMVtRrC, content-sha256 base64 IQP6I8Exn60kZVcI1K8mnmGWModpgOe4UE+EbOFf54c=, 182727 B), ONE read grant (s3:GetObject on opal-data-cot/platinum/satellites/registry.json joins holdings.json in Sid ReadSatellitesHoldings of aws_iam_role_policy.cot_satellites_characteristics_producer_s3; infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf, the patch's element and comment lines only), one dry-run invoke and ONE driven invoke. The ONE served key that moves: s3://opal-data-cot/platinum/satellites/characteristics.json (prior VersionId at the cut C8ZQnQw0ESDdnaIK8iq_f7OFbcW6tble, etag 6d77168a10ac70b49668e007f9aa5184, 68672 B, 2026-10-14T13:26:02Z), serving path the scoped route /api/scoped/satellites/characteristics.json (the Positioning Satellites mode and the factsheet popup). The rule cot-satellites-characteristics-producer-daily (cron(25 13 * * ? *)) and the hourly reattempt rule etfs-cot-satellites-characteristics-producer-reattempt-hourly (cron(55 * * * ? *), input {require_partition:true}) are NOT changed. GO: 2.0.0_SA_COO~J1 msg 5688 (order @1e3aa5a123); pair COO half e1dfba9db8 (wk-remote-J359), CTO half 2b6f842af2. No portal promote is part of this order.
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | preconditions 2a-2e re-measured (halves signed, clock, wk-remote-J359 tip carries efb3f6550f, the five members vs the COO column, sentinels across every live worktree), before print (function, rollback copy of the prior artifact by hash, rule and target, role policy verbatim, served key VersionId and saved bytes, input freshness, drift table, Bloomberg-sourced set) | all recorded and printed |  | OPEN |
| L2 | s3-prefix | the producer taken into box/dell1 by a one-file cherry-pick of efb3f6550f and the package built at that pin and uploaded to s3://opal-313476888478-lambda-artifacts/cot-pipeline/cot-satellites-characteristics-producer.zip | new version whose content-sha256 metadata (the module's base64 form) equals the zip's own hash, read back before planning |  | OPEN |
| L3 | activation | module.cot_satellites_characteristics_producer and aws_iam_role_policy.cot_satellites_characteristics_producer_s3 (D1: the patch, one targeted plan, one safe-apply) | plan moves only s3_object_version, source_code_hash and one added Resource element; CodeSha256 equals the zip; every sidecar module equals git show pin; policy gained registry.json only; unscoped re-plan clean |  | OPEN |
| L4 | activation | D2 the dry-run invoke {dry_run:true} then D3 the ONE driven invoke {} of cot-satellites-characteristics-producer | dry-run rc 0 and the served VersionId unchanged; driven 200, VersionId moved, registry_as_of present, method.renormalised true |  | OPEN |
| L5 | verify | the served read against the spec table (or oracle_check over the run's as_of), the positive controls, and the return-windows comparison for every bbg-sourced ticker, old rule against new (CTO condition 2) | every satellite fee/yield/duration/beta equal to the table; any moved window named with its cause |  | OPEN |
| L6 | verify | after print and close: function config (only CodeSha256 and LastModified), artifact versions, served key, rules and targets unchanged, policy one added element; no leg open across 21:00Z | differences listed, nothing deployed from them |  | OPEN |

## Log

- 20261014T184132Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 6 leg(s)
