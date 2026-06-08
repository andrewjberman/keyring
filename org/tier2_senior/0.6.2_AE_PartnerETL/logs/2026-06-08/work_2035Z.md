# 0.6.2_AE_PartnerETL — Session Log 2026-06-08T2035Z

**archetype:** IMPLEMENT
**TO:** ADVI_COTETL P1 (EC2 provision + session-fetch + session-populate)

## Summary

COO §6.1 GO arrived (194935Z, Outcome B: 99% "No RepName Assigned" → C_07/leaderboards/advisor-cohort SKIP for v1). Built user-data.sh (EC2 bootstrap), canonical TF layout files (CHANGELOG, outputs, layers, alarms, s3-notifications stubs), applied P1 TF (14 resources created, i-0643a5bee8a8feabf), stored BD credentials in SM, built + deployed cot_bd_session_fetch.py (Playwright OIDC), iterated SSM dry-runs (v1→v4), and confirmed LIVE session populate. blackdiamond/cot/session now populated (expires 2026-06-09T16:35Z). DS pinged GO for bronze dry-run.

## Work done

### §6.1 Outcome B ruling

- 99% of COT transactions have "No RepName Assigned" — no usable advisor dimension.
- C_07 / advisor leaderboards / advisor-cohort: SKIP for v1.
- No impact on bronze/silver/gold transaction pipeline — those proceed normally.

### user-data.sh (EC2 bootstrap)

`infra/aws/ec2/cot-exporter/user-data.sh` — AL2023 bootstrap:
- python3.11 + pip + playwright deps (nss, nspr, atk, cups-libs, libdrm, xvfb, etc.)
- `python3.11 -m playwright install chromium` runs as root → `/root/.cache/ms-playwright/`
- /opt/cot-exporter setup, pulls bronze scripts from opal-data-cot/code/bronze/ at boot
- **Key:** HOME not set in user-data (defaults to /root) → chromium installs to /root/.cache/

Commit: 53130afc0

### Canonical TF layout (cot-pipeline)

Files created to mirror bd-pipeline/inf-pipeline pattern:
- `infra/aws/terraform/cot-pipeline/CHANGELOG.json` — deployment changelog (updated with v0.2.0 apply record)
- `infra/aws/terraform/cot-pipeline/outputs.tf` — stub
- `infra/aws/terraform/cot-pipeline/layers.tf` — stub (openpyxl P1 candidate if §6.3 probe fails)
- `infra/aws/terraform/cot-pipeline/alarms.tf` — stub
- `infra/aws/terraform/cot-pipeline/s3-notifications.tf` — stub (sentinel-file pattern noted)

Also fixed main.tf header: "Cottonwood Capital Advisors (CW)" → "(COT)".

### P1 Terraform apply — cot-pipeline-v0.2.0

Apply: 14 resources created:
- `aws_instance.cot_exporter` → i-0643a5bee8a8feabf (t3.small, ami-0c1e21d82fe9c9336, subnet-023db8cbfd99ffff2)
- `aws_iam_instance_profile.cot_exporter` + role
- `aws_ssm_document.cot_bd_session_fetch` (opal-cot-bd-session-fetch)
- `aws_ssm_document.cot_bronze_run` (opal-cot-bronze-run)
- `aws_cloudwatch_event_rule` × 2 (cot-bd-session-daily, cot-bronze-daily-trigger) — **DISABLED**
- `aws_cloudwatch_event_target` × 2
- `aws_lambda_permission` × 2
- Lambda update: EXPORTER_INSTANCE_ID wired to i-0643a5bee8a8feabf
- 0-diff confirmed, tagged cot-pipeline-v0.2.0

### SM credentials (blackdiamond/cot/credentials)

BD credentials extracted from local HAR (`C:\Users\AndrewBerman\Downloads\bd3.bdreporting.com.har`) by AE — Andrew-authorized, local-only, never via message bus (CTO §7 ruling).
- Used Python `json.dumps()` to ensure proper JSON encoding (PowerShell bare string interpolation strips quotes)
- Secret confirmed parseable: `{"username": "Andrew.Opal", "password": "...", "firm_acronym": "Default"}`
- Secret ID: `blackdiamond/cot/credentials`

### cot_bd_session_fetch.py

`data/cot/scripts/bronze/cot_bd_session_fetch.py` — Playwright OIDC session refresh:
- Reads credentials from SM via boto3 (python3.11)
- Navigates BD app → OIDC redirect → `login.bdreporting.com/Auth/SignIn` → fills form → submits
- Captures `.bd.identity` cookie, probes `/datamining/auth/token` for live token
- Writes session bundle `{bd_identity, captured_at, expires_at}` to SM (DRY_RUN=false)
- SESSION_TTL_HOURS=20

Deployed to opal-data-cot/code/bronze/ via safe-deploy.

### SSM dry-run iterations

| Run | Issue | Fix |
|---|---|---|
| v1 | `ModuleNotFoundError: No module named 'boto3'` — system python3 (3.9), no boto3 | Changed SSM doc to use python3.11 |
| v2 | SM credential JSON malformed (PowerShell quote stripping) | Stored via Python json.dumps; script reads SM internally |
| v3 | `playwright._impl._errors.Error: Executable doesn't exist at /home/ec2-user/.cache/ms-playwright/...` | user-data installs as root → `/root/.cache/ms-playwright/`; SSM doc had HOME=/home/ec2-user |
| v4 | HOME=/root fix | Success — full OIDC flow: login.bdreporting.com → bd3.bdreporting.com/#/ → .bd.identity (len=347) → /datamining/auth/token LIVE |

SSM fix commit: 9f3dbe7c1. Applied via safe-apply.sh.

### LIVE session populate

SSM `opal-cot-bd-session-fetch` DRY_RUN=false dispatched:
- CommandId: f787a9cb-ba6a-44f9-9f4b-3f758fdb5210
- Status: Success (5s elapsed)
- `.bd.identity` captured (len=347)
- Token confirmed LIVE: 01CF0646...
- `blackdiamond/cot/session` written, expires 2026-06-09T16:35Z

DS pinged GO at 20:35Z (send_message → 0.4.0_DS_ClientPlatform). DS standing by to dispatch opal-cot-bronze-run DryRun=true transactions.

## Current state

| Component | State |
|---|---|
| EC2 i-0643a5bee8a8feabf | RUNNING |
| blackdiamond/cot/credentials | POPULATED |
| blackdiamond/cot/session | POPULATED (expires 16:35Z 2026-06-09) |
| SSM opal-cot-bd-session-fetch | WORKING |
| SSM opal-cot-bronze-run | REGISTERED (DS-owned) |
| EventBridge cot-bd-session-daily | DISABLED (pending COO GO) |
| EventBridge cot-bronze-daily-trigger | DISABLED (pending COO GO) |
| DS bronze dry-run | PENDING (DS standing by) |

## Next actions

1. DS dispatches opal-cot-bronze-run (DryRun=true, transactions, 1 day)
2. DS RAVC2 COO after bronze dry-run passes
3. COO GO → AE enables EventBridge (TF apply, re-enable rules)
4. Tag cot-pipeline-v0.3.0 after EventBridge ENABLE apply
