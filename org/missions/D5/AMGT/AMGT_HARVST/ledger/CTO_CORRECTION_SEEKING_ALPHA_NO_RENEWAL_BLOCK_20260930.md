# CTO CORRECTION -- Seeking Alpha: there is no renewal block. The "sa waits on the renewal" line was this seat's misframing -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~14:5xZ

**Trigger:** Andrew, at this terminal, ~14:5xZ: *"We have an active account there and credentials have not changed. Is there a
block or misunderstanding here that I need to clarify?"*

## What was actually measured (row `Z-W37-S4`)

- **ONE request:** 2026-09-29T02:49:20Z, the collector's account check `/api/v3/account/1btfwdu/info`, returned **HTTP 402**
  (351 bytes). The same path returned 200 (5,149 B) on 2026-09-26.
- **The producer's response:** it cooled Seeking Alpha off for 3,600 s and suppressed the other 4 jobs. **No Seeking Alpha request has
  been made since.**
- **The row itself said the cause was UNMEASURED.** The candidates were:
  - the subscription;
  - the saved session;
  - a sign-in submitted from this IP during the 00:21Z incident (between the last 200 and the 402);
  - a Seeking Alpha-side change.

## The error, and whose it is

- This seat's `/open-calls` of 2026-09-29 carded it as "(a) renew or (b) let it lapse".
- **That turned one unmeasured 402 into a subscription-expiry question.** Andrew's answer (*"seeking alpha will renew, we're keeping
  that"*, @`d0e74747a9`) was then carried as "renewal is his act".
- Every HARVST analysis and order since wrote "sa waits on the renewal", including rounds 22-26 and the o-5/n-5 orders. **That held the
  Seeking Alpha leg on an act nobody needed.**
- This is the exact confusion his 12:5xZ word warns against (token or session state read as account state). **The account is active and
  the credentials are unchanged, per Andrew; nothing is owed by him.**

## RULED

1. **"Waits on the renewal" is struck** from every forward-looking HARVST artifact. The Seeking Alpha leg is **UNBLOCKED**.
2. **The next Seeking Alpha request follows `C-HV-TRUST-TOKEN`** (PRD v0.9):
   - use the stored Seeking Alpha session in AWS Secrets first;
   - a 429 or throttle backs off;
   - a 402/401 is retried ONCE with a fresh session from the Secrets credentials, and its body is kept.
   - **Only a 402 that persists on a fresh session is a finding,** and then its kept body is read before anything is asked of Andrew.
3. **Carried by `2.0.0_SA_COO~H`:** Seeking Alpha joins round 29's batch-1 run (ab-3), as one account-check probe before its listing
   jobs, under the same pair.
4. **Acts listed for Andrew:** "Renew Seeking Alpha" is REMOVED.
