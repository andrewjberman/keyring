# P3 groundwork: Cottonwood back-end census and the portfolio-group read

**archetype:** EXPLORE

From `4.0.0_SA_CRO~DELL1` to `1.0.0_SA_CTO~DELL1`, on msg 5671 (due Oct 17). Read-only; nothing was written outside
this note. Everything was read on 2026-10-14 between 18:15Z and 18:40Z.

Starting record, not redone: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~82/PLAN_COTTONWOOD.json`
(read at 12:31Z; 2 buckets inspected, 28 Lambda configurations).

Andrew's words, as relayed (record `ANDREW_DIRECT_20261014_173xZ_DELIVERABLES_FOUR_PRIORITIES_AND_DATES.md`, 286.9-304.3 s):
"cottonwood, we need to establish their back-ends data. We need to check the portfolio group because I believe that is
how they actually are dividing up what clients go to what portfolios."

## Answer to (2) first: portfolio group divides ADVISORS, not portfolios

- **Where it lives:**
  - Black Diamond datamining saved query 270648 (template `data/cot/scripts/bronze/templates/account_attributes.json`),
    with columns `Portfolio Group, AccountID, Position Only, Account Supervised, Account Billable`;
  - landed daily as `s3://opal-data-cot/forwardfill_v2/account_attributes/ACCOUNT_ATTRIBUTES_DAILY_<date>.xlsx` (newest
    2026-10-13, landed 2026-10-14 11:31Z);
  - merged to `silver/account_attributes/` and joined into `gold/dimensions/accounts_dimension_latest.parquet` as
    `portfolio_group` (`data/cot/scripts/gold/A_00.accounts_dimension.py`).
- **Cardinality** (pull of 2026-10-13): **4 values** over 1,119 rows and 1,001 accounts.

  | Portfolio Group | Rows |
  |---|---|
  | Jay Rubottom | 405 |
  | Christa Bass | 239 |
  | Stephen Shipley | 239 |
  | No Advisor | 236 |

  - These are advisor books: three advisors plus an unassigned bucket. The pipeline already reads it that way
    (`data/cot/scripts/gold/D_05.supervised_split.py:9`, "the portfolio_group advisor-book split";
    `gold_validate_config.yaml:149`, "3 advisors + No Portfolio Group").
  - **117 accounts sit in two or three groups.** 116 of them pair an advisor with "No Advisor", for example Jay Rubottom
    + No Advisor 86 and Christa Bass + No Advisor 19. On 2026-08-19 only 1 account did.
- **Does it map clients to portfolios? No.** Cross-tab of the rebalancer strategy against portfolio group, over
  accounts joined on `fact_model_assignment.external_id` = datamining `AccountID` (990 of 995 join):

  | Strategy family | Christa Bass | Jay Rubottom | No Advisor | Stephen Shipley | not in pull |
  |---|---|---|---|---|---|
  | Opal Satellite NN | 146 | 123 | 55 | 74 | 0 |
  | Core \| Satellite NN | 8 | 31 | 9 | 25 | 0 |
  | Opal model (other) | 5 | 18 | 9 | 10 | 0 |
  | other strategy | 4 | 13 | 4 | 15 | 0 |
  | unassigned (`--`) | 75 | 219 | 150 | 115 | 5 |

  Each group spans many strategies: 19 (Bass), 37 (Rubottom), 26 (No Advisor) and 29 (Shipley) distinct strategies. A
  group does not determine a portfolio.
- **What does map clients to portfolios:** the Black Diamond **rebalancer** assignment.
  - Data: `s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_model_assignment/date=<d>/data.parquet`, column
    `strategy_name` (`program_name` has 2 values).
  - Writer: `cot-rebalancer-runner`, rule `cot-rebalancer-runner-daily`, cron(45 12 * * ? *).
  - Partition of 2026-10-14: 995 accounts, **56 distinct strategies, one per account** (no account has two), 0 closed.
    511 accounts read `--` (no strategy); the rest are mostly Opal Satellite 15 to 98 (Satellite 50 90, 60 89, 80 72,
    70 46, 40 29, ...) and "Core | Satellite NN".
  - This is the basis the MDPF account-distribution already uses: `basis: "bd-rebalancer-models +
    bd-datamining-values"`, source `.../fact_model_assignment/date=2026-10-14/`, 377 accounts in 12 models
    (`opal-data-assets/portal/gold/mdpf/cottonwood/account-distribution/2026-10-13.json`).
- **Sample (no client names; group level only):** the four labels and counts above, and the cross-tab. No account
  name, number or client field was printed or kept.

**Two defects found on the way (surprise-row candidates; not filed, read-only order):**

1. **`silver/account_attributes` stopped on 2026-08-20.** One partition, `2026-08-19.parquet`, plus its manifest, while
   the raw daily pull kept landing (88 objects, newest 2026-10-14). The template says it was "scheduled daily once the
   DS-side dict entries land", and the silver merge never went daily.
   - So the served accounts dimension (rebuilt 2026-10-14 11:33Z) carries portfolio groups as of August.
   - 60 of its 1,002 accounts have no `portfolio_group` at all; 59 accounts are new since 2026-08-19.
   - Any P3 view by advisor book reads an August split.
2. **The join key is not `account_id`.** The rebalancer `account_id` matches 0 datamining `AccountID`s; `external_id`
   matches 990 of 995. A consumer joining rebalancer to datamining on `account_id` silently gets nothing.

## Answer to (1): every Cottonwood back-end source

**Denominator.**
- Account buckets: 40. Fully listed: `opal-data-cot` (7,930 objects) and `opal-data-cottonwood` (7,638).
- Walked to depth 3 for a "cottonwood" or "/cot/" prefix: `opal-data-assets`, `opal-data-portal-v2`, `opal-data-etfs`,
  `opal-data-bd`. Found 7 prefixes; `opal-data-bd` holds none.
- One depth-4 prefix read by name: `opal-data-assets/portal/gold/mdpf/cottonwood/` (174 objects).
- Served AWS graph scanned for `cottonwood|opal-data-cot|/cot/`: 24 hits over 2,929 nodes (graph built 2026-10-14
  14:45Z). Its S3_BUCKET hits are only the two full-listed buckets.
- **Not covered:** a Cottonwood prefix deeper than level 3 in the four walked buckets, other than the one named, and
  any Cottonwood prefix in the other 34 buckets.
- Total objects counted: 35,675.

**Freshness basis.**
- S3 LastModified is land time, not data date.
- `lib/trading_calendar.py` `expected_last_trading_day` returns 2026-10-14 at the read, and
  `is_trading_day('2026-10-12')` is True. These feeds are T-1 by design, so the expected data date is **2026-10-13**.
- "Current" means landed on or after 2026-10-14 for a daily feed.

### Feeds (writers), from PLAN_COTTONWOOD `iam_env_column` and live rules

| Feed | Writer | Schedule / trigger | Lands in |
|---|---|---|---|
| BD datamining export: holdings, unrealized, realized, transactions, allocations, account_attributes | `cot-bd-session-trigger` -> exporter (SSM); `bd-cot-keepalive` every 15 min | session; then `cot-session-complete` -> `cot-bronze-complete` -> `cot-silver-complete` (S3 events) | `opal-data-cot` bronze/, forwardfill_v2/, silver/, gold/, platinum/ |
| BD rebalancer (model assignment) | `cot-rebalancer-runner` | cron(45 12 * * ? *) | `opal-data-assets/blackdiamond/cottonwood/` |
| Satellites registry and characteristics | `cot-satellites-registry-producer`, `cot-satellites-characteristics-producer` | cron(15 13) stamp-gated, cron(25 13), hourly reattempt | `opal-data-cot/platinum/satellites/` |
| MDPF gold for Cottonwood | `mdpf-gold-lambda` (Cottonwood gold writer role) | scheduled (~13:30Z) | `opal-data-assets/portal/gold/mdpf/cottonwood/`, `gold/mdpf_revamp/cottonwood/`, `opal-data-cottonwood/mdpf/cottonwood/`, `opal-data-portal-v2/platinum/mdpf/cottonwood/` |
| ETF ownership | `cot-etf-ownership-daily` | cron(30 10) | `opal-data-etfs/daily/cottonwood/` |
| Investor Reporting | `irpt-holdings`, `irpt-directory-refresh` (+ search, performance adapter readers) | scheduled | `opal-data-cot/investor-reporting/directory/`; `opal-data-cottonwood/irpt/cottonwood/` |
| Served guards | `opal-cot-served-guard` (on write), `opal-cot-value-parity` (hourly) | event / hourly | reads `opal-data-cot` platinum |
| Commonwealth custody (crosswalk input) | not read (Q below) | not read | `opal-data-assets/commonwealth/cottonwood/` |

### Stores, by family (objects; newest land time UTC; verdict)

`opal-data-cot` (legacy home; served to the portal):

| Family | Objects | Newest | Verdict |
|---|---|---|---|
| platinum/clients, firm, advisors, cottonwood, satellites | 1,134 / 12 / 3 / 1 / 3 | 2026-10-14 11:37 (satellites 13:26) | current |
| gold/entities, canonical, timeseries, client_timeseries, dimensions, positions_cube, views, artifacts, partner_analytics, single files | 2,138 / 494 / 177 / 681 / 132 / 175 / 5 / 15 / 3 / ... | 2026-10-14 11:33-11:37 | current |
| silver/holdings, unrealized, realized, allocations, transactions (+ manifests) | 89 / 141 / 121 / 141 / 124 | 2026-10-14 11:32-11:33 | current |
| forwardfill_v2/ (6 tables incl. account_attributes) | 1,103 | 2026-10-14 11:30-11:32 | current |
| bronze/<date>/ | 117 | 2026-10-14 11:32 | current |
| **silver/account_attributes** | 1 (+ manifest) | **2026-08-20 17:41** | **STALLED** (defect 1) |
| **silver/prices** | 90 | **2026-10-09 13:41** | **2 trading days behind** (10-12, 10-13 missing) |
| investor-reporting/directory | 27 | 2026-10-14 13:40 | current |
| logs/cot-exporter | 611 | 2026-10-14 11:37 | current (logs) |
| gold/validation, gold/client_performance.parquet, silver/cot_*.parquet, gold/logs | 15 / 1 / 3 / 1 | 2026-06-09 to 2026-07-09 | frozen legacy outputs; no reader read |
| code/, investor-reporting/qa | 161 / 5 | to 2026-10-09 / 2026-09-11 | code and one-off QA, not feeds |

`opal-data-cottonwood` (canonical home per the plan; IRPT writes here):

| Family | Objects | Newest | Verdict |
|---|---|---|---|
| irpt/cottonwood/platinum | 493 | 2026-10-14 14:17 | current |
| **irpt/cottonwood/gold** | 6,898 | **2026-10-11 16:07** | **1 trading day behind at least**; cadence not read |
| irpt/cottonwood/state, code | 77 / 1 | 2026-10-05 / 2026-10-09 | state and code, not feeds |
| mdpf/cottonwood/gold, state | 168 / 1 | 2026-10-14 13:31 / 2026-10-01 | current / state |

Other buckets:

| Root | Objects | Newest | Verdict |
|---|---|---|---|
| opal-data-assets/blackdiamond/cottonwood/ bronze, silver, gold, meta (rebalancer path) | 6,094 / 1,554 / 67 / 964 | 2026-10-14 11:45-13:30 | current |
| opal-data-assets/portal/gold/mdpf/cottonwood/ (account-distribution 37, account-units 35, aggregate-aua-timeseries 45, aum-metrics 37, category-views 20) | 174 | 2026-10-14 13:40 | current |
| opal-data-assets/gold/mdpf_revamp/cottonwood/ | 5 | 2026-10-14 13:31 | current |
| **opal-data-assets/commonwealth/cottonwood/** silver, bronze | 11,150 / 5 (3.2 GB) | **2026-10-09 12:41** | first landed 2026-10-06; cadence not read, so the gap cannot be called stale yet |
| opal-data-portal-v2/platinum/mdpf/cottonwood/ | 6 | 2026-10-14 16:34 | current |
| opal-data-etfs/daily/cottonwood/<date> | 86 | 2026-10-14 10:30 | current |
| opal-data-assets/_probe/blackdiamond/cottonwood, opal-data-etfs/daily/_archive/cottonwood | 1 / 1 | 2026-07-14 / 2026-09-10 | probe and archive |

Non-S3 back-ends (graph, not opened):
- DynamoDB `opal-partner-cottonwood`;
- secrets `blackdiamond/cot/credentials`, `/session`, `/otp-gateway-token`, `/otp-relay` (DECLARED), and
  `opal/bd/cottonwood/credentials` (LIVE-no-DECLARED, so it is live and Terraform does not declare it);
- role `irpt-core-firm-cottonwood` with policy `irpt-core-firm-cottonwood-prefix` (LIVE-no-DECLARED);
- CloudFront `EVTSA9VEHNZVH` with origin `opal-data-cot`.

**One structural observation:** Cottonwood's Black Diamond data comes in by **two separate paths**. The datamining
export lands in `opal-data-cot` and serves the portal. The rebalancer runner lands in
`opal-data-assets/blackdiamond/cottonwood/` and feeds MDPF and the client-to-model map. Account identity crosses
between them only through `external_id` = `AccountID` (defect 2). P3 work that needs "advisor book x model" has to join
the two.

## Open questions for the CTO (measured in the addendum below)

- Q-A: who owns the `silver/account_attributes` daily merge (defect 1)?
- Q-B: what is the expected cadence of `commonwealth/cottonwood` and `irpt/cottonwood/gold`, so their gaps can be graded?
- Q-C: is `opal/bd/cottonwood/credentials` (live, undeclared) a second credential path for the same BD tenant, or a
  different one?

## Addendum, 2026-10-14 ~18:3xZ: Q-A to Q-C measured (CTO msg 5679)

All gaps below are graded against an expected data date of 2026-10-13. `lib/trading_calendar.py` `is_trading_day` was
counted over (last date, 2026-10-13].

### Q-A: the writer of `silver/account_attributes`, and why it stopped

- **Code:** `data/cot/scripts/silver/cot_silver_merge.py`. Its `TABLE_CONFIG['account_attributes']` (`:129-143`)
  declares the table: forwardfill prefix, silver prefix, dedup on `account_id` + `portfolio_group`. The merge can write
  it, and nothing calls it to.
- **The invocation that omits it:**
  - SSM document `opal-cot-silver-run` (`infra/aws/terraform/cot-pipeline/ssm.tf:236-251`) runs `--table` for
    transactions, allocations, realized, unrealized and holdings only.
  - The **live** document (get-document, read now) carries the same 5 `--table` calls and 0 mentions of
    `account_attributes`.
  - The finalize stage's `_SILVER_STAGE_TABLES` (`cot_silver_merge.py:703`) lists 4 tables and omits it too.
  - The raw pull lands daily through `cot_bronze_ingest.py` (`SNAPSHOT_TABLES` `:147` includes `account_attributes`);
    the silver step was never added.
- **Gap:** last partition `2026-08-19.parquet`, landed 2026-08-20. That is **38 trading days** behind.
- **Root and project:**
  - `infra/logic/registry/root_map.json` root `cot-pipeline` reads system `advi`, scope `cottonwood`, source
    `blackdiamond`. root_map carries no project field (its `row_fields` has none).
  - The daily wiring was owed by the COT_SUPERVISED workstream, step G4b (`templates/account_attributes.json` comment
    "G1 bootstrap -> G4b daily").
  - COT_SUPERVISED is not a tree project. It is cited in `org/projects/ADVI_COTKEY.json`, `MDPF_COTREMEDIATION.json`
    and `DATA_BDINSURANCE.json`.
  - `ADVI_COTETL` (Cottonwood's Black Diamond onboarding) reads `closed`.
  - Last authors of `ssm.tf`: `0.6.2_AE_PartnerETL~S` (IRPT_BCKEND, 2026-09-27) and `0.7.0_AE_CloudOps~A` (2026-07-29).
- **The fix shape** (for the owner, not done here): one `--table account_attributes` line in the SSM document,
  non-gating like holdings, plus its manifest. It needs an applied-and-exercised proof: the next silver partition
  carrying the 2026-10-13 pull's 1,119 rows.

### Q-B: schedules and graded gaps

**`opal-data-assets/commonwealth/cottonwood/` is not a feed.**
- All 15 tables (bronze manifest, imaging and portfolio_accounting; silver documents (11,120), transactions,
  positions, performance, crosswalk, account_links, coverage, document_index, daily_returns, account_day_value,
  month_grades, price_evidence) carry a **single data date, 2026-06-23**. `price_evidence` reads 2022-10-12.
- They landed 2026-10-06 to 2026-10-09.
- No EventBridge rule names commonwealth, crosswalk or cwlth (rules matched for irpt, commonwealth, crosswalk: 1,
  `irpt-directory-keepwarm-5min`). No Scheduler schedule names commonwealth.
- The writers are the `data/assets/scripts/{bronze,silver}/commonwealth_*` scripts, run by hand.
- **Grade: a one-time as-of-2026-06-23 load. The gap is not staleness.** If a recurring feed is wanted, that is a new
  scheduled pipeline (Andrew's NEVER-rule: production pipelines are scheduled), not a stale one.

**`opal-data-cottonwood/irpt/cottonwood/gold/` has 7 tables:**

| Table | Data dates | Landed | Writer and schedule | Grade |
|---|---|---|---|---|
| holdings | 2026-09-22 .. **2026-10-08** (10 dates) | 2026-10-09 14:18 | Not resolved to a schedule. No Lambda carries `irpt-cot` in its name or role. The candidate is `irpt-holdings-snapshot`, cron(15 10 ? * MON-FRI) America/New_York -> `irpt-holdings-refresh-lambda`; whether it writes this table was not read. | **3 trading days** behind (10-09, 10-12, 10-13) |
| holdings_performance_daily (+ manifest) | 2026-06-10 .. **2026-09-25** (75) | 2026-09-29 10:54 | Channel `blackdiamond_z09` (= Cottonwood; `data/assets/scripts/gold/irpt_holdings_performance/sources.json:159`, registry master z09 -> cottonwood). The **only** schedule, `irpt-holdings-performance-daily` cron(30 7 ? * MON-FRI) America/New_York, passes `"source":"schwab_08335338"`; Inflection has its own (`irpt-inf-holdings-performance-daily`). **No schedule fires the z09 channel.** | **12 trading days** behind; unscheduled |
| account_return_daily (+ blank_reasons) | 2013-04-03 .. 2026-06-22 (3,325) | 2026-10-11 07:17 | `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, from the commonwealth load | A historical build ending at that load's as-of; not a daily feed |
| dim_return_method, holdings_qa | reference / QA | 2026-10-11, 2026-10-01 | -- | not feeds |

### Q-C: the two Cottonwood Black Diamond credentials (metadata only; no value read)

| | `opal/bd/cottonwood/credentials` | `blackdiamond/cot/credentials` |
|---|---|---|
| Graph | LIVE-no-DECLARED (no Terraform) | DECLARED (Terraform, owner_pipeline cot-pipeline) |
| Description | "Black Diamond portal login credentials for Cottonwood tenant (EC2 download scripts)" | "Cottonwood Capital Advisors BD platform login credentials for cot-exporter OIDC session refresh" |
| Tags | none | Project OpalPortal, Environment Production, ManagedBy Terraform, System CottonwoodPipeline |
| Created / last changed | 2026-05-27 / 2026-05-27 | 2026-06-08 / 2026-06-08 |
| Last accessed (day grain) | **2026-05-26 ET**, the day it was made; never since | 2026-10-06 ET |
| Versions / rotation | 1 / none | 2 / none |
| IAM roles that can read it | **0 of 304 roles** | 3: `cot-bd-session-trigger-lambda-role` (inline `cot-bd-session-trigger-policy`), `cot-exporter-ec2-role` (inline `cot-exporter-policy`), `cot-gold-layer-ec2-role` (inline `s3-scoped-cot`), each on `.../blackdiamond/cot/credentials-*` |

- Method: every role's inline policies and attached managed policies (50 distinct, default versions). Allow statements
  only, Action matching `secretsmanager:GetSecretValue` (wildcards honoured), Resource glob-matched to the ARN.
- **Not covered:** IAM users and groups, resource policies on the secret, and permission boundaries.
- **Reading:** the same tenant (both descriptions name Cottonwood's Black Diamond login). The undeclared one is the
  pre-pipeline "EC2 download scripts" credential: no role can read it, and it has not been accessed since its creation
  day.
- **It is an undeclared second credential path, so it is a FIRMBKTS row by your rule.** Retiring it is a delete and
  waits on Andrew's word. Whether it holds the same login as the declared secret was not read; that would need the
  value.

## Not read

- Object contents beyond the reads named above.
- The cot-exporter's own scripts.
- Whether `irpt-holdings-refresh-lambda` writes `irpt/cottonwood/gold/holdings`.
- IAM users and groups.
- The other 34 buckets below the graph's bucket-level hits.
