# name_rulings.json -- registry-owner rulings for the ruling_ref backfill (111 rows)

**By:** `4.0.0_SA_CRO~Z`, a lane of `4.0.0_SA_CRO`, the owner of `infra/logic/registry/**` (CTO ruling 106332). Written
2026-10-16 ~10:4xZ.
**Asked by:** `1.0.0_SA_CTO~Z` msg 34907.
**Input:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~115/RULING_REF_UNRESOLVED.json`. It was cited
@ecd2aad5d0 and read at HEAD; the file is byte-identical between ecd2aad5d0 and HEAD. It lists 111 rows.
**Why:** CVO verdict 6495 (`org/missions/D14/LGIC/LGIC_ENFORCE/ledger/CTO_AFTER_THE_FACT_REVIEW_NAMING_GATE_NAME_RULINGS_20261016.md`
@72cc8fe6af) says a row's `ruling_ref` must name a record that exists at a commit.

## Disposition of the 111 rows

| Disposition | Rows | ruling_ref |
|---|---|---|
| An existing record ruled the row | 27 | `org/tier1_exec/4.0.0_SA_CRO/deliverables/REGISTRY_ROUND9_RULINGS_20261009.md@cc85ec34f5c1a1555f6e8895a864b69f043e8f4e` (R9-1 trade, 22 rows; R9-2 opal-data-imo, 1; R9-3 security, 4) |
| An existing record ruled the row | 4 | `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPLGTW_CL7_NAMING_GATE_AND_MCPINDEX_AI_CLASSIFIED_20261016_Z.md@d97ea3ae82822d870d238ea80750e92b7878d912` (section 1 names all four Black Diamond identifiers) |
| Ruled in THIS record (R-Z1 to R-Z8) | 79 | this file at its landing commit |
| NOT RULED | 1 | none; see below |

Each row's disposition is in the appendix. The machine map for the backfill is
`NAME_RULINGS_BACKFILL_RULING_REFS_20261016.json`, beside this file.

**Why the other rows needed a new ruling.** Their introducing commits each carry a record, and none of those records rules
the rows:
- Round 5 (`331e3fe609`) has no record. It rested on items S1, S2 and S4 of the round-4 analysis @095d99c984, and that
  analysis delegates the ruling to this seat; it does not make it.
- Round 8 (`REGISTRY_ROUND8_RULINGS_20261009.md`) and round 10 (`ROOT_MAP_ROUND10_LANDED_20261009.md`) record the rows as
  WRITTEN. Their rulings cover other rows.
- LGIC_CANON step 13 (`8f630a5978`) is a worker's result under a task order that asked for drafts.

A row citing its own write would be the "lift by assertion" the CVO refused. So the rows are ruled here, on measurement
made today.

## Measurements this record rests on (box/sitez, 2026-10-16 ~10:3xZ)

- **Grader:** `lib/opal_naming.py grade()`. Each of the 57 canonicals among the 111 rows grades CONFORMANT, 57 of 57.
- **Control** (the grader can refuse): `opal-data-ycharts` and `news-api-700am` grade OUT-OF-PATTERN. `NewsIngestionPolicy`
  grades OUT-OF-PATTERN and offers `news-ingestion-policy`. `cache-control-injector` raises R1.f (`cache` is in no
  vocabulary).
- **scopes.json** holds 15 scope keys, none of them `news`, `pm`, `portfolio`, `smartx`, `trade` or `astn`.
  **systems.json** `unresolved` holds `astn` and `trade`.
- **news schedules:** `infra/aws/terraform/news-pipeline/eventbridge.tf:25-153` holds 21 schedule expressions, each a
  once-a-day cron. Line 163, the trending rule, fires twice a day.

## Rulings

**R-Z1. The 56 canonical rows are ADOPTED.** These are the 57 canonicals less `opal-data-ycharts`. For each, the system
word is the owning root's system (news for D8's root, portal, secops, advi, and inf through advi under round-8 ruling 2).
Each canonical is the name the grader prints from that word, and each grades CONFORMANT.
- `/aws/events/inf-gold-dispatch-release-audit` takes the function word of its event rule, as round-8 ruling 2 ruled for
  that rule.
- The 21 news schedules take `-daily` because each fires once a day (measured above).
- **Not ruled here:** the time words in those names (`700am`, `845am`, ...) do not match their crons. For example,
  `news-api-700am` fires at 10:00 UTC (eventbridge.tf:25). A time word is the owner's function word, so the canonical
  keeps it. Correcting it is the news product owner's (D8) to do, and it does not touch the grammar.
- A row authorizes no rename. Renaming is each root owner's act under R19.

**R-Z2. No scope row: none_owed ADOPTED.** Rows: `opal-data-news-v2`, `opal-data-news-av`, `opal-data-pm`,
`opal-data-portfolio`. A data bucket is `opal-data-{scope}`, and scopes.json has no row for the news product or for the
portfolio-management application. So no correct name exists to print. Printing `opal-data-news`, the grader's offer, would
name a bucket nobody registered. The row leaves when the owner registers the scope.

**R-Z3. Unresolved system token: none_owed ADOPTED.** Row: `astn/kimi/api-key`. A secret's name begins with its system.
`astn` is unresolved in systems.json, and grade() raises R1.c. This follows the trade precedent of R9-1.

**R-Z4. Not a resource: none_owed ADOPTED.** Rows: `calculated-group` (an Orion operation word,
`orion_adapter.py:36-38`), `unknown-topic`, `unknown-alarm` and `test-alarm` (code placeholders, never resources). There
is nothing to rename. This is round-4 item S4's "a pattern is printed as a pattern".

**R-Z5. No cadence word: none_owed ADOPTED.** Rows: `news-trending-analysis-daily` (twice a day), `finbert-scoring-post-ingestion`
(eleven hours a day), `ycharts-session-capture-schedule` (every 72 hours) and `irpt-intake-poll` (15 minutes inside a daily
window). The cadence words of E1_CADENCE_RULES_RATIFIED have no word for these. The grader prints a `{cadence}` placeholder,
except for `news-trending-analysis-daily`, which it reads as CONFORMANT on its `-daily` ending. The name keeps its form until
the cadence set rules one.

**R-Z6. Outside the log-group grammar: none_owed ADOPTED.** Rows: `/aws/vendedlogs/pipes/opal-globgrph-projection-worker`
and `/opal/github-actions-runner`. grade() raises L2 on each: the first segment gives no resource type. The name stays
until the grammar rules vended-logs and custom paths.

**R-Z7. Retired SmartX stores: none_owed ADOPTED.** Rows: `opal-data-smartx-v2` and `opal-data-smartx`.
- `opal-data-smartx-v2` holds a dead exporter's output, frozen 1 June
  (`smartx_ingestion_pipeline/compute_account_distribution.py:58-62, 83-84`). The live feed is `opal-data-mdpf`.
- `opal-data-smartx` is only a fallback default that no live path takes (`config.py:105-112, 208`).
- The basis is the dead store. The planned decommission ("smartx R5") is cited from code, not measured.

**R-Z8. Served and config keys: none_owed ADOPTED.** Rows: `config/yahoo_safe_tickers.txt` and the five
`platinum/advisors|clients/{*}/...` keys.
- Re-partitioning a served key changes a path that pages read by exact key. That is a served-output act (CLAUDE.md
  NEVER-1), never an answer the naming check prints.
- The ticker list's tier is set when its bucket moves.

## NOT RULED (1 row)

- **`opal-data-ycharts` (S3_BUCKET), canonical `opal-data-irpt`.** The canonical holds only if the evidence stays in ONE
  product bucket. Whether it does or moves into each firm's bucket (R21) is open:
  `infra/logic/03_CONTRADICTION_REPORTS/IRPT_BCKEND.md` row 3 leaves it open with an R20 declaration as the other route.
  The row itself says "NOT DECIDED HERE".
- Ruling it would decide that tenancy question from a registry row. The question is IRPT_BCKEND's (D9), and an R20
  declaration needs Andrew's acknowledgment.
- The row needs a ruling_ref from that decision. Until then it carries none.

## Appendix -- every row

| # | name | type | disposition |
|---|---|---|---|
| 1 | `opal-data-ycharts` | S3_BUCKET | NOT RULED |
| 2 | `opal-data-news-v2` | S3_BUCKET | R-Z2 |
| 3 | `calculated-group` | IAM_GROUP | R-Z4 |
| 4 | `astn/kimi/api-key` | SECRET | R-Z3 |
| 5 | `/aws/events/inf-gold-dispatch-release-audit` | LOG_GROUP | R-Z1 |
| 6 | `news-api-700am` | EVENT_RULE | R-Z1 |
| 7 | `news-api-845am` | EVENT_RULE | R-Z1 |
| 8 | `news-api-1100am` | EVENT_RULE | R-Z1 |
| 9 | `news-api-100pm` | EVENT_RULE | R-Z1 |
| 10 | `news-api-345pm` | EVENT_RULE | R-Z1 |
| 11 | `news-api-400pm` | EVENT_RULE | R-Z1 |
| 12 | `news-api-500pm` | EVENT_RULE | R-Z1 |
| 13 | `news-api-600pm` | EVENT_RULE | R-Z1 |
| 14 | `news-api-745pm` | EVENT_RULE | R-Z1 |
| 15 | `news-api-900pm` | EVENT_RULE | R-Z1 |
| 16 | `news-api-1100pm` | EVENT_RULE | R-Z1 |
| 17 | `news-api-100am` | EVENT_RULE | R-Z1 |
| 18 | `news-api-300am` | EVENT_RULE | R-Z1 |
| 19 | `news-api-500am` | EVENT_RULE | R-Z1 |
| 20 | `news-rss-9am` | EVENT_RULE | R-Z1 |
| 21 | `news-rss-12pm` | EVENT_RULE | R-Z1 |
| 22 | `news-rss-3pm` | EVENT_RULE | R-Z1 |
| 23 | `news-rss-6pm` | EVENT_RULE | R-Z1 |
| 24 | `news-rss-9pm` | EVENT_RULE | R-Z1 |
| 25 | `news-rss-1am` | EVENT_RULE | R-Z1 |
| 26 | `news-rss-4am` | EVENT_RULE | R-Z1 |
| 27 | `news-trending-analysis-daily` | EVENT_RULE | R-Z5 |
| 28 | `news-ingestion-lambda-role` | IAM_ROLE | R-Z1 |
| 29 | `NewsIngestionPolicy` | IAM_POLICY | R-Z1 |
| 30 | `opal-news-lambda-role` | IAM_ROLE | R-Z1 |
| 31 | `news-dashboard-processor-role` | IAM_ROLE | R-Z1 |
| 32 | `news-dashboard-policy` | IAM_POLICY | R-Z1 |
| 33 | `news-sentiment-lambda-role` | IAM_ROLE | R-Z1 |
| 34 | `news-sentiment-permissions` | IAM_POLICY | R-Z1 |
| 35 | `semantic-news-lambda-role` | IAM_ROLE | R-Z1 |
| 36 | `semantic-news-permissions` | IAM_POLICY | R-Z1 |
| 37 | `news-trending-deps` | LAMBDA_LAYER | R-Z1 |
| 38 | `news-ingestion-scheduler` | LAMBDA | R-Z1 |
| 39 | `news-trending-analysis` | LAMBDA | R-Z1 |
| 40 | `opal-news-layer3-curation` | LAMBDA | R-Z1 |
| 41 | `news-semantic-clustering` | LAMBDA | R-Z1 |
| 42 | `semantic-news-layer3-curation` | LAMBDA | R-Z1 |
| 43 | `opal-news-ai-sentiment` | LAMBDA | R-Z1 |
| 44 | `/aws/lambda/news-ingestion-scheduler` | LOG_GROUP | R-Z1 |
| 45 | `/aws/lambda/news-trending-analysis` | LOG_GROUP | R-Z1 |
| 46 | `/aws/lambda/opal-news-layer3-curation` | LOG_GROUP | R-Z1 |
| 47 | `/aws/lambda/news-semantic-clustering` | LOG_GROUP | R-Z1 |
| 48 | `/aws/lambda/semantic-news-layer3-curation` | LOG_GROUP | R-Z1 |
| 49 | `/aws/lambda/opal-news-ai-sentiment` | LOG_GROUP | R-Z1 |
| 50 | `opal-news-secrets-read` | IAM_POLICY | R-Z1 |
| 51 | `finbert-scoring-post-ingestion` | EVENT_RULE | R-Z5 |
| 52 | `opal-data-news-av` | S3_BUCKET | R-Z2 |
| 53 | `opal-data-smartx-v2` | S3_BUCKET | R-Z7 |
| 54 | `opal-data-smartx` | S3_BUCKET | R-Z7 |
| 55 | `portal-origin-verify-secret` | IAM_POLICY | R-Z1 |
| 56 | `cache-control-injector` | LAMBDA | R-Z1 |
| 57 | `/aws/lambda/cache-control-injector` | LOG_GROUP | R-Z1 |
| 58 | `security-sweep-comprehensive` | EVENT_RULE | R-Z1 |
| 59 | `security-sweep-dedicated-role` | IAM_ROLE | R-Z1 |
| 60 | `SecuritySweepComprehensive` | IAM_POLICY | R-Z1 |
| 61 | `security-sweep-comprehensive` | LAMBDA | R-Z1 |
| 62 | `/aws/lambda/security-sweep-comprehensive` | LOG_GROUP | R-Z1 |
| 63 | `portal-time-machine-invoke-downstream` | IAM_POLICY | R-Z1 |
| 64 | `/aws/vendedlogs/pipes/opal-globgrph-projection-worker` | LOG_GROUP | R-Z6 |
| 65 | `opal-data-pm` | S3_BUCKET | R-Z2 |
| 66 | `opal-data-portfolio` | S3_BUCKET | R-Z2 |
| 67 | `/opal/github-actions-runner` | LOG_GROUP | R-Z6 |
| 68 | `ycharts-session-capture-schedule` | EVENT_RULE | R-Z5 |
| 69 | `irpt-intake-poll` | SCHEDULE | R-Z5 |
| 70 | `trade-security-identifiers` | DYNAMODB_TABLE | R9 (existing) |
| 71 | `trade-users` | DYNAMODB_TABLE | R9 (existing) |
| 72 | `opal-trade-submissions` | DYNAMODB_TABLE | R9 (existing) |
| 73 | `trade-submission-lambda-role` | IAM_ROLE | R9 (existing) |
| 74 | `trade-submission-policy` | IAM_POLICY | R9 (existing) |
| 75 | `trade-auth-handler` | LAMBDA | R9 (existing) |
| 76 | `trade-authorizer` | LAMBDA | R9 (existing) |
| 77 | `trade-dashboard-api` | LAMBDA | R9 (existing) |
| 78 | `trade-identifier-cache` | LAMBDA | R9 (existing) |
| 79 | `trade-parquet-batch-export` | LAMBDA | R9 (existing) |
| 80 | `trade-submission-handler` | LAMBDA | R9 (existing) |
| 81 | `trade-workflow-handler` | LAMBDA | R9 (existing) |
| 82 | `/aws/lambda/trade-auth-handler` | LOG_GROUP | R9 (existing) |
| 83 | `/aws/lambda/trade-authorizer` | LOG_GROUP | R9 (existing) |
| 84 | `/aws/lambda/trade-dashboard-api` | LOG_GROUP | R9 (existing) |
| 85 | `/aws/lambda/trade-identifier-cache` | LOG_GROUP | R9 (existing) |
| 86 | `/aws/lambda/trade-parquet-batch-export` | LOG_GROUP | R9 (existing) |
| 87 | `/aws/lambda/trade-submission-handler` | LOG_GROUP | R9 (existing) |
| 88 | `/aws/lambda/trade-workflow-handler` | LOG_GROUP | R9 (existing) |
| 89 | `opal-data-trade-submissions` | S3_BUCKET | R9 (existing) |
| 90 | `trade-pipeline-ses-bounces` | SNS_TOPIC | R9 (existing) |
| 91 | `trade-pipeline-ses-complaints` | SNS_TOPIC | R9 (existing) |
| 92 | `opal-data-imo` | S3_BUCKET | R9 (existing) |
| 93 | `opal-data-security` | S3_BUCKET | R9 (existing) |
| 94 | `opal-data-security-access-logs` | S3_BUCKET | R9 (existing) |
| 95 | `opal-data-security` | S3_BUCKET_POLICY | R9 (existing) |
| 96 | `opal-data-security-access-logs` | S3_BUCKET_POLICY | R9 (existing) |
| 97 | `F49ServedAndSourceRead` | IAM_POLICY | R-Z1 |
| 98 | `NewsSemanticClusteringAccess` | IAM_POLICY | R-Z1 |
| 99 | `unknown-topic` | SNS_TOPIC | R-Z4 |
| 100 | `unknown-alarm` | CW_ALARM | R-Z4 |
| 101 | `test-alarm` | CW_ALARM | R-Z4 |
| 102 | `config/yahoo_safe_tickers.txt` | S3Key | R-Z8 |
| 103 | `platinum/advisors/{*}/positions.json` | S3Key | R-Z8 |
| 104 | `platinum/clients/{*}/concentration.json` | S3Key | R-Z8 |
| 105 | `platinum/clients/{*}/mix_timeseries.json` | S3Key | R-Z8 |
| 106 | `platinum/clients/{*}/summary.json` | S3Key | R-Z8 |
| 107 | `platinum/clients/{*}/views.json` | S3Key | R-Z8 |
| 108 | `bd_account_id` | hand-kept carrier | CTO ruling s.1 (existing) |
| 109 | `bd_account_number` | hand-kept carrier | CTO ruling s.1 (existing) |
| 110 | `fact_bd_allocation` | hand-kept carrier | CTO ruling s.1 (existing) |
| 111 | `market_value_profile` | INSTANCE_PROFILE | CTO ruling s.1 (existing) |

Rows are in the order of RULING_REF_UNRESOLVED.json.
