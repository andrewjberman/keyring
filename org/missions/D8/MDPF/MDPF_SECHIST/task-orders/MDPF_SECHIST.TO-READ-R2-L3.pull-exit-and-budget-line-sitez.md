<task_order>
  <metadata>
    <id>MDPF_SECHIST.TO-READ-R2-L3.pull-exit-and-budget-line-sitez</id>
    <issued_by>2.0.0_SA_COO~H1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~Z</issued_to>
    <date>2026-10-09</date>
    <status>complete</status>
    <project_code>MDPF_SECHIST</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- Round-less by design: an executor READ order, not a cell. It carries leg L3 of ledger mdpf-sechist-sh-t1-sitez-etf-daily-pull-20261007 (inherited by 2.0.0_SA_COO~H1 from the dead 2.0.0_SA_COO~Z, 0.0.0_AB_MSTR~DELL1 msg 1417) to the site-Z seat that can see the pull's files. Carrier per site-Z 1.0.0_SA_CTO~Z msg 32271 (relayed 0.0.0_AB_MSTR~DELL1 msg 1561): the dell1 issuer orders 0.7.0_AE_CloudOps~Z by task order for its site-Z acts. Model: AMGT_CORPUS 327ff38cf9. It adds no cell to round 2. -->
<risk>LOCAL</risk>
<proof_genre>READ</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP.md</decomp_doc> (round 1): leg L3 of the deploy of cell `SH-t-1` (per-security history depth in the site Z ETF daily pull), ledger `mdpf-sechist-sh-t1-sitez-etf-daily-pull-20261007`, owned by `2.0.0_SA_COO~H1` from msg 1417.
<owned_cells>SH-t-1</owned_cells>
</decomp_ref>

  <objective>
    READ ONLY. After the scheduled task `OPAL_BBGTML_daily_pull` fires at 2026-10-09 07:00 ET (11:00Z), copy its run
    result, its fire log and the day's Bloomberg budget ledger into one evidence file, commit it, and report. Run nothing,
    re-register nothing, edit nothing outside your deliverables folder. Read between 11:45Z and 13:30Z on 2026-10-09.
  </objective>

  <context>
    Legs L1 (merge fad25b1527) and L2 (working-tree blob 0e399c9523 of `integrations/bloomberg/pipeline/etf_daily_pull.py`)
    of `org/critical_paths/.open_deploys/mdpf-sechist-sh-t1-sitez-etf-daily-pull-20261007.json` are closed. L3 asks for the
    first SCHEDULED run after L1: the manifest (the issuer reads `s3://opal-data-etfs/bbg/<asof>/run_manifest.json` itself),
    leg exit 0, and a backfill line in the day's `bbg_budget` ledger. The pull records its backfill with
    `_bb.record("backfill", <rows>, "etf_history_backfill_<asof>")` (`etf_daily_pull.py:609`), so the line has
    `"mode": "backfill"` and a batch_id starting `etf_history_backfill_`. A zero-row line or no line is a finding, not a
    failure of this order.
    Files, on the site-Z Terminal machine:
    - fire log: wherever the task's action writes it -- read the action (step 1) and name the path you read;
    - budget ledger: `C:\Users\Opal Bloomberg\AppData\Local\opal_bbg_budget\bbg_budget_2026-10-09.jsonl` (unless
      `RIVALFUNDS_BBG_BUDGET_DIR` is set for that user; if it is, read where it points and say so).
  </context>

  <steps>
    1. `Get-ScheduledTask -TaskName OPAL_BBGTML_daily_pull | Get-ScheduledTaskInfo`, and the task's action (`Execute`,
       `Arguments`, `WorkingDirectory`): record `LastRunTime`, `LastTaskResult`, and the action. If LastRunTime is not
       2026-10-09 ~07:00 local, or the task is still running at 13:30Z: STOP, write what you read, and report.
    2. Copy the WHOLE fire log of that run, unedited, into
       `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.7.0_AE_CloudOps~Z/evidence/sh_t1_l3_fire_20261009.txt`
       under a `## fire log` heading, with a header line stating the log's path, its line count and its write time.
       No log file found is a finding: write ABSENT with the directory listing.
    3. Under `## budget ledger`, copy EVERY line of the day's ledger file, unedited, with its path and line count. Then
       `spent 2026-10-09 = <sum of rows>` computed by `python -c "import json;print(sum(int(json.loads(l).get('rows',0)) for l in open(r'<path>',encoding='utf-8')))"`.
       An absent ledger file is a finding: write ABSENT with the directory listing, never 0.
    4. Under `## task`, the step-1 read.
    5. Commit the one evidence file under your own author line via `.tools/safe-commit.sh`, on your box branch.
  </steps>

  <rules>
    Do not run the task, the pull, or any Bloomberg call. Do not re-register or edit the task. Do not edit the ledger, the
    log, or anything under `integrations/bloomberg/pipeline/`. Write only the one evidence file and this order's report
    section.
    Carried per 1.0.0_SA_CTO~DELL1 msg 1818: (1) a send that writes a firm data bucket, or assumes the 49F principal outside the
    runner's own job, is told to the laptop FIRST; (2) every send to mdpf-daily-runner is reported after the fact with its command id
    and purpose; (3) 49 Financial data never goes into another firm's tree. This order needs none of those acts.
  </rules>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of a fire that has already run; no schedule changes.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a read before the run is complete (window starts 11:45Z, step 1 checks the task is not running); the wrong day's ledger (file named by UTC date 2026-10-09); a redirected ledger dir (step 3 names RIVALFUNDS_BBG_BUDGET_DIR); an absent file read as zero (steps 2-3 forbid it). BLIND: whether the Terminal was signed in for the run -- the log's own lines and LastTaskResult carry that.
lane: CloudOps~Z reads site-Z local files only; the ledger close is the issuer's.
</preflight>

<proof_of_spec>
  <criterion id="AC1" cell_refs="SH-t-1"><invocation>grep -c '^## budget ledger$' org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.7.0_AE_CloudOps~Z/evidence/sh_t1_l3_fire_20261009.txt</invocation><expect>1</expect></criterion>
  <criterion id="AC2" cell_refs="SH-t-1" judgment="true"/>
  <!-- AC3-AC5: the dell1 IAM-parity conditions every CloudOps-lane order carries (1.0.0_SA_CTO~DELL1 msg 1818, ADDENDUM 3 of
       ANDREW_DIRECT_20261009_035xZ_DELL1_RUNS_OWN_DEPLOYS_SITE_BOUND_ONLY_TO_SITE_Z.md @947dd446e5). This order makes no AWS call, so each
       reads NOT EXERCISED when held; the issuer grades them from the report. -->
  <criterion id="AC3" cell_refs="SH-t-1" judgment="true"/><!-- a send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST -->
  <criterion id="AC4" cell_refs="SH-t-1" judgment="true"/><!-- every send to mdpf-daily-runner is reported after the fact with its command id and purpose -->
  <criterion id="AC5" cell_refs="SH-t-1" judgment="true"/><!-- 49 Financial data never goes into another firm's tree -->
</proof_of_spec>

  <report>
    Report ONCE to 2.0.0_SA_COO~H1 (dell1; via 0.0.0_AB_MSTR~Z's bus relay if no direct route): the commit hash and its
    measured push state, AC1's printed count, LastRunTime and LastTaskResult, the fire log's last three lines, every
    `"mode": "backfill"` ledger line, and the day's spent total. AC2 (leg L3's proof as the ledger states it) is the
    issuer's to grade: do not mark it. Leave the status flip to the issuer. If the read misses 13:30Z, say so to
    0.0.0_AB_MSTR~DELL1 as well.
  </report>
</task_order>
