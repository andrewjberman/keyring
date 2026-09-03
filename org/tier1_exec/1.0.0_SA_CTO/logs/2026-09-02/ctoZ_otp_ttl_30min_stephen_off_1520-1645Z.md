# CTO~Z delta log -- OTP expiry to 30 min, expiry now logged, Stephen MFA off, delivery levers measured

**serial:** 1.0.0_SA_CTO~Z   **window:** 2026-09-02T15:20Z -> 16:45Z   **archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE (where the OTP minutes go), IMPLEMENT (TTL + ttlSec + expiry event +
portal render), VALIDATE (served-plane + function-plane reads), RECORD (Andrew-direct x2, verbatim)

## Andrew-direct, VERBATIM
1. "We need to examine two things, 1.) A client is complaining that the email OTP takes so long to get
   to them that it expires before their mail server surfaces it. I think we need to push token expiry
   to 30 minutes. 2.) Is there anything on our side that could be done to diminish time to receipt of
   OTP? It could be out of our hands and an issue with their IT/mail-server policy, but it is worth
   investigating if there is any lever we can pull to that end"
2. "also let's turn off MFA for stephen from Cottonwood for now, so he can have access while we work
   this out." / "ping me when stephen mfa is rendered "false" that comes first" / "then proceed with
   the rest"
3. "Do we know who those other humans are based on id? I suspect that if they had no issue and stephen
   was the only one with a problem, this is user error, not a systematic problem that we need to
   account for beyond our TTL expanded life."

## DONE
- **Stephen OFF first:** USER#stephen.shipley@cottonwoodmail.com mfaEnabled=false (conditional
  update-item; strongly-consistent get-item read back False; channel left 'email'). 31 of 48 ON.
- **Measured (Logs Insights, auth-handler, 14 d, 103 mfa_* events, 7 accounts, hash=sha256(email)):**
  send->accept for every accepted HUMAN code: andrew@ 36 s; yang@ 109 s, 35 s; manav@ 140 s -- ALL
  INTERNAL @opalinvest.com. stephen (bee2228b3c38): challenge 15:12:57Z, code sent 15:13:32Z, never
  accepted -- the ONLY external/partner attempt so far (partner MFA enabled 14:4xZ). That send's
  Lambda invocation: 335 ms START->END, SES accept inside. Expired attempts were NOT logged, so "never
  tried" vs "tried too late" was indistinguishable for his attempt.
  SES plane: production access, DKIM SUCCESS, MAIL FROM mail.opalinvest.dev SUCCESS, SPF
  include:amazonses.com, DMARC p=none, suppression list EMPTY, no config set on the OTP send (SES->MX
  latency unmeasurable). OTP mail: code in SUBJECT; HTML body with 1 remote image + 1 link + Text part.
- **Backend f4659653e8** (AE lane, audited GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL; both AE seats
  down): CHALLENGE_TTL_SEC 600->1800 (row expiresAt/ttl, resend window, email copy all derive);
  ttlSec on both login returns + MfaChallengeResponse; NEW mfa_code_expired {account_hash,
  late_by_sec}. + 39f4a058a3 source-map artifact update. Deployed via build-nodejs-lambda ->
  s3 e0PKUos3 sha dYZiZ7Rz -> plan 1 change code-only -> safe-apply 16:23:20Z (tagauthz PASS,
  tombstone CLEAN) -> get-function-configuration CodeSha256 == built, Active/Successful -> 0-diff.
- **Portal 30ca034b -> PROD 6cb3d0f654 (portal-v2.1.176):** MfaChallenge.ttlSec; login() maps it;
  form renders round(ttlSec/60), omits the sentence if absent (never NaN). Parity 0 bytes, 1 commit /
  3 files, author set via GIT_AUTHOR_* (git merge has no --author). CI 33655348376 success 1/1;
  tag peeled == PROD. SERVED index-b1Com0o8.js: literal 'expires in 10 minutes' 0, render present,
  control 1. Pointer bump 60aed6f3a3. All pushes 0.0.0_AB_MSTR~Z's; no override on any push.
- Ledger otp-ttl-30min-and-expiry-event: L1-L6 CLOSED, entry CLOSED.

## Findings surfaced, not chased (AE lane)
- build-nodejs-lambda.sh to_native_path: /c/ only, not /cygdrive/c/; the throw is reported as
  "No source_dir found" while the map is correct. Workaround: /c/ cwd.
- record-terraform-deploy.sh: cp1252 decode of the UTF-8 map, then `/c/Users/Opal: Is a directory`
  (unquoted expansion on the path space). Wrote nothing; _last_deploy_recorded is STALE for this deploy.

## Compiler Tools
comp-find (TTL carriers, SES send, requireMFA), comp-read --enumerate (mfa.ts 22 TTL hits all
derived; email.ts; types.ts), tsc (auth-handler) rc=0, bun run typecheck rc=0 after 3 iterations
(void return type, CRLF anchors, MfaChallengeResponse), aws (logs start/get-query, sesv2, dynamodb
get/update-item, lambda get-function-configuration, s3api head-object), terraform plan/safe-apply,
deploy_ledger.py open/close-leg x6/close, gh run list/view by headSha. No commit-gate coverage on .ts.

## Current State
- OTP TTL 30 min LIVE for every challenge issued after 16:23:14Z; expiry attempts now logged with
  late_by_sec. Portal renders the server value; a cached pre-promote bundle shows its own old text
  until hard-refresh.
- 31 of 48 email-MFA (stephen OFF, Andrew's "for now"). 
- Push state: 60aed6f3a3 LOCAL (named to MSTR~Z); f4659653e8, 39f4a058a3 ON ORIGIN (MSTR reads).

## Next Steps
- **[Andrew]** whether Stephen goes back ON; lever 3 (strip remote image/link from the OTP mail);
  lever 4 (SES configuration set for delivery events -- monitor-class). Whether n=1 external is
  user error is NOT established; mfa_code_expired's late_by_sec will discriminate next time.
- **[0.0.0_AB_MSTR~Z]** push 60aed6f3a3 + this log.
- **[0.7.0_AE_CloudOps~Z]** the two script defects; _last_deploy_recorded stale.
- **[0.4.0_DE_ClientPlatform~Z]** stale-bundle caveat now applies to the OTP form text too.
