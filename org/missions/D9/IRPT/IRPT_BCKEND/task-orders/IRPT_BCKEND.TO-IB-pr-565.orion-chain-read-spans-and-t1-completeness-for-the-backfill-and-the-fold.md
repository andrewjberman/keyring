# TO IRPT_BCKEND.TO-IB-pr-565 -- READ the Orion chain's pull steps against the manual_api scripts, recompute the absent-day denominator per feed span, read Orion's T-1 completeness from the last 20 trading days' pulls, and locate the silver aggregator's source; READ ONLY, no Orion request

<to_id>IRPT_BCKEND.TO-IB-pr-565</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~409</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~PO</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling @1dca8c9e4d item 2 (msgs 8169, 8170) on the V2 read (IB-pr-560, rows W404-S1 to S10) | **Decomp cell:** `IB-pr-565` (decomposition section 202) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-409`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~409 <0.9.0_WK_IRPT_BCKEND~409@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Where the command rail denies an AWS enumeration it prints the command that answers: run that; or add a trailing `# rail-checked: <why>`. Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, timestamps, hashes, commit ids, field names, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch409/`).

**Cell `IB-pr-565` (inlined).** The CTO ruled (@1dca8c9e4d): the chain's pull steps (`INF_API_PULL_POSITIONS_DAILY`, `INF_API_PULL_TXN`, `INF_API_PULL_PERF` of `orion-gold-dispatch.sh`, `chain:full`, on the `inf-gold-layer-runner` EC2 started by `inf-gold-trigger` at about 11:32Z) take no date, and no date token is added to a scheduled producer. The absent trading days are backfilled ONCE with the same pull code plus a date. If the dispatch script invokes the `data/inf/manual_api` scripts, those scripts ARE the production code (run with a date, not retired); if not, the CLI's key shape and bytes must first be shown to match the chain's for one present day. The denominator is recomputed against `lib/trading_calendar.py` per feed span (days before a feed's first key are out of span, not missing). The 06:00 New York fold does NOT move until Orion's T-1 completeness is read from the last 20 trading days' pulls at the current 11:39Z landing. Your predecessor `0.9.0_WK_IRPT_BCKEND~404` left rows `IRPT_BCKEND-D2-W404-S1` to `S10` and the design `deliverables/0.9.0_WK_IRPT_BCKEND~404/IB203-1_orion_recut_design.json` (READ THEM FIRST; the S3 object `code/gold/orion-gold-dispatch.sh` and the three pull scripts' chain copies under `code/gold` are what it read). **This order READS. It makes no Orion request, pulls nothing, writes nothing to AWS, changes nothing.**

**Do, in this order:**
1. **Base and date.** `git rev-parse HEAD` before your first commit is `base_commit`. `read_date` is `date -u +%F`.
2. **Chain against the CLIs.** Download the dispatch script object `code/gold/orion-gold-dispatch.sh` (bucket `opal-data-inf`, existing object, GET to scratch) and the chain's copy of each pull script it runs for the three steps (the `code/gold` objects named in W404-S3 and the design, and for a script that has no `code/gold` object the copy under the other `code/` prefix the sync flattens: find it from the dispatch script's sync lines). For each feed record in `chain_invocation.steps.<feed>`: `step` (positions `INF_API_PULL_POSITIONS_DAILY`, transactions `INF_API_PULL_TXN`, performance `INF_API_PULL_PERF`), `script` (the file name of the manual_api script the step runs, which exists under `data/inf/manual_api/` in your worktree), `invokes_manual_api` (the dispatch script calls that script by name or path), `chain_copy_sha256` (sha256 of the chain's copy of the script), `repo_cli_sha256` (sha256 of `data/inf/manual_api/<script>` in your worktree), `identical` (the two hashes are equal) and `evidence` (40+ characters: the dispatch script's line number and the identifier on it). `positive_control_needed` is true exactly when some step neither invokes the manual_api script nor runs an identical copy; `positive_control_plan` (30+ characters) says how one present day's key shape and bytes would be compared (a later act under a signed pair, not this order), or `not needed: ..`. `cli_retirement_scope` (40+ characters): by the ruling, only a bronze write the chain does not reach is retired; say which of the manual scripts' bronze writes that is, from what you read.
3. **Silver aggregator (row W404-S5, now yours to close as a source-map and registry gap).** `lambda get-function-configuration` and `get-function` for `inf-silver-aggregator` (download the code zip to scratch, hash it, list its members). Record `silver_aggregator`: `function`, `code_sha256_b64` (the live CodeSha256), `handler`, `runtime`, `source_in_repo` (is there a source directory for it under `infra/aws/lambda/`; Glob the folder list, no recursive grep), `repo_path` (the path, or null), `source_map_entry` (is `inf-silver-aggregator` a key of `infra/aws/lambda/ci/lambda-source-map.json`) and `gap_statement` (40+ characters).
4. **Spans.** For each feed list the existing bronze prefix (positions, transactions, performance under `opal-data-inf`; print the count listed as the denominator `keys_listed`). A flat key is `<YYYY-MM-DD>.jsonl.gz`; a parquet key is `<YYYY-MM-DD>.parquet`; ignore other keys and count them in the notes. `first_key_day` is the earliest day with any key, `last_key_day` the latest. Using `lib/trading_calendar.py` `trading_days_between(first, last)` (inclusive): `trading_days_in_span`; `flat_present` (trading days with a flat key); `parquet_only` (trading days with a parquet key and no flat key); `missing` (sorted ISO trading days with neither) and `missing_count`; `out_of_span_note` (20+ characters). The partition must hold: `flat_present + parquet_only + missing_count = trading_days_in_span`. `absent_total` is the sum of the three missing counts.
5. **T-1 completeness (no Orion request).** The 20 days are the last 20 trading days up to `prev_trading_day(read_date)` (compute with the calendar). For each feed and each of the 20 days with a flat key: `landed_at_utc` (the object's LastModified from head-object, ISO UTC `YYYY-MM-DDTHH:MM:SSZ`, whose date equals the day), `asof_field` (the field name inside the pulled content that states the as-of date; read ONE small leading record of the gzip stream, never a value other than that date), `asof_day` (its ISO date) and `asof_is_prior_trading_day` (true when `asof_day` equals `prev_trading_day(day)`; the check recomputes it). A day with no flat key is `{"day":"..","key_present":false,"landed_at_utc":null,"asof_day":null}`. `data_ready_field`: `{"found":bool,"name":..or null,"note":"20+ characters"}` from what the leading record holds. `earliest_measured_complete`: `{"claim":"measured|inferred|absent","clock_ny":"HH:MM","reason":"40+ characters"}`: the earliest America/New_York clock time at which the T-1 data was complete, taken as the latest landing across the 20 days when every present day's as-of is the prior trading day; `measured` needs at least 12 present days per feed and every as-of equal to the prior trading day, else mark `inferred` and say what a probe would add. `trigger_moves_now` is `false`.
6. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~409/IB206-1_orion_chain_read.json` as one JSON object with exactly these members: `base_commit`, `read_date`, `chain_invocation` {`steps` {positions, transactions, performance}, `positive_control_needed`, `positive_control_plan`, `cli_retirement_scope`}, `silver_aggregator`, `spans` {positions, transactions, performance: `first_key_day`, `last_key_day`, `trading_days_in_span`, `flat_present`, `parquet_only`, `missing_count`, `missing`, `keys_listed`, `out_of_span_note`}, `absent_total`, `t1_completeness` {`feeds` {positions, transactions, performance: the 20 rows}}, `data_ready_field`, `earliest_measured_complete`, `trigger_moves_now`, `notes` (at least three lines of 30+ characters: what each fact rests on, the objects read counted, what was not read, where scratch sits), and the counters `functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`, all 0.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB206-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB206-1-AC1" cell_refs="IB-pr-565"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r206/p206_cells.py" . IB206-1-AC1</invocation><expect>IB206-1-AC1 PASS</expect></criterion>
<criterion id="IB206-1-AC2" cell_refs="IB-pr-565"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r206/p206_cells.py" . IB206-1-AC2</invocation><expect>IB206-1-AC2 PASS</expect></criterion>
<criterion id="IB206-1-AC3" cell_refs="IB-pr-565"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r206/p206_cells.py" . IB206-1-AC3</invocation><expect>IB206-1-AC3 PASS</expect></criterion>

<expected_criteria>IB206-1-AC1, IB206-1-AC2, IB206-1-AC3</expected_criteria>

What the checks grade: AC1 the chain's three steps against the manual_api scripts (the repo script's hash recomputed by the check), the control owed, the retirement scope and the silver aggregator's source status; AC2 the denominator recomputed per feed span against the calendar (the partition and the missing days); AC3 the T-1 completeness read over the last 20 trading days per feed (the as-of day recomputed against the calendar), the data-ready field, the earliest measured-complete time, the trigger not moving, notes and the six counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS: `s3api get-object` and `head-object` and `list-objects-v2` of EXISTING objects under `opal-data-inf` bronze prefixes, `code/gold` and every other `code/` prefix the dispatch script's sync flattens into the runner's code directory (the prefixes are named in the script; AMENDMENT 1: the positions pull script's chain copy sits under one of them), `lambda get-function` and `get-function-configuration`, `list`, `describe`. **Nothing is pulled, re-pulled, started, stopped, invoked, deployed, written to AWS, signed or sent, and no Orion request is made.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, starts, stops, invokes, pulls or sends; a need to read a secret value; a client identifier, account number or value in a tracked file; a need to type an object address for a NEW object. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W409-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~409/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 202 (round 5, workstream ~PO), cell `IB-pr-565`.
<owned_cells>IB-pr-565</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB206-1-AC1, IB206-1-AC2, IB206-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~409/IRPT_BCKEND.TO-IB-pr-565.orion-chain-read-spans-and-t1-completeness-for-the-backfill-and-the-fold.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads existing bronze objects (listing, head, one leading record per day), the dispatch script object, the chain's pull-script copies and two live Lambda configurations with the worker's own identity, and writes one record; nothing is pulled, started, stopped or deployed, so no served byte moves; the backfill and the fold are later acts under signed pairs.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p206_cells.py IB206-1 dry-run at base on dell2 2026-10-15 ~07:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp tree the run created itself (the real calendar, three stub scripts, a synthetic record computed from the calendar; removed): all three PASS; twenty-three negatives, each failing its own arm: a wrong step name, a script missing in the tree, a wrong repo hash, a wrong identical flag, the control flag wrong, a short retirement scope, the silver source in the repo with no path, a bad silver digest, a wrong span count, a missing day that is not a trading day, a broken partition, a wrong absent total, a wrong missing count, rows that are not the last 20 days, a wrong as-of flag, a measured claim over a stale as-of, a measured claim over too few present days, a landing day mismatch, an absent day carrying a landing, the trigger moving, a clock not HH:MM, short notes, a counter above 0.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~409` (worktree `C:/dev/wk-IRPT_BCKEND-409`). Class SERVED (reads a live data plane and writes only the worker's records).
</preflight>
