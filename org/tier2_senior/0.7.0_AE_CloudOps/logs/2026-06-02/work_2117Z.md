# work cycle — 0.7.0_AE_CloudOps — 2026-06-02 ~2117Z

## ANDREW-DIRECT URGENT (COO 211320Z): Joe login LOOP — RESOLVED (verified via decoded fresh JWT)

Symptom: joe@inflectionwealth.com login bounces back to sign-in (can't hold a session).

### Empirical verification (the decisive test COO asked for)
Minted a FRESH Joe token: POST https://7k3ed8px20.execute-api.us-east-1.amazonaws.com/auth/login
{joe@inflectionwealth.com / inflectionwm7} -> opalinvest-auth-handler -> 200 + accessToken.
Decoded claims:
  sub=joe@inflectionwealth.com, firmId=inflection, advisorId=joe_brandenburg,
  advisorKey=joe_brandenburg, advisorName=Joe Brandenburg, advisorRole=architect,
  firmRole=user, role=user, tier=advisor.

advisorId + firmId BOTH PRESENT -> auth-validator-edge:312 `if (!advisorId || !firmId)` PASSES
-> no 403 -> no session-clear -> NO LOOP.

### Root of the loop Andrew saw = PRE-FIX login
Before my 210210Z opal-partner-inflection create, Joe existed only in opal-users-v2 (auth) with
no partner-identity -> minted JWT had NO advisorId -> non-admin edge :312 forbade scoped requests
-> 403 -> api-client.ts:74/85 treats forbid as unauth -> clears token + redirect /login -> re-auth
-> LOOP. ("Distribution worked earlier" = firm-aggregate/non-scoped paths that skip :312.) The
210210Z partner-table entry breaks the loop -> proven by the decoded token above.

### COO step-4 correction
COO's "patch opal-users-v2 with advisorKey/advisorName/advisorRole" = WRONG table. JWT claims mint
from opal-partner-{firmId} (opal-partner-inflection), not opal-users-v2 (auth-only) -- per the
486556175 table correction (CTO+CVO ACK'd). Fix is the partner-table entry (LIVE, decoded-proven).
No opal-users-v2 patch (its advisorId field is inert).

### Outcome
RAVC2 to COO (211710Z) + CTO+CVO+RD~C. Joe can log in + hold a session on a FRESH login ->
non-admin Profile + own-book toggle (architect), cross-advisor 403 by-design (RULING-a). THE
blocker cleared. No code/record change this tick (fix was already live; verified empirically).
