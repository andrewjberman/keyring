# OPAL_BBGTML R4 -- never-widen pair, COO half: re-mint `opal/ticketing/svc-analyst-intake`, read the backlog, then the pin

> **WITHDRAWN 2026-10-13 ~20:5xZ, both halves.** Andrew-direct (CTO msg 33761): "this is a function we are going to want to sort
> out eventually so that it works correctly, but it is not a priority right now + TCKT work is on DELL2 not here." Record
> `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_205xZ_TICKET_INTAKE_NOT_PRIORITY_TCKT_IS_DELL2.md`. TO-Z6-R4 is
> cancelled; nothing below was executed. The text stands as the record of what a later re-mint would need.

**COO half SIGNED by** `2.0.0_SA_COO~ZB`, 2026-10-13 ~20:4xZ. **CTO half: SIGNED** by `1.0.0_SA_CTO~Z`,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_PAIR_SVC_ANALYST_INTAKE_REMINT_CTO_HALF_Z.md` @6d8f802b36 (msg 33755): it
covers section 4's radius exactly; any claim beyond the 08-20 set STOPS the act; on BRANCH ABOVE ZERO, N and the cursor go to the
CTO, who lists the post at Andrew.

**Authority:**
- CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_OPAL_BBGTML_Z6_REPAIR_DISPOSITIONS_20261013_Z.md` @61e3067f5c,
  disposition 4;
- CTO msg 33741, "YES to your REC": R4 is one OPAL_BBGTML cell, in this order: re-mint at the EXISTING name with the same claims
  and scope as the 08-20 mint and a rotate_by stated; then the dry-run backlog read; then the oid pin, ONLY on a zero count or Andrew's word;
- row `OPAL_BBGTML-Z-S14` @ab46847ed4 (the expired token; this cell disarms it).

**Applier:** the site Z CloudOps lane the R4 task order names (`0.7.0_AE_CloudOps~ZT`). No cross-box act. This seat reads no private key.

## 1. Before-state (MEASURED 2026-10-13 ~20:3xZ, claims and metadata only, the token value never printed)

| item | value |
|---|---|
| secret | `opal/ticketing/svc-analyst-intake`, ARN `arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/ticketing/svc-analyst-intake-HGzn67` |
| versions | `77bf1488-d32c-4e17-96b6-18bf9b2d7638` AWSCURRENT; `a62fd884-c744-4263-9ca0-96ebcb459d84` AWSPREVIOUS |
| rotation | RotationEnabled None (no automatic rotation: the ONLY writer of the value is a hand mint) |
| JWT header | RS256, typ JWT |
| JWT claims | `iss` opal-portal-auth, `aud` opal-portal-api, `sub` svc-analyst-intake, `userType` service, `name` "Opal Analyst Intake (service)", `iat`/`nbf` 2026-08-20T20:03:28Z, `exp` 2026-09-19T20:03:28Z |
| value JSON fields | token, sub, userType, authz, scope_pin, iss, aud, minted_at, expires_at, rotate_by, minted_by |
| live effect | the portal API answers the fetch HTTP 403 (r4_backlog_read.py rc=3, 2026-10-13 ~20:30Z) |

**Writers of the named properties, counted.** The secret value: 1 writer (a hand mint; RotationEnabled None). The pin
(`integrations/ticketing/intake/runner_config.json` `gateway_pin.identity`): 1 writer (a hand edit; the file is read, never
written, by the runner). N = 2 rules read, both hand acts inside this cell.

## 2. The token, exactly

Claims EXACTLY the 08-20 set and no other: `iss` opal-portal-auth, `aud` opal-portal-api, `sub` svc-analyst-intake, `userType`
service, `name` "Opal Analyst Intake (service)", `iat` now, `nbf` = iat, `exp` = iat + 30 days. NO `tier`, `firmId`, `role`,
`advisorId`, `allowedPages`, `allowedTabs` or `firmRole` (the 08-20 token carries none, and adding one is a widening). RS256, signed
with the CURRENT value of `opal/auth/jwt-private-key`, read into memory and never printed or written (method of
`org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/pk_mint/mint_packager.py`).

**The value JSON:** `token` = the new JWT; `minted_at` / `expires_at` (= exp) / `rotate_by` (= iat + 21 days, the 08-20 spacing) new;
`minted_by` "0.7.0_AE_CloudOps~ZT (OPAL_BBGTML R4, CTO~Z msg 33741)"; `sub`, `userType`, `authz`, `scope_pin`, `iss`, `aud` copied
byte-for-byte from the current value. The description's dates are updated; nothing else in the description changes.

**The write:** `put-secret-value` on the EXISTING secret (a new version becomes AWSCURRENT, the expired one AWSPREVIOUS). Never
`create-secret`, never a new name (rule 30), never `delete-secret`.

**Rotation:** owed by `rotate_by`. Owner: the OPAL_BBGTML COO lane, carried in this round's drain-end message as an open item.

## 3. Order -- one act, three steps

1. **Re-mint.** Before-read the versions table above; a different AWSCURRENT id means another writer moved it: STOP. Mint per
   section 2, `put-secret-value`, then read back: decode the stored token WITHOUT verifying; the claim set equals section 2 exactly
   and `exp - iat` = 30 days. Then one fetch: `GET {api_base}/api/scoped/tickets?status=open&limit=1` with the new token answers 200.
2. **Backlog read.** `python org/tier1_exec/2.0.0_SA_COO~ZB/deliverables/z6_checks/r4_backlog_read.py` (dry-run production pass,
   send stub that raises, counts only). Record its whole output.
3. **The pin, by branch -- BOTH branches are covered by this half:**
   - **BRANCH ZERO (`BACKLOG: ZERO`, rc 0):** open a change-management entry, set `gateway_pin.identity` to
     `517aa5ee-b4d0-425a-b493-5a22ff77ac4f` (line 11, nothing else in the file), and in the SAME act run
     `python -m integrations.ticketing.intake.runner --dry-run` from the repo root. The producer's own rule (`runner.py` `exit_code`
     + `main`): no `[TEAMS-IDENTITY-FAIL]` and no `FETCH_FAILED` line; exit 0 (6 = the sweep's own fault, a row, not a rollback). Then
     read the next scheduled pass in `%USERPROFILE%/opal_ticket_intake/runner.log`: `intake pass exit 0` with `buzzed=0`. Close the entry.
   - **BRANCH ABOVE ZERO (`BACKLOG: N`, rc 1):** the pin is NOT touched. The cell stops, records N and the cursor, and reports. The
     call is Andrew's (a post into the client ticket channel). The re-minted token stands: harmless, because the scheduled runner
     still refuses at the pin (exit 2) BEFORE it fetches, so nothing is posted.
   - **BRANCH UNKNOWN (rc 3 after the re-mint):** the pin is NOT touched; STOP, file a row, roll the secret back (below).

## 4. Blast radius and rollback

**May touch:** the one secret above (one new version) and, on BRANCH ZERO only, line 11 of `runner_config.json`. Nothing else.

**Rollback, per key:**
- the secret: `aws secretsmanager update-secret-version-stage --secret-id opal/ticketing/svc-analyst-intake --version-stage AWSCURRENT
  --move-to-version-id 77bf1488-d32c-4e17-96b6-18bf9b2d7638 --remove-from-version-id <new id>` (the expired token returns; the intake
  is no worse than before). The new JWT stays valid until its exp unless the signing slot rotates; its reach is the 08-20 token's
  reach, so that residue widens nothing;
- the pin: restore `"identity": "opalbloomberg"` (the runner returns to exit 2 within 5 minutes).

**Triggers:** a claim mismatch at read-back; the step-1 fetch not 200; a pass that posts while the backlog read said zero; a CTO or
Andrew word.

## 5. State coherence -- what this does NOT move

No IAM, no reader grant (site Z's identity already reads this secret: LastAccessed 2026-10-12), no change to `opal/auth/jwt-*`, no
other service subject, no authorizer or opal-ticket-api change, no change to the cursor item, no CREATE enablement (`authz` copied
unchanged). The Teams watcher and the BG seat's pin are untouched.

**COO half -- SIGNED.** `2.0.0_SA_COO~ZB`, 2026-10-13.
