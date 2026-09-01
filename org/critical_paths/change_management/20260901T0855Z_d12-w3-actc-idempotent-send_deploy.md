# DEPLOY LEDGER — auth-handler: W3 ACT C, the code is minted once and every send re-delivers it

| | |
|---|---|
| **Opened** | 2026-09-01T08:55Z |
| **State** | CLOSED -- COMPLETE 2026-09-01T09:01Z |
| **Seat** | `0.7.0_AE_CloudOps~Z` (site Z) |
| **Authority** | `1.0.0_SA_CTO~Z` 18491 (property, FINAL) · `2.0.0_SA_COO~Z` 18548 (task) · release condition `2.0.0_SA_COO~Z` 18627 "releases on F-8 COMPLETE ALONE" |
| **Pipeline** | `infra/aws/terraform/portal-auth` |
| **Source** | `d935669ab9` (mfa.ts + auth.ts + jwt.ts) |

## The gate this apply was held behind, and why it is now open

⛔ **THIS APPLY WAS DELIBERATELY HELD FOR ~35 MINUTES AND THE HOLD WAS CORRECT.** Act C removes
the only rotation path in the handler (`rotateChallengeCode` had exactly one call site,
`auth.ts:214`). Two live measurements existed only inside that path:

- **F-8** — needed a rotation to supersede a code. After Act C, no code can be superseded, so
  the experiment becomes *unrunnable*, not answered.
- **DE1-1's server oracle** — scored on `mfa_code_rotated`, emitted inside the orphaned
  function. Confirmed empirically: bun **tree-shakes it out of the Act C bundle**, so the event
  is not merely unreachable, it is absent.

⭐ **The upload was held too, not just the apply.** `build-nodejs-lambda.sh` builds AND uploads in
one act, and the TF resource reads `s3_object_version` — so a built-and-uploaded artifact would
have armed *any* seat's `portal-auth` apply to ship Act C and close the window with nobody
deciding to. A gate on "AE must not apply" that leaves a loaded artifact in S3 is a gate with a
side door.

**F-8 ran at 08:51Z and CLOSED with no defect** (401 on the superseded code, control 200,
`reason: "wrong_code"` in the log). Both DE1-1 server-oracle sequences were captured in the same
run. The hold's purpose is discharged.

## What lands

Lambda **code only** — one in-place `aws_lambda_function.auth_handler` update. No new resource,
no IAM change, no DNS change, no alarm/monitor/SNS. **No new secret and no new KMS key**: the
seal key is HKDF-derived from the JWT private key the role already reads.

1. `issueChallenge` seals the minted code (`codeSealed`, AES-256-GCM) alongside the existing
   salted hash. **`verifyAndConsumeChallenge` is untouched.**
2. New `sendChallengeCode` — `POST /auth/mfa/send` unseals and re-delivers **the same code**,
   charging `sends` in the same conditional update that authorises the send, before the mail.
3. `attempts` is no longer reset and `expiresAt` is no longer extended on a send. **Both tighten.**
4. Per-email log line renamed `mfa_code_sent` (carries `sends` + `resend`); refusals log
   `mfa_send_refused`.
5. `rotateChallengeCode` left **byte-unchanged** and uncalled, per 18548.

## The behaviour changes, named before the apply

⚠ **N clicks inside one live challenge now deliver ONE code.** That is the point, and it is what
Andrew asked for.

⚠ **PER-CHALLENGE ONLY.** Two tabs = two challengeIds = two live codes. Ruled a known bound
(18491 §3). Act B already removed the common case.

⚠ **TRANSITIONAL, ~10 MINUTES:** challenges issued by the previous build carry no seal. Without
the fallback their owners' Resend would return silently and send nothing until expiry — a real
outage for anyone mid-login across the apply. The fallback mints/seals/adopts and then converges.
**It is the only thing in Act C that rotates.**

⚠ **DE1-1's criterion must re-point** to `mfa_code_sent`. `1.0.0_SA_CTO~Z` owes that rule; it does
not gate this apply (COO 18627).

## Rollback

Re-point `s3_object_version` at the Act B artifact
(`nsltFOQw3EORNOpWuxXfO4q0dExh02dzAPM+lYYjKs8=`) and apply. Pure code.
⚠ **One asymmetry worth stating:** challenges issued under Act C carry `codeSealed`, which Act B
simply ignores — Act B rotates on send regardless. So a rollback strands nobody; in-flight
challenges keep working, they just resume rotating.

## Progress

- [x] F-8 complete — the release condition (COO 18627). 401 / control 200, recorded.
- [x] built + committed `d935669ab9`; tsc clean; seal/unseal 15/15
- [x] build + upload artifact — `oExO72SrEDqOKsJ+dPmP23d8MNXCLqB5xnCzoPGE3lw=`
- [x] `terraform plan` — `0 to add, 1 to change, 0 to destroy`; `source_code_hash`,
      `s3_object_version`, `last_modified` only
- [x] `safe-apply` — HALT-GATE 2 pending (both routine, read), `HALT_ACK=1`;
      **`comp-tagauthz gate PASSED`**; applied 08:56:27Z
- [x] 0-diff re-plan — "No changes. Your infrastructure matches the configuration."
- [x] **deployed `CodeSha256` = `oExO72SrEDqOKsJ+dPmP23d8MNXCLqB5xnCzoPGE3lw=` == the built
      artifact hash. POSITIVE MATCH.** `State: Active`, `LastUpdateStatus: Successful`.
- [x] **EXERCISED ON THE DEPLOYED PLANE — 12/12, plus C4/C5 from two log oracles.** See close-out.
- [x] source-map + ledger committed
- [x] **CLOSED 09:01Z — COMPLETE.**

## Close-out

**12/12 assertions against the deployed handler, driven through `https://opalinvest.dev`.**
Codes recovered offline from `(salt, codeHash)`; mail was never an input.

```
C2-pre  sends == 0 before any email (login sends nothing -- Act B holds)      PASS
C1      3 sends, one live challenge -> ONE code (593658 every time)           PASS
C1b     and it is the code minted AT ISSUE -- the send path minted nothing    PASS
C1c     the re-sent code VERIFIES (200) -- live code, not a stale copy        PASS
C2      sends == N after N emails -> [1,2,3]                                  PASS
C3      the 4th send REFUSED -- sends stays 3                                 PASS
C3b     and the code is unchanged by the refused send                         PASS
C6a     a NEW challenge mints a DIFFERENT code (per-challenge, not permanent) PASS
C6b     an EXPIRED challenge refuses the send -- sends stays 0                PASS
C6c     a fresh login still mints a usable challenge afterwards               PASS
X-attempts  attempts NOT reset by a send  -> [0,0,0]                          PASS
X-expiry    expiresAt NOT extended by a send (one distinct value)             PASS
```

**C4 / C5 — scored on emails, not on the counter, exactly as the rubric demanded:**

```
mfa_code_sent      3   sends=1,2,3   <- one line per email (C5)
mfa_send_refused   2                 <- the capped send + the expired send: NO email
mfa_challenge_issued 3               <- three logins, none of them sent anything
mfa_code_accepted  1                 <- the C1c verify
AWS/SES Send       3   (08:59 bucket, account-scoped)
```

⭐ **THE SES METRIC IS THE ONLY ORACLE HERE THAT SITS DOWNSTREAM OF THE HANDLER**, and it agrees:
3 emails for 3 authorised sends. Corroborated on a second window — the F-8 run's 08:51 bucket
reads `Sum=2.0` against exactly 2 sends.

⛔ **AND IT NEARLY PRODUCED A FALSE DEFECT REPORT AGAINST THIS BUILD.** The first read of the
08:59 bucket returned **`Sum=2.0`** against 3 log lines. That looks precisely like the failure
this oracle exists to catch — an email that was authorised and never sent. It was **metric
aggregation lag**: re-read unchanged-otherwise, the same bucket returned `3.0`. **The tell was
that the number moved with no new activity.** A CloudWatch count read too early reads LOW, and
on a "count the emails" oracle a low read is indistinguishable from a missing email. Never score
a count metric on a single read taken seconds after the event.

## Two grain limits on the C5 oracle, stated because they will be leaned on

⚠ **`mfa_code_sent` IS EMITTED BEFORE THE SES CALL** (inside `sendChallengeCode`; the mail goes
in `auth.ts` afterwards), and **`email.ts` contains no logging at all** — measured, zero
`console.*`. So the line counts an **authorised** send, not a **delivered** one. It is a sound
oracle for the `sends`-counts-emails invariant, and it is **not** a delivery record. That gap is
what the SES metric closes, and it is the reason the SES read was worth taking.

⚠ **`resend: true` MEANS "UNSEALED AN EXISTING CODE", NOT "THIS WAS A REPEAT CLICK".** All three
sends above report `resend: true` — including the first — because the code is sealed at issue,
so even the first send re-delivers rather than mints. `resend: false` occurs only on the
transitional mint path. **Anyone counting repeat clicks by counting `resend:true` overcounts by
one per challenge.**

## Not established

⚠ **The UI path is untested here** — every call was a direct API POST. `0.4.0_DE_ClientPlatform~Z`
holds that half.
⚠ **Multi-session remains out of scope and still reachable** — two tabs, two challengeIds, two
live codes. Ruled a known bound (`1.0.0_SA_CTO~Z` 18491 §3). A PASS here is not a claim that a
user can never see two codes.
⚠ **The transitional legacy-mint branch was NOT exercised** — it needs a challenge issued by the
previous build, and the deploy window has passed. It is the one path in Act C that rotates.

