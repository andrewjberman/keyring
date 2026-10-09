<task_order>
  <metadata>
    <id>MDPF_STRATID.TO-APPLY-W2-b.silver-wiring-explicit-deploy</id>
    <issued_by>2.0.0_SA_COO~S1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~DELL1</issued_to>
    <date>2026-10-09</date>
    <status>pending</status>
    <project_code>MDPF_STRATID</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- Round-less by design: an executor apply order, not a cell. Drain step 4's deploy leg (ledger mdpf-stratid-w2-wiring-silver L2):
the box/dell1 push held both silver files at its gate, and both are already on origin/CLOUD, so the deploy is an explicit act. -->
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP_W2.md</decomp_doc> (workstream 2, amendment A9, DRAIN SEQUENCE step 4): the deploy leg of cells `ST-w-5` and `ST-w-6`.
<owned_cells>ST-w-6</owned_cells>
</decomp_ref>

## THE ACT

The open change-management entry is `org/critical_paths/change_management/20261009T1444Z_mdpf-stratid-w2-wiring-silver_deploy_completion.md`
(sentinel `org/critical_paths/.open_deploys/mdpf-stratid-w2-wiring-silver.json`); it names both files by full repo path. Deploy, from a
tree at commit `ff8b8452f0` (or a descendant where both files are byte-equal to it), **in this order, one file per invocation**:

1. `bash .tools/safe-deploy.sh data/assets/scripts/silver/opal_strategy_matcher.py --author 0.7.0_AE_CloudOps~DELL1`
2. Only after 1 verifies: `bash .tools/safe-deploy.sh data/assets/scripts/silver/rebalancer_schemas.py --author 0.7.0_AE_CloudOps~DELL1`

`rebalancer_schemas.py` imports `opal_strategy_matcher`, so the reverse order would break the runner's import until the second upload.
If safe-deploy refuses the lane (Rule 13: DS owns QA-deploy of `data/*/scripts/silver`), stop before any upload and report the refusal
line; do not use `--allow-stale` and do not hand-copy with `aws s3 cp`.

Then read back: each S3 object under `s3://opal-data-mdpf/code/scripts/silver/` equals `git show ff8b8452f0:<repo path>` by content
(sha256 both), and the matcher's LastModified is not after the schemas'. Close ledger leg L2 with that proof (`deploy_ledger.py close-leg`).
Leg L3 (the next scheduled run) stays the issuer's.

## CONDITIONS (criteria of every order to a CloudOps lane; amendment A8)

(1) A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
    `opal-data-mdpf/code/` is the MDPF code prefix, not a firm data tree; state that in the report.
(2) Every send to `mdpf-daily-runner` is reported after the fact, with its command id and purpose (this order sends none).
(3) 49 Financial data never goes into another firm's tree (this order writes no data).
(4) IAM: none in this order.
(5) Naming-place enforcement: no new infra name in this order.

## ACCEPTANCE

<criterion id="APPLY-W2-b-AC1" cell_refs="ST-w-6"><invocation>python C:/Dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_5_ship.py</invocation><expect>W25-SHIP-OK</expect></criterion>
Run against the deploy tree before the first upload (both files ship together in every carrier).
<criterion id="APPLY-W2-b-AC2" cell_refs="ST-w-6" judgment="true"/>
`APPLY-W2-b-AC2` -- both S3 objects equal the committed bytes, uploaded matcher first, and ledger leg L2 is closed with that proof.

<expected_criteria>APPLY-W2-b-AC1 APPLY-W2-b-AC2</expected_criteria>

<proof_of_spec>
Criterion ids: APPLY-W2-b-AC1, APPLY-W2-b-AC2. Instance at `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.7.0_AE_CloudOps~DELL1/MDPF_STRATID.TO-APPLY-W2-b.silver-wiring-explicit-deploy.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> APPLY-W2-b-AC1,APPLY-W2-b-AC2` BEFORE the flip. Record AC2 as
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the issuer `2.0.0_SA_COO~S1`, who grades it on the report.
</proof_of_spec>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/tier2_senior/0.7.0_AE_CloudOps~DELL1/
org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.7.0_AE_CloudOps~DELL1/
</paths>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule moves; the runner syncs code/scripts/ at run time.
comp-iam: DECLARED-NOT-APPLICABLE no IAM; the runner role's read of the S3 list was granted and read back under TO-APPLY-W2-a.
comp-adversary: DECLARED-NOT-APPLICABLE the one hazard (upload order: schemas without the matcher breaks the runner's import) is controlled by the ordered act and AC1.
risk: WORLD -- a code upload the scheduled runner executes.
direct_act: true -- an executor apply order, round-less, no cell.
</preflight>

**REPORT:** each safe-deploy line, both sha256 pairs, both LastModified times, the ledger leg L2 close.
</task_order>
