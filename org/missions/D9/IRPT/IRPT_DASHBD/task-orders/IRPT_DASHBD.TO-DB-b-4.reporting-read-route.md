# TO IRPT_DASHBD.TO-DB-b-4 -- The read route: `irpt-49f-reporting-read-lambda` hands the signed-in page the account's `series.json.gz` and `manifest.json` after the scope enforcer covers the account

<to_id>IRPT_DASHBD.TO-DB-b-4</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** PRD @84cff9014b section 2 hop 3 ("the served file -> the signed-in portal page on DEV
(real login, real backend): one fetch of series and manifest"), C-SEAM, C-SERVE, C-NAMES, C-FIRM; CTO 103260 | **Decomp cell:** `DB-b-4`
(decomposition section 1) | **outcome_ref:** FWD-1 (hop 3) | **depends_on:** DB-b-2 (the objects it serves)

---

## WORKER FACE

**The cell.** Build the function that gives the page the two platinum files for an account the viewer may see, mirroring how the
Holdings tab's function serves its JSON today, under its OWN function and Terraform root; plan it, do not apply it.

**The pattern (read it first).** `infra/aws/lambda/investor-reporting/holdings/entry.py`: the module resolves the viewer's current
selection through the `_scope` enforcer BEFORE any S3 read (`_current_selection`, lines 38-55: `enforcer.resolve_now(request)`; a refusal
raises `AccountNotCovered`), reads the artifact from server storage only ("never an event fixture"), and registers itself at the bottom
(lines 136-150: `ROUTES = {ROUTE_KEY: OPERATION}` passed to the shared builder with `function_name="irpt-holdings"`). Its Terraform root
`infra/aws/terraform/investor-reporting/holdings/` wires the function to the IRPT API. The shared pieces you reuse, never edit:
`infra/aws/lambda/investor-reporting/_scope/`, `_authz/`, `_contracts/`, `_ids/`, `_gate/`. IRPT_BCKEND row W88-S1 is the trap you do not
walk into: adding a route to ANOTHER function's `ROUTES` or to the deployed boundary's route table raised `EntryError` in that boundary;
this cell adds ONE route under its OWN function only.

**What you build.**
- `infra/aws/lambda/investor-reporting/reporting/entry.py`: `FUNCTION_NAME = "irpt-49f-reporting-read-lambda"` (the builder's output
  `name("irpt","49financial","reporting-read","lambda")`); ONE route (a scoped GET taking `account_id` and `which` in `{series, manifest}`)
  whose operation resolves the selection through the enforcer, refuses an account outside the viewer's scope with `AccountNotCovered`
  BEFORE any S3 read, and streams the object bytes from `lib.opal_naming.address("irpt","49financial","platinum","reporting",
  "account=<id>","series.json.gz" | "manifest.json")` with `Content-Type application/json`, `Content-Encoding gzip` for the series, and
  the object's ETag; a missing object answers the public envelope's NOT_READY, never a 500. Expose `serve_series(account_id,
  scope_accounts, which) -> bytes` as the local entry the check invokes (it applies the same covered-set test and raises
  `AccountNotCovered`; it makes no S3 call on refusal). `ROUTES` has exactly one key. Unit tests beside it for the refusal branch and the
  content headers (`tests/`).
- Terraform root `infra/aws/terraform/investor-reporting/reporting-read/` (own state key `investor-reporting/reporting-read/tfstate`; NEW
  resources only: the function through `yang-lambda`, a role reading ONLY the platinum prefix of the firm bucket, and the API wiring the
  holdings root uses for its function -- read `holdings/*.tf` for the exact resources and mirror them; `locals.tf` registry-derived).
  `terraform init` + `terraform plan -no-color` saved VERBATIM to
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/reporting-read.plan.txt`. Register the function in
  `lambda-source-map.json` and run `build-and-upload.sh investor-reporting irpt-49f-reporting-read-lambda` so the plan reads an artifact.
  NO APPLY: the apply is the issuer's under both never-widen halves (a new served function) after your drain.
- Record in your report the exact route path the page will call and the response headers, for workstream F (the seam is the FILE; the
  route's shape is what F's fetch needs to know).

<criterion id="DB-4-AC1" cell_refs="DB-b-4"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_4_ac1_read_route_local.py" .</invocation><expect>DB-4-AC1 PASS</expect></criterion>
`DB-4-AC1` -- the module imports, registers ONE route under `irpt-49f-reporting-read-lambda`; `serve_series` returns the REAL series and
manifest bytes byte-equal to the S3 objects for the thread account and refuses an uncovered account; the saved plan creates the function
with 0 destroy. Base: FAIL (no module).

<expected_criteria>DB-4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **AWS writes admitted:** the artifact upload `investor-reporting/irpt-49f-reporting-read-lambda.zip` only. No apply, no S3 object
  writes, no vendor call.
- **Refusal clause.** If the API wiring cannot be expressed in a new root without editing a shared root, STOP on that limb, file a row
  naming the shared file and the line, and deliver the function + plan of the resources you CAN own.

<paths>
infra/aws/lambda/investor-reporting/reporting/
infra/aws/terraform/investor-reporting/reporting-read/
infra/aws/lambda/investor-reporting/holdings/entry.py
infra/aws/terraform/investor-reporting/holdings/
infra/aws/terraform/modules/yang-lambda/
infra/aws/lambda/investor-reporting/_scope/
infra/aws/lambda/investor-reporting/_authz/
infra/aws/lambda/investor-reporting/_contracts/
infra/aws/lambda/investor-reporting/_ids/
infra/aws/lambda/investor-reporting/_gate/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/build-and-upload.sh
lib/opal_naming.py
infra/logic/registry/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 1 (round 1, workstream B), cell `DB-b-4`.
<owned_cells>DB-b-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB-4-AC1. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/IRPT_DASHBD.TO-DB-b-4.reporting-read-route.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB-4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hashes, the criterion's last line, the route path and headers for F, the plan's `Plan:` line,
and any surprise row id (`IRPT_DASHBD-W1-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a request-driven read function; no schedule, trigger or cron is created or moved (the holdings root it mirrors carries none either).
comp-iam: RUN -- denominator: 1 execution role read in infra/aws/terraform/investor-reporting/holdings/ (the irpt-holdings function's, scoped to its served prefix); the NEW role mirrors it with 1 platinum read prefix in one firm bucket; 0 existing roles or policies touched; the apply is the issuer's under both halves.
comp-blast: RUN -- a new served function; no existing route or function moves (its own root, its own ROUTES).
comp-routes: RUN as a reading -- the static route table gains one row at the apply; nothing existing is modified.
comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- DB-4-AC1 base FAIL (no module).
sequencing: second in 0.9.0_WK_IRPT_DASHBD~1's queue, after DB-b-2 (it serves DB-b-2's objects).
lane: the <paths> block IS the grant.
</preflight>
