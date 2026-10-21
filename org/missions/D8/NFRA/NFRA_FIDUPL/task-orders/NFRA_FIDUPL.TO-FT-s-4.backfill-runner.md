# TO NFRA_FIDUPL.TO-FT-s-4 -- backfill-runner -- per G the earliest date, a run cap and a daily sign-in cap

<to_id>NFRA_FIDUPL.TO-FT-s-4</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~7</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-4` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 2) | **outcome_ref:** FWD-6 |
**depends_on:** FR-s-3 (the planner, merged)

---

## WORKER FACE

### THE CELL

**FT-s-4** -- Run the backfill: for each G number walk back through the planner's windows (`backfill.py`) as far as Fidelity serves, and keep ONE row per G naming the earliest date reached and why the walk stopped. A run cap and a session-count rule keep one run from exhausting the account: at most `max_exports_per_run` export requests per run, and no new sign-in when the day's recorded sessions have reached `max_sessions_per_day`. The real `ExportClient` adapter waits for Andrew's capture of the on-demand export (decomposition R3 gap 1): this cell builds the runner against an injected client.

**Read first (paths in your worktree):** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` sections 1 (rules), 7 (box layout), 9 to 12 (interfaces; section 12 is this round's); `backfill.py` (the planner, stop detection and per-G per-kind record: use them, do not rewrite them), `land.py` (`land`, `OK_ACTIONS`), the C-BACKFILL row of the PRD `C:/Dev/ajb_workspace/org/missions/D8/NFRA/NFRA_FIDUPL/prd/NFRA_FIDUPL_PRD.md` (read-only, absolute).

### WHAT TO BUILD

1. `backfill_run.py` (python 3.9): `run(plan_inputs, export_client, lander, session_factory, records, caps, now=None)` as in reference section 12. For each G (an ordinal, never the value in any output) call the planner's windows backward; each window is one request through `export_client`; a window served is landed through `lander`; the stop reason is the planner's (`entitlement`, `retention`, `open_date`) or `run_cap` when `max_exports_per_run` is reached (then `remaining` counts the G numbers not started). The per-G record `{"ordinal", "earliest_date", "stop_reason"}` is read at start and a G with a recorded earliest date resumes from it, never refetches landed windows.
2. The session rule: `records.sessions_today()` (injected) returns the count of sign-ins recorded for the current New York day; when it is `>= max_sessions_per_day` the runner returns without calling `session_factory` and says so in the result.
3. Five tests in `tests/test_backfill_run.py` (names in the criterion), fakes only.
**Fakes only.** No AWS call, no live call, no sign-in, no real secret, no real export file; every test uses synthetic data. ASCII, Python 3.9 syntax, ruff py39 clean.

### ACCEPTANCE

<criterion id="FT-s-4-AC1" cell_refs="FT-s-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft4</invocation><expect>R1-FT4-OK passed=\d+</expect></criterion>
`FT-s-4-AC1` -- the five named tests exist and pass.

<expected_criteria>FT-s-4-AC1</expected_criteria>

Dry-run at the base: `FT-s-4-AC1` base: FAIL as expected

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder. Everything else named here you READ.
- **WORLD by the floor**, fakes in effect. Nothing runs on the box or at Fidelity from this order.
- **Refusal clause.** A premise that fails is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
infra/aws/ec2/canonical-fidelity/backfill_run.py
infra/aws/ec2/canonical-fidelity/tests/test_backfill_run.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3), cell `FT-s-4`.
<owned_cells>FT-s-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-4-AC1. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~7/NFRA_FIDUPL.TO-FT-s-4.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-4-AC1` BEFORE the flip. Commit the work first, then pin.
</proof_of_spec>

**REPORT:** the criteria with output verbatim, the proof instance, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- built on fakes; runs when the live round touches the surface.
lane: the paths block.
</preflight>

Source: CTO msgs 8891 and 8909; PRD v0.5 @c4f8dc3d51; the first landed day (run record run-20261021T012004Z).
