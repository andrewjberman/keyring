# TO COMM_ASSIST.TO-CA-j-7 -- round 18 CA-j-7: the Terraform file declares a resource policy that lets only the assistant's execution role read the ingress-mark key (the edit only; the apply is CA-j-8)

<to_id>COMM_ASSIST.TO-CA-j-7</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~22</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>INGRESSKEY</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-7` (`decompositions/COMM_ASSIST_DECOMP.round18.md`, AMENDMENT 4) | **outcome_ref:** FWD-7 |
**depends_on:** CA-j-3 (CLOSED @1daa4a97ce); the CTO ruling `CTO_RULING_20261014_052xZ_COMM_ASSIST_INGRESS_MARK_KEY_NARROWED.md`

---

## WORKER FACE

### THE CELL

The assistant's two Lambdas (LDO-001, `module "ldo_001"` in `infra/aws/terraform/transcripts/chat_assist.tf`) mark every event they make for Andrew's texts with an HMAC keyed by the Secrets Manager secret `aws_secretsmanager_secret.ca_ingress_mark`
(`teams/global/ingress-mark`). Today any identity with administrator access can read that key, including the Dell agent users, so a valid mark could be forged. The CTO ruled that the key is narrowed: a RESOURCE POLICY on the secret DENIES `secretsmanager:GetSecretValue` to every principal except the assistant's execution role (the one role both Lambdas share). Management acts (put a new value, change or delete the policy, describe) stay open to admins; only reading the value is denied. This cell writes that policy into the Terraform file so the deploy that follows (cell CA-j-8, a separate act by a CloudOps seat) applies it. You edit the file and run NOTHING against AWS: no init, no plan, no apply; only `terraform fmt`.

### BUILD

1. In `chat_assist.tf`, after `module "ldo_001"` and before `output "ldo_001_manifest"`, add exactly this resource (then `terraform fmt` aligns it):

```
resource "aws_secretsmanager_secret_policy" "ca_ingress_mark" {
  secret_arn = aws_secretsmanager_secret.ca_ingress_mark.arn
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid       = "OnlyTheAssistantReadsTheMarkKey"
      Effect    = "Deny"
      Principal = "*"
      Action    = "secretsmanager:GetSecretValue"
      Resource  = aws_secretsmanager_secret.ca_ingress_mark.arn
      Condition = { StringNotEquals = { "aws:PrincipalArn" = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:role/${module.ldo_001.execution_role_name}" } }
    }]
  })
}
```

2. Above it, add a short comment (two or three lines): the CTO ruling `CTO_RULING_20261014_052xZ_COMM_ASSIST_INGRESS_MARK_KEY_NARROWED.md`; the policy denies only the value read; an admin can still rewrite the policy (a recorded management write, the residual stated in the PRD addendum).
3. Format with `terraform fmt` on that one file only. Edit nothing else. No other variable, resource, module call or file changes. Type no account number or role name: the ARN is built from `data.aws_caller_identity.current.account_id` and `module.ldo_001.execution_role_name` exactly as above. No non-ASCII.

### RULES

- Edit nothing but the files in `<paths>`. No `terraform init`, `plan`, `apply` or any AWS call; only `terraform fmt`.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj7-AC1" cell_refs="CA-j-7"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j7_tf.py"</invocation><expect>J7-TF ok=True arms=6 of 6</expect></criterion>
`CAj7-AC1` -- the issuer's check (read it; do not edit it): the policy resource is attached to the mark secret; one statement, Effect Deny, Principal `*`, the one action `secretsmanager:GetSecretValue`; the exception is a `StringNotEquals` on `aws:PrincipalArn` built from the module's `execution_role_name` and the caller identity, never a typed ARN; no Allow, no wildcard action, no second statement; the secret shell, its read grant and the mode from CA-j-2 are untouched (the CA-j-2 check still reads 7 of 7); `terraform fmt -check` passes. It prints ok=False at the base (2 of 6).

<criterion id="CAj7-AC2" cell_refs="CA-j-7"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i4a_tf.py"</invocation><expect>I4A-TF ok=True</expect></criterion>
`CAj7-AC2` -- the bound, a control that PASSES at the base and must still pass: muse's key pin and the mail-bearer join are unchanged and the file is formatted.
</proof_of_spec>

<expected_criteria>CAj7-AC1,CAj7-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~22/COMM_ASSIST.TO-CA-j-7.ingress-mark-key-resource-policy-in-terraform.proof_of_spec.json`. Model its structure on the prior instance for the same kind of edit, `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~21/COMM_ASSIST.TO-CA-j-2.ingress-mark-secret-and-mode-in-terraform.proof_of_spec.json`. Pin its `chat_assist.tf` artifact row to the commit that carries the edit (commit the edit FIRST, then write the instance and pin that hash: a row left as pending-this-commit goes INVALID the moment a later commit lands). Validate it by running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree AFTER your last commit: `python .tools/proof-of-spec-check.py <instance> CAj7-AC1,CAj7-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID at the final head. Your final report names the lines you added. Your surprise rows are `COMM_ASSIST-W22-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-7</owned_cells>
</decomp_ref>

<paths>
infra/aws/terraform/transcripts/chat_assist.tf
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-7.ingress-mark-key-resource-policy-in-terraform.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~22/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing and applies nothing.
comp-iam: RUN -- the one policy declared is a resource policy on ONE secret that only DENIES the value read to everyone but the execution role; it grants nothing and moves no identity policy. Measured by the issuer at ~05:3xZ with `simulate-principal-policy` and this exact policy supplied: the execution role `GetSecretValue` reads allowed, `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user` read explicitDeny (and allowed with no policy). Denominator: 3 principals simulated. BLIND: the policy is not live until CA-j-8; its live read is that cell's check.
comp-adversary: RUN -- a policy that also locks out the assistant (refused: AC1 `scope` arm pins the exception to the execution role; the issuer's simulation read allowed for it); a typed account number or role name (refused: AC1 `scope` arm rejects a literal ARN); a second statement or an Allow riding the policy (refused: AC1 `narrow` arm); a wildcard action that also denies management acts (refused: AC1 `deny` arm pins the one action); the CA-j-2 shell or mode disturbed (refused: AC1 `keep` arm). BLIND: that Terraform accepts the file is read by the plan in CA-j-8, not here.
naming: no name is created (a resource policy has none); the secret is the CA-j-2 shell named by its NAMES.json row (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1). Declared WORLD because the gate infers that floor from an infrastructure path; the act itself is an edit with no apply, so its close is the file and its check. The apply is cell CA-j-8 with its own pair.
</preflight>

Base: CAj7-AC1 base: FAIL as expected (2 of 6; the CA-j-2 shell and the formatting hold, the policy does not exist). CAj7-AC2 base: PASS as expected (control). AC1 green arm: PASS as expected (6 of 6) against a scratch copy carrying the intended edit; two negative controls read ok=False as intended (an Allow statement fails `deny` and `narrow`; a typed role name fails `scope`).
Source: CTO ruling `CTO_RULING_20261014_052xZ_COMM_ASSIST_INGRESS_MARK_KEY_NARROWED.md` (msg 109075); CVO half of CA-j-3 (AMENDMENT 3 of the round-18 decomposition); the module output `execution_role_name` (`infra/aws/terraform/modules/ldo/outputs.tf`).
