# TO IRPT_ANLREQ.TO-AR-y-486.resident-ticket-read-managed-policy-attribute-restricted-terraform-source -- WRITE AND PROVE OFFLINE THE TERRAFORM SOURCE of ONE customer-managed policy on the resident runner role: dynamodb:GetItem only, on table opal-tickets only, attribute-restricted to ticket_id, ticket_type, answers, created_at; nothing is planned, applied or run

<to_id>IRPT_ANLREQ.TO-AR-y-486.resident-ticket-read-managed-policy-attribute-restricted-terraform-source</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~360</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ145</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-486` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-AUDIT-RECORD (PRD v0.28) | **depends_on:** CTO ruling A, msg 11858 (attribute-restricted GetItem on opal-tickets, own pair; the code ships in a later release, not r34q)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~360`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-360` (branch `wk-IRPT_ANLREQ-360`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~360 <0.9.0_WK_IRPT_ANLREQ~360@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W360-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy, no release build.** Terraform is not installed on this box: do not try to run it. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first; `controls` holds `mutant` and `determinism` only), with `to_id` exactly the order's id; run `python .tools/proof-of-spec-check.py <instance> "AR486-y-AC1,AR486-y-AC2"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID. The instance's check-script reference is pinned to a commit that EXISTS (commit the script first, then pin it).

### THE CELL (`AR-y-486`, inlined)

*Why.* The resident's packager (AR-y-469 `ycharts/generate/ticket_audit_source.py`) reads the filed ticket (answers and created_at) to write the analysis-audit record. The role `irpt-ycharts-runner-role` is implicitly denied `dynamodb:GetItem` on `opal-tickets` (CTO measured it), and the ticket API gives the packager no read (issuer measured it). The CTO ruled (msg 11858): ONE customer-managed policy on that role only, `dynamodb:GetItem` only, on `table/opal-tickets` only, no index, restricted so a read may only return `ticket_id`, `ticket_type`, `answers` and `created_at` (never `requester`, `created_by`, `events` or anything else). The set is exactly those four attributes; `filer_user_type` is NOT in it (the code drops that read in a sister cell).

*The change.* ONE new file `infra/aws/terraform/investor-reporting/ycharts/resident_ticket_read_policy.tf` (read `infra/aws/terraform/investor-reporting/ycharts/resident_audit_policy.tf` first and copy its style: a `module "..._name"` from `../../modules/opal_name` with `system` irpt, `function` `ticket-audit-read`, `kind` policy and no `scope`; one `aws_iam_policy`; one `aws_iam_role_policy_attachment` to `aws_iam_role.runner.name`). The policy document, version `2012-10-17`, has exactly ONE statement:
- `Sid` `ReadTheFiledTicketForTheAuditOnly`, `Effect` `Allow`, `Action` exactly `["dynamodb:GetItem"]`, `Resource` exactly one ARN: `arn:aws:dynamodb:${var.aws_region}:${data.aws_caller_identity.current.account_id}:table/${local.resident_audit_tickets_table}` (no `/index/` suffix), where a `locals` block in THIS file declares `resident_audit_tickets_table = "opal-tickets"` with a comment that it is the existing table declared in `infra/aws/terraform/ticket-center/main.tf` (an existing resource; the name is not minted here).
- `Condition`, exactly three operators: `"Null" = { "dynamodb:Attributes" = "false" }` (the key must be PRESENT, so a GetItem with no projection, whose request carries no attributes key, is denied: `ForAllValues` alone passes on a missing key); `"ForAllValues:StringEquals" = { "dynamodb:Attributes" = ["ticket_id", "ticket_type", "answers", "created_at"] }` (every attribute named in the request must be one of the four); `"StringEqualsIfExists" = { "dynamodb:Select" = "SPECIFIC_ATTRIBUTES" }`.
Put a comment block at the top of the file stating why (the two measurements above), why `Null` is there (the ForAllValues trap), that the policy is a customer-managed policy (not the inline policy, which is at 10131 of 10240 bytes), and that the code that sends the projection ships in a later release. No other file changes (no edit of `resident.tf`; it is not in `<paths>`). If `data.aws_caller_identity.current` and `var.aws_region` are not declared in this stack, use what `resident.tf` uses for its own DynamoDB ARNs (it builds them at its lines 84-85 and 169); do not declare new variables.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~360/`: `check_ticket_read_policy.py` (stdlib only, ruff clean, offline). It reads the new file as TEXT and prints `TICKET-READ-POLICY-OK actions=1 resources=1 attrs=4 null_guard=yes select=yes attachment_runner_only=yes` only if: the `Action` list holds exactly `dynamodb:GetItem` and nothing else; exactly one `table/` ARN built from `local.resident_audit_tickets_table`, with no `index`, no `*`, no `Query`, `Scan`, `BatchGetItem`, `PutItem`, `UpdateItem` or `DeleteItem` anywhere in the file outside comments; the Attributes list equals the four names exactly (a fifth, `requester`, `created_by`, `events`, `filer_user_type` or `*` anywhere in the list is BAD); the `Null` guard with `false` is present on `dynamodb:Attributes`; `dynamodb:Select` is `SPECIFIC_ATTRIBUTES`; exactly one `aws_iam_role_policy_attachment` and it names `aws_iam_role.runner.name`; the local equals `opal-tickets`; no non-ASCII character. Else `TICKET-READ-POLICY-BAD <why>` (rc 1). `--selftest` mutates the text in memory five ways (add `dynamodb:Query` to the actions; add `requester` to the attributes; delete the `Null` condition; change the resource to end `/index/*`; change the local to `opal-users-v2`) and prints `CONTROL-FIRES` only when ALL FIVE read BAD. Commit order: the `.tf` as ONE commit first, message citing AR-y-486; then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR486-y-AC1" cell_refs="AR-y-486"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~360/check_ticket_read_policy.py</invocation><expect>^TICKET-READ-POLICY-OK actions=1 resources=1 attrs=4 null_guard=yes select=yes attachment_runner_only=yes$</expect></criterion>
<criterion id="AR486-y-AC2" cell_refs="AR-y-486"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~360/check_ticket_read_policy.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~360/IRPT_ANLREQ.TO-AR-y-486.resident-ticket-read-managed-policy-attribute-restricted-terraform-source.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-486.resident-ticket-read-managed-policy-attribute-restricted-terraform-source`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR486-y-AC1,AR486-y-AC2"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-486</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write. `test_audit_live_wiring.py` leaks `sys.path` at module level (row W350-S1): where it is in a pytest line it is listed last-but-one as written; report any other order problem as a row and do not fix files outside the grant.

<paths>
infra/aws/terraform/investor-reporting/ycharts/resident_ticket_read_policy.tf
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~360/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-486.resident-ticket-read-managed-policy-attribute-restricted-terraform-source.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one new Terraform file; nothing is planned, applied or run against AWS; IB2 applies it under its own never-widen pair after the CTO signs.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker (the simulations are the applier's, before apply).
comp-adversary: RUN -- by reading the CTO's ruling, the audit policy file and the ticket Lambda's attribute names against this cell; the lens: a policy that also allows Query or Scan or an index, a missing Null guard (GetItem with no projection passes ForAllValues), an attribute list wider than the four, a typed table ARN with a wrong table, a second attachment to another principal, a control that cannot fire. NOT seen (blind): how the IAM simulator populates dynamodb:Attributes for GetItem (the applier's simulations decide); denominator: two criteria.
</preflight>
