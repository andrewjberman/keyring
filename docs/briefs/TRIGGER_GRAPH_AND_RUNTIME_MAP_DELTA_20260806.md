# TRIGGER_GRAPH_AND_RUNTIME_MAP delta - 2026-08-06

**Prepared as:** `1.0.0_SA_CTO~A`
**Class:** read-only live-state reconciliation
**Baseline:** [`TRIGGER_GRAPH_AND_RUNTIME_MAP.md`](TRIGGER_GRAPH_AND_RUNTIME_MAP.md), measured 2026-07-29T20:50:29Z, SHA-256 `80B425CBF1AC95DBE6A31427858FD53DE0B731E35DF1A871B06D8D69F96F10BB`
**Current live read:** account `313476888478`, `us-east-1`, 2026-08-06 through 14:30:35Z / 10:30:35 EDT
**Activity delta window:** `[2026-07-29T20:50:29Z, 2026-08-06T14:30:35Z)`
**Mutation statement:** no AWS or baseline-document mutations were performed.

## 1. Executive delta

Every one of the baseline's **154 trigger rows** and **115 resource/action rows** was reconciled against live AWS. The logical estate is only one trigger larger, but that net number hides substantial route movement.

| Surface | 2026-07-29 baseline | 2026-08-06 live | Delta |
|---|---:|---:|---:|
| EventBridge Rules | 143 | 139 | -4 |
| - scheduled rules | 123 | 121 | -2 |
| - event-pattern rules | 20 | 18 | -2 |
| - enabled / disabled | 125 / 18 | 121 / 18 | -4 / 0 |
| Scheduler schedules | 11 | 16 | +5 |
| - enabled / disabled | 10 / 1 | 15 / 1 | +5 / 0 |
| **Total triggers** | **154** | **155** | **+1** |
| **Total enabled / disabled** | **135 / 19** | **136 / 19** | **+1 / 0** |
| EventBridge / Scheduler target edges | 152 / 11 | 148 / 16 | -4 / +5 |
| **Total target edges** | **163** | **164** | **+1** |
| **Distinct immediate resources/actions** | **115** | **115** | **0** |
| Triggered Lambda functions | 99 | 102 | +3 |
| Triggered Lambdas with source-map entry | 95 / 99 | 99 / 102 | +4 mapped, +3 denominator |

Baseline disposition: **143 unchanged, 4 migrated, 3 retired, 4 modified in place = 154**. Current disposition: **143 unchanged, 4 modified in place, 4 migration replacements, 4 genuinely new triggers = 155**.

The highest-impact changes are:

1. MDPF now has an ET-anchored `09:00` schedule floor, an ET-retimed accrual bridge at `09:40`, and an ET-retimed publisher at `09:50`. The old publisher Rule is gone.
2. Four UTC/event routes migrated: Inflection ETF ownership, Cottonwood BD session, Cottonwood ingest mirror, and the MDPF publisher.
3. Three actions were intentionally retired: the disabled crawl harness, the disabled legacy Schwab SI2 download route, and the never-used canonical Schwab runner start route.
4. Two new Inflection bronze routes and one estate-report route are live.
5. The live route registry is stale even though its total looks close: `trigger-map.json` has **4 map-only, 5 live-only, and 4 field-drift rows**.
6. `opal-assets-ingest-mirror` recorded **45 invocations / 45 errors** in the delta window. Its 2026-08-06 log fails on **551 Cottonwood `ALIEN SURPLUS` keys**. The new Cottonwood Scheduler route had not yet reached its first 18:30 ET fire at measurement time.

## 2. Trigger migrations

These are logical route migrations, not workload decommissions. The target Lambda survives in every row.

| Estate / product | Baseline route | Current route | Target and semantic delta | Activity since baseline |
|---|---|---|---|---:|
| Inflection / Model Portfolios | Rule `inf-etf-ownership-on-gold-complete`; S3 event on Inflection gold completion | Rule `inf-etf-ownership-daily-schedule`; `cron(0 15 * * ? *)` UTC = 11:00 EDT / 10:00 EST | Same `inf-etf-ownership-daily`; target id changed to `InfEtfOwnershipDailyScheduledFloor`; Lambda was redeployed 2026-08-01 | old Rule 2/0; new Rule 4/0; Lambda 16/0 |
| Cottonwood / Advisor Intelligence | Rule `cot-bd-session-daily`; `cron(0 2)` UTC = 22:00 EDT / 21:00 EST | Scheduler `cot-bd-session-daily-et`; daily 16:30 `America/New_York` | Same `cot-bd-session-trigger` and `{"mode":"session-refresh"}`; Scheduler role plus explicit 24h/185 retry policy | old Rule 7/0; Scheduler N/O; Lambda 22/0 |
| Cottonwood / Cross-product Data Platform | Rule `opal-assets-ingest-mirror-cot-daily`; `cron(30 3)` UTC = 23:30 EDT / 22:30 EST | Scheduler `opal-assets-ingest-mirror-cot-daily-et`; daily 18:30 `America/New_York` | Same `opal-assets-ingest-mirror`; Scheduler input `{}`, role, and explicit 24h/185 retry policy | old Rule 7/0; Scheduler N/O; Lambda **45/45 errors** |
| Cross-partner / Model Portfolios | Rule `opal-assets-mdpf-portal-publisher-daily`; `cron(15 16)` UTC = 12:15 EDT / 11:15 EST | Scheduler with the same name; daily 09:50 `America/New_York` | Same `opal-assets-mdpf-portal-publisher`; Scheduler input `{}`, role, and explicit 24h/185 retry policy | old Rule 5/0; Scheduler N/O; Lambda 14/0 |

The Cottonwood session and mirror migrations were applied at 2026-08-06T00:08Z with the old Rules absent and the new schedules enabled. At the 10:30 EDT census, neither new schedule had reached today's nominal fire, so configuration continuity is proven but first-fire success is not.

## 3. Retired triggers and resources

| Baseline trigger | Baseline state / activity | Current disposition | Underlying resource disposition | Evidence |
|---|---|---|---|---|
| `canonical-schwab-si2-download-schedule` | DISABLED; baseline 90d 35/0; delta 0/0 | Rule, target, single-purpose role, and policy removed | `canonical-schwab-si2` (`i-0f3d57a97f14727af`) remains **running** for the two per-account daily-pull Rules; only the obsolete action died | commit `bd1470c802`; change record `org/critical_paths/change_management/20260804T0505Z_t5-kill-K5-si2-download-schedule_change_record.md` |
| `canonical-schwab-xref-success` | ENABLED event rule; baseline 90d 0/0; delta 0/0 | Rule and start-path IAM removed with the compute | `canonical-schwab-runner` (`i-0ed92ce2e72f505dc`) terminated; preserved `s3://opal-data-bd/canonical/schwab/` data; live EC2 enumeration no longer returns the instance | commit `772ff82f55`; ledger `org/critical_paths/change_management/20260805T2215Z_canonical-schwab-runner_decommission_deploy_completion.md` |
| `dc2-test1-offpeak-harness` | DISABLED; baseline 90d 1/1; delta 0/0 | Rule and full crawl-harness stack removed | Custom SSM document `dc2-test1-offpeak-orchestrator` returns `InvalidDocument`; 16-resource destroy and declarations removed | commit `b6d033ae00`; ledger `org/critical_paths/change_management/20260730T2015Z_crawl-harness-destroy_deploy_completion.md` |

The baseline's three removed resource/actions are exactly the three rows above. No Lambda resource disappeared as a consequence of trigger migration or retirement.

## 4. New triggers and resources

| Trigger | Current trigger time | Target | Estate / product | Activity since baseline |
|---|---|---|---|---:|
| Rule `inf-api-eclipse-daily` | `cron(33 13)` UTC = 09:33 EDT / 08:33 EST | new Lambda `inf-api-eclipse` | Inflection / Advisor Intelligence Data Platform | Rule 2/0; Lambda 2/0 |
| Rule `inf-bronze-complete-emitter-daily` | `cron(43 14)` UTC = 10:43 EDT / 09:43 EST | new Lambda `inf-bronze-complete-emitter` | Inflection / Advisor Intelligence Data Platform | Rule 1/0; Lambda 1/0 |
| Scheduler `mdpf-scheduled-floor` | daily 09:00 `America/New_York` | existing `mdpf-daily-trigger`; production payload; `mdpf-daily-trigger-dlq`; 24h/185 retries | Cross-partner / Model Portfolios | Scheduler N/O; Lambda 11/0 all callers |
| Scheduler `estate-report-0900et` | daily 09:00 `America/New_York` | new `estate-report-orchestrator`; `{"mode":"daily-run"}`; 24h/185 retries | Internal Infrastructure / Estate Report | Scheduler N/O; Lambda 8/0 all callers |

`estate-report-0900et` was born disabled by the 2026-08-03 census and was enabled on 2026-08-04 after a validation fire (`a21238059b`). The two Inflection resources were introduced by `ee66f1d124`; both are active and their live updates are successful.

## 5. In-place schedule and state changes

| Trigger | Baseline | Current | Estate / product | Delta activity |
|---|---|---|---|---:|
| Rule `opal-inf-jwt-fetch` | `cron(0 13)` UTC = 09:00 EDT / 08:00 EST | `cron(5 12)` UTC = 08:05 EDT / 07:05 EST | Inflection / Advisor Intelligence | Rule 8/0; `inf-jwt-trigger` 16/0 all callers |
| Scheduler `mdpf-accrual-bridge-daily` | `cron(45 15)` UTC = 11:45 EDT / 10:45 EST | daily 09:40 `America/New_York` | Cross-partner / Model Portfolios | Scheduler N/O; `mdpf-accrual-trigger` 10/0 all callers |
| Rule `seeking-alpha-analysis-daily` | ENABLED; `cron(0 21)` UTC | DISABLED; expression and target unchanged | Global / Opal News | Rule and Lambda 1/0 before disable |
| Rule `seeking-alpha-news-daily` | ENABLED; `cron(0 14)` UTC | DISABLED; expression and target unchanged | Global / Opal News | Rule and Lambda 1/0 before disable |

The JWT retime happened in two applied steps: 13:00Z to 12:15Z (`b693d2ebd2`), then to 12:05Z (`21805fde2d`). The Seeking Alpha changes are only step 1 of the recorded teardown; both coordinator Lambdas remain active and source-mapped.

## 6. Exact common-route comparison

- **136 Rules survive by name.** Their target ARN, target id, input, role, retry policy, and service-specific target parameters are byte-equivalent after removing response-only null fields.
- **18 surviving event-pattern Rules** retain equivalent parsed event patterns, states, and rule roles.
- **11 Scheduler schedules survive by name.** All target ARNs, inputs, roles, retry policies, dead-letter settings, and flexible-window settings are unchanged. Only `mdpf-accrual-bridge-daily` changed expression/timezone.
- No surviving Rule changed target. No Scheduler target changed resource. There are no zero-target live Rules.
- Duplicate same-Lambda Rules remain unchanged for `market-rsi-tiered-daily` and the seven duplicate-target `news-api-*` rules. `inf-gold-dispatch-release-changed` also remains a deliberate two-target Rule, but its targets are different resources (Logs plus SNS), not a duplicate.

## 7. Runtime provenance delta

All **102 currently triggered Lambdas exist live**. Twelve have a live `LastModified` after the baseline cutoff:

| Lambda | Live LastModified (UTC) | Canonical source | Deployment provenance status |
|---|---|---|---|
| `mdpf-daily-trigger` | 2026-08-06 00:37:53 | `infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger` | source-map deploy record remains 2026-07-29; stale |
| `opal-assets-daily-emitter` | 2026-08-06 00:35:41 | `infra/aws/lambda/opal-assets/opal-assets-daily-emitter` | source-map deploy record remains 2026-07-14; stale |
| `inf-api-positions` | 2026-08-05 23:17:33 | `infra/aws/lambda/inf-pipeline/inf-api-positions` | source-map deploy record remains 2026-07-15; stale |
| `inf-silver-chain` | 2026-08-05 23:17:33 | `infra/aws/lambda/inf-pipeline/inf-silver-chain` | source-map deploy record remains 2026-07-15; stale |
| `inf-accounts-v2-daily` | 2026-08-05 23:17:33 | `infra/aws/lambda/inf-pipeline/inf-accounts-v2-daily` | source-map deploy record remains 2026-07-15; stale |
| `inf-api-reps` | 2026-08-05 23:17:33 | `infra/aws/lambda/inf-pipeline/inf-api-reps` | source-map deploy record remains 2026-07-15; stale |
| `inf-bronze-complete-emitter` | 2026-08-04 20:20:31 | `infra/aws/lambda/inf-pipeline/inf-bronze-complete-emitter` | source/Terraform mapped; no deploy commit/time recorded |
| `inf-api-eclipse` | 2026-08-04 20:20:23 | `infra/aws/lambda/inf-pipeline/inf-api-eclipse` | source/Terraform mapped; no deploy commit/time recorded |
| `etfs-reports-orchestrator` | 2026-08-02 03:19:18 | `infra/aws/lambda/etfs-reports-orchestrator` | source/Terraform mapped; no deploy commit/time recorded |
| `cot-etf-ownership-daily` | 2026-08-01 23:26:23 | `infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily` | recorded at `dbff7603bf`, 2026-08-01 23:30:16Z |
| `inf-etf-ownership-daily` | 2026-08-01 19:19:53 | `infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily` | recorded at `af4f123e2c`, 2026-08-01 19:35:16Z |
| `estate-report-orchestrator` | 2026-07-31 00:14:32 | `infra/aws/lambda/estate-report-orchestrator` | source/Terraform mapped; no deploy commit/time recorded |

Only **2 of these 12** live runtime changes have source-map deployment metadata at or after the live update. Source locations remain identifiable for all twelve, but the exact deployed commit is unresolved from the registry for ten.

Source-map coverage improved from **95/99** to **99/102** triggered Lambdas. `m365-ms-ingest-liveness` was repaired into the map by `474f534a56`. The only current source-map gaps are unchanged: `opal-49f-served-guard`, `opal-cot-served-guard`, and `opal-inf-served-guard`.

Across the 95 baseline mapped functions, source/Terraform/artifact paths did not move. Deployment metadata changed for `cot-bd-session-trigger`, `cot-etf-ownership-daily`, and `inf-etf-ownership-daily`; the latter two align to post-baseline live updates. `cot-bd-session-trigger` now records `49601d8851` at 2026-08-01T23:30:16Z even though the live function `LastModified` remains 2026-07-23, so that registry update is not evidence of a Lambda code update.

### Graph and CodeBuild runtime provenance

- All four graph target edges and task-definition revisions are unchanged: `globgrph-comp-learns-producer:1`, `globgrph-derive-runner:6`, `globgrph-fedobs-producer:1`, and `globgrph-cse-producer:1`.
- All four still resolve through mutable image tag `313476888478.dkr.ecr.us-east-1.amazonaws.com/opal-globgrph-derive-runner:latest`. The current tag resolves to digest `sha256:dc6cf568bb9cb565fc1298a41711edc5459ea7a6a57df3bda525dfd99f96ae63`, pushed 2026-07-19. Therefore no post-baseline tag movement was observed, but the trigger-facing provenance defect remains.
- `opal-drift-producer` and `opal-stitch-produce` retain their baseline S3 source ZIP locations and `aws/codebuild/amazonlinux2-x86_64-standard:5.0` image. Both project `lastModified` timestamps predate the baseline.

## 8. Activity and health since the baseline

CloudWatch Rule metrics across the union of 146 baseline/current Rule names recorded **1,912,821 invocations** and **1,888,799 failed invocations** in the exact delta interval. The count is dominated by the unchanged `FIRMSEP-s3-direct-access-bypass` control: **1,888,796 invocations / 1,888,795 failed**. `moltbot-ssm-sendcommand-alert` remains **4/4 failed**.

Scheduler exposes only `InvocationAttemptCount` at `ScheduleGroup=default`; it recorded **77 attempts** in the interval. There is still no supported per-schedule dimension, so every per-schedule count remains `N/O`.

EventBridge dispatch success does not prove Lambda success. The clearest example is `opal-assets-ingest-mirror`: Rule dispatches are clean, while the Lambda is **45/45 errors**. The latest 2026-08-06 stream completed Inflection Orion/Eclipse enumeration, then raised `MirrorRaise` on **551 unexpected `blackdiamond/cottonwood/bronze/` keys**, with three async attempts. The new 18:30 ET Cottonwood schedule points at this same all-row function and should be treated as unproven until the resource failure is resolved and the first fire is read.

## 9. Registry and tooling delta

`infra/aws/lambda/ci/trigger-map.json` says `_updated=2026-08-01T19:23Z`, `142` Rules + `12` schedules = `154`. Live is `139` + `16` = `155`. The near-equal total masks **13 stale rows**: four map-only identities, five live-only identities, and four surviving names with stale fields.

| Map-only (stale) | Live-only (missing) |
|---|---|
| `canonical-schwab-si2-download-schedule` | `cot-bd-session-daily-et` |
| `canonical-schwab-xref-success` | `inf-api-eclipse-daily` |
| `cot-bd-session-daily` | `inf-bronze-complete-emitter-daily` |
| `opal-assets-ingest-mirror-cot-daily` | `mdpf-scheduled-floor` |
|  | `opal-assets-ingest-mirror-cot-daily-et` |

| Field-drift row | Registry | Live |
|---|---|---|
| `estate-report-0900et` | DISABLED | ENABLED |
| `mdpf-accrual-bridge-daily` | `cron(45 15)` UTC | `cron(40 9)` at `America/New_York` |
| `opal-assets-mdpf-portal-publisher-daily` | EventBridge Rule, `cron(15 16)` UTC | Scheduler, `cron(50 9)` at `America/New_York` |
| `opal-inf-jwt-fetch` | `cron(0 13)` UTC | `cron(5 12)` UTC |

This is the highest-leverage tooling correction from the delta: count-only parity would pass close to green while the route identities are wrong. The registry generator/CI must compare the two trigger services by `(service, group/bus, name)`, target edge, state, expression, and timezone, and must fail on either set difference.

The current mission prose is also stale by its own declaration: `org/missions/MISSIONS.md` still states `121` scheduled Rules against `10` Scheduler schedules. Live is `121` scheduled Rules against `16` schedules.

## 10. Complete baseline trigger reconciliation

The eleven non-unchanged baseline rows are fully enumerated in sections 2, 3, and 5. The remaining **143 baseline rows** passed identity, state, expression/timezone, event-pattern where applicable, and target-edge comparison.

**Unchanged EventBridge Rules (133):** `FIRMSEP-s3-direct-access-bypass`, `access-anomaly-scanner-schedule`, `bd-49f-etf-ownership-scheduled-floor`, `bd-49f-fees-runner-daily`, `bd-49f-fees-session-daily`, `bd-49f-keepalive-sched`, `bd-49f-runner-daily`, `bd-49f-session-complete`, `bd-49f-session-daily`, `bd-allocation-file-check-daily`, `bd-allocation-pipeline-trigger`, `bd-asset-dim-pipeline-trigger`, `bd-canonical-prices-daily`, `bd-cot-keepalive-sched`, `bd-fees-pipeline-trigger`, `bd-gold-layer-monthly-trigger`, `bd-gold-nightly-fallback`, `bd-realized-pipeline-trigger`, `bd-transaction-pipeline-trigger`, `bd-unrealized-pipeline-trigger`, `canonical-schwab-si2-08242234-daily-pull`, `canonical-schwab-si2-08335338-daily-pull`, `consolidation-gold-runner-scheduled-start`, `cost-anomaly-scanner-schedule`, `cot-bronze-complete`, `cot-etf-ownership-daily-schedule`, `cot-rebalancer-runner-daily`, `cot-session-complete`, `cot-silver-complete`, `daily-agenda-generator`, `ec2-auto-shutdown-enforcer-schedule`, `ec2-runtime-monitor-15min`, `etf-ownership-dashboard-daily`, `etfs-canon-fanin-daily`, `etfs-netassets-daily`, `exec-summary-trigger`, `fear-greed-daily-update`, `finbert-scoring-post-ingestion`, `finbert-scoring-post-ingestion-45min`, `fred-ingestion-daily`, `fred-ingestion-monthly-early`, `fred-ingestion-monthly-late`, `fred-ingestion-monthly-mid`, `fred-ingestion-weekly`, `fred-macro-ingestion-daily`, `gldinc-ss4c-canary-daily`, `historical-prices-daily`, `incrparity-weekly`, `inf-accounts-v2-daily`, `inf-api-assets-v2-daily`, `inf-api-positions-daily`, `inf-api-reps-daily`, `inf-api-txn-daily`, `inf-assets-trigger-bronze-complete`, `inf-billing-daily`, `inf-canonical-prices-daily`, `inf-gold-dispatch-release-changed`, `inf-gold-full-on-bronze-complete`, `inf-gold-incremental-daily`, `inf-nna-partition-check-trigger`, `inf-otp-state-change`, `inf-performance-daily`, `inf-silver-chain-bronze-complete`, `inf-tax-daily`, `inf-unified-account-dim-daily`, `infrastructure-monitor-daily`, `infrastructure-snapshot-daily`, `keyword-drilldown-generator-daily`, `keyword-intelligence-generator-daily`, `layer3-gpt-curation-daily`, `m365-ms-ingest-liveness-6h`, `m365-otp-liveness-6h`, `market-rsi-tiered-daily`, `mdpf-daily-refresh-trigger`, `moltbot-ssm-sendcommand-alert`, `news-api-100am`, `news-api-100pm`, `news-api-1100am`, `news-api-1100pm`, `news-api-300am`, `news-api-345pm`, `news-api-400pm`, `news-api-500am`, `news-api-500pm`, `news-api-600pm`, `news-api-700am`, `news-api-745pm`, `news-api-845am`, `news-api-900pm`, `news-rss-12pm`, `news-rss-1am`, `news-rss-3pm`, `news-rss-4am`, `news-rss-6pm`, `news-rss-9am`, `news-rss-9pm`, `news-trending-analysis-daily`, `opal-49f-served-guard-on-write`, `opal-assets-bd49f-daily-pull-pull-daily`, `opal-assets-bd49f-daily-pull-reattempt-daily`, `opal-assets-daily-emitter-daily`, `opal-assets-ingest-mirror-inf-daily`, `opal-assets-silver-blackdiamond-sweep-daily`, `opal-assets-silver-eclipse-sweep-daily`, `opal-assets-silver-etf-sweep-daily`, `opal-assets-silver-orion-sweep-daily`, `opal-assets-silver-schwab-sweep-daily`, `opal-assets-silver-smartx-sweep-daily`, `opal-cot-served-guard-on-write`, `opal-cot-value-parity-hourly`, `opal-drift-producer-nightly`, `opal-globgrph-cloudtrail-mgmt`, `opal-globgrph-comp-learns-producer-nightly`, `opal-globgrph-derive-runner-nightly`, `opal-globgrph-fedobs-producer-nightly`, `opal-inf-bronze-runner-cron`, `opal-inf-ec2-state-change-monitor`, `opal-inf-export-schedule`, `opal-inf-served-guard-on-write`, `opal-inf-value-parity-hourly`, `opal-stitch-produce-nightly`, `security-sweep-comprehensive`, `smartx-account-distribution-daily`, `smartx-daily-export-trigger`, `trade-parquet-nightly-export`, `trending-image-selector-daily`, `trending-topics-portal-publisher-afternoon`, `trending-topics-portal-publisher-daily`, `trending-topics-portal-publisher-morning`, `volatility-daily-update`, `yang-refresh-fred-cache-weekly`, `ycharts-session-capture-schedule`, `ycharts-session-probe-schedule`.

**Unchanged Scheduler schedules (10):** `astn-wsjft-3am-run`, `etfs-reports-monthly-run`, `globgrph-cse-producer-nightly`, `opal-assets-bd49f-dim-convert-daily`, `smartx-assets-daily-pull-daily`, `smartx-jwt-refresher-daily`, `smartx-model-monthly-pull-daily`, `smartx-rest-pull-daily`, `wsb-49f-model-aua-pull-daily`, `wsd-49f-partner-held-etf-pull-daily`.

## 11. Complete resource/action reconciliation

The baseline and current estate each contain **115 distinct immediate resource/actions**. Three baseline SSM actions retired and three Lambda resources were added. Of the 112 common actions, 13 have a route, runtime, or provenance change and 99 have no detected mapped-field delta.

**Retired actions (3):** legacy SI2 `AWS-RunPowerShellScript` action, `AWS-StartEC2Instance -> canonical-schwab-runner`, and `dc2-test1-offpeak-orchestrator:$DEFAULT`.

**Added resources (3):** `estate-report-orchestrator`, `inf-api-eclipse`, `inf-bronze-complete-emitter`.

**Relinked common resources (5):** `cot-bd-session-trigger`, `inf-etf-ownership-daily`, `mdpf-daily-trigger`, `opal-assets-ingest-mirror`, `opal-assets-mdpf-portal-publisher`.

**Common resources with post-baseline runtime update (9):** `cot-etf-ownership-daily`, `etfs-reports-orchestrator`, `inf-accounts-v2-daily`, `inf-api-positions`, `inf-api-reps`, `inf-etf-ownership-daily`, `inf-silver-chain`, `mdpf-daily-trigger`, `opal-assets-daily-emitter`.

**Provenance-only registry improvement (1):** `m365-ms-ingest-liveness`.

**No detected route/runtime/provenance delta (99):** `/aws/events/inf-gold-dispatch-release-audit`, `CodeBuild opal-drift-producer`, `CodeBuild opal-stitch-produce`, `SSM RunPowerShell canonical-schwab-si2 / 08242234`, `SSM RunPowerShell canonical-schwab-si2 / 08335338`, `SSM StartEC2 consolidation-gold-runner`, `access-anomaly-scanner`, `astn-wsjft-orchestrator`, `bd-49f-etf-ownership-daily`, `bd-49f-fees-runner`, `bd-49f-keepalive`, `bd-49f-runner`, `bd-49f-session-trigger`, `bd-allocation-file-checker`, `bd-allocation-trigger`, `bd-asset-dim-trigger`, `bd-cot-keepalive`, `bd-fees-trigger`, `bd-gold-trigger`, `bd-incrparity-trigger`, `bd-realized-trigger`, `bd-transactions-trigger`, `bd-unrealized-trigger`, `cost-anomaly-scanner`, `cot-rebalancer-runner`, `daily-agenda-generator`, `ec2-auto-shutdown-enforcer`, `ec2-runtime-monitor`, `etf-ownership-dashboard`, `etfs-canon-fanin`, `etfs-netassets-daily`, `exec-summary-generator`, `finbert-batch-processor`, `fred-data-ingestion`, `fred-macro-ingestion`, `gldinc-ss4c-canary`, `globgrph-comp-learns-producer:1`, `globgrph-cse-producer:1`, `globgrph-derive-runner:6`, `globgrph-fedobs-producer:1`, `historical-prices-scheduler`, `inf-api-assets-v2`, `inf-api-txn`, `inf-assets-trigger`, `inf-billing-daily`, `inf-bronze-trigger`, `inf-ec2-launch-monitor`, `inf-gold-dispatch-release-alarm`, `inf-gold-trigger`, `inf-jwt-trigger`, `inf-nna-partition-checker`, `inf-otp-relay`, `inf-performance-daily`, `inf-tax-daily`, `inf-unified-account-dim-daily`, `infrastructure-daily-snapshot`, `keyword-intelligence-generator`, `m365-otp-liveness`, `mdpf-accrual-trigger`, `news-ingestion-scheduler`, `news-trending-analysis`, `opal-49f-served-guard`, `opal-assets-bd49f-daily-pull`, `opal-assets-bd49f-dim-convert`, `opal-assets-silver-blackdiamond`, `opal-assets-silver-eclipse`, `opal-assets-silver-etf`, `opal-assets-silver-orion`, `opal-assets-silver-schwab`, `opal-assets-silver-smartx`, `opal-cot-served-guard`, `opal-cot-value-parity`, `opal-globgrph-incremental-events`, `opal-inf-served-guard`, `opal-inf-value-parity`, `opal-infrastructure-alerts`, `opal-infrastructure-monitor`, `opal-keyword-drilldown-generator`, `opal-market-rsi-tiered-generator`, `opal-news-layer3-curation`, `opal-portal-fear-greed-fetcher`, `opal-portal-volatility-fetcher`, `opal-smartx-ingestion-pipeline`, `opal-trending-image-generator`, `opal-trending-topics-portal-publisher`, `security-sweep-comprehensive`, `seeking-alpha-analysis-coordinator`, `seeking-alpha-news-coordinator`, `smartx-assets-daily-pull`, `smartx-ec2-autostart`, `smartx-jwt-refresher`, `smartx-model-monthly-pull`, `smartx-rest-pull`, `trade-parquet-batch-export`, `wsb-49f-model-aua-daily`, `wsd-49f-partner-held-etf-daily`, `yang-refresh-fred-cache`, `ycharts-session-capture`, `ycharts-session-probe`.

## 12. Priority consequences

1. **Fix or explicitly hold `opal-assets-ingest-mirror` before the 18:30 ET Cottonwood fire.** The new schedule is configured correctly but targets a function currently failing every invocation.
2. **Regenerate `trigger-map.json` and make live identity and field parity a CI gate.** The 13-row drift is concrete proof that denominator parity is insufficient.
3. **Repair deployment provenance for the ten post-baseline Lambda updates not bound to current source-map commit/time.** A source path without a deploy identity cannot answer what code actually ran.
4. **Pin graph ECS targets to immutable image digests.** The current tag did not move in this interval, but the baseline provenance defect remains structurally open.

## 13. Method and limits

- Parsed and re-counted all 154 trigger rows and 115 resource rows in the immutable baseline.
- Token-walked three EventBridge Rule pages and five Lambda pages; enumerated all 139 Rule target sets; fetched all 16 Scheduler schedule details.
- Compared mapped fields only: service/name, state, schedule expression, timezone, event pattern, target ARN/id/input/role/retry/dead-letter/service parameters, immediate resource identity, Lambda runtime/source-map provenance, ECS task definition/image, and CodeBuild source/image.
- Queried Rule and Lambda CloudWatch metrics over the exact post-baseline interval. Resource metrics are all-caller counts. Rule metrics are dispatch counts, not target success.
- Scheduler per-schedule invocation attribution remains unavailable. Group attempts are not allocated across schedules.
- EventBridge UTC crons are shown in both EDT and EST. `America/New_York` schedules preserve the stated Eastern wall clock through DST.
- Decommission findings were cross-checked against live resource existence and the applied change ledgers, not inferred from Git alone.
