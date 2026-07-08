# NFRA_WEBSITE.TO-1 (W1) -- first-mover: TF scaffold (plan-only) + req-5 signal grounding + co-author handoff

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, VALIDATE

**Serial:** 0.5.0_AE_OpalETL | **Window:** ~17:06Z -> ~17:27Z 2026-07-08
**TO:** NFRA_WEBSITE.TO-1 (2.0.0_SA_COO GO; co-assignee, first-mover). Owner: 0.7.0_AE_CloudOps~A.
**Commit:** ec1148124 (TF scaffold, pushed CLOUD; stacks on 0.7.0~A's 61d7ed4b7 docs-home)

## Summary
COO GO'd me as the IMMEDIATE first-mover on NFRA_WEBSITE.TO-1 (WordPress lift-and-shift onto AWS) while
0.7.0_AE_CloudOps~A spawned as dedicated owner. Delivered my two legs: req-1 (the TF scaffold, PLAN-ONLY)
+ req-5 (ground the 2 PRD signals). RAVC'd the plan to COO; handed 0.7.0~A the resource addresses + the
EC2_MANIFEST entry (their lane). Apply is 0.7.0~A's (safe-apply + deploy-ledger + stack + Patricia WP-admin).

## Work done

### req-5 -- the 2 signals GROUNDED (live, not inferred)
- (a) Cloudflare PROXY vs Turnstile-only -> **Turnstile-CAPTCHA-ONLY, NOT proxying**. Grounded LIVE via
  DNS: opalcapital.com NS = ns73/ns74.domaincontrol.com (GoDaddy), apex+www A = 72.167.58.121 (a GoDaddy
  hosting IP, NOT a Cloudflare proxy range 104.16.x/172.67.x). Plugin set (PRD SS2) has only
  simple-cloudflare-turnstile. -> W3 cutover is a clean GoDaddy apex-A -> EIP flip (resolves PRD open-decision #3).
- (b) OpenLiteSpeed keeps litespeed-cache -> **YES** (OLS is the open-source LiteSpeed edition; LSCache
  plugin full-page/browser/object cache + minify all work; only ESI/edge is LS-Enterprise-only, not needed).
  -> req-2 web-server choice confirmed. Reported both to COO (ACK'd).

### req-1/req-7 -- TF scaffold (infra/aws/terraform/website/, PLAN-ONLY, ALL-Terraform)
15 resources, all declared in TF (Andrew req-7: no console/manual): 1x EC2 t3.small **Ubuntu 22.04**
(0.7.0~A OS decision -- OLS better-supported on jammy) in the Opal VPC (vpc-0cc0c6a75e54605e3) public
subnet-039d04cfaee66a5f6 + Elastic IP + SG (80/443 public, **NO 22** -- SSM only) + IAM instance role
scoped to ONLY AmazonSSMManagedInstanceCore + the opal-website-s3-backup inline policy (opal-website-backups
bucket ONLY; ZERO data-estate = firm-sep) + the backup bucket (versioned/SSE/PAB/lifecycle). Hardening:
IMDSv2-required, encrypted gp3, AutoShutdown=false (persistent, reaper-exempt), lifecycle
ignore_changes[ami,user_data]. Thin user_data seam (bootstrap_s3_uri default "" -> 0.7.0~A drives the
stack via SSM post-boot; NO inline stack install, Rule 12).

## Deployment Sequence + Verification (PLAN-ONLY -- apply is 0.7.0~A's)
- `.tools/terraform.exe -chdir=infra/aws/terraform/website init` -> OK (aws v5.100.0, backend s3 key=website/tfstate).
- `validate` -> Success. `plan` -> **15 to add, 0 to change, 0 to destroy** (no estate collision).
- Live collision check (rail-checked exception -- a fresh-name existence probe comp-iam's DESIRED view
  can't answer): opal-website-wp-role, opal-website-wp-profile, opal-website-backups, SG opal-website-wp-sg
  ALL return NoSuchEntity/404/empty -> apply lands clean.
- **NOT applied.** EC2_MANIFEST.json edit reverted (owned-paths hook: SHARED_CLOUD_OPS lane) -> entry handed
  to 0.7.0~A to commit in their lane.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| terraform init/validate/plan | infra/aws/terraform/website | PASS | 15-add/0-change/0-destroy, validate OK (plan-only) |
| comp-which | IAM-scope + collision routing | ADVISORY | routed to comp-iam service (DESIRED view; doesn't fit a fresh-name live probe) |
| live DNS (Resolve-DnsName) | opalcapital.com NS+A | PASS | grounded Cloudflare-not-proxying (GoDaddy NS + GoDaddy IP) |
| live collision check (aws get-role/head-bucket) | 4 fresh names | PASS | all NoSuchEntity/404 -- rail-checked marker (no comp-tool fits a pre-create existence probe) |
| safe-commit / owned-paths hook | scaffold + manifest | PASS | hook correctly blocked EC2_MANIFEST.json (CloudOps lane) -> handed to 0.7.0~A |

**What worked:** delegating the estate TF-convention sweep to a subagent kept my context clean + gave
exact constants (VPC/subnet/backend/AMI-pattern/EC2_MANIFEST shape) so the module planned clean first try.
Live-DNS grounding of the Cloudflare signal (vs inferring) = a decisive, cited answer. **What failed:** the
aws launcher word-splits quoted `--command` (execute-command) + MSYS mangles leading-`/` log groups ->
used run-task JSON files + PowerShell for logs (same gotchas as the P3 in-VPC work). **Gap found:** none.

## Blockers
None. Apply is GATED on COO GO + is 0.7.0~A's lane (not mine). My deliverables (req-1 scaffold plan-clean +
req-5 signals) are complete + handed off.

## Current State (handoff)
- **Module:** infra/aws/terraform/website/ (providers/variables/main/iam/s3/outputs/user_data.sh.tftpl/README/.terraform.lock.hcl), committed ec1148124, init'd, plan-clean. Backend s3 key=website/tfstate.
- **Addresses handed to 0.7.0~A:** aws_instance.website / aws_eip.website / aws_security_group.website /
  aws_iam_role.website_wp (opal-website-wp-role) / aws_iam_instance_profile.website_wp / aws_iam_role_policy.s3_backup
  (opal-website-s3-backup) / aws_s3_bucket.backup (opal-website-backups). Outputs: instance_id, elastic_ip, role/profile/bucket/sg.
- **0.7.0~A owns:** safe-apply + deploy-ledger, the stack install (their infra/aws/ec2/website/ scripts, SSM
  post-boot), Patricia WP-admin (req-3), the EBS-snapshot DLM policy (req-4 -- co-authors into my module),
  the infra/website/ RESOURCE-INVENTORY table + the EC2_MANIFEST entry.
- **Leash held:** old host 72.167.58.121 (GoDaddy) UNTOUCHED (rollback); no GoDaddy DNS change; firm-sep (role touches only opal-website-backups).

## Next Steps
1. **[2.0.0_SA_COO]** GO on the RAVC'd plan -> 0.7.0~A opens the deploy-ledger + safe-apply.
2. **[0.7.0_AE_CloudOps~A]** pull ec1148124 -> comp-iam the role -> add the DLM policy + EC2_MANIFEST entry ->
   safe-apply -> stack install -> Patricia WP-admin -> fill the infra/website/ inventory table -> W1 close.
3. **[0.5.0_AE_OpalETL]** (queued, not now) wire the in-VPC PROMOTE CSE producer @0.4 into 0.7.0's coupled
   derive-image deploy pass (~D's R4 contract) -- fires when that pass runs.
