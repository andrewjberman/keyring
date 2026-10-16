# TO TCKT_VNEXT.TO-R19-TR -- WRITE the Terraform SOURCE for the two new Lambda environment values (source only; nothing is planned or applied)

<to_id>TCKT_VNEXT.TO-R19-TR</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~48</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD (an infrastructure path; the worker plans, applies and invokes NOTHING)
**Decomp cell:** `R19-ev-4` (`decompositions/TCKT_VNEXT_DECOMP_R19.md`) | **outcome_ref:** row `IRPT_ANLREQ-D2-S134` items 1 and 2 | **depends_on:** the contract (names fixed in the decomposition's CONTRACT, items 1, 2 and 5)

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~48`.
- **Worktree:** `C:/dev/wk-tckt-vnext-48` (branch `wk-TCKT_VNEXT-48`), provisioned by the issuer. Work and commit only there, with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~48 <0.9.0_WK_TCKT_VNEXT~48@opal.agent>" -F <msgfile> -- <paths>`. If a `portal`
  folder exists in the worktree it is a separate repository: never touch or stage it.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `TCKT_VNEXT-D2-W48-S<k>` (take the next free `<k>`). Every `.py` you add passes `bash .tools/commit-gate.sh <file>` before its commit
  (Python 3.9 syntax). No non-ASCII in what you add. The proof instance: a judgment row needs `method`, `invocation` and `denominator`; every
  non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. NO live call: no AWS, no network, no `terraform plan`
  or `apply`; `terraform fmt -check` on the one file is allowed if the binary is installed. Scratch outside the product tree.

### THE CELL (`R19-ev-4`, inlined) -- SOURCE ONLY.

*Row S134, ruling ADDENDUM 7: the ticket Lambda's behaviour is now configured by two environment values. Both ship as CONFIG in `infra/aws/terraform/ticket-center/main.tf`; the Lambda code is `TO-R19-L1` and `TO-R19-L2`'s.*

In `infra/aws/terraform/ticket-center/main.tf`, inside the ticket Lambda's `environment_variables = { ... }` block (read first: the block starting about line 336, and how `COMMENTARY_ALLOWED_FIRMS` at about line 353 and `PACKAGE_ALLOWED_FIRMS` at about line 361 are written with their comment lines):

1. Add exactly `CLIENT_NOTICE_CONTACT_MAP = "{}"` (a string holding the empty JSON object) with a comment in the neighbours' style: the firm-keyed map of client-notice contacts, empty on purpose (REFUSE-IF-UNSET: with no contact the notice is not sent, `WE_CLIENT_NO_CONTACT`), the membership is an open input owned by `1.0.0_SA_CTO~DELL2`, and a row is added here, touching no code. Write the value as an HCL string that decodes to `{}` (use the same string style the file uses for `TICKET_DL_MAP`; read it first).
2. Add exactly `ANALYST_INTAKE_ALLOWED_FIRMS = "49financial,inflection,cottonwood"` with a comment: the firms the `svc-analyst-intake` principal may list tickets for (row S134 item 2), never `ALL` (the handler drops it), unset or empty is no firm.
3. **Nothing else in the file changes**: no other variable, resource, permission, route or routing entry. `terraform fmt -check` passes on the file if the binary is installed (say which in your record).
4. **Write `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~48/tf_shape_check_r19.py`** (AC1) and `mutant_check_r19.py` (AC2), and a short `R19_TR_RECORD.json` (the lines you added, the base sha, whether `terraform fmt` ran, `not_read`).

### ACCEPTANCE

<criterion id="R19TR-AC1" cell_refs="R19-ev-4"><invocation>python C:/dev/wk-tckt-vnext-48/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~48/tf_shape_check_r19.py</invocation><expect>^TF-SHAPE-OK </expect></criterion>
`R19TR-AC1`: you write `tf_shape_check_r19.py`: it reads `infra/aws/terraform/ticket-center/main.tf` (the path is an argument with this file as the default) and prints `TF-SHAPE-OK CLIENT_NOTICE_CONTACT_MAP={} ANALYST_INTAKE_ALLOWED_FIRMS=49financial,inflection,cottonwood` only when (a) the Lambda's `environment_variables` block holds `CLIENT_NOTICE_CONTACT_MAP` whose decoded value is the empty JSON object and `ANALYST_INTAKE_ALLOWED_FIRMS` exactly `49financial,inflection,cottonwood`, each once; (b) the set of every OTHER key of that block, and its value text, is byte-identical to the same block of the file at the commit this worktree was cut from (the parent of your first commit on the branch, read with `git show <sha>:infra/aws/terraform/ticket-center/main.tf`; record the sha); (c) the file outside that block is byte-identical to the same file at that commit; otherwise `TF-SHAPE-BAD <why>`, exit 1.

<criterion id="R19TR-AC2" cell_refs="R19-ev-4"><invocation>python C:/dev/wk-tckt-vnext-48/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~48/mutant_check_r19.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`R19TR-AC2` (the one mutant that fails): you write `mutant_check_r19.py`: it copies `main.tf` to a scratch folder OUTSIDE the product tree with `ALL` added to the `ANALYST_INTAKE_ALLOWED_FIRMS` value, runs the shape checker on the copy, and prints `MUTANT-FIRES` only when the checker prints `TF-SHAPE-BAD` (else `MUTANT-SURVIVES`, exit 1).

<criterion id="R19TR-AC3J" cell_refs="R19-ev-4" judgment="true"/>
`R19TR-AC3J` (judgment, graded at L9, never by you): exactly the two environment values were added, the contact map ships empty (no address was invented), the intake list is the three served firms and no wildcard, and nothing was planned or applied.

<expected_criteria>R19TR-AC1 R19TR-AC2 R19TR-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~48/` and this order's file
  (status flip only). If anything OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it.
- READ only: everything else, including the Lambda source.

<paths>
infra/aws/terraform/ticket-center/main.tf
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R19.md</decomp_doc>
<owned_cells>R19-ev-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~48/TCKT_VNEXT.TO-R19-TR.ticket-lambda-environment-for-the-notice-contacts-and-intake-firms.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R19-TR`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R19TR-AC1,R19TR-AC2,R19TR-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- Terraform SOURCE in a worker worktree; the apply is the applier's (`TO-R19-REL`) under `safe-apply` and a change-management entry.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this cell.
comp-adversary: RUN -- by reading row S134, ruling ADDENDUM 7 and the contract (items 1, 2, 5) against this cell; the lens: a wildcard in the intake list, an invented contact address, a variable that rides along, a string value that does not decode to the empty object. BLIND to: the live function environment and the live contact list (denominator: 1 ruling and 3 contract items read).
</preflight>

---

## RECORD FACE

- Cut on the CTO's ADDENDUM 7 (msg 8833) in round 19; fan-out 4 of 5 chains, cap 4 (dell2 CPU budget). `main.tf` has one spot changed by this round; the R18 cells' edits are already merged. Base: `R19TR-AC1` and `R19TR-AC2` FAIL as expected (no checker, environment unchanged).
