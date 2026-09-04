# TO NFRA_OUTSET.TO-OS-s-7 -- the code_heat parquet behind the federated join -- its refresh CADENCE and its OWNER, measured from the producer

<to_id>NFRA_OUTSET.TO-OS-s-7</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.7.0_AE_CloudOps</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO paired at cut (the spawn IS the GO for a worker face; a seat order is dispatched by its issuance). Authority: PRD v0.1 @`7fb59f239b` RATIFIED on Andrew's "all approved" (FWD-1..FWD-8) @`26da5ec0fa`; decomposition v0.1 @`6f1655f376`; Andrew-direct at this terminal 2026-09-04 ~15:5xZ, VERBATIM: "youre clear, first write every single task order" then "proceed with internal fan out".</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.1 @`7fb59f239b` (s.7 row OS-s-7; s.4 the bar; s.6 the rulings) · **Decomp cell:** `OS-s-7` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.1 @`6f1655f376`) · **outcome_ref:** FWD-2, FWD-3 · **verb:** audit · **depends_on:** --

---

## THE CELL

OS-s-7 (PRD s.7, brief precondition P3, UNMEASURED): the parquet is glue-bound; its refresh cadence and owner are unknown, and OS-s-4 prints its build time.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps/code-heat-parquet-cadence-and-owner.result.md` -- the result document: what you measured, what you changed, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9, and a PASS or FAIL written on one is INVALID.

<criterion id="O7-AC1" cell_refs="OS-s-7" judgment="true"/>
`O7-AC1` -- THE CADENCE, from the PRODUCER and not from the artifact's appearance: what writes code_heat, on what schedule, and when it last ran. A glue-bound artifact's own timestamp is NOT its cadence. Evidence with vintage. NO VERDICT.

<criterion id="O7-AC2" cell_refs="OS-s-7" judgment="true"/>
`O7-AC2` -- THE OWNER: the seat or system accountable for that refresh, named. If no owner exists, SAY SO PLAINLY -- an unowned artifact under a daily join is the finding, not a gap in the audit.

<expected_criteria>O7-AC1, O7-AC2</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below and nothing else.** A path you need that it does not name is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.
- **EVERY invocation is bounded.** You run each under `timeout 120` and a timeout is RECORDED AS THE OUTPUT -- so an unbounded command yields a criterion whose evidence is the word "timeout". Use a tool's own `--budget`/`--limit`; never name a whole-corpus sweep.
- **No new dependency. No second implementation.** PRD s.5 is out of scope and truthful non-application is not work.
- **NEVER-AUTO-DELETE (PRD R-5, absolute):** nothing is removed by a tool; a candidate list is advisory.
- **No alarm, monitor, freshness-checker or SNS** (standing moratorium).
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_OUTSET-W<n>-S<k>` for a worker (`<n>` = your slot) and `NFRA_OUTSET-S<k>` for a seat -- append, cite `path@commit`, never edit an existing row, keep working.
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote`).

<paths>
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> @`6f1655f376` (v0.1), cell `OS-s-7`.
<owned_cells>OS-s-7</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance -- the gate ledger read once for this issuance and quoted in the issuance commit; 0 armed gates name NFRA_OUTSET, comp-heat or the estate-report runner.
comp-iam: DECLARED-NOT-APPLICABLE for a repo-surface cell (no principal, policy or resource is read or changed); ON OS-s-6 and OS-s-7 it is the cell's own instrument and is RUN there.
comp-adversary: DECLARED-NOT-APPLICABLE -- this order is a FRESH CUT with no prior artifact to validate against; comp-adversary composes a validator-context declaration for an existing deliverable, and the first artifact this cell produces is the one it would read. It is the ASSIGNEE's instrument at report time, not the issuer's at cut.
lane: the `<paths>` block above IS the grant (RULING 1, Andrew 2026-09-04 ~04:58Z) -- a worker serial is admitted to exactly these paths while this order is NON-TERMINAL at HEAD, and to its own deliverables folder by the tree convention.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O7-AC1`, `O7-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps/NFRA_OUTSET.TO-OS-s-7.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O7-AC1,O7-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **A `complete` flip WITHDRAWS YOUR OWN GRANT** (the grant is read from a NON-TERMINAL order): flip only when every MECHANICAL criterion PASSES. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO` with per-criterion evidence, denominators, and push state as MEASURED.
