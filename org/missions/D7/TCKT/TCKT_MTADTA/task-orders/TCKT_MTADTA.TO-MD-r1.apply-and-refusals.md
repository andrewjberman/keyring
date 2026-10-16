# TO TCKT_MTADTA.TO-MD-r1 -- the release, part 1: one apply of the trino root, then FWD-8's first half exercised live

<to_id>TCKT_MTADTA.TO-MD-r1</to_id>
<project>TCKT_MTADTA</project>
<issued_to>0.7.0_AE_CloudOps~TM1</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D7 | **Fabric:** dell1 | **Decomp cell:** `MD-r-1` (`decompositions/TCKT_MTADTA_DECOMP_R2.md`) |
**outcome_ref:** FWD-8, FWD-1 | **depends_on:** `MD-x-1` and `MD-x-2` MERGED to the box branch. **STAGED: the issuer flips this order to `pending` (the GO) after both merges.**

---

## WORKER FACE

### THE CELL

`MD-r-1`: the first live act of TCKT_MTADTA. Nothing of this project exists in the account yet. You apply the Terraform root `infra/aws/terraform/trino/` ONCE, then exercise the first half
of FWD-8 against the live account. The root creates only NEW things (measured at the cut: no resource of it exists): the bucket `opal-data-trino` with its default KMS encryption and
public-access block, a customer-managed KMS key and alias, the IAM group `globgrph-trino-access-group`, the Lambda `globgrph-trino-access-lambda` with its role, two aliases (`collector`,
`member`), the bucket policy and the key policy, two Secrets Manager CONTAINERS (no value), the collector Lambda `m365-metadata-trino-collector-lambda`, its role, its hourly EventBridge rule
`m365-metadata-trino-collector-hourly` and their log groups. Read `infra/aws/terraform/trino/access.tf` (its header states the design and the residuals), `main.tf`, `identity.tf`,
`collector.tf`, and `org/missions/D7/TCKT/TCKT_MTADTA/prd/TCKT_MTADTA_PRD.md` rows C-ACCESS and C-RESIDUAL.

**What the design guarantees, and what you are proving.** Only the access role may touch an object; every other principal, administrators and YOU included (you run as the IAM user
`cloudops-dell1-agent-user`, measured at the cut), is denied every object data action; only members of `globgrph-trino-access-group` may invoke the `member` alias; only the collector role may
invoke the `collector` alias. You are deliberately NOT a member of the group: that is what makes your refusals meaningful. **You add exactly one member to the group, and only under item 7b** (the CTO ruled it on call 0017: `Andrew_Berman` alone, MFA-gated). You add no seat, no agent user and nobody else.

### ITEMS, in this order. Stop at the first that fails and write what stands.

1. **Preconditions.** `git log` of your worktree's base shows both repair merges: `TO-MD-x1` and `TO-MD-x2` complete (`<status>complete</status>`, proofs VALID). The three `r2_check_x*.py` checks
   print their OK tokens from the repository root. If not, STOP and report.
2. **Open the ledger** before any write: `python .tools/deploy_ledger.py open --slug tckt-mtadta-trino-root-apply-20261016 --title "TCKT_MTADTA round 2: apply the trino root (new resources only)" --author 0.7.0_AE_CloudOps~TM1 --leg ...`
   with the legs you will verify (apply, bucket policy, key policy, aliases, group). Record the blast radius: NEW resources only, nothing existing touched; the rollback per
   resource (`terraform destroy` of the root is safe while the bucket is empty; the key then waits out its 30-day deletion window).
3. **Office egress addresses (C-FIELDS (d)).** Look for where the estate holds Opal's office egress addresses (`comp-estate`, `comp-which "office egress ip addresses"`, `docs/`). If you find an
   authoritative list, put the addresses in `data/m365_metadata/scripts/population.json` key `office_ips` and commit it; if you find none, leave `office_ips` empty (every address then
   reads `remote`), and file a surprise row saying so. NEVER invent an address.
4. **Build the two zips** from the repository root: `bash infra/aws/lambda/globgrph-trino-access/build.sh` and `bash infra/aws/lambda/m365-metadata-collector/build.sh`. Neither zip is committed.
5. **The layer.** `access.tf` takes `var.pandas_layer_arn`. Read the CURRENT version ARN of the AWS-managed `AWSSDKPandas-Python312` layer for us-east-1
   (`aws lambda list-layer-versions --layer-name arn:aws:lambda:us-east-1:336392948345:layer:AWSSDKPandas-Python312 --max-items 1`; confirm the account in the ARN with `aws lambda get-layer-version-by-arn`),
   write `pandas_layer_arn = "<that ARN>"` to `infra/aws/terraform/trino/layer.auto.tfvars`, and commit that one file. It is a public AWS ARN, not a secret.
6. **Plan, read it, apply once.** `terraform -chdir=infra/aws/terraform/trino init`, then `plan -out=<file under your scratch>`. Read the plan: every line is a CREATE, no resource is destroyed or
   replaced, and the count matches the resources named in THE CELL. Then ONE apply through the gate: `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/trino apply <that plan file>` (never bare
   `terraform apply`). If the apply fails half-way, finish it in-session or roll back and escalate loudly; never leave it half-landed (NEVER-2).
7. **The access gate, in four acts (AMENDED 2026-10-16 ~08:5xZ on the CTO's rulings, msgs 6605 and 6614; ledger `ledger/CTO_RULING_R2_ADMIN_INVOKE_20261016.md`).** The first apply left an
   IAM administrator (and you) able to invoke both aliases with no MFA, because the group policy and the resource permission only GRANT and nothing DENIES. Do these under the SAME ledger entry (add legs):
   - **7a. MFA on the group's invoke.** Edit `infra/aws/terraform/trino/access.tf`: the statement in `aws_iam_group_policy.invoke` gets `Condition = { Bool = { "aws:MultiFactorAuthPresent" = "true" } }`.
     Nothing else in that file changes. `terraform fmt`, `plan` (an in-place update of that one policy only), then `bash .tools/safe-apply.sh ... apply <plan>`.
   - **7b. The one member.** Confirm `aws iam list-mfa-devices --user-name Andrew_Berman` lists at least one device (print the COUNT only). If it does, `aws iam add-user-to-group --group-name globgrph-trino-access-group --user-name Andrew_Berman`.
     If it lists none, add NOBODY, and report: the CTO's fallback is a new personal identity for Andrew (his act), never a seat or agent user. Nobody else is ever added in this order.
   - **7c. The Deny that binds administrators (the CTO's ruling (a)).** For EACH alias, add a resource-policy statement: `Effect: Deny`, `Principal: *`, `Action: lambda:InvokeFunction`, `Resource` the alias ARN, `Condition: BoolIfExists
     aws:MultiFactorAuthPresent = false`; on the `collector` alias the Deny also carries `StringNotEquals aws:PrincipalArn = <the collector role ARN>` (the carve-out, so its scheduled invoke still works). Terraform's
     `aws_lambda_permission` cannot express a Deny: use the Lambda API (`aws lambda put-resource-policy`, or the call the CLI offers that edits an alias's resource policy; read `aws lambda put-resource-policy help`),
     and KEEP the existing Allow statement of `aws_lambda_permission.collector_invoke` (the Deny must not remove it). Commit the exact policy JSON you put at
     `infra/aws/terraform/trino/door_resource_policy.json` and the drift in one paragraph at `infra/aws/terraform/trino/door_resource_policy.README.md` (what Terraform does not manage, how to re-apply it, what an
     `aws_lambda_permission` change would do to it). **If the API refuses a Deny, or the probe in 7d still reads rc=0, do (d) instead:** an explicit identity-side Deny on `lambda:InvokeFunction` for the door's ARNs unless MFA is
     present, attached to every principal holding an invoke grant (`AdministratorAccessOpalCapital`, `cloudops-dell-agents-group`, `cloudops-dell1-agent-user`, `Andrew_Berman`), found by an `iam simulate-principal-policy`
     census over all roles with its denominator printed; the same probe proves it; report which one landed.
   - **7d. The probe.** The same call that read rc=0 (`aws lambda invoke --function-name globgrph-trino-access-lambda --qualifier member --payload e30= <file>` as you, no MFA) must now read AccessDenied, and so must the `collector` alias.
     The collector role's own invoke must still work (AC2 simulates it with the new policy).
8. **Prove it** from the repository root, and read each output: `r2_check_r1.py applied`, `r2_check_r1.py refusals`, `r2_check_r1.py plan` (a plan after every policy has landed exits 0), `r2_check_r1.py mfa`.
   The admin `GetObject` probe is NOT run here: on a key that does not exist S3 answers NoSuchKey. It runs in `MD-r-2` after the first clean fire (`r2_check_r1.py getobject`).
9. **Close the ledger** with the read-back (the check lines), and write your report. Release acts 3 and 4 (`MD-r-2`: the consent, the secret values, the real fires) do not start until 7d reads AccessDenied.

### ACCEPTANCE

<criterion id="MD2-r1-AC1" cell_refs="MD-r-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_r1.py applied</invocation><expect>R1-APPLIED-OK</expect></criterion>
`MD2-r1-AC1` -- the live bucket policy denies the object data actions to every principal but the access role (and does not deny ListBucket), the key policy admits root and the role alone, the two aliases and the group exist.

<criterion id="MD2-r1-AC2" cell_refs="MD-r-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_r1.py refusals</invocation><expect>R1-REFUSALS-OK</expect></criterion>
`MD2-r1-AC2` -- the box identity with no MFA is refused with AccessDenied on BOTH aliases, and the collector role is simulated able to invoke its own alias under the new Deny (the carve-out) and nothing else (no member alias, no S3 read, no KMS action).

<criterion id="MD2-r1-AC3" cell_refs="MD-r-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_r1.py plan</invocation><expect>R1-PLAN-OK</expect></criterion>
`MD2-r1-AC3` -- `terraform plan -detailed-exitcode` on the root after the policy lands exits 0.

<criterion id="MD2-r1-AC4" cell_refs="MD-r-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R2_CHECKS/r2_check_r1.py mfa</invocation><expect>R1-MFA-OK</expect></criterion>
`MD2-r1-AC4` -- (a fourth mechanical criterion, with this reason: the CTO's call-0017 ruling, msg 6605, added the MFA gate and the one member after the cut) the group's invoke Allow carries `aws:MultiFactorAuthPresent`, the group holds `Andrew_Berman` alone, and he has an MFA device.

<expected_criteria>MD2-r1-AC1,MD2-r1-AC2,MD2-r1-AC3,MD2-r1-AC4</expected_criteria>

Dry-run at the base 2026-10-16 ~08:5xZ: AC1 `R1-APPLIED-REFUSED no bucket policy (... NoSuchBucket ...)`, AC2 `R1-REFUSALS-REFUSED an admin GetObject was not refused (rc=254); ...`,
AC3 `R1-PLAN-REFUSED exit=1 ...` -- each FAIL as expected. These are LIVE reads (get, describe, simulate) and one `terraform plan`; none writes.

## BOUNDS

- **Grant.** AWS: create the root's resources through the one gated apply; read, describe and simulate for the checks. Repo: `org/critical_paths/change_management/`, `org/critical_paths/.open_deploys/`,
  `infra/aws/terraform/trino/layer.auto.tfvars`, `data/m365_metadata/scripts/population.json` (item 3 only), the investigation file, and this order's file.
- **NEVER** bare `terraform apply` (use `.tools/safe-apply.sh`), `aws lambda update-function-code`, a grant to yourself, a group member other than the one item 7b names, a delete of any object, a change to any resource outside the root, an
  alarm, SNS topic or notification resource (standing moratorium), a push, or a change to any module. You do not read stored objects and you do not invoke the door.
- **No secret value, tenant id, client id or token** in a ledger entry, a record, a row or a message.
- **Refusal clause.** If a criterion cannot be met as written, stop. Roll back what you created if it is half-landed, write the reason in the ledger, and file a NEW surprise row (id
  `TCKT_MTADTA-D1-WTM1-S<k>`, `"fabric": "dell1"`). Do not weaken the test.
- Commit only through `.tools/safe-commit.sh` with your own `--author "0.7.0_AE_CloudOps~TM1 <0.7.0_AE_CloudOps~TM1@opal.agent>"`, `-F` a message file written with the Write tool, and `-- <paths>`.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/terraform/trino/layer.auto.tfvars
infra/aws/terraform/trino/access.tf
infra/aws/terraform/trino/door_resource_policy.json
infra/aws/terraform/trino/door_resource_policy.README.md
data/m365_metadata/scripts/population.json
org/missions/D7/TCKT/TCKT_MTADTA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your repo WRITE grant. Your AWS grant is the root's creation and the reads named above.

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP_R2.md</decomp_doc> (round 2), cell `MD-r-1`.
<owned_cells>MD-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: MD2-r1-AC1, MD2-r1-AC2, MD2-r1-AC3, MD2-r1-AC4. Instance at `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.7.0_AE_CloudOps~TM1/TCKT_MTADTA.TO-MD-r1.apply-and-refusals.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> MD2-r1-AC1,MD2-r1-AC2,MD2-r1-AC3,MD2-r1-AC4` BEFORE the flip. All four are mechanical.
</proof_of_spec>

**REPORT:** the ledger entry; the plan's create count and the statement that nothing is destroyed or replaced; the apply line; the three check lines; every refusal and denial verbatim; the layer ARN
used; whether office egress addresses were found (and where). No secret, tenant or client value.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at MD-r-2 (the hourly rule); here the rule is created and left as built.
comp-iam: RUN -- `iam simulate-principal-policy` on the collector role inside AC2; BLIND: the group has no member until Andrew's word.
comp-adversary: RUN in AC2 -- the admin GetObject, the non-member invoke and the collector grants are tried, not read; BLIND: the root user and any principal that can edit the policies (PRD C-RESIDUAL (1)(2)), stated for the FWD-8 statement.
lane: WORLD apply by a CloudOps seat under a change-management entry; CTO + COO halves are this order and the CTO's round-1 analysis (msg 6588) naming the release.
</preflight>

**ISSUER NOTES:** Source: CTO round-1 analysis item 1(a) and item 2; PRD v0.4. The collector's hourly rule starts firing as soon as the root is applied, and its credential secret has no value until MD-r-2:
those early invocations fail at the secret read (expected). MD-r-2's fire check counts only invocations after the subscriptions start.
