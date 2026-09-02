# OTP Expiry Postmortem -- the login code that expired before the client's mail server surfaced it

| | |
|---|---|
| **Date** | 2026-09-02 |
| **Author** | 1.0.0_SA_CTO~Z (site Z) |
| **Trigger** | Andrew-direct, ~15:2xZ: *"A client is complaining that the email OTP takes so long to get to them that it expires before their mail server surfaces it. I think we need to push token expiry to 30 minutes."* |
| **Affected** | stephen.shipley@cottonwoodmail.com (Cottonwood) -- the first external partner to attempt email MFA after the partner rollout |
| **Status** | Remediated same day. Backend `f4659653e8` live 16:23Z; portal-v2.1.176 served 16:3xZ. Deploy ledger `otp-ttl-30min-and-expiry-event`, 6 legs closed. |
| **Owner going forward** | D12 (site Z). Surface owners: 0.7.0_AE_CloudOps (auth-handler), 0.4.0_DE_ClientPlatform (portal auth UI). |

## The one-sentence finding

The OTP lifetime was sized against OUR delivery path (~1 s to SES accept) and never against the
recipient's (a corporate mail gateway that may hold a message for minutes), and the one outcome
that would have exposed the mismatch -- a code presented after expiry -- emitted no telemetry at
all, so the first evidence we had was the client telling us.

## Timeline (UTC)

```
2026-09-01 17:2xZ  Email MFA enabled for 13 internal Opal staff. Partner firms HELD pending "word
                   back it was smooth" -- every test login so far was on Opal's own mail system.
2026-09-02 14:4xZ  Andrew: "global MFA push on the client side". 9 partner humans enabled, then
                   8 more on his ruling. 32 of 48 accounts email-MFA.
           15:12:57  stephen (Cottonwood) logs in; challenge issued.
           15:13:32  He clicks "Send me a code". Lambda START -> END 335 ms, SES accept inside.
           15:13:32  ... nothing. No accept, no reject. (An expiry attempt was NOT logged.)
           15:2xZ    Andrew relays the complaint; asks for 30 min and for our-side levers.
           15:3xZ    Stephen MFA OFF (Andrew-direct, "for now"). Verified on a consistent read.
           16:10Z    Backend fix committed (f4659653e8).
           16:23:14Z Lambda live: CodeSha256 dYZiZ7Rz == built, 0-diff plan.
           16:3xZ    portal-v2.1.176 served: UI renders the server's TTL.
```

## What was measured before anything changed

All from `/aws/lambda/opalinvest-auth-handler` (Logs Insights, 14 d, 103 `mfa_*` events, 7 accounts;
`account_hash` = sha256 of the lowercased email, positive-controlled against Stephen's).

| account | mail path | send -> accept |
|---|---|---|
| andrew@opalinvest.com | Opal's own | 36 s |
| yang@opalinvest.com | Opal's own | 109 s, 35 s |
| manav@opalinvest.com | Opal's own | 140 s |
| **stephen.shipley@cottonwoodmail.com** | **Cottonwood's gateway** | **never accepted** |

- Our side of Stephen's send: **335 ms** end to end. Everything after SES accept is downstream.
- SES plane: production access (50k/day, HEALTHY); `opalinvest.dev` DKIM SUCCESS; custom MAIL FROM
  `mail.opalinvest.dev` SUCCESS (SPF-aligned); SPF `include:amazonses.com`; DMARC `p=none`;
  **account suppression list EMPTY** (a suppressed address is dropped silently and would have
  looked exactly like this -- it was not the cause).
- 14-day account metrics: Send 110 / Delivery 88 / Bounce 22. The bounces cannot be attributed
  to recipients: **no SES configuration set is attached to the OTP send, so there are no
  per-message Delivery events and SES -> MX latency is unmeasurable today.**
- The OTP mail: the code is in the SUBJECT LINE; HTML body with one remote image (logo) and one
  footer link; a Text part exists.

## The defect class

Three, and only the first is specific to OTP.

**1. A security parameter chosen against an unmeasured distribution -- and the code said so.**
`mfa.ts` at the constant, verbatim: *"DECLARED CHOSEN, NOT MEASURED ... ten minutes is long enough
to survive ordinary mail-delivery latency."* "Ordinary" meant the only latency anyone had seen:
Opal's own mail system, where every test code landed in under 2.5 minutes. The distribution that
matters -- a partner firm's inbound gateway -- had a sample size of zero at go-live.

**2. The silent outcome.** The verify path's expiry branch deleted the row and threw
`'Invalid or expired code'` with no log line. Every other outcome had an event (`mfa_code_sent`,
`mfa_code_accepted`, `mfa_code_rejected` with a reason). So a user who typed the code one minute
late was indistinguishable, in our own telemetry, from a user who never opened the email. Fourteen
days of logs could not answer "did Stephen try?" -- they still cannot for his attempt; they can for
the next one.

**3. Two carriers of one value with no named primary** (the estate's recurring class -- see
`docs/references/MDPF_POSTMORTEM_20260722.md`). The server derived everything from
`CHALLENGE_TTL_SEC`: the row's `expiresAt`, the DynamoDB `ttl`, the resend window, the email's own
"expires in N minutes". The portal did not: `MfaChallengeForm.tsx:112` hand-typed
*"It expires in 10 minutes."* Raising the server constant alone would have shipped a form that
lied to every user by 20 minutes -- and the `ttlSec` the server already emitted on the
enrolment path was never put on the login response at all.

## The part that should sting

The TTL's own comment flagged it as unmeasured and said it was *"surfaced to the issuing seat
rather than buried."* It was surfaced, and then it sat. A comment that says "not measured" is a
scheduled task nobody scheduled; the only thing that would have made it fire was an instrument on
the failure outcome, and that instrument was the one line missing from the code. The partner
rollout went live at 14:4xZ; the first partner login was at 15:12Z; the complaint arrived inside
the hour. There was never going to be a quieter moment to find this than before go-live, and the
data to find it with -- a single external-domain test login -- did not exist.

## What changed

| where | change | commit |
|---|---|---|
| `auth-handler/src/mfa.ts` | `CHALLENGE_TTL_SEC` 600 -> 1800. Row `expiresAt` + `ttl`, resend window, email copy all derive from it (enumerated: 22 hits, all derived). `MAX_ATTEMPTS` / `MAX_SENDS` unchanged -- a longer window buys no extra guesses. | `f4659653e8` |
| `auth-handler/src/mfa.ts` | NEW event `mfa_code_expired {account_hash, late_by_sec}` at the expiry branch. `late_by_sec` is the number that sizes the TTL next time and discriminates "gateway delay" from "walked away". | `f4659653e8` |
| `auth-handler/src/auth.ts`, `types.ts` | `ttlSec` on both login MFA returns so the UI renders the SERVER's lifetime. | `f4659653e8` |
| portal `AuthContext.context.ts`, `AuthContext.tsx`, `MfaChallengeForm.tsx` | `MfaChallenge.ttlSec`; login() maps it; the form renders `round(ttlSec/60)` and OMITS the sentence if the value is absent -- never a hand-typed fallback, never `NaN`. | portal `30ca034b` -> PROD `6cb3d0f654`, tag portal-v2.1.176 |
| `opal-users-v2` | stephen.shipley@cottonwoodmail.com `mfaEnabled=false` (Andrew-direct, "for now"; channel left `email` so re-enable is one field). | DynamoDB, verified on a consistent read |

Deploy order was backend first, then portal, so a new bundle never read an old backend. Verified
on each plane's own instrument: the function's `CodeSha256` (not the apply receipt), the served
bundle's bytes (not the tag), with a positive control on each read.

## What we still do not know

- **User error vs gateway delay: NOT established.** n=1 for external domains, and that one sample
  sits on a different mail path from the three that worked. Andrew's inference (user error) is the
  more likely reading; it is not the demonstrated one. The next `mfa_code_expired` with a small
  `late_by_sec` would argue gateway; a large one would argue user.
- **SES -> MX latency for cottonwoodmail.com.** Unmeasurable without a configuration set.
- **Whether Stephen even attempted a code.** Unknowable for his attempt; the old build did not log it.

## Levers on our side, ranked

1. **Longer TTL -- DONE.** The only lever that helps this client today; their gateway is the clock.
2. **Log the expiry outcome -- DONE.** Turns the next occurrence into data.
3. **Strip the remote logo image and the footer link from the OTP mail.** Corporate gateways
   (Defender Safe Links / URL detonation, remote-image fetching) hold HTML with remote content for
   scanning; a link-free, image-free body is the classic fast path. The code is already in the
   subject line, so a text-only body loses nothing functional. Cheap, reversible, customer-facing:
   **Andrew's call.**
4. **Attach an SES configuration set with event publishing to the OTP send** so Delivery events
   carry per-recipient timestamps and SES -> MX latency becomes measurable. Monitor-class under the
   standing moratorium: **Andrew's word.**
5. **Ask Cottonwood IT for their gateway's receipt-vs-delivery timestamps on the 15:13Z message.**
   The one measurement that settles where the minutes went, and it costs us nothing.

Recommendation: hold 3 and 4 until `mfa_code_expired` shows a second external user with a small
`late_by_sec`. One more occurrence answers the question with data instead of a hunch.

## What NOT to build

- **An alarm or monitor on OTP latency.** Standing moratorium (CLAUDE.md NEVER block); a monitor on
  an unmeasured route measures the wrong thing precisely. Lever 4 is the measurement, not an alarm.
- **An SMS fallback rushed in for this.** SMS is gated on SP-1 (toll-free provisioning + carrier
  verification, comp-schedule G-7). The `sms` channel with no phone is a MEASURED lockout path
  (3.0.0_SA_CVO~Z 18907) and its fix surface is in PROD with zero consumers.
- **Automatic resend / retry.** `MAX_SENDS` exists to stop `/auth/mfa/send` becoming a mail
  amplifier. A longer TTL is the safe direction; more sends is not.
- **A wider TTL "to be safe".** 30 minutes was chosen; the security cost is bounded by the attempt
  and send caps, which did not move. Widen again only against `late_by_sec` data.

## Incidental findings from the deploy (site Z, AE lane; surfaced, not fixed)

- `infra/aws/lambda/ci/build-nodejs-lambda.sh`: `to_native_path()` rewrites `/c/...` only. From a
  `/cygdrive/c/...` cwd (also mounted on site Z) native bun cannot open the path, `readFileSync`
  throws, and the script reports the throw as *"No source_dir found for <fn> in
  lambda-source-map.json"* -- the map had the entry the whole time. A misreported cause aims the
  investigation at the wrong file. Workaround: run from a `/c/` cwd.
- `infra/aws/lambda/ci/record-terraform-deploy.sh`: opens the UTF-8 source map without an encoding
  (cp1252 decode error on Windows Python; `PYTHONUTF8=1` gets past it), then fails at line 511 with
  `/c/Users/Opal: Is a directory` -- an unquoted expansion splitting on the SPACE in this box's
  path. It wrote nothing, so `lambda-source-map.json` `_last_deploy_recorded` is STALE for this
  deploy; a reader using it as the oracle will conclude the deploy did not happen. The ledger and
  the commit messages are the record.
- Both are the same class: scripts written on a space-free, single-mount path and run on a
  device with neither property. Third instance of the space-splitting class recorded at this seat.

## The honest meta-point

Nothing in this incident was hidden. The constant said it was unmeasured. The UI string was a
plain literal beside a comment naming the constant it duplicated. The expiry branch was three lines
long and visibly logged nothing. Every piece was readable by anyone who looked -- and nobody was
going to look, because nothing was failing. The fix that generalises is not "pick 30 instead of 10";
it is that a declared-unmeasured parameter needs an instrument on its failure outcome before it
ships, because that instrument is the only thing that turns the next quiet failure into a number.
