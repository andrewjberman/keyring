# TO IRPT_BCKEND.TO-IB-pr-577 -- WIRE the absent_at_source exemption LIVE with its visible listing: per-firm source evidence loaders, run_firm passes them to the gate, the exempted account stays listed ("Not reported by the custodian since <date>", no value), the published manifest carries it, and every "closed" name becomes absent_at_source

<to_id>IRPT_BCKEND.TO-IB-pr-577</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~420</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PH</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msgs 8284, 8290, 8302 and 8311 (the exemption and its listing land in ONE change; rename the closed names), on the worker 419 rows W419-S1 and S2 (rows D2-S201) | **Decomp cell:** `IB-pr-577` (decomposition section 212) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-420`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~420 <0.9.0_WK_IRPT_BCKEND~420@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/`, then add (locally, never committed) EXACTLY the further directories the import chain of the files you touch and their existing tests needs: run the existing test files named under READ FIRST and add the directory of each import error until they collect (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit. No typed bucket name, `s3://` address or key prefix in a product file: reuse the constants and helpers the builders already use.

**Cell `IB-pr-577` (inlined).** IB-pr-576 built the `absent_at_source` exemption of the publish gate's `account_lost` condition inside `holdings_snapshot.py` (`absent_at_source_exempt`, `absent_at_source_record`, `not_reported_display` and the gate argument `absent_at_source_evidence`, in blocks currently marked `CLOSED-AT-SOURCE-A`). It is INERT: `run_firm` (near line 3188) calls the gate without the provider. The CTO ruled (msg 8311): the exemption goes live ONLY together with the visible listing of the account (kept in the served snapshot, "Not reported by the custodian since <date>", no stale value as current), in ONE change, so it can never drop an account silently; and every remaining "closed" name becomes `absent_at_source` (the source cannot tell a closed account from one whose feed omitted it). This cell builds all of it, LOCAL, offline, with tests.

**READ FIRST (named files only):** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (the CLOSED-AT-SOURCE-A blocks near lines 3014 to 3125 and 3277; `run_firm` 3188 to 3301; `land` near 2840 to 2900; `_node` 560; `build_snapshot`; `VersionedInputs` use at 3197; `served_publication` 2938; `BUILDERS` near 2668), `data/assets/scripts/gold/investor_reporting/holdings_49f.py` (`load_49f_sources` near 210 to 233 and `build_49f_actual` near 310 to 380: what it reads, with which helper, and how an account id is minted), `data/assets/scripts/gold/investor_reporting/source_inputs.py` (VersionedInputs: reads of a candidate-day key return the pinned version), `infra/aws/lambda/investor-reporting/holdings/publication.py` (`HoldingsPublication.publish`, manifest dict near lines 269 to 290), `lib/trading_calendar.py` (`prev_trading_day`), and the tests `data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py` (the `VersionedS3`, `_Inputs`, `make_snapshot` and `fire` harness: drive `run_firm(upload=True)` end to end with it), `data/assets/scripts/gold/investor_reporting/tests/test_closed_at_source_exemption.py`, `data/assets/scripts/gold/investor_reporting/tests/test_holdings_bypass_one_date.py`, `infra/aws/lambda/investor-reporting/holdings/tests/test_publication.py`.

**Change 1: the rename (first, alone, one commit).** In `holdings_snapshot.py` and its tests, rename every identifier, constant, dict key, comment and marker line that carries `closed_at_source`, `CLOSED_AT_SOURCE` or `CLOSED-AT-SOURCE` to the `absent_at_source`, `ABSENT_AT_SOURCE`, `ABSENT-AT-SOURCE` form (the marker `CLOSED-AT-SOURCE-A` becomes `ABSENT-AT-SOURCE-A`; the test file is `git mv`-ed to `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_exemption.py`, the name its docstring already uses). DO NOT rename the TERMINATED path (`closed_account_ids`, `closed_accounts`, the `closed_accounts_not_refused` listed key): that is the directory's own closed mark and a different fact. A test `no_closed_names_remain` reads the product file and the test files and asserts no name containing `closed_at_source` (any case) remains. Every existing test passes after the rename.

**Change 2: the evidence loaders** (all new logic inside `# BEGIN ABSENT-AT-SOURCE-B` ... `# END ABSENT-AT-SOURCE-B` lines; module-level code outside the blocks must leave the module importable with the blocks removed). A function `source_evidence_for(builder, firm_id, inputs, candidate_day)` returns the evidence dict `absent_at_source_exempt` reads (documented in its docstring), plus `first_absent_day` and `since_bound_reached`, or `None` for any builder that has no reader. Dispatch by the BUILDER the firm maps to in `BUILDERS` (a table keyed by the builder function, NOT by a typed firm name): the 49 Financial builder (`holdings_49f.build_49f_meshed`) and the Cottonwood builder (`build_cot`). Rules both readers obey: (a) read through the `inputs` object `run_firm` already holds, so the candidate day returns the SAME pinned bytes the build read; reuse the prefixes, key builder and `_read_parquet` the builders use, typing none; (b) the candidate day is the build's CUSTODY date (`clocks.custody_as_of` for 49 Financial, `clocks.business_date` for Cottonwood), the prior day is `tcal.prev_trading_day(candidate_day)`; (c) `account_count` is the number of DISTINCT accounts in the partition; (d) `accounts_with_positions` holds the SERVED ids (the opaque ids the builder mints for an account: use the builder's own id function and text normaliser, so a lost account compares equal), for accounts whose row is not zero; a row whose value is non-numeric counts as PRESENT (fail closed); (e) any missing partition, empty object, `SourceRefused`, parse error or other exception returns `None` (the refusal then stands); (f) `first_absent_day`: read the POSITIONS table (account column only) back one trading day at a time from the prior day, up to 30 trading days, and name the earliest day of the unbroken run on which NONE of the lost account ids has positions; when the bound is reached `since_bound_reached` is true. 49 Financial: positions table `dim_position` (account `account_id`, a row has a position when `market_value_settled_unsettled` or `quantity_settled_unsettled` is not zero), balance table `dim_balance` (account `account_id`, `net_mv_plus_cash`). Cottonwood: positions table `fact_holdings` (account `AccountID`; a row has a position when any of `Market Value`, `Units`, `Unaccrued Market Value`, `Accrual` is not null and not zero; the builder treats a row with all four null as no position), balance table `fact_allocations` (account `AccountID`; use the SAME column the builder ties its independent total to near line 2387; if the builder uses no single column, STOP with a row).

**Change 3: the wiring and the listing.** `run_firm` passes `absent_at_source_evidence=lambda: source_evidence_for(...)` to the gate (a provider that returns `None` leaves today's behaviour). After the gate returns PUBLISHED with `listed.account_lost_absent_at_source`, and BEFORE `land`, `run_firm` appends for each exempted id a FRESH zero-value ACCOUNT node built with `_node` exactly as the holdout path builds its ACCOUNT nodes, with no children, `display=not_reported_display(first_absent_day)` and NO amount shown as current (amount 0.0; choose the basis/claim values that the snapshot schema allows for "not measured" and record your choice in the notes; `validate_snapshot` must pass), and it brings the snapshot's own account bookkeeping in line: the id in `scope.account_ids`, `custody_totals.unique_account_count` plus the count added, and `resolved_scope_fingerprint` recomputed by the same function `build_snapshot` uses (if the fingerprint cannot be recomputed by a pure function, STOP with a row). The listing runs ONLY when the gate exempted an id; a run with no exemption leaves nodes and manifest byte-identical (test `no_exemption_leaves_nodes_and_manifest_unchanged`). The next fire sees the listed account in the served snapshot, finds it missing from its own candidate and exempts it again while the evidence still shows absence (test `second_fire_exempts_again_with_the_same_since_date`); if the account reappears with positions the candidate carries it normally (test `reappearing_account_is_included_normally`).

**Change 4: the published manifest.** `absent_at_source_record` (inside the renamed block) records each exempted id as `{"account_id", "status":"absent_at_source", "absence_claim":"measured", "closure_claim":"unknown", "candidate_day", "prior_day", "first_absent_day", "since_bound_reached"}`. `infra/aws/lambda/investor-reporting/holdings/publication.py`: `HoldingsPublication.publish` takes an optional `absent_at_source=None` and, when it is a non-empty list, sets `manifest["absent_at_source"]` beside the `source_objects` block (all new lines inside `# BEGIN ABSENT-AT-SOURCE-B` / `# END` blocks; a call without the argument produces a byte-identical manifest). `land` passes `snapshot["_manifest"].get("absent_at_source")`, and ONLY when it is non-empty (so a publisher without the argument is never called with it).

**Write the tests** `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_wiring.py` (at least 14 tests; synthetic ids, tiny synthetic frames; the harness of `test_holdings_publish_gate.py`): `test_evidence_49f_counts_accounts_and_positions_in_both_tables`, `test_evidence_cottonwood_reads_holdings_and_allocations`, `test_evidence_missing_prior_partition_fails_closed`, `test_loader_error_keeps_the_refusal`, `test_run_firm_publishes_with_the_account_still_listed`, `test_listed_account_has_the_not_reported_words_and_no_value`, `test_scope_and_unique_count_include_the_listed_account`, `test_published_manifest_carries_absent_at_source_never_closed`, `test_second_fire_exempts_again_with_the_same_since_date`, `test_reappearing_account_is_included_normally`, `test_no_exemption_leaves_nodes_and_manifest_unchanged`, `test_no_closed_names_remain`. `evidence_missing_prior_partition_fails_closed` and `loader_error_keeps_the_refusal` assert the gate outcome is REFUSED with `account_lost`. `run_firm_publishes_with_the_account_still_listed` runs `run_firm(upload=True)` against the in-memory S3 twice: without the provider (REFUSED, today) and with the readers (PUBLISHED, the account listed).

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~420/IB216-1_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["evidence_49f_counts_accounts_and_positions_in_both_tables","evidence_cottonwood_reads_holdings_and_allocations","evidence_missing_prior_partition_fails_closed","loader_error_keeps_the_refusal","run_firm_publishes_with_the_account_still_listed","listed_account_has_the_not_reported_words_and_no_value","scope_and_unique_count_include_the_listed_account","published_manifest_carries_absent_at_source_never_closed","second_fire_exempts_again_with_the_same_since_date","reappearing_account_is_included_normally","no_exemption_leaves_nodes_and_manifest_unchanged","no_closed_names_remain"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where each integration is; the sparse directories you added"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` at your first act. `notes` has at least three lines of 30+ characters.

**The difference control (criterion 2).** The check removes every `ABSENT-AT-SOURCE-B` block IN MEMORY from the product file(s) and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error; reference the new names only inside test functions.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB216-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first; then set the instance's artifact rows to the commit and commit the instance alone in a second commit). Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB216-1-AC1" cell_refs="IB-pr-577"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r216/p216_cells.py" . IB216-1-AC1</invocation><expect>IB216-1-AC1 PASS</expect></criterion>
<criterion id="IB216-1-AC2" cell_refs="IB-pr-577"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r216/p216_cells.py" . IB216-1-AC2</invocation><expect>IB216-1-AC2 PASS</expect></criterion>
<criterion id="IB216-1-AC3" cell_refs="IB-pr-577"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r216/p216_cells.py" . IB216-1-AC3</invocation><expect>IB216-1-AC3 PASS</expect></criterion>

<expected_criteria>IB216-1-AC1, IB216-1-AC2, IB216-1-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 14) and the existing tests named in the paths block pass; AC2 with the ABSENT-AT-SOURCE-B blocks removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build of the product file and one lambda source file (a path under infra/ makes the class WORLD, though nothing is deployed): you write the files named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test stays green and no existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W420-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_wiring.py
data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_exemption.py
data/assets/scripts/gold/investor_reporting/tests/test_closed_at_source_exemption.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_bypass_one_date.py
infra/aws/lambda/investor-reporting/holdings/publication.py
infra/aws/lambda/investor-reporting/holdings/tests/test_publication.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~420/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 212 (round 1, workstream ~PH), cell `IB-pr-577`.
<owned_cells>IB-pr-577</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB216-1-AC1, IB216-1-AC2, IB216-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~420/IRPT_BCKEND.TO-IB-pr-577.wire-absent-at-source.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one producer file and one lambda source file and adds tests; nothing is deployed or run against a served prefix, so no served byte moves; the release of the changed code to the firms' bundles (an apply), the served DELTA per firm (a producer dry run with and without the exemption alone) and the never-widen pair are later acts under one pair covering 49 Financial and Cottonwood, both branches (closed, and a live account the feed omitted).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p216_cells.py IB216-1 dry-run at base on dell2 2026-10-15 ~13:5xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; seven negatives, each failing its own arm: no marker block, a marker removal that breaks import, a weak test file, too few tests, a stray path, a missing named test, a typed object address.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~420` (worktree `C:/dev/wk-IRPT_BCKEND-420`). Class WORLD.
</preflight>
