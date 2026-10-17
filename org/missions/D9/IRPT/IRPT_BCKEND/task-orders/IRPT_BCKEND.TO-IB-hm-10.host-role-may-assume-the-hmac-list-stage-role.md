# TO IRPT_BCKEND.TO-IB-hm-10 -- DECLARE in Terraform (no apply) the ONE `sts:AssumeRole` statement the shared daily-runner host role's identity policy needs for the HMAC list stage role (CTO ruling msg 10234: "the host profile gains only `sts:AssumeRole` on that one role"; the finding of IB-hm-8 step 6)

<to_id>IRPT_BCKEND.TO-IB-hm-10</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~455</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-hm-10` (decomposition section 247) | **outcome_ref:** FWD-21 | **Ordered by:** the CTO's ruling msg 10234 (B: the stage assumes a narrow role; the host profile gains only `sts:AssumeRole` on that one role) and the finding of worker ~454 (`deliverables/0.9.0_WK_IRPT_BCKEND~454/IBhm8_notes.md`, step 6: the host role's identity policy in `infra/aws/terraform/mdpf-pipeline/iam.tf` holds an `sts:AssumeRole` statement for the 49 Financial source principal and none for the stage role). **This order DECLARES; it never applies.** The apply is a leg of the HMAC list apply order under a signed never-widen pair.

---

## WORKER FACE

**Cell `IB-hm-10` (inlined).** The host role `mdpf_runner`'s inline policy in `infra/aws/terraform/mdpf-pipeline/iam.tf` has this statement for the 49F source principal (about lines 659 to 664):

```
      {
        Sid      = "IrptDirectory49fAssumeSourcePrincipal"
        Effect   = "Allow"
        Action   = "sts:AssumeRole"
        Resource = "arn:aws:iam::${local.account_id}:role/${module.irpt_49f_directory_read_role_name.name}"
      },
```

and, near line 984, the module that gives the role's name as builder output (`module "irpt_49f_directory_read_role_name"`, a name only; it creates nothing). **Mirror both, ADDITIVELY, and change nothing else in the file:**
1. **A name module** `module "irpt_hmac_list_stage_role_name"` with `source = "../modules/opal_name"`, `system = "irpt"`, `function = "hmac-list-stage"`, `kind = "role"` and NO scope (the same inputs as the module of the same purpose in `infra/aws/terraform/investor-reporting/directory/hmac_list_stage.tf`, which names the role `irpt-hmac-list-stage-role`). Put it beside the 49F module, with a short comment that cites cell IB-hm-10 and says it is a name only.
2. **One statement** added to the SAME policy statement list, directly after the 49F AssumeRole statement and before the next statement: `Sid = "IrptHmacListStageAssumeRole"`, `Effect = "Allow"`, `Action = "sts:AssumeRole"`, `Resource = "arn:aws:iam::${local.account_id}:role/${module.irpt_hmac_list_stage_role_name.name}"`, with a comment that says what it is for and that it is applied only under the never-widen sign-off of the HMAC list producer.

The change is ADDITIONS ONLY: no existing line is edited, moved or deleted. No `"*"` anywhere in what you add, no `Principal`.

**Do, in this order:**
1. Read `iam.tf` lines 600 to 700 and 970 to 1000, and `infra/aws/terraform/investor-reporting/directory/hmac_list_stage.tf` (the module blocks at its top).
2. Make the two additions. If `.tools/terraform.exe` exists and runs offline, run `terraform fmt -check -diff` on `iam.tf` and record the result; do not run `init`, `plan` or `apply` (no AWS call of any kind).
3. Run the three criteria below from the repository root, each under `timeout 300` (AC3 reads `HEAD~1..HEAD`: run it AFTER your one commit). Record AC1 and AC2 output verbatim in `deliverables/0.9.0_WK_IRPT_BCKEND~455/IBhm10_criteria_output.txt` BEFORE the commit; write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`; write `IBhm10_notes.md` (the change in a paragraph, the fmt result, anything odd).
4. **ONE commit** with explicit paths (`.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~455 <0.9.0_WK_IRPT_BCKEND~455@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool): `iam.tf`, your deliverables folder and any surprise row. If safe-commit is slow it is waiting on other seats: wait, never run it twice at once, never amend. Do not push. Report once, under 150 words.

**Criteria (run each under `timeout 300` from the repository root):**

<criterion id="IBHM10-AC1" cell_refs="IB-hm-10"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r253/p253_cells.py" . IBHM10-AC1</invocation><expect>IBHM10-AC1 PASS</expect></criterion>
<criterion id="IBHM10-AC2" cell_refs="IB-hm-10"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r253/p253_cells.py" . IBHM10-AC2</invocation><expect>IBHM10-AC2 PASS</expect></criterion>
<criterion id="IBHM10-AC3" cell_refs="IB-hm-10"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r253/p253_cells.py" . IBHM10-AC3</invocation><expect>IBHM10-AC3 PASS</expect></criterion>

<expected_criteria>IBHM10-AC1, IBHM10-AC2, IBHM10-AC3</expected_criteria>

What the checks grade: AC1 the `iam.tf` diff of your commit deletes nothing and adds exactly one name-module block, one statement (Sid, `sts:AssumeRole` once, Resource built from the module's name), no wildcard and no Principal; AC2 the module's inputs are exactly the builder inputs and `lib/opal_naming.py name()` returns `irpt-hmac-list-stage-role`; AC3 your ONE commit touches only `iam.tf` and this order's paths. The plan and the apply are another order's. Do not edit the checks.

## BOUNDS

- **Grant:** edit `infra/aws/terraform/mdpf-pipeline/iam.tf` (additions only); write `deliverables/0.9.0_WK_IRPT_BCKEND~455/`; the surprise channel for rows. **NO terraform init, plan or apply; NO AWS call; NO change to any existing line, resource or statement; NO other file; NO push.**
- **Refusal clause:** STOP and report, writing nothing further, if the statement list cannot take a new element without editing an existing line, or if the `opal_name` module refuses the inputs. File a surprise ROW for anything odd and keep working; a broker message is never the carrier.

<paths>
infra/aws/terraform/mdpf-pipeline/iam.tf
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~455/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-hm-10.host-role-may-assume-the-hmac-list-stage-role.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 247 (round 11, workstream ~PM), cell `IB-hm-10`.
<owned_cells>IB-hm-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBHM10-AC1, IBHM10-AC2, IBHM10-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~455/IRPT_BCKEND.TO-IB-hm-10.host-role-may-assume-the-hmac-list-stage-role.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- DECLARES one name module and one statement in the shared host role's inline policy; NOTHING is applied by this order. The apply is a later leg under the HMAC list never-widen pair: it changes 1 resource (the `mdpf_runner` inline policy) in the `mdpf-pipeline` root, which other projects also apply, so the pair counts the writers of that root and requires its ledger rule (no other apply on the root while the leg is open).
comp-iam: RUN -- the host role gains `sts:AssumeRole` on ONE role ARN (the stage role, built from the builder name); the stage role's own trust already names the host role only (IB-hm-8). Whether the statement is strictly required in the same account (a trust policy naming the role ARN suffices unless a permission boundary or an SCP intervenes) is NOT measured by me; the statement follows the 49F precedent in the same policy and the CTO's ruling.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p253_cells.py IBHM10 dry-run at base on dell2 2026-10-17 ~05:4xZ: AC1, AC2, AC3 FAIL. Positive control (control253.py) over synthetic git repos each with a base commit and ONE worker commit: the three positives PASS and each of 12 negatives (no name module, no statement, a wildcard resource, a resource not built from the module, a Principal, two statements, an existing line rewritten, a scope on the module, a wrong function, a builder returning another name, iam.tf not in the commit, another file touched) plus the empty repo fails its own arm, 0 unexpected. NOT measured by me: Terraform syntax validity beyond the worker's fmt run, the plan, anything live.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~455`. Class WORLD (the gate's floor for an infra path; this order declares and applies nothing).
</preflight>
