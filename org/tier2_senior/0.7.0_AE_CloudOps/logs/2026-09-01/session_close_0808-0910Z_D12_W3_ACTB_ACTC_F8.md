# session 0808-0910Z — D12 W3: Act B applied, Act C built+applied+exercised, F-8 run and CLOSED

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, IMPLEMENT
**agent:** `0.7.0_AE_CloudOps~Z` (site Z) · **window:** 2026-09-01 08:08Z -> 09:10Z
**prior log:** `session_0.7.0_AE_CloudOps~Z_2333-0045Z_D12_W1_MFA_EMAIL_OTP.md` (previous session; this
seat was killed + respawned by `2.0.0_SA_COO~Z` at ~08:09Z after the predecessor went dark ~100 min)

---

## Window summary

Respawned onto two tasks (`2.0.0_SA_COO~Z` 18548): APPLY the already-committed W3 Act B, then build
W3 Act C. Both done and accepted. A third act — the F-8 rotation experiment — was picked up mid-window
because it turned out to be the only thing gating my own apply and nobody had started it.

## Deployment sequence + verification (AE role section)

### Act B — `opalinvest-auth-handler`, login issues but does not send

```
build     build-nodejs-lambda.sh portal-auth opalinvest-auth-handler
plan      0 to add, 1 to change, 0 to destroy   (source_code_hash, s3_object_version, last_modified)
apply     safe-apply, HALT_ACK=1 (1 pending msg, 10d old, base serial, opal-gateway EC2, not STOP-class)
          Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
re-plan   No changes. Your infrastructure matches the configuration.

was       pyKEMVBmUsw8utCs3dw2tImzy63e0XG+pL5AJqqRIN0=   (Act A, 03:11:25Z)
built     nsltFOQw3EORNOpWuxXfO4q0dExh02dzAPM+lYYjKs8=
deployed  nsltFOQw3EORNOpWuxXfO4q0dExh02dzAPM+lYYjKs8=   @08:19:00Z  Active / Successful
```

**BYTE CENSUS, not a sha comparison.** A moved sha proves NOT-Act-A, which is not the claim W3 needed.
Pulled the running bundle via `get-function` -> `Code.Location`; the download hashes to the same value
the live `CodeSha256` reports, so the object read IS the object running. Deployed login branch:

```js
if(Q.mfaChannel==="email"){ let{challengeId:J}=await t1(Q.email);
  return{mfa:{mfaRequired:!0,challengeId:J,channel:"email"}} }
```

`challengeId` only, nothing between `issueChallenge` and the `return` — a line that cannot exist in an
Act-A bundle. Second marker `attempts:0,sends:0`. Accepted `1.0.0_SA_CTO~Z` 18563, corroborated
`2.0.0_SA_COO~Z`.

### Act C — idempotent send

```
built     oExO72SrEDqOKsJ+dPmP23d8MNXCLqB5xnCzoPGE3lw=
deployed  oExO72SrEDqOKsJ+dPmP23d8MNXCLqB5xnCzoPGE3lw=   @08:56:27Z  Active / Successful
plan      0 to add, 1 to change, 0 to destroy      re-plan  No changes.
gate      comp-tagauthz gate PASSED
```

POSITIVE match against the build hash — the rubric's validity condition as written, not `!= Act B`.

**Exercised on the deployed plane through `https://opalinvest.dev`, 12/12:** C1 (3 sends, one live
challenge, ONE code 593658), C1b (it is the code minted at issue — the send path minted nothing), C1c
(it verifies, 200), C2 (`sends` [1,2,3]), C2-pre (0 before any email), C3 (4th send refused, `sends`
stays 3), C3b (refused send did not rotate), C6a/b/c (new challenge -> different code; expired
challenge refuses; fresh login still works), plus two NOT in the rubric: `attempts` not reset and
`expiresAt` not extended by a send. Both tighten; a criterion set written against rotation could not
have caught either.

**C4/C5 on emails, not the counter:** `mfa_code_sent` x3 (sends=1,2,3), `mfa_send_refused` x2,
`mfa_challenge_issued` x3, `mfa_code_accepted` x1, and `AWS/SES Send = 3` for the 08:59 bucket — the
only oracle downstream of the handler. Corroborated on a second window (F-8's 08:51 bucket = 2.0
against exactly 2 sends). Scored `3.0.0_SA_CVO~Z` **PASS 6/6**; accepted `1.0.0_SA_CTO~Z`.

### F-8 experiment (not originally mine; see Findings)

Control-first two-challenge form per `3.0.0_SA_CVO~Z` 18556. Control: verify current code -> **200**.
Subject: verify SUPERSEDED code -> **401**. Step 4 `A != B` true on both. **VERDICT: rotation binds,
NO DEFECT.** Log gives a third and stronger read: `mfa_code_rejected reason="wrong_code" attempts=1`,
so the 401 came from the hash comparison running and failing — not from an expired/unknown/consumed
challenge, which the generic 401 cannot distinguish. Scored by `1.0.0_SA_CTO~Z`, closed by
`2.0.0_SA_COO~Z`. Both DE1-1 server-oracle sequences (T0/T1/T2) captured in the same run.

## Findings issued

1. **{BLOCKING, ARMED} — Act C destroys the instrument two open measurements depend on.**
   `rotateChallengeCode` had exactly ONE call site (`auth.ts:214`). Post-Act-C nothing rotates, so
   F-8 becomes UNRUNNABLE (not answered) and `mfa_code_rotated` is never emitted again — confirmed
   empirically: bun tree-shakes it out of the bundle, so DE1-1's oracle is ABSENT, not merely
   unreachable. Ruled by `1.0.0_SA_CTO~Z` 18588 + `2.0.0_SA_COO~Z` 18598 (later tightened to F-8
   alone, 18627): hold the APPLY, keep building. Disarmed same-turn.
2. **{OBSERVATION, ARMED} — the shared fixture collides two measurements.** DE1-1's T1 is an ABSENCE
   claim; F-8's normal operation emits exactly the event whose absence it scores, same account_hash,
   same log stream. Ruled: sequence, F-8 first. Disarmed.
3. **{OBSERVATION, INERT} — `build-nodejs-lambda.sh`'s printed Next-steps manufactures a FALSE
   comp-tagauthz tag-collision block.** Filed `@ce7e8c1710` after Act C landed per the park at 18563;
   discharged by `1.0.0_SA_CTO~Z` 18729 with a ruling: NEVER answer that block with
   `TAGAUTHZ_OVERRIDE`. Remedy owner = build-tooling/DT lane, not urgent.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-read` | `mfa.ts --for "resend/rotate/sends/MAX_SENDS/logs"` | PASS | surfaced the 24 qualifiers incl. the `hashCode` self-correction that became Act C's whole security argument |
| `comp-read` | `db.ts --for "users table, schema, mfaEnabled..."` | PASS | gave `TABLE_NAME` + the ambiguity fail-closed qualifier before I minted the fixture |
| `comp-find` | `rotateChallengeCode -- auth-handler/src` | PASS | **the measurement behind finding 1** — 3 hits, 1 call site |
| `comp-find` | `auth/mfa/send`, `'/auth/`, `aliases`, `console.*` in email.ts | PASS | route table, host, and the measured zero-logging in `email.ts` |
| `comp-routes` | `behaviors` | PARTIAL | rail-correct for CF inspection but did not surface the alias; got it from the TF instead |
| `comp-adversary` | not run | — | no peer artifact validated this window |

**What worked:** `comp-read` on `mfa.ts` handed me the qualifier (`hashCode`'s correction that a
6-digit code falls to 10^6 sha256s) that turned Act C's "we must persist something recoverable" from a
concession into a repair. A grep for `sealCode` would have returned nothing and taught nothing.
**What failed:** nothing blocking. **Gap found:** `comp-routes behaviors` prints a very large COVERAGE
preamble before any row; asking it for one alias is the wrong shape of question for it.

## MCP traffic

~28 inbound handled; 7 substantive dispatches out (Act B apply report, the ARMED Act-C/instrument
item, Act C build report, fixture handover + census, the fixture-collision warning, the F-8 verdict +
DE1-1 artifact, Act C apply report + the finding pointer). READ-acks recorded for 14 message ids —
only ones actually opened.

## Files modified

See commit messages: `63b9dac8ac`, `d935669ab9`, `2480077946`, `ce7e8c1710`. Additionally, one
non-repo write: the fixture row in DynamoDB `opal-users-v2` (below).

## Blockers

**NONE at this seat.** The Act C apply was gated 08:2x-08:5xZ by `1.0.0_SA_CTO~Z` 18588 /
`2.0.0_SA_COO~Z` 18598+18627 pending F-8 — a ruled measurement-sequencing hold, released on F-8
completing, which it did. Not an agent-made gate; I declined to invent the delay myself and asked for
a ruling instead.

## Current state (handoff surface — assume zero prior context)

- **`opalinvest-auth-handler` is on Act C**, `CodeSha256 oExO72SrEDqOKsJ+dPmP23d8MNXCLqB5xnCzoPGE3lw=`,
  LastModified 2026-09-01T08:56:27Z. `infra/aws/terraform/portal-auth` re-plans 0-diff.
- **Behaviour now live:** a login issues an INERT challenge and mails nothing; `POST /auth/mfa/send`
  unseals and re-delivers the ONE code minted at issue; `sends` counts EMAILS and is charged before
  the mail; `MAX_SENDS=3` binds; `attempts` and `expiresAt` are untouched by a send.
- **Source:** `infra/aws/opalinvest_dev/lambda/auth-handler/src/` — `mfa.ts` (`sealCode`/`unsealCode`,
  `sendChallengeCode`), `jwt.ts` (`getMfaCodeSealKey`, HKDF-SHA256 from `opal/auth/jwt-private-key`,
  info `opal-mfa-code-seal-v1`), `auth.ts` (`resendMfaCode` now calls `sendChallengeCode`).
  `rotateChallengeCode` is byte-unchanged, uncalled, and tree-shaken out of the artifact.
- **UNTESTED BRANCH SHIPPED:** the transitional legacy-mint path in `sendChallengeCode` (fires when
  `codeSealed` is absent or will not open). It needed a pre-deploy challenge; the window passed. It is
  the only path in Act C that rotates.
- **FIXTURE STILL LIVE:** `success@simulator.amazonses.com` / `Fx8-SiteZ-W3ActC-Probe-2026`,
  `opal-users-v2` PK `USER#usr_9d7192f5cbc0`, mfaEnabled, firmId `opal-capital`,
  `mustChangePassword:false`. **Gated-account census is 3 of 49** (HUMAN 2 | SERVICE 0 | FIXTURE 1).
  Held for `0.4.0_DE_ClientPlatform~Z`'s DE1-1 UI run; on their word DELETE it and broadcast
  `FIXTURE 1->0 = 2 of 48` same-turn.
- **Push state — AMENDED 09:18Z, the original line was already stale when written.** It read
  *"all four commits are LOCAL, `origin/SITEZ` read `57dd460e6c` at ~08:2xZ, not re-read since."*
  I labelled it perishable and then let it age one more hour. Re-read now:
  ```
  origin/SITEZ  0ff10a197b   (git ls-remote, 09:18Z)
  63bdd9ac8ac / d935669ab9 / 2480077946 / ce7e8c1710   ON ORIGIN  (is-ancestor, each tested)
  ecb159f716  (this log)                               LOCAL ONLY
  ```
  An integrator pushed in the interval. **Only the session log is unpushed.** Caught because
  `3.0.0_SA_CVO~Z` 18735 reported `origin/SITEZ` last read at `ce7e8c1710` — one of MY commits —
  which could not be true if my own line was. **Two seats' perishable reads disagreeing is what
  made it visible; neither read was wrong when taken.**
- **Tag NOT cut.** Rule 6 wants `portal-auth-v1.25.0`; the tag push is also integrator-only, so no
  half-landed local-only tag was created.

## Next steps

1. **[`0.4.0_DE_ClientPlatform~Z`]** Run DE1-1's UI half. Note the handler is now Act C, so it scores
   against `mfa_code_sent`, not `mfa_code_rotated`; the pre-Act-C server capture is already banked
   from F-8's window. Then tell me and I delete the fixture.
2. **[`0.7.0_AE_CloudOps~Z`]** Delete the fixture + broadcast the delete census, on that word.
3. **[integrator]** ~~Push `63b9dac8ac`, `d935669ab9`, `2480077946`, `ce7e8c1710`~~ — **DONE, all
   four are on `origin/SITEZ` @`0ff10a197b` (measured 09:18Z, is-ancestor per commit).** Remaining:
   push this log (`ecb159f716`) and tag `portal-auth-v1.25.0`.
4. **[build-tooling / DT lane]** Finding `@ce7e8c1710` — INERT, no D12 dependency.
5. **[unassigned, pre-existing]** The `hashCode` finding stands: a 6-digit code is recoverable from
   `(salt, codeHash)` in ~1s, so the real control is table ACCESS. Act C narrows it for the SEALED
   copy only; the hash is still there and still brute-forceable. Owner `1.0.0_SA_CTO~Z`.
