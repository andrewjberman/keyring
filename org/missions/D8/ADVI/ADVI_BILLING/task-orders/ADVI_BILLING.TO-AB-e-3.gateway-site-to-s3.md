# TO ADVI_BILLING.TO-AB-e-3 -- E2 path: a gateway capability that copies one SharePoint site item to the builder's SMArtX fee-statement bronze prefix, built and tested, not deployed

<to_id>ADVI_BILLING.TO-AB-e-3</to_id>
<project>ADVI_BILLING</project>
<issued_to>0.9.0_WK_ADVI_BILLING~5</issued_to>
<issued_by>2.0.0_SA_COO~B2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D8 | **Fabric:** dell2 | **PRD:** v0.2 @d45dc8a52f | **Decomp cell:** `AB-e-3` (decomposition section 3, round 2) | **outcome_ref:** FWD-1 / FWD-3 (E2 path) | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-advi-billing-5`; run everything from its root. Your folder is
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~5/`.

**The cell.** SMArtX's quarterly fee statements for 49 Financial exist only as `.xlsx` files in the SharePoint site `Shared`
(Documents/Billing/49F). The Opal gateway (`infra/aws/ec2/opal-gateway/app/`) already reads a site item's bytes with the caller's Graph
token: `tools.py:699-730` (`graph.call(t, "GET", f"/sites/{site_id}/drive/items/{item_id}/content")`) and
`integrations/opal_portal/integration.py:261-268` (`_graph_download`). Nothing writes such bytes to S3.

1. Build ONE new module `infra/aws/ec2/opal-gateway/app/integrations/advi_billing/site_to_s3.py` (+ `__init__.py`): a function
   `copy_site_file_to_s3(user_token, site_id, item_id, quarter)` that downloads the item's bytes (reuse the existing Graph call; do not
   re-implement auth), requires an `.xlsx` name, and writes it to EXACTLY `lib/opal_naming.py`
   `address("smartx","49financial","bronze","fee_statement","quarter=<quarter>","<sanitized original name>")`
   (= `s3://opal-data-assets/smartx/49financial/bronze/fee_statement/quarter=<q>/<name>.xlsx`), refusing any quarter not matching
   `^20\d\dQ[1-4]$`, any other destination, and an existing key (no overwrite). It returns `{s3_key, bytes, sha256}`. Read how the
   gateway imports the builder (or vendors it) and follow that.
2. Tests: `infra/aws/ec2/opal-gateway/tests/test_advi_site_to_s3.py` (mocked Graph and S3, no network), including a test named with
   `builder_address` (the key equals the builder's output) and tests named with `refuses` (bad quarter, non-xlsx, existing key).
3. Do NOT register the tool in the gateway's tool table (a shared file). Name in your report the exact registration line the issuer adds
   at the merge, and the IAM grant the gateway role will need (`s3:PutObject` on that prefix): the deploy is a later served act.

<criterion id="AB2-3-AC1" cell_refs="AB-e-3"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB2-3-AC1</invocation><expect>AB2-3-AC1 PASS</expect></criterion>
`AB2-3-AC1` -- the gateway module's tests pass, including *builder_address* and *refuses*. Base: FAIL.

<expected_criteria>AB2-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- No network call in tests; no S3 write; no deploy; no edit to tools.py, the server registration or any shared gateway file.
- **Refusal clause.** An edit outside the grant, a write the face does not name, a vendor call, a secret read, or an account
  number, name or dollar figure in a committed file is a defect: stop and file a row.

<paths>
infra/aws/ec2/opal-gateway/app/integrations/advi_billing/
infra/aws/ec2/opal-gateway/tests/test_advi_site_to_s3.py
org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~5/
org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_BILLING/task-orders/ADVI_BILLING.TO-AB-e-3.gateway-site-to-s3.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BILLING/decompositions/ADVI_BILLING_DECOMP.md</decomp_doc> section 3 (round 2), cell `AB-e-3`.
<owned_cells>AB-e-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AB2-3-AC1. The instance goes at
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~5/ADVI_BILLING.TO-AB-e-3.gateway-site-to-s3.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AB2-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, what the cell measured (counts, classes, masked ids only), and every row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- code only; no served key or route moves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role is created or changed in this cell.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: enrichment cell; no served claim is graded here.
checks dry-run at base: AB2-3-AC1 FAIL as expected.
lane: the <paths> block IS the grant.
</preflight>
