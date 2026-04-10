# 0.6.0_AE Log: bd-fees Standalone Download + Silver Pipeline (bd-v2.23.0)
**Date:** 2026-04-10
**Agent:** 0.6.0_AE_PartnerETL
**Tag:** bd-v2.23.0
**Project code (informal):** ADVI_FEEAUTO
**Predecessor:** bd-v2.22.0 (ADVI_GLDRST.022 Phase 1+2 shipped earlier today — `advi_gldrst_022_phase1_canonical_prices_daily_eventbridge.md`)

## Context

Andrew requested: "make sure we have one of the bd-pipeline runners be set up to get the BD fees files -- template `Fees_OpalCapital_Daily`, same typescript pattern as bd-allocations."

DD (provided by Andrew) confirmed the landscape:
- `data/black_diamond/scripts/silver/convert_fees_to_silver.py` exists (authored by 0.6.0_AE on 2026-04-06 during ADVI_GLDOPS), deployed to `s3://opal-data-bd/code/silver/`.
- `s3://opal-data-bd/bronze/fees/` has 16 historical xlsx files — ALL uploaded manually by Andrew from his Downloads.
- `s3://opal-data-bd/silver/fees/` has 1,820+ partitions — each written when DS or Andrew manually ran the converter locally.
- Nothing in `infra/aws/terraform/bd-pipeline/`, `infra/aws/lambda/bd-pipeline/`, or `infra/aws/ec2/bd-gold-layer-runner/` referenced the fees converter. No EventBridge, no S3 trigger, no SSM. Orphaned.

Andrew's preference: **dedicated EC2 instance**, copy the bd-allocations design bit-for-bit, so a fees failure cannot affect the allocation -> price-update -> gold chain.

Schedule: Mon-Fri 22:15 UTC (6:15 PM ET) — 15 min after the allocation wave (22:00 UTC) and 45 min before the gold nightly fallback (23:00 UTC).

## Work Done

### New resources (additive; no existing resource was modified except two IAM list appends)

| Resource | Type | Location |
|---|---|---|
| `aws_instance.bd_fees` | EC2 t3.medium, AL2023 | `infra/aws/terraform/bd-pipeline/ec2.tf` |
| `module "fees_trigger"` (bd-fees-trigger Lambda) | Python 3.11, 128 MB, 600 s | `infra/aws/terraform/bd-pipeline/lambdas.tf` |
| `aws_cloudwatch_event_rule.bd_fees_pipeline` | `cron(15 22 ? * MON-FRI *)` | `infra/aws/terraform/bd-pipeline/eventbridge.tf` |
| `bd-fees-trigger/lambda_function.py` | Lambda source | `infra/aws/lambda/bd-pipeline/bd-fees-trigger/` |
| `download-daily-fees.ts` | Playwright TS exporter | `infra/aws/ec2/bd-exporter/src/stepwise/` |
| `opal-bd-fees-download.json` | SSM document | `infra/aws/ssm/` |

Cloned bit-for-bit from bd-allocations, template name swapped to `Fees_OpalCapital_Daily`, default `S3_PREFIX=bronze/fees`, bd-price-update invocation dropped (fees does not feed the price chain).

### IAM additions (append-only to existing policy)

`bd-daily-trigger-lambda-role/bd-daily-trigger-policy`:
- `StartStopBDInstances.Resource[]` — added `aws_instance.bd_fees.arn`
- `SendSSMCommandsToBD.Resource[]` — added `aws_instance.bd_fees.arn` and `document/opal-bd-fees-download`

No other policy changes.

### uploader_user_data.sh hardening (incidental, discovered during verification)

Three pre-existing bugs in `infra/aws/ec2/bd-exporter/terraform/scripts/uploader_user_data.sh` were discovered because this was the first time anyone had provisioned a fresh uploader in some time — every existing uploader instance had been hand-patched via SSM. Fixed all three so the next provisioning runs clean:

1. **cloud-init HOME unbound.** Bun installer references `$HOME` under `set -u`; cloud-init runs user_data with empty env. Now exports `HOME=/root` at the top.
2. **Missing Playwright OS deps.** `bunx playwright install-deps` tries to invoke `node`, which isn't installed (only bun). Chromium crashes with `libatk-1.0.so.0: cannot open shared object file`. Now installs the full RHEL-family chromium dep set (`nss nspr atk at-spi2-atk cups-libs libdrm libgbm libxkbcommon libXcomposite libXdamage libXext libXfixes libXrandr libxcb alsa-lib pango cairo`) via dnf.
3. **Missing Python silver-conversion deps.** `convert_fees_to_silver.py` needs `boto3 pandas pyarrow openpyxl`. AL2023 ships python3 but not pip, and these libs were never installed. Also, `/usr/bin/aws` is a Python script with `#!/usr/bin/python3 -s` which skips user site — meaning ANY pip install to user site doesn't fix the system awscli. Now installs `python3-pip` via dnf, then installs the libs via `pip install --target=/usr/lib/python3.9/site-packages/` so both awscli and the silver scripts can import them.

These bugs meant the OTHER bd-exporter uploaders (bd-allocations, bd-transactions) were historically set up by hand. The fix is a belt-and-suspenders for future provisioning — existing instances are unaffected.

### download-daily-fees.ts filename fix (corrected mid-verification)

First draft of the TS used `download.suggestedFilename()` directly, which BD returns as the bare `Fees_OpalCapital_Daily.xlsx` with no dates. That would have overwritten the same S3 key every day.

Andrew pointed out: "note how they get that filename, the other scripts check the metadata page of the xlsx". Adapted the `extractAsOfDate.ts` pattern (from `download-daily-allocation.ts`) to read **both** `Start Date` and `End Date` from Sheet 2 of the BD xlsx and rename the file to `Fees_OpalCapital_Daily_{start}_to_{end}.xlsx`, matching Andrew's existing manual upload convention in `s3://opal-data-bd/bronze/fees/`.

Today's run extracted `Start Date=2026-04-09, End Date=2026-04-09` — BD's Fees template returned a single-day range. The historical files with wider ranges (e.g. `2025-06-20_to_2026-04-09`) were from one-time backfill exports.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read bd-allocation-trigger Lambda + opal-bd-allocation-download SSM doc + eventbridge.tf + iam.tf | Template identified |
| 2 | Write bd-fees-trigger lambda_function.py (clone of allocation-trigger) | New source file |
| 3 | Write download-daily-fees.ts (clone of allocation, swap template + prefix) | New TS file (first draft, later corrected for filename) |
| 4 | Write opal-bd-fees-download.json SSM document | Clone of allocation SSM doc, fees-specific steps, no bd-price-update invoke |
| 5 | Edit ec2.tf — add `aws_instance.bd_fees` (t3.medium, AL2023, bd-exporter-profile, user_data from uploader script, ignore_changes lifecycle) | +30 lines |
| 6 | Edit lambdas.tf — add `module "fees_trigger"` | +14 lines |
| 7 | Edit eventbridge.tf — add rule + target + permission (Mon-Fri 22:15 UTC) | +28 lines |
| 8 | Edit iam.tf — append bd_fees instance ARN to StartStopBDInstances + SendSSMCommandsToBD; append opal-bd-fees-download doc ARN | +3 lines |
| 9 | Update EC2_MANIFEST.json — new bd-fees entry | +20 lines |
| 10 | Update lambda-source-map.json — new bd-fees-trigger entry | +8 lines |
| 11 | git commit source + TF + manifests | `1bc64829` feat(bd-pipeline): bd-fees standalone download + silver pipeline |
| 12 | build-and-upload.sh bd-pipeline bd-fees-trigger | `s3://opal-313476888478-lambda-artifacts/bd-pipeline/bd-fees-trigger.zip` SHA256 `++HfmcFBYKVSbg0WMgWThDMOXTx/iJwl4RTuB93FEeQ=` |
| 13 | git commit updated source map | `e11c137e` ci: upload bd-fees-trigger artifact [skip ci] |
| 14 | terraform init (new fees_trigger module) | OK |
| 15 | terraform plan | `Plan: 6 to add, 1 to change, 0 to destroy` |
| 16 | terraform apply | `6 added, 1 changed, 0 destroyed` — instance `i-0868fc7e7ebec26f2` created |
| 17 | terraform plan (0-diff check) | `No changes. Your infrastructure matches the configuration.` |
| 18 | Register SSM doc via `aws ssm create-document opal-bd-fees-download` | DocumentVersion 1 created |
| 19 | Upload download-daily-fees.ts to `s3://opal-data-bd/scripts/src/stepwise/` | Uploaded |
| 20 | (Verification loop 1-6, see next section) | Converged after fixing uploader_user_data.sh bugs + TS filename bug |
| 21 | Edit uploader_user_data.sh — HOME fix, Playwright OS deps, Python libs, chromium cache copy to ec2-user | Belt-and-suspenders for future provisioning |
| 22 | Edit download-daily-fees.ts — extract Start/End Date from Sheet 2, rename file | Matches manual upload convention |
| 23 | Edit EC2_MANIFEST.json — fill `instance_id` for bd-fees | `i-0868fc7e7ebec26f2` |
| 24 | Update pipeline_inventory.xml — bd-v2.23.0, new EC2 service, new Lambda, new rule | Core doc in sync |
| 25 | git commit fixes + core doc | `0ad1ed0a` fix(bd-pipeline): bd-fees verification fixes + harden uploader_user_data |
| 26 | record-terraform-deploy.sh bd-pipeline --version bd-pipeline-v2.23.0 | CHANGELOG.json entry + auto-commit |
| 27 | Auto-commit from record-deploy | `eb6145ef` ci: record deploy bd-pipeline @ 0ad1ed0a [skip ci] |
| 28 | terraform plan (final 0-diff) | `No changes. Your infrastructure matches the configuration.` |
| 29 | git tag -a bd-v2.23.0 -m "..." | Annotated tag created |
| 30 | git push origin CLOUD --follow-tags | 4 commits + 1 tag pushed |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| BD | bd-v2.23.0 | `eb6145ef` (record-deploy), `0ad1ed0a` (fix+core doc), `e11c137e` (artifact), `1bc64829` (feat) |

### Related commits (full list for this ship)

| Commit | Subject |
|---|---|
| `1bc64829` | `feat(bd-pipeline): bd-fees standalone download + silver pipeline (ADVI_FEEAUTO)` — source files, Terraform, manifests |
| `e11c137e` | `ci: upload bd-fees-trigger artifact [skip ci]` — build-and-upload.sh output |
| `0ad1ed0a` | `fix(bd-pipeline): bd-fees verification fixes + harden uploader_user_data` — three user_data bugs + TS metadata filename + EC2 manifest instance_id + pipeline_inventory.xml |
| `eb6145ef` | `ci: record deploy bd-pipeline @ 0ad1ed0a [skip ci]` — CHANGELOG.json + source map |

## Verification

### Verification loop (6 manual Lambda invocations)

| # | Command ID | Status | Failure / Fix |
|---|---|---|---|
| 1 | (not invoked; bootstrap probe) | — | user_data bootstrap failed: `cloud-init status: error`, `HOME: unbound variable`. Root cause: bun install expected $HOME. Manually bootstrapped via SSM (dnf install xvfb, bun for root, playwright chromium, `/opt/bd-exporter/` package.json). |
| 2 | `b9b9d705-8737-49dd-b689-30eb165bd87d` | Success (no-op) | `bash line 140: /home/ec2-user/.bun/bin/bun: No such file or directory`. Root cause: bun only installed for root, SSM runuser's to ec2-user. Fix: `su - ec2-user -c 'curl -fsSL https://bun.sh/install \| bash'`. |
| 3 | `f4261c3a-5a42-4f57-9a08-8434adb2e90c` | Success (no-op) | `error: launch: Executable doesn't exist at /home/ec2-user/.cache/ms-playwright/chromium_headless_shell-1217/...`. Root cause: playwright chromium cache was under /root, SSM runs as ec2-user. Fix: `cp -a /root/.cache/ms-playwright /home/ec2-user/.cache/ms-playwright`. |
| 4 | `18a51331-7343-4189-bbce-f0eed7e8c345` | Success (no-op) | `libatk-1.0.so.0: cannot open shared object file`. Root cause: Playwright OS deps never installed (bunx install-deps needs node). Fix: `dnf install -y nss nspr atk at-spi2-atk cups-libs libdrm libgbm libxkbcommon libXcomposite libXdamage libXext libXfixes libXrandr libxcb alsa-lib pango cairo`. Phase 1-5 ran but downloaded filename was `Fees_OpalCapital_Daily.xlsx` (no date). |
| 5 | `00a3f130-f278-4c9e-907b-80b39464b97c` | Failed | `ModuleNotFoundError: No module named 'dateutil'` — awscli itself broken. Root cause: my earlier `pip install boto3 pandas pyarrow openpyxl` upgraded python-dateutil which broke the system awscli (which uses `python3 -s` and only sees system site-packages). Fix: `dnf install python3-pip`, `pip install --target=/usr/lib/python3.9/site-packages/ python-dateutil<=2.9.0 boto3 pandas pyarrow openpyxl`. Also updated TS to read Sheet 2 Start/End Date metadata. |
| 6 | `38328835-7a29-45ae-9154-28c757d26ed6` | **Success** | Full end-to-end pass. See next block. |

### Run 6 (successful) — stdout highlights

```
Phase 1: Login                                     OK: Login successful
Phase 2: Navigate to Fees Template                 OK: Build Query page loaded
Phase 3: Run Query                                 OK: Query complete (15s)
Phase 4: Download                                  OK: Downloaded temp (157 KB)
                                                   OK: Start Date=2026-04-09  End Date=2026-04-09
                                                   OK: Renamed to Fees_OpalCapital_Daily_2026-04-09_to_2026-04-09.xlsx
Phase 5: Upload to S3                              OK: Uploaded to s3://opal-data-bd/bronze/fees/Fees_OpalCapital_Daily_2026-04-09_to_2026-04-09.xlsx

Running fees silver conversion...
  Loading: s3://opal-data-bd/bronze/fees/Fees_OpalCapital_Daily_2026-04-09_to_2026-04-09.xlsx
  Raw rows: 1,072, columns: 34
  Skipped 5 dates (already exist)
DONE: 0 silver partitions written     <-- correct idempotent behavior

Done. Shutting down in 2 minutes...
```

The 0 new partitions is **correct**: DS's earlier manual run (documented in `docs/briefs/data-scientist-2026-04-10-pricing-cleanup-session.md:44`) already added 2026-04-03 through 2026-04-09 to silver/fees/ this morning. The Fees template from BD returned today's single-day range (2026-04-09 only), and convert_fees_to_silver.py correctly skipped it as already present.

### S3 artifact verification

```
$ aws s3 ls s3://opal-data-bd/bronze/fees/ | grep 2026-04-09_to_2026-04-09
2026-04-10 17:28:23     160421 Fees_OpalCapital_Daily_2026-04-09_to_2026-04-09.xlsx

$ aws s3 ls s3://opal-data-bd/silver/fees/ | tail -5
2026-04-10 16:32:36      21739 2026-04-05.parquet
2026-04-10 16:32:36    1032020 2026-04-06.parquet
2026-04-10 16:32:37     990954 2026-04-07.parquet
2026-04-10 16:32:39     105194 2026-04-08.parquet
2026-04-10 16:32:39      83556 2026-04-09.parquet

$ aws s3 ls s3://opal-data-bd/logs/fees-download-2026-04-10.log
2026-04-10 17:28:26       3059 fees-download-2026-04-10.log
```

Andrew's pre-existing 52 MB historical file (`Fees_OpalCapital_Daily_2025-06-20_to_2026-04-09.xlsx`) is unchanged.

### Terraform state verification

```
$ terraform state show aws_instance.bd_fees
    id              = "i-0868fc7e7ebec26f2"
    instance_state  = "running"
    private_ip      = "172.31.13.142"
    public_ip       = "44.203.42.248"

$ terraform plan    # final check
No changes. Your infrastructure matches the configuration.
```

### Live AWS verification

```
$ aws events describe-rule --name bd-fees-pipeline-trigger --query '[Name,State,ScheduleExpression]' --output text
bd-fees-pipeline-trigger   ENABLED   cron(15 22 ? * MON-FRI *)

$ aws events list-targets-by-rule --rule bd-fees-pipeline-trigger --query 'Targets[0].[Id,Arn]' --output text
1   arn:aws:lambda:us-east-1:313476888478:function:bd-fees-trigger

$ aws lambda get-function --function-name bd-fees-trigger --query 'Configuration.[State,Environment.Variables]' --output text
Active   {'EC2_INSTANCE_ID': 'i-0868fc7e7ebec26f2'}

$ aws ssm describe-document --name opal-bd-fees-download --query '[Name,Status,DocumentVersion]' --output text
opal-bd-fees-download   Active   1

$ aws ec2 describe-instances --instance-ids i-0868fc7e7ebec26f2 --query 'Reservations[0].Instances[0].State.Name' --output text
stopped    # auto-shutdown after run 6 completed — expected
```

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| 1 (before writing) | comp-blast | `comp-blast bd-allocation-trigger` | No edges surfaced — known graph gap: compiler does not index EventBridge -> Lambda, Lambda -> EC2 SSM, or SSM document invocations. Same gap flagged in the bd-v2.22.0 log this morning. |
| 1 (before writing) | comp-trace | `comp-trace bd-allocations --direction both` | Same gap. Verification fell back to direct file reads of lambdas.tf / eventbridge.tf / iam.tf / ec2.tf + SSM document JSON files + `aws ssm list-documents`. |
| 2 (before commit) | terraform plan | `terraform plan` | `Plan: 6 to add, 1 to change, 0 to destroy` — all adds match the intended 6 resources + 1 IAM list append |
| 2 (before commit) | terraform plan (post-apply) | `terraform plan` | `No changes. Your infrastructure matches the configuration.` — 0-diff confirmed |
| 3 (after commit) | aws events describe-rule + list-targets-by-rule | see Live AWS verification | Rule + target + schedule live |
| 3 (after commit) | aws lambda get-function | see Live AWS verification | Lambda deployed with correct env var |
| 3 (after commit) | aws ssm describe-document | see Live AWS verification | SSM doc Active, version 1 |
| 3 (after commit) | Manual Lambda invoke #6 | `aws lambda invoke --function-name bd-fees-trigger` | End-to-end pass: login -> query -> download -> metadata extract -> rename -> S3 upload -> silver convert -> log upload -> shutdown |

**Compiler gap logged** (same gap flagged in this morning's bd-v2.22.0 log): the dependency graph does not index EventBridge rule -> Lambda target edges, Lambda -> EC2 SSM send_command / start_instances edges, or SSM document -> S3 sync relationships. This made comp-blast and comp-trace useless for this change. For pipeline-infra work that touches EC2 + SSM + EventBridge, verification must use direct file reads + `aws events describe-rule` + `aws ec2 describe-instances` + terraform plan 0-diff.

**compiler-tools-log.md append deferred:** the file has uncommitted DT (0.4.0_DT_ClientPlatform) entries from ADVI_PROFIL.001 / .002 work earlier today that aren't mine to bundle into an AE-authored commit. The bd-v2.23.0 entry for this ship should be appended in the next org-tidy / cross-pod commit pass, formatted as: `2026-04-10 | 0.6.0_AE_PartnerETL | bd-fees standalone ship | comp-blast/comp-trace (known graph gaps: EventBridge->Lambda, Lambda->EC2 SSM, Lambda->Lambda invoke — no edges surfaced) | fallback: file reads + terraform plan 0-diff + aws events/lambda/ssm describe + manual Lambda invoke end-to-end | bd-v2.23.0`.

## Current State

| Component | State |
|---|---|
| `aws_instance.bd_fees` | `i-0868fc7e7ebec26f2` (t3.medium, AL2023), stopped. Auto-started by bd-fees-trigger Lambda on schedule. |
| `bd-fees-trigger` Lambda | Deployed, env `EC2_INSTANCE_ID=i-0868fc7e7ebec26f2`, role `bd-daily-trigger-lambda-role`. |
| `opal-bd-fees-download` SSM document | Version 1, Active. Registered via `aws ssm create-document` (not managed by Terraform — matches the existing pattern for opal-bd-allocation-download et al.). |
| `bd-fees-pipeline-trigger` EventBridge rule | ENABLED, `cron(15 22 ? * MON-FRI *)`. First production fire: 2026-04-13 22:15 UTC. |
| `download-daily-fees.ts` | In repo + `s3://opal-data-bd/scripts/src/stepwise/`. SSM doc syncs it on each run. |
| IAM `bd-daily-trigger-policy` | Updated in-place, bd_fees ARN + opal-bd-fees-download ARN appended. |
| `/opt/bd-exporter/` on bd-fees EC2 | Bootstrapped: bun (root + ec2-user), playwright chromium + cache (root + ec2-user), xvfb, Playwright OS deps, python3-pip, boto3/pandas/pyarrow/openpyxl in system site-packages, python-dateutil. |
| `uploader_user_data.sh` | Hardened with the three fixes above. Next fresh provisioning of any bd-exporter instance should come up clean without manual SSM patching. |
| `pipeline_inventory.xml` | Updated to bd-v2.23.0 with bd-fees service, Lambda, rule. |
| `bd-v2.23.0` tag | Pushed to origin with `--follow-tags`. |
| `lambda-source-map.json` | bd-fees-trigger entry with `artifact_s3_key` and `artifact_sha256` populated by build-and-upload.sh, `last_deployed_commit` updated by record-terraform-deploy.sh. |

## Next Steps

- **[0.6.0_AE_PartnerETL] Monday 2026-04-13 22:15 UTC** — First unattended production run. Watch `bd-fees-trigger` CloudWatch logs and the run log at `s3://opal-data-bd/logs/fees-download-2026-04-13.log`. Expected behavior: instance starts, Playwright downloads `Fees_OpalCapital_Daily_2026-04-10_to_2026-04-13.xlsx` (Fri through Mon range), uploads to bronze, silver converter picks it up and writes 4 new partitions (2026-04-10, 11, 12, 13), instance auto-shuts down.
- **[0.6.0_AE_PartnerETL]** After Monday's first prod run, verify silver/fees/ gained 4 new partitions and no manual intervention was required.
- **[0.6.0_AE_PartnerETL]** If Monday's run confirms the hardened uploader_user_data.sh works for net-new provisioning, the existing bd-allocations and bd-transactions instances could eventually be reprovisioned to eliminate their hand-patched state. Not urgent; both are stable. Low-priority cleanup backlog item.
- **[Andrew]** You can stop manually downloading the Fees_OpalCapital_Daily xlsx from BD's portal and uploading to bronze/fees/. The dedicated runner handles it Mon-Fri now. Ad-hoc manual uploads still work — they just land alongside the automated daily uploads.
- **[follow-up, not assigned]** The ADVI_GLDRST.022 Phase 1 canonical-prices-daily run fires tonight at 22:00 UTC (~30 min from this log's timestamp). This bd-fees ship is on a different EC2 and different schedule (22:15 UTC Mon-Fri) and does NOT interact with gold/price data. No collision risk.
- **[follow-up, not assigned]** Compiler graph gaps (EventBridge -> Lambda, Lambda -> EC2 SSM, Lambda -> Lambda invoke) remain. Documented in this log and in the bd-v2.22.0 log. Small PR to `org/modules/graph/` would unlock comp-blast / comp-trace for pipeline infra changes.

## Notes

- **Scope discipline:** the three uploader_user_data.sh bugs are load-bearing fixes for the NEW bd-fees provisioning but they also touch shared infrastructure used by bd-allocations and bd-transactions. I did NOT reprovision those existing instances — they continue to run on their hand-patched state. The uploader_user_data.sh fix only affects FUTURE provisioning (if any).
- **Filename convention alignment:** the TS now matches Andrew's existing manual upload convention (`Fees_OpalCapital_Daily_{start}_to_{end}.xlsx`) by reading both Start Date and End Date from Sheet 2 metadata. This matters because `convert_fees_to_silver.py --latest` sorts bronze by S3 LastModified (not filename), so the filename is cosmetic — but Andrew's historical pattern is worth preserving for traceability and readability.
- **Standalone isolation:** fees does NOT feed `bd-price-update` or `bd-gold-trigger`. `silver/fees/` is consumed downstream only by `bd-portal-publisher` and `bd-portal-advisor-publisher`, both of which run AFTER gold completes via the `pipeline-complete.json` sentinel. A fees download failure therefore cannot cascade into the allocation/price/gold chain.
- **6 manual invocations to converge end-to-end.** Each failure surfaced a distinct bug in either the uploader bootstrap (bugs 1-3 in user_data) or the TS filename logic (bug 4). The dedicated verification loop was valuable — it caught issues that would have otherwise fired unattended in production on Monday.
