# TO ADVI_BILLING.TO-AB-r-3 -- E2: the release packet that lets the gateway's owners ship the SMArtX statement copy -- registration, IAM grant planned, config, packet; nothing deployed

<to_id>ADVI_BILLING.TO-AB-r-3</to_id>
<project>ADVI_BILLING</project>
<issued_to>0.9.0_WK_ADVI_BILLING~7</issued_to>
<issued_by>2.0.0_SA_COO~B2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>

**Directive:** D8 | **Fabric:** dell2 | **PRD:** v0.2 @d45dc8a52f | **Decomp cell:** `AB-r-3` (decomposition section 4, round 3) | **outcome_ref:** FWD-1 / FWD-3 (E2) | **depends_on:** none. **Authority:** CTO ADDENDUM 3 @7f414eb19e (msg 3004).

---

## WORKER FACE

Your worktree is `C:/dev/wk-advi-billing-7`; run everything from its root. Your folder is
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~7/`.

**The cell.** Round 2 built `infra/aws/ec2/opal-gateway/app/integrations/advi_billing/site_to_s3.py` (`copy_site_file_to_s3(user_token, site_id,
item_id, quarter)`: copies one SharePoint `.xlsx` to the builder's `smartx/49financial/bronze/fee_statement/quarter=<q>/` prefix only, via a
conditional put; its destination root comes from env `ADVI_FEE_STATEMENT_S3_ROOT`; tests `infra/aws/ec2/opal-gateway/tests/test_advi_site_to_s3.py`).
The gateway is NFRA_OPLGTW's service (site Z), deployed by its owners through `infra/aws/ec2/safe-ec2-deploy.sh` +
`infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` (STALE-BASE GUARD: `DEPLOY_BASE_REF` must be the host's running ref). This cell prepares everything
they need; it deploys and applies nothing.

1. **Registration** in `infra/aws/ec2/opal-gateway/app/tools.py`: an `@mcp.tool()` `copy_site_file_to_s3(site_id, item_id, quarter)` wrapping the
   module through `_run(...)` exactly as the neighbouring tools do (`tools.py:117` `_run`), refusals returned as `{"error", "refused": true}`, and
   kept OUT of any read-only/safe tool set (it writes). Test `infra/aws/ec2/opal-gateway/tests/test_advi_site_to_s3_registration.py`: a test
   named with `registered` (the tool is in the server's tool table) and one named with `not_safe` (it is absent from the safe/read-only set).
2. **IAM grant:** a NEW file `infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf` modelled on `taxsma_gateway_iam.tf`: an inline policy
   on the gateway instance role allowing `s3:PutObject` on the builder's `smartx/49financial/bronze/fee_statement/*` and nothing else (the ARN built
   from `lib/opal_naming.py` output the way the root already does; if the root cannot call the builder, say how the neighbouring files carry
   addresses and follow that). Check it against `mcpmsp_gateway_firm_deny.tf` (a cross-firm deny may block the prefix) and say what you found.
   `terraform init` + `plan` of `infra/aws/terraform/opal-gateway/`; save the text to `AB_R3_PLAN.txt` in your folder. The plan may touch ONLY
   resources named with `advi_billing`; if it shows other drift, record it and STOP (file a row) -- never apply.
3. **Config:** name in the packet the exact place the gateway reads env (its systemd unit or env file under `infra/aws/ec2/opal-gateway/deploy/`)
   and the line `ADVI_FEE_STATEMENT_S3_ROOT=<address() prefix>`; do not edit the deployed config file unless it lives in the repo AND only the
   new line changes (then include it in the packet's diff).
4. **`RELEASE_PACKET_E2.md`** in your folder, for the gateway's owners: the commits to carry, the DEPLOY_BASE_REF rule (cut the release on the host's
   running ref plus these commits), the blast radius (one new write tool; one PutObject grant on one prefix; one env line), the rollback (redeploy the
   prior ref; destroy the one policy), and the post-deploy proof (tool listed; one refused call on a bad quarter; the env line equals `address()`).

<criterion id="AB3-3-AC1" cell_refs="AB-r-3"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB3-3-AC1</invocation><expect>AB3-3-AC1 PASS</expect></criterion>
`AB3-3-AC1` -- the registration tests pass, one *registered*, one *not_safe*. Base: FAIL.

<criterion id="AB3-3-AC2" cell_refs="AB-r-3"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB3-3-AC2</invocation><expect>AB3-3-AC2 PASS</expect></criterion>
`AB3-3-AC2` -- the saved plan destroys nothing and touches only advi_billing resources; the packet states DEPLOY_BASE_REF, the env line and the rollback. Base: FAIL.

<expected_criteria>AB3-3-AC1,AB3-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- terraform init/plan only; NO apply, no deploy, no S3 write, no secret read; edit only the files the face names.
- **Refusal clause.** An edit outside the grant, a write or deploy the face does not name, a vendor call, or an account number, name
  or dollar figure in a committed file is a defect: stop and file a row.

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/tests/test_advi_site_to_s3_registration.py
infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf
infra/aws/ec2/opal-gateway/deploy/
org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~7/
org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_BILLING/task-orders/ADVI_BILLING.TO-AB-r-3.gateway-release-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BILLING/decompositions/ADVI_BILLING_DECOMP.md</decomp_doc> section 4 (round 3), cell `AB-r-3`.
<owned_cells>AB-r-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AB3-3-AC1, AB3-3-AC2. The instance goes at
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~7/ADVI_BILLING.TO-AB-r-3.gateway-release-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AB3-3-AC1,AB3-3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, what the cell measured, and every row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- nothing live moves in the cell.
comp-iam: RUN -- 214 IAM roles parsed from Terraform (196 services, 21 EC2); opal-gateway-role is seen (sources infra/aws/terraform/opal-gateway/main.tf, taxsma_gateway_iam.tf); the new advi_billing grant is not in Terraform yet, so comp-iam is BLIND to it until the cell writes it -- the saved plan is the read of that one PutObject grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: enrichment cell; no served claim is graded here.
checks dry-run at base: AB3-3-AC1, AB3-3-AC2 FAIL as expected.
lane: the <paths> block IS the grant.
</preflight>
