# TO NFRA_OUTSET.TO-OS-s-1 -- comp-heat honours a caller ceiling on ALL FIVE subcommands -- the Rule T form, the reached denominator, the resume cursor, and an rc that is never clean at expiry

<to_id>NFRA_OUTSET.TO-OS-s-1</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.9.0_WK_NFRA_OUTSET~1</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO paired at cut (the spawn IS the GO for a worker face; a seat order is dispatched by its issuance). Authority: PRD v0.1 @`7fb59f239b` RATIFIED on Andrew's "all approved" (FWD-1..FWD-8) @`26da5ec0fa`; decomposition v0.1 @`6f1655f376`; Andrew-direct at this terminal 2026-09-04 ~15:5xZ, VERBATIM: "youre clear, first write every single task order" then "proceed with internal fan out".</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.1 @`7fb59f239b` (s.7 row OS-s-1; s.4 the bar; s.6 the rulings) · **Decomp cell:** `OS-s-1` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.1 @`6f1655f376`) · **outcome_ref:** FWD-1 · **verb:** fix · **depends_on:** --

---

## THE CELL

OS-s-1 (PRD s.7): `.tools/comp-heat` has NO `--budget` anywhere in 415 lines; 25 flag/def hits, zero budget; T20-AC4 is a standing FAIL. Rule T is the estate form at PRD s.4.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/rule-t-budget-across-comp-heat.result.md` -- the result document: what you measured, what you changed, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9, and a PASS or FAIL written on one is INVALID.

<criterion id="O1-AC1" cell_refs="OS-s-1"><invocation>.tools/comp-heat --help</invocation><expect>--budget</expect></criterion>
`O1-AC1` -- `--help` DISCLOSES the budget carrier -- flag > COMP_BUDGET_S > default, in the s.4.4 form.

<criterion id="O1-AC2" cell_refs="OS-s-1"><invocation>.tools/comp-heat freshness .tools --budget 5</invocation><expect>WITHIN BUDGET</expect></criterion>
`O1-AC2` -- a completing run prints WITHIN BUDGET with `scanned n of N`.

<criterion id="O1-AC3" cell_refs="OS-s-1"><invocation>.tools/comp-heat freshness --budget 0.001</invocation><expect>BUDGET REACHED</expect></criterion>
`O1-AC3` -- a cut run prints BUDGET REACHED with its REACHED denominator, never a silent partial.

<criterion id="O1-AC4" cell_refs="OS-s-1"><invocation>python .tools/tests/test_os1_budget_battery.py</invocation><expect>PASS</expect></criterion>
`O1-AC4` -- a NEW battery: one arm per subcommand (freshness, drift, score, compare, federated) plus a RED mutant that ignores --budget; each arm prints its own denominator.

<criterion id="O1-AC5" cell_refs="OS-s-1"><invocation>bash .tools/commit-gate.sh .tools/comp-heat</invocation><expect>pre-commit gate clean</expect></criterion>
`O1-AC5` -- the commit gate is clean on every .py/.sh this order touches.

<criterion id="O1-AC6" cell_refs="OS-s-1" judgment="true"/>
`O1-AC6` -- THE VERDICT-BEARING LIMB, graded by the CVO at L9: for any subcommand whose rc carries a verdict, the rc at BUDGET REACHED must be a NON-CLEAN value distinct from BOTH the clean and the failing verdict, carrying PARTIAL_OR_BLIND in the tool's own voice. RECORD the rc of each subcommand at a cut budget and at a clean run, side by side. NO VERDICT.

<expected_criteria>O1-AC1, O1-AC2, O1-AC3, O1-AC4, O1-AC5, O1-AC6</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below and nothing else.** A path you need that it does not name is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.
- **EVERY invocation is bounded.** You run each under `timeout 120` and a timeout is RECORDED AS THE OUTPUT -- so an unbounded command yields a criterion whose evidence is the word "timeout". Use a tool's own `--budget`/`--limit`; never name a whole-corpus sweep.
- **No new dependency. No second implementation.** PRD s.5 is out of scope and truthful non-application is not work.
- **NEVER-AUTO-DELETE (PRD R-5, absolute):** nothing is removed by a tool; a candidate list is advisory.
- **No alarm, monitor, freshness-checker or SNS** (standing moratorium).
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_OUTSET-W<n>-S<k>` for a worker (`<n>` = your slot) and `NFRA_OUTSET-S<k>` for a seat -- append, cite `path@commit`, never edit an existing row, keep working.
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote`).

<paths>
.tools/comp-heat
org/modules/heatmap/
.tools/_compbudget.py
.tools/tests/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> @`6f1655f376` (v0.1), cell `OS-s-1`.
<owned_cells>OS-s-1</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance -- the gate ledger read once for this issuance and quoted in the issuance commit; 0 armed gates name NFRA_OUTSET, comp-heat or the estate-report runner.
comp-iam: DECLARED-NOT-APPLICABLE for a repo-surface cell (no principal, policy or resource is read or changed); ON OS-s-6 and OS-s-7 it is the cell's own instrument and is RUN there.
comp-adversary: DECLARED-NOT-APPLICABLE -- this order is a FRESH CUT with no prior artifact to validate against; comp-adversary composes a validator-context declaration for an existing deliverable, and the first artifact this cell produces is the one it would read. It is the ASSIGNEE's instrument at report time, not the issuer's at cut.
lane: the `<paths>` block above IS the grant (RULING 1, Andrew 2026-09-04 ~04:58Z) -- a worker serial is admitted to exactly these paths while this order is NON-TERMINAL at HEAD, and to its own deliverables folder by the tree convention.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O1-AC1`, `O1-AC2`, `O1-AC3`, `O1-AC4`, `O1-AC5`, `O1-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-1.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O1-AC1,O1-AC2,O1-AC3,O1-AC4,O1-AC5,O1-AC6` BEFORE the complete flip, which the assignee commits itself.
⛔ **A `complete` flip WITHDRAWS YOUR OWN GRANT** (the grant is read from a NON-TERMINAL order): flip only when every MECHANICAL criterion PASSES. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (serial / TO / branch / HEAD; BLOCKING; CRITERIA with each invocation and its deciding line; PROOF with rc; ROWS; COMMITS; NEXT). You cannot send or receive messages -- anything you would ask is a surprise row.
