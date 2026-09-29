# AMGT_CORPUS task order -- `CRPS-r-1` -- ROUND 16: the daily trigger for the existing `induction_run` producer (pinned commit, builder-named) -- the trigger only, never its registration

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-r-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN -- 2026-09-29 ~22:3xZ: carriers C1 sentinel 7 gates, C2 deploy-ledger 19, C3 moratoria 12, C4 scope-guard 0; --drift names 0 gates on amgt/induction/harvest/crosswalk. The worker registers NOTHING (plan mode only); the registration and first fire are the issuer's drain act under a never-widen pair and a NEVER-2 entry.
comp-iam: DECLARED-NOT-APPLICABLE -- no cloud grant moves; the fire's S3 and Bloomberg legs are add_security's existing path.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 16. Serves **FWD-4 and FWD-19 (a new library folder gets its identity without a manual act)**.

## 1. THE CELL -- `CRPS-r-1`

**Where this came from.** The round-15 analysis (`org/missions/D5/AMGT/AMGT_CORPUS/ledger/ROUND_ANALYSIS.round15.md` s.2)
ruled: schedule the producer that already exists, and build nothing new. `lib/research/corpus/induction_run.py` is the estate's
scripted registration producer. It measures the backlog, collects every EFFECTIVELY-EVIDENCED folder into ONE
`add_security --batch` call per run (NO call when the population is empty), and REFUSES ambiguous or disagreeing folders. Its
`--fire` runs only when `OPAL_INDUCTION_FIRE=1` is set AND `--as-of` is today UTC (`induction_run.fire_permitted`), and it is
always refused under pytest. `--dry-run` uses an injected fake call, so it reaches no Bloomberg. Nothing triggers it today.
Site-Z Scheduled Tasks run whatever tree they point at, and the shared working tree changes under a peer's uncommitted edit.
So the trigger must run a PINNED COMMIT's own checkout.

**RULED -- what you build (the trigger only; no producer change):**
1. **`lib/research/corpus/induction_scheduled.py`** (new) is the entry the task runs.
   - `python -m lib.research.corpus.induction_scheduled --mode fire|dry-run` computes `as_of` as today UTC and calls
     `induction_run.main(["--as-of", as_of, "--fire" | "--dry-run"])`.
   - It prints ONE closing line: `induction_scheduled mode <m> as_of <date> rc <n> log <path>`.
   - It appends the run's stdout to a log under a DERIVED directory: `%LOCALAPPDATA%` (or the platform's user data dir)
     `/opal/<task name>/<as_of>.log`. Never hardcode a device path (CLAUDE.md: derive, don't hardcode).
   - It never sets `OPAL_INDUCTION_FIRE` itself; the task's action does.
2. **`lib/research/corpus/schedule_induction.ps1`** (new) takes `-Plan`, `-Register`, `-Unregister`, `-Status` and
   `-Commit <sha>`. The worker runs `-Plan` ONLY.
   - **Task name:** taken from the builder, `python -c "from lib import opal_naming as n; print(n.name('amgt', None,
     'induction', 'daily'))"` (reads `amgt-induction-daily` today). The name is never typed.
   - **Pinned checkout:** a detached checkout of `<sha>` at `<repo parent>/opal-pinned/<task name>/<sha[0:12]>`, derived from
     `git rev-parse --show-toplevel`. `-Register` creates it with `git worktree add --detach`; `-Plan` only prints it.
   - **Action:** `cmd.exe /c "set OPAL_INDUCTION_FIRE=1&& <python> -m lib.research.corpus.induction_scheduled --mode fire"`,
     with `WorkingDirectory` = the pinned checkout. The python path is resolved at plan time (a site-Z Scheduled Task does
     not inherit the profile).
   - **Trigger:** daily, once, with a start time that is an absolute instant (the `register_daily_task.ps1` precedent in
     `integrations/bloomberg/pipeline/`), and StartWhenAvailable.
   - **`-Plan` prints exactly these lines**, then exits 0 having created and registered nothing: `PLAN task <name>`,
     `PLAN commit <full sha>`, `PLAN workdir <path>`, `PLAN execute <exe>`, `PLAN arguments <args>` and `PLAN trigger <desc>`.
   - `-Register` prints `REGISTERED <name>`; `-Status` prints the task's state, next and last run, and last result.
3. **`lib/research/corpus/tests/test_induction_schedule.py`** (new, offline) drives `induction_scheduled --mode dry-run` through
   its real entry.
   - It builds a scratch library under `tmp_path` with TWO planted folders:
     - (a) one whose report carries ONE `(Ticker: <ROOT> <CC>)` line and whose folder name ends in the same `<ROOT> <CC>`;
     - (b) one whose reports carry two different tickers.
   - Point `OPAL_RESEARCH_LIBRARY_ROOT` at the scratch library, redirect `induction_run.DELIVERABLES_DIR` and the log dir to
     `tmp_path`, and point the crosswalk env overrides (`AMGT_CROSSWALK_PATH`, `AMGT_REGISTRATIONS_PATH`,
     `AMGT_HARVESTER_CONFIG_PATH`) at scratch files. The round-14 test `test_induction_planted_drive.py` does the same.
   - Assert: (a) is in the run's ONE batch request; (b) is REFUSED as ambiguous; the fake call made 0 Bloomberg calls; the
     `as_of` used is today UTC.
   - Then `print()` ONE line, exactly: `r1 scheduled_path planted_evidenced_requested 1 ambiguous_refused 1 bloomberg_calls 0
     as_of_is_today True`.

**KNOWN LIMIT, NOT YOURS TO WIDEN.** A folder whose ONLY identity evidence is its own name (for example `Hitachi 6501 JP`, whose
report has no `(Ticker: ...)` line) is NO_EVIDENCE to `induction_run` and is not registered by the schedule. The issuer carries
that to the CTO as a row. Do not change `induction_run.py`, `induction_request.py` or `add_security.py`.

## 3. SURFACES

<paths>
lib/research/corpus/induction_scheduled.py
lib/research/corpus/schedule_induction.ps1
lib/research/corpus/tests/test_induction_schedule.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-r-1.schedule-induction-run.md
</paths>

READ-ONLY: every other file in the repository, every S3 object, the research library on the synced drive, the Task Scheduler.
Scratch `.scratch/r1/`.

## 4. BOUNDS
- Pure ASCII, CRLF-free, Python 3.9-compatible; PowerShell 5.1-compatible.
- NO `-Register`, NO `Register-ScheduledTask`, NO `git worktree add` outside a test's tmp_path, and NO `--fire`.
- NO vendor call and NO S3 write. `induction_run --fire` is refused under pytest by construction; do not work around that.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-r-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round16/r1_AC1.sh</invocation><expect>(?m)^r1 scheduled_path planted_evidenced_requested 1 ambiguous_refused 1 bloomberg_calls 0 as_of_is_today True$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-r-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round16/r1_AC2.sh</invocation><expect>(?m)^r1 plan task_is_builder_name True commit_pinned True workdir_is_shared_tree False registered_now 0$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-r-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round16/r1_AC3.sh</invocation><expect>(?m)^paths_outside_grant 0$</expect></criterion>
</proof_of_spec>

- AC1: the scheduled path, driven offline on planted folders. AC2: the registration plan (builder name, pinned commit, not the
  shared tree, nothing registered). AC3: the bound.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-r-1.schedule-induction-run.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you
   changed plus the instance.
4. Report ONCE: each AC line, the full `-Plan` output, the python path the plan resolved, and the log path.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-15 analysis s.2 + s.4 cell 1 @`c265fbb6ff` (msg 26742). The checks were dry-run at base CLOUD `8f7237f20f` (~22:2xZ):
- r1_AC1 FAIL (no test file; no output line);
- r1_AC2 FAIL (`r1 plan MISSING lib/research/corpus/schedule_induction.ps1`);
- r1_AC3 PASS (`paths_outside_grant 0`).

The builder name was measured at the cut: `amgt-induction-daily`.

**Drain (the issuer's WORLD act, under a never-widen pair + NEVER-2 entry):** `-Register -Commit <merged sha>`; then the FIRST
scheduled fire is the acceptance. The expected outcome is read from the producer's rule: population 0 of 96, so the run makes no
call and no pool put. The rule at signing will name both branches.
<risk>WORLD</risk>
<status>pending</status>
<round>16</round>
<slot>~1</slot>
<fabric>site-z</fabric>
