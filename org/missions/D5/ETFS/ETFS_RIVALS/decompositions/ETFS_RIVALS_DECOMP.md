# ETFS_RIVALS -- DECOMPOSITION, ROUND 1, THE THREAD (FWD-1 for BASG, H1-H7 crossed once)

```json
{
 "project": "ETFS_RIVALS",
 "round": 1,
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md@808f1eb302 (v0.2, L4-R ADMITTED; bytes of @01e5499ae7 moved from D4)",
 "prd_version": "v0.2",
 "author": "2.0.0_SA_COO~RV",
 "cells": 9,
 "chains": 4,
 "join_cells": 1,
 "frozen": true
}
```

**Input:** PRD v0.2 THE THREAD (items 1-7) and SURFACE MANIFEST. **Output of this round:** one live BASG journey, issuer
site -> bronze -> silver -> `canonical_shape` -> `trade_schedule` -> the day's page at platinum -> `/rivalfunds`, fired
from AWS. Enrichment (the other five funds, Bloomberg, AI, FWD-2..9) is the PRD's ENRICHMENT BACKLOG and is NOT cut here.

## Rulings reaching every cell

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

## Cross-project sequencing

- ETFS_RIVALS is not listed in `org/missions/SEQUENCE.yaml` (sequence-check 2026-09-30: unsequenced; no cap ruled; 6
  COO lanes live on site Z).
- `etfs-netassets-daily` (ETFS_INGEST) is never read, extended or migrated (C-SEPARATE-PIPELINE).
- `ETFS_GUARDRAIL`'s armed gates (comp-schedule G-1..: etfs-reports-monthly-run) touch `etfs-reports-*`, not this
  pipeline's prefixes or names.

## 1. THE DOMAIN, BY SUBTRACTION

Domain = the PRD's THE THREAD items 1-7 (H1-H7 for BASG), printed denominator 7.

| hop | PRD thread item | cell(s) | residue |
|---|---|---|---|
| H1 homes | 1 | RIV-c-1 (homes module; registry already landed @d451070fb1) | 0 |
| H2 backfill into issuer bronze | 2 | RIV-c-1 (collector code), RIV-d-2 (the served backfill landing) | 0 |
| H3 silver | 3 | RIV-s-1 | 0 |
| H4 gold | 4 | RIV-g-1 (`canonical_shape`), RIV-g-2 (`trade_schedule`) | 0 |
| H5 page + serving | 5 | RIV-p-1 (render, platinum write), RIV-w-1 (gateway routes + grant), RIV-d-2 (deploy) | 0 |
| H7 guardrails | 6 | RIV-p-1 | 0 |
| H6 daily + AWS reachability | 7 | RIV-r-1 (first test), RIV-d-1 (schedule, triggers, wrappers), RIV-d-2 (apply + live fire) | 0 |

7 of 7 hops owned; residue 0. Manifest surfaces with no round-1 cell, by subtraction from the SURFACE MANIFEST: the
Bloomberg morning-vehicle leg (READS Bloomberg; enrichment FWD-3), OpenAI (enrichment FWD-7), the identity layer's
`add_security` registration (Bloomberg-backed; enrichment). Each is in the PRD's ENRICHMENT BACKLOG.

## 2. THE RECTANGLE -- 9 cells

Status vocabulary (Rule 24 (i)): `NOT-EVALUATED` | `ABSENT` (measured: nothing in the tree) | `PARTIAL` (measured:
something exists and does not meet the cell) | `PRESENT` (measured: meets the cell). Every status below is measured at
the cut (2026-09-30 ~06:45Z).

| cell | hop | status (evidence) | risk floor |
|---|---|---|---|
| `RIV-c-1` | H1+H2 | ABSENT (`data/etfs/scripts/rivalfunds/` does not exist) | LOCAL |
| `RIV-s-1` | H3 | ABSENT (same) | LOCAL |
| `RIV-g-1` | H4a | ABSENT (same) | LOCAL |
| `RIV-g-2` | H4b | ABSENT (same; method proven in `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/scripts/trade_inference_probe.py`) | LOCAL |
| `RIV-p-1` | H5+H7 | ABSENT (same) | LOCAL |
| `RIV-w-1` | H5 serving | ABSENT (`infra/aws/ec2/opal-gateway/app/rivalfunds_view.py` does not exist) | WORLD (infra path; nothing applied) |
| `RIV-d-1` | H6 | ABSENT (`infra/aws/terraform/etfs-rivalfunds/` does not exist; `opal-data-etfs` carries no `aws_s3_bucket_notification` in any `*.tf`) | WORLD (infra path; plan only) |
| `RIV-r-1` | H6 first test | NOT-EVALUATED (brief IV.1: none of the six fetched from AWS) | WORLD |
| `RIV-d-2` | H2/H5/H6 live | ABSENT (nothing deployed; no page exists) | WORLD |

## 3. THE CELLS -- 9 (round 1)

### `RIV-c-1` -- package core + the issuer collector, BASG adapter (H1, H2 code)

Build the package `data/etfs/scripts/rivalfunds/` core and the issuer collector:
- `__init__.py`; `homes.py` -- every address and name this pipeline uses, each computed by `address()`/`name()` at import
  (the list in the rulings above), raising on a builder refusal; `markers.py` -- write/read a batch-complete marker at the
  state address, idempotent on `batch_id` (a second write of the same batch is a no-op returning the existing marker);
  `sinks.py` -- `s3` and `local:<dir>` sinks with read-back on put (the bytes read back equal the bytes written, else raise).
- `collector_issuer.py` + `adapters/basg.py` -- `handler_entry` for stage `fetch-holdings`. `daily`: fetch BASG's file for
  T-1, `prev_trading_day(<today in America/New_York>)` (`lib/trading_calendar.py`), land the raw bytes unchanged in issuer bronze at
  `address('issuer-site','etfs','bronze','holdings','date=<acq>', 'basg-<ts>-<sha256[:12]>.txt')` with a JSON sidecar
  beside it (capture time UTC, requested date, URL, HTTP status, sha256, byte length, `claimed_report_date` = the file's
  internal `date` column value for BASG rows, `date_evidence` = `internal-date-column`, `status`). `backfill`: the same for
  every trading day in `[start, end]`, one file per day, a 404 recorded as status `NOT-PUBLISHED` in a sidecar and not a
  failure. A file whose internal date for BASG rows does not equal the requested date, or that has no BASG rows, lands with
  status `DATE-MISMATCH` / `NO-FUND-ROWS` and NO report date (`report_date` is set only on status `OK`). The sidecar also
  carries `runtime` = the `AWS_LAMBDA_FUNCTION_NAME` environment value, else `local`. The landing act is one public function
  both modes call: `land_bronze(raw: bytes, requested_date: str, source_url: str, sink: str, captured_at: str | None = None)
  -> dict` (the sidecar, with `bronze_uri` and `status`), the bronze `date=` taken from `captured_at` (default now, UTC).
  Write the stage marker when the batch is whole. Retry: 3 attempts, backoff; timeout 30 s per request.
- tests in `data/etfs/scripts/rivalfunds/tests/test_c1_*.py`.

### `RIV-s-1` -- bronze to typed silver, the BASG issuer shape (H3)

`data/etfs/scripts/rivalfunds/silver_issuer.py`, `handler_entry` for stage `build-silver`: read the issuer bronze objects
of a batch (the `fetch-holdings` marker's outputs) or, in `replay`, every bronze object under the issuer bronze prefix for a
date range; parse pipe-delimited utf-8-sig; type every source column (dates, decimals as float64, identifiers as strings
with leading zeros kept); keep EVERY source row and column (all Brown funds, cash and currency lines), plus lineage columns
(`bronze_uri`, `sha256`, `captured_at`, `parser_version`); dedupe ACROSS captures only: when two captures carry the same
report date, the latest capture's rows win whole and the other capture's are dropped (count recorded); rows within one
capture are never dropped; a replay of bronze already in silver adds nothing; write Parquet to
`address('issuer-site','etfs','silver','holdings','date=<report_date>', 'basg-<capture_id>.parquet')`; skip bronze whose
sidecar status is not OK (counted in `detail.skipped_not_ok`, never given a date); write the marker. Tests `tests/test_s1_*.py`. Consumes RIV-c-1's
bronze layout and sidecar.

### `RIV-g-1` -- gold `canonical_shape` for BASG (H4a)

`data/etfs/scripts/rivalfunds/gold_canonical_shape.py`, `handler_entry` for stage `build-canonical-shape` (first half):
coalesce the issuer silver of a report date (in `replay`, every silver report date) into the master shape of spec S4
(`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/GOLD_TABLES_AND_PROMPTS.md` S4): grain one
disclosed position per fund x report date x dataset revision, unique on (`fund_id`, `snapshot_id`, `position_id`); the
S4 families fund, position identity, economic position, instrument, Opal classification, GICS hierarchy (SEPARATE
fields, C-SHAPES v0.2), provider classifications, dates and lineage, research quality, and `extra_attributes` (a
source-namespaced map keeping every source field that has no canonical column). Identity through
`lib/research/identity/crosswalk.resolve()` tried on CUSIP, then ISIN, then SEDOL, then ticker; a miss keeps the position
with `resolution_status = UNRESOLVED` and the raw identifier, never a guessed key. Cash, currency and unidentified
positions stay as rows. Classification per the round-1 ruling above. Filter `fund_ticker == 'BASG'`. Columns the checks
read by name (more S4 columns are welcome): `fund_id, fund_ticker, report_date, snapshot_id, position_id, security_id,
raw_identifier, resolution_status, quantity, market_value, weight, position_type` (`cash` for cash and currency lines),
`asset_class, sub_asset_class, sub_asset_class_status, gics_sector, gics_industry_group, gics_industry, gics_sub_industry,
gics_status, extra_attributes` (a JSON string), `source_channel, bronze_uri, sha256`. Write
`address('rivalfunds','etfs','gold','canonical_shape','date=<report_date>', 'holdings-<revision>.parquet')`. Tests
`tests/test_g1_*.py`. Consumes RIV-s-1's silver.

### `RIV-g-2` -- gold `trade_schedule` for BASG (H4b, the foundation)

`data/etfs/scripts/rivalfunds/gold_trade_schedule.py`, `handler_entry` for stage `build-trade-schedule` (fired by the
`build-canonical-shape` marker, or in `replay` over every `canonical_shape` date), with the inference as a pure public
function `infer_trades(canonical: DataFrame) -> DataFrame` over `canonical_shape` rows of one fund: for each pair of
consecutive GENUINELY dated BASG reports in `canonical_shape`, over non-cash positions keyed by `security_id` when RESOLVED,
else by the raw CUSIP with confidence `UNRESOLVED` (C-TRADE-SCHEDULE, spec S5 `trade_schedule`): flow factor `f` = median of
`q_t / q_{t-1}` over positions held on both dates; discretionary shares `q_t - f*q_{t-1}`; a trade is a residual of at
least 0.2% of prior shares, plus every entry and exit; action `entry|add|trim|exit`; window `(prior_report_date,
report_date]`, `date` = window end, window length in trading days; estimated price = issuer implied close
(`market_value / quantity`) of the report carrying the position (the prior report for an exit), band `null` with reason
`bloomberg-band-enrichment`; notional = discretionary shares x price; weights before/after; confidence class
`CLEAN|FLOW-WINDOW|STALE-WIDENED|ID-CHANGE|CORP-ACTION|UNRESOLVED`; columns at least `fund_ticker, security_key, action,
window_start, window_end, shares_before, shares_after, flow_factor, discretionary_shares, est_price, est_notional,
weight_before, weight_after, window_trading_days, confidence`; `corporate_actions_applied = none-available-round-1`,
`dividends_applied = none-available-round-1`. Never placed on a day finer than its window. A pair of positions that exit
and enter on the same window with equal quantity x price within 1% is flagged `ID-CHANGE` rather than two trades. Write
`address('rivalfunds','etfs','gold','trade_schedule','date=<report_date>', 'trades-<revision>.parquet')` and the stage
marker. Tests `tests/test_g2_*.py`. Consumes RIV-g-1's `canonical_shape`.

### `RIV-p-1` -- the day's page and the pre-publish guardrails (H5 render, H7)

`data/etfs/scripts/rivalfunds/publish_page.py`, `guardrails.py`, `render.py`, `handler_entry` for stage `publish-page`:
render ONE self-contained HTML page (inline CSS and inline SVG only; no external script) for the publish day: it LEADS
with BASG's most recent trades (C-ONE-SIGNAL), newest window first; each trade row opens a trace panel showing the two
reports it was inferred from (the position's row in each `canonical_shape` snapshot: date, quantity, market value, weight)
and, for each report, the issuer file URL, bronze key and sha256. Below: the latest report's holdings (cash and unresolved
visible) and a data-status block naming source, report dates and the round-1 absences (no GICS, no Bloomberg band, no
dividends). Before any write, run the six C-GUARDRAILS checks (report-date freshness, content repeat, completeness,
identity coverage, analysis grounding, render and read-back); round 1 has no AI text, so analysis grounding returns
`NOT-APPLICABLE` with that reason; thresholds are read from `guardrails_config.json`, every value marked `PROVISIONAL`
(C-GUARDRAILS: the real thresholds come from a named enrichment cell). A failed check publishes the page with BASG marked
`data-status="not-updated"`, the failing check named, and NO trades table; it never renders failed figures as normal. The
event key `plant_failure: "<check>"` forces that check to fail (the H7 exercise). Sections carry `id="trades"` and
`id="holdings"`; each trace panel carries `class="trace"`. The manifest carries `checks` (`[{check, status, reason}]`,
names `report_date_freshness, content_repeat, completeness, identity_coverage, analysis_grounding, render_readback`),
`readback`, `revisions` and `runtime` (as the sidecar's). Write
`index.html` and `manifest.json` (inputs with URIs and hashes, check results) to
`address('rivalfunds','etfs','platinum','page','date=<day>', ...)` with read-back; a rerun that changes the bytes keeps
the prior object under `revisions/<utc-ts>/` and records it in the manifest, never a silent overwrite. Tests
`tests/test_p1_*.py`. Consumes RIV-g-2's `trade_schedule` and RIV-g-1's `canonical_shape`.

### `RIV-w-1` -- the gateway routes and read grant (H5 serving)

`infra/aws/ec2/opal-gateway/app/rivalfunds_view.py` (new), modelled on `sprint_view.py`: `is_rivalfunds_path(path)`,
`rivalfunds_page` (`/rivalfunds` -> the newest published day), `rivalfunds_day` (`/rivalfunds/{day}`, day
`YYYY-MM-DD`), `rivalfunds_archive` (`/rivalfunds/archive`, a delimiter listing of the platinum `page/` prefix whose
`CommonPrefixes` are `date=YYYY-MM-DD/`), reading `index.html` with the 2 MB cap; module-level `_s3()`, `_viewer(request)`,
`_list_days()` and `_location() -> (bucket, key_prefix)` as `/sprint` shapes them; bucket and prefix never typed: the
gateway host carries no `lib/`, so `app/gen_rivalfunds_location.py` (new) writes `app/rivalfunds_location.json` from
`address('rivalfunds','etfs','platinum','page', ...)` and the module reads that file; viewers = any signed-in account (C-SERVING;
`identity.get_user_email` non-empty), each view audit-logged like `/sprint`. `infra/aws/terraform/opal-gateway/rivalfunds-iam.tf`
(new): one `aws_iam_role_policy` on `aws_iam_role.gw` whose document is `file()` of
`infra/aws/terraform/opal-gateway/rivalfunds-iam.policy.json` (new, written by the same generator from `address()`):
`s3:GetObject` on the page prefix `/*` only; `s3:ListBucket` on the bucket with `s3:prefix` limited to the page prefix;
no Put, no Delete, nothing else in the bucket. Tests
`infra/aws/ec2/opal-gateway/app/tests/test_rivalfunds_view.py` (new). The route lines in `server.py` and any `config.py`
entry are HOOKUPS, added by the COO at the merge; the cell's report names them.

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

### `RIV-r-1` -- AWS reachability of BASG's issuer site (H6 first test)

From an Opal AWS host, one read-only HTTPS GET of BASG's issuer file for the last trading day, recording status code, bytes,
elapsed time and the first line; and the same GET for `https://brownadvisory.filepoint.live/` root. Instrument: `aws ssm
send-command` with `AWS-RunShellScript` on the opal-gateway instance (read its instance id from
`infra/aws/ec2/EC2_MANIFEST.json`), a single `curl -sS -o /tmp/basg.txt -w ...` plus `head -1 /tmp/basg.txt` and
`rm /tmp/basg.txt`; nothing else runs on the host. Result recorded as JSON under the cell's deliverables. A non-200 or a
bot-challenge body is a finding (a row), not a retry loop.

### `RIV-d-2` -- the live thread (join): apply, deploy, backfill, fire, read (H2, H5, H6 live)

Spawned only after RIV-c-1..RIV-p-1, RIV-w-1, RIV-d-1 and RIV-r-1 are merged with their hookups, in a fresh worktree from
the merged HEAD. Under a NEVER-2 ledger entry opened first (`.tools/deploy_ledger.py open`, entry and sentinel both
committed) and the never-widen pair signed by 1.0.0_SA_CTO~Z and 2.0.0_SA_COO~RV (blast radius: new objects under the eight
builder prefixes only; the bucket's notification configuration from empty to EventBridge-only; five new Lambdas, their
roles and two schedules; the gateway read policy; the gateway code with the three `/rivalfunds` routes; rollback per key in
the entry). Acts, in order: `safe-apply` the `etfs-rivalfunds` stack and the gateway policy; deploy the gateway through
`infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`; invoke
`etfs-rivalfunds-fetch-holdings-lambda` with `mode=backfill` 2025-06-13..the last trading day (QA-class landing, PRD
C-SOURCE-POLICY), let the markers drive silver, gold and the page (or invoke the sweep); read back the day's page; close
the ledger. Records under the cell's deliverables. The scheduled 07:00 fire of the next trading day is the acceptance and
is read at the close, never waited on.

## 4. PLACEMENT AXIS

Every cell executes on the site-Z fabric (this box, `C:\Users\Opal Bloomberg\Desktop\ajb_workspace`), per the project
row's `fabric_ruling`. AWS acts (RIV-r-1, RIV-d-1's plan, RIV-d-2) run from here through the `.tools/aws` shim.

## 5. DEPENDENCY EDGES AND CHAINS

Edges (consumer <- producer, keyed to the producer's task order reading `complete` with a VALID instance):
- `RIV-s-1` <- `RIV-c-1` (bronze layout + sidecar)
- `RIV-g-1` <- `RIV-s-1` (silver)
- `RIV-g-2` <- `RIV-g-1` (`canonical_shape`)
- `RIV-p-1` <- `RIV-g-2` (`trade_schedule`)
- `RIV-d-2` <- `RIV-p-1`, `RIV-w-1`, `RIV-d-1`, `RIV-r-1` (the join: it deploys what they built and reads the reach test)

Chains before the join, M = 4: A = c-1 -> s-1 -> g-1 -> g-2 -> p-1; B = w-1; C = d-1; D = r-1. The join `RIV-d-2` runs
after all four. RIV-d-1 wraps the stage modules through the fixed entry contract, not through their file contents, so it
carries no edge on chain A; its plan packages whatever is merged at the time and RIV-d-2 re-packages at apply.

## 6. BATTERY DISPOSITION (a thread round)

- **`comp-adversary` -- DECLARED-NOT-APPLICABLE:** thread round; the lens runs on the enrichment round that touches its
  surface.
- **`comp-schedule` -- RUN at the cut (2026-09-30 ~06:40Z), denominator printed by the tool:** 39 gates armed over five
  carriers (C1 sentinel 23, C2 deploy-ledger 20, C3 moratoria 12, C4 scope-guard 21 not decidable, C5 project-blocking 334
  not decidable). None names `opal-data-etfs`'s rivalfunds prefixes, the five names, or `opal-gateway`; the ETFS gates in
  view are `ETFS_GUARDRAIL`'s `etfs-reports-monthly-run` reads. The shared tree's `.open_deploys/` holds no entry
  matching gateway/etfs/rival (23 entries listed). Blindness: 50 linked worktrees were NOT read; RIV-d-2 reads every
  worktree's `.open_deploys/` before acting (NEVER-2). The standing notifier moratorium binds RIV-d-1: no alarm or SNS.
- **`comp-iam` -- RUN, because the thread touches IAM (RIV-w-1's gateway policy, RIV-d-1's Lambda roles), and its
  instrument is the cells' own:** RIV-w-1's `simulate-custom-policy` (page prefix ALLOWED; bronze prefix and another
  product's key DENIED) and RIV-d-1's simulation of each role's policy (its own prefixes ALLOWED; the bucket's tier-first
  `bronze/` root and `opal-data-assets` DENIED). Blindness: the lens sees the new policies and the named resources, not the
  rest of the account; the gateway role's existing statements are unchanged by this round.

## 7. RULE 24 FOUR-POSTULATE RECORD

- **(i) MECE over a declared domain:** domain = PRD THE THREAD items 1-7, denominator 7, subtraction in section 1 leaves 0.
  Falsification of the domain: the SURFACE MANIFEST was read unscoped; the three surfaces it holds with no round-1 cell
  (Bloomberg leg, OpenAI, `add_security`) are each an ENRICHMENT BACKLOG item by the PRD's own text, so the domain is the
  round's, not narrower than the sentence beside it. Cells are disjoint by write set (section 8 table).
- **(ii) Same grain:** every cell is one hop adapter (a stage module, a route module, a stack, a probe, or the live join).
- **(iii) Intent coherence:** one axis, "what round 1 must build or exercise so FWD-1's journey runs once, live".
- **(iv) State coherence:** the status vocabulary `NOT-EVALUATED|ABSENT|PARTIAL|PRESENT` is measured per cell; the
  remedy of any one cell does NOT move another cell's status (the join RIV-d-2 moves only live state, never a build
  cell's), and none of them moves FWD-2..FWD-9 (enrichment).

## 8. GATES, WRITE SETS AND THE CLOSE RUN

| cell | writes (disjoint) |
|---|---|
| RIV-c-1 | `data/etfs/scripts/rivalfunds/{__init__,homes,markers,sinks,collector_issuer}.py`, `data/etfs/scripts/rivalfunds/adapters/`, `data/etfs/scripts/rivalfunds/tests/test_c1_*.py` |
| RIV-s-1 | `data/etfs/scripts/rivalfunds/silver_issuer.py`, `tests/test_s1_*.py` |
| RIV-g-1 | `data/etfs/scripts/rivalfunds/gold_canonical_shape.py`, `tests/test_g1_*.py` |
| RIV-g-2 | `data/etfs/scripts/rivalfunds/gold_trade_schedule.py`, `tests/test_g2_*.py` |
| RIV-p-1 | `data/etfs/scripts/rivalfunds/{publish_page,guardrails,render}.py`, `data/etfs/scripts/rivalfunds/guardrails_config.json`, `tests/test_p1_*.py` |
| RIV-w-1 | `infra/aws/ec2/opal-gateway/app/{rivalfunds_view.py,gen_rivalfunds_location.py,rivalfunds_location.json}`, `infra/aws/ec2/opal-gateway/app/tests/test_rivalfunds_view.py`, `infra/aws/terraform/opal-gateway/rivalfunds-iam.{tf,policy.json}` |
| RIV-d-1 | `infra/aws/terraform/etfs-rivalfunds/`, `infra/aws/lambda/etfs-pipeline/{etfs-rivalfunds-*,rivalfunds-*}/`, `infra/aws/lambda/etfs-pipeline/rivalfunds_package.py`, `data/etfs/scripts/rivalfunds/sweep.py`, `tests/test_d1_*.py` |
| RIV-r-1 | its deliverables folder only |
| RIV-d-2 | `org/critical_paths/change_management/`, `org/critical_paths/.open_deploys/etfs-rivalfunds-thread-r1.json`, `infra/aws/ec2/EC2_MANIFEST.json` (the deploy wrapper's record), its deliverables folder |

Hookups at the merge (the COO's, one commit): `server.py` import, guard branch and four `Route` lines for `/rivalfunds`;
any `config.py` entry RIV-w-1 names; `ci/lambda-source-map.json` entries RIV-d-1 names.

The close run (the COO's one real run of FWD-1): a signed-in read of `/rivalfunds` for BASG on the live gateway, the
newest trade opened and traced to its two reports and the issuer file, screenshot committed under
`deliverables/2.0.0_SA_COO/`; then Andrew's own trace is FWD-1's DONE WHEN.

## 9. WHAT THIS DECOMPOSITION DOES NOT CLAIM

- It does not claim BASG's issuer site answers from AWS (RIV-r-1 measures it; a refusal re-shapes RIV-d-2 at the recut).
- It does not claim the crosswalk resolves BASG's ~35 holdings; unresolved positions are carried and counted.
- It does not claim trade dates finer than the window, a Bloomberg price band, dividends or corporate actions in round 1.
- It does not claim the provisional guardrail thresholds are right; the named enrichment cell sets them from real days.
- It does not claim the other five funds, the Bloomberg fallback, the AI analyses or FWD-2..FWD-9.
