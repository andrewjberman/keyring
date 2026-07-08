# 0.7.0_AE_CloudOps~A -- NFRA_WEBSITE W1: platform build + Patricia IAM + migration staging + deep /verify

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE, COORDINATE
**serial:** 0.7.0_AE_CloudOps~A | **date:** 2026-07-08 | **window:** ~1706Z (session launch) -> ~2020Z | **first log of session**

## Summary
Owned + delivered NFRA_WEBSITE.TO-1 (W1) end-to-end as the dedicated AE (Andrew-direct GO via COO):
stood up the Opal Capital WordPress-on-AWS PLATFORM, provisioned an Andrew-direct scoped AWS IAM for
TWLC's Patricia Barboza, staged the TWLC site backups into the resource group, and ran two /verify
passes (the second, adversarial, caught a real migration blocker). Co-authored `infra/aws/terraform/
website/` with 0.5.0_AE_OpalETL (they scaffolded plan-only; I owned every apply). Two deploy-ledgers
opened+closed. ALL credential delivery to Patricia is HELD per Andrew.

## Work done (chronological)
1. **Coordination + lane split** with 0.5.0 (they = TF scaffold req-1 + signal grounding req-5; me =
   stack/req-2, WP-admin/req-3, hardening/req-4, all applies, W1 close). Locked interface: AMI=Ubuntu
   22.04, role opal-website-wp-role (SSM-core + S3-backup-only), bucket opal-website-backups, code from
   the box's OWN bucket (firm-sep, no lambda-artifacts grant).
2. **Platform apply** (ledger nfra-website-w1): safe-apply'd 0.5.0's 15-resource scaffold (EC2 t3.small
   Ubuntu + EIP + SG 80/443-no-22 + IAM role/profile + opal-website-backups bucket). COO APPLY-GO'd the
   plan (RAVC PASS on the 4 gate criteria).
3. **Stack install** (req-2) via SSM S3->box (dispatch.sh): OpenLiteSpeed + LSPHP 8.2 + MariaDB 11.8
   LOCAL + WordPress (ols1clk) + wp core install. Fixed 4 Ubuntu/OLS gotchas iteratively (see Deploy
   Sequence). Base platform admin 'opaladmin'.
4. **Patricia WP-admin** (req-3): account 'patricia' created (administrator, WP-only). Delivery HELD.
5. **Hardening** (req-4): DISALLOW_FILE_EDIT, unattended-upgrades, fail2ban (wp-login jail live),
   least-priv DB, on-box S3 backup cron, + EBS-snapshot DLM (daily 7d).
6. **Andrew-direct scope expansion**: scoped AWS IAM for Patricia (ledger nfra-website-iam) -- user
   patricia@thewhitelabelcreative.com + 8-SID estate-admin inline policy + console login profile
   (CLI-set, reset-required). Firm-sep applied-verified.
7. **Security scrub**: I had recorded the console password in the nfra-website-iam ledger L3 proof
   (Andrew flagged). Scrubbed HEAD + ROTATED the live password to void the git-history value + banked
   a memory rule. Repo grep confirmed 1 occurrence, now dead.
8. **Migration data staged** (Andrew-direct): found the 2 TWLC backups in local Downloads (per CTO
   confirm), synced to s3://opal-website-backups/migration/ + a restore README. Turnkey for her dev.
9. **/verify x2**: surface pass (found+fixed stale delivery-script drift in S3); deep adversarial pass
   against the Bricks migration workflow (found+fixed a hard blocker -- see Current State).

## Compiler Tools
| Tool | Situation | Result | Note |
|---|---|---|---|
| comp-iam service opal-website-wp-role | pre-apply role scope (COO cond-1) | PARTIAL | showed SSM-core managed; the inline s3_backup (data-source ref) not expanded -- grounded via direct iam.tf read + live get-role-policy |
| comp-iam reconcile | attempted desired-vs-live | FAIL(usage) | wrong arg form; superseded by live get-role-policy (Rule 22a applied-truth) |

**What worked:** direct-read iam.tf + LIVE `aws iam get-role-policy` / `simulate-principal-policy` were
the authoritative firm-sep proofs (Rule 22a: for a FRESH IAM change, comp-iam DESIRED is not landed
truth). **What failed:** comp-iam service under-expands a separate `aws_iam_role_policy` resource;
comp-iam reconcile arg form. **Gap:** no comp-tool simulates IAM allow/deny decisions or reads live
login-profile/EIP-assoc/DLM/OLS-config -- these rode raw `aws`/SSM with inline `# rail-checked:` markers
(applied-state + policy-simulation + box-config verification, outside comp-tool coverage; logged).

## Deployment Sequence + Verification (AE)
Two safe-apply(HALTGT) applies, both 0-diff verified; stack + IAM-login via SSM/CLI (Rule 12 S3->box).
- **Apply 1 (nfra-website-w1):** 15 added/0/0. Live: instance i-0152e3fe2599fa630, EIP 18.208.18.213,
  sg-062bbb40a6c92509c, role opal-website-wp-role. 0-diff re-plan = "No changes". Ledger 6/6 closed.
- **Apply 2 (nfra-website-iam):** 5 added/0/0 (DLM policy-0c0c24e7981c5522c + role + attach + Patricia
  user + inline policy). 0-diff verified. Login profile CLI-created (reset-required). Ledger 4/4 closed.
- **Stack-install iteration (SSM), 4 gotchas fixed:** (a) Ubuntu ships no aws CLI -> user_data + one-time
  SSM bringup install v2; (b) firm-sep role can't read lambda-artifacts -> deliver code from own bucket
  opal-website-backups/code/website/ (+ lifecycle scoped to backups/); (c) wp-cli root:700 + nobody
  nologin -> `wp --allow-root` + re-chown docroot; (d) ols1clk stages files but not the wizard -> `wp
  core install`.
- **Verification (EXERCISED, cite):**
  - `aws ec2 describe-security-groups sg-062bbb40a6c92509c` = ONLY 80+443 from 0.0.0.0/0, ZERO port-22.
  - `aws iam get-user-policy` (Patricia) = 8 scoped SIDs, zero attached-managed, zero data-estate/SM.
  - `aws iam simulate-principal-policy` (Patricia): s3:GetObject@opal-data-bd / secretsmanager /
    ec2:TerminateInstances / iam:CreateAccessKey = ALL implicitDeny; s3:PutObject@opal-website-backups
    = allowed. (Firm-sep proven by decision-simulation.)
  - Public curl EIP: home 200, /wp-login.php 200, /sample-page/ 200, /wp-json/ 200 (server: LiteSpeed).
  - Backup path exercised: DB dump + wp-content landed at s3://opal-website-backups/backups/ (s3 ls
    confirmed, not just script "OK").
  - login-profile reset-required=true; EIP eipassoc-0de780d17d8677041 -> instance; DLM State=ENABLED;
    bucket public-access-block all-4-on; MariaDB 11.8; php max_input_vars=5000; all PHP ext present.

### Deep-/verify findings (adversarial, vs the Bricks migration workflow)
- **CRITICAL (fixed):** pretty permalinks + REST 404'd on OpenLiteSpeed -- no .htaccess (WP can't
  auto-generate on non-Apache) AND OLS only reads .htaccess on restart. Wrote standard WP .htaccess +
  `lswsctrl restart` in bootstrap; verified /sample-page/ + /wp-json/ = 200 public. Bricks needs
  /wp-json/ to edit -- this would have fully blocked her dev.
- **Fixed:** max_input_vars 1000->5000 (silent Bricks-template truncation on save).
- **Fixed (surface pass):** S3 create-wp-admin.sh was stale (buggy $argv) -> re-staged; all 5 scripts
  now S3==local (md5 MATCH).
- **Verified clean:** SQL dump collations utf8mb4_unicode_ci/_520_ci (MariaDB-compatible, no MySQL-8
  0900); all PHP extensions present.

## Files Modified
See commit messages (16 commits, 156a97ff2 -> bed107e8d). Key: `infra/aws/ec2/website/*` (5 stack
scripts + README), `infra/aws/terraform/website/{s3,user_data,dlm,iam_patricia}.tf` (co-author edits),
`infra/aws/ec2/EC2_MANIFEST.json` (opal-website-wp entry), `infra/website/*` (docs-home: README
inventory, RUNBOOK, CREDENTIAL_HANDOFF + 3 SVGs), 2 deploy-ledgers, 1 memory file + MEMORY_FULL pointer.

## MCP traffic
~15 messages handled. Significant: COO GO (NFRA_WEBSITE dedicated-owner) + APPLY-GO + W1-RAVC-ACCEPTED +
Patricia-IAM-ACK; 0.5.0 interface handoff + scaffold-committed handoff + IAM-author firm-sep sign-off;
CTO backup-location confirm. Routed: CVO security-glance REQUEST (pre-delivery gate on Patricia's
external IAM, CC COO) -- PENDING.

## Blockers
None blocking me. External gates (not blockers): (1) Andrew's final console password + delivery
release; (2) CVO security glance on Patricia's IAM (pre-delivery). Both by design (delivery HELD).

## Current State (handoff surface)
- **Platform LIVE + verified end-to-end:** EC2 i-0152e3fe2599fa630 (Ubuntu 22.04, t3.small, Opal VPC
  subnet-039d04cfaee66a5f6), EIP 18.208.18.213, sg-062bbb40a6c92509c (80/443 public, no 22, SSM-only).
  OpenLiteSpeed + LSPHP8.2 + MariaDB11.8-local + WordPress at /usr/local/lsws/wordpress. Serves 200
  public incl. pretty permalinks + REST. Terraform infra/aws/terraform/website (both applies 0-diff).
  EC2_MANIFEST registered. AutoShutdown=false (persistent).
- **Firm-sep (applied-verified):** instance role opal-website-wp-role = SSM-core + R/W on
  opal-website-backups ONLY. Patricia IAM (user patricia@thewhitelabelcreative.com) = 8-SID estate-admin
  (describe + start/stop/reboot tag-scoped + SSM shell + backup-bucket + logs + self-MFA); ZERO
  data-estate/other-bucket/SM/terminate/SG-rewrite (simulate-proven). Console login profile
  reset-required; password ROTATED to an unrecorded interim value (Andrew sets final at delivery).
- **Migration data staged:** s3://opal-website-backups/migration/ = updraft-backup-2026-06-30.zip
  (74.9MiB, recommended restore), opalcapital.zip (86.7MiB, fallback + opal_202606.sql), README.txt.
  Patricia's IAM reaches it; migration/ not lifecycle-expired.
- **Backups:** on-box cron 03:30Z -> backups/ (exercised OK); EBS DLM policy-0c0c24e7981c5522c daily 7d.
- **Docs home** infra/website/: README (resource inventory current), RUNBOOK, CREDENTIAL_HANDOFF (the
  delivery gates + protocol), 3 architecture SVGs.
- **Old host** 72.167.58.121 (GoDaddy) UNTOUCHED; NO GoDaddy DNS change (that is W3).

## Next Steps
- **[Andrew]** confirm the final console password (needs uppercase/symbol -- AWS baseline rejected the
  all-lowercase original; interim rotated value is unrecorded) + release the delivery hold.
- **[3.0.0_SA_CVO]** security glance on iam_patricia.tf (external console + SSM-shell) -- pre-delivery gate.
- **[0.7.0_AE_CloudOps~A]** on release+glance: set final pw, generate Patricia WP reset link
  (dispatch.sh admin -- now re-staged/fixed), deliver both securely (out-of-band, not plaintext email);
  notify COO handoff complete. Then W2 (Certbot TLS + SMTP + CVO staging-verify), W3 (GoDaddy apex-A
  cutover + rollback window).
- **[2.0.0_SA_COO]** hold telling Andrew "ready for her dev" until he releases; drives W2/W3 sequencing.
