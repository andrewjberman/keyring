# TO IRPT_BCKEND.TO-IB-pr-313 -- reconcile ~P's 42 not-closed remediation rows against live (E1)

<to_id>IRPT_BCKEND.TO-IB-pr-313</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~116</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-04</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>47</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ROUND ANALYSIS rounds 42-46 (msg 104972,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_42_46_P_20261004.md` section 3, item E1): "For
each, read the remedy's own close condition against live state now ... File one closing row per row whose condition already holds,
citing the read. Hand back the list of rows still live. One cell, read-only, no build." | **Decomp cell:** `IB-pr-313`
(decomposition section 40) | **outcome_ref:** the 42 rows | **depends_on:** none.

---

## WORKER FACE

**The job.** Remediation rows are the CVO's ledger of fixes owed. 42 of them are owned by `2.0.0_SA_COO~P` and not closed. Their
states are stale: some remedies have already landed and been served, while others are still live. You read each row's own close
condition against the live world today and record a verdict. No build: you change no code, no infrastructure and no AWS state.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-116`. Run everything from its root.

**The 42 rows.** They are listed in
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r47/e1_census_42_rows.json`, with each row's id, its
remediation file (under `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/`), state, class and remedy text. Read
each row in full in that file: `mechanism`, `evidence`, `remedy`. Then find its close condition. That is what the remedy says must
be true for the row to close: a file at HEAD, a deployed Lambda's CodeSha256, a served object, an IAM policy, a test result.

**Where to read live state** (all read-only):
- **Code at CLOUD HEAD:** your worktree's files and `git log`.
- **Portal PROD:** `git -C portal ls-remote origin refs/heads/PROD`. PROD is c69b4747. Read portal files with `git -C portal show
  <hash>:<path>`.
- **AWS reads, with boto3 in us-east-1:**
  - `lambda.get_function_configuration` (CodeSha256, Role, Environment);
  - `iam.get_role_policy` / `list_role_policies`;
  - `s3.head_object` / `list_objects_v2` on the served buckets the row names (opal-data-ycharts, opal-data-bd, opal-data-inf,
    opal-data-cot);
  - `scheduler.get_schedule`;
  - `logs.filter_log_events` with a bounded `startTime`.
- **Deploy ledgers:** `org/critical_paths/change_management/` and `org/critical_paths/.open_deploys/`.
- **Later investigation rows** in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`. A later
  row may already record the remedy, for example a DISARM row.

**What you produce:**
1. `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~116/E1_RECONCILE_ROUNDS_42_46.json` is a JSON list with
   one object per row: `{"id", "remediation_file", "class", "close_condition", "verdict": "HOLDS" | "LIVE", "read"}`.
   - `read` is the exact evidence you read now: the command and what it returned, a commit hash, a CodeSha256, an object key with
     its LastModified.
   - **HOLDS** means the close condition is true now.
   - **LIVE** means it is not, or cannot be shown. Then `read` says what was missing, and you add `"next"`: the one concrete
     remedy still owed.
2. **For every HOLDS row, one closing row** appended to `INVESTIGATION_v1.md`, in the channel's existing format (copy the shape of
   IRPT_BCKEND-S319):
   - `"id"`: the next free `IRPT_BCKEND-S<n>` at the time you append (re-read the file right before appending);
   - `"disposition": "DISMISSED_WITH_REASON"`, `"class": "OBSERVATION"`, `"hazard_standing": "INERT"`,
     `"disarm_owner": "2.0.0_SA_COO~P"`;
   - a `"one_line"` beginning `CLOSE of <row id>:`;
   - `"grounding": {"status": "GROUNDED", "evidence": [your read]}`, `"spec_asserts"`, `"world_is"` and `"dismissal_reason"`.
   You may close several rows in one appended row only when one read proves them all; name every id in its `one_line`.
3. Commit with safe-commit as you go. The surprise-row gate grades each appended row at commit.

**Do not edit any REMEDIATION file.** REMEDIATION rows stay the CVO's; your closing rows are what the CVO reads. When in doubt, the
verdict is LIVE: a wrong close hides a live defect, and a wrong LIVE costs one more cell.

<criterion id="IB47-1-AC1" cell_refs="IB-pr-313"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r47/p47_e1_reconcile.py" . IB47-1-AC1</invocation><expect>IB47-1-AC1 PASS</expect></criterion>
`IB47-1-AC1` -- the reconciliation file holds exactly the 42 census ids, each with verdict HOLDS or LIVE and a non-empty
close_condition and read. Base: FAIL.

<criterion id="IB47-1-AC2" cell_refs="IB-pr-313"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r47/p47_e1_reconcile.py" . IB47-1-AC2</invocation><expect>IB47-1-AC2 PASS</expect></criterion>
`IB47-1-AC2` -- every HOLDS row has a DISMISSED_WITH_REASON row appended to the channel since the base that names it. Base: FAIL.

<criterion id="IB47-1-AC3" cell_refs="IB-pr-313"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r47/p47_e1_reconcile.py" . IB47-1-AC3</invocation><expect>IB47-1-AC3 PASS</expect></criterion>
`IB47-1-AC3` -- a GUARD: your commits touch no REMEDIATION file and nothing outside IRPT_BCKEND. Base: PASS.

<expected_criteria>IB47-1-AC1,IB47-1-AC2,IB47-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** reads only. No write, no apply, no invoke, no SSM.
- **Refusal clause.** An edit to a REMEDIATION file, any code or infrastructure change, or any AWS write is a defect: stop and
  file a row.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~116/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-313.reconcile-42-not-closed-rows.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 40 (round 47, workstream ~P), cell `IB-pr-313`.
<owned_cells>IB-pr-313</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB47-1-AC1, IB47-1-AC2, IB47-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~116/IRPT_BCKEND.TO-IB-pr-313.reconcile-42-not-closed-rows.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB47-1-AC1,IB47-1-AC2,IB47-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes; the HOLDS and LIVE counts; the LIVE rows as a list in the order you would
fix them (BLOCKING first, each with its `next`); each criterion's last line; and any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- read-only reconciliation; 0 served bytes move, no code or infrastructure changes.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: schedules are read, never changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB47-1-AC1 base FAIL, IB47-1-AC2 base FAIL (no file), IB47-1-AC3 base PASS (guard; first dry-run read the shared tree's dirt and was recut to the worker's own commits), dry-run at base 2fd59da001 2026-10-04 ~21:3xZ. Census: 42 rows by latest copy across REMEDIATION_v1..v19 (388 rows parsed), matching the CTO's count.
lane: the <paths> block IS the grant.
</preflight>
