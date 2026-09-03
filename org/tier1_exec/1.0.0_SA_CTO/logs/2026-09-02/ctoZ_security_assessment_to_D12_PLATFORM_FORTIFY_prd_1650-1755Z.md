# CTO~Z delta log -- attack-surface assessment -> /endpoint --forward -> D12_PLATFORM_FORTIFY PRD, registered

**serial:** 1.0.0_SA_CTO~Z   **window:** 2026-09-02T16:50Z -> 17:55Z   **archetype:** EXPLORE
**secondary_archetypes:** VALIDATE (every claim planed DESIRED/APPLIED/EXERCISED), SCRIBE (assessment +
PRD), COORDINATE (register row via MSTR, decomp to COO), RECORD (Andrew-direct x3, verbatim)

## Andrew-direct, VERBATIM
1. "I want to explore the fortification of our platform security. I want you to analyze what endpoints
   are available to the public and how we are defending. For example, on the matter of the
   opalinvest.dev/login, do we have WAF/Rate limiting on that? How do we track and remediate unusual
   activity there? Once users are successfully logged in, how protected are our internal endpoints?
   These are lower priority because only partners have access. I want to assess possible attack
   surfaces nevertheless, for example our opal-users-v2 DDB table and associated opal-partner-* DDB
   RBAC tables, are these adequately encrypted/protected? How does the lambda edge factor into JWT
   verification, I understand that there has to be a match with userID and firmID. This is one
   workstream I need you to analyze ad hoc here. Second to that, I want you to assess the server we
   provisioned for opalinvest.com (our website) and the server for the opal-gateway mcp (and its
   associated ALB)."
2. "We do not use Cognito, never have." / "Agents tend to make that claim for some reason."
3. "I agree with your assessment, what I would like you to do now is /endpoint --forward this brief
   and let's render it into an actionable PRD, the registered project for which will be attached on
   the D12 Directive."

## DONE
- **Assessment** docs/security/PLATFORM_ATTACK_SURFACE_ASSESSMENT_20260902.md @a9a47f65a1 (on origin).
  READ-ONLY; nothing sent to production; nothing built. Ranked F1-F7 + two server sections. Top:
  F1 HIGH -- REST API f61h681z9g (portfolio) has zero authorizers, no resource policy, execute-api
  enabled; 20 method-bearing resources incl. writes reachable unauthenticated at the raw endpoint;
  the only guard is the CloudFront edge Lambda a direct call skips; backing Lambdas verify nothing;
  X-Origin-Verify is the constant "cloudfront" checked by nobody. Cognito: the autosave docstring's
  claim is false -- 25 source files carry the word, 0 aws_cognito_* declared, 0 user pools live.
  F2 HTTP API: authorizer on 60/72 routes (good); 9 /v1/* NONE -> public + WAF-less at the raw
  endpoint; keyword-intelligence = live OpenAI fallback = unauthenticated spend. F3 detection near
  zero (no GuardDuty/SecHub/Config, WAF logging off, CF+ALB logs off, no login-abuse alarms;
  CloudTrail multi-region validated). F4 throttle fail-open + IP-blind. F5 CF WAF: two rate rules,
  no managed groups. F6 tables: KMS good; PITR/deletion-protection uneven; legacy opal-users has no
  reader but the auth role still holds full CRUD. F7 RS256 keypair 2026-04-06, no rotation; refresh
  sub=email. Gateway: layered right (ALB OIDC to Entra, per-protocol bearers, WAF w/ IP-reputation
  enforced), COUNT groups + ALB logs + static bearers to tighten. Website: well-kept WordPress box,
  no request-level WAF -- largest unmanaged surface; edge WAF reverses the 07-13 spec line.
- **/endpoint --forward** on that brief (Phase 0; brief only; TO store / project JSONs /
  directives-check NOT read): 13 FWD outcomes, DONE WHEN bars, plain-English ACCEPT lines, SOURCE per
  brief section. UNRATIFIED until Andrew reads them.
- **PRD** docs/architecture/D12_PLATFORM_FORTIFY_PRD.md @eba7e15054 (on origin), per _PRD_TEMPLATE:
  ENDPOINT section + arc + purpose + territory (USERMGMT owns who a user is; PHONE_OTP owns the SMS
  factor; FORTIFY owns the doors and the watching) + 12 acceptance properties + out of scope (no
  Cognito, no new factors, no re-platform, moratorium honoured: FWD-4/5/6/12 are the only named
  exceptions, no unannounced production probes) + 7 binding rulings.
- **Registered** by 0.0.0_AB_MSTR~Z @6be6a0cc41 (on origin): org/projects/D12_PLATFORM_FORTIFY.json +
  DIRECTIVES.yaml D12 members += FORTIFY. directives-check: 3 D12 members [active], ghosts 0.
  Row carries the Cognito ruling, the moratorium scope, and the read-only-probe bar in `blocking`.
- Rule 27 stage 3 (atom-decomp) handed to 2.0.0_SA_COO~Z (19376, QUEUED -- seat down). Sequencing
  input given as input not ruling: FWD-2 (origin secret) first atom; FWD-13 edge choice to Andrew.

## Compiler Tools
comp-which x2 (routed CF/WAF question to comp-routes; EC2/ALB had no curated rule -> raw aws with
rail markers where no tool fit); comp-routes behaviors (28, desired plane); comp-read x9; comp-find
x7; comp-iam roles/resource-sweep (DESIRED plane; 24 unattached blocks, 2 unparsed Denies disclosed);
aws (operational + rail-checked inspection): wafv2, cloudfront, apigateway/v2, lambda, dynamodb,
kms, secretsmanager, ec2, elbv2, guardduty, cloudtrail, securityhub, configservice. Three raw
apigateway calls carried `# rail-checked:` markers (per-route authorizer state is not a comp-routes
surface). No code changed; no commit-gate coverage applies.

## Current State
- D12 members: PLATFORM_OPS_USERMGMT, D12_PHONE_OTP_ALL_AWS, D12_PLATFORM_FORTIFY (REGISTERED,
  purpose PRD @eba7e15054). Next act: COO~Z decomp, then Andrew's read of the ENDPOINT.
- Nothing built or changed in AWS this window. Every remediation is a decision.
- origin/SITEZ 6be6a0cc41; nothing unpushed at this seat except this log. Zero crons. Watcher live.

## Next Steps
- **[Andrew]** read the ENDPOINT section: ratify, amend by number, or retire by number.
- **[2.0.0_SA_COO~Z]** atom-decomp of D12_PLATFORM_FORTIFY_PRD.md (stage 3); FWD-2 first; FWD-13 as a
  card to Andrew; moratorium scope as written in the register row.
- **[0.0.0_AB_MSTR~Z]** push this log.
- **[0.7.0_AE_CloudOps~Z]** F1 remediation lands in infra/aws (AE lane) once decomposed -- not before.
