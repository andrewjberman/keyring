# TO ADVI_COTBKF.TO-CB-co-1.crm-job-key-from-the-grant-record -- round 93 CB-co-1: the CRM job reads its one key and its session name from the grant record and validates them; no code change is needed to run a second window

<to_id>ADVI_COTBKF.TO-CB-co-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~183</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>93</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-co-1` (`decompositions/ADVI_COTBKF_DECOMP.round93.md`) |
**outcome_ref:** FWD-8, FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Andrew, 2026-10-15, call `bccc`: the CRM zip WAS uploaded, so round 88's `head_object` 403 was a wrong key, a wrong place or a refusal. A second one-job window runs on the exact key Andrew reads from his console, under a NEW never-widen pair and a NEW grant record. Today `data/assets/scripts/silver/cotbkf_crm_match_job.py` fixes the key as a module constant (`KEY`, line 54) and its gate compares the grant record's `policy_resources` to that constant (about line 467); a different key would need a code change in the middle of a time-limited window. You remove that need: the job derives the key (and the session name) from the grant record, validates them, and keeps every other rule of the job unchanged. **You do not need Andrew's key, you read no CRM data, and you make no AWS call.**

**Read first (under the repository root):** `data/assets/scripts/silver/cotbkf_crm_match_job.py` whole (`GRANT_BUCKET`, `KEY`, `SESSION_NAME`, `GRANT_REL`, `_load_grant`, `gate`, `_blank_record`, `_steps`, `run_job`, `_run`, `main`, `MIN_MINUTES_LEFT`); its tests `data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py` (11 tests; you add, you edit none; they build a stub grant record and a stub client: study how); the grant record's SHAPE: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB1/GRANT_RECORD.json` (keys `role_arn`, `policy_actions`, `policy_resources` (a list holding exactly one `arn:aws:s3:::<bucket>/<key>`), `deadline_utc`; read, never edit) and the CloudOps check `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/round88/checks/crm_checks.py` (its `grant` limb fixes the grant record's shape and the restricted prefix and key literal; read only); the pair `org/missions/D8/ADVI/ADVI_COTBKF/ledger/NEVER_WIDEN_R88_CRM_MATCH_GRANT_COO_HALF.md` (section "What the act MAY touch").

**Your items.**

1. **Derive the key from the grant record.** Remove the module constant `KEY` as the source of truth. A function `grant_key(grant)` returns `(bucket, key)` parsed from the grant record's `policy_resources`, and RAISES `GrantKeyRefused` (a short code, no value in its text) unless ALL hold: the list has exactly one entry; the entry has the form `arn:aws:s3:::<bucket>/<key>`; the bucket equals `GRANT_BUCKET` (the module keeps this constant: the bucket is the firm bucket named in the signed pair and register exception X15; a different bucket is a different pair); the key starts with the restricted prefix (the same prefix the module builds from `opal_naming.key(cw.SOURCE, cw.SCOPE, "bronze", "crm", ...)` up to and including `.../bronze/crm/`, derived from the builder, never typed); the key ends with `.zip`; it contains no `*`, `?`, `[`, `]` and no `..`; and it is at most 512 characters. `gate` uses `grant_key(grant)` and keeps every existing refusal (role ARN differs, fewer than `MIN_MINUTES_LEFT` before the deadline); a malformed grant returns the refusal reason instead of raising out of `gate`.
2. **Derive the session name.** The grant record gains an OPTIONAL top-level key `session_name`; when present it must match `^cotbkf-crm-match-[0-9]{1,6}$` exactly, else `gate` refuses; when absent the module's existing `SESSION_NAME` constant is used (so the round-88 record still works). The session name used for `sts.assume_role` and written to the run record is the derived one.
3. **One key all the way down.** `_blank_record`, the `head_object` and `get_object` calls and the run record's `key` field use the derived `(bucket, key)`, never a module constant. `main` keeps its arguments; it gains none that names a key: the key comes ONLY from the grant record (a command-line key would let the job read an object the pair did not sign).
4. **Tests** (extend `test_cotbkf_crm_match_job.py`; edit none of the existing eleven; stub grant records and a stub client; made-up keys such as `commonwealth/<scope>/bronze/crm/date=2099-01-01/TEST_ZIP.zip` built from the module's own prefix function; no CRM value, no AWS): eight named tests, all names starting `test_grant_key_`:
   `test_grant_key_derives_bucket_and_key_from_the_single_resource`; `test_grant_key_refuses_two_resources`; `test_grant_key_refuses_a_wildcard_or_dotdot_or_a_non_zip`; `test_grant_key_refuses_a_key_outside_the_restricted_prefix`; `test_grant_key_refuses_a_different_bucket`; `test_grant_key_session_name_must_match_the_pattern_and_defaults_to_the_constant`; `test_grant_key_the_head_object_call_uses_the_derived_key` (a stub S3 client records the `Key` it was called with); `test_grant_key_the_run_record_carries_the_derived_key_and_session_name`. The eleven existing tests must pass unchanged.
5. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~183/KEY_FROM_GRANT_RECORD.json` with exactly these top-level keys: `module_path`, `module_blob` (`git rev-parse HEAD:<module_path>` after your last commit), `constant_removed` (true only if `grep` finds no module-level `KEY =` assignment left; use the native Grep tool), `refusals` (the list of refusal conditions you implemented, as short codes), `new_tests` (the eight names), `existing_tests_unchanged` (true only if `git diff` of the test file shows added lines only), `cli_accepts_a_key` (false), `not_established`; and a short `.md`. No CRM value, account number or real key in either.

### ACCEPTANCE

<criterion id="CB93co1-AC1" cell_refs="CB-co-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py -q -k grant_key</invocation><expect>8 passed</expect></criterion>
`CB93co1-AC1` -- the eight key-from-the-grant-record tests pass.

<criterion id="CB93co1-AC2" cell_refs="CB-co-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py -q</invocation><expect>19 passed</expect></criterion>
`CB93co1-AC2` -- the whole file, the eleven existing tests unchanged and the eight new ones, passes.

<criterion id="CB93co1-AC3" cell_refs="CB-co-1"><invocation>python -c "import json,subprocess;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~183/KEY_FROM_GRANT_RECORD.json',encoding='utf-8'));b=subprocess.check_output(['git','rev-parse','HEAD:'+d['module_path']]).decode().strip();print('CRM-KEY-FROM-GRANT blob_equal=%s constant_removed=%s tests_unchanged=%s cli_accepts_a_key=%s refusals=%d'%(b==d['module_blob'],d['constant_removed'],d['existing_tests_unchanged'],d['cli_accepts_a_key'],len(d['refusals'])))"</invocation><expect>blob_equal=True constant_removed=True tests_unchanged=True cli_accepts_a_key=False</expect></criterion>
`CB93co1-AC3` -- the record names the module at HEAD and its blob equals what is committed, the key constant is gone, no existing test was edited, and the command line takes no key.

<expected_criteria>CB93co1-AC1,CB93co1-AC2,CB93co1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. You edit `cotbkf_crm_match_job.py` and add tests to its test file; nothing else.
- **NO S3 call of any kind, no AWS call, no role, no CRM key, no network.** A stub grant record and a stub client only. Do not run the job (`main`, `_run`, `run_job` with a real client).
- **No CRM value, account number or real key** in any file, fixture, log or report: fixtures use made-up keys built from the module's own prefix function.
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; if it fails closed because the pinned set is absent on this box, report the exact error and do NOT look for the set.
- **NEVER** an S3 call, `--apply`, push, gate override or `--force`; do not weaken, delete, xfail or skip any test. Scratch under the worktree `.scratch/`, never committed. If a gate refuses a function name or a dtype call, rename or adapt without behaviour change; never override.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W183-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only.

<paths>
data/assets/scripts/silver/cotbkf_crm_match_job.py
data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round93.md</decomp_doc> (round 93), cell `CB-co-1`.
<owned_cells>CB-co-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB93co1-AC1, CB93co1-AC2, CB93co1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~183/ADVI_COTBKF.TO-CB-co-1.crm-job-key-from-the-grant-record.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB93co1-AC1,CB93co1-AC2,CB93co1-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the three criterion lines. Then: the refusal conditions implemented (short codes); whether any existing test needed the constant; the diff size of the module and the test file (removed lines must be 0 in the test file); the account-id scan result or exact error; commits; every gate refusal and hook denial, verbatim. Nothing in the report quotes a real key.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change to a one-shot job proven on stubs; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call at all; no role, no permission.
comp-adversary: RUN -- the criterion is that the key comes from ONE place, the signed grant record, and that a malformed or widened record is refused before any call; the test that the head_object call carries the derived key proves the plumbing; BLIND: the grant record is written by CloudOps from the signed pair, so the job trusts it exactly as far as the pair does (the record's own `policy_resources` is what the role can read, because the grant order's checker ties them; a record edited by hand after the apply would not match the live role, and the live role's allow is the real bound), and the prefix check cannot tell a right key from a wrong one inside the restricted prefix (that is the point of the second window).
lane: the <paths> block IS the grant (worker RULING 1). No S3, no AWS, no CRM key is touched.
</preflight>

**ISSUER NOTES:** Source: Andrew call `bccc` and the CTO's msgs 6235 and 6248. The second window itself is round 94: a NEW pair binding the key literal (COO half and CTO half), a grant order to a CloudOps seat, the job, the withdrawal as the job's next act, under the same limits as round 88 (in memory, link ids only, no personal data out, logged, removed at job end).
