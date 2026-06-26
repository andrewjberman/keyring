# comp-iam FALSE-MISSING root cause: cross-file Terraform resource-name collision

**Author:** 0.5.0_AE_OpalETL | **Date:** 2026-06-26 | **To:** 1.0.0_SA_CTO (comp-toolchain lane)
**Severity:** HIGH -- correctness bug in the Rule-20 deploy-gate tool. Directly produced a
misleading signal during the 06-26 CEO-brief outage diagnosis.
**Status:** Root cause CONFIRMED + grounded on source. Fix = CTO lane (extract_iam.py).

## TL;DR (and a correction)

`comp-iam service astn-wsjft-orchestrator` reported all 8 IAM operations as **MISSING** even
though (a) the Terraform DOES declare them and (b) I had just applied the policy live. I initially
mis-framed this as comp-iam "serving a stale cached snapshot of live AWS." **That framing is wrong
-- corrected here.** `comp-iam service`/`gaps` **never reads live AWS at all** (it parses Terraform
= DESIRED state; only the separate `reconcile` subcommand touches a live census). The real bug is a
**static Terraform-parser collision**: comp-iam keys roles by the *bare* TF resource name, not
namespaced by file/module, so two roots that reuse a generic local name (`orchestrator`,
`scheduler`, ...) collide -- last-writer-wins -- and the collision LOSER's role is credited with
**zero** policy statements => every action reports FALSE-MISSING.

This is neither a freshness/cache bug nor a census bug. It is a TF-parse keying defect.

## How it was found (grounded chain)

1. SYMPTOM: `comp-iam service astn-wsjft-orchestrator` -> all 8 ops `[MISSING]`, both before AND
   after my `terraform apply` landed the policy. (Invariant to the apply -> not a live-state read.)
2. SOURCE: `org/modules/graph/iam_cli.py` cmd_service calls `build_iam_report()` (parse TF + scan
   boto3 source); `cmd_reconcile` docstring is explicit: *"comp-iam's default modes parse Terraform
   = DESIRED state; they never see live AWS."* So `service` cannot be "stale live."
3. `comp-iam role astn-wsjft-orchestrator` -> **statements: 0**. `comp-iam role astn-wsjft-scheduler`
   -> **statements: 0**. A contrast role in another file (`etf-ownership-dashboard`) -> 6 statements,
   fine. => FILE-LEVEL failure on `astn-pipeline/orchestrator.tf`.
4. ISOLATED REPRO: ran `extract_iam._extract_tf_block` + `_parse_iam_statements` directly on
   orchestrator.tf -> parses **7** statements for the orchestrator policy (incl. ec2:StartInstances)
   and **1** for scheduler, linkage `role = aws_iam_role.orchestrator.id` resolves. So the policy
   parse + the role-ref regex are NOT the bug.
5. FULL-BUILD REPRO: `build_iam_report(workspace)` ->
   - `astn-wsjft-orchestrator-role` (tf_resource=orchestrator, astn-pipeline) -> **stmts=0**
   - `etfs-reports-orchestrator-role` (tf_resource=orchestrator, etfs-reports) -> stmts=16
   - `astn-wsjft-scheduler-role` (tf_resource=scheduler) -> **stmts=0**
   - `etfs-reports-scheduler-role` (tf_resource=scheduler) -> stmts=2
6. COLLISION CONFIRMED: `grep 'resource "aws_iam_role" "orchestrator"'` -> TWO files
   (astn-pipeline/orchestrator.tf + etfs-reports/orchestrator.tf); same for `"scheduler"`.

## Root cause (mechanism, source-grounded)

`org/modules/graph/extract_iam.py`, `build_iam_report()`:
- First pass (line ~792): `role_tf_to_name: dict[str,str]` maps **bare** `tf_resource` name ->
  `role_name`. Keyed by the local resource label only (`"orchestrator"`), NOT by (module/file,
  label). Two files both defining `resource "aws_iam_role" "orchestrator"` => the second scanned
  (etfs-reports, later in scan order than astn-pipeline) OVERWRITES the key.
- Second pass (line ~831-844): for each `aws_iam_role_policy`, it resolves the owning role via
  `role_name = role_tf_to_name.get(tf_role)` then `roles[role_name].statements.extend(stmts)`.
  - astn's `aws_iam_role_policy.orchestrator` (role ref `orchestrator`) resolves to the COLLISION
    WINNER `etfs-reports-orchestrator-role` -> astn's 7 statements are appended to the **wrong**
    role; `astn-wsjft-orchestrator-role` is never credited -> **stmts=0** -> all FALSE-MISSING.
  - The roles dict itself is keyed by role_NAME (both roles exist as separate entries), which is why
    you still SEE astn-wsjft-orchestrator-role -- just empty.

Two harms from one bug:
1. **FALSE-MISSING** on the collision loser (astn here): a correctly-declared (and applied) grant
   reported as missing.
2. **MIS-ATTRIBUTION** to the collision winner: the mechanism `.extend()`s the loser's statements
   onto the winner role, so the winner can be credited with grants it doesn't actually have (a
   FALSE-GRANTED / wrong-attribution risk). (etfs-reports-orchestrator-role shows 16 stmts; whether
   astn's 7 are double-counted in that total -- the mechanism implies yes -- is worth your confirm.)

## Blast radius

- CURRENT estate: 114 roles parsed; exactly **2 collision keys** (`orchestrator`, `scheduler`),
  each shared by astn-pipeline + etfs-reports. The **only** 2 roles with 0 parsed statements are the
  two astn roles -- i.e. the bug currently mis-reports precisely the roles behind the CEO-brief
  outage. (smartx schedulers escaped only because they use distinct labels model_monthly_scheduler
  / smartx_scheduler.)
- STRUCTURAL: recurs the instant any two TF roots reuse a generic local label. `orchestrator`,
  `scheduler`, `main`, `this`, `lambda_role`, `role`, `policy` are extremely common Terraform
  conventions -- this is a latent estate-wide trap, not an astn one-off.

## Severity

comp-iam is the Rule-20 / deploy-gate "missing perms before deploy" tool. A FALSE-MISSING erodes
trust + wastes diagnostic time (it sent me chasing a "still-broken" signal on an already-correct,
already-applied policy during a CEO-facing outage). The MIS-ATTRIBUTION direction is worse: a role
that looks GRANTED because it inherited another role's statements could greenlight a real gap to
ship. "Verify against live (get-role-policy)" is the correct interim ground-truth for any IAM
change until this is fixed -- comp-iam's DESIRED-state verdict is unreliable for any role whose
local label collides.

## Recommended fix (CTO lane)

Namespace the role key by module/file so labels are unique per root:
- Key `role_tf_to_name` by `(module_dir_or_relpath, tf_resource)` instead of bare `tf_resource`.
- In the policy-attach pass, resolve the policy's `role = aws_iam_role.<label>.id` ref **within the
  same file/module** (the ref is always module-local in Terraform), not against the global flat map.
- Add a guard/log when two roles would collide on a bare label (so a future collision is loud, not
  silent).
- Regression test: two fixture .tf files each with `aws_iam_role "orchestrator"` + an inline policy;
  assert each role gets ITS OWN statements and neither is 0/mis-attributed.

## Note on the "2nd independent observation"

You cited 0.6.0 hitting a comp-iam issue on cot firm-sep today. My estate scan shows only the 2
collision keys above (neither cot-related), and `service`/`gaps` never read live -- so the cot
observation may be a DIFFERENT root cause (possibly the `reconcile` census staleness, a separate
code path). Recommend triaging cot separately rather than assuming one shared root cause -- they may
be two distinct defects in the same tool.
