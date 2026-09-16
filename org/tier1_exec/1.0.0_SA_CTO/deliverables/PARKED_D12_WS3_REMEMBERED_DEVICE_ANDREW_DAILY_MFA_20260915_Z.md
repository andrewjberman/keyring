# PARKED -- D12 WS-3, the 30-day remembered device, on Andrew's question about daily MFA

**Owner:** `1.0.0_SA_CTO~Z`, the D12 owner. **Parked:** 2026-09-15 ~20:3xZ. **Carrier:** this file, per CLAUDE.md "queued if not live is a
wish": the item sits here with its owner and the condition that un-parks it.

## The word, as relayed (not heard at this terminal)

Andrew-direct at the laptop `4.0.0_SA_CRO` seat on 2026-09-15, relayed by `0.0.0_AB_MSTR` (bus 838fa807) and `0.0.0_AB_MSTR~Z` (msg
23251), VERBATIM AND ENTIRE:

> I thought we had the cookies set up from the MFA that you only had to input them once a month, that they lasted for 30 days. I put in
> an MFA for Opal every single day, need to see why that is.

The original receiver's record is at that seat; this file does not restate it as this seat's record.

## The finding, as relayed (4.0.0_SA_CRO's source reads, NOT exercised, NOT re-read here)

1. **The 30-day remembered device is ruled but not built.**
   - Ruled: D12 WS-3, `ctoZ_ANDREW_DIRECT_20260831_2315Z_ALL_RECS_APPROVED_SES_DKIM_2FA_SELFTEST.md` @ `efcfa8cc5b`;
     `docs/architecture/D12_PLATFORM_OPS_PRD.md:21`, TTL 30 days, revocable by sign-out-everywhere.
   - Not built: `infra/aws/opalinvest_dev/lambda/auth-handler/src/mfa.ts:41-42` says "WS-3 (remembered device) IS NOT BUILT HERE".
2. **A full login still happens near-daily.**
   - The refresh cookie lasts 7 days (`auth-handler/src/index.ts:102`).
   - The portal logs out after 30 minutes idle (`portal/src/hooks/useActivityTracker.ts:15`), and that logout clears the refresh token.
   - So an idle gap ends in a fresh login. With WS-3 built, that login asks for the password but not a code.

## Why it is parked, and what un-parks it

- **Why:** Andrew set this seat's goal at ~19:2xZ: POSN_AGGFIX to validated completion, then the portal integrate, then `/prod-deploy`
  (record @ `15827b3991`). The relay states that sequencing is this seat's and sets no bar.
- **Un-parks when:** POSN_AGGFIX's goal steps are done, or Andrew moves this item ahead of it.
- **The next act when it un-parks:** re-read both findings at HEAD, then take WS-3 through the canonical flow against its ruled acceptance.
  Whether that is a new project, a workstream in an existing D12 project, or a cell is decided then.

## The one decision that is Andrew's, not this seat's

The 30-minute idle logout is a portal security-posture constant. Lengthening it would cut the login frequency on its own, and it is his
call. It is not folded into WS-3. `0.0.0_AB_MSTR~Z` offered to put it to him, and this seat asked it to do so (msg to `0.0.0_AB_MSTR~Z`,
~20:3xZ).
