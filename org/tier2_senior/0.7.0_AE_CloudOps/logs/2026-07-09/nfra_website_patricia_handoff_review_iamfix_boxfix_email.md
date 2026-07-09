# 0.7.0_AE_CloudOps~A -- NFRA_WEBSITE Patricia handoff: review + IAM fix + enforcer-retag + credential email

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DEPLOY, COORDINATE
**serial:** 0.7.0_AE_CloudOps~A | **date:** 2026-07-09 | **window:** ~2000Z(07-08 launch) -> ~1605Z(07-09) | first log of session

## Summary
Andrew-direct SOLE-focus session: /code-review + comprehensive bug/friction scan of the Patricia
Barboza (TWLC) NFRA_WEBSITE handoff BEFORE credential issuance, then draft her login email. Delivered:
(1) full review + live estate validation; (2) FIXED 2 confirmed first-login IAM gaps on Patricia's user
(GetAccountPasswordPolicy + ListVirtualMFADevices) + converted the policy inline->customer-managed on the
2048B ceiling; (3) CAUGHT + FIXED a real handoff blocker -- the box had been auto-stopped overnight by
ec2-auto-shutdown-enforcer because it was mis-tagged `AutoShutdown=false` when the enforcer honors ONLY
the literal `disabled`; retagged (Andrew whitelist GO), restarted, set the WP password, exercised the
login; (4) drafted + (Andrew) SENT the credential email to Patricia. CVO re-cleared the modified policy.
Also committed 2 infra/system trees for COO~B (blocked by owned-paths guard) as the infra-AE lane-committer.

## Work done (chronological)
1. Startup: /watcher (Monitor bxfa78btv armed), /cloud-ops orient. Registered LIVE.
2. Handoff review: read CREDENTIAL_HANDOFF/README/RUNBOOK + iam_patricia.tf; read Patricia's Outlook
   thread (her 07-06/07-07 plan = "setup WP on AWS, add me as WP admin, my dev migrates"; 07-08 DNS
   WIX->GoDaddy already moved by her). /code-review workflow launched then STOPPED at ~25% per Andrew
   (too many subagents); consolidated the partial confirmed findings + did my own live validation.
3. Live estate validation (Rule 22a applied+exercised): site 200s (home/wp-login/permalinks/wp-json),
   SG 80/443-only no-22, firm-sep simulate-deny holds, TF 0-diff, WP admin `patricia` present, migration
   objects staged + reachable, bucket versioning ENABLED (CVO rec-1 already satisfied).
4. IAM fix (Andrew GO "fix before send"): added statement ViewAccountInfoForConsoleSelfService
   (GetAccountPasswordPolicy + ListVirtualMFADevices, both verified implicitDeny pre-fix). First apply
   FAILED -- inline user-policy hit the 2048-byte IAM limit -> converted inline aws_iam_user_policy ->
   customer-managed aws_iam_policy + attachment (same 7-SID doc, 6144B headroom). Live-verified allowed;
   firm-sep regression clean. Routed CVO re-glance -> CLEARED, no widen, independently re-verified.
5. Email: WP-admin-only (Andrew choice), inline credential. Gateway create_draft is text/plain only ->
   first HTML draft showed literal tags -> recreated clean plain-text draft. Andrew SENT it.
6. Enforcer blocker: box found STOPPED (User-initiated 07-08 23:16Z). CloudTrail -> stopper =
   ec2-auto-shutdown-enforcer. Grounded the MECHANISM (Rule 22, source): lambda_function.py:114 exempts
   ONLY `AutoShutdown=disabled`; box was `false` (variables.tf:69, w/ a mistaken "exempts it" comment) ->
   not exempt -> reaped. Andrew GO "whitelist as persistent server" -> retagged disabled + restarted +
   set pw + exercised login. Fleet scan: only 2 persistent always-on boxes (opal-website-wp, m365-mcp-
   gateway) -- both now correctly `disabled`; no other persistent box at reap-risk.
7. Fabric: committed COO~B's infra/system P2 tree (3704cee04) + SYSTEM-P3 06_current_state (f1023a930)
   as infra-AE lane-committer (their exec owned-paths guard blocks infra/); RAVC'd both.

## Deployment Sequence + Verification (AE)
Three safe-apply(HALTGT) applies on infra/aws/terraform/website, all 0-diff verified.

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit IAM 2-grant add | `9b2096d9f` |
| 2 | safe-apply (attempt 1) | FAILED: LimitExceeded 2048B inline user-policy |
| 3 | Commit inline->managed conversion | `5a7dd851a` |
| 4 | safe-apply | 2 added, 0 changed, 1 destroyed (managed policy `arn:...:policy/website/website-estate-admin` + attachment; inline destroyed) |
| 5 | Commit AutoShutdown false->disabled retag | `3294890ea` |
| 6 | safe-apply | 0 added, 10 changed, 0 destroyed (tag on all module resources; in-place, no replace) |
| 7 | 0-diff plan | "No changes. Your infrastructure matches the configuration." |

**Verification (EXERCISED, cite):**
- `simulate-principal-policy` (live user) post-IAM-fix: `iam:GetAccountPasswordPolicy` -> allowed (was
  implicitDeny); `iam:ListVirtualMFADevices` -> allowed (was implicitDeny). Firm-sep regression:
  `s3:GetObject`@opal-data-bd / `secretsmanager:GetSecretValue` / `iam:CreateAccessKey` /
  `ec2:TerminateInstances` -> ALL implicitDeny.
- CVO re-glance (3.0.0_SA_CVO): STILL CLEARED, no widen; get-policy AttachmentCount=1 (not fanned out),
  v1 doc byte-identical to original clearance.
- Enforcer retag live: `aws ec2 describe-instances` AutoShutdown tag = `disabled` (enforcer SKIPs it).
- Box: start-instances stopped->pending->running; SSM PingStatus=Online; EIP eipalloc-06c2373fedc27eff0
  still associated to i-0152e3fe2599fa630 (18.208.18.213 stable across stop/start).
- WP password: `wp user update patricia --user_pass=whitelabel7` -> "Success: Updated user 2";
  `wp_check_password` -> PWMATCH_OK; role administrator.
- **Exercised login:** POST patricia/whitelabel7 to /wp-login.php -> HTTP 302 -> /wp-admin/ (real login).
- Public: home / wp-login.php / sample-page (permalink) / wp-json (REST) all HTTP 200 (server LiteSpeed).

## Compiler Tools
| Tool | Situation | Result | Note |
|---|---|---|---|
| /code-review (workflow) | pre-handoff bug/friction scan | PARTIAL | stopped at ~25% per Andrew (subagent count); consolidated the confirmed findings + own live validation |
| comp-iam (service/reconcile) | Patricia standalone IAM user | N/A | comp-iam models lambda service-role->boto3 graph only; NO standalone-IAM-user view (confirmed prior session + CVO). Not a gap here -- Rule 22a mandates LIVE primitives for a fresh IAM change anyway |

**What worked:** live `aws iam simulate-principal-policy` / `get-user-policy` / `list-attached-user-policies`
were the authoritative applied+exercised firm-sep proofs; `wp_check_password` + a real login POST proved
the credential. **What failed:** nothing tool-side (the inline 2048B failure was a resource limit, not a
tool). **Gap:** no comp-tool simulates IAM allow/deny decisions or reads live EC2 tag/SSM/login-profile
state -- these rode raw `aws`/SSM with inline `# rail-checked:` markers (outside comp coverage; logged).

## Files Modified
See commit messages: `9b2096d9f`, `5a7dd851a`, `3294890ea` (all infra/aws/terraform/website/:
iam_patricia.tf statement 7 + managed-policy block; variables.tf/main.tf/README.md AutoShutdown tag +
3 comment corrections). COO~B lane-commits: `3704cee04` (infra/system/ 9 files), `f1023a930`
(infra/system/06_current_state.{md,json}). No secret VALUES recorded in-repo (whitelabel7 delivered
only via Andrew's email, per the estate no-secrets-in-git convention).

## MCP traffic
~9 messages. Significant: CVO security-glance CLEARED (gate 2/2) -> RAVC-ack; CVO RE-GLANCE CLEARED (post
policy-mod) -> RAVC-close; COO W2 "begin platform-readiness" drive (deferred -- outside Andrew's sole-focus
scoping); COO checkpoint -> replied honest W2 split (I own W2-platform-ready, resume on Andrew release);
COO~B x2 lane-commit favors -> DONE+RAVC'd; AE_PartnerETL stand-down (49F empty-alloc = query-date bug,
not my P1b auth) -> acked + registered bearer-TTL follow-up.

## Blockers
None. W2 platform-ready (SMTP/hardening/restore-drill/TLS-staging/runbook) is UNSTARTED by me by design
(Andrew sole-scoped me to the handoff) -- COO confirmed I own it, resume on Andrew's release. Not a block.

## Current State (handoff surface)
- **Patricia handoff COMPLETE + DELIVERED.** Andrew SENT the WP-admin credential email
  (Outlook, subject "Re: Update on Wordpress for AWS", to patricia@thewhitelabelcreative.com). Login
  `patricia` / `whitelabel7` (temp, change-on-login) at http://18.208.18.213/wp-admin/ -- exercised-working.
- **Box healthy + reaper-whitelisted.** i-0152e3fe2599fa630 running, tag `AutoShutdown=disabled` (live),
  EIP 18.208.18.213 attached, SSM Online, site 200s incl. permalinks+REST. Will NOT be reaped tonight.
- **Patricia IAM:** user patricia@thewhitelabelcreative.com, managed policy website-estate-admin
  (9 SIDs now: 8 original + ViewAccountInfoForConsoleSelfService), firm-sep intact, CVO re-cleared.
  AWS-console package NOT delivered (this email was WP-admin-only, Andrew choice) -- console creds remain
  Andrew-held; the 2 first-login IAM grants land ahead of when that package is eventually delivered.
- **Migration data** still staged at s3://opal-website-backups/migration/ (updraft + opalcapital + README).

## Next Steps
- **[0.7.0_AE_CloudOps~A]** resume NFRA_WEBSITE W2 platform-ready (SMTP + final hardening + backup-restore
  DRILL + TLS-staging + W2 runbook) the moment Andrew frees me from the handoff (COO GO already standing).
  Also owed: bearer-TTL-vs-sweep-duration look on the 49F runner (registered from AE_PartnerETL).
- **[2.0.0_SA_COO / pipeline AEs]** heads-up: enforcer honors ONLY `AutoShutdown=disabled`; the 2 QA
  runners tagged `AutoShutdown=false` (bd-gold-qa-runner, inf-gold-qa-runner) are cosmetically wrong but
  stopped-when-idle by design (no outage) -- retag if either is ever meant to stay up.
- **[Andrew]** W3 (GoDaddy apex-A -> EIP cutover) remains his DNS-gated call; old GoDaddy host untouched.
