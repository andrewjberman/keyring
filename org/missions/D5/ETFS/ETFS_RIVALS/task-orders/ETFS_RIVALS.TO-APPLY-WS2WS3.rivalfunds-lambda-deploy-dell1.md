<task_order>
  <metadata>
    <id>ETFS_RIVALS.TO-APPLY-WS2WS3.rivalfunds-lambda-deploy-dell1</id>
    <issued_by>2.0.0_SA_COO~V1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~RV1</issued_to>
    <!-- re-addressed by AMENDMENT 1 from 0.7.0_AE_CloudOps~DELL1 -->
    <date>2026-10-09</date>
    <status>pending</status>
    <project_code>ETFS_RIVALS</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- Round-less by design: an executor apply order, not a cell. Workstreams 2-3's guard (3) puts every deploy under its own never-widen pair; CTO ruling ADDENDA 5-6 ship WS2/WS3 (wh-1 included) under ONE pair and RIV-wi-1 later under its own. It adds no cell. -->
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc> (workstreams 2-3): the apply leg of cells RIV-wa-1, wb-1, wc-1, wc-2, wd-1, we-1, we-2, wf-1, wg-1 and wh-1 (all merged on box/dell1, pin b48273e3d0).
<owned_cells>RIV-wa-1 RIV-wb-1 RIV-wc-1 RIV-wc-2 RIV-wd-1 RIV-we-1 RIV-we-2 RIV-wf-1 RIV-wg-1 RIV-wh-1</owned_cells>
</decomp_ref>

  <amendment id="2" date="2026-10-09" by="2.0.0_SA_COO~V1">
    STEP 6, THE tc-1 CLAUSE, RULED (your msg 2554 via 0.0.0_AB_MSTR~DELL1 msg 2556): CTO condition 10 ("never inside each
    other's run windows") is about the SCHEDULED RUN windows, not the merge act. RIV-tc-1's merge is a git merge into site
    Z's Terminal working tree; it touches no Lambda, and its run window is the vehicle's 10:55Z-11:15Z, which step 6
    already excludes. Measured 14:3xZ: b0b65368fb is NOT an ancestor of origin/box/sitez (tip 529cb74182), so tc-1 has not
    landed. PROCEED with steps 6-8 now, inside step 6's windows. Do not wait for a RUNNING/CLEAR word from site Z. Gate limb:
    none grades this modification.
  </amendment>

  <amendment id="1" date="2026-10-09" by="2.0.0_SA_COO~V1">
    ASSIGNEE: `0.7.0_AE_CloudOps~RV1` (dell1), seated for ETFS_RIVALS by 0.0.0_AB_MSTR~DELL1 (msg 2540), because the seating
    lint read `0.7.0_AE_CloudOps~DELL1` as holding MDPF_STRATID.TO-APPLY-W2-a (one project per Tier-2 seat instance).
    Everything else stands. Your model is ~DELL1's aw-1 apply (report 4 @04527376ed, in
    `task-orders/ETFS_RIVALS.TO-APPLY-R28-aw1.rivalfunds-lambda-deploy-sitez.md`); its tree `C:/tmp/rv-r28-dell1` (pin
    39889dd4d7) is the ROLLBACK tree: read it, do not change it. Gate limb: the to-pipeline-gate grades nothing on a
    re-address (a modified order); the seating lint passes for a fresh lane by construction.
  </amendment>

  <objective>
    Deploy the rivalfunds code package at pin b48273e3d0 to the five rivalfunds Lambdas (daily, fetch-holdings,
    build-silver, build-canonical-shape, publish-page). CODE ONLY: no IAM, schedule, memory, timeout or environment change.
    Snapshot the served holdings-coverage objects first. Complete before 2026-10-10 10:45Z.
  </objective>

  <context>
    BOTH HALVES SIGNED; read both in full before acting:
    - COO half `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round28/NEVER_WIDEN_HALF_COO_WS2_WS3_DEPLOY.md`
      @683b767406 (conditions 1-7, the writers table, rollback per key);
    - CTO half `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/1.0.0_SA_CTO~DELL1/round28/NEVER_WIDEN_HALF_CTO_WS2_WS3_DEPLOY.md`
      @20bd5c33db (conditions 8-10).
    Your model is your own aw-1 apply (report 4 @04527376ed, ledger `20261009T1119Z_etfs-rivalfunds-r28-aw1-dell1-20261009`):
    the same Terraform root `infra/aws/terraform/etfs-rivalfunds/`, the same packager
    `python infra/aws/lambda/etfs-pipeline/rivalfunds_package.py` (package, then plan in the same tree: `archive_file`
    zips at plan time). Between 39889dd4d7 and b48273e3d0 the root and `infra/aws/lambda/etfs-pipeline/` change 0 files.
    Your aw-1 tree `C:/tmp/rv-r28-dell1` (pin 39889dd4d7) is the ROLLBACK tree: keep it.
  </context>

  <steps>
    1. STOP 1 (pin): `git worktree add --detach C:/tmp/rv-ws23-dell1 b48273e3d0`. A later commit only if `git diff --stat
       b48273e3d0 <commit> --` over the seven `STAGED` paths, `infra/aws/lambda/etfs-pipeline/` and
       `infra/aws/terraform/etfs-rivalfunds/` (tests left out) prints nothing. RIV-wi-1 is NOT in this pin.
    2. Package, then plan with `-out C:/tmp/rv_apply_ws23.tfplan` from the root in that tree.
    3. STOP 3 (plan): branch A is `0 to add, 5 to change, 0 to destroy`, the five `aws_lambda_function.stage`, package
       attributes only, read per attribute from `terraform show -json`. Anything else: apply NOTHING and report.
    4. SNAPSHOT (COO condition 5): from the repository root, `python
       org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round28/coverage_snapshot.py take
       C:/tmp/rv-ws23-covsnap 2026-10-09 20`. Commit `C:/tmp/rv-ws23-covsnap/manifest.json` as
       `deliverables/0.7.0_AE_CloudOps~DELL1/WS23_COVERAGE_SNAPSHOT_MANIFEST.json`. Keep the parquet files. No snapshot, no
       apply.
    5. ENV (CTO condition 9): print the five functions' environment KEY sets (names only, never values).
    6. WINDOWS (CTO condition 10 + COO condition 4): never inside 10:55Z-11:15Z or 12:55Z-13:15Z, and never while site Z's
       RIV-tc-1 merge is running (ask `0.0.0_AB_MSTR~DELL1` for its state if unsure). Open the NEVER-2 ledger entry with two
       legs: L1 the activation (yours); L2 the issuer's read of the 2026-10-10 11:00Z chain and 13:00Z sweep (the
       issuer closes it). BEFORE: the five `CodeSha256` and `LastModified`.
    7. Apply the saved plan through `.tools/safe-apply.sh` from `C:/tmp/rv-ws23-dell1`.
    8. AFTER: five `CodeSha256` moved and equal to the built zips (AC1), `LastModified` after the apply, `State Active`,
       `LastUpdateStatus Successful`, `MemorySize` 3008; the five environment key sets equal to step 5's; a re-plan at the
       same pin reads no changes. Close L1.
  </steps>

  <rules>
    Invoke no function; send no test event; write no S3 object (the snapshot is a READ); set no environment variable. No
    republish, no replay, no ad-hoc stage run (COO condition 6). Write only your deliverables folder, the ledger entry and
    its sentinel, and this order's report section.
  </rules>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this act changes no schedule (package hash only); the windows in step 6 keep it clear of the 11:00Z chain, the 13:00Z sweep and the tc-1 merge.
comp-iam: DECLARED-NOT-APPLICABLE -- denominator: 0 files change under infra/aws/terraform/etfs-rivalfunds/ between 39889dd4d7 and b48273e3d0, and branch A requires no policy change in the plan.
comp-adversary: RUN -- a plan made before packaging (package then plan in one tree, step 2); a pin carrying RIV-wi-1 (STOP 1); an apply inside a scheduled run or the tc-1 merge (step 6); an environment change riding the apply (steps 5 and 8); the in-place coverage rewrite with no pre-image (step 4). BLIND: whether a scheduled run fires early.
lane: CloudOps applies under both signed halves (COO @683b767406, CTO @20bd5c33db).
</preflight>

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-wh-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round28/ws23_deploy_check.py C:/tmp/rv-ws23-dell1</invocation><expect>WS23 DEPLOY RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-wh-1" judgment="true"/>
</proof_of_spec>

  <report>
    Once, in this section, committed, and the path + hash by broker message to `2.0.0_SA_COO~V1`:
    - STOP 1, the pin read (`git rev-parse HEAD` in the tree);
    - STOP 3, the plan read per attribute;
    - the snapshot line (`SNAPSHOT: n of 20 keys saved`) and the committed manifest's path and hash;
    - the environment key sets before and after;
    - BEFORE and AFTER per function;
    - AC1's output;
    - the re-plan line;
    - the ledger slug and the L1 close;
    - the measured push state.
    AC2 (the 2026-10-10 runs read against the writers table) is the issuer's.
  </report>
</task_order>
