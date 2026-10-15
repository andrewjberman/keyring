# TO ADVI_COTBKF.TO-CB-ci-1.price-need-reads-use-class -- round 87 CB-ci-1: commonwealth_price_need.py reads the Yahoo index's use_class, so a NOT_FOR_ACTIVE Yahoo price never counts as covering a security held in the active set

<to_id>ADVI_COTBKF.TO-CB-ci-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~172</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>87</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-ci-1` (`decompositions/ADVI_COTBKF_DECOMP.round87.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Andrew, 2026-10-15: "Active accounts should get BBG pricing exclusively, inactive accounts are fine with yahoo finance." MDPF_DEMQUE is adding a column `use_class` to the Yahoo price index (`opal_naming.address("yahoo","global","silver","price_history","index","index.parquet")`): `NOT_FOR_ACTIVE` for a security held in the active Cottonwood set V2, `INACTIVE_USE` otherwise. `data/assets/scripts/silver/commonwealth_price_need.py` ranks the securities that leave a held account-day unpriced, and marks a row `covered` when the index holds a price for its whole held span. Today that script does not read `use_class`, so a Yahoo price that is not allowed to feed an active account would still make that security read `covered` and drop off the Bloomberg need. The CTO's condition C3 asks for this read. You add it, the way the script already reads `porting_verdict`.

**Read first (under the repository root):**
1. `data/assets/scripts/silver/commonwealth_price_need.py` whole (345 lines): the docstring; the section "the porting verdict" (`PORTING_COL`, `porting_verdicts`, `load_porting`, `porting_of`, the four branches NO_COLUMN / VERDICTS / MALFORMED / UNREADABLE and why a failed read fails closed); `index_rows`; `need_rows` (where `covered` is computed); `COLUMNS`; `run` (where the index is read and `PORTING-VERDICT-INDEX` is printed).
2. `data/assets/scripts/silver/tests/test_commonwealth_price_need.py` (11 tests; copy its stub style; its last test checks the CSV header carries `porting_verdict` beside `demque_claim`).
3. The active set: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ACTIVE_COTTONWOOD_SET_V2.csv` (sha256 `5cef7ab0c9e10fe299cb757d4dba31792d069bad35f7250defa76e18773046ae`; columns `account_key,source_side,cusip,ticker,held_from,held_to,window_basis`; it carries raw account numbers: this script reads the `cusip` column ONLY and returns no account key) and `data/mdpf/scripts/demque/active_set.py` (how that file is read and its sha256 enforced; READ it for the pattern; do not import it and do not edit it).
4. The pair that fixes the vocabulary: `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/NEVER_WIDEN_R9_INACTIVE_YAHOO_CTO_HALF.md` (values `NOT_FOR_ACTIVE`, `INACTIVE_USE`; condition C3).

**Your items.**

1. **Read `use_class` the way `porting_verdict` is read.** New constants `USE_COL = "use_class"`, `USE_VALUES = ("NOT_FOR_ACTIVE", "INACTIVE_USE")`; a function `use_classes(index) -> ({cusip: class}, branch, why)` with the same four branches (NO_COLUMN: no such column; MALFORMED: no cusip column, or a value outside `USE_VALUES`, including a missing value; VERDICTS is named `CLASSES` here; UNREADABLE: the index did not read), and a `load_use_classes(loader)` that fails closed on any exception. `run` reads it from the same already-loaded index frame (no second S3 read) and prints one line `USE-CLASS-INDEX branch=<b> <why>` beside the `PORTING-VERDICT-INDEX` line.
2. **The active CUSIP set, read from the pinned file.** A function `active_cusips(path=None, expected_sha256=ACTIVE_SET_SHA256)` returning the set of distinct non-blank `cusip` values of the V2 file; the sha256 of the file's bytes must equal `ACTIVE_SET_SHA256 = "5cef7ab0c9e10fe299cb757d4dba31792d069bad35f7250defa76e18773046ae"`, else a loud `SystemExit` naming both hashes and nothing else (no row, no account key). Reads the working-tree file; no S3. The file path is a constant relative to the repository root.
3. **The guard in `need_rows`.** New row fields `in_active_set` (the cusip is in the V2 cusip set) and `use_class` (the index's class for the cusip; `NOT_FOR_ACTIVE` when the branch is not CLASSES, i.e. the read failed closed; `NOT_APPLICABLE` when the cusip is not in the index). The `covered` rule becomes: the index holds the whole held span (as today) AND NOT (`in_active_set` AND `use_class` is `NOT_FOR_ACTIVE`). A security outside the active set keeps today's rule exactly. A security in the active set with a `NOT_FOR_ACTIVE` price stays UNcovered (it still needs Bloomberg). The two new fields join `COLUMNS` immediately after `porting_verdict` (the CSV header changes only by appending those two names there). `need_rows` takes the new inputs as optional arguments with defaults that reproduce today's behaviour exactly when they are absent, so every existing test passes unchanged.
4. **Tests** (extend `test_commonwealth_price_need.py`; do NOT edit or weaken an existing test): five NEW tests whose names all contain `use_class`: `test_use_class_no_column_reads_not_for_active_in_the_active_set`, `test_use_class_not_for_active_price_does_not_cover_an_active_security`, `test_use_class_inactive_use_price_covers_as_before`, `test_use_class_outside_the_active_set_is_unchanged_by_the_class`, `test_use_class_active_set_file_with_a_wrong_hash_refuses_without_naming_a_row`. Stub frames, made-up CUSIPs (`T00000001`...), a temp V2-shaped file for the hash test; no real account number.
5. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~172/USE_CLASS_READ_RECORD.json` with exactly these top-level keys: `module_path`, `module_blob` (the output of `git rev-parse HEAD:data/assets/scripts/silver/commonwealth_price_need.py` after your last commit), `active_set_sha256`, `active_cusips` (the count read from the real file in your worktree), `branches` (the four branch names), `new_tests` (the five names), `existing_tests_unchanged` (true only if `git diff` of the test file shows added lines only), `columns_added` (the two names), `not_established` (include: what the real index carries today, which you did NOT read unless the read-only listing below ran); and a short `.md`.
6. **One read-only look at the real index** (S3 `get-object` of the index parquet at the address the module's `index_uri()` builds, the schema only): state in the record whether `use_class` is a column there today. Either answer is fine; the NO_COLUMN branch is the tested state until the column lands.

### ACCEPTANCE

<criterion id="CB87ci1-AC1" cell_refs="CB-ci-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_commonwealth_price_need.py -q -k use_class</invocation><expect>5 passed</expect></criterion>
`CB87ci1-AC1` -- the five `use_class` tests pass.

<criterion id="CB87ci1-AC2" cell_refs="CB-ci-1"><invocation>python -c "import subprocess,sys;r=subprocess.run([sys.executable,'-m','pytest','data/assets/scripts/silver/tests/test_commonwealth_price_need.py','-q'],capture_output=True,text=True);print('PRICE-NEED-TESTS rc=%d last=%s'%(r.returncode,r.stdout.strip().splitlines()[-1]))"</invocation><expect>PRICE-NEED-TESTS rc=0</expect></criterion>
`CB87ci1-AC2` -- the whole test file, the 11 existing tests and the 5 new ones, passes with the existing tests unchanged.

<criterion id="CB87ci1-AC3" cell_refs="CB-ci-1"><invocation>python -c "import json,subprocess;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~172/USE_CLASS_READ_RECORD.json',encoding='utf-8'));b=subprocess.check_output(['git','rev-parse','HEAD:'+d['module_path']]).decode().strip();print('USE-CLASS-RECORD blob_equal=%s active_cusips=%d tests_unchanged=%s'%(b==d['module_blob'],d['active_cusips'],d['existing_tests_unchanged']))"</invocation><expect>blob_equal=True</expect></criterion>
`CB87ci1-AC3` -- the record names the module at HEAD, its blob equals what is committed, and it reports the active CUSIP count read from the pinned file and the tests-unchanged flag.

<expected_criteria>CB87ci1-AC1,CB87ci1-AC2,CB87ci1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. You edit `commonwealth_price_need.py` (additions only; the existing behaviour is unchanged when the new inputs are absent) and `test_commonwealth_price_need.py` (added tests only). You edit nothing else; you do not touch `data/mdpf/`, the V2 file, `active_set.py`, or the scan test.
- **AWS: READ-ONLY, through the `.tools/aws` shim,** of the one index parquet (schema only) in item 6. No write, delete or serve; no other key; no Bloomberg or Yahoo call. Do not run `aws sts get-caller-identity`.
- **Account numbers never appear in any output.** The V2 file is read for its `cusip` column only; nothing prints, logs or stores an account key; a refusal names the two hashes and nothing else.
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`. On this box it may fail closed because the pinned account set is on another machine: then report the exact error and do NOT look for the set; the issuer runs a count-only substitute at the drain.
- **NEVER** `--apply`, an S3 write or delete, a re-run against a real data dir that writes into the repository. No push. No gate override and no `--force`. Do not weaken, delete, xfail or skip any test. Scratch under the worktree `.scratch/`, never committed.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W172-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
data/assets/scripts/silver/commonwealth_price_need.py
data/assets/scripts/silver/tests/test_commonwealth_price_need.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round87.md</decomp_doc> (round 87), cell `CB-ci-1`.
<owned_cells>CB-ci-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB87ci1-AC1, CB87ci1-AC2, CB87ci1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~172/ADVI_COTBKF.TO-CB-ci-1.price-need-reads-use-class.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB87ci1-AC1,CB87ci1-AC2,CB87ci1-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the three criterion lines. Then: whether `use_class` is a column in the real index today (item 6); the active CUSIP count read from the pinned file; the diff size of the module and of the test file (added lines, removed lines: removed must be 0 in the test file); every S3 read with its denominator; the account-id scan result or exact error; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change to a read-only ranking script and its tests; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE one read-only schema read of a parquet under the existing role; no new permission.
comp-adversary: RUN -- the guard rests on a column that does not exist yet, so the NO_COLUMN branch fails CLOSED (every active-set security reads NOT_FOR_ACTIVE and stays uncovered), the opposite of a silent pass; BLIND: this script is one reader of several (CB-ci-2 reads the others), and a security held by both an active and an inactive account is in the active set and takes the stricter rule by design.
lane: the <paths> block IS the grant (worker RULING 1). Existing behaviour is unchanged when the new optional inputs are absent.
</preflight>

Source: `1.0.0_SA_CTO~DELL1` msg 6119 and the never-widen CTO half, condition C3 (`MDPF_DEMQUE/ledger/NEVER_WIDEN_R9_INACTIVE_YAHOO_CTO_HALF.md`).
