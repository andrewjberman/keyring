# Deploy-completion ledger — Bloomberg tunnel: SSM hybrid activation + instance role

**Status:** CLOSED 2026-07-30 (in-session; 3 added, live-plane verified; two BY-DESIGN residuals recorded, not stranded)
<!-- scanner-alignment line added 2026-08-18 by 0.0.0_AB_MSTR (RED-disposition act, org/tier0_exec/0.0.0_AB_MSTR/deliverables/DEPLOY_LEDGER_RED_DISPOSITIONS_20260818.md): mirrors this file's own close declaration below; deploy_ledger.py's unindexed scanner could not read the original form (defects A/B/shape-C, see the disposition doc). Not a new closure. -->

**Opened:** 2026-07-30 ~22:20Z (at deploy-start, per CLAUDE.md NEVER#6)
**Owner:** `0.7.0_AE_CloudOps~Z` (site Z) · **Stack:** `infra/aws/terraform/bloomberg-tunnel/` (state key `bloomberg-tunnel/tfstate`)
**Code commit (pre-apply, per Deployment Rule 2):** `12920f0a4`, pushed to `origin/CLOUD`

**Authorization:** **Andrew-direct, sovereign, 2026-07-30 ~22:19Z at the site-Z terminal, VERBATIM:**
> *"you can apply that, i love it"*

Issued in direct reply to the gate-4 posture surfaced to him the prior turn, which stated plainly
that applying makes the site-Z workstation an AWS-managed instance and thereby grants SSM **command
execution** on the machine holding a licensed Bloomberg terminal seat. The authorization is
therefore informed and specific to that capability expansion, not a generic go-ahead.
Prior standing: MSTR~Z 20260730T213553Z held the apply for exactly this word.

## Why an apply is the right shape here (measured, not assumed)

- Plan is **3 to add, 0 to change, 0 to destroy** — pure to-add. No existing estate resource is
  mutated, so the rollback is a `destroy` of three brand-new resources with no blast radius.
- `terraform validate` **Success**, `fmt -check` **clean**.
- Zero pre-existing SSM hybrid activations in the account (`describe-activations` → empty) and zero
  `mi-*` managed instances (`describe-instance-information` → 4 results, all `i-*` EC2). Nothing to
  collide with, nothing to duplicate.
- `aws_ssm_activation.registration_limit = 1` — this activation can enroll **exactly one** machine.
  A leaked code cannot enroll a second host.

## Expected apply manifest (enumerated BEFORE, not after)

| # | Resource | Notes |
|---|---|---|
| 1 | `aws_iam_role.bloomberg_tunnel` | `opal-bloomberg-tunnel-instance-role`; trust `ssm.amazonaws.com` with an `aws:SourceAccount` confused-deputy condition |
| 2 | `aws_iam_role_policy_attachment.ssm_core` | `AmazonSSMManagedInstanceCore` (documented minimum — rationale in the module header) |
| 3 | `aws_ssm_activation.bloomberg_tunnel` | `opal-bloomberg-site-z`, `registration_limit=1`, expiry `2026-08-13T23:59:59Z` |

**`aws_iam_policy.bloomberg_tunnel_caller` MUST NOT appear** — it is `count`-gated on
`var.managed_instance_id`, which is empty until the box registers. Its presence in the plan would
mean the gate is broken.

**STOP-AND-REPORT if the plan shows anything outside this manifest.**

## Legs

| # | Leg | Status |
|---|---|---|
| 1 | ledger opened at deploy-start | **DONE** |
| 2 | code committed + pushed BEFORE apply (`12920f0a4`) | **DONE** |
| 3 | `terraform init` + `validate` + `plan` (3 to add / 0 / 0) | **DONE** |
| 4 | apply via `.tools/safe-apply.sh` (Rule 18 — never bare) — **Apply complete: 3 added, 0 changed, 0 destroyed** | **DONE** |
| 4a | **BLOCKED TWICE EN ROUTE, both fixed at the tool rather than overridden** — see below | **DONE** |
| 5 | **LIVE-PLANE verify** (not the apply's self-report) | **DONE** |
| 6 | Emit the one-time admin action for Andrew | **DONE** |
| 7 | ledger CLOSED in-session | **DONE** |

## Leg 4a — the two blocks, and why neither was overridden

`safe-apply` refused twice. Both refusals were CORRECT and neither was a tag collision.

1. **`safe-apply` could not produce plan JSON** → `safe-apply.sh:31` defaults `TERRAFORM` to
   `$SCRIPT_DIR/terraform.exe`, which **does not exist on site Z**. Fixed by supplying the
   sanctioned `SAFE_APPLY_TERRAFORM` env var (line 24) — this makes the gate **evaluate**, and is
   categorically different from `TAGAUTHZ_OVERRIDE`, which would have **bypassed** it.
2. **`comp-tagauthz` rc=1 "could not evaluate"** → its `sh()` resolves the executable with
   `shutil.which('aws')` → `~/bin/aws.CMD` → `.tools/aws.cmd` → a **hardcoded pip path that exists
   only on the laptop**. Fixed at the tool (`b27e756a1`): resolve rather than assume, laptop path
   first, loud 127 if nothing is found.

**Neither warranted `TAGAUTHZ_OVERRIDE`.** rc=1 means the gate never ran; overriding it would have
skipped an authorization check that had produced **no verdict at all** — the override exists for a
gate that has spoken, not for one that is broken. The blast radius of block 2 exceeds this deploy:
**no `default_tags` module was appliable on site Z**, presented as a tag-authz failure.

## LIVE-PLANE verification (leg 5)

| Check | Result |
|---|---|
| `ssm describe-activations` | `3d32065e-401f-453d-a2b9-34e4208c1864` · `opal-bloomberg-site-z` · role bound · Limit **1** · Count **0** · Expired **False** |
| `iam get-role` | `opal-bloomberg-tunnel-instance-role` created `2026-07-30T22:28:24Z`, trust `ssm.amazonaws.com` |
| `iam list-attached-role-policies` | `arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore` |

`aws_iam_policy.bloomberg_tunnel_caller` correctly **absent** — the `count` gate held.

## CLOSED — outcome

**3 resources added, verified on the live plane, nothing stranded.** Gate 4 is closed; gate 2 (the
one-time admin MSI install) is now unblocked and its inputs exist. `Count: 0` is the correct state —
the activation has enrolled nothing yet and enrolls exactly one machine when it does.

**Still open BY DESIGN** (unchanged from the pre-apply section): the `ssm:GetParameter*` residual,
and the caller-side port-forward pin awaiting the `mi-*` id.

## Post-apply state (deliberately NOT closed by this apply)

Two items remain open BY DESIGN and are recorded so they cannot quietly become permanent:

1. **`ssm:GetParameter*` on `Resource:"*"`** — inherited from `AmazonSSMManagedInstanceCore`
   (verified against policy version v2). The box can read every SSM parameter in the account,
   including decryptable SecureStrings; none of it is needed for port-forwarding. An inline Deny
   would override it, but stacking an **unverified** Deny onto the one-shot admin action
   reintroduces the half-working-registration risk the policy choice exists to avoid. Sequence:
   prove registration, THEN add the Deny with a live oracle available.
2. **Caller-side port-forward pin** — authored, `count`-gated, lands in a SECOND apply once the
   `mi-*` id exists. The activation id is **not** the instance id.

## Rollback

`terraform destroy` on this stack — three new resources, nothing pre-existing touched. If the
activation is applied but the MSI never installs, the activation simply expires
`2026-08-13T23:59:59Z` and enrolls nothing.
