# laneZ DECOMP — D12_PHONE_OTP_ALL_AWS (phone/SMS OTP, all-AWS)

**Seat:** `2.0.0_SA_COO~Z` (atom-decomp). **PRD:** `1.0.0_SA_CTO~Z` @`65f7a59396`
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/D12_PHONE_OTP_ALL_AWS_20260901.md`) — a complete
purpose-level PRD; this decomp builds on it and does not restate it.

**Authority (Andrew-direct, 2026-09-01, CTO~Z terminal, verbatim, relayed by `1.0.0_SA_CTO~Z` 18833):**
"lets push for all AWS" → "Authorized, go ahead", preceded by "I'd prefer to operate this entirely out
of AWS" and "very, very little traffic… no more than 10 people." **BUILD LEG AUTHORIZED. Two items
remain Andrew-gated and are NOT cleared — see §4.**

---

## 1. REGISTER + BOUNDARY DECISION (COO ruling)

⛔ **SIBLING PROJECT, not a re-open of `PLATFORM_OPS_USERMGMT`.** That project is the send-fix
workstream — COMPLETE, certified, and closed. Folding a new multi-week build with an external carrier
gate into it would re-open a finished record and blur its closure.
- **Project id:** `D12_PHONE_OTP_ALL_AWS` (matches the PRD deliverable name so citations resolve).
- **Umbrella:** the D12 program (Andrew's "D12 next leg"), a sibling to `PLATFORM_OPS_USERMGMT`.
- **Register writer:** `0.0.0_AB_MSTR~Z` (register is MSTR's write, Rule 27). **Requested in the
  broadcast that accompanies this decomp.** Until the row lands the decomp binds by reading, not by
  register.
- ✅ **This is NOT a shadow pipeline** (Andrew's standing veto): the SMS channel EXTENDS the existing
  MFA challenge system (`MfaChannel = email|sms|none` already exists per PRD §3), it does not stand up
  a parallel one. Same challenge table, same `issueChallenge`/`verifyAndConsume`, one new send path.

## 2. THE ATOMS — grouped by lane, each with its acceptance criterion

⛔ **Source anchors below are RELAYED from the PRD @`65f7a59396` (CTO~Z read them at source); each lane
CONFIRMS at source when building — do not treat a line number here as measured by this seat.**

### Lane A — backend sender + dispatch + IAM (`0.7.0_AE_CloudOps~Z`, auth-handler lane, holds Act B/C)
| atom | work | acceptance |
|---|---|---|
| **SB-1** | `sendMfaCodeSms(phoneE164, code, ttlMin)` via `@aws-sdk/client-pinpoint-sms-voice-v2` `SendTextMessageCommand` (`OriginationIdentity`=TFN ARN, `MessageType:'TRANSACTIONAL'`); mirror `email.ts sendMfaCodeEmail` | unit-exercised against the sandbox on a VERIFIED destination number only; returns a message id; **no send to an unverified number** (sandbox enforces, but the code asserts it too) |
| **SB-2** | `resendMfaCode` (`auth.ts:223`): after `sendChallengeCode` (already charges the channel-agnostic budget), branch on `user.mfaChannel` — email→`sendMfaCodeEmail`, sms→`sendMfaCodeSms(user.phoneNumber, issued.code, TTL)` | ONE code per challenge across N resends (Act C idempotency parity), on BOTH channels; the sealed code is re-sent, never rotated |
| **SB-3** | `login()` sms-branch: replace the current `503` with — if `user.phoneNumber` present, `issueChallenge(channel:'sms')`, return `{mfaRequired, challengeId, channel:'sms'}`, **send NOTHING** (Act B parity). Keep `503` only for sms-selected-but-no-number | login issues, does NOT send, on the sms channel; a CloudWatch check shows a challenge issued and NO send at credential time |
| **SB-4** | `issueChallenge` log: parameterize the hardcoded `channel:'email'` (cosmetic) | the log field reflects the actual channel; no other behavior change |
| **SB-5** | IAM: add `sms-voice:SendTextMessage` to the auth-handler role (today `ses:SendEmail`×2 per `email.ts:13`), **resource-scoped to the origination-identity ARN**, Terraform + `safe-apply` (never bare) | ⛔ the grant is RESOURCE-SCOPED, not a blanket Allow — **do NOT repeat F-1** (the unconditioned `ses:SendEmail` that restricts nothing). Terraform authored now; APPLY is gated on the TFN ARN existing (SP-1) |

### Lane B — frontend enable + phone capture/ownership-verify (`0.4.0_DE_ClientPlatform~Z`)
| atom | work | acceptance |
|---|---|---|
| **SF-1** | flip `sms` to `available:true` in `MfaOptInPrompt` CHANNELS | only AFTER Lane A is live in the target env; before that the picker stays "Unavailable" |
| **SF-2** | **NEW: phone capture + ownership-verify UI** — collect E.164, send a test code, confirm, store via `/auth/mfa/preference`. Channel chosen at ENROLMENT (stored pref); login-time picker reflects the stored channel | a user can enrol a number they demonstrably control (test-code round-trip), and cannot store an unverified number; E.164 validated client-side to match `auth.ts:245` |
| **SF-3** | fix STALE docstrings (`MfaOptInPrompt.tsx` header + `AuthContext.tsx:429`) still describing the pre-Act-B backend | the docstrings describe issue-not-send (Act B) reality — closes the F-6-adjacent "comment asserts a falsehood" class |

### Lane C — provisioning (Andrew-gated; HELD at `1.0.0_SA_CTO~Z`, see §4)
| atom | work | gate |
|---|---|---|
| **SP-1** | provision the toll-free number (~$2/mo) + submit toll-free VERIFICATION (the long pole, ~1–3wk external carrier gate) | ⛔ Andrew go-to-provision + Andrew sign-off of the carrier-verification content (PRD §5, outward under Opal's identity) |
| **SP-2** | posture: exit sandbox (production access) **or** verify the ~10 pilot numbers; raise the $1 spend cap if needed | Andrew posture choice; support case ~1–2 days |

## 3. CRITICAL PATH / SEQUENCING

```
[LONG POLE] SP-1 toll-free number + VERIFICATION  ~1-3 wks  — Andrew-gated, start FIRST, blocks nothing else
[parallel]  SB-1..SB-4 backend sender+dispatch     ~1 day    — launches NOW against the pending identity
[parallel]  SB-5 IAM Terraform authored            ~1/2 day  — authored NOW; APPLY gated on SP-1's ARN
[parallel]  SF-2 phone capture/verify UI           ~1 day    — launches NOW; SF-1 enable waits on Lane A live
[gate]      SP-2 sandbox exit / verify numbers      ~1-2 days — Andrew posture choice
[finish]    deploy -> pilot on Andrew + aj@ numbers          — after SP-1 verified + SP-2 + Lane A/B merged
```
⭐ **The build (SB-1..4, SB-5-author, SF-2, SF-3) launches immediately; only the outward SEND to real
users waits on SP-1/SP-2 + Andrew. Same shape as the send-fix: build behind a gate, cross it on Andrew's word.**

## 4. GATES — the build/send boundary is a HARD STOP

⛔ **NO SMS IS SENT TO A REAL (unverified) USER until ALL of:** SP-1 TFN verified · SP-2 sandbox
exited or the target number verified · Andrew's go. The sandbox enforces verified-destinations-only, so
the technical floor agrees with the policy — but the atoms ALSO assert it (SB-1) so a future sandbox
exit does not silently open the send path.
⛔ **Carrier-verification CONTENT is outward under Opal's identity — Andrew-gated (PRD §5).** No lane
edits or submits that text; the `[NEEDS ANDREW]` fields (business address, support contact, corporate
site/entity confirmation) are Andrew's. Held at `1.0.0_SA_CTO~Z`.
✅ **NOT a vendor-egress issue:** AWS End User Messaging is Opal's own AWS plane (like SES email), not a
third-party API — Andrew explicitly ruled out the Quo/third-party path. No per-use vendor-egress word needed.
⛔ **NO monitor / alarm / SNS-notify / freshness-checker** on this surface (standing moratorium) — an OTP
SENDER is the authorized build; a monitor on it is not. Findings land as gates or owned items, never a monitor.

## 5. CONSTRAINTS CARRIED FROM THE SEND-FIX (do not re-learn them)
- **F-1**: SB-5's IAM grant is resource-scoped, never a blanket Allow. The send-fix left F-1 OPEN as a
  cautionary specimen; the new grant is where we get it right the first time.
- **Act B parity**: SB-3 login issues, never sends. **Act C idempotency parity**: SB-2 re-sends the
  sealed code, never rotates — one code per challenge across N resends, on SMS as on email.
- **No shadow pipeline**: extend the existing challenge system; SB-2 reuses `sendChallengeCode`'s budget
  charge and the sealed-at-issue code. **All-AWS**: `pinpoint-sms-voice-v2` only, no third-party SDK.
- **F-10 sibling**: SF-2 stores the number against the account; the identity-continuity gap (email-keyed
  refresh) is AE~Z's plane, tracked in `PLATFORM_OPS_USERMGMT` F-10 — do not re-file here.

## 6. LANE ADJUDICATION + SEATING

CTO~Z's proposed split is SOUND and adopted: (A) `0.7.0_AE_CloudOps~Z` (auth-handler lane, holds Act
B/C — natural continuity for the sender/dispatch/IAM), (B) `0.4.0_DE_ClientPlatform~Z` (the SMS-enable +
capture UI), (C) provisioning held at CTO~Z pending Andrew.
⛔ **SEATING PRECONDITION (Rule 27 one-project-per-instance, `/mstr-spawn` 1d-ii):** AE~Z and DE~Z must
be FREE of their now-complete `PLATFORM_OPS_USERMGMT` TO faces before they hold this sibling project.
Their work is done+accepted+ON-ORIGIN; the faces need CLOSING (issuer's act) — measured, then closed
SUPERSEDED/COMPLETE — before or at seating. **Liveness + encumbrance measured at seating time, not
assumed from a 4.5h-old "nothing open at this seat."**

## 7. ROLES
Validation `2.0.0_SA_COO~Z`; acceptance `1.0.0_SA_CTO~Z`; independent certification `3.0.0_SA_CVO~Z`.
Surprise items → `3.0.0_SA_CVO~Z` (cc `0.0.0_AB_MSTR~Z`), one line, keep working. Push state MEASURED,
never defaulted (and per CVO~Z 18806, stated as an is-ancestor predicate for ON-ORIGIN, vintage-stamped
for LOCAL-ahead).

## 8. FUTURE SCOPE — registered, NOT built for the pilot (CTO~Z 19024)
⛔ **Enrolment surface RULED (c) post-login authenticated step** (CTO~Z 19024, concurring with the §6 scope
verdict). **Option (a) — a persistent ACCOUNT-SECURITY surface for MANAGING the SMS factor** (change number,
disable sms, re-verify) — is the correct long-term home but is OUT of this leg's scope: SF-2 stays
**enrolment-only via (c)**. Registered here as a FUTURE SCOPE item; it becomes its own project when Andrew
wants a settings/security surface. Not built now, not a pilot dependency — surfaced so it is not lost.
