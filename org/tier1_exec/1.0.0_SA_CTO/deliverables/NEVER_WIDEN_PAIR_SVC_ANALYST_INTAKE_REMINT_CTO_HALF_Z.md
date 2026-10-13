# OPAL_BBGTML R4 -- never-widen pair, CTO half: re-mint `opal/ticketing/svc-analyst-intake`, read the backlog, then the pin

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-13 ~20:5xZ.
**COO half:** `org/tier1_exec/2.0.0_SA_COO~ZB/deliverables/NEVER_WIDEN_PAIR_SVC_ANALYST_INTAKE_REMINT_COO_HALF.md`
@6338955a02 (read whole).
**Ask:** msg 33751.
**Authority:** this seat's ruling @61e3067f5c, disposition 4, and the YES in msg 33741.

## VERDICT: SIGNED, for exactly the COO half's section 4 blast radius

**May touch:**
- ONE new version of `opal/ticketing/svc-analyst-intake` via `put-secret-value` on the EXISTING secret. Never a new
  name, never `create-secret`, never `delete-secret`.
- On BRANCH ZERO only, line 11 of `integrations/ticketing/intake/runner_config.json`, set to
  `517aa5ee-b4d0-425a-b493-5a22ff77ac4f`. Nothing else in the file.

**The token:** claims EXACTLY the 08-20 set (`iss`, `aud`, `sub`, `userType`, `name`, `iat`/`nbf`, `exp` = iat + 30 days).
Adding `tier`, `firmId`, `role` or any page claim is a widening this half does NOT sign, and it STOPS the act.
`authz` and `scope_pin` are copied byte for byte. The signing key is read into memory only and never printed or written.

## All three branches, read from the producer's own rule

- **BRANCH ZERO (backlog read rc 0):**
  - the pin changes inside a change-management entry;
  - in the same act, `runner --dry-run` shows no `[TEAMS-IDENTITY-FAIL]` and no `FETCH_FAILED`, exit 0;
  - the next scheduled pass reads `intake pass exit 0` with `buzzed=0`.
  - A pass that posts while the read said zero is a rollback trigger.
- **BRANCH ABOVE ZERO (rc 1):** the pin is NOT touched, N and the cursor are recorded, and the post into the client
  ticket channel is Andrew's call. This seat puts it on the site Z open-calls list on receipt. The re-minted token
  stands: the scheduled runner still refuses at the pin before it fetches, so nothing is posted.
- **BRANCH UNKNOWN (rc 3 after the re-mint):** the pin is NOT touched; STOP, file a row, roll the secret back.

## Rollback, per key (as the COO half)

- **The secret:** move AWSCURRENT back to `77bf1488-d32c-4e17-96b6-18bf9b2d7638`. The new JWT's residual validity has
  the 08-20 token's reach, so it widens nothing.
- **The pin:** restore `"identity": "opalbloomberg"`.

## What this does NOT move

No IAM or reader grant, no `opal/auth/jwt-*` change, no other service subject, no cursor write, no Teams watcher or BG
pin change. Applier: `0.7.0_AE_CloudOps~ZT` (a site Z lane; no cross-box CloudOps).

**CTO half -- SIGNED.** `1.0.0_SA_CTO~Z`, 2026-10-13.
