# TO NFRA_OUTSET.TO-OS-s-16 -- a RANKED archive-candidate list with a reason per line a person can dispute -- and NOTHING is removed by the tool

<to_id>NFRA_OUTSET.TO-OS-s-16</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.9.0_WK_NFRA_OUTSET~1</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- 2026-09-05 ~10:3xZ, flipped by the ASSIGNEE `0.9.0_WK_NFRA_OUTSET~1` on branch `wk-OUTSET-1` (LOCAL, never pushed), after and only after the proof validated. CRITERIA: 1 MECHANICAL PASS-by-output, 1 JUDGMENT RECORDED with NO verdict (`O16-AC2`, graded by `3.0.0_SA_CVO` at L9). THE GATE FIRST: `OS-s-15`'s own `<status>` at HEAD, read with `git show HEAD:` rather than from the checkout, states verbatim "none of O2/O3/O4 is a RETIRE-CANDIDATE, so `OS-s-16` is NOT struck by this ruling -- and it is a WIRE, not a build", so `O16-AC2`'s STOP branch does not apply and no row was filed against it. `O16-AC1` -> `python .tools/tests/test_os16_archive_answer.py` rc=0, `OS16-ARCHIVE-ANSWER BATTERY: 10/10 PASS (denominator 10; every mutant run confined to a tempfile repo, 0 files removed from this estate)`; the RED mutant the criterion names splices `shutil.rmtree` into a temporary copy of comp-heat, removed 8 files from its THROWAWAY tree, and arm C's path+sha256 snapshot saw it while production on its own tree stayed byte-identical over 39 files -- so the integrity check is a control and not a promise. `O16-AC2` -> RECORDED: one real ranked answer, whole estate, rc=0 in 21.8 s, `364 maximal cold subtree(s) found across 4165 directory(ies) rolled up from 30702 scored path(s); 5 assessed, 359 UNASSESSED`, `0 RECOMMEND_ARCHIVE / 5 HOLD_REFERENCED`, every line carrying its numbers and a DISPUTE IT BY clause and the tail printed as "NOT cleared, just not examined". THE CELL IS A WIRE: O1 `build_budgeted`, O2 `aggregate_tree` + `maximal_cold_subtrees`, O3 `assess` all already existed and none had a caller; what was added is `comp-heat archive` plus one `timeout_s` parameter so O3's git pass takes its bound from Rule T's `clock.remaining()` (default unchanged, so every pre-existing caller behaves identically). `NFRA_OUTSET-W3-S4` IS DISARMED, BOTH HALVES, and the measurement that row deferred to this cell is made: on the real corpus `freshness`'s flat grouping lists 1,412 cold LEAF DIRS while the roll-up finds 364 MAXIMAL cold subtrees, and 50 of those 364 roots NEVER APPEAR in the flat list at all (`org/tier3_junior`, `tools`, `data/black_diamond`, `org/tier2_senior/0.4.0_DS_ClientPlatform/logs` among them); O2's own coverage disclosure reads clustered 30,704 of 30,704, so nothing was silently unplaced. The false label is gone -- `freshness` now prints "cold LEAF DIRS (immediate-parent grouping) -- NOT a subtree roll-up" and names `comp-heat archive` -- with the JSON key `cold_subtrees` UNCHANGED (a rename breaks consumers) and `cold_subtrees_basis` added beside it. RESIDUE NAMED RATHER THAN IMPLIED: `freshness`'s COMPUTATION is unchanged, which is now a correctly-labelled answer to a different question one subcommand from the roll-up. NEVER-AUTO-DELETE (R-5) was ENFORCED, not asserted: nothing was removed, moved or renamed by any production run, in the estate or in any temp tree, and 0 of the 5 top-ranked candidates reached RECOMMEND -- nothing in this estate is being proposed for archive today, and every RECOMMEND anywhere still carries a `comp-blast` graph gate this tool does NOT run. COMMITS (LOCAL on `wk-OUTSET-1`): `90e19829d8` wire + battery + rows, `b829b5a6ed` deliverables + regenerated `06_current_state` pair, plus this flip. ROWS: `NFRA_OUTSET-W1-S22` (OBSERVATION/INERT -- the W3-S4 disarm record with the deferred measurement); `NFRA_OUTSET-W1-S23` (OBSERVATION/ARMED, disarm_owner `2.0.0_SA_COO` -- O3's inbound check matches a candidate's path as a BARE SUBSTRING, measured on `tools` where a file carries 5 substring hits and ZERO real references, so a shallow candidate can essentially never reach RECOMMEND; direction is over-HOLD so R-5 is not breached, and it was deliberately NOT fixed because `object_recommend.py` IS in this grant and anchoring the pattern would make an ARCHIVE recommender less conservative -- a ruling's call, not a worker's mid-cell judgement). Result: `../deliverables/0.9.0_WK_NFRA_OUTSET~1/the-archive-candidate-answer.result.md`; proof: `../deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-16.the-archive-candidate-answer.proof_of_spec.json`, `python .tools/proof-of-spec-check.py <instance> O16-AC1,O16-AC2` -> VALID rc=0, 0 violations. GO paired at cut (the spawn IS the GO for a worker face; a seat order is dispatched by its issuance). Authority: PRD v0.1 @`7fb59f239b` RATIFIED on Andrew's "all approved" (FWD-1..FWD-8) @`26da5ec0fa`; decomposition v0.1 @`6f1655f376`; Andrew-direct at this terminal 2026-09-04 ~15:5xZ, VERBATIM: "youre clear, first write every single task order" then "proceed with internal fan out".</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.1 @`7fb59f239b` (s.7 row OS-s-16; s.4 the bar; s.6 the rulings) · **Decomp cell:** `OS-s-16` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.1 @`6f1655f376`) · **outcome_ref:** FWD-8 · **verb:** build · **depends_on:** OS-s-15

---

## THE CELL

OS-s-16 (PRD s.7): nothing answers "what is safe to put away" through the rail.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/the-archive-candidate-answer.result.md` -- the result document: what you measured, what you changed, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9, and a PASS or FAIL written on one is INVALID.

<criterion id="O16-AC1" cell_refs="OS-s-16"><invocation>python .tools/tests/test_os16_archive_answer.py</invocation><expect>PASS</expect></criterion>
`O16-AC1` -- a battery: the answer RANKS with a reason per line, and a RED mutant that DELETES or MOVES anything fails the arm.

<criterion id="O16-AC2" cell_refs="OS-s-16" judgment="true"/>
`O16-AC2` -- GATED ON OS-s-15: if OS-s-15 decided RETIRE for the leg this cell builds on, STOP and file a row -- DO NOT build against a retired leg. If BUILD, show one real ranked answer with its reasons and its denominator. Evidence. NO VERDICT.

<expected_criteria>O16-AC1, O16-AC2</expected_criteria>

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
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> @`6f1655f376` (v0.1), cell `OS-s-16`.
<owned_cells>OS-s-16</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance -- the gate ledger read once for this issuance and quoted in the issuance commit; 0 armed gates name NFRA_OUTSET, comp-heat or the estate-report runner.
comp-iam: DECLARED-NOT-APPLICABLE for a repo-surface cell (no principal, policy or resource is read or changed); ON OS-s-6 and OS-s-7 it is the cell's own instrument and is RUN there.
comp-adversary: DECLARED-NOT-APPLICABLE -- this order is a FRESH CUT with no prior artifact to validate against; comp-adversary composes a validator-context declaration for an existing deliverable, and the first artifact this cell produces is the one it would read. It is the ASSIGNEE's instrument at report time, not the issuer's at cut.
lane: the `<paths>` block above IS the grant (RULING 1, Andrew 2026-09-04 ~04:58Z) -- a worker serial is admitted to exactly these paths while this order is NON-TERMINAL at HEAD, and to its own deliverables folder by the tree convention.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O16-AC1`, `O16-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-16.the-archive-candidate-answer.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O16-AC1,O16-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **A `complete` flip WITHDRAWS YOUR OWN GRANT** (the grant is read from a NON-TERMINAL order): flip only when every MECHANICAL criterion PASSES. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (serial / TO / branch / HEAD; BLOCKING; CRITERIA with each invocation and its deciding line; PROOF with rc; ROWS; COMMITS; NEXT). You cannot send or receive messages -- anything you would ask is a surprise row.
