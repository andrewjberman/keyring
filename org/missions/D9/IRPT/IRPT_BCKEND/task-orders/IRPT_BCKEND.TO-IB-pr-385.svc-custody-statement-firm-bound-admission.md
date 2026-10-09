# TO IRPT_BCKEND.TO-IB-pr-385 -- verified_internal_subject admits ONE named, firm-bound service subject, svc-custody-statement

<to_id>IRPT_BCKEND.TO-IB-pr-385</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~196</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>95</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO msg 2311 (on ~K2 msgs 2304/2305) and msg 2351 (cut now, code-only) | **Decomp cell:** `IB-pr-385` (decomposition section 88) |
**outcome_ref:** FWD-8 / IRPT_CUSTDY E2a (a real Performance client statement submission) | **depends_on:** none for the code. The release follows IB-pr-383's after-read, under its own pair.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-196` (branch `wk-IRPT_BCKEND-196`, cut from `box/dell2`). Work and commit only there. Paths are
relative to the worktree. Keep scratch OUTSIDE the worktree.

**The gap.** custody-report-persist, POST /analysis and POST /export gate on `verified_internal_subject` (`infra/aws/lambda/investor-reporting/_authz/served.py:261-272`),
which admits only opal-capital or Dev. A cottonwood token is refused. An opal-capital token could select ANY firm (`served.py:1127-1138`).
IRPT_CUSTDY E2a needs one service token for its scoped POST.

**Your cell.**
1. Admit exactly ONE named service subject, `svc-custody-statement`, on those three routes.
   - Its firm comes ONLY from the verified token claim (cottonwood).
   - It never reaches the opal-capital any-firm selection, and never ALL.
   - Every other service subject is refused exactly as today.
   - Name the subject from the existing svc pattern (`svc-analyst-intake`, CTO msg 2124). Do not type a new pattern.
2. Write the tests in `infra/aws/lambda/investor-reporting/_authz/tests/test_svc_custody_statement.py`, names containing `svc_custody_statement`, at least 5:
   - cottonwood admitted on each of the 3 routes;
   - 49financial and inflection claims refused;
   - no any-firm or ALL selection;
   - another service subject refused.
   The whole `_authz/tests` suite still passes.

Prove each criterion by running its invocation from the worktree root.

<criterion id="IB95-2-AC1" cell_refs="IB-pr-385"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r95/p95_svc.py" . IB95-2-AC1</invocation><expect>IB95-2-AC1 PASS</expect></criterion>
<criterion id="IB95-2-AC2" cell_refs="IB-pr-385"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r95/p95_svc.py" . IB95-2-AC2</invocation><expect>IB95-2-AC2 PASS</expect></criterion>

<expected_criteria>IB95-2-AC1, IB95-2-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code and tests only: no build, upload, apply or deploy. AWS reads only, if any.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W196-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~196" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~196@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~196 <0.9.0_WK_IRPT_BCKEND~196@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool, outside the worktree.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_authz/tests/test_svc_custody_statement.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-385.svc-custody-statement-firm-bound-admission.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~196/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 88 (round 95, workstream ~P), cell `IB-pr-385`.
<owned_cells>IB-pr-385</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB95-2-AC1, IB95-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~196/IRPT_BCKEND.TO-IB-pr-385.svc-custody-statement-firm-bound-admission.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give what you built and where, the commit hashes, each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- CTO msg 2311 (on ~K2 msgs 2304/2305) and msg 2351 (cut now, code-only); code + tests only in this cell; its release follows IB-pr-383 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; any IAM is DESIRED code for the release pair.
comp-routes: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; a route, if needed, is DESIRED code for the release pair.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p95_svc.py dry-run at base 6172924378 on dell2 2026-10-09 ~03:5xZ: new-test criteria FAIL (0 selected), suite criteria PASS as control; 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's code (CTO msgs 2151, 2311, 2340, 2351).
</preflight>
