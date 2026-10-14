<task_order>
  <metadata>
    <id>ETFS_RIVALS.TO-APPLY-R30.rivalfunds-packages-deploy-dell1</id>
    <issued_by>2.0.0_SA_COO~V1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~DELL1</issued_to>
    <date>2026-10-14</date>
    <status>pending</status>
    <project_code>ETFS_RIVALS</project_code>
  </metadata>

<direct_act>true</direct_act>
<!-- Round-less by design: an executor apply order, not a cell. The three round-30 cells (RIV-xa-2, xc-2, xe-3) are merged and complete; this is their apply leg under a signed pair, so that the CVO's two J1 reads have a page the deployed code publishes and RIV-xe-2 has its deployed reader. It adds no cell. -->
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc> (round 30): the apply leg of cells RIV-xa-2, RIV-xc-2 and RIV-xe-3 (all merged on box/dell1; pin ea0e5025ac).
<owned_cells>RIV-xa-2 RIV-xc-2 RIV-xe-3</owned_cells>
</decomp_ref>

  <objective>
    Deploy pin ea0e5025ac to the rivalfunds stack: the five code packages and NOTHING else. The plan is exactly 0 to add, 5 to change, 0 to destroy: no environment key, no IAM
    statement, no schedule, memory or timeout moves. Complete before 2026-10-15 10:45Z, so the first scheduled chain on the pin is 2026-10-15 11:00Z.
  </objective>

  <context>
    BOTH HALVES SIGNED; read both in full before acting:
    - COO half `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/NEVER_WIDEN_HALF_COO_R30_DEPLOY.md` @77af4ef06f;
    - CTO half `org/missions/D5/ETFS/ETFS_RIVALS/ledger/NEVER_WIDEN_R30_DEPLOY_CTO_HALF.md @35d1f02bc3 (SIGNED, with condition C1)` (the window ruled; plan exactly 0/5/0, else STOP).
    The pin is the scratch branch `pin-ETFS_RIVALS-r30` at ea0e5025ac on this box: the last applied pin de3c6bf211 (round 29) plus exactly
    `data/etfs/scripts/rivalfunds/{ai_accounts,render,gold_trade_schedule}.py` at git blob ids 724b9ca5b1880bf47c45c9f9f5f0da967d862341, fda4ab160bb72d1f6e5b20ddf3a9df37997354fa and
    63c7f134d17a89a5e84806b104f3debd41a59941 (dramatic_move.py stays 37397a1057439b90aa2a9b759beb159375e91673). HEAD of box/dell1 is NOT the pin and must not be deployed: it carries
    RIV-xe-1 and RIV-xf-1 (site Z's producer deploy) and other seats' changes to staged paths.
    Your model is the round-29 apply (order `ETFS_RIVALS.TO-APPLY-R29.rivalfunds-packages-deploy-dell1.md`, its report): same root, same packager, package then plan in one tree.
    The CTO's condition C1 binds the issuer, not this order: row ETFS_RIVALS-D1-S16 is the issuer's (detect-and-void each tick); this order does not touch it. The dell1 restart tonight (21:00Z) is outside both fire windows: apply before it, or after the seat's re-seat.
    The ROLLBACK is a re-apply at de3c6bf211: make that tree at STOP 1 and keep it until L2 closes.
  </context>

  <steps>
    1. STOP 1 (pin): `git worktree add --detach C:/tmp/rv-r30-dell1 ea0e5025ac`; `git rev-parse HEAD` there starts `ea0e5025ac`, 0 porcelain lines, and the four blob ids above read by
       `git rev-parse HEAD:<path>`. A later commit only if `git diff --stat ea0e5025ac <commit> --` over the STAGED paths of `infra/aws/lambda/etfs-pipeline/rivalfunds_package.py`,
       `infra/aws/lambda/etfs-pipeline/` and `infra/aws/terraform/etfs-rivalfunds/` (tests left out) prints nothing. Also `git worktree add --detach C:/tmp/rv-r30-rollback de3c6bf211`.
    2. Package, then plan with `-out C:/tmp/rv_apply_r30.tfplan` from the root in the pin tree. Pre-package control: every shipped file compared RAW against its committed blob
       (`git cat-file blob`, never `git diff`).
    3. STOP 3 (plan, read per attribute from `terraform show -json`): `0 to add, 5 to change, 0 to destroy`: the five `aws_lambda_function.stage`, attributes `source_code_hash` and
       `last_modified` only. Anything else (an `environment` change, a policy, a role, a schedule, memory, timeout): apply NOTHING and report.
    4. ENV: print the five functions' environment KEY sets before (names only); the daily one is the four keys of the round-29 act.
    5. WINDOWS: never inside 10:55Z-11:15Z or 12:55Z-13:15Z. Open the NEVER-2 ledger entry with two legs: L1 the activation (yours); L2 this seat's read of the 2026-10-15 11:00Z chain and
       13:00Z sweep (the issuer closes it). BEFORE: the five `CodeSha256` and `LastModified`.
    6. Apply the saved plan through `.tools/safe-apply.sh` from `C:/tmp/rv-r30-dell1`.
    7. AFTER: AC1; the five functions' environment key sets unchanged; a re-plan at the same pin reads no changes. Close L1.
  </steps>

  <rules>
    Invoke no function; send no test event; make no search; write no S3 object; read no secret value. Write only your deliverables folder, the ledger entry and its sentinel, and this order's
    report. A lane refusal is reported verbatim; take no override. Tell `2.0.0_SA_COO~V1` when L1 is closed, with the five before and after `CodeSha256` values.
  </rules>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule changes; the first run on the pin is the existing 11:00Z chain; step 5's windows keep the apply clear of both scheduled runs.
comp-iam: DECLARED-NOT-APPLICABLE no role or policy changes (plan 0/5/0, packages only); AC1 re-reads the daily role's two secretsmanager statements unchanged.
comp-adversary: RUN -- a pin that is HEAD (STOP 1: the pin is a scratch branch commit; the four blob ids); an environment or policy change riding the plan (STOP 3 per attribute, AC1 limb 2); an apply inside a scheduled run (step 5); a package whose files differ from the pin's (AC1 limb 3 reads the zips' bytes). BLIND: the G5 stage's output on the first run (read by the issuer at L2).
lane: CloudOps applies under both signed halves (COO @77af4ef06f, CTO NEVER_WIDEN_R30_DEPLOY_CTO_HALF.md @35d1f02bc3).
</preflight>

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-xa-2 RIV-xc-2 RIV-xe-3"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/r30_deploy_check.py C:/tmp/rv-r30-dell1</invocation><expect>R30 DEPLOY RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

  <report>
    Applier `0.7.0_AE_CloudOps~DELL1`, dell1, `box/dell1`. LIVE AND VERIFIED 14:53:15Z-14:53:40Z on 2026-10-14. Start: msg 5613 (14:45Z, acked READ 14:45:17Z); the order and both
    halves read in full first (COO @77af4ef06f, CTO half @35d1f02bc3 with C1, which binds the issuer). The first run on the pin is the 2026-10-15 11:00Z chain, read by the
    issuer (L2) and the CVO (the two J1 reads), not by this order.

    STOP 1 (pin), as read in `C:/tmp/rv-r30-dell1`:
      git rev-parse HEAD = ea0e5025ac6422697c4c43003d0a384dee267980; porcelain lines = 0
      ai_accounts.py 724b9ca5b1880bf47c45c9f9f5f0da967d862341; render.py fda4ab160bb72d1f6e5b20ddf3a9df37997354fa;
      gold_trade_schedule.py 63c7f134d17a89a5e84806b104f3debd41a59941; dramatic_move.py 37397a1057439b90aa2a9b759beb159375e91673  (all four equal the order's ids)
      No later commit deployed: the pin tree is the scratch commit itself, so no staged-path diff was owed.
      rollback tree `C:/tmp/rv-r30-rollback` HEAD = de3c6bf211f806345d6e6930348795cbe7f755ce, 0 porcelain lines (KEPT until L2 closes; NOT initialised or packaged)
    Step 2 control (raw bytes vs `git cat-file blob ea0e5025ac:<path>`, negative control = one flipped byte, caught): packaged output (5 lambdas, wrapper + 8 staged
      sources) 480 of 480 identical, 0 different or missing. 480 equals the round-29 act's count (no staged path added).

    STOP 3 (graded per attribute from `terraform show -json C:/tmp/rv_apply_r30.tfplan`):
      resource_changes 45 = 40 no-op + 5 update; 0 create, 0 delete, 0 replace -> `Plan: 0 to add, 5 to change, 0 to destroy`
      each of the five `aws_lambda_function.stage[...]`: attributes different = [last_modified, source_code_hash] ONLY
      environment before==after on all five; memory_size and timeout equal; role, layers, handler, runtime equal
      STOP 3 RESULT: BRANCH A, 0 failures (control: a doctored memory_size is caught).
      My first grader run FAILED on a defect of its own, not of the plan: it counted an all-false `after_unknown` container (`architectures: [false]`) as unknown. I fixed it to
      count a value unknown only if it contains a true, kept the doctored control, and re-ran: the plan text itself showed only last_modified and source_code_hash all along.

    Environment KEY sets (names only), BEFORE and AFTER identical on all five:
      etfs-rivalfunds-daily-lambda: BD_SERP_ZONE, RIVALFUNDS_AI_ENABLE, RIVALFUNDS_OPENAI_SECRET, RIVALFUNDS_SERP_SECRET
      the other four: none

    BEFORE -> AFTER (CodeSha256 first 12 chars; LastModified), every function Active / Successful / 3008 MB. The five BEFORE hashes equal the round-29 AFTER hashes, so no third
    writer moved a function between the two applies:
      etfs-rivalfunds-daily-lambda            GUBCtyI9YHiQ 2026-10-13T13:59:36Z -> HpIx/ubb7B8E 2026-10-14T14:53:21Z
      etfs-rivalfunds-fetch-holdings-lambda   ra7H9s3ZuRQ5 2026-10-13T13:59:42Z -> CEueU5Imxn+7 2026-10-14T14:53:15Z
      rivalfunds-build-silver-lambda          ixXBp+Ru7zir 2026-10-13T13:59:48Z -> z0rNQLPGgJjn 2026-10-14T14:53:40Z
      rivalfunds-build-canonical-shape-lambda UcHilFR4q0hN 2026-10-13T13:59:29Z -> VGlInUCe62NA 2026-10-14T14:53:34Z
      rivalfunds-publish-page-lambda          LfekOrASXAyV 2026-10-13T13:59:23Z -> lBCs6sHKOTht 2026-10-14T14:53:28Z

    Act: `.tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-rivalfunds apply C:/tmp/rv_apply_r30.tfplan` from `C:/tmp/rv-r30-dell1`, invoked 14:52:47Z, returned 14:53:44Z
    (outside 10:55Z-11:15Z and 12:55Z-13:15Z; about 1192 min to the 2026-10-15 10:45Z deadline): comp-tagauthz gate PASSED, tombstone-gate CLEAN (0 creates vs 7),
    `Apply complete! Resources: 0 added, 5 changed, 0 destroyed.` rc=0. HALTGT is not cited; the pre-apply inbox read was the broker's `get_delivery_state` on the full lane
    serial (1 row, msg 5613, READ, 0 unread).

    AC1: `python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/r30_deploy_check.py C:/tmp/rv-r30-dell1`
      5 built zips; five CodeSha256 each = a built zip; daily env = the four keys; daily role secretsmanager statements 2, one on exactly `...find-insure/bright-data/api-key-7ojPkd`;
      dramatic_move.py / ai_accounts.py / render.py / gold_trade_schedule.py each held by 5 of 5 zips, 0 not the pin's bytes
      R30 DEPLOY RESULT: PASS 0 failures
    Second oracle: live CodeSha256 == the plan's declared `source_code_hash`, APPLIED==GRADED 5 of 5.
    Re-plan at the same pin (`-detailed-exitcode`): rc=0, `No changes. Your infrastructure matches the configuration.`
    Ledger: slug `etfs-rivalfunds-r30-dell1-20261014` (`org/critical_paths/change_management/20261014T1452Z_etfs-rivalfunds-r30-dell1-20261014_deploy_completion.md`), opened
      14:52Z before the apply; L1 CLOSED with the proof above; L2 (the 2026-10-15 11:00Z chain and 13:00Z sweep) is the issuer's and OPEN; entry HELD external on that read,
      re-read date 2026-10-16.

    Not done, by the order's rules: no function invoked, no test event, no search, no S3 write, no secret value read. C1 and row ETFS_RIVALS-D1-S16 untouched (the issuer's).
    Trees kept until L2 closes: `C:/tmp/rv-r30-dell1` (pin, built zips, initialised; AC1 reads those zips) and `C:/tmp/rv-r30-rollback` (de3c6bf211; a rollback needs
    `terraform init` and the packager run in it first, then plan, then safe-apply; plan 0/5/0). Tonight's 21:00Z dell1 restart does not touch either tree.

    Push state: filled in the broker message to the issuer from an `ls-remote` read at send time. This box does not push `box/dell1`; `box-sync` carries it.
  </report>
</task_order>
