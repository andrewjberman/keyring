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

    ---

    EXECUTOR REPORT -- `0.7.0_AE_CloudOps~RV1`, 2026-10-09, under both signed halves (COO @`194c4b3e7d` with
    AMENDMENT 1 @`fb2f737840`, CTO @`63bdddfbb9`), read in full before any act. Both halves' own reads were
    REPRODUCED here, not inherited. **THE LOOKUP IS LIVE AND VERIFIED; its first run is the 2026-10-10 13:00Z sweep.**

    **STOP 1 (pin).** Fresh detached tree `C:/tmp/rv-wi1-dell1` at `b86feccfeb`; `git rev-parse HEAD` reads
    `b86feccfeb85c4f802ff1d40f0af01b3bcde0e41`, 0 porcelain lines. No later commit was used, so condition 2's
    byte-equality clause did not arise.
    CONDITION 1: the WS2/WS3 apply landed first and its L1 is closed (ledger `etfs-rivalfunds-ws23-dell1-20261009`,
    report @`8ad8b51083`). Independently confirmed on the live plane -- the five `CodeSha256` read at this act's
    BEFORE are exactly that deploy's after-hashes.
    CONDITION 2 + AMENDMENT 1 REPRODUCED: over the eight `STAGED` paths plus the two infra roots, tests left out,
    `git diff --stat` reads **7 files +273 -18** (`b48273e3d0` -> `74308c98b6`) and **4 files +133 -6**
    (`74308c98b6` -> `b86feccfeb`) -- both halves' numbers exactly.
    CTO CONDITION 11 READ IN THE PIN, not taken from the amendment's word: `dramatic_move.void_rows` is present and
    `price_series` carries `VOID_PREFIX = "actions-void-"` with the skip in `_actions`. So the per-key rollback for
    a wrong row is an APPEND this seat can run, which is the gap the CTO half was signed to close.
    PRE-PACKAGE CONTROL: `core.autocrlf` is `false`; every shipped file compared RAW against its committed blob
    (`git cat-file blob`, never `git diff`, which normalizes and would hide a CRLF-only difference) -- **95 of 95
    byte-identical**, 0 missing, 0 different, negative control live. 95 = the WS2/WS3 pin's 82 plus the
    `data/find/dualbiz/scripts` directory `STAGED` gained for the SERP client (row W32-S2).

    **STOP 3 (plan), graded per attribute from `terraform show -json`, never from the summary line.**
    45 resource_changes, 39 no-op, 6 update; the change set regrades as **0 to add, 6 to change, 0 to destroy**.
    The movers are exactly the five `aws_lambda_function.stage` plus
    `aws_iam_role_policy.stage["etfs-rivalfunds-daily-lambda"]` -- nothing else, no other policy, role, schedule,
    memory or timeout.
    | mover | attributes DIFFERENT | verdict |
    |---|---|---|
    | the four non-daily functions | `['last_modified','source_code_hash']` | package only |
    | `etfs-rivalfunds-daily-lambda` | `['environment','last_modified','source_code_hash']` | env GAINS exactly `['BD_SERP_ZONE','RIVALFUNDS_SERP_SECRET']`, nothing lost, no pre-existing key's value changed |
    | `aws_iam_role_policy.stage["etfs-rivalfunds-daily-lambda"]` | `['policy']` | 10 -> 11 statements: exactly ONE added, NONE removed |
    The added statement: `Sid GetSerpSecret`, `Action` exactly `['secretsmanager:GetSecretValue']`, `Resource`
    exactly `arn:aws:secretsmanager:us-east-1:313476888478:secret:find-insure/bright-data/api-key-7ojPkd`,
    `Effect Allow`. **No IAM wildcard of EITHER kind in that Resource** -- checked for `?` as well as `*`, because
    the pre-existing `GetOpenAISecret` statement legitimately uses `??????` and an asterisk-only check would not
    see a single-character wildcard. `RIVALFUNDS_SERP_SECRET` equals the exact ARN and `BD_SERP_ZONE` equals
    `serp_opal`. `memory_size` 3008 before == after on all five; 0 of a 19-name forbidden-attribute denominator
    differs on any mover. **BRANCH A, 0 failures.**
    The ARN's EXISTENCE was read BEFORE the apply (`describe_secret` on the exact ARN: present, name
    `find-insure/bright-data/api-key`), because a policy read proves a pattern matches a string and never that the
    string names anything. No `GetSecretValue` call was made and no secret value was read at any point.

    **ENVIRONMENT, BEFORE and AFTER -- key NAMES, plus the two new values, neither of which is a secret value.**
    | function | BEFORE | AFTER |
    |---|---|---|
    | `etfs-rivalfunds-daily-lambda` | `['RIVALFUNDS_AI_ENABLE','RIVALFUNDS_OPENAI_SECRET']` | `['BD_SERP_ZONE','RIVALFUNDS_AI_ENABLE','RIVALFUNDS_OPENAI_SECRET','RIVALFUNDS_SERP_SECRET']` |
    | the other four | `[]` | `[]` -- unchanged, COO condition 5's second clause |

    **BEFORE and AFTER per function** (apply invoked 15:21:36Z, returned 15:22:42Z; modifications 15:22:10Z-15:22:34Z):
    | function | CodeSha256 BEFORE | CodeSha256 AFTER | LastModified AFTER | state |
    |---|---|---|---|---|
    | `etfs-rivalfunds-daily-lambda` | `Gn5el43Fkr+Z` | `pUPsGskqIXVf` | 15:22:34Z | Active/Successful/3008 |
    | `etfs-rivalfunds-fetch-holdings-lambda` | `co0WQL/Iospw` | `Woe/ivAht32r` | 15:22:10Z | Active/Successful/3008 |
    | `rivalfunds-build-silver-lambda` | `rl8rvn08aZst` | `hxTypwIuXS9N` | 15:22:16Z | Active/Successful/3008 |
    | `rivalfunds-build-canonical-shape-lambda` | `dgF/rCz3rRfK` | `RBdsHlgiMmno` | 15:22:28Z | Active/Successful/3008 |
    | `rivalfunds-publish-page-lambda` | `5R61Tu7/lY9u` | `PE1xU1taIXcm` | 15:22:22Z | Active/Successful/3008 |
    The apply ran `.tools/safe-apply.sh -chdir=<tree> apply C:/tmp/rv_apply_wi1.tfplan` -- the SAVED GRADED
    planfile, so the applied bytes are the graded bytes. `Apply complete! Resources: 0 added, 6 changed, 0
    destroyed`, rc=0.
    APPLIED == GRADED, checked independently of AC1 and across all three surfaces: **6 of 6** -- each live
    `CodeSha256` equals the plan's own declared after-hash, each live environment map equals the plan's declared
    after-map, and the live policy document equals the plan's declared after-policy statement for statement.

    **AC1.** `python .../wi1_deploy_check.py C:/tmp/rv-wi1-dell1` -> all five naming their own built zip, the daily
    role reading `secretsmanager statements 2` on the OpenAI pattern and the exact `-7ojPkd` ARN, then
    **`WI1 DEPLOY RESULT: PASS 0 failures`**, rc=0.

    **RE-PLAN.** `No changes. Your infrastructure matches the configuration.`, `-detailed-exitcode` rc=0.

    **ONE LIMB COULD NOT BE EXERCISED, AND IS NOT CLAIMED.** `simulate_principal_policy` on the daily role returns
    `AccessDenied`: this device's principal (`cloudops-dell1-agent-user`) lacks `iam:SimulatePrincipalPolicy`. That
    is a limit on the READER, not a statement about the grant, and it is distinguishable from a real deny by a
    positive control -- the same session CAN read IAM (`get_role_policy` returned 11 statements). No IAM was
    widened to obtain the read: the order's named oracle is AC1 limb 3, which passed on the live document. If the
    issuer wants an evaluated-decision read, it needs a principal that holds that action.

    **PREFLIGHT `comp-iam: RUN`, with its verdict stated honestly.** `comp-iam service etfs-rivalfunds-daily-lambda`
    reads `No AWS operations detected` -- it traces literal `boto3.client()` call sites in the wrapper
    `lambda_function.py` and cannot see through it into the packaged `rivalfunds` modules, and it prints its own
    floor warnings (445 policy blocks attached, 61 NOT ATTACHED, 10 deny statements unparsed). So it contributes
    NOTHING decisive to this act and is not cited as a pass; the deciding reads are the plan's per-attribute
    statement delta and AC1 limb 3's live document read. Denominator as the preflight states it: 1 of 5 role
    policies changes, 0 roles added.

    **LEDGER.** Slug `etfs-rivalfunds-wi1-dell1-20261009`, entry
    `org/critical_paths/change_management/20261009T1520Z_etfs-rivalfunds-wi1-dell1-20261009_deploy_completion.md`,
    opened 15:20Z BEFORE the apply with two legs. **L1 CLOSED with proof.** L2 is OPEN and HELD on a named external
    gate (re-read event: the issuer reads the 2026-10-10 13:00Z sweep and closes L2), so it reads KNOWN-HELD rather
    than half-landed RED. ROLLBACK VERIFIED EXECUTABLE: `C:/tmp/rv-ws23-dell1` is intact at `b48273e3d0`, 0
    porcelain lines, five built zips AND terraform already initialised, so the half's rollback is one command away.

    **RULES HELD.** No function invoked, no test event sent, NO SEARCH MADE, no S3 object written, the void CLI NOT
    run, no secret value read. Writes were confined to the ledger entry and its sentinel and this report section.

    **AC2 NOT MARKED** -- Tokio Marine adjusted on the served page, and a name with no discontinuity making 0
    calls, are read at the 2026-10-10 13:00Z sweep and are the issuer's.

    **PUSH STATE: measured at send time by `git ls-remote` and stated in the broker message.** This box does not
    push `box/dell1`; under `org/XXX.md`'s shared-branch law that branch moves by an MSTR or the box's scheduled
    `box-sync`.
  </report>
</task_order>
