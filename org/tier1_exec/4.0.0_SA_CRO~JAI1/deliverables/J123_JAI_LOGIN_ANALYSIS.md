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
