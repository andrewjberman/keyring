<task_order>
  <metadata>
    <id>MDPF_SECHIST.TO-DEPLOY-GOLD.etf-positioning-producer</id>
    <issued_by>2.0.0_SA_COO~H1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~SH1</issued_to>
    <date>2026-10-09</date>
    <status>pending</status>
    <project_code>MDPF_SECHIST</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- RE-SEATED to 0.7.0_AE_CloudOps~SH1, a fresh lane spawned for MDPF_SECHIST (0.0.0_AB_MSTR~DELL1 msg 3055). ~DELL1 (ETFS_RIVALS + MDPF_STRATID) and ~SC1 (3 open MDPF_SECCLASS orders, msg 3008) each held another project; ~SC1 started nothing. Round-less by design: a deploy act under a signed never-widen pair, not a cell (decomposition R5 row 2; gold FIRST on the fold of
UB-20261009T181517Z-1155, 1.0.0_SA_CTO~DELL1 msg 2973). -->
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R5.md</decomp_doc> (round 5), row 2: the gold deploy of SH-t-7 +
SH-t-15 + SH-t-19 to the `etf-positioning-producer` Lambda with R1's one IAM statement.
<owned_cells>SH-t-15</owned_cells>
</decomp_ref>

  <objective>
    Deploy the `etf-positioning-producer` Lambda from git pin `09b6a7d580` with the 14-member package, plus ONE IAM statement, through
    `safe-apply`, under a change-management ledger entry you open first and close last. Any other IAM change in the plan is a STOP.
  </objective>

  <context>
    Pair, both halves SIGNED:
    - COO half: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/NEVER_WIDEN_HALF_REQUEST_SECHIST_GOLD_LAMBDA_DEPLOY_20261009.md`
      @daf6309661, read whole; the sections R1, PACKAGE members -- measured, and GOLD FIRST bind.
    - CTO half: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_SECHIST_GOLD_LAMBDA_DEPLOY_20261009.md` (msg 2981). Its condition 1: the
      rollback is code + policy only, with no S3 delete.
    Dry run DELTA=0: `GOLD_PIN_DRYRUN_DIFF_20261009.md` @9842e9a0d5.
  </context>

  <steps>
    1. Open the ledger entry (`.tools/deploy_ledger.py open`) with legs L1 package, L2 IAM + apply, L3 first scheduled run (L3 is the
       issuer's read). Before anything else, read the function's current `CodeSha256` and the role's current policy, and write both into
       the entry: they are the rollback.
    2. L1, the package: add to `PACKAGE` in `infra/aws/lambda/etfs-pipeline/etf-positioning-producer/build_package.py` these 11 members,
       each at the same relative path as its source:
       - `etf_history_gap_record.py` (from `data/etfs/scripts/silver/`);
       - `lib/opal_naming.py`;
       - `infra/logic/registry/{systems,scopes,tiers,resources,exemptions,remediations,reporting_policies}.json`;
       - `org/standards/NAMING_SCHEMA.json`;
       - `data/firm_registry.json`.
       This follows the `mdpf-gold-lambda` pattern in its `build_package.py:184-201`. Build with `--pin 09b6a7d580`.
    3. The gate before apply: unzip the package into an empty directory, put only that directory and the calendar layer on the path, and
       run `import etf_positioning_gold, etf_history_gap_record; print(etf_history_gap_record.record_address('2026-10-12'))`.
       - It must print `s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=2026-10-12/gap_record.json`.
       - Write the output to `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.7.0_AE_CloudOps~SH1/evidence/gold_import_smoke_20261009.txt`.
       - `import-closure-check.py` is NOT this gate, because it grades top-level imports only.
    4. L2, IAM + apply: add ONE statement to `etf-positioning-producer-role`:
       - `s3:PutObject` on `arn:aws:s3:::opal-data-etfs/bloomberg/etfs/silver/history_gaps/*`, in
         `infra/aws/terraform/etfs-positioning/` (`producer-lambda.tf` / `main.tf`).
       - `safe-apply`, never a bare apply or `update-function-code`.
       - The plan must show the code change and that one statement only. Any other IAM change is a STOP: roll back and report.
       - Save the plan summary to the evidence folder as `gold_plan_20261009.txt`.
    5. Step F: report the grant after the fact to `0.0.0_AB_MSTR~DELL1` by name and what it grants.
    6. Close L1 and L2 and report. L3 is the issuer's: the first scheduled gold run, the gap record at `record_address(<as_of>)`, no
       `WRITE FAILED` or `ImportError`, and the served page diffed against the prior day (CTO condition 2).
  </steps>

  <rollback>
    Re-apply the prior `CodeSha256` and the prior role policy (both read at step 1). Do NOT delete `history_gaps` objects: the
    pre-pin code has no reader, so they are inert (CTO half condition 1).
  </rollback>

  <rules>
    - The three dell1 IAM-parity conditions ride this order (AC3-AC5).
    - The cot-satellites-characteristics-producer also vendors `etf_positioning_gold.py`. It is NOT rebuilt here.
    - Client-data bounds (standing):
      - never read, search, copy or `git show` any `org/**/W73_S*_EVIDENCE.json`, commits 1ba8eafcda / f5645bb6e9, the ADVI_COTBKF
        ~74/~66/~70 cottonwood manifests, the IRPT_DASHBD tie-out files, or anything under
        `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/`;
      - search only inside the paths named here.
  </rules>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the function's schedule is unchanged; only its code and one policy statement move.
comp-iam: RUN -- CVO measured the role grants PutObject on gold/* only (REMEDIATION_v3 D1-W14-S1); the one added statement is R1's; the plan is the gate on any other change.
comp-adversary: RUN -- a package missing the lazily-imported gap module (step 3 smoke, with a negative control measured: 3 members -> ImportError @81488fde3d); a plan carrying extra IAM (step 4 STOP); a moving pin (the builder refuses non-hex pins); served drift (the dry run diffed DELTA=0 @9842e9a0d5). BLIND: the book table and the publisher stage, which the dry run did not execute; the L3 read covers them.
risk: WORLD.
</preflight>

<proof_of_spec>
  <criterion id="AC1" cell_refs="SH-t-15"><invocation>grep -c 'history_gaps/as_of=2026-10-12/gap_record.json' org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.7.0_AE_CloudOps~SH1/evidence/gold_import_smoke_20261009.txt</invocation><expect>1</expect></criterion>
  <criterion id="AC2" cell_refs="SH-t-15" judgment="true"/><!-- the plan shows the code change and exactly ONE added IAM statement (R1), nothing else -->
  <criterion id="AC3" cell_refs="SH-t-15" judgment="true"/><!-- a send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST -->
  <criterion id="AC4" cell_refs="SH-t-15" judgment="true"/><!-- every send to mdpf-daily-runner is reported after the fact with its command id and purpose -->
  <criterion id="AC5" cell_refs="SH-t-15" judgment="true"/><!-- 49 Financial data never goes into another firm's tree -->
</proof_of_spec>

  <report>
    One message to 2.0.0_SA_COO~H1 when L1 and L2 are closed: the new `CodeSha256`, the plan summary path, the smoke output line, the
    ledger entry id, and the Step F report's message id.
  </report>
</task_order>
