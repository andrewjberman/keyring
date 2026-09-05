# TO NFRA_OUTSET.TO-OS-s-10 -- THE SEAM (PRD s.3): each outset tool publishes an ARTIFACT the report host reads -- answer state, vintage, denominators; a failed publish reads FAILED, never absent

<to_id>NFRA_OUTSET.TO-OS-s-10</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.9.0_WK_NFRA_OUTSET~1</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- 2026-09-05 ~09:3xZ, flipped by the ASSIGNEE `0.9.0_WK_NFRA_OUTSET~1` on branch `wk-OUTSET-1` (LOCAL, never pushed), after and only after the proof validated. CRITERIA: 1 MECHANICAL PASS-by-output, 1 JUDGMENT RECORDED with NO verdict (`O10-AC2`, graded by `3.0.0_SA_CVO` at L9). `O10-AC1` -> `python .tools/tests/test_os10_seam.py` rc=0, `OS10-SEAM BATTERY: 12/12 PASS (denominator 12; 0 AWS calls, 0 network)`; the RED mutant the criterion names replaces the consumer's ABSENT branch with a clean-empty result in a temporary copy of the runner, and under it a MISSING artifact renders `status=OK row_count=0` with the report printing `zero rows -- this is a RESULT, the instrument ran and found nothing`, while production on the same missing artifact renders `INSTRUMENT_FAILED` -- a failed publish reading as ABSENT, exactly the lie `_stratum()`'s own docstring says must never happen. `O10-AC2` -> RECORDED. WHAT WAS BUILT: the seam in two halves, and the split is forced rather than chosen -- the report host's systemd unit pulls exactly one file (`instance.tf:215`) and has no estate workspace, so the PRODUCER (`org/modules/heatmap/outset_seam.py`) and the CONSUMER (inside `_stratum_propagation`) can never import each other, and battery arm B is the contract test that keeps their vocabularies aligned in both directions. FOUR FACTS, FOUR RENDERINGS: not configured -> `INSTRUMENT_UNAVAILABLE` (today's behaviour, kept); configured-but-absent -> `INSTRUMENT_FAILED`; unreadable/stale -> `INSTRUMENT_FAILED` with the measured age; read -> the tool's own state, vintage and denominators. EVERY VALUE CARRIES ITS CLAIM, because two honesty problems surfaced on real tools: `comp-heat drift --json` emits no `answer_state` at all and `comp-heat freshness --json` emits `null` on a HEALTHY answer, so the artifact carries `answer_state_claim="inferred (...)"`; and `denominators` is never null. A hole in this worker's own control was found and closed: staleness is ONE-SIDED, so a future-dated artifact could never trip it -- a >0.5 h future artifact is now refused as clock skew, with its own arm. THE FALSIFIER DOES NOT FIRE AS STATED, AND THAT IS A MEASUREMENT, NOT A SOFTENING: the 09:00 window is real (EventBridge SCHEDULER `estate-report-0900et`, `cron(0 9 * * ? *)` tz `America/New_York`, ENABLED -- a Rules-only sweep would have read as "no schedule"), and the artifact-on-a-cadence pattern is real AND FRESH for a cloud-reachable tool (`served/comp_learns_status.json`, written 04:01:03Z, 0.18 d old, ~9 h of margin). It does NOT hold for a git-history-shaped tool: no producer exists, 0 of 142 rules, and the estate's one such artifact is frozen 51 days under a CTO ruling that the shape "can NEVER resolve in the Fargate derive". comp-heat's `freshness` and `drift` are git-history-shaped. NO BLOCKING ROW WAS FILED because "cannot be produced" is not what was measured -- what was measured is "is not produced, and NO CELL OF THE 17 OWNS PRODUCING IT"; inflating that would be as wrong as softening it, and `O10-AC2` is judgment=true so the call is not the worker's. THE UNCOVERED MEMBER: PRD s.3 names this shape's cost as "a publishing step and a freshness question per artifact" -- the freshness question has an owner (this cell, built and tested) and the publishing step has none. COMMITS (LOCAL on `wk-OUTSET-1`): `e0095e1502` seam + battery + rows, `e0aa230802` deliverables + regenerated `06_current_state` pair, plus this flip, which also carries a proof correction (`deployed_state` had an invented value the closed enum refused -- see `W1-S21` -- and the PENDING sentinels were re-pinned, OS-s-5's own lesson). ROWS: `NFRA_OUTSET-W1-S18` (OBSERVATION/INERT -- this worker's OWN earlier de-flake of OS-s-2's arm F was INCOMPLETE; the arm failed again on a git-sourced row with HEAD held because the tolerance EQUALLED the tool's 0.01d rounding quantum, and the earlier falsifier churned an untracked mtime so it was structurally incapable of catching it); `NFRA_OUTSET-W1-S19` (OBSERVATION/ARMED, disarm_owner `2.0.0_SA_COO` -- the runner's role holds `s3:GetObject` on exactly four resources and NOTHING on the globgrph bucket, read on the APPLIED plane and confirmed on DESIRED, so the seam cannot be turned on without an `iam.tf` line this order does not grant; handled by defaulting the seam OFF rather than pointing it somewhere unreadable); `NFRA_OUTSET-W1-S20` (OBSERVATION/ARMED -- the cadence measured in both arms, and the unowned publishing step); `NFRA_OUTSET-W1-S21` (OBSERVATION/ARMED -- `PROOF_OF_SPEC.schema.json` closes `deployed_state` to three values, none of which can describe a deploy-scope artifact deliberately not deployed, so this instance records the least-wrong value in a machine-read field with the truth only in adjacent prose). Result: `../deliverables/0.9.0_WK_NFRA_OUTSET~1/the-consumption-seam-artifacts.result.md`; proof: `../deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-10.the-consumption-seam-artifacts.proof_of_spec.json`, `python .tools/proof-of-spec-check.py <instance> O10-AC1,O10-AC2` -> VALID rc=0, 0 violations. GO paired at cut (the spawn IS the GO for a worker face; a seat order is dispatched by its issuance). Authority: PRD v0.1 @`7fb59f239b` RATIFIED on Andrew's "all approved" (FWD-1..FWD-8) @`26da5ec0fa`; decomposition v0.1 @`6f1655f376`; Andrew-direct at this terminal 2026-09-04 ~15:5xZ, VERBATIM: "youre clear, first write every single task order" then "proceed with internal fan out".</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.1 @`7fb59f239b` (s.7 row OS-s-10; s.4 the bar; s.6 the rulings) · **Decomp cell:** `OS-s-10` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.1 @`6f1655f376`) · **outcome_ref:** FWD-3 · **verb:** build · **depends_on:** OS-s-1, OS-s-4

---

## THE CELL

OS-s-10 (PRD s.7): the runner declares the propagation stratum UNAVAILABLE for want of a workspace. The PRD s.3 CHOICE is the artifact shape (the fedobs pattern), NOT a host given the tool chain.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/the-consumption-seam-artifacts.result.md` -- the result document: what you measured, what you changed, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9, and a PASS or FAIL written on one is INVALID.

<criterion id="O10-AC1" cell_refs="OS-s-10"><invocation>python .tools/tests/test_os10_seam.py</invocation><expect>PASS</expect></criterion>
`O10-AC1` -- a battery: one artifact per outset tool carrying answer state, vintage and denominators; plus a RED mutant whose FAILED publish reads ABSENT instead of FAILED.

<criterion id="O10-AC2" cell_refs="OS-s-10" judgment="true"/>
`O10-AC2` -- SHOW one real published artifact and the runner READING it. AND THE FALSIFIER: if the artifacts cannot be produced on a cadence the 09:00 window can rely on, that is PRD s.3's stated falsifier -- file a BLOCKING row saying so and STOP this criterion. It is a SCOPE CHANGE to L2, NOT a cell you fix. Evidence. NO VERDICT.

<expected_criteria>O10-AC1, O10-AC2</expected_criteria>

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
infra/aws/ec2/estate-report-runner/estate_report_runner.py
.tools/tests/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
infra/system/06_current_state.json
infra/system/06_current_state.md
</paths>

⛔ **`infra/system/06_current_state.{json,md}` GRANTED because this cell's `<paths>` TRIGGER THE COMP-SYSTEM GATE, not because the cell edits them.** `safe-commit.sh:789` fires `comp-system --gate --changed` on any pathspec matching `.tools/comp-`, `org/modules/graph/` or the DS deliverables tree, and BLOCKS at `:837` when `06_current_state` is stale -- so the assignee must be able to regenerate and COMMIT that pair or it can edit its surface and then not land it. Added at the drain by the issuer, generalising row `NFRA_OUTSET-W1-S5` from `OS-s-1` to every face in the population that shares the trigger. **A `<paths>` block must name what the GATES require, not only what the CELL touches.**

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> @`6f1655f376` (v0.1), cell `OS-s-10`.
<owned_cells>OS-s-10</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance -- the gate ledger read once for this issuance and quoted in the issuance commit; 0 armed gates name NFRA_OUTSET, comp-heat or the estate-report runner.
comp-iam: DECLARED-NOT-APPLICABLE for a repo-surface cell (no principal, policy or resource is read or changed); ON OS-s-6 and OS-s-7 it is the cell's own instrument and is RUN there.
comp-adversary: DECLARED-NOT-APPLICABLE -- this order is a FRESH CUT with no prior artifact to validate against; comp-adversary composes a validator-context declaration for an existing deliverable, and the first artifact this cell produces is the one it would read. It is the ASSIGNEE's instrument at report time, not the issuer's at cut.
lane: the `<paths>` block above IS the grant (RULING 1, Andrew 2026-09-04 ~04:58Z) -- a worker serial is admitted to exactly these paths while this order is NON-TERMINAL at HEAD, and to its own deliverables folder by the tree convention.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O10-AC1`, `O10-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-10.the-consumption-seam-artifacts.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O10-AC1,O10-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **A `complete` flip WITHDRAWS YOUR OWN GRANT** (the grant is read from a NON-TERMINAL order): flip only when every MECHANICAL criterion PASSES. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (serial / TO / branch / HEAD; BLOCKING; CRITERIA with each invocation and its deciding line; PROOF with rc; ROWS; COMMITS; NEXT). You cannot send or receive messages -- anything you would ask is a surprise row.
