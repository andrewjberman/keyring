# TO IRPT_BCKEND.TO-IB-pr-534 -- READ why 49financial's long fire exceeds the SSM execution timeout (the numbers) and write the one-date REPLAY packet for its missing 2026-10-08, READ ONLY (CTO round-192 analysis item 3 @296869062d and CTO half "Ruling carried"; rows D2-S164, D2-S165)

<to_id>IRPT_BCKEND.TO-IB-pr-534</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~381</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>192</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-192 analysis (item 3: "why a long fire exceeds the SSM execution timeout (the timeout value, the fire's duration distribution over the last 10 fires); the one-date replay's packet: what it writes (one date's keys), its rollback, and that it leaves every other date untouched. The replay itself runs after item 1's after-read, under its own pair.") | **Decomp cell:** `IB-pr-534` (decomposition section 184) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree (the only place you write):** `C:/dev/wk-IRPT_BCKEND-381` on a branch cut from the current branch. Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~381 <0.9.0_WK_IRPT_BCKEND~381@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). The `portal` gitlink shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read; print what a search covered before you read a zero as an absence). Commit gates take minutes: wait. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, durations, hashes, object names and public ticker symbols only in any tracked file; no account id, client id, position value or holding name; objects are read into memory or scratch OUTSIDE the worktree (`C:/dev/_scratch381/`), deleted at the end with a short bounded script.

**Cell `IB-pr-534` (inlined).** 49financial's served holdings series has no row for 2026-10-08 (a trading day): its 2026-10-09 scheduled fire (SSM command `irpt holdings refresh 49financial 2026-10-09`, id in the `ssm list-commands` output) TIMED OUT and was killed (ExecutionTimedOut, exit 137), and no later fire replays a date (rows D2-S164, D2-S165; read them first). The producer is described in `deliverables/0.9.0_WK_IRPT_BCKEND~378/IB190-3_producer_census.json` (merged): the schedule `irpt-holdings-snapshot` (`cron(15 10 ? * MON-FRI *)`) invokes the Lambda `irpt-holdings-refresh-lambda`, which sends one SSM `AWS-RunShellScript` command per firm that fetches the firm's standalone bundle and runs `holdings_snapshot.py --firms <firm> --upload`. The CTO ruled a one-date replay of 2026-10-08 as its own cell with its own pair, AFTER the producer release's after-read. **This order measures the timeout and writes the replay's packet. It writes and invokes nothing.**

**Do, in this order (every number is a MEASUREMENT with its source named in `notes`):**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit` (state it). Read `refresh_dispatch.py` (`infra/aws/lambda/investor-reporting/holdings_refresh/`), `holdings_refresh.tf` and `schedule.tf` under `infra/aws/terraform/investor-reporting/directory/`, `holdings_snapshot.py` `main` (about line 3227: `--as-of`, `--upload`), `run_firm`, `evaluate_publish_gate` (the `source_frontier_older` condition) and `HoldingsPublication` (the `publication` module of the `holdings` Lambda: how a date is added to the index, whether an older date than `latest_date` can be added, and what `begin()`/the conditional index write guard).
2. **The timeout numbers (READ).** The SSM execution timeout the dispatcher sets for the command (the document parameter or `TimeoutSeconds`/`executionTimeout`, from the dispatcher's code and, if it is set live, `lambda get-function-configuration` of `irpt-holdings-refresh-lambda`): record `timeout.ssm_execution_timeout_seconds` (integer seconds) and `timeout.ssm_source` (where the value comes from); `timeout.dispatcher` = `{"function":"irpt-holdings-refresh-lambda","timeout_seconds":<its own Lambda timeout>}`. If the value is the SSM service default (3600 seconds) say so in `ssm_source`.
3. **The fire durations.** From `ssm list-commands` (filter client-side on the Comment prefix `irpt holdings refresh 49financial`), take the 49financial command for each scheduled fire you can list (at least the latest TEN; page to the end and print the denominator), with `RequestedDateTime` as start and the command's completion time as end (use `ssm list-command-invocations --command-id <id>` for the invocation's `RequestedDateTime` and its `CommandPlugins[].ResponseFinishDateTime`, or the closest end timestamp the API gives; say which). Record `fires_49financial` = a list of `{"fire_date","status" (Success|Failed|TimedOut|Cancelled),"duration_seconds"}` and `fire_statistics` = `{"n","min","median","max","over_timeout"}` recomputed from them, where `over_timeout` counts fires whose status is TimedOut or whose duration reached the timeout. Read NO command output beyond status fields.
4. **The source for 2026-10-08.** Whether 49financial's source partitions for 2026-10-08 exist (list the `date=2026-10-08` prefixes of the source tables `holdings_snapshot.py`'s 49F builder reads; find them from the builder; a named-prefix list is a READ): record `source_for_2026_10_08` = `{"silver_partitions_present":bool,"evidence":".."}`.
5. **The replay.** Write the replay's facts into the record: `replay.command_shape` (the exact producer invocation, including `--as-of 2026-10-08`, and where it would run), `replay.writes` (the key shapes it writes: the dated revision objects and the index row; never other dates), `replay.index_effect`, `replay.leaves_other_dates_untouched` (true only if the code proves it; if it cannot be shown, STOP and file a row), `replay.gate_refuses_older_date` (true or false, from `evaluate_publish_gate`'s `source_frontier_older` rule: a candidate whose frontier is older than the served frontier is REFUSED) and, if true, `replay.route_needed` (what the replay therefore needs: a signed pair with a ruling, an operator path past the gate, a gate change; do not choose, name the options and what each moves) and `replay.rollback` (how the index returns to its prior version, by the named version of the one `current/manifest.json` key; read the current version id).
6. **The packet** `deliverables/0.9.0_WK_IRPT_BCKEND~381/ONE_DATE_REPLAY_PACKET_49F_20261008.md` (3,000 characters or more), in the shape of `deliverables/0.9.0_WK_IRPT_BCKEND~379/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-532.md` (read it as the model): **Branch A** (the replay), **Branch B** (rollback), the **blast radius** (one date's keys; **every other date** untouched; the index row added), the `source_frontier_older` answer and the route it needs, the ordering (**after the release's after-read**, never before), the releasing seat's own NEVER-2 **ledger**, and the **COO half and CTO half, both UNSIGNED**, the packet's own sha256 left for the signers; plus what it does not measure.
7. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~381/IB192-2_timeout_and_replay.json`: `{"base_commit":"<40hex>","timeout":{...},"fires_49financial":[...],"fire_statistics":{...},"source_for_2026_10_08":{...},"replay":{...},"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.
8. **Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB192-2_criteria_output.txt`, write the proof instance named under `<proof_of_spec>` and validate it with `python .tools/proof-of-spec-check.py <instance>` (every `artifacts_produced` row pinned to the commit that carried the artifact: commit the deliverables FIRST, then the instance last), and commit with explicit paths. Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record or packet (never the check). Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB192-2-AC1" cell_refs="IB-pr-534"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r192/p192_cells.py" . IB192-2-AC1</invocation><expect>IB192-2-AC1 PASS</expect></criterion>
<criterion id="IB192-2-AC2" cell_refs="IB-pr-534"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r192/p192_cells.py" . IB192-2-AC2</invocation><expect>IB192-2-AC2 PASS</expect></criterion>
<criterion id="IB192-2-AC3" cell_refs="IB-pr-534"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r192/p192_cells.py" . IB192-2-AC3</invocation><expect>IB192-2-AC3 PASS</expect></criterion>

<expected_criteria>IB192-2-AC1, IB192-2-AC2, IB192-2-AC3</expected_criteria>

What the checks grade: AC1 the timeout (an integer above 0 with its source), the dispatcher function and timeout, at least ten fires with date, status and a duration above 0, and the statistics (n, min, median, max, over_timeout) recomputed from the fires; AC2 the source presence with its evidence, the replay's command shape, writes (a non-empty list), index effect, rollback, `leaves_other_dates_untouched` true, `gate_refuses_older_date` stated and, when true, a route named; AC3 the packet (3,000 characters or more) naming Branch A, Branch B, blast radius, rollback, every other date, 2026-10-08, COO half, CTO half, unsigned, after the release, source_frontier_older and ledger, no long digit run, notes and the six bound counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and the scratch directory. READ ONLY. **Nothing is invoked, written, uploaded, applied, deployed or sent:** no Lambda invoke, no SSM `send-command`, no S3 put/copy/delete, no terraform, no sign-in, no vendor call. Allowed AWS calls (READ): `ssm list-commands` and `list-command-invocations` (status and timestamps only), `lambda get-function-configuration` of the dispatcher, `scheduler get-schedule`, `s3api list-objects-v2` on named source prefixes and `list-object-versions`/`head-object` on the one named manifest key, `sts get-caller-identity`. A denial is recorded, never worked around or widened.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a value, name or identifier of a client or account in a tracked file; a figure you cannot source (say so; do not estimate); a replay that cannot be shown to leave other dates untouched. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W381-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with the usual fields, including `grounding`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~381/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 184 (round 192, workstream ~P), cell `IB-pr-534`.
<owned_cells>IB-pr-534</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB192-2-AC1, IB192-2-AC2, IB192-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~381/IRPT_BCKEND.TO-IB-pr-534.49f-timeout-and-one-date-replay-packet.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads SSM command history (status and timestamps), the dispatcher's configuration, source and manifest listings and the producer's code; it writes and invokes nothing and sends no command; the replay itself (a producer run that would add one date to 49financial's served series) is a later cell under its own pair after the release's after-read.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; a denied read is recorded as a statement, never widened.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule is READ, never created or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p192_cells.py IB192-2 dry-run at base on dell2 2026-10-14 ~06:1xZ: AC1, AC2, AC3 FAIL (no record, no packet). Positive control in a temp root the run created itself (a synthetic record and packet; removed): all three PASS; negatives, each failing its own arm: statistics not matching the fires, a wrong over_timeout, nine fires, no timeout value, a replay that touches another date, a refusal with no route, no writes listed, source presence unstated, a write counter above 0, a long digit run, a packet without the every-other-date statement, a packet too short.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~381` (worktree `C:/dev/wk-IRPT_BCKEND-381`). Class SERVED (reads the live SSM history, the dispatcher's configuration and served listings; writes only the worker's records). The premises are my own reads of the failed fire and the missing date (rows D2-S164, D2-S165) and the census; the timeout value and the durations are what this order measures.
</preflight>
