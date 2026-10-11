# TO DSGN_IRPTV1.TO-IV-e-86 -- a per-outcome state table, read-only: FWD-1 to FWD-23 each DESIRED, APPLIED or EXERCISED with the evidence that says so, or ABSENT

<to_id>DSGN_IRPTV1.TO-IV-e-86</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~45</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's round analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_FROM_WATERMARK_20261002_20261011.md` @10d7d46e49, section 4 item 5 | **Decomp cell:** `IV-e-86` (decomposition v11) | **outcome_ref:** FWD-1 to FWD-23 (the table is the next analysis's input, not a grade) | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-dsgn-irptv1-45`; run everything from its root unless a step says the portal. Your folder is
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~45/`.

**THE CLIENT-DATA RULE (binding):** never print an account number, a client name or a client figure in a commit message, a record, a row or a report.
Fixtures are synthetic.

**The cell (`IV-e-86`).** The CTO's analysis grades no outcome because no seat holds per-outcome evidence. This cell produces that table. It is
read-only and it is NOT a grade.

In `C:/dev/wk-dsgn-irptv1-45`:
1. Read the PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` (v0.18): its ENDPOINT section defines FWD-1 to FWD-23. Print the 23 ids with
   each one's one-line statement.
2. For EACH outcome find the strongest evidence in the repo, in this order: a reviewer grade (the `ADJUDICATION_v*.md` and `REMEDIATION_v*.md` files
   under `org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/`, the two `ledger/ROUND_ANALYSIS.round*.md`), a walk or real-run record (the deliverables
   folders, `STATUS.md`, the old lane's drive logs under `org/tier1_exec/2.0.0_SA_COO~D/`), a landed commit (a task order `complete` with a VALID
   proof instance). Use `comp-find` and native Grep on named folders; never a blind recursive grep.
3. State, one of:
   - `EXERCISED`: a record shows the outcome's own act performed on a running page or a real entry point, and you cite it;
   - `APPLIED`: the code or data is landed (a commit, a terminal order) and no exercise record exists;
   - `DESIRED`: stated in the PRD and neither landed nor exercised as far as the repo shows.
   Evidence is a list of {kind (grade / walk / commit / order), ref (path with line, or commit hash)}, or the literal `ABSENT` (only under DESIRED).
   Cite what the record SAYS, with its date; a status word in `STATUS.md` or `project.json` alone is a claim, not evidence, and you mark it so.
4. Write `FWD_STATE_TABLE.json` {prd_version, outcomes: [{id, statement, state, evidence, note}]} and a one-page `.md` table. Under `not_established`
   list every outcome whose state you could not settle between two values, and why.

<criterion id="IV86-AC1" cell_refs="IV-e-86"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r11/p11_round11.py" . IV86-AC1</invocation><expect>IV86-AC1 PASS</expect></criterion>
`IV86-AC1` -- all 23 outcomes carry one of the three states with cited evidence or ABSENT, and no APPLIED or EXERCISED state stands on ABSENT. Base: FAIL.

<expected_criteria>IV86-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no vendor call, no secret read, no `bun install`, no download of any
  package, script or program.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. An edit outside the grant, a filled figure, or a client identifier in a committed file is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W45-S<k>`, with the real current UTC time.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~45/
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~45/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-86.fwd-state-table.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v11 (round 11), cell `IV-e-86`.
<owned_cells>IV-e-86</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV86-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~45/DSGN_IRPTV1.TO-IV-e-86.fwd-state-table.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV86-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: commit hashes in each repo, each criterion's last line, what you measured, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only table; no product, contract or infra edit.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched; nothing is deployed.
comp-adversary: RUN -- IV86-AC1 FAIL at base (no record). CTO round analysis @10d7d46e49.
lane: the <paths> block IS the grant.
</preflight>
