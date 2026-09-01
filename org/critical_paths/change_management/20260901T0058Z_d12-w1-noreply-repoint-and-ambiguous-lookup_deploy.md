# DEPLOY LEDGER — auth-handler: all-auth-mail-to-noreply + ambiguous identity lookup

| | |
|---|---|
| **Opened** | 2026-09-01T00:58Z |
| **State** | CLOSED -- COMPLETE 2026-09-01T01:10Z |
| **Seat** | `0.7.0_AE_CloudOps~Z` (site Z) |
| **Authority** | ANDREW-DIRECT ~00:5xZ (sender) + `1.0.0_SA_CTO~Z` lane ruling 1 (lookup), relayed 17260 |
| **Pipeline** | `infra/aws/terraform/portal-auth` |
| **Source** | `7f40b7c65b` · artifact sha `i6POeTZAHi14588lyM+x2PPiriq9rhGA6y0CE/BTkjI=` |

## What lands

Lambda **code only** — one in-place `aws_lambda_function.auth_handler` update. No new
resource, no IAM change, no DNS change, no alarm/monitor/SNS.

1. All three SES `Source:` sites → `noreply@opalinvest.dev` (was: two on `support@`).
2. `getUserPKByEmail` → `Limit: 2` and **fail closed** on a second match.

## Rollback

Re-point `s3_object_version` at the prior artifact (`T0Lf6MSrKtr4OKEuoEelpFaFMZwipkPFomVveCtqywc=`)
and apply. Both changes are pure code; nothing stateful moves.

⚠ **THE ONE BEHAVIOUR CHANGE THAT COULD BITE, NAMED BEFORE THE APPLY:** if a duplicate
email already exists in `opal-users-v2`, that account's login now **fails closed (500)**
where it previously authenticated as an arbitrary one of the two. That is the intended
direction — an ambiguous identity must not authenticate — but it is a login-affecting
change, so it is stated here rather than discovered. Pre-check below.

## Progress

- [x] **duplicate-email pre-check — 48 items carry an email, 48 DISTINCT, 0 duplicates
      (full scan, no further pages). NOBODY is locked out by the fail-closed change.**
      Run BEFORE the apply, because after it the answer would be a support ticket.
- [x] `terraform plan` read — `0 to add, 1 to change, 0 to destroy`
- [x] `safe-apply` — HALT-GATE acknowledged (same 10-day-old message, already read in full)
- [x] 0-diff re-plan — "No changes. Your infrastructure matches the configuration."
- [x] deployed sha == built sha — `i6POeTZAHi14588lyM+x2PPiriq9rhGA6y0CE/BTkjI=`
- [x] **senders verified in the DEPLOYED BYTES, not by a live send**
- [x] **CLOSED 01:10Z — COMPLETE.**

## Close-out

Verified by pulling the running bundle from the live function and censusing it — deliberately
**not** by firing `/auth/forgot-password`, per `1.0.0_SA_CTO~Z`'s ruling 3 that a probe with an
outbound side effect must not be aimed at a live sender. Tonight's W1-6 sweep sent real mail to
a real person; that is not repeated here.

```
sender addresses in the RUNNING code : ['noreply@opalinvest.dev']
support@opalinvest.dev occurrences   : 0
noreply@opalinvest.dev occurrences   : 1     <- ONE, because the two constants were collapsed
user_lookup_ambiguous                : 1     <- the fail-closed lookup is live
positive control mfa_challenge_issued: 1     <- the census engine works on this bundle
```

⚠ **STILL OPEN AND NOT CLOSED BY THIS DEPLOY:** the role's two-Allow SES structure. The
`ses:FromAddress = noreply@` condition remains defeated by an unconditioned sibling grant. Every
sender now happens to be `noreply@`, which makes the condition look satisfied — **that is
appearance, not enforcement.** No IAM policy was widened or narrowed here.
