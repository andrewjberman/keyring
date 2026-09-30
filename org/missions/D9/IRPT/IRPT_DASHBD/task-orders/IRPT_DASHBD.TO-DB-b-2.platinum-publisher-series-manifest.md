# TO IRPT_DASHBD.TO-DB-b-2 -- The platinum publisher: gold `account_return_daily` -> `series.json.gz` + `manifest.json` per account under the SERIES contract, its Lambda and schedule planned

<to_id>IRPT_DASHBD.TO-DB-b-2</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** PRD @84cff9014b section 2 hop 2, CONTRACTS C-SERVE, C-SEAM, C-TOPICS (the episode
rule only), C-NAMES, C-MORATORIUM, C-FIRM; CTO 103260 | **Decomp cell:** `DB-b-2` (decomposition section 1) | **outcome_ref:** FWD-1 (hop 2),
FWD-9 | **depends_on:** DB-b-1 (the gold it reads; its worker is spawned on the "gold landed" report)

---

## WORKER FACE

**The cell.** Build the platinum publisher that turns the reporting gold into the ONE file the page reads per account, write the SERIES
contract that is the seam between workstreams B and F, run the publisher ONCE locally for the round-1 sample so the real files exist at
the builder's addresses, and plan (not apply) its Lambda and daily schedule.

**Where things are (repo-relative from your worktree root).**
- The gold you read: `account_return_daily` at `lib.opal_naming.address("irpt","49financial","gold","account_return_daily","date=<D>")`
  + `/data.parquet` (one partition per trading day; columns per `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`:
  `firm, account_id, business_date, market_value_eod, external_flow, income_received, income_return, total_return_daily, return_basis,
  holdings_price_return, holdings_price_return_reason, fee_amount, fee_amount_reason, day_quality, history_scope, method_version,
  schema_version`) and `dim_return_method` at `address(...,"gold","dim_return_method","method_version=1")` + `/data.parquet`.
- The pattern for a scheduled Lambda that packages repo modules: `infra/aws/terraform/investor-reporting/holdings-performance/`
  (`main.tf` state key + provider, `lambda.tf` the `yang-lambda` module with `artifact_key
  "investor-reporting/<name>.zip"` and the existing `irpt-performance-native-layer` for pandas/pyarrow, `iam.tf` least privilege,
  `schedule.tf` an EventBridge Scheduler with its own role, `locals.tf` reading the registry files, never a typed bucket) and
  `infra/aws/lambda/investor-reporting/holdings-performance/handler.py` + the `lambda-source-map.json` entry `irpt-holdings-performance-lambda`
  (`source_dir`, `files`, `staged_from` pins; `infra/aws/lambda/ci/build-and-upload.sh investor-reporting <name>` builds and uploads).
- Names and addresses (rule 30; printed at the cut): function `irpt-49f-reporting-publish-lambda`, schedule
  `irpt-49f-reporting-publish-daily`, role `irpt-49f-reporting-publish-role` (all from `name("irpt","49financial","reporting-publish",<kind>)`);
  files `address("irpt","49financial","platinum","reporting","account=<id>","series.json.gz")` ->
  `s3://opal-data-49financial/irpt/49financial/platinum/reporting/account=<id>/series.json.gz` and `manifest.json`. Terraform cannot call
  the builder: mirror `holdings-performance/locals.tf` (registry-derived bucket; the key segments cited from the publisher's own constants).
- The drawdown-episode rule to reuse as code you read, not import: `infra/aws/lambda/investor-reporting/narrative/events.py` (peak,
  trough, recovery; a trough of at least 50 bp and 2 days; rolling 5-point moves of at least 50 bp).

**What you build.**
- `infra/aws/lambda/investor-reporting/reporting-publish/publisher.py` (pure functions over the gold rows -> the two documents) and
  `handler.py` (the Lambda entry: for a source key and the account set, read every gold partition, build per account, gzip the series,
  write both objects at the builder's addresses; a `--local --accounts ... --upload` CLI for this round's run). Print size and build time
  per account. Include unit tests beside them (`tests/`) with a synthetic gold frame for the pure functions (the real run below is the
  criterion, the tests are hygiene).
- The SERIES contract `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json`: `contract_version "0.1.0"`, `project`, `prd`, `writer "workstream B"`,
  `reader "the Performance page"`, `series.required` = [`date`, `value`, `total_return_daily`, `return_basis`, `day_quality`, `external_flow`,
  `income`, `holdings_price_return`, `method_version`, `as_of`, `first_data_date`, `history_scope`, `drawdown_episodes`], `series.optional` =
  [`class_value`, `class_weight`, `class_names`] (absent until `account_class_daily` exists; the page treats absence as "no class view yet"),
  `series.array_keys` (every per-day array, one length = `date`), `manifest.required` = [`account_id`, `firm`, `method_version`, `as_of`,
  `first_data_date`, `history_scope`, `coverage_summary`, `byte_sizes`, `built_at`, `publisher_version`], and one sentence per field
  (meaning, unit, null rule). `drawdown_episodes` is a list of `{peak_date, trough_date, recovery_date|null, depth}`; `coverage_summary`
  counts days per `day_quality` and per `return_basis`.
- Terraform root `infra/aws/terraform/investor-reporting/reporting-publish/` (its own state key
  `investor-reporting/reporting-publish/tfstate`; NEW resources only: the Lambda, its role reading the two gold prefixes and writing the
  platinum prefix in the firm bucket, the schedule at 08:15 America/New_York Mon-Fri with the reason stated beside it as
  `holdings-performance/schedule.tf` does -- after the adapter's own fire, never "on success of upstream"), `terraform init` + `terraform
  plan -no-color` saved VERBATIM to `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/reporting-publish.plan.txt`.
  Register the function in `lambda-source-map.json` (a new entry shaped like `irpt-holdings-performance-lambda`) and run
  `build-and-upload.sh investor-reporting irpt-49f-reporting-publish-lambda` so the plan can read the artifact. NO APPLY: the apply is the
  issuer's act under its own ledger after your drain.
- The one real run: ledger BEFORE the first platinum write, `python .tools/deploy_ledger.py open --slug irpt-dashbd-reporting-publish-49f-r1-20260930
  --title "<one line>" --author 0.9.0_WK_IRPT_DASHBD~1 --leg "C1|verify|SERIES contract|file written, required/optional lists"
  --leg "W1|activation|series + manifest for the 5 sample accounts|keys, gz sizes, build seconds"
  --leg "P1|verify|plan of the reporting-publish root|0 destroy; lambda, role, schedule created; artifact uploaded"`; then the local
  `--upload` run for the five sample accounts named in the gold (every `account_id` present in the newest partition); `close-leg` each
  with its proof; `close`. Commit the entry AND the sentinel `org/critical_paths/.open_deploys/irpt-dashbd-reporting-publish-49f-r1-20260930.json`.

<criterion id="DB-2-AC1" cell_refs="DB-b-2"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_2_ac1_series_manifest.py" .</invocation><expect>DB-2-AC1 PASS</expect></criterion>
`DB-2-AC1` -- the SERIES contract exists with the required lists; the thread account's `series.json.gz` and `manifest.json` exist at the
builder's addresses with every required key, arrays of one length, dates strictly increasing, and the manifest's byte size equal to the
object's. Base: FAIL (no contract, no objects).

<criterion id="DB-2-AC2" cell_refs="DB-b-2"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_2_ac2_series_link_and_plan.py" .</invocation><expect>DB-2-AC2 PASS</expect></criterion>
`DB-2-AC2` -- the seam with the real neighbour: three 20-day windows link identically from the series and from the gold rows, and the
series `value` equals the gold `market_value_eod`; the saved plan creates the Lambda, the role and the schedule with 0 destroy. Base: FAIL.

<criterion id="DB-2-AC3" cell_refs="DB-b-2"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_ledger_closed.py" . irpt-dashbd-reporting-publish-49f-r1-20260930 DB-2-AC3</invocation><expect>DB-2-AC3 PASS</expect></criterion>
`DB-2-AC3` -- the ledger entry is CLOSED with every leg proven and no sentinel. Base: FAIL (no entry).

<expected_criteria>DB-2-AC1,DB-2-AC2,DB-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **AWS writes admitted:** objects under `irpt/49financial/platinum/reporting/account=<id>/` in `opal-data-49financial` for the sample
  accounts; the artifact upload `investor-reporting/irpt-49f-reporting-publish-lambda.zip` in the artifacts bucket. NO `terraform apply`,
  no other bucket, no vendor call.
- **Refusal clause.** A field the page needs that the gold lacks is a contract note (`optional`, with the reason), never a page-side or
  publisher-side derivation from another source (C-SEAM); a builder refusal stops that limb with a row.

<paths>
infra/aws/lambda/investor-reporting/reporting-publish/
infra/aws/terraform/investor-reporting/reporting-publish/
infra/aws/terraform/investor-reporting/holdings-performance/
infra/aws/terraform/modules/yang-lambda/
infra/aws/lambda/investor-reporting/holdings-performance/handler.py
infra/aws/lambda/investor-reporting/narrative/events.py
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/build-and-upload.sh
org/standards/IRPT_DASHBD_SERIES_CONTRACT.json
org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json
org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json
lib/opal_naming.py
lib/trading_calendar.py
infra/logic/registry/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-dashbd-reporting-publish-49f-r1-20260930.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 1 (round 1, workstream B), cell `DB-b-2`.
<owned_cells>DB-b-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB-2-AC1, DB-2-AC2, DB-2-AC3. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/IRPT_DASHBD.TO-DB-b-2.platinum-publisher-series-manifest.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB-2-AC1 DB-2-AC2 DB-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hashes, each criterion's last line, per-account gz size and build seconds, the plan's
`Plan:` line, and any surprise row id (`IRPT_DASHBD-W1-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- denominator: 2 schedule resources read in infra/aws/terraform/investor-reporting/holdings-performance/schedule.tf (irpt-holdings-performance-daily, the Inflection twin), both cron(30 7 ? * MON-FRI *) America/New_York; the NEW scheduler this cell plans is a third, at 08:15 America/New_York, not applied here; blind spot: the live scheduler group was not listed (the plan-time stage sees it).
comp-iam: RUN -- denominator: 1 execution role read (holdings-performance/iam.tf, registry-derived read grants on two silver prefixes + write on one gold prefix); the NEW role mirrors it with 2 gold read prefixes + 1 platinum write prefix in one firm bucket; 0 existing roles or policies touched; the apply is the issuer's under its own ledger.
comp-blast: RUN -- new platinum keys; 0 readers today (the read route is DB-b-4; the page is F's).
comp-routes: DECLARED-NOT-APPLICABLE -- no route in this cell.
comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- DB-2-AC1 base FAIL (no contract); DB-2-AC2 base FAIL (no series); DB-2-AC3 base FAIL (no entry).
spawn: 0.9.0_WK_IRPT_DASHBD~1 is spawned when DB-b-1 reports the gold landed (chain B's first criterion reads that gold).
lane: the <paths> block IS the grant.
</preflight>
