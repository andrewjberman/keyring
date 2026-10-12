# TO IRPT_ANLREQ.TO-AR-y-162 -- the upload reader re-landed on CONTRACT C-STOREDINPUT, with the reviewer's two repairs and the version-pin test

<to_id>IRPT_ANLREQ.TO-AR-y-162</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the floor of an `infra/` path). BUILD ONLY: nothing is built into a package, uploaded, applied or invoked.
**Decomp cell:** `AR-y-162` (`decompositions/IRPT_ANLREQ_DECOMP_R16_Y.md`) | **outcome_ref:** FWD-1 (hop 2); TCKT_VNEXT FWD-3; PRD v0.4 CONTRACT C-STOREDINPUT | **depends_on:** `AR-y-161`, the count run, and the CTO's ruling on it

**NOT SPAWNED AT ISSUANCE.** The issuer spawns this order when the count of cell `AR-y-161` has been run and the CTO has ruled on
it, and states that ruling in a spawn amendment. If there is no spawn amendment, STOP: the order was spawned too early.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W52-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`.

### THE CELL (`AR-y-162`, inlined) -- BUILD. Nothing is released by this order.

*The upload reader's findings, words and first answer are re-landed ON CONTRACT C-STOREDINPUT.*

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, CONTRACT C-STOREDINPUT (five numbered points) and this order's SPAWN AMENDMENT (if there is none, STOP:
the order was spawned too early). The earlier build is in history and is your starting material, NOT to be re-typed: commits
`d95cf11106` (the reader), `4215d98f26` (words; the POST's first answer) and `5cb5ba4dbf` (one test). It was reverted at
`114c77fb01` because `read_input` refused stored inputs the new reader read differently.

1. **Bring the earlier build back** onto your branch (cherry-pick the three commits' product and test changes, or re-apply their
   diffs to the seven files: `git show <c> -- <path>`); do not bring back their records, rows or proofs. Say how you did it.
2. **C-STOREDINPUT, exactly as the contract's point 3:**
   - a constant `READER_VERSION` in `template_reader.py`, changed in the same commit as any change to what the reader returns;
   - the template stored at acceptance records it in ONE new member (name it once; say the name);
   - `read_input`: when the stored version EQUALS the running reader's, the re-read must equal the stored template, as today;
     when it is DIFFERENT OR ABSENT the re-read is NOT compared, and every other binding `read_input` checks stays exactly as it
     is (the original's bytes against the stored digest, the frozen document against its own, the artifact references, the owner
     and the source). A stored input with no version member reads as the version before this contract.
   - The reader's new findings apply at the upload door only. They never refuse an input already accepted.
3. **The reviewer's two repairs (row `IRPT_ANLREQ-D2-S64`):**
   - the ACCOUNT-HEADER list: it missed `account #` while holding `acct #`, and its subtraction ran over fixtures that hold no
     account column. Rebuild it on the LEADING WORD: a header cell whose first word, case-folded and stripped of trailing
     punctuation, is `account`, `acct` or `custodian` followed by `account`, IS an account header -- EXCEPT the named exclusions,
     kept as a closed list with a reason each: `account type`, `account name` (and any other you can justify from a header in
     real use; say where you saw it). Add fixtures-in-memory that HOLD account columns in several header forms so the list is
     checked against a population that has the thing. Write the Rule 24 record again
     (`deliverables/0.9.0_WK_IRPT_ANLREQ~52/r16/CLOSED_LISTS_RULE24.json`): members or rule, domain, denominator, the uncovered
     member hunted by subtraction over that population, the exclusions.
   - the REPEATED-HEADER words: they told a person to split the file. They must say WHAT IS SEEN and ASK, never tell: for example
     "Row N repeats the header row. If the rows below it are a second account, upload them as their own file; if they are the
     same account, remove the repeated header." Your wording, that rule.
4. **The version-pin test (the reviewer's addition, CTO msg 6304):** a test that computes the reader's output on a fixed set of
   fixtures (the folder's fixture files and your in-memory sheets), digests it, and compares the digest with a value stored
   BESIDE the version constant, keyed by `READER_VERSION`. A change to what the reader returns with no version bump FAILS the
   suite. Say in the test's docstring how to move the pin legitimately (bump the version AND the digest in one commit).
5. **Tests.** `infra/aws/lambda/investor-reporting/intake/tests/test_stored_input_contract.py` (new) with functions named exactly:
   `test_an_input_stored_by_the_base_reader_is_read_unchanged_by_the_new_reader`,
   `test_an_input_stored_by_the_new_reader_with_an_altered_template_is_refused`,
   `test_an_original_with_altered_bytes_is_refused_under_both_versions`,
   `test_a_stored_input_with_no_version_member_reads_as_the_version_before`,
   `test_the_readers_output_on_the_fixtures_is_pinned_to_its_version`.
   The first builds its stored input with the BASE reader (load `git show 35c3c4bd45:<path>` from a temp file, as a module under
   another name) for a two-sheet workbook, a `Total`-row sheet and a two-value account sheet, and reads each with the new code:
   each returns its document unchanged. And `infra/aws/lambda/investor-reporting/intake/tests/test_template_account_totals.py` with functions named exactly:
   `test_account_column_with_two_values_is_turned_back_with_words`, `test_account_number_sign_header_is_an_account_column`,
   `test_account_column_with_one_value_is_accepted`, `test_repeated_header_row_says_what_is_seen_and_asks`,
   `test_total_row_is_turned_back_with_its_row_number`, `test_same_ticker_on_two_rows_is_not_several_accounts`,
   `test_known_good_sheet_is_accepted`. Keep the earlier build's other tests (`test_correction_words.py`'s three,
   `test_deferred_resolution.py`'s two) passing.
6. In your report: the member's name; how equal, different and absent versions are each handled, with lines; the rebuilt list and
   its record; the new words; the pin's digest and how it is moved; every existing test whose expectation changed; whether the
   resident and the Lambda may now run different reader versions safely, and what a person sees in that state.

### ACCEPTANCE

<criterion id="AR162-y-AC1" cell_refs="AR-y-162"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r16/ar16_checks.py y162-reland --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y162-RELAND-OK</expect></criterion>
`AR162-y-AC1`: the five contract tests and the seven reader tests are present by name and pass, and the reader declares
`READER_VERSION`.

<criterion id="AR162-y-AC2" cell_refs="AR-y-162"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r16/ar16_checks.py y162-keep --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y162-KEEP-OK</expect></criterion>
`AR162-y-AC2`: the difference control -- the whole intake test folder passes (292 at the base).

<criterion id="AR162-y-AC3J" cell_refs="AR-y-162" judgment="true"/>
`AR162-y-AC3J` (judgment, graded at L9, never by you): the account-header rule and its exclusions are right against a population
that holds account columns, and each finding's words say what is seen and what to do without telling a person to do the wrong thing.

<expected_criteria>AR162-y-AC1 AR162-y-AC2 AR162-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's
  file (status flip only).
- READ only: everything else. No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

<paths>
infra/aws/lambda/investor-reporting/intake/template_reader.py
infra/aws/lambda/investor-reporting/intake/uploads.py
infra/aws/lambda/investor-reporting/ops/status.py
infra/aws/lambda/investor-reporting/intake/tests/test_stored_input_contract.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_account_totals.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_reader.py
infra/aws/lambda/investor-reporting/intake/tests/test_correction_words.py
infra/aws/lambda/investor-reporting/intake/tests/test_deferred_resolution.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_uploads.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R16_Y.md</decomp_doc>
<owned_cells>AR-y-162</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR162-y-AC1 AR162-y-AC2 AR162-y-AC3J. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-162.reader-reland-on-stored-input-contract.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-162`. `AR162-y-AC3J` is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR162-y-AC1,AR162-y-AC2,AR162-y-AC3J`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 census of the earlier build (2 functions package these files, both held back by map pins; 21 consumers, 1 of which, read_input, refused the new reader's result; the resident package is built from one backend pin over whole folders) and 1 revert (7 files, 114c77fb01); NOT seen: the re-landed code (it does not exist yet). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called by this cell. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers of what this cell writes. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change; nothing is applied.
comp-adversary: RUN -- by reading 1 contract of 5 points and 1 grade (row D2-S64) against the face; the lens: a reader change with no version bump reaching production, or a different-version input being compared anyway. The face orders a digest pin keyed by the version and a test for each of equal, different and absent. NOT seen: the count of stored inputs this changes (cell AR-y-161's run; the CTO rules on it before this order is spawned).
lane: the reader, the upload service, a words table, six test files, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on PRD v0.4 @4b1447e2cc ROUND-16 item 2, CONTRACT C-STOREDINPUT, row `IRPT_ANLREQ-D2-S64` and CTO msg 6304.
  `AR162-y-AC1` base: FAIL as expected (no contract test file, no reader test file, no `READER_VERSION`). `AR162-y-AC2` base: PASS
  as expected (292 passed).
- NOT SPAWNED AT ISSUANCE: spawned when the count has been run, is with the CTO, and the CTO has ruled what is done about the
  inputs the new reader would turn back; a spawn amendment states that ruling.
- BUILT, NOT RELEASED. Its merge to the trunk is safe only because of the contract; the release is its own pair. Row
  `IRPT_ANLREQ-D2-W53-S9` stands: no rebuild of `irpt-ycharts-generate` until its four unpinned members are pinned or released.
