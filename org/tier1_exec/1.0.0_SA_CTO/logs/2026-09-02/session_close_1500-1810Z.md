# CTO~Z session close -- 2026-09-02T15:00Z -> 18:10Z

**serial:** 1.0.0_SA_CTO~Z (site-Z lane; base folder, lane named here per XXX.md)
**archetype:** MIXED
**secondary_archetypes:** DEPLOY (OTP TTL, backend + portal-v2.1.176), DIAGNOSE (where the OTP minutes
go; the attack surface), EXPLORE (security assessment), SCRIBE (postmortem, assessment, PRD),
COORDINATE (3 integrator legs, register mint via MSTR, decomp to COO), RECORD (Andrew-direct x6, verbatim)

This is the HANDOFF for the afternoon. Substance sits in two delta logs and four documents; this
file consolidates the end state for a reader with zero context and points at each record.

  delta 1    logs/2026-09-02/ctoZ_otp_ttl_30min_stephen_off_1520-1645Z.md                      @ad12b41cc8
  delta 2    logs/2026-09-02/ctoZ_security_assessment_to_D12_PLATFORM_FORTIFY_prd_1650-1755Z.md @e837eb4da1
  postmortem docs/briefs/OTP_EXPIRY_POSTMORTEM_20260902.md                                     @b3559b0c82
  assessment docs/security/PLATFORM_ATTACK_SURFACE_ASSESSMENT_20260902.md                     @a9a47f65a1
  PRD        docs/architecture/D12_PLATFORM_FORTIFY_PRD.md                                     @eba7e15054 -> @7a51451d69
  register   org/projects/D12_PLATFORM_FORTIFY.json + DIRECTIVES.yaml D12 member (0.0.0_AB_MSTR~Z) @6be6a0cc41 -> @491af5ee58

## Andrew-direct this window (each recorded verbatim in the record named; each broadcast same turn)

1. OTP expires before a client's mail server surfaces it: push expiry to 30 min; investigate our-side
   levers. (15:2xZ; delta 1)
2. Turn Stephen (Cottonwood) MFA off "for now"; ping when false; then proceed. (15:3xZ; delta 1)
3. "Do we know who those other humans are based on id?" -- user-error hypothesis. (16:3xZ; delta 1)
4. Write a postmortem in docs/briefs/ unless a dedicated folder exists. (16:4xZ; b3559b0c82)
5. Security fortification: analyze public endpoints and defences, login WAF + tracking, post-login
   protection, opal-users-v2 + opal-partner-* protection, Lambda@Edge JWT/firmId, and the website +
   opal-gateway servers. Then: "We do not use Cognito, never have." Then: "/endpoint --forward this
   brief ... actionable PRD ... attached on the D12 Directive." (16:5xZ-17:4xZ; delta 2)
6. "agreed onall of these, plus ..." -- FWD-1..13 RATIFIED; FWD-14..18 ADDED (WAF-triggered email to
   andrew@opalinvest.com, triggerable auto-block, case files in an opal-data-security bucket, a DDB
   opal-suspicious-addresses table, means to unblock, block-on-trigger preferred over human
   remediation); asked for the CTO's assessment of the framework. (17:5xZ; 7a51451d69 section 7)

## Commits this window, author 1.0.0_SA_CTO~Z -- 9, ALL ON ORIGIN (is-ancestor of origin/SITEZ, read 18:0xZ)

  f4659653e8  auth-handler: CHALLENGE_TTL_SEC 600->1800; ttlSec on login response; mfa_code_expired event
              (AE lane, audited GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL; both AE seats down; the
              two BLOCK rows precede the OVERRIDE row in org/git-author-override-audit.log)
  39f4a058a3  lambda-source-map artifact update [skip ci] (same override)
  60aed6f3a3  portal pointer -> 30ca034b; PROD 6cb3d0f654 / portal-v2.1.176
  ad12b41cc8  delta log 1
  b3559b0c82  OTP expiry postmortem
  a9a47f65a1  attack-surface assessment (read-only; nothing built)
  eba7e15054  D12_PLATFORM_FORTIFY PRD (13 FWD outcomes)
  e837eb4da1  delta log 2
  7a51451d69  PRD: FWD-1..13 RATIFIED, FWD-14..18 ADDED, section 7 architecture

  Portal repo: DEV 30ca034b -> PROD 6cb3d0f654 (merge author 1.0.0_SA_CTO~Z via GIT_AUTHOR_*; parity 0
  bytes; 1 commit / 3 files, no passengers -- re-derived by the integrator before publishing). Every
  push this window was 0.0.0_AB_MSTR~Z's leg; NO override was spent on any push. Deploy ledger
  otp-ttl-30min-and-expiry-event: L1-L6 CLOSED.

## MCP traffic

9 frames from 0.0.0_AB_MSTR~Z received and read this window (19352, 19359, 19361, 19363, 19370,
19374, 19379, 19383, 19387): five push confirmations with ls-remote oracles, the register mint
(19379), the ratification record (19387). Two of them carry facts this log must not lose:
  - 19387: my 19384 named `prds[0].vintage`; in the row prds[0] is the BRIEF and prds[1] the PRD.
    0.0.0_AB_MSTR~Z put the vintage on the PRD entry -- the intended target -- and said so. My index
    was wrong; the outcome is right.
  - 19387: the register row now carries a THIRD guard on FWD-14 added by the register owner: a
    persistent block must never fire on an ALLOW-listed partner egress; and my three section-7
    design constraints are recorded as INHERITED atoms for the decomp.
  - 19352: the two remaining GATE 5 suite failures (`git -c pull.rebase=true pull`, generic flag
    before -c) are a LIVE NEVER#7 evasion on every device, {OBSERVATION, ARMED}, owner = the gate's
    option-consumer work. Not chased.
  - 19370: portal gitlink reads ` M portal` after every promote because of ONE untracked .pyc under
    portal/.frontend-dev/runners/__pycache__/; portal/.gitignore has no __pycache__ entry. One-line
    portal-repo fix; DE lane.
Sent: ~14 frames (leg requests naming each head, the register mint request, the decomp hand-off to
2.0.0_SA_COO~Z x2, the ratification record request, surprise lines). None outstanding.

## Compiler Tools (cited from context; nothing re-run for this table)

| tool | target | result | note |
|---|---|---|---|
| comp-read | mfa.ts, auth.ts, types.ts, email.ts, sms.ts, index.ts, throttle.ts, 005_backfill, safe-commit, comp-schedule, edge index.mjs, portal-authorizer, server.py, opal-partners-data, lambdas.tf, build-nodejs-lambda | PASS | --enumerate for carriers of 600 (22 hits, all derived from the constant) |
| comp-find | TTL carriers, SendEmail, requireMFA, SP-1, Cognito (25 SURFACED / 0 DEF / 0 TF), opal-users readers, X-Origin-Verify consumers (1: the edge only), ALLOWED_PATHS | PASS | denominators printed each run |
| comp-which x2 / comp-routes behaviors / comp-iam roles + resource-sweep | portal serving path (28 behaviors, DESIRED plane); IAM DESIRED plane with 24 unattached + 2 unparsed Denies disclosed | PASS | three raw apigateway reads carried rail-checked markers (per-route authorizer state is outside comp-routes) |
| tsc (auth-handler) / bun run typecheck (portal) | rc=0 / rc=0 after 4 iterations (void return type; CRLF anchors; MfaChallengeResponse; send-capture reverted) | PASS | |
| build-nodejs-lambda.sh | S3 e0PKUos3, sha dYZiZ7Rz (read back via head-object) | PASS | failed first from a /cygdrive cwd: to_native_path handles /c/ only; misreports as 'No source_dir' |
| terraform plan / safe-apply / plan -detailed-exitcode | 0/1/0 code-only; tagauthz PASS, tombstone CLEAN; 0-diff after | PASS | terraform on PATH (v1.15.8); no .tools/terraform.exe on site Z |
| aws (operational + rail-checked inspection) | logs Insights x2, sesv2, dynamodb x8, lambda, s3api, wafv2, cloudfront, apigateway/v2, kms, secretsmanager, ec2, elbv2, guardduty, cloudtrail, securityhub, configservice | PASS | Stephen's send: 335 ms Lambda START->END |
| deploy_ledger.py | open / close-leg x6 / close | PASS | |
| record-terraform-deploy.sh | FAILED twice on site Z (cp1252 decode; then unquoted expansion on the path space at :511); wrote nothing | FAIL | _last_deploy_recorded STALE for this deploy; surfaced to the AE lane |
| gh run list/view by headSha; tag peel; served-bundle read | CI 33655348376 success 1/1; portal-v2.1.176 == PROD; 'expires in 10 minutes' 0, ttlSec/60 render present, control 1 | PASS | |
| directives-check --code D12 (0.0.0_AB_MSTR~Z) + my direct row read | members 3 [active], ghosts 0 -- two instruments, same answer | PASS | |

What worked: comp-read --enumerate settled "every 600 is derived" in one call; the served-bundle
read with a positive control; the integrator re-deriving every leg before publishing.
What failed: heredoc-carried python mangled backslashes twice (asserts fired, nothing written;
Write-tool scripts used instead) -- and a third time at this close, a parse error before anything
ran (the log was then written by the Write tool). record-terraform-deploy.sh on this box's path.
Gap found: expired OTP attempts were the one MFA outcome with no log line (closed by
mfa_code_expired); X-Origin-Verify is a constant checked by nobody; the portfolio REST API has zero
authorizers; 25 source files claim Cognito, which has never existed here.

## Blockers

None at this seat. Nothing BLOCKED; every open item is owned elsewhere (Next Steps).

## Current State (zero-context handoff)

- **OTP:** CHALLENGE_TTL_SEC = 1800 LIVE since 16:23:14Z (deployed CodeSha256 dYZiZ7Rz == built,
  0-diff plan after); login response carries ttlSec; portal-v2.1.176 renders it (served bundle
  index-b1Com0o8.js). New event mfa_code_expired {account_hash, late_by_sec} -- the discriminator
  for user-error vs gateway-delay; n=1 external so far (stephen), UNRESOLVED. Our side of that send
  was 335 ms; SES plane clean (DKIM/SPF aligned, suppression list empty, no config set = SES->MX
  latency unmeasurable). Levers 3 (strip remote image/link from the OTP mail; the code is already in
  the subject) and 4 (SES config set for delivery events, monitor-class) at Andrew; recommendation:
  hold until a second external late_by_sec.
- **MFA:** 31 of 48 PROFILE accounts email-MFA ON; stephen.shipley@cottonwoodmail.com
  mfaEnabled=false (Andrew "for now"; channel left 'email' so re-enable is one field). Excluded set
  unchanged (13 test/demo/fixture, 2 service, 1 disabled).
- **D12_PLATFORM_FORTIFY:** REGISTERED (0.0.0_AB_MSTR~Z @6be6a0cc41, row updated @491af5ee58), D12
  member [active], ghosts 0. PRD @7a51451d69: FWD-1..13 RATIFIED; FWD-14..18 ADDED; section 7 = CTO
  architecture (table is truth, WAF IP set derived via DynamoDB Stream; tiered block with expiry +
  partner-egress ALLOW list; one email per incident + daily digest; FWD-2 origin secret FIRST or the
  sentinel is blind to the raw execute-api endpoints). Moratorium exceptions by Andrew's word:
  FWD-4/5/6/12 + FWD-14/15; nothing beyond, no other recipient/channel/cadence. Rule 27 stage 3
  (atom-decomp) is 2.0.0_SA_COO~Z's; that seat is DOWN; hand-off queued (19376, 19385) with
  sequencing input marked as input, not ruling.
- **Assessment top findings, none built:** F1 HIGH REST API f61h681z9g zero authorizers, 20
  resources incl. writes open at the raw endpoint; F2 nine /v1/* routes public + WAF-less at the raw
  endpoint, keyword-intelligence = OpenAI spend; F3 no GuardDuty/SecHub/Config/WAF logging/CF+ALB
  logs/login alarms; F4 throttle fail-open + IP-blind; F5 CF WAF no managed groups; F6 table posture
  uneven + legacy opal-users still granted; F7 RS256 keypair 2026-04-06 unrotated. Gateway: layered
  right (Entra OIDC at ALB, per-protocol bearers, WAF with IP-reputation enforced) -- graduate COUNT
  groups, ALB logs, rotate static bearers. Website: well-kept WordPress box, no request-level WAF.
  The assessment is on the shared remote (private repo) -- content went to Andrew first, but ACCESS
  is both fabrics; 0.0.0_AB_MSTR~Z credential-scanned it before pushing (6 shapes, all zero,
  positive control 5).
- **Site-Z script defects surfaced (AE lane):** build-nodejs-lambda.sh to_native_path (/c/ only,
  misreports the throw as a missing map entry); record-terraform-deploy.sh (cp1252 decode; space
  in path at :511). Workaround recorded: run the build from a /c/ cwd.
- **Fabric:** zero crons; watcher task ba9ps95uv, parent-tied pid 49253; live seats 0.0.0_AB_MSTR~Z +
  this seat; 2.0.0_SA_COO~Z / 3.0.0_SA_CVO~Z / 0.7.0_AE_CloudOps~Z / 0.4.0_DE_ClientPlatform~Z down
  all afternoon (their mail QUEUED). origin/SITEZ 491af5ee58 before this log. Portal main tree on
  DEV at 30ca034b; the ` M portal` status is the .pyc above, not a pointer move.

## Next Steps

- **[2.0.0_SA_COO~Z]** atom-decomp of D12_PLATFORM_FORTIFY_PRD.md (19376 + 19385; read section 7
  and the register row's `blocking` field first): FWD-2 first atom; FWD-13 edge choice as a card to
  Andrew; the three section-7 constraints + the partner-egress guard as inherited atoms.
- **[Andrew]** OTP levers 3/4; Stephen back ON when satisfied. (D12 FORTIFY endpoint already
  ratified -- nothing open there.)
- **[0.4.0_DE_ClientPlatform~Z]** stale-bundle caveat now covers the OTP form text; SF-2 part 2/2;
  `__pycache__/` line in portal/.gitignore (the recurring dirty-gitlink read).
- **[0.7.0_AE_CloudOps~Z]** the two site-Z script defects; _last_deploy_recorded stale for
  otp-ttl-30min; F1 remediation lands in infra/aws once decomposed -- not before.
- **[3.0.0_SA_CVO~Z]** the `git -c pull.rebase=true pull` NEVER#7 evasion (2 red arms in
  test_never_rules_gate.sh) -- ARMED observation with no seat holding it; needs an owner.
- **[0.0.0_AB_MSTR~Z]** push of this close log.
