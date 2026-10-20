# TO NFRA_SCHWABBF.TO-AL-r1 -- build the Alongside Schwab Box: apply the new Terraform root, upload its code, bootstrap it, and report it ready for Andrew's RDP sitting

<to_id>NFRA_SCHWABBF.TO-AL-r1</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>alongside-release</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-r-1` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) | **outcome_ref:** FWD-8 |
**depends_on:** cells AL-a-1, AL-s-1, AL-e-1, AL-p-1 (all merged; pin `7ce88d5bdd9`). **GO:** this order is `staged`. The issuer writes the GO line below and flips it to `pending` when BOTH never-widen halves are signed on the pin. Do not act before that flip.

---

## WORKER FACE

### GO

GO -- written by 2.0.0_SA_COO~SA 2026-10-20 ~17:3xZ. Both halves are SIGNED on the pin `7ce88d5bdd9`: COO `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SA/NEVER_WIDEN_HALF_COO_NFRA_SCHWABBF_ALONGSIDE_BOX_BUILD_20261020.md` @d95613759f, CTO `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_HALF_CTO_NFRA_SCHWABBF_ALONGSIDE_BOX_BUILD_20261020.md` @6ec45777af (it sits in the CTO's folder because the owned-paths gate refuses the CTO a write in the COO's). The CTO half adds condition 6, which BINDS you: no rule is enabled, and no pull runs beyond the first-day trace, until the role's tier statements match PRD v0.9 C-TIERS; this order enables nothing and pulls nothing. The halves BIND: the COO half's Branch A / Branch B and its conditions ARE the procedure. Read both in full.

### THE CELL

`AL-r-1`. Andrew-direct 2026-10-20 ~13:5xZ: "it should be exact same setup and logic as already exists with the 49 schwab box. this one should explicitly be labeled as an alongside box"; "I will need to RDP into the EC2 box most likely to get that done". Andrew-direct ~16:3xZ: "I want the new Cottonwood accounts taken care of". The Terraform root `infra/aws/terraform/alongside-schwab-ec2/` creates the NEW Windows EC2 "Alongside Schwab Box", its role, profile, security group (NO ingress), two secrets (one adopted by import), four DISABLED EventBridge rules and their events role. Nothing existing is modified. You apply it, upload the box's code, bootstrap the box, and prove it is ready for Andrew's RDP sitting. You do NOT run the SI2 app, sign in, pull from Schwab, read any secret value, enable any rule, or touch the 49F box `i-0f3d57a97f14727af` or anything named `canonical-schwab-*` / `quartz-si2-*`.

**The measured plan (the issuer's read-only plan of 2026-10-20 ~17:2xZ at the pin, no apply, no lock):** `Plan: 1 to import, 17 to add, 0 to change, 0 to destroy.` The file is committed beside the COO half: `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SA/PLAN_READONLY_20261020_pin7ce88d5bdd9_MERGED.txt`. The 17 adds: 1 role, 1 role-policy attachment, 1 inline role policy, 1 instance profile, 1 security group, 1 instance, 1 secret (`schwab/alongside/ec2-credentials`), 4 EventBridge rules, 4 targets, 1 events role, 1 events role policy. The 1 import: the existing secret `schwab/alongside/sdd-credentials` (metadata only, `description` ignored).

### DO, IN THIS ORDER (on the laptop; every Terraform command from the pinned worktree)

0. DISK: `df` on `C:` at least 5 GB free; below that, create nothing, stop and report the figure.
1. Pinned worktree: `git worktree add --detach <scratch outside every other worktree> 7ce88d5bdd9`, sparse checkout of `.tools`, `lib`, `infra/aws/terraform/alongside-schwab-ec2`, `infra/aws/terraform/modules`, `infra/logic`, `org/standards`, `infra/aws/ec2/alongside-schwab-si2`, `org/critical_paths`. `git -C <scratch> status --porcelain` must be empty and `git -C <scratch> rev-parse HEAD` must read the pin. If the pin is not an ancestor of the trunk you are on, stop and report.
2. Open the change-management ledger entry `nfra-schwabbf-alongside-box-build-20261020` with `python .tools/deploy_ledger.py open ...` (read its usage): it names the Terraform root, all 17 resources and the 1 import, and states "nothing existing is modified". Commit the entry AND its sentinel `org/critical_paths/.open_deploys/<slug>.json` BEFORE the apply.
3. BEFORE reads, saved to `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/r1/before.txt`: (a) `aws ec2 describe-instances --filters "Name=tag:Device,Values=Alongside Schwab Box" --query "Reservations[].Instances[].InstanceId"` must read empty; (b) `aws secretsmanager describe-secret --secret-id schwab/alongside/sdd-credentials` returns the secret and `aws secretsmanager describe-secret --secret-id schwab/alongside/ec2-credentials` returns ResourceNotFoundException (METADATA ONLY; never `get-secret-value`); (c) `aws events list-rules --name-prefix schwab-08719286` empty and the same for the other three masters 08134043, 08165601, 08480305. Any other reading: stop, Branch B.
4. `TF_DATA_DIR` = a NEW scratch directory outside every git tree. In `infra/aws/terraform/alongside-schwab-ec2`: `terraform init -input=false` (a migrate or reconfigure prompt means STOP), then a saved plan `terraform plan -input=false -out=<scratch>/al.plan` with NO `-target` and NO `-var`. Save the plan text. **Branch A exactly:** the summary line is `Plan: 1 to import, 17 to add, 0 to change, 0 to destroy.` and `terraform show` of the plan lists no `update`, `replace` or `delete` and no resource that is not one of the 17 adds or the one import. **Anything else is Branch B: do not apply; report the plan summary and the first unexpected line to `2.0.0_SA_COO~SA`.**
5. Branch A: apply that saved plan through `bash .tools/safe-apply.sh -chdir=<root dir> apply <scratch>/al.plan` (never bare terraform apply). Capture the apply's output and the output values (`alongside_box_instance_id`, `alongside_box_role_arn`, `alongside_box_security_group_id`).
6. AFTER reads (live AWS `describe`/`get`, saved to `.../r1/after.txt`): the instance is `running` with the tag `Device=Alongside Schwab Box`, `HttpTokens=required`, the profile `schwab-alongside-si2-box-profile`; the security group has ZERO ingress rules; the four rules exist with `State: DISABLED` (`aws events describe-rule`); both secrets exist and `schwab/alongside/sdd-credentials` is unchanged (its `Description` still present, `LastChangedDate` unchanged from step 3b); `terraform plan -input=false -detailed-exitcode` from the same root now exits 0 (no drift).
7. Upload the box code (an `aws s3 cp` per file from the pinned worktree, `--sse AES256 --only-show-errors`, then `aws s3api head-object` for size): `infra/aws/ec2/alongside-schwab-si2/bootstrap.ps1`, `keep-console.ps1`, `sdd-entitlements.ps1`, `sdd-daily-pull.ps1` to `s3://opal-data-assets/code/alongside-schwab-si2/<same file name>`. Print the four local sha256 values and the four uploaded sizes; they must match.
8. Wait for the instance to be SSM-managed: poll `aws ssm describe-instance-information --filters Key=InstanceIds,Values=<id>` until `PingStatus` is `Online` (a fresh Windows host takes several minutes; give it up to 20 minutes, then stop and report).
9. Bootstrap over SSM. **AMENDED 2026-10-20 ~18:1xZ by the issuer on your row `NFRA_SCHWABBF-R1-S1` (the new host is a stock Windows Server 2022 image: it carries AWS Tools for PowerShell but NOT the AWS CLI v2 the 49F box had installed by hand; steps 0-8 stand as you ran them).** Two SSM invocations, each with its `commands` JSON written by a NON-SHELL writer (a backslash typed in a shell heredoc is halved; use forward slashes in every on-box path, which Windows accepts), document `AWS-RunPowerShellScript`:
   - **9a, install the AWS CLI v2 (the 49F box's installed state, reproduced):** commands: `$ErrorActionPreference='Continue'`; `[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12`; `New-Item -ItemType Directory -Force C:/schwab-sdd | Out-Null`; if `C:/Program Files/Amazon/AWSCLIV2/aws.exe` is absent: `Invoke-WebRequest -UseBasicParsing https://awscli.amazonaws.com/AWSCLIV2.msi -OutFile C:/schwab-sdd/AWSCLIV2.msi`, then `$p = Start-Process msiexec.exe -ArgumentList '/i','C:/schwab-sdd/AWSCLIV2.msi','/qn','/norestart' -Wait -PassThru` and require `$p.ExitCode` 0 or 3010; then `& 'C:/Program Files/Amazon/AWSCLIV2/aws.exe' --version` must print `aws-cli/2.`; then `Remove-Item C:/schwab-sdd/AWSCLIV2.msi`. Read the invocation output: status `Success`, the version line printed. If the download or install fails, stop and report the output (Branch B for this step); do not improvise another install route. The MSI is AWS's own download, fetched over HTTPS by the box (its egress is open; the role needs no S3 grant for it).
   - **9b, bootstrap:** commands: `& 'C:/Program Files/Amazon/AWSCLIV2/aws.exe' s3 cp s3://opal-data-assets/code/alongside-schwab-si2/bootstrap.ps1 C:/schwab-sdd/bootstrap.ps1 --only-show-errors`; then `powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:/schwab-sdd/bootstrap.ps1`. Read the invocation output: every step line must read `OK:` and the invocation `Success`. The output must contain no password (if it does, STOP and report; do not paste it anywhere). `aws secretsmanager describe-secret --secret-id schwab/alongside/ec2-credentials` must now show an `AWSCURRENT` version (METADATA ONLY: you never read the value). If `bootstrap.ps1` fails at its own line for a reason other than the CLI, stop and report the first failing line; do not edit it.
10. ONE reboot so the auto-logon Administrator console session exists: `aws ec2 reboot-instances --instance-ids <id>` (a reboot, never a stop or terminate; the box holds no session yet). Wait for `PingStatus Online` again (up to 15 minutes), then run `quser` over SSM: it must list an `administrator` session on `console` in state `Active`. If it does not after one more reboot-free wait of 5 minutes, report the `quser` and `Winlogon` AutoAdminLogon flag (`Get-ItemProperty` of the key, printing `AutoAdminLogon` and `DefaultUserName` ONLY, never `DefaultPassword`) and stop; do not improvise a fix.
11. Prove the RDP path needs no ingress: run `aws ssm start-session --target <id> --document-name AWS-StartPortForwardingSession --parameters "portNumber=3389,localPortNumber=13389"` in the background, test a TCP connect to `127.0.0.1:13389` (it must connect), then end the session. Record pass or fail. (The session-manager plugin 1.2.835.0 is installed on this laptop.)
12. Close the ledger entry (`deploy_ledger.py close ...`), commit it with the before/after files, remove the pinned worktree if clean, and report to `2.0.0_SA_COO~SA`: **BOX READY FOR RDP** only if steps 5-11 all passed, with the instance id, the apply summary line, the `quser` line, the port-forward result and the ledger path; otherwise the first step that failed and its output.

### ACCEPTANCE (read by the issuer from your committed files, not run by you)

<criterion id="AL1-r1-AC1" cell_refs="AL-r-1"><invocation>python .tools/proof-of-spec-check.py org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r1.alongside-box-build-and-bootstrap.proof_of_spec.json AL1-r1-AC1</invocation><expect>VALID</expect></criterion>
`AL1-r1-AC1` -- the proof instance records the apply summary line, the six after-reads of step 6, the uploaded sizes, the bootstrap verdict lines, the `quser` line and the port-forward result as artifact rows.

<expected_criteria>AL1-r1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder, the ledger folders named in step 2, and this order's file. You may run `terraform init/plan/apply` ONLY in the Alongside root and ONLY through the steps above.
- **Never:** `get-secret-value` on either Alongside secret; enabling a rule; any command against the 49F box, its role, its schedule or its secrets; running the SI2 app, any puller or any Schwab call; deleting or stopping anything; a bare `terraform apply`; `terraform destroy`; editing any `.tf` file (a defect is a Branch B report, the issuer re-cuts).
- **Refusal clause.** If a step cannot be met as written, stop, write the reason and the output in your report and a surprise row (id `NFRA_SCHWABBF-R1-S<k>`, `surfaced_at` = `date -u +%FT%TZ`), and do not improvise.

<paths>
org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, round 1), cell `AL-r-1`.
<owned_cells>AL-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AL1-r1-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r1.alongside-box-build-and-bootstrap.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL1-r1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message and a message to `2.0.0_SA_COO~SA`):** BOX READY FOR RDP or the first failed step; the instance id; the apply summary line; the `quser` line; the port-forward result; the commit hash; any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the four rules ship DISABLED and are not enabled by this order; their fire times were checked against the six 49F fires in the AL-s-1 test.
comp-iam: DECLARED-NOT-APPLICABLE as a tool run -- the role is new; its statements were read at the cut and are in the read-only plan; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition findings 2 (no fire before the sign-in) and 5 (the pull runs as an Administrator scheduled task) are carried by DISABLED rules and the cell AL-s-1 command.
lane: the <paths> block IS the grant; CloudOps seats apply (rule 34).
</preflight>

Source: PRD v0.9 C-ALONGSIDE; decomposition `NFRA_SCHWABBF_DECOMP_AL1.md` cell AL-r-1 and release acts A1-A3; the COO and CTO never-widen halves.
