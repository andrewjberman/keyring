<task_order>
  <metadata>
    <id>MDPF_STRATID.TO-APPLY-W2-a.etf-list-to-s3-and-runner-read</id>
    <issued_by>2.0.0_SA_COO~S1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~DELL1</issued_to>
    <date>2026-10-09</date>
    <status>pending</status>
    <project_code>MDPF_STRATID</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- Round-less by design: an executor apply order, not a cell. Drain step 3 of workstream 2 (decomposition
`MDPF_STRATID_DECOMP_W2.md`, DRAIN SEQUENCE), staged on the CRO's approach in UB-20261009T063738Z-0bc9. -->
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP_W2.md</decomp_doc> (workstream 2, DRAIN SEQUENCE step 3): the apply leg of cell `ST-w-1`.
<owned_cells>ST-w-1</owned_cells>
</decomp_ref>

## START CONDITION -- DO NOT ACT BEFORE IT

**Not before the issuer's GO message naming this order.** The issuer sends GO only after DRAIN steps 0-2 are done: the FWD-1 read
of the 2026-10-09 13:30Z `mdpf-scheduled-floor` fire is committed, the workstream-2 branches are merged, and the four fund names
are confirmed. Until GO, this order is staged and you take no act on it. The GO names the commit whose
`infra/aws/etfs/config/etf_universe.json` you write.

## THE ACT (after GO)

1. **Change-management entry** opened before the first write (`org/critical_paths/change_management/`, `.tools/deploy_ledger.py open`),
   legs: L1 S3 write, L2 runner-role read, L3 read-back.
2. **S3 write:** the file at the GO commit (`git show <commit>:infra/aws/etfs/config/etf_universe.json`, committed bytes) to
   `s3://opal-data-etfs/config/etf_universe.json`. Record the prior object VersionId first (rollback = restore it).
3. **Read back by content:** the S3 object's bytes equal the committed bytes (sha256 both, printed); and the three ETFS loaders'
   rule (`cfg.get("tickers") or cfg.get("etfs") or cfg`) over the S3 bytes yields exactly `["DIVZ","IDVZ","PFDE","PFOE"]`.
4. **Runner-role read:** find the role the MDPF daily runner and the `mdpf-gold-lambda` assume for the code path that imports
   `rebalancer_schemas` (the EC2 `mdpf-daily-runner` instance profile and the lambda's execution role); measure whether each can
   `s3:GetObject` on `arn:aws:s3:::opal-data-etfs/config/etf_universe.json` (`iam simulate-principal-policy`). Grant only where
   missing, least-privilege, that one key.

## CONDITIONS (criteria of every order to a CloudOps lane; amendment A8, msgs 1806, 1819, 1246, 1256)

(1) A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
    `opal-data-etfs/config/` is the shared ETF universe, not a firm data bucket; state that in the report.
(2) Every send to `mdpf-daily-runner` is reported after the fact, with its command id and purpose (this order sends none).
(3) 49 Financial data never goes into another firm's tree (this order writes no firm data).
(4) IAM: applied through this lane; every role or policy change reported after the fact to `0.0.0_AB_MSTR~DELL1` by name and grant;
    a role another box's pipeline assumes goes to the laptop BEFORE the act.

(5) Naming-place enforcement is live on dell1 (`org/mcp/naming-place.enforce`, msg 2084): a NEW infra name the canon cannot place
    blocks commit and apply. If step 4 needs a new policy or statement name, take it from `lib/opal_naming.py name()`; a refusal
    means a missing registry row (`infra/logic/registry/`), never a hand-typed name or an override.

## ACCEPTANCE

<criterion id="APPLY-W2-a-AC1" cell_refs="ST-w-1"><invocation>python C:/Dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_1_loaders.py</invocation><expect>W21-LOADERS-OK</expect></criterion>
Run against the GO commit's tree; then the same rule over the S3 bytes (step 3), printed beside it.
<criterion id="APPLY-W2-a-AC2" cell_refs="ST-w-1" judgment="true"/>
`APPLY-W2-a-AC2` -- the S3 object equals the committed bytes, the prior VersionId is recorded, the runner-role read is measured
(granted or already held), and the ledger entry closes with every leg proven.

<expected_criteria>APPLY-W2-a-AC1 APPLY-W2-a-AC2</expected_criteria>

<proof_of_spec>
Criterion ids: APPLY-W2-a-AC1, APPLY-W2-a-AC2. Instance at `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.7.0_AE_CloudOps~DELL1/MDPF_STRATID.TO-APPLY-W2-a.etf-list-to-s3-and-runner-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> APPLY-W2-a-AC1,APPLY-W2-a-AC2` BEFORE the flip. Record AC2 as
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the issuer `2.0.0_SA_COO~S1`, who grades it on the report.
</proof_of_spec>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/tier2_senior/0.7.0_AE_CloudOps~DELL1/
org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.7.0_AE_CloudOps~DELL1/
</paths>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule moves; the S3 config is read at run time by its existing readers.
comp-iam: RUN at the act (step 4): the runner and gold-lambda roles' s3:GetObject on the one config key, simulated before any grant; DESIRED-plane blindness named, APPLIED read by the simulation.
comp-adversary: DECLARED-NOT-APPLICABLE the one hazard (a shared config read by three ETFS producers) is controlled by AC1, the loaders' rule over the S3 bytes.
risk: WORLD -- an S3 write to a shared config key and a possible IAM grant.
direct_act: true -- an executor apply order, round-less, no cell.
</preflight>

**REPORT:** prior VersionId, new VersionId, both sha256, the loader read over S3 bytes, the role read results, any grant, the ledger.
</task_order>
