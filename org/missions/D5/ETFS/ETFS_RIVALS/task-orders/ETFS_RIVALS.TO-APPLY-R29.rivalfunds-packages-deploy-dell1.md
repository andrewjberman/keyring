<task_order>
  <metadata>
    <id>ETFS_RIVALS.TO-APPLY-R29.rivalfunds-packages-deploy-dell1</id>
    <issued_by>2.0.0_SA_COO~V1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~RV1</issued_to>
    <date>2026-10-12</date>
    <status>pending</status>
    <project_code>ETFS_RIVALS</project_code>
  </metadata>

<direct_act>true</direct_act>
<!-- Round-less by design: an executor apply order, not a cell. The four round-29 cells (RIV-xa-1, xb-1, xc-1, xd-1) are merged and complete; this is their apply leg under a signed pair, so that the CVO's two J1 reads have a page the deployed code publishes. It adds no cell. -->
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc> (round 29): the apply leg of cells RIV-xa-1, RIV-xb-1, RIV-xc-1 and RIV-xd-1 (all merged on box/dell1; pin de3c6bf211).
<owned_cells>RIV-xa-1 RIV-xb-1 RIV-xc-1 RIV-xd-1</owned_cells>
</decomp_ref>

  <objective>
    Deploy pin de3c6bf211 to the rivalfunds stack: the five code packages and NOTHING else. The plan is exactly 0 to add, 5 to change,
    0 to destroy: no environment key, no IAM statement, no schedule, memory or timeout moves.
    START ONLY AFTER the issuer's word that the 2026-10-13 13:00Z sweep has been read (the CTO ruled the window: one served change per sweep).
    Complete before 2026-10-14 12:45Z, so the first sweep on the pin is 2026-10-14 13:00Z.
  </objective>

  <context>
    BOTH HALVES SIGNED; read both in full before acting:
    - COO half `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round29/NEVER_WIDEN_HALF_COO_R29_DEPLOY.md` @ff7e96adf6;
    - CTO half `org/missions/D5/ETFS/ETFS_RIVALS/ledger/NEVER_WIDEN_ROUND29_DEPLOY_CTO_HALF.md` (the window ruled; plan exactly 0/5/0, else STOP).
    The pin is the scratch branch `pin-ETFS_RIVALS-r29` at de3c6bf211 on this box: the last applied pin b86feccfeb (the wi-1 deploy) plus
    exactly `data/etfs/scripts/rivalfunds/{dramatic_move,ai_accounts,render}.py` at git blob ids
    37397a1057439b90aa2a9b759beb159375e91673, 025197135d89ae874ce824d745692ee4b14a3219 and deb9a7ffa8f2f4713ed6894f30aea771ef4cfd8d.
    HEAD of box/dell1 is NOT the pin and must not be deployed: it carries other seats' changes to staged paths.
    Your model is your own wi-1 apply (log `org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-10-09/rv1_wi1_lookup_deploy.md`): same root, same
    packager, package then plan in one tree. The ROLLBACK is a re-apply at b86feccfeb: make that tree at STOP 1 and keep it until L2 closes.
  </context>

  <steps>
    1. STOP 1 (pin): `git worktree add --detach C:/tmp/rv-r29-dell1 de3c6bf211`; `git rev-parse HEAD` there starts `de3c6bf211`, 0 porcelain
       lines, and the three blob ids above read by `git rev-parse HEAD:<path>`. A later commit only if `git diff --stat de3c6bf211 <commit> --`
       over the STAGED paths of `infra/aws/lambda/etfs-pipeline/rivalfunds_package.py`, `infra/aws/lambda/etfs-pipeline/` and
       `infra/aws/terraform/etfs-rivalfunds/` (tests left out) prints nothing. Also `git worktree add --detach C:/tmp/rv-r29-rollback b86feccfeb`.
    2. Package, then plan with `-out C:/tmp/rv_apply_r29.tfplan` from the root in the pin tree. Pre-package control: every shipped file
       compared RAW against its committed blob (`git cat-file blob`, never `git diff`).
    3. STOP 3 (plan, read per attribute from `terraform show -json`): `0 to add, 5 to change, 0 to destroy`: the five
       `aws_lambda_function.stage`, attributes `source_code_hash` and `last_modified` only. Anything else (an `environment` change, a policy,
       a role, a schedule, memory, timeout): apply NOTHING and report.
    4. ENV: print the five functions' environment KEY sets before (names only); the daily one is the four keys of the wi-1 act.
    5. WINDOWS: never inside 10:55Z-11:15Z or 12:55Z-13:15Z. Open the NEVER-2 ledger entry with two legs: L1 the activation (yours);
       L2 this seat's read of the 2026-10-14 13:00Z sweep (the issuer closes it). BEFORE: the five `CodeSha256` and `LastModified`.
    6. Apply the saved plan through `.tools/safe-apply.sh` from `C:/tmp/rv-r29-dell1`.
    7. AFTER: AC1; the five functions' environment key sets unchanged; a re-plan at the same pin reads no changes. Close L1.
  </steps>

  <rules>
    Invoke no function; send no test event; make no search; write no S3 object (the void CLI is NOT run by this order); read no secret value.
    Write only your deliverables folder, the ledger entry and its sentinel, and this order's report. A lane refusal is reported verbatim; take no override.
  </rules>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule changes; the first run on the pin is the existing 13:00Z sweep; step 5's windows keep the apply clear of both scheduled runs.
comp-iam: DECLARED-NOT-APPLICABLE no role or policy changes (plan 0/5/0, packages only); AC1 re-reads the daily role's two secretsmanager statements unchanged.
comp-adversary: RUN -- a pin that is HEAD (STOP 1: the pin is a scratch branch commit; the three blob ids); an environment or policy change riding the plan (STOP 3 per attribute, AC1 limb 2); an apply inside a scheduled run (step 5); a package whose files differ from the pin's (AC1 limb 3 reads the zips' bytes). BLIND: Bright Data's availability at 13:00Z (a failed search is counted and never blocks publish).
lane: CloudOps applies under both signed halves (COO @ff7e96adf6, CTO NEVER_WIDEN_ROUND29_DEPLOY_CTO_HALF.md).
</preflight>

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-xa-1 RIV-xb-1 RIV-xc-1 RIV-xd-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round29/r29_deploy_check.py C:/tmp/rv-r29-dell1</invocation><expect>R29 DEPLOY RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

  <report>
    Once, in this section, committed, and the path + hash by broker message to `2.0.0_SA_COO~V1`:
    - STOP 1 and STOP 3 as read, with the plan per attribute;
    - the environment key sets before and after;
    - BEFORE and AFTER per function (CodeSha256, LastModified);
    - AC1's output, the re-plan line, the ledger slug and the L1 close;
    - the measured push state.
    The first run on the pin (2026-10-14 13:00Z) is read by the issuer (L2) and the CVO (the two J1 reads), not by this order.
  </report>
</task_order>
