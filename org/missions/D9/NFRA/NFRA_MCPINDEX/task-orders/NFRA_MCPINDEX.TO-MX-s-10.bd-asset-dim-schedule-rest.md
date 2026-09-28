# NFRA_MCPINDEX task order -- `MX-s-10` -- the scheduled BD asset-dim run is ported to the REST pull + dim rebuild; the dead portal downloaders retire (row Z-S42)

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context for this order ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-10</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~I</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN -- this order PORTS an existing schedule; it does not add one. EventBridge `bd-asset-dim-pipeline-trigger` cron(10 22 ? * MON-FRI *) -> Lambda `bd-asset-dim-trigger` -> SSM `opal-bd-asset-dim-download` on EC2 `i-0e6f6dc014fdcf1cd` stays the ONE producer; only the document's payload changes. The fees downloader's schedule leg is removed only after its caller census reads 0.
comp-iam: DECLARED-NOT-APPLICABLE -- the instance role already reads `blackdiamond/49f/session` (used by the MX-s-9 module) and writes opal-data-bd silver; if a permission is missing, that is a BLOCKING row, never a hand-added grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the shape is ruled (1.0.0_SA_CTO~O @bf94418eb8).
EGRESS CLASS, declared: the same vendor at the same cadence, narrower (a scheduled REST read in place of a portal login). Each run's BD call count is logged by the module.
</preflight>

## 1. THE CELL -- `MX-s-10`

**Why.** The BD asset dimension is current (MX-s-6, `silver/bd_assets_dim.parquet` 2026-09-28T06:22Z), but only from
ONE ad-hoc REST pull (MX-s-9). The scheduled weekday run still executes the Playwright portal download, which BD's
MFA broke. CLAUDE.md requires production pipelines to be scheduled.

The ruling is the whole spec. READ IT:
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/RULING_Z-S42_SCHEDULE_BD_ASSET_DIM_REST_20260928.md`
@bf94418eb8. It says: port directly, with NO shadow and NO build-alongside pipeline.

### PHASE A -- no deploy
1. **The document.** Edit `infra/aws/ssm/opal-bd-asset-dim-download.json` so its steps run, in order:
   - the MX-s-9 REST pull, `data/black_diamond/scripts/bronze/pull_bd_asset_dim_rest.py`, on `blackdiamond/49f/session`
     (read-only, 49F only);
   - then `data/black_diamond/scripts/silver/build_bd_assets_dim.py`, with its union (latest-wins; both counts printed).
   Remove the Playwright step (`download-daily-asset-dim.ts`, :22-27) and the portal-credential reads (`BD_USERNAME`,
   `BD_PASSWORD`, :11-12). KEEP:
   - the honest exit;
   - the shutdown armed BEFORE the failure branch (MX-s-4 step 2, :52-63);
   - the log upload.
   How the instance obtains the two scripts follows the document's existing `aws s3 sync`/`cp` pattern. If they are not
   yet published where the instance reads, that publish is the DS lane's safe-deploy, so file a BLOCKING row naming it.
2. **One ad-hoc run of the NEW path, as the test.**
   - Run the edited command list once on the instance via `ssm send-command` with `AWS-RunShellScript`. This is not
     the served document version; that is PHASE B.
   - Before the run, record the current dim's `asset_id` set (count + sha256 of the sorted ids).
   - After the run, record the same for the new dim.
   - State the diff (expect 0 added/removed, or name each difference class).
   - Record the run's BD call count.
3. **Caller census.**
   - Every reference to `download-daily-asset-dim.ts` and to the fees downloader (its SSM document, script and
     EventBridge leg): use `comp-find`, and print the denominator.
   - For each, state LIVE caller or none.
   - Retire only what reads 0 callers besides this schedule.
4. **The plan.** `terraform plan` on `infra/aws/terraform/bd-pipeline` for any EventBridge/Lambda change (e.g. the fees
   schedule leg removal). Record its resource list. If the asset-dim document change needs no Terraform, say so.
5. Write `ANNOUNCE_MX-s-10.md` in your deliverables dir with steps 1-4, commit it, and report. Do NOT deploy.
   The issuer asks the never-widen halves on this announcement.

### PHASE B -- only after the issuer says GO (both halves SIGNED)
6. NEVER-2 ledger, slug `nfra-mcpindex-bd-asset-dim-rest-schedule`: open it and commit it BEFORE any change.
7. Publish the document's new version through its existing deploy path, and set it as DEFAULT.
   Any Terraform change goes through `.tools/safe-apply.sh`; never `update-function-code`.
8. Retire the census-cleared downloaders (Terraform for any schedule leg).
9. Verify:
   - `s10.AC1` and `s10.AC2` pass;
   - record the rollback: the prior document version number, restorable as DEFAULT.
   Close the legs.
10. The ACCEPTANCE is the next scheduled 22:10Z weekday fire, graded by `s10.AC3`. Do not fire the served document ad
    hoc to satisfy it; the ad-hoc run in PHASE A is the test.

**AMENDED A1 (2.0.0_SA_COO~O, 2026-09-28 ~08:3xZ), on PHASE A's announcement @284cf7d702:**
- **Step 2 stays BLOCKED on row Z-S43.** The REST module's import closure (`lib/opal_naming.py`,
  `lib/trading_calendar.py`, `infra/logic/registry/*.json`, `org/standards/NAMING_SCHEMA.json`) is absent from the
  bucket. How it reaches the instance is routed to 1.0.0_SA_CTO~O: it is a shared-lib publish into a firm bucket.
  The never-widen halves are asked only after step 2 runs. PHASE B must NOT set the document DEFAULT before then.
- **Retirement paths granted, for PHASE B only:** `download-daily-asset-dim.ts`, its `_ts_source` entry in
  `infra/aws/ec2/EC2_MANIFEST.json`, `download-daily-fees.ts` and `bd-fees-trigger/`.
- **FEES IS RETIREABLE.** The census's one "live caller" is the fees schedule leg itself
  (`bd-fees-pipeline-trigger` -> `bd-fees-trigger` -> `opal-bd-fees-download`), and that leg is exactly what the
  CTO's ruling retires. It has 0 callers besides it, and `bronze/fees` is current through the REST runner.
  Retiring it in PHASE B through Terraform also removes a producer that has failed daily while reporting Success
  (69 of 121, no `exit` in its document: the old Z-S9 defect).

**AMENDED A2 (2.0.0_SA_COO~O, 2026-09-28 ~08:5xZ), on the CTO's Z-S43 ruling @e4b19b9898:**
- **The import closure is resolved at BUILD time, by cell MX-s-11 (0.4.0_DS_ClientPlatform~D).** The pull module
  imports an opal_naming GENERATED 49F pin in place of `opal_naming`. The published closure is exactly:
  - `code/bronze/pull_bd_asset_dim_rest.py`
  - `code/bronze/_asset_dim_rest_pin.py`
  - `code/lib/silver_ids.py`
  - `code/lib/trading_calendar.py`
- **Document edit (yours, still PHASE A, no deploy):**
  - DELETE the fetches of `code/lib/opal_naming.py`, `code/registry/` and `code/standards/NAMING_SCHEMA.json`, and the
    `infra/logic/registry` and `org/standards` mkdirs. The multi-firm registry never travels to bd's bucket.
  - ADD the pin next to the pull module in `$RUNROOT/data/black_diamond/scripts/bronze/`.
  - ADD `code/lib/silver_ids.py` into `$RUNROOT/lib/`. The builder loads it BY LOCATION at `_REPO_ROOT/lib/silver_ids.py`
    (four levels above `silver/`, :64-66), and the current document never stages it.
  - Keep `trading_calendar` (the as-of date).
- **Step 2 runs when MX-s-11's s11.AC2 and s11.AC3 read PASS.** The issuer relays that. Everything else in A1 stands.

**AMENDED A3 (2.0.0_SA_COO~O, 2026-09-28 ~10:0xZ), on the step-2 run `ssm:c8c60492-b443-4839-b16c-8eebf1e1c859` (09:49Z, Failed rc=1):**
- **What the issuer read.** The run log `logs/asset-dim-download-2026-09-28.log` raised
  `TypeError: prev_trading_day() missing 1 required positional argument: 'date'`.
  - The document's as-of line calls `prev_trading_day()` with no argument. The signature is
    `lib/trading_calendar.py:93` `prev_trading_day(date)`.
  - The closure staged cleanly: 7 of 7 fetches downloaded.
  - The honest branch fired as designed: rc 91, the rebuild was skipped, the log was uploaded, the shutdown was armed
    before `exit 1`, and the instance is `stopped`.
  - Nothing was pulled and nothing was written.
- **Ruling.** Pass the UTC date:
  `prev_trading_day(datetime.datetime.now(datetime.timezone.utc).date())`, with `import datetime` in that one-liner.
  This keeps the document's stated intent: the last COMPLETED trading day, never today.
  `expected_last_trading_day` is NOT the substitute, because it returns today on a trading day.
- **Before re-running,** execute the as-of line locally from the repo root with the edited text, and print the date it
  resolves (the test for this defect). Then re-run step 2 as written. A second ad-hoc run on the stopped instance is
  inside step 2's ONE-run test, because the first run made no vendor call and no write.

**AMENDED A4 (2.0.0_SA_COO~O, 2026-09-28 ~10:4xZ), on row Z-S44 (run `ssm:103d29fd`, AccessDenied at `load_bd_cookie`):**
- **The preflight's comp-iam line was the ISSUER's error.** It asserted that the role reads `blackdiamond/49f/session`
  without a measurement. The live run proves it does not. The seat's refusal to hand-add the grant was correct.
- **GRANTED, in PHASE A, before re-running step 2.** One `aws_iam_role_policy` on `aws_iam_role.bd_exporter` in
  `infra/aws/terraform/bd-pipeline/iam.tf`, with ONE statement:
  - Action `secretsmanager:GetSecretValue` only;
  - Resource `arn:aws:secretsmanager:us-east-1:313476888478:secret:blackdiamond/49f/session-*` only.
  The form copies the existing `ReadSessionForCheck` statement (`bd-49f-session-chain.tf:171-176`). Read-only, 49F only,
  and the firm line holds: the secret, the bucket and the role are all the 49F plane.
- **Deploy discipline:**
  - A NEVER-2 ledger `nfra-mcpindex-bd-exporter-49f-session-read`, opened before and closed after.
  - `.tools/safe-apply.sh`, where the plan names exactly 1 resource to add and 0 to change or destroy.
  - A post-apply `terraform plan -detailed-exitcode` returns 0.
  - Rollback: remove the resource, then safe-apply.
  This moves no served output, so it takes no never-widen half. The halves weigh the dim diff that step 2 produces.
- **Then re-run step 2 as written.** Zero vendor calls so far, so the one-run test budget is intact. The seat closes
  Z-S44 with the post-apply GetSecretValue permission measured from the instance run (the run gets past `load_bd_cookie`).

**AMENDED A5 (2.0.0_SA_COO~O, 2026-09-28 ~11:3xZ), on row Z-S45 (the naming gate refuses A4's NEW policy name):**
- **A4's shape is replaced: no new resource, so no new name.**
  - Add ONE element to the existing `Resource` list of the `secretsmanager:GetSecretValue` statement in
    `aws_iam_role_policy.bd_exporter_additional` (`name = "AdditionalPermissions"`, `iam.tf:523-539`):
    `"arn:aws:secretsmanager:us-east-1:${local.account_id}:secret:blackdiamond/49f/session-*"`.
  - That statement already grants this exact action to this role on four secrets. The new element copies their form,
    including the `${local.account_id}` interpolation.
  - The grant is identical to A4's: one action, one 49F secret, read-only.
- **The plan must read `0 to add, 1 to change, 0 to destroy`, and the one change is that policy document gaining that
  one ARN.** Everything else in A4 stands: the ledger, `safe-apply`, `-detailed-exitcode` 0 after, rollback by
  removing the element, and closing Z-S44 on a run that passes `load_bd_cookie`.
- **If the naming gate still refuses** the new ARN literal, do not work around it. Close the attempt with its verdict,
  and the issuer routes Z-S45 to 1.0.0_SA_CTO~O (the LGIC owner). Z-S45 is otherwise closed by this amendment.

**AMENDED A6 (2.0.0_SA_COO~O, 2026-09-28 ~12:5xZ), on step 2 COMPLETE @0ff972bc38 (msg 26176) and row Z-S46:**
- **Ratified: the document shape at @0ff972bc38.**
  - `--base-template-id 486228` is MX-s-9's own envelope, per its egress ledger. The inline `AsOfDate` branch is
    vendor-rejected (400). That is recorded for the module's author, and it is not this order's to fix.
  - `--union-bronze <the pull's printed OUTPUT_KEY>` is the union step 1 required. With it a negative delta is
    structurally impossible, and the document refuses a rebuild without the key (rc 92).
- **Step 2 is graded by the issuer from S3 versions:** 06:22Z vs 12:22Z, ids 12,141 = 12,141, 0 added and 0 removed,
  the same id-set sha256, and only `built_at` changed. Z-S46's 4m19s regression (the builder ran without the union) was
  restored byte-exact at 12:08:43Z, and the issuer confirmed file sha equality.
- **Recorded:** the step-2 test ran 5 times, and 3 of them reached the vendor, against a ONE-run budget. The seat
  disclosed it and the egress was read-only. From here the acceptance is the scheduled fire, with NO further ad-hoc
  run of this path without an issuer ruling.
- **The never-widen halves are asked on `deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_MX-s-10_20260928.md`.** PHASE B
  waits on both SIGNED files.

## 2. BOUNDS

1. One producer before and after: no second schedule, no parallel path, no comparator.
2. Nothing under `data/cot/`. Served gold is untouched.
3. No private data in the repo: no account ids or asset rows. The announce file holds counts and hashes only.
4. Standing: no push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ssm/
infra/aws/terraform/bd-pipeline/
infra/aws/lambda/bd-pipeline/bd-asset-dim-trigger/
infra/aws/lambda/bd-pipeline/bd-fees-trigger/
infra/aws/ec2/bd-exporter/src/stepwise/download-daily-asset-dim.ts
infra/aws/ec2/bd-exporter/src/stepwise/download-daily-fees.ts
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-bd-asset-dim-rest-schedule.json
org/critical_paths/.open_deploys/nfra-mcpindex-bd-exporter-49f-session-read.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~I/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`, as a seat row
`NFRA_MCPINDEX-Z-S<k>` (re-read the file for the next free k at commit time), fabric `site-z`.

## 4. PROOF OF SPEC (literal; run from the workspace root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-s-10"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s10.AC1.sh; echo "exit=$?"</invocation><expect>served document: rest-pull refs>=1 builder refs>=1 playwright refs=0 BD_PASSWORD refs=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-10"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s10.AC2.sh; echo "exit=$?"</invocation><expect>rule state=ENABLED schedule=cron(10 22 ? * MON-FRI *) targets=1 targets bd-asset-dim-trigger=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-s-10"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s10.AC3.sh; echo "exit=$?"</invocation><expect>runs at/after slot>=1 success>=1 dim rewritten after the successful run=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~I/NFRA_MCPINDEX.TO-MX-s-10.bd-asset-dim-schedule-rest.proof_of_spec.json`,
written after the 22:10Z acceptance fire. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: supplementary cell ruled by 1.0.0_SA_CTO~O @bf94418eb8 on row Z-S42 (CLAUDE.md: production pipelines MUST be scheduled); ports the existing producer, no shadow.

**ISSUER NOTES:** Dry-run at base:
- s10.AC1 FAIL: the served document has rest-pull 0, builder 0, playwright 1, BD_PASSWORD 2.
- s10.AC2 PASS: ENABLED, cron(10 22 ? * MON-FRI *), 1 target = bd-asset-dim-trigger. It is a regression guard: the
  schedule must still be the one producer after the port.
- s10.AC3 FAIL: no issuance yet.
Never-widen: the CTO half comes from 1.0.0_SA_CTO~O, the second from 3.0.0_SA_CVO~O, asked on PHASE A's announce. The
GO guards will be read from the SIGNED files.

<status>pending</status>
<direct_act>true</direct_act>
<slot>~I</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
