# TO ADVI_COTBKF.TO-CB-cp-1.crm-job-grant-path-argument -- round 94 CB-cp-1: the CRM job takes the path of its grant record as a validated argument; the key still comes only from that record

<to_id>ADVI_COTBKF.TO-CB-cp-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~184</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>94</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cp-1` (`decompositions/ADVI_COTBKF_DECOMP.round94.md`) |
**outcome_ref:** FWD-8, FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Round 93 made `data/assets/scripts/silver/cotbkf_crm_match_job.py` read its one key and its session name from the grant record. The record's PATH is still the constant `GRANT_REL` (round 88's record under `deliverables/0.7.0_AE_CloudOps~CB1/`), read by `_load_grant()`; your predecessor filed it as row `ADVI_COTBKF-D1-W183-S1`. A second one-job window will have a NEW grant record at a new path (the first is committed history). Without this cell the window's job order would start with a code change under a time limit. **You make the path an argument. The key must still come ONLY from the record.** No AWS call, no CRM data, no key from Andrew is needed.

**Read first (under the repository root):** `data/assets/scripts/silver/cotbkf_crm_match_job.py` whole (`GRANT_REL`, `_load_grant`, `grant_key`, `gate`, `run_job` and its `grant=None` default, `_run`, `main` and its three arguments, `_blank_record`); its tests `data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py` (19 tests; you add, you edit none); the surprise row text `ADVI_COTBKF-D1-W183-S1` in `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md`.

**Your items.**

1. **The argument.** `main` gains `--grant PATH` (optional). `_load_grant(path=None)` reads the path when given, else the module's default `GRANT_REL` (unchanged, so every existing caller and test behaves as before). The path is validated BEFORE it is opened, and a failure returns the stop path with a short code and no value in its text (the way the existing refusals do): it must be repo-relative (no drive letter, no leading `/` or `\`), contain no `..`, start with `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/`, end with `GRANT_RECORD.json`, resolve inside the repository root after `resolve()`, and name an existing regular file. Code names (use exactly): `GRANT_PATH_ABSOLUTE`, `GRANT_PATH_OUTSIDE_DELIVERABLES`, `GRANT_PATH_NAME`, `GRANT_PATH_MISSING`.
2. **The run record names the grant it used.** The record gains the key `grant_file` (the validated repo-relative path as given) and `grant_sha256` (the sha256 of that file's bytes), so a later reader can tell which signed record governed the run. The five keys the CRM-record-safety order fixed and the round-93 key keys stay as they are. `_write_record`'s member-text canary stays in force (a path or a digest is not member text).
3. **Nothing else moves.** The key and session name still come from `grant_key(grant)` and the grant's optional `session_name`; no argument names a key, a bucket or a role; `--role-arn` stays required; the gate's refusals (role ARN differs, resource count and form, bucket, prefix, `.zip`, wildcard, session pattern, deadline) are unchanged.
4. **Tests** (extend `test_cotbkf_crm_match_job.py`; edit none of the existing nineteen; stub grant records written under `tmp_path` and monkeypatched `_ROOT` so a stub path resolves "inside the repository"; no CRM value, no AWS): six named tests, all names starting `test_grant_path_`: `test_grant_path_default_is_the_round_88_record_when_no_argument_is_given`; `test_grant_path_argument_reads_that_file`; `test_grant_path_refuses_an_absolute_path_and_dotdot`; `test_grant_path_refuses_a_path_outside_the_deliverables_folder_or_not_named_grant_record`; `test_grant_path_refuses_a_missing_file`; `test_grant_path_the_run_record_names_the_grant_file_and_its_sha256`. The nineteen existing tests must pass unchanged.
5. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~184/GRANT_PATH_RECORD.json` with exactly these top-level keys: `module_path`, `module_blob` (`git rev-parse HEAD:<module_path>` after your last commit), `argument` (`"--grant"`), `refusal_codes` (the four), `record_keys_added` (`["grant_file", "grant_sha256"]`), `new_tests` (the six names), `existing_tests_unchanged` (true only if `git diff` of the test file shows added lines only), `cli_accepts_a_key` (false), `not_established`; and a short `.md`. No CRM value, account number or real key in either.

### ACCEPTANCE

<criterion id="CB94cp1-AC1" cell_refs="CB-cp-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py -q -k grant_path</invocation><expect>6 passed</expect></criterion>
`CB94cp1-AC1` -- the six grant-path tests pass.

<criterion id="CB94cp1-AC2" cell_refs="CB-cp-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py -q</invocation><expect>25 passed</expect></criterion>
`CB94cp1-AC2` -- the whole file, the nineteen existing tests unchanged and the six new ones, passes.

<criterion id="CB94cp1-AC3" cell_refs="CB-cp-1"><invocation>python -c "import json,subprocess;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~184/GRANT_PATH_RECORD.json',encoding='utf-8'));b=subprocess.check_output(['git','rev-parse','HEAD:'+d['module_path']]).decode().strip();print('CRM-GRANT-PATH blob_equal=%s tests_unchanged=%s cli_accepts_a_key=%s argument=%s refusals=%d'%(b==d['module_blob'],d['existing_tests_unchanged'],d['cli_accepts_a_key'],d['argument'],len(d['refusal_codes'])))"</invocation><expect>blob_equal=True tests_unchanged=True cli_accepts_a_key=False argument=--grant refusals=4</expect></criterion>
`CB94cp1-AC3` -- the record names the module at HEAD and its blob equals what is committed, no existing test was edited, the command line still takes no key, and the four refusals are named.

<expected_criteria>CB94cp1-AC1,CB94cp1-AC2,CB94cp1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. You edit `cotbkf_crm_match_job.py` and add tests to its test file; nothing else.
- **NO S3 call of any kind, no AWS call, no role, no CRM key, no network.** Stub grant records and a stub client only. Do not run the job against a real client.
- **No CRM value, account number or real key** in any file, fixture, log or report.
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; if it fails closed because the pinned set is absent on this box, report the exact error and do NOT look for the set.
- **NEVER** an S3 call, `--apply`, push, gate override or `--force`; do not weaken, delete, xfail or skip any test. Scratch under the worktree `.scratch/`, never committed. If a gate refuses a function name or a dtype call, rename or adapt without behaviour change; never override.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W184-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only.

<paths>
data/assets/scripts/silver/cotbkf_crm_match_job.py
data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round94.md</decomp_doc> (round 94), cell `CB-cp-1`.
<owned_cells>CB-cp-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB94cp1-AC1, CB94cp1-AC2, CB94cp1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~184/ADVI_COTBKF.TO-CB-cp-1.crm-job-grant-path-argument.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB94cp1-AC1,CB94cp1-AC2,CB94cp1-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the three criterion lines. Then: the four refusal codes; the diff size of the module and the test file (removed lines must be 0 in the test file); the account-id scan result or exact error; commits; every gate refusal and hook denial, verbatim. Nothing in the report quotes a real key.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change to a one-shot job proven on stubs; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call at all; no role, no permission.
comp-adversary: RUN -- the argument is a PATH to a signed record, never a key, so the one-way flow pair to grant record to job holds; the record names the file and its sha256 so a run is attributable to one signed record; BLIND: a hand-written GRANT_RECORD.json at a path under the deliverables folder passes the path check (the live role's own allow, set by the signed apply, is the real bound on what can be read; the gate's role-ARN match ties the record to that role), and a record edited after the apply would show as a changed sha256 against the committed file.
lane: the <paths> block IS the grant (worker RULING 1). No S3, no AWS, no CRM key is touched.
</preflight>

**ISSUER NOTES:** Source: row `D1-W183-S1`; Andrew call `bccc`; CTO msgs 6235 and 6248. The window itself is round 95, which issues when Andrew's exact key arrives.
