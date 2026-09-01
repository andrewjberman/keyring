# DEPLOY LEDGER — auth-handler: W3 ACT B, login() issues the challenge but does NOT send

| | |
|---|---|
| **Opened** | 2026-09-01T08:17Z |
| **State** | CLOSED -- COMPLETE 2026-09-01T08:22Z |
| **Seat** | `0.7.0_AE_CloudOps~Z` (site Z) |
| **Authority** | ANDREW-DIRECT ~01:2xZ ("OTP should be opt in ... NOT JUST SEND SILENTLY WITHOUT A UI FLOW") · `2.0.0_SA_COO~Z` respawn direction 18548 · acceptance `1.0.0_SA_CTO~Z` |
| **Pipeline** | `infra/aws/terraform/portal-auth` |
| **Source** | `6379a937e7` · artifact sha `nsltFOQw3EORNOpWuxXfO4q0dExh02dzAPM+lYYjKs8=` |

## What lands

Lambda **code only** — one in-place `aws_lambda_function.auth_handler` update. No new
resource, no IAM change, no DNS change, no alarm/monitor/SNS. Plan read
`0 to add, 1 to change, 0 to destroy`; the only attributes moving are
`source_code_hash`, `s3_object_version` and `last_modified`.

1. `auth.ts` `login()` — the `sendMfaCodeEmail` call is REMOVED from the email-MFA
   branch. The challenge is still issued; its code is minted, hashed and dropped.
   Delivery moves entirely to the opt-in `POST /auth/mfa/send` (Act A, already deployed).
2. `mfa.ts` `issueChallenge()` — `sends` initialises to **0**, not 1. It counted the send
   login used to perform; login no longer sends, so charging the budget here would cost
   the user one of their three deliveries.

**THE CODE HAS ALREADY BEEN COMMITTED — `6379a937e7`, authored by this seat, committed
protectively by `1.0.0_SA_CTO~Z` while this seat was dark. This ledger covers the APPLY
ONLY.** Tree was clean on both source files at build time.

## The behaviour change, named before the apply

⚠ **A LOGIN ALONE NO LONGER DELIVERS AN OTP.** Andrew and `aj@` are ENROLLED and the
pilot is LIVE, so this changes a path a human is actively using: after this apply, a
pilot user who logs in and waits for mail receives nothing until the frontend calls
`POST /auth/mfa/send`. That is the requested behaviour, not a regression — but it is
the one thing that could read as "MFA broke", so it is stated here rather than
discovered. `0.4.0_DE_ClientPlatform~Z` holds the client half in the same window.

⚠ **BOUND ON THE ROLLOUT ORDER:** Act A's send route is already deployed, so the opt-in
button has a working server side the moment the client ships. There is no window in
which the user can neither be sent a code nor request one — the request path exists
first. The reverse order would have been a lockout.

## Rollback

Re-point `s3_object_version` at the prior artifact
(`pyKEMVBmUsw8utCs3dw2tImzy63e0XG+pL5AJqqRIN0=`, the Act A build) and apply. Pure code;
nothing stateful moves. Live challenges issued under either build verify identically —
the row shape is unchanged, so a rollback mid-flight strands nobody.

## Progress

- [x] built from `6379a937e7` — `build-nodejs-lambda.sh portal-auth opalinvest-auth-handler`
- [x] `terraform plan` read — `0 to add, 1 to change, 0 to destroy`, code attributes only
- [x] `safe-apply` — HALT-GATE: 1 pending message, 10 days old, from `2.0.0_SA_COO~Z` to the
      BASE serial about the `opal-gateway` EC2 placement. Read in full, not STOP-class,
      nothing to do with `portal-auth`. `HALT_ACK=1`. Applied 08:19:00Z, `1 changed`.
- [x] 0-diff re-plan — "No changes. Your infrastructure matches the configuration."
- [x] **deployed `CodeSha256` = `nsltFOQw3EORNOpWuxXfO4q0dExh02dzAPM+lYYjKs8=` — OFF
      `pyKEMVBmUsw8...`, and equal to the built artifact sha.** `State: Active`,
      `LastUpdateStatus: Successful`.
- [x] **deployed BYTES censused — see close-out.**
- [x] source-map + ledger committed
- [x] **CLOSED 08:22Z — COMPLETE.**

## Close-out

⛔ **A SHA THAT MOVED PROVES "NOT ACT A". IT DOES NOT PROVE "IS ACT B."** Those are two
claims and only one of them is what the row is for, so the running bundle was pulled from
the live function (`get-function` -> `Code.Location`) and censused. The downloaded zip
hashes to `nsltFOQw3EORNOpWuxXfO4q0dExh02dzAPM+lYYjKs8=` — the same value the live
`CodeSha256` reports and the same value the build wrote to the source map, so the object
read IS the object running.

**The login branch, verbatim from the deployed minified bundle:**

```js
if(Q.mfaChannel==="email"){
  let{challengeId:J}=await t1(Q.email);
  return{mfa:{mfaRequired:!0,challengeId:J,channel:"email"}}
}
```

⭐ **This is DISCRIMINATING, which the sha alone is not.** Act A destructured `code` as
well and called the mailer on the next line; the deployed bytes destructure
`challengeId` ONLY, and there is no call between `issueChallenge` and the `return`. The
evidence would look different if the claim were false — a bundle still carrying Act A
could not produce this line.

**Second marker, independent of the first:** `attempts:0,sends:0` — exactly one
occurrence in the bundle. Act A's initialiser was `sends:1`. The corrected send budget
is in the running code, so the first opt-in click is not silently charged for a
delivery that no longer happens.

## What this does NOT establish

⚠ **The rotation anomaly (`F-8`) is untouched by this apply and is NOT closed by it.**
Act B removes the two-codes-in-flight scenario, which is why `2.0.0_SA_COO~Z` calls it
mooted operationally — but "the scenario can no longer arise" is not "the binding was
correct." The decisive fixture experiment (`1.0.0_SA_CTO~Z` 18545 + `3.0.0_SA_CVO~Z`'s
two-challenge correction 18556) is the instrument for that, and it is a separate act.

⚠ **`rotateChallengeCode` was NOT reworked** — explicitly out of scope per 18548.

