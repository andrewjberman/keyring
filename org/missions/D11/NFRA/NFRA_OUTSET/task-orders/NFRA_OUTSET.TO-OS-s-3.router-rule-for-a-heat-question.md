# TO NFRA_OUTSET.TO-OS-s-3 -- a plain-English freshness/archive question ROUTES to comp-heat -- the router has no rule for it today

<to_id>NFRA_OUTSET.TO-OS-s-3</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.9.0_WK_NFRA_OUTSET~2</issued_to>
⛔ **RE-ADDRESSED TO `~2` BEFORE SEATING -- BOTH LIMBS, and the second limb is the one two workers had to find the hard way.** A mis-addressed order fails on TWO independent gate limbs, not one: `ADHC_OWNPTH.005` keys the worker grant on `<issued_to>`, AND clause 4 keys it on the DELIVERABLES FOLDER NAME. Amending only `<issued_to>` leaves the assignee admitted to a folder carrying another slot's serial. Measured on OS-s-8 (`NFRA_OUTSET-W2-S4`, 4 of 4 paths granted to `~1` and 0 of 4 to `~2`) and on OS-s-15 (`NFRA_OUTSET-W3-S6`, which corrected my own over-wide claim: only the TREE_DELIVERABLES limb refuses, because `task-orders/**` and the surprise channel are lane ANY and consult no serial). **This face was amended BEFORE its worker was seated rather than after it hit the wall** -- the first time on this project the population question was asked ahead of the second victim instead of behind it.

<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- flipped 2026-09-05 by `0.9.0_WK_NFRA_OUTSET~2` (the assignee, per this order's own <proof_of_spec> clause) AFTER all three mechanical criteria were exercised PASS-by-output and the instance validated. O3-AC1: `.tools/comp-which "what is stale and safe to archive"` -> `1. score 2.00 comp-heat freshness [path]`, rc 0 -- DISCLOSED: this criterion was ALREADY green on the committed router, so its PASS is not evidence of this cell's work (row `NFRA_OUTSET-W2-S9`). O3-AC2: `.tools/comp-which "what have I not touched in months"` -> `1. score 2.00 comp-heat freshness [path]`, rc 0; PRE it produced no route at all and RAN a comp-find content search. O3-AC3 (AMENDED by the issuer at `df14ecd5f1`, carried onto this branch and committed at `d9bd63b35a` BEFORE the re-run): -> `VERDICT: PASS -- controls held, zero pollution, and comp-which ABSTAINED on 100%% of generated gibberish.`, rc 0, 12 min 31 s, with 6 of 6 of the harness's own instrument controls held and `org/tier2_senior/` verified untouched. `python .tools/proof-of-spec-check.py org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~2/NFRA_OUTSET.TO-OS-s-3.router-rule-for-a-heat-question.proof_of_spec.json O3-AC1,O3-AC2,O3-AC3` -> `VALID (rc=0)`; 6 of 6 artifacts resolved at pin, 7 of 7 surprises resolve to a channel row. Rows filed: `NFRA_OUTSET-W2-S7`..`-W2-S13`, five of them still ARMED and none of them closed by this flip. PRIOR STATE, for the record: O3-AC3 was FAIL as originally written -- unsatisfiable on two independent limbs (`NFRA_OUTSET-W2-S7` the bound, `NFRA_OUTSET-W2-S8` the out-of-grant default write) -- and the flip was correctly WITHHELD then, with a VALID rc=0 instance already in hand at `bfa8e86e46`: a valid instance is not a met order. Original issuance status follows. || pending -- GO paired at cut (the spawn IS the GO for a worker face; a seat order is dispatched by its issuance). Authority: PRD v0.1 @`7fb59f239b` RATIFIED on Andrew's "all approved" (FWD-1..FWD-8) @`26da5ec0fa`; decomposition v0.1 @`6f1655f376`; Andrew-direct at this terminal 2026-09-04 ~15:5xZ, VERBATIM: "youre clear, first write every single task order" then "proceed with internal fan out".</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.1 @`7fb59f239b` (s.7 row OS-s-3; s.4 the bar; s.6 the rulings) · **Decomp cell:** `OS-s-3` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.1 @`6f1655f376`) · **outcome_ref:** FWD-1 · **verb:** wire · **depends_on:** OS-s-1, OS-s-2

---

## THE CELL

OS-s-3 (PRD s.7): `comp-which "what is comp-heat"` returns NO CURATED RULE MATCHED across 79 tools ranked, top score 0.36.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~2/router-rule-for-a-heat-question.result.md` -- the result document: what you measured, what you changed, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9, and a PASS or FAIL written on one is INVALID.

<criterion id="O3-AC1" cell_refs="OS-s-3"><invocation>.tools/comp-which "what is stale and safe to archive"</invocation><expect>comp-heat</expect></criterion>
`O3-AC1` -- the question routes to comp-heat rather than NO CURATED RULE MATCHED.

<criterion id="O3-AC2" cell_refs="OS-s-3"><invocation>.tools/comp-which "what have I not touched in months"</invocation><expect>comp-heat</expect></criterion>
`O3-AC2` -- a second phrasing of the same question routes the same way.

<criterion id="O3-AC3" cell_refs="OS-s-3"><invocation>timeout 1200 python .tools/comp-which-routing-test.py --out org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~2/comp-which-routing-baseline.json</invocation><expect>VERDICT: PASS</expect></criterion>
⛔ **AMENDED at the drain on rows `NFRA_OUTSET-W2-S7` and `W2-S8`. BOTH DEFECTS WERE THE ISSUER'S, and the criterion as cut was UNSATISFIABLE.** (1) THE BOUND: `comp-which-routing-test.py:284` shells `comp-which` ONCE PER COHORT QUESTION -- `R_raw 562` + `C 87` plus ~69 self-route probes and ~45 controls, at a MEASURED 1.01 s per invocation, so >= 763 invocations and >= ~770 s. The order's own blanket `timeout 120` is 6.4x too small, and `0.9.0_WK_NFRA_OUTSET~2` proved it empirically: 0 of 3 bounded runs produced a verdict at 120 s x2 and 600 s x1. (2) THE CLOBBER: the literal invocation carried no `--out`, and `:1055-1061` makes the default the shared baseline at `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/comp-which-routing-baseline.json` -- ANOTHER SEAT'S TREE, outside this order's `<paths>`, which the tool's own help calls a re-baseline that only a deliberate act should perform. **Raising the bound WITHOUT adding `--out` would have made that hazard reachable for the first time**, so the two fixes are one fix and neither ships alone.
⭐ **VERIFIED SATISFIABLE BEFORE BEING RE-CUT, because cutting a second unpassable criterion is the error this project has already paid for twice.** This issuer ran the amended invocation itself at `timeout 900` with `--out` to a scratch path: it TERMINATED, rc=0, wrote its baseline, and printed `VERDICT: PASS -- controls held, zero pollution, and comp-which ABSTAINED on 100%% of generated gibberish.` The bound is set to 1200 s to clear the measured floor with margin.
⛔ **THE `timeout 120` BOUND IS CARVED OUT FOR THIS ONE INVOCATION ONLY, and the reason is stated so it is not read as the bound lapsing.** That bound exists so no criterion names an UNBOUNDED sweep; `timeout 1200` is still bounded and a timeout is still RECORDED AS THE OUTPUT. Every other invocation on this face keeps 120 s.
⛔ **AND ONE PIECE OF THE REPORTING EVIDENCE DOES NOT SURVIVE, THOUGH THE CONCLUSION DOES.** `W2-S7` cites `grep -c -E "^\s*(PASS|FAIL)" = 0` as showing no verdict was produced. That detector returns 0 ON A PASSING RUN TOO -- the harness prints `VERDICT: PASS`, so the token never starts a line. The real evidence of non-completion was the expired bound, not the grep. The conclusion was right; one of its instruments was blind.

`O3-AC3` -- the routing battery still passes with the new rule -- the baseline is UPDATED, never broken.

<expected_criteria>O3-AC1, O3-AC2, O3-AC3</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below and nothing else.** A path you need that it does not name is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.
- **EVERY invocation is bounded.** You run each under `timeout 120` and a timeout is RECORDED AS THE OUTPUT -- so an unbounded command yields a criterion whose evidence is the word "timeout". Use a tool's own `--budget`/`--limit`; never name a whole-corpus sweep.
- **No new dependency. No second implementation.** PRD s.5 is out of scope and truthful non-application is not work.
- **NEVER-AUTO-DELETE (PRD R-5, absolute):** nothing is removed by a tool; a candidate list is advisory.
- **No alarm, monitor, freshness-checker or SNS** (standing moratorium).
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_OUTSET-W<n>-S<k>` for a worker (`<n>` = your slot) and `NFRA_OUTSET-S<k>` for a seat -- append, cite `path@commit`, never edit an existing row, keep working.
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote`).

<paths>
.tools/comp-which
.tools/tests/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~2/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
infra/system/06_current_state.json
infra/system/06_current_state.md
</paths>

⛔ **`infra/system/06_current_state.{json,md}` GRANTED because this cell's `<paths>` TRIGGER THE COMP-SYSTEM GATE, not because the cell edits them.** `safe-commit.sh:789` fires `comp-system --gate --changed` on any pathspec matching `.tools/comp-`, `org/modules/graph/` or the DS deliverables tree, and BLOCKS at `:837` when `06_current_state` is stale -- so the assignee must be able to regenerate and COMMIT that pair or it can edit its surface and then not land it. Added at the drain by the issuer, generalising row `NFRA_OUTSET-W1-S5` from `OS-s-1` to every face in the population that shares the trigger. **A `<paths>` block must name what the GATES require, not only what the CELL touches.**

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> @`6f1655f376` (v0.1), cell `OS-s-3`.
<owned_cells>OS-s-3</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance -- the gate ledger read once for this issuance and quoted in the issuance commit; 0 armed gates name NFRA_OUTSET, comp-heat or the estate-report runner.
comp-iam: DECLARED-NOT-APPLICABLE for a repo-surface cell (no principal, policy or resource is read or changed); ON OS-s-6 and OS-s-7 it is the cell's own instrument and is RUN there.
comp-adversary: DECLARED-NOT-APPLICABLE -- this order is a FRESH CUT with no prior artifact to validate against; comp-adversary composes a validator-context declaration for an existing deliverable, and the first artifact this cell produces is the one it would read. It is the ASSIGNEE's instrument at report time, not the issuer's at cut.
lane: the `<paths>` block above IS the grant (RULING 1, Andrew 2026-09-04 ~04:58Z) -- a worker serial is admitted to exactly these paths while this order is NON-TERMINAL at HEAD, and to its own deliverables folder by the tree convention.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O3-AC1`, `O3-AC2`, `O3-AC3`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~2/NFRA_OUTSET.TO-OS-s-3.router-rule-for-a-heat-question.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O3-AC1,O3-AC2,O3-AC3` BEFORE the complete flip, which the assignee commits itself.
⛔ **A `complete` flip WITHDRAWS YOUR OWN GRANT** (the grant is read from a NON-TERMINAL order): flip only when every MECHANICAL criterion PASSES. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (serial / TO / branch / HEAD; BLOCKING; CRITERIA with each invocation and its deciding line; PROOF with rc; ROWS; COMMITS; NEXT). You cannot send or receive messages -- anything you would ask is a surprise row.
