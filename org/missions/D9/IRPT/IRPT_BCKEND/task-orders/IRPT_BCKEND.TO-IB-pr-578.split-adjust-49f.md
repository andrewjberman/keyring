# TO IRPT_BCKEND.TO-IB-pr-578 -- BUILD the split-adjusted holdings price return for the 49 Financial channel: a declared split source, the custodian ratio measured as the median over accounts without other activity, SPLIT_RATIO_ABSENT where it is not clean, the manifest reason codes

<to_id>IRPT_BCKEND.TO-IB-pr-578</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~421</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PH</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling @9913bf3ed4 (the 2026-04-21 rows are a 6-for-1 split, non-flow; the price-only return must be split-adjusted) on the READ IB-pr-572 (record IB211-1_split_adjust_read.json, row D2-W415) | **Decomp cell:** `IB-pr-578` (decomposition section 212) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-421`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~421 <0.9.0_WK_IRPT_BCKEND~421@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/irpt_holdings_performance/`, then add (locally, never committed) EXACTLY the further directories the import chain of the files you touch and their existing tests needs: run the existing test files named under READ FIRST and add the directory of each import error until they collect (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit. No typed bucket name, `s3://` address or key prefix in a product file: reuse the constants and helpers the builders already use.

**Cell `IB-pr-578` (inlined).** The holdings price return (`holdings_return`, `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` near line 743; the contribution at line 816 is `v * (p1 / p0 - 1)`) is NOT split-adjusted: on a split day p1 is the post-split price, p0 the pre-split price, and a holding whose value did not change reads as a loss of about (N - 1) / N. The CTO ruled (@9913bf3ed4) that the 2026-04-21 6-for-1 rows are a stock split, non-flow, and the return must be adjusted by the custodian's own ratio. The READ (IB-pr-572, `deliverables/0.9.0_WK_IRPT_BCKEND~415/IB211-1_split_adjust_read.json`) measured the 49 Financial channel: 1,348 split rows over 47 split days in the custodian transactions table; Cottonwood and Inflection carry no usable key (they follow in their own cells). This cell builds the adjustment for the 49 Financial channel ONLY, LOCAL, offline, with tests. Producer changes move served values on split days: the served DELTA and the never-widen pair come after, from a producer dry run, not from this cell.

**READ FIRST (named files only):** `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` (`holdings_return` 743 to 900, `price_of` 623, `_frame_for` 973 to 1083, `validate_entry`, `declared_columns`, the manifest builder near 1140 to 1180, `STATUS_REASONS` 228), `data/assets/scripts/gold/irpt_holdings_performance/sources.json` (the first entry: its `quantity_column`, `identifier_columns`, `partition_form`), `data/assets/scripts/gold/irpt_holdings_performance/tests/test_holdings_performance.py` (how a day is driven offline with synthetic frames) and `data/assets/scripts/gold/irpt_holdings_performance/tests/test_holdings_comparison.py`.

**The measured source (given, do not re-read S3):** the 49 Financial transactions table sits under the prefix `schwab/08335338/silver/fact_trn/` (partitions `date=YYYY-MM-DD/`, the same bucket and partition form as the entry's positions prefix) and carries the columns `tran_srcde`, `transaction_source_code_description`, `cusip`, `account_id`, `quantity`, `business_date`. A split row has `tran_srcde` equal to `STK` and `transaction_source_code_description` equal to `STOCK SPLIT` (991 such rows on 2026-04-21, one per account and security). The positions table carries `cusip`, `account_id` and `quantity_settled_unsettled`.

**Change (all new producer logic inside `# BEGIN SPLIT-ADJUST-A` ... `# END SPLIT-ADJUST-A` lines; module-level code outside the blocks must leave the module importable with the blocks removed):**
1. `sources.json`, first entry only: an optional object `split_adjust` = `{"transactions_prefix": "schwab/08335338/silver/fact_trn/", "split_source_column": "tran_srcde", "split_source_value": "STK", "split_text_column": "transaction_source_code_description", "split_text_contains": "STOCK SPLIT", "security_column": "cusip", "account_column": "account_id", "clean_ratio_tolerance_percent": 0.5, "max_numerator": 60, "max_denominator": 10, "min_agreeing_percent": 90}` with a `split_adjust_comment` giving the READ as the basis. The other entries get no `split_adjust` and must behave byte-identically. `validate_entry` accepts and shape-checks the object (every key present, the percents in 0 to 100, the integers positive); a malformed object is a REFUSAL, never a default. The declaration `schema_version` stays "1.2" unless the producer cannot read the new key any other way: then STOP with a row.
2. A PURE function `measure_split_ratios(split_securities, prev_positions, day_positions, activity, cfg, src)` returning `{security: {"status": "OK"|"SPLIT_RATIO_ABSENT", "ratio": <float or None>, "accounts_used": n}}`. For each split security: for every account with quantity above zero on BOTH days and NO non-split transaction row that day in that security (`activity` is the day's transactions rows other than the split rows), r = q(day) / q(prior); the raw ratio is the MEDIAN of those r. The ratio is CLEAN when some n/m (n up to `max_numerator`, m up to `max_denominator`) lies within `clean_ratio_tolerance_percent` of the median; the ratio used is that exact n/m (6.0 for a 6-for-1, 0.5 for a 1-for-2). It is accepted only when at least `min_agreeing_percent` of the accounts used lie within the tolerance of it; with no account used, or a ratio that is not clean, or too few agreeing, the status is `SPLIT_RATIO_ABSENT` and the ratio None.
3. `holdings_return` gains an optional keyword `split_ratios=None` (None: byte-identical to today). For a security key with status OK the t-1 price basis `_p0` is divided by the ratio before the contribution: the contribution is `v * (p1 / (p0 / r) - 1)`. A security key with status `SPLIT_RATIO_ABSENT` is NOT graded: it is treated as unpriced (the existing excluded class), so it leaves the basket and counts in `excluded_count` and `excluded_value`. The columns of the emitted frame and the Arrow schema do not change.
4. `_frame_for` (the ruling-16 grade; `compute_day` calls it): when the entry declares `split_adjust`, read the day's transactions partition through the same `read` lambda (needed columns only), derive the day's split securities and the activity rows, call `measure_split_ratios` with the two positions partitions it already holds, and pass the result to `holdings_return`. The transactions partition absent for the day: the return stays unadjusted, and the frame carries `split_adjust_status = "SPLIT_UNADJUSTED_COMPARISON"` in `frame.attrs` (a fact, not a refusal). An entry with no `split_adjust` carries `SPLIT_UNADJUSTED_COMPARISON` too, so the manifest says which firms are unadjusted.
5. The run manifest (where the file builds it) gains `split_adjust`: `{"declared": bool, "reason_codes": {"SPLIT_RATIO_ABSENT": "...", "SPLIT_UNADJUSTED_COMPARISON": "..."}, "split_days": n, "securities_adjusted": n, "securities_ratio_absent": n}` with counts summed over the run; a run over a firm with no declaration and no split day changes only by this block.

**AMENDMENT 1 (issuer ruling on your rows W421-S1 and S2; this overrides the refusal clause on the one point it names).** (1) The existing test `test_an_own_date_source_reads_exactly_the_partitions_it_always_read` in `data/assets/scripts/gold/irpt_holdings_performance/tests/test_holdings_performance.py` (near lines 940 to 954) asserts the reads of a source that now declares `split_adjust`; it is the ONE existing assertion you may change, and only like this: keep the test, but give its stub entry NO `split_adjust` object (copy the entry and delete the key in the test, so the three-read assertion stays word for word true for an entry without the declaration), and put the four-read case in your NEW test file (`test_split_adjust.py`: an entry that declares `split_adjust` reads the transactions partition `date=DAY` through the same `read` lambda as a fourth read, and the stub answers it with a transactions-shaped frame). No other existing assertion changes. (2) Row W421-S2: the split security's key is the SAME identifier chain the positions use: the transactions read takes `cusip` AND `ticker_symbol`, and the security key is built with the entry's `identifier_columns` chain (first non-empty), so a split holding with a blank cusip still matches by ticker; add a test for it (`test_split_adjust.py`, any name).

**Write the tests** `data/assets/scripts/gold/irpt_holdings_performance/tests/test_split_adjust.py` (at least 10 tests; synthetic cusips, accounts and values, tiny frames): `test_split_day_unchanged_holding_reads_zero_return`, `test_ratio_is_the_median_over_accounts_without_other_activity`, `test_unclean_ratio_is_split_ratio_absent_and_not_graded`, `test_no_split_day_is_identical_to_the_unadjusted_return`, `test_reverse_split_ratio_below_one`, `test_firm_without_a_split_declaration_is_unchanged`, `test_declaration_shape_is_validated`, `test_manifest_carries_the_reason_codes_and_counts`, `test_partial_sale_on_the_split_day_is_not_used_for_the_ratio`. `split_day_unchanged_holding_reads_zero_return` builds a 6-for-1 day (quantity x6, price /6, value unchanged) and asserts the daily return is 0 with the ratio and about -83 percent without it (the defect). `ratio_is_the_median_over_accounts_without_other_activity` includes one account with a buy that day and asserts it is not in the median.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~421/IB216-2_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["split_day_unchanged_holding_reads_zero_return","ratio_is_the_median_over_accounts_without_other_activity","unclean_ratio_is_split_ratio_absent_and_not_graded","no_split_day_is_identical_to_the_unadjusted_return","reverse_split_ratio_below_one","firm_without_a_split_declaration_is_unchanged","declaration_shape_is_validated","manifest_carries_the_reason_codes_and_counts","partial_sale_on_the_split_day_is_not_used_for_the_ratio"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where each integration is; the sparse directories you added"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` at your first act. `notes` has at least three lines of 30+ characters.

**The difference control (criterion 2).** The check removes every `SPLIT-ADJUST-A` block IN MEMORY from the product file(s) and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error; reference the new names only inside test functions.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB216-2_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first; then set the instance's artifact rows to the commit and commit the instance alone in a second commit). Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB216-2-AC1" cell_refs="IB-pr-578"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r216/p216_cells.py" . IB216-2-AC1</invocation><expect>IB216-2-AC1 PASS</expect></criterion>
<criterion id="IB216-2-AC2" cell_refs="IB-pr-578"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r216/p216_cells.py" . IB216-2-AC2</invocation><expect>IB216-2-AC2 PASS</expect></criterion>
<criterion id="IB216-2-AC3" cell_refs="IB-pr-578"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r216/p216_cells.py" . IB216-2-AC3</invocation><expect>IB216-2-AC3 PASS</expect></criterion>

<expected_criteria>IB216-2-AC1, IB216-2-AC2, IB216-2-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 10) and the existing tests named in the paths block pass; AC2 with the SPLIT-ADJUST-A blocks removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the producer file, its declaration and the tests named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test stays green and no existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change (except the one edit AMENDMENT 1 names); a typed object address in product code; a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W421-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py
data/assets/scripts/gold/irpt_holdings_performance/sources.json
data/assets/scripts/gold/irpt_holdings_performance/tests/test_split_adjust.py
data/assets/scripts/gold/irpt_holdings_performance/tests/test_holdings_performance.py
data/assets/scripts/gold/irpt_holdings_performance/tests/test_holdings_comparison.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~421/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 212 (round 1, workstream ~PH), cell `IB-pr-578`.
<owned_cells>IB-pr-578</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB216-2-AC1, IB216-2-AC2, IB216-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~421/IRPT_BCKEND.TO-IB-pr-578.split-adjust-49f.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one producer file and its declaration file and adds tests; nothing is deployed or run against a served prefix, so no served byte moves; the release of the changed producer, the served DELTA on split days (a producer dry run, before and after) and the never-widen pair are later acts; Cottonwood and Inflection follow in their own cells.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p216_cells.py IB216-2 dry-run at base on dell2 2026-10-15 ~13:5xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; seven negatives, each failing its own arm: no marker block, a marker removal that breaks import, a weak test file, too few tests, a stray path, a missing named test, a typed object address.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~421` (worktree `C:/dev/wk-IRPT_BCKEND-421`). Class LOCAL.
</preflight>
