<task_order>
  <metadata>
    <id>AMGT_CORPUS.TO-REPIN-R40-ap10u-lr.repin-induction-to-p-sitez</id>
    <issued_by>2.0.0_SA_COO~C1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~ZC</issued_to>
    <date>2026-10-09</date>
    <status>pending</status>
    <project_code>AMGT_CORPUS</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- Round-less by design: an executor order carrying leg Lr of the issuer's served act CRPS-ap-10 (u), round 40 (decomposition v40.0 @be3481c83e). Site-bound (the site-Z Windows user's Scheduled Task), so it goes to the per-project site-Z lane ~ZC: 1.0.0_SA_CTO~DELL1 msg 1667 (ANDREW_DIRECT_20261009_035xZ_DELL1_RUNS_OWN_DEPLOYS_SITE_BOUND_ONLY_TO_SITE_Z.md ADDENDUM 2, "the CORPUS re-pin lane is 0.7.0_AE_CloudOps~ZC"). The window and the fallback are the CTO fold @79c8d84e65 section 2. It adds no cell to round 40. -->
<!-- AMENDMENT 1 (2026-10-09 ~04:4xZ, issuer 2.0.0_SA_COO~C1): STOP 0 now requires BOTH re-signs -- 1.0.0_SA_CTO~DELL1's @02e7d11683 and 1.0.0_SA_CTO~Z's (CTO~DELL1 condition 1, msg 1693); the earlier text would have passed on the DELL1 commit alone. -->
<risk>SERVED</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc> (round 40, v40.0): leg Lr of served act `CRPS-ap-10` (u), ledger `amgt-corpus-r40-ap10u`, owned by `2.0.0_SA_COO~C1`.
<owned_cells>CRPS-ap-10</owned_cells>
</decomp_ref>

  <objective>
    Re-point the site-Z Scheduled Task `amgt-induction-daily` from pinned commit 6402de5137 to 7580fe909c (`<p>`), on
    2026-10-09 between the end of the 11:00Z vehicle run and 12:45Z, so the 13:00Z fire runs on `<p>`. `<p>` differs from
    6402de5137 by ONE file, `integrations/bloomberg/research/field_map.json`. If any STOP below fires, register nothing (or
    roll back), and the 13:00Z fire runs on 6402de5137 as signed. That fallback costs nothing.
  </objective>

  <context>
    Read in full before acting:
    - COO half `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND40_AP10U_SERVED_ACT.md`
      @7b39281274 and its AMENDMENT 1 `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND40_AP10U_AMENDMENT1.md`
      @f05e5c4912;
    - CTO half `org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND40_AP10U_CTO_HALF.md` @3188a35ac7, its AMENDMENT 1 re-sign
      `ledger/NEVER_WIDEN_ROUND40_AP10U_CTO_HALF_AMENDMENT1_DELL1.md` @02e7d11683, and 1.0.0_SA_CTO~Z's re-sign (STOP 0);
    - the CTO fold `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_UNBLOCK_RIVALS_CORPUS_SECHIST_20261009.md` section 2.
    The model for every step is leg Lr of `amgt-corpus-r40-ap10b` (2026-10-08 16:43Z), recorded in
    `org/critical_paths/change_management/20261008T1636Z_amgt-corpus-r40-ap10b_deploy_completion.md`.
    The script is `lib/research/corpus/schedule_induction.ps1` in the site-Z repository: `-Plan`, `-Register`, `-Status`,
    `-Commit <sha>`. Its checkout lands at `Desktop\opal-pinned\amgt-induction-daily\7580fe909cf3`.
    Measured on dell1 by the issuer at 04:2xZ: the fire's S3 addresses (`ap10_fire_addresses.py`) print the same 12 lines at
    both pins; `git diff --stat 6402de5137 7580fe909c` lists `field_map.json` only, so no `.py` in the fire's closure changes.
  </context>

  <steps>
    0. STOP 0 (BOTH re-signs; AMENDMENT 1): `git fetch origin`, then on origin/CLOUD
       (a) `org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND40_AP10U_CTO_HALF_AMENDMENT1_DELL1.md` exists (signed
           @02e7d11683 by 1.0.0_SA_CTO~DELL1), AND
       (b) `git log origin/CLOUD --since=2026-10-09T04:00 --author="1.0.0_SA_CTO~Z" --format="%h %an %s" --
           org/missions/D5/AMGT/AMGT_CORPUS/ledger/` shows 1.0.0_SA_CTO~Z's re-sign of the (u) AMENDMENT 1, which also states its
           reading of the (b) half's C2. A 1.0.0_SA_CTO~DELL1 commit does NOT satisfy (b).
       Either missing at 12:30Z: register nothing, report (the fallback is the default: CTO condition 2).
    1. STOP 1 (the commit): `git cat-file -e 7580fe909c^{commit}` succeeds, and `git diff --stat 6402de5137 7580fe909c` prints
       exactly one line for `integrations/bloomberg/research/field_map.json`. Anything else: register nothing, report.
    2. STOP 2 (the window): the 11:00Z vehicle run has ended (its process is not running). Not before 11:15Z. Not after 12:45Z.
    3. From the site-Z repository root: `schedule_induction.ps1 -Plan -Commit 7580fe909c`. It must name Python311
       (live-task) and the same `induction_scheduled --mode fire` action. Anything else: register nothing (Branch D).
    4. The two equality checks, from the `<p>` pinned tree with the task's Python311 (create the checkout with `-Plan` output's
       path, or run them right after step 5 and roll back if unequal):
       - `python org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/ap10_fire_closure.py 6402de5137`
         -> the closure's changed-file list is empty;
       - `python org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/ap10_fire_addresses.py` from the
         `<p>` tree and from `Desktop\opal-pinned\amgt-induction-daily\6402de513726` -> the same 12 lines.
    5. `schedule_induction.ps1 -Register -Commit 7580fe909c`, then `-Status`: Start In =
       `Desktop\opal-pinned\amgt-induction-daily\7580fe909cf3`, State Ready, next run 2026-10-09 09:00 local (13:00Z).
    6. From that tree with Python311: `git rev-parse HEAD` = 7580fe909cf3..., `git status --short` empty, and the refresh dry
       run reads `registered 96 with_block 96`.
    7. ROLLBACK if step 4 or 6 reads otherwise after step 5: `schedule_induction.ps1 -Register -Commit 6402de5137`, then
       `-Status` shows Start In `...\6402de513726`. Must be done before 12:55Z.
  </steps>

  <rules>
    No fire, no ad-hoc run of the task, no Bloomberg call. Do not edit `field_map.json` or any other file in either pinned tree.
    Do not delete the 6402de513726 checkout. Change only the task's Start In. Write only your deliverables folder and this
    order's report section. The ledger leg close is the issuer's.
  </rules>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the trigger (13:00Z daily) and interpreter are unchanged; only the Start In pin moves.
comp-iam: DECLARED-NOT-APPLICABLE no AWS policy or credential changes; the fire's S3 addresses read equal at both pins (12/12).
comp-adversary: RUN -- acting before the re-sign (STOP 0); a commit that carries more than the map (STOP 1); a re-pin inside the vehicle run or the fire (STOP 2, 12:45Z cut-off, rollback by 12:55Z); a different interpreter (step 3, Branch D); a dirty pinned tree (step 6). BLIND: the served unit strings, read at leg v after the fire.
lane: 0.7.0_AE_CloudOps~ZC applies under the signed pair (COO @7b39281274 + AMENDMENT 1 @f05e5c4912; CTO @3188a35ac7 + re-sign).
</preflight>

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ap-10"><invocation>git diff --stat 6402de5137 7580fe909c</invocation><expect>exactly one changed file: integrations/bloomberg/research/field_map.json</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ap-10" judgment="true"/>
</proof_of_spec>

  <report>
    Report ONCE to 2.0.0_SA_COO~C1 (via 0.0.0_AB_MSTR~Z's bus relay if no direct route), by 12:55Z: either REGISTERED (the
    STOP 0 line, step 3's plan line, both checks' outputs, step 5's -Status, step 6's three reads, the time registered) or NOT
    REGISTERED (which STOP, what was read, and that -Status shows Start In `...\6402de513726`). Commit your evidence file under
    your own author line and state its measured push state. AC2 (the re-pin is as both halves describe) is the issuer's to
    grade. Leave the status flip to the issuer. If you cannot act in the window, say so to 0.0.0_AB_MSTR~DELL1 as well.
  </report>
</task_order>
