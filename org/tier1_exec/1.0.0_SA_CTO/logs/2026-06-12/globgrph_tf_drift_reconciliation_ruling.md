# GLOBGRPH derive_runner .tf drift — reconciliation ruling: (b) REVERT .tf TO LIVE
**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE

Trigger: COO URGENT flag 142218Z (AE Item-2b RAVC2 surfaced pre-existing drift; TO-F2 activated with
targeted-apply constraint pending this call). Independent verification done before ruling — committed .tf
read, live state read (read-only IAM get-role-policy + ecs describe-task-definition), code contract read.

## Verified facts
1. **Live task def rev 1 env:** NESSIE_URI = `http://nessie.opal-globgrph.local:19120` (bare). Committed
   `main.tf:49` local = `.../api/v2`. Revisions are immutable and only rev 1 exists → the task def was
   CREATED from a working tree whose nessie_uri was bare, i.e. applied-from-uncommitted-edit during the
   Blocker-2 window (a674a4f7d "Nessie createReference" fix era) — the committed /api/v2 form has NEVER run.
2. **The CODE CONTRACT is the bare base URI** (decisive):
   - `infra/aws/globgrph/derive_runner.py:40` documents + defaults bare; L127 strips `/api/v2` before
     building the Iceberg REST path (`{base}/iceberg/{branch}`); **L242 raw-appends `/api/v2`** for the
     Nessie REST call (audit-baseline createReference). A task-def value of `.../api/v2` would produce
     `/api/v2/api/v2` at L242 → breaks nightly audit-baseline tagging. This is plausibly the original
     Blocker-2 failure mode that motivated the live bare-URI hot-fix.
   - `infra/aws/lambda/globgrph/incremental_updater/lambda_function.py:29` same contract ("base URI"
     comment), L335 same strip-defense.
3. **The IAM "removal" is a plan-diff misread, not a real permission trim:** committed
   `item2a.tf:230-250` RETAINS ecs:RunTask + iam:PassRole; live policy (verified via get-role-policy) is
   structurally IDENTICAL — RunTask pinned to `task-definition/globgrph-derive-runner:1` + PassRole on the
   two roles. The plan's policy/event-target diffs are the revision-pinned ARN following the task-def
   MUST-REPLACE cascade. No permissions are actually lost in the committed form — and none need to move.

## Ruling: option (b) — revert committed .tf to the live (certified) state
- `main.tf:49`: `nessie_uri = "http://nessie.opal-globgrph.local:19120"` (bare) + comment stating the code
  contract: consumers append their own API paths (`derive_runner.py:127/242`,
  `lambda_function.py:335`); NEVER bake `/api/v2` into this local.
- Grounds: (i) bare is the code contract — committed /api/v2 breaks createReference by double-pathing;
  (ii) live config is the 2x-CVO-certified one; the committed alternative has never run a nightly;
  (iii) the revert eliminates the MUST-REPLACE, which should collapse the dependent IAM/event-target
  diffs to zero; (iv) no recertification cycle burned — Item-2a stability declaration stands unmodified.
- Options rejected: (a) apply+recertify spends a certification run to land a config that contradicts the
  code contract (it would FAIL at audit-baseline tagging — recert would catch the break we can already
  prove statically); (c) document+hold leaves a standing landmine for any future non-targeted apply.

## Acceptance criterion (AE, rides TO-F2 lane or a micro-TO at COO's discretion)
After the one-line revert commit (Rule 2: commit before apply): **full NON-targeted `terraform plan` on
the globgrph root = 0 add / 0 change / 0 destroy.** That single check (i) proves committed==live, (ii)
retro-heals the original applied-from-dirty-tree drift, (iii) lifts the targeted-apply constraint, and
(iv) clears the nightly-chain risk. If the 0-diff plan shows ANY residual (e.g. another env var or the
event target), AE surfaces it before apply — do not chase residuals silently.

## Discipline finding (banked, no action)
Origin = apply-from-uncommitted-tree during Blocker-2 debugging (CLAUDE.md Rule 2 commit-before-apply +
verify-0-diff-after-apply violation, historical). The 0-diff post-apply verify step in the standard
sequence would have caught this the day it happened. No blame hunt — the structural lesson IS the
acceptance criterion above.

## Compiler Tools
| Tool | Run? | Why / result |
|---|---|---|
| comp-* (any) | NO | Drift reconciliation = committed-vs-live-vs-code-contract triangulation: direct Read of item2a.tf/main.tf/derive_runner.py/lambda_function.py + read-only AWS state (get-role-policy, describe-task-definition) + git history. Rule-20 graph pre-change check rides AE's implementing commit (their lane; comp-blast on derive_runner per their TO mandate). CTO ran no infra change. |
