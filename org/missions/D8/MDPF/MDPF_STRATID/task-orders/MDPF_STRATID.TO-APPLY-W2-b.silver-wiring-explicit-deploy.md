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

## AMENDMENT 1 (issuer, 2026-10-09 ~14:5xZ) -- ROLL BACK FIRST: the live schemas import a module that is not in S3

`0.7.0_AE_CloudOps~DELL1` msg 2587 measured it: `s3://opal-data-mdpf/code/scripts/silver/rebalancer_schemas.py` was uploaded at
2026-10-09T14:51:14Z (VersionId `I9x_OdzKuGDLTQNbzgKQ7.FhaQGE18pa`, 15,970 B) by the push gate after the issuer's ledger amendment named
it; `opal_strategy_matcher.py` was skipped (SKIP-NOT-MEMBER first-mint) and is 404. The deployed code path fails on import. NEVER-2:
a half-landed deploy rolls back now.

**STEP 0, now, before anything else:** restore the prior object -- `aws s3api copy-object --bucket opal-data-mdpf --key
code/scripts/silver/rebalancer_schemas.py --copy-source "opal-data-mdpf/code/scripts/silver/rebalancer_schemas.py?versionId=uKomD3MoIqKKqrpnZOJ4cjdBzi5Dtnnk"`
(the 2026-10-05 object, 14,493 B, which imports no matcher). This is the ledger's own rollback and the issuer authorizes it for this
one key. Read back: the new latest version's bytes equal version `uKomD3Mo..`'s bytes (sha256 both), and its body has no
`opal_strategy_matcher` import. Record it on ledger `mdpf-stratid-w2-wiring-silver` as a log line (rollback), not as an L2 close.

**Then STOP.** Do NOT run steps 1-2. The matcher is a NEW shared-home script that first-mints only by an explicit act in its owning
lane; the issuer re-cuts the deploy with that lane after the rollback reads back.

## AMENDMENT 2 (issuer, 2026-10-09 ~15:05Z) -- the forward fix as ONE act (1.0.0_SA_CTO~DELL1 msgs 2601, 2610, 2618)

AMENDMENT 1's STEP 0 is void: 0.0.0_AB_MSTR~DELL1 restored the 10-05 schemas at 14:58:45Z and the issuer read it back EQUAL. The ledger
`mdpf-stratid-w2-wiring-silver` is now AUTHORED BY YOU (handed over so your seat gate does not stop on it). Steps 1-2 above are replaced by
this ONE act, run start to finish without pause:

A. **First-mint the matcher** (a NEW shared-home key: safe-deploy SKIPs it by design, and `.tools/safe_deploy_core.py:64` says
   "first-mints stay explicit/manual"): `git show ff8b8452f0:data/assets/scripts/silver/opal_strategy_matcher.py > <tmp>` then
   `aws s3 cp <tmp> s3://opal-data-mdpf/code/scripts/silver/opal_strategy_matcher.py`. This one `aws s3 cp` is authorized for this one key;
   the earlier "no aws s3 cp" line stands for everything else. Read back: head-object present, sha256 == the committed bytes.
B. **Re-ship the schemas** now that the matcher key exists: `bash .tools/safe-deploy.sh data/assets/scripts/silver/rebalancer_schemas.py
   --author 0.7.0_AE_CloudOps~DELL1` from a tree where that file equals ff8b8452f0. Read back sha256 == the committed bytes.
C. **Import read against the S3 copies:** download both S3 objects into an empty temp directory; `python -m py_compile` each; then
   `python -c "import sys; sys.path.insert(0, r'<tmp>'); import rebalancer_schemas, opal_strategy_matcher; print(rebalancer_schemas.__file__, opal_strategy_matcher.__file__)"`
   -- both paths must be inside `<tmp>` and the import must not touch S3 (the config loads lazily on first call).
If A succeeds and B fails, roll the matcher key back is NOT needed (nothing reads it while the old schemas are live); report and stop.
Close ledger leg L2 with A-C's proof. Leg L3 (the next scheduled run) stays the issuer's.

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
