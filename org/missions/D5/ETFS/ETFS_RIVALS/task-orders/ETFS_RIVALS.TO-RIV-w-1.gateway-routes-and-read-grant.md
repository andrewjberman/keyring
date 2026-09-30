# ETFS_RIVALS task order -- `RIV-w-1` -- ROUND 1 (THE THREAD, BASG): THE GATEWAY ROUTES `/rivalfunds`, `/rivalfunds/<day>`, `/rivalfunds/archive` AND THEIR READ GRANT (H5 serving)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-w-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
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

1. Nothing precedes this order. It builds and plans only: no `terraform apply`, no gateway deploy (those are `RIV-d-2`'s).

## 1. YOUR CELL (inlined verbatim from the decomposition)

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

**Battery finding touching this cell (comp-iam RUN):** AC3 IS the lens's instrument for the gateway policy; the gateway role's existing statements are not changed by this order.

## 2b. ISSUER AMENDMENT 1 (2026-09-30, 2.0.0_SA_COO~RV) -- the read policy's NAME is builder output

`infra/aws/terraform/opal-gateway/rivalfunds-iam.tf` names the policy `"${var.name}-rivalfunds-read"`. The value exists only in a
plan, so the commit-time naming gate passed it. safe-apply's ENFORCE naming-plan limb plans the WHOLE directory, ignoring
`-target`, and refuses `opal-gateway-rivalfunds-read -> gateway-rivalfunds-read-policy (ADDITION)`. While that addition is
unapplied and off-pattern, no seat can safe-apply anything in that directory (2.0.0_SA_COO~MS msg 27058, row
NFRA_MCPMSP-Z-W2-S3). This is an ARMED hazard on other seats: finish it first and fast.

Fix, in `rivalfunds-iam.tf` ONLY (now the whole of your `<paths>` besides the channel):
1. Add `module "gw_rivalfunds_read_policy_name" { source = "../modules/opal_name", system = "gateway", function =
   "rivalfunds-read", kind = "policy" }`, the shape `infra/aws/terraform/opal-gateway/mcpmsp_firm_roles.tf` uses (read
   it; never edit it).
2. Set `name = module.gw_rivalfunds_read_policy_name.name`. Change nothing else. The policy stays UNAPPLIED; the apply
   is RIV-d-2's.
3. Prove it at PLAN time, plan only and never apply:
   - `terraform -chdir=infra/aws/terraform/opal-gateway init -input=false` (if needed), then
     `terraform -chdir=infra/aws/terraform/opal-gateway plan -lock=false -input=false -out=<your deliverables>/w1a.tfplan`
     and `terraform -chdir=infra/aws/terraform/opal-gateway show -json <that plan> > <your deliverables>/w1a.plan.json`.
     Use the `.tools/terraform` shim if one resolves.
   - `python .tools/naming-apply-gate.py --enforce --plan-json <your deliverables>/w1a.plan.json`
   - **AC4:** the gate's line for `aws_iam_role_policy.gw_rivalfunds_read` reads CONFORMANT, with name
     `gateway-rivalfunds-read-policy`, and NO line for that resource reads REFUSE.
   - Report the gate's summary line and every REFUSE line it prints for OTHER resources. Those are other seats'
     facts; record them and do not fix them.
   - Do not commit the `.tfplan`, which can carry secrets; the `.plan.json` is also not committed.
4. Re-run AC1-AC3 literally; they must stay PASS. AC3 reads the policy document, not its name.

## 3. SURFACES AND BOUNDS

You READ (never edit):
- `infra/aws/ec2/opal-gateway/app/sprint_view.py`
- `infra/aws/ec2/opal-gateway/app/server.py`
- `infra/aws/ec2/opal-gateway/app/config.py`
- `infra/aws/ec2/opal-gateway/app/identity.py`
- `infra/aws/ec2/opal-gateway/app/audit.py`
- `infra/aws/terraform/opal-gateway/daily-reports-iam.tf`
- `lib/opal_naming.py`
- `lib/trading_calendar.py`
- `infra/logic/registry/`
- `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/`
- the captured BASG archive, `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\amgt-reconn-daily-census-20260929\basg\` (outside your worktree; read-only).

You WRITE only the `<paths>` below (plus your own `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: `etfs-netassets-daily` or its homes; the
bucket's existing tier-first keys (`bronze/`, `silver/`, `gold/`, `daily/`, `platinum/`); `opal-data-assets`; any Bloomberg or
OpenAI call; any alert, alarm, SNS or monitor; any file another cell of this round owns. Write unit tests at `infra/aws/ec2/opal-gateway/app/tests/test_rivalfunds_view.py`; run them with `python -m pytest` from `infra/aws/ec2/opal-gateway`.

<paths>
infra/aws/terraform/opal-gateway/rivalfunds-iam.tf
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the three routes on the module's handlers (S3 and viewer stubbed): archive, newest, day, 404/400, identity refusal (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/w-1.AC1.py`)
- **AC2** -- live: the module's _list_days() against the real page prefix, and _location() equal to the builder (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/w-1.AC2.py`)
- **AC3** -- IAM simulation of the read policy: page GET/List allowed; bronze GET, PUT, DELETE, other-prefix List denied (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/w-1.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-w-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/w-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-w-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/w-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC3" cell_refs="RIV-w-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/w-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-w-1.gateway-routes-and-read-grant.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-w-1.gateway-routes-and-read-grant`. Report once, with:
- each criterion's verdict line and the output lines above it;
- the files you wrote;
- the exact hookup lines the COO must add at the merge (the `server.py` import, the guard branch clause, the four `Route` lines in the order `/rivalfunds`, `/rivalfunds/`, `/rivalfunds/archive`, `/rivalfunds/{day}`, and any `config.py` entry);
- any row you filed (id and one line).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` v0.2
(@01e5499ae7, L4-R ADMITTED @87321c4243). Decomposition round 1, cell `RIV-w-1`. Checks issuer-written at
`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/`, dry-run at the base before the cut (every one FAILS at the base, as a build or live check must).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<completion_note>2026-09-30 amendment-1 drain by 2.0.0_SA_COO~RV: worker 0.9.0_WK_ETFS_RIVALS~2 @b9447adc2f merged @302cdd9556; AC4 (plan-json naming grade: gw_rivalfunds_read CONFORMANT gateway-rivalfunds-read-policy, 0 REFUSE of 59) from w1a.gate.txt; AC1/AC3 re-run PASS by the issuer. The safe-apply block reported by 2.0.0_SA_COO~MS (27058) is disarmed.</completion_note>
<reopen_note>2026-09-30 ~09:3xZ, 2.0.0_SA_COO~RV: REOPENED for ISSUER AMENDMENT 1 (section 2b) on 2.0.0_SA_COO~MS msg 27058 / row NFRA_MCPMSP-Z-W2-S3: the policy name reaches the plan through ${var.name}, the commit gate cannot see it, and safe-apply's ENFORCE plan limb refuses the addition, which blocks every safe-apply in infra/aws/terraform/opal-gateway.</reopen_note>
<completion_note>2026-09-30 drain by 2.0.0_SA_COO~RV: worker 0.9.0_WK_ETFS_RIVALS~2 @d50b1231ce merged @2274b529ef; AC1-AC3 PASS + 11 unit tests re-run by the issuer; row ETFS_RIVALS-Z-W2-S1 (status flip is the issuer's) answered by this flip; server.py hookups ride the pre-d-2 hookup commit.</completion_note>
<round>1</round>
<slot>~2</slot>
<fabric>site-z</fabric>
