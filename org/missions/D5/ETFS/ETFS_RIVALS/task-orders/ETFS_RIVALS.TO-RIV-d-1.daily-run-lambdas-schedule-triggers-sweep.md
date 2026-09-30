# ETFS_RIVALS task order -- `RIV-d-1` -- ROUND 1 (THE THREAD, BASG): THE DAILY RUN: FIVE LAMBDAS, THE 07:00 ET SCHEDULE, THE MARKER TRIGGERS AND THE SWEEP (H6 code, plan only)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-d-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~3</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-09-30 ~06:40Z) -- 39 gates armed over five carriers; none names the rivalfunds prefixes, the five names or opal-gateway; the shared tree's .open_deploys/ holds no gateway/etfs/rival entry; the 50 linked worktrees were not read (RIV-d-2 reads them). The notifier moratorium binds: no alarm, SNS or monitor.
comp-iam: RUN at L5 -- the thread touches IAM at RIV-w-1 (gateway read policy) and RIV-d-1 (five Lambda roles); each cell's own IAM simulation criterion is the instrument; no grant is applied before RIV-d-2, under the never-widen pair.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches its surface.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: six rival active ETFs' daily holdings, each fund's
reverse-engineered trade schedule, and a daily research page at `/rivalfunds`. **Round 1 builds ONE live journey for BASG**:
issuer site -> bronze -> silver -> `canonical_shape` -> `trade_schedule` -> the day's page -> `/rivalfunds`, fired from AWS.
Your cell is one hop of it. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 0. BEGIN ONLY WHEN THESE HOLD

1. Nothing precedes this order. It plans only: no `terraform apply`, no `safe-apply`, no Lambda upload.
2. `sweep.py` and the wrappers import `rivalfunds.markers` (RIV-c-1, built by another slot in parallel). If `data/etfs/scripts/rivalfunds/markers.py` is absent in your worktree, write the sweep against the marker API as the rulings state it; AC2 imports the real module and is run once it is merged -- report AC2 as blocked on RIV-c-1 if it is not there, never stub it into the package.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-d-1` -- the daily run: Lambdas, schedule, triggers, sweep (H6 code, plan only)

`infra/aws/terraform/etfs-rivalfunds/` (new stack, pattern `infra/aws/terraform/etfs-netassets/netassets-lambda.tf` and
`infra/aws/terraform/cot-pipeline/s3-notifications.tf`): five zip Lambdas named per the rulings, each wrapping one stage's
`handler_entry` (wrappers `infra/aws/lambda/etfs-pipeline/<lambda-name>/lambda_function.py`, one import and one call each),
packaged by `infra/aws/lambda/etfs-pipeline/rivalfunds_package.py` (Python, so the check runs it portably; it stages `data/etfs/scripts/rivalfunds/`,
`lib/opal_naming.py`, `lib/trading_calendar.py`, `lib/research/identity/` and `infra/logic/registry/` into a build
directory `<tree root>/.runtime/rivalfunds-build/` (gitignored; the `.tf` reaches it as `${path.module}/../../../../.runtime/rivalfunds-build`)
that `archive_file` zips) with
the existing pandas-pyarrow-requests layer; every name and prefix the `.tf` files use comes from
`generated.auto.tfvars.json`, and every role policy is `policies/<lambda-name>.json`, both written by
`infra/aws/terraform/etfs-rivalfunds/gen_policies.py --out <dir>` from `address()`/`name()` (rule 30: no `.tf` types the
bucket or a resource name); one IAM role per Lambda (role names from a CONFORMANT `name()` call) with
Put/Get only under the eight builder prefixes it needs and Get on `opal-data-harvest/crosswalk/v1/*` for the build stage;
an EventBridge Scheduler schedule `etfs-rivalfunds-daily` at 07:00 America/New_York Mon-Fri invoking the fetch Lambda; a
second schedule (qualifier from `name()`) at 09:00 America/New_York Mon-Fri invoking `etfs-rivalfunds-daily-lambda`, the
sweep; `aws_s3_bucket_notification` on `opal-data-etfs` with `eventbridge = true` and nothing else (the bucket's ONE
notification owner, C-TRIGGERS; the live configuration is empty); EventBridge rules on Object Created under the state
prefix of each stage invoking the next stage. The sweep, `data/etfs/scripts/rivalfunds/sweep.py` `handler_entry`: for the
day, run any stage whose input marker has no output marker, in order, then publish; idempotent; public
`run_sweep(date, sink, runners: dict[stage, callable(event) -> result])` so the runners are injectable, and `handler_entry`
binding the real stage modules. No alarm, no SNS (C-NO-NOTIFIER).
`terraform plan` only; nothing is applied in this cell. `ci/lambda-source-map.json` entries are HOOKUPS added at the merge.
The backend is `s3` bucket `opal-313476888478-terraform-state` key `etfs-rivalfunds/tfstate` (the `etfs-netassets` pattern);
the check plans against a local throwaway state through a temporary `backend_override.tf`.


## 2. THE RULINGS THAT REACH EVERY CELL (inlined verbatim from the decomposition)

- **Addresses and names are builder output only** (CLAUDE.md rule 30; PRD C-HOMES, C-NAMES). Code calls
  `lib/opal_naming.py address(source, scope, tier, table, partition, object=None)` and
  `name(system, scope, function, kind, qualifier=None)`; a literal `s3://opal-data-etfs/...` or resource name typed in
  product code is a defect. Measured at this cut, all resolve with 0 refusals:
  - `address('issuer-site','etfs','bronze','holdings','date=<D>')` -> `s3://opal-data-etfs/issuer-site/etfs/bronze/holdings/date=<D>`
  - `address('issuer-site','etfs','silver','holdings','date=<D>')` -> `s3://opal-data-etfs/issuer-site/etfs/silver/holdings/date=<D>`
  - `address('rivalfunds','etfs','gold','canonical_shape','date=<D>')`, `...'trade_schedule'...` -> `s3://opal-data-etfs/rivalfunds/etfs/gold/<table>/date=<D>`
  - `address('rivalfunds','etfs','platinum','page','date=<D>')` -> `s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=<D>`
  - `address('rivalfunds','etfs','state','<stage>','date=<D>')` -> `s3://opal-data-etfs/rivalfunds/etfs/state/<stage>/date=<D>`
  - names (all `grade()` CONFORMANT): `etfs-rivalfunds-daily` (schedule/rule), `etfs-rivalfunds-daily-lambda`,
    `etfs-rivalfunds-fetch-holdings-lambda`, `rivalfunds-build-silver-lambda` (new, `name('rivalfunds',None,'build-silver','lambda')`),
    `rivalfunds-build-canonical-shape-lambda`, `rivalfunds-publish-page-lambda`.
  - NOT conformant, never used: `name('etfs',None,'rivalfunds','role','lambda')` grades OUT-OF-PATTERN; a role name is
    taken from a `name()` call that grades CONFORMANT or the cell files a row.
- **Partition dates:** bronze `date=` is the ACQUISITION date (spec S2); silver and gold `date=` are the REPORT date; the
  page `date=` is the publish day. An undated payload stays in bronze with a status and never acquires a guessed report
  date (C-SHAPES).
- **The stage entry contract** (so the infra cell wraps what the stage cells export, without an edge on file contents):
  every stage module exposes `handler_entry(event: dict, context=None) -> dict`, event
  `{"date": "YYYY-MM-DD", "mode": "daily"|"backfill"|"replay", "batch_id": str, "sink": "s3"|"local:<dir>"}` (plus
  `start`/`end` for `backfill`, and optional `start`/`end` for `replay`, default everything under the input prefix), returning
  `{"status": "OK"|"PARTIAL"|"FAILED"|"SKIPPED", "batch_id", "outputs": [<uri>...], "marker": <uri>|null, "detail"}`.
  A `local:<dir>` sink mirrors `s3://<bucket>/<key>` as `<dir>/<bucket>/<key>` so every test runs without a served write.
- **Batch-complete markers** (C-TRIGGERS): a stage writes `address('rivalfunds','etfs','state','<stage>','date=<D>', '<batch_id>.json')`
  only when its batch is whole; the next stage is idempotent on `batch_id`. Stage names, in order: `fetch-holdings`,
  `build-silver`, `build-canonical-shape`, `build-trade-schedule`, `publish-page` (the two gold stages run in one
  Lambda, `rivalfunds-build-canonical-shape-lambda`, each writing its own marker). The marker API is RIV-c-1's
  `markers.write_marker(stage, date, batch_id, sink, payload=None) -> uri`, `markers.read_markers(stage, date, sink) -> list[dict]`,
  `markers.has_marker(stage, date, sink) -> bool`.
- **Universe in round 1: BASG only.** The BASG issuer file carries other Brown Advisory funds; silver keeps every row,
  gold filters `fund_ticker == 'BASG'`.
- **Real data, never a fixture, on the seam** (FWD-1 ACCEPT). The captured BASG archive on this box,
  `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\amgt-reconn-daily-census-20260929\basg\` (324 issuer `.txt`
  files 2025-06-13..2026-09-28, each with a `.json` probe sidecar; gitignored, device-local), is the real neighbour for
  the silver and gold cells. The live issuer URL is
  `https://brownadvisory.filepoint.live/assets/data/SEI_Brown_Tradedate_Holdings_<MMDDYYYY>.txt` (pipe-delimited,
  utf-8-sig; header `date|fund_id|fund_name|fund_cusip|fund_ticker|security_group|security_type|security_number|security_cusip|security_sedol|security_isin|security_ticker|security_description|quantity|market_value|notional_value|percent_of_market_value|percent_of_net_assets`).
- **No vendor call in round 1.** No Bloomberg (R-21 scripted legs are enrichment), no OpenAI (FWD-7 is enrichment). No
  alert, monitor or notifier (C-NO-NOTIFIER).
- **Classification in round 1:** `asset_class` from the source's `security_group`/`security_type` (Cash/Currency -> the
  vocabulary's cash values via `etf_positioning_gold.is_cash_sentinel`/`classify(is_cash, None)`; common stock ->
  Equity); equity `sub_asset_class` and every GICS level are NULL with status `UNRESOLVED` and source `none (GICS is
  Bloomberg enrichment)`. Row `ETFS_RIVALS-Z-S1` (the vocabulary's sector-valued sub-asset class vs C-SHAPES) binds the
  enrichment round, not this one.

**Battery findings touching this cell:** comp-iam RUN -- AC3 IS the lens's instrument for the five role policies. comp-schedule RUN at L5 -- the standing notifier moratorium binds: NO alarm, NO SNS, NO metric filter; the only cadence armed is the two schedules named in the cell.

## 3. SURFACES AND BOUNDS

You READ (never edit):
- `infra/aws/terraform/etfs-netassets/`
- `infra/aws/terraform/cot-pipeline/s3-notifications.tf`
- `infra/aws/terraform/modules/`
- `infra/aws/lambda/README.md`
- `lib/research/identity/`
- `data/etfs/scripts/rivalfunds/`
- `lib/opal_naming.py`
- `lib/trading_calendar.py`
- `infra/logic/registry/`
- `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/`
- the captured BASG archive, `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\amgt-reconn-daily-census-20260929\basg\` (outside your worktree; read-only).

You WRITE only the `<paths>` below (plus your own `deliverables/0.9.0_WK_ETFS_RIVALS~3/`). NEVER: `etfs-netassets-daily` or its homes; the
bucket's existing tier-first keys (`bronze/`, `silver/`, `gold/`, `daily/`, `platinum/`); `opal-data-assets`; any Bloomberg or
OpenAI call; any alert, alarm, SNS or monitor; any file another cell of this round owns. Write unit tests beside the code (`data/etfs/scripts/rivalfunds/tests/`), run with `python -m pytest <file> -q` from the tree root.

<paths>
data/etfs/scripts/rivalfunds/sweep.py
data/etfs/scripts/rivalfunds/tests/test_d1_*.py
infra/aws/lambda/etfs-pipeline/etfs-rivalfunds-*
infra/aws/lambda/etfs-pipeline/rivalfunds-*
infra/aws/lambda/etfs-pipeline/rivalfunds_package.py
infra/aws/terraform/etfs-rivalfunds/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- terraform plan on a throwaway local state: create-only, five Lambdas, EventBridge-only notification, 07:00 ET schedule, no alarm (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/d-1.AC1.py`)
- **AC2** -- the sweep runs exactly the stages missing an output marker, in order; a second sweep runs nothing (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/d-1.AC2.py`)
- **AC3** -- generated names/policies byte-equal a regeneration; IAM simulation: no write outside builder prefixes, no delete (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/d-1.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-d-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/d-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-d-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/d-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC3" cell_refs="RIV-d-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/d-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/ETFS_RIVALS.TO-RIV-d-1.daily-run-lambdas-schedule-triggers-sweep.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-d-1.daily-run-lambdas-schedule-triggers-sweep`. Report once, with:
- each criterion's verdict line and the output lines above it;
- the files you wrote;
- the `ci/lambda-source-map.json` entries the COO must add at the merge, and the plan's resource count;
- any row you filed (id and one line).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` v0.2
(@01e5499ae7, L4-R ADMITTED @87321c4243). Decomposition round 1, cell `RIV-d-1`. Checks issuer-written at
`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/`, dry-run at the base before the cut (every one FAILS at the base, as a build or live check must).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>1</round>
<slot>~3</slot>
<fabric>site-z</fabric>
