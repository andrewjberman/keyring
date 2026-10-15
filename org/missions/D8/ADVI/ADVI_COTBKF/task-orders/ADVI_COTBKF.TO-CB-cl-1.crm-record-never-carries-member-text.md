# TO ADVI_COTBKF.TO-CB-cl-1.crm-record-never-carries-member-text -- round 90 CB-cl-1: the CRM job's run record carries counts and declared role names, never a member's raw header text; a canary test proves a headerless member cannot reach the record

<to_id>ADVI_COTBKF.TO-CB-cl-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~179</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>90</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cl-1` (`decompositions/ADVI_COTBKF_DECOMP.round90.md`) |
**outcome_ref:** FWD-8, FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** The CVO's row `ADVI_COTBKF-D1-C-S3` (ARMED, BLOCKING): the CRM job `data/assets/scripts/silver/cotbkf_crm_match_job.py` records each CSV member's FIRST LINE verbatim (`header_columns[name] = list(header)` in `scan_zip`, then `rec["header_columns"] = scan["header_columns"]`, and `columns_used` carries `"%s:%s" % (name, col)` for each classified header cell) into the run record, which is COMMITTED. A member that has no header row, or a preamble line, would put a CRM data row (names, tax ids, birth dates) into git. The CRM zip is restricted data; no CRM value may leave the job in any committed file. The job has run once and read nothing (the record holds `header_columns: {}`), so nothing leaked; this cell closes the hazard BEFORE any re-run.

**Read first (under the repository root):** `data/assets/scripts/silver/cotbkf_crm_match_job.py` whole (`scan_zip`, `classify_columns`, `header_tokens`, `ROLES`, `_blank_record`, `_steps`, `_write_record`, `run_job`); its test file `data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py` (5 tests; you add, you edit none); the CVO's row text: `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/adjudications/ADJUDICATION_v62.md` row `ADVI_COTBKF-D1-C-S3` (its `notes` give the remedy); the order that made the job, `org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-cj-2.crm-match-job.md` (its rules block, "No value out").

**Your items.**

1. **No raw member text in the record.** Change the record, not the matching: for each CSV member the record carries (a) `columns` = the NUMBER of cells of its first line; (b) `roles` = the ROLE NAMES (from `ROLES`, a declared closed list inside the module) that `classify_columns` found, each with the COUNT of header cells of that role; (c) `first_line_is_header` = true only when EVERY cell of the first line classifies to a known header-token pattern or is an empty/short word that matches the declared header vocabulary (define the test in one small function, state it in its docstring, and be conservative: when in doubt it is false). `header_columns` becomes a dict `{member name: {"columns": n, "roles": {role: count}, "first_line_is_header": bool}}` and holds NO string drawn from the member's content. `columns_used` becomes a list of `"<member name>:<role>"` (role name, never header text). Member NAMES (file names inside the zip) may stay: they are the zip's own listing, not row content; but a member name is truncated to its basename of at most 80 characters and anything that is not `[A-Za-z0-9._ -]` is replaced by `?`.
2. **A headerless member is read as data, not as a header.** When `first_line_is_header` is false, the member's first line is treated as a DATA row (it joins the records the matcher reads) and the member is classified by position only if the job already had a declared schema for it; otherwise the member is skipped, counted under `skipped_members` with no text. Nothing about the first line's content reaches the record in either case.
3. **The record is checked against a content canary before it is written.** `_write_record` refuses to write when the record, serialised, contains any string of length 4 or more that was read from the zip's CSV rows or first lines (the module keeps an in-memory set of the first-line cells and the first 200 data cells of each member, hashed; it compares the record's string values against that set by hash and refuses on a hit with `RECORD_CARRIES_MEMBER_TEXT`, naming no text). The set is never written anywhere.
4. **Tests** (extend `test_cotbkf_crm_match_job.py`; edit none of the existing five; stub zips built with `zipfile` and `BytesIO`, made-up cell values such as `ZZ-CANARY-0001`): six named tests (all names start `test_record_safety_`, so `-k record_safety` selects exactly these six and none of the five existing): `test_record_safety_headerless_member_first_line_never_reaches_the_record` (a CSV whose first line is a data row carrying a canary string: the record's JSON text does not contain the canary and `first_line_is_header` is false); `test_record_safety_header_member_carries_counts_and_role_names_only` (a real header: the record holds `columns`, `roles` and no header text); `test_record_safety_columns_used_names_roles_not_header_text`; `test_record_safety_member_name_is_truncated_and_sanitised`; `test_record_safety_write_record_refuses_a_record_that_carries_member_text` (inject a member string into the record: `RECORD_CARRIES_MEMBER_TEXT`); `test_record_safety_headerless_member_first_line_is_read_as_data_or_skipped_never_recorded`. The five existing tests must still pass unchanged.
5. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~179/RECORD_SAFETY_RECORD.json` with exactly these top-level keys: `module_path`, `module_blob` (`git rev-parse HEAD:<module_path>` after your last commit), `record_keys_changed` (the names), `new_tests` (the six names), `existing_tests_unchanged` (true only if `git diff` shows added lines only on the test file), `canary_arm` (`{"headerless_member_in_record": false, "refusal_on_injected_text": true}` from the tests' own outcomes), `not_established`; and a short `.md`. No CRM value, name or account number in either.

### ACCEPTANCE

<criterion id="CB90cl1-AC1" cell_refs="CB-cl-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py -q -k record_safety</invocation><expect>6 passed</expect></criterion>
`CB90cl1-AC1` -- the six record-safety tests pass.

<criterion id="CB90cl1-AC2" cell_refs="CB-cl-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py -q</invocation><expect>11 passed</expect></criterion>
`CB90cl1-AC2` -- the whole file, the five existing tests unchanged and the six new ones, passes.

<criterion id="CB90cl1-AC3" cell_refs="CB-cl-1"><invocation>python -c "import json,subprocess;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~179/RECORD_SAFETY_RECORD.json',encoding='utf-8'));b=subprocess.check_output(['git','rev-parse','HEAD:'+d['module_path']]).decode().strip();print('CRM-RECORD-SAFETY blob_equal=%s tests_unchanged=%s headerless_in_record=%s refusal=%s'%(b==d['module_blob'],d['existing_tests_unchanged'],d['canary_arm']['headerless_member_in_record'],d['canary_arm']['refusal_on_injected_text']))"</invocation><expect>CRM-RECORD-SAFETY blob_equal=True tests_unchanged=True headerless_in_record=False refusal=True</expect></criterion>
`CB90cl1-AC3` -- the record names the module at HEAD and its blob equals what is committed, no existing test was edited, and the canary arm reads as the tests found it.

<expected_criteria>CB90cl1-AC1,CB90cl1-AC2,CB90cl1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. You edit `cotbkf_crm_match_job.py` and add tests to its test file; you edit nothing else.
- **NO S3 call of any kind, no AWS call, no role, no CRM key.** This is a code change proven on stubs. Do not run the job (`main`, `_run`, `run_job` with a real client). A stub client or a stub zip only.
- **No CRM value, name or account number** in any file, test fixture, log or report: fixtures use made-up strings only.
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; if it fails closed because the pinned set is absent on this box, report the exact error and do NOT look for the set.
- **NEVER** an S3 write or read, `--apply`, a push, a gate override or `--force`; do not weaken, delete, xfail or skip any test. Scratch under the worktree `.scratch/`, never committed. If a gate refuses a function name or a dtype call, rename or adapt without behaviour change; never override.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W179-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only.

<paths>
data/assets/scripts/silver/cotbkf_crm_match_job.py
data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round90.md</decomp_doc> (round 90), cell `CB-cl-1`.
<owned_cells>CB-cl-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB90cl1-AC1, CB90cl1-AC2, CB90cl1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~179/ADVI_COTBKF.TO-CB-cl-1.crm-record-never-carries-member-text.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB90cl1-AC1,CB90cl1-AC2,CB90cl1-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the three criterion lines. Then: the record's new shape (key names only); the `first_line_is_header` rule in one sentence; the diff size of the module and the test file (removed lines must be 0 in the test file); the account-id scan result or exact error; commits; every gate refusal and hook denial, verbatim. Nothing in the report quotes a fixture's content beyond its test name.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change to a one-shot job proven on stubs; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call at all; no role, no permission.
comp-adversary: RUN -- the criterion is a canary: a headerless stub member carrying a unique string is fed through the scan and the committed record's JSON must not contain it, with a second arm that injects member text into the record and requires the refusal; BLIND: the canary set holds hashes of the first 200 cells per member, so a leak of a cell beyond the 200th, or of a cell shorter than 4 characters, would not trip the refusal (the structural change, which carries no member text by construction, is the first control and the refusal is the backstop), and a real zip may hold a delimiter the stub does not.
lane: the <paths> block IS the grant (worker RULING 1). No S3, no AWS, no CRM key is touched.
</preflight>

**ISSUER NOTES:** Source: CVO row `ADVI_COTBKF-D1-C-S3` (ARMED, BLOCKING, disarm owner this seat) and the CTO's round-88 analysis item 1 (msg 6222): "Record a column count, or names checked against a declared schema; never raw line text. One criterion: the record holds no member text. This cell gates any CRM re-run, and the re-run itself waits on call bccc." The row is disarmed when this order's criteria PASS and the CVO has read it.
