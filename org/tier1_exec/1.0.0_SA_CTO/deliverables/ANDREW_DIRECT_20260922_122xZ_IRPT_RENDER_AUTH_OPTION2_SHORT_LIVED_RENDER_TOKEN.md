# ANDREW-DIRECT -- 2026-09-22 ~12:2xZ -- IRPT renderer authentication: Option 2 (short-lived scoped render token)

**Where:** the `1.0.0_SA_CTO` terminal.

## Andrew's words, verbatim

> "Option 2 is preferable"

## What he was answering

He first asked: *"Why can we not just design a service account now and you go run these steps?"*

This seat set out two options, plus a stopgap:

- **Option 1:** a dedicated portal user with MFA off. Its password is held in Secrets Manager, and the renderer logs in with it on each run.
- **Option 2:** the render job mints a short-lived JWT for each run. The token has a TTL of minutes, a new narrow `renderer` role, and is signed with a key held in Secrets Manager. Only the print route, and the data APIs that route reads, accept it. There is no password, no MFA bypass, and nothing long-lived.
- **Stopgap:** a one-time human capture to unblock testing while Option 2 is built.

## What led here

- The portal's refresh token lives for 7 days (`infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts:18`). A human-captured session would therefore expire every week.
- Andrew shared browser recordings of the ycharts.com and opalinvest.dev logins. Both contain his password in plaintext. Neither was used, and this seat advised deleting both.

## Operative consequence

1. The IRPT_BCKEND authenticated-render mechanism is **Option 2**. The human-captured session is no longer the standing path for exports.
2. **Research first.** `4.0.0_SA_CRO` researches the specifics before this seat writes the PRD addendum. That research was already requested at ~12:20Z and acknowledged. It covers:
   - every token verifier;
   - any existing machine identities;
   - the exact API routes the print page reads;
   - the signing key and whether to use a separate key;
   - the risks.
3. **PRD addendum.** This seat then amends the IRPT_BCKEND PRD. The addendum re-opens only the halves it changes, under the L4-R sign-off. `2.0.0_SA_COO~B` cuts round 17 on it.
4. **IB-rti-6** (the latency measurement) is re-cut to run on the render token instead of a captured session.
5. **The human capture ask is WITHDRAWN** as the standing path. Andrew may still run it once if he wants an earlier latency number, but it is no longer required.
6. **Security gate.** Auth changes are security-critical. They take the normal build path, CVO grading, and never-widen halves for any deploy.

**Scope:** IRPT render authentication only. This does not create any general machine-identity policy.
