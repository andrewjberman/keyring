# TO IRPT_DASHBD.TO-DB-c-18 -- the Cottonwood `account_dim` TERRAFORM ROOT: the function, its `*-cot-*` execution role (two silver reads, one gold prefix, nothing else) and a daily schedule created DISABLED; a new root `account-dim`; files only: nothing is planned or applied

<to_id>IRPT_DASHBD.TO-DB-c-18</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~411</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>123</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's decision C (msg 8167: its own package, a `*-cot-*` role and builder names; reads only the Black Diamond silver inputs; writes only its own `account_dim` gold prefix; scheduled in America/New_York after its input lands; trading-day frontier) and the merged code of `DB-c-16` | **Rows:** IRPT_DASHBD-D2-W411-S<k> | **Decomp cell:** `DB-c-18` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 10) | **outcome_ref:** FWD-2, FWD-11, FWD-15 | **depends_on:** none (`DB-c-16` is merged; the package entry is a parallel cell and the artifact key below is derived from the builder name, not from it).

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-411`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~411/`. Never push. No client data is read or written. No AWS call is needed or allowed. **Never run `terraform plan` or `terraform apply`**; you run only `init -backend=false`, `fmt` and `validate`.

**Amendments after your first run (issuer, CTO msg 8187 and the naming gate):** (i) the root directory and the state key carry NO firm token (the naming gate refuses a new `cot` literal): the directory is `infra/aws/terraform/investor-reporting/account-dim/` and the key `investor-reporting/account-dim/tfstate`; the files you wrote under `account-dim-cot/` are MOVED there (plain `mv`, they are uncommitted). (ii) Every Terraform block LABEL you write is token-free too (`module "irpt_account_dim"`, and likewise for the others). (iii) EVERY `opal_name` module block carries `scope = <the derived firm>` (the scheduler role, scheduler policy and schedule names included), so the printed names are `irpt-cot-account-dim-scheduler-role`, `irpt-cot-account-dim-scheduler-policy` and `irpt-cot-account-dim-daily`; the checker now refuses an `opal_name` block without `scope`. (iv) `.tools/terraform.exe` is a gitignored binary that exists only in the base checkout: run it by the absolute path `C:/dev/ajb_workspace/.tools/terraform.exe -chdir=<your worktree>/infra/aws/terraform/investor-reporting/account-dim <verb>`; the checker finds it the same way. Do not copy it.

**Why.** The Cottonwood holdings-performance function was added to the root `infra/aws/terraform/investor-reporting/holdings-performance/` by an earlier cell (`DB-c-7`). Read ITS Cottonwood blocks first, because you mirror them for a second function: in `locals.tf` the `irpt_hp_cot_*` locals (and the header comment on why every bucket and prefix is READ from `data/assets/scripts/gold/irpt_holdings_performance/sources.json` and the registry, never typed), in `lambda.tf` the `irpt_holdings_performance_cot` blocks and the `irpt_performance_native` layer data source, in `iam.tf` the Cottonwood role and policy, in `schedule.tf` the Cottonwood scheduler role, policy and schedule, and `main.tf` for the provider and backend. The new function writes one new gold table and needs its own root so a plan shows only its resources.

**The cell (`DB-c-18`).** Create the NEW directory `infra/aws/terraform/investor-reporting/account-dim/` with exactly these five files (copy the style, headers and idioms of the Cottonwood blocks above; ASCII only; no alarm, no SNS topic, no SES send, no notification):
1. `main.tf`: the same `terraform {}` block and provider as the holdings root, with the backend key `investor-reporting/account-dim/tfstate` (same bucket and region), the same `default_tags`, `data "aws_caller_identity" "current" {}`, and a header comment saying what the root holds and that every apply is `.tools/safe-apply.sh` under a change-management ledger entry.
2. `locals.tf`: read the declaration `data/assets/scripts/gold/irpt_holdings_performance/sources.json` (path relative to `path.module`, as the holdings root does) and select its ONE source whose custodian matches the Black Diamond source the Cottonwood holdings blocks use (reuse exactly how the `irpt_hp_cot_*` locals select it); derive the firm from the registry the same way; derive the silver bucket and the TWO silver prefixes (the declared `positions_prefix` with its `{monolith}` and `{scope}` filled as the existing locals fill it, for the table `fact_holdings` as declared and the same prefix with that last segment replaced by `fact_allocations`); derive the gold bucket from the registry scope row; the gold table name is the literal `account_dim`, cited in a comment as the constant `TABLE` in `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py`; the gold write prefix is `irpt/<firm>/gold/account_dim/`. No firm token, bucket name or silver prefix is typed.
3. `lambda.tf`: the `irpt_performance_native` layer data source as the holdings root has it; `opal_name` builder modules (`source = "../../modules/opal_name"`) for the function name (`system = "irpt"`, `scope` = the derived firm, `function = "account-dim"`, `kind = "lambda"`; it must print `irpt-cot-account-dim-lambda`); the function through the same module the holdings Cottonwood function uses (`../../modules/yang-lambda`) as `module "irpt_account_dim"`, with `artifact_key = "investor-reporting/${<the name module>.name}.zip"`, `handler = "lambda_function.lambda_handler"`, `runtime = "python3.12"`, `timeout = 300`, `memory_size = 1536`, the same layer, `log_retention_days = 14`, `system_tag = "InvestorReporting"`, tags `Cell = "DB-c-18"` and `Project = "IRPT_DASHBD"`; and outputs for the function name and ARN.
4. `iam.tf`: the execution role named by the builder (`function = "account-dim"`, `kind = "role"`; it must print `irpt-cot-account-dim-role`), its Lambda trust policy as the holdings Cottonwood role has it, and ONE inline policy whose statements are exactly: `s3:GetObject` on the two silver prefixes' objects; `s3:ListBucket` on the silver bucket conditioned (`s3:prefix`) on the two silver prefixes; `s3:ListBucket` on the gold bucket conditioned on the `account_dim` gold prefix; `s3:PutObject` on the `account_dim` gold prefix's objects; and the CloudWatch Logs statement the holdings Cottonwood role carries (copy its actions and resources form). NO other action (no delete, no `s3:*`, no `PutObjectAcl`, no KMS, no Secrets Manager, no other bucket, no wildcard resource). The gold bucket denies foreign-firm principals except roles named `*-cot-*`: the builder's role name matches, so no bucket-policy change is made or needed here.
5. `schedule.tf`: the scheduler role (trust `scheduler.amazonaws.com`, as the holdings Cottonwood scheduler role has it) and its policy, each named by the builder with `qualifier = "scheduler"` (and `kind = "policy"` for the policy), granting ONLY `lambda:InvokeFunction` on this function; the schedule named by the builder (`function = "account-dim"`, `kind = "daily"`), `group_name = "default"`, **`state = "DISABLED"`**, `schedule_expression = "cron(45 8 ? * MON-FRI *)"`, `schedule_expression_timezone = "America/New_York"`, `flexible_time_window { mode = "OFF" }` and a target that invokes the function with the input `jsonencode({ kind = "irpt_account_dim_daily", note = "scheduled fire; lambda_function.py resolves the target trading day itself" })`; outputs for the schedule name and state. Header comment: created DISABLED, enabled only by a later one-line change after the catch-up's after-read; the 08:45 fire is after the Black Diamond silver lands (about 11:46 UTC, 07:46 or 06:46 New York time) and after the 08:15 holdings fire.
6. Then run, from the repo root: `the terraform binary of amendment (iv) with `-chdir=infra/aws/terraform/investor-reporting/account-dim` and the verb `init` -backend=false -input=false`, then `fmt` (apply it so `fmt -check` is clean) and `validate`. Report each result. Commit only the five `.tf` files (not `.terraform/`, not a plan or state file; if `.terraform.lock.hcl` is produced, commit it only if the holdings root's lock file is tracked in git, else leave it uncommitted).
7. **Do NOT**: plan or apply; edit any other Terraform file, the source map, the Lambda, the adapter, the registry or any existing file; create any resource other than the function, its role and policy, the scheduler role and policy and the one schedule; give any statement a resource or action beyond item 4 and the scheduler policy.

<criterion id="DBC123-2-AC1" cell_refs="DB-c-18"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r123/p123_bcw.py" . DBC123-2-AC1</invocation><expect>DBC123-2-AC1 PASS</expect></criterion>
`DBC123-2-AC1` -- the five files exist; the state key, builder-module names, handler, runtime and artifact key are as above; no typed `irpt-` name; the schedule is DISABLED in America/New_York on trading weekdays; every IAM action is in the closed set; no wildcard resource; no foreign-firm token; and two planted mutations (a delete action added; DISABLED changed to ENABLED) are each refused by the same structure check. Base: FAIL.

<criterion id="DBC123-2-AC2" cell_refs="DB-c-18"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r123/p123_bcw.py" . DBC123-2-AC2</invocation><expect>DBC123-2-AC2 PASS</expect></criterion>
`DBC123-2-AC2` -- `terraform fmt -check -recursive` and `terraform validate` pass in the new root. Base: FAIL (no root).

<expected_criteria>DBC123-2-AC1, DBC123-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files and `git show`. Writes: the files in `<paths>`, your folder and scratch in your private folder (the ignored `.terraform/` directory `init` creates inside the new root is allowed). No AWS call, no plan, no apply, no upload, no invoke, no deploy, no push, no vendor call, no secret read. `init -backend=false` may download the AWS provider; that is allowed.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A builder REFUSAL for a name is a missing registry row: a BLOCKING row and a report, never a typed name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W411-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~411/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-18.cottonwood-account-dim-terraform-root-function-role-and-disabled-schedule.md
infra/aws/terraform/investor-reporting/account-dim/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 10, cell `DB-c-18`.
<owned_cells>DB-c-18</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC123-2-AC1, DBC123-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~411/IRPT_DASHBD.TO-DB-c-18.cottonwood-account-dim-terraform-root-function-role-and-disabled-schedule.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC123-2-AC1,DBC123-2-AC2` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the two criteria's last lines; the names the builder printed for the function, the role, the scheduler role, the policies and the schedule; the `init`, `fmt` and `validate` results; the five files; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: files only; nothing is planned or applied. The later act's blast (a new function, role, scheduler role and a DISABLED schedule, then one partition) is bounded in the CTO pair packet.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call; the new role's grants are written as files and graded by DBC123-2-AC1's closed action set, the apply being the packet's.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no live schedule is read or changed; the new schedule is created DISABLED by a later apply.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC123-2-AC1 plants two mutations itself.
</preflight>
