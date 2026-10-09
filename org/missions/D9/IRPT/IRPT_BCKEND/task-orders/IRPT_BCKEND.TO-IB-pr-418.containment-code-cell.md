# TO IRPT_BCKEND.TO-IB-pr-418 -- containment item 3: no client account id in the 12 BCKEND code files or TO-IB-er-201; the er-201 proof instance back in the tree, redacted and VALID

<to_id>IRPT_BCKEND.TO-IB-pr-418</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~280</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>117</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO containment ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_CLIENT_ACCOUNT_DATA_IN_REPO_CONTAINMENT_20261009.md` items 2, 3 and AMENDMENT 2 (msgs 3644, 3654, 3698) | **Decomp cell:** `IB-pr-418` (decomposition section 110) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Client data rule (CTO ruling @0e8209c33c item 6).** No account id, balance, fee or flow goes in any tracked file. The repo carries counts,
sha256 and reason codes only. Never print an account id into a commit message, a row or your report.

**The cell.** A HEAD census found real 49F account ids in 12 code files and one complete task order. The account set lives OUTSIDE the
repo: `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~35/TIEOUT_COMPOUND_V2.json`. Read it only to find and
replace ids. Root: `C:/dev/wk-irpt-bckend-280/`.

**Build:**
1. **Code** (the 12 `.py` files in `<paths>`):
   - A real account in a TEST or FIXTURE becomes a synthetic one: a 10-digit id that is NOT in the account set, one stable synthetic id
     per real id across files.
   - A RUNTIME literal (a live-seam check reading real S3) is read from the environment variable `IRPT_THREAD_ACCOUNT` instead. When it
     is unset, the script prints `SKIP: IRPT_THREAD_ACCOUNT unset` and exits 0.
   - Change nothing else. Every file still compiles.
2. **TO-IB-er-201.** Replace its one id with the token `acct#<first 8 hex of sha256("49financial:<account>")>` (AMENDMENT 2's single form).
3. **The er-201 proof instance.** Its bytes were moved out of the tree at `12b257c3ab`; the copy is at
   `C:/dev/_irpt_private_evidence_20261009/IRPT_BCKEND/<same repo path>`.
   - Put it back at its repo path with each id replaced by its token (same form).
   - Its `PENDING-THIS-COMMIT` artifact rows now fail as stale. Pin each to the commit that carried that artifact (`git log --format=%h
     -1 -- <path>` at or before the order's completion) until `proof-of-spec-check.py` reads VALID. Change no verdict.
   - The commit gate grades any edit to a complete order as a flip and needs this instance present and VALID in the same commit. Commit
     the TO and the instance together.

<criterion id="IB117-3-AC1" cell_refs="IB-pr-418"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r117/p117_cells.py" . IB117-3-AC1 --set "C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~35/TIEOUT_COMPOUND_V2.json"</invocation><expect>IB117-3-AC1 PASS</expect></criterion>
<criterion id="IB117-3-AC2" cell_refs="IB-pr-418"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r117/p117_cells.py" . IB117-3-AC2</invocation><expect>IB117-3-AC2 PASS</expect></criterion>

<expected_criteria>IB117-3-AC1, IB117-3-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No AWS, no deploy.
- **The files under `deliverables/2.0.0_SA_COO~P/` and `~142/` are in TREE_DELIVERABLES lanes not your own.** Commit them under
  `GIT_COMMIT_AUTHOR_OVERRIDE=TREE_DELIVERABLES`, audited, as the ruling's item 1 did, with one lane per commit.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W280-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~280" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~280@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~280 <0.9.0_WK_IRPT_BCKEND~280@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~142/make_fixtures_p340.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19/p19_1_ac1_implausible_fixture.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19/p19_1_ac2_live_seam.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19/p19_2_ac1_since_inception_fixture.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19/p19_2_ac2_live_seam.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r19/p19_4_ac1_reopen_fixture.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r1e/e1_ac1_thread_day_recompute.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r1e/e1_ac2_thread_ytd_coverage.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r20/p20_1_ac1_gold_fixture.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r20/p20_1_ac2_gold_live.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r22/p22_1_ac1_inf_gold_fixture.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r27/p27_3_blast_radius.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-er-201.holdings-gold-thread-one-49f-account.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~E/IRPT_BCKEND.TO-IB-er-201.holdings-gold-thread-one-49f-account.proof_of_spec.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~280/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-418.containment-code-cell.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 110 (round 117, workstream ~P), cell `IB-pr-418`.
<owned_cells>IB-pr-418</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB117-3-AC1, IB117-3-AC2. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~280/IRPT_BCKEND.TO-IB-pr-418.containment-code-cell.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the per-file counts (never an id), each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- 12 historical check/fixture scripts and one complete order in this project's tree, plus one proof instance restored redacted; no product code, no AWS.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p117_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~16:5xZ: AC1 FAIL (13 of 13 named files carry an account id), AC2 FAIL (no instance); ruff clean.
lane: the <paths> block IS the grant; ~P's (containment ruling item 3, one cell per project).
</preflight>
