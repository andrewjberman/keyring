# 0.7.0_AE_CloudOps~A -- NFRA_WEBSITE W2 SMTP: the "internal != SES-verified" trap + admin_email finding

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE
**serial:** 0.7.0_AE_CloudOps~A | **date:** 2026-07-09 | **window:** ~1950Z -> ~2020Z | third log of session

## Summary
W1 was ACCEPTED + TO-1 closed (`c602dde44`) on COO's independent live re-verify; COO GO'd W2. This log
covers the W2 SMTP wave, which a grounding pass turned from a routine config task into the decision. Net:
exercised the SES path both ways, established that no form emails an external submitter, then found that
BOTH live-form recipients are SES-UNVERIFIED -- so the naive "no external submitter -> sandbox is fine"
conclusion was WRONG, and a SES-in-sandbox cutover would have silently dropped the only contact form's
notifications. COO ruled with the finding: keep the existing external SMTP; do not cut over to SES until
production access + verified recipients; W3 apex-flip is now HARD-gated on proving email delivery
end-to-end. Also surfaced a separate finding (`admin_email = mike@hirst.digital`).

## The W2 SMTP finding, framed correctly
"Internal recipient" was the PROXY; "SES-verified recipient" is the PROPERTY. They are not the same, and
assuming they were would have shipped a silent failure to a customer-facing form.
- SES account is in the SANDBOX (delivers only to verified identities).
- The migrated site's only live form ("Contact") has 2 notifications, both to INTERNAL literals:
  `{admin_email}` and `info@opalinvest.com`. No external-submitter confirmation. On that axis, "fine."
- BUT: `opalinvest.com` is NOT an SES domain identity; `info@opalinvest.com` is NOT verified; and
  `admin_email` resolves to `mike@hirst.digital`, also unverified. So in sandbox, an SES cutover
  `MessageRejected`s BOTH notifications -> a contact submission notifies no one, silently, while the site
  looks healthy.
- The current `wp-mail-smtp` is generic SMTP from `no-reply@em.opalinvest.com` (an ESP subdomain carried
  from the old host) and delivers to those recipients TODAY.

This is the session's recurring shape (COO called it the 15th instance today): an instrument/decision
keyed on a proxy that is decoupled from the property it stands for -- same class as the WP least-priv
regex I found earlier (a control that ran, reported success, enforced nothing).

## Grounding -- exercised, not assumed (Rule 22a)
grounding:
  desired:  CLAUDE.md Rule 23 (opalinvest.dev = the clean sender); wp-mail-smtp mailer config on-box.
  applied:  live SES us-east-1 -- opalinvest.dev verification=Success + DKIM=Success; opalcapital.com NOT
            an identity; opalinvest.com NOT a domain identity; info@opalinvest.com NOT verified; SES
            account ProductionAccessEnabled=false (sandbox); instance role has zero ses:*.
  exercised: SES SUCCESS = `aws ses send-email` noreply@opalinvest.dev -> success@simulator.amazonses.com
            -> MessageId returned. SES FAILURE (sandbox limit) = -> an unverified external address ->
            `MessageRejected: Email address is not verified`. GF routing = `GFAPI::get_forms()` per-
            notification toType/to (config only, no entries/PII): Contact form, both notifications
            toType=email to internal literals; zero submitter-field routing.

## admin_email = mike@hirst.digital -- ESTABLISHED FACT, UNDETERMINED INTENT (COO framing, verbatim)
The WordPress admin address -- which receives every admin notification, password reset, and contact-form
submission -- is the external developer's personal domain (`hirst.digital`), NOT an Opal address. This is
NOT an SES problem: it is a question of who receives Opal's inbound contact-form traffic and who can
trigger a WP password reset. It may be entirely intended for the migration window. It is Andrew's call,
not mine -- COO is surfacing it to Andrew. I did NOT change it. Recorded here as directed: established
fact, undetermined intent.

## COO ruling (recorded in the runbook, `3b7dc4421`)
1. KEEP external SMTP; do NOT point wp-mail-smtp at SES until production access AND recipients verified.
2. FILE the SES production-access support case -- I drafted it (`infra/website/SES_PRODUCTION_ACCESS_CASE_DRAFT.md`,
   `7d31e966d`); routed to COO; Andrew approves BEFORE submission; NOT submitted on agent authority.
3. NEW HARD W3 GATE (runbook Section 5, step 2a): the apex-A cutover does NOT proceed until the Contact
   form's notification path is proven end-to-end to a REAL recipient on the REAL mail path. Old host
   (72.167.58.121) stays the rollback point.

## SES IAM grant -- DEFERRED to cutover (decision recorded)
The scoped `ses:SendEmail` grant on the instance role would sit unused until the (post-production-access)
wp-mail-smtp cutover; bundling grant + plugin switch at cutover is one clean deploy-ledger and avoids an
applied-but-unexercised capability. Deferred by default (COO can pull it forward if they want it
proven-and-ready ahead).

## Backtick safety (COO safety item #1) -- self-checked + adopted -F
Backticks in `safe-commit -m "..."` execute as command substitution in the caller's shell (silent
audit corruption + arbitrary execution with the committer's creds; the check can't live inside
safe-commit because substitution already happened). I committed 8x this session with backticks; git-log'd
every message -> ALL INTACT (I had escaped them, `\`` -> literal, so nothing fired). Adopted `-F <file>`
as the default going forward (this log + `3b7dc4421` used it).

## Compiler Tools
| Tool | Situation | Result | Note |
|---|---|---|---|
| rail-checked aws (ses/iam) | SES identity/DKIM/sandbox + instance-role ses check | used | no comp-tool models SES state or a standalone/instance-role SES grant; Rule 22a mandates live for a fresh SMTP-provider decision -> `# rail-checked:` markers |
| SSM RunCommand (wp-cli/GFAPI/mysql) | GF notification routing + wp-mail-smtp mailer + admin_email | used | config-routing only, no form entries/PII; the SSM-reach is itself the exercise |
| aws ses send-email | exercise SUCCESS (simulator) + FAILURE (unverified) | used | the behavioral proof COO required -- a MessageRejected is an observation, "sandbox should be fine" is an assumption |

**What worked:** the live SES send exercises + the GFAPI routing read were the authoritative evidence;
the failure exercise is what caught the trap. **What failed:** nothing tool-side. **Gap (same as W1):** no
comp-tool covers SES state, EC2-on-box app config (wp-mail-smtp, GF), or standalone/instance-role SES
grants -- all rode raw aws/SSM with markers (logged).

## MCP traffic
COO x4 this window: W2 SMTP both-decisions ruling (noreply@opalinvest.dev + file-the-case-via-gate) ->
ACK + plan; my SMTP results + the unverified-recipient finding + case draft; COO's finding-FLIPS ruling
(keep external SMTP, W3 email-gate, admin_email-to-Andrew, backtick safety) -> ACK + recorded.

## Blockers
None self-owned. NFRA_WEBSITE is at its real external gates: Andrew (DNS cutover + SES production-access
approval), TWLC (content migration done), CVO (staging-verify). W2 SMTP driven to its gate (external SMTP
kept; SES cutover + IAM grant deferred to post-production-access). layer2 MS-token L4 held on Andrew's
sign-in.

## Next Steps
- **[Andrew via COO]** approve + submit the SES production-access case; rule on `admin_email=mike@hirst.digital`.
- **[0.7.0_AE_CloudOps~A]** at cutover (post-production-access + verified recipients): provision the scoped
  ses:SendEmail grant (TF), switch wp-mail-smtp to SES/noreply@opalinvest.dev, EXERCISE end-to-end
  delivery; certbot TLS at W3 DNS; own deploy-ledger for each. Prove the Contact-form email path E2E
  before the W3 apex flip (the hard gate).
- **[TWLC dev]** finish the Bricks content migration -> triggers CVO staging-verify.
