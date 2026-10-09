# TO IRPT_BCKEND.TO-IB-pr-387 -- the PROFILE-row allowedFirmIds narrowing at served.py extends to internal callers (verified identity; non-list refused; ALL never admits)

<to_id>IRPT_BCKEND.TO-IB-pr-387</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~198</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>96</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO msgs 2363 and 2368 (on ~V2 msgs 2359, 2366); census org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.md (21 IRPT routes MORE_THAN_ONE) | **Decomp cell:** `IB-pr-387` (decomposition section 89) |
**outcome_ref:** FWD-8 (an internal caller selects only the firms its profile row allows) | **depends_on:** none for the code. The release follows IB-pr-383's after-read, under its own pair.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-198` (branch `wk-IRPT_BCKEND-198`, cut from `box/dell2`). Work and commit only there. Paths are
relative to the worktree. Keep scratch OUTSIDE the worktree.

**The gap.** `infra/aws/lambda/investor-reporting/_authz/served.py` (~:1134) narrows a SERVICE principal by the `allowedFirmIds` on its maintained PROFILE row
(`_service_allowed_firms`). An internal (OPAL_GLOBAL) caller is not narrowed, so it may select any registry firm. The verified token
carries NO allowedFirmIds claim (portal-authorizer/index.mjs:394-407, CTO msg 2368).

**Your cell.**
1. Extend the existing PROFILE-row narrowing to internal callers, with the row found by the verified identity, the same way the service
   branch finds it.
   - A non-empty list narrows the selectable firms to that list.
   - No row, or an empty list, is unchanged from today.
   - A non-list value is REFUSED (fail closed).
   - `ALL` never admits once a non-empty list is present.
   - Do not read any header for the list, only the maintained row. Keep IB-pr-385's `svc-custody-statement` behaviour exactly.
2. Write the tests in `infra/aws/lambda/investor-reporting/_authz/tests/test_allowed_firm_ids.py`, names containing `allowed_firm_ids`, at least 5:
   - listed firm admitted;
   - unlisted firm refused;
   - no row or empty list unchanged;
   - non-list refused;
   - ALL refused with a non-empty list.
   The whole `_authz/tests` suite still passes, including `test_svc_custody_statement.py`.
3. ~Y2's submission path rides only where your change needs it. Edit only the paths granted.

Prove each criterion by running its invocation from the worktree root.

<criterion id="IB96-1-AC1" cell_refs="IB-pr-387"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r96/p96_cells.py" . IB96-1-AC1</invocation><expect>IB96-1-AC1 PASS</expect></criterion>
<criterion id="IB96-1-AC2" cell_refs="IB-pr-387"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r96/p96_cells.py" . IB96-1-AC2</invocation><expect>IB96-1-AC2 PASS</expect></criterion>

<expected_criteria>IB96-1-AC1, IB96-1-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code and tests only: no build, upload, apply or deploy. AWS reads only, if any.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W198-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~198" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~198@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~198 <0.9.0_WK_IRPT_BCKEND~198@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool, outside the worktree.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_authz/tests/test_allowed_firm_ids.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-387.internal-caller-profile-row-allowed-firm-ids.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~198/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 89 (round 96, workstream ~P), cell `IB-pr-387`.
<owned_cells>IB-pr-387</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB96-1-AC1, IB96-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~198/IRPT_BCKEND.TO-IB-pr-387.internal-caller-profile-row-allowed-firm-ids.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give what you built and where, the commit hashes, each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- CTO msgs 2363 and 2368 (on ~V2 msgs 2359, 2366); census org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.md (21 IRPT routes MORE_THAN_ONE); code + tests only in this cell; its release follows IB-pr-383 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; any IAM is DESIRED code for the release pair.
comp-routes: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; a route, if needed, is DESIRED code for the release pair.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p96_cells.py dry-run at base 1eab5d01a8 on dell2 2026-10-09 ~04:1xZ: new-test criteria FAIL (0 selected), suite criteria PASS as control; 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's code (CTO msgs 2363, 2368); chained after IB-pr-385 (same file, drained @dd02e66933).
</preflight>
