**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Basis:** read-only measurement at repo `0f1caafb1d`; scratch artifacts named below were NOT committed.

# LGIC placeholder population -- HEAD recount, family reproduction, A5 sub-clustering

**Author:** 4.0.0_SA_CRO (fork, read-only measurement). Nothing in the repo was edited or committed.
**Scratch artifacts (same dir):** `NAMING_CENSUS_REPORT.head.md` (HEAD census), `not_judged_head.json`,
`census_added_raises.json`, `fam.py`, `fam2.py`, `cluster.py`, `a5_clusters.json`, `a5_dump.txt`.

## 0. Vintages

| number set | source | vintage |
|---|---|---|
| R13 / R18 (the brief's basis) | `NAMING_CENSUS_REPORT.r13.md` rows; R18 record @`659dca28f3` | estate 2026-09-19 05:56:38Z, registry `9f4a569d7a54b53c` |
| **HEAD (this run)** | `python lib/opal_naming.py census --live --repo --budget 600 --not-judged <scratch> --report <scratch>` | **repo `0f1caafb1d`**, run 2026-09-21T16:51:27Z, estate stitch 2026-09-21 12:15:51Z, **registry `1a6a3b1ebc808545`** (includes the R4/harvest landing `1675a8f631`) |

An earlier HEAD run at `3467f1d265` (registry `9f4a569d7a54b53c`, before `1675a8f631`) gave identical counts;
it is kept as `NAMING_CENSUS_REPORT.head_3467f1d265.md`.

**The census needed one scratch card to complete.** The first pass STOPPED at its first RAISE after 3060 judged:
repo S3Key `firms/{firm}/generations/{export_id}/receipt.json` (`infra/aws/lambda/investor-reporting/export/entry.py:78`,
"K1: segment 1 'firms' is neither a source nor a tier") -- a NEW raise since R13 (IRPT export code). It was carded
in a SCRATCH copy of `NOT_JUDGED_R13.json` only so the run could finish; that is not a disposition. Pass 2: COMPLETE.

## 1. Population at HEAD

```
judged          3286   (R13: 3264)   live 1722+131 of 1853 nameable, repo 1564+332 of 1896
population      1303   (R13: 1303)   rows whose canonical carries a literal {token}
{system} rows   1119   (R13: 1119)   the registry-assigning population
distinct {system} (current,type,plane) keys: 932 at R13, 932 at HEAD, set-identical
distinct {system} NAMES: 532   (rows double-count: most resources appear on BOTH the live and repo plane)
tokens: system 1119, scope 122, cadence 108, source 85, snap 7, dim_name 5, firm 1, d 1, dc 1
verdict of all 1119 {system} rows: OUT-OF-PATTERN
```

**The population has not moved since R13**; the 22 extra judged rows at HEAD all resolve without a placeholder.

## 2. The brief's families -- reproduced to within ONE row

The brief does not record its classification rule. My reconstruction (leading token = `current.lstrip('/')`
split on `-` only, case-sensitive):

| family | rule | brief | HEAD (mine) | distinct names |
|---|---|---|---|---|
| A2 log group | `current` starts with `/aws/` | 67 | **67** | 54 |
| A1 firm | leading token in {`bd`,`inf`,`cot`} | 217 | **217** | 118 |
| A3 AWS service | leading token in {s3, cloudwatch, lambda, secretsmanager, cloudfront, kms, sns, ssm, ecs, ses, rds} | 175 | **174** | 51 |
| A4 opal* | leading token lower-cased starts `opal` | 10 | **10** (all `opalinvest-*`, 5 names) | 5 |
| A5 rest | everything else | 650 | **651** | ~304 |

- Splitting on `[-_/.]` instead gives A1=220 (it pulls in 3 `inf/otp-relay/token` SECRET rows) -- so the brief split on `-`.
- The brief's A5 head (`find 56 . cross 55 . invoke 24 ... ec2 12 ... CloudWatchLogs 11 ...`) matches mine
  **exactly**, which fixes that `ec2` and `CloudWatchLogs` were NOT in the brief's A3 list.
- The one-row A3 gap: the brief's exact service list is unrecorded; one 1-row token (plausibly `codebuild`,
  `ecr`, `ddb` or similar) sat in its A3. Distinct A5 tokens: brief 155, mine 157. Immaterial to any decision.

## 3. THREE FINDINGS THAT CHANGE WHAT THE RULINGS MOVE (read before acting on rulings 2-4)

Read at `lib/opal_naming.py` @`0f1caafb1d`:

**(a) Ruling 4 (log groups graded after `/aws/<svc>/` only) is ALREADY the grader's behavior.**
`_grade_log_group()` (:1319-1344) splits off `/aws/<service>/` and grades only `rest_s` through
`_grade_resource()` (:1341). The 67 A2 rows carry `{system}` because their TAIL has no system:
`/aws/lambda/access-anomaly-scanner -> /aws/lambda/{system}-access-anomaly-scanner-lambda`. Tail leading tokens:
bd 19, us 5, find 4, shared 4, semantic 3, inf 3, access/auth/cost/daily/deck/ec2/finbert/historical/keyword/
opalinvest/public 2 each, ... **So ruling 4 moves 0 rows as written; A2 dissolves INTO the A1/A5 families by tail.**

**(b) Ruling 2 (bd/inf/cot are a firm field, not a system) is ALREADY the grader's behavior too.**
`Vocab` puts every scope token and `bd` into the refused set V3 (:1037-1038); `_slots()` then sends a firm-led name
to the R1.d branch (:1186-1200) and separately extracts the firm into the SCOPE slot (:1203-1212). The canonical
forms show it: `bd-gold-qa-runner-forgotten -> {system}-49f-gold-qa-runner-forgotten-alarm`. The firm is already
read as a firm; the row is still `{system}` because **nothing names which SYSTEM a firm-pipeline resource belongs
to** (second tokens: gold 61, exporter 17, allocation 15, bronze 12, silver 10, assets 8, api 8, s3 8, ...).
**So ruling 2 moves 0 rows unless it is read as a GRAMMAR change** -- e.g. "a firm-scoped pipeline resource takes
no `{system}` slot", or a registry default system for firm pipelines. That reading is not in the ruling's text.

**(c) Ruling 3 (an AWS service name is never a `{system}`) needs a real grader change** -- the only one of the
three that moves rows as written (174 at HEAD). Mechanism in s.5.

**(d) Every A5 leading token is ALREADY on a `systems.json` refused list.** First-word class across the 651 A5 rows:
generic_noun 389, workstream_code 117, purpose_word 95, not refused 50 (the 50 are PascalCase/compound words and
library layers: `bdpipelinepermissions`, `pandas`, `openpyxl`, `pyiceberg`, `security`, `sqsconsume`, `daily`,
`demo`, ...). A5 is not "unknown tokens": each token was deliberately refused AS a system, and the open question per
resource is WHICH registered (or new) system owns it. Note `purpose_word` = {cross, s3, cloudwatch, invoke,
secretsmanager, lambda, kms, secrets} -- `cross`, `invoke`, `secrets` sit in the brief's A5 but are the same class
as A3.

## 4. A5 sub-clustering -- 21 candidate families + 8 unplaced tokens (HEAD, 651 rows)

Grouped by reading the names and checking the declaring file; "rows" counts both planes, "names" is distinct.
Candidate owner = an existing `systems.json` key where one fits, else NEW. These are PROPOSALS for Andrew's card.

| # | candidate family -> candidate system | rows | names | leading tokens | examples | evidence |
|---|---|---|---|---|---|---|
| F01 | insurance prospecting (FIND) -> NEW (`find` is a REFUSED project code, systems.json `find_basis`) | 61 | 33 | find, brightdata, nopecha/api, google (cse-config) | find-insure-crawl-web; find-dualbiz/bright-data/serp; brightdata-api-key | `data/find/`; FIND_INSURE TOs |
| F02 | firm separation (cross-firm deny/read) -> `firmsep` | 59 | 6 | cross, CotServedAndSourceRead, InfServedAndSourceRead | cross-firm-bucket-deny; cross-firm-secret-deny; InfServedAndSourceRead | `infra/aws/terraform/inf-pipeline/cross-firm-deny.tf` |
| F03 | news / semantic intelligence -> NEW (`news`?) | 41 | 25 | semantic, finbert, trending, keyword, layer3, Layer3EC2Policy, Semantic*, CodeBuildSemanticClusteringPolicy, codebuild | semantic-clustering-lambda-build; finbert-batch-processor; keyword-intelligence-generator | `infra/aws/terraform/news-pipeline/`; `infra/aws/lambda/news_semantic_clustering/` |
| F04 | market data / market overview -> NEW | 50 | 25 | market, historical, fear, volatility, yield, MarketRSITieredPolicy, price_discovery, yfinance, massive, aaii/credentials, conferenceboard/credentials | market-rsi-tiered-daily; historical-prices-fetcher; fear-greed-daily-update | `infra/aws/terraform/market-overview/`; `infra/aws/lambda/historical-prices-scheduler/` |
| F05 | cloud-ops hygiene -> NEW (cloudops) | 44 | 25 | ec2, infrastructure, cost, CostAnomalyScannerPolicy, InfrastructureSnapshotPolicy, EC2RuntimeMonitorPolicy, self, describe, moltbot | ec2-auto-shutdown-enforcer; infrastructure-snapshot-daily; cost-anomaly-scanner | `infra/aws/lambda/ec2-auto-shutdown-enforcer/`; `.../infrastructure-daily-snapshot/`; `.../cost-anomaly-scanner/` |
| F06 | security / OPSEC -> NEW | 12 | 6 | access, AccessAnomalyScannerPolicy, OPSEC, security | access-anomaly-scanner; OPSEC-auth-throttled; security-scanner-deps | `infra/aws/terraform/opsec/`; `.../security-ops/`; `infra/aws/lambda/access-anomaly-scanner/` |
| F07 | critical-surface / parity guards + monitor role -> `globgrph` (surface alarm) / NEW | 29 | 10 | PublishSurfaceAlerts, SurfaceCheckArtifactPut, ServedKeyGuardS3, ExecIncrParityFailure, incrparity, Monitor* (5) | PublishSurfaceAlerts; ServedKeyGuardS3; MonitorLogsRead | `infra/aws/terraform/globgrph/item2c_surface_alarm.tf`; `.../modules/served-guard/`; `.../shared-infra/infra-monitor.tf` |
| F08 | estate graph producers -> `globgrph` | 58 | 29 | Stitch*, Drift*, DeriveRunner*, BoundedDeriveReadOnly, Fedobs*, ResourceSummariesProducer*, CseProducer*, Trino*, Nessie*, S3WarehouseWrite, pyiceberg | StitchProducePerms; DeriveRunnerS3; TrinoWarehouseReadOnly | `infra/aws/terraform/globgrph/{stitch-produce,cse_producer,fedobs,trino}.tf` |
| F09 | COMP_LEARNS producer -> `globgrph` or NEW | 6 | 3 | CompLearns* | CompLearnsServedWrite | `infra/aws/terraform/globgrph/comp_learns_producer.tf` |
| F10 | exec summary -> `advi` | 11 | 7 | exec | exec-summary-generator; exec-summary-advisors-processed-ceiling | `infra/aws/terraform/exec-summary/` |
| F11 | desk/fabric tools (daily sprint, agenda, workspace sync) -> NEW or `estate` | 12 | 7 | daily, workspace | daily-sprint-generator; daily-agenda-generator; workspace-sync-lambda-role | `infra/aws/terraform/daily-sprint-generator/` |
| F12 | deck generation -> NEW | 8 | 4 | deck | deck-generation; deck-generation-deps | `infra/aws/terraform/deck-generation-pipeline/` |
| F13 | portfolio management tool -> NEW (or `mdpf`) | 13 | 8 | portfolio, PortfolioExportPolicy, PortfolioExcelGenerator, openpyxl | portfolio-export-lambda-role; PortfolioExcelGenerator-Errors | `infra/aws/terraform/portfolio-management/` |
| F14 | firm pipelines (BD/49F gold runners, bronze/gold triggers, 49F pulls, consolidation) -> SAME QUESTION AS A1 | 55 | 27 | consolidation, start, BDPipeline*, ecs/bd, monolith, bronze, gold, wsb, wsd, send, pipeline, runner, ddb, demo, etf | consolidation-gold-runner; BDPipelinePermissions; wsb-49f-model-aua-pull-daily | `infra/aws/terraform/{consolidation-gold-runner,bd-pipeline}/`; wsb/wsd -> `infra/aws/lambda/mdpf-pipeline/` (`mdpf`); monolith -> `infra/aws/terraform/canonical-schwab-ec2/` (`schwab`) |
| F15 | partner ETL ops -> NEW or `advi` | 14 | 7 | partner, partners, PartnerEtlOpsConsumerPolicy, PartnerIdentityReadPermissions | partner-etl-ops-sqs-consumer; partners-lambda-role | `infra/aws/terraform/partner-etl-ops-alerts/`; `.../partners-api/` |
| F16 | portal auth / advisor API / OTP -> `advi` or `gateway` | 30 | 13 | auth, public, shared, jwt, user, sms, twilio/*, x, inf/otp | auth-validator-edge; shared-advisor-router; x-advisor-role | `infra/aws/lambda-edge/shared-advisor-router/index.mjs`; `infra/aws/terraform/portal-auth/`; `.../shared-infra/opal-portal-lambda-role.tf` |
| F17 | trading-ops tools (data refresh, security scanner, quartz) -> NEW | 21 | 11 | data, sscn, quartz | data-refresh-time-machine-invoke; sscn-s3-access; quartz-si2-spike-role | `infra/aws/terraform/data-refresh/main.tf`; `.../security-scanner-pipeline/iam.tf` |
| F18 | CI / GitHub -> NEW | 10 | 6 | github | github-actions-runner; github-token | `infra/aws/terraform/github-actions-runner/` |
| F19 | LLM vendor credentials + SDK layer -> NEW vendor keys (anthropic/openai are refused as generic nouns) | 10 | 4 | anthropic, openai, ai/claude | anthropic-api-key; ai/claude-api-key | -- |
| R1 | **RULE candidate**: inline/console policy names (verb or AWS noun, no system in the name) | 79 | 32 | CloudWatchLogs, SecretsManagerAccess, S3Access, SQSConsume, RecheckQueue, DynamoDBAccess(+Policy), AdditionalPermissions, LambdaSelfInvoke, ecsTaskExecutionRole, EventsRunECSTask, FargateTriggerPermissions, IncrementalUpdaterSNS, invoke (24), secrets, events, ecr, by, Projection* | CloudWatchLogs; invoke-publisher-fanout; by-role | same class as A3 (`purpose_word` holds invoke/secrets) |
| R2 | **RULE candidate**: library-named Lambda layers | 5 | 2 | pandas | pandas-pyarrow-layer | `_slots()` already sends every LAMBDA_LAYER to R1.d (:1186) |

**Unplaced: 23 rows, 8 tokens.** `gldinc` 11 (bd-pipeline canary, `infra/aws/terraform/bd-pipeline/gldinc-ss4c.tf` --
belongs with F14), `outset` 4 (NFRA_OUTSET drift publisher -- plausibly F08), `unknown` 2 (unknown-topic/-alarm),
`multi` 2 (multi-threadv2 secret), `test` 1 (test-alarm), `quo/api` 1, `google/andrew-goldengate/credentials` 1,
`google/officialmadeaux/credentials` 1. The last three look like personal/test credentials, not system-owned.

**Decision count, as a proxy:** 21 families + 8 unplaced tokens is ~29 decision points for A5, of which ~9 map to
an EXISTING system key (firmsep, globgrph x3, advi x2-3, mdpf, schwab) and 2 are rule candidates. Still a proxy.

## 5. The 15 template-variable rows -- they are .format() TEMPLATES, not shipped names

`current` carries a brace in 15 rows at HEAD (all repo-plane S3Key). **At the sites read, the brace is a
`str.format()` placeholder expanded at runtime**, so the brief's "something is shipping resource names with an
unexpanded placeholder" is not supported at those sites: `rate_limiter.py:37` is used as
`_STATE_KEY_FMT.format(dim_name=dim_name)` (:129); `mdpf-feeder-trigger/lambda_function.py:93/:100` are used as
`WSC_GATE_KEY.format(d=run_date)` / `WSE_GATE_KEY.format(dc=run_date_compact)` (:155-156, :167-168). The other
sites are constants named `*_TPL`/`*_FMT` and were NOT read at their use sites. **Remedy class: the repo-plane
census should treat a `{var}` in a key template as a variable slot -- an instrument fix, not an application fix.**

| rows | current | verdict | emitting site(s) (census rows carry no `where`; matched by string) |
|---|---|---|---|
| 4 | `bronze/positions/{snap}.parquet` | OUT-OF-PATTERN | `infra/aws/lambda/inf-pipeline/inf-api-positions/convert_orion_api_to_silver.py:651`; `inf-api-reps/...:651`; `inf-api-txn/...:627`; `inf-accounts-v2-daily/...:729` |
| 1 | `bronze/positions/{snap}.jsonl.gz` | OUT-OF-PATTERN | `infra/aws/lambda/inf-pipeline/inf-silver-chain/convert_orion_api_to_silver.py:785` (and `data/inf/scripts/silver/convert_orion_api_to_silver.py:785`) |
| 1 | `bronze/assets/{snap}.parquet` | OUT-OF-PATTERN | `infra/aws/lambda/inf-pipeline/inf-api-assets-v2/convert_assets_v2_to_silver.py:43` |
| 1 | `silver/assets_v2/{snap}.parquet` | OUT-OF-PATTERN | same file `:44` (and `data/inf/scripts/silver/convert_assets_v2_to_silver.py:54`) |
| 5 | `orion/rate_limit_state_{dim_name}.json` | **CONFORMANT** | `rate_limiter.py:37` in `infra/aws/lambda/inf-pipeline/{inf-accounts-v2-daily,inf-api-assets-v2,inf-api-positions,inf-api-reps,inf-api-txn}/` (and `data/inf/scripts/bronze/rate_limiter.py:37`, `data/inf/manual_api/run_backfill_orchestrator.py:55`) |
| 1 | `platinum/{firm}/ownership_map.json` | OUT-OF-PATTERN | `infra/aws/lambda/investor-reporting/_authz/loaders.py:32` |
| 1 | `gold/eclipse/{d}/_meta/gold_complete.json` | OUT-OF-PATTERN | `infra/aws/lambda/mdpf-pipeline/mdpf-feeder-trigger/lambda_function.py:93` |
| 1 | `schwab/silver/rps/date={dc}/data.parquet` | OUT-OF-PATTERN | same file `:100` |

## 6. The grader: where `{system}` is emitted, and what the rulings would touch

**Emit site:** `lib/opal_naming.py:1187` @`0f1caafb1d`, in `_slots()` (:1164-1215):
`elif t1 in v.v3 or typ == "LAMBDA_LAYER":  # R1.d, R1.e` -> `sysv, placeholder = "{system}", True`; it then scans
later tokens for a system (:1188-1196) and finally the `resources.json` `(name, type)` row (:1197-1200). V3 is built
at :1037-1038 from every `systems.json` `refused_keys` list PLUS every scope token and `bd`.

**What a change for the three rulings would touch (not made):**
1. **AWS service name (ruling 3, the only one that moves rows as written):** in `_slots()`, when `t1` is a service
   name (today inside `refused_keys.purpose_word`, which also holds the non-service words cross/invoke/secrets) and no
   later token resolves, return a new "no system applies" outcome instead of `{system}`; `grade()` then needs a new
   verdict value for it. A new verdict value is a SCHEMA change (Rule 24 record + token census required).
2. **bd/inf/cot (ruling 2):** already handled as SCOPE at :1203-1212. Moving rows needs a grammar decision the ruling
   does not state: a firm-scoped name may omit `{system}`, or a registry default system for firm pipelines.
3. **Log groups (ruling 4):** already implemented in `_grade_log_group()` :1319-1344; no change moves rows.
4. **Parity carriers:** the grader writes `infra/aws/terraform/modules/opal_name/generated_locals.tf` and its tests
   `.../tests/vectors.json` + `opal_name.tftest.hcl` (:62-64, :105-107), so any grammar change must regenerate those
   and pass their self-tests; the grammar prose is in `infra/logic/` (GRADING_RULE / NAMING_SCHEMA).
5. **Lane:** `lib/opal_naming.py` and `infra/aws/terraform/modules/opal_name/**` are outside the CRO's
   `infra/logic/**` lane; the `systems.json` / `resources.json` rows for A5 are inside it.
