# TO ADVI_COTBKF.TO-CB-ck-1.use-class-label-and-switch -- round 89 CB-ck-1: the served-returns builder gains a `use_class` label (last column of its three tables) and ONE switch, `--yahoo-active-policy interim|blank`; local build only

<to_id>ADVI_COTBKF.TO-CB-ck-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~178</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>89</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-ck-1` (`decompositions/ADVI_COTBKF_DECOMP.round89.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Andrew, 2026-10-15: "Active accounts should get BBG pricing exclusively, inactive accounts are fine with yahoo finance." The securities the active Cottonwood accounts hold (the active set V2) may not be priced from Yahoo; every other security may. The served-returns builder `data/assets/scripts/silver/commonwealth_fwd3_serve.py` prices account-days from a price store whose rows can carry a Yahoo-sourced label; today it labels each such row with a `porting_verdict` (see its comment block "The porting verdict" and the functions `porting_labels`, `day_porting`, `month_porting`) and nothing says that a security is not-for-active. The CTO ruled the guard is per SECURITY (no second price path). Which of the two things Andrew's word means for already-served days is HIS call (open call `3adb`): (i) **interim**: the days stay, labelled `NOT_FOR_ACTIVE`, until each security's Bloomberg series lands; (ii) **blank**: those holdings are blanked now. The CTO's instruction: build both behind ONE switch, default to the one that moves no value, and serve nothing. You build that.

**Read first (under the repository root):**
1. `data/assets/scripts/silver/commonwealth_fwd3_serve.py` whole: the schemas (`SCHEMAS`, the three tables `daily_returns`, `account_day_value`, `month_grades`, each ending in `porting_verdict`), the comment block on the porting verdict and `SEVERITY`, `porting_labels`, `day_porting`, `month_porting`, `daily_table`, `value_table`, `grade_table`, `hold_holdings`, `hold_returns`, `rederive`, `build`, the manifest, the CLI (`--hold-cusips`, `--index`).
2. `data/assets/scripts/silver/commonwealth_price_need.py` (round 87, `CB-ci-1`): `use_classes(index)`, `load_use_classes`, `active_cusips(path=None, expected_sha256=ACTIVE_SET_SHA256)`, `USE_VALUES`, the four branches NO_COLUMN / CLASSES / MALFORMED / UNREADABLE and the fail-closed rule (an unreadable class reads NOT_FOR_ACTIVE). Reuse by `import`; do not copy; do not edit that file.
3. `data/assets/scripts/silver/commonwealth_daily_valuation.py`: `YAHOO_SOURCES`, `is_yahoo_source`, `CASH_STORE` (how a priced row is known to be Yahoo-sourced), and `data/assets/scripts/silver/tests/test_commonwealth_fwd3_serve.py` if present (its style; you add tests, you edit none).
4. The vocabulary and the guard: `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/NEVER_WIDEN_R9_INACTIVE_YAHOO_CTO_HALF.md` (`NOT_FOR_ACTIVE` for a V2-held name, `INACTIVE_USE` otherwise) and `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~173/READERS_RECORD.json` (the readers and their gaps).

**Your items.**

1. **The label.** Add a column `use_class` to each of the three served tables, string typed, **immediately BEFORE `porting_verdict`, which stays the LAST column** (AMENDMENT 1: the existing test `test_commonwealth_fwd3_serve.py` line 331 asserts `porting_verdict` is last, and no existing test may be edited; a reader by name is unaffected either way), built exactly the way `porting_verdict` is: per holding row of the day-values frame, a row priced on a Yahoo-sourced label (cash excluded) reads its security's class, every other row reads `NOT_YAHOO`; the day's and the month's label is the WORST over its Yahoo-priced rows with `SEVERITY_USE = {"INACTIVE_USE": 1, "NOT_FOR_ACTIVE": 2}` (NOT_FOR_ACTIVE wins). A security's class: `NOT_FOR_ACTIVE` when its cusip is in `active_cusips()` OR when the index's class for it is `NOT_FOR_ACTIVE`; `INACTIVE_USE` otherwise; when the V2 set cannot be read or its hash differs, or the index read fails closed, EVERY Yahoo-priced row reads `NOT_FOR_ACTIVE` (fail closed). The existing `porting_verdict` columns and their values must not change by a byte on any existing input, and `porting_verdict` remains the last column of each table.
2. **The switch.** `build(..., yahoo_active_policy="interim")` and the CLI flag `--yahoo-active-policy {interim,blank}` (default `interim`). `interim`: no value moves; only the label is added. `blank`: every CUSIP that has at least one Yahoo-priced holding and class `NOT_FOR_ACTIVE` is added to the build's `hold_cusips` (the existing `--hold-cusips` mechanism: every holding-day of a held CUSIP blank, reason `HELD_SOURCE_UNDER_REVIEW`, the months it touches graded without it), together with any CUSIPs the caller passed; the union is recorded. Nothing else changes between the two branches.
3. **The manifest.** `manifest["use_class"] = {"policy", "branch" (the class read's branch name), "why", "active_set_sha256", "held_by_policy" (the CUSIPs the blank branch added: a COUNT only, never a list of account numbers), "rule": "per_security"}`; the printed `FWD3-BUILD` line gains `use_class_policy=<p>`.
4. **Local only.** The build still writes the three tables locally through `write_local` and the manifest; this cell changes NO S3 write path, runs no `--apply`, serves nothing. If `--apply` is combined with `--yahoo-active-policy blank`, refuse with a message naming call `3adb` (the served move waits for Andrew's reading and a pair).
5. **Tests** (extend the existing test file for the module, or create `data/assets/scripts/silver/tests/test_commonwealth_fwd3_serve_use_class.py` if none exists; edit no existing test): stub frames, made-up CUSIPs (`T00000001`...), eight named tests: `test_use_class_sits_immediately_before_porting_verdict_in_each_served_table`; `test_use_class_row_priced_on_yahoo_in_the_active_set_reads_not_for_active`; `test_use_class_row_not_priced_on_yahoo_reads_not_yahoo`; `test_use_class_day_and_month_take_the_worst_label`; `test_use_class_unreadable_class_or_active_set_fails_closed_to_not_for_active`; `test_use_class_interim_policy_moves_no_value`; `test_use_class_blank_policy_blanks_exactly_the_not_for_active_yahoo_priced_cusips`; `test_use_class_apply_with_blank_is_refused`. Plus one test that the existing `porting_verdict` columns are byte-equal before and after on the same stub input (a control).
6. **The real run, if a default run's data exists.** Look under `C:/dev/ajb_workspace/.scratch/advi_cotbkf/` (read only) for a default run's data dir holding `after/account_day_value.parquet` and `after/security_day_price.parquet` and the sweep re-grade's `<dir>_out/month_grades_after.parquet` and `..._before.parquet`; state what you find. If found, run the build twice to a temp folder under your worktree `.scratch/` (once per policy; `--index` default; no `--apply`) and report the two `FWD3-BUILD` lines; the `interim` run's three tables must equal the pre-change build's values (compare each table's hash with the pre-change commit's output on the same input). If NOT found, write `NO_DATA_DIR` and say so; the stub tests are then the evidence.
7. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~178/USE_CLASS_SERVE_RECORD.json` with exactly these top-level keys: `module_path`, `module_blob` (`git rev-parse HEAD:<module_path>` after your last commit), `new_tests` (the nine names), `existing_tests_unchanged` (true only if `git diff` of every test file you touched shows added lines only), `columns_added` (`use_class`, per table, with its position: just before `porting_verdict`), `policies` (`["interim", "blank"]`), `default_policy`, `real_run` (`{"data_dir_found", "interim_values_equal", "blank_run", "lines"}` or `{"data_dir_found": false, "reason": "NO_DATA_DIR"}`), `s3_writes` (0), `not_established`; and a short `.md`. No account number, name or dollar value in either.

### ACCEPTANCE

<criterion id="CB89ck1-AC1" cell_refs="CB-ck-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_commonwealth_fwd3_serve_use_class.py -q -k use_class</invocation><expect>8 passed</expect></criterion>
`CB89ck1-AC1` -- the eight `use_class` tests pass.

<criterion id="CB89ck1-AC2" cell_refs="CB-ck-1"><invocation>python -c "import json,subprocess;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~178/USE_CLASS_SERVE_RECORD.json',encoding='utf-8'));b=subprocess.check_output(['git','rev-parse','HEAD:'+d['module_path']]).decode().strip();print('USE-CLASS-SERVE blob_equal=%s default=%s s3_writes=%s tests_unchanged=%s'%(b==d['module_blob'],d['default_policy'],d['s3_writes'],d['existing_tests_unchanged']))"</invocation><expect>USE-CLASS-SERVE blob_equal=True default=interim s3_writes=0 tests_unchanged=True</expect></criterion>
`CB89ck1-AC2` -- the record names the module at HEAD and its blob equals what is committed; the default is `interim`; nothing wrote to S3; no existing test was edited.

<criterion id="CB89ck1-AC3" cell_refs="CB-ck-1"><invocation>python -c "import subprocess,sys,glob;fs=sorted(glob.glob('data/assets/scripts/silver/tests/test_commonwealth*fwd3*.py'));r=subprocess.run([sys.executable,'-m','pytest']+fs+['-q'],capture_output=True,text=True);print('FWD3-TESTS files=%d rc=%d last=%s'%(len(fs),r.returncode,r.stdout.strip().splitlines()[-1]))"</invocation><expect>rc=0</expect></criterion>
`CB89ck1-AC3` -- every fwd3 test file, the existing ones and the new one, passes (the existing tests are the control that the label and the switch moved nothing else).

<expected_criteria>CB89ck1-AC1,CB89ck1-AC2,CB89ck1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. You edit `commonwealth_fwd3_serve.py` (additions and the minimum changes the label and the switch need) and add tests; you edit no other module, you do not edit `commonwealth_price_need.py`, `commonwealth_daily_valuation.py` (it is read, not changed; a change you think it needs is a surprise row), `commonwealth_sweep_regrade.py`, the V2 file or any existing test.
- **AWS: READ-ONLY, through the `.tools/aws` shim,** of the one Yahoo index parquet (the footer/schema and the rows the module's index loader reads, as it does today). No S3 write, no `--apply`, no serve, no vendor call. Do not run `aws sts get-caller-identity`.
- **Account numbers and values never appear in any output.** The V2 file is read for its `cusip` column only through `active_cusips()`. The manifest and the record carry counts.
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; on this box it fails closed (the pinned set is on another machine): report the exact error, do NOT look for the set.
- **NEVER** serve, `--apply`, `--overwrite`, `--remint`, change a served key, push, override a gate or `--force`; do not weaken, delete, xfail or skip any test. Scratch under the worktree `.scratch/`, never committed. If a gate refuses a function name or a dtype call (`coerce_silver_ids`), rename or adapt without behaviour change; never override.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W178-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only.

<paths>
data/assets/scripts/silver/commonwealth_fwd3_serve.py
data/assets/scripts/silver/tests/test_commonwealth_fwd3_serve_use_class.py
data/assets/scripts/silver/tests/test_commonwealth_fwd3_serve.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round89.md</decomp_doc> (round 89), cell `CB-ck-1`.
<owned_cells>CB-ck-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB89ck1-AC1, CB89ck1-AC2, CB89ck1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~178/ADVI_COTBKF.TO-CB-ck-1.use-class-label-and-switch.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB89ck1-AC1,CB89ck1-AC2,CB89ck1-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the three criterion lines. Then: the columns added, the two policies and the default; the real-run result or `NO_DATA_DIR`; the diff size of the module and of each test file (removed lines must be 0 in every test file); every S3 read with its denominator; the account-id scan result or exact error; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change to a local builder; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE one read-only index read under the existing role; no write, delete or serve, and no new permission.
comp-adversary: RUN -- the label is built by the porting machinery already in the module and a control test holds `porting_verdict` byte-equal; the default branch moves no value (AC3 runs the existing tests unchanged); the class read fails CLOSED (unreadable reads NOT_FOR_ACTIVE) so a missing column cannot let a Yahoo price through as INACTIVE_USE; BLIND: a security the price store labels as non-Yahoo but whose value is derived from a Yahoo price upstream (the readers record's `not_established` names the Yahoo Close cache and the canonical-prices store's provenance), and the served tables on S3 are not touched by this cell, so the label is local until a served apply under a pair.
lane: the <paths> block IS the grant (worker RULING 1). Local build only; the served move is Andrew's call `3adb` and a never-widen pair.
</preflight>

Source: `1.0.0_SA_CTO~DELL1` msgs 6161, 6175; round 87 `CB-ci-1` and `CB-ci-2` records; row `ADVI_COTBKF-D1-W173-S3`.

**AMENDMENT 1 (2.0.0_SA_COO~C1, 2026-10-15 ~20:5xZ), on your rows `D1-W178-S1` and `D1-W178-S2`:** (S1, my defect at the cut) your worktree's sparse set now includes `data/assets/scripts/` whole and `lib/`; the import chain resolves. (S2) The order said both "use_class LAST" and "edit no existing test"; the existing test pins `porting_verdict` as last. Ruled: `use_class` is inserted immediately BEFORE `porting_verdict`, which stays last; no existing test is edited; the decomposition's cell line ("appended (LAST column)") is superseded by this sentence. Everything else, the criteria and the paths are unchanged. Status pending: continue from item 1; your rows S1 and S2 stay unedited.
