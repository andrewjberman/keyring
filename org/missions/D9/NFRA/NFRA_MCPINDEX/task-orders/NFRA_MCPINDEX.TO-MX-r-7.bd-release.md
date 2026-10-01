# NFRA_MCPINDEX task order -- `MX-r-7` -- the Black Diamond release: its reader role applied, `blackdiamond` enabled, then a live answer per tool class (r7.J1, FWD-4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-r-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~21</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy.
comp-iam: RUN -- 2026-09-30 ~08:4xZ by the issuer: `comp-iam role opal-gateway-role` shows sts:AssumeRole under the schwab ExternalId condition; `comp-iam role gateway-schwab-read-role` returns no match (its TF index does not resolve the reader role by name), so the APPLIED plane was read directly: simulate-principal-policy on gateway-schwab-read-role -> dim_position allowed, dim_transaction explicitDeny. This cell safe-applies MX-t-13's new reader role plus the gateway role's permission to assume it; nothing else moves.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-r-6 release pattern; never-widen halves (CTO + COO) and a G-A delta before PHASE B.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM, IAM).
</preflight>

## 1. THE CELL -- `MX-r-7` (round 5; `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/REINSTATE_RULINGS_20260930.md` @4e598ab7be, ruling B5)

**Start after MX-t-13 is complete and drained AND MX-r-6 is complete.** The gateway host takes one release at a time.
The issuer continues you with this order.

Follow MX-r-6's order exactly (`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-6.schwab-enable-release.md`,
PHASE A and PHASE B), with these differences:
1. The release is cut at the commit MX-r-6 left live, read by content, and cherry-picks MX-t-13's gateway commits.
2. `deploy-to-ec2.sh:197` gains exactly `blackdiamond`, giving 7 ids.
3. The saved `terraform plan` must CREATE only the Black Diamond reader role and its policy, plus the gateway role's
   permission to assume it. Any other planned change is a BLOCKING row.
4. `ANNOUNCE_MX-r-7.md` carries the pin, census, plan, tool-count delta and MX-a-8's read fence beside the role's
   resource list, so the halves can see they are equal.
5. NEVER-2 ledger `nfra-mcpindex-r5-bd-release`. Read back 7 ids, `/health` 200, and the tool count moved by exactly
   the delta. Roll back on any failed leg.
6. **r7.J1's material, after the deploy.** The ISSUER asks the first tool's question class through a principal session.
   You record in-process on the deployed tree which tools the host lists and what discover names for that question.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-09-30 ~09:3xZ), ruled by row Z-S62:** the integration id is `blackdiamond` (row
Z-W21-S1), and r7.AC2 reads it. PHASE A's ANNOUNCE also NAMES THE WRITER of `s3://opal-data-bd/silver/fees/` (row
Z-W21-S3) from a read-only trace, or states it unattributed with what was read, so the never-widen halves see it.
Graded by: no gate limb graded this modification.

**HELD (2.0.0_SA_COO~MI, 2026-09-30 ~11:2xZ, 1.0.0_SA_CTO~O msg 27114):** MX-t-13 is held on the R20 acknowledgement (its A3), so this release is not spawned until MX-t-13 lands.

## 2. BOUNDS

1. No identity, grant or sign-in change. The gateway role gains only the assume permission for the new data role.
2. Never half-landed: roll back from the rollback tree on any failed leg.
3. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/**
infra/aws/terraform/opal-gateway/blackdiamond_reader_iam.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r5-bd-release.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~21/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W21-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,J1</expected_criteria>
  <criterion id="AC1" cell_refs="MX-r-7" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/r7.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-7" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/r7.AC2.sh; echo "exit=$?"</invocation><expect>status=Success; /health=200; shipped 2 of 2; ids enabled 7 of 7 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="J1" cell_refs="MX-r-7" judgment="true"><!-- r7.J1, graded at L9 by 3.0.0_SA_CVO~O, never self-graded: FWD-4 (PRD:132-136) PROOF for Black Diamond -- the analysis record (MX-a-8), the tool list it produced, and a live answer per tool class with its denominators; the answer's figure and as-of equal the source object read by VersionId, and the route discover gave names that tool. The issuer's principal-session record is the material. --></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~21/NFRA_MCPINDEX.TO-MX-r-7.bd-release.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Reinstatement ruling B5; round-5 order item 4. Dry-run at base: r7.AC1 FAIL (no
entry); r7.AC2 FAIL (shipped 1 of 2, ids enabled 5 of 7).

<status>pending</status>
<round>5</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
