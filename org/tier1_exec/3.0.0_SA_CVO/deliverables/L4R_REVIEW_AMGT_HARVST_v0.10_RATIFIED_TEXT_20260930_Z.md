# L4-R ratified-text review -- AMGT_HARVST v0.10 @d0bc0a79f0 (CONTRACTS only: the `bot_check` line)

**Reviewer:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~17:2xZ - **Asked by:** CTO~Z msg 27285
**Span:** from this seat's own signed bytes (v0.9 @`e1b5fd6d8c`) to `d0bc0a79f0`. The ENDPOINT hash is `974dada544a2` at both, so there is
**no ENDPOINT change**. The only addition is one bullet under `C-HV-TRUST-TOKEN`.

## CHECKS

1. **It answers the ask it cites (ADJUDICATION_v38 s.2).**
   - `bot_check` becomes an attempt class, keyed on a named signature: DataDome `captcha-delivery.com`, FT "Security
     Verification", or bbg press-and-hold. The matched signature's name is written beside the class.
   - It never marks a token expired and never starts a sign-in or crawl, so it cannot fall through to the crawl Andrew said to
     avoid.
   - It stops the publisher's leg, with no retry against a check. That agrees with the round-29 CTO half's condition (ii): an
     interactive challenge is Andrew's login, never bypassed or retried.
   - A new signature comes only from a kept body, never inferred.
2. **Faithful to Andrew's record** (the v0.9 review's source). "Important to not confuse rate limit for trust token expiry" extends
   naturally to a bot check. No clause contradicts his words.
3. **Agreement with ENDPOINT:** unchanged.

## VERDICT: SIGN

**One gap, material for the round-30 build cell, not a condition on this text.**
- The last clause reads expiry as "an auth failure that persists after backoff whose kept body matches no bot-check signature".
- A refusal with **no kept body** satisfies "matches no signature" vacuously.
- Round 29 kept bodies for wsj (652 B) and ft (65,536 B) only. The bbg 403 and barrons 401 rows show none (the ROUND29 packet table,
  "refusal body: --").
- So under this text as written, a persistent bbg or barrons refusal would still read as expiry.
- **The fix (one line, v0.11 or the cell's spec):**
  - every refusal keeps its body, bounded as ft's F1 already is;
  - a refusal with no kept body is classed `unclassified`, and is never read as expiry.
