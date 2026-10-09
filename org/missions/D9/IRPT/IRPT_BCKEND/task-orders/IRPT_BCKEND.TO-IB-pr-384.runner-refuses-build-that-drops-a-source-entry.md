# TO IRPT_BCKEND.TO-IB-pr-384 -- the directory runner REFUSES to land a build that drops an entry the source still holds (row D2-W189-S4)

<to_id>IRPT_BCKEND.TO-IB-pr-384</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~195</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>95</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO msg 2151 (S4: yes, after 383) and msg 2351 (cut now, code-only); row D2-S23 (stale root header removal rides here) | **Decomp cell:** `IB-pr-384` (decomposition section 88) |
**outcome_ref:** FWD-7 (a build fault never reaches the served directory) | **depends_on:** none for the code. The release follows IB-pr-383's after-read, under its own pair.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-195` (branch `wk-IRPT_BCKEND-195`, cut from `box/dell2`). Work and commit only there. Paths are
relative to the worktree. Keep scratch OUTSIDE the worktree.

**The gap (row D2-W189-S4).** `data/assets/scripts/gold/investor_reporting/directory_runner.py` `land()` writes `directory.json` and
`latest.json` whatever the refresh's verdict. A build that drops an entry the source still holds (a BUILD fault, not a removal) therefore
reaches the served directory, and the refresh's REFRESH_FAILED cannot pull it back. That is how inflection and cottonwood lost entries.

**Your cell.**
1. Before landing, the runner compares the previous served directory, the new build and the source keys (`source_client_ids`, IB-pr-381).
   Then, by case:
   - **An entry that is in the source but missing from the build:** REFUSE the landing with a named error (for example
     `REFUSED: BUILD_DROPS_SOURCE_ENTRY`), print the opaque ids, and make 0 S3 puts.
   - **A genuine source removal:** land it as today, carried TERMINATED.
   - **Unknown source keys:** refuse only when a previous client is missing.
2. Write the tests in `data/assets/scripts/gold/investor_reporting/tests/test_directory_runner_refuse_drop.py`, names containing
   `refuse_drop`, at least 3, one per branch above, with a fake S3 that counts puts. The whole runner suite still passes, excusing only
   the pre-existing red S71 guard, which the check names by exact id.
3. Remove the stale comment clauses in `infra/aws/terraform/investor-reporting/directory/main.tf`: "SKELETON ONLY ... NOT INITIALISED,
   NOT PLANNED, NOT APPLIED" (~:14-18) and "No resources are declared by IB-s-18" (~:52). This is a comment-only edit (row D2-S23).
   Change no HCL.

Prove each criterion by running its invocation from the worktree root.

<criterion id="IB95-1-AC1" cell_refs="IB-pr-384"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r95/p95_s4.py" . IB95-1-AC1</invocation><expect>IB95-1-AC1 PASS</expect></criterion>
<criterion id="IB95-1-AC2" cell_refs="IB-pr-384"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r95/p95_s4.py" . IB95-1-AC2</invocation><expect>IB95-1-AC2 PASS</expect></criterion>

<expected_criteria>IB95-1-AC1, IB95-1-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code and tests only: no build, upload, apply or deploy. AWS reads only, if any.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W195-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~195" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~195@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~195 <0.9.0_WK_IRPT_BCKEND~195@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool, outside the worktree.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
data/assets/scripts/gold/investor_reporting/directory_runner.py
data/assets/scripts/gold/investor_reporting/tests/test_directory_runner_refuse_drop.py
infra/aws/terraform/investor-reporting/directory/main.tf
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-384.runner-refuses-build-that-drops-a-source-entry.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~195/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 88 (round 95, workstream ~P), cell `IB-pr-384`.
<owned_cells>IB-pr-384</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB95-1-AC1, IB95-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~195/IRPT_BCKEND.TO-IB-pr-384.runner-refuses-build-that-drops-a-source-entry.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give what you built and where, the commit hashes, each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- CTO msg 2151 (S4: yes, after 383) and msg 2351 (cut now, code-only); row D2-S23 (stale root header removal rides here); code + tests only in this cell; its release follows IB-pr-383 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; any IAM is DESIRED code for the release pair.
comp-routes: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; a route, if needed, is DESIRED code for the release pair.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p95_s4.py dry-run at base 6172924378 on dell2 2026-10-09 ~03:5xZ: new-test criteria FAIL (0 selected), suite criteria PASS as control; 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's code (CTO msgs 2151, 2311, 2340, 2351).
</preflight>
