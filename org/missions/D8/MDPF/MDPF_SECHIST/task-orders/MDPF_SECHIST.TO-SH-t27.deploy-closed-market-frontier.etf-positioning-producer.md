<task_order>
  <metadata>
    <id>MDPF_SECHIST.TO-SH-t27.deploy-closed-market-frontier.etf-positioning-producer</id>
    <issued_by>2.0.0_SA_COO~H1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~SH1</issued_to>
    <date>2026-10-14</date>
    <status>pending</status>
    <project_code>MDPF_SECHIST</project_code>
  </metadata>
<direct_act>true</direct_act>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>DEPLOY</workstream>
<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R6.md</decomp_doc> (round 6), row 1e: the producer apply of SH-t-24.
<owned_cells>SH-t-27</owned_cells>
</decomp_ref>

  <objective>
    Re-deploy the `etf-positioning-producer` Lambda from git pin `87a0dcf14d` (the same 14 members; two member bytes change) through `safe-apply`, under a
    change-management ledger entry you open first and close last. NO IAM change, NO schedule, env, layer or handler change: any of those in the plan is a STOP.
  </objective>

  <context>
    Pair, both halves SIGNED:
    - COO half: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/NEVER_WIDEN_HALF_REQUEST_SECHIST_CLOSED_MARKET_FRONTIER_DEPLOY_20261014.md` @9c0ab8819a, read whole.
    - CTO half: `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_CTO_HALF_SECHIST_CLOSED_MARKET_FRONTIER_DEPLOY_20261014.md` @2b58d0caf5. Its condition C1 is a SEQUENCE STOP, step 1 below.
    Dry run at the pin: `R6_CHECKS/r6_pin_dryrun_diff.py 2026-10-13` (188 holdings, 2 changed: SALXX in DIVZ and IDVZ, 16 cells), reported in the COO half.
    Live now (read 2026-10-14 13:41Z): `CodeSha256 YEYdzIZd2KQp3NngjJ5anv8RfTcsB8MqG21yRvCKVhM=`, LastModified 2026-10-09T20:08:21Z; artifact version `oqVg2A1LdkeHx5CHfzA6KfOs4HhEMq2T` of
    `s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip` (the rollback handle; record the live values again at step 2).
  </context>

  <steps>
    1. C1, the SEQUENCE STOP. Before anything else, read that the page rung is LIVE on PROD: `git -C C:/dev/ajb_workspace/portal fetch origin PROD -q && git -C C:/dev/ajb_workspace/portal merge-base --is-ancestor fa10e75861ab origin/PROD && echo RUNG-ON-PROD`
       AND `gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status` shows `completed` and `success` on a head that contains `fa10e75861ab`.
       If either does not read as stated, STOP and report; do not open a ledger entry. (The issuer sends this order when the DT lane's promote has read; the check is yours regardless.)
    2. Open the ledger entry (`.tools/deploy_ledger.py open`) with legs L1 package + apply and L2 first scheduled run (L2 is the issuer's read). Write into the entry the live `CodeSha256`, the
       artifact `VersionId` and the role's current inline policy sha256: they are the rollback.
    3. L1, the package: NO edit to `PACKAGE`. Build with `build_package.py --pin 87a0dcf14d` from `infra/aws/lambda/etfs-pipeline/etf-positioning-producer/`; the in-zip BUILD_MANIFEST must list the
       same 14 members as the live one, with exactly `etf_positioning_gold.py` and `etf_positioning_publisher.py` different in sha256 (write the member comparison to the evidence folder).
    4. The gate before apply: unzip into an empty directory, put only that directory and the calendar layer on the path, and run
       `import etf_positioning_gold, etf_history_gap_record; print(etf_positioning_gold.frontier_returns.__name__, etf_history_gap_record.record_address('2026-10-12'))`.
       It must print `frontier_returns s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=2026-10-12/gap_record.json`. Write the output to
       `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.7.0_AE_CloudOps~SH1/evidence/frontier_import_smoke_20261014.txt`.
    5. Upload and apply as the 2026-10-09 deploy did (artifact copy with `content-sha256` metadata verified by `head-object`, then `safe-apply` of the SAVED plan). The plan must show the Lambda's code change
       only (`s3_object_version`, `source_code_hash`, `last_modified`) and ZERO IAM change; grade it from the plan JSON, not the collapsed text. Save the plan summary to the evidence folder as
       `frontier_plan_20261014.txt`. Confirm a 0-diff re-plan (`terraform plan -detailed-exitcode` exit 0).
    6. Close L1 and report. L2 is the issuer's: the first scheduled run after the apply (cron(0 13 * * ? *), 2026-10-15 13:00Z) read against the dry run.
  </steps>

  <rollback>
    Restore the prior artifact bytes (version `oqVg2A1LdkeHx5CHfzA6KfOs4HhEMq2T`, `content-sha256` metadata `YEYdzIZd2KQp3NngjJ5anv8RfTcsB8MqG21yRvCKVhM=`) to the current version of the key, then `safe-apply`;
    the module reads the object at plan time, so the prior `CodeSha256` returns without `update-function-code`. No S3 delete and no policy change is needed.
  </rollback>

  <rules>
    - Never `aws lambda update-function-code`, never a bare `terraform apply`. Any IAM, schedule, env, layer or handler change in the plan is a STOP: roll back and report.
    - The `cot-satellites-characteristics-producer` also vendors `etf_positioning_gold.py`. It is NOT rebuilt here.
    - Client-data bounds (standing): never read, search, copy or `git show` any `org/**/W73_S*_EVIDENCE.json`, commits 1ba8eafcda / f5645bb6e9, the ADVI_COTBKF ~74/~66/~70 cottonwood manifests, the IRPT_DASHBD
      tie-out files, or anything under `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/`; search only inside the paths named here.
  </rules>

<paths>
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.7.0_AE_CloudOps~SH1/
org/critical_paths/.open_deploys/
org/critical_paths/change_management/
org/devices/state/dell1/
infra/aws/lambda/etfs-pipeline/etf-positioning-producer/
infra/aws/terraform/etfs-positioning/
org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the function's schedule is unchanged; only its code moves.
comp-iam: RUN -- the 2026-10-09 deploy measured the role at 9 statements; this act adds none (AC2 reads the plan JSON for ZERO IAM change).
comp-adversary: RUN -- a package missing a changed member (the member comparison, step 3); a plan carrying extra change (step 5 STOP); the rung not yet live (step 1 STOP); served drift (the dry run, 2 holdings / 16 cells). BLIND: the gold parquet write of the new column and the publisher stage, which the dry run did not execute; the L2 read covers them.
risk: WORLD.
</preflight>

<proof_of_spec>
  <criterion id="SH6-t27-AC1" cell_refs="SH-t-27"><invocation>grep -c "frontier_returns s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=2026-10-12/gap_record.json" org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.7.0_AE_CloudOps~SH1/evidence/frontier_import_smoke_20261014.txt</invocation><expect>1</expect></criterion>
  <criterion id="SH6-t27-AC2" cell_refs="SH-t-27" judgment="true"/><!-- the plan JSON shows the Lambda code change only and zero IAM, schedule, env, layer or handler change -->
  <criterion id="SH6-t27-AC3" cell_refs="SH-t-27" judgment="true"/><!-- a send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST -->
  <criterion id="SH6-t27-AC4" cell_refs="SH-t-27" judgment="true"/><!-- 49 Financial data never goes into another firm's tree -->
</proof_of_spec>

  <report>
    One message to 2.0.0_SA_COO~H1 when L1 is closed: the new `CodeSha256`, the plan summary path, the smoke output line, the member comparison path, the ledger entry id.
  </report>
</task_order>
