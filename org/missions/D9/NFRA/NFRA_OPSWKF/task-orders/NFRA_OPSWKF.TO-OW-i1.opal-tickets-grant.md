# TO NFRA_OPSWKF.TO-OW-i1 -- the trade Lambdas' role may read and update a ticket

<to_id>NFRA_OPSWKF.TO-OW-i1</to_id>
<project>NFRA_OPSWKF</project>
<issued_to>0.9.0_WK_NFRA_OPSWKF~4</issued_to>
<issued_by>2.0.0_SA_COO~O2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (path floor: Terraform, an IAM grant; you apply nothing) | **Decomp cell:** `OW-i-1` |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_NFRA_OPSWKF~4`. Your worktree is `C:/tmp/opswkf-r1-4` (branch `wk-NFRA_OPSWKF-4`, cut from box/dell2 at the
issuance commit). Work and commit ONLY there with `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_OPSWKF~4
<0.9.0_WK_NFRA_OPSWKF~4@opal.agent>" -F <msgfile> -- <paths>`; write the message file with the Write tool.

### THE CELL

`OW-i-1`. Two Terraform edits, both in `infra/aws/terraform/trade-pipeline/`:

1. **`iam.tf`.** In the policy attached to `aws_iam_role.trade_submission` (the role `trade-submission-handler` and
   `trade-workflow-handler` run as; see `lambdas.tf:191-193` and the comment at `iam.tf:14`), add ONE new statement:
   - `Sid = "TicketBridgeOpalTickets"`;
   - `Effect = "Allow"`;
   - `Action = ["dynamodb:GetItem", "dynamodb:UpdateItem"]`;
   - `Resource = "arn:aws:dynamodb:us-east-1:${local.account_id}:table/opal-tickets"`.

   Keep the statement compact: the Action list sits directly above the Resource line. Add no other action, no index ARN and no
   wildcard. Leave every existing statement unchanged.
2. **`lambdas.tf`.** Add `TICKETS_TABLE = "opal-tickets"` to the `environment.variables` of exactly two functions:
   `trade_submission_handler` and the workflow handler function (find it by `function_name = "trade-workflow-handler"`).

`opal-tickets` is an existing table (the ticket-center stack). This is a grant on an existing name, not a new resource, so no
naming builder applies. Run `terraform fmt` on the folder if `terraform` is on PATH. Never run `plan`, `init` or `apply`.

### ACCEPTANCE

<criterion id="OW-i1-AC1" cell_refs="OW-i-1"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/R1_CHECKS/ow_checks.py i1-grant</invocation><expect>OW-I1-GRANT-OK</expect></criterion>
`OW-i1-AC1`: the grant carries exactly GetItem + UpdateItem on table/opal-tickets, and TICKETS_TABLE is on both functions.

<expected_criteria>OW-i1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block, your deliverables folder `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~4/`,
  and this order's file (status flip only).
- Never call AWS. No `terraform init`/`plan`/`apply`. The applier applies, under an apply order the issuer cuts later.
- No non-ASCII. Rows go in as `NFRA_OPSWKF-D2-W4-S<k>`, appended in BINARY mode.

<paths>
infra/aws/terraform/trade-pipeline/iam.tf
infra/aws/terraform/trade-pipeline/lambdas.tf
org/missions/D9/NFRA/NFRA_OPSWKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPSWKF/decompositions/NFRA_OPSWKF_DECOMP.md</decomp_doc> (round 1), cell `OW-i-1`.
<owned_cells>OW-i-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: OW-i1-AC1. The instance is at
`org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~4/NFRA_OPSWKF.TO-OW-i1.opal-tickets-grant.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> OW-i1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (once):** the check line verbatim, the commits, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, hold or gate is created or consumed by this cell
comp-iam: RUN at the drain on the diff, and the applier's simulate read rides OW-d-1. The role trade-submission-lambda-role is SHARED by six functions (iam.tf:14), so the grant reaches all six; accepted because it is two read/update actions on one table, no delete, put or scan
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the comp-iam read of the diff is the adversarial arm for a grant
lane: infra/aws/terraform/trade-pipeline/** ; nothing applied by the worker.
</preflight>
