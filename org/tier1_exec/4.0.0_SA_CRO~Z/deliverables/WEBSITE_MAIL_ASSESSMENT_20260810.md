# Opal Website mail-failure assessment — Patricia's 2026-08-10 email

**Author:** 4.0.0_SA_CRO~Z · **Date:** 2026-08-10 ~22:35Z · **Trigger:** Andrew-direct (Patricia/TWLC email + WP Mail SMTP failure banner + form-entries screenshot)
**archetype:** DIAGNOSE

## Verdict

**The site is functioning properly and the contact form IS delivering to Andrew.** The failure banner is real but scoped: while SES is in sandbox, mail to any **non-SES-verified recipient** is rejected. The failing sends today were to the developer's own two addresses, not to Opal.

## Evidence (all live 2026-08-10)

1. **Site up:** `opalinvest.com` HTTP 200, LiteSpeed, WP serving — our EC2 `i-0152e3fe2599fa630` (NFRA_WEBSITE, `infra/website/RUNBOOK.md`).
2. **Mail path (as designed 07-10, Andrew-direct "SES sandbox -> Opal"):** PHP `mail()` → `ses-sendmail` shim → SES `send-raw-email` via instance role, sender forced to `noreply@opalinvest.dev` (DKIM `d=opalinvest.dev`, Rule-23-compliant). **Patricia's developer's premise (raw PHP mail, blocked/spam, "needs SMTP2Go") is factually wrong for this site** — mail already leaves via an authenticated, DKIM-aligned relay.
3. **Shim log (`/var/log/opal-website-ses-sendmail.log`, via SSM):** steady OK deliveries all month; **2026-08-10 21:21:45Z + 21:21:47Z — the exact minute of Patricia's 5:22 PM ET screenshot — two `MessageRejected: Email address is not verified` errors, recipients `mike@hirst.digital` and `mike@extonwebdesign.com`.** That is the banner's "last email unsuccessful."
4. **SES account:** `ProductionAccessEnabled=false` (sandbox, 200/day, sent 3/24h). Verified: `andrew@opalinvest.com` ✅, domain `opalinvest.dev` ✅. `info@opalinvest.com` was **Failed** (07-10 verification link never clicked, expired) — **re-initiated today, now Pending**; `mike@hirst.digital` Failed.
5. **Contact form (GF form 1) notifications:** both resolve to `andrew@opalinvest.com` (`{admin_email}` — the W3 admin_email gate DID land — plus a literal andrew@). Both recipients verified → the paired OK sends on 08-02/07/09 in the log are form notifications delivering. **No lead notification is currently failing.**
6. **Entries stored regardless:** 5 entries in GF DB (4 obvious bot gibberish + Patricia's test). Nothing is lost even when a notification fails.
7. WP admins: opaladmin(andrew@), mike(mike@extonwebdesign.com), patricia@, Lindsay@ — the failing sends were user-level mail (password-reset/test class) to mike's unverified externals.

## Plan of action (what / how / who)

| # | What | How | Who / gate |
|---|---|---|---|
| 1 | **Click the SES verification link** now in `info@opalinvest.com`'s inbox (re-sent today) | One click; makes info@ a deliverable recipient in sandbox | Andrew (or whoever holds info@) |
| 2 | **Submit the SES production-access case** — the real fix; lifts recipient-verification entirely | Case is fully drafted at `infra/website/SES_PRODUCTION_ACCESS_CASE_DRAFT.md` (corrected 07-13); ~24h AWS turnaround | **Andrew's word required** (outward-facing; never on agent authority) |
| 3 | **Do NOT sign up for SMTP2Go** | Redundant third-party vendor; would require editing the ONE live SPF TXT on `opalinvest.com` (M365 firm mail — RUNBOOK §"GRADUATE" hazard: two SPF records = permerror, firm-wide mail damage); the working SES path already exists | Recommendation to Patricia — Andrew relays |
| 4 | **reCAPTCHA on the form: yes** — Patricia's instinct is right (4/5 entries are bots) | Cloudflare Turnstile (account already exists per RUNBOOK) or GF's native reCAPTCHA add-on; her implementation call | Patricia/TWLC |
| 5 | *(Separate, later, gated)* sender graduation `opalinvest.dev` → `no-reply@opalinvest.com` | SES domain identity + 3 DKIM CNAMEs + **edit** of the single SPF TXT — its own scheduled mail change with header verification, never bundled | Andrew + CTO/COO co-sign (touches live firm mail) |

Explicitly NOT in plan: any bounce/complaint SNS/alarm build (moratorium, Andrew-direct 2026-07-28).

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-find | `"18.208.18.213"` | located `infra/website/` estate docs (49 hits, denominator printed) |
| comp-find | `"wordpress" infra` | located `infra/aws/terraform/website/` |
| live primitives | nslookup (A/NS/TXT/MX/DKIM ×2 domains), curl site, `sesv2 get-account`, `ses get-identity-verification-attributes`, SSM RunCommand ×5 (shim log, admin_email, GF notifications, wp users) | all rail-checked where inspection-class; grounded every claim above |
