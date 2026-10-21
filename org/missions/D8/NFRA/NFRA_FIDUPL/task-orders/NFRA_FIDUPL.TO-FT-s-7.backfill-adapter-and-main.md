# TO NFRA_FIDUPL.TO-FT-s-7 -- backfill-adapter-and-main -- the empirical earliest date, one business day per window

<to_id>NFRA_FIDUPL.TO-FT-s-7</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~8</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3-backfill</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-7` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 6) | **outcome_ref:** FWD-6 |
**depends_on:** FT-s-4 (the runner's interface, reference section 12; built on fakes in parallel)

---

## WORKER FACE

### THE CELL

**FT-s-7** -- Andrew's method for the backfill (CTO relay of Andrew-direct): go back day by day until the channel refuses or returns empty, land what it gives, and report per file type the earliest business date landed, the total volume, and any hard limit with its evidence. The measured calls already exist: `fetch.fetch_day(session, date_string, out_dir)` lists the exports of one `dateString` (`status.json`) and downloads them (`downloadExport.do`). So one business day is one window. You build the real adapter that gives the planner and the runner (`backfill.py`, `backfill_run.py`) an `ExportClient`, and the box command that runs it.

**Read first (paths in your worktree):** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` sections 1, 5, 6, 7, 9, 12; `infra/aws/ec2/canonical-fidelity/fetch.py` (`fetch_day`, `FetchError`, `PlaywrightSession`), `backfill.py` (the `ExportClient` abstract class, `EntitlementRefused`, `RetentionLimit`, `plan_windows`), `land.py` (`land`, the run record, `DATE_COLUMN`), `box/run.py` (how it signs in and lands: copy its shape) and `signin.py` (`open_session`, `Session.close` logs out).

### WHAT TO BUILD

1. **`backfill_adapter.py`** (python 3.9): `FetchDayClient(session, fetch_day, workdir)` implementing the planner's `ExportClient`: `request_export(kind, g, date_from, date_to)` returns a job naming the business day `date_to`; `wait(job)` calls `fetch_day(session, "<YYYY-MM-DD>", <workdir>/<day>)` ONCE per day (the measured `dateString` format has dashes: `box/run.py` passes the business day this way; the CRO's research `C:/Dev/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261021_NFRA_FIDUPL_EXPORT_CALLS_FOR_BACKFILL.md` probe 1 confirms it and says the Export Status list reaches 120 days back, so `--max-days` defaults to 125 and the stop evidence for an empty listing is `empty listing`) (cache the result: the six files of a day come together, so the other kinds of that day reuse it) and returns `"served"` when the listing carries files; an EMPTY listing raises `RetentionLimit`; an HTTP refusal (`FetchError` that carries a 401, 403 or 404-class status) raises `EntitlementRefused`; any other failure propagates. `download(job)` returns the day's folder for the lander. The G number argument is accepted and never printed.
2. **`backfill_main.py`** (python 3.9, the box command): `main(argv=None, deps=None)` with `--max-days` (default 125), `--max-exports` (default 12 per run, the runner's cap), `--max-sessions` (default 2 per New York day). It reads `config.json` like `box/run.py`, applies the session-count rule through `backfill_run`'s `records.sessions_today()` (counting the run records under `fidelity/<scope>/bronze/_runs/<today>/` that carry a `backfill: true` marker: write that marker in this command's records), signs in ONCE through `signin.open_session`, builds the `FetchDayClient` and the lander (`land.land` on the day's folder, scope from the config), calls `backfill_run.run(...)`, closes the session (it logs out), and writes the COMPLETION RECORD beside the run records: `address('fidelity', <scope>, 'bronze', '_runs', <today>, 'backfill-<run id>.json')` through the builder: per file type (`position`, `prices`, `security`, `account`, `balance`, `transact`) the earliest business date landed, the total number of days and bytes landed, and the stop: `{"reason": "retention|entitlement|run_cap|open_date|none", "evidence": "<the HTTP status class or 'empty listing'>"}`. Printed output: counts and dates only, never a G number, a label, a credential or a file content.
3. Five tests in `tests/test_backfill_adapter.py` (names in the criterion): fakes for the session, `fetch_day`, the lander and the clock.
**Fakes only.** No AWS call, no live call, no sign-in, no real secret, no real export file; synthetic data. ASCII, Python 3.9 syntax, ruff py39 clean.

### ACCEPTANCE

<criterion id="FT-s-7-AC1" cell_refs="FT-s-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft7</invocation><expect>R1-FT7-OK passed=\d+</expect></criterion>
`FT-s-7-AC1` -- the five named tests exist and pass.

<expected_criteria>FT-s-7-AC1</expected_criteria>

Dry-run at the base: `FT-s-7-AC1` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder. Everything else named here you READ.
- **WORLD by the floor** (GATE xii floors any `infra/` path), fakes in effect. Nothing runs on the box or at Fidelity from this order.
- **Refusal clause.** A premise that fails is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
infra/aws/ec2/canonical-fidelity/backfill_adapter.py
infra/aws/ec2/canonical-fidelity/backfill_main.py
infra/aws/ec2/canonical-fidelity/tests/test_backfill_adapter.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 6 addendum), cell `FT-s-7`.
<owned_cells>FT-s-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-7-AC1. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~8/NFRA_FIDUPL.TO-FT-s-7.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-7-AC1` BEFORE the flip. Commit the work first, then pin.
</proof_of_spec>

**REPORT:** the criterion with output verbatim, the proof instance, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- built on fakes; runs when the live backfill pass touches the surface.
lane: the paths block.
</preflight>

Source: CTO relay of Andrew-direct (MSTR 8912, 01:27Z); the first landed day (run record run-20261021T012004Z).
