# TO IRPT_BCKEND.TO-IB-pr-586 -- BUILD the Orion Scope account feed: a pull step with one Scope call per household, the coverage rule (ABSENT with a reason class, never a zero), fee_basis NET, its own bronze and silver prefixes built by address(), and its catalog row in the dispatch script

<to_id>IRPT_BCKEND.TO-IB-pr-586</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~429</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8411 and rulings of rounds 118 to 121, on the pair (b) addendum 1 (blob 1e138cbeea, COO half signed) | **Decomp cell:** `IB-pr-586` (decomposition section 218) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-429`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~429 <0.9.0_WK_IRPT_BCKEND~429@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/inf/manual_api/`, then add (locally, never committed) EXACTLY the further directories the import chain of the files you touch and their existing tests needs: run the existing test files named under READ FIRST and add the directory of each import error until they collect (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit. No typed bucket name, `s3://` address or key prefix in a product file: reuse the constants and helpers the builders already use.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array.

**Cell `IB-pr-586` (inlined).** The CTO ordered (msg 8411, on the round-118 to 121 rulings) a new pull step of the Inflection gold chain: the Orion SCOPE ACCOUNT FEED. The design, its rules and its blast radius are the addendum `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/ORION_PAIR_B_ADDENDUM_1_SCOPE_ACCOUNT_FEED.md` (blob `1e138cbeea`, COO half signed): READ ITS SECTIONS 1, 2, 3 AND 5 FIRST; they are the specification and this cell builds exactly them, LOCAL, offline, with tests. Nothing is run against Orion, S3 or the chain; the apply (upload of the script, the one catalog row) is a later act by CloudOps.

**READ FIRST (named files only):** the addendum above; `data/inf/manual_api/pull_inflection_performance_rest.py` (a neighbouring pull step: how it takes `--upload` and a pull date, authenticates, uses `AdaptiveRateLimiter` from `rate_limiter` (line 81, used at line 538), writes bronze, logs and exits); `infra/aws/lambda/investor-reporting/performance/orion_selected.py` (`requests_for`, lines 34 to 109: the inner scope body you must reproduce, ADJACENT to this script, self-contained: the chain runner syncs scripts only, it cannot import the Lambda directory), `infra/aws/lambda/investor-reporting/performance/orion_live.py` (the POST, the `Authorization: Session <jwt>` header, the secret name via `infra/aws/lambda/inf-pipeline/inf-performance-daily/jwt_freshness.py` `SM_SECRET_ID`; you reproduce the minimal auth read, you type no secret value), `infra/aws/lambda/investor-reporting/performance/orion_adapter.py` (lines 112 to 190: the response shape; names of group fields), the probe `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~306/scope_probe2.py` (the request that worked), `lib/opal_naming.py` (`address()`, near line 2499: you call it, you type no address), `data/inf/scripts/gold/orion-gold-dispatch.sh` (the catalog rows near lines 286 to 317, `CHAIN_PULL` near 348, `CHAIN_INCREMENTAL` near 363, the pull-stage tolerate branch near 696 to 716) and an existing test beside a pull script to mirror its harness.

**Build** (all new logic inside `# BEGIN SCOPE-FEED-A` ... `# END SCOPE-FEED-A` lines in the NEW file `data/inf/manual_api/pull_inflection_scope_account_returns.py`; the module must import with the blocks removed):
1. **Arguments:** `--upload` (write; without it nothing is written and the run prints what it would), `--pull-date YYYY-MM-DD` (default: the T-1 trading day, derived the way the neighbouring pull step derives its date; no hand-typed date), `--max-households N` (a bound for a smoke run).
2. **Universe:** the households and accounts of the newest `accounts_v2` roster snapshot at or before the pull date (the loader the neighbouring scripts or `infra/aws/lambda/investor-reporting/performance/orion_account_mapping.py` read it with; read it, mirror it self-contained), intersected with the accounts that hold positions on the pull date in the Inflection positions silver; each account row carries its household id, its Orion account id and its roster `accountStartDate`.
3. **One Scope call per household** with the Account grouping, the INNER scope body (never the wrapper), window = the pull date to the pull date, Daily frequency, `performanceOption.calcGrossOfFees` = false on EVERY request (the test asserts the value in the body of every call), paced by `AdaptiveRateLimiter`, ONE attempt per household (no retry). A call that fails (HTTP error, timeout) is recorded in the bronze envelope with its status and writes NO silver rows for that household (so the household is missing, never zero); a 429 or throttle response that persists after the limiter's own retries STOPS the run (exit non-zero) after recording it.
4. **The coverage rule (silver rows):** for every account in the universe of a successful call, ONE row per account per pull date: `status` `RETURNED` with Orion's return for the day (and the start and end market value of its group), or `status` `ABSENT` with `reason_class` and `reason_claim`: `NO_GROUP` (no Account group for the account), `GROUP_NO_SERIES` (a group with no return or series; cause `NOT_DETERMINED`), `NO_START_DATE_AT_SOURCE` (the roster shows a null `accountStartDate` and the account has no group or no series; claim `measured` when this run's own call saw the account missing, `inferred (pattern measured on 2 households)` otherwise is only for an account NOT observed missing by this run; an account the run DID observe missing with a null start date is `measured`). NEVER a zero return, never an Opal-computed fill. `return` is null on an ABSENT row.
5. **Provenance on every row:** `fee_basis` = `NET`, `fee_basis_note` = `calcGrossOfFees false; tied on 1 household, 2 fee-bearing accounts, Q3 2026`, `calc_gross_of_fees` = false, `source` = `orion_scope`, the pull date, and the call's `dataLastUpdated` when the response carries it.
6. **Writes (only with `--upload`) to the feed's OWN prefixes:** BRONZE one object per pull date: `address()` for source `orion`, scope `inflection`, tier `bronze`, table `scope_account_returns`, partition `date=<pull date>`, object name `scope.json.gz` (a `.json.gz`, NOT `.jsonl.gz`: a test asserts the key does not end in `.jsonl.gz`); it holds the envelope (calls with household token, HTTP status, row counts, failed households) and each successful response. SILVER one object per pull date: the same builder with tier `silver`, object `data.parquet`. **Each key is read ABSENT first (head-object); a key that exists is never overwritten (the run says SKIP and exits zero).** No other key is written. The addresses are builder output; a builder REFUSAL is STOP-and-row (a missing registry row), never a typed address.
7. **The chain hookup, in `data/inf/scripts/gold/orion-gold-dispatch.sh` (repository copy only):** one catalog row `INF_API_PULL_SCOPE_ACCTS|pull_inflection_scope_account_returns.py|--upload` after `INF_API_PULL_PERF`'s silver row, and the id added to `CHAIN_PULL`, `CHAIN_INCREMENTAL` and every other chain that carries `INF_API_PULL_PERF` EXCEPT the single-stage group chains, placed AFTER the steps that land `accounts_v2` and positions. It is a tolerated pull because the dispatch's `INF_API_PULL_*` case already tolerates a pull's failure; a test reads the dispatch text and asserts the row, its entries, their order after the roster and positions steps, and that no other line changed (compare with `git show HEAD:data/inf/scripts/gold/orion-gold-dispatch.sh`). Run the existing dispatch tests `data/inf/scripts/gold/tests/test_aor_resolution.py` and `test_aor_fold_derivation.py`: they stay green.

8. **AMENDMENT 1 (from `2.0.0_SA_COO~I2` msg 8454; the build gets a window parameter, its USE is a later act under its own pair):** an optional `--from-date YYYY-MM-DD`. Without it nothing above changes (window = the pull date). With it: still ONE call per household, window = `--from-date` to the pull date, Daily frequency, the same inner body and `calcGrossOfFees` false; the response's daily series points are split into per-day rows, each day getting the coverage rule over the accounts the household held ON THAT DAY (the roster snapshot at or before that day intersected with that day's positions silver); the bronze envelope and silver are written PER DAY under the same `date=` partitions, and EACH day's keys are read ABSENT first and a day that exists is SKIPPED, never overwritten (a re-run is therefore safe). A day that is not a trading day writes nothing. `--from-date` later than the pull date, or more than 4,000 days back, is refused with a message. Add the test named below.

**Write the tests** `data/inf/manual_api/test_pull_inflection_scope_account_returns.py` (at least 16 tests; synthetic ids and tiny fake roster, positions and responses; a fake transport and a fake S3; NO network): `test_request_body_is_the_inner_scope_with_account_grouping`, `test_every_request_keeps_calcgrossoffees_false`, `test_fee_basis_net_recorded_with_its_note`, `test_covered_account_carries_orion_return`, `test_missing_account_is_absent_no_group_never_zero`, `test_group_without_series_is_group_no_series_not_determined`, `test_null_start_date_account_is_no_start_date_at_source_with_claim`, `test_claim_promoted_to_measured_when_the_call_misses_a_null_start_account`, `test_no_zero_and_no_fill_for_an_absent_account`, `test_one_call_per_household_paced_no_retry`, `test_prefixes_are_address_output_and_bronze_is_json_gz`, `test_key_read_absent_first_and_never_overwritten`, `test_catalog_row_and_chain_entries_present_and_tolerated`, `test_from_date_window_splits_series_into_per_day_rows_and_skips_existing_keys`.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~429/IB223-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["request_body_is_the_inner_scope_with_account_grouping","every_request_keeps_calcgrossoffees_false","fee_basis_net_recorded_with_its_note","covered_account_carries_orion_return","missing_account_is_absent_no_group_never_zero","group_without_series_is_group_no_series_not_determined","null_start_date_account_is_no_start_date_at_source_with_claim","claim_promoted_to_measured_when_the_call_misses_a_null_start_account","no_zero_and_no_fill_for_an_absent_account","one_call_per_household_paced_no_retry","prefixes_are_address_output_and_bronze_is_json_gz","key_read_absent_first_and_never_overwritten","catalog_row_and_chain_entries_present_and_tolerated","from_date_window_splits_series_into_per_day_rows_and_skips_existing_keys"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where each integration is; the sparse directories you added"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` at your first act. `notes` has at least three lines of 30+ characters.

**The difference control (criterion 2).** The check removes every `SCOPE-FEED-A` block IN MEMORY from the product file and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error; reference the new names only inside test functions.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB223-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first; then set the instance's artifact rows to the commit and commit the instance alone in a second commit). Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB223-1-AC1" cell_refs="IB-pr-586"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r223/p223_cells.py" . IB223-1-AC1</invocation><expect>IB223-1-AC1 PASS</expect></criterion>
<criterion id="IB223-1-AC2" cell_refs="IB-pr-586"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r223/p223_cells.py" . IB223-1-AC2</invocation><expect>IB223-1-AC2 PASS</expect></criterion>
<criterion id="IB223-1-AC3" cell_refs="IB-pr-586"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r223/p223_cells.py" . IB223-1-AC3</invocation><expect>IB223-1-AC3 PASS</expect></criterion>

<expected_criteria>IB223-1-AC1, IB223-1-AC2, IB223-1-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 16) and the existing tests named in the paths block pass; AC2 with the SCOPE-FEED-A blocks removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the files named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test stays green and no existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W429-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/inf/manual_api/pull_inflection_scope_account_returns.py
data/inf/manual_api/test_pull_inflection_scope_account_returns.py
data/inf/scripts/gold/orion-gold-dispatch.sh
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-586.scope-account-feed.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~429/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 218 (round 1, workstream ~PN), cell `IB-pr-586`.
<owned_cells>IB-pr-586</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB223-1-AC1, IB223-1-AC2, IB223-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~429/IRPT_BCKEND.TO-IB-pr-586.scope-account-feed.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order adds one new pull script and one catalog row and tests in the repository; nothing is deployed, run against Orion or S3, or written to AWS, so no served byte moves; the apply (upload of the script, the one catalog row on the chain's dispatch object) is a later act under the signed addendum.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p223_cells.py IB223-1 dry-run at base on dell2 2026-10-15 ~16:3xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; seven negatives, each failing its own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~429` (worktree `C:/dev/wk-IRPT_BCKEND-429`). Class LOCAL.
</preflight>
