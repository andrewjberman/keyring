# ANDREW-DIRECT 2026-09-16 ~03:2xZ-03:3xZ -- D12 WS-3 spec restated, and the BUILD assigned to `0.0.0_AB_MSTR`

**Channel:** Andrew, directly, at the `0.0.0_AB_MSTR` terminal (laptop). Three consecutive messages.
**Received by:** `0.0.0_AB_MSTR`.

## 1. ~03:2xZ -- the third asking, VERBATIM AND ENTIRE

> Did anyone fix the MFA? I have logged in on the same computer multiple times a day and i keep having
> to do mfas, that is bullshit.

Answered NO, re-measured at `origin/CLOUD` `a8f204882b`: `mfa.ts:41-42` still declared WS-3 unbuilt; a
scoped census of the whole `auth-handler` for any implementation identifier returned **0 hits across 35
files**; and **16 commits had touched `auth-handler/` since his 2026-08-31 ruling** without building it.

## 2. ~03:2xZ -- THE SPEC, VERBATIM AND ENTIRE

> Let me explain what is supposed to happen here. The issue at hand is that when a user logs in through
> MFA, they should receive a long-standing cookie that is attached to that device. The purpose of this is
> so a device becomes trusted for a extended duration. That is what we are trying to achieve here. It has
> absolutely nothing to do with the expiry period of the OTP. I am referring to a long-standing cookie
> that the user receives. Does passing them through MFA. So they need to only enter a password pending
> that they have an unexpired longer term cookie, which they receive post successful MFA.

This is the contract the build is graded against. The distinction he draws -- a long-lived DEVICE cookie
issued on MFA success, versus the OTP challenge lifetime -- is exactly the one that had been missed:
`f4659653e8` tuned the OTP TTL in the very file whose comment says that constant is "NOT THE WS-3
CONSTANT".

## 3. ~03:3xZ -- THE BUILD ASSIGNMENT, VERBATIM AND ENTIRE

> you are going to be the one who builds it, start now.

Said in reply to this seat's four-point delta against `index.ts`. **This supersedes the D12 PRD's
placement (SITE Z) and owner (`1.0.0_SA_CTO~Z`) FOR THE BUILD ONLY.** It says nothing about who gates it.

## What followed, in order

- `0.0.0_AB_MSTR~Z` had just relaunched `1.0.0_SA_CTO~Z` (03:28:06Z) on this seat's infra ask. This seat
  told that lane over the bus, within minutes, that Andrew had assigned the build here -- ONE builder, not
  two -- and asked it to act as the CTO arch-gate instead.
- **Andrew then killed `1.0.0_SA_CTO~Z`** (~03:4xZ, at the site-Z terminal, VERBATIM to `~Z`: *"Did that
  agent actually do any work? I killed it the moment i saw MSTR base make a comment about it"*). `~Z`
  measured its lifespan at ~4 minutes, entirely inside startup: **no commits, `auth-handler/` untouched,
  no competing build.** `~Z` did not re-spawn it and was right not to.
- **Consequence: the build lands UNGATED by a CTO.** Stated plainly rather than assumed away. The options
  (re-seat that lane on his word; name another grader; accept ungated) are his.

## What this seat built, to the spec above -- `LD-0573`

A trusted-device cookie, minted ONLY on `/auth/mfa/verify` success, read at `/auth/login` to skip the
challenge for THAT account on THAT browser inside a fixed 30-day window (his 2026-08-31 ruling, PRD:21),
revocable by a new authenticated `POST /auth/logout-everywhere` (PRD:259's own word) and by the two
admin compromise-response paths, and **deliberately NOT cleared by `/auth/logout`** -- the route the
portal's 30-minute idle timeout calls. Storage is the existing `opal-portal-auth-mfa` table under its
own key prefixes (no shadow store); revocation is a per-account generation counter because the Lambda's
IAM has no `Query` on that table and there is no GSI.

**NOT done by this seat:** the deploy. Code is committed and pushed; the Lambda is fed from an S3
artefact via Terraform (`portal-auth/lambdas.tf:7-22`, built by `build-nodejs-lambda.sh`), which is a
ledgered served-surface act and waits on his word.
