<task_order>
  <metadata>
    <id>ETFS_RIVALS.TO-APPLY-R31.rivalfunds-packages-deploy-dell1</id>
    <issued_by>2.0.0_SA_COO~RV</issued_by>
    <issued_to>0.7.0_AE_CloudOps~RV1</issued_to>
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
    APPLIER: `0.7.0_AE_CloudOps~RV1` (the COO half names ~DELL1; the CTO half's AMENDMENT 1 @ledger/NEVER_WIDEN_R31_DEPLOY_CTO_HALF.md names ~RV1 as the applier, msg 6284: ~DELL1 holds another project's order, one project per Tier-2 seat). Same pin, plan, conditions and rollback.
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
    Applier `0.7.0_AE_CloudOps~RV1`, dell1, `box/dell1`. LIVE AND VERIFIED 21:56:46Z-21:58:21Z on 2026-10-15 (the apply itself 21:57:52Z-21:58:16Z by LastModified), about 12h47m before the
    2026-10-16 10:45Z deadline and outside 10:55Z-11:15Z and 12:55Z-13:15Z. The order, the COO half (sha256 3def65d3...6f18 read on disk equal to the CTO half's binding) and the CTO half with
    Amendment 1 were read in full first. The first run on the pin is the 2026-10-16 11:00Z chain and the 13:00Z sweep, read by the issuer (L2).

    STOP 1 (pin), read in `C:/tmp/rv-r31-dell1`:
      git rev-parse HEAD = 34b2ab63516b8028e5185e1b259ee7b7a0864121; porcelain lines = 0
      gold_trade_schedule.py 928331c8de7fde907d1cdf7a66f42a4be95ac51a; price_series.py 4c932a816434a702648f13da0c6530d02e11d3fa; ai_accounts.py 917e2fa12e0b2cde80d4d29d7ab864d1a9ef9fb6;
      ai_client.py 2b45ec0ac8c423ae6801c1370b8045f26fa52941; render.py fda4ab160bb72d1f6e5b20ddf3a9df37997354fa; dramatic_move.py 37397a1057439b90aa2a9b759beb159375e91673
      (6 of 6 equal the order's ids, read by `git rev-parse HEAD:<path>`). `git diff --stat ea0e5025ac 34b2ab6351`: 4 files, +61 -7. No later commit deployed: the pin tree is the scratch commit.
      rollback tree `C:/tmp/rv-r31-rollback` HEAD = ea0e5025ac6422697c4c43003d0a384dee267980, 0 porcelain lines (KEPT until L2 closes; NOT initialised or packaged).
    Step 2 control (every packaged file vs `git cat-file blob 34b2ab6351:<path>`, raw bytes, never `git diff`; negative control = one flipped byte, caught): 480 of 480 identical,
      0 different, 0 without a blob, 0 unmapped. 480 equals the round-30 act's count (no staged path added). Grader: scratchpad `r31_prepackage_control.py`.

    STOP 3 (graded per attribute from `terraform show -json C:/tmp/rv_apply_r31.tfplan`; all 46 attributes compared by value, computed only where `after_unknown` carries a true):
      resource_changes 45 = 40 no-op + 5 update; 0 create, 0 delete, 0 replace -> `Plan: 0 to add, 5 to change, 0 to destroy`
      each of the five `aws_lambda_function.stage[...]`: value-changed = [source_code_hash] ONLY; computed = [last_modified] ONLY; `environment` before == after on all five
      STOP 3 RESULT: BRANCH A, 0 failures (negative control: a doctored memory_size is caught). Evidence: `C:/tmp/rv-r31-evidence/plan.json`.

    Environment KEY sets (names only), BEFORE and AFTER identical on all five; no RIVALFUNDS_AI_MODEL key; memory 3008 and timeout (900/300/900/900/900) unchanged:
      etfs-rivalfunds-daily-lambda: BD_SERP_ZONE, RIVALFUNDS_AI_ENABLE, RIVALFUNDS_OPENAI_SECRET, RIVALFUNDS_SERP_SECRET
      the other four: none

    BEFORE -> AFTER (CodeSha256 first 12 chars; LastModified), every function Active / Successful / 3008 MB. The five BEFORE hashes equal the round-30 AFTER hashes, so no third writer
    moved a function between the two applies:
      etfs-rivalfunds-daily-lambda            HpIx/ubb7B8E 2026-10-14T14:53:21Z -> Cz/7q9b3P5m/ 2026-10-15T21:57:58Z
      etfs-rivalfunds-fetch-holdings-lambda   CEueU5Imxn+7 2026-10-14T14:53:15Z -> SZW7y4HPxrlE 2026-10-15T21:58:10Z
      rivalfunds-build-silver-lambda          z0rNQLPGgJjn 2026-10-14T14:53:40Z -> dtnfEcYe6F9U 2026-10-15T21:58:16Z
      rivalfunds-build-canonical-shape-lambda VGlInUCe62NA 2026-10-14T14:53:34Z -> VBCqhQXeKkr8 2026-10-15T21:57:52Z
      rivalfunds-publish-page-lambda          lBCs6sHKOTht 2026-10-14T14:53:28Z -> dtkAjlcUTGe8 2026-10-15T21:58:04Z
      full AFTER values (base64): daily Cz/7q9b3P5m/fsnxbx6sxEAzBeAnTYZTpjEaPz6MHQQ=; fetch-holdings SZW7y4HPxrlETW9MShhuyoQGWjASw2q+WHIRJ01GRJ8=; build-silver
      dtnfEcYe6F9UflRR0pNPNpXyxr6qxWAsk74D5vY1ua8=; build-canonical-shape VBCqhQXeKkr8AVnGTLJLu1asUWqBQgmHuRt0ZzPUVPk=; publish-page dtkAjlcUTGe8Sck1pX9T72QmWKI4HxDl89LwM6jeFBY=

    Act: `.tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-rivalfunds apply C:/tmp/rv_apply_r31.tfplan` from `C:/tmp/rv-r31-dell1`, invoked 21:56:46Z, returned 21:58:21Z: comp-tagauthz
    gate PASSED, tombstone-gate CLEAN (0 creates vs 7), `Apply complete! Resources: 0 added, 5 changed, 0 destroyed.` rc=0. HALTGT is not cited; the pre-apply inbox read was the broker's
    `get_delivery_state` on the full lane serial: 10 rows, 10 READ, 0 unread.

    AC1: `python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round31/r31_deploy_check.py C:/tmp/rv-r31-dell1`
      5 built zips; five CodeSha256 each = a built zip; daily env = the four keys; daily role secretsmanager statements 2, one on exactly `...find-insure/bright-data/api-key-7ojPkd`;
      dramatic_move.py / render.py / ai_accounts.py / ai_client.py / gold_trade_schedule.py / price_series.py each held by 5 of 5 zips, 0 not the pin's bytes
      R31 DEPLOY RESULT: PASS 0 failures
    AC2: `cd C:/tmp/rv-r31-dell1/data/etfs/scripts; python -m pytest -q -p no:cacheprovider <ya1, yb1, xe3 check files>` -> 12 passed in 1.27s
    Second oracle: live CodeSha256 == the plan's declared `source_code_hash`, APPLIED==GRADED 5 of 5.
    Re-plan at the same pin (`-detailed-exitcode`): rc=0, `No changes. Your infrastructure matches the configuration.`
    Ledger: slug `etfs-rivalfunds-r31-rv1-20261015` (`org/critical_paths/change_management/20261015T2156Z_etfs-rivalfunds-r31-rv1-20261015_deploy_completion.md`), opened 21:56Z before the
      apply; L1 CLOSED with the proof above; L2 (the 2026-10-16 11:00Z chain and 13:00Z sweep, with C7: the first sweep's token usage beside the 10-15 sweep's) is the issuer's and OPEN;
      entry HELD external on that read, re-read date 2026-10-17.

    Not done, by the order's rules: no function invoked, no test event, no search, no OpenAI call, no S3 write, no secret value read. Row ETFS_RIVALS-D1-S16 untouched (the issuer's).
    Trees kept until L2 closes: `C:/tmp/rv-r31-dell1` (pin, built zips, initialised; AC1 reads those zips) and `C:/tmp/rv-r31-rollback` (ea0e5025ac; a rollback needs `terraform init` and
    the packager run in it first, then plan, then safe-apply; plan 0/5/0). The round-30 trees `C:/tmp/rv-r30-dell1` and `C:/tmp/rv-r30-rollback` (ledger CLOSED) are left in place; the COO half
    says they may be removed and this order does not name that act.

    Push state: filled in the broker message to the issuer from an `ls-remote` read at send time. This box does not push `box/dell1`; `box-sync` carries it.
  </report>
</task_order>
