<task_order>
  <metadata>
    <id>AMGT_CORPUS.TO-READ-R40-ap10b-lv.fire-log-and-budget-line-sitez</id>
    <issued_by>2.0.0_SA_COO~C1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~Z</issued_to>
    <date>2026-10-09</date>
    <status>pending</status>
    <project_code>AMGT_CORPUS</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- Round-less by design: an executor READ order, not a cell. It carries leg Lv of the issuer's served act CRPS-ap-10 (b), round 40 (decomposition v40.0 @be3481c83e), to the site-Z seat that can see the fire's files. Carrier per site-Z 1.0.0_SA_CTO~Z msg 32271 (relayed 0.0.0_AB_MSTR~DELL1 msg 1437) and 1.0.0_SA_CTO~DELL1 msg 1442: the dell1 issuer orders 0.7.0_AE_CloudOps~Z by task order for its site-Z producer acts. It adds no cell to round 40. -->
<risk>LOCAL</risk>
<proof_genre>READ</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc> (round 40, v40.0): leg Lv of served act `CRPS-ap-10` (b), ledger `amgt-corpus-r40-ap10b`, owned by `2.0.0_SA_COO~C1` from seating (1.0.0_SA_CTO~DELL1 msg 1396).
<owned_cells>CRPS-ap-10</owned_cells>
</decomp_ref>

  <objective>
    READ ONLY. After the scheduled task `amgt-induction-daily` fires at 2026-10-09 13:00Z (09:00 local), copy its fire log
    and the day's Bloomberg budget ledger into one evidence file, commit it, and report. Run nothing, re-register nothing,
    edit nothing outside your deliverables folder. Read between 13:20Z and 14:30Z on 2026-10-09 (the 2026-10-08 fire wrote
    its log at 13:15Z).
  </objective>

  <context>
    Leg Lr of ledger `org/critical_paths/.open_deploys/amgt-corpus-r40-ap10b.json` is closed: the task was re-registered
    to pinned commit 6402de5137 at 2026-10-08 16:43Z (Start In `Desktop\opal-pinned\amgt-induction-daily\6402de513726`).
    That pin adds ONE budget record per fire. Leg Lv, the issuer's to close, asks for: `pulled 96 bloomberg_calls 768`,
    rc 0, and ONE ledger line of mode `amgt-model-block` with rows near 4,224 and a batch_id ending
    `rows_unit=returned-records`, printed beside the day's other ledger lines (CTO half
    `org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND40_AP10B_CTO_HALF.md` @4c0f314e86, condition C1).
    The model for this read is the 2026-10-08 read:
    `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/evidence/r40_ap10m_leg_v_fire_20261008.txt`.
    Files, on the site-Z Terminal machine:
    - fire log: `C:\Users\Opal Bloomberg\AppData\Local\opal\amgt-induction-daily\2026-10-09.log`;
    - budget ledger: `C:\Users\Opal Bloomberg\AppData\Local\opal_bbg_budget\bbg_budget_2026-10-09.jsonl` (unless
      `RIVALFUNDS_BBG_BUDGET_DIR` is set for that user; if it is, read where it points and say so).
  </context>

  <steps>
    1. `Get-ScheduledTask -TaskName amgt-induction-daily | Get-ScheduledTaskInfo`: record `LastRunTime`,
       `LastTaskResult`, and the action's working directory. If LastRunTime is not 2026-10-09 ~09:00 local, or the task is
       still running at 14:30Z: STOP, write what you read, and report.
    2. Copy the WHOLE fire log, unedited, into
       `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~Z/evidence/r40_ap10b_leg_v_fire_20261009.txt`
       under a `## fire log` heading, with a header line stating the log's path, its line count and its write time.
    3. Under `## budget ledger`, copy EVERY line of the day's ledger file, unedited, with its path and line count. Then
       `spent 2026-10-09 = <sum of rows>` computed by `python -c "import json;print(sum(int(json.loads(l).get('rows',0)) for l in open(r'<path>',encoding='utf-8')))"`.
       An absent ledger file is a finding: write ABSENT with the directory listing, never 0.
    4. Under `## task`, the step-1 read.
    5. Commit the one evidence file under your own author line via `.tools/safe-commit.sh`, on your box branch.
  </steps>

  <rules>
    Do not run the task, the pull, or any Bloomberg call. Do not re-register or edit the task. Do not edit the ledger or
    the log. Write only the one evidence file and this order's report section.
  </rules>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of a fire that has already run; no schedule changes.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a read before the log is complete (window starts 13:20Z, step 1 checks the task is not running); the wrong day's ledger (file named by UTC date 2026-10-09); a redirected ledger dir (step 3 names RIVALFUNDS_BBG_BUDGET_DIR); an absent file read as zero (step 3 forbids it). BLIND: whether the fire's Bloomberg session was healthy -- the log's own lines carry that.
lane: CloudOps~Z reads site-Z local files only; the ledger close is the issuer's.
</preflight>

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ap-10"><invocation>grep -c "^budget_record amgt-model-block .* written 1$" org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~Z/evidence/r40_ap10b_leg_v_fire_20261009.txt</invocation><expect>1</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ap-10" judgment="true"/>
</proof_of_spec>

  <report>
    Report ONCE to 2.0.0_SA_COO~C1 (dell1; via 0.0.0_AB_MSTR~Z's bus relay if no direct route): the commit hash and its
    measured push state, AC1's printed count, the fire log's last three lines, the `budget_record` line, the
    `amgt-model-block` ledger line(s), and the day's spent total. AC2 (leg Lv's proof as the CTO half's C1 states it) is the
    issuer's to grade: do not mark it. Leave the status flip to the issuer. If the read misses 14:30Z, say so to
    0.0.0_AB_MSTR~DELL1 as well.
  </report>
</task_order>
