# TO IRPT_BCKEND.TO-IB-pr-396 -- FWD-14 v0.33: where a firm marks no closures (all UNKNOWN), account_lost is listed and never refuses alone

<to_id>IRPT_BCKEND.TO-IB-pr-396</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~263</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>101</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO msg 2738 (PRD v0.33 @13ee60595d, CVO-admitted msg 2744); row D2-W261-S2 | **Decomp cell:** `IB-pr-396` (decomposition section 94) |
**outcome_ref:** FWD-14 | **depends_on:** none for the code. The release follows IB-pr-383's after-read, under its own pair.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-263` (branch `wk-IRPT_BCKEND-263`, cut from `box/dell2`). Work and commit only there. Paths are
relative to the worktree. Keep scratch OUTSIDE the worktree.

**The cell (CTO msg 2738; PRD ADDENDUM v0.33 @13ee60595d, admitted by the CVO, msg 2744).** IB-pr-393 built FWD-14's holdings publish
gate (drained @42793c81fc). Its row D2-W261-S2 found a gap. The v0.32 closed-account exemption reads TERMINATED markings from the landed
directory, but cottonwood marks every entry UNKNOWN. So a closed COT account would be refused as `account_lost` on every fire.

**Build v0.33 into the gate** in `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`:
- For a firm whose directory marks NO closures (no entry carries a TERMINATED or closed termination marking; all UNKNOWN), `account_lost`
  is LISTED in the refusal record's detail but never refuses on its own.
- The other five WORSE conditions still refuse.
- A firm that DOES mark closures keeps v0.32's behaviour: an unmarked lost account is still refused.

**Tests**, in `data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py`, with names containing
`publish_gate_all_unknown`:
- an all-UNKNOWN firm that loses an account PUBLISHES, and its record lists the lost account;
- a closures-marking firm that loses an unmarked account is still REFUSED.

Every existing `publish_gate` test still passes, and so does the runner suite (the S71 guard excused by id). Code and tests only; the
release pair follows.

Prove each criterion by running its invocation from the worktree root.

<criterion id="IB101-1-AC1" cell_refs="IB-pr-396"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r101/p101_v033.py" . IB101-1-AC1</invocation><expect>IB101-1-AC1 PASS</expect></criterion>
<criterion id="IB101-1-AC2" cell_refs="IB-pr-396"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r101/p101_v033.py" . IB101-1-AC2</invocation><expect>IB101-1-AC2 PASS</expect></criterion>

<expected_criteria>IB101-1-AC1, IB101-1-AC2</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code and tests only: no build, upload, apply or deploy. AWS reads only, if any.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W263-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~263" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~263@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~263 <0.9.0_WK_IRPT_BCKEND~263@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool, outside the worktree.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-396.fwd14-v033-all-unknown-account-lost-listed.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~263/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 94 (round 101, workstream ~P), cell `IB-pr-396`.
<owned_cells>IB-pr-396</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB101-1-AC1, IB101-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~263/IRPT_BCKEND.TO-IB-pr-396.fwd14-v033-all-unknown-account-lost-listed.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give what you built and where, the commit hashes, each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- CTO msg 2738 (PRD v0.33 @13ee60595d, CVO-admitted msg 2744); row D2-W261-S2; code + tests only in this cell; its release follows IB-pr-383 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; any IAM is DESIRED code for the release pair.
comp-routes: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; a route, if needed, is DESIRED code for the release pair.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p101_v033.py dry-run at base box/dell2 on dell2 2026-10-09 ~07:0xZ: new-test criteria FAIL (0 selected), suite criteria PASS as control; 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO msg 2738); the FWD-14 release pair follows this cell.
</preflight>
