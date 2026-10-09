# TO ADVI_BILLING.TO-AB-t-2 -- FWD-1 hop 3: the read route advi-49f-billing-read-lambda that hands the advisor page one household's fee object, built, invoked locally against the real object, planned (no apply)

<to_id>ADVI_BILLING.TO-AB-t-2</to_id>
<project>ADVI_BILLING</project>
<issued_to>0.9.0_WK_ADVI_BILLING~1</issued_to>
<issued_by>2.0.0_SA_COO~B2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D8 | **Fabric:** dell2 | **PRD:** v0.2 @d45dc8a52f | **Decomp cell:** `AB-t-2` (decomposition section 2) | **outcome_ref:** FWD-1 | **depends_on:** AB-t-1 (reads its object).

---

## WORKER FACE

Same worktree as your previous order: `C:/dev/wk-advi-billing-1`; your folder
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~1/`. The object you serve is the one AB-t-1 wrote;
its key and `client_key` are in `AB_T1_RECORD.json` there, and its shape is `org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json`.

**The cell.** An advisor on the 49 Financial page opens a household; the page will call
`GET /api/scoped/partners/books/relationship/{clientKey}/fee-quarter/{quarter}` and render the fee. Build the function that
answers it, under its OWN function and route (never a route added inside `opal-partners-data`'s boundary).

- **Names (rule 30, `lib/opal_naming.py` `name()`; never type one):** `name("advi","49financial","billing-read","lambda")` ->
  `advi-49f-billing-read-lambda`; `name("advi","49financial","billing-read","role")` -> `advi-49f-billing-read-role`. The object
  address comes from `address("advi","49financial","gold","advi_billing","quarter=<q>","<client_key>.json")`.
- **Pattern to mirror (read first):** `infra/aws/lambda/investor-reporting/reporting/entry.py` (one function, its own `ROUTES`,
  a local-invoke path for tests) and its root `infra/aws/terraform/investor-reporting/reporting-read/` (`main.tf` backend, `api.tf`
  integration + route on the shared API, `iam.tf`, `lambda.tf`, `locals.tf`, `remote_state.tf`); packaging through
  `infra/aws/lambda/ci/lambda-source-map.json` (add ONE new entry for this function; touch no other entry).
- **Who may read (the refusal branch):** scope the viewer exactly as `opal-partners-data` scopes its relationship routes --
  firm from the claims (49 Financial only), the advisor's book, pseudonymization of PII -- see
  `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py:1841-1870` and the `_pseudonymize_s3_response`
  it calls. Reuse that code by import or vendoring as that function's own build does; do not re-invent the rule. A viewer outside
  the firm or outside the household's book gets a refusal and NO S3 read. `quarter` must match `^20\d\dQ[1-4]$`; `clientKey`
  must match `^rel_[A-Za-z0-9_]+$`; anything else is 400.
- **Source:** `infra/aws/lambda/advi/billing-read/entry.py` (+ whatever the mirrored pattern needs beside it). **Root:**
  `infra/aws/terraform/advi/billing-read/`, backend key `advi/billing-read/tfstate`, IAM read-only (`s3:GetObject`) on
  `<the builder's advi_billing gold prefix>/*` and nothing else.
- **Tests:** `infra/aws/lambda/advi/billing-read/tests/test_billing_read.py`, run with pytest. At least: a test whose name
  contains `real_object` that invokes the handler locally for the AB-t-1 household as an in-scope viewer and asserts the body
  bytes equal the S3 object's bytes (after any pseudonymization the scope rule applies -- if it rewrites names, assert the fee
  fields are unchanged); and a test whose name contains `refused` asserting an out-of-scope viewer is refused with no S3 read.
- **Plan, no apply.** `terraform init` + `terraform plan -out` in the root; save the plan's text to `AB_T2_PLAN.txt` in your
  folder (it must add only: 0 to change, 0 to destroy). The apply is the issuer's act after the drain.

<criterion id="AB1-2-AC1" cell_refs="AB-t-2"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r1/r1_checks.py . AB1-2-AC1</invocation><expect>AB1-2-AC1 PASS</expect></criterion>
`AB1-2-AC1` -- the local-invoke tests pass, one serving the real object's bytes and one refusing an out-of-scope viewer. Base: FAIL.

<criterion id="AB1-2-AC2" cell_refs="AB-t-2"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r1/r1_checks.py . AB1-2-AC2</invocation><expect>AB1-2-AC2 PASS</expect></criterion>
`AB1-2-AC2` -- the saved plan adds only and names the builder's function and role. Base: FAIL.

<expected_criteria>AB1-2-AC1,AB1-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **AWS:** S3 reads; `terraform init`/`plan` only. NO `terraform apply`, no `aws lambda` write, no S3 write, no secret read beyond
  what `plan` itself resolves, no vendor call.
- **Refusal clause.** An apply, a deploy, an edit to another function's source or root, a second source-map entry, or a route
  inside `opal-partners-data` is a defect: stop and file a row.

<paths>
infra/aws/lambda/advi/billing-read/
infra/aws/terraform/advi/billing-read/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~1/
org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_BILLING/task-orders/ADVI_BILLING.TO-AB-t-2.fee-quarter-read-route.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BILLING/decompositions/ADVI_BILLING_DECOMP.md</decomp_doc> section 2 (round 1), cell `AB-t-2`.
<owned_cells>AB-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AB1-2-AC1, AB1-2-AC2. The instance goes at
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~1/ADVI_BILLING.TO-AB-t-2.fee-quarter-read-route.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AB1-2-AC1,AB1-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the plan's add count and resource list, the scope rule reused (file and
function), the route key, and every row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- a NEW function, role and route planned; 0 existing served keys or routes modified (plan must read 0 to change).
comp-iam: RUN -- `comp-iam role advi-49f-billing-read-role` -> "No role matching" (planned, not in Terraform yet); BLINDNESS: the
  template `irpt-49f-reporting-read-role` also does not resolve by name in comp-iam (its role name is built in locals), so comp-iam
  cannot grade this role before the plan; the saved plan (AB1-2-AC2) is the IAM read, re-read by the issuer before the apply.
comp-routes: RUN as a reading -- the shared API gains ONE route at the issuer's apply; none is modified.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: thread round; the lens runs on the enrichment round that touches its surface.
checks dry-run at base: AB1-2-AC1/AC2 FAIL as expected.
lane: the <paths> block IS the grant.
</preflight>
