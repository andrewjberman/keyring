<task_order>
  <metadata>
    <id>ETFS_RIVALS.TO-APPLY-R31.rivalfunds-packages-deploy-dell1</id>
    <issued_by>2.0.0_SA_COO~RV</issued_by>
    <issued_to>0.7.0_AE_CloudOps~DELL1</issued_to>
    <date>2026-10-15</date>
    <status>pending</status>
    <project_code>ETFS_RIVALS</project_code>
  </metadata>

<direct_act>true</direct_act>
<!-- Round-less by design: an executor apply order, not a cell. The two round-31 cells (RIV-ya-1, RIV-yb-1) are merged and complete; this is their apply leg under a signed pair, so that row ETFS_RIVALS-D1-S16 can disarm and the CVO's J1 read of RIV-yb-1 has a sweep the deployed code writes. It adds no cell. -->
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc> (round 31): the apply leg of cells RIV-ya-1 and RIV-yb-1 (both merged on box/dell1; pin 34b2ab6351).
<owned_cells>RIV-ya-1 RIV-yb-1</owned_cells>
</decomp_ref>

  <objective>
    Deploy pin 34b2ab6351 to the rivalfunds stack: the five code packages and NOTHING else. The plan is exactly 0 to add, 5 to change, 0 to destroy: no environment key (in particular NO RIVALFUNDS_AI_MODEL),
    no IAM statement, no schedule, memory or timeout moves. Complete before 2026-10-16 10:45Z, so the first scheduled chain on the pin is 2026-10-16 11:00Z and the first sweep 13:00Z.
  </objective>

  <context>
    BOTH HALVES SIGNED; read both in full before acting:
    - COO half `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round31/NEVER_WIDEN_HALF_COO_R31_DEPLOY.md` @72c4185226 (sha256 3def65d313cb33d97089fced974175b5b4ea5ad315721a846061902eff106f18);
    - CTO half `org/missions/D5/ETFS/ETFS_RIVALS/ledger/NEVER_WIDEN_R31_DEPLOY_CTO_HALF.md` @1081824c7a (SIGNED, with C7).
    The pin is the scratch branch `pin-ETFS_RIVALS-r31` at 34b2ab6351 on this box: the last applied pin ea0e5025ac (round 30) plus exactly
    `data/etfs/scripts/rivalfunds/{gold_trade_schedule,price_series,ai_accounts,ai_client}.py` at git blob ids 928331c8de7fde907d1cdf7a66f42a4be95ac51a, 4c932a816434a702648f13da0c6530d02e11d3fa,
    917e2fa12e0b2cde80d4d29d7ab864d1a9ef9fb6 and 2b45ec0ac8c423ae6801c1370b8045f26fa52941 (render.py stays fda4ab160bb72d1f6e5b20ddf3a9df37997354fa; dramatic_move.py 37397a1057439b90aa2a9b759beb159375e91673).
    HEAD of box/dell1 is NOT the pin and must not be deployed: it carries RIV-xe-1 (`enrichment_bloomberg.py`) and RIV-xf-1 (`peer_groups.json`, `bbg_budget.json`), site Z's producer deploy.
    Your model is the round-30 apply (order `ETFS_RIVALS.TO-APPLY-R30.rivalfunds-packages-deploy-dell1.md`, its report): same root, same packager, package then plan in one tree.
    The issuer read the suite in a full checkout of this pin (`C:/tmp/rv-r31-pin-dry`, 71,147 files, 0 porcelain lines): `rivalfunds/tests` 1011 passed, 6 skipped, 1 failed (`test_r6ap1_ai_stage.py::test_rest_client_request_shape`:
    the test that expects a temperature key for a non-gpt-5 model; tests are not packaged and the pin carries no test file; HEAD updates it) and the three round checks 12 passed. That tree is already removed; make your own at STOP 1.
    The ROLLBACK is a re-apply at ea0e5025ac: make that tree at STOP 1 and keep it until L2 closes.
  </context>

  <steps>
    1. STOP 1 (pin): `git worktree add --detach C:/tmp/rv-r31-dell1 34b2ab6351`; `git rev-parse HEAD` there starts `34b2ab6351`, 0 porcelain lines, and the six blob ids above read by
       `git rev-parse HEAD:<path>`. A later commit only if `git diff --stat 34b2ab6351 <commit> --` over the STAGED paths of `infra/aws/lambda/etfs-pipeline/rivalfunds_package.py`,
       `infra/aws/lambda/etfs-pipeline/` and `infra/aws/terraform/etfs-rivalfunds/` (tests left out) prints nothing. Also `git worktree add --detach C:/tmp/rv-r31-rollback ea0e5025ac`.
    2. Package, then plan with `-out C:/tmp/rv_apply_r31.tfplan` from the root in the pin tree. Pre-package control: every shipped file compared RAW against its committed blob
       (`git cat-file blob`, never `git diff`), with a flipped-byte negative control.
    3. STOP 3 (plan, read per attribute from `terraform show -json`, every attribute compared by value, a computed one counted only where `after_unknown` carries a true): `0 to add, 5 to change, 0 to destroy`:
       the five `aws_lambda_function.stage`, attributes `source_code_hash` and `last_modified` only. Anything else (an `environment` change, a policy, a role, a schedule, memory, timeout): apply NOTHING and report.
    4. ENV: print the five functions' environment KEY sets before (names only); the daily one is the four keys of the round-29 act.
    5. WINDOWS: never inside 10:55Z-11:15Z or 12:55Z-13:15Z. Open the NEVER-2 ledger entry with two legs: L1 the activation (yours); L2 the issuer's read of the 2026-10-16 11:00Z chain and
       13:00Z sweep (the issuer closes it). BEFORE: the five `CodeSha256` and `LastModified`.
    6. Apply the saved plan through `.tools/safe-apply.sh` from `C:/tmp/rv-r31-dell1`.
    7. AFTER: AC1; AC2; the five functions' environment key sets unchanged; a re-plan at the same pin reads no changes. Close L1.
  </steps>

  <rules>
    Invoke no function; send no test event; make no search; make no OpenAI call; write no S3 object; read no secret value. Write only your deliverables folder, the ledger entry and its sentinel, and this order's
    report. A lane refusal is reported verbatim; take no override. Tell `2.0.0_SA_COO~RV` when L1 is closed, with the five before and after `CodeSha256` values.
  </rules>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule changes; the first run on the pin is the existing 2026-10-16 11:00Z chain; step 5's windows keep the apply clear of both scheduled runs.
comp-iam: DECLARED-NOT-APPLICABLE no role or policy changes (plan 0/5/0, packages only); AC1 re-reads the daily role's two secretsmanager statements unchanged.
comp-adversary: RUN -- a pin that is HEAD (STOP 1: the pin is a scratch branch commit; the six blob ids); an environment or policy change riding the plan (STOP 3 per attribute, AC1 limb 2, no RIVALFUNDS_AI_MODEL key); an apply inside a scheduled run (step 5); a package whose files differ from the pin's (AC1 limb 3 reads the zips' bytes). BLIND: the AI stage's accepted request on the first run (read by the issuer at L2, with the token usage, CTO C7).
lane: CloudOps applies under both signed halves (COO @72c4185226, CTO NEVER_WIDEN_R31_DEPLOY_CTO_HALF.md @1081824c7a).
</preflight>

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ya-1 RIV-yb-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round31/r31_deploy_check.py C:/tmp/rv-r31-dell1</invocation><expect>R31 DEPLOY RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-ya-1 RIV-yb-1"><invocation>cd C:/tmp/rv-r31-dell1/data/etfs/scripts; python -m pytest -q -p no:cacheprovider C:/dev/ajb_workspace/org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round31/checks/ya1_bloomberg_wins_check.py C:/dev/ajb_workspace/org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round31/checks/yb1_model_gpt6_astra_check.py C:/dev/ajb_workspace/org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/checks/xe3_union_reader_check.py</invocation><expect>12 passed</expect></criterion>
</proof_of_spec>

  <report>
    (the applier writes here)
  </report>
</task_order>
