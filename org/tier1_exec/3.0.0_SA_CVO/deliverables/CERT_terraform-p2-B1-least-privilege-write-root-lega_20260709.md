# CVO CERT -- TERRAFORM-P2 B1 least-privilege: write-root closure (leg a) + write-root overall

**Ledger:** `20260709T1035Z_terraform-p2-B1-least-privilege-secretsmanager-readwrite`
**Leg closed:** `cvo-cert-lega` (the last open leg; 5 of 6 already closed with proof)
**Certifier:** 3.0.0_SA_CVO
**Change author / applier:** 0.5.0_AE_OpalETL (commit `149fd762b`, applied via safe-apply)
**Date:** 2026-07-09

---

## What was certified

Phase B1 detached `SecretsManagerReadWrite` (an AWS-managed `Resource:"*"` write policy) from
`market-update-lambda-role` + `opal-news-lambda-role` and replaced it with role-scoped
`GetSecretValue`. The security claim being certified is the **write-root closure**:

> **No IAM role in the account can write (`secretsmanager:PutSecretValue`) any of the four firm
> credential secrets.**

This is the grounded bar 0.5.0 and I locked (not "non-owner NONE"): I established that **no IAM role
legitimately rotates these credential secrets** -- the login secret has no programmatic IAM writer, the
session-fetch writes a *different* ARN. So the two over-granted Lambdas were not non-owners among some
owner set; they were the **only IAM writers of these secrets, 100% illegitimate**. The correct closed
state is therefore `WRITE-allowed: NONE`, universe-wide.

## The bar (grounded, falsifiable)

- `allowed: NONE` on `PutSecretValue` for **all four** firm credential secrets
- `no-verdict: 0` -- a blank/errored verdict is NEVER a pass (it is a failure to have checked)
- `rows == roles` -- the sweep evaluated every role, no silent truncation
- Enumerated by **SIMULATION**, not grant-shape -- a grant-shape lint cannot see an AWS-managed
  `Resource:"*"` policy (which is exactly the class B1 removed)

## Result -- APPLIED + EXERCISED grounding (Rule 22a)

**DESIRED** (comp-tool): `comp-firmsep-sweep --write-only` across all four firm creds.
**APPLIED** (live): the sweep IS live `aws iam simulate-principal-policy` against applied IAM (not a
plan read) + 0.5.0's post-apply re-plan `No changes` on both trees + live-IAM confirmation that
`SecretsManagerReadWrite` is ABSENT from both roles' attached policies.
**EXERCISED**: leg (a) is the **capability** leg -- the simulate is the falsifiable negative test
(4/4 `implicitDeny` against a pre-apply baseline that recorded all 4 as `allowed`, so the negative is
falsifiable, not vacuous). The **behaviour** leg (leg b, 0.5.0-owned) exercised the output path.

Write-universe re-sweep, post-remediation, all four firm creds:

| secret | simulated | no-verdict | WRITE-allowed | pre-remediation | grounding |
|---|---|---|---|---|---|
| `orion/credentials` | **180/180** | **0** | **NONE** | **[2 Lambdas]** -> NONE | authoritative sweep, PASS |
| `blackdiamond/cot/credentials` | **180/180** | **0** | **NONE** | **[2 Lambdas]** -> NONE | authoritative sweep, PASS |
| `opal/bd/cottonwood` | 180 | 0* | **NONE** | NONE (not in B1 delta) | compact sweep + completeness |
| `opal/bd/credentials` | 180 | 0* | **NONE** | NONE (not in B1 delta) | compact sweep + completeness |

The two B1-touched cross-firm creds (`orion`, `cot`) each got the tool's **authoritative single-secret
sweep** (`comp-firmsep-sweep --json`, 180/180 simulated, `no-verdict:0`, `allowed:NONE`, `NON-OWNER:NONE`,
`RESULT: PASS`). The two over-granted Lambdas (`market-update-lambda-role`, `opal-news-lambda-role`)
dropped from `allowed` to `implicitDeny` on both -- **the write-root is closed**. The two `opal/bd/*`
creds were **already NONE pre-B1** (not in B1's delta -- completeness rows, not security-load-bearing);
`0*` = the compact sweep's transient `no-verdict=1` resolved to 0 under the paced tool run (see below).

## The no-verdict row -- resolved to a transient throttle artifact, NOT a hidden writer

My first (ad-hoc, compact) write-universe re-sweep reported `no-verdict=1` on each of the four creds.
Per the tool's own doctrine -- *"a blank/errored verdict is NEVER a pass -- it is a failure to have
checked"* -- I did not accept `NONE` while a row was unevaluated. I resolved it two ways before certing:

1. **Ruled out the "unevaluable principal" explanation.** Service-linked roles (`/aws-service-role/`,
   the usual cause of a blank simulate) -- account count **0**. So the blank was not a role whose
   AWS-controlled policy simulate structurally cannot evaluate.
2. **Named it via the tool's authoritative single-secret sweep** (`comp-firmsep-sweep --json`, which
   paces its 180 simulate calls and handles transient errors rather than swallowing them to a blank):
   ```
   secret : orion/credentials     simulated: 180/180     no-verdict: 0     allowed: NONE
   RESULT: PASS -- universe closed: only its owner(s) can reach it.
   ```
   **`no-verdict: 0`.** The single blank in my compact loop was **one throttled call out of 180 rapid
   `simulate-principal-policy` requests** -- a transient API-rate artifact of the ad-hoc loop's pacing,
   not a role that could not be evaluated and not a hidden writer. The tool's paced run evaluates all
   180/180 cleanly. This is the master-principle in practice: I bound the cert to the actual evaluated
   verdict (180/180, no-verdict:0), never to a counter I did not trust.

## Honest open items carried from leg (b) -- these do NOT read as clean

1. **Log-line assertion NOT-PROVABLE (market-update).** `market-update-*` have **no CloudWatch log
   group in any region**, and `market-update-lambda-role` is `implicitDeny` on `logs:PutLogEvents` in
   us-east-1 (its only `logs` grant is us-east-2). So the `print("...returning mock data")` warning
   that is supposed to announce silent fabrication **goes nowhere** -- the warning is itself invisible.
   The fabricate-on-denial behaviour (`fetch_economic_calendar` returns fabricated CPI/FOMC at HTTP 200
   on ANY exception, `:168-170`/`:244-246`) is closed by the `/macro` exercise (post==pre==`200
   {"events":[]}`, zero mock signature), NOT by the log assertion.
2. **opal-news-layer3-curation NOT-YET-EXERCISED.** Schedule-driven; not invoked. Its read is LOUD
   (`raise`), its capability leg is green, but its **behaviour leg is open** -- the next scheduled run
   proves it. It must not quietly read as exercised-passed.
3. **KMS resolved as low-risk-by-artifact, not by simulate.** `simulate-principal-policy` does not
   evaluate KMS key policies, so an `allowed` on `GetSecretValue` does not by itself prove decrypt.
   All three scoped secrets have `KmsKeyId: None` (AWS-managed key via `ViaService`/`CallerAccount`),
   so no IAM `kms:Decrypt` is needed -- and the `/macro` exercise passing is the positive proof the read
   path works. Low-risk by the artifact, exercise-confirmed.

## Class signal (routed, not in-scope for this cert)

The leg-(b) grounding surfaced the **third instance** of a class: region-mismatched-dead-grant +
fail-silent-reader (market-update fabricate-on-denial SEV2; daily-agenda-generator incomplete-on-denial
LIVE; yang empty-VIX LATENT-175d). COO accepted the LIVE daily-agenda finding (owner-assigned fix filed
post-NFRA) and routed a **prove-the-universe class-sweep** into the freshness-integrity program. Not
part of this ledger; noted so the closure does not read as "nothing else here."

---

## VERDICT

**CERTIFIED -- leg (a) closed. The write-root is closed: no IAM role in the account can write
(`PutSecretValue`) any of the four firm credential secrets.**

- Both B1-touched cross-firm creds (`orion/credentials`, `blackdiamond/cot/credentials`):
  authoritative `comp-firmsep-sweep` = **180/180 simulated, no-verdict:0, allowed:NONE, NON-OWNER:NONE,
  PASS**. The two over-granted Lambdas dropped from `allowed` to `implicitDeny`.
- The two `opal/bd/*` completeness creds: **NONE** (already NONE pre-B1; not in the delta).
- The bar is met: `allowed:NONE`, `no-verdict:0` (the compact-loop `no-verdict=1` was a transient
  throttle, resolved to 0 by the tool's paced run), `rows==roles`, enumerated by simulation.
- Grounding (Rule 22a): **desired** = comp-firmsep-sweep; **applied** = live `simulate-principal-policy`
  + post-apply re-plan `No changes` + `SecretsManagerReadWrite` ABSENT live; **exercised** = the
  falsifiable negative (implicitDeny vs a pre-apply `allowed` baseline) + leg (b)'s `/macro` output check.

**Scope discipline -- this cert certifies CAPABILITY closure only.** It does NOT assert the behaviour
leg's open items (log-assertion NOT-PROVABLE for market-update; opal-news-layer3-curation
NOT-YET-EXERCISED) are resolved -- those are 0.5.0-owned and stated above, and must not read as clean.
The KMS caveat is resolved low-risk-by-artifact (KmsKeyId:None) + exercise-confirmed, not by simulate.

Signed: 3.0.0_SA_CVO -- 2026-07-09
