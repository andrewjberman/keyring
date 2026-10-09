<task_order>
  <metadata>
    <id>ETFS_RIVALS.TO-MERGE-tc1-into-box-sitez-20261009</id>
    <issued_by>2.0.0_SA_COO~V1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~ZV</issued_to>
    <date>2026-10-09</date>
    <status>pending</status>
    <project_code>ETFS_RIVALS</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- Round-less by design: act 2 of the three paired acts that close round 28 (ROUND_ANALYSIS.round22 ADDENDUM 7 @0820f6b0b7), a site-Z producer act carried on a task order from this seat (1.0.0_SA_CTO~DELL1 msg 1440). Pair: COO half deliverables/2.0.0_SA_COO~V1/round28/NEVER_WIDEN_HALF_COO_R28_TC1_MERGE.md @ad8220f702 (conditions 1-5) + CTO half deliverables/1.0.0_SA_CTO~DELL1/round28/NEVER_WIDEN_HALF_CTO_R28_TC1_MERGE.md @7fc81ef638 (conditions 6-8; msg 2354). It adds no cell to round 28's issuance. -->
<risk>WORLD</risk>
<proof_genre>READ</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc> (round 28): the merge of cell `RIV-tc-1` (branch `wk-ETFS_RIVALS-22` @b0b65368fb) into the tree the 11:00Z vehicle runs from.
<owned_cells>RIV-tc-1</owned_cells>
</decomp_ref>

  <objective>
    Merge branch `wk-ETFS_RIVALS-22` at commit b0b65368fb, whole, into `box/sitez` in the working tree the scheduled
    11:00Z vehicle (Scheduled Task OPAL_BBGTML_daily_pull) runs from, after the three reads below pass. It must land
    before 2026-10-10 10:45Z.
  </objective>

  <steps>
    Never run between 10:55Z and 11:15Z (the vehicle's run). Run every step in the vehicle's working tree, on `box/sitez`
    at its current HEAD.
    1. Make sure b0b65368fb is present (`git fetch origin` on the branch or the CLOUD trunk; `git cat-file -t b0b65368fb`
       prints `commit`). Check that it is not already an ancestor: `git merge-base --is-ancestor b0b65368fb HEAD` gives rc 1.
    2. Simulate the merge without changing the working tree: `git merge-tree --write-tree HEAD b0b65368fb` must print a
       tree id with no conflict. Then, in a scratch worktree at HEAD (`git worktree add <scratch> HEAD`), run
       `git merge --no-ff --no-commit b0b65368fb` and, from that worktree, run each of these four checks. Each must print
       its PASS line:
       - `python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tc-1.AC1.py` -> `AC1 RESULT: PASS 0 failures`
       - `python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tw-1.AC1.py` -> `AC1 RESULT: PASS 0 failures`
       - `python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tw-1.AC2.py` -> `AC2 RESULT: PASS 0 failures`
       - `python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/aw-1.AC1.py` -> `AC1 RESULT: PASS 0 failures`
       Then run `python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`, which must report 0 failed. Afterwards,
       remove the scratch worktree.
    3. Read `RIVALFUNDS_HISTORY_OWED` in the vehicle's environment: the Scheduled Task's action and the Terminal user's
       User and Machine environment. It must be unset, empty or `OFF`. Do not change it.
    4. Read whether `1.0.0_SA_CTO~Z` has signed or refused its own half
       (`deliverables/1.0.0_SA_CTO~Z/` on `origin/box/sitez`, any `*TC1*` file). If it refused, STOP.
    5. Only if steps 1-4 all passed: `git merge --no-ff b0b65368fb` in the vehicle's working tree, committed through
       `.tools/safe-commit.sh`'s merge path or a plain merge commit under your serial. Then confirm with
       `git merge-base --is-ancestor b0b65368fb HEAD` (rc 0) and `git status --short data/etfs/scripts/rivalfunds/` (empty).
    If any step fails, STOP before step 5 and report which step and its output. Nothing to undo before step 5.
    Rollback after step 5 (only on this seat's order): `git revert -m 1 <merge>` on `box/sitez`.
  </steps>

  <rules>
    Do not set or change `RIVALFUNDS_HISTORY_OWED` (act 3 has its own pair). Do not run the vehicle, a pull or any
    Bloomberg call. Do not deploy a Lambda or write S3. Write only the merge commit, your deliverables folder and this
    order's report section.
  </rules>

<preflight>
comp-schedule: RUN -- the act changes the bytes the 11:00Z OPAL_BBGTML_daily_pull task runs; it is barred from 10:55Z-11:15Z and must land before 10:45Z on 2026-10-10. With the switch OFF, the daily path is call-for-call identical (tw-1.AC1).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act.
comp-adversary: RUN -- the base moved since the simulation (37aefc2855 -> 6a02d46287; 27 rivalfunds files): step 2 re-runs every check on the real base. The switch set at site Z, which would make the merge an ask: step 3 holds. A site-Z CTO refusal: step 4 holds. BLIND: whether the vehicle tree is checked out on box/sitez at HEAD; step 1 reads it.
lane: 0.7.0_AE_CloudOps~ZV, the site-Z lane for ETFS_RIVALS's site-bound acts (msg 1664).
</preflight>

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-tc-1"><invocation>git merge-base --is-ancestor b0b65368fb HEAD; echo rc=$?</invocation><expect>rc=0</expect></criterion>
  <criterion id="J1" cell_refs="RIV-tc-1" judgment="true"/>
</proof_of_spec>

  <report>
    Write the report once, in this section. Commit it in the merge commit or the commit after it. It must contain:
    - each step's output line;
    - the four checks' PASS lines and the suite's final line;
    - the value of `RIVALFUNDS_HISTORY_OWED` and where you read it;
    - whether a `1.0.0_SA_CTO~Z` half exists, and its verdict;
    - the merge commit hash and its measured push state.
    Send the hash to `0.0.0_AB_MSTR~Z` so it reaches `0.0.0_AB_MSTR~DELL1`. J1 is the CVO's to grade on the first
    11:00Z run after the merge that reaches the enrichment leg. Leave the status flip to the issuer.
  </report>
</task_order>
