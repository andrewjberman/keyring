# TO IRPT_BCKEND.TO-IB-hm-2 -- BUILD the per-firm HMAC list stage of the directory runner (CTO ruling msg 10203): a LAST stage in `run_firm`, after `land()`, that writes HMAC-SHA256(key, UPPER(raw account key)) and the minted hex to ONE key per firm; its failure cannot touch the directory

<to_id>IRPT_BCKEND.TO-IB-hm-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~449</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-hm-2` (decomposition section 243) | **outcome_ref:** FWD-21 | **Ordered by:** the CTO's rulings: msg 10161 (conditions: a last stage whose failure cannot alter or roll back the directory output, shown by a planted-failure test; the object holds only HMACs, no firm, no count by firm, no id; one builder-named secret; a never-widen pair) and msg 10203 (the raw keys are in process at the mint, so the step goes in `directory_runner.py` per firm in `run_firm`: HMAC(key, UPPER(raw)) plus the minted hex, ONE key per firm; no combined key, no hand-off, no new reader). The facts are the cited lines of `deliverables/0.9.0_WK_IRPT_BCKEND~447/IBhm1_facts.json` (the READ cell IB-hm-1, graded by the issuer).

---

## WORKER FACE

**Cell `IB-hm-2` (inlined).** `data/assets/scripts/gold/investor_reporting/directory_runner.py` builds one firm's directory. `run_firm` (from line 1091) builds the entries, then calls `land(bucket, prefix, business_date, payload, upload, local_out)` at line 1185 and returns a dict containing `landed`. In the entry builder (from line 484) every account's RAW key is in process just before it is minted: `opaque_id("account", firm_id, a.get("raw_key") or a["account_number"])` (`raw_key` is `accounts_v2.account_id` for Inflection, `fact_allocations.AccountID` for Cottonwood, the account number for 49 Financial). The repository's `.tools/git-hooks/client-data-check.py` (lines 11 to 12, 28, 66 to 68) hashes each staged token with `tok.upper()`; the list it will read must be keyed so that those tokens match. **Your build adds one LAST stage to `run_firm`** that, per firm, writes the keyed list of those raw keys and of the minted hex to one S3 key. You change ONE source file and add ONE test file.

**What the stage does (exactly):**
1. **The inputs, already in process.** Collect the raw key of every account row the entry builder mints from, per firm, without a new read and without putting any raw key into an entry, the payload, a log line or a manifest (a module-level collector that `run_firm` resets at its start is acceptable if it never leaves the process; or a return value threaded out; your choice, stated in the module docstring). Also take the minted account ids (the `acc_` + 24 hex strings in `ids.account_ids`).
2. **The hashes.** For each distinct raw key `r` (stripped of surrounding whitespace, empty skipped): the token `UPPER(r)` (the hook's own `tok.upper()` after its own tokenisation: a raw key is hashed as the hook would see it as one token), and, when it differs, the hyphen-stripped upper form. For each minted id: `UPPER(hex)` where `hex` is the 24-hex part after the `acc_` prefix (the hook's token regex splits at `_`, so the hex part is the token a staged `acc_<hex>` yields). Each form is hashed as `HMAC-SHA256(key_bytes, form_utf8)` and written as lowercase hex. The `key_bytes` are the UTF-8 bytes of the `SecretString` of ONE Secrets Manager secret read with `boto3` (`get_secret_value`), cached for the process. **The secret id and the destination are ARGUMENTS, never typed:** `--hmac-secret-id <id>` and `--hmac-list-uri s3://bucket/key` on the runner's argument parser (they will be passed by the dispatch in a later cell). Record the exact convention (key bytes, token forms, ordering) in the stage's docstring: the hook's author reads it.
3. **The object.** Lines of lowercase hex only, one HMAC per line, **sorted, unique, LF-terminated, ASCII**, nothing else: no header, no firm, no count, no id, no timestamp. Written with a single `put_object` to the `--hmac-list-uri` key, only when `upload` is on and both arguments are given. **If the list is empty, nothing is written** (and the stage reports `skipped_empty`).
4. **Isolation (CTO condition 1).** The stage runs AFTER `land()` has returned and everything is verified. Its whole body, the call included, sits inside a `try/except Exception` in `run_firm`; on an exception it prints ONE line `ERROR: hmac list stage failed: <ExceptionClassName>` (the class name only: an exception message can carry an id) and `run_firm` still returns the SAME result it would have returned (the `landed` dict is untouched; a new additive key `hmac_list` carries only `{"status": "written"|"skipped_no_args"|"skipped_empty"|"failed"}`). A failure of the stage must be unable to raise out of `run_firm`, to change `landed`, or to delete or overwrite any directory object.
5. **No leakage.** Nothing the stage prints contains a raw key, a minted id, an HMAC or a count. The only lines are `OK: hmac list written`, `INFO: hmac list skipped (no arguments)`, `INFO: hmac list skipped (empty)` and the `ERROR:` line above (ASCII only, repository rule).
6. **The function name** the check looks for is `emit_hmac_list` (a module-level function called from `run_firm`). It takes what it needs as parameters and the boto3 clients as injectable parameters so a test can stub them.

**The ten tests** (a new file `data/assets/scripts/gold/investor_reporting/tests/test_directory_hmac_list.py`; the names are fixed, stub boto3, no AWS call, no real id: use invented values like `ACCT-12345-X` and `acc_` + 24 hex you make up):
`test_known_raw_key_yields_the_reference_hmac` (the expected value computed in the test with `hmac`/`hashlib` directly), `test_minted_hex_is_hashed_uppercase_with_the_prefix_dropped`, `test_output_is_sorted_unique_lines_of_hex_only`, `test_output_holds_no_plain_sha256_of_any_known_id` (for each known id, `sha256(UPPER(id))` hex does not occur in the object), `test_same_input_is_byte_identical`, `test_empty_input_writes_nothing`, `test_a_planted_failure_in_the_stage_leaves_the_directory_result_untouched` (the stubbed secret read raises; `run_firm`'s returned `landed` equals the result of a run with the stage off, and no exception escapes), `test_stage_is_skipped_without_the_two_arguments`, `test_no_id_appears_in_any_printed_line` (capture stdout/stderr), `test_hyphen_stripped_variant_is_included_when_different`.

**Do, in this order:**
1. Read `directory_runner.py` lines 100 to 200, 440 to 530, 1046 to 1192 and `main` (from 1194), the hook `.tools/git-hooks/client-data-check.py` and an existing runner test for the stub style (for example `tests/test_directory_account_masks.py`). Run the existing directory tests once and record the count that pass at base.
2. Implement the stage and the arguments; write the ten tests; run `python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_directory_hmac_list.py -q` and then the whole `data/assets/scripts/gold/investor_reporting/tests` folder: no test that passed at base may fail.
3. Run the three criteria below from the repository root, record each output and exit code verbatim in `deliverables/0.9.0_WK_IRPT_BCKEND~449/IBhm2_criteria_output.txt`; write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`.
4. **ONE commit** with explicit paths (`.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~449 <0.9.0_WK_IRPT_BCKEND~449@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool): the runner, the test file, and your deliverables folder (the criteria output, the proof instance and a short `IBhm2_notes.md` with the convention in one paragraph and the base and after test counts). The check reads `HEAD~1..HEAD`, so everything goes in the one commit, including any surprise row you file and the order's `<status>` flip. Report once, under 150 words.

**Criteria (run each under `timeout 300` from the repository root):**

<criterion id="IBHM2-AC1" cell_refs="IB-hm-2"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r248/p248_cells.py" . IBHM2-AC1</invocation><expect>IBHM2-AC1 PASS</expect></criterion>
<criterion id="IBHM2-AC2" cell_refs="IB-hm-2"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r248/p248_cells.py" . IBHM2-AC2</invocation><expect>IBHM2-AC2 PASS</expect></criterion>
<criterion id="IBHM2-AC3" cell_refs="IB-hm-2"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r248/p248_cells.py" . IBHM2-AC3</invocation><expect>IBHM2-AC3 PASS</expect></criterion>

<expected_criteria>IBHM2-AC1, IBHM2-AC2, IBHM2-AC3</expected_criteria>

What the checks grade: AC1 the ten named tests exist and all pass (the check runs pytest itself); AC2 the stage is wired right by AST (`land()` before `emit_hmac_list`, the call inside a `try` whose handler catches `Exception`, `run_firm` still returns); AC3 your ONE commit touches only the runner, the new test file and this order's paths, and both code files are in it. The grading of the stage's convention and of the existing tests (no regression) is the issuer's, at the drain. Do not edit the checks.

## BOUNDS

- **Grant:** edit `data/assets/scripts/gold/investor_reporting/directory_runner.py`; create `data/assets/scripts/gold/investor_reporting/tests/test_directory_hmac_list.py`; write `deliverables/0.9.0_WK_IRPT_BCKEND~449/`; the surprise channel for rows. **NO AWS call of any kind (boto3 is stubbed in tests); NO real account id, name or value in any file; NO change to `refresh.py`, Terraform, the registry or any other file; NO push; NO real secret or key material.**
- **Refusal clause:** STOP and report, writing nothing further, if the raw key cannot be reached at the entry builder without a new read or a change outside the one file; or if making the stage's failure unable to alter `landed` needs a change to `land()`. File a surprise ROW (`spec_asserts` plus `world_is`) for anything odd and keep working; a broker message is never the carrier.

<paths>
data/assets/scripts/gold/investor_reporting/directory_runner.py
data/assets/scripts/gold/investor_reporting/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~449/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-hm-2.build-the-runner-hmac-list-stage.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 243 (round 7, workstream ~PM), cell `IB-hm-2`.
<owned_cells>IB-hm-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBHM2-AC1, IBHM2-AC2, IBHM2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~449/IRPT_BCKEND.TO-IB-hm-2.build-the-runner-hmac-list-stage.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a source and test edit in a worktree; nothing is deployed, no AWS call; the stage is inert until a later cell passes the two arguments and a later pair authorises the apply.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed by this order (the runner profile grants are the next cell).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p248_cells.py IBHM2 dry-run at base on dell2 2026-10-17 ~03:3xZ: AC1, AC2, AC3 FAIL. Positive control (control248.py) over synthetic git repos each with a base commit and ONE worker commit: the three positives PASS and each of 10 negatives (a test name missing, a named test failing, no test file, the stage before land(), the stage outside a try, a handler too narrow, run_firm not returning, the runner or the tests not in the commit, another file touched) fails its own arm (0 unexpected; the first run caught a pytest-output parsing defect of mine, fixed). NOT measured by me: the stage's correctness (the ten tests are the worker's and the issuer reads them at the drain), the hook's final convention (the laptop CTO's), anything live.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~449`. Class LOCAL.
</preflight>
