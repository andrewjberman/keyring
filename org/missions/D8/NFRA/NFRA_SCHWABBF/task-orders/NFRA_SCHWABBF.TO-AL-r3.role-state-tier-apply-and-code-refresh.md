# TO NFRA_SCHWABBF.TO-AL-r3 -- the Alongside box: apply the role's state-tier policy update and the VNC password secret, upload the box's four files, and refresh the box's copies (no Schwab contact; the fence row is NOT in this order)

<to_id>NFRA_SCHWABBF.TO-AL-r3</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>alongside-state-release</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-r-3` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) | **outcome_ref:** FWD-8 |
**depends_on:** `AL-i-2`, `AL-p-2`, `AL-e-2` (merged); `AL-s-3` (merged); pin `a51bd5cad5f`.

---

## WORKER FACE

### GO

GO -- written by 2.0.0_SA_COO~SA 2026-10-20 ~21:0xZ. The pair that covers this order's IAM change is SIGNED on both sides: COO `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SA/NEVER_WIDEN_ALONGSIDE_STATE_FENCE_COO_HALF.md` @5af57b99d0 (section 1, change 1: the Alongside root, one `aws_iam_role_policy` updated in place), CTO `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_ALONGSIDE_STATE_FENCE_CTO_HALF.md` @a9bc898596. The halves BIND (read both in full). **This order does NOT apply the fence row** (change 2 of that pair): the Cottonwood bucket's fence applies inside `2.0.0_SA_COO~SB`'s window 2026-10-21 12:00-20:00Z through her order `TO-BF-r3` (the CTO's condition 1: ride that apply, never `-target` beyond what that order names). You do not touch `shared-infra` or `infra/logic/registry`. **AMENDED ~21:3xZ (re-pinned to `a51bd5cad5f`):** the root now also creates the secret `schwab/alongside/vnc-credentials` (metadata only) and the role's write-only statement covers it; both are the CTO's own ruling (msg 110029: the TigerVNC server on the box requires a password stored in that secret, the box role cannot read it back) and the COO signs the same: the added blast radius is ONE new empty secret and ONE `PutSecretValue` resource, no read grant, nothing existing modified. CTO conditions still binding: the four rules stay DISABLED, and no pull runs beyond the first-day trace.

**ORDER OF WORK (issuer, ~21:4xZ, on the CTO's ask msg 110034 that the VNC path must not wait on the whole of r3):** do steps 0-6 of this order now (they end with the apply and its after-reads, and they create the VNC secret). Then do `TO-AL-r4` (org/missions/D8/NFRA/NFRA_SCHWABBF/task-orders/NFRA_SCHWABBF.TO-AL-r4.tigervnc-console-path.md) in full. Then return to steps 7-9 of this order (the four uploads, the box refresh, the ledger close): `r4` does not need them.

### THE CELL

`AL-r-3`. The Alongside role's inline policy changes in place (PRD v1.0 C-TIERS: its run records go to the Cottonwood firm bucket's state tier): two master-scope statements `MonolithSchwabOpsWrite` and `MonolithSchwabMetaPullsWrite` leave, one statement `StateTierWrite` arrives. The box's puller (`infra/aws/ec2/alongside-schwab-si2/sdd-daily-pull.ps1`) was re-synced to the amended 49F puller and `bootstrap.ps1` now installs the AWS CLI itself. The issuer's read-only plan at the pin (no apply, `-lock=false`, file `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SA/PLAN_READONLY_20261020_pina51bd5cad5f_ROLE_AND_VNC_SECRET.txt`) reads `Plan: 1 to add, 1 to change, 0 to destroy.`: the add is `aws_secretsmanager_secret.alongside_vnc_credentials`, the change is `aws_iam_role_policy.alongside_inline` updated in place. You apply that, upload the four files, and refresh the box's three code copies so the first-day pull (`TO-AL-r2`) runs the current puller. The state-tier writes themselves stay refused by the bucket fence until `TO-BF-r3` applies it; the puller treats a run-record write failure as a WARN, not a failed pull. You contact Schwab for nothing.

### DO, IN THIS ORDER (on the laptop; every Terraform command from the pinned worktree)

0. DISK: `df` on `C:` at least 5 GB free, else stop and report the figure.
1. Pinned worktree: `git worktree add --detach <scratch outside every other worktree> a51bd5cad5f`, sparse checkout of `.tools`, `lib`, `infra/aws/terraform/alongside-schwab-ec2`, `infra/aws/terraform/modules`, `infra/logic`, `org/standards`, `infra/aws/ec2/alongside-schwab-si2`, `org/critical_paths`. `git -C <scratch> status --porcelain` empty and `rev-parse HEAD` equals the pin.
2. Open the ledger entry `nfra-schwabbf-alongside-role-state-tier-20261020` with `python .tools/deploy_ledger.py open ...`: it names the one in-place IAM policy update, the three S3 uploads and the box-file refresh, and states "no resource added or destroyed". Commit entry and sentinel BEFORE the apply.
3. BEFORE reads saved to `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/r3/before.txt`: `aws iam get-role-policy --role-name schwab-alongside-si2-box-role --policy-name schwab-alongside-si2-box-policy` (the live policy; this is the rollback copy), and `aws secretsmanager describe-secret --secret-id schwab/alongside/vnc-credentials` must return ResourceNotFoundException (the secret is absent before the apply), and the SHA-256 of the three box files currently on the box (`C:/schwab-sdd/sdd-daily-pull.ps1`, `sdd-entitlements.ps1`, `bootstrap.ps1`) read over SSM (read-only `Get-FileHash`).
4. `TF_DATA_DIR` = a NEW scratch directory outside every git tree. In `infra/aws/terraform/alongside-schwab-ec2`: `terraform init -input=false` (a migrate or reconfigure prompt means STOP), then a saved plan `terraform plan -input=false -out=<scratch>/al.plan` (no `-target`, no `-var`). **Branch A exactly:** the summary is `Plan: 1 to add, 1 to change, 0 to destroy.`; the add is `aws_secretsmanager_secret.alongside_vnc_credentials` (metadata only, no `secret_version`); the one change is `aws_iam_role_policy.alongside_inline` in place; and `terraform show` of the plan shows ONLY: the statements `MonolithSchwabOpsWrite` and `MonolithSchwabMetaPullsWrite` removed, `StateTierWrite` added (8 resources: 4 masters x tables `pulls` and `daily_pull`, bucket `opal-data-cottonwood`, `s3:PutObject`), the statement `AlongsideEc2CredentialsWrite` renamed `AlongsideBoxSecretsWrite` with the two ARNs (ec2-credentials and vnc-credentials), `PutSecretValue` only, every other statement unchanged. **Anything else is Branch B: do not apply; report the summary and the first unexpected line to `2.0.0_SA_COO~SA`.**
5. Branch A: `bash .tools/safe-apply.sh -chdir=<root dir> apply <scratch>/al.plan` (never bare terraform apply).
6. AFTER reads saved to `.../r3/after.txt`: `aws iam get-role-policy` again (no `OpsWrite`/`MetaPullsWrite`, `StateTierWrite` with 8 resources, PutObject only, `AlongsideBoxSecretsWrite` with two ARNs); `aws secretsmanager describe-secret --secret-id schwab/alongside/vnc-credentials` returns the secret with NO `AWSCURRENT` version yet (METADATA ONLY, never get-secret-value; step 3 reads it as ResourceNotFoundException before the apply);  `terraform plan -input=false -detailed-exitcode` exits 0; `aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::313476888478:role/schwab-alongside-si2-box-role` with ONE action and ONE resource per call: `s3:PutObject` on `arn:aws:s3:::opal-data-cottonwood/schwab/cottonwood/state/pulls/date=2026-10-20/08719286.test.json` must read `allowed`; the same action on `.../state/complete/date=2026-10-20/08719286.test.json` and on `arn:aws:s3:::opal-data-assets/schwab/49financial/bronze/acc/date=2026-10-20/08403355.test.zip` must read `implicitDeny` (negative controls); and `secretsmanager:PutSecretValue` on the new secret's ARN must read `allowed` while `secretsmanager:GetSecretValue` on the same ARN reads `implicitDeny`. State plainly that this simulation reads the IDENTITY policy only; the bucket fence is not in it.
7. Upload from the pinned worktree to `s3://opal-data-assets/code/alongside-schwab-si2/` with `aws s3 cp <file> <dest> --sse AES256 --only-show-errors`: `bootstrap.ps1`, `keep-console.ps1`, `sdd-entitlements.ps1`, `sdd-daily-pull.ps1`. Print each local SHA-256.
8. Refresh the box's copies over SSM (a `commands` JSON from a NON-SHELL writer; forward slashes in on-box paths): for `sdd-daily-pull.ps1`, `sdd-entitlements.ps1` and `bootstrap.ps1`, `& 'C:/Program Files/Amazon/AWSCLIV2/aws.exe' s3 cp s3://opal-data-assets/code/alongside-schwab-si2/<file> C:/schwab-sdd/<file> --only-show-errors`, then print `Get-FileHash -Algorithm SHA256` of each. The three on-box hashes must equal the three local hashes of step 7. You do NOT run `bootstrap.ps1`, the entitlement script or the puller. (`keep-console.ps1` is unchanged and stays as bootstrap staged it; compare its on-box hash to the local one and report the result.)
9. Close the ledger, commit the evidence with `safe-commit.sh` paths-only, remove the pinned worktree if clean, and report to `2.0.0_SA_COO~SA`: the apply summary line, the after-read verdicts (allowed / the two implicitDeny controls), the four hashes local vs box, the commit hash, any row id.

### ACCEPTANCE (read by the issuer from your committed files)

<criterion id="AL2-r3-AC1" cell_refs="AL-r-3"><invocation>python .tools/proof-of-spec-check.py org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r3.role-state-tier-apply-and-code-refresh.proof_of_spec.json AL2-r3-AC1</invocation><expect>VALID</expect></criterion>
`AL2-r3-AC1` -- the proof instance records the apply summary, the after-reads of step 6 including the simulations, and the four local-versus-box hashes as artifact rows.

<expected_criteria>AL2-r3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder, the ledger folders named in step 2, and this order's file. `terraform init/plan/apply` ONLY in the Alongside root and ONLY through the steps above.
- **Never:** touching `shared-infra`, the registry or the fence; `get-secret-value` on any Alongside secret; enabling a rule; running the SI2 app, the puller, the entitlement script or any Schwab call; deleting or stopping anything; a bare `terraform apply`; editing a `.tf` file (a defect is a Branch B report).
- **A surprise row you file is committed AT ONCE** with `bash .tools/safe-commit.sh ... -- <the investigations file and your r3/ files>` (paths only) and its hash sent to `2.0.0_SA_COO~SA`; an uncommitted row blocks other workers' merges.
- **Refusal clause.** If a step cannot be met as written, stop, write the reason and the output in your report and a surprise row, and do not improvise.

<paths>
org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, enrichment), cell `AL-r-3`.
<owned_cells>AL-r-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AL2-r3-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r3.role-state-tier-apply-and-code-refresh.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL2-r3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message and a message to `2.0.0_SA_COO~SA`):** as step 9.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the four rules stay DISABLED and are not touched.
comp-iam: DECLARED-NOT-APPLICABLE as a tool run -- the change is one inline policy; its before and after are read with get-role-policy and tested with simulate-principal-policy including two negative controls.
comp-adversary: DECLARED-NOT-APPLICABLE -- the armed row NFRA_SCHWABBF-W15-S1 (the old puller on the box writes master-scope _ops, which this apply removes) is closed by the order of steps: the box's puller is refreshed in step 8 in the same order, and a run-record write failure is a WARN in the puller.
lane: the <paths> block IS the grant; CloudOps seats apply (rule 34).
</preflight>

Source: PRD v1.0 C-TIERS, C-ALONGSIDE; the fence pair (both halves); CTO condition 6; decomposition cell AL-r-3.
