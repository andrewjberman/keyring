# TO IRPT_BCKEND.TO-IB-pr-365 -- comp-tagauthz's IAM read is bounded: a verdict in bounded time on a real default_tags tree, a forced overrun fails CLOSED with a named reason, and S334 is disarmed

<to_id>IRPT_BCKEND.TO-IB-pr-365</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~173</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>78</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO round analysis ADDENDUM 1 @e4ad79e976 (msg 1344), E4, on the laptop
`1.0.0_SA_CTO` ruling relayed as msg 1342 | **Decomp cell:** `IB-pr-365` (decomposition section 71) | **outcome_ref:** row S334 |
**depends_on:** none.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-173` (branch `wk-IRPT_BCKEND-173`). Work and commit only there. Paths below are
relative to it.

**The defect (row IRPT_BCKEND-S334).** `.tools/safe-apply.sh` gates every apply of a Terraform tree that sets `default_tags`
with `.tools/comp-tagauthz` (a bash wrapper over `.tools/comp-tagauthz.py`). Its `sh()` helper (line ~39) runs
`aws iam get-account-authorization-details --output json` through `subprocess.run` with NO timeout. On the laptop that read made
no progress for 30+ minutes, so the gate never answered. On dell2 it returns in about 26-61 s. The defect is the unbounded read.

**Your cell: bound that read.**
- Add a timeout to the IAM read, from env `COMP_TAGAUTHZ_IAM_TIMEOUT` (seconds). Pick a default comfortably above the measured
  61 s and at most 200 s.
- On timeout the gate must FAIL CLOSED: exit 1, the same could-not-evaluate code safe-apply already blocks on. It must print one line
  naming the token `TAGAUTHZ_IAM_READ_TIMEOUT`, the bound, and the command.
- A narrower read is allowed in addition, if it keeps every policy Condition the gate needs; you would have to show that.
- Change nothing else in the gate's logic or exit codes. Do not edit `.tools/safe-apply.sh`.

**Commit lane (the CTO's ruling).** `.tools/comp-tagauthz.py` belongs to `0.5.0_AE_OpalETL`. Commit that file in its OWN commit,
with `GIT_COMMIT_AUTHOR_OVERRIDE=0.5.0_AE_OpalETL` set in the environment. The message body must name "laptop 1.0.0_SA_CTO ruling,
msg 1342 (relayed); CTO analysis ADDENDUM 1 @e4ad79e976". The override is audited in `org/git-author-override-audit.log`; that
file is in your grant.

**Then the row.** Append ONE row `IRPT_BCKEND-W173-S1` to the channel. Use `"disposition": "DISMISSED_WITH_REASON"`. The
`dismissal_reason` STARTS with `Resolves IRPT_BCKEND-S334:` and names your comp-tagauthz commit hash, plus both criteria's
last lines. `class` is OBSERVATION and `hazard_standing` is INERT. Copy the field set of the rows above it.

<criterion id="IB78-1-AC1" cell_refs="IB-pr-365"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r78/p78_cells.py" . IB78-1-AC1</invocation><expect>IB78-1-AC1 PASS</expect></criterion>
`IB78-1-AC1` -- the gate, run on the real default_tags tree `infra/aws/terraform/investor-reporting/export` with one candidate,
returns rc 0 or 2 within 240 s under your default bound; the elapsed seconds are printed. (No regression: this passes at base on dell2.)

<criterion id="IB78-1-AC2" cell_refs="IB-pr-365"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r78/p78_cells.py" . IB78-1-AC2</invocation><expect>IB78-1-AC2 PASS</expect></criterion>
`IB78-1-AC2` -- with `COMP_TAGAUTHZ_IAM_TIMEOUT=1` the same run exits 1 and the output names `TAGAUTHZ_IAM_READ_TIMEOUT`. Base: FAIL.

<criterion id="IB78-1-AC3" cell_refs="IB-pr-365"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r78/p78_cells.py" . IB78-1-AC3</invocation><expect>IB78-1-AC3 PASS</expect></criterion>
`IB78-1-AC3` -- a row whose dismissal_reason starts `Resolves IRPT_BCKEND-S334` names a commit that changes
`.tools/comp-tagauthz.py`. Base: FAIL.

<expected_criteria>IB78-1-AC1, IB78-1-AC2, IB78-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block and nothing else. No AWS write; the IAM read is the only AWS call the checks make.
- **The `.py` edit passes `.tools/commit-gate.sh`** (py_compile, ds-precommit, ruff py39); safe-commit runs it.
- **Refusal clause.** If a criterion cannot be met as written, stop, file a row `IRPT_BCKEND-W173-S<k>`, and report. Never
  weaken a check.
- **Row ids** are `IRPT_BCKEND-W173-S<k>`. Re-read the channel right before you append. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~173" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~173@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~173 <0.9.0_WK_IRPT_BCKEND~173@opal.agent>" -F <msgfile> -- <paths>`.
  Add `GIT_COMMIT_AUTHOR_OVERRIDE=0.5.0_AE_OpalETL` ONLY for the comp-tagauthz.py commit. Do NOT pre-`git add`. Write the
  message file with the Write tool.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
.tools/comp-tagauthz.py
org/git-author-override-audit.log
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-365.comp-tagauthz-iam-read-bounded.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~173/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 71 (round 78, workstream ~P), cell `IB-pr-365`.
<owned_cells>IB-pr-365</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB78-1-AC1, IB78-1-AC2, IB78-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~173/IRPT_BCKEND.TO-IB-pr-365.comp-tagauthz-iam-read-bounded.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the commit hashes, the default bound you chose, each criterion's last line, and the row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one file, .tools/comp-tagauthz.py; its one caller is .tools/safe-apply.sh (COMP_TAGAUTHZ, rc 0/2/1 contract unchanged).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission changes; the read is the existing iam get-account-authorization-details.
comp-routes: DECLARED-NOT-APPLICABLE -- no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p78_cells.py (cut as p77b_cells.py, same body) dry-run at base 212717f781 on dell2 2026-10-08 ~17:5xZ: AC1 PASS (rc 0, 61.4 s), AC2 FAIL (rc 0, no bound), AC3 FAIL (no row).
lane: the <paths> block IS the grant; .tools/comp-tagauthz.py under GIT_COMMIT_AUTHOR_OVERRIDE=0.5.0_AE_OpalETL per the laptop CTO ruling msg 1342.
</preflight>
