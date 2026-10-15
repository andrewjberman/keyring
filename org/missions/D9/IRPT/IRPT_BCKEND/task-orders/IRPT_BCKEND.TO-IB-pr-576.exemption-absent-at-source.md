# TO IRPT_BCKEND.TO-IB-pr-576 -- BUILD the closed_at_source exemption of the account_lost condition in the holdings publish gate: exempt ONLY when the source shows the account with no positions in BOTH tables on the candidate date AND the prior trading day, both partitions complete, and record it in the manifest; the guard otherwise unchanged

<to_id>IRPT_BCKEND.TO-IB-pr-576</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~419</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PG</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msgs 8268 and 8284 ("build the S196 exemption now, one pair for both firms, with a completeness condition") on the 49 Financial and Cottonwood reads (IB-pr-570 to 575, rows D2-S194, S197, W417-S1 to S6, W418-S1 to S3) | **Decomp cell:** `IB-pr-576` (decomposition section 211) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-419`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~419 <0.9.0_WK_IRPT_BCKEND~419@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.** Python: ASCII only in product code and logs; tests use synthetic ids and values.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/`, then add (locally, never committed) EXACTLY the directories the import chain of `holdings_snapshot.py` and its existing tests needs: run `python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py -q` and add the directory of each import error until it collects (earlier workers on this file needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared` and `docs/contracts/investor-reporting/v1`). Nothing wider.

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value; tests use synthetic ids and values.

**Cell `IB-pr-576` (inlined).** The holdings publish gate (`evaluate_publish_gate` in `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, near lines 2888 to 3060; the lost-account condition is added near line 3058 as `add("account_lost", gone - closed)`) refuses a candidate that LOSES an account the served snapshot holds. Cottonwood (served 2026-10-08) and 49 Financial (the P1 firm, served 2026-10-12) are stale because the source shows their lost account with NO positions (Cottonwood: two no-position rows per day and an empty custody frame; 49 Financial: 20 positions on 2026-10-12 and none on 2026-10-13 or 2026-10-14), and the directory carries no TERMINATED mark the gate's `closed` set could read (the directory writer cannot produce one for an account absent from its source). The CTO ruled (msg 8284) the **closed_at_source exemption**: **exempt an `account_lost` ONLY when ALL hold: (1) the source shows the account with no positions (absent OR zero) in BOTH the positions and the balance tables on the candidate date AND the prior trading day; (2) each of those partitions is COMPLETE: its account count is at least 95 percent of the prior day's (a truncated file never exempts); (3) each exempted account is recorded in the publication manifest as `closed_at_source` with its dates.** A reappearing account is re-included by the daily rebuild (it is simply no longer lost). One zero day alone still refuses; TERMINATED handling is unchanged; every other condition is untouched; nothing else in the gate changes.

**READ FIRST (named files only):** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (`evaluate_publish_gate`, `closed_account_ids`, `directory_marks_no_closures`, the `listed` block with `account_lost_not_refused`, `write_refusal_record`, the manifest the publisher writes and `run_firm`'s call of the gate near line 3185) and the tests `data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py`, `test_directory_exemption_source_marks.py`, `test_holdings_bypass_one_date.py` (how a gate is driven offline with a synthetic snapshot and stub providers: mirror it).

**AMENDMENT 1 (the CTO's msg 8290, CVO ADJUDICATION_v117: closure and feed omission are indistinguishable). Three changes to the text below: (i) the manifest records each exempted account as `absent_at_source` WITH ITS DATES (the candidate day and the prior trading day), with the claim `measured` for the absence and `unknown` for closure; the word "closed" is NEVER written anywhere in the manifest, the gate's listing or the snapshot (the gate listing is `account_lost_absent_at_source`); (ii) to cover a live account dropped by omission, the SERVED SNAPSHOT keeps the exempted account listed in its household: no current holdings (no position nodes), the words "Not reported by the custodian since <date>" (the date is the first day the source stopped reporting it: the candidate day's prior trading day... use the earliest of the evidence's absent days), and its last served value is NEVER shown as current; (iii) the pair will state both branches (closed, or omitted). Wherever this order says `closed_at_source` read `absent_at_source`, and the test name `manifest_records_closed_at_source_with_dates` is now `manifest_records_absent_at_source_with_dates_never_closed`; a NEW eighth named test `served_snapshot_keeps_the_account_listed_with_the_not_reported_words` is required (the nine tests in all).**

**AMENDMENT 2 (issuer, on your rows W419-S1 to S3): (i) SCOPE: part (ii) of AMENDMENT 1 (the exempted account kept listed in its household of the SERVED snapshot) needs `holdings_49f.py`, `holdings_inf.py`, `holdings_membership.py` and the publisher's `publication.py`, which are outside this order's paths; it moves to the next cell (IB-pr-577). In THIS order build what you built: the pure exemption, the gate's provider argument, the `absent_at_source` record in the run manifest (snapshot `_manifest`, as you did; the published `.manifest.json` is written by `publication.py`, also the next cell's) and the `not_reported_display` words helper with the test of the eighth name; your test named `served_snapshot_keeps_the_account_listed_with_the_not_reported_words` must say in its docstring that it grades the words helper and the run-manifest record, and that the household placement is IB-pr-577. (ii) THE INSTANCE PATH: the long order path exceeds Windows MAX_PATH on this box; the instance now goes at the SHORT path under proof_of_spec below; write it there, commit it, and validate it as you did (a short copy of the order file may stand in for the long order path in your validation run; the issuer re-validates in the main tree at the drain). Its `decomp_ref.to_ref` and `spec_ref.doc` keep the order's real repository path.**

**Change (all new logic inside `# BEGIN CLOSED-AT-SOURCE-A` ... `# END CLOSED-AT-SOURCE-A` lines in `holdings_snapshot.py`; module-level code outside the blocks must leave the module importable with the blocks removed):** (1) a PURE function `closed_at_source_exempt(lost_ids, evidence)` where `evidence` is the source evidence for one firm and one candidate date: for each of the two tables (positions, balance) and each of the two days (candidate, prior): `{"account_count": <n>, "accounts_with_positions": <set of ids with positions above zero>}`; it returns `(exempt_ids, details)` where an id is exempt only when it is in neither `accounts_with_positions` set of either table on either day (absent or zero) AND, for every table, the candidate day's `account_count` is at least 95 percent of the prior day's and the prior partition exists; `details` carries per-id `{"candidate_day","prior_day"}`; (2) `evaluate_publish_gate` takes ONE new optional provider argument (default `None`, which changes nothing: every existing call and test is unaffected) returning that evidence; an exempted lost id is removed from the `account_lost` condition and listed under `gate["listed"]["account_lost_closed_at_source"]` with its dates; a lost id that is NOT exempted still raises `account_lost`; (3) the publication manifest records each exempted account as `closed_at_source` with its dates (the candidate day and the prior trading day), written by the same place that writes the other manifest facts; the manifest of a run with no exempted account is byte-unchanged. The loader that builds the evidence from each firm's source partitions is the NEXT cell: here the provider is an injected callable and the tests use synthetic evidence.

**Write the tests** `data/assets/scripts/gold/investor_reporting/tests/test_closed_at_source_exemption.py` (at least 9 tests; synthetic ids): `test_exempts_when_both_days_have_no_positions_and_both_partitions_are_complete`, `test_one_zero_day_still_refuses` (zero on the candidate day only), `test_truncated_partition_never_exempts` (a candidate-day partition at 94 percent of the prior day's: refuses; at 95 percent: exempts), `test_present_in_either_table_refuses` (positions above zero in the balance table or the positions table, on either day), `test_manifest_records_absent_at_source_with_dates_never_closed` (and no "closed" string in the manifest entry), `test_served_snapshot_keeps_the_account_listed_with_the_not_reported_words`, `test_terminated_path_unchanged`, `test_other_conditions_still_refuse` (an exempted account does not hide a second lost account or another condition, and the outcome stays REFUSED), and at least one more (a provider that is `None` leaves the existing outcome identical; an absent prior partition never exempts). Name the eight listed exactly (the check reads the names).

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~419/IB215-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["exempts_when_both_days_have_no_positions_and_both_partitions_are_complete","one_zero_day_still_refuses","truncated_partition_never_exempts","present_in_either_table_refuses","manifest_records_closed_at_source_with_dates","terminated_path_unchanged","other_conditions_still_refuse"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where the gate integration is; the sparse directories you added"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` before your first commit.

**The difference control (criterion 2).** The check removes every `CLOSED-AT-SOURCE-A` block IN MEMORY from `holdings_snapshot.py` and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error; reference the new names only inside test functions.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB215-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product file, tests, record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR work (never the check); a check no work can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB215-1-AC1" cell_refs="IB-pr-576"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r215/p215_cells.py" . IB215-1-AC1</invocation><expect>IB215-1-AC1 PASS</expect></criterion>
<criterion id="IB215-1-AC2" cell_refs="IB-pr-576"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r215/p215_cells.py" . IB215-1-AC2</invocation><expect>IB215-1-AC2 PASS</expect></criterion>
<criterion id="IB215-1-AC3" cell_refs="IB-pr-576"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r215/p215_cells.py" . IB215-1-AC3</invocation><expect>IB215-1-AC3 PASS</expect></criterion>

<expected_criteria>IB215-1-AC1, IB215-1-AC2, IB215-1-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 9) and the existing publish-gate tests pass; AC2 with the CLOSED-AT-SOURCE-A blocks removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the eight named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the product file and the tests named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. The publish guard's other conditions, the TERMINATED path, the one-date bypass and every existing test stay unchanged.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs the producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change (never edit an existing assertion); a typed object address in product code; a real account id in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W419-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_closed_at_source_exemption.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_bypass_one_date.py
data/assets/scripts/gold/investor_reporting/tests/test_directory_exemption_source_marks.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~419/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 211 (round 1, workstream ~PG), cell `IB-pr-576`.
<owned_cells>IB-pr-576</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB215-1-AC1, IB215-1-AC2, IB215-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~419/IRPT_BCKEND.TO-IB-pr-576.exemption-absent-at-source.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one producer file and adds tests in the repository; nothing is deployed or run against a served prefix, so no served byte moves; the release of the changed gate to the firms' bundles, the evidence loaders and the served DELTA (measured by a producer dry run, before and after, per firm) are later acts under one never-widen pair covering 49 Financial and Cottonwood.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p215_cells.py IB215-1 dry-run at base on dell2 2026-10-15 ~13:2xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; seven negatives on this cell, each failing its own arm: no marker block, a marker removal that breaks import, a weak test file, too few tests, a stray path, a missing named test, a typed object address.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~419` (worktree `C:/dev/wk-IRPT_BCKEND-419`). Class LOCAL (repository edits and tests; no deploy, no served byte).
</preflight>
