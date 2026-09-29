# NFRA_MCPINDEX task order -- `MX-r-5` -- a NARROW gateway release of MX-d-4, MX-d-5 and MX-t-9, then the thread re-run over the 4 A2 surfaces (r5.J1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-r-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~14</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- host, role and Terraform untouched.
comp-adversary: DECLARED-NOT-APPLICABLE -- R-8 narrow release; never-widen halves and a G-A delta for the new tool before the deploy.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM).
</preflight>

## 1. THE CELL -- `MX-r-5` (round 4; `org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round3.md` @f354170b42)

**Start after MX-d-4, MX-d-5 and MX-t-9 are complete and drained.** The issuer continues you with this order.

The MX-r-4 order is the worked precedent. READ ITS A1 AND A2 BLOCKS:
`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-4.thread-live-enable.md`. It covers the release
tree cut at the LIVE deployed commit, the census, the rollback tree, and the DEPLOY-ONLY tree (CLOUD with the gateway
directory replaced) that the halt gate admits.

### PHASE A -- no deploy
1. Read the deployed commit from the host's artifact, by content; the manifest can lag. Cut the release at it, then
   cherry-pick this project's new gateway commits (MX-d-4, MX-d-5, MX-t-9).
   - The census names only their files.
   - `deploy-to-ec2.sh:197` keeps the 5-id `ENABLED_INTEGRATIONS` value UNCHANGED.
2. Build the rollback tree at the live commit, and prove it per file against the live artifact.
3. Build the deploy-only tree (CLOUD, with the gateway directory replaced by the release's). Prove its gateway tree
   object equals the release's.
4. Write `ANNOUNCE_MX-r-5.md` and report the pin. The issuer takes it to 1.0.0_SA_CTO~O for the G-A delta (MX-t-9 adds
   a tool) and for both never-widen halves. DO NOT DEPLOY.

### PHASE B -- only on the issuer's GO
5. NEVER-2 ledger `nfra-mcpindex-r4-gateway-release`. Deploy from the deploy-only tree. Read the host back: the 5-id
   `.env` is unchanged, and the tool count gains exactly MX-t-9's tool. Record the manifest, then close the ledger.

### The thread re-run (item 5) -- after the deploy
6. The close run over the 4 A2 surfaces again (`platinum/mdpf`, `platinum/etfs`, `platinum/advi`, `json/*`).
   - Workers have no authenticated route, so the ISSUER runs it through a principal session, as in round 3.
   - You record what you can measure: which tools the host lists, and what discover names in-process on the deployed
     tree.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-09-29 ~05:2xZ):** MX-t-10 is released (G-W stands for platinum/etfs, @dc75ddbe32).
- If MX-t-10 is drained before your PHASE A cut, the release carries its gateway commits as well, and the census names
  them.
- If it is not, it rides the next release. The issuer states which at the GO.

## 2. BOUNDS

1. Terraform, the ALB, the role and the secrets are untouched. `deploy-to-ec2.sh:197` is unchanged.
2. Never half-landed: roll back from the rollback tree on any failed leg.
3. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/**
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r4-gateway-release.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~14/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W14-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,J1</expected_criteria>
  <criterion id="AC1" cell_refs="MX-r-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/r5.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/r5.AC2.sh; echo "exit=$?"</invocation><expect>status=Success; /health=200; new integrations shipped 2 of 2; new ones enabled=2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="J1" cell_refs="MX-r-5" judgment="true"><!-- r5.J1, graded at L9 by 3.0.0_SA_CVO~O, never self-graded: per A2 surface, is the question answered by a purpose-built tool whose figure and as-of equal the portal's served object, AND does the route discover gave name that tool? Denominator: 4 surfaces, printed. An answer that is right but reached through a route that named another tool FAILs that surface. The issuer's principal-session close run is the material. --></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~14/NFRA_MCPINDEX.TO-MX-r-5.release-and-thread-rerun.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-3 analysis s.5 items 2 (release), 3a (release) and 5 (the re-run + r5.J1). `infra/aws/ec2/opal-gateway/**` is granted ONLY on the never-merged dep- and rel- branches (the MX-r-4 A2 pattern). HELD cells MX-t-10/11 ride a later release once G-W stands.

<status>pending</status>
<round>4</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
