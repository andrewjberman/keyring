# TO IRPT_BCKEND.TO-IB-pr-581 -- READ the served DELTA of the 49 Financial split adjustment over the 47 split days: the producer return BEFORE and AFTER, the account-days moved, the returns at or below -50 percent; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-581</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~423</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PJ</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling @9913bf3ed4 and the READ IB-pr-572 (1,291 account-days projected) on the merged build IB-pr-578 | **Decomp cell:** `IB-pr-581` (decomposition section 214) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-423`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~423 <0.9.0_WK_IRPT_BCKEND~423@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/irpt_holdings_performance/`, then add (locally, never committed) the further directories the import chain of the modules you call needs: import the module, and add the directory of each import error until it imports (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`). Use `python -I` only for files you do not trust; your own harness runs with the repository's modules on `sys.path`.

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier, no object key that carries an account. The harness script you commit prints and writes counts only.

**READ-ONLY on every served prefix.** You may call AWS read APIs through the repository's own readers (`get_object`, `list_objects_v2`, `head_object`) with this box's credentials, nothing else: no `put`, `delete`, copy, invoke, publish or sign-in, no upload flag, no call of `land`, `write_refusal_record`, `HoldingsPublication.publish` or any function that writes. Scratch files go in a directory OUTSIDE the repository.

**Cell `IB-pr-581` (inlined).** IB-pr-578 (merged @07f60f52f3) split-adjusts the 49 Financial holdings price return in `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py`, declared in `data/assets/scripts/gold/irpt_holdings_performance/sources.json` (`split_adjust` on the first entry). The CTO's ruling @9913bf3ed4 and the READ IB-pr-572 projected 1,291 account-days affected over 47 split days. This cell MEASURES the served DELTA by a READ-ONLY run of the producer's own return over each split day, BEFORE and AFTER the adjustment, on the live custodian partitions. Nothing is written anywhere.

**READ FIRST (named files only):** `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` (`_frame_for`, `holdings_return`, `measure_split_ratios`, `_split_ratios_for_day`, `load_declaration`/`source_entry`, `validate_entry`, `read_partition`, `PartitionCache`-style cache class, the status constants), `data/assets/scripts/gold/irpt_holdings_performance/sources.json` (first entry), `data/assets/scripts/gold/irpt_holdings_performance/tests/test_split_adjust.py` (how a day is driven), and the READ record `deliverables/0.9.0_WK_IRPT_BCKEND~415/IB211-1_split_adjust_read.json` (its `split_source.49financial.split_days` is the list of the 47 split days).

**Do:**
1. Take the 47 split days from the READ record (49 Financial). Confirm each is a trading day with `lib/trading_calendar.py`; a split day that is not one: STOP and file a row.
2. For each split day run `_frame_for(s3, doc, source, day, cache=<one shared cache for the whole run>)` TWICE with the box's default S3 client: **BEFORE** = the declaration entry with the `split_adjust` key removed (an in-memory copy of the document: never edit the file), **AFTER** = the declaration as it is. Each returns a frame (`account_id`, `daily_return`, `status`, ...) or `None` with a note; a day that returns `None` in either arm: record it in the notes and exclude it from the totals (its entry in `per_day` shows `account_days_changed` 0 and a `"not_computable": true` flag).
3. Per day and in total: `account_days_run` (rows of the AFTER frame), `account_days_changed` (an account whose `daily_return` differs by more than 1e-12, or whose `status` differs, between the arms), `account_days_holding_a_split_security` (accounts with a t-1 row whose identifier, by the entry's `identifier_columns` chain, is one of the day's split securities: use the producer's own `identifier()` on the t-1 positions partition and the day's split securities from `_split_ratios_for_day`), `securities_adjusted` and `securities_ratio_absent` (summed over days from the AFTER arm's ratio results), `at_or_below_minus_50pct_before` and `_after` (rows with a non-null `daily_return` at or below -0.5), and `status_moves` as `{"FROM->TO": count}` over rows whose status differs. `account_days_changed` must not exceed `account_days_holding_a_split_security`; if it does, STOP and file a row (a change on an account that held no split security is a defect, not a result).
4. 2026-04-21 must appear in `per_day` with its own `account_days_changed` (at least 1). Print the ruling's 920 and this run's count for that day in the notes.

**Record shape** (`IB218-2_split_delta.json`): `"firm_scope":"49financial"`, `"split_days":[sorted ISO dates of the days you ran]`, `"totals":{"account_days_run":n,"account_days_changed":n,"account_days_holding_a_split_security":n,"securities_adjusted":n,"securities_ratio_absent":n,"at_or_below_minus_50pct_before":n,"at_or_below_minus_50pct_after":n,"status_moves":{"FROM->TO":n}}`, `"per_day":[{"day":"YYYY-MM-DD","account_days_changed":n, ...}]` with one entry per split day in `split_days`.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~423/IB218-2_split_delta.json`: the JSON object described above, plus `"base_commit":"<40hex: git rev-parse HEAD at your first act>"`, `"read_date":"<today ISO>"`, `"method":"<120+ characters: exactly what you ran, in what order, and the two arms>"`, `"claim":"measured"`, `"notes":[at least three lines of 30+ characters: what each fact rests on, what was not read, the sparse directories you added]` and the six counters, all 0: `functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`. Commit the harness script you ran under your deliverables folder beside the record, so the issuer can re-run it. If a number cannot be measured, STOP on that part, file a row, and write what you have with the field absent: the check then fails honestly; never estimate.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB218-2_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record, harness, criteria output first; then the instance alone in a second commit). Do not flip the order's status: the issuer does. Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB218-2-AC1" cell_refs="IB-pr-581"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r218/p218_cells.py" . IB218-2-AC1</invocation><expect>IB218-2-AC1 PASS</expect></criterion>
<criterion id="IB218-2-AC2" cell_refs="IB-pr-581"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r218/p218_cells.py" . IB218-2-AC2</invocation><expect>IB218-2-AC2 PASS</expect></criterion>
<criterion id="IB218-2-AC3" cell_refs="IB-pr-581"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r218/p218_cells.py" . IB218-2-AC3</invocation><expect>IB218-2-AC3 PASS</expect></criterion>

<expected_criteria>IB218-2-AC1, IB218-2-AC2, IB218-2-AC3</expected_criteria>

What the checks grade: AC1 the identity and method (base commit, read date, the split days as trading days with 2026-04-21 among them, firm scope 49financial, both arms named); AC2 the arithmetic (changed not above those holding a split security, not above those run; adjusted plus ratio-absent at least 1; returns at or below -50 percent do not rise; status moves; per-day changed counts sum to the total; 2026-04-21 present with at least one changed); AC3 notes of 30+ characters, the six counters 0, no long digit run (no id). Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS and on every served prefix, as above. **Nothing is deployed, published, minted, written to AWS, signed or sent.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS; a need to edit a file outside the paths block (the issuer amends); a step that would take longer than 25 minutes of wall clock without progress (record where it stalled); a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W423-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~423/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 214 (round 1, workstream ~PJ), cell `IB-pr-581`.
<owned_cells>IB-pr-581</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB218-2-AC1, IB218-2-AC2, IB218-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~423/IRPT_BCKEND.TO-IB-pr-581.split-delta.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- a READ-ONLY dry run: it reads the live pinned inputs and the served publication through the repository's own readers and writes nothing to AWS or to any served prefix; the record carries counts only. The apply of the changed code and the never-widen pair that uses this DELTA are later acts.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use this box's existing credentials.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p218_cells.py IB218-2 dry-run at base on dell2 2026-10-15 ~14:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in temp roots the run created itself (the real calendar, a synthetic record; removed): all pass; six negatives each fail their own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~423` (worktree `C:/dev/wk-IRPT_BCKEND-423`). Class SERVED (a read of served data and the live pinned inputs).
</preflight>
