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

## 2c. ISSUER AMENDMENT 2 (2026-09-30 ~11:3xZ, 2.0.0_SA_COO~RV) -- rules BLOCKING row ETFS_RIVALS-Z-W5-S1

**State at this amendment:**
- Gate 1 held: a HEAD deploy would ship 23 other projects' gateway files.
- The `etfs-rivalfunds` stack (39) and `gateway-rivalfunds-read-policy` (1) are APPLIED, create-only, and inside the pair.
- Ledger `etfs-rivalfunds-thread-r1` is OPEN with L1/L2 closed. Its window ends ~16:13Z.
- Everything is on branch `wk-ETFS_RIVALS-5` in `C:	mp\wk-rivals-5`.

The issuer rules: NO rollback. Finish in two legs, both inside the signed pair (COO half @462db51701, CTO half @f468b621da).

**LEG A -- the data plane, now. It needs no gateway.**
1. Print the backfill request volume (CTO condition 4).
2. Invoke the fetch Lambda in `backfill` ranges.
3. Let the markers drive silver, gold and the page, or invoke the sweep.
4. Write `d2_live.json` (below).
5. Run AC1 and AC3.
6. Stamp the five source-map entries (`artifact_sha256`, `last_deployed_commit`, `last_deployed_at`).

**LEG B -- the gateway, from a DEPLOY-ONLY commit, never HEAD.**
1. `git worktree add -b deploy-rivalfunds-gw-r1 C:	mp\wk-rivals-5gw 093fc247c6`. That is the EC2_MANIFEST's deployed
   commit; re-read the manifest and STOP if it moved.
2. Bring in exactly the key-16 files from HEAD:
   - `app/rivalfunds_view.py`, `app/rivalfunds_location.json`, `app/gen_rivalfunds_location.py`, `app/tests/test_rivalfunds_view.py`
     (byte copies from HEAD);
   - the `server.py` hookup, as `git apply` of `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/hookup_d2.patch`,
     server.py hunks only (`--include=infra/aws/ec2/opal-gateway/app/server.py`).
   - If the hunks do not apply to that server.py, STOP with a row. Never hand-merge.
   - If `rivalfunds_view.py` imports anything that differs between `093fc247c6` and HEAD, STOP with a row.
3. Initialise `mcportal` as `deploy-to-ec2.sh` needs, and commit on that branch. This branch is a DEPLOY REF; it is never
   merged into CLOUD.
4. Re-run gate 1 against the deploy commit. The deployed-vs-deploy-commit diff must be exactly the key-16 files; anything
   else STOPs.
5. Then run `safe-ec2-deploy.sh` from that worktree, read `/healthz` 200, and do the CTO condition-5 read.
6. `d2_live.json` gains `gateway_deploy_commit` = that commit. The amended AC2 compares the deployed bytes to it and asserts
   its `rivalfunds_view.py` equals HEAD's.
7. Record the deploy ref in the ledger entry and the EC2 manifest.

**Close:**
- Close the ledger when both legs land.
- If LEG B STOPs, LEG A still closes its keys. Leave the gateway leg OPEN in the ledger with the STOP row, and report. The
  issuer decides before ~16:13Z.
- Never deploy HEAD's gateway directory.

## 2d. ISSUER AMENDMENT 3 (2026-09-30 ~12:2xZ, 2.0.0_SA_COO~RV) -- rules BLOCKING rows ETFS_RIVALS-Z-W5-S4 and -W5-S6

**W5-S4 (gold package gap) -- fix it in this order.**
- **Cause:** `infra/aws/lambda/etfs-pipeline/rivalfunds_package.py` `STAGED` never copies the positioning vocabulary module
  that `gold_canonical_shape._epg()` loads from `/var/task/gold/etf_positioning_gold.py`.
- **The issuer's test:** it built the package in scratch with ONE added `STAGED` line,
  `("data/etfs/scripts/gold/etf_positioning_gold.py", "gold/etf_positioning_gold.py")`. It then imported
  `gold_canonical_shape`, `gold_trade_schedule` and `publish_page` in `python -I` from the built canonical-shape and
  publish-page Lambda trees: `_epg()` loaded, and the handlers were present. Negative control: with `gold/` removed, the
  same `FileNotFoundError` the Lambda raised.

Acts:
1. Add exactly that line to `STAGED`. The file is now in your `<paths>`. Change nothing else.
2. Re-run the package build, then `safe-apply` the `etfs-rivalfunds` stack. The plan must be IN-PLACE UPDATES ONLY of
   `aws_lambda_function.stage[...]` code (`source_code_hash`) for rivalfunds Lambdas: 0 create, 0 destroy, 0 other update.
   Anything else STOPs. This is key 12 of the pair, the same five functions this act created.
3. Invoke the sweep, `etfs-rivalfunds-daily-lambda` with mode daily, so gold, trade_schedule and the page run over every
   silver-marked batch.
   - If a batch is not picked up, invoke `rivalfunds-build-canonical-shape-lambda` with `mode: replay` over the silver
     prefix.
   - Read every stage's result. A NEW failure behind gold is a BLOCKING row, not a retry loop.
4. Re-stamp the five source-map entries.
5. Re-run AC1 and AC3.

**W5-S6 (LEG B stop) -- ruled IMMATERIAL; continue LEG B from step 2.**
The issuer read the diffs of `app/audit.py` and `app/config.py` between `093fc247c6` and HEAD against the names
`rivalfunds_view.py` uses:
- `audit.log_call(email, tool, args, outcome, detail)` has an identical signature at `093fc247c6` (:125).
- `get_config()` and `Config.AWS_REGION` are unchanged.
- The audit diff only adds other tools' allowlist entries. `rivalfunds_view` has no allowlist entry on either side, so its
  args are omitted identically.
- The config diff touches no name the view reads.

Continue in `C:	mp\wk-rivals-5gw` (branch `deploy-rivalfunds-gw-r1` @`093fc247c6`) from amendment 2 step 2. Every other
STOP there still binds.

Two added conditions, from `1.0.0_SA_CTO~Z` msg 27119:
- Record the deploy ref's commit hash AND the host's post-deploy file hashes in the NEVER-2 entry.
- The issuer tags the ref at the drain, so leave the branch in place.

**CTO condition 5 (OIDC read):** a worker cannot pass the Entra login. Record the SSM-hashed deployed bytes (AC2), plus a
read of the newest `platinum/page` object's bytes and sha256, as what you COULD read. The authenticated read stays OPEN for
a human with a login, as a row. Never fake it.

## 2e. ISSUER AMENDMENT 4 (2026-09-30 ~12:5xZ, 2.0.0_SA_COO~RV) -- rules BLOCKING row ETFS_RIVALS-Z-W5-S8

LEG A is DONE: AC1 and AC3 PASS, gold/trade_schedule/page served. LEG B's base moved: NFRA_MCPMSP deployed `288fa78c93` at
11:37Z, and the host matches it 79 of 79. A second release is in flight.

Ruling: the deploy ref is based on **the commit the EC2 manifest names as deployed AT ACT TIME**, never on a hash pinned in
this order. This is the same no-rider construction as amendment 2, made robust to the base moving. Steps, in order, with
no pause between steps 4 and 6:
1. Read `infra/aws/ec2/EC2_MANIFEST.json` for the gateway's `deployed_commit`; call it BASE. SSM-hash the live host's app
   files, read-only, and require an exact match to BASE for every file. Any mismatch STOPs, because a deploy is in flight
   or the manifest is stale.
2. Re-point `C:	mp\wk-rivals-5gw` (branch `deploy-rivalfunds-gw-r1`) to BASE (`git reset --hard BASE` inside that
   deploy-only worktree only).
   - Bring in the key-16 files from HEAD, as byte copies, plus the `hookup_d2.patch` server.py hunks.
   - A non-applying hunk STOPs.
   - At BASE, check the three names `rivalfunds_view.py` uses: `audit.log_call(email, tool, args, outcome, detail)`,
     `config.get_config`, `Config.AWS_REGION`. A missing one STOPs. The issuer read them present at `288fa78c93`.
3. Initialise mcportal and commit the ref. The deployed-vs-ref diff must be exactly the key-16 files.
4. IMMEDIATELY before the deploy, re-read the manifest. If BASE moved, go back to step 1, at most once, then STOP.
5. `safe-ec2-deploy.sh` from the deploy-only worktree. Then `/healthz` 200 and AC2.
6. Record in the NEVER-2 entry and `d2_live.json` / `EC2_MANIFEST.json`:
   - the ref hash;
   - BASE;
   - the host's post-deploy hashes of every key-16 file.
7. Close the ledger. The issuer tags the ref and tells the in-flight release's seat to base on it.

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
infra/aws/ec2/opal-gateway/app/rivalfunds_view.py
infra/aws/ec2/opal-gateway/app/rivalfunds_location.json
infra/aws/ec2/opal-gateway/app/gen_rivalfunds_location.py
infra/aws/ec2/opal-gateway/app/tests/test_rivalfunds_view.py
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/etfs-pipeline/rivalfunds_package.py
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
