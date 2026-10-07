# AMGT_RESAPP task order -- `AMGT-ba-25` -- THE RESEARCH-PULL DRIVER FOR THE SEGMENT AND OFFICER PULLS: PLAN, CALL COUNT, CAPACITY STOP -- BUILT AGAINST FAKES, NO VENDOR CALL

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-25</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~287</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; the driver runs once per pull, by hand, under a pair.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell builds and tests against fakes; it reads and writes no store. The pulls' own bronze writes use the box's existing harvest access (the `exec_officers` channel already holds 5 names).
comp-adversary: RUN by the issuer at the cut -- no producer exists for a Bloomberg segment pull (segments come only from 12 stored filing analyses; 83 of 95 names serve a reason, row Z-W240-S1). The officer pull exists per name (`lib/research/management/bloomberg_fallback.pull_exec_officers`) with no batch runner, no stated call count and no capacity stop (84 names, row Z-W227-S1). `lib/research/harvest/bloomberg.py:40` admits six bronze requests; `segments` is not one.
EGRESS CLASS, declared: NONE for this cell. NO Bloomberg call, no vendor call of any kind: every test uses a fake client.
</preflight>

**Your worktree:** `C:/tmp/r77-287` (branch `wk-AMGT_RESAPP-287`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r77-287`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-25` (round 77, decomposition s.85)

Andrew authorized three one-time Bloomberg research pulls (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_211xZ_ALL_RECS_APPROVED_CTOZ_OPEN_CALLS_FOUR_CARDS.md`). The issuer runs each as its own paired
act. This cell builds the driver two of them run through. Conditions the driver enforces, as approved: a pull runs AFTER the
firm's 7:00 AM ET vehicle that day; ONE AT A TIME; it states its Bloomberg call count BEFORE it runs; a capacity refusal STOPS
the sequence and is not retried that day; no agent signs in to the Terminal (a signed-out Terminal pulls nothing).

Build `integrations/bloomberg/research/research_pulls.py` (`research/` is outside Andrew's no-modify order; nothing under
`integrations/bloomberg/pipeline/` or `auth/` is touched or imported for sign-in):

1. **`plan(kind, names=None)`** for `kind` in `segments`, `officers`. It returns the names (Bloomberg yellow keys), the fields,
   the calls per name and the total call count, and makes NO Bloomberg call.
   - `officers`: the names whose chain needs a new pull. Read them the way `lib/research/management/exec_roster_chain.py` does
     (`needs_new_pull`, :195); 84 of 95 at the cut. One `ReferenceDataRequest` per name (`NAME`, `COMPANY_EXEC_OFFICERS`).
   - `segments`: the covered names (`lib/research/coverage/covered_universe.covered_security_keys`) whose
     `scoped_amgt.read_segment_breakdown` serves no rows; 83 of 95 at the cut.
   - The segment FIELDS are data, not code: `integrations/bloomberg/research/research_pull_fields.json`, one entry per kind with
     `fields`, `calls_per_name` and `probed` (false until the issuer's one-name probe confirms them). Propose the segment
     mnemonics from what the repository already records about Bloomberg fields (`integrations/bloomberg/research/field_map.json`,
     `integrations/bloomberg/docs/`); mark each UNPROBED. Do not call Bloomberg to find them.
2. **`run(kind, names, blp, write, vehicle_ran, health)`**, one name at a time, in the order given:
   - `vehicle_ran()` false -> stop `VEHICLE_NOT_RUN`, no call. The real read is the scheduled task `OPAL_BBGTML_daily_pull`'s last
     run time being today's local date with the task not running (`integrations/bloomberg/pipeline/README.md:210`); read it with
     `schtasks` or `Get-ScheduledTaskInfo`, never by importing or editing a pipeline file.
   - `health()` false -> stop `TERMINAL_DOWN`, no call, and NO sign-in attempt.
   - a capacity refusal (the client raising `CapacityRefused`, or an error text carrying `LIMIT` or `-4001`) -> stop `CAPACITY`,
     report what was pulled, do not call again.
   - each response lands as received through `lib/research/harvest/bloomberg.bronze_write(request, security_key, fetched_at,
     body)`: `exec_officers` for officers (the existing channel), `segments` for segments. Add `"segments"` to `BRONZE_REQUESTS`
     (`lib/research/harvest/bloomberg.py:40`); the address is the builder's, never a typed key.
3. **A command line**: `plan <kind>` prints `names N calls M` and the list; `run <kind> --confirm-calls M [--names a,b]` refuses
   unless M equals the plan's count; `--probe <name>` runs ONE name. `EXIT = {"OK": 0, "CAPACITY": 3, "VEHICLE_NOT_RUN": 4,
   "TERMINAL_DOWN": 5}`.
4. **Tests** in `integrations/bloomberg/research/tests/test_research_pulls.py`, all on fakes.

The check file's docstring states the exact contract `plan` and `run` are graded on. The served read of the new `segments` bronze
(the page's segment breakdown) is NOT this cell.

Run `integrations/bloomberg/research/tests/` and `lib/research/harvest/tests/` before your commit and report each last line. Write no file under `lib/research/harvest/tests/` (another cell of this round owns that directory); your tests live in `integrations/bloomberg/research/tests/`.
**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W287-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. NO Bloomberg call and no other vendor call, including a field search. Do not open a session to 127.0.0.1:8194.
2. Write only the paths below. Nothing under `integrations/bloomberg/pipeline/`, `integrations/bloomberg/auth/` or
   `integrations/bloomberg/mcp/`. No deploy, no store write, no schedule.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
integrations/bloomberg/research/research_pulls.py
integrations/bloomberg/research/research_pull_fields.json
integrations/bloomberg/research/tests/test_research_pulls.py
lib/research/harvest/bloomberg.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~287/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-25"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba25.py" --cell plan; echo "exit=$?"</invocation><expect>each plan states its names, calls per name and their product, and makes no Bloomberg call; R77 BA25 PLAN: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-25"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba25.py" --cell stops; echo "exit=$?"</invocation><expect>refused before the vehicle, refused on a signed-out Terminal, stopped at the capacity refusal with no further call, and the healthy control pulls every name; R77 BA25 STOPS: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ba-25"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba25.py" --cell source; echo "exit=$?"</invocation><expect>the driver names no sign-in script and nothing under pipeline/ or auth/; R77 BA25 SOURCE: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~287 <0.9.0_WK_AMGT_RESAPP~287@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~287/AMGT_RESAPP.TO-AMGT-ba-25.research-pull-driver.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- both test directories' last lines;
- `plan officers` and `plan segments` as run against the live stores: the name counts and the call counts (a store READ is fine;
  a Bloomberg call is not);
- the proposed segment fields, each marked UNPROBED, and where in the repository each came from;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-75 ADDENDUM 3 item 2 and the CTO's round-76 analysis ruling 8, enrichment item 6. Wave 0. It feeds the
issuer's paired acts ba-21 (segments, 83) and ba-22 (officers, 84); ba-23 (FWD-2's uncovered name) uses the existing box-side
consumer `integrations/bloomberg/research/pull_consumer.py --once` and needs no driver. Checks dry-run at the base: ba-25 AC1, AC2
and AC3 base FAIL as expected (no driver). Write-set note for the merge: `lib/research/harvest/bloomberg.py` (one tuple entry).

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~287</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @bd772a3e6a; proof VALID (worktree checker); the research-pull driver on fakes: plan and call count, vehicle/terminal/capacity stops; AC1, AC2, AC3 YES; live-store plans officers 86 calls, segments 83 calls; segment fields UNPROBED; rows Z-W287-S1, S2</status>
