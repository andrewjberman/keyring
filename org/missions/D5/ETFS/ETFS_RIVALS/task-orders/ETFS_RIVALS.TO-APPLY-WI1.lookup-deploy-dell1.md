<task_order>
  <metadata>
    <id>ETFS_RIVALS.TO-APPLY-WI1.lookup-deploy-dell1</id>
    <issued_by>2.0.0_SA_COO~V1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~RV1</issued_to>
    <date>2026-10-09</date>
    <status>pending</status>
    <project_code>ETFS_RIVALS</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- Round-less by design: an executor apply order, not a cell. CTO ruling ADDENDA 6-7 put the dramatic-move lookup live under its OWN pair after WS2/WS3; CTO half condition 11 required the void path first (RIV-wk-1, complete @b86feccfeb). It adds no cell. -->
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc> (workstream 3): the apply leg of cells RIV-wi-1, RIV-wj-1 and RIV-wk-1 (all merged on box/dell1; pin b86feccfeb).
<owned_cells>RIV-wi-1 RIV-wj-1 RIV-wk-1</owned_cells>
</decomp_ref>

  <objective>
    Deploy pin b86feccfeb to the rivalfunds stack: the five code packages, the daily Lambda's environment gaining
    `RIVALFUNDS_SERP_SECRET` and `BD_SERP_ZONE`, and the daily role gaining ONE statement `GetSerpSecret`
    (`secretsmanager:GetSecretValue` on exactly the `-7ojPkd` ARN). Complete before 2026-10-10 12:45Z.
  </objective>

  <context>
    BOTH HALVES SIGNED; read both in full before acting:
    - COO half `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round28/NEVER_WIDEN_HALF_COO_WI1_LOOKUP_DEPLOY.md`
      @194c4b3e7d with AMENDMENT 1 @fb2f737840 (the re-pin to b86feccfeb; conditions 1-7; the void rollback);
    - CTO half `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/1.0.0_SA_CTO~DELL1/round28/NEVER_WIDEN_HALF_CTO_WI1_LOOKUP_DEPLOY.md`
      @63bdddfbb9 (condition 11: the void path first -- met by RIV-wk-1).
    Your model is your own WS2/WS3 apply (report @8ad8b51083): same root, same packager, package then plan in one tree.
    Your WS2/WS3 tree `C:/tmp/rv-ws23-dell1` (pin b48273e3d0) is the ROLLBACK tree for this act: keep it.
  </context>

  <steps>
    1. STOP 1 (pin): `git worktree add --detach C:/tmp/rv-wi1-dell1 b86feccfeb`. A later commit only if `git diff --stat
       b86feccfeb <commit> --` over the eight `STAGED` paths, `infra/aws/lambda/etfs-pipeline/` and
       `infra/aws/terraform/etfs-rivalfunds/` (tests left out) prints nothing.
    2. Package, then plan with `-out C:/tmp/rv_apply_wi1.tfplan` from the root in that tree.
    3. STOP 3 (plan, read per attribute from `terraform show -json`): branch A is `0 to add, 6 to change, 0 to destroy`:
       the five `aws_lambda_function.stage` (package attributes; on the daily one also `environment` gaining exactly the
       two keys) and `aws_iam_role_policy.stage["etfs-rivalfunds-daily-lambda"]` gaining exactly the one statement.
       Anything else (any other policy, role, schedule, memory, timeout, a wildcard in that Resource): apply NOTHING and
       report.
    4. ENV: print the five functions' environment KEY sets before (names only).
    5. WINDOWS: never inside 10:55Z-11:15Z or 12:55Z-13:15Z. Open the NEVER-2 ledger entry with two legs: L1 the
       activation (yours); L2 this seat's read of the 2026-10-10 13:00Z sweep (the issuer closes it). BEFORE: the five
       `CodeSha256` and `LastModified`.
    6. Apply the saved plan through `.tools/safe-apply.sh` from `C:/tmp/rv-wi1-dell1`.
    7. AFTER: AC1; the four non-daily functions' environment key sets unchanged; a re-plan at the same pin reads no changes.
       Close L1.
  </steps>

  <rules>
    Invoke no function; send no test event; make no search; write no S3 object (the void CLI is NOT run by this order);
    read no secret value. Write only your deliverables folder, the ledger entry and its sentinel, and this order's report.
  </rules>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule changes; the lookup runs inside the existing 13:00Z sweep (run_dag); step 5's windows keep the apply clear of both scheduled runs.
comp-iam: RUN -- ONE inline statement added to the daily role: secretsmanager:GetSecretValue on exactly arn:aws:secretsmanager:us-east-1:313476888478:secret:find-insure/bright-data/api-key-7ojPkd (CTO ruling ADDENDUM 7, option (a)); denominator: 1 of 5 role policies changes, 0 roles added; read live at AC1 limb (3).
comp-adversary: RUN -- a wildcard or a second action riding the statement (STOP 3 and AC1 limb 3); an environment change on another function (step 4 and AC1 limb 2); a pin without the void path (STOP 1: b86feccfeb carries RIV-wk-1); an apply inside a scheduled run (step 5). BLIND: Bright Data's own availability at 13:00Z (a failed search is counted and never blocks publish).
lane: CloudOps applies under both signed halves (COO @194c4b3e7d + AMENDMENT 1 @fb2f737840, CTO @63bdddfbb9).
</preflight>

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-wi-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round28/wi1_deploy_check.py C:/tmp/rv-wi1-dell1</invocation><expect>WI1 DEPLOY RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-wi-1" judgment="true"/>
</proof_of_spec>

  <report>
    Once, in this section, committed, and the path + hash by broker message to `2.0.0_SA_COO~V1`:
    - STOP 1 and STOP 3 as read, with the plan per attribute;
    - the environment key sets before and after;
    - BEFORE and AFTER per function;
    - AC1's output, the re-plan line, the ledger slug and the L1 close;
    - the measured push state.
    AC2 (Tokio Marine adjusted on the served page; a name with no discontinuity makes 0 calls, read at the 2026-10-10
    13:00Z sweep) is the issuer's.
  </report>
</task_order>
