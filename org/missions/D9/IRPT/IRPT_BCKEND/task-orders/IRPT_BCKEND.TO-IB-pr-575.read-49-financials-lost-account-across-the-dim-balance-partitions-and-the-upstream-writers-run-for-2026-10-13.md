# TO IRPT_BCKEND.TO-IB-pr-575 -- READ 49 Financial's lost ACTIVE account across the dim_balance partitions 2026-10-08 to 2026-10-14 and the upstream writer's run for 2026-10-13: where the gap starts, whether it clears on 2026-10-14, and whether the run failed or truncated; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-575</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~418</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~PE</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8274 ("cut the presence READ now; absent is not empty") on the 49 Financial offline gate run (IB-pr-573, merged @dbfd95217d, row D2-S197) | **Decomp cell:** `IB-pr-575` (decomposition section 210) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-418`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~418 <0.9.0_WK_IRPT_BCKEND~418@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Where the command rail denies an AWS enumeration it prints the command that answers: run that; or add a trailing `# rail-checked: <why>`. Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting` (local, never committed, nothing wider), so the writer's code and the check's file reads resolve under the worktree root.

**Client data rule:** counts, dates, hashes, commit ids, column names, status names and file paths only in any tracked file; **no account id, household id, client id, name, quantity, value or holding name.** Scratch lives OUTSIDE the worktree (`C:/dev/_scratch418/`); delete downloaded partitions from scratch after you read them.

**Cell `IB-pr-575` (inlined).** The 49 Financial offline gate run (`deliverables/0.9.0_WK_IRPT_BCKEND~416/IB212-1_49f_screen_offline_read.json`, rows `D2-W416-S1`, `S2`, `D2-S197`; READ THEM FIRST) found: 49 Financial (the P1 firm) is served at 2026-10-12, two trading days behind T-1; the candidate for 2026-10-13 was refused on `account_lost` count 1; **the lost account is ACTIVE in the directory, has ONE row in the 2026-10-12 `dim_balance` partition and NONE in the 2026-10-13 one**, so no screen drops it: it is a SOURCE GAP on the candidate date. The CTO (msg 8274): read the account's presence across `dim_balance` 2026-10-08 to 2026-10-14, and the upstream writer's run for 2026-10-13 (row counts by partition: did it fail or truncate). **An account ABSENT from the source is not the zero-position case; the guard keeps refusing.** If 2026-10-14 carries the account again, the 2026-10-14 candidate publishes cleanly (and 2026-10-13 stays an unpublished day stated in words); if it is gone for good, the remedy is a custodian-confirmed TERMINATED mark (a partner-firm contact the issuer drafts for Andrew).

**Do, in this order:**
0. `git sparse-checkout add data/assets/scripts/gold/investor_reporting`. `git rev-parse HEAD` before your first commit is `base_commit`; `read_date` is `date -u +%F`.
1. **The partitions.** Find the 49 Financial `dim_balance` partitions (the same source the IB-pr-573 worker read; its record names the declaration entry and the builder `build_49f_actual` in `holdings_49f.py`; existing objects, head/get/list only; the canonical address and a read-only list stand if the served graph is blocked). For EACH trading day 2026-10-08 to 2026-10-14 (the check recomputes the list from `lib/trading_calendar.py`: `2026-10-08, 2026-10-09, 2026-10-12, 2026-10-13, 2026-10-14`, in that order) record `partitions` = `[{"day":"<ISO>","partition_present":bool,"row_count":<n or null if absent>,"account_present":bool},...]` (`account_present` for the ONE lost account, whose id stays in scratch only; an absent partition has `row_count` null and `account_present` false). Also `served_snapshot_day` `"2026-10-12"`, `candidate_day_refused` `"2026-10-13"`, and `gap` = `{"first_absent_day":"2026-10-13","claim":"measured|inferred|absent"}` (the account must be present on 2026-10-12 and absent from a present 2026-10-13 partition, as IB-pr-573 found; if your read disagrees, say so in a row and STOP at the record).
2. **The upstream writer.** Find the code that writes the `dim_balance` partition (from `build_49f_actual`'s source back to its writer: the job, function or script, its owner and its schedule; Glob folder lists, read named files). `upstream_writer` = `{"site":{"file","line","identifier"} (the line that writes the partition; the check reads it),"name":"10+ characters: the job or function and its owner, no bucket name","run_2026_10_13":{"status":"succeeded|failed|truncated|not_found|unknown","claim":"measured|inferred|absent","row_counts":{"prior_day":n,"day":n,"next_day":n} (the partitions' own row counts for 2026-10-12, 2026-10-13, 2026-10-14),"truncation_signal":bool (a row count far below its neighbours, a partial file, a failed step in the run's log),"statement":"60+ characters: what the run evidence says and does not say, no id"}}`. Read the run's log or status from existing records only (CloudWatch logs read, Step Functions or SSM history read, the partition objects' LastModified); never invoke or re-run it.
3. **Does it clear?** `self_clears` = `{"claim":"measured|inferred|absent","account_present_on_2026_10_14":bool or null if the partition is absent,"statement":"60+ characters"}`; `remedy` = `{"path":"40+ characters: if the account returned on 2026-10-14, the 2026-10-14 candidate publishes and 2026-10-13 stays an unpublished day in words; if it is gone, the custodian-confirmed TERMINATED mark as a partner-firm contact drafted for Andrew","partner_contact_needed":bool}`.
4. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~418/IB214-1_49f_presence_read.json` with exactly: `base_commit`, `read_date`, `partitions`, `served_snapshot_day`, `candidate_day_refused`, `gap`, `upstream_writer`, `self_clears`, `remedy`, `notes` (at least three lines of 30+ characters), and the six counters (`functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`), all 0.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB214-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB214-1-AC1" cell_refs="IB-pr-575"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r214/p214_cells.py" . IB214-1-AC1</invocation><expect>IB214-1-AC1 PASS</expect></criterion>
<criterion id="IB214-1-AC2" cell_refs="IB-pr-575"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r214/p214_cells.py" . IB214-1-AC2</invocation><expect>IB214-1-AC2 PASS</expect></criterion>
<criterion id="IB214-1-AC3" cell_refs="IB-pr-575"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r214/p214_cells.py" . IB214-1-AC3</invocation><expect>IB214-1-AC3 PASS</expect></criterion>

<expected_criteria>IB214-1-AC1, IB214-1-AC2, IB214-1-AC3</expected_criteria>

What the checks grade: AC1 one row per trading day 2026-10-08 to 2026-10-14 (recomputed against the calendar), the partitions' presence and row counts, the account present on 2026-10-12 and absent from the present 2026-10-13 partition, the gap located; AC2 the upstream writer read in the code (file and line verified at HEAD) and its 2026-10-13 run: status, claim, the row counts around it, the truncation signal; AC3 whether the refusal clears (the 2026-10-14 partition), the remedy and whether a partner contact is needed, notes, the six counters 0 and no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS: `s3api head-object`, `get-object` and `list-objects-v2` of EXISTING objects (49 Financial's `dim_balance` partitions and their run records), CloudWatch Logs `filter-log-events` and `describe` reads, Step Functions and SSM history reads, `list`, `describe`. **Nothing is published, re-run, invoked, backfilled, written to AWS, signed or sent. The producer and the upstream writer are NOT run.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a need to re-run the writer; an account id, name or value in a tracked file; a need to type an object address for a NEW object. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W418-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~418/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 210 (round 2, workstream ~PE), cell `IB-pr-575`.
<owned_cells>IB-pr-575</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB214-1-AC1, IB214-1-AC2, IB214-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~418/IRPT_BCKEND.TO-IB-pr-575.read-49-financials-lost-account-across-the-dim-balance-partitions-and-the-upstream-writers-run-for-2026-10-13.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads existing partitions, run logs and the writer's code with the worker's own identity and writes one record; nothing is re-run, published or invoked, so no served byte moves; any remedy (a re-landed row, a TERMINATED mark and a partner-firm contact) is a later act.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p214_cells.py IB214-1 dry-run at base on dell2 2026-10-15 ~13:1xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp tree the run created itself (the real calendar, a stub writer file, a synthetic record; removed): all three PASS; seventeen negatives, each failing its own arm: a missing day, an extra day, a present partition with no count, an absent partition with an account, the account present on the gap day, a wrong served day, a wrong gap day, a wrong writer line, an unknown run status, missing row counts, a truncation signal not boolean, a self-clears claim not a claim, a short remedy, a partner flag not boolean, short notes, a counter above 0, a long digit run.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~418` (worktree `C:/dev/wk-IRPT_BCKEND-418`). Class SERVED (reads a served surface and writes only the worker's records).
</preflight>
