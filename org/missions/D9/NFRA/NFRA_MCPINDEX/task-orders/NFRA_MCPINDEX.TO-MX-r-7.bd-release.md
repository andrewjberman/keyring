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

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-09-30 ~23:5xZ) -- UN-HELD; this release also carries MX-t-10; cut on the live ref with the stale-base guard.**
- MX-t-13 is complete on CLOUD (@d3b0efe5c6), under R20 X12. MX-t-10 (`etfs_get_positioning`) is complete on CLOUD
  (@29a40f5d4c), under R20 X11. It rides this release, so the census names both cells' gateway commits and the tool
  delta is +2.
- **Base, by REF (the MX-r-6 A6 rule):** read the live ref from the manifest and the artifact at PHASE A (MX-r-6 left
  42c52ed4d9). Re-read it immediately before the ANNOUNCE. PHASE B runs `deploy-to-ec2.sh` with `DEPLOY_BASE_REF` set.
  Preserve every other seat's files (list every live file absent or changed, and justify each as ours).
- **Sequencing:** 2.0.0_SA_COO~O's OG-t-2 is also cutting on 42c52ed4d9 (msg 27389). Before PHASE B, the issuer agrees
  the order with ~O. Whichever lands second re-cuts on the first's ref; the guard enforces this.
- ENABLED_INTEGRATIONS gains `blackdiamond` (7 ids). The saved `terraform plan` CREATES only the Black Diamond reader
  role, its policy, and the gateway role's permission to assume it. Its A1 terms stand (the fees writer is named in the
  ANNOUNCE).
- Graded by: no gate limb graded this modification (to-pipeline-gate LIMB 6 grades only a newly-added order; GATE (viii)
  finds `<placeholders>NONE</placeholders>`).

**AMENDED A3 (2.0.0_SA_COO~MI, 2026-10-01 ~04:3xZ) -- the base is OG-t-2's live ref; two carry-overs from it.**
- 2.0.0_SA_COO~O's OG-t-2 LANDED first (msg 27472): live since 2026-10-01T01:38:29Z at
  d61fde46933221e8afbac7418f06d7525d3347c8 (on base 42c52ed4d9). Per A2 this release re-cuts on that ref. Re-read the
  live ref from the host and the manifest at PHASE A and again immediately before the ANNOUNCE; if it is no longer
  d61fde4693, STOP and report it.
- Do NOT merge or cherry-pick OG-t-2's rel-branch manifest commit dc8f99b436 (row NFRA_OPLGTW Z-W12-S11). The
  manifest edit this release makes is its own.
- The host `.env` now carries MASTER_ADMIN_PRINCIPALS and WRITE_CAPABLE_PRINCIPALS (33->35 lines). PHASE A's census
  lists the live `.env` KEYS (never values) and the release must preserve both. The template's guard refuses (exit 3)
  without OG_MASTER_ADMIN_PRINCIPALS / OG_WRITE_CAPABLE_PRINCIPALS at deploy time; the issuer obtains them off-repo
  from 2.0.0_SA_COO~O for PHASE B. Never write their values into any file.
- Another gateway release is queued (NFRA_MCPMSP MS-d-2, which adds INTERNAL_READER_ROLE_ARN). The host takes one
  release at a time; whichever lands second re-cuts on the first's ref, and `DEPLOY_BASE_REF` enforces it.
- Graded by: no gate limb graded this modification (LIMB 6 grades only a newly-added order; GATE (viii) finds
  `<placeholders>NONE</placeholders>`).

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
