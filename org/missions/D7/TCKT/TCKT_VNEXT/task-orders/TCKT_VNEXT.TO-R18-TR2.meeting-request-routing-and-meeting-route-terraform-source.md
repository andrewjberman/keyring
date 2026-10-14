# TO TCKT_VNEXT.TO-R18-TR2 -- WRITE the Terraform SOURCE for the meeting coordinator's queue and the meeting-outcome route (source only; nothing is planned or applied)

<to_id>TCKT_VNEXT.TO-R18-TR2</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~43</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD (an infrastructure path; the worker plans, applies and invokes NOTHING)
**Decomp cell:** `R18-mt-2` (`decompositions/TCKT_VNEXT_DECOMP_R18.md`) | **outcome_ref:** FWD-11 | **depends_on:** none (the route's path and name are fixed by the wire contract; your queue order is `TO-R18-TR1`, then this, then `TO-R18-TR3`: you start this after `TR1` is terminal)

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~43` (the same worker, continued; worktree `C:/dev/wk-tckt-vnext-43`, branch `wk-TCKT_VNEXT-43`).
Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~43 <0.9.0_WK_TCKT_VNEXT~43@opal.agent>" -F <msgfile> -- <paths>`. The rules
of `TO-R18-TR1`'s face stand (Write tool for message files, rows `TCKT_VNEXT-D2-W43-S<k>`, each `.py` through `bash .tools/commit-gate.sh`,
no non-ASCII, a `controls.mutant` that FIRES, and NO live call: no AWS, no network, no `terraform plan` or `apply`; `terraform fmt -check` on
the one file is allowed if the binary is installed).

### THE CELL (`R18-mt-2`, inlined) -- SOURCE ONLY.

*PRD v0.6 C-MEETING-REQUEST: the Meeting Request ticket lands in the meeting coordinator's queue, `jeanette@opalinvest.com`, and the
coordinator records the outcome through a new route. Routing is CONFIG in `infra/aws/terraform/ticket-center/main.tf`; routes are the
`local.ticket_routes` map there.*

In `infra/aws/terraform/ticket-center/main.tf` (read first: the `ROUTING_MATRIX = jsonencode({...})` block about lines 360-390 and the
`locals { ticket_routes = {...} }` block about lines 408-433):

1. `ROUTING_MATRIX.meeting_request.primary` becomes exactly `["jeanette@opalinvest.com"]` (today `manav` and `alyssa`); `secondary` and
   `visibility` stay `[]`. No other type's routing changes. Keep the file's comment style: one comment line saying why (the coordinator
   named by Andrew, PRD v0.6 C-MEETING-REQUEST).
2. In `local.ticket_routes` add ONE entry `meeting = "POST /api/scoped/tickets/{ticketId}/meeting"`, with a comment in the style of its
   neighbours (same CloudFront behavior `/api/scoped/tickets/*`, same invoke permission, no permission added). The Lambda handler is
   `TO-R18-L1`'s; the other new routes are `TO-R18-TR3`'s.
3. Nothing else in the file changes. `terraform fmt -check` passes on it if the binary is installed (say which).
4. **Write `deliverables/0.9.0_WK_TCKT_VNEXT~43/tf_shape_check_mt2.py`** (AC1) and `mutant_check_mt2.py` (AC2).

### ACCEPTANCE

<criterion id="R18TR2-AC1" cell_refs="R18-mt-2"><invocation>python C:/dev/wk-tckt-vnext-43/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~43/tf_shape_check_mt2.py</invocation><expect>^TF-SHAPE-OK </expect></criterion>
`R18TR2-AC1`: you write `tf_shape_check_mt2.py`: it reads `infra/aws/terraform/ticket-center/main.tf` (the path is an argument with this file as the
default) and prints `TF-SHAPE-OK meeting_request.primary=[jeanette@opalinvest.com] route=meeting` only when (a) the `meeting_request` block's `primary`
is exactly the one address, `secondary` and `visibility` empty; (b) `trade_request`, `service_request`, `other` and `analysis_request` routing blocks
are byte-identical to the same blocks of the file at the commit this worktree was cut from (the parent of your first commit on the branch, read with
`git show <sha>:infra/aws/terraform/ticket-center/main.tf`; record the sha in your record); (c) `ticket_routes` holds `meeting` with exactly the route key above and every other
route key is unchanged; otherwise `TF-SHAPE-BAD <why>`, exit 1.

<criterion id="R18TR2-AC2" cell_refs="R18-mt-2"><invocation>python C:/dev/wk-tckt-vnext-43/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~43/mutant_check_mt2.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`R18TR2-AC2` (the one mutant that fails): you write `mutant_check_mt2.py`: it copies `main.tf` to a scratch folder OUTSIDE the product tree with a second address
added to `meeting_request.primary`, runs the shape checker on the copy, and prints `MUTANT-FIRES` only when the checker prints `TF-SHAPE-BAD` (else
`MUTANT-SURVIVES`, exit 1).

<criterion id="R18TR2-AC3J" cell_refs="R18-mt-2" judgment="true"/>
`R18TR2-AC3J` (judgment, graded at L9, never by you): only the meeting coordinator's routing and one route entry changed, no permission or
other resource was added, and nothing was planned or applied.

<expected_criteria>R18TR2-AC1 R18TR2-AC2 R18TR2-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~43/` and this order's file
  (status flip only). If anything OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it.
- **Shared file:** `main.tf` is also edited by the next order of your queue (`TO-R18-TR3`: two routes, environment variables and the S3
  permission). Touch only the two spots above so the two merge cleanly.
- READ only: everything else.

<paths>
infra/aws/terraform/ticket-center/main.tf
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R18.md</decomp_doc>
<owned_cells>R18-mt-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~43/TCKT_VNEXT.TO-R18-TR2.meeting-request-routing-and-meeting-route-terraform-source.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R18-TR2`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R18TR2-AC1,R18TR2-AC2,R18TR2-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- Terraform SOURCE in a worker worktree; the apply is the applier's (`TO-R18-REL`) under `safe-apply` and a change-management entry.
comp-routes: RUN -- the new route key sits under the existing CloudFront behavior `/api/scoped/tickets/*` and the existing `/*/*` invoke permission (the comments of the neighbouring routes say so); the release order re-checks it live. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this cell; the S3 permission is `TO-R18-TR3`.
comp-adversary: RUN -- by reading C-MEETING-REQUEST against this cell; the lens: a routing change that touches another type, an extra address in the coordinator's queue, a route that needs a permission this cell does not add. BLIND to: the live routing environment variable and the live route table (denominator: 1 cell and 1 contract row read).
</preflight>

---

## RECORD FACE

- Cut on PRD v0.6 @c578883de8 (C-MEETING-REQUEST); the coordinator's users-table PROFILE was confirmed by the CTO (msg 7806). Second order of slot 43's queue; round 18 chain B. Base: `R18TR2-AC1` and `R18TR2-AC2` FAIL as expected (no checker, routing unchanged).
