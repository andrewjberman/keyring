# TO NFRA_OUTSET.TO-OS-s-2 -- comp-heat freshness answers at a PATH grain with that corner's own denominator, not the whole repo's

<to_id>NFRA_OUTSET.TO-OS-s-2</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.9.0_WK_NFRA_OUTSET~1</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- 2026-09-05 ~04:0xZ, flipped by the ASSIGNEE `0.9.0_WK_NFRA_OUTSET~1` on branch `wk-OUTSET-1` (LOCAL, never pushed), after and only after the proof validated. CRITERIA: 3 of 3 MECHANICAL, all PASS-by-output; no judgment criterion on this face. `O2-AC1` -> `timeout 120 .tools/comp-heat freshness .tools --budget 60` rc=0, deciding line `denominator: 388 of 388 files under .tools/ -- PATH-SCOPED to this corner, NOT the whole repository` (was `scanned 30543 of 30543 files` at `79ec54bb37`), basis block prints. `O2-AC2` -> same tool on `org/modules/heatmap` rc=0, `denominator: 8 of 8 files under org/modules/heatmap/` (was `30544 of 30544`) -- the number MOVES with the path, 8 vs 388 vs 30563 no-path, each checked against an INDEPENDENT `git ls-files` census. `O2-AC3` -> `python .tools/tests/test_os2_path_grain.py` rc=0, `OS2-PATH-GRAIN BATTERY: 10/10 PASS (denominator 10)`, carrying both arms the criterion names: E (the no-path form still scores the whole repo, 30563) and H (a RED MUTANT neutering `_scope_pathspec()` in a temporary engine copy OUTSIDE the repo makes a scoped call return the repo denominator again, 30563 instead of 8). THE GRADED QUANTITY IS A COUNT, NOT A DURATION, deliberately: `O1-AC2` was first mis-graded by ranking warm-cache runs over cold ones, and neither recency nor repetition is a provenance axis. Timings are disclosed (engine `used` 5.25s -> 0.55-1.22s) and are NOT load-bearing; the structural claim rests on battery arm G, which reads the git ARGV in process with a negative control, and arm F, which shows the cheaper answer is the SAME answer (key-diff 0, band-diff 0, age-diff 0 over 388 of 388). COMMITS (LOCAL on `wk-OUTSET-1`): `2282527e51` code + battery + rows, `2f9b158342` deliverables + regenerated `06_current_state` pair, plus this flip. ROWS: `NFRA_OUTSET-W1-S10` (OBSERVATION/INERT -- the DISARM RECORD for `W1-S1`/`W1-S6`/`W1-S8`; the path-scoped git call is real, and the residual is named: the NO-PATH form still walks the whole history by design, so their hazard is closed for a NAMED CORNER only); `NFRA_OUTSET-W1-S11` (OBSERVATION/ARMED, disarm_owner `2.0.0_SA_COO` -- the `infra/system/06_current_state` grant this cut added is NECESSARY BUT NOT SUFFICIENT for a linked-worktree worker: comp-system refuses to compile from an uncommitted source, and `safe-commit.sh:789` resolves `comp-system` through a PATH shim hard-coded to the MAIN workspace, so the gate deciding a WORKTREE commit grades a different tree -- discriminated by two different target fingerprints from one baseline). Result: `../deliverables/0.9.0_WK_NFRA_OUTSET~1/freshness-at-a-path-grain.result.md`; proof: `../deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-2.freshness-at-a-path-grain.proof_of_spec.json`, `python .tools/proof-of-spec-check.py <instance> O2-AC1,O2-AC2,O2-AC3` -> VALID rc=0, 0 violations, read POST-COMMIT against the committed bytes at `2f9b158342`. GO paired at cut (the spawn IS the GO for a worker face; a seat order is dispatched by its issuance). Authority: PRD v0.1 @`7fb59f239b` RATIFIED on Andrew's "all approved" (FWD-1..FWD-8) @`26da5ec0fa`; decomposition v0.1 @`6f1655f376`; Andrew-direct at this terminal 2026-09-04 ~15:5xZ, VERBATIM: "youre clear, first write every single task order" then "proceed with internal fan out".</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.1 @`7fb59f239b` (s.7 row OS-s-2; s.4 the bar; s.6 the rulings) · **Decomp cell:** `OS-s-2` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.1 @`6f1655f376`) · **outcome_ref:** FWD-1 · **verb:** fix · **depends_on:** OS-s-1

---

## THE CELL

OS-s-2 (PRD s.7): `freshness .tools --json` returns rc 0 in 9 s over 382 paths, but the no-path form scores the whole repo. A caller naming one corner must get that corner's denominator.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/freshness-at-a-path-grain.result.md` -- the result document: what you measured, what you changed, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9, and a PASS or FAIL written on one is INVALID.

<criterion id="O2-AC1" cell_refs="OS-s-2"><invocation>.tools/comp-heat freshness .tools --budget 60</invocation><expect>denominator</expect></criterion>
`O2-AC1` -- a named corner answers with THAT corner's denominator, and the basis block prints.

<criterion id="O2-AC2" cell_refs="OS-s-2"><invocation>.tools/comp-heat freshness org/modules/heatmap --budget 60</invocation><expect>denominator</expect></criterion>
`O2-AC2` -- a second, smaller corner answers with its own denominator -- the number MOVES with the path, which is the whole claim.

<criterion id="O2-AC3" cell_refs="OS-s-2"><invocation>python .tools/tests/test_os2_path_grain.py</invocation><expect>PASS</expect></criterion>
`O2-AC3` -- a battery arm proving the no-path form still scores the whole repo, plus a RED mutant returning the repo denominator for a scoped call.

<expected_criteria>O2-AC1, O2-AC2, O2-AC3</expected_criteria>

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
.tools/tests/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
infra/system/06_current_state.json
infra/system/06_current_state.md
</paths>

⛔ **`infra/system/06_current_state.{json,md}` GRANTED because this cell's `<paths>` TRIGGER THE COMP-SYSTEM GATE, not because the cell edits them.** `safe-commit.sh:789` fires `comp-system --gate --changed` on any pathspec matching `.tools/comp-`, `org/modules/graph/` or the DS deliverables tree, and BLOCKS at `:837` when `06_current_state` is stale -- so the assignee must be able to regenerate and COMMIT that pair or it can edit its surface and then not land it. Added at the drain by the issuer, generalising row `NFRA_OUTSET-W1-S5` from `OS-s-1` to every face in the population that shares the trigger. **A `<paths>` block must name what the GATES require, not only what the CELL touches.**

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> @`6f1655f376` (v0.1), cell `OS-s-2`.
<owned_cells>OS-s-2</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance -- the gate ledger read once for this issuance and quoted in the issuance commit; 0 armed gates name NFRA_OUTSET, comp-heat or the estate-report runner.
comp-iam: DECLARED-NOT-APPLICABLE for a repo-surface cell (no principal, policy or resource is read or changed); ON OS-s-6 and OS-s-7 it is the cell's own instrument and is RUN there.
comp-adversary: DECLARED-NOT-APPLICABLE -- this order is a FRESH CUT with no prior artifact to validate against; comp-adversary composes a validator-context declaration for an existing deliverable, and the first artifact this cell produces is the one it would read. It is the ASSIGNEE's instrument at report time, not the issuer's at cut.
lane: the `<paths>` block above IS the grant (RULING 1, Andrew 2026-09-04 ~04:58Z) -- a worker serial is admitted to exactly these paths while this order is NON-TERMINAL at HEAD, and to its own deliverables folder by the tree convention.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O2-AC1`, `O2-AC2`, `O2-AC3`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-2.freshness-at-a-path-grain.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O2-AC1,O2-AC2,O2-AC3` BEFORE the complete flip, which the assignee commits itself.
⛔ **A `complete` flip WITHDRAWS YOUR OWN GRANT** (the grant is read from a NON-TERMINAL order): flip only when every MECHANICAL criterion PASSES. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (serial / TO / branch / HEAD; BLOCKING; CRITERIA with each invocation and its deciding line; PROOF with rc; ROWS; COMMITS; NEXT). You cannot send or receive messages -- anything you would ask is a surprise row.
