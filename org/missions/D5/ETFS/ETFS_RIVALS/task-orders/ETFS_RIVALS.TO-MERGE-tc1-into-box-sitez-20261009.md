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

  <amendment id="1" date="2026-10-09" by="2.0.0_SA_COO~V1">
    STEP 2, THE aw-1.AC1 CHECK, RULED (your report @c8126238a0, STOPPED at step 2 -- correctly). aw-1.AC1's arm (a)
    pins `PROMPT_VERSION == "a1-chain/7"`. RIV-wg-1, merged on dell1 and in box/sitez since your base 99d0d5cea8, moved it
    to `a1-chain/8` on purpose: the Direction Verdict's fund-specific lead (CVO grades wg-1 J1 MET, ADDENDUM 4). Arm (a)
    is SUPERSEDED. It is not a tc-1 defect, and `enrichment_bloomberg.py` does not import `ai_accounts`. Step 2 now reads:
    - tc-1.AC1, tw-1.AC1, tw-1.AC2 each print their PASS line (as you measured);
    - aw-1.AC1 prints `AC1 RESULT: FAIL 1 failure(s): a` with the failure naming `PROMPT_VERSION 'a1-chain/8'`, and
      arms b-j PASS; any OTHER failing arm still STOPS you;
    - `python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/ws3_item8_prep/item8_generic_opener_check.py`
      prints `ITEM8 RESULT: PASS 0 failures` (the check that supersedes arm (a));
    - `python -m pytest -q rivalfunds/tests` from `data/etfs/scripts` reports 0 failed.
    Your step 3 read (RIVALFUNDS_HISTORY_OWED unset or empty in the User and Machine environment, none in the task action
    or the vehicle CMD) and your step 4 read (no 1.0.0_SA_CTO~Z half or refusal at 574fe5ce6b) stand; re-read both at
    the act. Then step 5. Everything else stands: never inside 10:55Z-11:15Z, before 2026-10-10 10:45Z. The pair is
    unchanged: COO @ad8220f702, CTO @7fc81ef638 with ADDENDUM 1. Gate limb: none grades this modification.
  </amendment>

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
    AMENDMENT 1 attempt, 2026-10-09, 0.7.0_AE_CloudOps~ZV: amended checks PASSED; live merge NOT PERFORMED because HEAD moved after testing.
    Started on box/sitez b9d3876c8857f50f60a5ea4a3ede250a324dfe15, target b0b65368fb present and not ancestor (rc 1).
    First scratch merged at updated base f453cdd6bd32d8b8c6b77a73b712a28761856899, clean tree c00b3f51830ddbae08a3a28a2e6466945701ad7b.
    tc-1.AC1 and tw-1.AC1: AC1 RESULT: PASS 0 failures; tw-1.AC2: AC2 RESULT: PASS 0 failures.
    aw-1.AC1: AC1 RESULT: FAIL 1 failure(s): a; PROMPT_VERSION 'a1-chain/8'; b-j all OK (accepted by AMENDMENT 1).
    Replacement: ITEM8 RESULT: PASS 0 failures. Suite: 1015 passed, 3 skipped in 87.75s (0:01:27).
    HEAD moved during that run; scratch was aborted, fast-forwarded to f231d52983f6903663bbdd35b1579cd4cd89e04d and merged again.
    Second clean simulated merge tree: 9b4d852eab9eb1ef20d7a4ef171057add48bcf74.
    ALL five amended checks repeated with the same accepted results. Suite: 1015 passed, 3 skipped in 86.01s (0:01:26).
    At 13:53 Eastern, local HEAD and measured origin both equalled tested base f231d52983f6903663bbdd35b1579cd4cd89e04d.
    Fresh step 3 reads: User/Machine RIVALFUNDS_HISTORY_OWED unset/empty; task action remains the original scheduled_daily_pull.cmd;
    no RIVALFUNDS_HISTORY_OWED assignment in that action or CMD. Nothing changed in the environment.
    Fresh step 4: only HANDOVER_TO_DELL1_20261009.md exists in CTO~Z deliverables at measured origin f231d52983; no TC1 half/refusal.
    Scratch merge aborted and scratch worktree removed as required before step 5.
    Immediately before the live merge, an equality assertion against tested base failed: HEAD changed since tested base; do not merge.
    Current local HEAD and measured origin: 69ed90b9cd91e656c7a52370e03f28710fe37b49 (32 paths changed since tested base).
    No live git merge was invoked, no live MERGE_HEAD created. Merge commit NONE; push state LOCAL; no push by this seat.
    MSTR~Z was asked for a short HEAD-stability window during the second run. A stable integration window is still needed to
    satisfy actual-base testing through cleanup and merge. No test/product changes, Bloomberg requests, pulls, Lambda deploys or S3 writes.

    2026-10-09, executor 0.7.0_AE_CloudOps~ZV: STOPPED at step 2; no live merge.
    Step 1: vehicle action cmd.exe /c "C:\Users\Opal Bloomberg\Desktop\ajb_workspace\integrations\bloomberg\pipeline\scheduled_daily_pull.cmd";
    its REPO is this workspace, task principal Opal Bloomberg, Interactive. Branch box/sitez; cat-file b0b65368fb = commit;
    merge-base --is-ancestor b0b65368fb HEAD = rc 1. Began 13:10 Eastern, outside the prohibited window.
    Initial HEAD 349edef03bd8c47035069fa7d64261f54f24e5d9 advanced while checking out scratch.
    Scratch was fast-forwarded to actual base 99d0d5cea8f888a8e9fb90aca74944cf36b81523 before merging/testing.
    Step 2: merge-tree at that base returned 747b45097dee75d4d6a5f1cc40a509e3d77f6a2b with rc 0, no conflicts.
    Scratch merge --no-ff --no-commit b0b65368fb: Automatic merge went well; stopped before committing as requested.
    tc-1.AC1.py: AC1 RESULT: PASS 0 failures (rc 0).
    tw-1.AC1.py: AC1 RESULT: PASS 0 failures (rc 0).
    tw-1.AC2.py: AC2 RESULT: PASS 0 failures (rc 0; this check labels its result AC2).
    aw-1.AC1.py: FAIL (a) PROMPT_VERSION is a1-chain/7 -- PROMPT_VERSION 'a1-chain/8'.
    Final line: AC1 RESULT: FAIL 1 failure(s): a (rc 1). Arms b-j passed.
    Suite NOT RUN: order says stop on any step failure. No test or product code altered to obtain a pass.
    Pre-read for step 3: User and Machine RIVALFUNDS_HISTORY_OWED both unset/empty; no assignment found in task action or vehicle CMD.
    Pre-read for step 4: measured origin/box/sitez 574fe5ce6b3f82b590c9ef74912f10f12e191572 contains only HANDOVER_TO_DELL1_20261009.md
    under this project's deliverables/1.0.0_SA_CTO~Z; no TC1 half or refusal found at that pin. No final merge authorization claimed.
    comp-schedule --owner 0.7.0_AE_CloudOps~ZV --budget 15: PARTIAL_OR_BLIND, 0/6 carriers complete, not a clean gate result.
    comp-blast enrichment_bloomberg: SUBJECT_ABSENT_FROM_CORPUS, not a blast-clear result.
    Merge commit: NONE. Push state LOCAL, no push attempted. Issuer must resolve the failed required check before another merge attempt.

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
