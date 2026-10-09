<task_order>
  <metadata>
    <id>ETFS_RIVALS.TO-APPLY-R28-aw1.rivalfunds-lambda-deploy-sitez</id>
    <issued_by>2.0.0_SA_COO~V1</issued_by>
    <!-- issued 2026-10-08 by 2.0.0_SA_COO~RV; re-issued by AMENDMENT 1 below to 2.0.0_SA_COO~V1 (dell1) -->

    <issued_to>0.7.0_AE_CloudOps~DELL1</issued_to>
    <!-- re-addressed by AMENDMENT 2 from 0.7.0_AE_CloudOps~Z (site Z) -->
    <date>2026-10-08</date>
    <status>pending</status>
    <project_code>ETFS_RIVALS</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- Round-less by design: an executor apply order, not a cell. ROUND_ANALYSIS.round22 ADDENDUM 7 @0820f6b0b7 (1.0.0_SA_CTO~Z R31) rules that round 28 closes on three paired acts, "none a cell", and R22 puts the apply on the executor seat. It adds no cell to round 28's issuance 222194aee0. -->
<risk>SERVED</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc> (round 28): the apply leg of cell `RIV-aw-1` (built and merged, tip a2283fc349; CTO ruling R31, ROUND_ANALYSIS.round22 ADDENDUM 7 @0820f6b0b7). Executor seat per R22 and Andrew-direct ~22:0xZ 2026-10-08 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_220xZ_ONE_LAPTOP_APPLIER_EXCEPTION_YES.md`).
<owned_cells>RIV-aw-1</owned_cells>
</decomp_ref>

  <amendment id="2" date="2026-10-09" by="2.0.0_SA_COO~V1">
    ASSIGNEE AND BOX: `0.7.0_AE_CloudOps~DELL1`, on dell1. Andrew ~03:5xZ via site Z, VERBATIM: "why is DELL1 sending
    deployment orders here? They should be able to run deploys on their own box"; ruled by 1.0.0_SA_CTO~DELL1 msg 1594
    (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_035xZ_DELL1_RUNS_OWN_DEPLOYS_SITE_BOUND_ONLY_TO_SITE_Z.md`
    @5084dd2328). Neither signed half names the applier ("the executor seat (R22)"), so both halves stand unchanged.
    WHAT CHANGES FOR A DELL1 APPLIER:
    - The deploy tree `C:/tmp/rv-r8` and its plan are on site Z and are NOT used. Cut your own detached tree on dell1:
      `git worktree add --detach C:/tmp/rv-r28-dell1 39889dd4d7` (the pin is in dell1's history), then steps 1-3 from it
      (STOP 1 pin read, package, plan with `-out C:/tmp/rv_apply28_dell1.tfplan`, STOP 3 plan read). Branch A is required:
      0 to add, 5 to change, 0 to destroy, the five `aws_lambda_function.stage`, package attributes only. Read the plan
      per attribute from `terraform show -json`, as executor report 1 did at site Z (45 resource_changes, 40 no-op, 5 update).
    - Do steps 1-3 NOW (before 10:30Z) and report the plan read to `2.0.0_SA_COO~V1` by broker message, path + hash.
    - Steps 4-6 run under AMENDMENT 1's conditional GO, unchanged: (a)-(d) read by you, inside 11:15Z-12:50Z. Your rollback
      tree: a second detached worktree at 325bd4e0f8, packaged and planned only if a rollback is ordered.
    - Reports: broker message to `2.0.0_SA_COO~V1` plus this file's report section, committed. AMENDMENT 1's relay through
      `0.0.0_AB_MSTR~Z` no longer applies.
  </amendment>

  <amendment id="1" date="2026-10-09" by="2.0.0_SA_COO~V1">
    ISSUER: the project moved to dell1 mid-round (record
    `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_015xZ_RIVALS_CORPUS_TO_DELL1_NOW_MID_ROUND.md`,
    re-placed @a0db38c8ae). The issuer is now `2.0.0_SA_COO~V1`; `2.0.0_SA_COO~RV` has no live process. Everywhere below,
    "2.0.0_SA_COO~RV" reads "2.0.0_SA_COO~V1".
    THE SECOND GO IS GIVEN HERE, CONDITIONALLY. This order file is the only carrier between dell1 and site Z (1.0.0_SA_CTO~DELL1
    msg 1440), and it travels by box-sync, so a GO sent after 11:00Z could miss the window. Step 4 therefore runs on 2026-10-09
    without a further word from the issuer when ALL of these hold, read by you before the apply:
    (a) the five rivalfunds Lambdas' runs of the 11:00Z chain have each logged a REPORT line in CloudWatch Logs (all five
        functions the chain invokes that day; print each REPORT line whole);
    (b) no REPORT shows Duration above 720,000 ms, and no run of the chain logged `Status: timeout`, a `Task timed out`,
        or an unhandled error;
    (c) the clock reads between 11:15Z and 12:50Z;
    (d) a re-plan at pin 39889dd4d7 in `C:/tmp/rv-r8` reads branch A again (0/5/0, package only), packaged first.
    Any of (a)-(d) not met: apply NOTHING, record which one in the report section, commit it, and tell `0.0.0_AB_MSTR~Z` the
    hash so it reaches `0.0.0_AB_MSTR~DELL1`. The issuer reads the REPORT lines from dell1 independently; a WITHDRAW, if
    sent, arrives as AMENDMENT 2 in this file and overrides this GO when it is on `box/sitez` before you apply.
    REPORTS go in this file's report section, committed and pushed, hash to `0.0.0_AB_MSTR~Z`. The L2 leg of the ledger entry
    you open in step 4 is read and closed by `2.0.0_SA_COO~V1`.
  </amendment>

  <objective>
    Deploy the rivalfunds code package at pin 39889dd4d7 to the five rivalfunds Lambdas (daily, fetch-holdings,
    build-silver, build-canonical-shape, publish-page). CODE ONLY: no IAM, schedule, memory, timeout or environment
    change. Prepare and read the plan NOW (steps 1-3). APPLY ONLY on 2026-10-09, between 11:15Z and 12:55Z, after
    `2.0.0_SA_COO~RV` sends GO (it reads the 11:00Z chain's REPORT lines first).
  </objective>

  <context>
    BOTH HALVES SIGNED; read both in full before acting:
    - COO half `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round28/NEVER_WIDEN_HALF_COO_R28_AW1_DEPLOY.md`
      @d3d6c3e73f (five conditions, branches A-C, rollback);
    - CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_ETFS_RIVALS_R28_AW1_DEPLOY_20261008.md` @a0ee589cc2.
    The model for every step is round 27's deploy, ledger
    `org/critical_paths/change_management/20261008T1449Z_etfs-rivalfunds-r27_deploy_completion.md`. The deploy tree is
    `C:/tmp/rv-r8` (a detached worktree, today at 325bd4e0f8, the live pin). The Terraform root is
    `infra/aws/terraform/etfs-rivalfunds/`. The packager is `python infra/aws/lambda/etfs-pipeline/rivalfunds_package.py`:
    it stages each Lambda's tree under `<tree>/.runtime/rivalfunds-build/`, and `archive_file` zips them at plan time, so
    the plan must be made in the same tree right after packaging. Between 325bd4e0f8 and 39889dd4d7, the root and the
    wrappers under `infra/aws/lambda/etfs-pipeline/` change 0 files.
  </context>

  <steps>
    1. STOP 1 (pin): in `C:/tmp/rv-r8`, `git checkout --detach 39889dd4d7`. If you take a later commit instead, `git diff
       --stat 39889dd4d7 <commit> --` over the seven `STAGED` paths of the packager, `infra/aws/lambda/etfs-pipeline/`
       and `infra/aws/terraform/etfs-rivalfunds/` (tests left out) must print nothing. Anything printed: STOP and report.
    2. Package, then plan with `-out C:/tmp/rv_apply28.tfplan` from the root in that tree.
    3. STOP 3 (plan): branch A is `0 to add, 5 to change, 0 to destroy`, the five `aws_lambda_function.stage`, with the
       package (`source_code_hash`, and `last_modified`) as the only changing attributes. Anything else: apply NOTHING.
       Either way, REPORT the plan as read to `2.0.0_SA_COO~RV` now, and wait for GO.
    4. On GO, inside 11:15Z-12:55Z on 2026-10-09 and never inside 10:55Z-11:15Z or 12:55Z-13:15Z, open the NEVER-2 ledger
       entry with two legs. L1 is the activation (yours). L2 is the verify, the 13:00Z sweep of 2026-10-09; the issuer
       reads it and closes it. BEFORE: the five functions' `CodeSha256` and `LastModified`.
    5. Apply the saved plan through `.tools/safe-apply.sh` from `C:/tmp/rv-r8`. If GO arrives after 12:50Z, apply
       nothing and report.
    6. AFTER: five `CodeSha256` moved, `LastModified` after the apply, `State Active`, `LastUpdateStatus Successful`,
       `MemorySize` unchanged (3008). A re-plan at the same pin reads no changes. Close L1.
  </steps>

  <rules>
    Invoke no function; send no test event; write no S3 object; set no environment variable (`RIVALFUNDS_HISTORY_OWED` and
    `RIVALFUNDS_AI_ENABLE` stay as they are). No untargeted change beyond the five functions. Write only your deliverables
    folder, the ledger entry and its sentinel, and this order's report section.
  </rules>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this act changes no schedule (package hash only; the 11:00Z chain and 13:00Z sweep rules are untouched).
comp-iam: DECLARED-NOT-APPLICABLE -- denominator: 0 files change under infra/aws/terraform/etfs-rivalfunds/ between the pins, and branch A requires no policy change in the plan; the applier is site Z's own applier seat.
comp-adversary: RUN -- a plan made before packaging (stale zip: package then plan in one tree, step 2); a pin carrying tc-1 (STOP 1: tc-1 is not merged); an apply inside a scheduled run (windows, step 4); an environment flip riding the deploy (rules). BLIND: the model's behaviour under the new prompts, which is graded at the 13:00Z sweep (J1, the COO half's branches B and C).
lane: CloudOps applies under both signed halves (COO @d3d6c3e73f, CTO @a0ee589cc2).
</preflight>

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-aw-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/aw-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-aw-1" judgment="true"/>
</proof_of_spec>

  <report>
    Report TWICE to 2.0.0_SA_COO~RV. First, at STOP 3: the pin and the STOP 1 read, AC1's line at the pin, and the plan as
    read. Second, when L1 closes, or at any STOP (name the step): the BEFORE and AFTER reads, the safe-apply line, the
    re-plan, THE HOUR THE DEPLOY WENT LIVE, the ledger entry's path, commit hashes and the measured push state. AC2 (the
    deploy is as both halves describe) is the issuer's and the CVO's to grade: do not mark it. Leave the status flip to
    the issuer.

    EXECUTOR REPORT 1 (STOP 3) -- `0.7.0_AE_CloudOps~Z`, 2026-10-08 ~22:53Z, sent to the issuer
    (`20261008T225339Z`, 1061 bytes delivered). Pin `39889dd4d7` taken exactly; STOP 1's six reads, AC1's
    `AC1 RESULT: PASS 0 failures` at the pin, and the plan read as BRANCH A (0 to add, 5 to change, 0 to
    destroy; package-only, verified per-attribute on `terraform show -json`, 45 resource_changes / 40 no-op /
    5 update) are recorded whole, with the audit script beside them, in
    `org/tier2_senior/0.7.0_AE_CloudOps~Z/deliverables/ETFS_RIVALS.TO-APPLY-R28-aw1_STOP3_PLAN_READ_20261008T2253Z.md`.
    APPLIED NOTHING. Steps 4-6 held for the issuer's second GO inside 2026-10-09 11:15Z-12:55Z. One note for
    the rollback: step 1 moved the deploy tree off `325bd4e0f8`, which the COO half's rollback describes as
    where that tree sits, so a rollback needs a re-checkout there first.

    EXECUTOR REPORT 2 (STOP 3, from dell1) -- `0.7.0_AE_CloudOps~DELL1`, 2026-10-09 ~04:15Z, under AMENDMENT 2.
    Both halves read in full at their pins first (COO @d3d6c3e73f, CTO @a0ee589cc2); AMENDMENT 2 read before 1.
    Own tree cut per AMENDMENT 2, `C:/tmp/rv-r28-dell1` detached at `39889dd4d7` exactly (HEAD
    39889dd4d71a67bc108fe15ae746ed7ab6cbe6f6); the site-Z tree `C:/tmp/rv-r8` was not used. STOP 1: the CTO half's
    four reads re-run here and all four reproduce, RIV-tc-1 `b0b65368fb` rc 1 (NOT in the pin). Packaged (rc 0, five
    trees), then planned in the same tree to `C:/tmp/rv_apply28_dell1.tfplan` (30,352 B, 0 errors). A fresh worktree
    has no `.terraform`, so the root needed one `terraform init` (aws v5.100.0, archive v2.8.1) -- named, not left
    implicit; no lock file committed. STOP 3 reads **BRANCH A**: `0 to add, 5 to change, 0 to destroy`, the five
    `aws_lambda_function.stage` and nothing else; `terraform show -json` gives 45 resource_changes / 40 no-op / 5
    update, matching executor report 1 exactly, and every one of the five declares `['last_modified',
    'source_code_hash']` only. Forbidden attributes proven equal, not assumed: `memory_size` 3008 unchanged on all
    five and NONE of role/timeout/environment/layers/architectures/handler/runtime/vpc_config/kms_key_arn/
    reserved_concurrent_executions differs; the daily Lambda's `environment` has before == after, so
    `RIVALFUNDS_AI_ENABLE` stays `1`. AC1 at the pin: `AC1 RESULT: PASS 0 failures`, exit 0. AC2 not marked.
    APPLIED NOTHING; steps 4-6 wait on AMENDMENT 1's (a)-(d) inside 11:15Z-12:50Z. Full read, with a correction to my
    own first per-attribute pass (I wrongly counted `after_unknown` as the change set and so produced a false FAIL;
    the authoritative set is `before != after`), in
    `org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/ETFS_RIVALS.TO-APPLY-R28-aw1_STOP3_PLAN_READ_DELL1_20261009T0415Z.md`.
    ONE ASK SURFACED THERE for the issuer before the window: 23 of the 239 tracked files under the packager's seven
    STAGED paths are `w/crlf` on dell1 (all data `.json`, no `eol=lf` attribute; the `.py` files are all `w/lf`), so
    this box's `source_code_hash` is not what an LF box building the same pin produces. It breaks neither STOP 1 nor
    branch A and is inert at runtime, but it means the shipped bytes are not the committed bytes. Take the plan as it
    stands, or have me re-cut with `-c core.autocrlf=false`, re-package and re-plan before 11:15Z.
  </report>
</task_order>
