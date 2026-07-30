# Deploy-completion ledger — Bloomberg tunnel: SSM hybrid activation + instance role

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
| 4 | apply via `.tools/safe-apply.sh` (Rule 18 — never bare) | PENDING |
| 5 | **LIVE-PLANE verify** — not the apply's self-report: `describe-activations` shows the activation, `get-role` + `list-attached-role-policies` show the role and attachment | PENDING |
| 6 | Emit the one-time admin action for Andrew (activation id + install command; code retrieved via `terraform output -raw`) | PENDING |
| 7 | ledger CLOSED in-session | PENDING |

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
