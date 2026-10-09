# TO IRPT_BCKEND.TO-IB-pr-392 -- H1 WITHDRAWN before any apply: remove the READY event-source mapping and its kms:Decrypt grant (IRPT_ANLREQ I3 is the one trigger)

<to_id>IRPT_BCKEND.TO-IB-pr-392</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~260</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>98</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO msg 2621 (ruling @19c5067e12; rescinds msg 2507 (a)); ~Y2 msg 2610 | **Decomp cell:** `IB-pr-392` (decomposition section 91) |
**outcome_ref:** NFRA_TRNSPT FWD-10 (one trigger, I3) | **depends_on:** none for the code. The release follows IB-pr-383's after-read, under its own pair.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-260` (branch `wk-IRPT_BCKEND-260`, cut from `box/dell2`). Work and commit only there. Paths are
relative to the worktree. Keep scratch OUTSIDE the worktree.

**The cell (CTO msg 2621, ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_IRPT_BCKEND_IB_pr_388_H1_WITHDRAWN_20261009.md`
@19c5067e12; on ~Y2 msg 2610).** H1 is WITHDRAWN before any apply. IRPT_ANLREQ's I3 queue (AR-t-11) is the one trigger for the commentary
Lambda. With H1 as well, it would draft twice per READY and re-open the grant CTO msg 2341 forbids. Nothing was ever planned or applied.

**Do:**
1. Delete `infra/aws/terraform/investor-reporting/core/ready_trigger.tf`, the file IB-pr-388 added. That removes:
   - the event-source mapping;
   - the inline policy (4 stream actions plus kms:Decrypt);
   - the two data sources.
2. Keep the table's stream (`stream_enabled` / `stream_view_type`) and the `requests_stream_arn` output in `dynamodb.tf` / `outputs.tf`
   unless the ruling file says otherwise. Read it.
3. Leave no reference to the commentary role or its DLQ in the core root.

No plan, no apply.

Prove each criterion by running its invocation from the worktree root.

<criterion id="IB98-1-AC1" cell_refs="IB-pr-392"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r98/p98_h1_withdraw.py" . IB98-1-AC1</invocation><expect>IB98-1-AC1 PASS</expect></criterion>
<criterion id="IB98-1-AC2" cell_refs="IB-pr-392"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r98/p98_h1_withdraw.py" . IB98-1-AC2</invocation><expect>IB98-1-AC2 PASS</expect></criterion>

<expected_criteria>IB98-1-AC1, IB98-1-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code and tests only: no build, upload, apply or deploy. AWS reads only, if any.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W260-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~260" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~260@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~260 <0.9.0_WK_IRPT_BCKEND~260@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool, outside the worktree.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/terraform/investor-reporting/core/ready_trigger.tf
infra/aws/terraform/investor-reporting/core/dynamodb.tf
infra/aws/terraform/investor-reporting/core/outputs.tf
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-392.h1-withdrawn-remove-ready-trigger.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~260/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 91 (round 98, workstream ~P), cell `IB-pr-392`.
<owned_cells>IB-pr-392</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB98-1-AC1, IB98-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~260/IRPT_BCKEND.TO-IB-pr-392.h1-withdrawn-remove-ready-trigger.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give what you built and where, the commit hashes, each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- CTO msg 2621 (ruling @19c5067e12; rescinds msg 2507 (a)); ~Y2 msg 2610; code + tests only in this cell; its release follows IB-pr-383 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; any IAM is DESIRED code for the release pair.
comp-routes: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; a route, if needed, is DESIRED code for the release pair.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p98_h1_withdraw.py dry-run at base 8f73005546 on dell2 2026-10-09 ~06:3xZ: new-test criteria FAIL (0 selected), suite criteria PASS as control; 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO msgs 2621, 2655); the FWD-14 deploy is a never-widen pair after the cell.
</preflight>
