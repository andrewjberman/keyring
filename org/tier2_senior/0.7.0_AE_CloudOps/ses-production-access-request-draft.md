# SES Production-Access Request -- STAGED (awaiting Andrew account-owner GO)

**Status:** drafted, ready to file. Do NOT file until Andrew (AWS account owner) says go.
**Owner:** 0.7.0_AE_CloudOps. **Date staged:** 2026-06-25.
**Account:** 313476888478. **Region:** us-east-1 (where the identities + Lambdas live).

## Why (dual-use -- one case unblocks two things)
SES us-east-1 is in SANDBOX (`ProductionAccessEnabled=false`): it can only send to VERIFIED
recipients. That currently blocks:
1. **OTP-gateway liveness alert -> Andrew** (PREMCP P1c): the SES app-level alert channel can't
   reach andrew@opalinvest.com until it's verified / prod-access lands.
2. **ETFS month-end morning-brief email -> Andrew** (0.5.0, first fire 2026-07-01): same sandbox
   limit caps the report recipient list to verified addresses.

Production access removes the per-recipient verify requirement entirely -> both go click-free.

## How to file (Andrew, or me on his GO)
AWS Console -> SES -> Account dashboard -> "Request production access"
(or Support -> Create case -> Service limit increase -> SES Sending Limits).

## Case content (paste-ready)
- **Mail type:** Transactional.
- **Website URL:** https://opalinvest.dev (+ https://mcp.opalinvest.dev for the gateway).
- **Use case description:**
  "Opal Capital sends two low-volume internal transactional emails from its own verified domain
  (opalinvest.dev) to its own staff: (1) automated infrastructure liveness alerts to an internal
  operator when an auth token lapses, and (2) a once-monthly internal portfolio report (PDF) to
  internal recipients on the 1st of each month. All recipients are internal Opal Capital staff who
  have explicitly requested these messages. No marketing, no external/third-party recipients, no
  purchased lists."
- **How recipients sign up / consent:** Internal staff only; recipients are configured by the
  account owner. Not a public sign-up.
- **How bounces/complaints are handled:** Volume is very low (a few/month + occasional alerts).
  Bounces and complaints are monitored via SES event notifications; any hard-bounce address is
  removed from the recipient config immediately. We will configure an SNS bounce/complaint topic.
- **Expected volume:** < 100 emails/month.
- **Compliance:** All mail FROM the verified opalinvest.dev domain (DKIM-signed). Recipients are
  internal and consenting; unsubscribe is handled by removing the address from config.

## After prod-access lands (my follow-ups)
- Confirm `ProductionAccessEnabled=true` (`aws sesv2 get-account`).
- Liveness SES alert to andrew@opalinvest.com then delivers without the verify step.
- Notify 0.5.0 (ETFS report recipient list no longer needs each recipient verified).
- (Recommended) wire an SES bounce/complaint SNS topic per the case commitment.
