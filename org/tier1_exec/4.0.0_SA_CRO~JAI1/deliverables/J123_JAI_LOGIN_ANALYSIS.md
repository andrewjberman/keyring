# J123 -- Jai's Opal dashboard login: analysis (4.0.0_SA_CRO~JAI1, 2026-10-21)

Order: `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADHOC.J123.jai-opal-dashboard-login.md` (J2 run, J3 draft are
this seat's; J1/J4 reads, proof and receipt are 0.7.0_AE_CloudOps~ADVI1's). Division: CTO msg 9159.
Authority: Andrew-direct 16:32Z "make sure the dell1 box is handling the JAI account creation as an opal user";
16:46Z "i need them to spawn a new CRO to analyze this and run it".

## 1. Full name -- measured from a read, never guessed

| Read (gateway, Andrew's mailbox/calendar) | Result |
|---|---|
| `search_email "Jai"` | 16 rows; one Opal hit: Yang Liu 2026-10-19 20:05Z "Jai, our intern, will present..." -- no surname |
| `search_email "jai@opalinvest.com"` | 0 rows |
| `read_email` (that 10/19 thread) | to/cc lists 9 Opal staff; Jai not on it; no surname |
| `list_chats` top 40 | 125 ids; no "jai" match in names or previews |
| `search_files "Jai intern"` (OneDrive) | 0 rows |
| `list_calendar 2026-10-19 +3d` | **OCIO IC, 2026-10-20 14:00-15:00Z, organizer Austin Graff: optional attendee `"Jai Mukraj" <Jai@opalinvest.com>`, response accepted** |

The name is **Jai Mukraj**: the Opal tenant (Exchange) display name on the exact username, on the meeting where Yang
said Jai presents. DISTRACTOR excluded: `"Jai Sisodia" <jai@cycoresecure.com>` (Cycore kick-off, 2026-10-20 15:00Z) is a
vendor contact, a different domain and person.
Claim class: MEASURED (directory display name), not Andrew's word -- open-calls row dell1-20261021T164621Z-5956 stays
open for him; whether J1 accepts this read is the CTO's ruling (asked 16:58Z).

## 2. Username

`jai@opalinvest.com` -- the calendar read confirms the mailbox exists in the Opal tenant (stored lowercase by the script).

## 3. What Jai can open

- Firm `opal-capital`, tier `internal` (`users/scripts/create_user_v2.py` FIRMS). `portal/src/lib/firmAccess.ts`:
  internal users (firmId `opal-capital`) "see everything"; the per-firm allowlist binds partner firms only.
- Role `user` (the script default), not `admin`: an intern needs no admin functions.
- No portal page changes: this is one user row, so the client-facing PROD-push rule does not apply.

## 4. Credential handling (no secret anywhere)

- The script requires `--password`. The runner (`j123_insert.py`, session scratchpad) generates a random 32-character
  `secrets.token_urlsafe(24)` value, passes it only in the child's argv, and redacts it from the output. It is never
  printed, stored, committed or sent. `mustChangePassword` stays true.
- Jai sets his own password through **Forgot password** on the login page (`portal/src/pages/auth/ForgotPasswordPage.tsx`).
  The reset path works for every firm since the 2026-10-08 fix
  (`org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-10-08/kenny_password_recovery.md`). The server minimum is 12 characters.
- `--no-ses`: SES is in production access (`sesv2 get-account`: ProductionAccessEnabled true, 50,000/24h), so the
  recipient needs no verification. The script's `verify_email_identity` would send AWS mail to Jai: an outbound send
  that nobody confirmed, and it gains nothing.

## 5. Run plan

`create_user_v2.py --firm opal-capital --email jai@opalinvest.com --name "Jai Mukraj" --role user --no-ses`, once,
between ADVI1's BEFORE (Count 0) and AFTER (Count 1) email-index reads. Then one gateway `create_draft` to
Yang@opalinvest.com (username, firm/tier, the Forgot-password first step); nothing sent.

## 6. Result (measured)

- J1 source ruling: 1.0.0_SA_CTO~DELL1 msgs 9169/9171 (order amended @f83e33639e) accept the Opal-tenant calendar read.
  Source quoted: invite "OCIO IC", 2026-10-20 14:00-15:00Z, organizer Austin Graff <Austin@opalinvest.com>, optional
  attendee "Jai Mukraj" <Jai@opalinvest.com>, response accepted.
- ADVI1 BEFORE read: email-index Count 0 at 2026-10-21T17:00:16Z (msg 9172).
- J2: one run of `j123_insert.py` at 2026-10-21T17:00:49Z, rc=0: `USER#jai@opalinvest.com/PROFILE written
  (firm=opal-capital, tier=internal, role=user)`, `FIRM#opal-capital/MEMBER#jai@opalinvest.com written`,
  must_change=True, no SES call. The script's closing line "user receives SES email" is boilerplate; `--no-ses` sent nothing.
- J3: gateway `create_draft` to Yang@opalinvest.com, subject "Dashboard login for Jai is set up", created
  2026-10-21T17:01:03Z, `isDraft: true`, internetMessageId
  `<PH0P220MB050655A1CAC2C4316428FE6DBF662@PH0P220MB0506.NAMP220.PROD.OUTLOOK.COM>`. Nothing was sent.
- NOT EXERCISED: Jai's own Forgot-password reset and first sign-in (user journey); the draft names
  https://opalinvest.dev as the login page, which is INFERRED from the 2026-10-08 reset-endpoint log and not read from a
  route table. Andrew checks both before he sends.

## 7. Andrew-direct and the send

ANDREW-DIRECT, dell1 terminal to 4.0.0_SA_CRO~JAI1, 2026-10-21 ~17:0xZ, verbatim: "confirm the login URL from the portal
route config + once we know the account is good to go send the draft to yang"

Login URL, MEASURED (supersedes the INFERRED line in section 6):
- Route config: `portal/src/App.tsx:601-603` declares `/login`, `/forgot-password`, `/reset-password`;
  `portal/src/pages/auth/LoginPage.tsx:182-185` links "Forgot password?" to `/forgot-password`.
- Domain: `infra/aws/terraform/portal-auth/cloudfront-distribution.tf:110` aliases `opalinvest.dev`, `www.opalinvest.dev`;
  live `cloudfront get-distribution EVTSA9VEHNZVH`: Deployed, enabled, same aliases.
- Served: `https://opalinvest.dev/login` 200, `https://opalinvest.dev/forgot-password` 200.

Account good to go, MEASURED at 17:0xZ:
- `opal-users-v2` PROFILE: firmId opal-capital, tier internal, role user, status active, name "Jai Mukraj"
  (first Jai / last Mukraj), mustChangePassword true, mfaEnabled false / mfaChannel none; key set equals the script's
  contract. `FIRM#opal-capital/MEMBER#jai@opalinvest.com` present (role user). email-index Count 1.
- Reset path: `infra/aws/opalinvest_dev/lambda/auth-handler/src/auth.ts:644-669` `forgotPassword` looks up
  `getUser(email.toLowerCase())` with no firm filter; the stored email is lowercase. Sender domain `opalinvest.dev`
  SES identity: VerificationStatus Success.
- Still NOT EXERCISED: Jai's own reset and first sign-in.

SENT on Andrew's word: gateway `send_email` to Yang@opalinvest.com, subject "Dashboard login for Jai is set up", body
identical to the 17:01:03Z draft; Sent Items shows it at 2026-10-21T17:07:54Z. The 17:01:03Z draft still sits in
Drafts (the gateway has no draft-delete or draft-send tool); a second send from it would duplicate.
