# ANDREW-DIRECT — 2026-09-01 ~00:20Z — test 2FA on his own account, using the Graph mailbox as the reality check

**Received by:** `0.7.0_AE_CloudOps~Z` · **Channel:** direct terminal message to this seat, mid-turn
**Recorded:** 2026-09-01T00:22Z · **Broadcast:** same turn, MCP to COO~Z / CTO~Z / MSTR~Z

## VERBATIM — two messages, in order. The phrasing is the ruling; this is not a paraphrase.

> **"test it on me, andrew@opalinvest.com, you should have access to my email via opal-gateway graphAPI"**

> **"that is easiest mechanism to test reality"**

## What it settles

1. **It authorises MFA on his LIVE account**, not a stand-in. Until this message the TO's §5 carried
   only his earlier *"we will want to do the testing for 2FA on my account so we know it works before
   pushing anything to clients"* — an ORDERING. This is the direct instruction to act on that account.
2. **It names the instrument**: the `opal-gateway` Microsoft Graph mailbox surface, which this seat
   holds and which reads `Andrew@opalinvest.com`.
3. **"test reality"** is the operative half. It reads as a preference for an end-to-end observation on
   a real mailbox over any closer-in proxy.

## What I did on it, same turn

- Set `andrew@opalinvest.com` (`USER#usr_7f83e30de95f`, role `admin`) to `mfaChannel='email'`,
  `mfaEnabled=true`. **Read back and confirmed**: before `{'mfaChannel': 'none', 'mfaEnabled': False}`,
  after `{'mfaChannel': 'email', 'mfaEnabled': True}`.
- **His next portal login now requires a code emailed to `andrew@opalinvest.com`.** That is the
  intended effect and he asked for it; it is recorded here so nobody has to infer it from a table.

## ⚠ THE ONE THING THIS INSTRUCTION DOES NOT GIVE ME, STATED PLAINLY

**I do not hold his password, so I cannot drive the login leg of his account myself.** The password
check happens before the OTP is issued, so the full loop on HIS account needs him to type it once.
What I could and did prove without it, on a controlled test account whose mail lands in the same
mailbox: challenge issued, code emailed, wrong code rejected, correct code accepted, replayed code
rejected, dashboard unreachable before and reachable after.

⛔ **I did not consider changing or resetting his password to close that gap.** An instruction to test
on an account is not an instruction to take it over, and a login I could complete alone would not have
tested the thing he asked about.

## Scope — surfaced, not adjudicated

This seat does not widen his word. It names his account and this test; it is **not** read as
authorisation to enable MFA for any other user, and no other account was touched. Every one of the
other 48 profiles remains `mfaChannel='none'`, which is the OFF state.
