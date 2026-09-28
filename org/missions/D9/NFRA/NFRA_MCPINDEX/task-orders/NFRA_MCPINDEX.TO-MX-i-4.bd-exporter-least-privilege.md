# NFRA_MCPINDEX task order -- `MX-i-4` -- least privilege on `bd_exporter_additional`: the portal-login secret leaves the exporter role once nothing reads it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-i-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~8</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- an IAM policy change; no schedule, rule, cron or monitor.
comp-iam: RUN -- denominator: 1 inline policy read live by the issuer at the cut (bd-exporter-ec2-role AdditionalPermissions: 4 statements, 1 GetSecretValue action, 1 resource naming opal/bd/credentials, 1 naming blackdiamond/49f/session); blind to other roles that may read the secret, which step 1 censuses. This order NARROWS `aws_iam_role_policy.bd_exporter_additional` (`name = "AdditionalPermissions"`, `infra/aws/terraform/bd-pipeline/iam.tf`) by one Resource element; it adds nothing.
comp-adversary: DECLARED-NOT-APPLICABLE -- a removal gated on a printed caller census.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (IAM read, SSM get-document, Terraform).
</preflight>

## 1. THE CELL -- `MX-i-4` (round 3, enrichment item 5)

**Start this order only after MX-s-12's acceptance.** The issuer continues you with it.

**Why.** The live inline policy `AdditionalPermissions` on `bd-exporter-ec2-role` grants `secretsmanager:GetSecretValue`
on several secrets. One of them is `opal/bd/credentials`, the Black Diamond PORTAL login. The Playwright portal legs
that read it are the ones MX-s-12 retires or ports. A role that no longer needs a secret should not be able to read it.

1. **Caller census, before any change.** Who reads `opal/bd/credentials` using THIS role?
   - Every SSM document the role's instances run (`aws ssm get-document`; the enumerated BD documents): does any
     still read the secret?
   - Every tracked script those documents call, found with `comp-find 'opal/bd/credentials'`, with the denominator
     printed.
   - Name each reader LIVE (a scheduled or triggered path runs it today) or DEAD. Write the census to
     `CENSUS_MX-i-4.md` in your deliverables.
2. **If the census reads 0 live readers:** remove the one Resource element `opal/bd/credentials` from that statement in
   `iam.tf`. Nothing else in the policy changes.
   - Open the NEVER-2 ledger `nfra-mcpindex-bd-exporter-least-privilege` and commit it before the apply.
   - Apply with `.tools/safe-apply.sh`, where the plan reads exactly `0 to add, 1 to change, 0 to destroy` and the one
     change is that policy losing that element.
   - A post-apply `terraform plan -detailed-exitcode` returns 0.
   - Rollback is re-adding the element, then safe-apply.
   - Close the ledger.
3. **If the census reads >= 1 live reader:** do NOT change the policy. REFUSE AC1 with the census as its measurement.
   Name each live reader in a row.
4. Run AC1 and AC2.

## 2. BOUNDS

1. Only that one Resource element. No other statement, role, secret or resource.
2. The secret itself is untouched: no rotation, no deletion. Both are Andrew's.
3. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/terraform/bd-pipeline/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-bd-exporter-least-privilege.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~8/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W8-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-i-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/i4.AC1.sh; echo "exit=$?"</invocation><expect>get-role-policy rc=0; statements read>=1; resources naming opal/bd/credentials: 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-i-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/i4.AC2.sh; echo "exit=$?"</invocation><expect>get-role-policy rc=0; GetSecretValue actions>=1; resources naming blackdiamond/49f/session>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~8/NFRA_MCPINDEX.TO-MX-i-4.bd-exporter-least-privilege.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once: the census table, the plan line, the ledger path, the
commit hashes, and any rows. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-2 analysis s.5 item 5 @e4445020f5, "after item 1 lands".
- Dry-run at base: i4.AC1 FAIL (4 statements read; 1 resource names opal/bd/credentials). i4.AC2 PASS (the 49F session
  grant is present; a regression guard for MX-s-12's producer).
- The census may read >= 1: the transaction and allocation Playwright downloaders are not retired by MX-s-12. A
  refusal with its census is a valid outcome, and the issuer routes the readers.
- This narrows a grant and moves no served output, so it takes no never-widen half. The NEVER-2 ledger covers the act.

<status>pending</status>
<round>3</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
