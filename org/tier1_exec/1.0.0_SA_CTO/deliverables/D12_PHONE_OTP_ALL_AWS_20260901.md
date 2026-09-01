# D12 PLATFORM_OPS -- Phone (SMS) OTP, all-AWS: architecture, account state, plan

**Authority (Andrew-direct, 2026-09-01, CTO~Z terminal, verbatim):** "lets push for all
AWS" -> "Authorized, go ahead." Preceded by "I'd prefer to operate this entirely out of AWS
though" (ruling out the Quo/third-party send path) and "very, very little traffic... probably
could even get away with a $1 cap... no more than 10 people."

**Seat:** `1.0.0_SA_CTO~Z`. **Status:** build leg AUTHORIZED; provisioning gated on Andrew's
sign-off of the carrier-verification content below (outward registration under Opal's identity).

---

## 1. Decision

Deliver phone/SMS one-time codes via **AWS End User Messaging SMS** (API namespace
`pinpoint-sms-voice-v2`; `sms-voice:` IAM prefix). No third-party API, no egress off AWS.
Origination identity: a **toll-free number provisioned inside AWS** (recommended over 10DLC for
this scale -- one verification form, no TCR brand/campaign to replicate, ample throughput for
<10 users). 10DLC-under-the-reused-brand remains the alternative if a geographic number is wanted.

**The Quo number is NOT used as the sending identity.** A US A2P number originates on exactly one
platform (CSP) and carriers gate on the originating number matching a campaign registered on that
platform. AWS cannot send from a number hosted/registered on Quo. Reusable across platforms: the
*brand* vetting only (company/EIN), and only if 10DLC is chosen. The *number + campaign* must live
in AWS (fresh number, or a port-in that removes it from Quo).

## 2. Account state (MEASURED 2026-09-01, region us-east-1, acct 313476888478)

| Fact | Value | Instrument |
|---|---|---|
| End User Messaging tier | **SANDBOX** (verified-destinations-only) | `describe-account-attributes` ACCOUNT_TIER |
| Text spend limit | **$1/mo, MaxLimit $1, not overridden** | `describe-spend-limits` |
| Origination numbers | **0** | `describe-phone-numbers` |
| 10DLC registrations | **0** | `describe-registrations` |
| Pools / Sender IDs | **0 / 0** | `describe-pools` / `describe-sender-ids` |
| Verified dest numbers | **1: +17862617679 (PENDING)** = the ops-alerts number | `describe-verified-destination-numbers` |
| SNS account SMS | MonthlySpendLimit "1" | `sns get-sms-attributes` |

Reading: nothing is provisioned in AWS End User Messaging. The $1 *per-message spend cap* is
plausibly sufficient at this volume, but the number lease (~$2/mo) and registration are separate
line items, and the sandbox + spend cap gate reaching real users regardless of volume.

## 3. What exists vs. the lift

**Already built (backend + frontend shell):**
- `types.ts` MfaChannel = email|sms|none; `db.ts` stores `mfaChannel` + `phoneNumber`; E.164
  validation (`auth.ts:245`); `setMfaPreference` / `/auth/mfa/preference` round-trip.
- `login()` already branches on `sms` (currently fails closed 503 -- no sender).
- Frontend picker already renders "Text message" (disabled, "Unavailable" badge) in
  `MfaOptInPrompt.tsx`.

**The lift:**
1. **Backend sender + dispatch** (lane: `0.7.0_AE_CloudOps~Z`).
   - New `sendMfaCodeSms(phoneE164, code, ttlMin)` -- `@aws-sdk/client-pinpoint-sms-voice-v2`
     `SendTextMessageCommand { DestinationPhoneNumber, OriginationIdentity: <TFN id/ARN>,
     MessageBody, MessageType: 'TRANSACTIONAL' }`. Mirrors `email.ts sendMfaCodeEmail`.
   - `resendMfaCode` (`auth.ts:223`): after `sendChallengeCode` (which already charges the
     channel-agnostic send budget), look up the user and branch on `user.mfaChannel`:
     email -> `sendMfaCodeEmail`; sms -> `sendMfaCodeSms(user.phoneNumber, issued.code, TTL)`.
   - `login()` sms-branch: replace the 503 with -- if `user.phoneNumber` present, `issueChallenge`
     (channel 'sms'), return `{mfaRequired, challengeId, channel:'sms'}`, send NOTHING (Act B
     parity holds unchanged). Keep 503 only for sms-selected-but-no-number.
   - `issueChallenge` log currently hardcodes `channel:'email'` -- parameterize (cosmetic).
2. **IAM** (lane: `0.7.0_AE_CloudOps~Z` / DT for apply). Add `sms-voice:SendTextMessage` to the
   auth-handler role (today it carries only ses:SendEmail x2 per `email.ts:13`), resource-scoped to
   the origination identity ARN. Terraform + safe-apply (never bare).
3. **Frontend** (lane: `0.4.0_DE_ClientPlatform~Z`).
   - Flip `sms` to `available:true` in `MfaOptInPrompt` CHANNELS (once backend is live).
   - **New: phone capture + ownership-verify** -- collect E.164, send a test code, confirm, store
     via `/auth/mfa/preference`. This is the real added UI. Channel is chosen at ENROLMENT (stored
     pref), not per-login -- the login-time picker reflects the stored channel.
   - Also fix the STALE docstrings (`MfaOptInPrompt.tsx` header + `AuthContext.tsx:429`) still
     describing the pre-Act-B backend as current.
4. **Provisioning** (Andrew-gated -- see s.5).

## 4. Critical path

```
[LONG POLE] toll-free number + toll-free VERIFICATION  ~1-3 wks (external carrier gate)
[parallel]  backend sender+dispatch                    ~1 day  AE
[parallel]  IAM grant (Terraform)                       ~1/2 day AE/DT
[parallel]  frontend enable + phone capture/verify      ~1 day  DE
[gate]      exit sandbox (or verify the ~10 numbers) + spend cap  support case, ~1-2 days
[finish]    deploy -> pilot on Andrew + aj@ numbers
```
Toll-free verification is the only multi-week item and blocks nothing else -- start it first;
build the rest against the pending identity.

## 5. Andrew gates (outward / spend)

- **Toll-free verification content sign-off** (below) -- submitted under Opal's identity to
  carriers; wrong content = weeks of re-review. Needs the [NEEDS ANDREW] fields.
- **Go to provision** the TFN (~$2/mo) + submit the verification.
- Sandbox exit vs. verify-the-10-numbers is a posture choice (production access = clean;
  verify-numbers = cheapest/fastest, onboarding tax).

### Toll-free verification -- DRAFT for sign-off

- **Business / brand:** Opal Capital
- **Website:** https://opalinvest.dev  *(confirm corporate site / legal entity name)*
- **Business address:** [NEEDS ANDREW]
- **Support contact (email + phone):** [NEEDS ANDREW]
- **Use case:** Two-factor authentication (2FA) / one-time passcodes for account sign-in.
  Transactional only; no marketing.
- **Est. monthly volume:** < 300 messages (< 10 active users).
- **Opt-in workflow:** User opts in inside the authenticated app. After signing in with email +
  password, the two-step verification screen lets the user choose "Text message," enter and
  confirm their own mobile number, and confirm. A code is sent only after that explicit election.
  The number is used solely for sign-in codes the user requested; no other messages are sent.
- **Sample message 1 (the code):**
  `Opal Capital: your sign-in verification code is 123456. It expires in 10 minutes. Do not share this code.`
- **Sample message 2 (opt-in confirmation):**
  `Opal Capital: text-message verification codes are now on for your account. Msg & data rates may apply. Reply HELP for help, STOP to stop.`
- **Opt-out / help:** STOP / HELP handled by AWS End User Messaging opt-out list (default).

## 6. Confidence

- Account state (s.2): read directly -- HIGH.
- 10DLC/toll-free CSP-binding + sandbox/spend gates: general knowledge + measured gates -- HIGH on
  the shape, MEDIUM on exact registration mechanics/pricing. Confirm against current AWS End User
  Messaging docs before submitting the verification or committing spend. AWS changes these.
