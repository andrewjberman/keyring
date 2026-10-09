# Deploy Completion Record
**Date opened:** 2026-10-09T07:32:15.619496+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: sovereign / iam:SimulatePrincipalPolicy on arn:aws:iam::313476888478:role/cot-rebalancer-runner-role for the caller arn:aws:iam::313476888478:user/cloudops-dell1-agent-user -- a dell1 IAM-parity gap that only C5 needs. L3's C4 arm IS proven (live policy 4 statements, ReadOwnRunResult with the exact ARN, DenyBlackdiamond49fFirmSep unchanged, re-plan 0-diff); only C5's three simulate arms are unrunnable here. CONTROLLED, so this is the instrument and not the world: the SAME action against the caller's OWN user ARN returns 'allowed', so the grant is RESOURCE-SCOPED to self, not absent wholesale; iam:SimulateCustomPolicy is denied too, so there is no substitute instrument on this box. Needs the grant, or the issuer grades C5 from a box that holds the action. (held since 2026-10-09T07:40:31.977692+00:00)
**Deploy:** MDPF_HEALGAP R2-1 / HG-t-8: add s3:GetObject on the runner's own meta/*-result.json to cot-rebalancer-runner-role (amendment A1, CTO ruling H)
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf ReadOwnRunResult statement committed | the commit hash, plus C1 IAM-OK, C2 FMT-OK and C8 naming-gate PASS at those bytes | PASS. Commit ba88934f7b (1 file changed, 7 insertions, 0 deletions) carries the ReadOwnRunResult statement with the Resource read from the grammar: "arn:aws:s3:::${local.monolith_bucket}/blackdiamond/${one(local.monolith_source_scopes.blackdiamond)}/meta/*-result.json" (amendment A1 @83028dca8a, read verbatim at its pin; CTO ruling H @1af255b7da). At those bytes: C1 hg_t8_iam.py IAM-OK statements=4 (base reads IAM-BAD 0 of 1, so the control moved); C2 hg_tf_fmt.py FMT-OK, corroborated by terraform fmt -check -diff rc=0; C8 naming-gate.py --diff --enforce NAMING-GATE PASS 0 graded rc=0, and the same limb PASSED again inside safe-commit, denominator 1 of 1 path seen. LF preserved, 0 non-ASCII. The earlier typed-cottonwood cut was REFUSED by this limb and is recorded in row MDPF_HEALGAP-D1-S9 @20ec950171. | CLOSED 20261009T073250Z |
| L2 | activation | targeted safe-apply of aws_iam_role_policy.cot_rebalancer_runner_write in infra/aws/terraform/opal-assets | C3: plan reads 0 to add 1 to change 0 to destroy and prints the identical rendered ARN; the safe-apply line | PASS. C3 graded per-attribute from terraform show -json BEFORE the apply, never from the summary line: 2 resource_changes, 1 no-op, 1 update; the ONLY mover is aws_iam_role_policy.cot_rebalancer_runner_write; the ONLY attribute with before != after is 'policy' (name and role both before==after, so no ForceNew attribute moved -- the monolith.tf:79-81 ForceNew-description hazard does not reach a policy document); statements 3 -> 4 with exactly ONE added, zero removed; the added statement renders Resource arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/meta/*-result.json, IDENTICAL to the refused typed form as amendment A1 requires; DenyBlackdiamond49fFirmSep byte-identical before and after. Summary line: 'Plan: 0 to add, 1 to change, 0 to destroy.' Applied via .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply <the graded planfile> -- the SAVED plan, so the applied bytes are the graded bytes and safe-apply reads a planfile with show -json rather than re-planning. CONVERGENCE PROVEN AFTER: a re-plan at the same target reads 'No changes. Your infrastructure matches the configuration.' with -detailed-exitcode rc=0. No HALTGT pass is cited (ADHC_HALTGT: a pass is not evidence a halt was absent). | CLOSED 20261009T073931Z |
| L3 | verify | the live policy and the live principal | C4: four statements with ReadOwnRunResult and DenyBlackdiamond49fFirmSep unchanged; C5: allowed / implicitDeny / explicitDeny from three SEPARATE simulate invocations |  | OPEN |

## Log

- 20261009T073215Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 3 leg(s)
- 20261009T073250Z LEG L1 closed: PASS. Commit ba88934f7b (1 file changed, 7 insertions, 0 deletions) carries the ReadOwnRunResult statement with the Reso
- 20261009T073931Z LEG L2 closed: PASS. C3 graded per-attribute from terraform show -json BEFORE the apply, never from the summary line: 2 resource_change
- 20261009T074031Z HELD-SOVEREIGN-GATED gate=sovereign/iam:SimulatePrincipalPolicy on arn:aws:iam::313476888478:role/cot-rebalancer-run
