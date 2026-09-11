# MFA Silent Send Refusal -- the login that reported "sent" and sent nothing

| | |
|---|---|
| **Date** | 2026-09-11 |
| **Author** | 0.7.0_AE_CloudOps~A |
| **Trigger** | Yang Liu -> Andrew, Teams 20:34Z: *"the MFA seems not work today for the dashboard"*; Andrew-direct: *"he does not receive OTP after multiple attempts ... can we look into sign in attempts?"* |
| **Affected** | yang@opalinvest.com (`usr_91abace15084`, firm `opal-capital`) -- one user, one session |
| **Status** | DIAGNOSED, NOT REMEDIATED. No code change authorized or made. User-side recovery is a fresh login. |
| **Surface owners** | `0.7.0_AE_CloudOps` (auth-handler), `0.4.0_DE_ClientPlatform` (portal auth UI) |
| **Sibling** | `docs/briefs/OTP_EXPIRY_POSTMORTEM_20260902.md` -- same subsystem, 9 days earlier, and see "The part that should sting" |

## The one-sentence finding

His multi-factor authentication (MFA) challenge expired unused, and `POST /auth/mfa/send` answers
`200 {success:true}` whether or not it sent anything -- so a recoverable thirty-second mistake
presented to the user as a broken product, and the button he kept pressing was the one button that
could never fix it.

## Timeline (UTC, 2026-09-11)

```
18:24:30  POST /auth/login from 173.79.153.38                      [WAF edge log]
18:24:34  mfa_challenge_issued, account_hash 6df1cf2e..., email    [auth-handler log]
          -> password CORRECT. Login deliberately sends no code (W3 Act B, 2026-09-01).
18:54:34  challenge expires (CHALLENGE_TTL_SEC = 1800)             [derived]
          ---- 37 minutes. No HTTP request of any kind from his IP. ----
19:02:29  POST /auth/mfa/send from 173.79.153.38                   [WAF edge log]
19:02:30  mfa_send_refused -- no code minted, no mail              [auth-handler log]
          -> client still receives 200 {success:true}
19:16:53  POST /auth/mfa/send from 173.79.153.38                   [WAF edge log]
19:16:53  mfa_send_refused -- identical outcome                    [auth-handler log]
20:34:04  Yang reports it to Andrew on Teams
```

## What was measured, and with which instrument

| Claim | Instrument | Result |
|---|---|---|
| Password was correct | auth-handler log, `mfa_challenge_issued` | MEASURED. Fires only post-password; a wrong one logs `login_failed`. |
| Both refusals were his | WAF edge log, client IP | MEASURED. Same `173.79.153.38` as the login. Not inferred from timing. |
| No request left his browser in the gap | WAF edge log (`aws-waf-logs-opal-cloudfront`) | MEASURED. 3 requests from that IP in 75 min; none between. |
| No code was minted | `opal-portal-auth-mfa` scan; zero `mfa_code_sent` for his hash | MEASURED. |
| Email delivery is healthy | SES `get-account` | MEASURED. SendingEnabled, ProductionAccessEnabled, EnforcementStatus HEALTHY, 9 sends/24h vs 50,000 quota. Not on the suppression list. |
| Not a deploy regression | Lambda `LastModified` 2026-09-09T23:39Z (`CodeSha256 sJyR6xk2...`); portal bundle 2026-09-09T19:38Z | MEASURED. Same bytes served him two clean logins on 09-10. |
| His baseline behaviour | auth-handler log, 30-day retention | MEASURED. 11 logins, every one challenge -> send in 1-110 s -> accepted. 09-11 is the only challenge of his that produced no send. |

Denominators: 33,842 auth events over the retention window; 1,123 analytics rows for this user out
of 956,491 scanned.

## The mechanism

`infra/aws/opalinvest_dev/lambda/auth-handler/src/mfa.ts:596` -- the send is one atomic
conditional write, and all three failure modes share one branch:

```
ConditionExpression: 'attribute_exists(pk) AND expiresAt > :now AND sends < :maxSends'
```

`CHALLENGE_TTL_SEC = 1800` (`:68`), `MAX_SENDS = 3` (`:88`). The catch at `:607` is explicit:
*"Unknown id, expired, or send budget exhausted -- deliberately one branch."*

For this session the binding clause is provably `expiresAt > :now`: `sends` was 0 (no `mfa_code_sent`
line carries his hash today, across all 1,436 events), so the cap cannot have bound.

`infra/aws/opalinvest_dev/lambda/auth-handler/src/index.ts`, the route:

```
// ALWAYS 200. Unknown, expired and budget-exhausted challenges are
// indistinguishable from a successful send, so this route leaks nothing
await resendMfaCode(body?.challengeId);
return jsonResponse(200, { success: true }, undefined, origin);
```

## The defect class

Four. Only the first is specific to this incident.

**1. An unrecoverable retry loop with no exit sign.** Once a challenge expires, `/auth/mfa/send`
against it can never succeed -- the row is gone or dead, and the route takes no email address, so
it cannot mint a replacement. The only exit is a fresh `POST /auth/login`. Nothing in the product
says so. The user's instinct (press resend again) is the one action guaranteed to fail, and he
performed it twice over fourteen minutes before giving up and messaging a human two hours later.

**2. A security control whose entire cost lands on the legitimate user.** The always-200 is correct
anti-enumeration design: it stops an attacker holding a stolen `challengeId` from learning whether
it is live. But the person on the other end of a refusal has *already proven the password*. The
design treats a post-password, pre-code user as an untrusted stranger, and buys enumeration
resistance with the one signal that user needs. The trade was never wrong -- it was never priced.

**3. The pre-auth screens emit no telemetry at all.** `opal-sessions` (the client analytics plane)
begins at `session_start`, which fires *after* MFA succeeds -- confirmed against this user's own
09-10 row at 20:25:30Z, one second after his `mfa_code_accepted`. He has zero rows on 09-11. So the
one screen that failed is the one screen nothing watches, and "he did not click", "he clicked and
the JavaScript threw", and "the button never rendered" are indistinguishable with what we have.
The WAF edge log is what closed the network half of that question, and it is not an auth instrument
-- it was reachable only because someone attached a firewall for unrelated reasons.

**4. `mfa_send_refused` carries no `account_hash` and no reason.** Every neighbouring event carries
the hash. Attribution here required correlating a second plane (WAF) on client IP. Three distinct
causes -- unknown id, expired, budget exhausted -- arrive as one indistinguishable line, so the
question "how often does this happen and to whom" is currently unanswerable from the auth log alone.

## The part that should sting

`OTP_EXPIRY_POSTMORTEM_20260902.md`, nine days ago, on the verify path, verbatim:

> **The silent outcome.** The verify path's expiry branch deleted the row and threw
> `'Invalid or expired code'` with no log line. [...] a user who typed the code one minute late was
> indistinguishable, in our own telemetry, from a user who never opened the email.

That was fixed -- `mfa_code_expired` now logs with `late_by_sec` (`mfa.ts:408`), and the comment
above it says the client complaint that raised the TTL *"was invisible in our own logs"*. The
**send** path kept exactly the same blindness, and it is the path that failed this time. The
remedy was applied to the instance, not to the class, and the class had already been named in our
own document.

Second-order: the 09-02 brief also recorded this same user's delivery at 35-109 s. That number is
why "Yang's mail is slow" was a tempting read today and a wrong one -- nothing was ever handed to
SES to be slow with.

## What is NOT established

- **Whether he clicked at 18:24 and the click died in the browser.** Ruled out: blocked by WAF,
  dropped at CloudFront, lost in transit, rejected by CORS -- all would have left an edge-log row.
  Not ruled out: a click that never became a network request. No instrument covers it (defect 3).
  Worth one question to him; a browser console would settle it.
- **Why a user whose ten prior logins clicked within 1-110 s waited 37 minutes.** Out of character,
  unexplained, and the honest answer is that we cannot see it.
- **Per-message delivery**, still. No SES configuration set is attached to the OTP send, so there
  are no per-message Delivery events -- carried forward unremediated from the 09-02 brief.

## Recommended, not built

Surfaced rather than implemented -- these touch a security path and the always-200 is deliberate.

1. **Distinguish expiry to the client.** Return a typed "challenge expired, please sign in again"
   for the *expired* branch only, leaving unknown-id and budget-exhausted opaque. An expired
   challenge the caller already holds leaks nothing it does not already know, and it converts an
   unrecoverable loop into a one-click recovery. Cheapest fix, largest user-visible gain.
2. **Put `account_hash` and a reason code on `mfa_send_refused`.** Makes the next one of these a
   single query instead of a two-plane correlation, and makes the rate measurable.
3. **One client event on the pre-auth screens** -- MFA screen rendered, send clicked, request
   fired. This is the instrument whose absence cost the most time today.
4. Consider whether 30 minutes is the right challenge lifetime given that the code is no longer
   sent at login: the clock now starts before the user has done the thing that starts the clock.

Deliberately excluded: an alarm or monitor on refusal rate. Standing moratorium -- Andrew's word
required, and a monitor on a route whose semantics may change with (1) would measure the wrong
thing precisely.
