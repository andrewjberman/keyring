# TO TCKT_VNEXT.TO-R18-TR3 -- WRITE the Terraform SOURCE for the two attachment routes, the Lambda's two environment variables and its S3 permission on the firm prefixes (source only; nothing is planned or applied)

<to_id>TCKT_VNEXT.TO-R18-TR3</to_id>
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
**Decomp cell:** `R18-tf-3` (`decompositions/TCKT_VNEXT_DECOMP_R18.md`) | **outcome_ref:** FWD-10 | **depends_on:** `R18-tf-1` (`TO-R18-TR1`, same slot: its `ATTACH_ADDRESS.json` is in your branch), then `R18-mt-2` (`TO-R18-TR2`, same file)

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~43` (the same worker, continued; worktree `C:/dev/wk-tckt-vnext-43`, branch `wk-TCKT_VNEXT-43`).
Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~43 <0.9.0_WK_TCKT_VNEXT~43@opal.agent>" -F <msgfile> -- <paths>`. The rules
of `TO-R18-TR1`'s face stand (Write tool for message files, rows `TCKT_VNEXT-D2-W43-S<k>`, each `.py` through `bash .tools/commit-gate.sh`,
no non-ASCII, a `controls.mutant` that FIRES, and NO live call: no AWS, no network, no `terraform plan` or `apply`; `terraform fmt -check` on
the one file is allowed if the binary is installed).

### THE CELL (`R18-tf-3`, inlined) -- SOURCE ONLY.

*PRD v0.6 C-ATTACH, C-DEPLOY: the ticket API issues short-lived presigned URLs for the trade form's upload and open. This cell gives the
Lambda (`TO-R18-L2`) what it reads from its environment and the one permission it needs, in `infra/aws/terraform/ticket-center/main.tf`. The
bucket policy and the bucket's CORS are NOT here: a Dell writes no bucket policy (C-DEPLOY); they are a laptop role request the issuer sends.*

Read first: `deliverables/0.9.0_WK_TCKT_VNEXT~43/ATTACH_ADDRESS.json` (your `TR1` record: `bucket_template`, `buckets`, `key_template`, `addresses`), the wire
contract `decompositions/TCKT_VNEXT_DECOMP_R18.md` section WIRE CONTRACT items 2 and 3, and in `main.tf` the Lambda module block that
carries `ROUTING_MATRIX` (its `environment_variables` or equivalent, about lines 340-392), the `local.ticket_routes` map (about 408-433),
and the `opal_ticket_api_ddb` policy with its `Sid`s (the `IrptRequestsInputOwnerRead` statement is the model of a narrow grant with a
`Condition`).

1. **Routes.** Add to `local.ticket_routes`: `attachment_upload = "POST /api/scoped/tickets/attachment-upload"` and `attachment_open =
   "GET /api/scoped/tickets/{ticketId}/attachment"`, with comments in the style of the neighbours (same CloudFront behavior
   `/api/scoped/tickets/*`, same `/*/*` invoke permission, no permission added). Do not touch the `meeting` entry (`TO-R18-TR2`'s).
2. **Environment.** Add to the Lambda's environment exactly `TICKET_ATTACH_BUCKET_TEMPLATE` = the `bucket_template` of `ATTACH_ADDRESS.json` and
   `TICKET_ATTACH_KEY_TEMPLATE` = its `key_template`, each as a literal copied from that file with a one-line comment naming the file and
   rule 30 (the values are builder output, printed by `TR1`; you type no address of your own).
3. **Permission.** One new IAM statement (a new `Sid`, `TicketAttachmentsTradeForm`, in the Lambda role's policy next to the DynamoDB
   statements, or a new `aws_iam_role_policy` attached to the same role if that is the file's pattern; say which and why): `Effect` Allow,
   `Action` exactly `["s3:PutObject", "s3:GetObject"]` (no List, no Delete, no Put ACL), `Resource` exactly one ARN per served firm,
   `arn:aws:s3:::<that firm's bucket from the record's `buckets`>/<key_template with {firm} replaced by the firm id>*` (a DIFFERENT bucket per firm: the state tier homes one per firm, R21) for `49financial`, `inflection` and `cottonwood` (a new firm
   is a grant edit; never a wildcard on the firm segment). No `Principal`, no condition needed.
4. Nothing else in the file changes. `terraform fmt -check` passes if the binary is installed (say which).
5. **Write `deliverables/0.9.0_WK_TCKT_VNEXT~43/tf_shape_check_tf3.py`** (AC1) and `mutant_check_tf3.py` (AC2), and a short `R18_TR3_RECORD.json`:
   the lines changed, the exact names the release order and the laptop role request need (the three buckets, the three prefixes, the two env names), `not_read`.

### ACCEPTANCE

<criterion id="R18TR3-AC1" cell_refs="R18-tf-3"><invocation>python C:/dev/wk-tckt-vnext-43/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~43/tf_shape_check_tf3.py</invocation><expect>^TF-ATTACH-OK </expect></criterion>
`R18TR3-AC1`: you write `tf_shape_check_tf3.py`: it reads `main.tf` (the path is an argument with this file as the default) and
`ATTACH_ADDRESS.json`, and prints `TF-ATTACH-OK routes=2 env=2 resources=3` only when (a) `ticket_routes` holds `attachment_upload` and `attachment_open` with
exactly the route keys above, plus the `meeting` and every earlier key unchanged; (b) the Lambda environment carries `TICKET_ATTACH_BUCKET_TEMPLATE` and
`TICKET_ATTACH_KEY_TEMPLATE` equal to the record's `bucket_template` and `key_template`; (c) the `TicketAttachmentsTradeForm` statement exists once with
`Action` exactly the two S3 actions and `Resource` exactly the three ARNs the record's per-firm buckets and key template give, no other S3 statement was added
and no statement of the file was widened; otherwise `TF-ATTACH-BAD <why>`, exit 1.

<criterion id="R18TR3-AC2" cell_refs="R18-tf-3"><invocation>python C:/dev/wk-tckt-vnext-43/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~43/mutant_check_tf3.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`R18TR3-AC2` (the one mutant that fails): you write `mutant_check_tf3.py`: it copies `main.tf` to a scratch folder OUTSIDE the product tree with `s3:DeleteObject`
added to the statement's actions, runs the shape checker on the copy, and prints `MUTANT-FIRES` only when the checker prints `TF-ATTACH-BAD` (else
`MUTANT-SURVIVES`, exit 1).

<criterion id="R18TR3-AC3J" cell_refs="R18-tf-3" judgment="true"/>
`R18TR3-AC3J` (judgment, graded at L9, never by you): the permission is the narrowest that serves a presigned put and get (two actions, three
firm prefixes, no wildcard on the firm), the environment values are the builder's output, no bucket policy or CORS is written here, and nothing
was planned or applied.

<expected_criteria>R18TR3-AC1 R18TR3-AC2 R18TR3-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~43/` and this order's file
  (status flip only). If anything OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it.
- If `ATTACH_ADDRESS.json` is absent from your branch, or `TR1` filed a BLOCKING row about the tier, STOP on this order and file a BLOCKING row
  naming it: you do not choose a bucket.
- AMENDMENT 1 (issuer, 2026-10-14, after worker 43's row `TCKT_VNEXT-D2-W43-S1`): the tier is `state` (R21) and homes a bucket PER FIRM, so the environment is a bucket TEMPLATE and a key
  TEMPLATE and the permission names three buckets; the single-bucket wording of the first cut is superseded.
- READ only: everything else.

<paths>
infra/aws/terraform/ticket-center/main.tf
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R18.md</decomp_doc>
<owned_cells>R18-tf-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~43/TCKT_VNEXT.TO-R18-TR3.ticket-attachment-routes-environment-and-s3-permission-terraform-source.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R18-TR3`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R18TR3-AC1,R18TR3-AC2,R18TR3-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- Terraform SOURCE in a worker worktree; the apply is the applier's (`TO-R18-REL`) under `safe-apply` and a change-management entry.
comp-routes: RUN -- both routes sit under the existing CloudFront behavior `/api/scoped/tickets/*` and the existing `/*/*` invoke permission; the release order re-checks it live. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: RUN -- one statement, two actions, three prefixes in three per-firm buckets, on the ticket Lambda's role; `comp-iam` gaps are read by the applier after the apply (necessary, not sufficient). The bucket policy is the laptop's. BLIND to: the live role's other statements and the live bucket policy (denominator: 1 new statement of 1 role policy file), so nothing here proves the permission is sufficient or that no other grant widens it.
comp-adversary: RUN -- by reading C-ATTACH and rule 30 against this cell; the lens: a wildcard on the firm segment, a Delete or List action, an address typed rather than copied from the builder's record, a bucket policy written from a Dell. NOT seen: the live role, the live bucket, its policy and CORS.
</preflight>

---

## RECORD FACE

- Cut on PRD v0.6 @c578883de8 (C-ATTACH, C-DEPLOY). Third order of slot 43's queue; round 18 chain B. Base: `R18TR3-AC1` and `R18TR3-AC2` FAIL as expected (no checker, no record).
- The laptop role request for the bucket policy and CORS is sent by the issuer from `ATTACH_ADDRESS.json` once `TR1` is merged; the release waits on it.
