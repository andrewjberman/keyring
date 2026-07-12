# 0.7.0_AE_CloudOps~A -- NFRA_WEBSITE phase 2 (W2): SES SMTP + TLS prep + DLM fix + requirements.txt

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, IMPLEMENT, VALIDATE, COORDINATE
**serial:** 0.7.0_AE_CloudOps~A | **date:** 2026-07-10 (logged 2026-07-12 per Andrew-direct /log-now) | **window:** ~1854Z(session start) -> ~2153Z (Patricia draft) | first + only log of this session

## Summary
Andrew-direct in-session drive of NFRA_WEBSITE "phase 2" (= W2 = "configure SMTP + issue TLS", his own
words to Patricia). Migration was completed by TWLC's dev between sessions; I verified it, then executed
the Opal-side of step two end-to-end: wired the WordPress Contact form to AWS SES (no stored secret, via a
scoped instance-role + a sendmail shim -- the free wp-mail-smtp has the SES mailer disabled Pro-only),
repointed form notifications to andrew@ (verified, delivering now), sent SES opt-in verifications for
mike + patricia, prepped+verified TLS/certbot (W3-DNS-gated cert), fixed a silently-broken EBS-snapshot
backup, set up opalcapital.com SES domain+DKIM for the sender graduation Andrew requested, built a
consolidated requirements.txt + emailed it to his gmail, and drafted (not sent) the reply to Patricia
(CC CFO AJ Graff) since the remaining next-steps are GoDaddy DNS changes.

## Work done (chronological)
1. Startup: /watcher (Monitor buehoglbw), /cloud-ops, org/XXX startup. ACKed COO's [STOP] vendor-API
   prohibition (already sovereign in memory; re-bound; zero vendor calls all session).
2. Grounded NFRA_WEBSITE: PRD + project JSON + prior logs + runbook + CREDENTIAL_HANDOFF. Checked
   Patricia's email (M365): 07-10T16:12Z "all set, ready for step two" + she stood up a fresh WP admin
   for Andrew. Verified: site serves the REAL migrated Opal Capital (Bricks/ACSS, WP7.0.1); box healthy
   (running, EIP 18.208.18.213, AutoShutdown=disabled, SSM Online); Andrew's login exercised (POST ->
   302 /wp-admin, opaladmin=andrew@opalinvest.com admin; email-as-login).
3. Grounded SMTP state: migrated wp-mail-smtp = mailer=smtp with EMPTY host = already broken. Contact
   form (1 form) 2 notifications -> info@opalinvest.com + {admin_email}=mike@hirst.digital; no external
   confirmation. SES = SANDBOX (ProductionAccessEnabled=false); opalinvest.dev verified+DKIM SUCCESS;
   info@ + mike@ NOT verified. AskUserQuestion -> Andrew chose SES-sandbox->Opal + leave admin_email.
4. SES wiring (no stored secret): scoped ses:SendEmail/SendRawEmail on opal-website-wp-role (iam.tf).
   FIRST apply used Resource=identity ARNs -> L4 exercise caught AccessDenied on the RECIPIENT identity
   (SES evaluates SendEmail authz against the recipient) -> fixed to Resource=* + ses:FromAddress=
   noreply@opalinvest.dev condition (AWS-documented pattern; still one-sender-scoped). Free wp-mail-smtp
   has AmazonSES disabled=>true (Pro-only, source-confirmed) -> built ses-sendmail.sh shim (PHP mail() ->
   aws ses send-raw-email via instance role), sendmail_path via lsphp82 scan-dir ini, wp-mail-smtp
   mailer=mail force-from. Shim base64-JSON raw-message fix (fileb:// not expanded in shorthand).
   EXERCISED: wp_mail()->andrew@ delivered inbox from "Opal Capital" <noreply@opalinvest.dev>.
5. Contact form recipients (Andrew: "send to both mike and me at andrew@"): repointed the "Info
   Notification" -> andrew@opalinvest.com (verified, delivers now); fired GF test notification -> arrived
   ("New Inquiry via Opal Capital Website", blank body b/c synthetic entry). Admin Notification stays
   {admin_email}=mike (separate notification so andrew@ always delivers). SES opt-in verifications
   CREATED (Andrew-direct) for mike@hirst.digital + patricia@thewhitelabelcreative.com (both absent).
6. DLM backup fix: terraform plan drift showed aws_dlm_lifecycle_policy.website State=ERROR ("Tag
   (Project) already defined" -- copy_tags + tags_to_add both set Project) => ZERO EBS snapshots since
   W1. Dropped the dup key; targeted safe-apply -> State=ENABLED.
7. TLS prep (non-disruptive): tls-prep.sh -> certbot 5.6.0 (snap), HTTP-01 webroot armed + VERIFIED (OLS
   serves /.well-known/acme-challenge static over HTTP -> 200, not WP-rewrite-intercepted), renewal
   OLS-reload deploy-hook. Cert issue + OLS SSL listener wiring documented for W3 (DNS-gated).
8. opalcapital.com sender graduation (Andrew-direct "graduate to the actual official url"): created SES
   domain identity + Easy DKIM (3 CNAME tokens, PENDING). Handed Andrew the exact GoDaddy records.
9. requirements.txt: aggregated all 61 real requirements*.txt across the estate -> 83 distinct packages,
   consolidated inventory at repo root (owned-paths lane guard BLOCKED the commit -- root file outside my
   lane; left in working tree, not force-committed). Emailed inline to andrew.opalinvest@gmail.com via
   M365 (gateway can't attach binaries; SES-sandbox can't reach external gmail).
10. Patricia reply: drafted (Andrew feedback: no em-dashes/--; closing reframed to his offer to log in),
    created in Outlook Drafts to Patricia CC AJ Graff (aj@opalinvest.com) -- NOT sent.

## Deployment Sequence + Verification (AE)
| Ledger / step | Commit | Verify (EXERCISED) |
|---|---|---|
| SES iam (Resource=identity, too tight) | `974af3ebb` | simulate on identity ARN allowed, but live send AccessDenied on recipient |
| SES iam Resource=* + FromAddress cond | `d6b441462` | simulate: ALLOW noreply@ / DENY spoof / DENY no-ctx / POS-CTL s3:PutObject allowed / FIRMSEP opal-data-bd deny; targeted 0-diff |
| ses-sendmail shim + base64 fix | `1ee34e208`, `096a5d1ff` | wp_mail()->andrew@ = WP_MAIL_RETURNED_TRUE + shim log OK msgid; delivered inbox 19:57Z |
| DLM dup-tag fix | `04bc1a412` | targeted safe-apply state ERROR->ENABLED; live get-lifecycle-policy State=ENABLED |
| runbook SMTP + TLS docs | `5be82b8cb`, `0956c99f8` | doc parity |
| tls-prep.sh | `02af3ab60` | certbot 5.6.0; curl http://EIP/.well-known/acme-challenge/probe -> 200 body |
Ledgers `nfra-website-w2-ses-smtp` (5/5) + `nfra-website-dlm-tagfix` (2/2) both CLOSED; `check --red` clean.
requirements.txt NOT committed (owned-paths lane block; in working tree).

## Compiler Tools
| Tool | Situation | Result | Note |
|---|---|---|---|
| comp-iam gaps | after iam.tf SES change (AE minimum) | ses = COVERAGE-UNKNOWN | comp-iam does NOT model ses, and models (action) not (action,resource,condition) -> live simulate is the Rule-22a authority |
| aws iam simulate-principal-policy | fresh condition-scoped SES grant verify | PASS (all controls behaved) | rail-checked marker (no comp-tool fits); the authoritative applied+exercised proof incl. positive + firm-sep controls |
| comp-which HUD | nudged raw `aws` IAM/DLM/EC2 inspection | rail-checked | 2 gated calls carried `# rail-checked:` (SES/DLM state not comp-modeled) |

**What worked:** live `aws` primitives (simulate-principal-policy, ses send-raw-email, ssm wp-cli) were the
authoritative applied+exercised proofs; the L4 exercise catching the recipient-authz AccessDenied is the
textbook "exercise, not config-read" (Rule 22a) win -- simulate on the from-identity passed while the real
send failed. **What failed:** nothing tool-side (two self-inflicted CLI bugs -- --source vs --from, and
fileb:// in shorthand -- both caught by the shim log + retest). **Gap:** no comp-tool models SES
identities/sandbox, DLM policy state, standalone-user IAM, or on-box (OLS/LSPHP/wp-cli) state -- all rode
raw aws/SSM with markers.

## Files Modified
See commit messages: `974af3ebb` `d6b441462` `1ee34e208` `096a5d1ff` `04bc1a412` `5be82b8cb` `02af3ab60`
`0956c99f8` (infra/aws/terraform/website/{iam.tf,dlm.tf}, infra/aws/ec2/website/{ses-sendmail.sh,
tls-prep.sh}, infra/website/RUNBOOK.md, + 2 deploy-ledger entries). Uncommitted: requirements.txt (root,
lane-blocked). On-box (repo->S3->box, Rule 12): /usr/local/bin/ses-sendmail, lsphp82 zz-ses-sendmail.ini,
certbot + renewal hook. WP DB (wp-cli): wp_mail_smtp option + GF Contact form notification recipient.
Memory: project_nfra_website_phase2_ses_smtp_and_gates.md.

## MCP traffic
~4 significant: ACK [STOP] vendor prohibition -> COO; NFRA_WEBSITE W2 status (SMTP wired+exercised,
ledgers closed, gates) -> COO. Inbound: CTO ANDREW-DIRECT /log-now (this log).

## Blockers
None BLOCKED. Open items are Andrew/external-gated, not blocks:
- opalcapital.com DKIM CNAMEs at GoDaddy -- Andrew lacks the sign-in; CFO AJ Graff has it. Draft reply
  (Patricia CC AJ) staged in Outlook. Sender graduates + form flips to no-reply@opalcapital.com on verify.
- W3 apex-A cutover = Andrew's DNS-gated go-live call; old host untouched (rollback point).
- mike@/patricia@ SES opt-in = recipient clicks (their inboxes).

## Current State (handoff surface)
- **Contact form email LIVE to Opal.** andrew@opalinvest.com receives submissions now via SES
  (noreply@opalinvest.dev, DKIM-clean), through the ses-sendmail shim (instance role, no stored secret).
  mike@ delivers once he clicks his SES opt-in.
- **Box:** i-0152e3fe2599fa630, EIP 18.208.18.213, OLS/LSPHP82/MariaDB; SES grant applied+exercised;
  DLM snapshots ENABLED again; certbot installed + HTTP-01 webroot verified.
- **opalcapital.com** SES domain identity created, DKIM PENDING (3 CNAMEs to add at GoDaddy).
- **requirements.txt** at repo root (working tree, uncommitted), emailed to andrew.opalinvest@gmail.com.
- **Patricia reply** = Outlook DRAFT (to Patricia, CC AJ Graff), NOT sent.
- No vendor API calls; no 49F/bd/Schwab touch (sovereign). SES sends only to internal Opal addresses +
  Andrew-direct mike/patricia opt-ins; requirements email to Andrew's own gmail (Andrew-direct).

## Next Steps
- **[Andrew / CFO AJ Graff]** add the 3 opalcapital.com DKIM CNAMEs at GoDaddy (records in the Outlook
  draft); then W3 apex-A cutover (his call).
- **[0.7.0_AE_CloudOps~A]** on DKIM verify: flip wp-mail-smtp from_email + iam.tf FromAddress condition to
  no-reply@opalcapital.com; route CTO/COO the Rule-23 graduation note (opalcapital.com becomes DKIM-clean).
  At W3: certbot certonly --webroot (documented) + wire OLS wordpressssl listener to the LE cert + reload.
- **[Andrew]** if he wants requirements.txt committed to the repo (root file, needs --force past owned-paths)
  or delivered as a true attachment (needs his gmail SES-verified).
