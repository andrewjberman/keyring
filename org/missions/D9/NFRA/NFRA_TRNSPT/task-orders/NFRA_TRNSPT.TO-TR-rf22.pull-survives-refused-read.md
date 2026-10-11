# TO NFRA_TRNSPT.TO-TR-rf22 -- the Teams pull survives a refused content read: record the row, carry on, finish the run

<to_id>NFRA_TRNSPT.TO-TR-rf22</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>pullfix</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-rf-22` (`decompositions/NFRA_TRNSPT_DECOMP_R22.md`, AMENDMENT 2) | **outcome_ref:** FWD-3 |
**depends_on:** NFRA_TRNSPT.TO-TR-rc22 (complete)

---

## WORKER FACE

### THE CELL

`TR-rf-22`: the scheduled Teams pull has failed on every fire since 2026-10-09T16:00Z. Measured cause
(`org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R22_ROOT_CAUSE_LIVE_READ_20261011.md`): the gateway lists 20 `monday_meeting`
transcripts but answers `502 graph_error` to the content read of every one older than about 120 days. In
`data/transcripts/scripts/teams/pull.py` `_pull_series`, that read raises `GatewayGraphError`. The only skip branch is `except Expired`
(line 161), which only the fixture transport raises. So the run dies at the first aged-out row: no run record, no listing snapshot, and
the three later series are never pulled.

**Build (the repo code and its tests only; nothing is deployed by this order):**
1. In `data/transcripts/scripts/teams/pull.py` `_pull_series`: a content read of ONE row that raises `GatewayGraphError`,
   `GatewayRouteRefused`, `GatewayUnexpected`, `GatewayInvalidId` or `GatewayCorrupt` is recorded and the loop continues.
   - The row's outcome is a new constant `READ_REFUSED = "READ-REFUSED"`, with `transcript_id` and a `detail` holding the exception class
     name and its status only. Never the body, never the bearer.
   - The series dict gains a counter `read_refused`, starting at 0, beside `expired`.
   - `GatewayUnauthorized`, `GatewayNeedsLogin`, `GatewayNotConfigured` and `GatewayToolsAbsent` are run-wide conditions: they still raise.
   - The `except Expired` branch and the refused-LISTING handling stay as they are.
   - If `RunRecord.body()` or the handler sums per-series counters, carry `read_refused` through the same way `expired` is carried.
2. `data/transcripts/scripts/tests/test_pull_read_refused.py`, with injected transports and the in-memory S3 the existing pull tests use
   (`data/transcripts/scripts/tests/test_teams_pull.py` shows the pattern); no AWS, no HTTP:
   - `test_refused_read_is_recorded_and_the_loop_continues`: a series of five rows whose first two reads raise `GatewayGraphError`; the
     other three land, `read_refused == 2`, and two outcomes read `READ-REFUSED`.
   - `test_run_completes_and_reaches_every_series`: `pull.run` over the real `series.json`, the first series carrying a refused read;
     the run returns, every series has an entry in the record, and with `apply=True` the run record is written.
   - `test_run_wide_refusal_still_raises`: a read that raises `GatewayUnauthorized` still raises out of `pull.run`.
3. `data/transcripts/scripts/tests/test_monday_skip_replay.py`: its scheduled-path test asserts the OLD behaviour (the live read failure
   raises). Change that test, its docstring and its file:line reference to the NEW verdict (the row is recorded `READ-REFUSED`, the run
   continues). Keep the three test names.

### ACCEPTANCE

<criterion id="TR22-rf22-AC1" cell_refs="TR-rf-22"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R22_CHECKS/r22_checks.py rf22</invocation><expect>R22-RF22-OK</expect></criterion>
`TR22-rf22-AC1` -- the three named tests exist and the four pull test files pass together.

<expected_criteria>TR22-rf22-AC1</expected_criteria>

Dry-run at the base: `R22-RF22-FAIL absent: data/transcripts/scripts/tests/test_pull_read_refused.py` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** No AWS or HTTP call, no deploy, no Terraform, no change to `gateway_client.py`, the handler's schedule or any other module.
  No transcript text anywhere: ids, dates, statuses and counts only. ASCII only.
- If the fix cannot be made inside `_pull_series` (and the counter's carry-through) without touching another module, file a surprise row
  (`NFRA_TRNSPT-D2-W2-S<k>`, next unused across every document under `surprise-channel/`) naming the module, and stop.

<paths>
data/transcripts/scripts/teams/pull.py
data/transcripts/scripts/tests/test_pull_read_refused.py
data/transcripts/scripts/tests/test_monday_skip_replay.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R22.md</decomp_doc> (round 22, AMENDMENT 2), cell `TR-rf-22`.
<owned_cells>TR-rf-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR22-rf22-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-rf22.pull-survives-refused-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR22-rf22-AC1` BEFORE the flip. Commit first, then pin.
</proof_of_spec>

**REPORT:** the lines changed in `pull.py`, the exception classes caught and the ones left to raise, the test names with pass or fail,
the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a repo build; the deploy is cell TR-ra-22 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no new AWS call; the pull's role is unchanged.
comp-adversary: RUN -- sources: the live read record R22_ROOT_CAUSE_LIVE_READ_20261011.md, the worker's R22_ROOT_CAUSE.md, row D2-S16; BLIND to the Graph retention figure (only the 118-to-125-day bracket is measured). Traps: a blanket catch that hides an expired bearer (the run-wide classes still raise, and a test holds it); a deploy slipped into a build cell; a refused read mislabelled EXPIRED (a distinct outcome, because 502 is not proof of expiry).
lane: the paths block.
</preflight>

Source: row NFRA_TRNSPT-D2-S16; decomposition round 22 AMENDMENT 2, cell TR-rf-22; TR-rc-22's report (drain @7e77ac162b).
