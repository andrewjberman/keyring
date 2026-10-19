# TO IRPT_BCKEND.TO-IB-cw-4 -- BUILD (no deploy): the runner's drop guard counts a previous client key as RETAINED when every account id of its entry is present in ONE current entry; a key with any account missing, split over two entries, or with no account ids still fails closed; every other path stays byte-equal (CTO ruling on row D2-S239, msg 10788, S239 yes; ruling 481d; pause lifted msg 11047)

<to_id>IRPT_BCKEND.TO-IB-cw-4</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~460</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-cw-4` (decomposition section 253) | **outcome_ref:** FWD-7 (the directory is READY at all 3 firms) | **Ordered by:** the CTO's msg 10788 (S239: "A previous key counts as retained when every account_id of its entry is present in one current entry, and any missing account fails closed") and msg 11047. **This order edits source and tests in your worktree. It deploys nothing: the release is a later order under its own never-widen pair, whose CTO half is the CTO's.**

---

## WORKER FACE

**Cell `IB-cw-4` (inlined).** `carry_forward_removed(previous_entries, entries, source_ids, source_removed_on)` in `data/assets/scripts/gold/investor_reporting/directory_runner.py` (about line 993) returns `(carried, held)`. Today it compares CLIENT KEYS: a previous entry whose key (`entry_key(e)`, the `ids.client_id` else `ids.relationship_id`) is absent from this build's entries is "gone"; a gone key still in the source snapshot is HELD (a build fault: `run_firm` then refuses with `BUILD_DROPS_SOURCE_ENTRY`), and a gone key absent from the source is carried TERMINATED. Measured fact: 11 Cottonwood previous keys are accounts that moved from an account-level key to a relationship-level key; every one of those accounts is still in a current entry under the NEW key. The guard reads them as dropped clients and refuses the whole build. **The contract (the CTO's, not yours to change):**
1. **Add a pure helper `rekeyed_keys(previous_entries, entries) -> list[str]`** in the same module, placed just above `carry_forward_removed`. For each previous key that is NOT among the current entries' keys: let `A` be the union of `str(a)` over `ids.account_ids` of ALL that key's previous entries. The key is **retained** iff `A` is non-empty AND `A` is a subset of the `ids.account_ids` of ONE single current entry. Return the retained keys, sorted, unique.
2. **`carry_forward_removed` leaves a retained key alone:** it is neither held nor carried TERMINATED. Its signature and its 2-tuple return stay exactly as today. This applies BEFORE the source test, and also when `source_ids` is `None` (a re-keyed key whose accounts are all present is retained; every other gone key behaves exactly as today, including all gone keys being held when `source_ids` is `None`).
3. **Fails closed.** A key with any account in NO current entry is NOT retained; a key whose accounts are SPLIT over two or more current entries is NOT retained; a previous entry with no `account_ids` is NOT retained. Each of those is held (or carried TERMINATED if absent from the source) exactly as today.
4. **Record the count.** In `run_firm`, where `carry_info` is filled after `carry_forward_removed`, add `carry_info["rekeyed"] = len(rekeyed_keys(body.get("entries") or [], entries))`. Nothing else in `run_firm` changes.
5. **Every other path is byte-equal to today** (an unchanged build; a gone key absent from the source; a gone key still in the source with no account present; an unknown source).
Keep the change minimal and local: reuse `entry_key`; add the smallest code that meets 1 to 5; do not restructure, do not touch any other file than the new test file. No non-ASCII anywhere (CLAUDE.md).

**Eight new tests** in a NEW file `data/assets/scripts/gold/investor_reporting/tests/test_directory_runner_retained_key.py` (names fixed; invented keys and account ids only such as `K1`, `a1`, `R1`; no AWS call; import the runner the way `tests/test_directory_runner_terminated.py` does, `import directory_runner as dr` after putting the parent folder on `sys.path`; entries can be the minimal dict `{"ids": {"client_id": "K1", "account_ids": ["a1"]}}`):
- `test_a_key_whose_every_account_is_in_one_current_entry_is_retained`
- `test_a_retained_key_is_neither_held_nor_carried_terminated`
- `test_a_key_with_one_account_in_no_current_entry_is_held`
- `test_a_key_whose_accounts_are_split_over_two_current_entries_is_held`
- `test_a_previous_entry_with_no_account_ids_is_held`
- `test_a_key_absent_from_the_source_is_still_carried_terminated`
- `test_a_missing_source_still_holds_every_unretained_gone_key`
- `test_rekeyed_keys_lists_exactly_the_retained_keys`

**Do, in this order:**
1. Read `directory_runner.py` lines 900 to 1010 (`entry_key`, `_carried_terminated`, `carry_forward_removed`) and 1260 to 1300 (`run_firm`'s use of it), and `tests/test_directory_runner_terminated.py` and `tests/test_directory_runner_refuse_drop.py` for the style. Run `python -m pytest data/assets/scripts/gold/investor_reporting/tests -q --color=no -p no:cacheprovider --continue-on-collection-errors` once and record passed, failed and error counts (the folder may be red at base for reasons that are not yours; the failing and error sets must be identical after).
2. Implement and test. Run the three criteria below from the repository root under `timeout 300` (AC3 reads `HEAD~1..HEAD`: run it AFTER your one commit). Record AC1 and AC2 output verbatim in `deliverables/0.9.0_WK_IRPT_BCKEND~460/IBcw4_criteria_output.txt` BEFORE the commit; write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`; write `IBcw4_notes.md` (the change in a paragraph, the before and after test counts, the folder's failing set before and after).
3. **ONE commit** with explicit paths (`.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~460 <0.9.0_WK_IRPT_BCKEND~460@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool): `directory_runner.py`, the new test file, your deliverables folder and any surprise row. If safe-commit is slow it is waiting on other seats: wait, never run it twice at once, never amend. Do not push. Report once, under 150 words, with AC3's result.

**Criteria (run each under `timeout 300` from the repository root):**

<criterion id="IBCW4-AC1" cell_refs="IB-cw-4"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r260/p260_cells.py" . IBCW4-AC1</invocation><expect>IBCW4-AC1 PASS</expect></criterion>
<criterion id="IBCW4-AC2" cell_refs="IB-cw-4"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r260/p260_cells.py" . IBCW4-AC2</invocation><expect>IBCW4-AC2 PASS</expect></criterion>
<criterion id="IBCW4-AC3" cell_refs="IB-cw-4"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r260/p260_cells.py" . IBCW4-AC3</invocation><expect>IBCW4-AC3 PASS</expect></criterion>

<expected_criteria>IBCW4-AC1, IBCW4-AC2, IBCW4-AC3</expected_criteria>

What the checks grade: AC1 the eight named tests exist in the new file and all pass; AC2 a differential and scenarios, run by the check itself over fixtures, base (HEAD~1) against your new module: the unchanged paths give byte-identical results, the re-key fixture is retained (neither held nor carried) including with an unknown source, the split, account-less and mixed fixtures fail closed, `rekeyed_keys` lists exactly the retained keys, and `directory_runner.py` actually changed; AC3 that your ONE commit touches only `directory_runner.py`, the new test file and this order's paths, and both code files are in it. The no-regression read of the whole folder is the issuer's. Do not edit the checks.

## BOUNDS

- **Grant:** edit `data/assets/scripts/gold/investor_reporting/directory_runner.py`; add `data/assets/scripts/gold/investor_reporting/tests/test_directory_runner_retained_key.py`; write `deliverables/0.9.0_WK_IRPT_BCKEND~460/`; the surprise channel for rows. **NO AWS call; NO S3 read or write; NO change to any other source file, Terraform or registry; NO real client or account identifier (invent fakes); NO deploy; NO push; NO run of the runner against live data.**
- **Refusal clause:** STOP and report, writing nothing further, if the contract cannot be met without changing a file outside the two, or if the 5 unchanged paths cannot stay byte-equal. File a surprise ROW for anything odd and keep working; a broker message is never the carrier.

<paths>
data/assets/scripts/gold/investor_reporting/directory_runner.py
data/assets/scripts/gold/investor_reporting/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~460/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-cw-4.a-rekeyed-previous-client-key-is-retained-not-dropped.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 253 (round 16, workstream ~PM), cell `IB-cw-4`.
<owned_cells>IB-cw-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBCW4-AC1, IBCW4-AC2, IBCW4-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~460/IRPT_BCKEND.TO-IB-cw-4.a-rekeyed-previous-client-key-is-retained-not-dropped.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a gold-script source and test edit in a worktree; nothing is deployed and no AWS call is made. The release is a separate order under a never-widen pair (CTO msg 10788): a runner change that reaches the build host through the bundle the refresh Lambda's SSM command runs, outside the 11:30Z to 14:15Z band, with every reader of the client key listed (cell IB-cw-3).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p260_cells.py IBCW4 dry-run at base on dell2 2026-10-19: AC1, AC2, AC3 FAIL (no tests; the runner is unchanged so the differential refuses). Positive control (control260.py) over synthetic git repos each with the REAL base directory_runner.py and its import siblings and ONE worker commit: the three positives PASS (the issuer's REFERENCE implementation, a string patch of the real file, with eight passing named tests, so the check is satisfiable); each negative (a named test missing, a named test failing, no test file, the runner unchanged, a rule that retains when ANY account is present, a rule that lets accounts split over entries, a rule that retains an account-less entry, an unchanged path altered so nothing is ever held, no `rekeyed_keys` helper, a file outside the paths, the runner or the tests not in the commit) plus the empty repo fails its own arm, 0 unexpected. NOT measured by me: your implementation, that `run_firm` records `carry_info["rekeyed"]` (the issuer reads that line), anything run against live data or deployed.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~460`. Class WORLD (the code, once released, changes what the served Cottonwood directory contains; this order edits source and tests in a worktree and deploys nothing).
</preflight>
