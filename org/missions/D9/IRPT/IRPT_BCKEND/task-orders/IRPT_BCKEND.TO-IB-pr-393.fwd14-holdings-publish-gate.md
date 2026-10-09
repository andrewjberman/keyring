# TO IRPT_BCKEND.TO-IB-pr-393 -- FWD-14: the holdings publish gate -- a WORSE candidate (six conditions) does not re-point; the last good publication keeps serving; one refusal record per firm

<to_id>IRPT_BCKEND.TO-IB-pr-393</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~261</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>98</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** PRD v0.31 + v0.32 @97826891e9 (both halves signed, CTO msg 2655); Andrew-direct @f8e7d992dd | **Decomp cell:** `IB-pr-393` (decomposition section 91) |
**outcome_ref:** FWD-14 | **depends_on:** none for the code. The release follows IB-pr-383's after-read, under its own pair.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-261` (branch `wk-IRPT_BCKEND-261`, cut from `box/dell2`). Work and commit only there. Paths are
relative to the worktree. Keep scratch OUTSIDE the worktree.

**The cell: FWD-14, the holdings publish gate** (PRD `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @97826891e9, FWD-14 at
~line 119 and ADDENDA v0.31 and v0.32; Andrew-direct @f8e7d992dd). Read FWD-14's DONE WHEN, ACCEPT, PROOF and CONSTRAINT in full first; the
PRD text wins over this summary.

- **Where:** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, in its publish step (`HoldingsPublication`, the
  `current/manifest.json` re-point).
- **The comparison:** before a firm's index moves, compare the candidate with the publication the firm serves NOW. WORSE is any of the six
  conditions the PRD names:
  - the four S392 conditions: reconcile difference above 0.01; any multi_asset; any class outside the six; a security classified in the
    served publication that is unclassified in the candidate;
  - an account lost;
  - a stale source frontier, read with `lib/trading_calendar.py`, so a Monday is never stale against a Friday.
  - EXCEPTION (v0.32): an account the firm's source records as closed or terminated is LISTED, never refused.
- **WORSE:** do NOT re-point. The firm keeps its last good publication. Write ONE refusal record per firm, beside the manifest, at a
  `lib/opal_naming.py` `address()` path. A builder refusal is a missing registry row to add (rule 30), never a hand-typed path.
- **Equal or better:** re-point as today.
- **Constraint:** a gate on the producer's own write, never a monitor or alert.

**Tests:** in `data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py`, at least 9 tests with names containing
`publish_gate`:
- one per WORSE condition (6), each refused with the prior kept;
- a closed or terminated account listed, not refused;
- an equal-or-better candidate re-points;
- the refusal record written at its `address()` path.

**QA trace (DONE WHEN):** ONE seat-driven run, offline against fixture or real-shaped inputs with nothing published live, with both arms.
- Worse arm: one classified security's class dropped. The outcome is REFUSED, the refusal record is written, and the index is unchanged.
- Restored arm: the class put back. The outcome is PUBLISHED and the index is re-pointed.

Write the trace to `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~261/IB98-2_publish_gate_qa_trace.json` as
`{same_run: true, worse: {outcome, refusal_record, index_moved}, restored: {outcome, index_moved}}`.

Code and tests only. The deploy is a never-widen pair after this cell.

Prove each criterion by running its invocation from the worktree root.

<criterion id="IB98-2-AC1" cell_refs="IB-pr-393"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r98/p98_fwd14.py" . IB98-2-AC1</invocation><expect>IB98-2-AC1 PASS</expect></criterion>
<criterion id="IB98-2-AC2" cell_refs="IB-pr-393"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r98/p98_fwd14.py" . IB98-2-AC2</invocation><expect>IB98-2-AC2 PASS</expect></criterion>

<expected_criteria>IB98-2-AC1, IB98-2-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code and tests only: no build, upload, apply or deploy. AWS reads only, if any.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W261-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~261" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~261@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~261 <0.9.0_WK_IRPT_BCKEND~261@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool, outside the worktree.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py
infra/logic/registry/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-393.fwd14-holdings-publish-gate.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~261/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 91 (round 98, workstream ~P), cell `IB-pr-393`.
<owned_cells>IB-pr-393</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB98-2-AC1, IB98-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~261/IRPT_BCKEND.TO-IB-pr-393.fwd14-holdings-publish-gate.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give what you built and where, the commit hashes, each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- PRD v0.31 + v0.32 @97826891e9 (both halves signed, CTO msg 2655); Andrew-direct @f8e7d992dd; code + tests only in this cell; its release follows IB-pr-383 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; any IAM is DESIRED code for the release pair.
comp-routes: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; a route, if needed, is DESIRED code for the release pair.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p98_fwd14.py dry-run at base 8f73005546 on dell2 2026-10-09 ~06:3xZ: new-test criteria FAIL (0 selected), suite criteria PASS as control; 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO msgs 2621, 2655); the FWD-14 deploy is a never-widen pair after the cell.
</preflight>
