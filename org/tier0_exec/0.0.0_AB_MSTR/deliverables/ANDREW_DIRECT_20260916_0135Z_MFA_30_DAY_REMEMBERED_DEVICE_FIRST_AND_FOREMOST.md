# ANDREW-DIRECT 2026-09-16 ~01:35Z -- the 30-day remembered device is to be handled FIRST AND FOREMOST

**Channel:** Andrew, directly, at the `0.0.0_AB_MSTR` terminal (laptop).
**Time received:** 2026-09-16 ~01:35Z.
**Received by:** `0.0.0_AB_MSTR`.

## His word, VERBATIM AND ENTIRE (the MFA portion of a longer message)

> I also want to know who was in charge of the login cookie expiry. I thought we had designed MFA in
> a manner where the user is remembered for a period of 30 days from login, it is obnoxious to have
> to do it every time. I want that handled first and foremost.

The rest of the same message concerns `/integrate parity` and a 50-commit gate on the two remotes;
it is recorded separately and is NOT part of this item, on his own ordering ("first and foremost").

## THIS IS THE SECOND TIME HE HAS ASKED TODAY

`4.0.0_SA_CRO` was asked the same question at its own terminal earlier on 2026-09-15 and relayed it
at ~20:19Z (msg 97227). His words then, VERBATIM:

> I thought we had the cookies set up from the MFA that you only had to input them once a month, that
> they lasted for 30 days. I put in an MFA for Opal every single day, need to see why that is.

⚠ **The CRO's relay was correctly PARKED rather than dispatched, because `1.0.0_SA_CTO~Z` -- the D12
owner -- was reported down at ~16:2xZ. THAT SEAT IS NOW LIVE** (it ran the POSN_AGGFIX DEV->PROD
promote at ~01:18Z and posted FREEZE CLOSED). **So the condition that parked the item has cleared,
and the item is deliverable.** He should not have had to ask twice, and the reason he did is that the
owner was down, not that the finding was missing.

## WHO WAS IN CHARGE -- his actual question, answered

| | |
|---|---|
| **The work item** | **D12 WS-3, "remembered device"** |
| **Owner / builder** | **`1.0.0_SA_CTO~Z`** -- D12 owner, placement **SITE Z**, closed by his own ruling |
| **Who ruled the 30 days** | **Andrew**, 2026-08-31 ~23:15Z, "all recs approved" -- recorded by `1.0.0_SA_CTO~Z` at `ctoZ_ANDREW_DIRECT_20260831_2315Z_ALL_RECS_APPROVED_SES_DKIM_2FA_SELFTEST.md` @`efcfa8cc5b` |
| **Where it is written down** | `docs/architecture/D12_PLATFORM_OPS_PRD.md:21` -- TTL **30 days, revocable by sign-out-everywhere**, listed under **CLOSED by his ruling** |
| **Where it was to be built** | `auth-handler`, CLOSED by the CTO arch-gate under that PRD's own decision #3 (WS-2) |

**So nobody mis-set a cookie expiry. The 30 days he remembers is real, it is ruled, it is written in
the PRD -- and the code to honour it was never written.** The design is not wrong; the build is
absent.

## WHY HE GETS MFA EVERY DAY -- verified at source by this seat, not taken on the CRO's report

The CRO's finding was explicitly "source reads, not exercised". Each leg was re-read here at
`origin/CLOUD` `ac36792590` (portal legs at the local `portal/` DEV checkout `acdb02e917`):

1. **The remembered device does not exist.**
   `infra/aws/opalinvest_dev/lambda/auth-handler/src/mfa.ts:41-43`, in the module's own header:
   > *"WS-3 (remembered device) IS NOT BUILT HERE. Its TTL is settled at 30 days, revocable by
   > sign-out-everywhere; no remembered-device state is written, read or referenced by this module."*
   **The code says of itself that it is unbuilt.** So every full login asks for MFA.

2. **A full login happens about daily, by a three-part chain nobody designed as a whole:**
   - `portal/src/hooks/useActivityTracker.ts:15` -- `IDLE_THRESHOLD_MS = 30 * 60 * 1000`, a **30-minute** idle threshold.
   - `portal/src/contexts/AuthContext.tsx:288-313` -- on the active->idle transition a warning countdown starts, and at zero it calls `logoutRef.current()`.
   - `AuthContext.tsx:582` -- that logout calls `POST /auth/logout`, which **clears the refresh token**.
   - `infra/aws/opalinvest_dev/lambda/auth-handler/src/index.ts:101-103` -- the refresh cookie is `Max-Age = 7 * 24 * 60 * 60`, **7 days** -- and it never gets to spend them, because the idle logout deletes it first.

   **The 7-day refresh cookie is not the binding constraint. The 30-minute idle logout is.** Thirty
   idle minutes discards a seven-day credential, and with no remembered device behind it the next
   visit is a full login and a fresh code.

3. **What WS-3 actually fixes, stated precisely so the fix is not oversold:** WS-3 removes the
   repeated **MFA code**. The idle logout would still ask for the **password**. If he wants the idle
   logout itself changed, that is a SEPARATE decision and is HIS -- it is a security control, not a
   defect, and this seat is not touching it on inference.

## Scope -- what this seat did and did NOT do

- **DID:** verified all four legs at source; recorded this; relayed to `1.0.0_SA_CTO~Z` (LIVE) over
  the agentbus with his words verbatim and the CRO's prior finding attached, marked as the second
  asking.
- **DID NOT:** build it, schedule it, or set an acceptance. D12's placement is SITE Z and the owner
  is live; MSTR does not take a Tier-1 seat's work item because the sovereign is impatient.
- **DID NOT:** touch the idle timeout, the refresh cookie TTL, or any auth code.
- **NOT ADJUDICATED:** whether "handled first and foremost" re-orders `1.0.0_SA_CTO~Z`'s own queue
  against work it holds that this seat cannot see. His words go over verbatim; that seat orders its
  own queue or asks him.
