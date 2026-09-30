# ETFS_RIVALS task order -- `RIV-d-2` -- ROUND 1 (THE THREAD, BASG): THE LIVE THREAD (JOIN): APPLY, DEPLOY, BACKFILL FROM AWS, FIRE, READ (H2, H5, H6 live)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-d-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~5</issued_to>
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

1. `RIV-c-1`, `RIV-s-1`, `RIV-g-1`, `RIV-g-2`, `RIV-p-1`, `RIV-w-1`, `RIV-d-1` and `RIV-r-1` are complete and MERGED, and your worktree is cut from that merged HEAD. The hookups (server.py routes, lambda source map) are YOUR first act, per section 2b (ISSUER AMENDMENT 1). Print `git log --oneline -3` first.
2. BOTH never-widen halves are COMMITTED: the COO half `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/NEVER_WIDEN_HALF_COO_D2.md` and 1.0.0_SA_CTO~Z's half, named in your spawn line. Act only inside them.
3. `RIV-r-1`'s result (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~4/r1_reachability.json`) reads HTTP 200 with BASG bytes. If it does not, STOP with a BLOCKING row: the collector cannot run from AWS as built.
4. NEVER-2: before the first act, read EVERY live worktree's `org/critical_paths/.open_deploys/` (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`), union them, print the per-tree denominator; an open entry touching opal-gateway or opal-data-etfs is a BLOCKING row. Then open the ledger entry `etfs-rivalfunds-thread-r1` with `.tools/deploy_ledger.py open` and COMMIT the entry and its sentinel before any apply; close it at completion or roll back and say so.

## 1. YOUR CELL (inlined verbatim from the decomposition)

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

## 1b. THE ACT, STEP BY STEP (each act inside the signed halves)

1. `safe-apply` the `infra/aws/terraform/etfs-rivalfunds` stack (run `infra/aws/lambda/etfs-pipeline/rivalfunds_package.py`
   first), then the `infra/aws/terraform/opal-gateway` policy file `rivalfunds-iam.tf` (a targeted apply of that one
   `aws_iam_role_policy` if the stack carries other drift -- print the plan and act only if it is create-only for it).
   Run `ci/record-terraform-deploy.sh` per `infra/aws/lambda/README.md` if it applies.
2. Deploy the gateway: `bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`,
   then `curl -s -o /dev/null -w '%{http_code}' https://mcp.opalinvest.dev/healthz` (or the health route the README names)
   reads 200.
3. Backfill from AWS: invoke `etfs-rivalfunds-fetch-holdings-lambda` with
   `{"mode":"backfill","start":"2025-06-13","end":"<last trading day>","batch_id":"backfill-r1","sink":"s3","date":"<act day>"}`
   (split into date ranges if one invocation would exceed the Lambda timeout; each range its own batch id).
4. Let the markers drive silver, gold and the page; if any stage has not run within 10 minutes, invoke
   `etfs-rivalfunds-daily-lambda` (the sweep) with `{"date":"<act day>","mode":"daily","batch_id":"sweep-r1","sink":"s3"}`.
   Silver and gold must process the whole backfill (`replay`), so the page's trade schedule spans BASG's archive.
5. Write `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~5/d2_live.json` with `act_day`,
   `newest_basg_report_date`, `gateway_instance_id`, `gateway_app_root`, the Lambda invocation request ids, and the S3
   prefixes with object counts.
6. Run AC1-AC3. Close the ledger entry (or roll back per key and say so). Rollback per key: delete-by-prefix of the new
   objects is a HUMAN word, never yours; a failed apply is rolled back by `terraform destroy -target` of the new resources
   only, and the notification configuration is returned to empty.
7. The scheduled 07:00 America/New_York fire of the next trading day is the acceptance and is read by the COO at the close;
   do not wait for it.

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

**Battery findings touching this cell:** comp-schedule RUN at L5 found no open deploy entry on the shared tree touching opal-gateway or opal-data-etfs, but did NOT read the 50 linked worktrees -- begin-condition 4 is that read. comp-iam RUN -- the policies you apply were simulated at RIV-w-1 AC3 and RIV-d-1 AC3.

## 2b. ISSUER AMENDMENT 1 (2026-09-30, 2.0.0_SA_COO~RV) -- the hookups ride this order

The issuer's own hookup commit was refused by the lane gate. `infra/aws/ec2/opal-gateway/app/server.py` is lane
CLOUD_OPS_OR_ETL, and `infra/aws/lambda/ci/lambda-source-map.json` is under an IRPT grant. So the hookups ride this
order, whose `<paths>` now name both files. The exact change is filed as a patch:
`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/hookup_d2.patch`.
- `server.py`: import `rivalfunds_view`; the `/login` guard branch admits `rivalfunds_view.is_rivalfunds_path(path)`; four
  routes are added beside `/sprint`.
- The source map: five `functions` entries, with `iam_role` read from `generated.auto.tfvars.json`.

As your FIRST act, before the ledger entry:
1. `git apply --check <the patch>`, then `git apply <the patch>`. If it does not apply, STOP with a BLOCKING row; never
   hand-merge it.
2. `python -m pytest infra/aws/ec2/opal-gateway/app/tests/test_rivalfunds_view.py -q` stays green.
3. Commit the two files, one commit, before anything else.
At the apply, record each Lambda's `artifact_sha256`, `last_deployed_commit` and `last_deployed_at` into its source-map
entry, per `infra/aws/lambda/README.md`. The gateway read policy's name is builder output as of TO-RIV-w-1's amendment
(`gateway-rivalfunds-read-policy`): if your HEAD does not carry it, STOP. safe-apply refuses the old name.

## 3. SURFACES AND BOUNDS

You READ (never edit):
- `infra/aws/terraform/etfs-rivalfunds/`
- `infra/aws/terraform/opal-gateway/`
- `infra/aws/ec2/opal-gateway/`
- `infra/aws/ec2/safe-ec2-deploy.sh`
- `.tools/deploy_ledger.py`
- `.tools/safe-apply`
- `data/etfs/scripts/rivalfunds/`
- `lib/opal_naming.py`
- `lib/trading_calendar.py`
- `infra/logic/registry/`
- `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/`
- the captured BASG archive, `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\amgt-reconn-daily-census-20260929\basg\` (outside your worktree; read-only).

You WRITE only the `<paths>` below (plus your own `deliverables/0.9.0_WK_ETFS_RIVALS~5/`). NEVER: `etfs-netassets-daily` or its homes; the
bucket's existing tier-first keys (`bronze/`, `silver/`, `gold/`, `daily/`, `platinum/`); `opal-data-assets`; any Bloomberg or
OpenAI call; any alert, alarm, SNS or monitor; any file another cell of this round owns. 

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/.open_deploys/etfs-rivalfunds-thread-r1.json
org/critical_paths/change_management/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the served page in the real bucket leads with trades, names the newest report, written by the publish Lambda, guardrails pass (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/d-2.AC1.py`)
- **AC2** -- the deployed gateway files hash equal to HEAD (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/d-2.AC2.py`)
- **AC3** -- >= 300 BASG raw objects in real issuer bronze written by the fetch Lambda, plus silver/gold for the newest report (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/d-2.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-d-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/d-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-d-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/d-2.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC3" cell_refs="RIV-d-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/d-2.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~5/ETFS_RIVALS.TO-RIV-d-2.live-thread-apply-deploy-backfill-fire.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-d-2.live-thread-apply-deploy-backfill-fire`. Report once, with:
- each criterion's verdict line and the output lines above it;
- the files you wrote;
- every S3 prefix written with object counts, the ledger entry's open and close commits, the apply outputs, and the act day;
- any row you filed (id and one line).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` v0.2
(@01e5499ae7, L4-R ADMITTED @87321c4243). Decomposition round 1, cell `RIV-d-2`. Checks issuer-written at
`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/`, dry-run at the base before the cut (every one FAILS at the base, as a build or live check must).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>1</round>
<slot>~5</slot>
<fabric>site-z</fabric>
