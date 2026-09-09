# TO NFRA_OUTSET.TO-OS-s-5 -- comp-heat federated --sql is BOUNDED like every other subcommand, or refused with its reason -- an unbounded remote query is not a mode

<to_id>NFRA_OUTSET.TO-OS-s-5</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.9.0_WK_NFRA_OUTSET~1</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- 2026-09-05 ~07:2xZ, flipped by the ASSIGNEE `0.9.0_WK_NFRA_OUTSET~1` on branch `wk-OUTSET-1` (LOCAL, never pushed), after and only after the proof validated. CRITERIA: 2 of 2 MECHANICAL, both PASS-by-output; no judgment criterion on this face. `O5-AC1` -> `timeout 120 .tools/comp-heat federated --sql "SELECT 1" --budget 30` rc=0, deciding line `budget: 30 s (flag)`, with the criterion's own second limb satisfied by `comp-heat federated: refusing to dispatch to the LIVE Trino plane -- budget below the transport's own known floor (~200s; _trino_fed.py: '~3-4 min/call')`; 3 of 3 runs, 0 of 3 containing the transport's dispatch banner. STATED PLAINLY RATHER THAN WORKED AROUND: 30 is below the tool's own 200 s floor, so this criterion can only be satisfied on the REFUSAL path, and that is the correct outcome -- the alternative is raising the budget to force a live dispatch, i.e. paying a shared plane to make a criterion look better. `O5-AC2` -> `python .tools/tests/test_os5_sql_bound.py` rc=0, `OS5-SQL-BOUND BATTERY: 10/10 PASS (denominator 10; 10 child runs, 0 live Trino dispatches -- arm Z is the check, not the claim)`. THE DEFECT AND THE FIX: `_trino_fed.py:82` declares `run_federated_query(sqls, *, delay=15, max_attempts=40)`, which bounds the ECS tasks_stopped waiter; `cmd_federated` called it with NEITHER, so every dispatched query waited on a fixed 15x40 = 600 s ceiling no `--budget` could shorten -- the caller's ceiling never reached the transport at all. It now derives both from `clock.remaining()` (build ladder rung 4: the transport already had the parameter, and `.tools/_trino_fed.py` is not in this grant), measured 5x45 = 225 s at `--budget 250` and 5x75 = 375 s at `--budget 400`, monotone; `--budget 0` returns the transport's OWN defaults and says so, because Rule T's `0 = unbounded` means the tool must not invent a ceiling the caller declined; and a WaiterError is reported as `ANSWER-STATE: PARTIAL_OR_BLIND` with rc 3, while refuse-before-dispatch keeps rc 0 (OS-s-1's drained battery asserts it, and refusing IS a complete answer to "should I run this?" whereas a cut after dispatch leaves the caller nothing). `NFRA_OUTSET-W1-S2` IS CLOSED BY LIMB, WHICH IS THE ONLY HONEST WAY TO CLOSE IT: limb 1, the tiny-budget RACE -- DISARMED, and shown NOMINAL rather than elapsed-time by a discrimination test (`--budget 199.9` refuses, `200.1` dispatches, 0.2 s of DECLARED budget apart and nothing in wall-clock); limb 2, the CALLER'S WAIT -- DISARMED by this cell; limb 3, CANCELLING THE REMOTE TASK -- STILL ARMED, because the ECS task ARN never crosses `run_federated_query`'s return and `.tools/_trino_fed.py` is not in this grant. Not disarmed by having reached this cell. LIVE-PLANE DISCIPLINE: 0 Trino dispatches and 0 AWS API calls under this order, and that is CHECKED not asserted -- refusal arms run below the floor, past-the-floor arms run a temporary comp-heat copy beside a STUB transport it imports by construction, and arm Z sweeps every captured child-process output for the real transport's banner (10 outputs, 0 hits). No budget was raised to make anything pass. COMMITS (LOCAL on `wk-OUTSET-1`): `0c7e4cc9bf` code + battery + rows, `7459e1d22f` deliverables + regenerated `06_current_state` pair, plus this flip, which also carries a correction to the proof instance (`7459e1d22f` landed it with a third `controls` key the schema closes out; `proof-of-spec-check` refused it and the evidence was folded into `determinism`). ROWS: `NFRA_OUTSET-W1-S15` (OBSERVATION/ARMED on limb 3, disarm_owner `2.0.0_SA_COO` -- the limb-by-limb close of `W1-S2`); `NFRA_OUTSET-W1-S16` (OBSERVATION/INERT, explicitly NOT BLOCKING -- this face's title needs `.tools/_trino_fed.py` for its third limb and the `<paths>` omits it, but no criterion is stopped and a blocking row on a passing criterion would be a false stop); `NFRA_OUTSET-W1-S17` (OBSERVATION/ARMED -- comp-heat's docstring claims READ-ONLY "never writes to ... any store" while `--sql` passes the statement through unread; deliberately NOT fixed, because an unrequested verb filter is a manufactured gate and a keyword filter over arbitrary SQL is a false sense of safety, and deliberately NOT tested, because proving a write would succeed means issuing one against a live shared store). Result: `../deliverables/0.9.0_WK_NFRA_OUTSET~1/bound-the-arbitrary-federated-query.result.md`; proof: `../deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-5.bound-the-arbitrary-federated-query.proof_of_spec.json`, `python .tools/proof-of-spec-check.py <instance> O5-AC1,O5-AC2` -> VALID rc=0, 0 violations. GO paired at cut (the spawn IS the GO for a worker face; a seat order is dispatched by its issuance). Authority: PRD v0.1 @`7fb59f239b` RATIFIED on Andrew's "all approved" (FWD-1..FWD-8) @`26da5ec0fa`; decomposition v0.1 @`6f1655f376`; Andrew-direct at this terminal 2026-09-04 ~15:5xZ, VERBATIM: "youre clear, first write every single task order" then "proceed with internal fan out".</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.1 @`7fb59f239b` (s.7 row OS-s-5; s.4 the bar; s.6 the rulings) · **Decomp cell:** `OS-s-5` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.1 @`6f1655f376`) · **outcome_ref:** FWD-2 · **verb:** fix · **depends_on:** OS-s-1

---

## THE CELL

OS-s-5 (PRD s.7): `--sql` runs an arbitrary federated query against the live Trino plane with no bound.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/bound-the-arbitrary-federated-query.result.md` -- the result document: what you measured, what you changed, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9, and a PASS or FAIL written on one is INVALID.

<criterion id="O5-AC1" cell_refs="OS-s-5"><invocation>.tools/comp-heat federated --sql "SELECT 1" --budget 30</invocation><expect>budget</expect></criterion>
`O5-AC1` -- the --sql path honours the budget carrier, or refuses naming the reason.

<criterion id="O5-AC2" cell_refs="OS-s-5"><invocation>python .tools/tests/test_os5_sql_bound.py</invocation><expect>PASS</expect></criterion>
`O5-AC2` -- a battery arm with a RED mutant running --sql unbounded.

<expected_criteria>O5-AC1, O5-AC2</expected_criteria>

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
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> @`6f1655f376` (v0.1), cell `OS-s-5`.
<owned_cells>OS-s-5</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance -- the gate ledger read once for this issuance and quoted in the issuance commit; 0 armed gates name NFRA_OUTSET, comp-heat or the estate-report runner.
comp-iam: DECLARED-NOT-APPLICABLE for a repo-surface cell (no principal, policy or resource is read or changed); ON OS-s-6 and OS-s-7 it is the cell's own instrument and is RUN there.
comp-adversary: DECLARED-NOT-APPLICABLE -- this order is a FRESH CUT with no prior artifact to validate against; comp-adversary composes a validator-context declaration for an existing deliverable, and the first artifact this cell produces is the one it would read. It is the ASSIGNEE's instrument at report time, not the issuer's at cut.
lane: the `<paths>` block above IS the grant (RULING 1, Andrew 2026-09-04 ~04:58Z) -- a worker serial is admitted to exactly these paths while this order is NON-TERMINAL at HEAD, and to its own deliverables folder by the tree convention.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O5-AC1`, `O5-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-5.bound-the-arbitrary-federated-query.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O5-AC1,O5-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **A `complete` flip WITHDRAWS YOUR OWN GRANT** (the grant is read from a NON-TERMINAL order): flip only when every MECHANICAL criterion PASSES. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (serial / TO / branch / HEAD; BLOCKING; CRITERIA with each invocation and its deciding line; PROOF with rc; ROWS; COMMITS; NEXT). You cannot send or receive messages -- anything you would ask is a surprise row.
