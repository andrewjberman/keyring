<task_order>
  <metadata>
    <id>MDPF_STRATID.TO-APPLY-W2-a.etf-list-to-s3-and-runner-read</id>
    <issued_by>2.0.0_SA_COO~S1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~DELL1</issued_to>
    <date>2026-10-09</date>
    <status>complete -- landed by 0.7.0_AE_CloudOps~DELL1. S3: s3://opal-data-etfs/config/etf_universe.json carries the committed bytes at 7a8a5e39ab, put-object 14:14:17Z, read back FROM THE SERVED OBJECT with sha256 0c468c17.. equal and cmp IDENTICAL; the loaders rule over those bytes yields exactly [DIVZ,IDVZ,PFDE,PFOE]. AC1 W21-LOADERS-OK (3 of 3 loaders). IAM, on the LAPTOP CTO exact terms which supersede the issuer (1.0.0_SA_CTO msg 107995 via MSTR~DELL1 2562, relayed 2563): one statement per role, Sid EtfsConfigUniverseRead, s3:GetObject on that one key only -- mdpf-runner-scoped in place 33 to 34 with zero removed (commit 5bd12eb0b5), and a NEW separate policy mdpf-gold-etf-universe-policy on mdpf-gold-lambda-role named by the opal_name module so mdpf-gold-scoped stays byte-equal (commit 12bb251442, and the plan confirms that resource is not among the movers). safe-apply: 1 added, 1 changed, 0 destroyed. READ BACK LIVE: both roles allowed on the key, a SIBLING key in the same prefix implicitDeny on both, which is what proves no config/* wildcard. Ledger CLOSED 3 of 3, sentinel unlinked. Instance VALID rc=0, controls 5 of 5 discriminate. AC2 recorded UNVERIFIABLE-BY-INSTRUMENT for 2.0.0_SA_COO~S1 with no verdict. ONE CLAUSE OF AC2 CANNOT BE MET AS WRITTEN: there is no prior VersionId, because opal-data-etfs has never had versioning enabled -- the prior BYTES are committed instead @8625048a7b, before the write, and the gap is row MDPF_STRATID-D1-S3. Conditions: none of the three fired; the laptop had the condition-(4) before-notice and the after-the-fact report went to MSTR~DELL1 for the bus.</status>
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
