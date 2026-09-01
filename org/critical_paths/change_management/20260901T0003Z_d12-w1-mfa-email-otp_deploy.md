# DEPLOY LEDGER — D12_PLATFORM_OPS WS-1: identity record + email OTP

| | |
|---|---|
| **Opened** | 2026-09-01T00:03Z |
| **State** | OPEN |
| **Seat** | `0.7.0_AE_CloudOps~Z` (site Z) |
| **TO** | `D12_PLATFORM_OPS.W1-SITEZ.identity-record-and-email-otp` (amendments 1 + 2) |
| **Pipeline** | `infra/aws/terraform/portal-auth` |
| **Closes to** | `2.0.0_SA_COO~Z` (validation), `1.0.0_SA_CTO~Z` (acceptance) |

## What lands

| # | Change | Kind |
|---|---|---|
| 1 | `opal-portal-auth-mfa` DynamoDB table (TTL, no GSI, no PITR) | CREATE |
| 2 | `opalinvest-auth-permissions` — one added statement, 4 actions on that ONE table ARN | MODIFY |
| 3 | `aws_ses_domain_mail_from` on `opalinvest.dev` -> `mail.opalinvest.dev` | CREATE |
| 4 | Route53 `TXT opalinvest.dev` (SPF) | CREATE |
| 5 | Route53 `TXT _dmarc.opalinvest.dev` (DMARC p=none) | CREATE |
| 6 | Route53 `MX mail.opalinvest.dev` | CREATE |
| 7 | Route53 `TXT mail.opalinvest.dev` (MAIL FROM SPF) | CREATE |
| 8 | `opalinvest-auth-handler` Lambda code (S3 artifact version bump) | MODIFY |
| 9 | `opal-users-v2` — backfill `mfaChannel='none'`, `mfaEnabled=false` on 48 PROFILE items | DATA |

**NOT in this deploy, stated so the absence is auditable:** no alarm, no SNS topic
or subscriber, no monitor, no freshness checker, no deliverability watcher, no SMS
sender, no remembered-device state, no DMARC report-collection pipeline, and no
change to `opalinvest.com` (different nameservers, not ours).

## Rollback

| Leg | Reversal |
|---|---|
| DNS (4-7) | `terraform destroy -target` on the individual records, or delete the record sets. All four are pure adds to a zone that had none — reverting restores the exact prior state (11 records, one TXT). |
| MAIL FROM (3) | Remove the resource — SES falls back to its own `amazonses.com` subdomain. `BehaviorOnMxFailure=UseDefaultValue` means mail keeps sending throughout, so this leg cannot cause a login outage even mid-rollback. |
| Table + IAM (1,2) | Drop the added statement, then delete the table. Safe once no MFA-enabled account exists. |
| Lambda (8) | Re-point `s3_object_version` at the prior artifact version and apply. |
| Data (9) | `mfaChannel='none'` / `mfaEnabled=false` is the OFF state — it enables nothing for anybody, so there is nothing to undo for safety. Removing the attributes is possible but pointless. |

⭐ **THE ORDERING IS THE REAL SAFETY PROPERTY, NOT THE ROLLBACK.** Every account
lands at `mfaChannel='none'` (leg 9), so legs 1-8 change the behaviour of exactly
ZERO logins. MFA becomes live for an account only when that account's preference
is deliberately flipped — which satisfies Andrew's staged-rollout ordering
("testing for 2FA on my account ... before pushing anything to clients") without
a separate gate, because nothing is exposed to clients by this deploy at all.

## Progress

- [x] 00:03Z — entry opened, before any apply
- [ ] source committed
- [ ] artifact built + uploaded
- [ ] `terraform plan` read
- [ ] `safe-apply` (Rule 18)
- [ ] 0-diff re-plan
- [ ] migration `--apply`
- [ ] W1-1..W1-10 exercised
- [ ] closed
