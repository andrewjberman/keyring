# The start-to-finish walk of the model-portfolio pipeline (MDPF) -- what the legacy-transform run did not see, measured with the comp-tools that exist

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Recon ID:** RCN-0010 -- registered in RECON_REGISTER.md
**Date:** 2026-09-18 ~18:4xZ to ~19:3xZ
**Commissioned:** Andrew-direct ~18:3xZ at this terminal (record
`ANDREW_DIRECT_20260918_183xZ_LGCTFM_ALL_COMP_TOOLS_PIPELINE_WALK_TO_CONSUMERS_BRIEF.md` @c9e54d5c0f): *"give it a
shot based on what youve already found via your MDPF_CANON /legacy-transform run"*. The brief it feeds is
`docs/briefs/d14-lgctfm-pipeline-walk-brief-20260918.md`. Binding requirement it lands into: `1.0.0_SA_CTO` R-81
@4443e7308e (msg 98046).
**Posture:** every instrument READ-ONLY; nothing on the applied plane moved; every count carries its instrument,
plane and vintage. This is the WORKED EXAMPLE the brief's ruleset was extracted from, not a project run.

---

## 0. THE ANSWER TO ANDREW'S QUESTION

**Is a start-to-finish walk to the consumers already established in `/legacy-transform`? NO.** Measured on the
engine and its six runs (RCN-0009 @edcbe51fb4): the walk is bucket-seeded, writes `"edges": []`, takes no consumer
hop, and its own method note says the served-route plane (DEC-3's final step) is not read
(`infra/logic/10_LEGACY_TRANSFORM.md` "Coverage hole"). The pieces exist as separate comp-tools; no run composes
them, and nothing in the run answers "who consumes the final artifact and can a viewer see it".

**Did the walk find crucial resources the run declared absent? YES, in every class Andrew named.** The engine's
mdpf run carried 14 real rows across 7 kinds (RCN-0009). This walk, over the same subject at the same graph
vintage, carries the population in s.2 -- 6 Lambdas, 1 EC2 runner, 13 roles, 11 policies, 6 schedules, 1
event rule, 3 alarms, 6 log groups, a layer, a security group, an instance profile, an SSM parameter, a secret
path, a DLQ, ~17 repo scripts, ~30 storage locations, 3 portal routes, 1 component -- and one CROSS-SYSTEM
trigger dependency (s.2.1) that no per-subject instrument can see and the firm-bucket migration must carry.

---

## 1. INSTRUMENTS AND VINTAGES

| hop | instrument | plane | denominator / vintage |
|---|---|---|---|
| live plane by token | `comp-find --corpus aws '\bmdpf\b' -i --all` | applied (graph) | 60 hits / 2590 nodes, 15 types; graph built 2026-09-18 12:17:28 UTC |
| triggers, both APIs | `comp-trigger --list --json` | applied | 167 triggers = 144 rules + 23 schedules; 7 MDPF; **the JSON carries NO target field** (keys: arn, kind, name, pattern, schedule, state) |
| trigger -> target | Terraform `target {}` blocks read in 8 `.tf` files (`infra/aws/terraform/mdpf-pipeline/*.tf`, `opal-assets/mdpf_portal_publisher.tf`) | desired | 7 of 7 targets resolved |
| compute identity | `comp-find --corpus aws` LAMBDA/EC2 nodes with `drift_class` | applied | R-81: function identity from the graph, never the source map |
| compute -> source, artifact | `infra/aws/lambda/ci/lambda-source-map.json` (216 entries) | hand surface | **R-81: 19 names out of step with 217 live functions; used here for `source_dir` only, declared** |
| EC2 -> scripts | `infra/aws/ec2/EC2_MANIFEST.json`; `infra/aws/ec2/mdpf-daily-runner/*.sh` read with `comp-read --enumerate` | hand surface + source | **the runner is ABSENT from EC2_MANIFEST.json** (only `consolidation-gold-runner` is there) |
| identity grants | `comp-iam service <fn>` / `comp-iam role <role>` | desired (Terraform) -- the tool prints this itself | 476 `.tf` files; 31 policy blocks NOT ATTACHED; 6 deny statements unparsed |
| script I/O | `comp-pipescript io <script> --pipeline mdpf` | source (static) | on `mdpf_gold_consolidator`: READS 0 detected, 2 UNRESOLVED-PREFIX, WRITES 0 detected |
| writer census | `comp-legacywriter mdpf --json` | source (static) | 9,015 files; 811 write sites; 586 (bucket,key) locations; 40 mdpf-bearing locations |
| graph neighbourhood | `comp-blast <arn|gold:id> --direction both --json` | applied (graph) | universe 28,123 nodes / 60,389 edges; **node ids are ARNs or `gold:<script>`, never `lambda:<name>`** |
| storage | `comp-keys prefix <bucket> <prefix>`; `.tools/aws s3api list-objects-v2` | applied (live s3api) | four prefixes, LastModified in UTC |
| serving | `comp-routes rewrites|trace|endpoints`; `comp-platinum reverse <key>`; `comp-transform fields <Component>` | desired (parsed TF + router source + portal/src) | 60 rewrite lines; 3 MDPF routes; 1 component |
| business chains | `comp-estate --resource mdpf` | ontology snapshot (last review 2026-07-30) | 2 chains of 135 |
| record scans | `comp-find -i mdpf org/critical_paths/change_management --files`; python name-extraction over `org/**/logs/**/*.md` | record | change-management 128 of 831 files, 112 distinct names; session logs 884 of 6,068 files, 299 distinct names |

Not run, and why: `comp-whoread` (CloudTrail S3 data events -- card 3's read logging covers the four firm buckets,
not `opal-data-assets` or `opal-data-portal-v2`, so the OBSERVED-reader axis for MDPF's artifacts is out of
instrument coverage today); a live GET through the portal page (the applied-plane viewer check; the design
names it, this record did not exercise it).

---

## 2. THE WALK, IN THE DIRECTION OF DATA

### 2.1 Triggers (7 of 167 census'd) and what each fires -- the hop the run cannot make

| trigger | API | expression | target (Terraform) | DLQ |
|---|---|---|---|---|
| `wsb-49f-model-aua-pull-daily` | Scheduler | `cron(30 3 ? * TUE-SAT *)` | Lambda `wsb-49f-model-aua-daily` (`wp5-feeder-schedules.tf:251-266`) | -- |
| `wsd-49f-partner-held-etf-pull-daily` | Scheduler | `cron(30 3 ? * TUE-SAT *)` | Lambda `wsd-49f-partner-held-etf-daily` (`:270-283`) | -- |
| `mdpf-feeder-backstop-daily` | Scheduler | `cron(52 12 * * ? *)` | Lambda `mdpf-feeder-trigger` (`feeder-trigger.tf:233-252`) | `mdpf-daily-trigger-dlq` |
| `mdpf-feeder-accelerator` | EventBridge rule | **event pattern: `Object Created` on bucket `opal-data-inf`, key `gold/meta/pipeline-complete.json`** | Lambda `mdpf-feeder-trigger` (`feeder-trigger.tf:259-285`) | `mdpf-daily-trigger-dlq` |
| `mdpf-scheduled-floor` | Scheduler | `cron(30 13 * * ? *)` | Lambda `mdpf-gold-lambda` (`scheduled-floor.tf:110-155`; target SWAPPED from `mdpf-daily-trigger` 2026-08-07, change-management `20260807_mdpf_canplat_cutover_bundle_AE_Z.md`) | `mdpf-daily-trigger-dlq` |
| `mdpf-accrual-bridge-daily` | Scheduler | `cron(40 13 * * ? *)` | Lambda `mdpf-accrual-trigger` (`accrual-bridge.tf:165-194`) | -- |
| `opal-assets-mdpf-portal-publisher-daily` | Scheduler | `cron(50 13 * * ? *)` | Lambda `opal-assets-mdpf-portal-publisher` (`mdpf_portal_publisher.tf:211-234`) | -- |

**The cross-system dependency.** `mdpf-feeder-accelerator` fires the MDPF feeder when the INFLECTION gold chain
writes its completion sentinel into `opal-data-inf` -- a legacy firm bucket `ADVI_FIRMBKTS` retires. The
engine's mdpf run carried this rule as one GRAMMAR tension on its NAME and nothing about its PATTERN; the 49F
run does not carry it at all (its seeds are `opal-data-bd` / `-49financial`). So the resource that binds the two
migrations together is invisible to both runs. The runner's dispatch script waits on the same sentinel
(`mdpf-daily-dispatch.sh:283-301`, `INF_BUCKET="opal-data-inf"`). **A cutover that moves `opal-data-inf` without
repointing this pattern silently stops the MDPF feeder, and no per-subject instrument would say so.**

### 2.2 Compute (6 Lambdas + 1 EC2 live; 2 named in the repo and records but NOT live)

| resource | live (graph) | declared | source (map / repo) | role |
|---|---|---|---|---|
| `mdpf-gold-lambda` | LAMBDA, DECLARED | `mdpf-pipeline/gold-lambda.tf` | `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda` -- a BUILD dir (`build_package.py`, zip, BUILD_MANIFEST), no handler in the repo; **artifact key `portal/gold/mdpf/_code/mdpf-gold-lambda.zip` -- code inside the served gold tree** (MDPF_CANON v2.3 R4's hold) | `mdpf-gold-lambda-role`, 11 statements |
| `mdpf-feeder-trigger` | LAMBDA, DECLARED | `feeder-trigger.tf` | `mdpf-pipeline/mdpf-feeder-trigger` | `mdpf-feeder-trigger-role` |
| `mdpf-accrual-trigger` | LAMBDA, DECLARED | `accrual-bridge.tf` | `mdpf-pipeline/mdpf-accrual-trigger` | `mdpf-accrual-trigger-role` |
| `wsb-49f-model-aua-daily` | LAMBDA, DECLARED (owner_pipeline mdpf-pipeline) | `wp5-feeder-schedules.tf` | `mdpf-pipeline/wsb-49f-model-aua-daily` | `wsb-49f-model-aua-daily-role` |
| `wsd-49f-partner-held-etf-daily` | LAMBDA, DECLARED | same | `mdpf-pipeline/wsd-49f-partner-held-etf-daily` | `wsd-49f-partner-held-etf-daily-role` |
| `opal-assets-mdpf-portal-publisher` | LAMBDA, DECLARED | `opal-assets/mdpf_portal_publisher.tf` | `opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py` | `opal-assets-mdpf-egress-publisher-role` (scoped `platinum/mdpf/*`) |
| `mdpf-daily-runner` | EC2_INSTANCE `i-02448edb624a7a7cf`, DECLARED (t3.medium, stop between runs) | `mdpf-pipeline/ec2.tf` | `infra/aws/ec2/mdpf-daily-runner/` (user-data, `mdpf-daily-dispatch.sh` 664 lines, two one-off scripts); **not in `EC2_MANIFEST.json`** | `mdpf-daily-runner-ec2-role` (34 statements), profile `mdpf-daily-runner-profile`, SG `mdpf-daily-runner-sg`. **Started by:** `mdpf-feeder-trigger` and `mdpf-accrual-trigger` -- both roles hold `ec2:StartInstances` + `ssm:SendCommand` + `ec2:DescribeInstances` (`comp-iam service`, desired plane; the `ec2.tf` comment still names the retired `mdpf-daily-trigger`) |
| `mdpf-daily-trigger` | **NOT LIVE** (0 LAMBDA nodes; only the DLQ and the alarm carry the name) | referenced in `ec2.tf` comment ("started by mdpf-daily-trigger Lambda") | `mdpf-pipeline/mdpf-daily-trigger/` present with tests | **RETIRED 2026-08-07** (the floor's target swap, record above); 15 change-management files and 103 session-log files still name it |
| `mdpf-freshness-checker` | **NOT LIVE** | not in the source map | `mdpf-pipeline/mdpf-freshness-checker/lambda_function.py` present | NEVER-DEPLOYED or RETIRED -- **UNMEASURED which**; 24 session-log files name it; a monitor of the class the standing moratorium covers |

Also live and involved, outside the compute rows: layer `mdpf-gold-calendar-deps`; alarms
`mdpf-daily-trigger-dlq-not-empty`, `wsb-49f-model-aua-daily-errors`, `wsd-49f-partner-held-etf-daily-errors`;
6 log groups (one, `/aws/lambda/mdpf-gold-lambda`, `LIVE-no-DECLARED`); SQS `mdpf-daily-trigger-dlq`; SSM
parameter `/mdpf/custody_source` (`lambdas.tf:25`); secret path `smartx/credentials/*` (runner role statement 1).
**The SSM parameter and the secret path are OUTSIDE the 33-type node vocabulary** the contract grades
(`SSM_DOCUMENT` is in it, `SSM_PARAMETER` is not; `SECRET` is, as a slash-path) -- R-36's untypeable class, met
on a real subject.

### 2.3 Scripts (what the compute actually runs)

- The gold Lambda's package manifest (`build_package.py:134-159`) names **17 repo files**: 10 from
  `data/mdpf/scripts/gold/` (`mdpf_gold_consolidator`, `dim_mdpf_aggregate_aua_timeseries`,
  `dim_mdpf_account_distribution`, `dim_mdpf_aum_metrics`, `dim_mdpf_non_model_assets`, `mdpf_aggregate_aua`,
  `build_mdpf_spine`, `mdpf_revamp_model_crosswalk`, `mdpf_calendar_binding`, `mdpf_category_registry`) plus
  `mdpf_model_registry.json`, 5 from `data/assets/scripts/gold/` (the cottonwood slice/pair/interpolation
  builders, `build_dim_model_portfolio`), 1 from `data/assets/scripts/silver/` (`rebalancer_schemas`).
- The EC2 runner pulls its chain from **S3, not the repo**: `s3://opal-data-mdpf/code/scripts/` and `code/config/`
  (`mdpf-daily-dispatch.sh:123-130`; runbook `data/mdpf/scripts/RUNBOOK_AE_mdpf_daily_chain.md`). What is IN that
  S3 code prefix versus the repo is UNMEASURED here -- a deploy-parity question (`comp-lambdamap parity` is the
  Lambda-side instrument; the EC2 side has none but `verify-ec2.sh`).
- **Two static instruments disagree on the same script.** `comp-pipescript io mdpf_gold_consolidator --pipeline
  mdpf`: READS none detected, WRITES none detected, 2 UNRESOLVED-PREFIX, one monolith silver read
  (`fact_model_assignment`). `comp-legacywriter`: write sites at `mdpf_gold_consolidator.py:1460,1463,1691`,
  `mdpf_aggregate_aua.py:308,592,626`, `dim_mdpf_aum_metrics.py:114`, `dim_mdpf_aggregate_aua_timeseries.py:774`,
  `dim_mdpf_aum_timeseries.py:87`, the two feeders. One tool's zero is the other's nine.

### 2.4 Artifacts (storage plane; live listing 2026-09-18 ~19:0xZ)

| bucket / prefix | what | writer | newest seen | reader |
|---|---|---|---|---|
| `opal-data-mdpf/mdpf/bronze/orion_model_composition/{date}/` | bronze JSON (Orion model pulls) -- **JSON at bronze, not parquet: R9's irreversible class is NOT present here** | the runner chain | `comp-keys partitions`: 89 partition dates, earliest 2026-05-18, **latest 2026-09-18** (19 weekday gaps, calendar not trading) -- LIVE today | the runner |
| `opal-data-mdpf/mdpf/feeds/{model_aua,partner_held_etf,non_model_aua,etf_net_assets}/{firm}/*.parquet` | feeds | `wsb-*`, `wsd-*` feeders | -- | `mdpf-gold-lambda` (GetObject on `mdpf/feeds/*`, statement 8) |
| `opal-data-mdpf/{gold,silver}/eclipse/{*}/*.parquet`, `silver/netassets_daily.parquet`, `platinum/mdpf/aggregate_aua_timeseries.json` | the engine's 6 S3Key rows | runner (writer-firm attribution) | -- | UNMEASURED |
| `opal-data-mdpf/{code,telemetry,diagnostics,bmkaud-evidence}/` | code, run telemetry (`status.json`, `history/`, `logs/`), evidence | dispatch script | -- | the runner; operators |
| `opal-data-assets/gold/mdpf_revamp/{49financial,cottonwood,global}/*.json`, `_aggregate_aua/{date}.json` | the REVAMP gold tree (492 objects per tension map) | runner Stage 6 + `mdpf-gold-lambda` (Put on `gold/mdpf_revamp/*`) | `49financial/aggregate_aua_timeseries.json` **2026-09-18T13:31:09Z** -- LIVE today | `mdpf-gold-lambda` |
| `opal-data-assets/portal/gold/mdpf/{firm}/{artifact}/{date}.json`, `_manifests/` | the dated gold the publisher reads (415 objects) | `mdpf-gold-lambda` (Put on `portal/gold/mdpf/*`) | `comp-keys partitions` on `49financial/account-distribution/`: 29 dates, 2026-07-28 to **2026-09-18**, 10 weekday gaps (calendar) -- LIVE today | `opal-assets-mdpf-portal-publisher` |
| `opal-data-assets/config/mdpf/route_bindings.yaml`, `gold/dim_model_portfolio/*`, six partner silver trees | config + inputs | -- | -- | `mdpf-gold-lambda` (statements 1, 4, 10) |
| `opal-data-portal-v2/platinum/mdpf/49financial/{account-distribution,aggregate-aua-timeseries,aum-metrics,category-views}.json` | **the FINAL artifacts** | the publisher | all four **2026-09-18T13:50:49Z** -- LIVE today | CloudFront OAC -> the portal (s.2.5) |
| `opal-data-portal-v2/platinum/mdpf/_manifests/{date}/{run}.json` | publisher run manifests | the publisher | daily | operators |
| `opal-data-portal-v2/platinum/mdpf/global/*` | global aggregates | `IN_REPO` stitch (drift class) | -- | no declared endpoint (s.2.5) |
| `opal-data-portal-v2/json/mdpf/*`, `json/portfolios/non_model_assets.json` | LEGACY serving keys | none (read-only grant, statement 7) | -- | `mdpf-gold-lambda` reads them |
| DynamoDB `opal-portal-market-data` | reported by `comp-blast` at depth 3 downstream of both Lambdas | -- | -- | **graph-reported, UNVERIFIED** -- through the CloudFront principal chain, not a grant either role holds |

### 2.5 Consumers and the viewer verdict (the final step Andrew asked for)

Routes (`comp-routes trace`, desired plane; 3 MDPF routes of the portal's endpoint set):

| final artifact (per firm) | route | CloudFront | component | field used (`comp-transform fields ModelPortfolios`) | **viewer verdict** |
|---|---|---|---|---|---|
| `platinum/mdpf/{firm}/account-distribution.json` | `getAccountDistributionByFirm` `/api/general/mdpf/{firm}/account-distribution.json` | `/api/general/*` -> origin `S3-opal-data-portal-v2-json`, edge JWT | `ModelPortfolios` | `distributionData` (root) | **VISIBLE** (desired plane); live GET not exercised here |
| `platinum/mdpf/{firm}/category-views.json` | `getCategoryViewsByFirm` -- **client-composed URL, CloudFront UNRESOLVED statically** | -- | `ModelPortfolios` | `categoryViews` (root) | **CONSUMED-BY-FIELD, ROUTE UNRESOLVED** -- verify at the served edge |
| `platinum/mdpf/{firm}/aum-metrics.json` | `getAUMMetricsByFirm` `/api/general/mdpf/{firm}/aum-metrics.json` | same | `ModelPortfolios` | **not in the used-fields list (2 of 2 listed are the other two)** | **ROUTED, FIELD-USE UNMEASURED** -- fetched-unrendered candidate |
| `platinum/mdpf/{firm}/aggregate-aua-timeseries.json` (139,839 bytes, written daily) | **no route in the trace** | rewrite `/api/general/mdpf/ -> platinum/mdpf/` would reach it | none found | -- | **NO-ROUTE (INVISIBLE on the desired plane)** |
| `platinum/mdpf/global/*` | no endpoint | reachable by the same rewrite | none found | -- | **NO-ENDPOINT (INVISIBLE)**; `IN_REPO` stitch |
| `platinum/mdpf/_manifests/*` | -- | -- | -- | -- | OPERATIONAL, invisible by design |
| everything in s.2.4 above the platinum tier | -- | -- | -- | -- | INTERMEDIATE, invisible by design |

`comp-platinum reverse platinum/mdpf/49financial/aum-metrics.json` prints **PRODUCER: (empty)** and CONSUMED BY
`ModelPortfolios` -- the serving tool cannot name the writer of a served key; the writer is known only from the
publisher's own source (s.2.3) and its grant. `comp-estate --resource mdpf` places the vertical in two business
chains: `PPI-05-opal-portal-data-proxy` and `mdpf-global-view` (stitch).

**Graph consumers** (`comp-blast`, both directions): the gold Lambda's downstream set includes
`advi-49f-gold-dispatch` (depth 2, via a role the graph links), CloudFront and OAI `EU39UXW7CMSI5` service
principals (depth 3), and 13 node types in all; upstream is exactly one SCHEDULE (`mdpf-scheduled-floor`). The
publisher's downstream includes `opal-security-scanner-processor` (depth 2) -- an edge this walk did not verify
and records as the graph's claim.

### 2.6 The record scans -- the "athletic" check, with every off-plane name classified

- change-management: **128 of 831** records name the subject; **112 distinct** resource-shaped names.
- session logs: **884 of 6,068** log files; **299 distinct** names.
- live plane by token: **60 nodes**.

Every name the records carry and the live plane does not is ONE of five things, and only the last fails a run:

| class | examples from this subject | evidence |
|---|---|---|
| RETIRED (a record names the retirement) | `mdpf-daily-trigger` (Lambda; 2026-08-07 floor target swap) | `20260807_mdpf_canplat_cutover_bundle_AE_Z.md`; live 0 LAMBDA, DLQ + alarm keep the name |
| NEVER-BUILT or UNMEASURED-WHICH | `mdpf-freshness-checker`, `mdpf-daily-refresh-trigger`, `mdpf-legacy-emit-on-demand`, `mdpf-data-router` | live 0 of 4; TF references only in comments/DLQ names; `mdpf-freshness-checker` has a source dir and no source-map entry |
| SCRIPT-NOT-RESOURCE | `mdpf-daily-dispatch`, `mdpf_gold_consolidator`, `mdpf_aggregate_aua`, `mdpf_category_registry`, `mdpf_revamp_model_crosswalk` | repo files under `infra/aws/ec2/mdpf-daily-runner/`, `data/mdpf/scripts/gold/` |
| ALIAS / TOKEN of a live thing | `mdpf-pipeline`, `mdpf-pipeline-v1`, `mdpf-pipeline-v2`, `mdpf_revamp`, `mdpf-gold`, `mdpf-runner` | the Terraform module, the REVAMP prefix, short forms |
| MISSED (live, involved, and absent from the run's rows) | the 6 Lambdas, the EC2 runner, 13 roles, 11 policies, 3 alarms, 6 log groups, the layer, the SG, the profile | present on the live plane by token; 0 rows in the engine's run |

The classification above is this seat's reading of the census; the instrument for the first class is the
change-management record itself, which is why Andrew's "change-management scan" earns its place: **it is the only
surface that can turn an absence on the live plane into a RETIRED verdict instead of a MISS.** `comp-blast`
already reads that directory for HOLD claims (74 on `mdpf-gold-lambda`, 17 on the publisher); a name census over
it is the second read the same directory supports.

---

## 3. THE DELTA AGAINST THE ENGINE'S RUN (the number that answers "not done")

| class | engine mdpf run (RCN-0009) | this walk | source of the gap |
|---|---|---|---|
| triggers | 5 rows (names only) | 7, each with target, expression, DLQ, and one cross-system pattern | comp-trigger's list has no target; the run reads names |
| compute | 0 | 6 Lambdas + 1 EC2 (+2 retired/unbuilt, classified) | bucket seed |
| identity | 1 (a plant) | 13 roles + 11 policies + profile | bucket seed |
| observability | 0 | 3 alarms + 6 log groups | bucket seed; two types outside the seed's reach |
| params / secrets | 0 | 1 SSM parameter + 1 secret path | outside the 33-type vocabulary |
| scripts | 0 | 17 packaged + the S3-synced chain | no compute row, so no declaration evidence |
| storage | 6 S3Key + 1 bucket + 1 policy + 2 planes | ~30 locations across 3 buckets + 1 legacy key family + 1 DynamoDB claim | static writer census + grants + live listing |
| consumers / routes / component | 0 | publisher, 3 routes, 1 component, 2 business chains | no consumer hop in the run |
| viewer verdicts | 0 | 7 artifact classes, 5 verdict values | no final step in the run |
| edges | 0 | every row above is one end of an edge with a named instrument | the run writes `[]` |

---

## 4. WHAT THIS RECORD DOES NOT CLAIM

- No applied-plane GET through the portal page was made; every viewer verdict is DESIRED-plane (parsed
  Terraform, router source, portal source). The design in the brief names the applied check.
- The DynamoDB and `advi-49f-gold-dispatch` and `opal-security-scanner-processor` consumers are the GRAPH's
  claims at depth 2-3; not verified against a grant or a call site.
- Newest-object dates are from the first listing page for two prefixes (alphabetical, not newest); the four
  platinum keys and the REVAMP 49financial key were read from their own rows.
- The S3 code prefix the runner syncs was not diffed against the repo.
- `comp-iam` reads Terraform (it says so); no live simulate was run. R-81's re-point (comp-iam live / simulate for
  the applied grant) is the design, not this record's measurement.
- The record-scan classification is by this seat's reading; the brief makes the classes a closed enum with an
  instrument each.
