# TO NFRA_OUTSET.TO-OS-s-15 -- the heat engine's O2-O4 legs (locality, verify-before-recommend, hygiene report): each REACHABLE from comp-heat under never-auto-delete, or RETIRED with the ruling cited -- a DECISION, not a build

<to_id>NFRA_OUTSET.TO-OS-s-15</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.9.0_WK_NFRA_OUTSET~3</issued_to>
⛔ **`<issued_to>` RE-ADDRESSED from `~1` to `~3` at the drain, and this is an ISSUER defect, not a re-assignment.** The issuance addressed all thirteen worker cells to `~1` because the decomposition's chain read put chain A on ONE slot. Round 2 was then widened to THREE slots on a FILE-CONTENTION read (four cells write `.tools/comp-heat`, so they queue; this cell's surfaces are disjoint, so it runs beside them) -- and the orders were never re-addressed to match. `.tools/owned-paths-validate.py:213-215` keys the worker grant on `_normalize_serial(<issued_to>) == _normalize_serial(agent)`, so the seated worker held NO grant and could not commit finished, green work. Measured by `0.9.0_WK_NFRA_OUTSET~2` on OS-s-8 with a positive control discriminating on the serial alone: 4 of 4 paths granted to `~1`, 0 of 4 to `~2`. Rows `NFRA_OUTSET-W2-S3` (descriptive) and `NFRA_OUTSET-W2-S4` (mechanical, BLOCKING). **A FAN-OUT DECISION IS ALSO AN ADDRESSING ACT: widening the slot count re-addresses every order it moves, or the new slots hold nothing.**

<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- flipped 2026-09-05 by `0.9.0_WK_NFRA_OUTSET~3` (the RE-SEATED assignee. `<issued_to>` was RE-ADDRESSED `~1` -> `~3` by `2.0.0_SA_COO` at `b630052d6a`, ABSORBED HERE AFTER this worker's decision commit `7a0126b323`; the divergence as this worker met it is row `NFRA_OUTSET-W3-S1` and the absorption is row `NFRA_OUTSET-W3-S6`). Both criteria are `judgment="true"`, so NOTHING MECHANICAL PASSED and none was self-graded: each is RECORDED with its evidence and NO verdict, and `3.0.0_SA_CVO` grades them at L9. Proof-of-spec instance VALID: `python .tools/proof-of-spec-check.py org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~3/NFRA_OUTSET.TO-OS-s-15.reachability-of-the-heat-engine-legs.proof_of_spec.json O15-AC1,O15-AC2` -> `violations=0 ... VALID (rc=0)`, surprises limb `4 entries; 4 open with a row id; 4 resolve to a channel row`. THE DECISION: none of O2/O3/O4 is a RETIRE-CANDIDATE, so `OS-s-16` is NOT struck by this ruling -- and it is a WIRE, not a build. Rows filed: `NFRA_OUTSET-W3-S1`..`S5` (`W3-S4` ARMED, disarm needs a `.tools/comp-heat` write this read-only cell did not hold; `W3-S5` BLOCKING-resolved -- the lane gate REFUSED the deliverables write into the `~1` folder this order's `<paths>` grants, so the deliverable and the instance landed in `deliverables/0.9.0_WK_NFRA_OUTSET~3/`, which this order's `<preflight>` separately grants. No override was used. THE `<paths>` BLOCK AND THE LANE GATE DISAGREE ABOUT THAT FOLDER AND THE FIX IS THE ISSUER'S). Nothing was built and nothing removed. ORIGINAL ISSUANCE STATUS BELOW, unchanged: pending -- GO paired at cut (the spawn IS the GO for a worker face; a seat order is dispatched by its issuance). Authority: PRD v0.1 @`7fb59f239b` RATIFIED on Andrew's "all approved" (FWD-1..FWD-8) @`26da5ec0fa`; decomposition v0.1 @`6f1655f376`; Andrew-direct at this terminal 2026-09-04 ~15:5xZ, VERBATIM: "youre clear, first write every single task order" then "proceed with internal fan out".</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.1 @`7fb59f239b` (s.7 row OS-s-15; s.4 the bar; s.6 the rulings) · **Decomp cell:** `OS-s-15` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.1 @`6f1655f376`) · **outcome_ref:** FWD-8 · **verb:** decide · **depends_on:** OS-s-1

---

## THE CELL

OS-s-15 (PRD s.7): seven modules from 2026-06-25 exist under org/modules/heatmap/; the CLI reaches O1 only.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/reachability-of-the-heat-engine-legs.result.md` -- the result document: what you measured, what you changed, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9, and a PASS or FAIL written on one is INVALID.

<criterion id="O15-AC1" cell_refs="OS-s-15" judgment="true"/>
`O15-AC1` -- FOR EACH of object_locality.py, object_recommend.py, object_report.py: state REACHABLE-FROM-CLI or RETIRE-CANDIDATE, with the file:line the CLI would call and the measured fact that the CLI reaches O1 only. A DECISION with its evidence. NOTHING IS BUILT BY THIS CELL. NO VERDICT.

<criterion id="O15-AC2" cell_refs="OS-s-15" judgment="true"/>
`O15-AC2` -- NEVER-AUTO-DELETE (PRD R-5, ABSOLUTE) is restated in your answer for any leg touching removal: the list is advisory and nothing is removed by a tool. A leg that cannot honour that is a RETIRE-CANDIDATE and you say so.

<expected_criteria>O15-AC1, O15-AC2</expected_criteria>

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
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
infra/system/06_current_state.json
infra/system/06_current_state.md
</paths>

⛔ **`infra/system/06_current_state.{json,md}` GRANTED because this cell's `<paths>` TRIGGER THE COMP-SYSTEM GATE, not because the cell edits them.** `safe-commit.sh:789` fires `comp-system --gate --changed` on any pathspec matching `.tools/comp-`, `org/modules/graph/` or the DS deliverables tree, and BLOCKS at `:837` when `06_current_state` is stale -- so the assignee must be able to regenerate and COMMIT that pair or it can edit its surface and then not land it. Added at the drain by the issuer, generalising row `NFRA_OUTSET-W1-S5` from `OS-s-1` to every face in the population that shares the trigger. **A `<paths>` block must name what the GATES require, not only what the CELL touches.**

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> @`6f1655f376` (v0.1), cell `OS-s-15`.
<owned_cells>OS-s-15</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance -- the gate ledger read once for this issuance and quoted in the issuance commit; 0 armed gates name NFRA_OUTSET, comp-heat or the estate-report runner.
comp-iam: DECLARED-NOT-APPLICABLE for a repo-surface cell (no principal, policy or resource is read or changed); ON OS-s-6 and OS-s-7 it is the cell's own instrument and is RUN there.
comp-adversary: DECLARED-NOT-APPLICABLE -- this order is a FRESH CUT with no prior artifact to validate against; comp-adversary composes a validator-context declaration for an existing deliverable, and the first artifact this cell produces is the one it would read. It is the ASSIGNEE's instrument at report time, not the issuer's at cut.
lane: the `<paths>` block above IS the grant (RULING 1, Andrew 2026-09-04 ~04:58Z) -- a worker serial is admitted to exactly these paths while this order is NON-TERMINAL at HEAD, and to its own deliverables folder by the tree convention.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O15-AC1`, `O15-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-15.reachability-of-the-heat-engine-legs.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O15-AC1,O15-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **A `complete` flip WITHDRAWS YOUR OWN GRANT** (the grant is read from a NON-TERMINAL order): flip only when every MECHANICAL criterion PASSES. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (serial / TO / branch / HEAD; BLOCKING; CRITERIA with each invocation and its deciding line; PROOF with rc; ROWS; COMMITS; NEXT). You cannot send or receive messages -- anything you would ask is a surprise row.
