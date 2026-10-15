# TO IRPT_BCKEND.TO-IB-pr-587 -- LIFT the one-account limit of orion_account_mapping.py: a household with several accounts is addressable account by account, a household-members helper is added, every other refusal stays

<to_id>IRPT_BCKEND.TO-IB-pr-587</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~430</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-118 ruling 1 and the feed addendum section 2 item 5 (the limit is lifted in the same release as the feed) | **Decomp cell:** `IB-pr-587` (decomposition section 218) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-430`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~430 <0.9.0_WK_IRPT_BCKEND~430@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add infra/aws/lambda/investor-reporting/performance/`, then add (locally, never committed) EXACTLY the further directories the import chain of the files you touch and their existing tests needs: run the existing test files named under READ FIRST and add the directory of each import error until they collect (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`).

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier; tests use synthetic ids and values.

**Python:** ASCII only in product code, tests and logs; ruff py39 and py_compile run at commit. No typed bucket name, `s3://` address or key prefix in a product file: reuse the constants and helpers the builders already use.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array.

**Cell `IB-pr-587` (inlined).** `infra/aws/lambda/investor-reporting/performance/orion_account_mapping.py` maps one canonical account id to one Orion account id and REFUSES any account whose household holds more than one account (lines 83 to 86: `members = int((frame["household_id"] == household).sum())`, then `if members != 1: raise InflectionMappingRefused(...)`). The CTO ruled (round 118, ruling 1, and the feed addendum `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/ORION_PAIR_B_ADDENDUM_1_SCOPE_ACCOUNT_FEED.md` section 2 item 5) that this limit is lifted in the same release as the Scope account feed, each account attributed to itself, no household figure built from it. This cell builds that, LOCAL, offline, with tests. The module's serve-path consumers are not changed here (`retained.py` says the Orion read for Inflection is retired); this lifts only the mapping.

**READ FIRST (named files only):** `infra/aws/lambda/investor-reporting/performance/orion_account_mapping.py` (whole), its test `infra/aws/lambda/investor-reporting/performance/tests/test_orion_account_mapping.py` (its `FakeS3` already takes a `households=` map; the test `test_an_account_sharing_its_orion_household_is_not_individually_addressable` near lines 67 to 74 asserts the refusal), `infra/aws/lambda/investor-reporting/performance/orion_selected.py` (`calculate`, near line 140: it requires exactly one selected account and one Account group; you do NOT change it, say in the notes that it still has that guard).

**Change** (all new logic inside `# BEGIN ORION-HOUSEHOLD-A` ... `# END ORION-HOUSEHOLD-A` lines; the module must import with the blocks removed): (1) the `members != 1` refusal is removed for an account whose household holds several accounts: the loader returns the account's own Orion account id and its household, as for a single-account household; (2) a new function `household_account_ids(...)` returning, for a household, the list of its accounts' canonical and Orion ids from the SAME newest `accounts_v2` snapshot at or before `as_of`; (3) every OTHER refusal stays: an unknown account, an unmapped household (no row) and a missing snapshot still raise `InflectionMappingRefused` exactly as today. The existing refusal test is FLIPPED in `infra/aws/lambda/investor-reporting/performance/tests/test_orion_account_mapping.py`: that ONE test now asserts the account is addressable, and every other existing assertion in the file stays unchanged.

**Write the tests** `infra/aws/lambda/investor-reporting/performance/tests/test_orion_account_mapping_household.py` (at least 8 tests; synthetic ids): `test_household_with_many_accounts_is_no_longer_refused`, `test_household_members_listed_for_a_household`, `test_single_account_household_unchanged`, `test_unknown_account_still_refused`, `test_unmapped_household_still_refused`, `test_each_account_attributed_to_itself`.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~430/IB223-2_record.json`: `{"base_commit":"<40hex>","changed_paths":[the repository paths you changed, sorted; deliverables and the channel excluded],"negative_tests":["household_with_many_accounts_is_no_longer_refused","household_members_listed_for_a_household","single_account_household_unchanged","unknown_account_still_refused","unmapped_household_still_refused","each_account_attributed_to_itself"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n from your own removal run, 1 or more>,"notes":["what each fact rests on and what was not read; where each integration is; the sparse directories you added"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `base_commit` is `git rev-parse HEAD` at your first act. `notes` has at least three lines of 30+ characters.

**The difference control (criterion 2).** The check removes every `ORION-HOUSEHOLD-A` block IN MEMORY from the product file and runs YOUR new test file: it must then FAIL on ASSERTIONS, not on an import or collection error; reference the new names only inside test functions.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB223-2_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (product files, tests, record and criteria output first; then set the instance's artifact rows to the commit and commit the instance alone in a second commit). Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB223-2-AC1" cell_refs="IB-pr-587"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r223/p223_cells.py" . IB223-2-AC1</invocation><expect>IB223-2-AC1 PASS</expect></criterion>
<criterion id="IB223-2-AC2" cell_refs="IB-pr-587"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r223/p223_cells.py" . IB223-2-AC2</invocation><expect>IB223-2-AC2 PASS</expect></criterion>
<criterion id="IB223-2-AC3" cell_refs="IB-pr-587"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r223/p223_cells.py" . IB223-2-AC3</invocation><expect>IB223-2-AC3 PASS</expect></criterion>

<expected_criteria>IB223-2-AC1, IB223-2-AC2, IB223-2-AC3</expected_criteria>

What the checks grade: AC1 the new tests (at least 8) and the existing tests named in the paths block pass; AC2 with the ORION-HOUSEHOLD-A blocks removed the new tests fail on assertions; AC3 the record: your own paths exactly as recorded and inside the grant, the named tests present, no typed object address, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. LOCAL build: you write the files named in the paths block and your records, nothing else. **Nothing is deployed, run against a served prefix, published, written to AWS, signed or sent. Every existing test stays green and no existing assertion is edited.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS or runs a producer against a served prefix; a need to edit a file outside the paths block (record which and why; the issuer amends); an existing test that fails because of your change; a typed object address in product code; a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W430-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
infra/aws/lambda/investor-reporting/performance/orion_account_mapping.py
infra/aws/lambda/investor-reporting/performance/tests/test_orion_account_mapping_household.py
infra/aws/lambda/investor-reporting/performance/tests/test_orion_account_mapping.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-587.orion-household-accounts.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~430/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 218 (round 1, workstream ~PN), cell `IB-pr-587`.
<owned_cells>IB-pr-587</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB223-2-AC1, IB223-2-AC2, IB223-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~430/IRPT_BCKEND.TO-IB-pr-587.orion-household-accounts.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order adds one edit of a lambda source file (a path under infra/ makes the class WORLD, though nothing is deployed) and tests in the repository; nothing is deployed, run against Orion or S3, or written to AWS, so no served byte moves; the apply (upload of the script, the one catalog row on the chain's dispatch object) is a later act under the signed addendum.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p223_cells.py IB223-2 dry-run at base on dell2 2026-10-15 ~16:3xZ: AC1, AC2, AC3 FAIL (no work, no record). Positive control in temp git roots the run created itself (stub files at the real relative paths, a worker commit, a synthetic record; removed): all three PASS; seven negatives, each failing its own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~430` (worktree `C:/dev/wk-IRPT_BCKEND-430`). Class WORLD.
</preflight>
