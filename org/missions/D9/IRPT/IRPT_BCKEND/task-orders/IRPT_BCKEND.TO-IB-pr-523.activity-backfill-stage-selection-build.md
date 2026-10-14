# TO IRPT_BCKEND.TO-IB-pr-523 -- BUILD Design (B) of the 49 Financial activity backfill: the reporting-gold backfill event can select its stages, so an activity-and-lots-only run never writes the returns or class partitions (CTO round-187 analysis @718356ee39, ruling 1; census IB-pr-522, row D2-S155)

<to_id>IRPT_BCKEND.TO-IB-pr-523</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~370</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>187</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-187 analysis (ruling 1: "Design (B): an activity-and-lots-only run, through a small code change under its own pair, with returns untouched") | **Decomp cell:** `IB-pr-523` (decomposition section 179) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree (the only place you write):** `C:/dev/wk-IRPT_BCKEND-370` on a branch cut from the current branch. Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~370 <0.9.0_WK_IRPT_BCKEND~370@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). The `portal` gitlink shows modified in a fresh worktree: NEVER commit it. Never push, deploy, invoke a Lambda or call AWS (everything is offline). Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Cell `IB-pr-523` (inlined).** The Lambda `irpt-49f-reporting-gold-lambda` (source `infra/aws/lambda/investor-reporting/reporting-gold/handler.py`) has an explicit backfill event `{"backfill": {"start", "end"}, "accounts": "population" | [ids], "dry_run": true}`. `run_backfill` (about lines 546-590) computes the RETURNS frame for the range, writes each returns day (`ard.emit_day`), then the class days (`emit_classes`), then the lots days (`emit_lots`, which also writes `account_activity_daily`). The census (IB-pr-522) found that a backfill over the 565 days the activity table needs would also REWRITE the 565 landed returns partitions. The CTO ruled Design (B): **a backfill event may select its stages; an activity-and-lots-only run must not compute or write returns or class.**

**The design (build exactly this, no more):**
1. **A new event key `stages`**, valid ONLY inside a backfill event. Absent: all three stages, exactly the behaviour today (a default backfill event must make exactly the calls it makes now, in the same order). Exactly the list `["lots"]`: the activity-and-lots-only run. **Anything else is REFUSED by name**, with `SystemExit("REFUSED: ...stages...")` whose text contains the word `stages`, BEFORE any other call: an unknown stage, an empty list, `["returns"]` or `["class"]` or any other list, a string. A `stages` key on an event with NO `backfill` object (a scheduled event) is also REFUSED by name before anything runs (put that check in `run`, before the route to `run_backfill`).
2. **The lots-only run (`stages == ["lots"]`):** it keeps every existing guard (the account set declaration, the chunk bound `MAX_BACKFILL_DAYS` unchanged at 25, the range not past the newest landed day, a range with no trading day) and the account set exactly as the default path builds it; it does NOT call `compute`, does NOT call `ard.emit_day`, does NOT call `emit_classes`; it calls `emit_lots(s3, firm, <the trading days of the range, oldest first>, accounts, upload=not dry_run, workers=workers)` exactly once and then `record_lots_status` as today; the "producer yielded no rows" refusal belongs to the returns frame and does not apply. **Do not change `MAX_BACKFILL_DAYS`** (the timeout-sized chunking is the later pair's matter).
3. **The result names its stages:** the dict `run_backfill` returns gains `"stages": [...]` (the list that ran: `["returns","class","lots"]` by default, `["lots"]` lots-only); for the lots-only run `rows` is `{}` or the days mapped to 0 (no returns row was written), `class_rows` and `class_failed` are `{}`.
4. **Confinement (the check enforces it):** change ONLY `infra/aws/lambda/investor-reporting/reporting-gold/handler.py` and ADD ONLY `infra/aws/lambda/investor-reporting/reporting-gold/tests/test_backfill_stages.py`; in `handler.py` the hunks may sit only in the functions `backfill_days`, `run_backfill` and `run` (put a small helper function, for example `backfill_stages(event)`, immediately BEFORE `run_backfill`, so its hunk reads as `backfill_days`'s neighbour) and in nothing else; no other file in that folder, no `lambda.tf`, no source map, no staged copy changes.

**Tests (`tests/test_backfill_stages.py`, at least FIVE test methods named `test_...`):** copy the fixture style of `tests/test_backfill_mode.py` (its `patches` list of `mock.patch.object` stubs, no network) and prove: the lots-only event calls neither `compute` nor the returns emit nor the class emit and calls the lots emit once with the right days and a non-empty account set; the result carries `stages` `["lots"]`; a default backfill event makes exactly the calls it made before (compute, one returns emit per day, the class emit, the lots emit); each of an unknown stage, an empty list, `["returns"]`, a string is refused by name and makes no call; a `stages` key on an event without `backfill` is refused by name. Run the whole folder from `infra/aws/lambda/investor-reporting/reporting-gold` with `python -m pytest -q -p no:cacheprovider tests`: the 90 pre-existing tests and yours must all pass (at least 95 passed).

**Do, in this order:** (1) `git rev-parse HEAD` before your first commit is `base_commit` (state it); (2) read `handler.py` lines 20-40 (the module docs), 519-633 (`backfill_days`, `run_backfill`, `run`) and `tests/test_backfill_mode.py`; (3) make the change and write the tests; (4) update the module docstring paragraph that documents the backfill event (a few lines naming `stages`: this hunk sits before the first function and is allowed as module level); (5) run the folder's tests; (6) run the three criteria below from your worktree root, record each output and exit code verbatim in `deliverables/0.9.0_WK_IRPT_BCKEND~370/IB187-1_criteria_output.txt`; (7) write the proof instance named under `<proof_of_spec>`, validate it with `python .tools/proof-of-spec-check.py <instance>` (every `artifacts_produced` row pinned to the commit that carried the artifact: commit the code, the tests and the criteria output FIRST, then the instance last), and commit with explicit paths. Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR change (never the check). Report once, under 150 words.

**Criteria (run each under `timeout 200` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB187-1-AC1" cell_refs="IB-pr-523"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r187/p187_cells.py" . IB187-1-AC1</invocation><expect>IB187-1-AC1 PASS</expect></criterion>
<criterion id="IB187-1-AC2" cell_refs="IB-pr-523"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r187/p187_cells.py" . IB187-1-AC2</invocation><expect>IB187-1-AC2 PASS</expect></criterion>
<criterion id="IB187-1-AC3" cell_refs="IB-pr-523"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r187/p187_cells.py" . IB187-1-AC3</invocation><expect>IB187-1-AC3 PASS</expect></criterion>

<expected_criteria>IB187-1-AC1, IB187-1-AC2, IB187-1-AC3</expected_criteria>

What the checks grade: AC1 the folder's tests pass (at least 95 passed: the 90 pre-existing and your new ones in `tests/test_backfill_stages.py`, at least 5), the tests directory holds exactly the baseline eight files plus yours, and `handler.py` differs from its base blob only inside `backfill_days`, `run_backfill`, `run` and module level; AC2 a lots-only backfill event (the check's own stubs) calls neither `compute`, the returns emit nor the class emit, calls the lots emit once for the three declared trading days and a non-empty account set, and the result carries `stages` `["lots"]`; AC3 a default backfill event makes exactly `compute`, three returns emits, the class emit, the lots emit; an unknown stage, an empty list, `["returns"]` and a string are each refused by name (text contains REFUSED and stages) with no call made; a `stages` key on a non-backfill event is refused by name. Do not edit the checks.

## BOUNDS

- **Write surface:** exactly the `<paths>` below. **BUILD ONLY and offline:** nothing is deployed, uploaded, applied or invoked; no AWS call; no Lambda invoke; the served function does not change until a later, separately signed apply moves it.
- **Refusal clause:** STOP, file a row and report if: the existing 90 tests do not all pass at base before your change (say which fail; do not edit them); the design cannot be built without touching a function outside `backfill_days`, `run_backfill` and `run`, or a file outside the two named; `emit_lots` turns out to need the returns frame or the `first_seen` value the skipped `compute` supplies (say what it reads; do not work around it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W370-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with the usual fields) and keep working.

<paths>
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/test_backfill_stages.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~370/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 179 (round 187, workstream ~P), cell `IB-pr-523`.
<owned_cells>IB-pr-523</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB187-1-AC1, IB187-1-AC2, IB187-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~370/IRPT_BCKEND.TO-IB-pr-523.activity-backfill-stage-selection-build.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the served function `irpt-49f-reporting-gold-lambda` is NOT changed by this order (build only, offline); the code path changed is the explicit backfill event of `handler.py`; a default backfill event and the scheduled path make the calls they make today (checked by the AC3 arm and the 90 pre-existing tests); the later census, pair and apply carry the blast radius (the write set is the activity and lot prefixes only, never the returns or class prefixes).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the function role's write set is unchanged.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p187_cells.py IB187-1 dry-run at base on dell2 2026-10-14 ~01:3xZ: AC1, AC2, AC3 FAIL (no new test file; the default event runs compute, emit_day and emit_classes under a lots-only request; an unknown stage is not refused). Positive control in a throwaway git worktree at HEAD (created and removed by the run; my own hand implementation of the design plus a five-test file): all three PASS (95 tests); negatives in a temp copy, each failing its own arm: a lots-only run that still runs the returns, unknown stages accepted, a stages key on a scheduled event not refused, no new tests, an extra test file.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~370` (worktree `C:/dev/wk-IRPT_BCKEND-370`). Class WORLD (the gate infers the floor from the infrastructure path `infra/aws/lambda/...`; the order itself is BUILD ONLY and applies nothing). The design premises (run_backfill's stages, emit_lots' signature) are the census's and my read of `handler.py` lines 546-590.
</preflight>
