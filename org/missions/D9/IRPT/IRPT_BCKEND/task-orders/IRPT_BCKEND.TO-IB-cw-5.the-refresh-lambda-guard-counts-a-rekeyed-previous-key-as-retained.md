# TO IRPT_BCKEND.TO-IB-cw-5 -- BUILD (no deploy): the refresh Lambda's own drop guard (`disappeared_entries`, `resolve_disappeared`, `compute_delta`) counts a previous client key as RETAINED when every account id of its entry is present in ONE current entry; a key with any account missing, split over two entries, or with no account ids still fails closed; every other path stays byte-equal (CTO ruling on row D2-S239, msg 10788, S239 yes, applied to the second surface the reader census found: readers R02, R03 and R15 of `IBcw3_findings.json`)

<to_id>IRPT_BCKEND.TO-IB-cw-5</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~461</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-cw-5` (decomposition section 254) | **outcome_ref:** FWD-7 (the directory is READY at all 3 firms) | **Ordered by:** the CTO's msg 10788 (S239: "A previous key counts as retained when every account_id of its entry is present in one current entry, and any missing account fails closed") applied to the Lambda side, found by the reader census (`deliverables/0.9.0_WK_IRPT_BCKEND~459/IBcw3_findings.json`, R02, R03, R15). **This order edits source and tests in your worktree. It deploys nothing: the release is a later order under its own never-widen pair.**

---

## WORKER FACE

**Cell `IB-cw-5` (inlined).** The runner's guard is being fixed by order `TO-IB-cw-4` (branch of worker ~460) so that a re-keyed account (an account-level client key moved to a relationship-level key, the account still in a current entry) is not a dropped client. The refresh Lambda re-checks the SAME thing on the runner's output, in `infra/aws/lambda/investor-reporting/directory/refresh.py`, with the same key-level comparison, so the runner fix alone would leave the Cottonwood build failed. The three places (HEAD):
- `disappeared_entries(previous_entries, current_entries)` (about line 424): the previous entries whose key (`_entry_key`: `ids.client_id`, else `ids.relationship_id`) the current build lacks. `resolve_disappeared` (about 481) starts from it and HOLDS every one still in the source snapshot (`source_client_ids`).
- `compute_delta(previous_entries, current_entries)` (about 504): `disappeared = sorted(set(prev) - set(cur))`, the count `refresh_firm` fails the build on (step 3, about line 1175).
- `refresh_firm` (about 1125 to 1175) calls them in that order and never touches the keys itself.

**The contract (the CTO's rule, not yours to change):**
1. **Add a pure helper `rekeyed_keys(previous_entries, current_entries) -> list[str]`** in `refresh.py`, placed just above `disappeared_entries`. For each previous key that is NOT among the current entries' keys: let `A` be the union of `str(a)` over `ids.account_ids` of ALL that key's previous entries. The key is **retained** iff **every** previous entry of that key names at least one account id (so `A` is non-empty and no previous entry of the key is account-less) AND `A` is a subset of the `ids.account_ids` of ONE single current entry. Return the retained keys, sorted, unique. (This is the same rule `TO-IB-cw-4` builds in the runner; the Lambda cannot import the runner, so the helper is repeated here on purpose.)
2. **`disappeared_entries` leaves a retained key out**, so `resolve_disappeared` neither holds nor carries it, whatever the source (including a `None` source).
3. **`compute_delta`'s `disappeared` count leaves a retained key out** (its `prev` and `cur` maps and every other count stay as they are). **The delta gains NO new key.**
4. **Fails closed.** A key with any account in NO current entry, a key whose accounts are SPLIT over two or more current entries, and a key with an account-less previous entry are NOT retained: they disappear, are held (or carried TERMINATED if absent from the source) exactly as today.
5. **Every other path is byte-equal to today** (an unchanged build; a gone key absent from the source; a gone key still in the source with no account present; an unknown source). Do not change `refresh_firm`, `last_manifest`, the dispatcher or the failure handling that the earlier order `TO-IB-cw-2` added.
Keep the change minimal and local: reuse `_entry_key`; add the smallest code that meets 1 to 5; do not restructure; touch no other file than the new test file. No non-ASCII anywhere (CLAUDE.md).

**Eight new tests** in a NEW file `infra/aws/lambda/investor-reporting/directory/tests/test_refresh_retained_key.py` (names fixed; invented keys and account ids only such as `K1`, `a1`, `R1`; no AWS call; import `refresh` the way `tests/test_refresh_failed_command_redispatch.py` and `tests/test_refresh_manifest_dispatch_date.py` do; entries can be the minimal dict `{"ids": {"client_id": "K1", "account_ids": ["a1"]}}`):
- `test_a_rekeyed_previous_key_is_not_a_disappearance_in_the_delta`
- `test_a_rekeyed_previous_key_is_neither_held_nor_carried`
- `test_a_key_with_one_account_in_no_current_entry_still_disappears`
- `test_a_key_whose_accounts_are_split_over_two_current_entries_still_disappears`
- `test_a_previous_entry_with_no_account_ids_still_disappears`
- `test_a_key_absent_from_the_source_is_still_carried_terminated`
- `test_an_unknown_source_still_holds_every_unretained_disappeared_key`
- `test_rekeyed_keys_lists_exactly_the_retained_keys`

**Do, in this order:**
1. Read `refresh.py` lines 415 to 540 and 1120 to 1200, and the two test files named above for the style. Run `python -m pytest infra/aws/lambda/investor-reporting/directory/tests -q --color=no -p no:cacheprovider --continue-on-collection-errors` once and record passed, failed and error counts (the folder is red at base for reasons that are not yours; the failing and error sets must be identical after).
2. Implement and test. Run the three criteria below from the repository root under `timeout 300` (AC3 reads `HEAD~1..HEAD`: run it AFTER your one commit). Record AC1 and AC2 output verbatim in `deliverables/0.9.0_WK_IRPT_BCKEND~461/IBcw5_criteria_output.txt` BEFORE the commit; write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`; write `IBcw5_notes.md` (the change in a paragraph, the before and after test counts, the folder's failing set before and after).
3. **LINE ENDINGS (a measured trap).** `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md` uses LF in the repository. Append your rows with a tool that does not rewrite the file (open it in append mode and write LF-ended text; do not use an editor tool that rewrites the whole file). Before the commit run `git diff --numstat HEAD -- <that file>`: it must show only your appended lines and `0` deleted. A previous worker's commit rewrote all 42711 lines to CRLF; that commit cannot be merged.
4. **ONE commit** with explicit paths (`.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~461 <0.9.0_WK_IRPT_BCKEND~461@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool): `refresh.py`, the new test file, your deliverables folder and any surprise row. If safe-commit is slow it is waiting on other seats: wait, never run it twice at once, never amend. Do not push. Report once, under 150 words, with AC3's result.

**Criteria (run each under `timeout 300` from the repository root):**

<criterion id="IBCW5-AC1" cell_refs="IB-cw-5"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r261/p261_cells.py" . IBCW5-AC1</invocation><expect>IBCW5-AC1 PASS</expect></criterion>
<criterion id="IBCW5-AC2" cell_refs="IB-cw-5"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r261/p261_cells.py" . IBCW5-AC2</invocation><expect>IBCW5-AC2 PASS</expect></criterion>
<criterion id="IBCW5-AC3" cell_refs="IB-cw-5"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r261/p261_cells.py" . IBCW5-AC3</invocation><expect>IBCW5-AC3 PASS</expect></criterion>

<expected_criteria>IBCW5-AC1, IBCW5-AC2, IBCW5-AC3</expected_criteria>

What the checks grade: AC1 the eight named tests exist in the new file and all pass; AC2 a differential and scenarios, run by the check itself over fixtures, base (HEAD~1) against your new module: the unchanged paths give byte-identical results from `disappeared_entries`, `resolve_disappeared` and `compute_delta`, the re-key fixture no longer disappears and is neither held nor carried (also with an unknown source), the delta carries no new key, the split, account-less and mixed fixtures fail closed, `rekeyed_keys` lists exactly the retained keys, and `refresh.py` actually changed; AC3 that your ONE commit touches only `refresh.py`, the new test file and this order's paths, and both code files are in it. The no-regression read of the whole folder is the issuer's. Do not edit the checks.

## BOUNDS

- **Grant:** edit `infra/aws/lambda/investor-reporting/directory/refresh.py`; add `infra/aws/lambda/investor-reporting/directory/tests/test_refresh_retained_key.py`; write `deliverables/0.9.0_WK_IRPT_BCKEND~461/`; the surprise channel for rows. **NO AWS call; NO S3 read or write; NO change to any other source file, Terraform or registry; NO real client or account identifier (invent fakes); NO deploy; NO push.**
- **Refusal clause:** STOP and report, writing nothing further, if the contract cannot be met without changing a file outside the two, or if the 5 unchanged paths cannot stay byte-equal. File a surprise ROW for anything odd and keep working; a broker message is never the carrier.

<paths>
infra/aws/lambda/investor-reporting/directory/refresh.py
infra/aws/lambda/investor-reporting/directory/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~461/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-cw-5.the-refresh-lambda-guard-counts-a-rekeyed-previous-key-as-retained.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 254 (round 17, workstream ~PM), cell `IB-cw-5`.
<owned_cells>IB-cw-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBCW5-AC1, IBCW5-AC2, IBCW5-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~461/IRPT_BCKEND.TO-IB-cw-5.the-refresh-lambda-guard-counts-a-rekeyed-previous-key-as-retained.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a Lambda source and test edit in a worktree; nothing is deployed and no AWS call is made. The release is a separate order under a never-widen pair (CTO msg 10788): one Lambda function (`irpt-directory-refresh`), a new zip version through Terraform, outside the 11:30Z to 14:15Z band, together with the runner bundle carrying `TO-IB-cw-4` and the `TO-IB-cw-2` wedge fix, with every reader of the client key listed (`IBcw3_findings.json`).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p261_cells.py IBCW5 dry-run at base on dell2 2026-10-19: AC1, AC2, AC3 FAIL (no tests; the refresh is unchanged so the differential refuses). Positive control (control261.py) over synthetic git repos each with the REAL base refresh.py and expiry.py and ONE worker commit: the three positives PASS (the issuer's REFERENCE implementation, a string patch of the real file, with eight passing named tests, so the check is satisfiable); each negative (a named test missing, a named test failing, no test file, refresh.py unchanged, a rule that retains when ANY account is present, a rule that lets accounts split over entries, a rule that retains an account-less entry, compute_delta not patched, disappeared_entries not patched, an unchanged path altered so nothing is held, a new key in the delta, no `rekeyed_keys` helper, a file outside the paths, refresh.py or the tests not in the commit) plus the empty repo fails its own arm, 0 unexpected. NOT measured by me: your implementation, the live behaviour on a real manifest history (the release order reads it), anything deployed.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~461`. Class WORLD (the gate's floor for an `infra/aws/lambda` path; once released the code changes what the served Cottonwood directory contains; this order edits source and tests in a worktree and deploys nothing).
</preflight>
