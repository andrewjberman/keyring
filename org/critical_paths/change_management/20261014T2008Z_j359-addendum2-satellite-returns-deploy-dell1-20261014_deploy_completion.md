# Deploy Completion Record
**Date opened:** 2026-10-14T20:08:23.450956+00:00
**Status:** OPEN
**Deploy:** J359 addendum 2 (ADHOC.j359-addendum2-satellite-returns-deploy, WORLD): the cot-satellites-characteristics-producer function rebuilt at 7337fdfa6d (wk-remote-J359b; each satellite's trailing returns = (1-g) x the sleeve-average of the underlying Opal models' realized returns + g x GLD) and uploaded to the artifact key s3://opal-313476888478-lambda-artifacts/cot-pipeline/cot-satellites-characteristics-producer.zip (prior VersionId 3yaAgYL1ZY9OElyISnHodcGLE7nn0TPo, content-sha256 base64 mpFb3up8mjaS9cHDqlFdAXtIjePtRhJV1kXvCeBkewA=, 205906 B), ONE read grant (s3:GetObject on opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json joins positioning_data.json in Sid ReadServedPositioningData of aws_iam_role_policy.cot_satellites_characteristics_producer_s3; infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf, the patch's element and comment lines only), one dry-run invoke and ONE driven invoke. The ONE served key that moves: s3://opal-data-cot/platinum/satellites/characteristics.json (prior VersionId at the cut to be read, 6z8c7qDDQTd2Q9k8qSoPpO78CxlsWAgZ at 20:01Z), serving path the scoped route /api/scoped/satellites/characteristics.json (the Positioning Satellites mode and the factsheet popup, both live on PROD). The daily rule cron(25 13 * * ? *) and the hourly reattempt rule cron(55 * * * ? *) are NOT changed. GO: 2.0.0_SA_COO~J1 msg 5826 (order @5598c3f766); pair COO half 5500bce348 (wk-remote-J359b, sha256 800adb54...), CTO half 675488ce32 (conditions C1-C5). The read through the served route is the issuer's open leg. No portal change is part of this order.
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | preconditions 2a-2e re-measured (halves signed, clock, wk-remote-J359b tip carries 7337fdfa6d, the five members vs the COO column, sentinels across every live worktree), before print (function, rollback copy of the prior artifact by hash, rule, role policy verbatim, served key VersionId and saved bytes, input freshness, drift table, Bloomberg-sourced set) | all recorded and printed |  | OPEN |
| L2 | s3-prefix | the package built at 7337fdfa6d and uploaded to s3://opal-313476888478-lambda-artifacts/cot-pipeline/cot-satellites-characteristics-producer.zip | new version whose content-sha256 metadata (the module's base64 form) equals the zip's own hash, read back before planning |  | OPEN |
| L3 | activation | module.cot_satellites_characteristics_producer and aws_iam_role_policy.cot_satellites_characteristics_producer_s3 (D1: the patch, one targeted plan, one safe-apply) | plan moves only s3_object_version, source_code_hash and one added Resource element; CodeSha256 equals the zip; every sidecar module equals git show pin; policy gained the benchmarks element only; unscoped re-plan clean |  | OPEN |
| L4 | activation | D2 the dry-run invoke {dry_run:true} then D3 the ONE driven invoke {} of cot-satellites-characteristics-producer | dry-run rc 0 and the served VersionId unchanged; driven 200, VersionId moved, benchmarks_as_of present, coverage absent |  | OPEN |
| L5 | verify | the served read against the table (or verify_producer_returns over the run's as_of), the controls, the windows comparison for every bbg-sourced ticker (CTO C2) and the partial-sleeve names (CTO C4) | every satellite's eight windows equal the table to 2 dp; scalars, total_weight, sources and tickers unchanged; any moved window named with its cause; every partial-sleeve window named |  | OPEN |
| L6 | verify | after print and close: function config (only CodeSha256 and LastModified), artifact versions, served key, rules and targets unchanged, policy one added element; no leg open across 21:00Z | differences listed, nothing deployed from them |  | OPEN |

## Log

- 20261014T200823Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 6 leg(s)
